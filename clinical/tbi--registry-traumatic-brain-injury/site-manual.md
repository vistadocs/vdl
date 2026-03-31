---
title: TBI Version 4.2 System Management Guide
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: System Management Guide
app_code: TBI
app_name: "Registry: Traumatic Brain Injury"
section: CLI
app_status: active
pkg_ns: TBI
patch_ver: 4.2
patch_id: TBI*4.2
group_key: "TBI:TBI:4.2"
file_numbers: []
security_keys: []
menu_options: 0
description: The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the Global War on Terror (GWOT) report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic B
audience: 
keywords: 
  - table
  - class
  - contents
  - registry
  - strong
  - injury
  - traumatic
  - brain
  - span
  - names
page_count: 0
word_count: 890
section_count: 5
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbitm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbitm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Traumatic Brain Injury (TBI) Registry

  System Management Guide
---

![](tbi-version-4-2-system-management-guide/001.png)

Increment 1.0

July 2015

Office of Information and Technology (OIT)

Product Development

Revision History

|         |                                                                  |                                    |                                    |             |            |
|---------|------------------------------------------------------------------|------------------------------------|------------------------------------|-------------|------------|
| Version | Description                                                      | Author                             | Reviewer(s)                        | Review Type | Issue Date |
| 4.2     | Reviewed for TBI Enhancements Increment 1. No updates necessary. | <span class="mark">REDACTED</span> |                                    |             | 7/7/15     |
| 4.1     | Updated for Increment 5 release and refined formatting.          | <span class="mark">REDACTED</span> |                                    | Technical   | 5/6/14     |
| 4.0     | Final Version                                                    | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | Peer        | 5/1/12     |
| 1.0     | Final Version                                                    | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | Peer        | 9/09/11    |

<span id="_Toc303325181" class="anchor"></span>Table 1 - Typographical Conventions

Table of Contents

List of Tables

[Table 1 - Typographical Conventions [2](#_Toc303325181)](#_Toc303325181)

[Table 2 - Graphical Conventions [2](#_Toc303325182)](#_Toc303325182)

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [The Traumatic Brain Injury Registry Application](#the-traumatic-brain-injury-registry-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
- [Background](#background)
- [Technical Overview](#technical-overview)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other conventions are used:

<table>
<caption><p><span id="_Toc303325182" class="anchor"></span>Table 2 - Graphical Conventions</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 33%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Font</strong></th>
<th><strong>Used for…</strong></th>
<th><strong>Examples:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blue text, underlined</td>
<td>Hyperlink to another document or URL</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Green text, dotted underlining</td>
<td>Hyperlink within this document</td>
<td>See Release History for details.</td>
</tr>
<tr class="odd">
<td>Courier New</td>
<td>Patch names, VistA filenames</td>
<td>Patch names will be in this font</td>
</tr>
<tr class="even">
<td>Franklin Gothic Demi</td>
<td><p>Keyboard keys</p>
<p>Web application panel, pane, tab, and button names</p></td>
<td><p>&lt; F1 &gt;, &lt; Alt &gt;, &lt; L &gt;</p>
<p>Other Registries panel</p>
<p>[Delete] button</p></td>
</tr>
<tr class="odd">
<td>Microsoft Sans Serif</td>
<td>Software Application names</td>
<td>Traumatic Brain Injury (TBI)</td>
</tr>
<tr class="even">
<td rowspan="4">Microsoft Sans Serif bold</td>
<td>Registry names</td>
<td><strong>TBI</strong></td>
</tr>
<tr class="odd">
<td>Database field names</td>
<td><strong>Mode field</strong></td>
</tr>
<tr class="even">
<td>Report names</td>
<td><strong>National Summary Report</strong></td>
</tr>
<tr class="odd">
<td>Organization and Agency Names</td>
<td><strong>DoD, VA</strong></td>
</tr>
<tr class="even">
<td>Microsoft Sans Serif, 50% gray and italics</td>
<td>Read-only fields</td>
<td><em>Procedures</em></td>
</tr>
<tr class="odd">
<td>Times New Roman</td>
<td>Normal text</td>
<td>Information of particular interest</td>
</tr>
<tr class="even">
<td rowspan="3">Times New Roman Italic</td>
<td>Text emphasis</td>
<td>“It is <em>very</em> important . . .”</td>
</tr>
<tr class="odd">
<td>National and International Standard names</td>
<td><em>International Statistical Classification of Diseases and Related Health Problems</em></td>
</tr>
<tr class="even">
<td>Document names</td>
<td><em>Traumatic Brain Injury (TBI) Registry User Manual</em></td>
</tr>
</tbody>
</table>

<span id="_Toc303325182" class="anchor"></span>Table 2 - Graphical Conventions

| Graphic                                                                                          | Used for…                                                                          |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-system-management-guide/002.png) | Information of particular interest regarding the current subject matter.               |
| ![](tbi-version-4-2-system-management-guide/003.png) | A tip or additional information that may be helpful to the user.                       |
| ![](tbi-version-4-2-system-management-guide/004.png) | A warning concerning the current subject matter.                                       |
| ![](tbi-version-4-2-system-management-guide/005.png) | Information about the history of a function or operation; provided for reference only. |
| ![](tbi-version-4-2-system-management-guide/006.png)  | Indicates an action or process which is optional                                       |
| ![](tbi-version-4-2-system-management-guide/007.png)  | Indicates a resource available either in this document or elsewhere                    |

## The Traumatic Brain Injury Registry Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Traumatic Brain Injury Registry application (TBI Registry) supports the maintenance of local and national registries for clinical and resource tracking of care for such Veterans. The TBI Registry software application allows case managers to identify Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI Registry permits the case manager to oversee and track the comprehensive evaluation of these patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This System Management Guide provides the technical details for the TBI Registry, which has been developed for the Department of Veterans Affairs (VA) in support of Veterans who are potential TBI patients.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry software is designed for use by designated case managers who are responsible for screening and overseeing the records of patients both seen and not seen for the comprehensive TBI evaluation.

# Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the *Global War on Terror (GWOT)* report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic Brain Injury’ Surveillance Center and Registry to monitor returning service members who have possibly sustained head injury and thus may potentially have a traumatic brain injury in order to provide early medical intervention.”

The Traumatic Brain Injury (TBI) Registry software application collects data on the population of Veterans who participated in Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF). These individuals need to be seen within 30 days for a comprehensive TBI evaluation. Each facility can produce local reports (information related to patients evaluated and treated in their system).

# Technical Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBI is a component of the Converged Registries Solution (CRS).  Refer to CRS technical documentation in TSPR <span class="mark">REDACTED</span>