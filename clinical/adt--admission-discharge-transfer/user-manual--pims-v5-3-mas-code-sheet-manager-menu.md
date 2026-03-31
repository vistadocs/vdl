---
title: PIMS Version 5.3 User Manual - MAS Code Sheet Manager Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: MAS Code Sheet Manager Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - sheet
  - amis
  - segment
  - segments
  - generate
  - print
  - table
  - contents
  - year
page_count: 0
word_count: 550
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_mcsm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_mcsm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

## Table of Contents

  - [Overview](#overview)
    - [MAS Code Sheet User Menu](#mas-code-sheet-user-menu)
PIMS V. 5.3 ADT Module User ManualMAS Code Sheet Manager Menu
![](pims-version-5-3-user-manual-mas-code-sheet-manager-menu/001.png)
July 1998
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
MAS Code Sheet User Menu
> Generate a Code Sheet
> Create a Code Sheet
> Keypunch a Code Sheet
> Code Sheet Edit
> Review a Code Sheet
> Delete a Code Sheet
> Print a Code Sheet
MAS Code Sheet Batch Menu
> Code Sheets Ready for Batching
> Batch Code Sheets
> Batch Edit
> Mark Code Sheets for Rebatching
MAS Code Sheet Transmission Menu
> Batches Waiting to be Transmitted
> Transmit Code Sheets
> Mark Batch for Retransmission
> Status of all Batches
Purge Transmission Records/Code Sheets
PLEASE NOTEOther than the Generate a Code Sheet and Print a Code Sheet options, documentation for the MAS Code Sheet Manager Menu is not provided in the PIMS manual. For assistance, refer to the Generic Code Sheet User Manual.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MAS Code Sheet User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Generate a Code Sheet

This option is used to generate AMIS segments 223 (prior to FY 95), 334-341, 345-346, and 401-420.

PRINT A CODE SHEET

This option allows the printing of AMIS segments 167, 223, 290, 334-341, 345-346, and 401-420.

#### Generate a Code Sheet

The Generate a Code Sheet option is used to generate AMIS segments 334-341, 345-346, and 401-420. AMIS (Automated Management Information System) is a general system of computer programs used to process management reports. For AMIS code sheets generated after installation of the MAS v5.2 software, the AMIS 419 code sheet will not be created.

When a range of AMIS segments is chosen, the entire range will be generated. You cannot generate individual segments within the range. If the AMIS segments for the month/year you choose are not in balance, the following message will be displayed and you will not be allowed to proceed: "AMIS {selected segment \#s} code sheets can not be generated for this month/year until the following segments are balanced: {out of balance segment \#s}".

Once the AMIS segment(s) and month/year are selected, the system will automatically stuff the appropriate data into the fields and mark the code sheet(s) for batching. A display of how the transmitted code sheet will look is provided.

An ID# will automatically be assigned by the system in the syntax: code sheet number-fiscal year.

If you are at a multidivisional facility and select other than a 300 segment, you will be prompted for the division. If a 300 segment is selected, the system assumes all divisions.

#### Print a Code Sheet

The Print a Code Sheet option allows printing of the 167, 290, 334-341, 345-346, and the 401-420 AMIS segments. AMIS (Automated Management Information System) is a general system of computer programs used to process management reports.

Following is a brief description of the type of activity reported by each segment.

167 mental health clinic

290 compensation and pension examinations

334-341 admission/discharge/transfer for each inpatient service

345-346 VA nursing home and domiciliary units

401-420 applications for care (registrations) by veteran category and

dispositioning group

You will be prompted for the ID# of the MAS code sheet you wish to print. You may enter double question marks (??) for a list. This list provides the following information, if applicable: ID#, AMIS segment \#, date the code sheet was created, and the AMIS month/year for each code sheet.

The selected segment will print in the transmission format followed by a list of each field for that segment. However, if the selected code sheet was "keypunched" (entered through the Keypunch a Code Sheet option), it will be shown in the keypunched format only.