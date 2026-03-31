---
title: PIMS Version 5.3 User Manual - Means Test Supervisor Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Means Test Supervisor Menu
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
description: This menu contains the options used in all aspects of Means Testing. This includes adding, completing, editing, deleting, viewing past Means Tests, referral to Adjudication, if necessary, and generating management reports containing Means Test signature statistics. This menu is locked with the DGMEA
audience: 
keywords: 
  - test
  - means
  - income
  - blockquote
  - table
  - strong
  - dependent
  - status
  - date
  - veteran
page_count: 0
word_count: 12369
section_count: 30
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_mts_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_mts_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

# PIMS V. 5.3 ADT Module User Manual Means Test Supervisor Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PIMS V. 5.3 ADT Module User Manual Means Test Supervisor Menu](#pims-v-53-adt-module-user-manual-means-test-supervisor-menu)
  - [Overview](#overview)
  - [Delete a Means Test](#delete-a-means-test)
  - [Delete Means Test/Copay Dependents](#delete-means-testcopay-dependents)
  - [Duplicate Dependents Report](#duplicate-dependents-report)
  - [Duplicate Dependents Report](#duplicate-dependents-report-1)
  - [Means Test Signature Reports](#means-test-signature-reports)
  - [Means Test Signature Reports](#means-test-signature-reports-1)
  - [Means Test User Menu](#means-test-user-menu)
  - [ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).](#ed-expand-dependent-will-move-to-another-screen-expand-dependent-it-is-used-to-edit-the-effective-date-date-the-person-became-a-dependent-of-the-veteran)
  - [Means Test User Menu](#means-test-user-menu-1)
  - [Means Test User Menu](#means-test-user-menu-2)
  - [Means Test User Menu](#means-test-user-menu-3)
  - [Means Test User Menu](#means-test-user-menu-4)
  - [Means Test User Menu](#means-test-user-menu-5)
  - [Means Test User Menu](#means-test-user-menu-6)
  - [Means Test User Menu](#means-test-user-menu-7)
  - [Means Test User Menu](#means-test-user-menu-8)
  - [Means Test User Menu](#means-test-user-menu-9)
  - [<table>](#table)
  - [<table>](#table-1)
  - [<table>](#table-2)
  - [Means Test User Menu](#means-test-user-menu-10)
  - [Means Test User Menu](#means-test-user-menu-11)
  - [Means Test User Menu](#means-test-user-menu-12)
  - [Means Test User Menu](#means-test-user-menu-13)
  - [Merge Duplicate MT/Copay Dependents](#merge-duplicate-mtcopay-dependents)
  - [Purge Duplicate Income Tests](#purge-duplicate-income-tests)
  - [Purge Income Test Monitor](#purge-income-test-monitor)
  - [View Means Test Editing Activity](#view-means-test-editing-activity)
Delete a Means Test
Delete Means Test/Copay Dependents
Duplicate Dependents Report
Means Test Signature Reports
> Means Test Signature Summary Report
> Means Test Signature Detail Report
Means Test User Menu
> Add a New Means Test
> Adjudicate a Means Test
> Complete a Required Means Test
> Document Comments on a Means Test
> Edit an Existing Means Test
> GMT Thresholds Lookup by Zip Code
> Hardships
> Pseudo SSN Report for Means Test Dependents
> View a Past Means Test
Merge Duplicate MT/Copay Dependents
Purge Duplicate Income Tests
Purge Income Test Monitor
View Means Test Editing Activity
Revision History
Initiated on 1/20/05
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 24%" />
<col style="width: 24%" />
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
<td>1/20/05</td>
<td>Added documentation for Purge Duplicate Income Tests and Purge Income Test Monitor options</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/05</td>
<td><p>DG*5.3*624 – 10-10EZ 3.0 Enhancements</p>
<ul>
<li><blockquote>
<p>Changed Printing Prompt Sequence in Financial Assessment Applications. Added note for Roll-Up Means Test Dollar Amounts (GAI and NW) to conform with amounts on Feb 2005 VistA-Printed 10-10EZ/EZR Forms.</p>
</blockquote></li>
<li><blockquote>
<p>Added updates based on revised business rules for evaluating child(ren)’s Income Available to veteran and how it affects the Gross Annual Income dollar amounts printed on the 10-10EZ/EZR and displayed in the Child(ren)’s column on the Previous Calendar Year Gross Income Screen 2.</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/14/05</td>
<td>DG*5.3*655 – Remove Income Test Inconsistency Checks – Updated Means Test User Menu options</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/7/06</td>
<td>DG*5.3*611 – Fix Means Test Display – Updated Add a New Means Test, Complete a Required Means Test, and Edit an Existing Means Test options</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/11/07</td>
<td>DG*5.3*653 – Enrollment VistA Changes Release 1 (EVC R1) – Added new Pseudo SSN Report for Means Test Dependents option</td>
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
<td>11/21/08</td>
<td>Corrected error in GMT Thresholds Lookup by ZIP Code option</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/30/09</td>
<td><p>DG*5.3*688 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<ul>
<li><blockquote>
<p>Removed “Copy Data” function from income tests</p>
</blockquote></li>
<li><blockquote>
<p>Added “Modify Means Test Data Collection - Means Test Version Indicator” to Overview section</p>
</blockquote></li>
</ul>
<p>Changed <em>environmental contaminants</em> to <em>SW Asia Conditions</em></p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/10/09</td>
<td><p>DG*5.3*803 – Priority Group 8 Changes</p>
<p>Updated the <em>GMT Thresholds Lookup by Zip Code</em> option with the new priority 8 sub-categories ‘b’ and ‘d’.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/17/09</td>
<td><p>DG*5.3*754 – Priority Group 6 ESR 3.1 Changes:</p>
<p>New Special Treatment Authority Expiration date fields for Agent Orange and SWAC to the Means Test User Menu section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/18/10</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes:</p>
<p>Modified Screen 1 - <em>Marital Status/Dependent</em> section of <em>Means Test User Menu/Add a New Means Test</em> section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/28/13</td>
<td><p>DG*5.3*858 – ESR 3.10</p>
<p>Veterans Financial Assessment – Discontinue Annual Means Test Renewal</p>
<p>Update to Overview Means Test User Menu options:</p>
<ul>
<li><p>Adjudicate a New Means Test</p></li>
<li><p>Complete a Required Means Test</p></li>
<li><p>Edit an Existing Means Test</p></li>
<li><p>Hardships</p></li>
</ul>
<p>Update to options:</p>
<ul>
<li><p>Complete a Required Means Test</p></li>
<li><p>Edit an Existing Means Test</p></li>
</ul>
<p>Hardships</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/5/15</td>
<td>DG*5.3*890 – Contributed to Spouse and Contributed to Child – Amount Contributed is no longer asked and is replaced with Did you contribute to support Y/N</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/05/2015</td>
<td>TW review: DG_53_P891_KID</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/02/2019</td>
<td>DG*5.3*972 – Added “is not awarded Medal of Honor” to conditions under which a Means Test is required (p. 32).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>05/15/2020</td>
<td>DG*5.3*996 – Updated GRANT HARDSHIP List Manager action to remove Hardship Review Date prompt (p. 43)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/10/2020</td>
<td>DG*5.3*997 – Updated Overview/Hardships Section to remove allowance for editing or deleting Hardships, p. 10; Updated resolutions to Hardship-related inconsistency messages in Table 2 to indicate Hardships are to be edited in the Enrollment System, p. 36-37; Updated Means Test User Menu/Hardships Section to remove allowance for editing or deleting hardships, p. 43; Revised description of how hardships are expired, p. 43.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/02/2020</td>
<td>DG*5.3*1014 – Updated throughout to remove the requirement for entry of Previous Calendar Year Net Worth and indicate that Screen 4 will only be displayed when data was entered on Screen 4 prior to patch DG*5.3*1014 (described in Overview Section, p. 8; Means Test User Menu – Add a New Means Test, p. 19 and p. 21; Means Test User Menu – Adjudicate a Means Test, p. 23; Means Test User Menu – Complete a Required Means Test, p. 24 and p. 27; Means Test User Menu – Edit an Existing Means Test, p. 32 and Table 1 items “3.” and “4.”, p. 35; Means Test User Menu – GMT Thresholds Lookup by ZIP Code, item “f.” p. 41; Means Test User Menu – View a Past Means Test Section, p. 45).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains the options used in all aspects of Means Testing. This includes adding, completing, editing, deleting, viewing past Means Tests, referral to Adjudication, if necessary, and generating management reports containing Means Test signature statistics. This menu is locked with the DGMEANSTEST key.

Public Law 101-508 permits the VA to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income. The income verification match (IVM) process for VHA medical facilities is centralized and performed at the Health Eligibility Center (HEC), Atlanta, GA.

With the installation of the IVM v1.0 software, all Means Tests completed since January 1, 1993 that met the following criteria were transmitted to the HEC. Subsequently, any Means Test added or edited is sent via a nightly background job.

- Patient is MT Copay Exempt, but was neither adjudicated nor given a hardship exemption.
- Patient is MT Copay Required but has no active health insurance on file.

This information provides the HEC with the ability to compare the income reported to VHA by the veteran with records maintained by SSA and IRS. The HEC then begins verification of the cases. If applicable, the Means Test is updated and the veteran signs the revised 10-10EZ/R. The new Means Test is electronically transmitted to the field facility and automatically updated. The original Means Test conducted by the facility will be inactivated and the IVM test will become the Primary (active) test for the test date. Both the original VAMC test and verified IVM test are not editable, but may be viewed and printed.

The automatic filing of the IVM verified Means Test may change the patient's current Means Test status. If the status changes from MT Copay Exempt to MT Copay Required and the patient received medical care after the Means Test date, Means Test copayment charges for those episodes of care will automatically be created. These charges must be reviewed before being passed to Accounts Receivable.

Overview

Modify Means Test Data Collection - Means Test Version Indicator

A Means Test version indicator will be created and will support the display and collection of Means Test information for both the 1010EZ form prior to February 2005 and the 1010EZ form from February. 2005. These modifications (outlined in Patches IVMB\*2\*860 and IVMB \*2\*886) support the February 2005 form. The Means Test information collected prior to installation of this patch will continue to be collected, printed, and displayed in the February 2005 format.

Listed below are the following modifications created to display the Means Test version indicator VistA Options:

> Load/Edit Patient \[DG LOAD PATIENT DATA\]

> Register a Patient \[DG REGISTER PATIENT\]

> Add a New Means Test \[DG MEANS TEST ADD\]

> Complete a Required Means

> Test \[DG MEANS TEST COMPLETE\]

> Edit an Existing Means Test \[DG MEANS TEST EDIT\]

> View a Past Means Test \[DG MEANS TEST VIEW TEST\]

> Purge Duplicate Income Tests \[DG CLEANUP INCOME TEST DUPES\]

> Add a Copay Exemption Test \[DG CO PAY TEST ADD\]

> Edit an Existing Copay Exemption

> Test \[DG CO PAY TEST EDIT\]

> View a Past Copay Test \[DG CO PAY TEST VIEW TEST\]

The benefits for supporting the Means Test version indicator will include the following elements:

- Income Available Response collected for Dependent Child(ren) will now support collection of children Net Worth Dollar Amounts. Children Net Worth Dollar amounts will be collected with the new form.
- A limit of 19 dependent children will be collected for a Means Test. This limit applies to those dependents with relationships of son, daughter, step-son, and step-daughter.
- The collection of Previous Calendar Year Gross Annual Income with February 2005 Data format will be changed to collect 3 data elements rather than the 10 data elements collected with the pre February 2005 format.
- Means Test data collection will collect the Gross Medical Expenses dollar amount, within Deductible Expenses, labeled as "Total Non-Reimbursed Medical Expenses.”

Overview

- February 2005 1010EZ form Means Test data collection will no longer require a spouse or dependent child (associated with the Means Test) to collect funeral and burial expenses.
- The collection of Previous Calendar Year Net Worth with February 2005 Data format will be changed to collect 3 data elements rather than the 5 data elements collected with the pre February 2005 format. Subsequent updates with DG\*5.3\*1014 have removed the requirement for entry of Previous Calendar Year Net Worth; however, the ability to view this data if entered prior to patch installation will remain.
- The system will continue to display the summary Income, Net Worth, and Deductible Expenses amounts in the February 2005 data collection format as was displayed with the pre February 2005 data collection format. The system will continue to calculate the summary Income, Net Worth, and Deductible Expense amounts in the February 2005 data collection format with the same formulas as with the existing data collection format.
- Entry of Means Test information in the February 2005 data collection format will produce the same Means Test status that results when the Means Test information is entered with the existing data collection format.
- The "Copy Data" function will be removed from the Means Test user interface for both February 2005 form and pre February 2005 form. The "Copy Data" function will still be performed by the Means Test system when done automatically. For example, if the Primary Eligibility Code changes from Non-Service Connected to Service Connected, a Pharmacy Copay test will automatically be created. When this "automatic" copy occurs, the Annual Income information will be checked for the data collection form. If that data is in pre February 2005 form, it will convert to the February 2005 form to match the newly created Pharmacy Copay Test.

Overview

The following is a list of the options contained in this menu and a brief description of their major function.

DELETE A MEANS TEST

This option allows deletion of Means Test data from the ANNUAL MEANS TEST file (#408.31) for specified patient(s). In order to use this option, users must hold the DG MTDELETE security key.

DELETE MEANS TEST/COPAY DEPENDENTS

This option allows holders of the DG MEANSTEST security key to delete a Means Test Dependent and/or a Copay Test Dependent without having to manually process all Means Tests on file for the specified patient. Data deleted during this process is stored in a temporary global for 10 days.

DUPLICATE DEPENDENTS REPORT

This option allows Means Test supervisors who hold the DG MEANSTEST security key to generate a report to determine which dependents could be duplicates in the PATIENT RELATION file (#408.12). In most cases, these duplicates can be corrected by using either the Delete Means Test/Copay Dependents or Merge Duplicate MT/Copay Dependents menu options.

MEANS TEST SIGNATURE REPORTS

> MEANS TEST SIGNATURE SUMMARY REPORT

> This option is used to help VAMCs monitor the Means Test images returned to them by the HEC.

> MEANS TEST SIGNATURE DETAILED REPORT

> This option is used to list those veterans at a particular site for which a signature still needs to be obtained.

MEANS TEST USER MENU

> ADD A NEW MEANS TEST

> This option allows adding a new Means Test for patients who require one.

> ADJUDICATE A MEANS TEST

> This option allows entry of final outcome of Means Tests less than 1 year old from the effective date referred to Adjudication.

> COMPLETE A REQUIRED MEANS TEST

> This option allows completion of Means Tests less than 1 year from the effective date for patients in a REQUIRED status.

> DOCUMENT COMMENTS ON A MEANS TEST

This option is used to add/edit/delete free-text comments on a selected Means Test.

> EDIT AN EXISTING MEANS TEST

> This option is used to make changes to existing Means Tests. This is the only option that allows changes to completed Means Tests less than 1 year old from the effective date.

> GMT THRESHOLDS LOOKUP BY ZIP CODE

> This option displays GMT threshold values for valid zip code.

> HARDSHIPS

> This option allows the user to grant hardships for the current Means Test when the test is less than 1 year old from the effective date.

> PSEUDO SSN REPORT FOR MEANS TEST DEPENDENTS

> This option allows the user to print a report of dependents, sorted by patient, who have Pseudo SSNs.

> VIEW A PAST MEANS TEST

> This option allows viewing of past Means Tests.

MERGE DUPLICATE MT/COPAY DEPENDENTS

This option allows holders of the DG MEANSTEST security key to merge dependents considered to be duplicates in the PATIENT RELATION file (#408.12). Data deleted during this process is stored in a temporary global for 10 days.

PURGE DUPLICATE INCOME TESTS

This option allows holders of the DG MEANSTEST security key to purge duplicate tests that appear on the same day. It will also delete tests that have a null status.

PURGE INCOME TEST MONITOR

This option is used to monitor the cleanup process selected in the Purge Duplicate Income Tests option.

VIEW MEANS TEST EDITING ACTIVITY

This option provides a method of viewing specific changes made to Means Test data for a selected patient.

## Delete a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete a Means Test option is used to delete individual dates of Means Tests for a specified patient from the ANNUAL MEANS TEST file (#408.31). It can also be used to delete all Means Tests for a non-veteran patient.

Means Tests that have been verified by the HEC and the corresponding VAMC test are uneditable and cannot be deleted. If you choose such a Means Test, the system will display a message informing you it cannot be deleted.

Deletion of a patient's most recent Means Test requires a change in Means Test status. The system automatically assigns the status corresponding to the next most recent Means Test and displays a message.

Utilizing this option only deletes the patient's Means Test record entry in the ANNUAL MEANS TEST file (#408.31). All information concerning income, assets, debts, spouse, dependent children, etc., is maintained.

Only users holding the DG MTDELETE security key may access this option.

## Delete Means Test/Copay Dependents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete Means Test/Copay Dependents option allows you to delete a Means Test Dependent and/or a Copay Test Dependent from the PATIENT RELATION file (#408.12) without having to manually process all Means Tests on file for the specified patient. At the “Select MT/Copay Dependent to be deleted:” prompt, enter the SSN of the patient whose Patient Relation entries you want to delete.

The software displays the selected patient’s enrollment information and prompts you to verify that this is the correct patient. YES response takes you to the “Would you like to PERMANENTLY DELETE this record? NO//” prompt; NO response returns you to the “Select MT/Copay Dependent to be deleted:” prompt.

After you verify that you want to permanently delete the duplicate record, the software confirms that the entry was successfully deleted.

You must hold the DG MEANSTEST security key to access this option.

## Duplicate Dependents Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duplicate Dependents Report option allows Means Test supervisors to determine which dependents could be duplicates in the PATIENT RELATION file (#408.12). In most cases, these duplicates can be corrected by using either the Delete Means Test/Copay Dependents or the Merge Duplicate MT/Copay Dependents menu options.

The following information displays when you enter this option:

\*\*\* DUPLICATE PATIENT RELATIONS REPORT \*\*\*

This report will search the PATIENT RELATION file (#408.12) to identify

those entries where potential duplicates exist.

This report is designed for an 80 column print device or a terminal

using the HOME device. The report may take a long time to generate,

accordingly, it is recommended that it be queued to an 80 column

print device. The P-MESSAGE device is NOT recommended for use, nor

should the output format be specified at the device prompt in order to

do a screen capture.

DEVICE: HOME//

This option generates eight (8) separate reports for the potential duplicates. The report generation will take some amount of time, based on the size of the site’s database. Queuing to an 80-column print device is highly recommended. If you accept the HOME default at the “DEVICE:” prompt, your terminal will be tied up during the job run time. An asterisk (\*) in the SSN column of the various reports indicates an entry in the INCOME PERSON file (#408.13) without an SSN. The reports generated are categorized as follows:

## Duplicate Dependents Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If patient is NOT DECEASED

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Report Heading</strong></th>
<th><strong>Report Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Active Duplicate Entries</p>
<p>Category C</p>
<p>NON-CMOR</p></td>
<td><p>Means Test Cat C</p>
<p>CMOR is a site other than the facility generating the report.</p></td>
</tr>
<tr class="even">
<td><p>Active Duplicate Entries</p>
<p>Category C</p>
<p>CMOR</p></td>
<td><p>Means Test Cat C</p>
<p>CMOR is the site generating this report.</p></td>
</tr>
<tr class="odd">
<td><p>Active Duplicate Entries</p>
<p>Non Category C</p>
<p>NON-CMOR</p></td>
<td><p>Other Category Means Test</p>
<p>CMOR is a site other than the facility generating the report.</p></td>
</tr>
<tr class="even">
<td><p>Active Duplicate Entries</p>
<p>Non Category C</p>
<p>CMOR</p></td>
<td><p>Other Category Means Test</p>
<p>CMOR is the site generating this report.</p></td>
</tr>
</tbody>
</table>

If patient is DECEASED

> **NOTE:** No Action required in reference to the deceased reports.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Report Heading</strong></th>
<th><strong>Report Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Deceased Patient, No Action Required</p>
<p>Category C</p>
<p>NON-CMOR</p></td>
<td><p>Means Test Cat C</p>
<p>CMOR is a site other than the facility generating the report.</p></td>
</tr>
<tr class="even">
<td><p>Deceased Patient, No Action Required</p>
<p>Category C</p>
<p>CMOR</p></td>
<td><p>Means Test Cat C</p>
<p>CMOR is the site generating this report.</p></td>
</tr>
<tr class="odd">
<td><p>Deceased Patient, No Action Required</p>
<p>Non Category C</p>
<p>NON-CMOR</p></td>
<td><p>Other Category Means Test</p>
<p>CMOR is a site other than the facility generating the report.</p></td>
</tr>
<tr class="even">
<td><p>Deceased Patient, No Action Required</p>
<p>Non Category C</p>
<p>CMOR</p></td>
<td><p>Other Category Means Test</p>
<p>CMOR is the site generating this report.</p></td>
</tr>
</tbody>
</table>

The report output includes the following information:

- Report title (Specific in terms of categorization outlined in the table above)
- Date/Time the report was generated
- Name of the supervisor who generated the report
- Page number
- Veteran’s Name and SSN
- Dependent’s SSN and name
- Dependent’s date of birth
- Whether the dependent is active in the PATIENT RELATION file (#408.12) (YES or NO)
- Date on which the individual became the patient’s dependent (EFF DATE)
- Type of test (Means, Copay, or UNK). UNK indicates the type of test could not be determined by the software.

You must hold the DG MEANSTEST security key to access this option.

## Means Test Signature Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Means Test Signature Summary Report

The Means Test Signature Reports menu provides for the generation of management reports containing Means Test signature statistics. Only users holding the DG SUPERVISOR security key may access this menu.

The statistics generated by these reports will only include those veterans who have a Means Test with Status of A, C, or Pending Adjudication as these are the only MT statuses that require obtaining a signature.

The purpose of the Means Test Signature Summary Report is to help VAMCs monitor the Means Test images returned to them by the HEC. The report only shows signature indicators for Means Tests that were submitted by the local site (which may or may not be designated as the *primary* site). It does NOT take into account that the HEC may already have a signature on file for the veteran as sent from a different, primary site.

The report may be requested for the previous income year, current income year, or next income year.

The report generated will include a count of the MT signature indicators for the local site in each of the following categories.

|         |                                                                   |
|---------|-------------------------------------------------------------------|
| YES     | Means Test images signed by veteran                               |
| NO      | Means Test images NOT signed by veteran                           |
| DELETED | Means Test signature indicators deleted by direct user edit\* |
| NULL    | A Means Test document has not been imaged                         |

\* The MT signature indicator would be deleted by direct user edit in cases where HEC assigned a value to an image and then later discovered that they had selected the wrong veteran/site/income year combination. The value “DELETED” is used in this report to track those cases wherein the indicator was entered and then later deleted due to an error being made as noted above.

## Means Test Signature Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Means Test Signature Detail Report

The Means Test Signature Reports menu provides for the generation of management reports containing Means Test signature statistics. Only users holding the DG SUPERVISOR security key may access this menu.

The statistics generated by these reports will only include those veterans who have a Means Test with Status of A, C, or Pending Adjudication as these are the only MT statuses that require obtaining a signature.

The purpose of the Means Test Signature Detail Report is to list those veterans at a particular site for which a signature still needs to be obtained. A veteran will ONLY be listed if NEITHER the local site NOR the primary site (if different) has obtained a signature. Once a signature has been obtained by EITHER the local OR primary site (if different), the veteran will be removed from this list.

The report may be requested for the previous income year, current income year, or next income year.

The report generated will include the following information on each veteran listed: name, Social Security Number, Means Test status and Means Test Signature Indicator (see table above for key). It will also give a count of the total number of veterans in the report and of the number of Nulls, Nos, and Deleted indicators.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add a New Means TestNote: With the installation of the Enrollment VistA Changes Release 2 (EVC R2) software (DG\*5.3\*688, IVM\*2.0\*115, and EAS\*1.0\*70), all Means Tests added with this option are created in the FEB 2005 format.

The Add a New Means Test option is used to enter a new Means Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Means Test.

- date of test cannot be before 7/1/86
- date of test cannot be before the last date of test
- new date of test cannot be added if one exists in the last 365 days unless it is a new calendar year

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Screen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. When the spouse address is updated, the SPOUSE ADDR LAST DT/TM UPDATED (#1.9) will be filed in the 408.13 file. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is important, as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed - to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. The “If you did not live with child, amount contributed to child last year?” question is no longer asked. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test (using the RE protocol).

## ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Screen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Means Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

> **NOTE:** The same rules apply to the printed 10-10EZR and 10-10EZ forms. The system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk, as included in the Means Test regardless of whether or not the child(ren)’s income has been marked as available to the veteran.

The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data has been updated by the Enrollment System Redesign application, the Total Reimbursed Medical Expenses amount and all Means Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

When adding a Means Test, completion of the test is optional; however, the marital and dependent children sections must be completed in order to complete the Means Test. If you choose not to complete the Means Test, it may be completed later through the Complete a Required Means Test or Edit an Existing Means Test options.

You may choose to print the 10-10EZR form when the Means Test is completed or print the prior Means Test (if one exists) at the beginning of the option.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adjudicate a Means Test

The Adjudicate a Means Test option is used to enter the patient's Means Test category into the system when the determination is returned from Adjudication. Only patients who currently have the Means Test status of PENDING ADJUDICATION may be selected.

Access to this option is limited to holders of the DG MEANSTEST security key.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means Test

The Complete a Required Means Test option is used to complete Means Tests generated through registration or by other circumstances. Only Means Test records with a status of REQUIRED and less than 1 year old from the effective date may be completed.

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means TestScreen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is important, as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran during the last calendar year or, if they did not live together, the veteran contributed to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test (using the RE protocol).
- ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means TestScreen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from the information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) have been marked as being included in the Means Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

> **NOTE:** The same rules apply to the printed 10-10EZR and 10-10EZ forms. The system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk, as included in the Means Test, regardless of whether or not the child(ren)’s income has been marked as available to the veteran.

The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed. The required information will be prompted for each column shown.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed, if the child had total employment income available.

The Gross Medical Expenses amount (Before FEB 2005 format) or Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable only by the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data has been updated by the Enrollment System Redesign (ESR) application, the Gross Medical Expenses amount or Total Non-Reimbursed Medical Expenses amount and all Means Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means Test

For Means Tests done prior to the existence of the Gross Medical Expenses amount, the system will re-calculate and present the Gross Medical Expenses amount from the patient’s existing Medical Expenses amount. For these historical Means Tests, the existing Medical Expenses amount becomes the Adjusted Medical Expenses amount. And, if and when the Gross Medical Expenses amount is updated, the system will automatically re-calculate the Adjusted Medical Expenses amount.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means Test

Completion of the Means Test through this option is mandatory. The Means Test status will automatically be updated once editing is complete.

You may choose to print the 10-10EZR form when the Means Test is completed.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

1.  Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social)
2.  Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
- \[1\] Social Security (Not SSI) +
- \[2\] U.S. Civil Service +
- \[3\] U.S. Railroad Retirement +
- \[4\] Military Retirement +
- \[5\] Unemployment Compensation +
- \[6\] Other Retirement +
- \[8\] Interest, Dividend, Annuity +
- \[9\] Worker’s Comp or Black Lung
3.  Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[1\] Cash, Amts in Bank Accts +
- \[2\] Stocks and Bonds

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a Required Means Test

Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:

- \[4\] Other Property or Assets –
- \[5\] Debts

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Document Comments on a Means Test

The Document Comments on a Means Test option is used to add/edit/delete comments to an existing Means Test. This allows the user to enter any pertinent information concerning the selected Means Test such as efforts made to obtain Means Test information.

You will be prompted for the patient name and the Means Test date. The latest Means Test date will appear as the default. A question mark (?) may be entered to obtain a list of Means Test dates for that patient. Comments may then be added through a word-processing field. Existing comments can be edited or deleted.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit an Existing Means Test

The Edit an Existing Means Test option is used to make changes to data in existing Means Tests less than 1 year old from the effective date. It may also be used to complete Means Tests on patients identified through Registration as requiring Means Testing. Only the latest Means Test may be edited. A Means Test that has been verified by the HEC and its corresponding original VAMC Means Test are both uneditable. If you choose such a Means Test, the system will display a message containing this information. However, this option will let you view or print such a test.

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit an Existing Means Test option operates similarly to the Add a New Means Test and Complete a Required Means Test options; however, it is the only option that allows changes to completed Means Tests. After these changes are entered, the system re-determines the patient's Means Test category and changes it, if necessary. If additional information is needed to make a determination or if it is necessary to refer the case to adjudication, the system prompts accordingly.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Means Test Editing Activity option.

A Means Test is required under the following conditions.

- primary eligibility is NSC or 0% service-connected non-compensable
- does not receive disability retirement from the military
- is not eligible for Medicaid
- is not awarded Medal of Honor
- is not on a domiciliary ward
- has not been Means Tested in the past year

Should these criteria change (excluding the last two), a Means Test status of NO LONGER REQUIRED will be assigned to the Means Test. Tests with this status cannot be edited.

Depending on the information entered on Screen 1, Screen 2 may appear with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

You may print the 10-10EZR form when the Means Test is complete.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

1.  Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
- \[1\] Social Security (Not SSI) +
- \[2\] U.S. Civil Service +
- \[3\] U.S. Railroad Retirement +
- \[4\] Military Retirement +
- \[5\] Unemployment Compensation +
- \[6\] Other Retirement +
- \[8\] Interest, Dividend, Annuity +
- \[9\] Worker’s Comp or Black Lung
4.  Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[1\] Cash, Amts in Bank Accts +
- \[2\] Stocks and Bonds
5.  Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[4\] Other Property or Assets –
- \[5\] Debts

Access to this option is limited to holders of the DG MEANSTEST security key.

How to Correct Means Test Inconsistency Errors

There are two types of conditions that cause the inconsistency messages:

1.  Data entry omissions or mistakes (error numbers 1-4 in Table 1)
2.  Erroneous or corrupted data filed in the records (error numbers 5-17 in Table 2)

> **NOTE:** Only the Primary site for the Means Test can correct the inconsistent data.

Table 1 - Inconsistency Messages Caused by Data Entry Omissions or Mistakes

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 38%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1. Dependent (&lt;dependent type&gt;) transmitted without SSN</td>
<td><p>A dependent is added to an Income Test without entering the Social Security Number (SSN). The dependent's relationship is displayed in the message to facilitate its update. Examples:</p>
<ul>
<li><blockquote>
<p>Dependent (SON) transmitted without SSN</p>
</blockquote></li>
<li><blockquote>
<p>Dependent (DAUGHTER) transmitted without SSN</p>
</blockquote></li>
<li><blockquote>
<p>Dependent (STEPDAUGHTER) transmitted without SSN</p>
</blockquote></li>
</ul></td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to enter the SSN for the dependent who generated the inconsistency message.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="even">
<td>2. Two dependents transmitted with same SSN</td>
<td>Data values in the SOCIAL SECURITY NUMBER field (#.09) in the INCOME PERSON file (#) for at least two dependents are identical.</td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to check the SSN for each of the dependents listed on the test.</p>
<p>3. Update the invalid SSN for the dependent who generated the inconsistency message.</p>
<p>4. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 24%" />
<col style="width: 38%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3. Shouldn't have income data if Child Had Income is NO</td>
<td><ul>
<li><blockquote>
<p>The dependent is not the spouse, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The INCOME AVAILABLE TO YOU field (#.12) in the INCOME RELATION file (#408.22) is No, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>Any of the income fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the dependent contain any amount. (Any entry including a zero [$0] is a valid amount.)</p>
</blockquote></li>
</ul>
<p>When the INCOME AVAILABLE TO YOU field (#.12) is set to No, and there are income entries for the dependent, the amounts are not visible on the INCOME screen.</p></td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field to YES.</p>
<p>3. Go to the GROSS INCOME (#2) screen and delete the amounts entered for the dependent.</p>
<p>4. Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1); use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field (#.12) back to NO.</p>
<p>5. Re-complete the test.</p></td>
</tr>
<tr class="even">
<td>4. No income data allowed if spouse didn't live w/Vet &amp; Vet did not contribute to spouse’s support</td>
<td><ul>
<li><blockquote>
<p>The data value in the INCOME RELATION file (#408.22) LIVED WITH PATIENT field (#.06) is "NO", and</p>
</blockquote></li>
<li><blockquote>
<p>The CONTRIBUTED TO SPOUSAL SUPPORT field (#.21) is “NO”,</p>
</blockquote></li>
<li><blockquote>
<p>Any of the income fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the spouse contain any amount. Any entry including a zero ($0) is a valid amount.</p>
</blockquote></li>
</ul>
<p>When the LIVED WITH PATIENT field is set to No, and the CONTRIBUTED TO SPOUSAL SUPPORT field is ”NO”, and there are income entries for the dependent, the amounts are not visible on the INCOME screen.</p></td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to YES.</p>
<p>3. Go to the GROSS INCOME (#2) screen and delete the amounts entered for the spouse.</p>
<p>4. Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1) and use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to NO.</p>
<p>5. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

Table 2- Inconsistency Messages Caused by Erroneous or Corrupted Data

Checks 5 through 9 in the table below are performed for Means Tests and Copay Exemption Tests when one or more of the following fields in the ANNUAL MEANS TEST file (#408.31) contains data:

- HARDSHIP? Field (#.2)
- HARDSHIP REVIEW DATE Field (#.21)
- SITE GRANTING HARDSHIP Field (#2.04)
- HARDSHIP EFFECTIVE DATE Field (#2.01)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5. Missing Hardship Indicator</td>
<td><ul>
<li><blockquote>
<p>The Hardship Indicator, HARDSHIP? field (#.2) is NULL, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>At least one of the other Hardship-related fields contains data.</p>
</blockquote></li>
</ul>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><blockquote>
<p>HARDSHIP?</p>
</blockquote></li>
<li><blockquote>
<p>SITE GRANTING HARDSHIP</p>
</blockquote></li>
<li><blockquote>
<p>HARDSHIP EFFECTIVE DATE</p>
</blockquote></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="even">
<td>6. Missing Site Granting Hardship</td>
<td><p>The SITE GRANTING HARDSHIP field (#2.04) is NULL, and at least one of the other Hardship-related fields contains data.</p>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><blockquote>
<p>HARDSHIP?</p>
</blockquote></li>
<li><blockquote>
<p>SITE GRANTING HARDSHIP</p>
</blockquote></li>
<li><blockquote>
<p>HARDSHIP EFFECTIVE DATE</p>
</blockquote></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
</tbody>
</table>

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>7. Missing Hardship Effective Date</td>
<td><ul>
<li><blockquote>
<p>The HARDSHIP EFFECTIVE DATE field (#2.01) is NULL, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The year in the DATE OF TEST field (#.01) is the year 2000 or later, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>At least one of the other Hardship-related fields contains data.</p>
</blockquote></li>
</ul>
<p>Starting in the year 2000, all hardships must have an effective date.</p>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><blockquote>
<p>HARDSHIP?</p>
</blockquote></li>
<li><blockquote>
<p>SITE GRANTING HARDSHIP</p>
</blockquote></li>
<li><blockquote>
<p>HARDSHIP EFFECTIVE DATE</p>
</blockquote></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="even">
<td>8. Invalid Hardship Effective Date</td>
<td><ul>
<li><blockquote>
<p>The date in the HARDSHIP EFFECTIVE DATE field (#2.01) could not be converted into FileMan format, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>At least one of the other Hardship-related fields contains data.</p>
</blockquote></li>
</ul></td>
<td>Use the Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="odd">
<td>9. Hardship Effective Date earlier than Means Test Date</td>
<td><ul>
<li><blockquote>
<p>The HARDSHIP EFFECTIVE DATE field (#2.01) is <strong>not</strong> NULL, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The date is prior to the date in the DATE OF TEST field (#.01) in the ANNUAL MEANS TEST file (#408.31), <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>At least one of the other Hardship-related fields contains data.</p>
</blockquote></li>
</ul></td>
<td>Use the Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
</tbody>
</table>

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10. Source of Test must be identified</td>
<td><p>The SOURCE OF INCOME TEST field (#.23) in the ANNUAL MEANS TEST file (#408.31) does <strong>not</strong> contain one of the following values found in the SOURCE OF INCOME TEST file (#408.34):</p>
<ul>
<li><blockquote>
<p>VAMC (#1)</p>
</blockquote></li>
<li><blockquote>
<p>IVM (#2)</p>
</blockquote></li>
<li><blockquote>
<p>DCD (#3)</p>
</blockquote></li>
<li><blockquote>
<p>OTHER FACILITY (#4)</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="even">
<td>11. Site Conducting Test must be identified</td>
<td>The SITE CONDUCTING TEST field (#2.05) in the ANNUAL MEANS TEST file (#408.31) is NULL <strong>and</strong> the SOURCE OF INCOME TEST field (#.23) is OTHER FACILITY.</td>
<td>The means test can only be corrected at the site where it was entered/completed.</td>
</tr>
<tr class="odd">
<td>12. Incorrect Means Test Status for Test-Determined Status</td>
<td><ul>
<li><blockquote>
<p>The INCOME field (#.04) in the ANNUAL MEANS TEST file (#408.31) is greater than the THRESHOLD A field (#.12), <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The HARDSHIP? field (#.2) is "NO" or NULL, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>the ADJUDICATION DATE/TIME field (#.1) is NULL, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The TEST-DETERMINED STATUS field (#2.03) is neither MT COPAY REQUIRED ("C") nor PENDING ADJUDICATION ("P").</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="even">
<td>13. Invalid Means Test Status for Test-Determined Status</td>
<td><p>The TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31) does not contain a valid value:</p>
<ul>
<li><blockquote>
<p>MT COPAY EXEMPT (A)</p>
</blockquote></li>
<li><blockquote>
<p>MT COPAY REQUIRED (C)</p>
</blockquote></li>
<li><blockquote>
<p>PENDING ADJUDICATION (P)</p>
</blockquote></li>
<li><blockquote>
<p>GMT COPAY REQUIRED (G)</p>
</blockquote></li>
</ul>
<p>This is caused when there is an error in the calculation of the Test-Determined Status due to corruption in the Means Test data.</p></td>
<td><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="odd">
<td>14. Income plus net worth not greater than threshold value-incorrect status</td>
<td><ul>
<li><blockquote>
<p>The INCOME field (#.04) in the ANNUAL MEANS TEST file (#408.31) is not greater than the THRESHOLD A field (#.12), <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The NET WORTH field (#.05) added to the INCOME is not greater than the THRESHOLD, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The TEST-DETERMINED STATUS field (#2.03) is MT COPAY REQUIRED ("C").</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15. Copay Test Status should be &lt;calculated status&gt;</td>
<td>The Copay Exemption Status is calculated based on income and net worth, then compared to the TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31). This message is returned when the calculated status does not equal the TEST-DETERMINED STATUS.</td>
<td><p>1. From the Copay Exemption Test Menu, use the Edit an Existing Copay Exemption Test option to view the data on each of the Income Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="even">
<td>16. Invalid Copay Test Status for Test-Determined Status</td>
<td><p>The TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31) does not contain one of the following values:</p>
<ul>
<li><blockquote>
<p>EXEMPT (E)</p>
</blockquote></li>
<li><blockquote>
<p>NON-EXEMPT (M)</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Copay Exemption Test Menu, use the Edit an Existing Copay Exemption Test option to view the data on each of the Income Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
<tr class="odd">
<td>17. Income does not exceed child exclusion amount-educational expense not allowed</td>
<td><ul>
<li><blockquote>
<p>The dependent is not the spouse, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>the EDUCATIONAL EXPENSES field has an amount, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The CHILD INCOME EXCLUSION for the Income Year is not less than the TOTAL INCOME FROM EMPLOYMENT</p>
</blockquote></li>
</ul>
<p>This message will only be displayed when the Means Test process failed to delete the EDUCATIONAL EXPENSES from the INDIVIDUAL ANNUAL INCOME record for the child.</p>
<p>The normal processing of the Post-Secondary Education Expenses for a child between the ages of 18 and 23 are:</p>
<ul>
<li><blockquote>
<p>If the TOTAL INCOME FROM EMPLOYMENT is above the CHILD INCOME EXCLUSION threshold found in the MAS PARAMETERS file (#43), the expenses can be entered.</p>
</blockquote></li>
<li><blockquote>
<p>When the income amount is modified to be below this threshold, the EDUCATIONAL EXPENSES are deleted from the INDIVIDUAL ANNUAL INCOME record for the child.</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

GMT Thresholds Lookup by ZIP Code

On January 23, 2002, former President Bush signed into law H.R. 3477, The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001. Section 202 of this Act requires the implementation of U.S. Department of Housing and Urban Development (HUD) Indices to determine geographic income thresholds in support of more discrete Means Testing. A new GMT copayment status identifies veterans who qualify for a reduced inpatient copayment rate. The effective date of the regulation to support this legislation is October 1, 2002. Like traditional Means Test thresholds, the GMT Thresholds will be applied in a retrospective manner (i.e., HUD Indices published in Calendar Year 2002 will be used for Means Tests performed in Calendar Year 2003). Information about HUD income limits is available on the Data Sets Page of the HUD User Web Site at http://www.huduser.org/datasets/il.html.

The GMT Thresholds will be uploaded into VistA annually, along with the traditional Means Test threshold values, in a patch released in December of each year. They will be activated on January 1<sup>st</sup> of each year. The indices from previous years will be stored indefinitely in both VistA and HEC systems. For information about the implementation of HUD Indices, refer to the GMT Installation Guide and GMT Technical Manual.

> **NOTE:** On January 17, 2003, VA discontinued enrolling new Priority Group 8 veterans into the VA health care system based on VA’s inability to provide timely and quality health care to all enrolled veterans. The new relaxed Priority Group 8 enrollment restrictions allow certain PG8 veterans to be enrolled in the VA health care system if their household income does not exceed the current VA income thresholds (Means Test threshold and/or Geographical Means Test threshold) by more than 10%. These changes do not open enrollment to all PG8 veterans, however. For more details, visit the VA Health Care Eligibility & Enrollment Web Site at <http://www.va.gov/healtheligibility>.

The GMT software provides the following functionality.

1.  Automatically populates City, State, and County fields of the Patient Demographics Screen when ZIP Code is entered during patient registration or edit of patient demographic data (load/edit), unless the Bad Address Indicator is set. (Refer to Screen 1, Data Group 4, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
6.  State and County fields can only be edited by users who hold the EAS GMT COUNTY EDIT security key.
7.  Automatic Address Changes from HEC will clear the Bad Address Indicator field (if it was set). (Refer to Screen 1, Data Group 4, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
8.  A conversion of veterans based on their existing financial assessment information will be run at the HEC. An ongoing process assigns veterans to the appropriate medical care copayment and enrollment priority group upon completion of a financial assessment.
9.  NSC and non-compensable 0% SC veterans with current income above the MT Threshold and below the applicable GMT Threshold will be placed in the new Means Test status “GMT Copayment Required”. These veterans will be assigned to Enrollment Priority Group 7 (unless Catastrophically Disabled \[CD\] or exposed to Agent Orange, Ionizing Radiation, or SW Asia Conditions). Veterans who are in GMT Copay Required status must submit income for yearly testing.
10. Veterans who are subject to the full inpatient medical care copayment and placed in Enrollment Priority Group 8 (unless CD or exposed to toxic substances) include:
- Veterans with income greater than the GMT threshold plus 10% where GMTT\>MTT
- Veterans declining to provide income info
- Veterans with income greater than the MT threshold plus 10% who live in an area where the GMT threshold is less than or equal to the MT threshold
- Veterans with income above the MT threshold plus 10% whose income info is over one year old at the time the GMT software is installed.
11. Although this does not affect the GMT functionality, all user viewable references to Category A and Category C Means Test statuses in enrollment-related software have been modified to reflect the following changes:
- Category A (Cat A) is now MT Copay Exempt
- Category C (Cat C) is now MT Copay Required.
12. A variety of reports and data screens have been modified to display the new subcategories ‘b’ and ‘d’ for Enrollment Priority Group 8 and GMT Copayment Required status.
13. Provides a new user option, GMT Thresholds Lookup by ZIP Code, which displays GMT Threshold values for a valid user-specified ZIP Code.
14. Adds a new field, Hardship Reason, to the Hardship Determinations Screen.
15. Agent Orange and SW Asia Conditions will include a new Special Treatment Authority Expiration date fields that will be added to the MAS PARAMETERS file (#43). The initial value of these fields will be null or empty. A subsequent patch will be released to populate the date fields once the expiration of the Special Treatment Authority is scheduled to expire. The assigning of newly enrolled veterans to Priority Group 6 determination rules whose AO Indicator is "Y" and Location is *Vietnam* and/or their SWAC exposure indicator is "Y" will be ignored if the Special Treatment Authority Expiration Date fields are not null or empty.

This option is used to display GMT Threshold values for a valid Postal Code (ZIP Code). The only user prompt is “ZIP Code:”, and a response is required. You must enter a ZIP Code or a city name to generate an output, or a caret (^) to return to the menu. If you enter a city name and the software finds multiple cities with the same name, it returns a list of the cities with their corresponding ZIP Codes from which you can make your selection.

The software returns the following information for a valid ZIP Code.

- ZIP Code
- County Name
- State
- Income year in which the GMT Thresholds apply
- Federal Information Processing Standard (FIPS) \[County\] Code
- Number of family members in household
- GMT Threshold dollar amounts for up to eight members in household
- Family size adjustments information for all income limits
- The formula for determining GMT Threshold dollar amounts for households with more than eight family members

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hardships

This option replaces the Change a Patient’s Means Test Category option. It allows users to grant hardships for the current Means Test when the test is less than 1 year old from the effective date.

Hardship Determinations continue to be the responsibility of the VAMCs; however, they will be sent to the HEC and distributed nationally along with the Primary Means Test to all VAMCs that the veteran has visited. Once granted, a Hardship is in effect until it expires on December 31 of the calendar year in which it was granted or is manually expired in the Enrollment System. The VAMC that granted the hardship will retain the original Means Test Status when the status changes. For example, if a Hardship determination changes the original status from MT Copay Required to MT Copay Exempt, the new status (Exempt) is stored as the Means Test status. The original status (MT Copay Required) is then stored as Test Determined Status.

After the GMT conversion runs at the HEC, if a veteran's Means Test status is MT Copay Required, the user is prompted to enter the status (GMT Copay Required or MT Copay Exempt) and a Hardship Reason.

The Hardship Determinations screen provides the following List Manager actions.

- GRANT HARDSHIP

> Allows you to grant hardships for current Means Tests for the selected patient and will prompt for the Hardship Effective Date. Once granted, a hardship remains in effect until a new Means Test is completed.

- EDIT COMMENTS

> Allows you to add, edit, and delete comments related to hardships for current Means Tests for the selected patient.

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pseudo SSN Report for Means Test Dependents

The Pseudo SSN Report for Means Test Dependents is used to print a report of spouses and/or dependents, sorted by patient, who have Pseudo SSNs. You can choose to print the report for one or all Pseudo SSN reasons.

The output includes:

1.  Report title and page number
2.  Whether the report includes one or all Pseudo SSN reasons
3.  Report date
4.  Patient name and SSN
5.  Dependent/spouse name and relationship to patient
6.  Dependent/spouse Pseudo SSN
7.  Dependent/spouse Pseudo SSN reason
8.  A summary at the end of the report provides the following information:
- If you chose to print the report for a specific Pseudo SSN reason, the summary provides the total number of dependents with Pseudo SSNs.
- If you chose to print the report for all Pseudo SSN reasons, the summary provides the total number of dependents with Pseudo SSNs *and* the number of dependents/spouses for each of the reason(s) selected.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

View a Past Means Test

The View a Past Means Test option is used to view past Means Tests data. The option does not allow editing. You will be prompted for the patient's name and the date of the Means Test you wish to view. Double question marks (??) entered at the date prompt will provide you with a list of the patient's Means Test dates from which to choose.

If certain circumstances exist for the selected patient, messages may be displayed. A message will be printed if no detailed income information is on file for the veteran, or if the veteran's Means Test status is NO LONGER REQUIRED. Since income data can be entered/edited through registration, once a Means Test has this status, the income data being viewed may differ from that originally entered as part of the Means Test.

You will be able to view the following four Means Test screens through this option.

> Screen 1 - Marital Status/Dependents

> Screen 2 - Previous Calendar Year Gross Income

> Screen 3 - Deductible Expenses

> Screen 4 - Previous Calendar Year Net Worth (only if data is present)

The option may display the dependent totals not converted. Totals not converted will only be displayed under the following conditions.

- Converted totals exist and Means Test income is 0 or greater
- For a spouse - the veteran is married but detailed income information is not available
- For dependent children - the veteran has dependent children but detailed income information is not available

The option will display Screen 4 only when data that had been entered on Screen 4 prior to patch DG\*5.3\*1014 is present

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Merge Duplicate MT/Copay Dependents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You might want to use the Duplicate Dependents Report option to generate a report of potential duplicate entries in the PATIENT RELATION file (#408.12) before using this option.

The Merge Duplicate MT/Copay Dependents option is used to merge dependents considered to be duplicates in the PATIENT RELATION file (#408.12). The software prompts you to select a Patient SSN. Enter the SSN for the duplicate dependent whose data you want to merge. The software searches for entries in the PATIENT file (#2) and the PATIENT RELATION file (#408.12), and displays the results.

The software determines what patient you must use to merge the duplicate dependent information, and asks if you’d like to continue with the merge. YES response merges the data into the original entry, and deletes the duplicate entry. The software confirms that the merge was successful. NO response returns you to the “Select Patient SSN:” prompt. Data deleted during this process is stored in a temporary global for 10 days.

You must hold the DG MEANSTEST security key to access this option.

## Purge Duplicate Income Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows holders of the DG MEANSTEST security key to purge duplicate tests that appear on the same day. It will also delete tests that have a null status.

Duplicate tests are defined as those that are of the same test type, test date, and test status.

The option will let you run a small group of records or all records. It will be scheduled via TaskMan and can be stopped via TaskMan if desired. The small group will process 5 or so qualified records and then stop automatically. The purge clean up can be reselected any time after it has been stopped and it will resume where it left off.

You will receive a summary MailMan message showing the number of records processed and purged from the ANNUAL MEANS TEST file (#408.31) and subsequent MailMan message(s) listing details of what was deleted.

## Purge Income Test Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to monitor the cleanup process selected in the Purge Duplicate Income Tests option. The following is an example of what may appear on the screen when utilizing this option.

1/20/05 1:47:27 pm Completed 100%

<u>Cleanup Duplicates in the Means Test file</u>

Status Total recs Dupes Purged Nulls Purged Last DFN Completed Time

COMPLETED 3 0 0 12 1/20/05@13:47:25

screen refreshes automatically every 5 seconds

Press \<Enter\> to Stop Monitor.........

## View Means Test Editing Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Means Test Editing Activity option provides a method of viewing changes made to Means Test data. If the selected patient has more than one Means Test on file, they will be listed for selection.

The computer keeps track, by patient, each time any change is made to the Means Test data either through Means Test or Registration. The types of changes that are captured are shown below. Both the old and new status value will be shown on the report.

- Add New Means Test
- Adjudicate Means Test
- Means Test Category Change
- Edit Existing Means Test Info
- Means Test Status Change
- Primary Means Test Change

The output generated by this option will include the following information: patient name, Means Test date, date of change, type of change, and the user who made the change. The time will appear along with the date of change if it was part of the original entry.

If no changes have been made to the selected Means Test, the output will state that fact.

You must hold the DG MEANSTEST security key to access this option.