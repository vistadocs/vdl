---
title: PIMS Version 5.3 User Manual - PTF Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: PTF Menu
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
menu_options: 2
description: 
audience: 
keywords: 
  - patient
  - date
  - record
  - report
  - census
  - table
  - admission
  - contents
  - records
  - number
page_count: 0
word_count: 30471
section_count: 67
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_ptf.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_ptf.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

---
title: <span id="_Toc423443133" class="anchor"></span>PIMS V. 5.3 ADT Module User Manual
---

Patient Treatment File (PTF) PTF Menu

![](pims-version-5-3-user-manual-ptf-menu/001.png)

November 2025

Office of Information and Technology (OIT)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table 1: Screen “101” Data Fields</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 53%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description (Patch # if applic.)</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2025</td>
<td>DG*5.3*1117 – minor updates to verbiage in sections 7.1.1, 7.1.2, and 7.3 for COMPACT Act. Updated cover page and footers.</td>
<td>Booz Allen Hamilton</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2024</td>
<td><p>DG*5.3*1104 – The following sections were updated:</p>
<ul>
<li><p><strong>7.1.2</strong> Acute Suicidal Crisis Status (New)</p></li>
<li><p><strong>7.3</strong> Data Screen 501</p></li>
<li><p><strong>7.9.5</strong> Display Start date, Number of remaining days and End date from Data Screen 501</p></li>
<li><p><strong>13.7</strong> Updated field name and title of prompt.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>12/2023</td>
<td><p>DG*5.3*1095 - The following sections were added:</p>
<ul>
<li><p><strong>7.1.1</strong> COMPACT Act Eligibility Status</p></li>
</ul>
<p>The following sections were updated:</p>
<ul>
<li><p><strong>7.9.1</strong> Editing Leave and Pass Days</p></li>
<li><p><strong>7.9.2</strong> Error Messages</p></li>
<li><p><strong>7.9.3</strong> Differences Between VA/Non-VA PTF</p></li>
<li><p><strong>7.9.4</strong> Edit Options</p></li>
<li><p><strong>7.9.5</strong> Load Edit PTF Data Screen 101</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/2021</td>
<td><p>DG*5.3*1057 – 72 HR and POA PTF updates. The following enhancements were included in the patch:</p>
<ul>
<li><p>Updates the Set Up Non-VA PTF record option and the Load/Edit PTF Data option to allow users to add Outpatient procedures that occur for a patient up to 72 hours prior to that patient's admission to the PTF record.</p></li>
<li><p>Allows users to enter an Initial Date of Service for Non-VA PTFs [DG PTF FEE BASIS ADD] up to 72 hours prior to an Inpatient Admission.</p></li>
<li><p>Updates the Present on Admission Indicator fields in PTF records [DG PTF FEE BASIS ADD] to allow the Exempt Value (1) to be entered for the Non-VA sites that are exempted by CMS from reporting Present on Admission information.</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/2016</td>
<td>DG*5.3*917 – Update to re-activate the Add/Edit Suffix Effective Date [DG PTF SUFFIX EFF DATE EDIT] option on p. 126.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/2015</td>
<td><p>Updates for DG*5.3*884, ICD-10 Patient Treatment File Modifications Project:</p>
<ul>
<li><p>Added Table of Contents and List of Figures.</p></li>
<li><p>Reformatted footers and page numbers.</p></li>
<li><p>Updated Overview, RELEASE CLOSED CENSUS RECORDS verbiage on p.3.</p></li>
<li><p>Added Present on Admission (POA) verbiage to Overview, EDIT IN PTF – ONLY AFFECTS PTF on p.10.</p></li>
<li><p>Added Census date verbiage to 101 SCREEN on pp.11 and 48.</p></li>
<li><p>Added POA verbiage and information on expanded number of ICD codes to Load/Edit PTF Data, MAS SCREEN (pp.12, 49), 501 SCREEN (pp.13, 49), 401 SCREEN (pp.13, 50), 601 SCREEN (pp.14, 50), and 701 SCREEN (pp.14, 52).</p></li>
<li><p>Updated 601-# PROCEDURE CODE and 701 SECONDARY DIAGNOSIS fields on pp.23, 63, 110, and 116.</p></li>
<li><p>Changed PTT mail group to PTI mail group on pp.35, 38, 120, and 121.</p></li>
<li><p>Updated 501-# ICD fields on pp.60 and 112.</p></li>
<li><p>Added examples to PTF Output Menu, Comprehensive Report by Admission on pp.74-76.</p></li>
<li><p>Added POA to DRG Information Report on p.78.</p></li>
<li><p>DRG Case Mix Summary can now go back 75 codes (p.79).</p></li>
<li><p>ALOS Report for DRGs can now go back 75 codes (p.81).</p></li>
<li><p>Batch Multiple DRG Reports can now go back 75 codes (p.83).</p></li>
<li><p>DRG Frequency Report can now go back 75 codes (p.86).</p></li>
<li><p>DRG Index Report can now go back 75 codes (p.87).</p></li>
<li><p>Trim Point DRG Report can now go back 75 codes (p.90).</p></li>
<li><p>Updated Quick Load/Edit PTF Data option, 401 and 601 Transactions on p.106.</p></li>
<li><p>Updated 401 OPERATION CODE field on p.114.</p></li>
</ul></td>
<td>REDACTED, VA PM</td>
<td><p>REDACTED</p>
<p>M.M.-G.</p></td>
</tr>
<tr class="odd">
<td>7/2014</td>
<td><p>DG*5.3*850 (ICD-10 implementation):</p>
<ul>
<li><blockquote>
<p>Added POA indicator to 701 screen, and text changed to indicate that DRG is stored in PTF.</p>
</blockquote></li>
<li><blockquote>
<p>Changed ICD-9 references throughout to “ICD.”</p>
</blockquote></li>
</ul>
<ul>
<li><p>501-# screen</p></li>
<li><p>701 screen</p></li>
<li><p>801 screen</p></li>
<li><p>501-# screen</p></li>
<li><p>701 screen</p></li>
<li><p>101 and 701 screens</p></li>
<li><p>501 screen</p></li>
</ul>
<ul>
<li><blockquote>
<p>DRG Calculation includes Present on Admission (POA) indicator if an ICD-10 diagnosis code was entered.</p>
</blockquote></li>
<li><blockquote>
<p>Added Diagnosis Codes and Operation/procedure Codes to list of items computed and displayed for DRG.</p>
</blockquote></li>
<li><blockquote>
<p>Added ICD9/10 search selection for Diagnostic Code PTF Record Search</p>
</blockquote></li>
<li><blockquote>
<p>Added Diagnosis Codes and Operation/procedure codes to list computed and displayed in the DRG Information Report.</p>
</blockquote></li>
<li><blockquote>
<p>Removed duplicate “Primary Diagnosis” field and added POA field to screens 101 and 701.</p>
</blockquote></li>
</ul></td>
<td><p>REDACTED, VA PM</p>
<p>REDACTED, ICD-10 PM</p></td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>3/30/09</td>
<td><p>DG*5.3*664 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<ul>
<li><blockquote>
<p>Change <em>environmental contaminants</em> to <em>SW Asia Conditions</em></p>
</blockquote></li>
<li><blockquote>
<p>Update following screens in load/edit options with Project 112/SHAD – MAS, 101, 501, 801</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/29/09</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/14/08</td>
<td>Minor Formatting Changes</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/6/07</td>
<td>DG*5.3*729 - PTF Fields No Longer Needed – enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/20/06</td>
<td>DG*5.3*702 - Edit Census Date Parameters option changed to display only</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/13/06</td>
<td><p>DG*5.3*683 - NHCU Treating Specialties</p>
<p>Update Open PTF Record Listing option</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/22/06</td>
<td><p>DG*5.3*687 Maintenance</p>
<p>Remove PTF Archive/Purge function</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/3/05</td>
<td><p>DG*5.3*635 Enhancements</p>
<p>PTF 801 screen updates</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Table 1: Screen “101” Data Fields

  
Table of Contents

<u>List of Figures</u>

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Overview](#overview)
  - [Census Menu](#census-menu)
  - [Supervisor Menu](#supervisor-menu)
  - [National Patient Care Database](#national-patient-care-database)
  - [PTF Output Menu](#ptf-output-menu)
  - [DRG Reports Menu](#drg-reports-menu)
  - [Update DRG Information Menu](#update-drg-information-menu)
  - [Utility Menu](#utility-menu)
  - [Uneditable Elements](#uneditable-elements)
- [Census Menu](#census-menu-1)
  - [Load/Edit PTF Data](#loadedit-ptf-data)
  - [Close Open Census Record](#close-open-census-record)
  - [Census Status Report](#census-status-report)
  - [Inquire Census Record](#inquire-census-record)
  - [Other Census Outputs](#other-census-outputs)
    - [Comprehensive Census Report](#comprehensive-census-report)
    - [Productivity Report by Clerk (Census Only)](#productivity-report-by-clerk-census-only)
    - [Records by Completion Status (Census Only)](#records-by-completion-status-census-only)
    - [Transmitted Census Records List](#transmitted-census-records-list)
    - [Unreleased Census Records Report](#unreleased-census-records-report)
  - [Release Closed Census Records](#release-closed-census-records)
  - [Transmit Census Records](#transmit-census-records)
  - [Open Closed Census Records](#open-closed-census-records)
  - [Open Released or Transmitted Census Records](#open-released-or-transmitted-census-records)
  - [099 Transmission for Census Record](#099-transmission-for-census-record)
  - [Supervisor Menu](#supervisor-menu-1)
    - [Display Census Date Parameters](#display-census-date-parameters)
    - [Regenerate Census Workfile](#regenerate-census-workfile)
  - [Fee Basis Census Status Report](#fee-basis-census-status-report)
- [Checkoff PTF Message](#checkoff-ptf-message)
- [DRG Calculation](#drg-calculation)
- [Enter PTF Message](#enter-ptf-message)
- [Inquire PTF Message](#inquire-ptf-message)
- [Load/Edit PTF Data](#loadedit-ptf-data-1)
  - ["101" SCREEN](#101-screen)
    - [COMPACT Act Administrative Eligibility Status](#compact-act-administrative-eligibility-status)
    - [Acute Suicidal Crisis Status](#acute-suicidal-crisis-status)
  - ["MAS" SCREEN](#mas-screen)
  - ["501" SCREEN](#501-screen)
  - ["401" SCREEN](#401-screen)
  - ["601" SCREEN](#601-screen)
  - ["MPCR" SCREEN](#mpcr-screen)
  - ["701" SCREEN](#701-screen)
  - ["801" SCREEN](#801-screen)
  - [Close Out](#close-out)
    - [Editing Leave and Pass Days](#editing-leave-and-pass-days)
    - [Error Messages](#error-messages)
    - [Differences between VA/Non-VA PTF](#differences-between-vanon-va-ptf)
    - [Edit Options](#edit-options)
    - [Data Fields](#data-fields)
- [National Patient Care Database](#national-patient-care-database-1)
  - [Transmission Reports](#transmission-reports)
    - [PIMS Events Transmitted Yesterday](#pims-events-transmitted-yesterday)
  - [Transmission Utilities](#transmission-utilities)
    - [Retransmit Patient Demographics](#retransmit-patient-demographics)
    - [Retransmit Admission Data](#retransmit-admission-data)
    - [Retransmit Entry in ADT/HL7 PIVOT File](#retransmit-entry-in-adthl7-pivot-file)
- [Open Closed PTF Record](#open-closed-ptf-record)
- [Open Released or Transmitted PTF Records](#open-released-or-transmitted-ptf-records)
- [PTF Output Menu](#ptf-output-menu-1)
  - [Admissions without an Associated PTF Record](#admissions-without-an-associated-ptf-record)
  - [Comprehensive Report by Admission](#comprehensive-report-by-admission)
  - [Diagnostic Code PTF Record Search](#diagnostic-code-ptf-record-search)
  - [DRG Information Report](#drg-information-report)
  - [DRG Reports Menu](#drg-reports-menu-1)
    - [DRG Case Mix Summary](#drg-case-mix-summary)
    - [ALOS Report for DRGs](#alos-report-for-drgs)
    - [Batch Multiple DRG Reports](#batch-multiple-drg-reports)
    - [Batch Multiple DRG Reports](#batch-multiple-drg-reports-1)
    - [DRG Frequency Report](#drg-frequency-report)
    - [DRG Frequency Report](#drg-frequency-report-1)
    - [DRG Index Report](#drg-index-report)
    - [Trim Point DRG Report](#trim-point-drg-report)
  - [Inquire PTF Record](#inquire-ptf-record)
  - [Listing of Records by Completion Status](#listing-of-records-by-completion-status)
  - [Means Test Indicator of 'U' Report](#means-test-indicator-of-u-report)
  - [MPCR Inquiry](#mpcr-inquiry)
  - [Open PTF Record Listing](#open-ptf-record-listing)
  - [Patient Summary by Admission](#patient-summary-by-admission)
  - [Pro Fees Not Sent to PCE](#pro-fees-not-sent-to-pce)
  - [Productivity Report by Clerk](#productivity-report-by-clerk)
  - [Surgical Code PTF Record Search](#surgical-code-ptf-record-search)
  - [Transmitted Records List](#transmitted-records-list)
  - [Unreleased PTF Record Output](#unreleased-ptf-record-output)
- [PTF Transmission](#ptf-transmission)
- [Quick Load/Edit PTF Data](#quick-loadedit-ptf-data)
  - ["101" and "701" Transactions](#101-and-701-transactions)
  - ["501" Transaction](#501-transaction)
  - ["401" Transaction](#401-transaction)
  - ["801" Transaction](#801-transaction)
  - ["601" Transaction](#601-transaction)
  - [Diference between VA PTF and Non-VA PTF](#diference-between-va-ptf-and-non-va-ptf)
    - [Admission Records](#admission-records)
    - [Automatic Updating](#automatic-updating)
    - [Discharge Information](#discharge-information)
  - [Select 401 Surgery Date](#select-401-surgery-date)
- [Release PTF Records for Transmission](#release-ptf-records-for-transmission)
- [Set Up Non-VA PTF Record](#set-up-non-va-ptf-record)
- [Update DRG Information Menu](#update-drg-information-menu-1)
  - [Update Transfer DRGs for Current FY](#update-transfer-drgs-for-current-fy)
- [Utility Menu](#utility-menu-1)
  - [099 Transmission](#099-transmission)
  - [Record Print-Out (RPO)](#record-print-out-rpo)
  - [Add/Edit Suffix Effective Date](#addedit-suffix-effective-date)
  - [Delete PTF Record](#delete-ptf-record)
  - [Establish PTF Record from Past Admission](#establish-ptf-record-from-past-admission)
  - [Print Special Transaction Request Log](#print-special-transaction-request-log)
  - [PTF Expanded Code Listing](#ptf-expanded-code-listing)
  - [Purge Special Transaction Request Log](#purge-special-transaction-request-log)
  - [Set Transmit Flag on Movements](#set-transmit-flag-on-movements)
  - [Validity Check of PTF Record](#validity-check-of-ptf-record)
Patient Treatment File (PTF) is a record which is kept on all patients who receive inpatient care in a VA medical care facility or who receive inpatient care in a non-VA medical care facility at VA expense. Every VA inpatient admission generates a PTF record in the computer. Non-VA admissions at VA expense should have a PTF record created using the Set Up Non-VA PTF Record option.
The PTF provides a record of inpatient activity, diagnoses, procedures, and surgeries performed from the time of admission to the time of discharge from inpatient care. The PTF options provide functions to enter and edit this data in the Patient Treatment File.
A PTF record is automatically created for a patient when a patient admission is entered into the system. The PTF initially consists of patient demographic data from the main PATIENT file and admission information.
During certain ADT processes, the PTF record is automatically updated to match the inpatient Bed Control record. The user will be informed when the PTF record is being updated through a message displayed on the screen.
After patient discharge, the PTF record should be completed and closed. The data from the closed PTF is sent to the Austin Information Technology Center (AITC), which uses the data to compute the Diagnostic Related Groups for resource allocation to the hospital.
A census record will be required for all active admissions as of 11:59 p.m. on a specific date as established by HHAS (Headquarters Health Administration Service), VA Central Office. A census record is created when the PTF is closed for census purposes. Until the census record is created, the PTF record is displayed/printed when using the census options. Non-VA hospital and community nursing home data is now included in the census report that is transmitted to AITC; however, state home facility and 1-day stay dialysis patient data will continue to be excluded.
The following is a brief description of the major function of each PTF option.

## Census Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LOAD/EDIT PTF DATA

> This option is used to enter, edit, and view data contained in the PTF for a patient's period of hospitalization and to close and release these records for transmission. The load/edit function provided in the Census Menu is intended for census purposes only.

CLOSE OPEN CENSUS RECORD

> This option provides you with a quick, easy means of closing PTF records for census purposes. PTF records can also be closed through the Load/Edit PTF Data option.

CENSUS STATUS REPORT

> This option allows you to print a report of all active admissions as of a specified census date. The first time the Census Status Report is run for a particular census date, a Census Workfile is created for that date.

INQUIRE CENSUS RECORD

> This option is used to view the information contained in one or several patients' census record(s).

OTHER CENSUS OUTPUTS

COMPREHENSIVE CENSUS REPORT

> This option provides a way to view the information contained in the census records in the PTF screen format.

PRODUCTIVITY REPORT BY CLERK (CENSUS ONLY)

> This option provides a report of the census records processed by each coding clerk. The report pertains only to those records which have a status of closed or released.

RECORDS BY COMPLETION STATUS (CENSUS ONLY)

> This option produces a census coding report by completion status - closed, released or transmitted. Records in an open status are not included.

TRANSMITTED CENSUS RECORDS LIST

> This option is used to obtain a list of all transmitted records for a specified date range.

UNRELEASED CENSUS RECORDS REPORT

> This option provides a listing of census records with a status of CLOSED. These records have not been released for transmission to Austin.

RELEASE CLOSED CENSUS RECORDS

> This option allows you to release closed census records for future transmission. Once the record has been released, it is ready for transmission to the Austin Information Technology Center (AITC) through the Transmit Census Records option.

TRANSMIT CENSUS RECORDS

> This option is used to transmit released census records to the Austin Information Technology Center (AITC). Only holders of the security key DG PTFTRANS may access this option.

OPEN CLOSED CENSUS RECORDS

> This option is used to reactivate census records that have been closed but not released or transmitted.

OPEN RELEASED OR TRANSMITTED CENSUS RECORDS

> This option is used to reopen released (record has been closed and is awaiting transmission) or transmitted (record has been transmitted to Austin, TX) census records for the purpose of changing or correcting the record.

099 TRANSMISSION FOR CENSUS RECORD

> This option is used to delete the master record (for census purposes) at the Austin Information Technology Center (AITC) by electronically transmitting a 099 record. For non-free form transmissions, use of this option deletes the entire master record (for census purposes) in Austin and changes the census status of the record at the local facility from transmitted to open.

## Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY CENSUS DATE PARAMETERS

> This option allows the supervisor to view census date and parameters.

REGENERATE CENSUS WORKFILE

> This option allows the supervisor to regenerate the Census Workfile entries for a particular census date.

FEE BASIS CENSUS STATUS REPORT

> The Fee Basis Census Status Report option is used to generate the PTF Census Status Report for census records with a type of FEE BASIS.

CHECKOFF PTF MESSAGE

> This option is used to delete PTF messages from the PTF MESSAGE file. Before a PTF record can be closed, all PTF messages for the patient admission must be deleted.

DRG CALCULATION

> This option computes the Diagnostic Related Group based on diagnoses and procedures/operations.

ENTER PTF MESSAGE

> This option is used to enter and transmit PTF messages to the HIMS printer. PTF messages are stored in the PTF MESSAGE file.

INQUIRE PTF MESSAGE

> This option is used to display PTF messages.

LOAD/EDIT PTF DATA

> This option is used to enter/edit data to the open PTF record using screen entry format.

## National Patient Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TRANSMISSION REPORTS

PIMS EVENTS TRANSMITTED YESTERDAY

This option is used to generate a report of all PIMS events that were transmitted to the National Patient Care Database yesterday.

PIMS EVENTS TRANSMITTED FOR DATE RANGE

This option is used to generate a report of all PIMS events that were transmitted to the National Patient Care Database for a selected date range.

TRANSMISSION UTILITIES

RETRANSMIT PATIENT DEMOGRAPHICS

This option is used to retransmit demographic data for a selected patient.

RETRANSMIT ADMISSION DATA

This option is used to retransmit admission data/history for a selected patient and admission.

RETRANSMIT ENTRY IN ADT/HL7 PIVOT FILE

This option is used to retransmit an entry in the ADT/HL7 PIVOT file (#391.71).

OPEN CLOSED PTF RECORD

This option is available to holders of the DG PTFREL security key to reopen a closed PTF record.

OPEN RELEASED OR TRANSMITTED PTF RECORDS

This option is used to reopen released or transmitted PTF records. Security key DG PTFTRANS is required to utilize this option.

## PTF Output Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADMISSIONS WITHOUT AN ASSOCIATED PTF RECORD

This option provides a listing of admission records from Bed Control that have no corresponding PTF record.

COMPREHENSIVE REPORT BY ADMISSION

This option provides a way to view the information contained in the PTF records in screen format.

DIAGNOSTIC CODE PTF RECORD SEARCH

This option is used to search for occurrences of specified diagnostic codes in the PTF records. Security key DG PTFSUP is required.

DRG INFORMATION REPORT

This option is used to generate a report displaying the DRG based on a patient's diagnoses and any operations/procedures performed. The DRG is calculated for each entered diagnosis code.

## DRG Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DRG CASE MIX SUMMARY

This option provides a report that groups the DRGs by Service, Specialty, and Provider and calculates the average weight for each grouping.

ALOS REPORT FOR DRGS

This option provides a listing of DRG totals by average length of stay.

BATCH MULTIPLE DRG REPORTS

This option allows the user to batch process the following DRG Reports: Trim Point Report, DRG Frequency Report, Breakeven by DRG Report, and ALOS for DRGs.

DRG FREQUENCY REPORT

This option shows the frequency with which patients are grouped into various DRGs.

DRG INDEX REPORT

This option allows the user to generate a report which sorts and lists patient names according to their DRG.

TRIM POINT DRG REPORT

This option provides a listing of DRG totals by trim points - below trim, within trim, and above trim.

INQUIRE PTF RECORD

This option is used to view the information contained in a patient's PTF records.

LISTING OF RECORDS BY COMPLETION STATUS

This option produces a report of PTF records by completion status - closed, released, or transmitted.

MEANS TEST INDICATOR OF 'U' REPORT

This option is used to list PTF records, within a specified date range, for which the Means Test has not been done or has not been completed.

MPCR INQUIRY

This option allows you to view the Monthly Program Cost Report (MPCR) information related to a particular PTF record. The information displayed is the same as that shown on the MPCR Screen of the Load/Edit PTF Record option.

OPEN PTF RECORD LISTING

This option provides a list of PTF records with an open status for discharged patients.

PATIENT SUMMARY BY ADMISSION

This option is used to generate a list of a patient's movements, surgeries, and procedures for a selected admission from the PTF record.

PRO FEE CODING NOT SENT TO PCE

This option provides a report of inpatient professional records (801) that have not been transmitted to PCE for the specified date range.

PRODUCTIVITY REPORT BY CLERK

This option provides a report of the PTF records processed by each coding clerk. Security key DG PTFSUP is required.

SURGICAL CODE PTF RECORD SEARCH

This option is used to search for occurrences of specified surgical codes in the PTF records. Security key DG PTFSUP is required for access to this option.

TRANSMITTED RECORDS LIST

This option is used to obtain a list, in social security number order, of all transmitted records for a specified date range.

UNRELEASED PTF RECORD OUTPUT

This option provides a listing of PTF records with the status of closed.

PTF TRANSMISSION

This option is used to electronically transmit released PTF records to the Austin Information Technology Center (AITC). Security key DG PTFTRANS is required to utilize this option.

QUICK LOAD/EDIT PTF DATA

This option is used to enter/edit data to the open PTF record using list format, rather than screen format, which allows for faster editing.

RELEASE PTF RECORDS FOR TRANSMISSION

This option is used to update the status of PTF records which have been closed by Health Information Management Section to released status. Security key DG PTFREL is required to utilize this option.

SET UP NON-VA PTF RECORD

This option creates PTF records for veterans being treated in a private facility at VA expense.

## Update DRG Information Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UPDATE TRANSFER DRGS FOR CURRENT FY

This option is used to update/recalculate the Transfer DRGs for all PTF records that were active anytime in the current fiscal year.

## Utility Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

099 TRANSMISSION

This option is used to delete the master record in the Austin Information Technology Center (AITC) by transmitting a 099 deletion transaction. This option is only available to holders of the DG PTFTRANS security key.

RECORD PRINT-OUT (RPO)

This option is used to generate a record print-out request to the Austin Information Technology Center (AITC).

ADD/EDIT SUFFIX EFFECTIVE DATE

This option is used to add/edit/delete the EFFECTVE DATE multiple of the FACILITY SUFFIX file (#45.68).

DELETE PTF RECORD

This option is used to delete PTF records from the system. This option is only available to holders of the DG PTFREL security key.

ESTABLISH PTF RECORD FROM PAST ADMISSION

This option is used to create a PTF record for an admission that does not have a corresponding PTF record. This may occur if the patient was admitted before ADT V. 3.21, if the PTF record had been deleted, or the record was not set up on admission.

PRINT SPECIAL TRANSACTION REQUEST LOG

This option allows the user to generate a listing of special transaction requests.

PTF EXPANDED CODE LISTING

This option will generate a listing of the expanded codes by category and ICD code.

PURGE SPECIAL TRANSACTION REQUEST LOG

This option allows the user to purge special transaction requests.

SET TRANSMIT FLAG ON MOVEMENTS

This option allows the supervisor to flag 501 or 535 movements for transmittal purposes. If a PTF record has more than twenty-five 501 or 535 movements (a limitation set by Austin), the record cannot be closed or transmitted.

VALIDITY CHECK OF PTF RECORD

This option performs a validity check on all required fields of the PTF record.

## Uneditable Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information provided below shows different data elements which can/cannot be edited in PTF and, when entered/edited, which data is transferred to ADT or other VistA applications.

- CANNOT EDIT IN PTF - MUST EDIT THRU ADT

Name, SSN, Admission Date, Discharge Date, Means Test Indicator, Discharge Status, Income, Service Connection Percentage, Period of Service

- CAN EDIT IN PTF - TRANSFERS TO ADT

Vietnam/Agent Orange, POW, Ionizing Radiation, Marital Status, Bed Section/Treating Specialties, Spinal Cord Injury, Movement Dates, Race, Sex, State, Zip, County, Date of Birth

- EDIT IN PTF - DOES NOT TRANSFER TO ADT

Leave and Pass Days, ASIH Days

- EDIT IN PTF - TRANSFERS TO PCE

All Inpatient Professional Services (801)

- EDIT IN PTF - ONLY AFFECTS PTF

Facility & Suffix, Source of Admission, Principal Diagnosis, Source of Payment, Transferring Facility, Place of Disposition, Receiving Facility, Outpatient Treatment, VA Auspices, Compensation & Pension, Diagnostic ICD codes and Present on Admission (POA) indicators, All 401s and 601s, Expanded PTF Questions, 501 - Treated for SC Conditions

# Census Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Load/Edit PTF Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Load/Edit PTF Data option is used to enter, edit, and view data contained in the PTF for a patient's period of hospitalization and to close and release these records for transmission. The Load/Edit PTF Data option under the Census Menu is intended for census purposes. Unless you are using this option for census purposes, please use the Load/Edit PTF Data option under the PTF Menu.

After selecting the patient name and admission date or PTF number at the start of this option, the system updates the patient's PTF. During this updating process, some PTF information is being filled in from the patient's record in the PATIENT file and from the patient's Bed Control information which corresponds to the admission date selected. This data should be verified and/or edited through the Extended Bed Control option.

The PTF data is arranged so that it may be viewed and edited through various screens.

For easy viewing of the screens, this option allows you to "jump" from one screen display to another by entering an up-arrow \<^\> and the desired screen name. On some screens, data is grouped into sections for editing. Each section is labeled with a number to the left of the data items in reverse video. The patient's name, social security number, date of admission and the screen number appear at the top of every screen.

"101" SCREEN

The first screen that will appear is the "101" screen. This screen may contain admission and discharge information for the episode of care, basic patient demographic information, and the CENSUS STATUS. Much of this screen is automatically filled in from data in the PATIENT file, and the corresponding admission record in the PATIENT file. Choose the number(s) to the left of the group of data items you wish to edit. You will be prompted to indicate if treatment was related to MST only if the patient’s MST Status is YES. The 101 screen will display country, province, and postal code in place of state, county, and zip code if the patient has a foreign address. The Census date will display at the top of the screen on the right side if displaying a Census record.

"MAS" SCREEN

The "MAS" screen contains patient diagnoses, Present on Admission (POA) indicators, and information about patient movement(s), surgery(s), procedure(s) and inpatient CPT record data such as CPT record date and time, provider information, rendering location, CPT/HCPCS, modifiers, quantity, and up to 8 diagnosis codes per CPT’/HCPS. For each diagnosis code entered, PTF also tracks the following conditions: SC (service connected), AO (agent orange), IR (ionizing radiation), SWAC (SW Asia Conditions), MST (military sexual trauma), and HNC (head/neck cancer).

Information for surgical episode(s) and procedure(s) must be filled in through PTF as Bed Control does not track information for these episodes. Many different actions are available to enter/edit the patient movements, surgery episodes, procedures, and inpatient CPT records. These are displayed at the bottom of the "MAS" screen.

Some patient movement information is filled in from the admission record including losing specialty (the specialty from which the patient is transferring). Patient movements of less than 24 hours and transfers that only involve a facility treating specialty change and not a PTF specialty change will not create a new patient movement in PTF.

It should be noted that 401P transactions (which are valid only for admissions prior to 10/1/87) allow up to five procedure codes per admission and are not stored by date. 601 transactions allow up to twenty-five codes per procedure date. To add/delete a procedure code for a 601 transaction, select "E". 801 transactions allow more than one CPT record date and time per day. The CPT record date and time value must have a date and time value between the date and time of admission and the date and time of discharge. Each CPT record must have a rendering provider and at least one CPT code. Each CPT code must have at least one (up to 8) associated diagnosis. For each associated diagnosis, PTF also tracks service connection, agent orange, ionizing radiation, SW Asia conditions, military sexual trauma, and head/neck cancer conditions if the patient is registered with these conditions in Registration. To add a CPT record, select “I”.

"501" SCREEN

The "501" screen(s) contains information about the patient movement(s) listed on the "MAS" screen including the patient discharge movement. Because a "501" screen is generated for every patient movement which involves a specialty change, there may be more than one "501" screen. The screens are numbered as follows: 501-1, 501-2, 501-3, etc. Since the discharge movement is displayed on this screen every PTF will have at least one "501" screen. (See Note \#1 at the end of this option documentation for important information regarding editing leave and pass days.)

Each movement may contain up to 25 diagnosis codes with associated Present on Admission indicators. A maximum of 25 movements may be transmitted. If this limit is exceeded, the system will warn the user. The Set Transmit Flag on Movements option will allow the supervisor to choose which movement(s) to delete from the transmission.

If a TRANSFER DRG can be computed for a movement, it will be displayed on the applicable "501" screen. TRANSFER DRGs are generated based on codes entered when a movement between Services has occurred AND a change in the DRG has occurred. Applicable Services are Surgery, Neurology, Rehab. Medicine, Psychiatry, and Medicine. Other Services (pass through) are not applicable to TRANSFER DRGs. TRANSFER DRGs are stored in the PTF file and are used as a basis for the DRG reports. After editing, the “501-#” screen is redisplayed with the new values. However, due to the processing time involved, TRANSFER DRGs are not updated after editing the “501” screen. They will be updated the next time the PTF is load/edited when you see the message, “Updating PTF record \#” or upon exiting the option when you see the message, “Updating TRANSFER DRGs.”

"401" SCREEN

The "401" screen(s) contains information for any surgical episode(s) listed on the "MAS" screen. Because there is a “401” screen for every date a surgical episode occurred, there may be more than one "401" screen. However, if there were 2 surgical episodes on the same date, they will appear on different "401" screens. The screens are numbered as follows: 401-1, 401-2, 401-3, etc. You may enter up to twenty-five operation codes per surgical episode. After 10-1-87, 3 surgical episodes per date are allowed. Prior to that date, only 2 episodes per date were allowed. If no surgical episodes were performed during the inpatient stay, a "401" screen will not exist for that PTF.

"601" SCREEN

The "601" screen(s) contains information for any procedures performed. Because there is a "601" screen for every date a procedure occurred during the hospitalization, there may be more than one "601" screen. The screens are numbered as follows: 601-1, 601-2, 601-3, etc. You may enter up to twenty-five procedures per Non-OR procedure date. If no procedures were performed during the inpatient stay, a "601" screen will not exist for that PTF. If receiving dialysis, data pertaining to the number of treatments per procedure date will be contained in this transaction.

"MPCR" SCREEN

The "MPCR" screen contains information for those patient movements affecting the Monthly Program Cost Report. It contains information regarding those interward transfer movements that change the ward MPCR for the patient but the treating specialty remains the same. The screen is for viewing only with no editing allowed. The data displayed is compiled from activities made through the Bed Control options. The MPCR information will begin with the first 501 or 535 movement to occur after 10/1/90.

"701" SCREEN

The user chooses the principal diagnosis (the diagnosis responsible for the major length of stay) through the "701" screen. The 702 and 703 segments contain diagnoses 2-10 if ICD-9 and diagnoses 2-24 if ICD-10, which are also entered through the "701" screen. For ICD-10 codes, the user is prompted to indicate whether or not the condition was Present on Admission (POA). Once this is entered, the system calculates and displays the DRG based on the principal diagnosis and diagnosis codes 2-10 if ICD-9, or based on the principal diagnosis and diagnosis codes 2-24 from the 702-703 segments if ICD-10, and operations/procedures from the 401 and 601 segments. The DRG on the "701" screen is stored in the PTF.

The "701" screen is also where the PTF or census record can be closed, released, or reopened. A census record is created when the PTF record is successfully closed for census purposes.

If the PTF requires a census record, the record must be closed for census purposes before the PTF record can be closed. If you attempt to close a PTF record (requiring a census record) that has not yet been closed for census purposes, the following message will appear, "Record \#{#} MUST be closed for CENSUS first" and you will be prompted to close the census record.

If you release a PTF record and the corresponding census record has not yet been released, the following message will appear, "Census Record \#{#} also needs to be 'released'" and you will be prompted to release the census record. Once a record has been released, it can only be reopened through either the Open Released or Transmitted Census Records option under the Census Menu or Open Released or Transmitted PTF Records option under the PTF Menu.

"801" SCREEN

The “801” screen(s) contains information for professional services administered during the inpatient stay. It contains information regarding CPT record date and time, provider information, rendering location, procedure (CPT-4) and diagnosis (ICD~~9~~) codes, modifiers, and quantity, as well as any service connection or environmental indicators. Because there is an “801” screen for every CPT record occurring during the hospitalization, there may be more than one “801” screen. The screens are numbered as follows: 801-1, 801-2, 801-3, etc. Each time an “801” screen is entered, the user is prompted to send the data to PCE. If the user chooses not to send the data, the data is sent at release of the PTF record. If no professional services were captured during the inpatient stay, an “801” screen will not exist for that patient

Some of the data items that can be found on the different PTF screens, with a brief description of each item, are provided at the end of this option documentation.

Four items which come from the admission record cannot be entered/edited through PTF: ADMISSION DATE, DISCHARGE DATE, DISCHARGE SPECIALTY, and TYPE OF DISPOSITION.

Four checks (edits) are performed on the record at the time of closing. The first review checks to see that facility number and discharge date are completed and that a DRG has been calculated. If you are closing the record for census purposes, a discharge date is not required.

Because the PTF cannot be closed if PTF messages are remaining, the second review checks to see that all PTF messages are cleared. The user is given the opportunity to delete any PTF messages remaining at this time. This check is not performed if you are closing the record for census purposes only.

Thirdly, the PTF is checked to see that required fields are completed and that numeric fields do not have non-numeric characters and vice versa. Any erroneous fields are listed and the user is given the opportunity to enter the correct value for the field. The PERIOD OF SERVICE field may not be edited through PTF. If this field is in error, it will be listed, but must be edited through the Load/Edit Patient Data option in Registration.

Lastly, the record is checked for inconsistent data fields.

Each edit is not applied until the record has passed all preceding edits. For example, if the first two checks were passed, but not the third, the system would list the blank fields. If there were any inconsistent data fields contained in this record, these would not be displayed until all the blank values were completed.

Additional edit checks were added with V. 5.3. If the record does not pass these checks, a List Manager screen will appear displaying the inconsistencies for viewing only. The error listing resembles the EAL report from Austin. These inconsistencies cannot be corrected through the List Manger screen. You may use the up-arrow \<^\> to drop out of List Manager and return to Load/Edit.

The system updates the TRANSFER DRGs at exiting the option for open records and at close out on the "701" screen (for VA PTF records only). This is done so that any DRG reports subsequently run which include that PTF record will contain current TRANSFER DRGs based on what has been coded.

1)  Leave and pass days of a patient movement may be edited through Bed Control or through the PTF "501" screens. However, NO corresponding change will be made to the admission record of edits made on these fields through PTF only. Because an open PTF will be updated to match the admission record when the PTF is selected again, any leave/pass day changes made only through PTF will be lost. To ensure that these changes to the PTF are not lost, the PTF can be closed after editing. Closed PTF records are not updated by the system. If the PTF is not closed at the end of the editing session, leave/pass day changes must be made to the admission record through the appropriate Bed Control option. For consistency of the data, leave/pass days should be edited ONLY through Bed Control.
2)  During the verification process that is performed when the user selects to close the PTF, error messages may be displayed and any required fields that are in error or incomplete will be listed. Following are messages that may be displayed to indicate that the PTF cannot be closed as is:

<u>MESSAGE</u> <u>ACTION</u>

"Unable to close without Enter discharge date through

a discharge date.” Bed Control

"Unable to close without a Enter principal diagnosis on

DRG being calculated.” "701" screen

"Not all messages have been cleared up Checkoff remaining PTF messages

for the patient--cannot close."

3)  The system will fill in the facility field, if blank. If this is done, the facility name will be displayed after the PTF record is selected. If there are no treating specialty transfers for the selected record, the system will display a message at this time stating same.

This following is included to give a further explanation of the fields (data items) that constitute the Patient Treatment File. It lists some of the data items that can be edited through the different PTF screens and a brief description of each item. A description of the data elements contained on the MPCR screen is also provided.

<table>
<caption><p>Table 2: Screen “MAS” Data Fields</p></caption>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME OR PROMPT</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FACILITY</td>
<td>Facility number where patient was admitted</td>
</tr>
<tr class="even">
<td>SUFFIX</td>
<td>Suffix of admitting facility</td>
</tr>
<tr class="odd">
<td>SOURCE OF ADMISSION</td>
<td>Source of this patient admission; from SOURCE OF ADMISSION file</td>
</tr>
<tr class="even">
<td>SOURCE OF PAYMENT</td>
<td>For patients treated at non-VA hospitals at VA expense; from set of codes</td>
</tr>
<tr class="odd">
<td>TRANSFERRING FACILITY</td>
<td>VA facility from which the patient was transferred</td>
</tr>
<tr class="even">
<td>TRANSFERRING SUFFIX</td>
<td>Suffix of transferring facility</td>
</tr>
<tr class="odd">
<td>CATEGORY OF BENEFICIARY</td>
<td>Code that indicates the patient's military status from CATEGORY OF BENEFICIARY file</td>
</tr>
<tr class="even">
<td>ENTER THE ELIGIBILITY FOR THIS ADMISSION</td>
<td>For patients with dual eligibility, the eligibility associated with the admission</td>
</tr>
<tr class="odd">
<td>MARITAL STATUS</td>
<td>Patient's marital status</td>
</tr>
<tr class="even">
<td>RACE</td>
<td>Patient's race</td>
</tr>
<tr class="odd">
<td>SEX</td>
<td>Patient's sex</td>
</tr>
<tr class="even">
<td>SPINAL CORD INJURY</td>
<td>Code that indicates if this patient sustained a spinal cord injury and, if so, what type</td>
</tr>
<tr class="odd">
<td>DATE OF BIRTH</td>
<td>Patient's date of birth</td>
</tr>
<tr class="even">
<td>VIETNAM SERVICE INDICATED</td>
<td>YES/NO - Did patient serve in Viet Nam?</td>
</tr>
<tr class="odd">
<td>AGENT ORANGE EXPOS. INDICATED</td>
<td>YES/NO/UNKNOWN - Was patient exposed to Agent Orange?</td>
</tr>
<tr class="even">
<td>RADIATION EXPOSURE INDICATED</td>
<td>YES/NO/UNKNOWN - Was patient exposed to radiation?</td>
</tr>
<tr class="odd">
<td>MST INDICATED</td>
<td>YES/NO/UNKNOWN/DECLINED TO ANSWER Was the patient a victim of Military Sexual Trauma?</td>
</tr>
<tr class="even">
<td>COMBAT VETERAN</td>
<td>YES/NO/UNKNOWN Did the patient see combat service?</td>
</tr>
<tr class="odd">
<td>PROJ 112/SHAD</td>
<td>YES/NO Was the patient exposed to Shipboard Hazard and Defense?</td>
</tr>
<tr class="even">
<td>NOSE/THROAT RADIUM</td>
<td>YES/NO/UNKNOWN - Does the patient claim he or she received nose/throat radium treatment while in the military?</td>
</tr>
<tr class="odd">
<td>POW CONFINEMENT LOCATION</td>
<td>War in which patient was a prisoner of of war</td>
</tr>
<tr class="even">
<td>POW STATUS INDICATED</td>
<td>YES/NO - Was patient ever a prisoner of war?</td>
</tr>
<tr class="odd">
<td>STATE</td>
<td>Patient's state of residence</td>
</tr>
<tr class="even">
<td>COUNTY</td>
<td>Patient's county of residence</td>
</tr>
<tr class="odd">
<td>ZIP+4</td>
<td>Patient's zip code, 5 or 9 digits</td>
</tr>
<tr class="even">
<td>PLACE OF DISPOSITION</td>
<td>Where patient is going upon discharge from this hospital episode; from the PLACE OF DISPOSITION file</td>
</tr>
<tr class="odd">
<td>OUTPATIENT TREATMENT</td>
<td>YES/NO - Will patient receive outpatient care after discharge?</td>
</tr>
<tr class="even">
<td>VA AUSPICES</td>
<td><p>YES/NO - Will VA pay for continued medical care</p>
<p>for this patient after discharge?</p></td>
</tr>
<tr class="odd">
<td>C&amp;P STATUS</td>
<td>Code that indicates the Compensation and Pension status of patient; from set of codes.</td>
</tr>
<tr class="even">
<td>RECEIVING FACILITY</td>
<td>Facility number of VA medical care center to which patient is transferring for further medical care; from PTF TRANSFERRING FACILITY file</td>
</tr>
<tr class="odd">
<td>RECEIVING SUFFIX</td>
<td>Suffix of receiving facility</td>
</tr>
<tr class="even">
<td>MEANS TEST</td>
<td>Means Test Indicator</td>
</tr>
<tr class="odd">
<td>ASIH DAYS</td>
<td>For nursing home or domiciliary patients, number of days patient was absent due to admission to a hospital</td>
</tr>
</tbody>
</table>

Table 2: Screen “MAS” Data Fields

| FIELD NAME OR PROMPT                                    | DESCRIPTION                                                                                                                                                                                                                                 |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPECIALTY TRANSFER DATE                                     | Date patient is admitted to the treating specialty                                                                                                                                                                                              |
| FACILITY TREATING                                           | Treating specialty patient moved to SPECIALTY                                                                                                                                                                                                   |
| PRIMARY CARE PHYSICIAN                                      | Provider responsible for patient's care; from PROVIDER file                                                                                                                                                                                     |
| PROFESSIONAL SERVICE DATE/TIME                              | Must have a date/time value between the date/time of admission and the date/time of discharge                                                                                                                                                   |
| REFERRING OR ORDERING PROVIDER                              | Name of provider ordering the service                                                                                                                                                                                                           |
| RENDERING PROVIDER                                          | Name of provider performing the service                                                                                                                                                                                                         |
| RENDERING LOCATION                                          | Location where service is performed                                                                                                                                                                                                             |
| CPT                                                         | CPT/HCPCS codes used for a patient                                                                                                                                                                                                              |
| CPT MODIFIER                                                | Used to indicate a service or procedure has been altered                                                                                                                                                                                        |
| QUANTITY                                                    | Used to indicate the number of times the procedure was performed                                                                                                                                                                                |
| PRIMARY DIAGNOSIS                                           | Primary diagnosis associated with the procedure performed.                                                                                                                                                                                      |
| SECONDARY DIAGNOSIS                                         | Secondary diagnoses associated with the procedure performed.                                                                                                                                                                                    |
| TREATED FOR SC/AO/IR/SWAC/MST/HEAD and/or NECK CA CONDITION | Was this treatment for a service- connected condition or related to agent orange exposure, ionizing radiation exposure, SW Asia conditions exposure, military sexual trauma, or head and/or neck cancer? These will appear as separate prompts. |
| COMBAT VET                                                  | Was this treatment related to combat?                                                                                                                                                                                                           |
| PROJ 112/SHAD                                               | Was this treatment related to Shipboard Hazard and Defense?                                                                                                                                                                                     |

Table 3: Screen “501-#” Data Fields

| FIELD NAME OR PROMPT            | DESCRIPTION                                                                                                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LEAVE DAYS                          | Number of days patient was on leave (an absence of more than 96 hours but not more than 14 days) from a specialty during that patient movement                                                |
| PASS DAYS                           | Number of days patient was on pass (an absence of less than 96 hours) from a specialty during that patient movement                                                                           |
| ICD 1                               | ICD CM Diagnosis code of diagnosis greatest length of stay on a specialty; (for each specialty patient was admitted to during this period of hospitalization)                                 |
| ICD 2-5                             | ICD CM Diagnosis code of second, third, ..., fifth diagnoses responsible for patient's stay on a specialty                                                                                    |
| TREATED FOR SC/AO/IR/SWAC CONDITION | Was this treatment for a service-connected condition or related to agent orange exposure, ionizing radiation exposure, or SW Asia conditions exposure? These will appear as separate prompts. |
| TREATMENT FOR MST                   | Was this treatment related to military sexual trauma?                                                                                                                                         |
| TREATMENT FOR HEAD/NECK CA          | Was this treatment related to head and/or neck cancer?                                                                                                                                        |
| TREATMENT RELATED TO COMBAT         | Was this treatment related to combat?                                                                                                                                                         |
| TREATMENT RELATED TO PROJ 112/SHAD  | Was this treatment related to Shipboard Hazard and Defense?                                                                                                                                   |

Table 4: Screen “401-#” Data Fields

| FIELD NAME OR PROMPT       | DESCRIPTION                                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| SURGERY/PROCEDURE DATE         | Date of this patient's surgery episode(s), if any                                                                           |
| SURGICAL SPECIALTY             | Code of the surgical specialty associated with the chief surgeon for each surgery episode; from the SURGICAL SPECIALTY file |
| CATEGORY OF CHIEF SURGEON      | Code that indicates the category of the chief surgeon for patient's surgical episode(s); from set of codes                  |
| CATEGORY OF FIRST ASSISTANT    | Code that indicates the category of the first assistant for patient's surgical episode(s); from set of codes                |
| PRINCIPAL ANESTHETIC TECHNIQUE | Code that indicates the major type of anesthetic technique of patient's surgical episode(s); from set of codes              |
| OPERATION CODE                 | Operation code(s) of patient's surgical episode(s)                                                                          |
| SOURCE OF PAY                  | Source of payment for patients operated on in a non-VA facility and returned to a VA facility within a 24-hour period       |

Table 5: Screen “601-#” Data Fields

<table>
<caption><p>Table 6: Screen “701” Data Fields</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME OR PROMPT</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PROCEDURE DATE</td>
<td>Date procedure performed</td>
</tr>
<tr class="even">
<td>PROCEDURE CODE</td>
<td>ICD-9 Procedure Code Number for first,.... fifth procedure for selected procedure date<br />
<br />
ICD-10 Procedure Code Number for First….twenty-fifth procedure for selected procedure date</td>
</tr>
<tr class="odd">
<td>NUMBER OF DIALYSIS TREATMENTS <em>(prompt appears only for select procedure codes)</em></td>
<td>Number of dialysis treatments which occurred on the selected procedure date</td>
</tr>
</tbody>
</table>

Table 6: Screen “701” Data Fields

<table>
<caption><p>Table 7: Screen “801” Data Fields</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME OR PROMPT</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRIMARY DIAGNOSIS</td>
<td>ICD CM code of diagnosis responsible for patient's greatest length of stay for this hospital episode</td>
</tr>
<tr class="even">
<td>SECONDARY DIAGNOSIS</td>
<td>ICD-9 CM code of second, third, ..., twelfth diagnoses for this patient’s episode of care<br />
<br />
ICD-10 CM code of second, third….twenty- fourth diagnoses for this patient’s episode of care</td>
</tr>
<tr class="odd">
<td>Present on Admission Indicator (POA)</td>
<td>ICD-10 only – a POA associated with each diagnosis code entered</td>
</tr>
</tbody>
</table>

Table 7: Screen “801” Data Fields

| FIELD NAME OR PROMPT                                    | DESCRIPTION                                                                                                                                                                                                                                |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROFESSIONAL SERVICE DATE/TIME                              | Must have a date/time value between the date/time of admission and the date/time of discharge                                                                                                                                                  |
| REFERRING OR ORDERING PROVIDER                              | Name of provider ordering the service                                                                                                                                                                                                          |
| RENDERING PROVIDER                                          | Name of provider performing the service                                                                                                                                                                                                        |
| RENDERING LOCATION                                          | Location where service is performed                                                                                                                                                                                                            |
| CPT MODIFIER                                                | Used to indicate a service or procedure has been altered                                                                                                                                                                                       |
| QUANTITY                                                    | Used to indicate the number of times the                                                                                                                                                                                                       |
| CPT                                                         | CPT/HCPCS codes used for a patient procedure was done                                                                                                                                                                                          |
| PRIMARY DIAGNOSIS                                           | Primary diagnosis for the CPT code used                                                                                                                                                                                                        |
| SECONDARY DIAGNOSIS                                         | Secondary and succeeding diagnoses for the CPT code                                                                                                                                                                                            |
| TREATED FOR SC/AO/IR/SWAC/MST/HEAD and/or NECK CA CONDITION | Was this treatment for a service-connected condition or related to agent orange exposure, ionizing radiation exposure, SW Asia conditions exposure, military sexual trauma, or head and/or neck cancer? These will appear as separate prompts. |
| COMBAT VET                                                  | Was this treatment related to combat?                                                                                                                                                                                                          |
| PROJ112/SHAD                                                | Was this treatment related to Shipboard Hazard and Defense?                                                                                                                                                                                    |

Table 8: MPCR Data Fields

| Field             | Definition                                                                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| LOSING DATE           | Date of patient movement off ward, treating specialty or both                                                                                       |
| REC TYPE              | Transaction type (501 or 535)                                                                                                                       |
| WARD/DRG              | Ward patient is moving from and DRG associated with the treating specialty assigned to the losing ward                                              |
| LOSING WARD MPCR/SPEC | Specialty assigned to losing ward                                                                                                                   |
| PTF MPCR/SPEC         | Losing PTF MPCR specialty assigned to patient                                                                                                       |
| LEAVE                 | Number of days patient was on leave (an absence of more than 96 hours but not more than 14 days) from a specialty during that patient movement      |
| PASS                  | Number of days patient was on pass (an absence of less than 96 hours) from a specialty during that patient movement                                 |
| LOS (LENGTH OF STAY)  | Length of stay on the losing ward or, for the 501, length of stay while being treated for the specialty. LOS = elapsed time (-) leave and pass days |

## Close Open Census Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Close Open Census Record option provides you with a quick, easy means of closing PTF records for census purposes. The census record is created when the PTF record is closed for census purposes either through this option or the Load/Edit PTF Data option.

You will first enter the PTF record number or name of the patient whose record you wish to close. If you enter the name of a patient who has more than one record which has not been closed for census purposes, all open records will be displayed with the date of admission for selection. If you choose an admission which does not require a census transaction, the following message will appear:

"\>\>\>\> Census transactions are not required for this PTF record."

The system will first use ADT and Registration data to update the PTF record and transfer DRGs. An edit check is then performed to determine that the PTF data is correct and complete. If the record is incomplete or incorrect, it may be necessary to correct or complete the information using the Load/Edit PTF Data option of the Census Menu. If this is necessary, the following message will be displayed.

"\>\>\>\> Not able to close for census. Please use 'Load/Edit' option to edit PTF".

<u>  
</u>

## Census Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Census Status Report allows you to print a report of all active admissions as of a specified census date. The first time the Census Status Report is run for a particular census date, a Census Workfile is created for that date.

One or all statuses may be selected, and some or all of the following information will be provided for each census record: patient name and last four digits of the social security number; the admission date, ward location on the census date, and census status; the PTF number and census number. At the conclusion of the report, the total number of census records for each status and the overall statistics are given.

The status report is sorted in the following order:

- division
- status
- ward location on census date
- alphabetically by patient name

If all statuses are included, the report will also be sorted by the census status.

If your facility is multidivisional, you will be prompted to select one, several, or all divisions. If you are printing the report for more than one division, the report and the totals given at the end of the report will be sorted by division.

You may choose to queue the report to print during non-work hours, depending on the length of the report. This report was not designed to be run to a terminal. It requires 132 column and may take quite a while to run if the Census Workfile has not been generated.

## Inquire Census Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquire Census Record option is used to view the information contained in one or several patients' census record(s). The census record is created when the PTF record is closed for census purposes. If a census record does not yet exist, the PTF record is displayed with the following message.

"NOTE: This is the PTF record for the admission. Census record does not exist."

The records may be selected by census number, patient name(s) or, if a census record does not yet exist, the PTF number. If there are multiple admissions for a patient, selection will also be made by admission. Only PTF records which require a census record for the current census may be selected.

Information provided in the display may include marital status, race, date of birth, admission date, census date, ASIH (absent-sick-in-hospital) days, census status, date of surgery, anesthesia technique, chief surgeon and surgical procedure (if any), pass days, source of pay, etc. Period of Serv field will appear as Cat of Ben for discharges before 10/1/90.

The following fields are not required for census purposes: Type of Disch., Disch. Specialty, Place of Disp., Out Treat, VA Auspices, and Receiv. facil.

## Other Census Outputs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Comprehensive Census Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Comprehensive Census Report option provides a way to view the information contained in the census records in the PTF screen format.

The census records are selected by patient name. You may choose to view the records of a single patient or a range of patients alphabetically. A range of admission dates may then be specified with further breakdown by status, or all statuses may be selected. The statuses are assigned the following numbers for selection purposes:

- OPEN = 0
- CLOSED = 1
- RELEASED = 2
- TRANSMITTED = 3

A census record is created only when the PTF record is "closed for census purposes". If any of the records within the selected ranges have not been closed for census purposes, the PTF record will be displayed. The following message will appear when a PTF record is printed.

"This is the PTF record for the admission. Census record does not exist."

Information provided for each record may include race, sex, date of birth, marital status, C&P (compensation and pension) status, ASIH (absent-sick-in-hospital) days, leave days, pass days, surgical procedures, surgical specialty, anesthesia technique, etc. Period of Serv field will appear as Cat of Ben for discharges before 10/1/90.

You may wish to queue the report to run during off-hours.

<u>  
</u>

### Productivity Report by Clerk (Census Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Productivity Report by Clerk (Census Only) option provides a report of the census records processed by each coding clerk. The report pertains only to those records which have a status of CLOSED or RELEASED. It may be run for all close out or release dates or a specified range. The user can select to run the report to show the records of all coding clerks or selected clerks. Only holders of the security key DG PTFSUP may access this option.

The report is sorted alphabetically by coding clerks' last name. The following information will be listed for each record.

- Patient Name and SSN
- Census Date
- Number of Patient Movements (#PM)
- Number of Surgical Episodes (#Surg)
- Name of individual who closed/released the record and close out/release date

> The system computes and displays the following for each coding clerk.

- Subtotals indicating the number of patient movements and surgical episodes
- Subcount indicating the number of records coded
- Submean indicating the average number of patient movements and surgical episodes per record

Grand total amounts are displayed at the end of the report.

### Records by Completion Status (Census Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a census coding report by completion status - CLOSED, RELEASED, or TRANSMITTED. Records in an OPEN status are not included. The report may be run for all completion statuses or a single status.

The report can be generated for a particular PTF census date or for a specified release, transmission, or close-out date range. If you wish to begin the report with the first date but not sort to the last date, you must specify the beginning date at the “Start with Date: First//” prompt rather than entering a \<RET\> to accept the default.

For each status, all applicable census records for the census date selected or within the specified release, transmission, or close-out date range will be listed. The following will be provided for each census record.

- Patient Name SSN Census Date
- \# of Patient Movements \# of Surgical Episodes
- Name of individual who closed the record and date closed
- Name of individual who released the record and date released, if applicable

The total number of census records, patient movements, and surgical episodes are given. If the report is run for all statuses, subtotals and subcounts are given for each status.

You may wish to queue the report to run during non-work hours depending on the length of the report.

### Transmitted Census Records List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmitted Census Records List option is used to obtain a list of all transmitted census records for a specified date range. The report is designed to correspond with the Edit Analysis List (EAL) generated by the Austin Information Technology Center (AITC). The output and the EAL may be compared to ensure that all census records that have a status of TRANSMITTED have been received at Austin.

The listing is in numerical order by social security number. In addition to the SSN, the following information is provided: admission date, facility/ suffix number, patient name, census \#, census date, person who released record, and release and transmission dates.

The output is divided such that suffix AO and null suffixes are listed together. All other suffixes are grouped together and will be printed on a separate page. The total number of transmitted records for each grouping is also provided.

The output must be generated at a margin width of 132 columns.

### Unreleased Census Records Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unreleased Census Records Report option provides a listing of census records with a status of CLOSED. These records have not been released for transmission to Austin.

The report is sorted sequentially by close out date. The user may specify a range of close out dates or begin the report with the first close out date for which there is an unreleased census record and end with the last. You may choose to queue this report to print during non-work hours, depending on the length of the report.

Information provided for each census record includes patient name and social security number, admission and discharge date, close out date, and name of the clerk who closed the record. The total number of records listed is given at the end of the report.

## Release Closed Census Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Closed Census Records option allows you to release closed census records for later transmission. Once the record has been released, it is ready for transmission to the Austin Information Technology Center (AITC) through the Transmit Census Records option.

Once you have entered the name of the patient whose record you wish to release, the patient's date of birth, SSN, date of admission, and census status are displayed. When the process is completed, the census status will be updated to RELEASED.

Closed census records can also be released through the census release action of the 701 screen in the Load/Edit PTF Data option.

Only holders of security key DG PTFREL may access this option.

## Transmit Census Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmit Census Records option is used to electronically transmit released census records to the Austin Information Technology Center (AITC). The records are selected for transmittal by release date. The user may choose a single date or a range of dates. Only holders of the security key DG PTFTRANS may access this option.

The system will list the patient names and admission dates of the released census records that fall within the date range selected. For records that have passed the validity check, the system will display the word "Okay" and the record will be transmitted. For those records that do not pass the validity check, the system will list the invalid fields showing the transaction type number which contains that field, field name, column number, and value. The record will be automatically reopened and will NOT be transmitted. The census record will be deleted along with the corresponding entries in the PTF CLOSE OUT and PTF RELEASE files. The user must use the Load/Edit PTF Data option of the Census Menu to correct or complete the invalid fields and close the record.

Electronic MailMan messages are generated through the use of this option. The sender will receive these messages in their IN basket. On invalid records, the message shows the PTF record number and patient name and states that the record has been reopened. On valid records, the message shows how the data was actually sent to Austin. A "Q"uery at this message will provide the MailMan transmission status (i.e. Awaiting Transmission, Sent) and the message number.

The third MailMan message generated is a summary sent only to the user who utilized the option. This message shows the run date, the release date range selected, the total number of census records transmitted, and the local message ID number(s). The local message ID number is used for comparison to the confirmation message received from Austin which is received by all users in the PTI mail group.

## Open Closed Census Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open Closed Census Records option is used to reactivate census records that have been closed but not released or transmitted. It sometimes may be necessary to change or correct a CLOSED census record, but changes cannot be made until the record is reopened. Upon reopening, the corresponding entry in the PTF CLOSE OUT file is deleted and the census status is returned to OPEN.

If you attempt to reopen a census record when the corresponding PTF record does not have a status of OPEN, the following message will appear:

"Associated PTF record {#} must be RE-OPENED in order to re-open Census record {#}".

You may reopen the PTF record through the Open Closed PTF Record option, or both records may be reopened through the 701 screen of the Load/Edit PTF Data option.

Only holders of the security key DG PTFREL may access this option.

## Open Released or Transmitted Census Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to reopen released (record has been closed and is awaiting transmission) or transmitted (record has been electronically transmitted to Austin, TX) census records for the purpose of changing or correcting the record. Changes cannot be made until the record is reopened. When a record is reopened, the corresponding census entries in the PTF CLOSE OUT file and PTF RELEASE file are deleted. Also, the census record is deleted, and the census status is returned to OPEN.

If you attempt to reopen a census record when the corresponding PTF record has been released or transmitted, the following message will appear.

"Associated PTF record {#} must be RE-OPENED in order to re-open Census record {#}".

Although it is possible to open a transmitted record through this option, it is preferable to use the Census Menu Option, 099 Transmission. Use of the 099 option deletes the master record in Austin, while this option does not.

Only holders of the security key DG PTFTRANS may access this option.

You will be prompted for the census record to open. You may enter the patient's name or census record number at this prompt.

## 099 Transmission for Census Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 099 Transmission for Census Record option is used to delete the master record (for census purposes) at the Austin Information Technology Center (AITC) by electronically transmitting a 099 record. For non-free form transmissions, use of this option deletes the entire master record (for census purposes) in Austin and changes the census status of the record at the local facility from TRANSMITTED to OPEN. Upon reopening, the census record is deleted, and the corresponding entries in the CENSUS CLOSE OUT file and in the CENSUS RELEASE file are deleted. Once this record is edited and closed again, the entire record can then be retransmitted to the AAC.

A free form 099 transaction may also be sent through this option. This would be used to delete a master record in Austin where the SSN or admission date had been entered incorrectly or a pseudo social security number had been used and you now have the correct number.

When utilizing this option, enter the social security number of the patient exactly as it was entered when the master record was created. Pseudo social security numbers should be entered in the following format: P#########.

Electronic MailMan messages are generated through the use of this option. The sender will receive these messages in their IN basket. The first message shows how the data was actually sent. A "Q"uery at this message will provide the status of the message and the message number. This number can be checked against the message number in the response from Austin to aid in matching up messages with the correct response. The second message is the response from Austin showing that the data was received or not received and the reason why. This message is sent to members of the PTI mail group.

Only holders of the security key DG PTFTRANS may access this option. You may not utilize this option while other records are being transmitted.

## Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display Census Date Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the supervisor to view census date and parameters. The following is a list of the census date parameters and a brief explanation of each.

CENSUS PERIOD START DATE

The first date of the census period (usually the first day of the fiscal year). All specialty movements and procedures which occur for active admissions between this date and the census period end date should be included in the census record.

CENSUS PERIOD END DATE \[CENSUS DATE\]

The last date of the census period (usually the last date of the fiscal year). All active admissions between the census period start date and this date are listed on the Census Status Report and need a census transaction. This date will be known as the Census Date and will be used to identify the census period.

CLOSE-OUT DATE

The last date the census transaction may be transmitted to the Austin Information Technology Center (AITC).

OK TO XMIT PTF TRANSACTIONS

The date PTF transactions can be transmitted for those admissions which also had census transactions. If PTF transactions are transmitted to Austin before this date, the PTF transaction would overlay the census transaction for the admission. This could have an adverse effect on RAM allocations. It is possible to close and release PTF transactions prior to this date; however, they cannot be transmitted.

CURRENTLY ACTIVE

This field indicates whether or not the date selected is the currently active census date. Only one census date may be active at one time.

### Regenerate Census Workfile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Regenerate Census Workfile option allows the supervisor to regenerate the census workfile entries for a particular census date. One entry is placed in the census workfile for each admission requiring a census record for the selected census date.

When the regeneration is complete, the WORKFILE LAST UPDATED field in the PTF CENSUS DATE file is updated with the current date and time. This can be seen by viewing the Quick Parameter Profile screen for the selected census date through the Display Census Date Parameters option. A MailMan bulletin is also sent to the user who requested the regeneration. These are two methods by which you can monitor the completion of a regeneration. The MailMan message will also inform the user if any ADT changes have affected the workfile entry for the census date.

The first time the Census Status Report is generated for a particular census date, the census workfile is automatically generated. Thereafter, the workfile should be regenerated through this option at the beginning and at the end of the census process to ensure that no admissions have been added via bed control.

Examples of the types of MailMan bulletins received by the user when the Census Workfile is regenerated.

1.  This is an example of the type of message received if the workfile did not change as a result of regeneration.

Subj: Census Workfile Update (CENSUS DATE: SEP 30,1989) 01 May 90 15:47 16 Lines

From: ADTEMPLOYEE,ONE (<span class="mark">redacted</span>) in 'IN' basket. \*\*NEW\*\*

-------------------------------------------------------------------------

Census Work File Compilation Finished: MAY 1,1990@16:02

\*\*\*\* Work File did NOT change as a result of update.\*\*\*\*

2.  2\. The following is an example of the types of messages generated if the workfile entry for the census date has been affected by ADT bed control activity. The first message indicates the admission WAS part of the workfile; however, since the workfile was last compiled, this admission no longer meets the criteria for the current census date. The second message indicates to the user that these admissions are new to the workfile.

Subj: Census Workfile Update (CENSUS DATE: SEP 30,1989) 01 May 90 15:47 16 Lines

From: ADTEMPLOYEE,ONE (<span class="mark">redacted</span>) in 'IN' basket. \*\*NEW\*\*

----------------------------------------------------------------------------------

Census Work File Compilation Finished: MAY 1,1990@15:47

\>\>\> OLD ADMISSIONS no longer needing a Census Record:

Name Admission Date PTF# Census#

---- -------------- ---- -------

ADTPATIENT,ONE (5465) DEC 4,1988@13:00 1055

\>\>\> NEW ADMISSIONS added to workfile needing a Census Record:

Name Admission Date PTF# Census#

---- -------------- ---- -------

ADTPATIENT,TWO (4581) AUG 25,1989@24:00 1321 1324

ADTPATIENT,THREE (3454) JUL 8,1988@14:04 1030

## Fee Basis Census Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis Census Status Report option is used to generate the PTF Census Status Report for census records with a type of FEE BASIS. The report is sorted by census date (census report is produced quarterly) and then by census status (open, closed, released, transmitted). You may choose to run the report for one selected status or all statuses.

Information provided on the report for each record includes patient name, last four digits of the Social Security Number, admission date, PTF number, census number, and census status. A total count is also provided.

# Checkoff PTF Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Checkoff PTF Message option is used to delete PTF messages from the PTF MESSAGE file. All PTF messages for a patient’s period of hospitalization must be deleted prior to closing the PTF recod. The PTF messages may be deleted by patient name or PTF message number. The user may choose to delete all messages, a group of messages, or an individual message. If desired, the system will display a list of the messages for the patient selected.

# DRG Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Calculation option is used to compute and display the Diagnosis Related Group (DRG) for a patient based on that patient's diagnoses and any operations/procedures performed. This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you enter an INACTIVE diagnosis code, a message will be displayed and the prompt will be repeated.

You will initially be prompted for an effective date. This date will be used to validate diagnosis, operation/procedure, and DRG codes. You will also be prompted for the principal diagnosis. Answer with the ICD Code Number of the diagnosis responsible for the major portion of the patient stay. Multiple secondary diagnoses and operations/procedures may also be entered. If an ICD-10 diagnosis code was entered, you will be prompted for Present on Admission (POA).

POA indicator choices and selection behavior are as follows:

- Y = present at the time of inpatient admission.
  - The POA is set to Yes for the particular diagnosis code, and the user is prompted to enter the next diagnosis.
- N = not present at the time of inpatient admission.
  - The POA is set to No for the particular diagnosis code, and the user is prompted to enter the next diagnosis.
- U = documentation is insufficient to determine if condition is present on admission.
  - The POA is set to U for the particular diagnosis code.
  - The POA is flagged to No for the DRG calculation.
  - The user is prompted to enter the next diagnosis code.
- W = provider is unable to clinically determine whether condition was present on admission or not.
- “” = null, no POA entered, user pressed \<Return\>.

The following is a list of those items that are computed and displayed for the DRG:

- Weight - The value assigned to the DRG.
- Low day(s) - The low trim point day for the assigned DRG (always 1 day).
- High days - The high trim point day for the assigned DRG.
- Avg len of stay - The geometric national average length of stay for the DRG.
- Diagnosis Codes – The ICD Diagnosis code for the DRG.
- Operation/Procedure Codes – The Operation/Procedure codes for the DRG.

The data may be calculated for VA or non-VA patients. The system does not store the DRG compiled for each patient. It is recalculated each time this option is utilized.

# Enter PTF Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter PTF Message option is used to send a PTF message to HIMS (Health Information Management Section). Some PTF messages are generated and forwarded by the system. For example, when a patient's diagnosis changes or when a treating specialty transfer occurs, an automatic PTF message is sent. Surgical episode information, however, does not generate a message. This option provides a way to send to HIMS that data which is not automatically forwarded.

The site has the option to enable or disable the printing of PTF messages by setting the field, PRINT PTF MESSAGES, to YES or NO under ADT System Definition. This is defined for the entire medical center. If so selected, the messages will be printed on the HIMS MESSAGE PRINTER as defined under ADT System Definition (by division if multidivisional site). If a device has not been established as HIMS MESSAGE PRINTER, the system will send the messages to DEFAULT PTF MESSAGE PRINTER.

As with other PTF messages, those created using this option are stored in the PTF MESSAGE file. All messages for the patient's period of hospitalization must be deleted prior to closing the PTF record. Therefore, after entering information from a message into the associated PTF record, HIMS personnel will delete the message from the file.

# Inquire PTF Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquire PTF Message option is used to display PTF messages. This option has only one prompt, "Select PTF MESSAGE NUMBER". At this prompt, the user may enter the PTF message number, the patient's name, the ward of the patient whose PTF message he/she wishes to view, or double question marks (??) to obtain a list of PTF message numbers.

If a patient's name is entered who has more than one PTF message on file, the system will display a list of the message numbers and ask the user to choose the PTF message to be displayed. When the ward is entered, the system will display a list of all patients on that ward who have messages in the PTF MESSAGE file, asking for the desired patient. If double question marks (??) are entered, the system will provide a list of PTF message numbers with the associated patient name and the message date/time.

# Load/Edit PTF Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Load/Edit PTF Data option is used to enter, edit, and view data contained in the PTF record for a patient's period of hospitalization. When utilizing this option for census specific purposes, the Load/Edit PTF Data option from the Census menu should be used.

VA or Non-VA (hospitalization in a private facility at VA expense) PTF records may be edited through this option; however, there are some differences between the two records. Notes \#3 and \#4 on at the end of this option documentation provide information regarding the Non-VA PTF and should be read by users before editing Non-VA PTF records.

After selecting the patient name and admission date or PTF Record Number at the start of this option, the system updates the patient's PTF record. During this updating process, some PTF information is being filled in from the patient's record in the PATIENT file and from the patient's Bed Control information which corresponds to the admission date selected. This data should be verified and/or edited through the Extended Bed Control option.

The PTF data is arranged so that it may be viewed and edited through various screens. For easy viewing of the screens, this option allows you to "jump" from one screen display to another by entering an up-arrow \<^\> and the desired screen name. On some screens, data is grouped into sections for editing. Each section is labeled with a number to the left of the data items in reverse video. The patient's name, social security number, date of admission and the screen number appear at the top of every screen. After editing a screen, the system redisplays the screen with the changes.

## "101" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first screen that will appear is the "101" screen. This screen contains admission and discharge information for the episode of care and basic patient demographic information. This screen will show the CENSUS STATUS field if the patient needs a census record for the current census. Much of this screen is automatically filled in from data in the PATIENT file and, for VA PTF records, from the corresponding admission record in the PATIENT file. Choose the number(s) to the left of the group of data items you wish to edit. The 101 screen will display country, province, and postal code in place of state, county, and zip code if the patient has a foreign address. The Census date will display at the top of the screen on the right side if displaying a Census record. In addition, users may enter or edit an Initial Date of Service for Non-VA PTF records; this date can be up to 72 hours prior to the Inpatient Admission.

### COMPACT Act Administrative Eligibility Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For any patient records, this will display the current COMPACT Act administrative eligibility status (Eligible, Undetermined, Not Eligible). If it is clinically determined the patient is in acute suicidal crisis, the patient will be afforded the benefit.

### Acute Suicidal Crisis Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all inpatient admissions that are related to Acute Suicidal Crisis, the PTF 101 screen will display, “Acute Suicidal Crisis: Yes.” This value is from the “Admitted for Acute Suicidal Crisis?” prompt captured during the admission workflow. This value is stored in the PTF file (#45) and a pointer to this value is stored in the COMPACT ACT EPISODE OF CARE (EOC) file (#818).

## "MAS" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "MAS" screen contains patient diagnoses and information about patient movement(s), surgery(s), procedure(s) and inpatient CPT record data such as CPT record date and time, provider information, rendering location, CPT/HCPCS modifiers, quantity, and up to 8 diagnosis codes per CPT’/HCPS. For each diagnosis code entered, PTF also tracks the following conditions: SC (service connected), AO (agent orange), IR (ionizing radiation), SWAC (SW Asia conditions), MST (military sexual trauma), and HNC (head/neck cancer).

Some patient movement information is filled in from the admission record (applies to VA PTF only) including losing specialty (the specialty from which the patient is transferring). Patient movements of less than 24 hours and transfers that only involve a facility treating specialty change and not a PTF specialty change will not create a new patient movement in PTF.

It should be noted that 401P transactions (which are valid only for admissions prior to 10/1/87) allow up to five procedure codes per admission and are not stored by date. 601 transactions allow up to twenty-five codes per procedure date. To add, edit, or delete a procedure code for a 601 transaction, select “P” to add, select “Q” to delete, or select "E" to edit. 801 transactions allow more than one CPT record date and time per day. The CPT record date and time value must have a date and time value between the date and time of admission and the date and time of discharge. Each CPT record must have a rendering provider and at least one CPT code. Each CPT code must have at least one (up to 8) associated diagnosis. For each associated diagnosis, PTF also tracks service connection, Agent Orange, ionizing radiation, SW Asia conditions, military sexual trauma, and head/neck cancer conditions if the patient is registered with these conditions in Registration. To add a CPT record, select “I”.

## "501" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "501" screen(s) contains information about the patient movement(s) listed on the "MAS" screen including the patient discharge movement. Because a "501" screen is generated for every patient movement which involves a specialty change, there may be more than one "501" screen. The screens are numbered as follows: 501-1, 501-2, 501-3, etc. Since the discharge movement is displayed on this screen, every PTF will have at least one "501" screen. (See Note \#1 at the end of this option documentation for important information regarding editing leave and pass days.)

The maximum number of movements which can be transmitted is 25. If this limit is exceeded, the system will warn the user. Each movement may contain up to twenty-five ICD-10 diagnosis codes along with the associated Present on Admission indicator. The Present on Admission Indicator fields in PTF records will allow the choice of Exempt (the numeral 1) to be entered; this is used for Non-VA sites that are exempted by CMS from reporting Present on Admission information. The Set Transmit Flag on Movements option will allow the supervisor to choose which movement(s) to delete from the transmission.

If a TRANSFER DRG can be computed for a movement, it will be displayed on the applicable "501" screen. TRANSFER DRGs are generated based on codes entered when a movement between Services has occurred AND a change in the DRG has occurred. Applicable Services are Surgery, Neurology, Rehab. Medicine, Psychiatry, and Medicine. Other Services (pass through) are not applicable to TRANSFER DRGs. TRANSFER DRGs are stored in the PTF File and are used as a basis for the DRG reports. After editing, a screen is usually redisplayed with the new values. However, due to the processing time involved, TRANSFER DRGs are not updated after editing the “501” screen. They will be updated the next time the PTF is load/edited when you see the message, “Updating PTF record \#” or upon exiting the option when you see the message, “Updating TRANSFER DRGs.”

If a patient is in an Acute Suicidal Crisis Episode of Care (EOC), the current “501” screen will display the EOC benefit dates, the start date, the number of remaining days, and/or the end date. For all inpatient movements with treatment that is related to Acute Suicidal Crisis, the PTF 501 screen will display, “Treated for Acute Suicidal Crisis: Yes.” This value is from the “Treatment for Acute Suicidal Crisis?” prompt captured during the admission or transfer workflows. This value is stored in the PTF 501 sub-file (#45.02).

> **NOTE:** If the user determines that an ICD-10 PTF record needs to be coded as an ICD-9 record, the user must use the “D” delete code Action to delete the ICD-10 codes 6 through 25. The user will be able to edit codes 1-5 and replace the ICD-10 codes with ICD-9 codes.

## "401" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "401" screen(s) contains information for any surgical episode(s) listed on the "MAS" screen. Because there is a “401” screen for every date a surgical episode occurred, there may be more than one "401" screen. However, if there were 2 surgical episodes on the same date, they will appear on different "401" screens. The screens are numbered as follows: 401-1, 401-2, 401-3, etc. You may enter up to twenty-five operation codes per date. After 10-1-87, 3 surgical episodes per date are allowed. Prior to that date, only 2 episodes per date were allowed. If no surgical episodes were performed during the inpatient stay, a "401" screen will not exist for that PTF. Note: Users can now add Surgical procedures that occur for a patient up to 72 hours prior to that patient's admission to the PTF record.

> **NOTE:** If the user determines that an ICD-10 PTF record needs to be coded as an ICD-9 record, the user must use the “C” delete code Action to delete the ICD-10 codes 6 through 25. The user will be able to edit codes 1-5 and replace the ICD-10 codes with ICD-9 codes.

## "601" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "601" screen(s) contains information for any procedures performed. Because there is a "601" screen for every date a procedure occurred during the hospitalization, there may be more than one "601" screen. The screens are numbered as follows: 601-1, 601-2, 601-3, etc. You may enter up to twenty-five ICD-10 procedures per date. If numerous procedures were performed on the same day, they may be listed on more than one screen. If no procedures were performed during the inpatient stay, a "601" screen will not exist for that PTF. If receiving dialysis, data pertaining to the number of treatments per procedure date will be contained in this transaction. Note: Users can now add Outpatient procedures that occur for a patient up to 72 hours prior to that patient's admission to the PTF record.

> **NOTE:** If the user determines that an ICD-10 PTF record needs to be coded as an ICD-9 record, the user must use the “Q” delete Action to delete the ICD-10 codes (#11 through 25). The user will be able to edit codes 1-10 and replace the ICD-10 codes with ICD-9 codes.

## "MPCR" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "MPCR" screen contains information for those patient movements affecting the Monthly Program Cost Report. It contains information regarding those interward transfer movements that change the ward MPCR for the patient but the treating specialty remains the same. The screen is for viewing only with no editing allowed. The data displayed is compiled from the system entries made through the Bed Control options. Every PTF record will have a "MPCR" screen. MPCR information is required for those records with a discharge date after 10/1/90. Only 501 & 535 movements after 10/1/90 are displayed.

## "701" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user chooses the principal ICD-9 diagnosis (diagnosis responsible for the major length of stay) through the "701" screen. The 702 segment contains ICD-9 diagnoses 2-10, which are also entered through the “701” screen. Once this data is entered, the system calculates and displays the DRG based on the principal ICD-9 diagnosis, ICD-9 diagnoses 2-10 from 702, and ICD-9 operations/procedures from 401 and 601 segments.

The user chooses the principal ICD-10 diagnosis (diagnosis responsible for the major length of stay) through the "701" screen. The 702 segment contains ICD-10 diagnoses 2-24, which are also entered through the “701” screen. Once this data is entered, the system calculates and displays the DRG based on the ICD-10 principal diagnosis, ICD-10 diagnoses 2-24 from the 702 segment, and ICD-10 operations/procedures from 401 and 601 segments.

The DRG on the "701" screen is not stored in the PTF and is recalculated every time this screen is displayed. This is also the screen through which the PTF can be closed and released.

> **NOTE:** If the user determines that an ICD-10 PTF record needs to be coded as an ICD-9 record, the user must delete the ICD-10 codes 13 through 25. The user will be able to edit codes 1-12 and replace the ICD-10 codes with ICD-9 codes.

## "801" SCREEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “801” screen(s) contains information for professional services administered during the inpatient stay. It contains information regarding CPT record date and time, provider information, rendering location, procedure (CPT-4) and diagnosis (ICD ) codes, modifiers, and quantity, as well as any service connection or environmental indicators. Because there is an “801” screen for every CPT record occurring during the hospitalization, there may be more than one “801” screen. The screens are numbered as follows: 801-1, 801-2, 801-3, etc. Each time an “801” screen is entered, the user is prompted to send the data to PCE. If the user chooses not to send the data, the data is sent at release of the PTF record. If no professional services were captured during the inpatient stay, an “801” screen will not exist for that patient.

Some of the data items that can be found on the different PTF screens, with a brief description of each item, are provided at the end of this option documentation.

Four items which come from the admission record cannot be entered/edited through PTF: ADMISSION DATE, DISCHARGE DATE, DISCHARGE SPECIALTY, and TYPE OF DISPOSITION. (This data is editable through PTF on a non-VA PTF record.)

Four checks (edits) are performed on the PTF at the time of closing. The first review checks to see that facility number and discharge date are completed and that a DRG has been calculated.

Because the PTF cannot be closed if PTF messages are remaining, the second review checks to see that all PTF messages are cleared. The user is given the opportunity to delete any PTF messages remaining at this time.

Third, the PTF is checked to see that required fields are completed and that numeric fields do not have non-numeric characters and vice versa. Any erroneous fields are listed and the user is given the opportunity to enter the correct value for the field. The PERIOD OF SERVICE field may not be edited through PTF. If this field is in error, it will be listed but will have to be edited through the Load/Edit Patient Data option in Registration.

Lastly, the record is checked for inconsistent data fields.

Each edit is not applied until the record has passed all preceding edits. For example, if the first two checks were passed, but not the third, the system would list the blank fields. If there were any inconsistent data fields contained in this record, these would not be displayed until all the blank values were completed.

Additional edit checks have been added with V. 5.3. If the record does not pass these checks, a List Manager screen will appear displaying the inconsistencies for viewing only. The error listing resembles the EAL report from Austin. These inconsistencies cannot be corrected through the List Manger screen. You may use the up-arrow \<^\> to drop out of List Manager and return to Load/Edit.

The system updates the TRANSFER DRGs at exiting the option for open records and at close out on the "701" screen (for VA PTF records only). This is done so that any DRG reports subsequently run which include that PTF record will contain current TRANSFER DRGs based on what has been coded.

## Close Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Editing Leave and Pass Days 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Leave and Pass days of a patient movement may be edited through Bed Control or through the PTF "501" screens. However, NO corresponding change will be made to the admission record of edits made on these fields through PTF only. Because an open PTF will be updated to match the admission record when the PTF is selected again, any leave/pass day changes made only through PTF will be lost. To ensure that these changes to the PTF are not lost, the PTF can be closed after editing. Closed PTF records are not updated by the system. If the PTF is not closed at the end of the editing session, leave/pass day changes must be made to the admission record through the appropriate Bed Control option.

For consistency of the data, leave/pass days should be edited ONLY through Bed Control.

### Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the verification process that is performed when the user selects

to close the PTF, error messages may be displayed and any required fields that are in error or incomplete will be listed.

Following are messages that may be displayed to indicate that the PTF cannot be closed as is.

> <u>MESSAGE</u> <u>ACTION</u>

> "Unable to close without Enter discharge date

> a discharge date." through Bed Control

> "Unable to close without a Enter principal diagnosis

> DRG being calculated." on “701” screen

> "Not all messages have been Checkoff remaining

> cleared up for the patient-- PTF messages

> cannot close."

<u>  
</u>

### Differences between VA/Non-VA PTF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Differences between the VA PTF and the non-VA PTF are explained below.

> \- there is no corresponding admission record for the non-VA PTF...

> An admission record is created upon admission to a VA medical center. Since the non-VA PTF only applies to admissions to private facilities, there is no admission record for non-VA PTF.

> \- automatic updating does not occur on the non-VA PTF...

> Since the automatic updating matches the PTF with the associated admission record and there is no associated admission record for the non-VA PTF, it cannot be updated. All data on the non-VA PTF is entered by the system from the PATIENT file or entered by the user during the load/edit process. However, updating will occur for demographic information.

> \- discharge information is entered directly during load/edit process on the non-VA PTF...

> Discharge information is retrieved for the VA PTF from the admission record and cannot be edited through PTF. Since there is no admission record for the non-VA PTF, the discharge information is entered by the user through the Load/Edit PTF Data option.

> Users are able to enter an Initial Date of Service for Non-VA PTF records up to 72 hours prior to an Inpatient Admission. This date is entered when using the Set Up Non-VA PTF Record option and can be edited via use of the Load/Edit PTF data option. The date is displayed at the top of the \<101\> screen and can be edited by choosing ‘1’ and then navigating to the Initial Date of Service prompt. This date is also displayed below the Date of Admission on the \<MAS\> and \<701\> screens.

### Edit Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two edit options that are different on the non-VA PTF “MAS” screen are:

'M' - used to add a patient movement

'X' - used to delete a patient movement

Other edit options are the same as on the VA PTF "MAS" screen.

### Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will fill in the facility field, if blank. If this is done, the facility

name will be displayed after the PTF record is selected. If there are no treating specialty transfers for the selected record, the system will display a message at this time stating same.

The following is included to give a further explanation of the fields (data items) that constitute the Patient Treatment File. It lists some of the data items that can be edited through the different PTF screens and a brief description of each item. A description of the data elements contained on the MPCR screen is also provided.

> FIELD NAMESCREEN OR PROMPT DESCRIPTION

"101" FACILITY Facility number where patient was

admitted

SUFFIX Suffix of admitting facility

SOURCE OF ADMISSION Source of this patient admission;

from SOURCE OF ADMISSION file

SOURCE OF PAYMENT For patients treated at non-VA

hospitals at VA expense; from set

of codes

TRANSFERRING VA facility from which the

FACILITY patient was transferred

TRANSFERRING SUFFIX Suffix of transferring facility

INITIAL DATE OF SERVICE For Non-VA PTF records, this date can be

up to 72 hours prior to the Admission

date. Facilitates billing of procedures prior

to admission.

CATEGORY OF Code that indicates the patient's

BENEFICIARY status from CATEGORY OF

BENEFICIARY file

ENTER THE ELIGIBILITY For patients with dual eligibility, the

FOR THIS ADMISSION eligibility associated with the admission

MARITAL STATUS Patient's marital status

RACE Patient's race

SEX Patient's sex

DATE OF BIRTH Patient's date of birth

SPINAL CORD INJURY Code that indicates if this

patient sustained a spinal cord

injury and, if so, what type

> FIELD NAMESCREEN OR PROMPT DESCRIPTION

"101" VIETNAM SERVICE INDICATED? YES/NO - Did patient serve in Vietnam?

AGENT ORANGE YES/NO/UNKNOWN - Was patient

EXPOS. INDICATED exposed to Agent Orange?

RADIATION EXPOSURE YES/NO/UNKNOWN - Was patient INDICATED exposed to radiation?

MST INDICATED YES/NO/UNKNOWN/DECLINED TO

ANSWER - Was the patient a victim of

Military Sexual Trauma?

COMBAT VETERAN YES/NO/UNKNOWN

Did the patient see combat service?

NOSE/THROAT RADIUM YES/NO/UNKNOWN - Does the patient

claim he or she received nose/throat

radium treatment while in the military?

PROJ 112/SHAD YES/NO - Was the patient exposed to

Shipboard Hazard and Defense?

POW STATUS YES/NO - Was patient ever a

INDICATED prisoner of war?

POW CONFINEMENT War in which patient was a

LOCATION prisoner of war

ACUTE SUICIDAL CRISIS YES/NO – Was this inpatient admission for

Acute Suicidal Crisis?

COMPACT ACT ADMINISTRATIVE ELIGIBLE/UNDETERMINED/NOT

ELIGIBILITY ELIGIBLE – What is the patient’s

Administrative Eligibility status?

STATE Patient's state of residence

COUNTY Patient's county of residence

ZIP+4 Patient's zip code, 5 or 9 digits

PLACE OF DISPOSITION Where patient is going upon

discharge from this hospital

episode; from the PLACE OF

DISPOSITION file

OUTPATIENT TREATMENT YES/NO - Will patient receive

outpatient care after discharge?

VA AUSPICES YES/NO - Will VA pay for

continued medical care for this

patient after discharge?

> FIELD NAMESCREEN OR PROMPT DESCRIPTION

“101” C&P STATUS Code that indicates the

Compensation and Pension status

of patient; from set of codes

RECEIVING FACILITY Facility number of VA medical care center

to which patient is transferring for

further medical care

RECEIVING SUFFIX Suffix of receiving facility

MEANS TEST Means Test Indicator

ASIH DAYS For nursing home or domiciliary patients,

number of days patient was absent due to

admission to a hospital

"MAS" SPECIALTY TRANSFER DATE Date patient is admitted to the

treating specialty

FACILITY TREATING SPECIALTY Treating specialty patient moved to

PRIMARY CARE Provider responsible for patient’s care;

PHYSICIAN from the PROVIDER file

PROFESSIONAL SERVICE Must have a date/time value between

DATE/TIME the date/time of admission and the

date/time of discharge

REFERRING OR Name of provider ordering the

ORDERING PROVIDER service

RENDERING PROVIDER Name of provider performing the

procedure

RENDERING LOCATION Location where service is performed

CPT CPT/HCPCS codes used for a patient

CPT MODIFIER Used to indicate a service or procedure

has been altered

QUANTITY Used to indicate the number of times the

procedure was performed

PRINCIPAL DIAGNOSIS Principal diagnosis associated

with the procedure performed.

FIELD NAMESCREEN OR PROMPT DESCRIPTION

“MAS” POA PRINCIPAL DIAGNOSIS This is the Present on Admission (POA)

indicator for the Principal Diagnosis. One

of the following values should be assigned

in accordance with the official coding

guidelines:

Y = present on the time of inpatient

admission

N = not present on the time of inpatient

admission

U = documentation is insufficient to

determine if condition is POA

W = provider is unable to clinically

determine whether condition was POA

1 = exempt

SECONDARY DIAGNOSIS Secondary diagnoses associated with the

procedure performed.

POA SECONDARY DIAGNOSIS This is the Present on Admission (POA)

indicator for Secondary Diagnoses. For

every Secondary Diagnosis entered, a

POA indicator is also required. The

choices are the same as for the POA

PRINCIPAL DIAGNOSIS field.

TREATED FOR SC/AO/ Was this treatment for a service

IR/SWAC/MST/HEAD and/or connected condition or related to

NECK CA CONDITION agent orange exposure, ionizing

> radiation exposure, SW Asia conditions exposure, military sexual trauma, or head and/or neck cancer? These will appear as separate prompts.

COMBAT VET Was this treatment related to combat?

PROJ 112/SHAD Was this treatment related to Shipboard

Hazard and Defense?

"501-#" LEAVE DAYS Number of days patient was on leave (an

absence of more than 96 hours but not

more than 14 days) from a specialty

during that patient movement

PASS DAYS Number of days patient was on pass (an

absence of less than 96 hours) from a

specialty during that patient movement

ICD 1 ICD Diagnosis code of

diagnosis that is responsible for

patient's greatest length of stay

on a specialty; (for each specialty

patient was admitted to during this

period of hospitalization)

POA FOR ICD 1 This is the Present on Admission (POA)

indicator for ICD 1. One of the following

values should be assigned in accordance

with the official coding guidelines:

Y = present on the time of inpatient

admission

N = not present on the time of inpatient

admission

U = documentation is insufficient to

determine if condition is POA

W = provider is unable to clinically

determine whether condition was POA

1 = exempt

ICD 2-5 ICD-9 Diagnosis code of

second, third, ..., fifth

diagnoses responsible for

patient's stay on a specialty

ICD 2-25 ICD-10 Diagnosis code of

second, third,…, twenty-

fifth diagnoses responsible

for patient’s stay on a specialty

POA FOR ICD 2-25 This is the Present on Admission (POA)

indicator for ICD-10 codes 2-25. For every

ICD code entered, a POA indicator is also

required. The choices are the same as for

the POA FOR ICD 1 field.

TREATED FOR SC/AO/ Was this treatment for a service-

IR/SWAC CONDITION connected condition or related to

agent orange exposure, ionizing

radiation exposure, or SW Asia

conditions exposure? These will

appear as separate prompts.

> FIELD NAMESCREEN OR PROMPT DESCRIPTION

"501-#" TREATMENT FOR MST Was this treatment related to military

sexual trauma?

TREATMENT FOR HEAD/ Was this treatment related to head and/or

NECK CA neck cancer?

TREATMENT RELATED Was this treatment related to combat?

> TO COMBAT

TREATMENT RELATED TO Was this treatment related to Shipboard

PROJ 112/SHAD Hazard and Defense?

TREATED FOR Was this treatment related to

ACUTE SUICIDAL CRISIS Acute Suicidal Crisis?

COMPACT Start Date Date of the Start of the COMPACT Act Episode of Care

COMPACT Remaining Days Number of Remaining Days for the COMPACT Act Inpatient Benefit (30 days or less)

COMPACT End Date Date of the End of the COMPACT Act Episode of Care

"401-#" SURGERY/PROCEDURE Date of this patient's surgery episode(s),

DATE if any; from set of codes

SURGICAL SPECIALTY Code of the surgical specialty

associated with the chief surgeon

for each surgery episode; from

the SURGICAL SPECIALTY file

CATEGORY OF CHIEF Code that indicates the category of the

SURGEON chief surgeon for patient’s surgical

episode(s); from set of codes

CATEGORY OF FIRST Code that indicates the category of the

ASSISTANT first assistant for patient's surgical

episode(s); from set of codes

PRINCIPAL ANESTHETIC Code that indicates the major type of

TECHNIQUE anesthetic technique of patient’s surgical

episode(s); from set of codes

OPERATION CODE Operation code(s) of patient's

surgical episode(s)

SOURCE OF PAY Source of payment for patients

operated on in a non-VA facility

and returned to a VA facility

within a 24 hour period

> FIELD NAMESCREEN OR PROMPT DESCRIPTION

"601-#" PROCEDURE DATE Date procedure performed

PROCEDURE CODE

ICD-9 Procedure Code Number for

first,…fifth procedure for selected

procedure date

ICD-10 Procedure Code Number

for first,….twenty-fifth procedure

for selected procedure date

NUMBER OF DIALYSIS Number of dialysis treatments which

TREATMENTS *(prompt appears* occurred on the selected procedure

*only for select procedure codes)* date

"701" PRINCIPLE DIAGNOSIS ICD code of diagnosis responsible

for patient's greatest length of stay

for this hospital episode

SECONDARY DIAGNOSIS ICD-9 code of second, third, ..., twelfth 1-12 diagnoses for this patient’s episode of care

ICD-10 code of second, third, ..., twenty-fourth 1-24 diagnoses for this patient’s episode of care

PRESENT ON ADMISSION Indicates whether or not the diagnosis was present on admission (for ICD-10 codes only). The Principle and all of the Secondary Diagnoses fields require an associated POA value. One of the following values should be assigned in accordance with the official coding guidelines:

Y = present on the time of inpatient

admission

N = not present on the time of inpatient

admission

U = documentation is insufficient to

determine if condition is POA

W = provider is unable to clinically

determine whether condition was POA

1 = exempt

"801" PROFESSIONAL SERVICE Must have a date/time value between the

DATE/TIME date/time of admission and the date/time

of discharge

REFERRING OR Name of provider ordering the service

ORDERING PROVIDER

RENDERING PROVIDER Name of provider performing the service

RENDERING LOCATION Location where service is performed

CPT CPT/HCPCS codes used for a patient

CPT MODIFIER Used to indicate a service or procedure

has been altered

QUANTITY Used to indicate the number of times the

procedure was done

PRIMARY DIAGNOSIS Primary diagnosis for the CPT code used

SECONDARY DIAGNOSIS Secondary and succeeding diagnoses for

the CPT code

TREATED FOR SC/AO/ Was this treatment for a service-

IR/SWAC/MST/HEAD and/or connected condition or related to

NECK CA CONDITION agent orange exposure, ionizing

radiation exposure, SW Asia

conditions exposure, military sexual

trauma, or head and/or neck cancer?

These will appear as separate prompts.

COMBAT VET Was this treatment related to combat?

PROJ 112/SHAD Was this treatment related to Shipboard

Hazard and Defense?

MPCR Screen Data Fields

LOSING DATE Date of patient movement off ward, treating specialty or both

REC TYPE Transaction type (501 or 535)

WARD/DRG Ward patient moving from/DRG associated

with the treating specialty assigned to

the losing ward

LOSING WARD MPCR/SPEC Specialty assigned to losing ward

PTF MPCR/SPEC Losing PTF MPCR specialty assigned to patient

LEAVE Number of days patient was on leave (an absence of

more than 96 hours but not more than 14 days) from

a specialty during that patient movement

PASS Number of days patient was on pass (an absence of

less than 96 hours) from a specialty during that

patient movement

LOS Length of stay (elapsed time (-) leave and pass days)

on the losing ward or, for the 501, length of stay

while being treated for the specialty

# National Patient Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Transmission Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PIMS Events Transmitted Yesterday

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to generate a report of all PIMS events that were transmitted to the National Patient Care Database yesterday.

The Austin Information Technology Center (AITC) will be sending daily reports to the medical centers listing what transmissions they have received. The medical center can then use this report to verify that the number sent was the same as that received by the AITC.

The only prompt is for a device.

#### PIMS Events Transmitted for Date Range

This option is used to generate a report of all PIMS events transmitted to the NPCD for a selected date range. If this option has been previously utilized, the last date range that was selected will be displayed.

The Austin Information Technology Center (AITC) will be sending monthly reports to the medical centers listing what transmissions they have received. The medical center can then use this report to verify that the number they sent was the same as that received by the AITC.

## Transmission Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Retransmit Patient Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to retransmit demographic data for a selected patient.

The Austin Information Technology Center (AITC) will be sending reports to the medical centers listing rejects. For rejects that pertain to a patient’s demographic data, the medical center can use this option to resend the data to the AITC.

There exists a background job scheduled to run periodically throughout the day that builds HL7 demographic messages. This background job will generate this HL7 message during its next run.

The Transmission Utilities Menu is locked with the DG PTFTRANS security key.

### Retransmit Admission Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to retransmit admission data/history for a selected patient and admission. This data includes admission, discharge, and all transfers. Only patients with an admission on file can be selected.

The Austin Information Technology Center (AITC) will be sending daily reports to the medical centers listing what transmissions they have received. The medical center can compare this with their G&L to verify that all admissions, discharges, and transfers had been received. This option would be used to reconcile any discrepancies that may be found.

The display begins with a default date range of T-45 through today. You may change the date range; however, it may not exceed 366 days. The display lists all admissions for the selected patient that occurred in the given timeframe. If you select a new patient, the currently selected timeframe will be used.

The Transmission Utilities Menu is locked with the DG PTFTRANS security key.

### Retransmit Entry in ADT/HL7 PIVOT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to retransmit an entry in the ADT/HL7 PIVOT file (#391.71). Entries can be selected by date of event, pivot number, or patient name.

Event Types may include the following:

| Inpatient Events          | Admission (does not store individual transfers and discharges) |
|---------------------------|----------------------------------------------------------------|
| Updates to Data           | Demographic changes                                            |
| Registration Events       | Registration                                                   |
| Treating Facility Updates | Treating facility transfer/update                              |

The Transmission Utilities Menu is locked with the DG PTFTRANS security key.

# Open Closed PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open Closed PTF Record option is used to reactivate PTF records that have been closed but not released or transmitted. It sometimes becomes necessary to change or correct the codes in a CLOSED PTF record. Changes cannot be made until the record is reopened. Upon reopening, the corresponding PTF entry in the PTF CLOSE OUT file is deleted.

Only holders of the security key DG PTFREL may access this option.

# Open Released or Transmitted PTF Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open Released or Transmitted PTF Records option is used to reopen released or transmitted PTF records. The PTF records with a status of RELEASED have been closed and are awaiting transmission to Austin. The records with a status of TRANSMITTED have been electronically sent to the Austin Information Technology Center (AITC).

It may be necessary to change or correct the codes in a particular record. Changes cannot be made to a released or transmitted record until it is reopened. Upon reopening, the corresponding PTF entries in the PTF CLOSE OUT file and in the PTF RELEASE file are deleted. The Load/Edit PTF Data option may be used to reopen a closed record but not one that has been released or transmitted. Use of the Load/Edit PTF Data option requires security key DG PTFREL.

Although it is possible to open a transmitted record through this option, it is preferable to use the 099 Transmission option to accomplish this. The use of the 099 option deletes the master record in Austin while use of this option does not.

Only holders of the security key DG PTFTRANS may access this option.

You will be prompted for the PTF record to open. You may enter the patient's name or PTF record number at this prompt.

# PTF Output Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Admissions without an Associated PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admissions without an Associated PTF Record option provides a listing of admission records from Bed Control that have no corresponding PTF record. This happens either because the admission occurred in an earlier ADT version which did not automatically generate PTF records for hospital admissions (as is presently done), or the PTF record was deleted.

The report is sorted sequentially by discharge date. The user may select all admissions without an associated PTF record or a discharge date range may be selected. It should be noted that depending upon the number of admissions without PTF records and the size of your database, this report could be time-consuming if a discharge date range is not specified. You may choose to queue the report to print during off-hours.

Patient name, patient ID#, admission date and discharge date are shown for each admission listed. Admission and discharge times may also be shown.

You will be prompted for a date range and device.

## Comprehensive Report by Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Comprehensive Report by Admission option provides a way to view the information contained in the PTF records in the PTF screen format.

The PTF records are selected by patient name. You cannot search using the patient’s SSN.

You may choose to view the records of a single patient or a range of patients alphabetically by full name (last name first). If selecting a single patient, an exact match of the full name, including middle name, is required. Selecting a range of names requires entry of values to ensure inclusion, e.g. A to Azz. A range of admission dates may then be specified with further breakdown by PTF status. If you wish to include all statuses, accept the default. Individual statuses must be selected by number: Open=0, Closed=1, Released=2, and Transmitted=3.

Information provided for each record may include race, sex, date of birth, marital status, date of discharge, type of discharge, discharge bedsection, Compensation and Pension (C&P) status, Absent Sick in Hospital (ASIH) days, leave days, pass days, surgical procedures, surgical specialty, anesthesia technique, etc. PERIOD OF SERV field will appear as CAT OF BEN for discharges before 10/1/90.

If you wish to view a single patient's records, you may prefer to use the Inquire PTF Record option of the PTF Output Menu.

Depending upon the size of your database and the ranges selected, this report could be quite time-consuming. You may wish to run the report during off-hours.

The examples below demonstrate how to select patients for the Comprehensive Report by Admission.

When START and GO TO names entered are different but GO TO name is longer than START name, you will obtain records that are in the date and name range selected.

<span id="_Toc422997955" class="anchor"></span>Figure 1: Example of Selecting a Range of Patients for Comprehensive Report by Admission Using Longer GO TO Name

Select OPTION NAME: Comprehensive Report by Admission

Comprehensive Report by Admission

\* Previous selection: PATIENT equals MCGAITC,TEST M

START WITH PATIENT: MCGAITC,TEST M// MCGAITC \<=

GO TO PATIENT: MCGAITC,TEST M//\<=

\* Previous selection: ADMISSION DATE from Jan 1,2015 to Apr 2,2015@24:00

START WITH ADMISSION DATE: Jan 1,2015// (JAN 01, 2015)

GO TO ADMISSION DATE: Apr 2,2015// (APR 02, 2015)

\* Previous selection: STATUS from 0 (Open) to 3 (Transmitted)

START WITH STATUS: 0// Open

GO TO STATUS: 3// Transmitted

DEVICE: VIRTUAL TELNET Right Margin: 80//

PTF RECORD JUN 22,2015 17:07 PAGE 1

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

--------------------------------------------------------------------------------

MCGAITC,MSG TEST DDS10044MAR 1,2015 12:00

If the START and GO TO names are an exact match and the date range is appropriate, then data will appear on the report.

<span id="_Toc165304520" class="anchor"></span>Figure 2: Example of Selecting a Range of Patients for Comprehensive Report by Admission Using the Same START and GO TO Names

Select OPTION NAME: DG PTF COMPREHENSIVE REPORT Comprehensive Report by Admission

Comprehensive Report by Admission

\* Previous selection: PATIENT from PTFKL,REDACTED to PTFKL,REDACTEDZ

START WITH PATIENT: PTFKL,REDACTED// \<=

GO TO PATIENT: PTFKL,REDACTEDZ// PTFKL,REDACTED \<=

\* Previous selection: ADMISSION DATE from Jan 1,2013 to Jun 22,2015@24:00

START WITH ADMISSION DATE: Jan 1,2013// (JAN 01, 2013)

GO TO ADMISSION DATE: Jun 22,2015// (JUN 22, 2015)

\* Previous selection: STATUS from 0 (Open) to 3 (Transmitted)

START WITH STATUS: 0// Open

GO TO STATUS: 3// Transmitted

DEVICE: VIRTUAL TELNET Right Margin: 80//

PTF RECORD JUN 22,2015 17:21 PAGE 1

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

--------------------------------------------------------------------------------

PTFKL,REDACTED 443 DEC 5,2014 09:54

Placing a Z at the end of the GO TO name can help to ensure the record for a single patient is located.

<span id="_Toc165304521" class="anchor"></span>Figure 3: Example of Using Z in the GO TO Name to Locate a Patient for Comprehensive Report by Admission

Select OPTION NAME: Comprehensive Report by Admission

Comprehensive Report by Admission

\* Previous selection: PATIENT from MCGAITC,R to MCGAITC,REDACTED

START WITH PATIENT: MCGAITC,R// AAB,BOB \<=

GO TO PATIENT: MCGAITC,REDACTED// AAB,BZ \<=

\* Previous selection: ADMISSION DATE from Jan 1,2013 to Jan 1,2014@24:00

START WITH ADMISSION DATE: Jan 1,2013// (JAN 01, 2013)

GO TO ADMISSION DATE: Jan 1,2014// (JAN 01, 2014)

\* Previous selection: STATUS from 0 (Open) to 3 (Transmitted)

START WITH STATUS: 0// Open

GO TO STATUS: 3// Transmitted

DEVICE: VIRTUAL TELNET Right Margin: 80//

PTF RECORD JUN 22,2015 17:51 PAGE 1

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

--------------------------------------------------------------------------------

AAB,BOB JAN 15,2013 JAN 14,2013SSN 108 Open

:::::::::::::::::::::::::::::

PAGE AAB,BOBNOV 5,201414:52 JAN 22,2013 08:29SSN 110 Open

If the START name is longer than the GO TO name, you will get an error message.

<span id="_Toc165304522" class="anchor"></span>Figure 4: Example of Error Message When Selecting Patients for Comprehensive Report by Admission

Select PTF Output Menu \<TEST ACCOUNT\> Option: Comprehensive Report by Admission

\* Previous selection: PATIENT from MCGAITC,TEST to MCGAITC,TEST Z

START WITH PATIENT: MCGAITC,TEST // ABCD,E F \<=

GO TO PATIENT: MCGAITC,TEST M// ABCD,E \<=Less than 'FROM' value.

Searching for a range is based on <u>patient name only; y</u>ou cannot search by SSN.

<span id="_Toc165304523" class="anchor"></span>Figure 5: Example of Selecting a Range of Patients for Comprehensive Report by Admission Based on Name Only

Select PTF Output Menu \<TEST ACCOUNT\> Option: COMprehensive Report by Admission

\* Previous selection: PATIENT from MCGAITC to MCGAITC,MSG TEST DDS

START WITH PATIENT: MCGAITC// PTFKG \<=

GO TO PATIENT: LAST// PTFKG,REDACTED \<=

\* Previous selection: ADMISSION DATE from Jan 1,2014 to Apr 1,2015@24:00

START WITH ADMISSION DATE: Jan 1,2014// 010113 (JAN 01, 2013)

GO TO ADMISSION DATE: Apr 1,2015// 123114 (DEC 31, 2014)

\* Previous selection: STATUS from 0 (Open) to 3 (Transmitted)

START WITH STATUS: 0// Open

GO TO STATUS: 3// Transmitted

DEVICE: VIRTUAL TELNET Right Margin: 80//

PTF RECORD JUN 23,2015 11:11 PAGE 1

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

--------------------------------------------------------------------------------

PTFKG,CLINREM APR 7,2015 12:00 DEC 10,2014 14:39

SSN 189 Open

:::::: additional data

PAGE 8

PTFKG,HATTIE J NOV 3,2014 12:52

SSN 154 Open

:::::::::::: additional data

PAGE 13

PTFKG,REDACTED REDACTED MAY 2,2015 11:3 NOV 16,2014 18:34

SSN 235 Transmitted

## Diagnostic Code PTF Record Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Diagnostic Code PTF Record Search option is used to search for occurrences of specified diagnostic codes in the PTF Records. Only holders of security key DG PTFSUP may access this option.

The search asks whether you would like to search on ICD-9 or ICD-10 codes. It may be performed for matches of a specific diagnostic code(s) or for matches within a range of diagnostic codes. You may select to have this report totaled by either the number of matching diagnostic codes found (ICD count) or the number of PTF records containing matches. You may further select to have the report sorted by any field(s) within the PTF File (in their entirety or within a specified range). If you wish to sort the report by number, but also have it broken down further by other fields, you must type in the word NUMBER or N at the “SORT BY: NUMBER//” prompt rather than entering \<RET\> to accept the default.

Depending upon the number of fields specified and/or whether ranges are specified for those fields, you may have the opportunity to store the search format in a sort template for later retrieval.

The actual appearance of the output may vary depending upon the user specifications; however, the following will be shown for each PTF Record in which a match is found.

- Patient Name
- Admission Date
- Ward at Discharge
- Social Security Number
- Discharge Date
- PTF Number
- Sequential Number of Code in the patient movement (i.e., "ICD 3" - matched code is the third code listed in the patient movement)
- Date of patient movement corresponding to matched code
- Diagnostic Code Number matched
- Principal Diagnosis - displayed where primary diagnosis is same as matched diagnostic code
- Number of matches found (either ICD count or PTF records)

Depending upon the size of your database and your particular report specifications, the printing of this report may be quite time consuming. You may wish to queue the report to run during off-hours.

## DRG Information Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Information Report option is used to generate a report displaying the Diagnosis Related Group (DRG) for a patient based on an effective date entered by the user, that patient's diagnoses, and any operations/procedures performed. The DRG is calculated for each entered diagnosis code, determining what the DRG would be if each of the secondary diagnosis codes was treated as the principal diagnosis (diagnosis responsible for major portion of patient’s stay).

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

The following is a list of those items that are computed and displayed for the DRG:

- Effective Date - The effective date entered by the user.
- Weight - The value assigned to the DRG.
- Low day(s) - The low trim point day for the assigned DRG (always 1 day).
- High days - The high trim point day for the assigned DRG.
- Avg len of stay - The geometric national average length of stay for the DRG.
- Diagnosis Codes – The ICD Diagnosis code for the DRG.
- Present on Admission Indicator (POA) – Associated with ICD-10 Diagnosis code.
- Operation/Procedure Codes – The Operation/Procedure codes for the DRG.

The data may be calculated for VA or non-VA patients. The system does not store the DRG compiled for each patient. It is recalculated each time this option is utilized.

## DRG Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DRG Case Mix Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Case Mix Summary option provides a report that groups the DRGs by Service, Specialty, and Provider and calculates an average weight for each grouping.

This report can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run the report for active admissions, your site must be doing concurrent coding. For discharged patients, it can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another, with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the report is run for active admissions, Transfer DRGs are always used.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, from next-next-to-last specialty, etc., back seventy-five codes. Codes and length of stay on pass-through services are ignored for Transfer DRGs.

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If this field is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the DRG Case Mix Summary based on Transfer DRGs, the discharge Transfer DRG is calculated from the discharge 501.

If you run the report based on DRG only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

The following information is shown for all DRGs for each Service, Specialty and Provider: total weight, total number of discharges, and average weight. "Discharges" in this report does not always mean discharged from the hospital. A patient gets counted in the total number of discharges when the patient is either discharged from the hospital with that DRG or when a service transfer or discharge occurs which generates that Transfer DRG. The total weight equals the sum of all DRGs. The average weight is the sum divided by the number of cases.

Only holders of security key DG PTFSUP may access this option.

This report is designed to run with a right margin setting of 132.

### ALOS Report for DRGs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ALOS Report for DRGs option provides a listing of DRG totals by average length of stay. The report shows how the facility's length of stays for the various DRGs compares to the national average length of stay. National ALOS values from the DRG file are according to the fiscal year of the report's ending date.

This report can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run the report for active admissions, your site must be doing concurrent coding. For discharged patients, it can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another, with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the report is run for active admissions, Transfer DRGs are always used. Further breakout by DRG for medical center only, Service only, or both DRG for medical center and Service can be selected. Service breakdown is further divided into specialty.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, from next-next-to-last specialty, etc., back seventy-five codes. Codes and length of stay on pass-through services are ignored for Transfer DRGs.

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If this field is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the ALOS Report for DRGs based on Transfer DRGs, the discharge Transfer DRG is calculated from the discharge 501.

If you run the report based on DRG only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

The following information is shown for each DRG listed: low and high trim points, the national average length of stay, weight, total discharges, total length of stay, and average length of stay per discharge. These totals are broken down to show each value for below average length of stay and above average length of stay. "Discharges" in this report does not always mean discharged from the hospital. A patient gets counted in the total number of discharges when the patient is either discharged from the hospital with that DRG or when a service transfer or discharge occurs which generates that Transfer DRG. The total weight and average weight is then listed. The total weight equals the weight times the total number of discharges. The average weight is the sum divided by the number of cases.

The total length of stay is computed as total days less pass days and leave days. If the user selects to base the report on Transfer DRGs, the length of stay is the length of stay on the service. Otherwise, the length of stay is the cumulative length of stay for the hospitalization.

A cover page and table of contents page is provided for each breakout in this report including specialty. Due to the processing sequence, the table of contents is printed last. You may wish to insert this page in your report following the cover page.

The option can generate up to nine separate ALOS Reports depending on the user's selection. Only holders of security key DG PTFSUP may access this option.

This report is designed to run with a right margin setting of 132. Depending on the date range selected and the number of records for that range, this report can be quite lengthy. You may choose to queue the report to run during off hours.

### Batch Multiple DRG Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Batch Multiple DRG Reports option allows the user to batch process the following DRG Reports: Trim Point Report, DRG Frequency Report, DRG Case Mix Summary, and ALOS for DRGs. A single report, any combination of reports, or all four reports may be selected for batch processing through this option.

The pre-processing performed by the computer for each of these DRG Reports is the same. Considerable computer processing time is saved when the reports are batch processed instead of run individually as the pre-processing is performed only once for all the selected reports.

These reports can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run these reports for active admissions, your site must be doing concurrent coding. For discharged patients, they can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another, with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the reports are run for active admissions, Transfer DRGs are always used. Further breakout by DRG for medical center only, Service only, or both DRG for medical center and Service can be selected. Service breakdown is further divided into specialty.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, etc., back seventy-five codes. Codes and length of stay on pass-through services are ignored for Transfer DRGs.

### Batch Multiple DRG Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If the principal diagnosis is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the Batch Multiple DRG Reports based on Transfer DRGS, the discharge Transfer DRG is calculated from the discharge 501. If you run the report based on DRG only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

A cover page and table of contents page is provided for each breakout in this report including specialty. Due to the processing sequence, the table of contents is printed last. You may wish to insert this page in your report following the cover page.

These reports are designed to run with a right margin setting of 132. Depending on the date range selected and the number of records for that range, these reports can be quite lengthy. You may choose to queue the report to run during off hours.

Only holders of security key DG PTFSUP may access this option.

### DRG Frequency Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Frequency Report option shows the frequency with which patients are grouped into various DRGs. The report is sorted by DRG frequency, beginning with the most frequently occurring DRG.

This report can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run this report for active admissions, your site must be doing concurrent coding. For discharged patients, it can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the report is run for active admissions, Transfer DRGs are always used. Further breakout by DRG for medical center only, Service only, or both DRG for medical center and Service can be selected. Service breakdown is further divided into specialty.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, etc., back seventy-five codes. Codes and length of stay on pass-through services are ignored for Transfer DRGs.

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If the principal diagnosis is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the DRG Frequency Report based on Transfer DRGS, the discharge Transfer DRG is calculated from the discharge 501.

If you run the report based on DRG only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

### DRG Frequency Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information is shown for each DRG listed: low and high trim points, the national average length of stay, weight, total 1-day stays, total number of discharges, total length of stay, and average length of stay per discharge. "Discharges" in this report does not always mean discharged from the hospital. A patient gets counted in the total number of discharges when either discharged from the hospital with that DRG or when a service transfer or discharge occurs which generates that Transfer DRG. The total weight and average weight is then listed. The total weight equals the weight times the total number of discharges. The average weight is the sum divided by the number of cases.

A cover page and table of contents page is provided for each breakout in this report including specialty. Due to the processing sequence, the table of contents is printed last. You may wish to insert this page in your report following the cover page.

The option can generate up to nine separate DRG Frequency Reports depending on the user's selection. Only holders of security key DG PTFSUP may access this option.

This report is designed to run with a right margin setting of 132. Depending on the date range selected and the number of records for that range, this report can be quite lengthy. You may choose to queue the report to run during off hours.

### DRG Index Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Index Report option allows the user to generate a report which sorts and lists patient names according to their DRG. The report is sorted in DRG order and further sorted by patient name or terminal digit order. One DRG, a range of DRGs, or all DRGs may be selected for inclusion. All PTF statuses may be included, or any one status chosen.

The report can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run the report for active admissions, your site must be doing concurrent coding. For discharged patients, it can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another, with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the report is run for active admissions, Transfer DRGs are always used.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, from next-next-to-last specialty, etc., back seventy-five codes and length or stay on pass-through services are ignored for Transfer DRGs.

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If the principal diagnosis is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the DRG Index Report based on Transfer DRGS, the discharge Transfer DRG is calculated from the discharge 501. If you run the report based on DRG only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

The following information from the DRG file is given for every DRG included in the report for which there is a hit:

- weight
- low/high trim values
- DRG description
- average length of stay value - based on fiscal year (National)

For each patient listed, the following information is provided: social security number, admission and discharge date, transfer date (if applicable), length of stay, PTF status, transferring provider, and losing specialty. The LOS column on this report applies to LOS on the Service excluding leave and pass days.

A flags column ("FLGS") is shown on the report. The indicators in this column are described on the bottom of each applicable page in the report along with the total number in each category.

Two columns on the report take on a different meaning depending on whether or not Transfer DRGs are included when running the report.

Column Transfer DRGs Transfer DRGs

Name included in report not included

======================================================

TRANSFER A date in this column This column will

DATE indicates that this always contain a

DRG is based on a PTF line through it,

Service Transfer. A indicating it is

line in this column not applicable.

indicates that the DRG

is based on the last or

current service and codes.

LOS LOS is based on time LOS is based on

in last or current entire hospitalization.

service.

(LOS always excludes leave and pass days)

The following totals are given for every DRG included in the report for which there is a hit.

- Total - total hits for that DRG
- Total Unique Patients - A patient may group into the same DRG more than once. Unique is determined according to social security number.

A summary page follows the main report showing the total hits for each DRG included in the report. Following the summary page, a list will be provided (if applicable) showing any PTF records for which a DRG could not be computed due to codes not being entered either for the entire stay or for a particular movement; however, the option provides the capability to suppress processing of this list so that it will not be printed.

A cover page and table of contents page are provided. Due to the processing sequence, the table of contents is printed last. You may wish to insert this page in your report following the cover page.

This option can generate up to three separate DRG Patient Index Reports depending on the user's selection. Only holders of security key DG PTFSUP may access this option.

Depending on the date range selected and the number of records for that range, this report can be quite lengthy. You may choose to queue the report to run during off hours.

### Trim Point DRG Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trim Point DRG Report option provides a listing of DRG totals by trim points; below trim, within trim, and above trim. Trim points represent an expected length of stay range. The values are calculated from Medicare data and are based upon the length of stay distribution for each DRG category.

This report can be run for active admissions or discharged patients within a specified date range. Date ranges selected may not begin prior to 10/1/00 and date ranges may not overlap fiscal years.

This report utilizes the DRG weight and trim values published annually in the Federal Register for each Fiscal Year. These values are based on national Medicare data.

If you choose to run the report for active admissions, your site must be doing concurrent coding. For discharged patients, it can be run for DRGs from the 701/702/703 transactions or Transfer DRGs. Transfer DRGs are generated when a patient moves from one service to another, with a change in DRG. The transfers are based on patient movements in PTF, not on physical interward transfers. When determining Transfer DRGs, the surgical episodes are applied to the appropriate service based on the date of surgery. If the report is run for active admissions, Transfer DRGs are always used. Further breakout by DRG for medical center only, Service only, or both DRG for medical center and Service can be selected. Service breakdown is further divided into specialty.

When a transfer occurs, and the patient has been on more than one specialty within the service, codes are taken in the following order: from last specialty, from next-to-last specialty, etc., back seventy-five codes and length of stay on pass-through services are ignored for Transfer DRGs.

The provisional discharge DRG for an inpatient is based on the principal diagnosis (diagnosis mainly responsible for length of stay). If the principal diagnosis is blank, it is based on the first code of the discharge 501. Secondary codes come from the 501s. At discharge, if you run the Trim Point DRG Report based on Transfer DRGs, the discharge Transfer DRG is calculated from the discharge 501. If you run the report based on DRGs only, the discharge DRG is based on the principal diagnosis with secondary diagnoses from the 702/703.

The following information is shown for each DRG listed: low and high trim points, the national average length of stay, weight, number of discharges below trim point, number of discharges and total length of stay within trim points, number of discharges above trim point, days above trim, and total length of stay above trim. "Discharges" in this report does not always mean discharged from the hospital. A patient gets counted in the total number of discharges when the patient is either discharged from the hospital with that DRG or when a service transfer or discharge occurs which generates that Transfer DRG. The totals for each DRG are then given - discharges, length of stay, weight, and average weight. The total weight equals the weight times the total number of discharges. The average weight is the sum divided by the number of cases. A grand total line is also displayed.

The total length of stay is computed as total days less pass days and leave days. If the user selects to base the report on Transfer DRGs, the length of stay is the length of stay on the service. Otherwise, the length of stay is the cumulative length of stay for the hospitalization.

A cover page and table of contents page are provided for each breakout in this report including specialty. Due to the processing sequence, the table of contents is printed last. You may wish to insert this page in your report following the cover page.

This option can generate up to nine separate Trim Point Reports depending on the user's selection. Only holders of security key DG PTFSUP may access this option.

This report is designed to run with a right margin setting of 132. Depending on the date range selected and the number of records for that range, this report can be quite lengthy. You may choose to queue the report to run during off hours.

## Inquire PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquire PTF Record option is used to view the information contained in a patient's PTF records. The records are selected by patient name and, if there are multiple admissions for that patient, by admission. The user may select several different patients' records for viewing at one time through this option.

Information provided in the display may include marital status, race, date of birth, admitting eligibility, admission date, discharge date, discharge specialty, type of discharge, ASIH (absent-sick-in-hospital) days, PTF status, date of surgery, anesthesia technique, chief surgeon and surgical procedure (if any), pass days, source of pay, etc. The display will also include exposure to Agent Orange and Ionizing Radiation, Military Sexual Trauma, and Nose/Throat Radium Treatment information. The display will show the census status field if the patient needs a census record for the current census. PERIOD OF SERV field will appear as CAT OF BEN for discharges before 10-1-90.

## Listing of Records by Completion Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report of PTF records by status - CLOSED, RELEASED, or TRANSMITTED. Records in an OPEN status are not included.

The report may be run for all completion statuses or a single status. A completion status date range or discharge date range may be specified. If you wish to begin the report with the first date, but not sort to the last applicable date, you must specify the actual date at the “START WITH ... DATE: FIRST//” prompt rather than entering a \<RET\> to accept the default.

For each status, all applicable PTF records within the specified date range will be listed. The following will be provided for each PTF record.

- Patient Name and SSN
- Discharge Date
- \# of Patient Movements
- \# of Surgical Episodes
- Name of individual who closed the record and date closed.
- Name of individual who released the record and date released, if applicable.

Depending upon the size of your database and your individual report specifications, you may wish to queue the report to run during off-hours.

The total number of PTF Records, patient movements, and surgical episodes will be computed and displayed at the conclusion of the report. The mean number of patient movements and surgical episodes will also be computed and displayed. If the report is run for all statuses, this information is provided for each status as well as for the total report.

## Means Test Indicator of 'U' Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Means Test Indicator of 'U' Report option is used to list PTF records, within a specified date range, for which the Means Test is not done or not completed. The system searches every PTF record for each patient in the date range selected for a Means Test indicator of 'U'. It then determines, by looking at the patient record in the PATIENT file, if the indicator should still be 'U'. If so, these patients are listed on the report. If not, the system updates the Means Test indicator to the appropriate value in the PTF record and these patients will not appear on this report.

The user may choose to run the report for either a discharge date range or admission date range. The report can be sorted by patient last name or terminal digit (social security number). Information provided includes patient name and social security number, PTF number, and applicable date of test. This date is the Means Test date that is used to determine the Means Test indicator, as it may be possible to have more than one Means Test date for a single admission.

The system looks for the closest Means Test date previous to the discharge date for the applicable date of test. If there is no discharge date, it will search for the closest test date previous to the admission date. If no test date is found, the date shown on the report in the applicable date of test column will be the admission date if admission date range is chosen and the discharge date if discharge date range is chosen. These dates are signified on the report by a double asterisk (\*\*).

If there are no PTF records with a Means Test indicator of 'U' in the date range selected, the following message will appear and the system will return to the menu.

"No PTF records with Means Test Indicators of 'U' within (discharge/admission) date range selected"

## MPCR Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view the Monthly Program Cost Report (MPCR) information related to a particular PTF record. The information displayed is the same as that shown on the MPCR Screen of the Load/Edit PTF Record option. If the PTF record for the selected patient is not closed, the PTF record is automatically updated using the latest specialty and ward movement information.

The MPCR display contains information for those patient movements affecting the Monthly Program Cost Report. The display is for viewing only with no editing allowed. The data displayed is compiled by the system from activities made through the Bed Control options. The MPCR information will begin with the first 501 or 535 movement to occur after 10/1/90. If the discharge date is prior to 10/1/90, the following statement will appear on the MPCR screen: "MPCR information not required for this admission."

Below is a list of the data fields displayed and a brief description of each.

LOSING DATE Date of patient movement off ward, treating specialty or both

REC TYPE Transaction type

WARD/DRG Ward patient is moving from and the DRG

associated with the treating specialty assigned to

the losing ward

LOSING WARD MPCR/SPEC Treating specialty assigned to losing ward

PTF MPCR/SPEC Losing PTF MPCR specialty assigned to patient

LEAVE Number of days patient was on leave (an absence of

more than 96 hours but not more than 14 days)

from a specialty during that patient movement

PASS Number of days patient was on pass (an absence of

less than 96 hours) from a specialty during that patient movement

LOS (LENGTH OF STAY) Length of stay on the losing ward or, for the 501,

length of stay while being treated for the specialty

## Open PTF Record Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open PTF Record Listing option provides a list of PTF records with an OPEN status for discharged patients. The report is sorted sequentially by discharge date. You may select a range of discharge dates, or you can begin the report with the first discharge date having an open PTF record and sort to the last.

The output provides patient name and social security number, admission, and discharge dates (times may also be shown), PTF \#, and discharge specialty for each PTF record listed, if applicable. Psychiatry discharges will be shown as 93-High Intensity Gen Psych Inpat or 92-Gen Intermediate Psych. A count of the total number of PTF records listed on the report is also provided.

This report may be quite lengthy depending upon the date range selected and size of your database. You may choose to queue the report to run during off-hours.

You will be prompted for a date range and device.

## Patient Summary by Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Summary by Admission option is used to generate a list of a patient's movements, surgeries, and procedures from the PTF record for a selected admission. The date, description, and code number is provided for each action displayed. The losing specialty is listed for each movement. The output may be run to include up to 20 PTF records. Both VA and non-VA (Fee Basis) PTF records may be selected.

The following data items are shown for each record: patient name, social security number, eligibility and eligibility status, discharge provider, admission date, discharge date, PTF record number, and total LOS (length of stay) including pass but excluding leave days. Fee Basis records are so indicated and the length of stay for these records appears as the last line of the report. The discharge provider is not shown for Fee Basis records.

You will be prompted for the PTF patient record(s) and a device. The PTF record number or patient name may be entered.

## Pro Fees Not Sent to PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pro Fees Not Sent to PCE option provides a report displaying the professional services (801s) provided to a patient that have not been transmitted to PCE for the selected date range. The fields captured in this report are:

- CPT Record Date/Time
- Patient Name
- Patient Social Security Number

## Productivity Report by Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Productivity Report by Clerk option provides a report of the PTF records processed by each coding clerk. The report pertains only to those PTF records which have a status of CLOSED or RELEASED. It may be run for all close out or release dates or a specified range. The user can select to run the report to show the records of all coding clerks or selected clerks. Only holders of the security key DG PTFSUP may access this option.

The report is sorted alphabetically by coding clerks' last name. The following information will be listed for each PTF record listed on the report.

- Patient Name and SSN
- Discharge Date
- Number of Patient Movements (#PM)
- Number of Surgical Episodes (#Surg)
- Name of individual who closed/released the record and close out/release date

The system computes and displays the following for each coding clerk.

- Subtotals indicating the number of patient movements and surgical episodes
- Subcount indicating the number of records coded
- Submean indicating the average number of patient movements and surgical episodes per record

Grand total amounts are displayed at the end of the report.

## Surgical Code PTF Record Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgical Code PTF Record Search option is used to search for occurrences of specified surgical codes in the PTF Records. Only holders of security key DG PTFSUP may access this option.

The search may be performed for matches of a specific surgical code(s) or for matches within a range of surgical codes. You may select to have this report totaled by either the number of matching surgical codes found (ICD count) or the number of PTF records containing matches. You may further select to have the report sorted by any field(s) within the PTF file (in their entirety or within a specified range). If you wish to sort the report by number, but also have it broken down further by other fields, you must type in the word NUMBER (or "N") at the “SORT BY: NUMBER// prompt rather than entering \<RET\> to accept the default.

Depending upon the number of fields specified and/or whether ranges are specified for those fields, you may have the opportunity to store the search format in a sort template for later retrieval.

The actual appearance of the output may vary depending upon the user specifications; however, the following will be shown for each PTF Record in which a match is found.

- Patient Name
- Social Security Number
- Admission Date
- Discharge Date
- Ward at Discharge
- PTF Number
- Sequential Number of procedure/surgery in segment (i.e. "Op Co. 2" - the second procedure/surgery listed in the procedure/surgery segment)
- Date on which surgery took place (procedure dates are not displayed)
- Surgical Code Number matched
- Number of matches found (ICD count or PTF records)

Depending upon the size of your database and your particular

report specifications, the printing of this report may be quite

time consuming. You may wish to queue the report to run during off-hours.

## Transmitted Records List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmitted Records List option is used to obtain a list of all transmitted records for a specified date range. The report is designed to correspond with the Edit Analysis List (EAL) generated by the Austin Information Technology Center (AITC). The output and the EAL may be compared to ensure that all PTF records that have a status of TRANSMITTED have actually been received at Austin.

The listing is in entire social security number order. Information provided includes social security number, admission date, facility/suffix number, patient name, PTF \#, discharge date, person who released record, and release and transmission dates.

The output is divided such that null suffixes and active suffixes within the Psychiatric Medical Center Station type (A0, A1, A2, or A3) are listed together. All other suffixes are grouped together and will be printed on a separate page. The total number of transmitted records for each grouping is also provided.

The output must be generated at a margin width of 132 columns.

## Unreleased PTF Record Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unreleased PTF Record Output option provides a listing of PTF records with the status of CLOSED. These records have not been released for transmission to Austin.

The report is sorted sequentially by close out date. The user may specify a range of close out dates or may begin the report with the first close out date for which there is an unreleased PTF record and end with the last. Depending on the date range selected and the size of your database, you may choose to queue this report to print during off-hours.

Information provided for each PTF record includes patient name and social security number, admission and discharge date, close out date, and name of clerk who closed the record. A count of the number of records listed is given at the end of the report.

# PTF Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PTF Transmission option is used to electronically transmit released PTF records to certain domains. The domains are locations set up to receive the transmissions. Most sites will only transmit to one domain - the Austin Information Technology Center (AITC). However, it is possible to transmit data to more than one domain at the same time.

The records are selected for transmittal by release date. The user may choose a single date or a range of dates.

The system will list the patient names and admission dates of the released PTF records that fall within the date range selected. For records that have passed the validity check, the system will display the word "Okay" and the record will be transmitted. For those records that do not pass the validity check, the system will list the invalid fields showing the transaction type number which contains that field, field name, column number and value. The record will be automatically reopened and will NOT be transmitted. Corresponding entries in the PTF CLOSE OUT and PTF RELEASE files are deleted. The user must use the Load/Edit PTF Data option to correct or complete the invalid fields and close the record.

Electronic MailMan messages are generated through the use of this option. The sender will receive these messages in his/her IN basket. On invalid records, the message shows the PTF record number and patient name and states that the record has been reopened. On valid records, the message shows how the data was actually sent to Austin. A "Q"uery at this message will provide the MailMan transmission status (i.e., Awaiting Transmission, Sent) of the message and the message number.

The third MailMan message generated is a summary sent only to the user who utilized the option. It shows the run date, the release date range selected, the total number of PTF records transmitted, and the local message ID number(s) for comparison to Austin's confirmation message.

There may be more than one MailMan message per transmission. The total length of any one MailMan message that the PTF module transmits to Austin is about 150 lines. If every PTF record sent had 3 lines in it, for example, a new MailMan message would be created every 50 records with its own local message ID number.

A transmit flag allows transmission to be enabled/disabled for each domain. If the transmit flags for all receiving users for the PTF domains are turned off at your facility, the following message will be displayed upon entering the option and you will be returned to the menu.

"Transmission is turned OFF for receiving domains in TRANSMISSION ROUTERS file"

Only holders of the security key DG PTFTRANS may access this option.

# Quick Load/Edit PTF Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Quick Load/Edit PTF Data option is used to enter/edit data contained in the 101, 701, 501, 401, 801, and 601 transactions in list format (rather than screen format) which allows for faster editing.

VA or non-VA (hospitalization in a private facility at VA expense) PTF records may be edited. Only PTF records with a status of OPEN may be selected. Note \#1 found at the end of this option documentation, provides information regarding the non-VA PTF and should be read by users before editing non-VA PTF records.

After selecting the patient name and admission date or PTF record number for VA PTF records, the system automatically updates the patient's PTF. A delay occurs while the record is being updated. During this updating process, some PTF information is being filled in from the patient's record in the PATIENT file and from the patient's Bed Control information which corresponds to the admission date selected.

The editing in this option is broken down into five segments as follows.

| Segment | Data                     |
|-------------|------------------------------|
| 1st segment | 101 and 701 transaction data |
| 2nd segment | 501 transaction data         |
| 3rd segment | 401 transaction data         |
| 4th segment | 801 transaction data         |
| 5th segment | 601 transaction data         |

## "101" and "701" Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These transactions contain admission and discharge information for the episode of care and basic patient demographic information. Much of this data is automatically filled in from data in the PATIENT file and, for VA PTF records, from the corresponding admission record in the PATIENT file. Principal diagnosis (the diagnosis responsible for the major length of stay) and secondary diagnoses are also contained here.

## "501" Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "501" transaction allows you to edit information concerning patient movements such as movement date, losing bedsection, leave days, pass days, and ICD codes; however, on a VA PTF record, you may only edit the ICD codes. The patient movements must be more than 24 hours apart and involve a specialty change to be counted.

## "401" Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This transaction allows you to edit information for surgical episodes. Data may include surgery/procedure date, surgical specialty, category of chief surgeon, category of first assistant, principal anesthetic technique, source of payment, and operation codes. You may enter up to 5 ICD-9 or up to 25 ICD-10 operation codes per surgical episode. For discharges prior to 10-1-87, only 2 episodes per date were allowed. For discharges after 10-1-87, 3 surgical episodes per date are allowed.

## "801" Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This transaction allows editing of data pertaining to professional services. You must select which professional service date/time to edit or create a new professional service. Existing related diagnosis codes may be edited or new diagnosis codes may be added as long as long as they do not exceed 8 related diagnosis codes per CPT code. Existing CPT codes may be edited or new CPT codes may be added. The user can select to send the 801 transaction to PCE at the completion of the 801 entry.

## "601" Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This transaction allows editing of data pertaining to procedures performed. Existing procedures may be edited or new procedures may be added. You may enter up to 5 ICD-9 or up to 25 ICD-10 procedure codes per date. If receiving dialysis, data pertaining to the number of treatments per procedure date will be contained in this transaction.

The "101" and "701" transaction data displayed consists of fields from both the PATIENT file and the PTF file. The fields that are indented in this segment are PATIENT file fields. The option allows you to "jump" from one prompt to another by entering an up-arrow \<^\> and the first few letters of the desired prompt; however, this can only be done between prompts for fields in the same file.

Five items which come from the admission record cannot be entered/edited through this option: ADMISSION DATE, DISCHARGE DATE, DISCHARGE SPECIALTY, TYPE OF DISPOSITION, and MEANS TEST INDICATOR; however, this data can be edited through this option on a non-VA PTF record (except for ADMISSION DATE). The ADMISSION DATE for a non-VA PTF record can be edited through the PTF option, Load/Edit PTF Data.

Transfer DRGs are updated on VA PTF records when this option is exited in order that any DRG reports subsequently run which include that PTF record will contain current Transfer DRGs based on what has been coded.

A description of most of the fields found in the different PTF transactions is provided at the end of this option documentation.

## Diference between VA PTF and Non-VA PTF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Differences between the VA PTF and the non-VA PTF are explained below.

### Admission Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no corresponding admission record for the non-VA PTF...

An admission record is created upon admission to a VA medical center. Since the non-VA PTF only applies to admissions to private facilities, there is no admission record for non-VA PTF.

### Automatic Updating

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automatic updating does not occur on the non-VA PTF...

Since the automatic updating matches the PTF with the associated admission record and there is no associated admission record for the non-VA PTF, it cannot be updated. All data on the non-VA PTF is entered by the system from the PATIENT file or entered by the user during the load/edit process. However, updating will occur for demographic information.

### Discharge Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Discharge information is entered directly during load/edit process on the non-VA PTF...

Discharge information is retrieved for the VA PTF from the admission record and cannot be edited through PTF. Since there is no admission record for the non-VA PTF, the discharge information is entered by the user through the Load/Edit PTF Data option.

## Select 401 Surgery Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If at the "Select 401 SURGERY DATE" prompt or the “Select PROCEDURE" prompt, you enter a date which is before the admission or after the discharge date, the following appropriate message will appear and the prompt will be repeated.

"Not after discharge ??"

"Not before admission ??"

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

"101" FACILITY Facility number where patient

& was admitted.

"701"

SUFFIX Suffix of admitting facility

SOURCE OF ADMISSION Source of this patient admission;

from SOURCE OF ADMISSION file

SOURCE OF PAYMENT For patients treated at non-VA

hospitals at VA expense; from

set of codes

TRANSFERRING VA facility from which the

FACILITY patient was transferred

TRANSFERRING SUFFIX Suffix of transferring facility

ENTER THE ELIGIBILITY For patients with dual eligibility, the

FOR THIS ADMISSION eligibility associated with the

admission

SPINAL CORD INJURY Code which indicates if this

patient sustained a spinal cord

injury and, if so, what type

DATE OF BIRTH Patient's date of birth

AGENT ORANGE Was patient exposed to Agent

EXPOS. INDICATED Orange? Yes/No/Unknown

RADIATION EXPOSURE How was patient exposed to

METHOD radiation? Hiroshima-Nagasaki

/Nuclear Testing/Both

RELATED TO MST Was this treatment related to Military

Sexual Trauma? YES/NO/UNKNOWN/

DECLINED TO ANSWER (This will

only be prompted if the patient’s MST

Status is YES).

COMBAT VETERAN YES/NO/UNKNOWN

Did the patient see combat service?

PROJ 112/SHAD YES/NO

Was patient exposed to Shipboard

Hazard and Defense?

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

"101" TREATMENT FOR HEAD/ Was the treatment related to Head

& NECK CA and or Neck Cancer?

“701”

POW CONFINEMENT War in which patient was a

LOCATION prisoner of war

MEANS TEST Represents patient's Means Test

INDICATOR status

DISCHARGE Specialty from which patient

SPECIALTY was discharged

ZIP+4 5 or 9 digit zip code

TYPE OF Disposition type for this patient

DISPOSITION for this episode of care (i.e.,

Regular, Transfer, Irregular)

DISCHARGE STATUS Status of patient at time of

discharge (i.e., On pass, Bed

occupant)

PLACE OF Where patient is going upon

DISPOSITION discharge from this hospital

episode; from the PLACE OF

DISPOSITION file

OUTPATIENT Will patient receive outpatient care

TREATMENT after discharge? Yes/No

VA AUSPICES Will VA pay for continued medical

care for this patient after

discharge? Yes/No

RECEIVING FACILITY Facility number of VA medical center

to which patient is being transferred

RECEIVING SUFFIX Suffix of receiving facility

C&P STATUS Code that indicates the Compensation

and Pension status of patient; from

set of codes

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

“101” ASIH DAYS For nursing home or domiciliary

& patients, number of days patient

“701” was absent due to admission to a

hospital

PRINCIPLE DIAGNOSIS ICD diagnosis code responsible

for patient's major length of stay

for this hospital episode; from ICD

DIAGNOSIS file. Used for DRG

calculation.

PRESENT ON ADMISSION Indicates whether or not the diagnosis

was present on admission (for ICD-10

codes only). The Principle and all of

the Secondary Diagnoses fields

require an associated POA value. One

of the following values should be

assigned in accordance with the

official coding guidelines:

Y = present on the time of inpatient

admission

> N = not present on the time of

inpatient admission

U = documentation is insufficient to

determine if condition is POA

W = provider is unable to clinically

determine whether condition

was POA

1 = exempt

SECONDARY DIAGNOSIS ICD-9 code of second, third....,

twelfth diagnoses for this patient;

from ICD DIAGNOSIS file

ICD-10 code of second, third,…,,

Twenty-fourth diagnoses for this

Patient; from ICD DIAGNOSIS file

PRESENT ON ADMISSION This is the Present on Admission

(POA) indicator for Secondary

Diagnoses. For every Secondary

Diagnosis entered, a POA indicator is

also required. The choices are the

same as for the POA PRINCIPAL

DIAGNOSIS field.

"501" MOVEMENT DATE Date of patient movement - movements

must be more than 24 hours apart and

involve a specialty change to be

counted

LOSING SPECIALTY Name of specialty patient left in

this patient movement

LEAVE DAYS Number of days patient was on leave

(an absence of more than 96 hours

but not more than 14 days) from a

specialty during this patient

movement

PASS DAYS Number of days patient was on pass

(an absence of less than 96 hours)

from a specialty during this

patient movement

TREATED FOR SC/IR/ Indicates whether or not treatment

AO/SWAC CONDITION was for a service-connected condition,

related to ionizing radiation exposure,

Agent Orange exposure, or SW Asia

conditions exposure. These will

appear as separate prompts.

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

“501” TREATMENT FOR MST Identifies whether treatment was for

Military Sexual Trauma.

TREATMENT FOR Identifies whether treatment was for

HEAD/NECK CA Head and/or Neck Cancer.

TREATMENT RELATED Was this treatment related to combat?

> TO COMBAT

TREATMENT RELATED Was this treatment related to

TO PROJ 112/SHAD Shipboard Hazard and Defense?

TREATED FOR Was this treatment for

ACUTE SUICIDAL CRISIS Acute Suicidal Crisis?

COMPACT Start Date Date of the Start of the COMPACT Act Episode of Care

COMPACT Remaining Days Number of Remaining Days for the COMPACT Act Inpatient Benefit (30 days or less)

COMPACT End Date Date of the End of the COMPACT Act Episode of Care

ICD 1 ICD diagnosis code responsible

for patient's major length of stay on a

specialty; from ICD DIAGNOSIS file

POA FOR ICD 1 This is the Present on Admission

(POA) indicator for ICD 1. One of the

Following values should be assigned in

accordance with the official coding

guidelines:

Y = present on the time of inpatient

admission

N = not present on the time of

Inpatient admission

U = documentation is insufficient to

determine if condition is POA

W = provider is unable to clinically

determine whether condition was

POA

1 = exempt

ICD 2-5 ICD-9 diagnosis code of second,

third..., fifth diagnoses responsible

for patient's stay on a specialty;

from ICD DIAGNOSIS file

ICD 2-25 ICD-10 diagnosis code of second,

third,…,twenty-fifth diagnoses

responsible for patient’s stay on a

specialty; from ICD DIAGNOSIS

file

POA FOR ICD 2-25 This is the Present on Admission

(POA) indicator for ICD-10 codes 2-25.

For every ICD code entered, a POA

indicator is also required. The choices

are the same as for the

POA FOR ICD 1 field.

"401" SURGICAL SPECIALTY Surgical specialty code associated

with the chief surgeon for each

surgery episode; from the SURGICAL

SPECIALTY file

CATEGORY OF CHIEF Code indicating the category of the

SURGEON chief surgeon for patient's surgical

episode(s); from set of codes

CATEGORY OF FIRST Code indicating the category of the

ASSISTANT first surgical assistant for

patient's surgical episode(s); from

set of codes

PRINCIPAL ANESTHETIC Code indicating the major type of

TECHNIQUE anesthetic method used for

patient's surgical episode(s); from

set of codes

SOURCE OF PAYMENT Source of payment for patients

operated on in a non-VA facility

and returned to a VA facility

within a 24 hour period

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

“401” OPERATION CODE ICD-9 Operation code(s) of patient's

surgical episode(s); up to five

operation codes allowed per each

surgical episode; from ICD

OPERATION/PROCEDURE file

ICD-10 Operation codes(s) of

patient’s surgical episode(s);up to

twenty-five operation codes

allowed per each surgical episode;

> from the ICD

> OPERATION/PROCEDURE file

"801" PROFESSIONAL SERVICE Must have a date/time value between

DATE/TIME the date/time of admission and the

date/time of discharge

REFERRING OR Name of provider ordering the service

ORDERING PROVIDER

RENDERING PROVIDER Name of provider performing the

service

RENDERING LOCATION Location where service is performed

CPT CPT/HCPCS codes used for a patient

CPT MODIFIER Used to indicate a service or procedure

has been altered

QUANTITY Used to indicate the number of times

the procedure was done

PRIMARY DIAGNOSIS Primary diagnosis associated with the

procedure performed.

SECONDARY DIAGNOSIS Secondary diagnoses associated with

the procedure performed.

TREATED FOR SC/AO/ Was this treatment for a service-

IR/SWAC/MST/HEAD and/or connected condition or related to

NECK CA CONDITION agent orange exposure, ionizing

radiation exposure, SW Asia

conditions exposure, military sexual

trauma, or head and/or neck cancer?

These will appear as separate prompts.

COMBAT VET Was this treatment related to combat?

PROJ 112/SHAD Was this treatment related to

Shipboard Hazard and Defense?

> FIELD NAME/SCREEN TITLE OF PROMPT DESCRIPTION

"601" PROCEDURE DATE Date procedure performed

PROCEDURE CODE ICD-9 Procedure Code Number for

first,…fifth procedure for selected

procedure date

ICD-10 Procedure Code Number

for first,..twenty-fifth procedure

for selected procedure date

NUMBER OF DIALYSIS Number of dialysis treatments which

TREATMENTS *(prompt appears* occurred on the selected procedure

*only for select procedure codes)* date

# Release PTF Records for Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release PTF Records for Transmission option is used to update the status of PTF records which have been CLOSED by Health Information Management Section to RELEASED status. This status indicates the records are complete for transmittal to Austin. The data from the released PTF record is electronically sent to the Austin Information Technology Center (AITC), where it is used to compute the Diagnostic Related Groups (DRGs) for resource allocation to the hospital.

This option does not do the actual transmission of data to Austin. It creates an entry for the PTF record in the PTF RELEASE file where it is stored for later transmission through the VADATS PTF Transmission option.

Only holders of security key DG PTFREL may access this option.

You will be prompted for the PTF record you wish to release. You may enter double question marks (??) at the prompt for a list of PTF records with a CLOSED status.

When a PTF record is released, any 801 entries associated with that record that have not been transmitted to PCE, will be transmitted.

# Set Up Non-VA PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create a PTF for a veteran being treated at VA expense in a private facility. The user may enter only those patients who are already established in the PATIENT file. The system creates the new PTF and enters information from the PATIENT file into the PTF. To set up a non-VA PTF record for a patient who is not in the PATIENT file, the user must first use the Registration Menu option, Register a Patient, to establish the patient in the PATIENT file and then utilize this option.

A PTF record profile is displayed for the selected patient. This contains the PTF#, status, and admission date for the patient's last 15 PTF records.

Once the non-VA PTF is created for the patient, the "101" screen is displayed. Information may be entered and edited on this and the other PTF screens as described in the Load/Edit PTF Data option documentation.

A note regarding functionality that is specific to Non-VA PTF records: Patch DG\*5.3\*1057 introduces a new field called Initial Date of Service, which can be up to 72 hours prior to the Admission Date. This date can be entered during the Set Up Non-VA PTF Record process and can be entered or edited (only for Non-VA PTF records) via the Load/Edit PTF Data option, on the \<101\> screen, section \[1\]. This new field facilitates the ability to enter surgical \<401\> and Procedure \<601\> movements up to 72 hours prior to the Admission Date.

It should be noted that the PTF information entered through this option does not affect Bed Control files.

# Update DRG Information Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Update Transfer DRGs for Current FY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update Transfer DRGs for Current FY option is used to update/recalculate the Transfer DRGs for all PTF records that were active anytime in the current fiscal year. This process does not apply to non-VA PTF (Fee Basis) records.

You should run this option after the installation of a new DRG Grouper.

The line "TRANSFER DRG update in progress...on PTF \# {number}" will appear once for every 300 PTF records updated.

# Utility Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## 099 Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 099 Transmission option is used to delete the master record at the Austin Information Technology Center (AITC) by electronically transmitting a 099 record. For non-free-form transmissions, use of this option deletes the entire master record in Austin and changes the PTF status of the record at the local facility from TRANSMITTED to OPEN. Upon reopening, the corresponding PTF entries in the PTF CLOSE OUT file and in the PTF RELEASE file are deleted. Once this record is edited and closed again, the entire record can then be retransmitted to the AITC.

A free-form 099 transaction may also be sent through this option. This would be used to delete a master record in Austin where the SSN or admission date had been entered incorrectly or a pseudo social security number had been used and you now have the correct number.

Electronic MailMan messages are generated through the use of this option. The sender will receive these messages in his/her IN basket. The first message shows how the data was actually sent. A "Q"uery at this message will provide the status of the message and the message number. This number can be checked against the message number in the response from Austin to aid in matching up messages with the correct response. The second message is the response from Austin showing that the data was received or not received and the reason why. This is sent to members of the PTI mail group.

Only holders of security key DG PTFTRANS may access this option. You may not utilize this option while other records are being transmitted.

Utilizing this option creates an entry in the PTF Transaction Request Log. You may generate this log through the Print Special Transaction Request Log option, Utility Menu, PTF Menu.

A transmit flag allows transmission to be enabled/disabled for receiving users and their mail router domains (locations set up to receive the transmissions). If disabled for all receiving users, the following message will be displayed.

"Transmission is turned OFF for receiving domains in TRANSMISSION ROUTERS file

Cannot transmit code sheet!"

## Record Print-Out (RPO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Record Print-Out (RPO) option is used to generate a record print-out request to the Austin Information Technology Center (AITC). You may request a print-out of a specific admission (N150) or a print-out of all admissions for a selected patient at a selected VA medical center (N151). With this functionality, medical center personnel may obtain specific medical information on a patient from another part of the country who is at their facility temporarily.

The date/time of admission and admission facility number/suffix cannot be filled in for the 151 transaction.

Electronic MailMan messages are generated through the use of this option. The sender will receive these messages in his/her IN basket. The first message shows how the data was actually sent. A "Q"uery at this message will provide the status of the message and the message number. This number can be checked against the message number in the response from Austin to aid in matching up messages with the correct response. The second message is the response from Austin showing that the data was received or not received and the reason why. This is sent to members of the PTI mail group.

Utilizing this option creates an entry in the PTF Transaction Request Log. You may generate this log through the Print Special Transaction Request Log option, Utility Menu, PTF Menu.

A transmit flag allows transmission to be enabled/disabled for receiving users and their mail router domains (locations set up to receive the transmissions). If disabled for all receiving users, the following message will be displayed: "Transmission is turned OFF for receiving domains in TRANSMISSION ROUTERS file Cannot transmit code sheet!"

Only holders of security key DG PTFTRANS may access this option. You may not utilize this option while other records are being transmitted.

## Add/Edit Suffix Effective Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit Suffix Effective Date option is used to add/edit/delete the effective date multiple of the FACILITY SUFFIX file (#45.68). The current status of the selected facility suffix is displayed prior to and after editing.

It is important to remember to add a new effective date and not just edit the initial effective date. Each suffix must have at least one effective date, allowing sites to maintain a history of when suffixes became active/inactive.

Only holders of security key DG PTFSUP may access this option.

## Delete PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete PTF Record option is used to delete an entire PTF record from the system. Only PTF records with an OPEN status can be deleted.

If it becomes necessary to recreate a PTF record after it has been deleted, this may be accomplished through the Establish PTF Record from Past Admission option.

The Delete PTF Record option is only available to holders of security key DG PTFREL.

## Establish PTF Record from Past Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Establish PTF Record from Past Admission option is used to create a PTF record for an admission that does not have a corresponding PTF record. This may occur if the patient was admitted before ADT V. 3.21 or if the PTF record had been deleted for some reason.

After selecting the patient name, the system will prompt for the admission date. To prevent duplicate PTF records for the same admission, an admission date for which a PTF record already exists will not be accepted at this prompt.

## Print Special Transaction Request Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Special Transaction Request Log option allows the user to generate a listing of special transaction requests. These include the following.

099 - used to delete the master record at the Austin Information Technology Center (AITC)

150 - request a print-out of a specific admission for a patient

151 - request a print-out of all admissions for a selected patient at a selected VA medical center

You may choose to print a listing of a single special transaction type or ALL types. You will be prompted for a date range, which type of special transaction should be included in the output, and a device. The default date at the "Start with DATE OF REQUEST" prompt will be the date the first entry was made into the log.

The log contains the date initiated (date request entered into log), user, block (type of special transaction), patient's SSN, admission date, and admission facility for each entry, if applicable.

If there are no entries in the log for the date range selected, you will be so notified.

## PTF Expanded Code Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The load/edit options in PTF will no longer allow the selection of ICD codes that were VA specific in nature (codes with a three-character suffix). PTF codes will now be prompted with additional questions when certain standard ICD codes are selected; i.e., certain substance abuse diagnoses will now ask for the substance. The PTF Expanded Code Listing option will generate a listing of all the ICD codes that now require additional questions.

These codes are currently grouped into five categories - KIDNEY TRANSPLANT STATUS, LEGIONNAIRE'S DISEASE, PSYCHIATRY AXIS CLASSIFICATION, SUBSTANCE ABUSE, and SUICIDE INDICATOR.

You may choose to print the list for a single category, a range of categories, or all categories. The same applies to the ICD code numbers. If you wish to sort from the first category/code but not to the last, you must enter the category name/

diagnosis procedure code at the applicable prompt instead of accepting the default of FIRST.

The category name must be entered in uppercase letters. If a range of categories is being selected, they must be entered in proper sequence (alphabetical order).

The output should be generated at a 132 col. margin width. For each selected code, it will contain the ICD code number, name, category, and inactive date, if applicable.

The data contained in the additional question fields will appear on the 101, MAS, 401, 501, and 701 PTF screens when present.

## Purge Special Transaction Request Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Special Transaction Request Log option allows the user to purge special transaction requests. These include the following.

099 - used to delete the master record at the Austin Information Technology Center (AITC)

150 - request a print-out of a specific admission for a patient

151 - request a print-out of all admissions for a selected patient at a selected VA medical center

You may choose to purge a single special transaction type or ALL types. You will be prompted for a date range, which type of special transaction should be purged, and verification of the date range and type of transaction(s) involved. The default date at the "Start with DATE OF REQUEST" prompt will be the date the first entry was made into the log.

If there are no entries in the log for the date range and transaction type selected, you will be so notified.

Utilization of this option will produce a mail bulletin showing the purge has completed, the record format, and total number of records deleted.

## Set Transmit Flag on Movements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set Transmit Flag on Movements option allows the supervisor to flag 501 or 535 movements for transmittal purposes.

If a PTF record has more than 25 501 or 535 movements (a limitation set by Austin), the record cannot be closed or transmitted. If you attempt to close a record through the Load/Edit PTF Data option which exceeds this limitation, the following message will appear.

"{501/535} There are {'#'} movements but only '25' can be sent to Austin. \*\*\* Contact PTF supervisor \*\*\*".

The purpose of the Set Transmit Flag on Movements option is to allow the supervisor to select which movements should not be transmitted.

Only PTF records with more than 25 501 or 535 movements may be selected. You may enter a \<?\> at the "select" prompts for a list of movements. You cannot flag discharge movements or 501 movements which have a transfer DRG associated with them. These movements will not be listed for selection.

Although this option allows you to flag a movement to "YES TRANSMIT", the purpose of the option is to flag those movements which should not be transmitted.

## Validity Check of PTF Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Validity Check of PTF Record option is used to perform a validation of the data contained in the PTF record. The validity check performed in this option is the same validity check performed at the time of closeout. A PTF record cannot be closed until it passes the validity check.

Four checks (edits) are initially performed on the PTF record during this option. The first review checks to see that facility number and discharge date are completed and that a DRG has been calculated. Because the PTF cannot be closed if PTF messages are remaining, the second review checks to see that all PTF messages are cleared. The user is given the opportunity to delete any PTF messages remaining at this time.

Thirdly, the PTF is checked to see that required fields are completed and that numeric fields do not have non-numeric characters and vice versa. Lastly, the record is checked for inconsistent data fields.

Each edit is not applied until the record has passed all preceding edits. For example, if the first two checks were passed, but not the third, the system would list the blank fields. If there were any inconsistent data fields contained in this record, these would not be displayed until all the blank values were completed.

If the record passes the verification process, the user will receive an electronic mail message in his/her IN mailbox from POSTMASTER showing the data contained in the PTF record in code form.

If the record does not pass the check, a list of incorrect fields is displayed on the screen. The list provides the transaction number, field name, column number from the transaction coding sheets, and reason for rejection. If the field is from the 501 transaction, the date of the movement will also be displayed. Correcting the PTF record fields is accomplished through the Load/Edit PTF Data option.

Additional edit checks were added with PIMS V. 5.3. If the record does not pass these checks, a List Manager screen will appear displaying the inconsistencies for viewing only. The error listing resembles the EAL report from Austin. These inconsistencies cannot be corrected through the List Manger screen. This is accomplished through the Load/Edit PTF Data option.