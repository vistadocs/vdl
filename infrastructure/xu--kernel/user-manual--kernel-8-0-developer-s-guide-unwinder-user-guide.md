---
title: "Kernel 8.0 Developerâ€™s Guide: Unwinder User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Unwinder"
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
  - guide
  - table
  - xqorm
  - contents
  - kernel
  - xqor
  - unwinder
  - developer
  - protocol
  - protocols
page_count: 0
word_count: 1249
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
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_unwinder_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_unwinder_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259721" class="anchor"></span>Unwinder Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-unwinder-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-unwinder-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Unwinder Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-unwinder-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [EN^XQOR(): Navigating Protocols](#enxqor-navigating-protocols)
  - [EN1^XQOR(): Navigating Protocols](#en1xqor-navigating-protocols)
  - [MSG^XQOR(): Enable HL7 Messaging](#msgxqor-enable-hl7-messaging)
  - [EN^XQORM(): Menu Item Display and Selection](#enxqorm-menu-item-display-and-selection)
  - [XREF^XQORM(): Force Menu Recompile](#xrefxqorm-force-menu-recompile)
  - [DISP^XQORM1(): Display Menu Selections From Help Code](#dispxqorm1-display-menu-selections-from-help-code)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Unwinder Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Kernel Unwinder APIs are available for developers. These APIs are described below.

## EN^XQOR(): Navigating Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10101

Description: The EN^XQOR API is the main routine for navigating protocols. The routine processes the initial protocol and the subordinate protocols. This processing of subordinate protocols happens according to the type of protocol and the navigation variables that get set along the way.

Format: EN^XQOR(x)

Input Parameters: x: (required) Identifies the initial protocol that EN^XQOR should process. The x input parameter should be in VARIABLE POINTER format. For example:

x="1234;ORD(101,"

This would cause the processing to start with the protocol that has an internal entry number (IEN) of 1234.

An alternative to using VARIABLE POINTER format is to set x equal to the name or number of the protocol and DIC equal to the number or global reference of the file you are working in (generally the PROTOCOL \[#101\] file).

Output: none.

## EN1^XQOR(): Navigating Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10101

Description: The EN1^XQOR API is identical to the <u>EN^XQOR(): Navigating Protocols</u> API, except that the ENTRY and EXIT actions of the initial protocol are *not* executed. This API provides backwards compatibility with the way Kernel 6 processed protocols that were defined in the OPTION (#19) file.

Format: EN1^XQOR(x)

Input Parameters: x: (required) Identifies the initial protocol that EN^XQOR should process. The x input parameter should be in VARIABLE POINTER format. For example:

x="1234;ORD(101,"

This would cause the processing to start with the protocol that has an internal entry number (IEN) of 1234.

An alternative to using VARIABLE POINTER format is to set x equal to the name or number of the protocol and DIC equal to the number or global reference of the file you are working in (generally the PROTOCOL \[#101\] file).

Output: none.

## MSG^XQOR(): Enable HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10101

Description: The MSG^XQOR API enables Health Level Seven (HL7) messaging through the XQOR Unwinder.

Format: MSG^XQOR(protocol,.msgtext)

Input Parameters: protocol: (required) The name of the protocol with which the HL7 message are associated.

.msgtext: (required) The array containing the HL7 message.

Output: none.

## EN^XQORM(): Menu Item Display and Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10140

Description: The EN^XQORM API handles the display of and selection from a menu; this routine processes a single menu only. This is the call that the <u>EN^XQOR(): Navigating Protocols</u> API uses to obtain menu selections. The caller is responsible to handle any selections from the menu that are returned in the y array. If you want navigation to the selected items handled for you, use the <u>EN^XQOR(): Navigating Protocols</u> API. The menus handled by this routine are the multiple selection, multiple column menus that are typical in Order Entry/Results Reporting (OE/RR).

Format: EN^XQORM(xqorm,xqorm(0))

Input Parameters: xqorm: (required) A VARIABLE POINTER to the menu that should be displayed (such as XQORM=“1234;ORD(101,”).

xqorm(0): (required) A string of flags that control the display and prompting of the menu:

- NUMERIC—Maximum number of selections allowed.
- A—Prompt for a selection from the menu.
- D—Display the menu.

Output Parameters: y(): This array contains the items that the user selected from the menu.

## XREF^XQORM(): Force Menu Recompile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10140

Description: The XREF^XQORM API forces a menu to recompile. Menus are compiled into the XUTL global. This should happen automatically. However, you can use this API to force a menu to recompile.

Format: XREF^XQORM(xqorm)

Input Parameters: xqorm: (required) A VARIABLE POINTER to the protocol that should be recompiled.

Output: returns: Returns recompiled menu.

## DISP^XQORM1(): Display Menu Selections From Help Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Unwinder

ICR \#: 10102

Description: The DISP^XQORM1 API displays menu selections from help code, if you have replaced the standard help by setting XQORM(“??”). This API should only be called from within the code used by XQORM(“??”).

Format: DISP^XQORM1(x)

Input Parameters: x: (required) *Must* be a question mark (?).

Output: returns: Returns menu selections.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-unwinder-user-guide/004.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-unwinder-user-guide/005.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-unwinder-user-guide/006.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.