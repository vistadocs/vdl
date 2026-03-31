---
title: "Kernel 8.0 Developerâ€™s Guide: File Access Security User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: File Access Security"
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
  - access
  - span
  - guide
  - developer
  - kernel
  - security
  - table
  - class
  - contents
  - dlaygo
page_count: 0
word_count: 1437
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_file_access_security_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_file_access_security_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259322" class="anchor"></span>File Access Security Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: File Access Security Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

[Figure 1: File Access Security—Setting DLAYGO in a Template [3](#_Ref499704376)](#_Ref499704376)

<span id="_Ref38421374" class="anchor"></span>

Orientation

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Developer Tools](#developer-tools)
  - [Field Level Protection](#field-level-protection)
  - [File Navigation](#file-navigation)
  - [Use of DLAYGO When Navigating to Files](#use-of-dlaygo-when-navigating-to-files)
  - [Use of DLAYGO in ^DIC Calls](#use-of-dlaygo-in-dic-calls)
  - [Use of DIDEL in ^DIE Calls](#use-of-didel-in-die-calls)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: File Access Security Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Access Security system is an optional Kernel module. It provides an enhanced security mechanism for controlling user access to VA FileMan files.

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/004.png) REF: For an overview of the functionality provided by the File Access Security system, see the “File Access Security” section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf).

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several File Access Security developer tools are available for developers. These developer tools are described below.

## Field Level Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DUZ(0) check is *not* performed when a user traverses fields in a DR string or in a template; field-level protection is checked during the template-building process, but *not* subsequently when the template is invoked by a user. If you want to make the presentation of fields conditional, based on a user’s DUZ(0), branching logic may be used as described in the *VA FileMan Developer’s Guide*.

## File Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit-type options that navigate to a second file do so by calling VA FileMan and, hence, depending on the type of navigation and the existing file protection, requires that the user have:

- WRITE access to change data in the pointed-to file.
- DELETE access to delete an entry.
- (Perhaps) LAYGO access to add a new entry.

Adding new entries when navigating to a file is controlled by LAYGO access. If a pointing field allows Learn As You Go (LAYGO), as specified in the data dictionary, and the pointed-to file also allows LAYGO, the user does *not* need explicit file access to add entries. If the pointed-to file is protected, however, the user needs explicit LAYGO access to the file. DELETE access is checked when the user tries to delete a file entry.

When coding calls, if DIC(0) contains L, DIC allows the user to add a new entry if one of three conditions is met:

- The user has been granted LAYGO access to the file.
- The user’s DUZ(0) is equal to @.
- The DLAYGO variable is defined equal to the file number.

## Use of DLAYGO When Navigating to Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of input templates or VA FileMan ^DIE calls as part of edit-type options permits user access to the first file. However, if navigation to a second file is involved, LAYGO access is *not* automatically granted. One of the three conditions mentioned above *must* be met to allow navigation to the second file:

- LAYGO access is granted.
- DUZ(0)=@.
- DLAYGO variable is set.

Providing LAYGO access by using the DLAYGO variable obviates the need for system administrators to grant LAYGO file access to the pointed-to file through the File Access system. An example of setting DLAYGO in a template is shown in <u>Figure 1</u>.

<span id="_Ref499704376" class="anchor"></span>Figure 1: File Access Security—Setting DLAYGO in a Template

INPUT TO WHAT FILE: <span class="mark">RENTAL</span>

EDIT WHICH FIELD: <span class="mark">TRANSACTION NUMBER</span>

THEN EDIT FIELD: <span class="mark">DATE RENTED</span>

THEN EDIT FIELD: <span class="mark">S DLAYGO=800265</span>

THEN EDIT FIELD: <span class="mark">LINE ITEM:</span>

By 'LINE ITEM', do you mean the LINE ITEM File,

pointing via its 'RENTAL TRANSACTION' Field? YES// <span class="mark">Y \<Enter\></span> (YES)

WILL TERMINAL USER BE ALLOWED TO SELECT PROPER ENTRY IN 'LINE ITEM' FILE? YES// <span class="mark">\<Enter\></span> (YES)

DO YOU WANT TO PERMIT ADDING A NEW 'LINE ITEM' ENTRY? NO// <span class="mark">Y \<Enter\></span> (YES)

WELL THEN, DO YOU WANT TO \*\*FORCE\*\* ADDING A NEW ENTRY EVERY TIME? NO// <span class="mark">\<Enter\></span> (NO)

DO YOU WANT AN 'ADDING A NEW LINE ITEM' MESSAGE? NO// <span class="mark">N \<Enter\></span> (NO)

EDIT WHICH LINE ITEM FIELD: <span class="mark">LINE ITEM</span>

THEN EDIT LINE ITEM FIELD: <span class="mark">RENTAL TRANSACTION</span>

THEN EDIT LINE ITEM FIELD: <span class="mark">K DLAYGO</span>

THEN EDIT LINE ITEM FIELD:

## Use of DLAYGO in ^DIC Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user attempts to add an entry at the top level of a file in a VA FileMan ^DIC call, their file access security is checked for LAYGO access to the file. Developers can override this check (and save the site from having to grant explicit LAYGO access) by setting DLAYGO to the file number in question.

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/005.png) REF: For more information on DLAYGO as used in ^DIC calls, see the *VA FileMan Developer’s Guide*.

## Use of DIDEL in ^DIE Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user attempts to delete an entry at the top level of a file in a VA FileMan ^DIE call, their file access security is checked for DELETE access to the file. Developers can override this check (and save the site from having to grant explicit DELETE access) by setting DIDEL to the file number in question. Use of DIDEL does *not* override a file’s “DEL” nodes, however.

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/006.png) REF: For more information on DIDEL as used in ^DIE calls, see the *VA FileMan Developer’s Guide*.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/007.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/008.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-file-access-security-user-guide/009.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.