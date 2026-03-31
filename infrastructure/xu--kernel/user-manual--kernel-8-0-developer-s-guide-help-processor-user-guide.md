---
title: "Kernel 8.0 Developerâ€™s Guide: Help Processor User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Help Processor"
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
  - help
  - frame
  - guide
  - table
  - contents
  - kernel
  - developer
  - frames
  - processor
  - history
page_count: 0
word_count: 1034
section_count: 5
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259329" class="anchor"></span>Help Processor Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-help-processor-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-help-processor-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Help Processor Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-help-processor-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Entry and Exit Execute Statements](#entry-and-exit-execute-statements)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [EN^XQH: Display Help Frames](#enxqh-display-help-frames)
  - [EN1^XQH: Display Help Frames](#en1xqh-display-help-frames)
  - [ACTION^XQH4(): Print Help Frame Tree](#actionxqh4-print-help-frame-tree)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Help Processor Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Entry and Exit Execute Statements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HELP FRAME (#9.2) file contains two fields for the entry of M code:

- Entry Execute Statement—Code in the Entry Execute Statement is executed just before the help frame is displayed.
- Exit Execute Statement—Code in the Exit Execute Statement is executed afterwards.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Help Processor APIs are available for developers. These APIs are described below.

## EN^XQH: Display Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Help Processor

ICR \#: 10074

Description: The EN^XQH API displays a help frame. It immediately clears the screen and displays the help frame (unlike the <u>EN1^XQH: Display Help Frames</u> API, which does *not* clear the screen and offers the user a choice of whether to load the help frame).

Format: EN^XQH

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: XQH: (required) Help Frame name (the .01 value from the HELP FRAME \[#9.2\] file).

Output: none.

## EN1^XQH: Display Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Help Processor

ICR \#: 10074

Description: The EN1^XQH API displays a help frame as <u>ACTION^XQH4(): Print Help Frame Tree</u> does, except that it does *not* clear the screen beforehand, and prior to loading the help frame, EN1^XQH invokes end of page handling (that is prompting the user “Enter return to continue or ‘^’ to quit”). If the user enters an ^, the help frame is *not* displayed. If they press \<Enter\>, the help frame is displayed.

Format: EN1^XQH

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Variable: XQH: (required) Help Frame name (the .01 value from the HELP FRAME \[#9.2\] file).

Output: none.

## ACTION^XQH4(): Print Help Frame Tree

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Help Processor

ICR \#: 10080

Description: The ACTION^XQH4 API prints out all the help frames in a help frame tree, including a table of contents showing the relationships between help frames and the page of the printout where each help frame is found. Since help frames can be referenced by more than one help frame, any help frame referenced multiple times appears in the table of contents in each appropriate location, but the help text itself is printed only once. You can alter the format of the output with the xqfmt input parameter.

Format: ACTION^XQH4(xqhfy\[,xqfmt\])

Input Parameters: xqhfy: (required) Help frame name, equal to the .01 field of the desired entry in the HELP FRAME (#9.2) file. It should be set to the NAME of the top-level help frame for which a listing is desired.

xqfmt: (optional) Specifies the output format. Value of xqfmt can be:

- T—Text of help frames only (default).
- R—Text of help frames, plus a table of related frames and keywords (if any) for each help frame.
- C—Complete listing (text of help frames, table of related frames for each help frame, and internal help frame names).

Output: none.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-help-processor-user-guide/004.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-help-processor-user-guide/005.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-help-processor-user-guide/006.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.