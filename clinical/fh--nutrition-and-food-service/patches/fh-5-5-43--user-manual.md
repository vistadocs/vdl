---
title: FH*5.5*43 Manager/ADPAC Guide Change Pages
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: patch
doc_subject: Change Pages
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
menu_options: 0
description: - [Document Purpose](#document-purpose) - [Scope of Patch FH\5.5\43](#scope-of-patch-fh5543) - [Updates to Nutrition and Food Service](#updates-to-nutrition-and-food-service) - [Enhancements](#enhancements) - [Patch FH\5.5\43 Functionality Changes/Enhancements](#patch-fh5543-functionality-changesenh
audience: 
keywords: 
  - tray
  - table
  - contents
  - ticket
  - flag
  - patch
  - print
  - supplemental
  - patient
  - nutrition
page_count: 0
word_count: 1114
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_ag_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_ag_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

Nutrition and Food Service

Manager/ADPAC Guide

Change Pages for Patch FH\*5.5\*43

![](fh-5-5-43-manager-adpac-guide-change-pages/001.png)

March 2019

Revision History

| Date    | Description of Change(s)                                                                                                                                                                                                                                                                          | VA Project Manager                 | Technical Writer                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 03/2019 | Added a Note to page [5](#FHPRO11_setting_Note) to clarify a required field value.                                                                                                                                                                                                                | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 01/2019 | Added Patch [FH\*5.5\*43 Functionality Changes/Enhancements](#patch-fh5.543-functionality-changesenhancements) information. Updated [Print Tray Tickets](#pt-print-tray-tickets-fhmtkp-page-120) and [Patient Supplemental Feeding List](#sl-list-supplemental-feedings-fhno5-page-267) sections. | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

# Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Document Purpose](#document-purpose)
- [Scope of Patch FH\5.5\43](#scope-of-patch-fh5543)
- [Updates to Nutrition and Food Service](#updates-to-nutrition-and-food-service)
- [Enhancements](#enhancements)
  - [Patch FH\5.5\43 Functionality Changes/Enhancements](#patch-fh5543-functionality-changesenhancements)
  - [PT Print Tray Tickets \[FHMTKP\] (Page 120)](#pt-print-tray-tickets-fhmtkp-page-120)
  - [SL List Supplemental Feedings \[FHNO5\] (Page 267)](#sl-list-supplemental-feedings-fhno5-page-267)
This document presents the new functionality provided by patch FH\*5.5\*43 and should be considered an update to the content contained in the existing *Nutrition and Food Service Manager/ADPAC Guide, Version 5.5* (2005, updated 2007). The new material presented in this document is provided in lieu of inserting revisions directly into the text of the Guide because no editable (MS Word) document can be located.

# Scope of Patch FH\*5.5\*43

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 modifies the VistA Dietetics Report Queuing software to automatically queue Nutrition and Food Service (NFS) reports and labels to run daily, or as often as necessary, without requiring Dietetics staff to manually queue them each day. This enhancement also modifies the Patient Supplemental Feeding List to display the most recent patient Diet Order, and enables staff in a Community Living Center (CLC) to enter meal instructions for morning, midday, and evening meals that are displayed as flags at the bottom of each tray ticket.

# Updates to Nutrition and Food Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements and modifications discussed herein are provided to update the existing *VistA Nutrition and Food Service Manager/ADPAC Guide* to include the functionality provided in patch FH\*5.5\*43.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch FH\*5.5\*43 Functionality Changes/Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This content adds a new section following the Introduction.

Patch FH\*5.5\*43 modifies the VistA Dietetics Report Queuing software to automatically queue NFS reports and labels to run using values defined by an NFS Manager, Clinical Application Coordinator (CAC), or Automated Data Processing Application Coordinator (ADPAC). The patch also enhances the Patient Supplemental Feeding List to display the most recent patient Diet Order, and adds new fields to the NUTRITION PERSON file (#115) that the staff in a Community Living Center (CLC) can use to enter meal instructions.

Specifically, this patch:

- Adds three new options to the existing Tray Tickets \[FHMTKM\] menu to enable automatic queuing of NFS reports and labels.

> Note: The Manager/CAC/ADPAC must be assigned the Nutrition and Food Service security key FHMGR to access these options.

- Queued Options Edit \[FHQUE OPTION EDIT\] displays a list of available reports. From this list, a report can be selected and configured to run at a specified frequency and to send the job to a specified printer. A new report option, Print Tray Tickets \[FHMTKP\], prompts the user for the meal ticket to print (Breakfast, Noon, or Evening).
- Queue Diet Reports \[FHQUE QUEUE DIET REPORTS\] passes the configured reports and labels to TaskMan to be executed and printed at the scheduled time. This option is used for testing to ensure all configured reports print as expected.
- Test an Individual Queued Option \[FHQUE TEST\] is used to immediately run a single configured report to validate selected options.

> ![](fh-5-5-43-manager-adpac-guide-change-pages/002.png)

> New VistA Options for Queuing Dietetics Reports

> Note: The new options can alternatively be accessed by typing “FHQUE” at the “Select OPTION NAME:” prompt.

> ![](fh-5-5-43-manager-adpac-guide-change-pages/003.png)

> Queuing Dietetics Reports Options Displayed from the FHQUE Option

- Adds three new files to store the values required for printing NFS reports and labels automatically.
  - FHQUE AVAILABLE OPTIONS (#117.0243) stores values such as the time the report is scheduled to run and the printer to which it will be sent.
  - FHQUE QUEUED REPORTS/LABELS (#117.024) stores a meaningful description for each of the available reports that display when Queued Options Edit is selected.
  - FHQUE REPORT DAYS (#117.0241) stores the days of the week to enable a user to select the day to run the report.
- Adds three new fields to the NUTRITION PERSON (#115) file that the staff in a CLC can use to enter meal instructions for morning, midday, and evening meals. The new free-text fields include:
  - BREAKFAST FLAG (#22)
  - NOON FLAG (#22.1)
  - EVENING FLAG (#22.2)
- Adds a new option Tray Ticket Flag Edit \[FHMTK1D TRAY TICKET EDIT\], which enables CLC staff to enter flag text in the new fields.
- Modifies the existing Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\] option to print flag text on the bottom of the tray ticket.

> ![](fh-5-5-43-manager-adpac-guide-change-pages/004.png)

Tray Ticket Flag Edit and Print Tray Tickets Options

- Enhances the Patient Supplemental Feeding List to display the most recent patient Diet Order. Diet orders can change frequently based on a patient’s medical needs; sometimes diet orders are changed in VistA after a supplemental feeding is prepared by a food service worker.

## PT Print Tray Tickets \[FHMTKP\] (Page 120)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables printing patient Tray Tickets. Refer to this section in the *VistA Nutrition and Food Service Manager/ADPAC Guide, Version 5.5*, for additional details. The functionality described here represents a modification of this option.

Patch FH\*5.5\*43 enables CLC staff to enter meal instructions for morning, midday, and evening meals that are displayed as flags on the bottom of the tray ticket.

- The option Tray Ticket Flag Edit \[FHMTK1D TRAY TICKET EDIT\] enables CLC staff to enter meal instructions that are easily seen by staff at mealtime.
- The existing Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\] option is modified to print flag text on the bottom of the tray ticket where it can be easily seen by clinical staff at mealtime.

![](fh-5-5-43-manager-adpac-guide-change-pages/005.png)

Tray Ticket Flag Edit and Print Tray Tickets Options

Three new free text fields in the NUTRITION PERSON (#115) file are used to store the flag text that the staff in a CLC use to enter meal instructions. The new free-text fields include:

- BREAKFAST FLAG (#22)
- NOON FLAG (#22.1)
- EVENING FLAG (#22.2)

> Note: Flags are limited to 18 characters

![](fh-5-5-43-manager-adpac-guide-change-pages/006.png)

Tray Ticket Displaying a Tray Ticket Flag

## SL List Supplemental Feedings \[FHNO5\] (Page 267)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing Patient Supplemental Feeding List is enhanced to display the most recent patient Diet Order. Diet orders can change frequently based on a patient’s medical needs; sometimes diet orders are changed in VistA after a supplemental feeding is prepared by a food service worker.

The enhanced Patient Supplemental Feeding List is accessible from the “Run SF Labels/Consolid Ingred List” \[FHNO2\] option on the SUPPLEMENTAL FEEDINGS \[FHNOM\] menu.

<span id="FHPRO11_setting_Note" class="anchor"></span>Note: The Diet Order will display on the Patient Supplemental Feeding List only if the SEPARATE SUPP FDG LABELS? field (#20) in the SUPPLEMENTAL FEEDING SITE file (#119.74) is set to NO, or if the site does not have a Supplemental Feeding Site configured.

> An ADPAC who is assigned the FHMGR key can change the value of the SEPARATE SUPP FDG LABELS? field for a site by accessing the “Enter/Edit Supplemental Fdg. Sites” \[FHPRO11\] option in VistA and then responding “NO” at the SEPARATE SUPP FDG LABELS?: NO// prompt.

> Dietetics Management \[FHMGR\]

> Dietetics Facilities \[FHPRG\]

> Enter/Edit Supplemental Fdg. Sites \[FHPRO11\]

> ![](fh-5-5-43-manager-adpac-guide-change-pages/007.png)

> Refer to the *NE Enter/Edit Supplemental Fdg. Sites \[FHPRO11\]* section in the *Nutrition and Food Service Manager/ADPAC Guide* for more information on the FHPRO11 option.