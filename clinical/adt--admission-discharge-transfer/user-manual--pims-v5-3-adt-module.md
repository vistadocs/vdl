---
title: PIMS Version 5.3 User Manual - ADT Module
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: ADT Module
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The PIMS User Manual is divided into modules, ADT and Scheduling. The PIMS ADT User Manual provides instructional guidance to a broad range of users within VA medical facilities in daily use of the Admission-Discharge-Transfer (ADT) Module of the PIMS software.
audience: 
keywords: 
  - patient
  - enrollment
  - table
  - report
  - test
  - status
  - code
  - date
  - class
  - manual
page_count: 0
word_count: 12928
section_count: 23
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/adtbe_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/adtbe_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

## Table of Contents

  - [## User Manual - Menus, Intro, Orientation, etc.](#user-manual-menus-intro-orientation-etc)
  - [User Manual - ADT Outputs Menu](#user-manual-adt-outputs-menu)
  - [User Manual - Bed Control Menu](#user-manual-bed-control-menu)
  - [User Manual - Contract Nursing Home Rug Menu](#user-manual-contract-nursing-home-rug-menu)
  - [User Manual - Copay Exemption Test Supervisor Menu](#user-manual-copay-exemption-test-supervisor-menu)
  - [User Manual - MAS Code Sheet Manager Menu](#user-manual-mas-code-sheet-manager-menu)
  - [User Manual - Means Test Supervisor Menu](#user-manual-means-test-supervisor-menu)
  - [User Manual - PTF Menu](#user-manual-ptf-menu)
  - [User Manual - Registration Menu](#user-manual-registration-menu)
  - [User Manual - RUG-II Menu](#user-manual-rug-ii-menu)
  - [User Manual - Security Officer Menu](#user-manual-security-officer-menu)
  - [User Manual - Supervisor ADT Menu](#user-manual-supervisor-adt-menu)
  - [User Manual - Veteran Identification Card Menu](#user-manual-veteran-identification-card-menu)
  - [Introduction](#introduction)
  - [Orientation](#orientation)
    - [How To Use This Manual](#how-to-use-this-manual)
    - [ICD-10 Searches](#icd-10-searches)
  - [Orientation](#orientation-1)
    - [On-line Help](#on-line-help)
  - [Enrollment Query Process](#enrollment-query-process)
  - [Enrollment Query Process](#enrollment-query-process-1)
  - [Enrollment Query Process](#enrollment-query-process-2)
  - [Enrollment Priority Algorithm](#enrollment-priority-algorithm)
  - [Military Sexual Trauma stand-alone Menu](#military-sexual-trauma-stand-alone-menu)
    - [MST Status Add/Edit](#mst-status-addedit)
    - [MST Outputs](#mst-outputs)
  - [Home Telehealth stand-alone Menu](#home-telehealth-stand-alone-menu)
    - [Patient Sign-Up/Inactivation](#patient-sign-upinactivation)
    - [Patient Inactivation](#patient-inactivation)
    - [Patient Summary Report](#patient-summary-report)
    - [Transmission Report](#transmission-report)
---
title: |
  ADT Module
  PIMS Version 5.3
  User Manual
---
![](pims-version-5-3-user-manual-adt-module/001.png)
December 2023
Office of Information and Technology (OIT)
PIMS V. 5.3 ADT Module User Manual
The manual is broken down into the following PDF files.
User Manual - Menus, Intro, Orientation, etc.
User Manual - ADT Outputs MenuUser Manual - Bed Control Menu
User Manual - Contract Nursing Home RUG Menu
User Manual - Copay Exemption Test Supervisor MenuUser Manual - MAS Code Sheet Manager MenuUser Manual - Means Test Supervisor MenuUser Manual - PTF MenuUser Manual - Registration MenuUser Manual - RUG-II MenuUser Manual - Security Officer MenuUser Manual - Supervisor ADT MenuUser Manual - Veteran ID Card Menu
Revision History
Initiated on 11/5/04
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description (Patch # if applic.)</th>
<th>Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2023</td>
<td><p>DG*5.3*1095</p>
<p>Updated sections pertaining to COMPACT Act administrative eligibility:</p>
<p><strong>Enrollment Priority Algorithm.</strong> Added Public Law No: 116-214</p></td>
<td>VA PM</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/2023</td>
<td><p>DG*5.3*1103</p>
<p>Updated Enrollment Priority Algorithm Table to add TOXIC EXPOSURE RISK ACTIVITY (TERA) (<strong>p. <a href="#TERA_indicator">33</a></strong>)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/2023</td>
<td><p>DG*5.3*1098</p>
<p>Updated Enrollment Priority Algorithm Table to add WORLD WAR II</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/2021</td>
<td><p>DG*5.3*1034</p>
<p>Updated Former OTH Patient Eligibility Change Report and Former OTH Patient Detail Report under Other Than Honorable Reports Menu option to include inpatient care</p>
<p>Added missing reports from DG*5.3*952</p>
<blockquote>
<p>Tracking Report (OTH-90)</p>
<p>Authorization Reports (OTH-90)</p>
<p>Other Than Honorable MH Status Report</p>
<p>Potential 'OTH' Patient Report</p>
</blockquote>
<p>Added missing report from DG*5.3*977</p>
<blockquote>
<p>Statistical Report (OTH-90)</p>
</blockquote></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/2021</td>
<td><p>DG*5.3*1018 (Blue Water Navy)</p>
<p>-Added Blue Water Navy to Agent Orange Exposure Location in Enrollment Priority Group Algorithm – Group 6 Table and Footnote</p>
<p>-Added Continuous Enrollment rule for Vietnam/Blue Water Navy</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/16/2020</td>
<td><p>DG*5.3*1025</p>
<p>Added Former OTH Patient Eligibility Change Report and Former OTH Patient Detail Report to Other Than Honorable Reports Menu option</p>
<p>DG*5.3*952, DG*5.3*977</p>
<p>Update the DG Registration Menu with the ‘Other Than Honorable Menu’</p>
<p>Other Than Honorable Menu</p>
<p>OTH Management</p>
<p>Patient Inquiry (OTH)</p>
<p>Other Than Honorable Reports …</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/2020</td>
<td><p>DG*5.3*993 (Separate Registration from Enrollment)</p>
<p>-Added VA OIG Audit under section “Public Law 114-315 Change”</p>
<p>-Added “Null” row to Enrollment Priority Algorithm table</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/2020</td>
<td><p>DG*5.3*977 (SHRPE):</p>
<p>- Added "Suicide High Risk Patient Enhancement patch" notes to the "Military Sexual Trauma stand-alone Menu" sections.</p>
<p>- Also under the "Military Sexual Trauma stand-alone Menu" section, specifically under the "MST Outputs" sub-section, added "No longer in Service" statement next to the relevant reports for which the statement applies.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/2019</td>
<td><p>DG*5.3*972 (Medal of Honor (MOH) Awardees in Priority Group 1)</p>
<p>- Added information about Public Law 114-315</p>
<p>- Added MOH to Enrollment Priority Group 1 under the Enrollment Priority Algorithm</p>
<p>- Added MOH AWARD DATE, MOH STATUS DATE, and MOH COPAYMENT EXEMPTION DATE to Enrollment Query Process fields</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/2016</td>
<td><p>DG*5.3*909 (Camp Lejeune-Veterans)</p>
<p>- Added Camp Lejeune to list of</p>
<p>fields under Enrollment Query<br />
Process</p>
<p>- Added information about Public<br />
Law 112-154</p>
<p>- Added Camp Lejeune to<br />
Enrollment Priority Group 6<br />
under the Enrollment Priority<br />
Algorithm</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/2014</td>
<td><p>DG*5.3*850 (ICD-10 Implementation):</p>
<ul>
<li><p>Added the following section in (Removed link)</p></li>
<li><p>Updated (Removed link) section</p></li>
<li><p>Changed ICD-9 to ICD in (Removed link) section</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/25/2011</td>
<td><p>DG*5.3*840 – ESR 3.5 VistA changes for PL111-163.</p>
<p>Updated Query menu with CURRENT MOH INDICATOR field. Added Public Law 111-163 explanation to Priority Algorithm section. Updated glossary.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/3/2010</td>
<td><p>DG*5.3*754 – ESR 3.1 VistA</p>
<p>Added and removed fields in the PATIENT file (#2).<br />
Updated <em>Enrollment Priority Algorithm,</em> <em>PG 6</em> algorithm.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/18/10</td>
<td><p>DG*5.3*754 – ESR 3.1 VistA</p>
<ul>
<li><p>Added addition fields in the PATIENT file (#2) will be uploaded as a result of the query reply in the <strong>Enrollment Query Process</strong> section.</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/17/09</td>
<td><p>DG*5.3*754 – ESR 3.1 VistA Changes to Priority Algorithm:</p>
<ul>
<li><p>New Special Treatment Authority Expiration date fields for Agent Orange and SWAC to the Means Test User Menu section.</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/10/09</td>
<td><p>DG*5.3*803 – Priority Group 8 Changes</p>
<ul>
<li><blockquote>
<p>Updated the <em>Enrollment Priority Algorithm</em> section and <em>Enrollment Priority Group</em> table</p>
</blockquote></li>
<li><blockquote>
<p>Updated <em>Continuous Enrollment Rules</em> in <em>Enrollment Priority Algorithm</em> section</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/30/09</td>
<td><p>DG*5.3*688 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<ul>
<li><blockquote>
<p>Updated Enrollment Priority Group 6 in Enrollment Priority Algorithm</p>
</blockquote></li>
<li><blockquote>
<p>Added Project 112/SHAD Indicator to Enrollment Query Process section</p>
</blockquote></li>
<li><blockquote>
<p>Changed <em>Environmental Contaminants</em> to <em>SW Asia Conditions</em>.</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/29/09</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/4/08</td>
<td>DG*5.3*644 – Home Telehealth – enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/6/07</td>
<td>DG*5.3*729 - PTF Fields No Longer Needed - enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/11/07</td>
<td><p>DG*5.3*653 – Enrollment VistA Changes Release 1 (EVC R1) –</p>
<ul>
<li><blockquote>
<p>Added names of new pseudo SSN report options</p>
</blockquote></li>
<li><blockquote>
<p>Updated Enrollment Priority Algorithm section for SHAD exposure</p>
</blockquote></li>
<li><blockquote>
<p>Added new Z07 Build Consistency Check option</p>
</blockquote></li>
<li><blockquote>
<p>Added Rule 8 to Continuous Enrollment Rules</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/3/06</td>
<td>DG*5.3*659 – Updating Ionizing Radiation exposure methods – revised Enrollment Priority Group 6 in the Enrollment Priority Algorithm table</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/27/06</td>
<td>DG*5.3*717 – Continuous Enrollment Enhancements – revised the continuous enrollment rules in the Enrollment Priority Algorithm section</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/14/06</td>
<td>DG*5.3*694 – Added new option, Invalid State/Inactive County Report, to Registration Menu</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/20/06</td>
<td>DG*5.3*702 - Edit Census Date Parameters option changed to display only</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/22/06</td>
<td>DG*5.3*687 - Remove PTF Archive/Purge function</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/21/06</td>
<td><p>DG*5.3*672 – Enrollment VistA Changes Early Release</p>
<p>Added new option to Supervisor ADT menu.</p>
<p>Updated continuous enrollment priority algorithm.</p>
<p>Updated PG3 in enrollment priority algorithm.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/9/05</td>
<td>DG*5.3*658 – Address Updates. Added <em>Patient Address Update</em> option to Registration Menu and Option Index</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/3/05</td>
<td>DG*5.3*635 Enhancements – PTF 801 screen updates</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/05</td>
<td>DG*5.3*624 - 10-10EZ 3.0 Enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/5/05</td>
<td>DG*5.3*666 Enhancements - add 2 options to Security Officer Menu</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/23/04</td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/5/04</td>
<td>DG*5.3*564 - HEC VistA Enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

## ## User Manual - Menus, Intro, Orientation, etc.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menus

Introduction

Orientation

> How to Use This Manual

> On-line Help

Enrollment Query Process

Enrollment Priority Algorithm

Military Sexual Trauma stand-alone Menu

Home Telehealth stand-alone Menu

Glossary

> Military Time Conversion Table

Option Index

## User Manual - ADT Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10/10 Print

ADT Third Party Output Menu

> Patient Review Document

> Review Document by Admission Range

> Veteran Patient Insurance Information

AMIS Reports Menu

> AMIS 334-341 Reports

> AMIS 345-346 Reports

> AMIS 401-420 Reports

Bed Availability

Disposition Outputs Menu

> Disposition Time Processing Statistics

> Log of Dispositions

> Summary of Dispositions

Enrollment Reports

> Enrolled Veterans Report

> Pending Applications for Enrollment

> Enrollees by Status, Priority, Preferred Facility

> Upcoming Appointments without Enrollment

> EGT Impact Report

> Non-Treating Preferred Facility Clean up

> Former OTH Patient Eligibility Change Report

> Former OTH Patient Detail Report

Gains and Losses (G&L Sheet)

Inconsistent Data Elements Report

Inpatient/Lodger Report Menu

> Absence List

> ASIH Listing

> Current Lodger List

> Female Inpatient List (Current)

> Historical Female Inpatient List

> Historical Inpatient Listing

> Inpatient Listing

> Inpatient Roster

> Insurance List of UNKNOWNs for Inpatients

> Lodgers for a Date Range

> Patient Movement List

> Religion List for Inpatients

> Seriously Ill Inpatient Listing

> Treating Specialty Inpatient Information

User Manual - ADTOutputs Menu, cont.

Means Test Outputs

> Duplicate Spouse/Dependent SSN Report

> Hardship Review Date

> List Required/Pending Means Tests

> Means Test Indicator of 'U' Report

> Means Test Specific Income Amount Report

> Means Test Specific Income Less Threshold Report

> Means Test w/Previous Year Threshold

> Patients Who Have Not Agreed To Pay Deductible

> Required Means Test At Next Appointment

N/T Radium Treatment Pending Verification List

Pending/Open Disposition List

Print Patient Label

Scheduled Admission Statistics

Scheduled Admissions List

Treating Specialty Print

VBC Form By Admission Date

VBC Form for Specific Patient

Waiting List Output

Z07 Build Consistency Check

## User Manual - Bed Control Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Admit a Patient

Cancel a Scheduled Admission

Check-in Lodger

Delete Waiting List Entry

Detailed Inpatient Inquiry

Discharge a Patient

DRG Calculation

Extended Bed Control

Lodger Check-out

Provider Change

Schedule an Admission

Seriously Ill List Entry

Switch Bed

Transfer a Patient

Treating Specialty Transfer

Waiting List Entry/Edit

## User Manual - Contract Nursing Home Rug Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Close a CNH PAI Record

CNH PAI Edit

Create a CNH PAI Record

Delete a CNH PAI Record

Open a Closed or Transmitted CNH PAI

Outputs Menu

> Incomplete PAIs by Location

> PAIs for a Date Range

> Record Status Report

> RUG-II Index

> Single PAI Print

RUG-II Grouper

Test Grouper

## User Manual - Copay Exemption Test Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copay Exemption Test User Menu

> Add a Copay Exemption Test

> Copay Exempt Test Needing Update At Next Appt.

> Edit an Existing Copay Exemption Test

> List Incomplete Copay Exemption Test

> View a Past Copay Test

Delete a Copay Exemption Test

View Copay Exemption Test Editing Activity

## User Manual - MAS Code Sheet Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

## User Manual - Means Test Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

> View a Past Means Test

Merge Duplicate MT/Copay Dependents

Purge Duplicate Income Tests

Purge Income Test Monitor

View Means Test Editing Activity

## User Manual - PTF Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Census Menu

> Load/Edit PTF Data

> Close Open Census Record

> Census Status Report

> Inquire Census Record

> Other Census Outputs Menu

> Comprehensive Census Report

> Productivity Report by Clerk (Census Only)

> Records By Completion Status (Census Only)

> Transmitted Census Records List

> Unreleased Census Records Report

> Release Closed Census Records

> Transmit Census Records

> Open Closed Census Records

> Open Released or Transmitted Census Records

> 099 Transmission for Census Record

> Supervisor Menu

> Display Census Date Parameters

> Regenerate Census Workfile

> Fee Basis Census Status Report

Checkoff PTF Message

DRG Calculation

Enter PTF Message

Inquire PTF Message

Load/Edit PTF Data

National Patient Care Database

> Transmission Reports

> PIMS Events Transmitted Yesterday

> PIMS Events Transmitted for Date Range

> Transmission Utilities

> Retransmit Patient Demographics

> Retransmit Admission Data

> Retransmit Entry in ADT/HL7 PIVOT File

Open Closed PTF Record

Open Released or Transmitted PTF Records

PTF Output Menu

> Admissions without an Associated PTF Record

> Comprehensive Report by Admission

> Diagnostic Code PTF Record Search

> DRG Information Report

User Manual - PTF Menu, cont.

> DRG Reports Menu

DRG Case Mix Summary

> ALOS Report for DRGs

> Batch Multiple DRG Reports

> DRG Frequency Report

> DRG Index Report

> Trim Point DRG Report

> Inquire PTF Record

> Listing of Records by Completion Status

> Means Test Indicator of 'U' Report

> MPCR Inquiry

> Open PTF Record Listing

> Patient Summary by Admission

> Pro Fee Coding Not Sent to PCE

> Productivity Report by Clerk

> Surgical Code PTF Record Search

> Transmitted Records List

> Unreleased PTF Record Output

PTF Transmission

Quick Load/Edit PTF Data

Release PTF Records for Transmission

Set Up Non-VA PTF Record

Update DRG Information Menu

> Update Transfer DRGs for Current FY

Utility Menu

> 099 Transmission

> Record Print-Out (RPO)

> Delete PTF Record

> Establish PTF Record from Past Admission

> Print Special Transaction Request Log

> PTF Expanded Code Listing

> Purge Special Transaction Request Log

> Set Transmit Flag on Movements

> Validity Check of PTF Record

## User Manual - Registration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disposition an Application

Patient Enrollment

Other Than Honorable Menu

OTH Management

Patient Inquiry (OTH)

Other Than Honorable Reports …

> Tracking Report (OTH-90)

> Authorization Reports (OTH-90)

> Statistical Report (OTH-90)

> Other Than Honorable MH Status Report

> Potential 'OTH' Patient Report

> Former OTH Patient Eligibility Change Report

> Former OTH Patient Detail Report

Purple Heart Request History

Purple Heart Status Report

Add/Edit/Delete Catastrophic Disability

Collateral Patient Register

Copay Exemption Test User Menu

> Add a Copay Exemption Test

> Copay Exempt Test Needing Update at Next Appt.

> Edit an Existing Copay Exemption Test

> List Incomplete Copay Exemption Test

> View a Past Copay Test

Death Entry

Delete a Registration

Disposition Log Edit

Edit Inconsistent Data for a Patient

Eligibility Inquiry for Patient Billing

Eligibility Verification

Enter/Edit Patient Security Level

Invalid State/Inactive County Report

Load/Edit Patient Data

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

Patient Address Update

Patient Inquiry

User Manual - RegistrationMenu, cont.

Preregistration Menu

> Display Preregistration Call List

> Outputs for Preregistration

> Calling Statistics Report

> Percentage of Patients Pre-Registered Report

> Pre-Registration Source Report

> Print Preregistration Audits

> Supervisor Preregistration Menu

> Add New Appointments to Call List

> Clear the Call List

> Purge Call Log

> Purge Contacted Patients

> Patient Inquiry

> Preregister a Patient

Print Patient Wristband

Pseudo SSN Report (Patient)

Register a Patient

Report - All Address Change with Rx

Report - All Address Changes

Report - All Patients flagged with a Bad Address

Report - Patient Catastrophic Edits

Unsupported CV End Date Report

View Patient Address

View Registration Data

Registration Supplement

## User Manual - RUG-II Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Close a PAI Record

Create a PAI from Past Admission/Transfer

Delete a PAI

Open a Closed or Transmitted PAI

Outputs Menu

> Incomplete PAIs by Location

> PAIs for a Date Range

> Record Status Report

> RUG-II Index

> Single PAI Print

PAI Enter/Edit

RUG-II Grouper

Test Grouper

Transmission via VADATS

## User Manual - Security Officer Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display User Access to Patient Record

Enter/Edit Patient Security Level

Purge Non-sensitive Patients from Security Log

Purge Record of User Access from Security Log

ISO Sensitive Records Report-Export

ISO Sensitive Records Report-Formatted Report

## User Manual - Supervisor ADT Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADT System Definition Menu

> Add/Edit Beds

> Bed Out-of-Service Date Enter/Edit

> Bulletin Selection

> Device Selection

> Edit Bed Control Movement Types

> Edit Ward Out-of-Service Dates

> Embosser Edit Menu

> Edit Data Card File (39.1)

> Edit Embosser Device File (39.3)

> Enter/Edit Transmission Routers File

> G&L Parameter Edit

> Gains and Losses Initialization

> MAS Parameter Entry/Edit

> Means Test Threshold Entry/Edit

> Reasons for Lodging Entry/Edit

> Template Selection

> Treating Specialty Set-up

> Ward Definition Entry/Edit

Check Routine Integrity

Current MAS Release Notes

Inconsistency Supervisor Menu

> Overview

> Determine Inconsistencies to Check/Don't Check

> Purge Inconsistent Data Elements

> Rebuild Inconsistency File

> Update Inconsistency File

Institution File Enter/Edit

Insurance Company Entry/Edit

Military Service Data Inconsistencies Report

Patient Type Update

Purge Scheduled Admissions

Recalculate G&L Cumulative Totals

Reimbursable Insurance Primary EC Report

RUG Semi-Annual Background Job

Sharing Agreement Category Update

Show MAS System Status Screen

Transmit/Generate Release Comments

Unsupported CV End Date Report

View G&L Corrections

WWU Enter/Edit for RUG-II

## User Manual - Veteran Identification Card Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Card Download

Outpatient Card Download

Preadmission Card Download

Single Patient Download Request

DataCard’s HL7 Interface Technical Reference

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIMS User Manual is divided into modules, ADT and Scheduling. The PIMS ADT User Manual provides instructional guidance to a broad range of users within VA medical facilities in daily use of the Admission-Discharge-Transfer (ADT) Module of the PIMS software.

The ADT module of the PIMS package provides a comprehensive range of software dedicated to the support of administrative functions related to patient admission, discharge, transfer, and registration. The functions of this package apply throughout a patient's inpatient and/or outpatient stay, from registration, eligibility determination and Means Testing through discharge with on-line transmission of Patient Treatment File (PTF) data to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). The ADT software also aids in recovery of cost of care by supplying comprehensive PTF/RUG-II and Means Test software.

Several features have been designed to maximize efficiency and maintain control over user access of specified sensitive patient records. The Patient Sensitivity function allows a level of security to be assigned to certain records within your database (i.e., records of employees, government officials, etc.) in order to maintain control over unauthorized user access. The Patient Lookup screens user access of these records. It also provides for efficient and faster retrieval of patient records and identifies potential duplicate patient entries.

The information gathered and maintained by the ADT software is available on-line to a broad range of users within the medical facility to assist in daily operations; providing for greater efficiency, reduction of paperwork, and minimization of error. The ADT software provides for efficient and accurate collection, maintenance, and output of data, thus enhancing your health care facility's ability to provide quality care to its patients.

With V. 2.2 of Order Entry/Results Reporting, OE/RR notifications for ADT may be displayed for admissions, death discharges, deaths, and unscheduled (1010) visits. The notifications (ADMISSION, DECEASED, and UNSCHEDULED (1010) VISIT) will be displayed for patients who are defined as members of a list in the OE/RR LIST file (#100.21). The recipients of the notifications would need to be defined as users in the same OE/RR LIST entry. The notifications will appear as "alerts" when the user is prompted to select an option from a menu. Please refer to the documentation for Order Entry/Results Reporting for more information concerning OE/RR notifications.

Introduction

ADT is fully integrated with the VA FileMan, thus allowing ad hoc reports to be extracted by non-programmer personnel. It is integrated with Version 2.1 of the Fee Basis software allowing Fee personnel to register patients through a select Fee option.

ADT includes the following menus:

- ADT Outputs Menu
- Bed Control Menu
- Contract Nursing Home RUG Menu
- Copay Exemption Test Supervisor Menu
- MAS Code Sheet Manager Menu
- Means Test Supervisor Menu
- PTF Menu
- Registration Menu
- RUG-II Menu
- Security Officer Menu
- Supervisor ADT Menu
- Veteran ID Card (VIC) Menu

The Eligibility Inquiry for Patient Billing option documentation and the Patient Inquiry option documentation can be found in the Registration Menu.

Other related materials are the PIMS Technical Manual, the PIMS Installation Guide, and the PIMS Release Notes. The Technical Manual is provided to assist the site manager in maintenance of the software. The Installation Guide provides assistance in installation of the package and the Release Notes describe any modifications and enhancements to the software that are new to the version.

The ADT module makes use of Current Procedural Terminology (CPT) codes which is an AMA copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the American Medical Association.

Introduction

The Eligibility/ID Maintenance Menu provides the options needed to accommodate VA/DOD sharing agreement requirements with regard to Patient Identification Number. For most medical centers, the PT ID will be the social security number of the patient and the SHORT ID will be the last four digits of the patient's social security number. For those sites with DOD sharing agreements using VA/DOD software developed by the Dallas CIOFO, the PT ID will be determined by the ID number given that patient by the military.

For most sites, each eligibility simply needs to be associated with the VA STANDARD format.

Other than The Primary Eligibility ID Reset (All Patients) option, the remaining six options would only be used by DOD sites using VA/DOD software developed by the Dallas CIOFO. They should not be run without Central Office and/or DOD approval/direction. Please contact your local CIOFO for guidance if you feel your site needs to utilize these options.

Documentation for the options in the Eligibility/ID Maintenance Menu can be found in the PIMS Technical Manual under the Implementation and Maintenance Section.

> **NOTE:** MAS is an acronym for Medical Administration Service. This service, where it still exists, is now generally referred to as Health Administration Service. Several file names, option names, and reports in the PIMS software contain the initials MAS. These will be retained to avoid confusion and ensure continuity.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How To Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT User Manual is provided in Adobe Acrobat PDF (portable document format) files. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the V*IST*A Home Page, “Viewers” Directory.

Once you open the file, you may click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. You may print any or all pages of the file. Click on the “Print” icon and select the desired pages. Then click “OK”.

Each menu file contains a listing of the menu, a brief description of the options contained therein, and the actual option documentation. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

### ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT package provides the ability to search on International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) diagnosis codes and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) procedure codes.

> **NOTE:** Existing ICD-9 functionality has not changed.

#### ICD-10-CM Diagnosis Code Search

The ADT ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and display its description. The ADT user interface prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user.

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes.

ICD-10-CM diagnosis code search highlights include:

- At least two characters must be entered to start a diagnosis code search.
- Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.
- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.
- The user is presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, the user is prompted to refine the search.
- The user can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

#### ICD-10-PCS Procedure Code Search

The ADT ICD-10 procedure code search functionality allows the end user to select a single, valid ICD-10 procedure code and display its description. The procedure code selection is based on the individual characters of ICD-10-PCS codes. The user must enter at least one character of a code. The system displays the possible values for the next digit, so the user can build the procedure code dynamically. The ADT ICD-10 procedure code search utility provides the user interface, which prompts the user for input and invokes the Lexicon utility to get data and then presents that data to the end user for selecting either a single, valid ICD-10 procedure code character or ICD-10 procedure code.

This search method provides a “decision tree” type presentation which makes use of the specific ICD-10-PCS code format and structure, where all codes consist of seven characters, with each position in the code having a specific meaning, as shown in the following table:

| Position | 1       | 2           | 3                   | 4         | 5        | 6      | 7         |
|----------|---------|-------------|---------------------|-----------|----------|--------|-----------|
| Aspect   | Section | Body System | Root Operation/Type | Body Part | Approach | Device | Qualifier |

ICD-10-PCS procedure code search highlights include:

- This is a completely code-based search (i.e., not text-based). The user essentially “builds” the ICD-10 procedure code as they go, character by character.
- The user is presented with the list of possible values, with their descriptions, for each character (position) in the code, as they enter/select a value for each character.
- The list of options presented for each character is based on the values selected for each previous character up to that point. Initially, the user is presented with the list of possible values for character 1 (Section). Then, as the value for each character is entered/selected, the list of possible values for each subsequent character displays.
- Additional information (i.e. Definitions, Explanations, and/or Includes Examples) is provided along with the values and descriptions for each character, if applicable, to assist with the selection of the correct value.
- If part of the full ICD-10-PCS code is known, the user can enter the initial characters and the system displays the list of possible values for the subsequent character. Full code entry is also possible, if the full ICD-10-PCS code is known.
- When values for all seven characters have been entered/selected, the code and full description display for user verification. Short descriptions for the ICD-10-PCS codes display.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements which provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". In some cases, such as at an ICD-10 Diagnosis Code or Procedure Code search prompt, typing “???” provides an additional level of help. The HELP message will appear under the prompt, then the prompt will be repeated. For example, perhaps you see the prompt

> *FACILITY TREATING SPECIALTY:*

and you need assistance answering. You enter ? and the HELP message would appear.

> *Enter the TREATING SPECIALTY assigned to this patient with this movement.*

> *This must be an active treating specialty.*

> *Answer with FACILITY TREATING SPECIALTY NAME*

> *FACILITY TREATING SPECIALTY:*

For some prompts, the system will list the possible answers from which you may choose. Any time choices appear with numbers, the system will usually accept the number or the name.

A HELP message may not be available for every prompt. If you enter a "?", "??" or “???” at a prompt that does not have a HELP message, the system will repeat the prompt.

## Enrollment Query Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the enrollment functionality provided by Patch DG\*5.3\*147, sites are able to query the Health and Eligibility Center (HEC) (formerly known as the IVM Center) for patient eligibility and enrollment information. The queries are generated automatically when you register a patient using the Register a Patient option.

You can also send a query for patient enrollment and eligibility data by using the new Send Query action of the Patient Enrollment option. When using the Patient Enrollment option to query HEC, you can choose whether or not you should be notified via a MailMan message when the reply is received. The status bar will display the status of the last enrollment/eligibility query sent for the specified patient, (whether or not a reply was received), and, if received, whether or not the reply resulted in patient data being uploaded to the local database. Use the Check Query Status action to check the status of an outstanding query.

Patch DG\*5.3\*147 established a new mail group, DGEN ELIGIBILTY ALERT, which is used when uploading eligibility data to notify the site of certain changes. HEC may also use the mail group to communicate with the site regarding patient eligibility. Local users who are responsible for maintaining patient eligibility information should be entered as members of this mail group.

There is no guarantee that you will receive the query reply immediately, but, in most cases, the reply should be received very quickly. You are allowed to proceed with your business without waiting for the reply. Within the Register a Patient option, the software checks every time you navigate between screens. If the reply has been received, and is currently being processed, you will be notified that "Upload of patient enrollment/eligibility data is in progress ..." and you will experience a short pause. The MS 3/9/05 registration software handles the receipt of the query reply similarly.

If HEC has an enrollment record for the patient being enrolled, the reply will contain that patient's enrollment record. If HEC has eligibility data on file, that data will also be included in the query reply. The data will be automatically uploaded to the PATIENT file (#2) and the PATIENT ENROLLMENT file (#27.11), unless a problem is detected. All the fields in the PATIENT ENROLLMENT file (#27.11) will be uploaded as a result of the query reply.

## Enrollment Query Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields in the PATIENT file (#2) will be uploaded as a result of the query reply.

- ELIGIBILITY STATUS DATE
- ELIGIBILITY STATUS
- ELIGIBILITY VERIF. METHOD
- CLAIM NUMBER
- \*CLAIM FOLDER LOCATION
- POW STATUS INDICATED?
- POW FROM DATE
- POW TO DATE
- POW LOCATION
- SC AWARD DATE
- TOTAL ANNUAL VA CHECK AMOUNT
- VETERAN Y/N?
- SERVICE CONNECTED?
- SERVICE CONNECTED PERCENTAGE
- COMBINED SC PERCENT EFFECTIVE DATE
- RECEIVING A VA PENSION?
- RECEIVING A&A BENEFITS?
- RECEIVING HOUSEBOUND BENEFITS?
- RECEIVING VA DISABILITY?
- DISCHARGE DUE TO DISABILITY
- MILITARY DISABILITY RETIREMENT
- AGENT ORANGE EXPOS. INDICATED?
- RADIATION EXPOSURE INDICATED?
- RADIATION EXPOSURE METHOD
- SW ASIA CONDITIONS?
- CAMP LEJEUNE
- CAMP LEJEUNE CHANGE SITE
- CAMP LEJEUNE DATE
- CAMP LEJEUNE SOURCE
- PRIMARY ELIGIBILITY CODE
- PATIENT ELIGIBILITIES ç *Uploaded data will replace the data currently in the file.*
- P&T
- UNEMPLOYABLE
- INELIGIBLE DATE
- INELIGIBLE REASON
- INELIGIBLE VARO DECISION
- ELIGIBLE FOR MEDICAID?
- DATE MEDICAID LAST ASKED
- PREFERRED FACILITY
- RATED DISABILITIES (VA) MULTIPLE, FIELD .3721, MULTIPLE 2.04
- RATED DISABILITIES (VA) ç *Uploaded data will replace the data currently in the file.*
- DISABILITY %
- SERVICE CONNECTED
- EXTREMITY AFFECTED
- ORIGINAL EFFECTIVE DATE
- CURRENT EFFECTIVE DATE
- CATASTROPHIC DISABILITY:
- REVIEW DATE
- DECIDED BY
- FACILITY MAKING DETERMINATION
- DATE OF DECISION
- PROJECT 112/SHAD INDICATOR
- AGENT ORANGE EXPOSURE LOCATION
- SPINAL CORD INJURY
- CURRENT MOH INDICATOR
- MOH AWARD DATE
- MOH STATUS DATE
- MOH COPAYMENT EXEMPTION DATE

## Enrollment Query Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEC also has the capability of sending unsolicited updates of enrollment and eligibility data to local sites. An example of when HEC will use this capability is as follows: a veteran visits multiple facilities and reports a change to one of them. The other facilities will be automatically updated via an unsolicited update from HEC, which will contain the same data as the enrollment/eligibility query response.

## Enrollment Priority Algorithm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the algorithm used to derive a patient’s enrollment priority. The following is the General Counsel’s interpretation of the law and the data elements associated with deriving each Enrollment Priority Group in V*IST*A. The priority algorithm uses the value of the data elements at the time the priority is derived. The value of the data elements used is then stored with the enrollment record. All groupings apply to patients who are veterans that are eligible for care.

Note that if the Means Test Status for a veteran is Required or a Means Test does not exist for a non-service-connected veteran or for a veteran who is 0% SC and is required to have a Means Test, Enrollment Priority Groups 5, 7 and 8 will not be determined until the Means Test is completed.

#### Unemployable SC Enrollment Priority Group Change:

Veterans who are unemployable and whose Service Connection is greater than 0%, and whose total check amount is greater than \$0, and who are not receiving VA Pension, A&A or HB will be enrolled in Priority Group 1 and be exempt of Pharmacy Copayments.

#### Relaxation of Priority Group 8 Enrollment Restrictions Change:

The 2009 Appropriations Act directed the Department of Veterans Affairs to support increased enrollment for veterans in Priority Group (PG) 8 with income exceeding the applicable Means Test (MT) or Geographic Means Test (GMT) threshold by 10% or less. In support of these enrollment rule changes, additional PG8 sub-categories ‘b’ and ‘d’ and continuous enrollment rules have been added for implementing changes in Enrollment to allow veterans with income equal to or less than 10% above the applicable Department of Veterans Affairs (VA) MT threshold or GMT threshold to be enrolled in the VA healthcare system.

*Public Law 111-163 Change:*

On May 5, 2010, the President signed into law, Public Law (PL) 111-163, the Caregivers and Veterans Omnibus Health Services Act of 2010. This law provides assistance to caregivers of Veterans and improves the provisions of healthcare services to Veterans. Section 511 prohibits collections of copayments from Veterans who are Catastrophically Disabled. This includes pharmacy copayments.

*Public Law 112-154 Change:*

Public Law 112-154, requires Veterans Affairs (VA) to provide hospital care and medical services to Veterans who served on active duty at Camp Lejeune (North Carolina) for one or more of 15 specified illnesses or conditions (Esophageal cancer; Lung cancer; Breast cancer; Bladder cancer; Kidney cancer; Leukemia; Multiple myeloma; Myelodysplastic syndromes; Renal toxicity; Hepatic steatosis; Female infertility; Miscarriage; Scleroderma; Neurobehavioral effects; or Non-Hodgkin's lymphoma). To be eligible for care under the provisions of this bill, the Veteran must have served on active duty at Camp Lejeune for not fewer than thirty (30) consecutive or nonconsecutive days between August 1, 1953 and December 31, 1987. The Camp Lejeune – Veterans (CL-V) Project provides software enhancements to the Enrollment System (ES) and VistA. Host file DG_5_3_P909.KID (patches DG\*5.3\*909 and IVM\*2\*161) adds the ability to enter Camp Lejeune information in VistA and share CL-V data between ES and VistA. The initial enrollment determination algorithm was modified to place CL-V eligible Veterans in priority group 6 unless a higher priority is determined based on other eligibility factors. No changes were made to continuous enrollment rules within VistA.

*Public Law 114-315 Change:*

Public Law 114-315, signed into law on December 16, 2016, amends United States Code Title 38 Section 1705 to place Veterans awarded the Medal of Honor (MOH) into the highest Department of Veterans Affairs (VA) Enrollment Priority group - Enrollment Priority Group 1. Veterans awarded Medal of Honor are currently assigned to Enrollment Priority Group 3.

PL 114-315 amends United States Code Title 38 Section 1710(a), 1710B, and 1722A and exempts Veterans awarded Medal of Honor from copayments for healthcare, medications, and extended care services.

Additionally, PL 114-315 provides that all Veterans awarded the Medal of Honor currently enrolled for VA hospital care and medical services, and whose Veterans Health Administration (VHA) enrollment records are not currently assigned to Priority Group 1, will have their enrollment record updated to reflect enrollment in Priority Group 1 and exemption from copayments for health care, medications, and extended care services.

VA OIG Audit (16-00355-296) \#4 *Separate Registration from Enrollment*

Veterans who register but do not wish to apply for enrollment for VHA healthcare services are not assigned a Priority Group. The Enrollment Status of REGISTRATION ONLY is assigned to these Veterans, as well as to all Non-Veterans registered at a VistA site.

Public Law No: 116-214 (12/05/2020) Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020 or the Veterans COMPACT Act of 2020

- Any one of the following  can go to a VA or non-VA emergency room for emergent suicidal care, a:
  - Veteran – whether enrolled in VA or not who meets the minimum duty requirements according to 38 USC 5303A
  - Former Service Member who meets the requirements according to 38 USC 1720i while awaiting adjudication
- VA will provide the treatment or cover the costs for treatment including transportation, inpatient or crisis residential care for up to 30 days, and outpatient care for up to 90 days

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Null</td>
<td><ul>
<li><p>Veterans who do not wish to enroll in VHA Healthcare and all nonveterans</p></li>
</ul></td>
<td>If patient has an enrollment status of REGISTRATION ONLY, a priority group of null (“”) will be returned.</td>
</tr>
<tr class="even">
<td>1</td>
<td><ul>
<li><p>Veterans with service-connected disabilities rated greater than 0%</p></li>
<li><p>Veterans awarded Medal of Honor</p></li>
</ul></td>
<td><p>[Unemployable is Yes</p>
<p>AND</p>
<p>SC &gt;0%</p>
<p>AND</p>
<p>Total Check Amount &gt;$0</p>
<p>AND</p>
<p>Receiving a VA Pension is No</p>
<p>AND</p>
<p>Eligibility Code of AID &amp; ATTENDANCE is No</p>
<p>AND</p>
<p>Eligibility Code of HOUSEBOUND is No]</p>
<p>OR</p>
<p>[Service-Connected is Yes</p>
<p>AND</p>
<p>Service-Connected Percentage between 50 and 100%]</p>
<p>OR</p>
<p>[Eligibility Code of SERVICE CONNECTED 50% TO 100%]</p>
<p>OR</p>
<p>[MOH is Yes]</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Veterans with service-connected disabilities rated 30% or 49%</td>
<td><p>[Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage between 30 and 49%</p>
<p>AND</p>
<p>Eligibility Code of SC LESS THAN 50%]</p></td>
</tr>
<tr class="even">
<td>3</td>
<td><ul>
<li><p>Former prisoners of war</p></li>
<li><p>Veterans who are awarded the Purple Heart</p></li>
<li><p>Veterans with service-connected disabilities rated 10% or 20%</p></li>
<li><p>Veterans discharged or released from active military service for a compensable disability that was incurred or aggravated in the line of duty</p></li>
<li><p>Veterans who are in receipt of Section 1151 benefits</p></li>
</ul></td>
<td><p>[POW Status Indicated is Yes]</p>
<p>OR</p>
<p>[Eligibility Code of POW]</p>
<p>OR</p>
<p>[PH Indicated is YES]</p>
<p>OR</p>
<p>[Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage between 10 and 29%</p>
<p>AND</p>
<p>Eligibility Code of SC LESS THAN 50%]</p>
<p>OR</p>
<p>[Disability Ret. From Military is 2 for Yes, Receiving Military Retirement in Lieu of VA Compensation]</p>
<p>OR</p>
<p>[Discharge Due to Disability is YES]</p>
<p>OR</p>
<p>[Military Disability Retirement is YES]</p></td>
</tr>
</tbody>
</table>

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4</td>
<td><ul>
<li><p>Veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason being permanently housebound</p></li>
<li><p>Other veterans who are catastrophically disabled</p></li>
</ul></td>
<td><p>[Receiving A&amp;A Benefits is Yes]</p>
<p>OR</p>
<p>[Eligibility Code of AID &amp; ATTENDANCE]</p>
<p>OR</p>
<p>[Receiving Housebound Benefits is Yes]</p>
<p>OR</p>
<p>[Eligibility Code of HOUSEBOUND]</p>
<p>OR</p>
<p>[Catastrophically Disabled is Yes]</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Veterans who have annual income and net worth below the Means Test threshold</td>
<td><p>[Means Test Copay Exempt]</p>
<p>OR</p>
<p>[Eligible for Medicaid is Yes]</p>
<p>OR</p>
<p>[Receiving a VA Pension is Yes]</p>
<p>OR</p>
<p>[Eligibility Code of NSC, VA PENSION]</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>All other eligible veterans who are not required to pay a copayment for their care</td>
<td><p>[Eligibility Code of WORLD WAR I]</p>
<p>OR</p>
<p>[Eligibility Code of WORLD WAR II]</p>
<p>OR</p>
<p>[Eligibility Code of MEXICAN BORDER WAR]</p>
<p>OR</p>
<p>*[Agent Orange Expos. Indicated is Yes]</p>
<p>AND</p>
<p>[Agent Orange Expos. Loc. is Vietnam or Blue Water Navy]</p>
<p>OR</p>
<p>[Radiation Exposure Indicated is Yes</p>
<p>AND</p>
<p>Radiation Exposure Method is 2, 3, or 4]</p>
<p>OR</p>
<p>*[SW Asia Conditions is Yes]</p>
<p><span id="TERA_indicator" class="anchor"></span>OR</p>
<p>[TOXIC EXPOSURE RISK ACTIVITY (TERA) is YES]</p>
<p>OR</p>
<p>[Total Annual VA Check Amount is greater than 0]</p>
<p>OR</p>
<p>[Combat Veteran Eligible is Yes]</p>
<p>OR</p>
<p>[SHAD Exposure is Yes</p>
<p>AND</p>
<p>SHAD Exposure is the sole reason for enrollment]</p>
<p>OR</p>
<p>Camp Lejeune is Yes</p></td>
</tr>
<tr class="even">
<td>7</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[GMT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication]</p>
<p><strong><u>Note</u></strong>: All Priority Group 7 veterans will be prioritized</p>
<p>into a sub-category (a, c, e, or g)</p>
<p>based on qualifications as noted.</p></td>
</tr>
</tbody>
</table>

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>7a</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[GMT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage is 0</p>
<p>AND</p>
<p>Total VA Check Amount is 0 or null</p>
<p>AND</p>
<p>Eligibility Code of SC LESS THAN 50%</p>
<p>AND</p>
<p>Enrolled on a date specified in the Federal Register and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="even">
<td>7c</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[GMT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is No</p>
<p>AND</p>
<p>Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="odd">
<td>7e</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[GMT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage is 0</p>
<p>AND</p>
<p>Total VA Check Amount is 0 or null</p>
<p>AND</p>
<p>NOT Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
</tbody>
</table>

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>7g</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[GMT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is No</p>
<p>AND</p>
<p>NOT Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication]</p>
<p><strong><u>Note</u></strong>: All Priority Group 8 veterans will be prioritized</p>
<p>into a sub-category (a, b, c, d, e, or g)</p>
<p>based on qualifications as noted.</p></td>
</tr>
<tr class="odd">
<td>8a</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage is 0</p>
<p>AND</p>
<p>Total VA Check Amount is 0 or null</p>
<p>AND</p>
<p>Eligibility Code of SC LESS THAN 50%</p>
<p>AND</p>
<p>Enrolled on a date specified in the Federal Register and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
</tbody>
</table>

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8b</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold) plus 10%</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Initial enrollment date is on or after 1/1/2009</p>
<p>AND</p>
<p>Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage is 0</p>
<p>AND</p>
<p>Total VA Check Amount is 0 or null</p>
<p>AND</p>
<p>Not Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="even">
<td>8c</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is No</p>
<p>AND</p>
<p>Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="odd">
<td>8d</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold) plus 10%</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Initial enrollment date is on or after 1/1/2009</p>
<p>AND</p>
<p>Service Connected is No</p>
<p>AND</p>
<p>Not Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
</tbody>
</table>

Enrollment Priority Algorithm

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enrollment Priority</p>
<p>Group</p></th>
<th>Veterans Included</th>
<th>How They Qualify</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8e</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is Yes</p>
<p>AND</p>
<p>Service Connected Percentage is 0</p>
<p>AND</p>
<p>Total VA Check Amount is 0 or null</p>
<p>AND</p>
<p>Not Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
<tr class="even">
<td>8g</td>
<td>Veterans who agree to pay specified copayments with income and/or net worth above the VA Means Test threshold and the HUD geographic index (a.k.a. GMT Threshold)</td>
<td><p>[MT Copay Required]</p>
<p>OR</p>
<p>[Means Test is Pending Adjudication</p>
<p>AND</p>
<p>Service Connected is No</p>
<p>AND</p>
<p>Not Enrolled on a date specified in the Federal Register</p>
<p>and enrolled continuously thereafter (Refer to the continuous enrollment rules following this table).</p>
<p>AND</p>
<p>EGT is Type 4, Enrollment Decision]</p></td>
</tr>
</tbody>
</table>

\* Agent Orange and SW Asia Conditions will include new Special Treatment Authority Expiration date fields that will be added to the MAS PARAMETERS file (#43). The initial value of these fields will be null or empty. A subsequent patch will be released to populate the date fields once the expiration of the Special Treatment Authority is scheduled to expire. The assigning of newly enrolled veterans to Priority Group 6 determination rules whose AO Indicator is "Y" and Location is *Vietnam* or *Blue Water Navy* and/or their SWAC exposure indicator is "Y" applies only if the Enrollment Date is before the Special Treatment Authority Date, or if the Special Treatment Authority Date is null.

\*\*The following criteria must be met before a Veteran is eligible for Camp Lejeune benefits:

1\. Person is a Veteran AND

2\. Person has one or more Military Service Episode(s) (MSE) that include no less than 30 days of service between August 1, 1953 and December 31, 1987 (inclusive) AND

3\. All of the identified MSE(s) used for the 30-day service duration have a character of discharge other than:

• Dishonorable

• Other Than Honorable

• Undesirable

• Bad Conduct

• Dishonorable-VA

Enrollment Priority Algorithm

#### Continuous Enrollment Rules

To determine a veteran’s current enrollment record for the purpose of continuous enrollment, ignore any records with an enrollment status in the following list and look to the most recent record that is not in one of these statuses:

- Pending Means Test Required
- Pending Purple Heart Unconfirmed
- Pending Eligibility Status Unverified
- Pending Other
- Pending No Eligibility Code
- Deceased
- Not Eligible; Ineligible Date
- Not Eligible; Refused to Pay Copay

Once the current enrollment record has been determined, the following rules will be executed in this order:

1.  If the beneficiary’s initial enrollment date occurred on or after 1/1/2009

> AND

> the most current financial assessment identifies income above the VA MT or GMT threshold (whichever is higher) by 10% or less

> AND

> the beneficiary is currently non-compensable 0% service-connected

> THEN

> the system shall continuously enroll and set the enrollment priority/sub-priority to 8b.

> If the beneficiary’s initial enrollment placed the veteran in an 8e

> AND

> is a 0% non-compensable service-connected veteran who submits a 2008 Income Year Means test or later

> AND

> the system calculates the income (income minus medical and educational expenses) to be under the VA MT threshold and Income plus assets are greater than or equal to \$80K

> THEN

> the system shall continuously enroll and set the enrollment priority/sub-priority to 8b.

Enrollment Priority Algorithm

2.  If the beneficiary’s initial enrollment date occurred on or after 1/1/2009

> AND

> the most current financial assessment identifies income above the VA MT or GMT threshold (whichever is higher) by 10% or less

> AND

> the beneficiary is currently non-service-connected

> THEN

> the system shall continuously enroll and set the enrollment priority/sub-priority to 8d.

> If the beneficiary’s initial enrollment placed the veteran in an 8g

> AND

> is a non-service-connected veteran who submits a 2008 Income Year Means test or later

> AND

> the system calculates the income (income minus medical and educational expenses) to be under the VA MT threshold with Income plus assets greater than or equal to \$80K

> THEN

> the system shall continuously enroll and set the enrollment priority/sub-priority to 8d.

3.  If the enrollment record is in a REJECTED enrollment status due to a manual override \[at the HEC\] (i.e., Enrollment Status Override =YES), it will remain in a REJECTED status unless the veteran is assigned to an enrollment priority group that is being accepted for enrollment

> OR

> until a new EGT is set that could qualify the veteran for enrollment

> OR

> the record in a REJECTED enrollment status is manually overridden \[at the HEC\] to ENROLLED.

4.  If the enrollment record is in a REJECTED enrollment status, it will stay REJECTED as long as the veteran stays in an enrollment priority group that is not being accepted for new enrollment.

  
Enrollment Priority Algorithm

5.  If the enrollment record is in a VERIFIED enrollment status due to a manual override \[at the HEC\] (i.e., Enrollment Status Override =YES), the veteran will remain ENROLLED until a new EGT is set that could disqualify the veteran from enrollment

> OR

> the record in an ENROLLED category is manually overridden \[at the HEC\] to a REJECTED enrollment status.

6.  If the enrollment record is in a CANCEL/DECLINED enrollment status on or after the EGT Effective Date, it will be treated the same as a record in a REJECTED enrollment status. The veteran will not be continuously enrolled as long as s/he stays in an enrollment priority group that is not being accepted for new enrollments.
7.  If the current enrollment record does not meet any of the conditions in Rules 1-6 above, the veteran’s enrollment records will be evaluated from most current to earliest, with the following rules applied in this order:
- If the earliest Effective Date of Change is prior to the EGT Effective Date, the veteran will be continuously enrolled.
- If there is any Enrollment Application Date prior to the EGT Effective Date, the veteran will be continuously enrolled.
8.  If the veteran has ever had a verified enrollment record with an eligibility in the following list, s/he will be continuously enrolled:
- SC 10% or greater

> AND

> SC% is changed to SC 0% non-compensable (total check amount \$0 or null)

- Aid & Attendance = YES

> AND

> A&A is now not YES

- Housebound = YES

> AND

> Housebound is now not YES

Enrollment Priority Algorithm

- VA Pension = YES

> AND

> VA Pension is now not YES

- AO indicator = YES

> AND

> Location = DMZ was entered prior to Enrollment System Redesign V. 3.0 (ESR) implementation.

- AO indicator = YES

> AND

> AO Location is Vietnam OR Blue Water Navy

> AND

> AO Special Treatment Expiration Date is not null

> AND

> Enrollment Date is prior to the AO Special Treatment Authority

> Expiration Date

- The CV End Date expires on or after the Enrollment Application Date (or, in the absence of an Application Date, the earliest Effective Date of Change)

> AND

> the CV End Date has not been removed.

- The veteran is enrolled due to a Means Test that qualifies for enrollment

> AND

> a subsequent income year Means Test was added or edited that would place the veteran in a priority group that is not being enrolled

> UNLESS

> the Means Test on the first verified enrollment record is edited to a Means Test Status that places the record in a priority group not being enrolled and veteran has no subsequent record that would qualify for enrollment

> OR

> the Means Test on the first verified enrollment record is converted by IVM to a Means Test Status that places the record in a priority group not being enrolled and veteran has no subsequent record that would qualify for enrollment.

Enrollment Priority Algorithm

9.  If the enrollment record history does not support any of Rules 1-8 above

> AND

> the base priority is numerically greater than the EGT threshold

> THEN

> the decision is to REJECT enrollment.

10. If the veteran’s SHAD Exposure indicator is changed to NO or deleted (by the HEC only)

> THEN

> the veteran may be placed in a REJECTED status

> AND

> the veteran will not be continuously enrolled if his/her sole reason for enrollment was SHAD exposure.

## Military Sexual Trauma stand-alone Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Military Sexual Trauma (MST) software provides the following stand-alone menu that can be added to the user’s secondary menu.

MST Status Add/Edit

MST Outputs

> Print Statistical Report \*\*No longer in Service\*\*

> MST Summary Report \*\*No longer in Service\*\*

> Detailed Demographic Report \*\*No longer in Service\*\*

> MST History Report by Patient \*\*No longer in Service\*\*

\*\*\*With the advent of the Suicide High Risk Patient Enhancement patch implementation DG\*5.3\*977, the MST options noted above were disabled. Instead of processing the end user request to run the option, an on-screen message will be displayed to the user and they will be left at the Select Military Sexual Trauma Menu Option \> prompt.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;CPM&gt; Select Military Sexual Trauma Menu &lt;SHRPECC&gt; Option: MST Outputs</p>
<p>   STAT   Print Statistical Report</p>
<p>             &gt; Out of order:  MST reports are available at vssc.med.va.gov</p>
<p>  </p>
<p>SUM    MST Summary Report</p>
<p>             &gt; Out of order:  MST reports are available at vssc.med.va.gov</p>
<p>   DET    Detailed Demographic Report</p>
<p>             &gt; Out of order:  MST reports are available at vssc.med.va.gov</p>
<p>   HIS    MST History Report by Patient</p>
<p>             &gt; Out of order:  MST reports are available at vssc.med.va.gov</p>
<p>&lt;CPM&gt; Select Military Sexual Trauma Menu &lt;SHRPECC&gt; Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Military Sexual Trauma stand-alone Menu

### MST Status Add/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*With the advent of the Suicide High Risk Patient Enhancement patch implementation DG\*5.3\*977, if the end user selects the ‘MST Status Add/Edit’ option, the VistA system will now display the following to the end user; “Out of order: Add/edit MST status only in MST Clinical Reminder.”

This option is used to enter, edit, delete, and display new MST status codes for patients through a series of List Manager Screens. The EL Edit Entry and DL Delete Status Entry actions will only be allowed for entries that you make in the current session. You cannot modify entries made in previous sessions.

When you exit the option, HL7 messages are triggered to send the updated MST status, date MST status changed, and site determining MST status information to the Health Eligibility Center (HEC).

Military Sexual Trauma stand-alone MenuMST Status Add/Edit

\*\*\*With the advent of the Suicide High Risk Patient Enhancement patch implementation DG\*5.3\*977, if the end user selects the ‘MST Status Add/Edit’ option, the VistA system will now display the following to the end user; “Out of order: Add/edit MST status only in MST Clinical Reminder.”

Screen Actions

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Synonym</th>
<th>Action Name</th>
<th>Description</th>
</tr>
<tr class="odd">
<th>EP</th>
<th>Enter by Patient</th>
<th><p>Displays the following information for each patient for whom entries were made during the current session.</p>
<ul>
<li><p>Last four numbers of patient's SSN</p></li>
<li><p>Name of patient</p></li>
<li><p>MST status</p></li>
<li><p>Name of the provider who determined the MST status</p></li>
<li><p>Date of last status change</p></li>
</ul>
<p>Prompts the user to enter the following information for each patient.</p>
<ul>
<li><p>Patient's name</p></li>
<li><p>New/changed MST status</p></li>
<li><p>Date of new/changed status</p></li>
<li><p>Provider determining new/changed status</p></li>
</ul></th>
</tr>
<tr class="header">
<th>ES</th>
<th>Enter by Status</th>
<th><p>Displays the following information for each patient for whom entries were made during the current session.</p>
<ul>
<li><p>Last four numbers of patient's SSN</p></li>
<li><p>Name of patient</p></li>
<li><p>MST status</p></li>
<li><p>Name of the provider who determined the MST status</p></li>
<li><p>Date of last status change</p></li>
</ul>
<p>Prompts the user to enter the following information for each patient.</p>
<ul>
<li><p>New/changed MST status</p></li>
<li><p>Patient's name</p></li>
<li><p>Date of new/changed status</p></li>
<li><p>Provider determining new MST status/status change</p></li>
</ul></th>
</tr>
<tr class="odd">
<th>EX</th>
<th>Expand Patient</th>
<th><p>Displays the following information on the MST Status History Screen for the selected patient.</p>
<ul>
<li><p>Status Date - date and time of the last status update</p></li>
<li><p>MST Status - single alpha character representing the MST status code entered for the selected patient</p></li>
<li><p>Site - primary station number of the site determining MST status</p></li>
<li><p>Provider who determined the MST status for the selected patient</p></li>
<li><p>User who entered the MST status for the selected patient</p></li>
</ul></th>
</tr>
<tr class="header">
<th>EL</th>
<th>Edit Entry</th>
<th>Edit status entries made in the current session only</th>
</tr>
<tr class="odd">
<th>DL</th>
<th>Delete Status Entry</th>
<th>Delete status entries made in the current session only</th>
</tr>
<tr class="header">
<th>DP</th>
<th>Display Patient</th>
<th>Displays the MST Status History Screen for the selected patient and provides the same information as the EX action</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

  
Military Sexual Trauma stand-alone Menu

### MST Outputs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*With the advent of the Suicide High Risk Patient Enhancement patch implementation DG\*5.3\*977, if the end user selects any of the MST Outputs;

> Print Statistical Report \*\*No longer in Service\*\*

> MST Summary Report \*\*No longer in Service\*\*

> Detailed Demographic Report \*\*No longer in Service\*\*

> MST History Report by Patient \*\*No longer in Service\*\*

The following message will be displayed:

“\*\*\> Out of order: MST reports are available at vssc.med.va.gov”

#### Print Statistical Report \*\*No longer in Service\*\*

This option is used to print the MST Statistical Report. The report displays the number of new cases identified for MST and provides the following statistics for a user-specified date range.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Outpatient</th>
<th>Inpatient</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Number of outpatient encounters related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of outpatient encounters not related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of unique outpatients treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Average number of encounters related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Average number of encounters not related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of male/female outpatient encounters by ICD code</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Number of inpatient episodes related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of inpatient episodes not related to MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of unique inpatients treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Average number of inpatient episodes treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Average number of inpatient episodes not treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Total length of stay of inpatients treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Average length of stay of inpatients treated for MST</p>
</blockquote></li>
<li><blockquote>
<p>Number of male/female inpatient encounters by ICD code</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

  
Military Sexual Trauma stand-alone Menu*MST Outputs*MST Summary Report \*\*No longer in Service\*\*

This option is used to print the MST Summary Report. The report provides total overall patient count, total counts by patient gender, and the percentage of all patients for the following MST statuses within a user-specified date range.

| Synonym | Status Name                   | Description                                                          |
|---------|-------------------------------|----------------------------------------------------------------------|
| Y (YES) | Screened, Reports MST         | Indicates that the patient has been screened and reports MST         |
| N (NO)  | Screened, Does Not Report MST | Indicates that the patient has been screened and does not report MST |
| D       | Screened, Declines to Answer  | Indicates that the patient has been screened and declines to answer  |
| U       | Unknown, Not Screened         | Indicates that the patient has not been screened                     |

Military Sexual Trauma stand-alone Menu*MST Outputs*Detailed Demographic Report \*\*No longer in Service\*\*

This option is used to print the MST Detailed Demographic Report. The report provides the following demographic data for user-specified MST status codes within a user-specified date range.

- SSN
- Name, address, and phone number
- Gender
- Eligibility Code
- Period of Service
- Service Indicator

The software prompts for the following sort criteria.

- MST status code - allows selection of multiple status codes
- Gender
- Period of Service - sorts the report by patient name or by period of service (and within period of service, by patient name)

  
Military Sexual Trauma stand-alone Menu*MST Outputs*MST History Report by Patient \*\*No longer in Service\*\*

This option is used to print the MST History Report. The report provides the following information from the MST HISTORY File (#29.11) for user-specified patient(s).

- Patient's name and SSN
- Status date(s) - date of the original status entry and date(s) of any status change(s)
- MST status code
- Site - primary station number of the site determining MST status
- Provider name
- Name of the person who entered the MST status

## Home Telehealth stand-alone Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Telehealth software provides the following stand-alone menu that can be added to the user’s secondary menu.

Home Telehealth Menu

The following submenu options were created under the Home Telehealth Menu.

> Patient Sign-Up/Activation

> Patient Inactivation

> Patient Summary Report

> Transmission Report

Home Telehealth Menu

### Patient Sign-Up/Inactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Sign Up /Activation is the continuation of a process that is started by a Care Coordinator. Care Coordinators are licensed health care professionals who help veteran patients self-manage their condition.

The Care Coordinator creates a consult using VistA’s Computerized Patient Records System (CPRS). After the consult is completed, an authorized Care Coordinator can sign-up/activate a patient needing Home Telehealth services through this option.

When adding a Home Telehealth patient, the user is required to enter information in the following fields: patient, vendor, consult number, and care coordinator. Upon completion of these required fields, the user is asked if they want to “send sign-up/activation”. If YES, the patient information is sent to the Home Telehealth vendor server system via the Austin Interface Engine.

If the patient has already been signed-up with a vendor, that information will be displayed, and the user is asked if they want to continue the sign-up/activation.

Home Telehealth Menu

### Patient Inactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to inactivate a Home Telehealth patient.

The selected patient’s active Home Telehealth record is displayed. The user then enters the inactivation date and time.

Home Telehealth Menu

### Patient Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to generate a report displaying a summary of all patients that have been signed up for Home Telehealth care for a specified date range. The user may sort the report by patient or transmission date.

Information provided for each patient on the report includes patient name, status (active/inactive), date of last change, and Home Telehealth vendor. Total numbers for active patients, inactive patients, and patient records are provided.

Home Telehealth Menu

### Transmission Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides the Care Coordinator with detailed information pertaining to the transmission of the HL7 A04 (register) sign-up/activation message and the HL7 A03 (discharge) inactivation message. A HL7 A04 (register) message is transmitted through the Patient Signup/Activation option while a HL7 A03 (discharge) message is transmitted through the Patient Inactivation option.

The user must select a date range, message status, and one/many/all care coordinators. The report contains the following data.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Column Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient</td>
<td>Name of the Home Telehealth patient</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Last 4 digits of the Home Telehealth patient’s Social Security Number</td>
</tr>
<tr class="odd">
<td>HT Vendor</td>
<td>This is the name of the Home Telehealth vendor with which this patient is signed up.</td>
</tr>
<tr class="even">
<td>Care Coordinator</td>
<td>Name of the Care Coordinator that has signed up the Home Telehealth patient.</td>
</tr>
<tr class="odd">
<td>Consult #</td>
<td>Internal entry number of the consultation.</td>
</tr>
<tr class="even">
<td>Event/Trans Date</td>
<td>Date and time the event (patient VistA Interface Engine) was transmitted to the Home Telehealth vendor server.</td>
</tr>
<tr class="odd">
<td>Message ID</td>
<td>Message control ID of the transmission of Home Telehealth patient sign-up/activation to the Home Telehealth vendor server.</td>
</tr>
<tr class="even">
<td>ACK Date/Time</td>
<td>Acknowledgement date and time of when the Home Telehealth vendor server received the transmission.</td>
</tr>
<tr class="odd">
<td>Status</td>
<td><p>Acknowledgement of the transmission has one of the following statuses:</p>
<ul>
<li><p>Accepted</p></li>
<li><p>Rejected</p></li>
<li><p>Unknown</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Message Type</td>
<td><p>This is the type of message transmitted for the Home Telehealth patient:</p>
<ul>
<li><p>Activation -This is a ‘A04’ (register) HL7 type message</p></li>
<li><p>Inactivation. This is an ‘A03’ (discharge) HL7 type message</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Reject Message</td>
<td>If there is an error in the processing of the transmission message, this field contains the 3-50 characters of the error message.</td>
</tr>
<tr class="even">
<td>Retransmitted</td>
<td>Indicates the number of retransmissions. This number is used by a site configurable parameter to identify the number of retransmits that are allowed before a bulletin is sent to a mail group.</td>
</tr>
</tbody>
</table>

Glossary

ADC Average Daily Census

ALOS Average Length of Stay

AMIS Automated Management Information System

attending Supervising physician who is responsible for the care of the patient.

physician Non-affiliated hospitals may choose not to use this field.

breakeven A day on which the actual cost of care equals the estimated

day allocation.

catastrophically CD is a permanent, severely disabling injury, disorder, or disease

disabled (CD) that compromises the individual's ability to carry out the activities of daily living to such a degree that s/he requires personal or mechanical assistance to leave home or bed, or requires constant supervision to avoid physical harm to her/himself or others.

CDR Cost Distribution Report

collateral A visit by a non-veteran patient whose appointment is related to or

visit associated with a service-connected patient's treatment.

Consistency Provides a method of assuring the accuracy of data contained in a

checker patient file.

Copay Test A financial report used to determine if a patient may be exempted

from pharmacy copayments.

DRG Diagnostic Related Group

DXLS Diagnosis responsible for the major portion of a patient's stay.

G&L Gains and Losses

HINQ Hospital Inquiry

Means Test A financial report used to determine if a patient may be required to

make Copayments for care.

MOH Medal of Honor

Glossary

PAI Patient Assessment Instrument

PAF Patient Assessment File

primary The health care provider with primary responsibility for the direct

physician care of the patient. This may be the resident or intern in a

teaching facility or the staff physician in a non-affiliated hospital.

PTF Patient Treatment File

routing slip When printed for a specified date, it shows the current appointment

time, clinic, location and stop code. It also shows future appointments.

RUG Resource Utilization Group

security code A code assigned to each user identifying them specifically to the

system and allowing them access to the functions/options assigned

to them.

security key Used in conjunction with locked options or functions. Only holders

which perform a sensitive task.

Special An ongoing survey of care given to patients alleging Agent Orange

Survey or ionizing radiation exposure. Each visit by such a patient must

receive special survey dispositioning which records whether

treatment provided was related to that exposure. This data is used

for congressional reporting purposes.

stop code A three-digit number corresponding to an additional stop/service a

patient received in conjunction with a clinic visit. Stop code entries

are used so that medical facilities may receive credit for the

services rendered during a patient visit.

third party Billings where a party other than the patient is billed.

billings

trim point The expected Length of Stay range based on the LOS distribution

for each DRG category.

VADATS Veterans Administration Data Transmission System

WWU Weighted Work Unit

Military Time Conversion Table

STANDARD MILITARY

12:00 MIDNIGHT 2400 HOURS

11:00 PM 2300 HOURS

10:00 PM 2200 HOURS

09:00 PM 2100 HOURS

08:00 PM 2000 HOURS

07:00 PM 1900 HOURS

06:00 PM 1800 HOURS

05:00 PM 1700 HOURS

04:00 PM 1600 HOURS

03:00 PM 1500 HOURS

02:00 PM 1400 HOURS

01:00 PM 1300 HOURS

12:00 NOON 1200 HOURS

11:00 AM 1100 HOURS

10:00 AM 1000 HOURS

09:00 AM 0900 HOURS

08:00 AM 0800 HOURS

07:00 AM 0700 HOURS

06:00 AM 0600 HOURS

05:00 AM 0500 HOURS

04:00 AM 0400 HOURS

03:00 AM 0300 HOURS

02:00 AM 0200 HOURS

01:00 AM 0100 HOURS

Option Index

*Does not include stand-alone options*

099 Transmission

099 Transmission for Census Record

10/10 Print

Absence List

Add a New Means Test

Add a Copay Exemption Test

Add/Edit Beds

Add/Edit/Delete Catastrophic Disability

Add New Appointments to Call List

Adjudicate a Means Test

Admissions without an Associated PTF Record

Admit a Patient

ALOS Report for DRGs

AMIS 334-341 Reports

AMIS 345-346 Reports

AMIS 401-420 Reports

ASIH Listing

Batch Code Sheets

Batch Edit

Batch Multiple DRG Reports

Batches Waiting to be Transmitted

Bed Availability

Bed Out-of-Service Date Enter/Edit

Bulletin Selection

Calling Statistics Report

Cancel a Scheduled Admission

Census Status Report

Check-in Lodger

Check Routine Integrity

Checkoff PTF Message

Clear the Call List

Close a CNH PAI Record

Close a PAI Record

Close Open Census Record

CNH PAI Edit

Code Sheet Edit

Code Sheets Ready for Batching

Collateral Patient Register

Complete a Required Means Test

Comprehensive Census Report

Comprehensive Report by Admission

Copay Exempt Test Needing Update At Next Appt.

Create a CNH PAI Record

Create a Code Sheet

Create a PAI from Past Admission/Transfer

Current Lodger List

Current MAS Release Notes

Death Entry

Delete a CNH PAI Record

Delete a Code Sheet

Delete a Copay Exemption Test

Delete a Means Test

Delete a PAI

Delete a Registration

Delete Means Test/Copay Dependents

Delete PTF Record

Delete Waiting List Entry

Detailed Inpatient Inquiry

Determine Inconsistencies to Check/Don't Check

Device Selection

Diagnostic Code PTF Record Search

Discharge a Patient

Display Census Date Parameters

Display Preregistration Call List

Display User Access to Patient Record

Disposition an Application

Disposition Log Edit

Disposition Time Processing Statistics

Document Comments on a Means Test

DRG Calculation

DRG Case Mix Summary

DRG Frequency Report

DRG Index Report

DRG Information Report

Duplicate Dependents Report

Duplicate Spouse/Dependent SSN Report

Edit an Existing Copay Exemption Test

Edit an Existing Means Test

Edit Bed Control Movement Types

Edit Data Card File (39.1)

Edit Embosser Device File (39.3)

Edit Inconsistent Data for a Patient

Edit Ward Out-of-Service Dates

EGT Impact Report

Eligibility Inquiry for Patient Billing

Eligibility Verification

Enrolled Veterans Report

Enrollees by Status, Priority, Preferred Facility

Enter/Edit Patient Security Level

Enter/Edit Transmission Routers File

Enter PTF Message

Establish PTF Record from Past Admission

Extended Bed Control

Fee Basis Census Status Report

Female Inpatient List (Current)

G&L Parameter Edit

Gains and Losses (G&L Sheet)

Gains and Losses Initialization

Generate a Code Sheet

GMT Thresholds Lookup by Zip Code

Hardship Review Date

Hardships

Historical Female Inpatient List

Historical Inpatient Listing

Incomplete PAIs by Location

Inconsistent Data Elements Report

Inpatient Card Download

Inpatient Listing

Inpatient Roster

Inquire Census Record

Inquire PTF Message

Inquire PTF Record

Institution File Enter/Edit

Insurance Company Entry/Edit

Insurance List of UNKNOWNS for Inpatients

Invalid State/Inactive County Report

ISO Sensitive Records Report-Export

ISO Sensitive Records Report-Formatted Report

Keypunch a Code Sheet

List Incomplete Copay Exemption Test

List Required/Pending Means Tests

Listing of Records by Completion Status

Load/Edit Patient Data

Load/Edit PTF Data

Lodger Check-out

Lodgers for a Date Range

Log of Dispositions

Mark Batch for Retransmission

Mark Code Sheets for Rebatching

MAS Parameter Entry/Edit

Means Test Indicator of 'U' Report

Means Test Signature Detail Report

Means Test Signature Summary Report

Means Test Specific Income Amount Report

Means Test Specific Income Less Threshold Report

Means Test Threshold Entry/Edit

Means Test w/Previous Year Threshold

Merge Duplicate MT/Copay Dependents

Military Service Data Inconsistencies Report

MPCR Inquiry

Non-Treating Preferred Facility Clean up

N/T Radium Treatment Pending Verification List

Open a Closed or Transmitted CNH PAI

Open a Closed or Transmitted PAI

Open Closed Census Records

Open Closed PTF Record

Open PTF Record Listing

Open Released or Transmitted Census Records

Open Released or Transmitted PTF Records

Outpatient Card Download

PAI Enter/Edit

PAIs for a Date Range

Patient Address Update

Patient Enrollment

Patient Inquiry

Patient Movement List

Patient Review Document

Patient Summary by Admission

Patient Type Update

Patients Who Have Not Agreed To Pay Deductible

Pending Applications for Enrollment

Pending/Open Disposition List

Percentage of Patients Pre-Registered Report

PIMS Events Transmitted for Date Range

PIMS Events Transmitted Yesterday

Pre-Registration Source Report

Preadmission Card Download

Preregister a Patient

Print a Code Sheet

Print Patient Label

Print Patient Wristband

Print Preregistration Audits

Print Special Transaction Request Log

Pro Fee Coding Not Sent to PCE

Productivity Report by Clerk

Productivity Report by Clerk (Census Only)

Provider Change

Pseudo SSN Report for Means Test Dependents

Pseudo SSN Report (Patient)

PTF Expanded Code Listing

PTF Transmission

Purge Call Log

Purge Contacted Patients

Purge Duplicate Income Tests

Purge Income Test Monitor

Purge Inconsistent Data Elements

Purge Non-sensitive Patients from Security Log

Purge Record of User Access from Security Log

Purge Scheduled Admissions

Purge Special Transaction Request Log

Purge Transmission Records/Code Sheets

Purple Heart Request History

Purple Heart Status Report

Quick Load/Edit PTF Data

Reasons for Lodging Entry/Edit

Rebuild Inconsistency File

Recalculate G&L Cumulative Totals

Reimbursable Insurance Primary EC Report

Record Print-Out (RPO)

Record Status Report

Records By Completion Status (Census Only)

Regenerate Census Workfile

Register a Patient

Release Closed Census Records

Release PTF Records for Transmission

Religion List for Inpatients

Report - All Address Change with Rx

Report - All Address Changes

Report - All Patients flagged with a Bad Address

Report - Patient Catastrophic Edits

Required Means Test At Next Appointment

Retransmit Admission Data

Retransmit Entry in ADT/HL7 PIVOT File

Retransmit Patient Demographics

Review a Code Sheet

Review Document by Admission Range

RUG-II Grouper

RUG-II Index

RUG Semi-Annual Background Job

Schedule an Admission

Scheduled Admission Statistics

Scheduled Admissions List

Seriously Ill Inpatient Listing

Seriously Ill List Entry

Set Transmit Flag on Movements

Set Up Non-VA PTF Record

Sharing Agreement Category Update

Show MAS System Status Screen

Single PAI Print

Single Patient Download Request

Status of all Batches

Summary of Dispositions

Surgical Code PTF Record Search

Switch Bed

Template Selection

Test Grouper

Transfer a Patient

Transmission via VADATS

Transmit Census Records

Transmit Code Sheets

Transmit/Generate Release Comments

Transmitted Census Records List

Transmitted Records List

Treating Specialty Inpatient Information

Treating Specialty Print

Treating Specialty Set-up

Treating Specialty Transfer

Trim Point DRG Report

Unreleased Census Records Report

Unreleased PTF Record Output

Unsupported CV End Date Report

Upcoming Appointments without Enrollment

Update Inconsistency File

Update Transfer DRGs for Current FY

Validity Check of PTF Record

VBC Form By Admission Date

VBC Form for Specific Patient

Veteran Patient Insurance Information

View a Past Copay Test

View a Past Means Test

View Copay Exemption Test Editing Activity

View G&L Corrections

View Means Test Editing Activity

View Patient Address

View Registration Data

Waiting List Entry/Edit

Waiting List Output

Ward Definition Entry/Edit

WWU Enter/Edit for RUG-II

Z07 Build Consistency Check