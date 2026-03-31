---
title: MRSA Program Tools Version 1 User Manual
doc_type: UM
doc_label: User Manual
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
menu_options: 1
description: - [Revision History](#revision-history) - [List of Tables](#list-of-tables) - [List of Figures](#list-of-figures) - [Text Conventions](#text-conventions) - [Graphic Conventions](#graphic-conventions) - [Keyboard Conventions](#keyboard-conventions) - [IRM Staff](#irm-staff) - [Laboratory Staff](#labo
audience: 
keywords: 
  - mrsa
  - class
  - strong
  - span
  - report
  - table
  - nares
  - unit
  - admission
  - patient
page_count: 0
word_count: 17330
section_count: 13
table_count: 14
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: January 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

[![](mrsa-program-tools-version-1-user-manual/001.png)](#TOC)

MRSA PROGRAM TOOLSVersion 1.0

Patch MMRS\*1.0\*1

User Manual

January 2010 (Revised July 2010)

Office of Enterprise Development (OED)

Field Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [List of Tables](#list-of-tables)
- [List of Figures](#list-of-figures)
  - [Text Conventions](#text-conventions)
  - [Graphic Conventions](#graphic-conventions)
  - [Keyboard Conventions](#keyboard-conventions)
  - [IRM Staff](#irm-staff)
  - [Laboratory Staff](#laboratory-staff)
  - [MRSA Prevention Coordinator](#mrsa-prevention-coordinator)
- [MRSA Tools Reports Menu](#mrsa-tools-reports-menu)
  - [MRSA IPEC Report](#mrsa-ipec-report)
  - [Admission Report](#admission-report)
  - [Admission Summary Report](#admission-summary-report)
  - [Discharge/Transmission Report](#dischargetransmission-report)
  - [## Discharge/Transmission Summary Report](#dischargetransmission-summary-report)
  - [Isolation Report (Census List and MDRO History)](#isolation-report-census-list-and-mdro-history)
    - [This section contains supplemental information regarding MRSA-PT.](#this-section-contains-supplemental-information-regarding-mrsa-pt)
- [Troubleshooting](#troubleshooting)
- [Printing in Landscape](#printing-in-landscape)
    - [This section contains supplemental information regarding how reports from MRSA-PT can assist MRSA Prevention Coordinators with data entry into IPEC.](#this-section-contains-supplemental-information-regarding-how-reports-from-mrsa-pt-can-assist-mrsa-prevention-coordinators-with-data-entry-into-ipec)
- [Validation of Data Capture](#validation-of-data-capture)
    - [Nares Screening Compliance](#nares-screening-compliance)
    - [Transmission Review](#transmission-review)
    - [Clinical Culture Assignment Review](#clinical-culture-assignment-review)
    - [Clinical Culture Transmission Review](#clinical-culture-transmission-review)
    - [Transmission Review – CLC Periodic Screening](#transmission-review-clc-periodic-screening)
- [# Laboratory Reporting of MRSA Test](#laboratory-reporting-of-mrsa-test)
- [# Schedule TaskMan Tasks (Optional)](#schedule-taskman-tasks-optional)
- [# MAS Movements](#mas-movements)
<table>
<caption><p><span id="_Toc268767175" class="anchor"></span>Table 1 – Text Conventions</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 55%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>July 2010</td>
<td><p>Updated for Patch MMRS*1.0*1. Major changes:</p>
<ul>
<li><p><em>Figure 2 – Print MRSA IPEC Admission Report</em>, <em>Table 3 – Data Points: MRSA IPEC Admission Report</em>, <em>Figure 4 – MRSA IPEC Discharge/ Transmission Report</em>, and <em>Table 6 – Data Points: MRSA IPEC Discharge/Transmission Report</em> updated to show/explain asterisk (*) before patient name, indicating patient was indicated for nasal screen upon admission to unit, based on site’s business rules.</p></li>
<li><p>Hyperlink errors in initial release were fixed. Usual start and end dates for the <em>MRSA IPEC Report</em> were clarified.</p></li>
<li><p>Appendix D, Business Rules for Nares Screening (Examples) was deleted and appendixes following were renumbered.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>January 2010</td>
<td>Initial Release. MMRS Package 1.0 installs the MRSA Program Tools software</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
<span id="_Toc268767175" class="anchor"></span>Table 1 – Text Conventions

# List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc268767137" class="anchor"></span>ORIENTATION

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:
| Font                       | Used for…                             | Examples:                                                                                                                                          |
|--------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or URL      | “For further instructions on using KIDS, please refer to the [*Kernel Version 8.0 Systems Manual*](http://www.hardhats.org/kernel/docs/KRN8_0SM.PDF).” |
| Green text, dotted underlining | Hyperlink within this document            | “For instructions on how to set task these reports, see Print Isolation Report (Tasked).”                                                              |
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
|                                | Document names                            | *MRSA Program Tools User Manual*                                                                                                                       |
<span id="_Toc268767176" class="anchor"></span>Table 2 – Graphic Conventions

## Graphic Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following graphic symbols are used throughout this document, usually in a boxed note or the equivalent.
| Graphic                                        | Used for…                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------|
| ![](mrsa-program-tools-version-1-user-manual/002.png)  | Information of particular interest regarding the current subject matter |
| ![](mrsa-program-tools-version-1-user-manual/003.png) | A tip or additional information that may be helpful to you              |
| ![](mrsa-program-tools-version-1-user-manual/004.png) | A warning concerning the current subject matter                         |
<span id="_Ref232825595" class="anchor"></span>Table 3 – Data Points: MRSA IPEC Admission Report

## Keyboard Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Text centered between arrows represents a keyboard key that should be pressed in order for the system to capture a user response or to move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.
*Example:* Press \<Tab\> to move the cursor to the next field.
Press \<Enter\> to select the default.
- One, two, or three question marks can be entered at any of the prompts for online help.
| ?   | One question mark displays a brief statement of what information is appropriate for the prompt.             |
|-----|-------------------------------------------------------------------------------------------------------------|
| ??  | Two question marks provide more help, plus any hidden actions.                                              |
| ??? | Three question marks will provide more detailed help, including a list of possible answers, if appropriate. |
<span id="_Ref232825538" class="anchor"></span>Table 4 – Data Points: Prevalence Measures (Facility Wide)
- The caret ^ (also called the “up arrow” or circumflex) plus \<Enter\> can be used to exit the current option.
<span id="_Toc232559630" class="anchor"></span>
INTRODUCTION
<span id="_Toc268767142" class="anchor"></span>About the MRSA Program Tools Application
Manual data collection for the MRSA (Methicillin-resistant Staphylococcus aureus) Prevention Initiative is time consuming. The MRSA Program Tools (MRSA-PT) application provides a method to extract data related to MRSA nares screening, clinical cultures, and patient movements within the selected facility. MRSA-PT contains reports that will extract and consolidate required data for entry into the [Inpatient Evaluation Center](#Glos_IEPC) (IPEC). Reports can also be generated to display real-time patient specific information, and can be used to identify patients that have a selected multi-drug resistant organism (MDRO) and to identify patients who did or did not receive a MRSA nares screen upon admission to the unit.
<span id="_Toc268767143" class="anchor"></span>Intended Audience

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for:
- Installing MRSA-PT
- Assigning menu and [Security Keys](#Glos_Sec_Key)
- Adding new divisions to the parameters
- Tasking the Print Isolation Report (Tasked)
- Tasking the Print Nares Screen Compliance List (Tasked)

## Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *highly recommended* that the Laboratory Information Manager (LIM) and/or Laboratory Automated Data Processing Application Coordinator (ADPAC), and a representative from the Microbiology section (director, supervisor, or technologist) *jointly* participate in reviewing the parameter set-up for historical MRSA laboratory reporting, as well as the laboratory parameter setup for other multi-drug resistant organisms, as appropriate.

## MRSA Prevention Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Prevention Coordinator is required to participate in the parameter set-up due to the multi-disciplinary nature of the information to be retrieved by MRSA-PT. This will facilitate coordination of subsequent site interactions once the actual patch has been installed (*i.e.,* to be responsible for validation of reports).
<span id="_Toc268767147" class="anchor"></span>USING MRSA TOOL REPORTS

# MRSA Tools Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the five options in the MRSA Tools Setup Menu have been set up (*see* Installation Manual), the user can go to the MRSA Tools Reports Menu to select reports to print for the Division and/or Unit. The following are the three options:

MRSA IPEC Report: This option allows the user to print the MRSA IPEC Report. The report can be run for all the locations in a Division or a specific location. The report can be run for either Admission (prevalence measures) or Discharge/Transmission (transmission measures).

Isolation Report (Census List and MDRO History) : This option allows the user to print the Isolation Report for each unit. The Isolation Report includes MDROs selected in the initial setup and the historical time frame to search for the last positive result. If sites utilize Isolation Orders, these will also print on the report. If no Isolation Orders are used at the site then these fields will be excluded from the report.

Nares Screen Compliance List: This option allows the user to print a report to capture real-time patient information on a unit at a specified time to determine if a nares screen was obtained upon admission to the unit. This report allows the unit to determine patients that received (or did not receive) a nares screen upon admission.

## MRSA IPEC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is used to obtain all pertinent information for data entry into the Inpatient Evaluation Center (IPEC) for Facility-Wide Prevalence Measures and Unit-Specific Prevalence and Transmission Measures. After selecting the report, you will be prompted to run either the <u>A</u>dmission Report or <u>D</u>ischarge/Transmission Report.

| ![](mrsa-program-tools-version-1-user-manual/005.png) | Note: The MRSA IPEC Report should be run no earlier than 5 business days after the close of the month. This allows the laboratory to complete testing and enter the results into VistA. This is a suggested timeframe; it will be dependent on the laboratory practices at each facility. |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref232825550" class="anchor"></span>Table 5 – Data Points: Prevalence Measures (Unit Specific)

| ![](mrsa-program-tools-version-1-user-manual/006.png) | Note: The MRSA IPEC Report should be run monthly to gather the required data for entry into IPEC. The reports are not meant for daily monitoring. Daily monitoring can be conducted using the Isolation Report and Nares Screen Compliance Report. |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref266799883" class="anchor"></span>Table 6 – Data Points: MRSA IPEC Discharge/Transmission Report

The Admission Report uses unit admission dates, while the Discharge Report uses unit discharge dates. For example, if the Admission Report is set to run for the CCU for the month of February 2009, it will display all patients admitted into the CCU during February 2009, regardless of when they were discharged from the unit (or if they still remain on the unit). If the Discharge Report is run for February 2009, it will display all patients that were discharged from the CCU during February 2009, regardless of when they entered the unit. The Discharge report will also display all patients that were still on the unit at the end of February.

The user will be prompted to enter a start date to run the report and an ending date for the report. Reports normally should be run beginning with the first day of the month and ending with the last day of the month.

After setting the date range to run the report, the user will be prompted to enter the Geographical Locations for the report. The report can be run for one unit or all units. Only Geographical Units created using the MRSA Tools Ward Mapping Setup option can be selected. The report is designed for a 176 column format (landscape) (see Appendix A to see sample Terminal Type landscape setup).

<span id="_Toc268767185" class="anchor"></span>Figure 1 – Print MRSA IPEC Report

<table>
<caption><p><span id="_Toc268767181" class="anchor"></span>Table 7 – Data Points: Transmission Measures (Unit Specific)</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print MRSA IPEC Report</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Select one of the following:</p>
<p>A Admission Report</p>
<p>D Discharge/Transmission Report</p>
<p>Run (A)dmission Or (D)ischarge/Transmission Report: Admission Report</p>
<p>Begin with ward admission date: <strong>020109</strong> (FEB 01, 2009)</p>
<p>End with ward admission date: <strong>022809</strong> (FEB 28, 2009)</p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Geographical Location:</p>
<p>Do you want to only print the summary report? NO//</p>
<p>This report is designed for a 176 column format (landscape).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT LANDSCAPE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767181" class="anchor"></span>Table 7 – Data Points: Transmission Measures (Unit Specific)

| ![](mrsa-program-tools-version-1-user-manual/007.png) | Important Note: Do not generate a MRSA IPEC Report for any Geographical Unit that is an OBS unit. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------|

<span id="_Toc268767182" class="anchor"></span>Table 8 – Data Points: Census List and MDRO History

## Admission Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admission Report displays the listing of patients that have been admitted to the unit for the calendar month. If a patient was admitted to the unit multiple times during the calendar month, then the patient will be displayed for each admission to the unit.

<span id="_Toc268767186" class="anchor"></span>Figure 2 – Print MRSA IPEC Admission Report

<table>
<caption><p><span id="_Toc268767183" class="anchor"></span>Table 9 – Data Points: Nares Screen Compliance List</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC ADMISSION REPORT</p>
<p>GEOGRAPHICAL LOCATION: 11AB</p>
<p>Report period: Oct 01, 2007 to Oct 31, 2007@24:00</p>
<p>Report printed on: Jan 16, 2009@14:07:26 PAGE: 1</p>
<p>NARES NARES CULTURE</p>
<p>DATE MAS MOVE SCREEN RESULT RESULT MRSA IN</p>
<p>WARD PATIENT SSN ENTERED WARD ADT TYPE 24H 48H 48H PAST YEAR</p>
<p>---------------------------------------------------------------------------------------------------------</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/07@09:43 A DIRECT Y</p>
<p>11ABSURG XXXXXXXXXXXXXXXXXX XXXX 10/1/07@16:11 T INTEWARD TRA Y</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/1/07@20:25 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/07@23:49 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/07@19:57 A DIRECT</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/1/07@11:01 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/13/07@13:42 A DIRECT Y POS</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/13/07@18:41 A DIRECT Y</p>
<p>11ABSURG XXXXXXXXXXXXXXXXXX XXXX 10/20/07@23:14 T INTERWARD TRA Y</p>
<p>11ABMED XXXXXXXXXXXXXXXXXX XXXX 10/21/07@14:34 T INTERWARD TRA Y POS POS</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/23/07@01:19 A DIRECT Y POS</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/13/07@13:42 A DIRECT Y</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767183" class="anchor"></span>Table 9 – Data Points: Nares Screen Compliance List

A description of each of the columns appears in Table 3 below.

| Data Point                 | Displays…                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WARD                       | The VistA Ward the patient was admitted/transferred-in to.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PATIENT                    | Patient’s last name, first name. An asterisk (\*) before the patient’s name denotes that the patient was indicated for a nasal screen upon admission to the unit based on the site’s business rules.                                                                                                                                                                                                                                                                                                                   |
| SSN                        | Last 4 digits of the patient’s social security number                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DATE ENTERED WARD          | Date patient was admitted/transferred-in to the unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADT                        | How the patient entered the unit: <u>A</u>dmission or <u>T</u>ransfer-In to the unit                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [MAS](#Glos_MAS) MOVE TYPE | Type of admission movement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| NARES SCREEN 24H           | Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit. Only tests that follow the new MRSA lab standards will be picked up (the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’). Please see the *Installation Manual* for more information on setting up the new MRSA lab standards.                                                                                                                                                                     |
| NARES RESULT 48H           | POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of admission/transfer-in to the unit. Only tests that follow the new MRSA lab standards will be picked up (for nares screens, the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’; for surveillance cultures they must be called ‘MRSA SURVL OTHER AGAR’ or ‘MRSA SURVL OTHER DNA’). Please see the *Installation Manual* for more information on setting up the new MRSA lab standards. |
| CULTURE RESULT 48H         | POS (positive) if the patient had a clinical culture and it was positive within 48 hours of admission/transfer-in to the unit. Only cultures that were reported using the new MRSA lab standards will be picked up (the site must report positives cultures using the Etiology ‘STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)’). Please see the *Installation Manual* for more information on setting up the new MRSA lab standards.                                                                              |
| MRSA IN PAST YEAR          | Patient’s MRSA history going back one year prior to admission/transfer-in to the unit until the date/time of admission/transfer-in. It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year. The program will determine what’s considered a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.                                                   |

<span id="_Ref232489687" class="anchor"></span>Table 10 – MAS Movement Types

## Admission Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report displays all pertinent information to enter Prevalence Measure data into the Inpatient Evaluation Center (IPEC). The report displays Facility-Wide and Unit-Specific information.

The report will print a summary report for each unit. If multiple units were printed together, then an additional summary report will print, containing summary data for all the units combined. This combined summary report can be useful to get the Facility-Wide prevalence measures that are needed to be inputted into IPEC (saving the user the task of adding all the individual Facility wide measures together).

<span id="_Toc268767187" class="anchor"></span>Figure 3 – MRSA IPEC Admission Summary Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC ADMISSION SUMMARY REPORT</p>
<p>Geographical Location: 11AB</p>
<p>Report period: Oct 01, 2007 to Oct 31, 2007@24:00</p>
<p>Report printed on: Jan 16, 2009@14:07:26 PAGE: 2</p>
<p>Prevalence Measures (Facility Wide)</p>
<p>1. Number of Admissions to the facility: 31</p>
<p>2. Number of (1) who received MRSA nasal screening upon admission to facility: 28</p>
<p>3. Number of (1) positive for MRSA based on nasal screening upon admission to facility: 5</p>
<p>4. Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility: 0</p>
<p>Prevalence Measures (Unit Specific)</p>
<p>1. Number of admissions (admissions + transfers in) to the unit for the month: 41</p>
<p>2. Number of (1) for whom nasal screening was indicated: 41</p>
<p>3. Number of (2) who received nasal screening upon admission to unit (within 24 hours): 38</p>
<p>4. Number of (1) positive for MRSA based on nasal screening upon admission to unit: 6</p>
<p>5. Number of (1) positive for MRSA based on clinical cultures upon admission to unit: 0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description of each of the data points appears in Table 4 and Table 5 below.

| Data Point                                                                                     | Displays…                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of admissions to the facility                                                           | Direct admissions to the facility for the calendar month. \[NOTE: This includes all admissions (direct, non-service connected, etc.) and TO ASIH admissions.\] (It will not include unit-to-unit transfers).                                                                                                                                                                                         |
| Number of (1) who received MRSA nasal screening upon admission to facility                     | Direct admissions who received a MRSA nasal screen within 24 hours of admission to the facility.                                                                                                                                                                                                                                                                                                     |
| Number of (1) positive for MRSA based on nasal screening upon admission to facility            | Direct admissions who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the facility and results were positive for MRSA, plus those direct admissions that had a prior history of MRSA in the past 12 months based on nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the facility will be excluded. |
| Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility | Direct admissions that had a clinical culture upon admission to the facility and results were positive within 48 hours of admission. \[NOTE: If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.\]                                                                                                   |

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Point</th>
<th>Displays…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number of admissions (admissions + transfers in) to the unit for the month</td>
<td>Direct admissions <em>plus</em> transfers-ins to the unit for the calendar month.</td>
</tr>
<tr class="even">
<td>Number of (1) for whom nasal screening was indicated</td>
<td><p>The number of admissions and transfers-in to the unit for the calendar month for whom a nasal screen was indicated. The program will determine this information based on the site parameters entered during setup.</p>
<p>If the admitting unit at a site does not screen patients on unit-to-unit transfers (but the discharging unit does), then only Facility admissions will be indicated for a swab.</p>
<p>If a site does not screen patients with MRSA history on transfer-ins, then a patient with a <em>known</em> MRSA history (within 365 days prior to entering the unit) will not be indicated for a swab on unit-to-unit transfers. To be considered ‘<em>known</em> positive’ the lab result must have been <em>verified</em> before the patient entered the unit. [NOTE: This is different from the column ‘MRSA IN PAST YEAR’, where the collection date (not verification date) was used.]</p></td>
</tr>
<tr class="odd">
<td>Number of (2) who received MRSA nasal screening upon admission to unit (within 24 hours)</td>
<td>Admissions and transfers-in to the unit for the calendar month that were indicated for a MRSA nares screen and who received a MRSA nasal screen within 24 hours of admission to the unit.</td>
</tr>
<tr class="even">
<td>Number of (1) positive for MRSA based on nasal screening upon admission to unit</td>
<td>Admissions and transfers-in to the unit for the calendar month who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the unit and results were positive for MRSA, plus those admissions and transfers-in that had a prior history of MRSA in the past 12 months, either by nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the unit will be excluded.</td>
</tr>
<tr class="odd">
<td>Number of (1) positive for MRSA based on clinical cultures upon admission to unit</td>
<td>Admissions and transfers-in to the unit who had a clinical culture upon admission to the unit and results were positive within 48 hours of admission to unit. [NOTE: If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.]</td>
</tr>
</tbody>
</table>

## Discharge/Transmission Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Discharge/Transmission Report displays all discharges that occurred for the calendar month. It also includes all patients that were still on the unit at the end of the calendar month. If a patient was discharged from the unit more than once, they will show up multiple times.

<span id="_Toc268767188" class="anchor"></span>Figure 4 – MRSA IPEC Discharge/Transmission Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>MRSA IPEC DISCHARGE/TRANSMISSION REPORT</strong></p>
<p><strong>Geographical Location: 11AB</strong></p>
<p><strong>Report period: Oct 01, 2007 to Pct 31, 2007@24:00</strong></p>
<p><strong>Report printed on: Jan 16, 2009#14:25:15 PAGE: 1</strong></p>
<p><strong>ADM NARES NARES DIS NARES NARES MRSA</strong></p>
<p><strong>DATE ADM MAS MOVE SCREEN RESULT MRSA IN DATE DIS MAS MOVE SCREEN RESULT IN CURR</strong></p>
<p><strong>WARD PATIENT SSN ENTERED WARD ADT TYPE 24H 48H PAST YR LEFT WARD ADT TYPE 24H 48H PRD TRANS</strong></p>
<p><strong>---------------------------------------------------------------------------------------------------------------------------------------------------------------</strong></p>
<p><strong>11ABS XXXXXXXXXXXXXXX XXXX 9/7/07@17:51 T INTERWARD TRA POS 10/27/07@18:20 D NON-SERVICE C Y</strong></p>
<p><strong>11ABM *XXXXXXXXXXXXXXX XXXX 9/26/07@18:17 A DIRECT Y POS 10/12/07@15:24 D MPM=SERVICE C</strong></p>
<p><strong>11ABS XXXXXXXXXXXXXXX XXXX 9/27/07@16:26 T INTERWARD TRA Y POS POS 10/1/07@12:07 T INTERWARD TRA Y POS POS</strong></p>
<p><strong>11ABM *XXXXXXXXXXXXXXX XXXX 9/28/07@19:58 A DIRECT Y 10/2/07@21:22 D MOM-SERVICE C</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 9/28/07@20:03 A DIRECT Y 10/2/07@21:12 D TRANSFER OUR Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 9/28/07@22:11 A DIRECT Y 10/1/07@16:40 D NON-SERVICE C Y</strong></p>
<p><strong>11ABM XXXXXXXXXXXXXXX XXXX 10/13/07@13:42 A DIRECT Y POS POS 10/14/07@23:57 D IRREGULAR POS</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/14/07@15:11 A DIRECT Y 10/26/07@17:21 D NON-SERVICE C Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/16/07@11:05 T INTERWARD TRA Y 10/18/07@19:50 T INTEWARD TRA Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/16/07@17:35 A DIRECT Y 10/20/07@13:10 D NON-SERVICE C Y POS POS T</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/17/07@17:00 A DIRECT Y 10/17/07@22:19 T INTERWARD TRA</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description of each of the data points is in Table 6.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Point</th>
<th>Displays…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WARD</td>
<td>The VistA Ward the patient was on.</td>
</tr>
<tr class="even">
<td>PATIENT</td>
<td>Patient’s last name, first name. An asterisk (*) before the patient’s name denotes that the patient was indicated for a nasal screen upon discharge from the unit based on the site’s business rules.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Last 4 digits of the patient’s social security number</td>
</tr>
<tr class="even">
<td>DATE ENTERED WARD</td>
<td>Date patient was admitted to the unit</td>
</tr>
<tr class="odd">
<td>ADM ADT</td>
<td>How the patient entered the ward: <u>A</u>dmission or <u>T</u>ransfer-In to the unit</td>
</tr>
<tr class="even">
<td><a href="#Glos_MAS">MAS</a> MOVE TYPE</td>
<td>Type of admission movement</td>
</tr>
<tr class="odd">
<td>NARES SCREEN 24H</td>
<td>Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit. Only tests that follow the new MRSA laboratory standards will be picked up (the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’). Please see the <em>Installation Manual</em> for more information on setting up the new MRSA lab standards.</td>
</tr>
<tr class="even">
<td>NARES RESULT 48H</td>
<td>POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of admission to the unit. Only tests that follow the new MRSA lab standards will be picked up (for nares screens, the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’; for surveillance cultures they must be called ‘MRSA SURVL OTHER AGAR’ or ‘MRSA SURVL OTHER DNA’). Please see the <em>Installation Manual</em> for more information on setting up the new MRSA lab standards.</td>
</tr>
<tr class="odd">
<td>MRSA IN PAST YEAR</td>
<td><p>Patient’s MRSA history going back one year prior to admission until 48 hours after admission. It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year.</p>
<p>Begin time frame: (Admission – 365 days) or (report start date – 365 days), whichever is later</p>
<p>End time frame: (Admission + 48 hours) or (report start date), whichever is later</p>
<p>The program will determine a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>DATE LEFT WARD</td>
<td>Date the patient left the unit</td>
</tr>
<tr class="odd">
<td>DIS ADT</td>
<td>How the patient left the unit: <u>D</u>ischarge or <u>T</u>ransfer-out</td>
</tr>
<tr class="even">
<td>DIS MAS MOVE TYPE</td>
<td>Type of discharge movement</td>
</tr>
<tr class="odd">
<td>NARES SCREEN 24H</td>
<td>Y (yes) if the patient had a nares screen within 24 hours of being discharged from the unit. Only tests that follow the new MRSA lab standards will be picked up (the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’). Please see the <em>Installation Manual</em> for more information on setting up the new MRSA lab standards.</td>
</tr>
<tr class="even">
<td>NARES RESULT 48H</td>
<td>POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of exiting the unit. Only tests that follow the new MRSA lab standards will be picked up (for nares screens, the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’; for surveillance cultures they must be called ‘MRSA SURVL OTHER AGAR’ or ‘MRSA SURVL OTHER DNA’). Please see the <em>Installation Manual</em> for more information on setting up the new MRSA lab standards.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>MRSA IN CURR PRD</th>
<th><p>POS (positive) if the patient had a positive MRSA nasal screen, surveillance culture or clinical culture during the current admission.</p>
<p>Begin time frame: (Admission + 48 hrs) or (Report start date), whichever is later</p>
<p>End time frame: (Discharge + 48 hours) or (Report end date), whichever is earlier.</p>
<p>The program will determine what’s considered a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TRANS</td>
<td><p>T if the patient had a transmission within the selected time range.</p>
<p>Transmission is defined as a patient with a negative nares screen within 48 hours of admission to the unit (NARES RESULT 48H) and no history of MRSA within the past 365 days (MRSA IN PAST YEAR). In addition, on transfer and/or discharge from the unit the patient must have a positive nares screen (NARES RESULT 48H), or be positive for MRSA during the current admission (MRSA IN CURR PRD).</p></td>
</tr>
</tbody>
</table>

## ## Discharge/Transmission Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report displays all pertinent information to enter Transmission Measure data into the Inpatient Evaluation Center (IPEC). The report displays information for Unit-Specific data entry.

<span id="_Toc268767189" class="anchor"></span>Figure 5 – MRSA IPEC Discharge/Transmission Summary Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC DISCHARGE/TRANSMISSION SUMMARY REPORT</p>
<p>Geographical Location: SICU</p>
<p>Report period: Mar 01, 2009 to Mar 15, 2009@24:00 PAGE: 1</p>
<p>Transmission Measures (Unit Specific)</p>
<p>10. Number of bed days of care for the unit: 115</p>
<p>11. Number of exits (discharges + deaths + transfers out) from the unit: 33</p>
<p>12. Number of (11) for whom a discharge/transfer swab was indicated: 33</p>
<p>13. Number of (12) who received MRSA nasal screening upon exit from unit: 31</p>
<p>14. Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures: 0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description of each of the data points appears as follows:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Point</th>
<th>Displays…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number of bed days of care for the unit</td>
<td>Bed days of care for the unit for the calendar month.</td>
</tr>
<tr class="even">
<td>Number of exits (discharges + deaths + transfers out) from the unit</td>
<td>The number of exits (discharges/deaths/transfers out) from the unit for the calendar month.</td>
</tr>
<tr class="odd">
<td>Number of (11) for whom a discharge/transfer swab was indicated</td>
<td><p>The number of discharges, deaths and transfer out from the unit for the calendar month, for whom a nasal screen was indicated. The program will determine this information based on the site parameters entered during setup.</p>
<p>If the discharging unit at a site does not screen patients on unit-to-unit transfers (but the admitting unit does), then only Facility discharges or death will be indicated for a swab.</p>
<p>If a site does not screen patients with MRSA history on discharge/death/transfer-outs, then a patient with a <em>known</em> MRSA history (within 365 days prior to leaving the unit) will not be indicated for a swab. To be considered ‘<em>known</em> positive’ the lab result must have been <em>verified</em> before the patient left the unit. [NOTE: This is different than the column ‘MRSA IN PAST YEAR’, where the collection date (not verification date) was used.]</p></td>
</tr>
<tr class="even">
<td>Number of (12) who received MRSA nasal screening upon exit from the unit</td>
<td>Those discharges, deaths and transfers out who were indicated for a MRSA nares screen and received a MRSA nares screen within 24 hours from exit from the unit.</td>
</tr>
<tr class="odd">
<td>Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures</td>
<td>The number of transmissions on the units for the calendar month identified either by MRSA nares screen or clinical culture, while taking into account the patient’s history of MRSA in the past 12 months.</td>
</tr>
</tbody>
</table>

## Isolation Report (Census List and MDRO History) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is optional. It can be used to print a ward census and will identify patients on the unit that have a selected MDRO (*i.e.*, MRSA, CRB-R, VRE, *C. diff*, VRE, ESBL). The report displays real-time unit-specific patient information. The report is based off of information entered in the parameter setup (MDRO and historical days, and Isolation Orders, if applicable). The report will display the patient’s last known positive MDRO and active Isolation Orders, if used by the facility.

The report is designed for a 176 column format (landscape) (see Appendix A to see sample Terminal Type landscape setup).

<span id="_Toc268767190" class="anchor"></span>Figure 6 – Isolation Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print Isolation Report</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Location:</p>
<p>This report is designed for a 176 column format (landscape).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT LANDSCAPE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The report can be tasked to print to a specific unit at one or more specific times of day. This allows the unit to identify patients to be placed in contact precautions and to see if any Isolation Orders have been ordered for the patient. See Print Isolation Report (Tasked) for instructions on how to setup this option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CENSUS LIST AND MDRO HISTORY</strong></p>
<p><strong>Geographical location: 11AB</strong></p>
<p><strong>Report printed on: Mar 05, 2009@14:28:10 PAGE: 1</strong></p>
<p><strong>LAST MRSA POS LAST CRB-R POS LAST ESBL POS LAST VRE POS LAST CDF POS</strong></p>
<p><strong>PATIENT SSN IN 365 DAYS IN 365 DAYS IN 356 DAYS IN 365 DAYS IN 28 DAYS ISOLATION ORDER START DATE</strong></p>
<p><strong>--------------------------------------------------------------------------------------------------------------------------------------------------</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX CONTACT PRECAUTIONS 3/1/09</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/28/09@17:00 6/1/09@13:30 5/13/09@15:15 6/5/09@13:30 CONTACT PRECAUTIONS 2/27/09</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/28/09@17:00 6/1/09@13:30 5/13/09@15:15 6/5/09@13:30 CONTACT PRECAUTIONS 11/13/08</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 10/7/08@21:57</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/25/09@15:05 5/14/09@20:01 CONTACT PRECAUTIONS 2/25/09</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 3/3/09@18:44 CONTACT PRECAUTIONS 3/4/09</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description of each of the data points appears as follows:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Point</th>
<th>Displays…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT</td>
<td>Patient’s last name, first name</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Last 4 digits of the patient’s social security number</td>
</tr>
<tr class="odd">
<td>MRSA IN 365 DAYS</td>
<td><p>Last positive MRSA result (either by nares screen, surveillance culture or clinical culture) in the past 365 days.</p>
<p>The program will determine a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>CRB-R IN XXX DAYS</td>
<td><p>Last positive CRB-R result in the past XXX days. This column is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p>The program will determine a CRB-R positive based on the parameter set-up (MRSA Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="odd">
<td>ESBL IN XXX DAYS</td>
<td><p>Last positive ESBL result in the past XXX days. This column is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p>The program will determine an ESBL positive based on the parameter set-up (MRSA Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="even">
<td>VRE IN XXX DAYS</td>
<td><p>Displays the last positive VRE result in the past XXX days. This column is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p>The program will determine a VRE positive based on the parameter set-up (MRSA Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="odd">
<td>CDIFF IN XXX DAYS</td>
<td><p>Last positive C. <em>difficile</em> result in the past XXX days. This column is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p>The program will determine a C. <em>diff</em> positive based on the parameter set-up (MRSA Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="even">
<td>ISOLATION ORDER</td>
<td>Type of Isolation Order the provider has ordered for the patient. This will only be displayed if the site uses Isolation Orders, and information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit). If more than one Isolation Order has been ordered for the patient, then the patient will be listed multiple times on the report, dependent on the number of Isolation Orders.</td>
</tr>
<tr class="odd">
<td>START DATE</td>
<td>Start Date for the Isolation Order that the provider ordered for the patient. This will only be displayed if the site uses Isolation Orders, and information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit).</td>
</tr>
</tbody>
</table>

#### Nares Screen Compliance List

This report is optional. It can be used to print a ward census and identify if a MRSA nares screen was ordered for the patient. This report prints real-time patient information on the unit. The report is designed for a 132 column format (compressed).

<span id="_Toc268767191" class="anchor"></span>Figure 7 – Nares Screen Compliance List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print Nares Screen Compliance List</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Location:</p>
<p>This report is designed for a 132 column format (compressed).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT COMPRESSED</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767192" class="anchor"></span>Figure 8 – Nares Swab Order List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NARES SWAB ORDER LIST</p>
<p>Geographical Location: 11AB</p>
<p>Report printed on: Mar 02, 2009@15:31:27 PAGE: 1</p>
<p>DATE MRSA IN NARES LAB</p>
<p>PATIENT SSN ENTERED WARD ADT PAST YEAR ORDERED ORDER DATE RECEIVED</p>
<p>-------------------------------------------------------------------------------------------</p>
<p>XXXXXXXXXXXXXXX XXXX 2/27/09@19:13 T POS YES 2/27/09@18:53 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/27/09@19:37 A YES 2/27/09@23:30 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/24/09@18:37 A POS YES 2/24/09@22:05 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 3/2/09@14:19 A</p>
<p>XXXXXXXXXXXXXXX XXXX 3/2/09@02:48 A YES 3/2/09@07:00 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 3/1/09@13:40 A YES 3/1/09@14:15 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/22/09@11:02 T POS YES 2/22/09@01:48 YES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description of each of the data points appears as follows:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Point</th>
<th>Displays…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT</td>
<td>Patient’s last name, first name</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Last 4 digits of the patient’s social security number</td>
</tr>
<tr class="odd">
<td>DATE ENTERED WARD</td>
<td>Date the patient was admitted to the unit</td>
</tr>
<tr class="even">
<td>ADT</td>
<td>How the patient entered the ward: <u>A</u>dmission or <u>T</u>ransfer-In to the unit</td>
</tr>
<tr class="odd">
<td>MRSA IN PAST YEAR</td>
<td><p>POS (positive) if the patient had a positive MRSA result (either by nares screen or clinical culture).</p>
<p>The program will determine a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>NARES ORDERED</td>
<td><p>YES if a nares screen was ordered for the patient. The report starts searching for a nares screen beginning 24 hours before admission – going forward. The first active or completed order it finds once it starts searching, is the order that gets displayed on the report. If there are no active or completed orders, then the first pending order within that time frame will be displayed.</p>
<p>Only orders for tests that follow the new MRSA lab standards will be picked up (the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’). Please see the <em>Installation Manual</em> for more information on setting up the new MRSA lab standards.</p></td>
</tr>
<tr class="odd">
<td>ORDER DATE</td>
<td>Date the nares screen was ordered for the patient.</td>
</tr>
<tr class="even">
<td>LAB RECEIVED</td>
<td>YES if the nares screen was received in the lab.</td>
</tr>
</tbody>
</table>

This report can be tasked to print to a specific unit at one or more specific times of the day. This allows the unit to determine if a patient did not have a nares screen upon admission and to obtain one, if needed. See page [39](#print-nares-screen-compliance-list-tasked) for instructions on setting up this option.

| ![](mrsa-program-tools-version-1-user-manual/008.png) | Important Note: This report is based on the laboratory standards for the following test names: MRSA SURVL NARES DNA and MRSA SURVL NARES AGAR. If the standards have not been implemented or have been set up incorrectly, then the report will not display accurate information. |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="AppA" class="anchor"></span>

APPENDIX A

### This section contains supplemental information regarding MRSA-PT.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If errors are encountered when generating a report, the following messages might be displayed:

1.  Running any option, except for MRSA Tools Parameter Setup (Main), without first defining a Division:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the division has been setup using option:</p>
<p>‘MRSA Tools Parameter Setup (Main)’</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Running any reports, without setting up one of the following Chemistry subscripted tests (MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the MRSA Chemistry subscripted tests have been setup according to the National Guidelines. Laboratory needs to setup at least one of the lab tests in the system before generating reports:</p>
<p>1. ‘MRSA SURVL NARES DNA’</p>
<p>2. ‘MRSA SURVL NARES AGAR’</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Running any reports without setting up the etiology STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the Etiology has been setup according to the National Guidelines. The following etiology must be added to the Etiology Field File (#61.2):</p>
<p>‘STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)’</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Running any report without defining the Geographical Unit:

| \>\>\> Make sure the Ward Mappings for each Geographical Unit has been setup |
|------------------------------------------------------------------------------|

# Printing in Landscape

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a sample Terminal Type for a landscape setup. Actual entries may vary depending on make and model of printer.

NAME: P-TCP LANDSCAPE RIGHT MARGIN: 176

FORM FEED: \# PAGE LENGTH: 51

BACK SPACE: \$C(8)

OPEN EXECUTE: W \$C(27),"&l1O",\$C(27),"&l7C",\$C(27),"&k2S",\$C(27),"&l2E"

CLOSE EXECUTE: W \$C(27),"E" D CLOSE^NVSPRTU

  
<span id="_Toc268767159" class="anchor"></span>APPENDIX B

### This section contains supplemental information regarding how reports from MRSA-PT can assist MRSA Prevention Coordinators with data entry into IPEC.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a screen shot for an acute care unit for data entry into IPEC.

![](mrsa-program-tools-version-1-user-manual/009.png)

Reports generated by the MRSA-PT software can be used to aid in data entry; thereby, eliminating manual data collection and reducing error.

# Validation of Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites will have to evaluate the MRSA Program Tools software program once it is implemented to ensure that the software is accurately capturing MRSA data for entry into the [Inpatient Evaluation Center (IPEC).](#Glos_IEPC)

Once the initial parameters are completed, it is recommended that the MRSA IPEC Report option is run to evaluate at least 3 months of data. The Admission and Discharge Summary reports should be compared with site specific records to ensure optimal data capture of by MRSA-PT. This comparison will also help determine that site parameters have been accurately defined.

### Nares Screening Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compliance with nares screening is based on the collection date and time. The program searches within 24 hours (before and after) movement. If the time the specimen was obtained is not entered, then the program defaults to a time of 00:00 on the day that the nares screen was obtained.

> Example: MRSA nares screen was collected on October 21, 2009. No time was entered. The collection date and time will be 10/21/2009@00:00.

> If in the example above the swab was obtained in the Emergency Department and the patient was admitted on October 22, 2009 at 8:41am, the nares screen will <u>not</u> be considered compliant due to the fact that the time was not entered. The program will consider the swab obtained 32 hours and 41 minutes prior to admission.

It is important the collection date and time is entered into the system. Failure to do so will *more than likely* count the nares screen obtained as non-compliant due to the timeframe that is being searched.

### Transmission Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A transmission is assigned when a patient has a length of stay greater than 48 hours and does not have a history of MRSA within the past 12 months. The algorithm below illustrates how a transmission is assigned to a patient/unit.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>MRSA IN PAST YEAR</th>
<th><p>Patient’s MRSA history going back one year prior to admission until 48 hours after admission. It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year.</p>
<p>Begin time frame: (Admission – 365 days) or (report start date – 365 days), whichever is later</p>
<p>End time frame: (Admission + 48 hours) or (report start date), whichever is later</p>
<p>The program will determine a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MRSA IN CURR PRD</td>
<td><p>POS (positive) if the patient had a positive MRSA nasal screen, surveillance culture or clinical culture during the current admission.</p>
<p>Begin time frame: (Admission + 48 hrs) or (Report start date), whichever is later</p>
<p>End time frame: (Discharge + 48 hours) or (Report end date), whichever is earlier.</p>
<p>The program will determine what’s considered a MRSA positive based on the parameter set-up (MRSA Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>TRANS</td>
<td><p>T if the patient had a transmission within the selected time range.</p>
<p>Transmission is defined as a patient with a negative nares screen within 48 hours of admission to the unit (NARES RESULT 48H) and no history of MRSA within the past 365 days (MRSA IN PAST YEAR). In addition, on transfer and/or discharge from the unit the patient must have a positive nares screen (NARES RESULT 48H), or be positive for MRSA by clinical culture during the current admission (MRSA IN CURR PRD).</p></td>
</tr>
</tbody>
</table>

Example: Mr. Smith is admitted to Unit X on August 20, 2009 at 2:10am. His nares screen was collected on August 20, 2009 at 4:22pm and the result was negative for MRSA. On August 22, 2009 he was discharged at 10:55am, and his nares screen was collected at 11:00am. The program assigned a Transmission for this patient. Mr. Smith does not have a history of MRSA within the past 12 months.

MRSA IN PAST YEAR:

> Begin Time Frame: August 20, 2009 at 2:10am – 365 days = August 20, 2008 at 2:10am

End Time Frame: August 20, 2009 at 2:10am + 48 hours = August 22, 2009 at 2:10am

MRSA IN CURRENT PERIOD:

Begin Time Frame: August 20, 2009 at 2:10am + 48 hours = August 22, 2009 at 2:10am

> End Time Frame: August 22, 2009 at 10:55am + 48 hours = August 24, 2009 at 10:55am

Transmission defined:

> This patient had a negative nares screen on admission and on discharge he had a positive nasal screen. His length of stay was greater than 48 hours so a transmission was assigned. Remember to look back 48 hours after the positive result was obtained to determine if a transmission occurred. The positive result was obtained on August 22, 2009 at 11:00am and 48 hours prior to it (August 20, 2009 at 11:00am) he was on Unit X.

### Clinical Culture Assignment Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Positive clinical cultures should be reviewed for accuracy to ensure that the clinical culture is assigned to the appropriate unit. A clinical culture should be assigned to the unit that collected the culture (or if the culture was obtained prior to admission in an outpatient setting). There may be instances in which the clinical culture gets assigned to multiple units, depending if the patient moves multiple times within 48 hours of admission.

Example: Mr. Jones was admitted on September 15, 2009 at 11:00am to the ICU. He had a nares screen and clinical culture at 11:45am. On September 15 at 9:02pm Mr. Jones was transferred to 3 North. On transfer he had a nares screen at 9:55pm. The IPEC Admission Report for the month of September displayed a POS in the column “CULTURE RESULT 48 HRS” for both the ICU and 3 North. This is <u>incorrect</u>. The positive clinical culture should only be assigned to the ICU. Manual data correction will need to be made. In this instance, for 3 North you would decrease the number positive by clinical culture (Line 5) and increase the number positive by nasal screen (Line 4).

### Clinical Culture Transmission Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All transmissions should be reviewed for accuracy. There may be instances in which the program may assign a transmission but upon chart review it is determined that a transmission did not occur.

Example: Mr. Jones was admitted to 4 South on Friday, October 2, 2009 at 10:22pm. Upon admission he had a nares screen performed (collected on October 2, 2009 at 11:14pm) and the result was negative (upon review he does not have a history of MRSA within the past 12 months). Mr. Jones had a wound on his leg and a fever of 101°F, which was documented in the chart. On Tuesday, October 6 at 8:14am, the physician ordered a clinical culture because the wound began to pus. The culture was positive for MRSA. A transmission was assigned to 4 South for Mr. Jones because he does not have a history of MRSA within the past 12 months, his admission nares screen was negative and he had a positive clinical culture greater than 48 hours after admission. However, this would <u>not</u> be considered a transmission because there was evidence that the wound was incubating on admission based on information obtained from Mr. Jones’ chart. You would decrease the number of transmission on 4 South by 1 in this example.

### Transmission Review – CLC Periodic Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When periodic screening is conducted in the Community Living Center for the month in question, the Transmission Measures section needs to be reviewed and adjusted manually. On the Discharge/Transmission Report for Line 14 (Number of MRSA transmissions on unit based on MRSA nasal screenings or clinical cultures) this number will need to be adjusted if the resident has a positive nasal screen and does not have a history of MRSA within the past 12 months.

Example: For the month of July the Discharge/Transmission Report shows 4 transmissions for the month for a CLC unit. During the month of July, Periodic Screening was conducted on this CLC unit. Upon review of the transmissions, 3 of the transmissions were identified during the periodic screening and the 1 transmission was due to a clinical culture on a resident. In this situation, manual correction of the data needs to be made. When entering data into IPEC, you would enter 1 transmission in Line 14 and 3 transmissions in Line 18. This is because the 3 transmissions were identified during Periodic Screening and need to be recorded appropriately under this section.

<span id="AppB" class="anchor"></span>APPENDIX C

# # Laboratory Reporting of MRSA Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Each VA facility is to implement the following test names and laboratory reporting for MRSA tests. This standardization allows for national collection of data on MRSA nares screening and culture-positive results. VHA Laboratory Services must record results of MRSA Tests performed within a VA laboratory using the following methodology:
1.  MI-subscripted tests will be used for clinical culture based tests; A clinical culture is ordered by the provider for clinical reasons (e.g., patient is sick, presents clinical symptoms) to determine if a pathogenic organism is present and the appropriate antibiotics for treatment.
2.  CH-subscripted tests will be used for nares screening or other types of surveillance screening because they have limited defined values. Surveillance cultures are used to establish prevalence, or monitor and control a situation (i.e., identification of asymptomatic individuals or carriers).
2.  Implementation Notes
    1.  MI-Subscripted Tests:
        1.  <u>ONLY</u> clinical cultures (C&S) will be reported using MI-subscript.
        2.  STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the <u>only</u> etiology that will be used to report positive clinical cultures.
        3.  Emerging Pathogens Initiative (EPI) will use the etiology listed above for its data pull.
    2.  CH-Subscripted Tests:
        1.  MRSA nares screens or MRSA surveillance cultures (e.g., perineum, axilla, etc.) will be reported using CH-subscript.
        2.  The following Test Names and Logical Observation Identifiers Names & Codes (LOINC) will be used:
            1.  MRSA SURVL NARES DNA
                1.  35492-8 MRSA DNA XXX Q1 PCR, Staphylococcus aureus.methicillin resistant DNA
                2.  SITE/SPECIMEN is limited to “Nares”; no other SITE/SPECIMEN can be used with this test name
            2.  MRSA SURVL OTHER DNA
                1.  35492-8 MRSA DNA XXX Q1 PCR, Staphylococcus aureus.methicillin resistant DNA
                2.  Test is for MRSA Surveillance Screening other than “Nares”. SITE/SPECIMEN could be “Axilla” or “Perineum” or other surveillance testing done locally.
            3.  MRSA SURVL NARES AGAR
                1.  13317-3 MRSA XXX Q1 Cult, Staphylococcus aureus.methicillin resistant isolate
                2.  52969-3\* MRSA Nose Q1 Cult, Staphylococcus aureus.methicillin resistant isolate (*\*will be available when File 95.3 is updated; until then 13317-3 is to be used*)
                3.  SITE/SPECIMEN is limited to “Nares”; no other SITE/SPECIMEN can be used with this test name
            4.  MRSA SURVL OTHER AGAR
                1.  13317-3 MRSA XXX Q1 Cult, Staphylococcus aureus.methicillin resistant isolate
                2.  Test is for MRSA Surveillance Screening other than “Nares”. SITE/SPECIMEN could be “Axilla” or “Perineum” or other surveillance testing done locally.
        3.  For integrated or co-located sites that need to offer site/division specific tests, the test name has to start with “MRSA SURVL NARES DNA” (or any other standard test name listed above) and modifiers are added at the end of the name. For example, MRSA SURVL NARES DNA Site 1 and MRSA SURVL NARES DNA Site 2, etc.
        4.  To standardize data entry format, when the Data name is created for each test the CH-subscript test input transform needs to be Set of Codes:

> Negative is to Negative

> POSITIVE is to POSITIVE

> Invalid is to Invalid Inhibitors Present.

> *NOTE:Positive is intentionally in uppercase for impact.*

1.  Enter data type of MRSA SURVL NARES DNA: (N)umeric, (S)et of Codes, or (F)ree text ? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
    3.  INTERNALLY-STORED CODE://Invalid WILL STAND FOR:// Invalid Inhibitors Present
2.  Enter data type of MRSA SURVL NARES AGAR: (N)umeric, (S)et of Codes, or (F)ree text ? S
1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
3.  Enter data type of MRSA SURVL OTHER DNA: (N)umeric, (S)et of Codes, or (F)ree text ? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
    3.  INTERNALLY-STORED CODE://Invalid WILL STAND FOR:// Invalid Inhibitors Present
4.  Enter data type of MRSA SURVL OTHER AGAR: (N)umeric, (S)et of Codes, or (F)ree text? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
5.  To standardize the interpretation of the test result, VHA Laboratory Services will need to add a “Comment” to each invalid PCR test result. This is a new entry in the Lab Description File (File 62.5).
    1.  NAME: MRSAIR
        1.  Expansion: Inhibitors Present, Please Repeat
    2.  NAME: MRSAIC
        1.  Expansion: Inhibitors Present, Culture Is Being Performed
        2.  NOTE: This comment should be used if the first swab is invalid and the laboratory uses agar to process the second swab.
6.  The results must be documented under a specifically created MRSA Section of Laboratory Results display in Computerized Patient Record System (CPRS) Graphic User Interface (GUI). The report sections must be set up in the Lab Reports File (File 64.5) under the Cumulative Report name.
    1.  VistA GUI Cumulative View will need to be set-up for Horizontal Format reporting to ensure that test results will be easily accessible.
    2.  At least one Major Header will need to be created. To ensure that all test results are displayed appropriately, it is important to work with Infection Control to ascertain if MRSA screens are performed for sites other than the Nares. In this display format, Minor headers will need to be created for each specimen type and test type to display all of the appropriate tests by specimen type (Nares, Perineum, Axilla, etc.) and to ensure the results are displayed legibly.
    3.  Only the Minor Headers show in the CPRS Cumulative View but they are grouped together by the Major Header.
    4.  Sample Major Header: SURVEILLANCE TESTING
    5.  Sample Minor Headers appear below:
        1.  MRSA Surveillance DNA Nares
        2.  MRSA Surveillance DNA Axilla
        3.  MRSA Surveillance DNA Perineum
        4.  MRSA Surveillance AGAR Nares
        5.  MRSA Surveillance AGAR Axilla
        6.  MRSA Surveillance AGAR Perineum

> etc.....

> *\*NOTE: In the Horizontal format the Major header does not need to be specific to DNA or Agar based CH-subscripted tests. A combined major header like the Surveillance Testing Header suggested can be created. However, for the Minor headers it is recommended that separate Minor headers be created for each SITE/SPECIMEN and TEST type (DNA and Agar based CH-subscripted test otherwise the results display will suffer in the horizontal format recommended.*

> NOTE: The previous laboratory test names can be updated for the new test names. However, certain cross-references need to be updated and there can be issues for data objects in CPRS; coordination is required. A new test should be created <u>only</u> if the original test and the new test are vastly different (i.e., methodology is different, new reference ranges that are clinically significant, etc.).

3.  Critical View Alert: A delta check can be created to provide a mechanism to alert providers if a patient is MRSA positive. When the test is resulted as POSITIVE it will set the flag to a CRITICAL high to generate a View Alert to the provider. The test must be set up as a Set of Codes with POSITIVE stands for POSITIVE to ensure consistency of reporting and flagging. If sites need to generate a Critical View Alert the following Delta Check can be created in File 62.1. It will then need to be added to the File 60 test set up in the Site/Specimen (field 100) multiple subfield 7, Type of Delta Check. This mechanism is case-sensitive so the Set of Codes (POSITIVE) and the Delta check (POSITIVE) should match if this specific coding is utilized.

> NAME: TEXT ALERT POS \*H

> XECUTABLE CODE: Q:\$D(LRGVP) I X\["POSITIVE" S LRFLG="H\*"

4.  Laboratory Management Index Program (LMIP): MRSA Surveillance testing is countable (billable) for the LMIP program. The National Laboratory Test (NLT) code chosen is based on the methodology used to perform the test at the site and must be marked billable in File 64 for workload recording purposes. Since method specific NLT codes are not available in File 64 for MRSA then the following NLT codes will need to be created by adding a method specific suffix from the WKLD Suffix codes file (File 64.2) to the WKLD Code file (File 64) NLT code, based on the methodology used to perform the test at the site. Create the suffixed workload code necessary using "Add a new WKLD code to file \[LRCAP CODE ADD\]". The recommended suffixed NLT codes for MRSA are as follows:
    1.  Staphylococcus Aureus Meth Resist~ORGANISM SPECIFIC CULTURE 87293.7059 for CH-subscripted “Agar” based culture tests.
    2.  Staphylococcus Aureus Meth Resist~PCR 87293.4451 for CH-subscripted “DNA” based tests.
    3.  For MI-Subscripted culture tests that have an MRSA organism identified and a sensitivity performed will require both the Etiology and Sensitivity LMIP NLT workload codes added to the Etiology Field organism entry: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) referred to in section a.ii MI-subscripted tests.

> ETIOLOGY WKLD CODE: Sensitivity Testing or MIC

> ETIOLOGY WKLD CODE \#: 87954.0000

> ETIOLOGY WKLD CODE: Bacti Organism ID

> ETIOLOGY WKLD CODE \#: 87570.0000

> *\*NOTE:* See example in Sectionf. Organisms in the Etiology Field File. These codes may need to be suffixed with the methodology used if applicable.

5.  Current Procedural Terminology (CPT): At this point in time, MRSA surveillance tests are not usually billable to a third party payer for reimbursement (versus a normal culture test or PCR test not used for MRSA surveillance which are billable). Therefore, these MRSA surveillance tests should not be passing CPT codes to the Patient Care Encounter (PCE) application.

> *\*NOTE: Refer to the Additional Notes section under LEDI and HDR for related information if your site sends this testing to a reference lab.*

6.  Organisms in the Etiology Field File: The following etiology will have to be added to the Etiology Field File (File 61.2), if this separate organism is not currently in the file. The following SNOMED CT code needs to be used when SNOMED CT coding is available in the VISTA system (Lab patches LA\*5.2\*68, LR\*5.2\*350, and LA\*5.2\*74).

NAME: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)SNOMED CODE: *(Local entry code in the format \###XXX where \### is the station ID and XXX is the next local code suffix available: example: 523001)*

GRAM STAIN: GRAM POSITIVE IDENTIFIER: BACTERIUM

ABBREVIATION: MRSA

\*SENSITIVITY DISPLAY

HEALTH DATA REPORT: YES

SNOMED CT ID: 115329001 *(Methicillin resistant Staphylococcus aureus (organism) specific SCT code)*

SCT CODE STATUS: PREFERRED TERM

SCT TOP CONCEPT: SCT Organism

Example:

> NAME: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)

> SNOMED CODE: 523700 GRAM STAIN: GRAM POSITIVE

> IDENTIFIER: BACTERIUM ABBREVIATION: MRSA

> HEALTH DEPT REPORT: YES

> SYNONYM: METHICILLIN RESISTANT STAPH AUREUS

> SYNONYM: MRSA

> ETIOLOGY WKLD CODE: Sensitivity Testing or MIC

> ETIOLOGY WKLD CODE \#: 87954.0000

> ETIOLOGY WKLD CODE: Bacti Organism ID

> ETIOLOGY WKLD CODE \#: 87570.0000

> SNOMED CT ID: 115329001

> SCT CODE STATUS: PREFERRED TERM

> SCT TOP CONCEPT: SCT Organism

> NOTE: Sites should not change the existing Etiology field entries <u>unless</u> the previous etiology and the new standardized etiology are synonymous. For example, a site used the etiology “Meth Res Staph Aureus” for positive MRSA. It would be appropriate to update the field entry to “STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)” since they are considered the same organism. Sites can add “Meth Res Staph Aureus” as a synonym for historical look back. This is only appropriate if the etiology previously used was to denote MRSA.

> If the site used the etiology “Staphylococcus Aureus” and set the Antimicrobial Susceptibility resistant to Oxacillin then it would not be appropriate to modify the existing Etiology field entry. Sites will have to add the etiology “STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)” to File 61.2

3.  Additional Notes for Sites:
    1.  Lab Electronic Data Interchange (LEDI) and Health Data Repository (HDR):

> Tests require National VA Lab codes for the HDR (the CH-subscripted tests need this information) and if LEDI is used by a site and they send their testing to another lab then the tests need National VA Lab codes as Order NLT codes and Result NLT codes as Result codes.  So there is an issue that it would be good to have National codes assigned to tests BUT the lab shouldn't pass CPT codes for surveillance issues.  Since the National VA Lab code field is one of the mechanisms the lab uses to pass CPT coding to PCE this needs to be considered. The way to handle this is to leave the field blank if LEDI is not an issue or have a generic NLT code that doesn’t carry any CPT code in it and/or remove the CPT code if one is there.  This is not a critical issue at this point as long as these tests are not passing CPT codes to billing. So sites may need to address this issue at some point for LEDI issues and HDR issues. This is more important in CH-subscripted tests at the moment but with LEDI IV (Patches LR\*5.2\*350 and LA\*5.2\*74) Micro tests will be passing info across LEDI so it will be more important in the near future.

2.  EPI, LOINC, and LEDI TOPOGRAPHY FILE 61 set-up issue:

> EPI, LOINC, and LEDI all use topography file information. The topography file entry is the SITE/SPECIMEN associated with a file 60 test. Two fields in the topography entries should be mapped to avoid errors for EPI and LEDI. LOINC mapping requires these as well, they are the HL7 CODE and the LEDI HL7 CODE fields in FILE 61. If the specimen code is missing in any topography reported in the EPI a W07 error is generated. These W07 errors usually occur in culture test site specimens that weren’t mapped. All possible topographies that could be used by a site for the MRSA testing should be mapped for these two fields. The following are examples of topographies that sites may use but this is applicable for ALL topographies that are used for any MI-Culture based tests or CH-subscripted tests that are captured in EPI, have LOINC codes, and/or are available for LEDI testing in a site. If “NARES” is not an option in the Topography file then the site will have to create a new entry for the SITE/SPECIMEN. See example below for new entries in the Topography file.

Examples:

> NAME: NARESSNOMED CODE: *(Local entry code in the format \###XXX where \### is the station ID and XXX is the next local code suffix available: example: 523001)*

> HL7 CODE: ORH LEDI HL7: Nose (nasal passage)

> SNOMED CT ID: 363538002

> SCT CODE STATUS: LOCAL

> SCT TOP CONCEPT: SCT Body Structure

NAME: AXILLA SNOMED CODE: Y8100

WEIGH: YES

HL7 CODE: ORH LEDI HL7: Other

SYNONYM: AXI

SNOMED CT ID: 34797008 SCT CODE STATUS: SYNONYM

SCT TOP CONCEPT: SCT Body Structure

NAME: PERINEUM SNOMED CODE: Y1700

HL7 CODE: ORH LEDI HL7: Other

SYNONYM: PERI

SNOMED CT ID: 38864007 SCT CODE STATUS: SYNONYM

SCT TOP CONCEPT: SCT Body Structure

<span id="AppF" class="anchor"></span>

APPENDIX D

# # Schedule TaskMan Tasks (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the clinical staff wants to schedule the Isolation Report and Nares Compliance List to automatically print to designated printers at specified times during the day, schedule these tasks in TaskMan.

#### Print Isolation Report (Tasked)

This option should *not* be run interactively. It should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options \[XUTM SCHEDULE\]. This option will print the Isolation Report at the times specified.

<span id="_Toc268767193" class="anchor"></span>Figure 9 – Print Isolation Report (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>"MMRS ISOLATION REPORT (TASKED)"</strong></p>
<p>Are you adding 'MMRS ISOLATION REPORT (TASKED)' as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED</p>
<p>Menu Text: Print Isolation Report (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: <strong>MAR 5,2009@15:50</strong></p>
<p>DEVICE FOR QUEUED JOB OUTPUT: <strong>IDM1$PRT LANDSCAPE;P-TCP LANDS</strong></p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule/Unschedule Options \[XUTM SCHEDULE\], several variables need to be setup on page 2 of the form.

- The Variable Name MMRSDIV should be added, and its value should be set to the IEN in File \#104 for the Division this option is being run for.
- If the option will print the report for all locations, then MMRSLOC should be added as a Variable Name and its Value should be set to "ALL" (The quotes need to be entered in the Value). If the option will only print for a few locations, then for each location that will be printed, a Variable Name should be added as follows: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File \#104.3), and its value should be set to "" (the two double quotes need to be entered for the Value; do not leave the Value blank).

Sample Screen shot on how to get the IEN for a Division. The number highlighted in yellow is the IEN.

<span id="_Toc268767194" class="anchor"></span>Figure 10 – Get MRSA Division IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA SITE PARAMETERS

Select MRSA SITE PARAMETERS DIVISION: XXXXX VAMC

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 1</span> DIVISION: XXXXX VAMC

RECEIVING UNIT SCREEN: YES DISCHARGING UNIT SCREEN: YES

SCREEN POS ON TRANSFER IN: YES SCREEN POS ON DISCHARGE: YES

Sample Screen shot on how to get the IEN for a Geographical Location. The number highlighted in yellow is the IEN.

<span id="_Toc268767195" class="anchor"></span>Figure 11 – Get Geographical Location IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA WARD MAPPINGS

Select MRSA WARD MAPPINGS NAME: 11AB

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 5</span> NAME: 11AB

DIVISION: XXXXX VAMC TYPE: ACUTE CARE

IPEC UNIT ID: 726

WARD LOCATION: 11AB

WARD LOCATION: 11ASURG

Sample screen shot for running the option for Division 1, and geographical locations 3 and 5:

<span id="_Toc268767196" class="anchor"></span>Figure 12 – Print Isolation Report (Tasked) (Division 1 & Geographical Locations 3 & 5)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Sample screen shot for running the option for Division 1 and all Geographical Locations:

<span id="_Toc268767197" class="anchor"></span>Figure 13 – Print Isolation Report (Tasked) (Division 1 & All Geographical Locations)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>­­­­­­­­­­­­­­­­­­­_________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-user-manual/010.png) | Tip: To schedule the option more than once (for example, if the site wants to schedule the report to print at different printers for different locations), put the option name in quotes. This will allow you to schedule the option more than once. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-user-manual/011.png) | Tip: When tasking options, ALL has to be in quotations (“ALL”). |
|----------------------------------------------------|---------------------------------------------------------------------|

#### Print Nares Screen Compliance List (Tasked)

This option should *not* be run interactively. It should only be scheduled by IRM staff to run via TaskMan using option 'Schedule/Unschedule Options' \[XUTM SCHEDULE\]. This option will print the Nares Compliance List at the times specified.

<span id="_Toc268767198" class="anchor"></span>Figure 14 – Print Nares Screen Compliance List (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>“MMRS NARES SWAB LIST (TASKED)”</strong></p>
<p>Are you adding ‘MMRS NARES SWAB LIST (TASKED)’ as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED</p>
<p>Menu Text: Print Nares Screen Compliance List (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: MAR 5,2009@15:50</p>
<p>DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule/Unschedule Options \[XUTM SCHEDULE\], several variables need to be setup on Page 2 of the form.

- The Variable Name MMRSDIV should be added, and its value should be set to the IEN in File \#104 for the Division this option is being run for.
- If the option will print the report for all locations, then MMRSLOC should be added as a Variable Name and its Value should be set to ALL. If the option will only print for a few locations, then for each location that will be printed, a Variable Name should be added as follows: MMRSLOC(LOCIEN) (where LOCIEN is the geographical unit IEN from File \#104.3) and its Value should be set to "" (the two double quotes need to be entered for the Value; do not leave the Value blank).

Sample screen shot for running the option for Division 1, and geographical locations 3 and 5.

<span id="_Toc268767199" class="anchor"></span>Figure 15 – Print Nares Swab List (Tasked) (Div 1 & Geographical Locations 3 & 5)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Sample screen shot for running the option for Division 1 and all Geographical Locations.

<span id="_Toc268767200" class="anchor"></span>Figure 16 – Print Nares Swab List (Tasked) (Div 1 & All Geographical Locations)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-user-manual/012.png) | Tip: To schedule the option more than once (for example, if the site wants to schedule the report to print at different printers for different locations), put the option name in quotes. This will allow you to schedule the option more than once. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-user-manual/013.png) | Tip: When tasking options, ALL has to be in quotations (“ALL”). |
|----------------------------------------------------|---------------------------------------------------------------------|

<span id="AppG" class="anchor"></span>

APPENDIX E

# # MAS Movements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For purposes of the MRSA Prevention Initiative, several [Medical Administration Service](#Glos_MAS) (MAS) Movement types were re-coded. This information did not change in the MAS file of the patient; it just changed the way MRSA-PT presents this information.

For example, a Specialty Transfer is a “transfer” movement, but the definition of this “movement” is that the patient did not leave his/her room. Rather, their status changed or they were assigned a new service. In these situations we would *exclude* these movements.

Or, consider patients who move between the [Community Living Center](#Glos_CLC) (CLC) and acute care. If a patient leaves the CLC and is admitted to the VA Hospital two movements are created: (1) Transfer and (2) Absent Sick in Hospital (ASIH). For MRSA-PT purposes, we would ignore the ASIH movement and code the Transfer as a Discharge. When the patient returns to the CLC, it is it is considered a transfer but for MRSA-PT purposes we consider it to be an Admission.

Table 10 below lists the MAS Movement Type; the original Transaction Type; whether or not the movement was *included* or *excluded* for MRSA-PT purposes; whether it was re-coded and if so the re-coded movement type; and a Description of each movement. The only exception to the list below is if a Discharge directly follows an Authorized Absence (for example, the patient never returned from AA and was therefore discharged). In such cases, the program will ignore the Discharge.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>NAME</th>
<th>TRANSACTION TYPE</th>
<th><p>INCLUDE/</p>
<p>EXCLUDE</p></th>
<th>CODE AS…</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AMBULATORY CARE (OPT-AC)</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Admission to the VA facility from the Ambulatory Care (A/C) rolls.</td>
</tr>
<tr class="even">
<td>DIRECT</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Direct admission to the VA facility for treatment.</td>
</tr>
<tr class="odd">
<td>NON-SERVICE CONNECTED (OPT-NSC)</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Admission for inpatient treatment from the facility OPT-NSC program.</td>
</tr>
<tr class="even">
<td>NON-VETERAN (OPT-NVE)</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Admission of a patient who is not a veteran applicant for inpatient treatment.</td>
</tr>
<tr class="odd">
<td>OPT-SC</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Admission for inpatient treatment from the facility OPT-SC program.</td>
</tr>
<tr class="even">
<td>PRE-BED CARE (OPT-PBC)</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td></td>
<td>Admission from the OPT-PBC program for inpatient treatment.</td>
</tr>
<tr class="odd">
<td>READMISSION TO IMLTC/NHCU/DOMICILIARY</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Readmission to NHCU or Domiciliary within 30 days of last discharge from NHCU/Domiciliary.</td>
</tr>
<tr class="even">
<td>TO ASIH</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>To the parent VA Hospital from the VANH or VAD in Absent Sick in Hospital (ASIH) status. Does not cause discharge from sending facility.</td>
</tr>
<tr class="odd">
<td>TRANSFER IN</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Transfer in (admission) from another VA facility to this VA facility.</td>
</tr>
<tr class="even">
<td>WAITING LIST</td>
<td>ADMISSION</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Admission type to be used when admitting a patient from a waiting list.</td>
</tr>
<tr class="odd">
<td>CHECK-IN LODGER</td>
<td>CHECK-IN LODGER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Check a lodger into the VA facility without impacting census data.</td>
</tr>
<tr class="even">
<td>CHECK-IN LODGER (OTHER FACILITY)</td>
<td>CHECK-IN LODGER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Check a lodger into a non-VA facility such as a local hotel.</td>
</tr>
<tr class="odd">
<td>CHECK-OUT LODGER</td>
<td>CHECK-OUT LODGER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Check a lodger out of lodger status from either VA or non-VA facility.</td>
</tr>
<tr class="even">
<td>CONTINUED ASIH (OTHER FACILITY)</td>
<td>DISCHARGE</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Discharge from the parent facility to ASIH in another VA (or non-VA) facility. Patient must have been sent to parent facility in ASIH status originally.</td>
</tr>
<tr class="odd">
<td>DEATH</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspicies. Autopsy was NOT accomplished.</td>
</tr>
<tr class="even">
<td>DEATH WITH AUTOPSY</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspices. Autopsy was accomplished.</td>
</tr>
<tr class="odd">
<td>DISCHARGE FROM IMLTC/NHCU/DOM WHILE ASIH</td>
<td>DISCHARGE</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>This movement type is used when discharging a patient from the NHCU/DOM ward prior to his hospital discharge and prior to 30 days. Use this type when it is evident that the patient will not return to the NHCU/DOM ward.</td>
</tr>
<tr class="even">
<td>DISCHARGE TO CNH</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge type for the AMIE package for use when discharging a patient to a community nursing home.</td>
</tr>
<tr class="odd">
<td>FROM ASIH</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge from VAH ASIH status with resumption of VANH/VAD episode of care.</td>
</tr>
<tr class="even">
<td>IRREGULAR</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge from inpatient treatment against medical advice.</td>
</tr>
<tr class="odd">
<td>NON-BED CARE</td>
<td>DISCHARGE</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Discharge from inpatient treatment to the NBC (Non-bed care) rolls.</td>
</tr>
<tr class="even">
<td>NON-SERVICE CONNECTED (OPT-NSC)</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge from inpatient treatment to the facility OPT-NSC rolls.</td>
</tr>
<tr class="odd">
<td>NON-VETERAN</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge of a patient from inpatient care who was treated in a status other than as a veteran.</td>
</tr>
<tr class="even">
<td>OPT-SC</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge from inpatient treatment to the OPT-SC rolls.</td>
</tr>
<tr class="odd">
<td>REGULAR</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Regular discharge from inpatient treatment.</td>
</tr>
<tr class="even">
<td>TO DOM FROM HOSP</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge type created for the AMIE package to be used when discharging a hospital patient for admission to a domiciliary ward.</td>
</tr>
<tr class="odd">
<td>TO IMLTC/NHCU FROM DOM</td>
<td>DISCHARGE</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Discharge type created for AMIE for use when discharging a patient from a dom ward for admission to a nursing home care unit.</td>
</tr>
<tr class="even">
<td>TO IMLTC/NHCU FROM HOSP</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge type created for the AMIE package used when discharging a hospital patient to the nursing home care unit.</td>
</tr>
<tr class="odd">
<td>TRANSFER OUT</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Transfer out (discharge) to another VA facility from this VA facility.</td>
</tr>
<tr class="even">
<td>VA IMLTC/NHCU TO CNH</td>
<td>DISCHARGE</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Discharge type added for the AMIE package to be used when discharging a patient from a VA nursing home care unit to a community nursing home.</td>
</tr>
<tr class="odd">
<td>WHILE ASIH</td>
<td>DISCHARGE</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Discharge from VAD/VANH while in an ASIH status at other facility either by termination of inpatient care or exceeding the 30-day ASIH period.</td>
</tr>
<tr class="even">
<td>PROVIDER/SPECIALTY CHANGE</td>
<td>SPECIALTY TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Change of provider and/or treating specialty without any other change in status, <em>i.e.</em>, ward, room remain same as prior to change.</td>
</tr>
<tr class="odd">
<td>AUTH ABSENCE 96 HOURS OR LESS</td>
<td>TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Transfer to a absence (pass) of 96 hours or less.</td>
</tr>
<tr class="even">
<td>AUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>To an authorized absence status of more than 96 hours but not greater than 7 days for hospital or 30 days for NHCU/Domiciliary.</td>
</tr>
<tr class="odd">
<td>CHANGE ASIH LOCATION (OTHER FACILITY)</td>
<td>TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Continuation of ASIH status but to another VA or Non-VA facility at VA expense. [Previously called CONTINUED ASIH (OTHER FACILITY)]</td>
</tr>
<tr class="even">
<td>FROM ASIH (VAH)</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Return to NHCU or Domiciliary within the 30 day timeframe from Absence Sick in Hospital status.</td>
</tr>
<tr class="odd">
<td>FROM AUTH. ABSENCE OF 96 HOURS OR LESS</td>
<td>TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Return from a pass status which didn't exceed 96 hours in duration.</td>
</tr>
<tr class="even">
<td>FROM AUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Return from authorized absence which was scheduled for greater than 96 hours.</td>
</tr>
<tr class="odd">
<td>FROM AUTHORIZED TO UNAUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Transfer from an authorized absence status to an unauthorized absence status.</td>
</tr>
<tr class="even">
<td>FROM UNAUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Return from an unauthorized absence status within the 30 day limit (hospital) or 90 day limit (NHCU/Domiciliary).</td>
</tr>
<tr class="odd">
<td>FROM UNAUTHORIZED TO AUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>EXCLUDE</strong></td>
<td></td>
<td>Transfer from unauthorized absence to authorized absence status.</td>
</tr>
<tr class="even">
<td>INTERWARD TRANSFER</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>TRANSFER</td>
<td>Transfer from one ward location in the VA facility to another.</td>
</tr>
<tr class="odd">
<td>RESUME ASIH IN PARENT FACILITY</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>ADMISSION</td>
<td>Return to the parent VAH to continue ASIH status after being ASIH in another VA or non-VA facility. [Previously called CONTINUED ASIH]</td>
</tr>
<tr class="even">
<td>TO ASIH (OTHER FACILITY)</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>To Absent Sick in Hospital Status (ASIH) to somewhere other than the parent VA Hospital.</td>
</tr>
<tr class="odd">
<td>TO ASIH (VAH)</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>Transfer from NHCU/Domiciliary to VA hospital for further care in Absent Sick in Hospital status. Can't exceed 30 days in duration.</td>
</tr>
<tr class="even">
<td>UNAUTHORIZED ABSENCE</td>
<td>TRANSFER</td>
<td><strong>INCLUDE</strong></td>
<td>DISCHARGE</td>
<td>To an unauthorized absence status of not more than 30 days for hospital or 90 days for NHCU/Domiciliary.</td>
</tr>
</tbody>
</table>

<span id="_Toc232405454" class="anchor"></span>GLOSSARY

[![](mrsa-program-tools-version-1-user-manual/014.png)](\l) [![](mrsa-program-tools-version-1-user-manual/015.png)](#G_B) [![](mrsa-program-tools-version-1-user-manual/016.png)](#G_C) [![](mrsa-program-tools-version-1-user-manual/017.png)](#G_D) [![](mrsa-program-tools-version-1-user-manual/018.png)](#G_E) [![](mrsa-program-tools-version-1-user-manual/019.png)](#G_F) [![](mrsa-program-tools-version-1-user-manual/020.png)](#G_G) [![](mrsa-program-tools-version-1-user-manual/021.png)](#G_I) [![](mrsa-program-tools-version-1-user-manual/022.png)](#G_K) [![](mrsa-program-tools-version-1-user-manual/023.png)](#G_L) [![](mrsa-program-tools-version-1-user-manual/024.png)](#G_M) [![](mrsa-program-tools-version-1-user-manual/025.png)](#G_N) [![](mrsa-program-tools-version-1-user-manual/026.png)](#G_P) [![](mrsa-program-tools-version-1-user-manual/027.png)](#G_S) [![](mrsa-program-tools-version-1-user-manual/028.png)](#G_T) [![](mrsa-program-tools-version-1-user-manual/029.png)](#G_V) [![](mrsa-program-tools-version-1-user-manual/030.png)](#G_W)

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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/031.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/032.png)</a></td>
</tr>
<tr class="even">
<td>Begin Date/Time</td>
<td colspan="3">The date that the report is to start.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_C" class="anchor"></span><strong>C</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/033.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/034.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/035.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/036.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/037.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/038.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/039.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/040.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/041.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/042.png)</a></td>
</tr>
<tr class="even">
<td>Namespace</td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/043.png)</a></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td colspan="3">A specific type of <a href="#Glos_MailMan">MailMan</a> message used to distribute <a href="#Glos_KIDS">KIDS</a> builds.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_S" class="anchor"></span><strong>S</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/044.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/045.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/046.png)</a></td>
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
<td><a href="#G_Top">![](mrsa-program-tools-version-1-user-manual/047.png)</a></td>
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