---
title: FH*5.5*43 Technical Manual and Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: and Security Guide Change Pages
app_code: FH
app_name: Nutrition and Food Service
section: CLI
app_status: active
pkg_ns: FH
patch_ver: 5.5
patch_id: FH*5.5*43
group_key: "FH:FH:5.5"
file_numbers: []
security_keys: []
menu_options: 1
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 46%\\" /> <col style=\\"width: 19%\\" /> <col style=\\"width: 16%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Description of Change(s)</th> <th>VA Project Manager</th> <th>Technical Writer</th> </tr> </thead> <tbody> <tr clas"
audience: 
keywords: 
  - table
  - contents
  - files
  - strong
  - tray
  - style
  - width
  - class
  - patch
  - food
page_count: 0
word_count: 922
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

Nutrition and Food Service

Outpatient Meals

Technical Manual and Security Guide

Change Pages for Patch FH\*5.5\*43

![](fh-5-5-43-technical-manual-and-security-guide-change-pages/001.png)

January 2019

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 46%" />
<col style="width: 19%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description of Change(s)</th>
<th>VA Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2019</td>
<td><p>Added Patch FH*5.5*43 enhancements to modify the following sections:</p>
<p><a href="#files-page-15">Files</a></p>
<p><a href="#modified-files-page-19">Modified Files</a></p>
<p><a href="#modified-files-page-19">Exported Options</a></p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Document Purpose](#document-purpose)
- [Scope of Patch FH\5.5\43](#scope-of-patch-fh5543)
- [Updates to Nutrition and Food Service](#updates-to-nutrition-and-food-service)
- [Enhancements](#enhancements)
  - [Files (Page 15)](#files-page-15)
    - [New Files (New subsection)](#new-files-new-subsection)
  - [Modified Files (Page 19)](#modified-files-page-19)
  - [Exported Options (Page 29)](#exported-options-page-29)
This document presents the new functionality provided by patch FH\*5.5\*43 and should be considered an update to the content contained in the existing *VistANutrition and Food Service Outpatient Meals Technical Manual and Security Guide, Version 5.5* (2005). The new material presented in this document is provided in lieu of inserting revisions directly into the text of the Guide because no editable (MS Word) document can be located.

# Scope of Patch FH\*5.5\*43

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 modifies the VistA Dietetics Report Queuing software to automatically queue Nutrition and Food Service (NFS) reports and labels to run daily, or as often as necessary, without requiring Dietetics staff to manually queue them each day. This enhancement also modifies the Patient Supplemental Feeding List to display the most recent patient Diet Order, and enables staff in a Community Living Center (CLC) to enter meal instructions for morning, midday, and evening meals that are displayed as flags at the bottom of each tray ticket.

# Updates to Nutrition and Food Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements and modifications discussed herein are provided to update the existing *VistANutrition and Food Service Outpatient Meals Technical Manual and Security Guide, Version 5.5* to include the functionality provided in patch FH\*5.5\*43.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files (Page 15)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Files (New subsection)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch FH\*5.5\*43 adds three new files to store the values required for printing NFS reports and labels automatically.

| File Number | File Name               | Global   | Description                                                                                                                                                                                                               |
|-----------------|-----------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 117.0243        | FHQUE AVAILABLE OPTIONS     | ^FH(117.0243 | Stores values such as the time the report is scheduled to run and the printer to which it will be sent. For the new option Print Tray Tickets \[FHMTKP\], stores the meal ticket to be printed (Breakfast, Noon, or Evening). |
| 117.024         | FHQUE QUEUED REPORTS/LABELS | ^FH(117.024  | Stores the configured reports with the day, time selected, printer, active or inactive, and (if appropriate) the meal. This file contains the information that will be used by TaskMan.                                       |
| 117.0241        | FHQUE REPORT DAYS           | ^FH(117.0241 | Stores the days of the week to enable a user to select the day to run the report.                                                                                                                                             |

## Modified Files (Page 19)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Number</strong></th>
<th><strong>File Name</strong></th>
<th><strong>Global</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr class="odd">
<th>115</th>
<th>NUTRITION PERSON</th>
<th>^FHPT(</th>
<th><p>Three new free-text fields are added to this file so that the staff in a CLC can enter meal instructions for morning, midday, and evening meals.</p>
<p>The new fields are: BREAKFAST FLAG field (#22), NOON FLAG field (#22.1), and EVENING FLAG field (#22.2).</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Exported Options (Page 29)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 adds six new options to the NFS package.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 29%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Internal Entry Name</strong></th>
<th><strong>Option Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FHQUE OPTION EDIT</td>
<td>Queued Options Edit</td>
<td><p>Displays a list of available reports to select and configure. Prompts the user for the time to run the option, the desired printer and whether it is active, and the days of the week to run the report. The Print Tray Tickets [FHMTKP] option also prompts for the meal ticket to print (B, N, E).</p>
<p>Security Key FHMGR is required to access this option.</p></td>
</tr>
<tr class="even">
<td>FHQUE QUEUE DIET REPORTS</td>
<td>Queue Diet Reports</td>
<td><p>Passes the configured reports and labels to TaskMan to be executed and printed at the scheduled time.</p>
<p>Security Key FHMGR is required to access this option.</p></td>
</tr>
<tr class="odd">
<td>FHQUE TEST</td>
<td>Test an Individual Queued Option</td>
<td><p>Used to immediately run a test report to validate selections made using Queued Options Edit and is used only for testing.</p>
<p>Security Key FHMGR is required to access this option.</p></td>
</tr>
<tr class="even">
<td>FHMTKM Tray Tickets</td>
<td>Tray Tickets</td>
<td><p>Adds the Tray Ticket Flag Edit option.</p>
<p>Modifies the existing Print Tray Tickets option to display flags on patient Tray Tickets.</p></td>
</tr>
<tr class="odd">
<td>FHMTK1D TRAY TICKET EDIT</td>
<td>Tray Ticket Flag Edit</td>
<td><p>Enables CLC staff to enter flags in free text (18-character limit) for one or more meals (Breakfast, Noon, and Evening).</p>
<p>Only for use in CLC facilities.</p></td>
</tr>
<tr class="even">
<td>FHMTK1P TRAY TICKET PRINT</td>
<td>Print Tray Tickets</td>
<td>Prints flag text on the bottom of the tray ticket where it is easily seen by clinical staff.</td>
</tr>
</tbody>
</table>