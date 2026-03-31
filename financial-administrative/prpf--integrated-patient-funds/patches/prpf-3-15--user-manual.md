---
title: PRPF*3*15 PFOP Data Diagnostic Patch User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: PFOP Data Diagnostic Patch
app_code: PRPF
app_name: Integrated Patient Funds
section: FIN
app_status: active
pkg_ns: PRPF
patch_ver: 3
patch_id: PRPF*3*15
group_key: "PRPF:PRPF:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 10%\\" /> <col style=\\"width: 13%\\" /> <col style=\\"width: 33%\\" /> <col style=\\"width: 20%\\" /> <col style=\\"width: 21%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><blockquote> <p><strong>Version</strong></p> </blockquote></th> <th><blockquote> <p><strong>Section Ch"
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - blank
  - style
  - width
  - even
  - table
  - cannot
  - patient
page_count: 0
word_count: 9422
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/prpf_datamigrationpatchuserguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/prpf_datamigrationpatchuserguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=46"
---

> Veterans Personal Finance System (VPFS)

Personal Funds of Patients (PFOP) Data Diagnostic Patch User Guide

> PRPF\*3.0\*15

![](prpf-3-15-pfop-data-diagnostic-patch-user-guide/001.png)

> November 3, 2006

> U.S. Department of Veterans Affairs Health Systems Design & Development

> History of Revisions

