---
title: MRSA Program Tools Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: MMRS
app_name: Methicillin Resistant Staph Aurerus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1
group_key: "MMRS:MMRS:1"
file_numbers: 
  - 42
  - 60
  - 61
  - 62
  - 63
security_keys: []
menu_options: 0
description: [![](mrsa-program-tools-version-1-technical-manual/001.png)](#table-of-contents)
audience: 
keywords: 
  - class
  - mrsa
  - span
  - colspan
  - glos
  - table
  - anchor
  - href
  - tools
  - even
page_count: 0
word_count: 6381
section_count: 12
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

[![](mrsa-program-tools-version-1-technical-manual/001.png)](#table-of-contents)

MRSA PROGRAM TOOLSVersion 1.0

Patch MMRS\*1.0\*1

Technical Manual  
and  
Security Guide

January 2010 (Revised July 2010)

Office of Enterprise Development (OED)

Field Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# List of Tables](#list-of-tables)
  - [Text Conventions](#text-conventions)
  - [IRM Staff](#irm-staff)
  - [Laboratory Staff](#laboratory-staff)
  - [MRSA Prevention Coordinator](#mrsa-prevention-coordinator)
  - [MRSA Program Tools Test Sites](#mrsa-program-tools-test-sites)
  - [Database Integration Agreements (DBIA)](#database-integration-agreements-dbia)
  - [MRSA-PT Routines](#mrsa-pt-routines)
  - [MRSA-PT Namespace](#mrsa-pt-namespace)
  - [MRSA-PT Files](#mrsa-pt-files)
  - [MRSA-PT Globals](#mrsa-pt-globals)
    - [New Global](#new-global)
    - [Temporary Global](#temporary-global)
  - [MRSA-PT Menus and Options](#mrsa-pt-menus-and-options)
    - [MRSA Tools Setup Menu](#mrsa-tools-setup-menu)
    - [MRSA-PT Reports Menu](#mrsa-pt-reports-menu)
    - [Report Tasking Options](#report-tasking-options)
    - [MRSA-PT Key](#mrsa-pt-key)
- [Security Introduction](#security-introduction)
- [Security Keys](#security-keys)
| Date      | Description                                                                                                                                                                                                                                                                                                                                                                                                           | Author                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| July 2010 | Updated for Patch MMRS\*1.0\*1. Adds sample internal hyperlink; adds Print Isolation Report as function which requires IRM Staff; and corrects access for file Laboratory Test (#60) in *Table 3 – Approved Database Integration Agreements*; adds caption for that table. Adds captions for *Table 6 – MRSA Tools Setup Menu Options; Table 7 – MRSA-PT Reports Menu Options; and Table 8 – Report Tasking Options*. | <span class="mark">REDACTED</span> |
| July 2010 | Initial Release. MMRS Package 1.0 installs the MRSA Program Tools software                                                                                                                                                                                                                                                                                                                                            | <span class="mark">REDACTED</span> |
<span id="_Ref251310381" class="anchor"></span>Table 1 – Text Conventions

# # List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc268768025" class="anchor"></span>ORIENTATION

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:

| Font                       | Used for…                             | Examples:                                                                                                                                          |
|--------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or URL      | “For further instructions on using KIDS, please refer to the [*Kernel Version 8.0 Systems Manual*](http://www.hardhats.org/kernel/docs/KRN8_0SM.PDF).” |
| Green text, dotted underlining | Hyperlink within this document            | “MRSA-PT contains reports that will extract and consolidate required data for entry into the [Inpatient Evaluation Center](#Glos_IEPC) (IPEC).”        |
| Arial                          | Text inside tables                        | (This table)                                                                                                                                           |
| Courier New                    | Menu options                              | MRSA Tools Parameter Setup                                                                                                                             |
|                                | Screen prompts                            | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                                                  |
|                                | Patch names                               | MMMS\*1.0\*1                                                                                                                                           |
|                                | VistA filenames                           | XYZ file \#798.1                                                                                                                                       |
|                                | VistA field names                         | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.”                              |
| Courier New, bold              | User responses to screen prompts          | NO                                                                                                                                                 |
| Franklin Gothic Demi           | Keyboard keys                             | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                                                       |
| Microsoft Sans Serif           | Software Application names                | MRSA Program Tools                                                                                                                                     |
|                                | Report names                              | Procedures report                                                                                                                                      |
| Times New Roman                | Body text (Normal text)                   | “There are no changes in the performance of the system once the installation process is complete.”                                                     |
| Times New Roman Italic         | Text emphasis                             | “It is *very* important…”                                                                                                                              |
|                                | National and International Standard names | *International Statistical Classification of Diseases and Related Health Problems*                                                                     |
|                                | Document names                            | *MRSA Program Tools Technical Manual & Security Guide*                                                                                                 |

<span id="_Ref251310415" class="anchor"></span>Table 2 – MRSA-PT Test Sites

THIS PAGE INTETIONALLY LEFT BLANK<span id="_Toc232559630" class="anchor"></span>

INTRODUCTION

<span id="_Toc268768028" class="anchor"></span>About the MRSA Program Tools Application

Manual data collection for the MRSA Prevention Initiative is time consuming. The MRSA Program Tools (MRSA-PT) application provides a method to extract data related to MRSA nares screening, clinical cultures, and patient movements within the selected facility. MRSA-PT contains reports that will extract and consolidate required data for entry into the [Inpatient Evaluation Center](#Glos_IEPC) (IPEC). Reports can also be generated to display real-time patient specific information, and can be used to identify patients that have a selected multi-drug resistant organism (MDRO) and to identify patients who did or did not receive a MRSA nares screen upon admission to the unit.

<span id="_Toc268768029" class="anchor"></span>Intended Audience

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for:

- Installing MRSA-PT
- Assigning menu and [Security Keys](#Glos_Sec_Key)
- Adding new divisions to the parameters
- [Tasking the Print Isolation Report (Tasked](#Rpt_PIRT))
- [Tasking the Print Nares Screen Compliance List (Tasked)](#Rpt_PNSCLT)

## Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *highly recommended* that the Laboratory Information Manager (LIM) and/or Laboratory Automated Data Processing Application Coordinator (ADPAC), and a representative from the Microbiology section (director, supervisor, or technologist) *jointly* participate in reviewing the parameter set-up for historical MRSA laboratory reporting, as well as the laboratory parameter setup for other multi-drug resistant organisms, as appropriate.

## MRSA Prevention Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Prevention Coordinator is required to participate in the parameter set-up due to the multi-disciplinary nature of the information to be retrieved by MRSA-PT. This will facilitate coordination of subsequent site interactions once the actual patch has been installed (*i.e.,* to be responsible for validation of reports).

  
THIS PAGE INTENTIONALLY LEFT BLANK<span id="_MRSA-PT_Setup_Menu" class="anchor"></span>

TECHNICAL GUIDE

## MRSA Program Tools Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 displays the sites that assisted in testing MRSA-PT prior to the release date.

<table>
<caption><p><span id="_Toc268768053" class="anchor"></span>Table – Approved Database Integration Agreements</p></caption>
<colgroup>
<col style="width: 69%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Test Site</strong></th>
<th><p><strong>Type of</strong></p>
<p><strong>Test Site</strong></p></th>
<th><strong>Date Installed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Alpha</td>
<td>01/22/09</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/22/09</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/23/09</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>07/27/09</td>
</tr>
</tbody>
</table>

<span id="_Toc268768053" class="anchor"></span>Table – Approved Database Integration Agreements

## Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 15 [database integration agreements](#Glos_DBIA) (DBIAs) approved for MRSA-PT. The following table lists the approved DBIAs.

<table style="width:100%;">
<caption><p><span id="_Toc249158675" class="anchor"></span>Table 4 – MRSA-PT Routines</p></caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Access</th>
<th>DBIA</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient (#2)</td>
<td>^DPT('CN',</td>
<td>#5431</td>
<td>Private</td>
</tr>
<tr class="even">
<td>Medical Center Division (#40.8)</td>
<td><p>^DG(40.8,D0,0)</p>
<p>.01</p></td>
<td>#728</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td>Census (#41.9)</td>
<td><p>^DG(41.9,'B',</p>
<p>^DG(41.9,D0,'C',D1,0)</p>
<p>2</p></td>
<td>#5433</td>
<td>Private</td>
</tr>
<tr class="even">
<td>Ward Location (#42)</td>
<td><p>^DIC(42,D0,44)</p>
<p>44</p></td>
<td>#10039</td>
<td>Supported</td>
</tr>
<tr class="odd">
<td>Hospital Location (#44)</td>
<td><p>^SC(D0,0)</p>
<p>.01</p></td>
<td>#10040</td>
<td>Supported</td>
</tr>
<tr class="even">
<td rowspan="2">Laboratory Test (#60)</td>
<td><p>^LAB(60,'B'</p>
<p>^LAB(60,’AB’,</p>
<p>^LAB(60,D0,1,D1,0)</p>
<p>1, 2</p></td>
<td>#67</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td><p>^LAB(60,D0,0)</p>
<p>.01, 4, 5</p>
<p>^LR(D0,'CH',D1,2...x)</p>
<p>^LR(D0,'MI',D1,0)</p>
<p>.01, .03, .05</p>
<p>^LR(D0,'MI',D1,1)</p>
<p>11.5</p>
<p>^LR(D0,'MI',D1,3,D2,0)</p>
<p>.01</p>
<p>^LR(D0,'MI',D1,3,D2,2.0001...x)</p>
<p>x.1</p>
<p>^LR(D0,'MI',D1,4,D2,0)</p>
<p>.01</p></td>
<td>#91</td>
<td>Controlled</td>
</tr>
<tr class="even">
<td>Lab Data (#63)</td>
<td><p>^LR(D0,'CH',D1,0)</p>
<p>.03, .05</p></td>
<td>#525</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td>Order (#100)</td>
<td><p>^OR(100,D0,0)</p>
<p>21</p>
<p>^OR(100,D0,3)</p>
<p>5</p>
<p>^OR(100,'AOI',</p></td>
<td>#5429</td>
<td>Private</td>
</tr>
<tr class="even">
<td>Orderable Items (#101.43)</td>
<td>^ORD(101.43,'ID',</td>
<td>#5430</td>
<td>Private</td>
</tr>
<tr class="odd">
<td rowspan="3">Patient Movement (#405)</td>
<td><p>^DGPM('AMV1',</p>
<p>^DGPM('AMV2',</p>
<p>^DGPM('AMV3',</p></td>
<td>#419</td>
<td>Controlled</td>
</tr>
<tr class="even">
<td><p>^DGPM(D0,0)</p>
<p>.03</p>
<p>^DGPM("ATT1",</p>
<p>^DGPM("ATT2",</p>
<p>^DGPM("ATT3",</p></td>
<td>#1865</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td><p>^DGPM(APTT1,</p>
<p>^DGPM(APTT2,</p>
<p>^DGPM(APTT3,</p></td>
<td>#2090</td>
<td>Controlled</td>
</tr>
<tr class="even">
<td>Clinical Reminder Index (PXRMINDX)</td>
<td><p>^PXRMINDX(63,</p>
<p>^PXRMINDX(100,</p></td>
<td>#4290</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td>Routine: ORX8</td>
<td>EN^ORX8</td>
<td>#871</td>
<td>Controlled</td>
</tr>
<tr class="even">
<td>Routine: LRPXAPIU</td>
<td>LRDFN^ LRPXAPIU</td>
<td>#4246</td>
<td>Controlled</td>
</tr>
<tr class="odd">
<td>Routine: LR7OR1</td>
<td>RR^LR7OR1</td>
<td>#2503</td>
<td>Controlled</td>
</tr>
</tbody>
</table>

<span id="_Toc249158675" class="anchor"></span>Table 4 – MRSA-PT Routines

## MRSA-PT Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following M routines are included in the KID build MMRS 1.0 (checksums were generated using the CHECK1^XTSUMBLD):

| Routine  | Routine Description                                | Checksum  |
|----------|----------------------------------------------------|-----------|
| MMRSIPC  | MRSA IPEC Report                                   | 96473573  |
| MMRSIPC2 | MRSA IPEC Report (continued)                       | 34845828  |
| MMRSIPC3 | MRSA IPEC Report (continued)                       | 103482398 |
| MMRSIPC4 | MRSA IPEC Report (continued)                       | 58171274  |
| MMRSIPC5 | Auto-Extract MRSA prevalence and transmission data | 24723912  |
| MMRSIPCP | All Setup Options                                  | 27513898  |
| MMRSISL  | Isolation Report                                   | 59561295  |
| MMRSORD  | Nares Screen Compliance List                       | 37424974  |

<span id="_Toc249158676" class="anchor"></span>Table – MRSA-PT Files

## MRSA-PT Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT has been assigned an independent [namespace](#Glos_Namespace) – MMRS.

## MRSA-PT Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are exported with the MRSA-PT software.

| File Name (Number)                          | Description                                                                                                                                       | Remarks                                                                                                                                                                                                         |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MRSA SITE PARAMETERS file (#104)            | Holds the set of parameters which modify the operation of MRSA-PT to suit the needs of the site.                                                  | For multi-divisional facilities, each division should have a separate entry in this file.                                                                                                                       |
| MRSA TOOLS LAB SEARCH/EXTRACT file (#104.1) | Contains search criteria used by MRSA-PT.                                                                                                         | This file should only be edited using the MRSA Tools Lab Parameter Setup option provided with this software.                                                                                                    |
| MDRO TYPES file (#104.2):                   | Contains the different multi-drug resistant organisms (MDROs) that are needed for the MRSA Program Tools software.                                | Entries in this file should not be edited. This file will be maintained by the Support Team.                                                                                                                    |
| MRSA WARD MAPPINGS file (#104.3)            | Contains the Ward Mappings for MRSA-PT. Facilities will create 'Geographical Units' which consist of one or more Ward Locations (from file \#42). | For the purposes of MRSA-PT, all Ward Locations belonging to the same Geographical Unit are considered one unit. Any interward transfers between wards belonging to the same Geographical Unit will be ignored. |

<span id="_Toc268768056" class="anchor"></span>Table – MRSA Tools Setup Menu Options

## MRSA-PT Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new global will be created with the installation of the MMRS 1.0 KIDS Build: ^MMRS. This global is quite small and mostly static. It contains the configuration parameters, ward mappings, lab/search extract parameters, etc. The data used for the MRSA-PT reports are extracted from the respective packages (LAB, PIMS, etc.) on-the-fly and are not stored in the MRSA-PT package.

### Temporary Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT uses the ^TMP global during report generation to store data needed to compile the reports.

## MRSA-PT Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT comes with two stand-alone menus:

- The MRSA Tools Setup Menu \[MMRS MRSA TOOLS SETUP MENU\] is used to setup the MRSA parameters. This menu is used to setup the parameters and is locked by the MMRS SETUP security key.
- The MRSA Tools Reports Menu \[MMRS REPORTS MENU\] is used to run the MRSA-PT reports.

### MRSA Tools Setup Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Tools Setup Menu consists of five options:

| Option                            |                                   | Purpose/Remarks                                                                                                                                                                                                                                       |
|-----------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MRSA Tools Parameter Setup (Main) | \[MMRS MRSA PARAMETER SETUP\]     | Allows the user to add/edit the parameters which will modify the operation of MRSA-PT; defines the division(s) and business rules for MRSA nares screening.                                                                                           |
| MRSA Tools Lab Parameter Setup    | \[MMRS MRSA LAB PARAMETER SETUP\] | Allows the user to define parameters for the [multi-drug resistant organism](#Glos_MDRO) (MDRO) that is to be searched for. This information is used to obtain prior history of MRSA and to display precaution measures for the selected organism(s). |
| MRSA Tools Ward Mapping Setup     | \[MMRSA WARD MAPPING SETUP\]      | Allows the user to define geographical units for the division(s). It will allow the user to map units together.                                                                                                                                       |
| MDRO Historical Days Edit         | \[MMRS MRSA MDRO HIST DAYS EDIT\] | Allows the user to define the timeframe to search the history of the selected MDRO for the MRSA Tools Isolation Report.                                                                                                                               |
| Isolation Orders Add/Edit         | \[MMRS ISLT ORD EDIT\]            | Allows the user to enter the orders at the site that are used for isolation purposes. This will be used to populate the MRSA Tools Isolation Report.                                                                                                  |

<span id="_Toc268768057" class="anchor"></span>Table – MRSA-PT Reports Menu Options

### MRSA-PT Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Tools Reports Menu consists of three options:

| Option                             |                           | Purpose/Remarks                                                                                                                                                                                                                                                        |
|------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Print MRSA IPEC Report             | \[MMRS MRSA IPEC REPORT\] | Allows the user to print the MRSA IPEC report. The report can be run for the division or for a specific unit(s). It allows the user to select either the Admission Report or the Discharge/Transmission report.                                                        |
| Print Isolation Report             | \[MMRS ISOLATION REPORT\] | Allows the user to print the Isolation Report for each unit. The report includes MDROs selected in the initial setup and the historical timeframe to search for the last positive result. Isolation Orders will print on the report, if they are utilized by the site. |
| Print Nares Screen Compliance List | \[MMRS NARES SWAB LIST\]  | Allows the user to print a report to capture the patient on a unit at a given time and if a nares screen was ordered upon admission to the unit. This report prints real-time patient information for the unit.                                                        |

<span id="_Toc268768058" class="anchor"></span>Table – Report Tasking Options

### Report Tasking Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are also three options that are used to task some of the reports.

| Option                                                                                  |                                    | Used To…                                                                                                                                         |
|-----------------------------------------------------------------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Rpt_PIRT" class="anchor"></span>Print Isolation Report (Tasked)               | \[MMRS ISOLATION REPORT (TASKED)\] | Task the Isolation Report.                                                                                                                       |
| <span id="Rpt_PNSCLT" class="anchor"></span>Print Nares Screen Compliance List (Tasked) | \[MMRS NARES SWAB LIST (TASKED)\]  | Task the Nares Screen Compliance List.                                                                                                           |
| MRSA IPEC Auto-Extract (Tasked)                                                         | \[MMRS MRESA IPEC AUTO-EXTRACT\]   | Auto-extract MRSA data for entry into the Inpatient Evaluation Center (IPEC) for the previous month's MRSA prevalence and transmission measures. |

### MRSA-PT Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT comes with one [security key](#Glos_Sec_Key). The MMRS SETUP key is used to lock the MRSA Tools Setup Menu and all its options. A user assigned to this key is allowed to run the MRSA Tools Parameter Setup Menu and to setup or change the system parameters.

<span id="_Toc249158630" class="anchor"></span>SECURITY GUIDE

# Security Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Security Guide aids in controlling the release of sensitive information related to national software. MRSA-PT does not contain highly sensitive information, so this component of the manual may be included in Freedom of Information Act (FOIA) request releases. There are no unique/atypical features or other information that would be of interest to security personnel or other support groups.

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT has one [security key](#Glos_Sec_Key) – MMRS SETUP. This key locks the following options, and should only be given to users who will need to setup/edit the parameters to run the software.

MRSA Tools Setup Menu

MRSA Tools Parameter Setup (Main)

MRSA Tools Lab Parameter Setup

MRSA Tools Ward Mapping Setup

MDRO Historical Days Edit

Isolation Orders Add/Edit

<span id="_Toc232405454" class="anchor"></span>GLOSSARY

[![](mrsa-program-tools-version-1-technical-manual/002.png)](\l) [![](mrsa-program-tools-version-1-technical-manual/003.png)](#G_B) [![](mrsa-program-tools-version-1-technical-manual/004.png)](#G_C) [![](mrsa-program-tools-version-1-technical-manual/005.png)](#G_D) [![](mrsa-program-tools-version-1-technical-manual/006.png)](#G_E) [![](mrsa-program-tools-version-1-technical-manual/007.png)](#G_F) [![](mrsa-program-tools-version-1-technical-manual/008.png)](#G_G) [![](mrsa-program-tools-version-1-technical-manual/009.png)](#G_I) [![](mrsa-program-tools-version-1-technical-manual/010.png)](#G_K) [![](mrsa-program-tools-version-1-technical-manual/011.png)](#G_L) [![](mrsa-program-tools-version-1-technical-manual/012.png)](#G_M) [![](mrsa-program-tools-version-1-technical-manual/013.png)](#G_N) [![](mrsa-program-tools-version-1-technical-manual/014.png)](#G_P) [![](mrsa-program-tools-version-1-technical-manual/015.png)](#G_S) [![](mrsa-program-tools-version-1-technical-manual/016.png)](#G_T) [![](mrsa-program-tools-version-1-technical-manual/017.png)](#G_V) [![](mrsa-program-tools-version-1-technical-manual/018.png)](#G_W)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Term or Acronym</th>
<th colspan="3">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td><strong>A</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/019.png)</a></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td colspan="3"><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a></td>
</tr>
<tr class="odd">
<td>ANTIMICROBIAL SUSCEPTIBILITY file #62.6</td>
<td colspan="3">Antimicrobial used to determine sensitive/resistant <a href="#Glos_etiology">etiologies</a>.</td>
</tr>
<tr class="even">
<td><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td colspan="3">The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or <a href="#Glos_IRM">Information Resource Management</a> (IRM). Also, the designated individual responsible for user-level management and maintenance of an application package (<em>e.g.</em>, Laboratory).</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_B" class="anchor"></span><strong>B</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/020.png)</a></td>
</tr>
<tr class="even">
<td>Begin Date/Time</td>
<td colspan="3">The date that the report is to start.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_C" class="anchor"></span><strong>C</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/021.png)</a></td>
</tr>
<tr class="even">
<td>CLC</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Center</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_ClientServer" class="anchor"></span>Client-server</td>
<td colspan="3">A common form of distributed system in which software is split between server tasks and client tasks. A client sends requests to a server, according to some protocol, asking for information or action, and the server responds. This is analogous to a customer (client) who sends an order (request) on an order form to a supplier (server) who dispatches the goods and an invoice (response). The order form and invoice are part of the “protocol” used to communicate in this case.</td>
</tr>
<tr class="even">
<td><span id="Glos_CLC" class="anchor"></span>Community Living Center (CLC)</td>
<td colspan="3"><p>A CLC provides a dynamic array of services in person-centered environments that meet the individual needs of residents, providing excellent health care and quality of life.</p>
<p><em>Formerly known as</em> VA Nursing Home Care Units (NHCU).</p></td>
</tr>
<tr class="odd">
<td><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td colspan="3">A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients’ healthcare information. CPRS is the Department of Veteran’s Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient’s medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td colspan="3"><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="odd">
<td>CPT</td>
<td colspan="3"><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="even">
<td><span id="Glos_CPT" class="anchor"></span>Current Procedural Terminology (CPT)</td>
<td colspan="3"><p>CPT® is the most widely accepted medical nomenclature used to report medical procedures and services under public and private health insurance programs. CPT codes describe a procedure or service identified with a five-digit CPT code and descriptor nomenclature. The CPT code set accurately describes medical, surgical, and diagnostic services and is designed to communicate uniform information about medical services and procedures among physicians, coders, patients, accreditation organizations, and payers for administrative, financial, and analytical purposes. The current version is the CPT 2009.</p>
<p><em>Note:</em> CPT® is a registered trademark of the American Medical Association.</p>
<p><em>See also</em> <a href="#Glos_ICD9">ICD-9</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_D" class="anchor"></span><strong>D</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/022.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td colspan="3">A formal understanding between two or more application packages which describes how data is shared or how packages interact. This agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td colspan="3">See <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="even">
<td>Domiciliary</td>
<td colspan="3">The VHA Domiciliary Residential Rehabilitation and Treatment program provides coordinated, integrated rehabilitative and restorative clinical care in a bed-based program, with the goal of helping eligible veterans achieve and maintain the highest level of functioning and independence possible. Domiciliary Care, as an integral component of VHA's continuum of health care services, is committed to providing the highest quality of clinical care in a coordinated, integrated fashion within that continuum.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_E" class="anchor"></span><strong>E</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/023.png)</a></td>
</tr>
<tr class="even">
<td>End Date/Time</td>
<td colspan="3">The date the report is to stop.</td>
</tr>
<tr class="odd">
<td><span id="Glos_etiology" class="anchor"></span>Etiology</td>
<td colspan="3">The cause or causes of a disease or abnormal condition; also, a branch of medical science dealing with the causes and origin of diseases.</td>
</tr>
<tr class="even">
<td>ETIOLOGY FIELD file #61.2</td>
<td colspan="3">This file is used to select the etiology/organism.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_F" class="anchor"></span><strong>F</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/024.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td colspan="3"><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="odd">
<td><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="3">A <a href="#Glos_ClientServer">client-server</a> protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in <a href="http://www.ietf.org/rfc/rfc959.txt">Internet Standard 9, Request for Comments 959</a>.</td>
</tr>
<tr class="even">
<td>FREE TEXT field</td>
<td colspan="3"><p>You can enter almost any character from your keyboard in a FREE TEXT-type field. The program will accept numbers, letters, and most of the symbols that can be entered. The FREE TEXT field places a restriction on the number of characters that you can enter. If you enter a question mark ("<strong>?</strong>") in response to the prompt for a FREE TEXT field, you'll learn how many characters you are allowed to enter.</p>
<p>For example, a FREE TEXT field would probably be used to hold a patient's street address:</p>
<p>ADDRESS: <strong>235 Begonia Street</strong></p>
<p>In some places, even though the field is FREE TEXT, checks are applied to make sure what is entered matches a certain format. For example, if you're entering a Social Security Number (which is stored as a FREE TEXT, not NUMERIC, field), your input would typically be checked to make sure it is nine characters in length, and contains all digits:</p></td>
</tr>
<tr class="odd">
<td>FTP</td>
<td colspan="3"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_G" class="anchor"></span><strong>G</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/025.png)</a></td>
</tr>
<tr class="odd">
<td>Geographical Unit</td>
<td colspan="3">A field in the <a href="#Glos_Ward_Mapping">Ward Mapping</a> setup file used to assign an arbitrary name to a group of units (wards) to run the reports.</td>
</tr>
<tr class="even">
<td><span id="Glos_Global" class="anchor"></span>Global</td>
<td colspan="3"><p><a href="#Glos_M">M</a> uses <em>globals</em>: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
<p><strong>SET ^A(“first_name”)=”Bob”</strong></p>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common M programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_I" class="anchor"></span><strong>I</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/026.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_ICD9" class="anchor"></span>ICD-9</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, ninth edition (commonly abbreviated as “ICD-9”) provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The “9” refers to the ninth edition of these codes; the tenth edition has been published, and VA expects to begin using ICD-10 in the future. On January 15, 2009, the U.S. Department of Health and Human Services (HHS) published a final rule establishing ICD-10 as the new national coding standard. The implementation date, initially proposed for October 2011, has been set for October 1, 2013.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="odd">
<td>Indicated Value</td>
<td colspan="3">Code to determine how to compare data (<em>e.g.</em>, “<strong>R</strong>” equals “resistant”).</td>
</tr>
<tr class="even">
<td>Indicator</td>
<td colspan="3">Code to determine how to match results/interpretations.</td>
</tr>
<tr class="odd">
<td><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="even">
<td><span id="Glos_IEPC" class="anchor"></span>Inpatient Evaluation Center (IPEC)</td>
<td colspan="3">The IPEC is a national program to improve outcomes (risk adjusted mortality and length of stay) in VA Intensive Care Units (ICUs) and eventually in inpatient care through feedback of outcomes and implementation of evidenced-based practices. Currently two of the initiatives deal with issues related to infection prevention— catheter-related bloodstream infections and ventilator-associated pneumonias— both of which may involve resistant organisms. These data are reported back immediately to the local facilities who can track their rates over time and compliance with performance, as well as see the national mid-range statistical analysis results.</td>
</tr>
<tr class="odd">
<td>IPEC</td>
<td colspan="3"><em>See</em> <a href="#Glos_IEPC">Inpatient Evaluation Center</a></td>
</tr>
<tr class="even">
<td>IRM</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_isolate" class="anchor"></span>Isolate</td>
<td colspan="3">(noun) An individual (as a spore or single organism), a viable part of an organism (as a cell), or a strain that has been isolated (as from diseased tissue, contaminated water, or the air); also: a pure culture produced from such an isolate.</td>
</tr>
<tr class="even">
<td>Isolation Order</td>
<td colspan="3">Ordered by the provider to place a patient in a certain type of precaution (<em>e.g.</em>, Contact Precautions, Airborne Precautions, etc.) based on the patient’s clinical status.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_K" class="anchor"></span><strong>K</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/027.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_KIDS" class="anchor"></span>Kernel Installation and Distribution System (KIDS)</td>
<td colspan="3">The Kernel system permits any <a href="#Glos_VistA">VistA</a> software application to run without modification to its base structure no matter what hardware or software vendor the application was built on. The Kernel contains a number of building management supplies which provide its foundation, including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</td>
</tr>
<tr class="odd">
<td>Keys</td>
<td colspan="3"><em>See</em> <a href="#Glos_Sec_Key">Security Keys</a></td>
</tr>
<tr class="even">
<td>KIDS</td>
<td colspan="3"><em>See</em> <a href="#Glos_KIDS">Kernel Installation and Distribution System</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_L" class="anchor"></span><strong>L</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/028.png)</a></td>
</tr>
<tr class="even">
<td>LAB DATA file #63</td>
<td colspan="3">This file is used to store the patient’s laboratory data.</td>
</tr>
<tr class="odd">
<td><span id="Glos_LIM" class="anchor"></span>Laboratory Information Manager</td>
<td colspan="3">The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> (CPRS) functions.</td>
</tr>
<tr class="even">
<td>LABORATORY TEST file #60</td>
<td colspan="3">This is the file that holds the names and ordering, display of tests.</td>
</tr>
<tr class="odd">
<td>LIM</td>
<td colspan="3"><em>See</em> <a href="#Glos_LIM">Laboratory Information Manager</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_M" class="anchor"></span><strong>M</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/029.png)</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_M" class="anchor"></span>M</td>
<td colspan="3"><p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p></td>
</tr>
<tr class="even">
<td>MAS</td>
<td colspan="3">See <a href="#Glos_MAS">Medical Administration Service</a></td>
</tr>
<tr class="odd">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="even">
<td><span id="Glos_MailMan" class="anchor"></span>MailMan</td>
<td colspan="3">MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</td>
</tr>
<tr class="odd">
<td>MDRO</td>
<td colspan="3"><em>See</em> <a href="#Glos_MDRO">Multi-Drug Resistant Organism</a></td>
</tr>
<tr class="even">
<td><span id="Glos_MAS" class="anchor"></span>Medical Administration Service (MAS)</td>
<td colspan="3">The Chief, MAS at health care facilities is responsible for administrative aspects of the hospital including determination of eligibility, maintenance and reconciliation of records, review of claims for payment, and compliance with VA Regulations.</td>
</tr>
<tr class="odd">
<td><span id="Glos_MRSA" class="anchor"></span>Methicillin-resistant <em>Staphylococcus aureus</em> (MRSA)</td>
<td colspan="3">A type of bacterium that is resistant to certain antibiotics.</td>
</tr>
<tr class="even">
<td>Methicillin-Resistant <em>Staphylococcus aureus</em> Prevention Initiative</td>
<td colspan="3">The initiative involves establishment of a national MRSA Prevention Initiative for all VA Medical Centers. In January 2007 VHA administration took strong directive action in plan to address infection with MRSA nationwide as a prototype agent for multidrug resistance issues; this national plan employs a bundle approach which includes hand hygiene, contact precautions, active surveillance culturing and cultural change. Seventeen VA medical centers ("beta-sites") across the country are also participating in a cooperative evaluation of this process with the Centers for Disease Control and Prevention (CDC). The initiative was implemented in January 2007; by December 31, 2007 all inpatient acute care units nationwide in VHA had begun the initiative. This work is ongoing, with evaluation for expansion into additional settings such as the long-term care/nursing home/community living center area. National data collection has begun for areas of prevalence of MRSA infection/colonization on admission, healthcare-associated infection with MRSA and MRSA transmission.</td>
</tr>
<tr class="odd">
<td>MMRS SETUP</td>
<td colspan="3">The name of the key that is given to a user to lock the MRSA Tools Setup Menu and all its options. The user(s) assigned to this key is allowed to run the MRSA Tools Parameter Setup Menu and setup/change the system parameters.</td>
</tr>
<tr class="even">
<td>MPC</td>
<td colspan="3">See <a href="#Glos_MPC">MRSA Prevention Coordinator</a></td>
</tr>
<tr class="odd">
<td>MRSA</td>
<td colspan="3">See <a href="#Glos_MRSA">Methicillin-resistant <em>Staphylococcus aureus</em></a></td>
</tr>
<tr class="even">
<td><span id="Glos_MPC" class="anchor"></span>MRSA Prevention Coordinator (MPC)</td>
<td colspan="3">Individual responsible with oversight of the MRSA Prevention Program at their facility.</td>
</tr>
<tr class="odd">
<td><span id="Glos_MDRO" class="anchor"></span>Multi-Drug Resistant Organism</td>
<td colspan="3">A bacterium that is resistant to multiple antibiotics.</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_N" class="anchor"></span><strong>N</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/030.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_Namespace" class="anchor"></span>Namespace</td>
<td colspan="3">A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Global">globals</a>, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In <a href="#Glos_VistA">VistA</a>, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MRSA-PT.</td>
</tr>
<tr class="odd">
<td>Nares Screening</td>
<td colspan="3">One method used to detect the presence of MRSA in humans is by means of a sample taken from the nares (nose) using a swab. The sample taken is then tested for the presence of MRSA.</td>
</tr>
<tr class="even">
<td>NHCU</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Centers</a></td>
</tr>
<tr class="odd">
<td>Nursing Home Care Units (NHCU)</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Centers</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_P" class="anchor"></span><strong>P</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/031.png)</a></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td colspan="3">A specific type of <a href="#Glos_MailMan">MailMan</a> message used to distribute <a href="#Glos_KIDS">KIDS</a> builds.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_S" class="anchor"></span><strong>S</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/032.png)</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_Sec_Key" class="anchor"></span>Security Keys</td>
<td colspan="3">Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The <a href="#Glos_VistA">VistA</a> option file refers to the security key as a “lock.” Only those individuals assigned that “lock” can use a particular VistA option or perform a specific task that is associated with that security key/lock. In MRSA-PT, keys are used to access specific options that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="even">
<td>Selected Etiology</td>
<td colspan="3">Organism or final microbial diagnosis/<a href="#Glos_isolate">isolate</a>.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_T" class="anchor"></span><strong>T</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/033.png)</a></td>
</tr>
<tr class="even">
<td>Tasked Report</td>
<td colspan="3">Reports that can be scheduled via <a href="#Glos_TaskMan">TaskMan</a>.</td>
</tr>
<tr class="odd">
<td><span id="Glos_TaskMan" class="anchor"></span>TaskMan</td>
<td colspan="3">The Kernel module that schedule and processes background tasks (aka Task Manager)</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td colspan="3"><em>See</em> <a href="#Glos_TCPIP">Transmission Control Protocol over Internet Protocol</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_TCPIP" class="anchor"></span>Transmission Control Protocol over Internet Protocol (TCP/IP)</td>
<td colspan="3">The <em>de facto</em> standard Ethernet protocols, TCP/IP was developed for internetworking and encompasses both network layer and transport layer protocols. While TCP and IP specify two protocols at specific protocol layers, TCP/IP is often used to refer to the entire Department of Defense protocol suite based upon these, including telnet, File Transfer Protocol (FTP), User Datagram Protocol (UDP), and Reliable Data Protocol (RDP).</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_V" class="anchor"></span><strong>V</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/034.png)</a></td>
</tr>
<tr class="odd">
<td>Value</td>
<td colspan="3">Code used to determine how to compare results.</td>
</tr>
<tr class="even">
<td><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3">VistA is a comprehensive, integrated health care information system composed of numerous software modules. <em>See</em> <a href="http://www.va.gov/vista_monograph/docs/2008VistAHealtheVet_Monograph.pdf">http://www.va.gov/VistA_monograph/docs/2008VistAHealtheVet_Monograph.pdf</a> and <a href="http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm">http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm</a>.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_W" class="anchor"></span><strong>W</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-technical-manual/035.png)</a></td>
</tr>
<tr class="odd">
<td>WARD LOCATION File #42</td>
<td colspan="3">This file contains all of the facility ward locations and their related data (<em>e.g.</em>, operating beds, bed section, etc.). The wards are created/edited using the Ward Definition option of the ADT module.</td>
</tr>
<tr class="even">
<td><span id="Glos_Ward_Mapping" class="anchor"></span>Ward Mapping</td>
<td colspan="3">Ward mapping indicated inpatient units (wards) that have been mapped together to create one geographical unit to facilitate data collection.</td>
</tr>
</tbody>
</table>