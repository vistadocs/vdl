---
title: "Kernel 8.0 Developerâ€™s Guide: XTMP Global User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: XTMP Global"
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
  - xtmp
  - global
  - guide
  - kernel
  - developer
  - table
  - contents
  - history
  - date
  - revision
page_count: 0
word_count: 1207
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xtmp_global_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xtmp_global_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259910" class="anchor"></span>^XTMP Global Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: ^XTMP Global Developer Tools User Guide</em>.</p>
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

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Rules for Use of the ^XTMP Global](#rules-for-use-of-the-xtmp-global)
  - [SAC Exemptions](#sac-exemptions)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: ^XTMP Global Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a recurring need by VistA software to store data in a translated global for relatively short periods of time. However, this data needs to be accumulated for a period longer than an individual user's logon session and longer than the time a specific process/job might run. The ^UTILITY, ^TMP, and ^XUTL globals do *not* meet the basic requirements for storing this type of data due to the following:

- These globals are *not* translated, and thus, *cannot* be relied upon for transferring data from one job to another.
- The data is *not* stored for excessively long periods of time and is constantly being processed and purged.
- The data is stored in an intermediate form, temporarily, so that it can be further processed in an efficient manner.
- The original data is stored in a VA FileMan file from which the temporary data can be recreated, or on another system (usually *non*-VistA) from which it can be resent, if necessary. Hence, the creation of a VA FileMan file, while feasible, would add unnecessary overhead to the VistA systems.

Therefore, the Standards and Conventions Committee (SACC) asked Kernel to establish the ^XTMP global, which can be used by *any* VistA software application. This global is dynamic in size and activity, with one copy accessible to *all* members of a UCI and should be placed accordingly.

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/004.png) CAUTION: The ^XTMP global should *not* be used for long-term storage of data; data requiring long-term storage should be placed within a file. The ^XTMP global should only be used for near-term storage needs and should respect size constraints.

## Rules for Use of the ^XTMP Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The structure of each top node of the ^XTMP global has the following format:

^XTMP(namespaced- subscript,0)=purge date^createdate^optional descriptive information

(Both dates *must* be in VA FileMan internal date format.)

As per the Standards and Conventions (SAC, Section 2.11.8), developers are encouraged to include other descriptive information on the third piece of the 0 node of the ^XTMP global (such as task description and creator DUZ).

1.  First Subscript Must be Namespaced—The first subscript of the ^XTMP global *must* be namespaced; however, other characters can follow the namespace. For example, if the namespace for the software is "RA," the first subscript could be "RA"\_DUZ, "RA"\_literal, "RA"\_\$J, and so on. This allows the developer to use the global in different parts of the software.
2.  0 Node Must Exist—There must be a 0 node for the global in which the first piece contains the PURGE DATE in VA FileMan internal date format, and the second piece contains the CREATE DATE in VA FileMan internal date format. For example:

^XTMP("RA1",0)=2920416^2920401

3.  KILL ^XTMP After Use—The developer is responsible for KILLing ^XTMP(*x*) when its use is complete (where "*x*" is their namespaced subscript).
4.  Code Cleanup—Kernel has included the necessary code in the XQ82 routine to clean up the ^XTMP global (such as ^XTMP("RA1"). It KILLs this global under any of the following conditions:
- There is no 0 node (such as ^XTMP("RA1",0).
- The 0 node does *not* contain a purge date as the first piece.
- The date in the first piece of the 0 node is the same as or before the system date.

## SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of May 17, 2002, the Standards and Conventions (SAC) document has the following exemptions regarding the ^XTMP global:

- Section 2.3.2.1—Subscripts used in the ^TMP and ^XTMP globals can be lowercase.
- Section 2.3.2.5—The ^TMP, ^UTILITY, and ^XTMP globals do *not* have to be VA FileMan compatible.
- Section 2.3.2.5.2—The ^XTMP global will be translated, with one copy for the entire VistA production system at each site.
- Section 2.7.3.3—All documented temporary scratch global nodes (such as ^TMP and ^UTILITY) are created by a called supported reference, except for ^XTMP global data.
- Section 2.7.3.4—All local variables, locks, and scratch global nodes (except ^XTMP, or other scratch globals designed to be passed between parts of a package) are created by the application.

A new extension *must* be added to the SAC stating that this global should be used as a scratch area when a translated scratch global is required by software applications.

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/005.png) REF: To view the entire SAC document, see the [SACC VA Intranet website](https://dvagov.sharepoint.com/sites/OITEPMODevelopment/sac/default.aspx).

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/006.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/007.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-xtmp-global-user-guide/008.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.