> History of Revisions

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Changed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Effective Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contacts</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0.1</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>New document created from selected sections of the VistAMigrate Data Migration Guide to facilitate use of M Patch PRPF*3.0*15.</p>
</blockquote></td>
<td><blockquote>
<p>9/02/2005</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.2</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected numbering of items in table.</p>
</blockquote></td>
<td><blockquote>
<p>09/08/05</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.3</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>10/10/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.4</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>10/14/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>11/1/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.6</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>11/4/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.7</p>
</blockquote></td>
<td><blockquote>
<p>Appendix B.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>11/7/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.8</p>
</blockquote></td>
<td><blockquote>
<p>Footer changes.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid date on all page footers.</p>
</blockquote></td>
<td><blockquote>
<p>11/7/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.9</p>
</blockquote></td>
<td><blockquote>
<p>Appendix B.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15</p>
</blockquote></td>
<td><blockquote>
<p>11/8/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.10</p>
</blockquote></td>
<td><blockquote>
<p>Appendix B.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in table and patch from review results associated with P15 and patch user doc</p>
</blockquote></td>
<td><blockquote>
<p>11/21/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.11</p>
</blockquote></td>
<td><blockquote>
<p>Appendix B.</p>
</blockquote></td>
<td><blockquote>
<p>Corrected invalid information in</p>
</blockquote></td>
<td><blockquote>
<p>11/21/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>appendix A</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0.12</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>Turn off tracking doc changes for initial distribution</p>
</blockquote></td>
<td><blockquote>
<p>12/06/05</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.13</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>Turn on tracking doc changes and update information on Patient Type in the appendix</p>
</blockquote></td>
<td><blockquote>
<p>01/10/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.14</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A and B</p>
</blockquote></td>
<td><blockquote>
<p>Update Appendix with information from P15T31</p>
</blockquote></td>
<td><blockquote>
<p>02/13/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.15</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A and B</p>
</blockquote></td>
<td><blockquote>
<p>Update Appendix with information from review with Tami</p>
</blockquote></td>
<td><blockquote>
<p>02/14/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.16</p>
</blockquote></td>
<td><blockquote>
<p>1.1, 1.3.3,</p>
<p>Appendix A</p>
</blockquote></td>
<td><blockquote>
<p>Updates from final review items from Tami and business rules updates from Stefan</p>
</blockquote></td>
<td><blockquote>
<p>02/24/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.17</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>Implemented changes per WPR Issues Resolution Log from SEPG/SQA 4/4/06</p>
</blockquote></td>
<td><blockquote>
<p>6/12/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.18</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A</p>
</blockquote></td>
<td><blockquote>
<p>Change to line item 47 in Table A-1, added comment for same.</p>
</blockquote></td>
<td><blockquote>
<p>6/26/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.19</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A</p>
</blockquote></td>
<td><blockquote>
<p>Revised comment for line item 47 in Table A-1.</p>
</blockquote></td>
<td><blockquote>
<p>6/30/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.20</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A</p>
</blockquote></td>
<td><blockquote>
<p>Revised comment for line item 14 in Table A-1.</p>
</blockquote></td>
<td><blockquote>
<p>10/26/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.21</p>
</blockquote></td>
<td><blockquote>
<p>Appendix A</p>
</blockquote></td>
<td><blockquote>
<p>Corrected spelling on page A-5 and A-10.</p>
</blockquote></td>
<td><blockquote>
<p>11/03/06</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  [Objective 2](#_bookmark1)
2.  [Overview of Steps in the M Environment 3](#_bookmark2)
3.  [Performing Diagnostics and Data Cleanup in the M Environment 3](#_bookmark2)
    1.  [Patient Funds Diagnostic Summary Report 4](#_bookmark3)
    2.  [Patient Funds Diagnostic Detail Report 4](#_bookmark3)
    3.  [Correcting Patient Funds Errors 5](#_bookmark4)

> List of Tables

> [Table A-1. Migration Business Rules....................................................................................................................... A-1](#Appendix_A._Migration_Business_Rules)

> [Table B-1. Description of Diagnostic Summary Report............................................................................................B-1](#Appendix_B._Diagnostic_Report_Samples)

<span id="About_This_Document" class="anchor"></span>About This Document

# About This Document


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [About This Document](#about-this-document)
  - [Document Purpose](#document-purpose)
  - [Document Audience](#document-audience)
  - [Conventions Used in this Document](#conventions-used-in-this-document)
  - [Additional Resources](#additional-resources)
- [Patch PRPF\3.0\15](#patch-prpf3015)
  - [Objective](#objective)
  - [Overview of Steps in the M Environment](#overview-of-steps-in-the-m-environment)
  - [Performing Diagnostics and Data Cleanup in the M Environment](#performing-diagnostics-and-data-cleanup-in-the-m-environment)
    - [Patient Funds Diagnostic Summary Report](#patient-funds-diagnostic-summary-report)
    - [Patient Funds Diagnostic Detail Report](#patient-funds-diagnostic-detail-report)
    - [Correcting Patient Funds Errors](#correcting-patient-funds-errors)

## Document Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of the Personal Funds of Patients (PFOP) Data Diagnostic Patch User Guide is to provide assistance with using MUMPS (M) Patch PRPF\*3.0\*15 to diagnose and clean data in the M environment prior to the data migration process.

## Document Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The audience for this document includes:

- Primary audience: Local Information Resource Management (IRM), Automated Data Processing Application Coordinator (ADPAC), Personal Funds of Patients (PFOP) staff responsible for diagnosing and cleaning data before migration, National Training and Education Office (NT&EO) responsible for training
- Others: Project Implementation Office (PIO)

## Conventions Used in this Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Format</strong></th>
<th><strong>Indicates…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>bold</strong></td>
<td><p>A control that you click, such as a button, icon, or link, or a field label.</p>
<p>Example: Click <strong>Deploy</strong>.</p></td>
</tr>
<tr class="even">
<td>Courier - normal</td>
<td><p>Text that appears on the screen or in a log file.</p>
<p>Example: Table created.</p></td>
</tr>
<tr class="odd">
<td>Courier - <strong>bold</strong></td>
<td><p>Text that you type.</p>
<p>SQL&gt;<strong>quit</strong></p></td>
</tr>
<tr class="even">
<td>&lt;<em>Courier&gt;</em> italic and enclosed in angle brackets</td>
<td><p>A variable that you replace with the specified text</p>
<p>Enter password: &lt;<em>sysDBA password</em>&gt;</p></td>
</tr>
</tbody>
</table>

## Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For the complete description of Patch 15 including installation instructions, see the documentation included with Patch 15.

> For additional documentation, such as the VistAMigrate Data Migration Guide, go to the Veterans Health Administration (VHA) Application Modernization website:

REDACTED

> <span id="_bookmark1" class="anchor"></span>1. Patch PRPF\*3.0\*15

# Patch PRPF\*3.0\*15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Objective

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The objective of PRPF\*3.0\*15 (Diagnostic Patch 15) is to allow sites to diagnose and resolve as many issues as possible before they migrate from VistA legacy Personal Funds of Patients (PFOP) to the Veterans Personal Funds System (VPFS). Install and use Diagnostic Patch 15 well in advance of your actual data migration date to allow time to run the diagnostic routine, review the reports, and make corrections in the M environment repeatedly to narrow down the count of errors. Although it is desirable, you do not need to cleanse your data 100%. It is important, however, to correct any data that violates the rules imposed by the FileMan data dictionary’s input transform for a field. Such data errors could cause the migration process to fail. For example, if the input transform says a field must be between 3 and 30 characters, but the actual data is 40 characters, this error should be corrected.

> Note: Patch 15 is a reporting tool only. It does not prevent records with errors from being extracted from the M environment. Later, when you run the Analyze step on your extracted data in the reengineered environment, records with errors will be moved to an error file and will *not* be migrated.

> Patch 15 does the following:

- Menu Option: Patch 15 adds a new menu option to the supervisor’s menu that allows users of the Patient Funds package to initiate a database diagnostic analysis. This database analysis is restricted to files relating to the Patient Funds package. The new menu option, Database Diagnostic Report \[PRPF DATA DIAGNOSTIC REPORT\], requires the PRPF SUPERVISOR key.
  - Summary Report: The database diagnostic analysis produces a diagnostic summary report of invalid or missing data elements, and a count of how many of each needs to be investigated. A prompt appears at the end of the summary report providing the option to produce the detail report.
  - Detail Report: The detail report includes specific break out information regarding all invalid or missing data elements that are in the summary report. For easy reference, error numbers in the detail report refer to error (or line) numbers in the summary report.

> Following is a sample of the Supervisor menu including the Database Diagnostic Report menu option:

> Select Patient Funds (INTEGRATED) System Option: 8 Supervisor Menu

1.  Add/Edit Patient Funds Forms
2.  Enter/Edit Remarks Codes
3.  Clear Account Lock
4.  Deferral Date Edit
5.  Productivity Report
6.  Update Patient Status for ALL Accounts
7.  Verify and Correct Balance
8.  Archive Patient Funds Transactions
9.  Summarize & Purge Patient Funds Transactions
10. Date Variance Report
11. Negative Balance Report
12. Database Diagnostic Report
    1.  <span id="_bookmark2" class="anchor"></span>Patch PRPF\*3.0\*15

> Select Supervisor Menu Option:

## Overview of Steps in the M Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Staff at the local site completes the following iterative steps in the M environment. Cycle through these steps repeatedly until you are confident that your data is cleansed to your needs and will migrate successfully.

1.  Diagnostics: Select menu option \[PRPF DATA DIAGNOSTIC REPORT\] to run the diagnostic routine in the M environment to check for errors, such as invalid date format or missing social security number (SSN).
2.  Review: Review the summary report that is produced by the diagnostic routine to identify errors that need to be corrected before migrating data to the reengineered application. When prompted at the end of the summary report, run the detail report if you need detailed information.
3.  Cleanup: Use the appropriate Veterans Health Information Systems and Technology Architecture (VistA) menu options to clean your data by correcting any data errors found in the summary and detail error reports produced by the diagnostic routine. You may need to get assistance outside the realm of PFOP to clean data for you, such as patient names, date of birth (DOB), or SSN.

> Notes: Cleanup should be performed by staff members who understand the data and the business rules. If necessary, authorized users can clean up the data by going into the M code using standard processes and documenting changes.

## Performing Diagnostics and Data Cleanup in the M Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Diagnostics and data cleanup is an iterative process that typically requires several cycles of error checking and correcting before data for the site can be migrated. The Diagnostic routine checks all of the data for a number of identified errors that may prevent the data from migrating successfully. The Cleanup routine produces both a summary and a detailed report, that you use as a reference to locate and correct data errors. You can print or view the reports online.

> Generally, you use the VistA menu options to correct errors. However, if this is not feasible, ask your local ADPAC representative to coordinate the cleanup of data owned by other groups.

> Note: All data cleanup cycles must be completed 2 weeks prior to the beginning of the actual data migration for the site. Several days before cutover, there will be one more run of the Diagnostic routine to check the data quality prior to beginning the data migration process.

> To access the Patient Funds Diagnostic reports:

1.  Log on to PFOP as PRPF Supervisor.
2.  Open the Patient Funds Supervisor Menu \[PRPF SUPERVISOR\].
3.  Select PRPF DATA DIAGNOSTIC REPORT.

> After a short period, dots appear to indicate that the report is running, the Patient Funds Diagnostic Summary report is displayed. The DEVICE: prompt appears.

> <span id="_bookmark3" class="anchor"></span>1. Patch PRPF\*3.0\*15

4.  Do any of the following:
    - Let the report print to the screen using ;132;999, then copy and paste the report to a text editor.
    - Turn on capture to file in KEA.
    - Enter a printer name to print both the summary and detail versions of the Patient Funds Diagnostic Summary report.

> DEVICE: \<*your_printer*\>

> Both reports are printed on the printer you specified. File the reports in the site’s data migration binder.

- Enter a file name to save both the reports to file.

> DEVICE: \<*folder*/*file_name*\>

> A file containing both versions of the report is saved to the location and file name that you specified.

- To exit without saving or printing the reports, enter the caret symbol (^).

### Patient Funds Diagnostic Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Funds Diagnostic Summary report is designed to be a quick and easy way for you to validate all data that will be involved with the migration of the Patient Funds package to the new VPFS application.

> The diagnostic report generates a Summary Report, which is intended to be a quick reference to the amount of data elements that are not validating correctly. The Summary Report contains the total number of patient accounts processed and the total balance of all patient accounts at the time the summary was generated. For a sample of this report, see Appendix B.

### Patient Funds Diagnostic Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At the end of the summary report a prompt appears asking if you would like to generate the detail report. Typically, the error count in the summary report provides all the information that you need to view your progress in cleaning up data and generating the detail report is not necessary.

> Note: The detail report can be quite large. Before you generate the detail report, check the notation at the end of the summary report indicating how many lines will be in the detail report. (See the highlighted text in the sample below.)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE: In addition to the summary report there is an available detail

> report, this report can be sent to any device or flat file if required.

> \>\>\>\>\> The detail diagnostic report will contain 2550 lines.

> If you still desire the detail report, then please input the name of the device that the report will be sent to.

> If the detail report is not desired then input "^" at the device prompt and the detail report will not print.

> DEVICE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> To access the detail report, at the DEVICE prompt, do one of the following:

- To display the report on the screen, accept the defaults.
  1.  <span id="_bookmark4" class="anchor"></span>Patch PRPF\*3.0\*15
- To print the report, enter the name of a printer.
- To save the report to a flat file, enter a file name.
- To return to the Supervisor's Menu without displaying, printing, or saving the report, enter ^. The detail report records consist of a series of data fields (STATION ID,ERR#,NAME,DESC,VALUE).

> Each field is separated by the delimiter “^”. All detail records can be imported into a spreadsheet and sorted or generated into other reports. The detail report is sorted by default in the order of Station-id then by error number and then by patient name. For a sample of this report, see Appendix B.

- VPFS data: If an asterisk (\*) appears by the error number on the summary report, the data for the field is owned by VPFS and can be edited by VPFS. Patient Funds staff can use the appropriate VistA Patient Funds menu options to correct the data for each patient.
- Non-VPFS data: If no asterisk (\*) appears by the error number on the summary report, the data for the field is not editable by Patient Funds staff. Contact your ADPAC to coordinate changes to data that is owned by other packages.

### Correcting Patient Funds Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides tips for correcting errors in the M environment.

> Note: If you cannot correct the error through the local VistA legacy application, or if there are too many of a certain type of error to correct easily manually, follow the appropriate chain of command to escalate the issue. This may include asking the Enterprise VistA Support (EVS) team for assistance.

- Use the appropriate VistA Patient Funds menu options to make your corrections.
- It is highly recommended that you keep a log of the corrections you make and store the log in your site’s Data Migration binder. The log should note what the errors were, who corrected them, and the date corrected.
- Decide how to handle cases where required data is missing. You may decide to replace missing data with a default value. For example: If a date field is missing the day part of the date, provide a default day value such as “01.” Be sure to document your decisions and document any data that you will need if you decide to re-enter any records or data after cutover.
- Repeat the Diagnosis and Data Cleanup process until the Summary Report shows a count of 0 for any actual errors, or until the site data owners have decided that the data is sufficiently clean to migrate even if it still contains errors that will not stop the automated migration process.
  - It is recommended that you hold a weekly data cleanup review to share findings with other sites to improve the process and to ensure successful migration for all sites. Sites can work together to:
    - Develop consistent approaches for specific kinds of errors. For example: In the case of missing data in the day field, sites may decide to make the correction the same way, such as entering 1 for a missing day.
    - Share frequently asked questions (FAQs).
    - Recommend modifications to diagnostic routines.

> <span id="Appendix_A._Migration_Business_Rules" class="anchor"></span>Appendix A. Migration Business Rules

> Appendix A. Migration Business Rules

> The table in this appendix is intended for users who are ready to attempt to migrate their data to the reengineered environment. It lists the minimum requirements that each data element must meet in order for a record to be migrated to the new database.

> Unless otherwise stated, blank values are allowed.

> Note: The diagnostic routine that you run via the new menu option Database Diagnostic Report \[PRPF DATA DIAGNOSTIC REPORT\] and in VistAMigrate will identify invalid or missing data. Data not meeting the Minimum Requirements to Migrate in the table below needs to be corrected because records not meeting these requirements will *not* be migrated to VPFS. Errors that violate the rules imposed by the FileMan data dictionary’s input transform could cause the migration process to fail, so it is especially important to correct them.

> Migration Business Rules

> Table A-1. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>NAME, #.01</td>
<td>Patient name cannot be blank.</td>
<td>Patient name cannot be blank.</td>
<td>Pointer to File 2</td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>NAME, #.01</td>
<td><p>Patient name cannot contain values other than alpha characters, one comma, apostrophe, and space after first name.</p>
<p>Must be 3-30 characters,</p></td>
<td>Patient name must be 3-30 characters.</td>
<td><p>Some names being migrated will contain data that is considered invalid now (special characters) but was valid in the past.</p>
<p>Pointer to File 2</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>SSN, #50</td>
<td>SSN cannot be blank.</td>
<td>SSN cannot be blank.</td>
<td>Computed from File 2, #.09</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>SSN, #50</td>
<td>SSN must be 9 digits.</td>
<td>SSN must be 9 digits or 9 digits followed by a ‘P’ to allow for pseudo-SSN.</td>
<td><p>Allow ‘P’ as an optional 10<sup>th</sup> character for pseudo-SSN.</p>
<p>Computed from File 2, #.09</p></td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>File</strong></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td>470</td>
<td>SSN, #50</td>
<td>SSN cannot be a duplicate.</td>
<td><p>SSN cannot be a duplicate at <em>any</em></p>
<p>station.</p></td>
<td>Computed from File 2, #.09</td>
</tr>
<tr class="even">
<td>6</td>
<td>470</td>
<td>SSN, #50</td>
<td>SSN contains pseudo SSN value.</td>
<td>Not an error; pseudo-SSN values are allowed.</td>
<td>Computed from File 2, #.09</td>
</tr>
<tr class="odd">
<td>7</td>
<td>470</td>
<td>DOB, #51</td>
<td>DOB cannot be blank.</td>
<td>DOB cannot be blank.</td>
<td>Computed from File 2, #.03</td>
</tr>
<tr class="even">
<td>8</td>
<td>470</td>
<td>DOB, #51</td>
<td>DOB must be a valid VistA date.</td>
<td><p>DOB must be 7 digits, in VistA date format.</p>
<p>Imprecise dates will be defaulted to the first of the month or year during migration.</p></td>
<td><p>Imprecise dates having a ‘00’ for the month and/or day will be defaulted to ‘01’.</p>
<p>Computed from File 2, #.03</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>470</td>
<td>WARD, #52</td>
<td>Ward must be 2-30 characters.</td>
<td>Ward must be 2-30 characters.</td>
<td>Computed from File 2, #.1</td>
</tr>
<tr class="even">
<td>10</td>
<td>470</td>
<td>CLAIM NUMBER, #53</td>
<td>Claim Number must be ‘SS’ or 7-9 digits.</td>
<td>Claim Number must be 'SS' or 7-9 digits.</td>
<td>Computed from File 2, #.313</td>
</tr>
<tr class="odd">
<td>11</td>
<td>470</td>
<td>ZIP CODE, #59</td>
<td>ZIP Code must be 5 digits.</td>
<td>Not migrated.</td>
<td>Computed from File 2, #.116</td>
</tr>
<tr class="even">
<td>12</td>
<td>470</td>
<td>REGIONAL OFFICE, #8</td>
<td>NA</td>
<td>Not migrated.</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>2</td>
<td>INTEGRATION CONTROL NUMBER (ICN), #991.01</td>
<td>ICN cannot be a duplicate.</td>
<td><p>ICN cannot be duplicate at <em>any</em></p>
<p>station.</p></td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>2</td>
<td>ICN, #991.01</td>
<td>ICN must be at least 1 character.</td>
<td>ICN must be 1-10 digits, optionally followed by a ‘V’ and a 6 digit checksum. An additional 6 digit prefix and 6 digit suffix are allowed for future use.</td>
<td>Allows current ICN format (10V6), with or without the checksum, and future ICN format (16V12). Note: This will not effect migration and does not need to be corrected.</td>
</tr>
</tbody>
</table>

Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>PROVIDER AUTH RESTRICT, #10.7</td>
<td>Provider Name cannot contain values other than alpha characters, one comma, apostrophe, and space. (Must meet VistA standard naming requirements.)</td>
<td>Provider Name must be 3-30 characters.</td>
<td><p>M Diagnostic Summary: item only validates name if present. This field can be blank. It is not associated with item #20 and will not increment the report counter if an error is registered on item #20.</p>
<p>Pointer to File 200 source.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>DATE OF CURRENT RESTRICTION, #10.5</td>
<td>Date of Current Restriction must be a valid VistA date.</td>
<td><p>Date of Current Restriction must be 7 digits in VistA date format.</p>
<p>Imprecise dates are not allowed.</p>
<p>Cannot be blank if patient type is restricted (R) or limited unrestricted (L).</p></td>
<td>Month or day cannot be 00.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td></td>
<td>Demographic record</td>
<td>Missing demographic record for account. Record must be present.</td>
<td>Demographic record must exist for account.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>ACCOUNT STATUS, #1</td>
<td>Account Status must be A, I or blank.</td>
<td>Account Status must be A, I, or blank. Blanks will be defaulted to A during migration.</td>
<td><p>A nightly update process will set active/inactive: if zero balance &amp; no transactions for 30+ days, set to I.</p>
<p>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>PATIENT TYPE, #2</td>
<td>Patient Type must be L, R, U, X or blank.</td>
<td>Patient Type must be L, R, U, X, or blank. Blanks will be defaulted to U during migration.</td>
<td>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>PROVIDER AUTH RESTRICT, #10.7</td>
<td>Provider Name cannot be blank if the Patient Type is restricted or limited unrestricted.</td>
<td>Provider Name cannot be blank if the Patient Type is restricted (R) or limited unrestricted (L).</td>
<td></td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>PATIENT STATUS, #3</td>
<td>Patient Status must be A, R, C, N, X or blank.</td>
<td>Patient Status must be A, R, C, N, X, or blank. Blanks will be defaulted to X during migration.</td>
<td>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>INDIGENT, #4</td>
<td>Indigent indicator must be Y, N or blank.</td>
<td>Indigent must be Y, N, or blank. Blanks will be defaulted to N during migration.</td>
<td>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>APPORTIONEE $, #5</td>
<td>Apportionee $ cannot be less than 0 or greater than 99,999.00.</td>
<td><p>Apportionee $ must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Populates income source type and amount during conversion.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>GUARDIAN $, #6</td>
<td>Guardian $ cannot be less than 0 or greater than 99,999.00.</td>
<td><p>Guardian $ must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Populates income source type and amount during conversion.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>INSTITUTION AWARD, #7</td>
<td>Institutional Award $ cannot be less than 0 or greater than 99,999.00.</td>
<td><p>Institutional Award $ must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Populates income source type and amount during conversion.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>OTHER ASSETS, #9</td>
<td>Other Assets $ cannot be less than 0 or greater than 99,999.00.</td>
<td><p>Other Assets $ must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Populates income source type and amount during conversion.</td>
</tr>
</tbody>
</table>

Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>STORED BALANCE, #14</td>
<td>Stored Balance cannot be less than 0 or greater than 99,999.</td>
<td><p>Stored Balance must be a number must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
<p>Must equal sum of Stored Private Source Balance and Gratuitous Source Balance.</p></td>
<td>Blank value will default to 0.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>STORED PRIVATE SOURCE, #15</td>
<td>Stored Private Source Balance cannot be less than 0 or greater than 99,999.</td>
<td><p>Stored Private Source Balance must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Blank value will default to 0.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>STORED GRATUITOUS, #16</td>
<td>Stored Gratuitous Balance cannot be less than 0 or greater than 99,999.</td>
<td><p>Stored Gratuitous Balance must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Blank value will default to 0.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>AMOUNT RESTRICTED PER MONTH, #17</td>
<td>Amount Restricted / Month cannot be less than 0 or greater than 99,999.</td>
<td>Amount Restricted / Month must be a number between 0 and 99,999.</td>
<td>Blank value means no restriction limit.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>AMOUNT RESTRICTED PER WEEK, #18</td>
<td>Amount Restricted / Week cannot be less than 0 or greater than 99,999.</td>
<td>Amount Restricted / Week must be a number between 0 and 99,999.</td>
<td>Blank value means no restriction limit.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>AMOUNT RESTRICTED PER MONTH / WEEK, #17, 18</td>
<td>Restricted Monthly Amount cannot be less than 5 times the Weekly Amount.</td>
<td>Display a warning if the Restricted Monthly Amount is less than 5 times the Weekly Amount.</td>
<td></td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>AMOUNT RESTRICTED PER MONTH / WEEK, #17, 18</td>
<td>Restricted Monthly Amount cannot be less than the Weekly Amount.</td>
<td>Restricted Monthly Amount cannot be less than the Weekly Amount.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>MONTHLY RESTRICTION BALANCE 1, #21</td>
<td>NA</td>
<td>Monthly Restricted Balance cannot be less than 0 or greater than 99,999.</td>
<td>Not checked in M Diagnostic.</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>WEEKLY RESTRICTION BALANCE 1, #22</td>
<td>NA</td>
<td>Weekly Restricted Balance cannot be less than 0 or greater than 99,999.</td>
<td>Not checked in M Diagnostic.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>MINIMUM BALANCE #1;#23</td>
<td>Minimum Balance cannot be less than 0 or greater than 99,999.</td>
<td><p>Minimum Balance must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Blank value means no minimum balance.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>MAXIMUM BALANCE #1, #24</td>
<td>Maximum Balance cannot be less than 0 or greater than 99,999</td>
<td><p>Maximum Balance must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p></td>
<td>Blank value means no maximum balance.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>Balance record</td>
<td>Missing balance record for account. Record must be present.</td>
<td>Balance record must exist for account.</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>PAYEE, #1 of SubFile INCOME SOURCE #470.05</td>
<td>Income source Payee cannot be blank.</td>
<td>Income source Payee cannot be blank.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>AMOUNT, #2 of</p>
<p>SubFIle INCOME SOURCE, #470.05</p></td>
<td>Income source Amount cannot be blank.</td>
<td>Income source Amount cannot be blank.</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>AMOUNT, #2 of</p>
<p>SubFIle INCOME SOURCE, #470.05</p></td>
<td>Income Amount cannot be less than 1 or greater than 99,999.00.</td>
<td><p>Income Amount must be a number greater than or equal to 0.</p>
<p>A warning will be displayed if value</p></td>
<td>PFOP does not allow values less than 1, but checks for values less than 1 are</td>
</tr>
</tbody>
</table>

Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>is greater than 99,999.</td>
<td>possible.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>FREQUENCY, #3 of</p>
<p>SubFile INCOME SOURCE, #470.05</p></td>
<td>Income source Frequency must be D, W, M, Y, X, V, O or blank.</td>
<td>Income source Frequency must be D, W, M, Y, X, V, O or blank.</td>
<td>M Diagnostic Summary: The number of blank entries will be displayed in the summary.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>STATION NAME, #73</td>
<td>Station ID cannot be blank or unassigned.</td>
<td>Station ID must be a valid station ID*.</td>
<td><p>* If blank, parent station ID will be inserted as the default station ID during migration.</p>
<p>M Diagnostic: Although the Summary Report does count these errors, they are not displayed in the Detail Report to save space.</p>
<p>Pointer to File 4.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>STATION NAME, #73</td>
<td>Station ID must be valid. (Must exist in File 4, Institution table.)</td>
<td><p>Station ID must be a valid station ID*. Station ID must be the division ID being migrated or a child of that station.</p>
<p>(Must exist in the SDS Institution table.)</p></td>
<td><p>* If blank, parent station ID will be inserted as the default station ID during extraction.</p>
<p>Pointer to File 4.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>GENERAL INFORMATION/ REMARKS, #34</td>
<td>NA</td>
<td>General Remarks cannot be more than 2000 characters.</td>
<td><p>Not checked by M Diagnostic</p>
<p>A Description that is too long will be truncated to 2000 characters during migration.</p></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>SPECIAL REMARKS, #35</td>
<td>NA</td>
<td>Special Remarks cannot be more than 2000 characters.</td>
<td><p>Not checked by M Diagnostic</p>
<p>A Description that is too long will be truncated to 2000 characters during migration.</p></td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>SUSPENSE DATE,</p>
<p>#.01 of SubFile SUSPENSE DATE, #32</p></td>
<td>Suspense Date must be a valid VistA date.</td>
<td><p>Suspense Date must be 7 digits in VistA date format.</p>
<p>Imprecise dates are not allowed. Cannot be blank.</p></td>
<td><p>Detail report contains two types of errors reported:</p>
<ol type="1">
<li><p>- Suspense date is blank</p></li>
<li><p>- Suspense date is not valid</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>ITEM ID, #.01 of SubFile ID, #470.04,</p>
<p>of SubFile SUSPENSE DATE, #32</p></td>
<td>Suspense ID cannot be blank or more than 40 characters.</td>
<td>Suspense ID cannot be blank or more then 50 characters.</td>
<td><p>Detail report contains two types of errors reported:</p>
<ol type="1">
<li><p>- Suspense ID is blank</p></li>
<li><p>- Suspense ID &lt; 1 or &gt; 40 characters</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><p>FULL DESCRIPTION,</p>
<p>#1, of SubFile ID, #470.04, of SubFile SUSPENSE DATE, #32</p></td>
<td>Suspense Text cannot be blank or more than 255 characters.</td>
<td>Suspense Text cannot be blank or more than 255 characters.</td>
<td><p>Detail report contains two types of errors reported:</p>
<ol type="1">
<li><p>- Suspense description is blank</p></li>
<li><p>- Suspense description &lt; 1 or &gt; 255 characters</p></li>
</ol>
<p>Maximum length cannot be verified in the Analyze Report. A Description that is too long will be truncated to 255 characters during migration.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Invalid suspense item</td>
<td>NA</td>
<td>Cannot have a Suspense Item record (S2) without a corresponding Suspense Date record (S1).</td>
<td><p>Not checked by M Diagnostic.</p>
<p>Verify the integrity of the suspense records in the extraction file.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td>DEFERRED CREDIT REF #, #31</td>
<td>Display a count of the deferred transactions.</td>
<td>NA</td>
<td>M Diagnostic Summary: Shows count of deferred transactions. Is not an error and does not display in the Detail Report.</td>
</tr>
</tbody>
</table>

Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><strong>File</strong></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td>470.1</td>
<td>Transaction record</td>
<td><p>Missing transaction record or record is blank. Record must be present.</p>
<p>Deferred Credit Reference Number must match the Transaction ID.</p></td>
<td>NA</td>
<td>See comment below:</td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>47 - Comment</p>
<p>Master Transaction IDs should always be the same as the Deferred Credit Reference Number with an ‘M’ appended to the end. The ‘M’ is stripped off when doing this check.</p>
<p>Important Note: If you find that there are deferred transactions that have Master Transaction IDs (.01 field of file 470.1) that do not match the Deferred Credit Reference number (the .01 field of an entry in file 470 field 31, which is also the IEN of file 470.1) this indicates:</p>
</blockquote>
<ol type="1">
<li><p>The Master transaction counter in file 470.3 is out of sync. This must be corrected or the counter will continue to be incorrect for all future transactions in Patient Funds. Each site has the following two options for resolving this matter:</p>
<ol type="a">
<li><p>Correct the transaction counter by contacting IRM to register a Remedy ticket. This is recommended so transactions will be in sync for future transactions.</p></li>
<li><p>Leave the transaction counter out of sync. This option is not recommended but is acceptable. If transactions are not corrected, transactions will be out of sync in VistA but will have no negative effect on VPFS data or the Patient Funds migration.</p></li>
</ol></li>
<li><blockquote>
<p>Master Transaction IDs do not match the Deferred Credit Reference Numbers. Each site has the following three options for resolving this matter:</p>
</blockquote>
<ol type="a">
<li><p>Let the deferred transaction clear or move up the deferred date so the transaction will clear sooner.</p></li>
<li><p>Correct the transactions that do not have a matching Master Transaction ID by contacting IRM to register a Remedy ticket. This is recommended so transactions in the past will be in sync.</p></li>
<li><p>Leave the transactions that do not have matching Master Transaction IDs unchanged. This option is not recommended but is acceptable. If transactions are not corrected transactions will be out of sync in VistA but this will have no negative effect on VPFS data or the Patient Funds migration.</p></li>
</ol></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td>470.1</td>
<td>PATIENT NAME, #1</td>
<td>Patient name must match the deferred transaction name.</td>
<td>NA</td>
<td>Pointer to PATIENT FUNDS FILE, #470 which is a pointer to PATIENT FILE, #2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>470.1</td>
<td>TRANSACTION ID, #.01</td>
<td><p>Transaction ID cannot be blank.</p>
<p>Transaction ID must match the transaction ID for the patient account.</p></td>
<td>NA</td>
<td></td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><strong>File</strong></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>470.1</td>
<td>AMOUNT, #3</td>
<td>Transaction Amount cannot be blank, less than .01 or greater than 99,999.</td>
<td><p>Transaction Amount must be a number between 0 and 99,999 and cannot be blank.</p>
<p>Must equal sum of Private Source Amount and Gratuitous Source Amount.</p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>470</td>
<td>LAST TRANSACTION DATE, #</td>
<td>NA</td>
<td><p>Last Transaction Date must be 7 digits, in VistA date format.</p>
<p>Imprecise dates are not allowed.</p></td>
<td>Not checked in M Diagnostic.</td>
</tr>
<tr class="odd">
<td></td>
<td>470.1</td>
<td>DEFERRAL DATE, #19</td>
<td>NA</td>
<td>Deferral Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</td>
<td>Not checked in M Diagnostic.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>470.1</td>
<td>TRANSACTION DATE, #4</td>
<td>Transaction Date must be a valid VistA date and cannot be blank.</td>
<td>Transaction Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>470.1</td>
<td>DATE TRANSACTION ENTERED, #5</td>
<td>Transaction Entered Date must be a valid VistA date and cannot be blank.</td>
<td>Transaction Entered Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>53</p>
</blockquote></td>
<td>470.1</td>
<td>REFERENCE, #6</td>
<td>Reference must be 1-10 characters and cannot be blank.</td>
<td>Reference must be 1-10 characters and cannot be blank.</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td>470.1</td>
<td>DEPOSIT/ WITHDRAWAL, #7</td>
<td>Deposit/Withdrawal field must be D or W and cannot be blank.</td>
<td>Deposit/Withdrawal field must be D or W and cannot be blank.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td>470.1</td>
<td>CASH/CHECK/ OTHER, #8</td>
<td>Cash/Check/Other field must be 1, 2, or 3 and cannot be blank.</td>
<td>Cash/Check/Other field must be 1, 2, or 3 and cannot be blank.</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>56</p>
</blockquote></td>
<td>470.1</td>
<td>SOURCE, #9</td>
<td>Transaction Income Source must be P, G, or B and cannot be blank.</td>
<td>Transaction Income Source must be P, G, or B and cannot be blank.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>57</p>
</blockquote></td>
<td>470.1</td>
<td>FORM, #10</td>
<td>Form cannot be blank and must be a value in the standard Form list</td>
<td>Form cannot be blank.</td>
<td>Form is a pointer to File 470.2.</td>
</tr>
</tbody>
</table>

Appendix A. Migration Business Rules

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><strong>File</strong></th>
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule</strong></p>
<p><strong>(Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(user-maintained, in table).</td>
<td>Display warning if Form value is not in the standard Form list in VPFS.</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>58</p>
</blockquote></td>
<td>470.1</td>
<td>PRIVATE SOURCE AMT, #11</td>
<td>Private Source Amount cannot be less than .01 or greater than 99,999, but can be blank.</td>
<td><p>Private Source Amount must be between 0 and 99,999.</p>
<p>Either the Private or Gratuitous Amount must <em>not</em> be blank.</p></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>59</p>
</blockquote></td>
<td>470.1</td>
<td>GRATUITOUS AMOUNT, #12</td>
<td>Gratuitous Source Amount cannot be less than .01 or greater than 99,999, but can be blank.</td>
<td><p>Gratuitous Amount must be between 0 and 99,999.</p>
<p>Either Private or Gratuitous Amount must <em>not</em> be blank.</p></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>60</p>
</blockquote></td>
<td>470.1</td>
<td>PATIENT FUNDS CLERK, #13</td>
<td>Patient Funds Clerk cannot be blank and must exist in File 200.</td>
<td>Patient Funds Clerk must be 3-35 characters and cannot be blank.</td>
<td>Pointer to NEW PERSON FILE, #200</td>
</tr>
</tbody>
</table>

> Appendix A. Migration Business Rules

> This page intentionally blank.

> <span id="Appendix_B._Diagnostic_Report_Samples" class="anchor"></span>Appendix B. Diagnostic Report Samples

> Appendix B. Diagnostic Report Samples

> This appendix contains sample portions of the reports, logs, and error files produced by the routines that you perform while moving through the data migration process in VistAMigrate.

> Diagnostic Summary Report

> This report is accessed in both of the following ways:

- In the VistA legacy application: Select the function Database Diagnostic Report.
- In VistAMigrate: Select step 2 M Diagnostics

> The Diagnostic Summary Report lists the number of occurrences for each type of error, and also lists how many deferred transactions are to be migrated (this is not an error). The following table lists descriptions of the information in the fields on the Diagnostic Summary Report.

> Table B-1. Description of Diagnostic Summary Report

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Error #</strong></p>
</blockquote></td>
<td><blockquote>
<p>Code assigned to the error type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>Name of the field where the error occurred.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Error Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>Description of the error.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Total Count</strong></p>
</blockquote></td>
<td><blockquote>
<p>Number of occurrences of the specific type of error.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Total Accounts processed =</strong></p>
</blockquote></td>
<td><blockquote>
<p>Total number of patient records processed by the M diagnostics routine.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\* Patient Funds Diagnostic Summary (version 5.9) \*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Run Date: FEB 13, 2006 Run Time: 14:18:12 \*\*

> Total accounts processed = 27 \*\*

> Total balance of accounts for migration = \$202,152.00 \*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 52%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Err#</p>
<blockquote>
<p>#</p>
</blockquote></th>
<th><blockquote>
<p>Field</p>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Error</p>
<p>Description</p>
</blockquote></th>
<th><blockquote>
<p>Total</p>
<p>Count</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"></td>
</tr>
<tr class="even">
<td>#1</td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>Name is blank</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td>#2</td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>Name contains invalid data</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="even">
<td>#3</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN is blank</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>#4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td>#5</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains duplicate value</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td>#6</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains Pseudo SSN value</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td>#7</td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>DOB is blank</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>#8</td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>DOB contains invalid date</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="even">
<td>#9</td>
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>Ward loc invalid length</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#10</p>
</blockquote></td>
<td><blockquote>
<p>CLAIM</p>
</blockquote></td>
<td><blockquote>
<p>Claim # contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#11</p>
</blockquote></td>
<td><blockquote>
<p>ZIP</p>
</blockquote></td>
<td><blockquote>
<p>Zipcode contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#12</p>
</blockquote></td>
<td><blockquote>
<p>REGION OFFICE</p>
</blockquote></td>
<td><blockquote>
<p>Regional Office ID invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
</tbody>
</table>

> Appendix B. Diagnostic Report Samples

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 48%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>#13</th>
<th><blockquote>
<p>ICN</p>
</blockquote></th>
<th>ICN Duplicate</th>
<th>2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#14</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td>ICN unassigned or invalid</td>
<td>1</td>
</tr>
<tr class="even">
<td>#15</td>
<td><blockquote>
<p>PROVIDER AUTHR</p>
</blockquote></td>
<td>Provider Name contains invalid data</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#16</td>
<td><blockquote>
<p>PROVID AUTH DT</p>
</blockquote></td>
<td>Date of current restriction invalid date</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#17</td>
<td><blockquote>
<p>NO DEMO RECORD</p>
</blockquote></td>
<td>No demographic record for account</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#18</td>
<td><blockquote>
<p>ACCOUNT STATUS</p>
</blockquote></td>
<td>Account status not (A),I,Blank=1</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#19</td>
<td><blockquote>
<p>PATIENT TYPE</p>
</blockquote></td>
<td>Patient type not L,R,(U),X,Blank=3</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#20</td>
<td><blockquote>
<p>PAT TYPE/PHY</p>
</blockquote></td>
<td>Patient type L or R without Phy name</td>
<td>9</td>
</tr>
<tr class="even">
<td>*#21</td>
<td><blockquote>
<p>PATIENT STATUS</p>
</blockquote></td>
<td>Patient Status not A,R,C,N,(X),Blank=3</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#22</td>
<td><blockquote>
<p>INDIGENT</p>
</blockquote></td>
<td>Indigent status not (N),Y,Blank=4</td>
<td>1</td>
</tr>
<tr class="even">
<td>*#23</td>
<td><blockquote>
<p>APPORTIONEE $</p>
</blockquote></td>
<td>Apportionee amount invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#24</td>
<td><blockquote>
<p>GUARDIAN $</p>
</blockquote></td>
<td>Guardian amount invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#25</td>
<td><blockquote>
<p>INSTITUT AWARD</p>
</blockquote></td>
<td>Institut award invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#26</td>
<td><blockquote>
<p>OTHER ASSETS</p>
</blockquote></td>
<td>Other assets invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#27</td>
<td><blockquote>
<p>STORED BALANCE</p>
</blockquote></td>
<td>Stored balance invalid or &lt; $0 or &gt; $99,999</td>
<td>6</td>
</tr>
<tr class="odd">
<td>*#28</td>
<td><blockquote>
<p>STORED PRIVATE</p>
</blockquote></td>
<td>Stored private invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#29</td>
<td><blockquote>
<p>STORED GRATUIT</p>
</blockquote></td>
<td>Stored gratuitous invalid or &lt; $0 or &gt; $99,999</td>
<td>4</td>
</tr>
<tr class="odd">
<td>*#30</td>
<td><blockquote>
<p>RESTRCT MONTH</p>
</blockquote></td>
<td>Restricted Monthly invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#31</td>
<td><blockquote>
<p>RESTRCT WEEKLY</p>
</blockquote></td>
<td>Restricted Weekly invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#32</td>
<td><blockquote>
<p>RESTRCT AMT ER</p>
</blockquote></td>
<td>Restrict Mnthly amount &lt; (5X) weekly amt</td>
<td>4</td>
</tr>
<tr class="even">
<td>*#33</td>
<td><blockquote>
<p>RESTRCT AMT ER</p>
</blockquote></td>
<td>Restrict Mnthly amount &lt; weekly amt</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#34</td>
<td><blockquote>
<p>MINIMUM BAL</p>
</blockquote></td>
<td>Minimum balance #1 invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#35</td>
<td><blockquote>
<p>MAXIMUM BAL</p>
</blockquote></td>
<td>Maximum balance #1 invalid or &lt; $0 or &gt; $99,999</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#36</td>
<td><blockquote>
<p>NO BALANCE REC</p>
</blockquote></td>
<td>Balance record missing for account</td>
<td>2</td>
</tr>
<tr class="even">
<td>*#37</td>
<td><blockquote>
<p>INCOME PAYEE</p>
</blockquote></td>
<td>Income payee blank, Income source present</td>
<td>2</td>
</tr>
<tr class="odd">
<td>*#38</td>
<td><blockquote>
<p>INCOME AMOUNT</p>
</blockquote></td>
<td>Income amount error, Income source present</td>
<td>4</td>
</tr>
<tr class="even">
<td>*#39</td>
<td><blockquote>
<p>INCOME AMOUNT</p>
</blockquote></td>
<td>Income amount &lt; $1 or &gt; $99,999</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#40</td>
<td><blockquote>
<p>INCOME FREQCY</p>
</blockquote></td>
<td>Income frequency not D,W,M,Y,X,V,O,Blank=4</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#41</td>
<td><blockquote>
<p>STATION ID</p>
</blockquote></td>
<td>Station ID blank or unassigned</td>
<td>9</td>
</tr>
<tr class="odd">
<td>#42</td>
<td><blockquote>
<p>STATION ID</p>
</blockquote></td>
<td>Station ID invalid</td>
<td>1</td>
</tr>
<tr class="even">
<td>*#43</td>
<td><blockquote>
<p>SUSPENSE DATE</p>
</blockquote></td>
<td>Suspense date has invalid date</td>
<td>3</td>
</tr>
<tr class="odd">
<td>*#44</td>
<td><blockquote>
<p>SUSPENSE ID</p>
</blockquote></td>
<td>Suspense ID has Invalid data</td>
<td>4</td>
</tr>
<tr class="even">
<td>*#45</td>
<td><blockquote>
<p>SUSPENSE TEXT</p>
</blockquote></td>
<td>Suspense text is &lt; 1 or &gt; 255 characters</td>
<td>6</td>
</tr>
<tr class="odd">
<td>*#46</td>
<td><blockquote>
<p>DEFERRED TRANS</p>
</blockquote></td>
<td>There are 6 deferred transactions</td>
<td>6</td>
</tr>
<tr class="even">
<td>*#47</td>
<td><blockquote>
<p>TRANSACTION REC</p>
</blockquote></td>
<td>Transaction record missing, blank or ID invalid</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#48</td>
<td><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
<td>Patient name does not match deferred trans</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#49</td>
<td><blockquote>
<p>PATIENT TRANS #</p>
</blockquote></td>
<td>Patient transaction # invalid</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#50</td>
<td><blockquote>
<p>DEFR AMOUNT</p>
</blockquote></td>
<td>Deferred amount invalid</td>
<td>2</td>
</tr>
<tr class="even">
<td>*#51</td>
<td><blockquote>
<p>TRANSACTN DATE</p>
</blockquote></td>
<td>Transaction date Invalid</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#52</td>
<td><blockquote>
<p>DT TRAN ENTD</p>
</blockquote></td>
<td>Date transaction entered Invalid</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#53</td>
<td><blockquote>
<p>REFERENCE</p>
</blockquote></td>
<td>Reference Invalid &lt; 1 or &gt; 10 in length</td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#54</td>
<td><blockquote>
<p>DEPOSIT/WTHDRWL</p>
</blockquote></td>
<td>Deposit/Withdrawal status Invalid</td>
<td>0</td>
</tr>
<tr class="even">
<td>*#55</td>
<td><blockquote>
<p>CASH/CHECK/OTR</p>
</blockquote></td>
<td>Cash/Check/Other status Invalid</td>
<td>1</td>
</tr>
<tr class="odd">
<td>*#56</td>
<td><blockquote>
<p>SOURCE</p>
</blockquote></td>
<td>Transaction source invalid</td>
<td>1</td>
</tr>
<tr class="even">
<td>*#57</td>
<td><blockquote>
<p>FORM</p>
</blockquote></td>
<td>Form does not match</td>
<td>2</td>
</tr>
</tbody>
</table>

> <span id="Detail_Report" class="anchor"></span>Appendix B. Diagnostic Report Samples

> \*#58 PRVT SOURCE AMT Private source amount invalid or \< 0 or \> 99999 0

> \*#59 GRATUITOUS AMT Gratuitous amount invalid or \< 0 or \> 99999 3

> \*#60 PFUNDS CLERK PFunds clerk invalid 6

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> NOTE: In addition to the summary report there is an available detail report, this report can be sent to any device or flat file if required.

> \>\>\>\>\> The detail diagnostic report will contain 83 lines.

> If you still desire the detail report, then please input the name of the device that the report will be sent to.

> If the detail report is not desired then input "^" at the device prompt and the detail report will not print.

> DEVICE:

> Detail Report

> The Detail report provides detail of each record in the Diagnostic Summary Report that contains an error. Use this information to diagnose the problem and locate the record containing the error so that you can correct it. The following is a sample portion of the M Diagnostic Detail report.

> Important Note: Each detail record has the Patient name (if one exists) included in each detail record as well as the Patient data file number (DFN) to “aid” in identifying exactly which Patient specifically is being reported on. If the Patient name is not available, then in that situation the SSN is displayed as well to aid in specifically identifying what Patient is being reported on. IRM can be contacted and provided the DFN and they will be able to help specifically identify any Patient name that might have duplicates, for example, more than one John Smith appearing in the detail report.

> STATION ID=16541^ERR#=20^NAME=VPFSPATIENT,ONE_7170957^DESC=No Physician name for L or R^VALUE=\>R\<

> STATION ID=16541^ERR#=33^NAME= VPFSPATIENT,ONE_7170957^DESC=Restrict Mnthly amount \<weeklyamt^VALUE=\>5\< STATION ID=16541^ERR#=51^NAME= VPFSPATIENT,ONE_7170957_DefTrans#2^DESC=Transaction date Invalid^VALUE=\>\< STATION ID=ERRBADID1^ERR#=42^NAME= VPFSPATIENT,TWO_7169949^DESC=STATION ID INVALID^VALUE=\>ERRBADID1\<REDAC