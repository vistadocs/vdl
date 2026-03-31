---
title: PIMS Version 5.3 Registration Menu User Manual (Updated DG*5.3*858)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Registration Menu  (Updated DG*5.3*858)
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*858
group_key: "SD:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 1
description: - [## Overview](#overview) - [Disposition an Application](#disposition-an-application) - [<u> </u>Patient Enrollment](#u-upatient-enrollment) - [Purple Heart Request History](#purple-heart-request-history) - [Purple Heart Status Report](#purple-heart-status-report) - [Add/Edit/Delete Catastrophic Di
audience: 
keywords: 
  - patient
  - test
  - means
  - date
  - edit
  - address
  - table
  - veteran
  - registration
  - contents
page_count: 0
word_count: 41007
section_count: 88
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_p858_reg_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_p858_reg_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

## Table of Contents

  - [## Overview](#overview)
  - [Disposition an Application](#disposition-an-application)
  - [<u> </u>Patient Enrollment](#u-upatient-enrollment)
  - [Purple Heart Request History](#purple-heart-request-history)
  - [Purple Heart Status Report](#purple-heart-status-report)
  - [Add/Edit/Delete Catastrophic Disability](#addeditdelete-catastrophic-disability)
  - [Collateral Patient Register](#collateral-patient-register)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu)
  - [Add a Copay Exemption Test](#add-a-copay-exemption-test)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu-1)
  - [Copay Exempt Test Needing Update At Next Appt.](#copay-exempt-test-needing-update-at-next-appt)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu-2)
  - [Edit an Existing Copay Exemption Test](#edit-an-existing-copay-exemption-test)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu-3)
  - [List Incomplete Copay Exemption Test](#list-incomplete-copay-exemption-test)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu-4)
  - [View a Past Copay Test](#view-a-past-copay-test)
  - [Death Entry](#death-entry)
  - [Delete a Registration](#delete-a-registration)
  - [Disposition Log Edit](#disposition-log-edit)
  - [Edit Inconsistent Data for a Patient](#edit-inconsistent-data-for-a-patient)
  - [Eligibility Inquiry for Patient Billing](#eligibility-inquiry-for-patient-billing)
  - [Eligibility Verification](#eligibility-verification)
  - [<u> </u>Enter/Edit Patient Security Level](#u-uenteredit-patient-security-level)
  - [Invalid State/Inactive County Report](#invalid-stateinactive-county-report)
  - [Load/Edit Patient Data](#loadedit-patient-data)
  - [Means Test User Menu](#means-test-user-menu)
  - [Add a New Means Test](#add-a-new-means-test)
  - [Means Test User Menu](#means-test-user-menu-1)
  - [Adjudicate a Means Test](#adjudicate-a-means-test)
  - [Means Test User Menu](#means-test-user-menu-2)
  - [Complete a Required Means Test](#complete-a-required-means-test)
  - [Means Test User Menu](#means-test-user-menu-3)
  - [Document Comments on a Means Test](#document-comments-on-a-means-test)
  - [Means Test User Menu](#means-test-user-menu-4)
  - [Edit an Existing Means Test](#edit-an-existing-means-test)
  - [Means Test User Menu](#means-test-user-menu-5)
  - [GMT Thresholds Lookup by ZIP Code](#gmt-thresholds-lookup-by-zip-code)
  - [Means Test User Menu](#means-test-user-menu-6)
  - [Hardships](#hardships)
  - [Means Test User Menu](#means-test-user-menu-7)
  - [Pseudo SSN Report for Means Test Dependents](#pseudo-ssn-report-for-means-test-dependents)
  - [<u> </u>Means Test User Menu](#u-umeans-test-user-menu)
  - [View a Past Means Test](#view-a-past-means-test)
  - [Patient Address Update](#patient-address-update)
  - [Patient Inquiry](#patient-inquiry)
  - [Preregistration Menu](#preregistration-menu)
  - [Display Preregistration Call List](#display-preregistration-call-list)
  - [Preregistration Menu](#preregistration-menu-1)
  - [Outputs for Preregistration](#outputs-for-preregistration)
  - [Calling Statistics Report](#calling-statistics-report)
  - [Preregistration Menu](#preregistration-menu-2)
  - [Outputs for Preregistration](#outputs-for-preregistration-1)
  - [Percentage of Patients Pre-Registered Report](#percentage-of-patients-pre-registered-report)
  - [Preregistration Menu](#preregistration-menu-3)
  - [Outputs for Preregistration](#outputs-for-preregistration-2)
  - [Pre-Registration Source Report](#pre-registration-source-report)
  - [Preregistration Menu](#preregistration-menu-4)
  - [Outputs for Preregistration](#outputs-for-preregistration-3)
  - [Print Preregistration Audits](#print-preregistration-audits)
  - [Preregistration Menu](#preregistration-menu-5)
  - [Supervisor Preregistration Menu](#supervisor-preregistration-menu)
  - [Add New Appointments to Call List](#add-new-appointments-to-call-list)
  - [Preregistration Menu](#preregistration-menu-6)
  - [Supervisor Preregistration Menu](#supervisor-preregistration-menu-1)
  - [Clear the Call List](#clear-the-call-list)
  - [Preregistration Menu](#preregistration-menu-7)
  - [Supervisor Preregistration Menu](#supervisor-preregistration-menu-2)
  - [Purge Call Log](#purge-call-log)
  - [Preregistration Menu](#preregistration-menu-8)
  - [Supervisor Preregistration Menu](#supervisor-preregistration-menu-3)
  - [Purge Contacted Patients](#purge-contacted-patients)
  - [Preregistration Menu](#preregistration-menu-9)
  - [Patient Inquiry](#patient-inquiry-1)
  - [Preregistration Menu](#preregistration-menu-10)
  - [Preregister a Patient](#preregister-a-patient)
  - [Print Patient Wristband](#print-patient-wristband)
  - [Pseudo SSN Report (Patient)](#pseudo-ssn-report-patient)
  - [Register a Patient](#register-a-patient)
  - [Report - All Address Change with Rx](#report-all-address-change-with-rx)
  - [Report - All Address Changes](#report-all-address-changes)
  - [Report - All Patients flagged with a Bad Address](#report-all-patients-flagged-with-a-bad-address)
  - [Report - Patient Catastrophic Edits](#report-patient-catastrophic-edits)
  - [Unsupported CV End Date Report](#unsupported-cv-end-date-report)
  - [View Patient Address](#view-patient-address)
  - [View Registration Data](#view-registration-data)
  - [Registration Supplement](#registration-supplement)
PIMS V. 5.3 ADT Module User ManualRegistration Menu
Overview
Disposition an Application
Patient Enrollment
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
Registration Supplement for Newborns
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
<th><strong>Date</strong></th>
<th><strong>Description (Patch # if applic.)</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/5/04</td>
<td>DG*5.3*564 - HEC VistA enhancements</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/23/04</td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/5/05</td>
<td><p>DG*5.3*628 - HVE Follow-up enhancements</p>
<p>Removal of AO Exposure Location Change Bulletin</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/21/05</td>
<td>Added 2 options - Percentage of Patients Pre-Registered Report and Report-All Address Change with Rx</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/28/05</td>
<td>DG*5.3*563 - Date of Death enhancements</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/21/05</td>
<td>DG*5.3.*633 - Added All Patients flagged with a Bad Address option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>4/26/05</td>
<td>DG*5.3.*638 - Preventing Catastrophic Edits enhancements</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/12/05</td>
<td><p>DG*5.3*624 – 10-10EZ 3.0 enhancements</p>
<p>Changed Printing Prompt Sequence in Financial Assessment Applications.</p>
<p>Added note for Roll-Up Means Test Dollar Amounts (GAI and NW) to conform with amounts on Feb 2005 VistA-Printed 10-10EZ/EZR Forms.</p>
<p>Added 10-10 Print – Means Test Selection (Test Director Defect #108) Selection List info under Register a Patient section.</p>
<p>Added “Print 1010EZ/EZR” as an available option under the Patient Enrollment section.</p>
<p>Added updates based on revised business rules for evaluating child(ren)’s Income Available to veteran and how it affects the Gross Annual Income dollar amounts printed on the 10-10EZ/EZR and displayed in the Child(ren)’s column on the Previous Calendar Year Gross Income Screen 2.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/26/05</td>
<td><p>DG*5.3*677 – Emergency Response, Hurricane Katrina Project</p>
<p>Updated Patient Inquiry and Registration Screen 2 in Registration Supplement Section</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/14/05</td>
<td>DG*5.3*655 – Remove Income Test Inconsistency Checks Updated Means Test User Menu options</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/9/05</td>
<td><p>DG*5.3*658 – Address Updates</p>
<p>Added Patient Address Update option.</p>
<p>Added prompt to update permanent address through the following options:</p>
<blockquote>
<p>Register a Patient</p>
<p>Load/Edit Patient Data</p>
<p>Preregister a Patient.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/21/06</td>
<td><p>DG*5.3*672 – Enrollment VistA Changes Early Release</p>
<p>Updated table in Patient Enrollment option.</p>
<p>Updated screen example and Data Group 13 of Screen 6 in Registration Supplement section.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>4/26/06</td>
<td><p>DG*5.3*695 – Revised the following options for Permanent Address Update:</p>
<blockquote>
<p>Register a Patient</p>
<p>Load/Edit Patient Data</p>
<p>Preregister a Patient.</p>
</blockquote>
<p>Revised Patient Address Update option narrative for logical flow.</p>
<p>Revised Patient Demographics Screen &lt;1&gt; Date Group 4 in Registration Supplement section.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/7/06</td>
<td><p>DG*5.3*611 – Fix Means Test Display</p>
<p>Updated Add a New Means Test, Add a Copay Exemption Test, Complete a Required Means Test, Edit a Copay Exemption Test, and Edit an Existing Means Test options</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/14/06</td>
<td>DG*5.3*694 – Added Invalid State/Inactive County Report option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/13/06</td>
<td>DG*5.3*673 – Added new registration menu Screen 6 – Military Service Data - for OEF/OIF in Registration Supplement section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/4/06</td>
<td>DG*5.3*689 – Enhancements to Registration Supplement Military Service Data Screen 6</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/23/06</td>
<td>DG*5.3*716 – Revised Data Group 1 on Screen 11 in Registration Supplement section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/3/06</td>
<td>DG*5.3*659 - Updated dependent effective date description for Screen 8 and radiation exposure method for Screen 6 in Registration Supplement section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/27/06</td>
<td><p>DG*5.3*583 – Enable Upload of Claim Folder Location</p>
<p>Added list of acceptable Claim Folder Locations and Preferred Facilities.</p>
<p>Updated Patient Enrollment Option.</p>
<p>Updated Screen 7, Data Group 1, in Registration Supplement section.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/19/07</td>
<td><p>DG*5.3*657 – Update Data Entry Consistency Checks</p>
<p>Updated data group fields for Screens 6 &amp; 7 in the Registration Supplement section.</p>
<p>Added Pseudo SSN note to Overview and Registration Supplement sections.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/11/07</td>
<td><p>DG*5.3*653 – Enrollment VistA Changes Release 1 (EVC R1) Added Pseudo SSN Report (Patient) option.</p>
<p>Added Pseudo SSN Report for Means Test Dependents option.</p>
<p>Updated Registration Screens 1, 7, and 8 in the Registration Supplement section.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/14/08</td>
<td>Minor Formatting Changes</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/29/08</td>
<td>Updated Registration Supplement Section with missing information</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/29/09</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/30/09</td>
<td><p>DG*5.3*688 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<ul>
<li><blockquote>
<p>Updated Registration screens 1, 1.1, 6, 7, 8, 9 in Registration Supplement</p>
</blockquote></li>
<li><blockquote>
<p>Removed Copy Data function from income tests</p>
</blockquote></li>
<li><blockquote>
<p>Updated the following options: <em>Patient Inquiry</em></p>
</blockquote></li>
</ul>
<blockquote>
<p><em>Report-All Address Changes with Rx</em></p>
<p><em>Report-All Address Changes</em></p>
<p><em>View Patient Address</em></p>
</blockquote>
<ul>
<li><blockquote>
<p>Added “Modify Means Test Data Collection – Means Test Version Indicator” to Overview Section</p>
</blockquote></li>
<li><blockquote>
<p>Changed “environmental contaminants” to “SW Asia Conditions”</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>4/24/09</td>
<td><p>DG*5.3*808 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<ul>
<li><blockquote>
<p>Removed reference to Rated Disability mail message sent in Registration Supplement, Screen 11, Data Group 4</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/10/09</td>
<td><p>DG*5.3*803 – Priority Group 8 Changes</p>
<ul>
<li><blockquote>
<p>Updated the <em>GMT Thresholds Lookup by ZIP Code</em> section with the new priority 8 sub-categories ‘b’ and ‘d’.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/5/09</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<ul>
<li><blockquote>
<p>Added new Special Treatment Authority Expiration date info for AO and SWAC to the <strong>Means Test User Menu</strong> section.</p>
</blockquote></li>
<li><blockquote>
<p>Updated <strong>Additional Patient Demographic</strong> <strong>Data</strong> screen 1.1 w/Confidential Phone.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/18/10</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<ul>
<li><blockquote>
<p>Added additional parameters to the <em>Enroll Patient</em> table entry in the <strong>Patient Enrollment</strong> section.</p>
</blockquote></li>
<li><blockquote>
<p>Added additional <em>Date of Death</em> parameters in the <strong>Death Entry</strong> section.</p>
</blockquote></li>
<li><blockquote>
<p>Added additional <em>Date of Birth</em> parameters to <strong>Screen 1</strong>, <strong>Data Group 1</strong> section.</p>
</blockquote></li>
<li><blockquote>
<p>Added additional Date of Death condition to the <strong>Screen 7</strong>, <strong>Data Group 1</strong> section for <em>P&amp;T Effective Date</em>, <em>DATE RULED INCOMPETENT (CIVIL)</em>, <em>DATE RULED INCOMPETENT (VA)</em></p>
</blockquote></li>
<li><blockquote>
<p>Added additional parameter to the <strong>Screen 10, Data Group 1</strong> section for <em>INELIGIBLE DATE</em>.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/27/11</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<p>Removed <em>Date of Death</em> parameter (Enroll. App. Date) in the <strong>Death Entry</strong> section.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/25/2011</td>
<td><p>DG*5.3*840</p>
<p>New fields added to Patient and Patient Enrollment:</p>
<ul>
<li><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></li>
<li><blockquote>
<p>CURRENT MOH INDICATOR field (#.541) PATIENT file (#2)</p>
</blockquote></li>
<li><blockquote>
<p>MEDAL OF HONOR INDICATED? field (#50.23) PATIENT ENROLLMENT file (#27.11)</p>
</blockquote></li>
</ul>
<p>Edited Copayment and Means Test Exemptions/Add a New Means Test sections regarding Catastrophically Disabled and Medal of Honor changes.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/23/2011</td>
<td><p>DG*5.3*838</p>
<p>New field added</p>
<ul>
<li><p>PATIENT file (#2)</p></li>
<li><p>SOURCE DESIGNATION field (#27.03)</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/1/2011</td>
<td><p>DG*5.3*797 changes</p>
<ul>
<li><p>Edit working of the Unnsupported CV End Date Report description.</p></li>
<li><p>Updated Registration Screen 6</p></li>
<li><p>Added Screen 6.1 and 6.2</p></li>
<li><p>Added Service Discharge Types to include Dishonorable-VA and Honorable-VA</p></li>
<li><p>Added MSDS description of MSE changes</p></li>
<li><p>Removed second and third military service episodes</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/5/2011</td>
<td><p>DG*5.3*797 changes</p>
<p>TW Review, minor formatting</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/19/2012</td>
<td><p>DG*5.3*797 changes</p>
<p>Added definitions for new Service Discharge Types: Dishonorable-VA and Honorable-VA.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/26/2012</td>
<td><p>DG*5.3*841 changes (PL163-111)</p>
<p>Added <em>Medal of Honor</em> Data Group 9 to Screen &lt;6&gt;.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/26/2012</td>
<td><p>DG*5.3*842 – ESR 3.6 VBA Pension Data Sharing</p>
<p>Updated screen shots:</p>
<ul>
<li><p>MILITARY SERVICE DATA, SCREEN &lt;6&gt;</p></li>
<li><p>ELIGIBILITY STATUS DATA, SCREEN &lt;7&gt;</p></li>
<li><p>Added new Pension and Dental fields to the Check Query Status list.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/29/2012</td>
<td><p>DG*5.3*842 – ESR 3.6 VBA Pension Data Sharing</p>
<p>Minor updates to</p>
<ul>
<li><p>ELIGIBILITY STATUS DATA, SCREEN &lt;7&gt;</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/25/2012</td>
<td><p>DG*5.3*851 – ESR 3.8 Permanent Address Modifications</p>
<p>Update to options for permanent address functionality:</p>
<ul>
<li><blockquote>
<p>LOAD/EDIT PATIENT DATA</p>
</blockquote></li>
<li><blockquote>
<p>REGISTER A PATIENT</p>
</blockquote></li>
<li><blockquote>
<p>PREREGISTER A PATIENT</p>
</blockquote></li>
</ul>
<p>Update to Registration Supplement for temporary and confidential Addresses:</p>
<ul>
<li><blockquote>
<p>Screen 1, Data Group 5</p>
</blockquote></li>
<li><blockquote>
<p>Screen 1.1, Data Group 1</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/10/2013</td>
<td><p>DG*5*3*867 - Caregiver Newborn Claims Processing</p>
<p>Added new Registration Supplement for Newborn.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/5/2014</td>
<td><p>DG*5.3*858 – ESR 3.10</p>
<p>Veterans Financial Assessment – Discontinue Annual Means Test Renewal</p>
<p>Update to Overview Means Test User Menu options:</p>
<ul>
<li><p>Add a New Means Test</p></li>
<li><p>Complete a Required Means Test</p></li>
<li><p>Edit an Existing Means Test</p></li>
<li><p>Hardships</p></li>
</ul>
<p>Update to options:</p>
<ul>
<li><p>Adjudicate a Means Test</p></li>
<li><p>Complete a Required Means Test</p></li>
<li><p>Edit an Existing Means Test</p></li>
<li><p>Hardships</p></li>
<li><p>Report – All Patients Flagged with a Bad Address</p></li>
</ul>
<p>Supplement for Bad Address Indicator:</p>
<ul>
<li><p>Screen 1, Data Group 4</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

## ## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains those options related to the processing of patient applications for care. This includes creation and editing of patient records, assigning a sensitive security level to certain patient records in order to restrict user access, registration and disposition, determination of need for and performance of Means Tests and Copay Tests, and updating eligibility status on a patient.

Central to just about all functions in the ADT system is the creation of patient records in your computer. This will usually be accomplished through the Register A Patient option at the time a patient applies for care at your facility. If a patient is not applying for care, but you wish to enter them into your database, you should do so using the Load/Edit Patient Data option rather than Register A Patient.

The information necessary to create a patient's record is gathered and displayed via a series of formatted data screens. You will see these screens in several other registration-related options as well as Register A Patient and Load/Edit Patient Data. The information which is gathered on each patient depends upon their patient type assignment; i.e., non-service connected, service connected, employee, etc. There are a number of exported patient types, and your site also has the ability to enter its own. For each patient type various Registration Screens may be turned OFF and ON depending upon what information is needed for that particular patient type. You will find this more fully explained in the documentation pertaining to those options that utilize the screens.

OverviewModify Means Test Data Collection - Means Test Version Indicator

A Means Test version indicator will be created and will support the display and collection of Means Test information for both the 1010EZ form prior to February 2005 and the 1010EZ form from February 2005. These modifications (outlined in Patches IVMB\*2\*860 and IVMB \*2\*886) support the February 2005 form. The Means Test information collected prior to installation of this patch will continue to be collected, printed, and displayed in the February 2005 format.

Listed below are the following modifications created to display the Means Test version indicator VistA Options:

Load/Edit Patient \[DG LOAD PATIENT DATA\]

Register a Patient \[DG REGISTER PATIENT\]

Add a New Means Test \[DG MEANS TEST ADD\]

Complete a Required Means Test \[DG MEANS TEST COMPLETE\]

Edit an Existing Means Test \[DG MEANS TEST EDIT\]

View a Past Means Test \[DG MEANS TEST VIEW TEST\]

Purge Duplicate Income Tests \[DG CLEANUP INCOME TEST DUPES\]

Add a Copay Exemption Test \[DG CO PAY TEST ADD\]

Edit an Existing Copay Exemption

Test \[DG CO PAY TEST EDIT\]

View a Past Copay Test \[DG CO PAY TEST VIEW TEST\]

The benefits for supporting the Means Test version indicator will include the following elements:

- Income Available Response collected for Dependent Child(ren) will now support collection of children Net Worth Dollar Amounts. Children Net Worth Dollar amounts will be collected with the new form.
- A limit of 19 dependent children will be collected for a Means Test. This limit applies to those dependents with relationships of son, daughter, step-son, and step-daughter.
- The collection of Previous Calendar Year Gross Annual Income with February 2005 Data format will be changed to collect 3 data elements rather than the 10 data elements collected with the pre February 2005 format.
- Means Test data collection will collect the Gross Medical Expenses dollar amount, within Deductible Expenses, labeled as "Total Non-Reimbursed Medical Expenses.”

Overview

- February 2005 1010EZ form Means Test data collection will no longer require a spouse or dependent child (associated with the Means Test) to collect funeral and burial expenses.
- The collection of Previous Calendar Year Net Worth with February 2005 Data format will be changed to collect 3 data elements rather than the 5 data elements collected with the pre February 2005 format.
- The system will continue to display the summary Income, Net Worth, and Deductible Expenses amounts in the February 2005 data collection format as was displayed with the pre February 2005 data collection format. The system will continue to calculate the summary Income, Net Worth, and Deductible Expense amounts in the February 2005 data collection format with the same formulas as with the existing data collection format.
- Entry of Means Test information in the February 2005 data collection format will produce the same Means Test status that results when the Means Test information is entered with the existing data collection format.
- The "Copy Data" function will be removed from the Means Test user interface for both February 2005 form and pre February 2005 form. The "Copy Data" function will still be performed by the Means Test system when done automatically. For example, if the Primary Eligibility Code changes from Non-Service Connected to Service Connected, a Pharmacy Copay test will automatically be created. When this "automatic" copy occurs, the Annual Income information will be checked for the data collection form. If that data is in pre February 2005 form, it will convert to the February 2005 form to match the newly created Pharmacy Copay Test.

The following menus/options are included in the Registration menu.

DISPOSITION AN APPLICATION

This option is used to enter the final outcome of a registration; i.e., whether the patient was admitted, scheduled for a return visit, treated with no further care necessary, etc.

PATIENT ENROLLMENT

This option is used to enroll patients that are eligible for care. This option is also used to cease enrollment, expand an enrollment history record, and update a patient's preferred facility.

PURPLE HEART REQUEST HISTORY

This option lists the history entries of all updates to the Purple Heart Indicator, Status, and Remarks fields for an individual patient.

Overview

PURPLE HEART STATUS REPORT

This option lists all patients who have a current Purple Heart status of *Pending* or *In Process*.

ADD/EDIT/DELETE CATASTROPHIC DISABILITY

This option is used to enter, edit, delete, and view a patient’s catastrophic disability (CD) information.

COLLATERAL PATIENT REGISTER

This option is used to enter a collateral patient into the system. The patient selected cannot be a veteran.

COPAY EXEMPTION TEST USER MENU

> ADD A COPAY EXEMPTION TEST

> This option allows adding a new Copay Test into the system.

> COPAY EXEMPT TEST NEEDING UPDATE AT NEXT APPT.

> This option is used to generate a listing of future appointments listing Copay Exemption Tests which will require updating.

> EDIT AN EXISTING COPAY EXEMPTION TEST

> This option is used to make changes to data in existing Copay Tests.

> LIST INCOMPLETE COPAY EXEMPTION TEST

> This option is used to generate a listing of patients who have an incomplete Copay Test on file.

> VIEW A PAST COPAY TEST

> This option is used to view past Copay Test data.

DEATH ENTRY

This option is used to enter, edit, or delete date of death information for a patient record.

Overview

DELETE A REGISTRATION

This option is used to delete a registration which has not been dispositioned.

DISPOSITION LOG EDIT

This option is used to edit information appearing on the Disposition Log for selected patients.

EDIT INCONSISTENT DATA FOR A PATIENT

This option is used to run the Consistency Checker for a selected patient, edit their inconsistent/unspecified data, and update the INCONSISTENT DATA file accordingly.

ELIGIBILITY INQUIRY FOR PATIENT BILLING

This option provides a quick reference to patient information used in determining appropriate patient billing.

ELIGIBILITY VERIFICATION

This option is used to enter/edit a patient's eligibility data as well as update their verification status without accessing their entire record.

ENTER/EDIT PATIENT SECURITY LEVEL

This option is used to restrict user access to computer records of certain patients by flagging them as sensitive. Access of such records is tracked and logged by the system.

INVALID STATE/INACTIVE COUNTY REPORT

This option is used to create a report that lists patient records where the address fields contain invalid states and/or inactive counties.

LOAD/EDIT PATIENT DATA

This option is used to create and/or edit a patient record without generating a registration.

MEANS TEST USER MENU

> ADD A NEW MEANS TEST

> This option allows the user to add a means test if the patient is subject to means testing and a means test does not exist for the current income year. You must hold the DG MEANSTEST security key in order to use this option.

Overview

> ADJUDICATE A MEANS TEST

> This option allows entry of final outcome of Means Tests referred to Adjudication. You must hold the DG MEANSTEST security key in order to use this option.

> COMPLETE A REQUIRED MEANS TEST

> This option allows completion of Means Tests for patients in a required status, whose names appear on the Means Test List. The user may only complete the required means test if the test is less than 1 year old.

> Document Comments on a Means Test

> This option is used to add/edit/delete free-text comments on a selected Means Test.

> EDIT AN EXISTING MEANS TEST

> This option is used to make changes to and/or view data in existing Means Tests that are less than 1 year old. A message asking the user to add a new means test will be displayed if the test is older than 1 year old. You must hold the DG MEANSTEST security key in order to use this option.

> GMT Thresholds Lookup by Zip Code

> This option displays GMT threshold values for valid zip code.

> HARDSHIPS

> This option allows the user to grant, edit, and delete hardships for the current income year Means Test.

> PSEUDO SSN REPORT FOR MEANS TEST DEPENDENTS

> This option allows the user to print a report of dependents, sorted by patient, who have Pseudo SSNs.

> VIEW A PAST MEANS TEST

> This option allows viewing of past Means Tests data.

PATIENT ADDRESS UPDATE

This option allows the user to update the patient’s permanent address, temporary address, or both. It may be placed on other application’s menus so users can update patient addresses directly from their own applications’ menus.

PATIENT INQUIRY

This option displays current patient information including basic demographic information, inpatient status, and future appointments.

Overview

PREREGISTRATION MENU

> DISPLAY PREREGISTRATION CALL LIST

> This option displays the Preregistration Call List in List Manager screen format.

> OUTPUTS FOR PREREGISTRATION

> CALLING STATISTICS REPORT

> This option prints the Preregistration Call Statistics report which provides a breakdown of the current entries in the PRE-REGISTRATION CALL LOG file (#41.43).

> PERCENTAGE OF PATIENTS PRE-REGISTERED REPORT

> This option prints a report containing information on the number and percentages of pre-registered patients for a user-defined date range.

> PRE-REGISTRATION SOURCE REPORT

> This option prints a report containing information on preregistration insurance and billing policies.

> PRINT PREREGISTRATION AUDITS

> This option prints the audits pertaining to preregistration from the PATIENT file (#2).

> SUPERVISOR PREREGISTRATION MENU

> ADD NEW APPOINTMENTS TO CALL LIST

> This option lets you add patients to the Preregistration Call List based on patient appointments on a user-specified search date.

> CLEAR THE CALL LIST

> This option deletes all entries in the PRE-REGISTRATION CALL LIST file (#41.42) regardless of the call status.

> PURGE CALL LOG

> This option purges all entries prior to a user-specified date from the PRE-REGISTRATION CALL LOG file (#41.43).

> PURGE CONTACTED PATIENTS

> This option purges patients who have already been contacted from the Preregistration Call List.

Overview

> PATIENT INQUIRY

> This option displays registration information for a selected patient, including any preregistration items, and the Bad Address Indicator.

> PREREGISTER A PATIENT

> This option lets you preregister a selected patient through the use of the Load/Edit process without using the Preregistration Call List.

PRINT PATIENT WRISTBAND

This option is used to print a patient wristband with bar coded social security number.

PSEUDO SSN REPORT (PATIENT)

This option allows the user to print a report that lists patients with Pseudo SSNs. It can be printed for veterans, non-veterans or both, and for all Pseudo SSN Reasons or a specific Pseudo SSN Reason.

REGISTER A PATIENT

This option is used to create and/or edit a patient record while generating a registration (Application for Health Benefits). This registration must subsequently be dispositioned.

REPORT - ALL ADDRESS CHANGE WITH RX

This option lists those patients with active pharmacy prescriptions whose primary address fields have been changed during the previous 24 hours.

REPORT - ALL ADDRESS CHANGES

This option can be run from the Registration Menu or scheduled via Task Manager. If a patient’s permanent address is changed during the previous 24 hours, the report will list the patient permanent address as of now and the patient permanent address as of 24 hours ago. The output is sent to the DG DAILY ADDRESS CHANGE mail group.

REPORT - ALL PATIENTS FLAGGED WITH A BAD ADDRESS

This option lists those patients flagged with a bad address indicator.

REPORT - PATIENT CATASTROPHIC EDITS

This option is used to print a report for a user-selected date range which provides a listing of patients who were flagged as having a potential catastrophic edit alert created for supervisory review.

Overview

UNSUPPORTED CV END DATE REPORT

The HEC calculates and shares the CV End Date with VistA sites.  Because VistA may not have Military Service Data (MSD) to support this determination, there may be some inconsistencies created at the V*IST*A Site. This option runs a report helping the sites identify CV End Dates without the supporting MSD.

VIEW PATIENT ADDRESS

This option allows a user to view the patient's address along with the address change date, address change source, address change site (if applicable), and Bad Address Indicator.

VIEW REGISTRATION DATA

This option is used to view the data contained in a patient's record. Editing is not permitted through this option.

A Registration Supplement is provided giving examples of each of the registration screens and descriptions of the data elements that will be prompted for when using them.

PSEUDO SSN NOTE: For every option that displays the patient’s SSN, if the patient has a Pseudo SSN on file, the message “\*\*Pseudo SSN\*\*" will be displayed next to the SSN.

## Disposition an Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to record the final outcome of a patient’s application for health benefits (i.e., whether they were admitted, scheduled for a return visit, no treatment was necessary). Patients having open registrations (registrations which have not been dispositioned) may not be reregistered until dispositioning is accomplished. You may obtain a list of those dispositions which are open or pending determination through the Pending/Open Disposition List option under the ADT Outputs menu.

If applicable, you will be afforded the opportunity to complete a Means Test.

If the amount of hours between registration and disposition is greater than the amount of time specified in the PIMS site parameter, TIME FOR LATE DISPOSITION, the “Reason for Late Disposition” prompt will appear.

Following data entry, the system will disposition the application and categorize the registration in the correct AMIS 401-420 series. All patient registrations must be dispositioned in order to be counted in this series. For Means Test patients, final determination will be made at the time the AMIS 401-420 report is actually run. This has been done to account for possible fluctuation in patients’ Means Test categories as a result of having multiple Means Tests performed within a period of time.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may be displayed with V. 2.5 of Order Entry/Results Reporting. The disposition must have a change in status from APPOINTMENT W/O EXAM to 10/10 or UNSCHEDULED in order for a notification to be displayed. The notification will only be displayed for patients who are defined in an OE/RR LIST entry and will only be displayed to users defined in that list entry. Please refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

When dispositioning a patient to admission, a warning will appear and the admission process will be bypassed if the patient is currently an inpatient or a lodger. If the patient is a lodger, he/she must be checked out as a lodger prior to being dispositioned. This can be accomplished through the Lodger Check-out option found in the Bed Control menu.

Disposition an Application

Depending on the type of disposition selected, other PIMS functionality may be accessed (i.e., Make Appointment). Please refer to the appropriate option documentation, if necessary.

The eligibility code and period of service are now required before a registration can be dispositioned. These elements were previously checked for at registration.

The validation logic performs the same validation checks as the Austin database to identify errors before they are transmitted. The validator (or edit checker) will review the entire encounter rather than stopping after the first error is found. You may be given the opportunity to correct these errors through this option.

The Veterans Healthcare Eligibility Reform Act of 1996, PL 104-262, prohibits providing care for veterans who are not enrolled after October 1, 1998 (with limited exceptions). The Disposition an Application option displays enrollment information and provides the ability to enroll the patient in the VA Patient Enrollment System.

A preliminary priority value is calculated on an initial enrollment application. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is *at or below* the latest EGT setting for a new enrollee or *below* the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is *below* the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” shall be assigned.

At verification, the HEC will recalculate these fields based on a Master Veteran Record containing all nationally available patient data.

## <u> </u>Patient Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option permits those patients that are eligible for care to be enrolled. It is also used to expand an enrollment history record and update a patient’s preferred facility. The screens which may be displayed while utilizing this option are *Enrollment*, *Priority Factors*, and *Enrollment History*. Note that actions that appear on the screens enclosed in parentheses ( ) are not available for selection.

A preliminary priority value is calculated on an initial enrollment application. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is *at or below* the latest EGT setting for a new enrollee or *below* the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is *below* the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” shall be assigned. At verification, the HEC will recalculate these fields based on a Master Veteran Record containing all nationally available patient data.

The CE Cease Enrollment functionality in this option has been disabled. Veterans will now sign a form declaring their wish to cancel/decline which will then be faxed to the HEC for processing.

The following is a description of the actions available through this option.

<u>  
</u>Patient Enrollment

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 19%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Short Name</strong></td>
<td><strong>Full Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>EP</td>
<td>Enroll Patient</td>
<td>Lets you enroll patients that are eligible for care but not previously enrolled. The Enrollment Application Date must be a precise date, cannot be a date prior to the Date of Birth, cannot be a date after the Date of Death, cannot be a date prior to 10/1/1996 and cannot be a date in the future.</td>
</tr>
<tr class="odd">
<td>PF</td>
<td>Preferred Facility</td>
<td><p>Lets you edit the treatment facility preferred by the patient when the SOURCE DESIGNATION is null, VistA, or PCP Inactive.</p>
<p>Note: The Preferred Facility is locked when the SOURCE DESIGNATION is ESR or PCP Active.</p>
<p>The preferred facility must be an active facility and preferred facility type must be one of the following:</p>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>CBOC</th>
<th>(Community Based Outpatient Clinic)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HCS</td>
<td>(Health Care System)</td>
</tr>
<tr class="even">
<td>HEALTHCARE</td>
<td>(VA Boston Health Care System</td>
</tr>
<tr class="odd">
<td>M&amp;ROC</td>
<td>(Medical and Regional Office Center)</td>
</tr>
<tr class="even">
<td>MOC</td>
<td>(Mobile Outpatient Clinic)</td>
</tr>
<tr class="odd">
<td>MORC</td>
<td>(Mobile Outreach Clinic)</td>
</tr>
<tr class="even">
<td>NETWORK</td>
<td>(VA Healthcare Network Upstate NY)</td>
</tr>
<tr class="odd">
<td>NHC</td>
<td>(Nursing Home Care)</td>
</tr>
<tr class="even">
<td>OC</td>
<td>(Outpatient Clinic - Independent)</td>
</tr>
<tr class="odd">
<td>OCMC</td>
<td>(Outpatient Clinic - Subordinate)</td>
</tr>
<tr class="even">
<td>OCS</td>
<td>(Outpatient Clinic Substation)</td>
</tr>
<tr class="odd">
<td>OPC</td>
<td>(Out Patient Clinic)</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>(Outreach Clinic)</td>
</tr>
<tr class="odd">
<td>RO-OC</td>
<td>(Regional Office - Outpatient Clinic)</td>
</tr>
<tr class="even">
<td>SATELLITE</td>
<td>(Satellite Outpatient Clinic)</td>
</tr>
<tr class="odd">
<td>SOC</td>
<td>(Satellite Outpatient Clinic)</td>
</tr>
<tr class="even">
<td>VAMC</td>
<td>(VA Medical Center)</td>
</tr>
<tr class="odd">
<td>VANPH</td>
<td>(Neural Psychiatric Hospital)</td>
</tr>
<tr class="even">
<td>VA ROSEBERG</td>
<td>(VA Roseburg Health Care System)</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="even">
<td>EH</td>
<td>Expand History</td>
<td>Lets you scroll through the enrollment history screens. This action is only available if the selected patient is already enrolled.</td>
</tr>
<tr class="odd">
<td>SQ</td>
<td>Send Query</td>
<td>Lets you transmit an enrollment query. The software asks if you want to be notified when the query returns. The notification information is then displayed on the status bar.</td>
</tr>
<tr class="even">
<td>CD</td>
<td>Catastrophic Disability</td>
<td>Works the same as the Add/Edit/Delete Catastrophic Disability menu option.</td>
</tr>
<tr class="odd">
<td>SP</td>
<td>Select Patient</td>
<td>Lets you select another patient without leaving the Patient Enrollment option.</td>
</tr>
</tbody>
</table>

Patient Enrollment

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 19%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Short Name</strong></td>
<td><strong>Full Name</strong></td>
<td colspan="2"><strong>Description</strong></td>
</tr>
<tr class="even">
<td>AU</td>
<td>View Upload Audit</td>
<td colspan="2">Displays fields in the PATIENT file (#2) that are changed when a transaction is uploaded from the HEC.</td>
</tr>
<tr class="odd">
<td>PZ</td>
<td>Print 1010EZ/EZR</td>
<td colspan="2">Lets you print the 10-10EZ or 10-10EZR</td>
</tr>
<tr class="even">
<td rowspan="2">QS</td>
<td rowspan="2">Check Query Status</td>
<td colspan="2"><p>Lets you check the status of an outstanding enrollment/eligibility</p>
<p>query. The status bar displays the status of the last enrollment/</p>
<p>eligibility query sent for the selected patient. If HEC has an enrollment record for the patient being enrolled, the reply will contain the patient's enrollment record. If HEC has eligibility data on file, that data will also be included in the query reply. The data will be automatically uploaded for all fields in the PATIENT ENROLLMENT file (#27.11) and to the following fields in the PATIENT file (#2) (unless a problem is detected).</p></td>
</tr>
<tr class="odd">
<td><p>Eligibility Status Date</p>
<p>Eligibility Status</p>
<p>Eligibility Verif. Method</p>
<p>Date of Death</p>
<p>Claim Number</p>
<p>Claim Folder Location*</p>
<p>POW Status Indicated?</p>
<p>SC Award Date</p>
<p>Total Annual VA Check Amount</p>
<p>Veteran Y/N?</p>
<p>Service Connected?</p>
<p>Service Connected Percentage</p>
<p>Receiving a VA Pension?</p>
<p>Pension Award Effective Date</p>
<p>Pension Award Reason</p>
<p>Pension Terminated Date</p>
<p>Pension Terminated Reason 1</p>
<p>Pension Terminated Reason 2</p>
<p>Pension Terminated Reason 3</p>
<p>Pension Terminated Reason 4Receiving A&amp;A Benefits?</p>
<p>Receiving Housebound Benefits?</p>
<p>Receiving VA Disability?</p>
<p>Military Disability Retirement</p>
<p>Discharge Due to Disability</p>
<p>Agent Orange Expos. Indicated?</p>
<p>Agent Orange Expos. Location</p>
<p>Radiation Exposure Indicated?</p>
<p>SW Asia Conditions</p></td>
<td><p>Primary Eligibility Code</p>
<p>Patient Eligibilities</p>
<p>P&amp;T</p>
<p>Unemployable</p>
<p>Rated Incompetent?</p>
<p>Ineligible Date</p>
<p>Ineligible Reason</p>
<p>Ineligible VARO Decision</p>
<p>Eligible For Medicaid?</p>
<p>Preferred Facility</p>
<p>Rated Disabilities (VA) multiple, field .3721, multiple 2.04</p>
<p>Rated Disabilities (VA)</p>
<p>Disability %</p>
<p>Service Connected</p>
<p>Catastrophic Disability</p>
<p>Review Date</p>
<p>Decided By</p>
<p>Facility Making Determination</p>
<p>Date Of Decision</p>
<p>Medal of Honor</p>
<p>Source Designation</p>
<p>Class II Dental Indicator</p>
<p>Dental Appl Due Before Date</p></td>
</tr>
</tbody>
</table>

\*Starred for deletion.

\*\*Uploaded data will replace existing data

Patient Enrollment

For information about how a veteran's priority is derived, please refer to the Enrollment Priority Algorithm portion of the ADTBE.pdf file. To upload patient demographic information, use the Demographics Upload option on the IVM Upload Menu. Refer to the IVM V. 2.0 User Manual for information about using this option, if necessary.

## Purple Heart Request History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purple Heart Request History option is used to view the history of a Purple Heart request for an individual patient. The only prompts are for patient name and device.

Information provided includes station and division (at multi-divisional facilities), patient name and social security number, current Purple Heart indicator, status, remarks, and name of the individual who updated the information.

The STATUS field may contain the following values.

> Pending - set when the Current Purple Heart Indicator contains a YES value.

> In Process - set when message received from the HEC (Health Eligibility Center).

> Confirmed - set when confirmation message is received from the HEC.

The REMARKS field will only contain a value if the CURRENT PURPLE HEART INDICATOR field is NO.

## Purple Heart Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view a list of all patients with current Purple Heart requests with a status of *Pending* or *In Process*. The report is sorted by number of days since the last status change in either ascending or descending order (user-selected). The only prompts are for sort order and device.

Information provided includes station and division (at multi-divisional facilities), and for each request, patient name and social security number, days pending, and date pending. Totals are provided at the end of the report.

## Add/Edit/Delete Catastrophic Disability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit/Delete Catastrophic Disability option is used by holders of the proper security keys to add, edit, delete, and view a patient’s CD information created at their facility.

The DGENCD ADD/EDIT security key allows users to add and edit Catastrophic Disability Evaluations. The CD DELETE security allows users to delete Catastrophic Disability Evaluations.

CD can also be accessed from the Patient Enrollment option by entering CD from the list manager screen.

A local user can add a CD evaluation only if:

- S/he holds the DGENCD ADD/EDIT security key,
- a CD evaluation does not currently exist for this person,
- a current CD evaluation with a Method of Determination = Medical Record Review exists for this person.

A local user can delete a CD evaluation only if:

- S/he holds the CD DELETE security key.

The local user can delete or edit a local CD evaluation with the Method of Determination = Physical Exam and Catastrophically Disabled? = YES only if they answer a prompt saying they are making this change due to an entry error in the existing CD evaluation.

When CD information stored at their facility is edited or deleted, a mail message is sent to members of the DGEN ELIGIBILITY ALERT mail group.

Add/Edit/Delete Catastrophic Disability

The following is a list of the available CD option-specific and approved List Manager Actions and Mnemonics.

| Action                        | Mnemonic | Description                                                                                  |
|-----------------------------------|--------------|--------------------------------------------------------------------------------------------------|
| Add/Edit Catastrophic Disability  | AE           | Lets users who hold the DGENCD ADD/EDIT security key add a CD evaluation or edit an existing one |
| Delete Catastrophic Disability    | DE           | Lets users who hold the CD DELETE security key delete an existing CD evaluation                  |
| Actions common to all options |              |                                                                                                  |
| Next Screen                       | \+           | Go to the next page of the list                                                                  |
| Previous Screen                   | –            | Go to the previous page of the list                                                              |
| Up a Line                         | UP           | Move up one line in the list                                                                     |
| Down a Line                       | DN           | Move down one line in the list                                                                   |
| Shift View to Right               | \>           | Move the display to see to the right                                                             |
| Shift View to Left                | \<           | Move the display to see to the left                                                              |
| First Screen                      | FS           | Go to the first page of the list                                                                 |
| Last Screen                       | LS           | Go to the last page of the list                                                                  |
| Go to Page                        | GO           | Go to a particular page in the list                                                              |
| Re Display Screen                 | RD           | Clear and re-display the current screen                                                          |
| Print Screen                      | PS           | Print only the content of the current screen                                                     |
| Print List                        | PL           | Print the entire list                                                                            |
| Search List                       | SL           | Search the entire list for …                                                                     |
| Auto Display (On/Off)             | ADPL         | Turns on/off display of actions at bottom of screen                                              |
| Quit                              | Q            | Quits the Application                                                                            |

## Collateral Patient Register

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter a collateral patient into your system. A collateral patient is a non-veteran patient whose appointment is related to or associated with a veteran's treatment. The patient selected must have an eligibility code of COLLATERAL OF VET and a period of service of OTHER NON-VETERAN.

You may enter new patients as collaterals or designate patients already in your database as collaterals. If you enter a patient already in your database, the system checks data in the patient's file to determine if he/she meets the conditions which qualify him/her as a collateral patient. If the requirements are not met, a message is displayed on your screen and you will not be permitted to proceed.

You may also use this option to edit information pertaining to a collateral patient. In these cases, the existing information will be shown as defaults.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Add a Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With the installation of the Enrollment VistA Changes Release 2 (EVC R2) software (DG\*5.3\*688, IVM\*2.0\*115, and EAS\*1.0\*70), all Copay Tests added with this option are created in the FEB 2005 format.

The Add a Copay Exemption Test option is used to enter a new Copay Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Copay Test.

- the date of test cannot be before 10/29/92
- the date of test cannot be before the last date of test
- a new date of test cannot be added if one exists in the last 365 days unless it is a new calendar year

Reasons a Copay Test cannot be added:

- Patient is not a veteran.
- Patient does not have a Primary Eligibility Code.
- Patient is Service Connected 50-100%.
- Patient eligibility is NSC or SC 0% and Means Test options must be used instead of Copay options.
- Patient is receiving Aid and Attendance, automatically exempted.
- Patient is receiving Housebound Benefits, automatically exempted.
- Patient is receiving a VA Pension, automatically exempted.
- Patient is in a DOM ward, automatically exempted.
- Patient is an inpatient, automatically exempted.
- Patient was a POW, automatically exempted.
- Patient is Unemployable, automatically exempted.
- Patient is Catastrophically Disabled.

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

Copay Exemption Test User MenuAdd a Copay Exemption Test

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Copay Exemption Test User MenuAdd a Copay Exemption TestScreen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Copay Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed at least \$600 to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions which may be taken.

DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Copay Test (using the RE protocol).

ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Copay Exemption Test User MenuAdd a Copay Exemption TestScreen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/ dependents). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Copay Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

*Please note: The same rules apply to the printed 10-10EZ and 10-10EZR forms whereas the system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk as included in the Copay Test regardless of whether or not the child(ren)’s income has been marked as available to the veteran.*

The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Copay Test data has been updated by the Enrollment System Redesign application, the Total Reimbursed Medical Expenses amount and all Copay Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

You may choose to print the 10-10EZR form when the Copay Test is completed.

To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Access to this option is limited to holders of the DG MEANSTEST security key.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Copay Exempt Test Needing Update At Next Appt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Copay Exempt Test Needing Update At Next Appt. option is used to generate a listing of future appointments for a selected date range. The output will list copay exemption tests which will require updating by that appointment time.

You may select to report one/many/all divisions and one/many/all clinics. The output includes the date range, report run date, clinic name, and division. Patient name, patient ID, appointment date/time, Copay Test status, and date of last Copay Test are provided for each patient listed.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Edit an Existing Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Existing Copay Exemption Test option is used to make changes to data in existing Copay Tests. It may also be used to complete Copay Tests on patients. Only the latest Copay Test may be edited.

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit a Copay Exemption Test option operates similarly to the Add a Copay Exemption Test option; however, it is the only option which allows changes to completed Copay Tests. After these changes are entered, the system redetermines the patient's Copay status and changes it, if necessary.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Copay Exemption Test Editing Activity option.

A patient may apply for a Copay Test under the following conditions.

Copay Exemption Test User MenuEdit an Existing Copay Exemption TestAn existing Copay Exemption Test may be edited for patients who meet the following criteria:

> Applicant is a veteran

> Applicant's primary or other eligibility does NOT contain:

> \- service connected 50% to 100% or

> \- aid and attendance or

> \- housebound or

> \- VA pension

> Primary eligibility is NSC and a Means Test is not required

> Applicants who have answered NO to receiving A&A, HB, or pension

- Applicants who have NOT answered YES to Veteran Catastrophically Disabled?

> Applicants, who have previously qualified and applied for a Copay exemption, still qualify, and have NOT been Copay Tested in the past year

Should these criteria change, a Copay Test status of NO LONGER APPLICABLE will be assigned to the Copay Test. Tests with this status CANNOT be edited.

The following is a brief explanation of some of the actions which may be taken on Screen 1 - Marital Status/Dependents.

DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Copay Test (using the RE protocol).

ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). <u>It may also used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).</u>

Depending on the information entered on Screen 1, Screen 2 may appear with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

You may print the 10-10EZR form when the Copay Test is complete.

To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Copay Exemption Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

- Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “*3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.*” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Social Security (Not SSI) +
  - \[2\] U.S. Civil Service +
  - \[3\] U.S. Railroad Retirement +
  - \[4\] Military Retirement +
  - \[5\] Unemployment Compensation +
  - \[6\] Other Retirement +
  - \[8\] Interest, Dividend, Annuity +
  - \[9\] Worker’s Comp or Black Lung
- Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “*1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Cash, Amts in Bank Accts +
  - \[2\] Stocks and Bonds

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

- Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “*3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[4\] Other Property or Assets –
  - \[5\] Debts

You may not edit or delete a Copay Exemption Test that was created at another VAMC and distributed by the HEC.

Access to this option is limited to holders of the DG MEANSTEST security key.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List Incomplete Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Incomplete Copay Exemption Test option is used to generate a listing of patients who have an incomplete Copay Test on file. The patient name, patient ID number, source of test, and date of test are provided. The patients are listed in alphabetical order on the output.

You will be prompted for the Copay Test status, a date range, and a device.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## View a Past Copay Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View a Past Copay Test option is used to view past Copay Tests data. The option does not allow editing. You will be prompted for the patient's name and the date of the Copay Test you wish to view. A question mark (?) entered at the date prompt will provide you with a list of the selected patient's Copay Test dates.

If certain circumstances exist for the selected patient, messages may be displayed. A message will be printed if no detailed income information is on file for the veteran, or if the veteran's Copay Test status is NO LONGER APPLICABLE. Since income data can be entered/edited through registration, once a Copay Test has this status, the income data being viewed may differ from that originally entered as part of the Copay Test.

You will be able to view the following three Copay Test screens through this option.

Screen 1 - Marital Status/Dependents

Screen 2 - Previous Calendar Year Gross Income

Screen 3 - Deductible Expenses

## Death Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Death Entry option is used to enter, edit, or delete date of death information for a patient. If you attempt to enter an inpatient, you will be prompted to discharge the patient through the Bed Control Menu. You must hold the DG DETAIL security key in order to access this option.

When a date of death is entered or updated, the system prompts you to provide the source of notification for the date of death. Once the date of death and the source of notification for the date of death have been entered, the software records the date of last entry or update on the DATE OF DEATH field and information about the local submitter (user) making the entry or change.

The date of death must be precise, cannot be prior to the P&T date (if a P&T date is on file), cannot be prior to the Date Ruled Incompetent (VA) (if one is on file) and cannot be prior to the Date Ruled Incompetent (Civil) (if one is on file).

When a veteran's Enrollment Status is DECEASED and there is no date of death on file in V*ist*A, a message displays asking you to either add the date of death information or contact the HEC to remove an incorrect date of death.

Once a date of death has been entered into the system, the message "\[PATIENT DIED ON {date}\] PATIENT HAS DIED" will be displayed whenever the patient's name is entered through other options.

You can use this option to delete a date of death entered in error by entering “@” at the “DATE OF DEATH: \[date\]//” prompt, and responding “Yes” when asked, “SURE YOU WANT TO DELETE?” This will delete the entries for the specified patient in the DATE OF DEATH (#.351), DEATH ENTERED BY (#.352), and SOURCE OF NOTIFICATION (#.353) fields of the PATIENT (#2) file. It will update the DATE OF DEATH LAST UPDATED (#.354) field with the date and time the date of death was deleted. It will update the LAST EDITED BY (#.354) field with the User ID of the user who deleted the date of death.

When you enter, edit, or delete a date of death through this option, a MailMan message is sent to members of the DGEN ELIGIBILITY ALERT mail group to notifying them of future clinic appointments and/or scheduled admissions for the patient. It will also include source of notification for date of death, date of last entry or update, and local submitter/user information. Future admissions will automatically be cancelled but clinic appointments must be cancelled through the appropriate Scheduling option. When the date of death is the same as the discharge date, the mail message will indicate that the patient died while an inpatient.

## Delete a Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete a Registration option is used to delete patient registrations that have not been dispositioned.

When a registration is deleted using this option, all information on the selected patient remains on file. The system only removes record of the patient being registered on that particular date.

You may enter double question marks (??) at the "PATIENT NAME" prompt to obtain a list of patients with open registrations. Once the patient name is entered, information concerning the undispositioned registration is displayed.

## Disposition Log Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disposition Log Edit option is used to edit the disposition record of a patient registration.

The system displays each data field of the disposition record for editing. The values that were entered at the time of registration and disposition will appear as defaults. You may accept the default or enter new information. Based on the information entered/edited through this option, the system will recategorize the registration in the appropriate AMIS 401-420 segment.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may be displayed with V. 2.5 of Order Entry/Results Reporting. The disposition must have a change in status from APPOINTMENT W/O EXAM to 10/10 or UNSCHEDULED in order for a notification to be displayed. The notification will only be displayed for patients who are defined in an OE/RR LIST entry and will only be displayed to users defined in that list entry. Please refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

The validation logic performs the same validation checks as the Austin database to identify errors before they are transmitted. The validator (or edit checker) will review the entire encounter rather than stopping after the first error is found. You may be given the opportunity to correct these errors through this option.

You will be prompted to indicate if treatment was related to Military Sexual Trauma (MST) only if the patient’s MST Status is YES.

## Edit Inconsistent Data for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit data for patients who have been identified as having missing/inconsistent data in their files through the use of the Consistency Checker. The data items will be displayed for updating. If you do not hold the DG ELIGIBILITY security key, you will not be able to edit certain data items. Those items will appear followed by an asterisk(\*). Items which are displayed with two asterisks (\*\*) can only be updated using the appropriate PIMS menu options. When updating is complete, the system will again search the patient's file for any remaining inconsistent/unspecified data items.

The Consistency Checker feature provides a method of better assuring accuracy of the data contained in patients' records. It will look at data items to assure entries are consistent with entries in other data fields. It will also check certain data items to be sure they have not been left blank. Your site may choose whether or not to use this feature by setting the CONSISTENCY CHECKER field in the MAS Parameter Entry/Edit option. Further, your site may specify from a list of data items, those which it wishes the Consistency Checker to check. Some items, however, are automatically set by the PIMS software to be checked/not checked. Specifying the data elements is accomplished through the Determine Inconsistencies to Check/Don't Check option. If your site has the Consistency Checker turned OFF, you will not be able to fully utilize this option.

Each of the inconsistent/unspecified data elements will be prompted for updating. Please refer to the Registration Supplement if you need assistance in answering these prompts. At the conclusion of updating, the consistency checker will run once again to check for any remaining inconsistent/unspecified data elements.

The Consistency Checker places the names of those patients whose records contain inconsistent/unspecified data in the INCONSISTENT DATA file (#38.5). When the data is corrected through this option, the names are automatically removed from the file. Names contained in this file will appear on the Inconsistent Data Elements Report.

Edit Inconsistent Data for a Patient

Although the process of updating the INCONSISTENT DATA file is automatic when using this option, it is not automatic when data is entered/edited through other PIMS options (except options which utilize the load/edit registration screens). Three options found on the Inconsistency Supervisor Menu of the Supervisor ADT menu are dedicated to keeping the INCONSISTENT DATA file up to date for such records. It is important to note that entries in the INCONSISTENT DATA file may not be accurate. Inconsistent data can be updated through options which do not involve the Consistency Checker (i.e., FileMan). By using the options available on the Inconsistency Supervisor Menu, the INCONSISTENT DATA file can be kept up to date.

Whenever inconsistent/unspecified data items remain in a patient's file, either by selecting not to edit it or not holding the DG ELIGIBILITY key, a MailMan message will be generated. This message will be sent to the Inconsistency Edit mail group specified through the Bulletin Selection option. There are three possible messages which may be sent; an initial message when inconsistencies are first found, a reminder message if inconsistencies were reported more than seven days ago and some remain unresolved, and an updated message if inconsistencies have previously been reported (and not updated) and additional inconsistencies have been found. If an initial MailMan message has been sent within the past seven days and no new inconsistencies have been found, no MailMan message will be sent.

## Eligibility Inquiry for Patient Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility Inquiry for Patient Billing option provides a quick reference to patient information used in determining appropriate patient billing. The output may display the following elements, where applicable.

- Means Test - status and date last Means Test performed
- health insurance - insurance company, policy number, group number, holder
- agent orange and ionizing radiation exposure
- Medicaid eligibility
- primary and other eligibility codes
- service-connected percentage
- rated disabilities

Once the patient name is entered, the output is automatically displayed.

## Eligibility Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility Verification option is used to enter/edit/verify data pertaining to a patient's rated disabilities and service record. It allows for entry, edit, and viewing of the following registration screens, as applicable, according to site parameters set up by PATIENT TYPE.

PATIENT DEMOGRAPHIC DATA - 1

ADDITIONAL PATIENT DEMOGRAPHIC DATA 1.1

PATIENT DATA - 2

MILITARY SERVICE DATA - 6

ELIGIBILITY STATUS DATA - 7

FAMILY DEMOGRAPHIC DATA - 8

INCOME SCREENING DATA - 9

INELIGIBLE/MISSING DATA - 10

ELIGIBILITY VERIFICATION DATA - 11

Entry/edit of most of the data in this option is restricted to holders of the DG ELIGIBILITY security key once eligibility has been verified. Until it has been verified, it may be entered/edited by any user; after verification, all users may view but only those with the security key may edit. Verification of data takes place through the ELIGIBILITY VERIFICATION DATA (Screen 11) and must be accomplished by a holder of the DG ELIGIBILITY security key.

This option works in the same manner as the Register a Patient and Load/Edit Patient Data options. A patient name is entered, and the various screens appropriate for that patient are presented. Registration screens 1, 1.1, 2, and 7 will always be displayed. The display of screens 6, and 8 through 11 will vary depending on PATIENT TYPE. This is due to your site's ability to turn these screens OFF and ON during the registration process depending upon whether the information collected through them is pertinent to the PATIENT TYPE. If necessary, you may refer to the Registration Supplement for further explanation of this function.

You may edit the data shown on the screens by selecting the number(s) of the data group(s) you wish to edit; move to another screen by entering up-arrow screen number \<^#\> to specify the screen; move to the next screen by entering a \<RET\>; or quit by entering an up-arrow \<^\>. Should you select to enter/edit data, each appropriate field of the data group selected will be prompted. Any previously entered data will be shown as a default. When editing is complete, the screen will be redisplayed with the newly entered data shown.

Eligibility Verification

If your site has the Consistency Checker function turned ON, the system will perform a check for inconsistent/unspecified data elements at the conclusion of the verification process. If any inconsistent/unspecified data elements are found, you will be given the opportunity to make the necessary corrections. If the Consistency Checker is not turned ON, the message "CONSISTENCY CHECKER TURNED OFF!!" will appear at the conclusion of the process.

## <u> </u>Enter/Edit Patient Security Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Patient Security Level option is used to assign/remove a level of sensitivity to a patient record. Use of this option enters the patient into the DG SECURITY LOG file. Any access of a sensitive patient record is tracked in this file. The DG SECURITY LOG file also contains the name of the person who assigned the security and when the security was assigned.

With the initialization of ADT V. 3.6, all existing patients with an eligibility code of employee were automatically entered into the security log as sensitive by the system. This is not automatic for employee patients subsequently entered into the system.

Accessing a sensitive patient record can trigger different messages and bulletins to be sent.

Only holders of the DG SENSITIVITY security key may access this option.

## Invalid State/Inactive County Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create a report that lists patient records whose address fields contain invalid states and/or inactive counties according to the following criteria.

- A state is considered invalid, and will appear on the report, if the AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No”

> OR

> The first character of the state name is “Z”.

- A county is considered inactive, and will appear on the report, if it has a date in the INACTIVE DATE field (#5) in the COUNTY sub-file (#5.01) of the STATE file (#5)

> OR

> The county is in a state whose AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No”.

- An address is considered a US or US Possession if the US STATE OR POSSESSION field (#2.2) in the STATE file (#5) is set to “Yes”.
- An address is considered foreign if the US STATE OR POSSESSION field (#2.2) is set to “No” or blank.

> NOTE: Even if the address is considered foreign, it will appear on the report *only if* the AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No” for that particular entry.

If you run the report for the purpose of resolving the discrepancies it will display, be sure to use the appropriate resources to verify the correctness of the changes you wish to make. Edit the fields in the PATIENT file (#2) by using the Load/Edit Patient Data option on the Registration Menu. This report may take a long time to generate; you should queue it to print at a later time.

PATIENT file (#2) fields reported at your site as containing incorrect state data should be edited only to states recognized by the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). PATIENT file (#2) fields reported as containing inactive counties should be edited only to counties that have no inactive date and are connected to states that are recognized by the AITC.

Invalid State/Inactive County Report

You can choose to run the report for U.S. and U.S. Possessions Only, Foreign Addresses Only, or Both. If you choose “Both”, you will receive outputs for *both* U.S. and U.S. Possessions Only *and* Foreign Addresses Only. Each time you run the report, you will receive a VA MailMan message containing summary data. The report includes the following information for all output criteria:

- Report title (“Report of States Not Recognized by AAC and Inactive Counties”)
- Report subtitle (“U.S. and U.S. Possessions Only” and/or “Foreign Addresses Only”)
- Page number(s)
- Patient Name
- Patient SSN
- Field\*
- State/County

\*The “Field” column in the report may include data in one or more of the fields from the PATIENT file (#2) listed in the tables below.

*For US and US Possessions Only*

| Field Number | Field Name                   | Appears on the Report as  |
|------------------|----------------------------------|-------------------------------|
| .093             | PLACE OF BIRTH \[STATE\]         | Place of Birth                |
| .115             | STATE                            | Permanent Address - State     |
| .117             | COUNTY                           | Permanent Address - County    |
| .1215            | TEMPORARY STATE                  | Temporary Address - State     |
| .12111           | TEMPORARY COUNTY                 | Temporary Address - County    |
| .1415            | CONFIDENTIAL ADDRESS STATE       | Confidential Address - State  |
| .14111           | CONFIDENTIAL ADDRESS COUNTY      | Confidential Address - County |
| .1654            | INELIGIBLE TWX STATE             | Ineligible TWX                |
| .1659            | MISSING PERSON TWX STATE Missing | Person TWX                    |
| .217             | K-STATE                          | Next of Kin                   |
| .2197            | K2-STATE                         | Next of Kin 2                 |
| .256             | SPOUSE'S EMPLOYER'S STATE        | Spouse's Employer             |
| .2917            | STATE (VA)                       | VA Guardian                   |
| .2927            | STATE (CIVIL)                    | Civil Guardian                |
| .3117            | EMPLOYER STATE                   | Employer                      |
| .3317            | E2-STATE                         | Emergency Contact 2           |
| .337             | E-STATE                          | Emergency Contact             |
| .347             | D-STATE                          | Designee                      |
| 2.06             | INS TYPE-EMPLOYER CLAIMS STATE   | Insurance Type - Emp Claims   |
| 3.09             | INS TYPE-INSURED'S STATE         | Insurance Type - Insured's    |
| 13               | INS TYPE-AGENT'S STATE           | Insurance Type - Agent's      |
| 35               | INS TYPE-A-STATE                 | Attorney                      |

Invalid State/Inactive County Report

*For Foreign Addresses Only*

| Field Number | Field Name                 | Appears on the Report as     |
|--------------|----------------------------|------------------------------|
| .115         | STATE                      | Permanent Address - State    |
| .1215        | TEMPORARY STATE            | Temporary Address - State    |
| .1415        | CONFIDENTIAL ADDRESS STATE | Confidential Address - State |

## Load/Edit Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Load/Edit Patient Data option is used to enter, edit, and view information contained in a patient's record without making a registration entry in the Disposition Log or creating a 10/10 Form (Application for Health Benefits). You may also make HINQ inquiries and print patient data cards. New patient records may be entered into the system or the records of existing patients may be edited. You may wish to use it to enter new patients into your database for whom applicable information has been mailed to your facility for actual registration at a future date.

After you select this option, patient demographic, enrollment, eligibility, and emergency response indicator(s) information is displayed. If the patient is deceased, date of death information (including source of notification for date of death, date of last entry or update, and local submitter/user information) is also displayed. The date of death information is READ ONLY.

If the user chooses not to upload the date of death from the HEC, a mail message is sent to the members of the DGEN ELIGIBILITY ALERT mail group telling them to contact the HEC to explain why they did not accept the date of death.

When a veteran's Enrollment Status is deceased and there is no date of death on file in VistA, a message displays asking the user to either add the date of death information or contact the HEC to remove an incorrect date of death.

Prior to entering patient data, the permanent address is displayed and the user is asked, “<u>Do you want to edit the Patient's Address?</u>”.

- If the user answers YES, the system will prompt each address field and the user will be allowed to update the patient’s permanent address information. The old and the new address information is displayed and the system will ask the user “<u>Are you sure that you want to save the above changes?</u>”
  - If the user answers YES, the system displays “Change saved”, the patient’s permanent address change date/time stamp will be updated, and a trigger is set to send a message to the HEC.

> *Please note: It takes a actual change to the permanent address to update the permanent address change date/time stamp. If there were no changes to the permanent address information, and the user responds YES; no updates are made to the permanent address fields or permanent address change date/time stamp and a message is <u>NOT</u> triggered to the HEC.*

- If the user answers NO, the system displays “Change aborted”. Neither the patient’s permanent address information nor the permanent address change date/time stamp is updated and a message is <u>NOT</u> triggered to the HEC.
- If the user answers NO at the “<u>Do you want to edit the Patient's Address?</u>” prompt, the system will not prompt the user for address information and the system will continue the Load/Edit Patient Data process.

Load/Edit Patient Data

Entry/edit of a patient's record is done via a series of formatted data screens. There are a total of fifteen screens distributed with the PIMS Package. Screens 12-14 are informational only. The enter/edit process will not be the same for every patient, nor for every user due to several variables which exist in the system. Your site has the ability to create its own additional screen in order to capture certain information it may need or to capture information in a different format. It has the ability to turn certain data screens ON and OFF according to Patient Type. Within the screens, it may specify which data groups may be entered/edited. The DG ELIGIBILITY security key also plays a role in your ability to enter/edit data. Depending upon whether eligibility has been verified, certain information may only be edited by a user holding this security key.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields have been established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert will be displayed. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields will display an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts will remain on file for one year.

The HIGH INTENSITY field in the MAS Parameters has been provided to assist you in the identification of those fields which may/may not be edited. If this field has been set to YES at your facility, the number next to those data groups which may be edited will be in boldface type; those which are uneditable will not (excluding Screen 8). For those sites not using High Intensity, numbers of data groups which may be edited will be enclosed in \[ \]s, while those which are uneditable will be enclosed in \< \>s (excluding Screen 8).

The Registration Supplement provides an example of each data screen and a description of each associated field. Please refer to this Supplement when entering or editing patient information.

If your site has the Consistency Checker function turned ON, the system will perform a check for inconsistent/unspecified data elements at the conclusion of the entry/edit process. If any inconsistent/unspecified data elements are found, you will be given the opportunity to make the necessary corrections.

Load/Edit Patient Data

The system will also determine a patient’s need for Means Testing and Copay Testing and, if necessary, allow you to complete the required test. For the Copay Test, the veteran has to request the test be completed. For instructions on Means Test, see the Add a New Means Test or Complete a Required Means Test options. For instructions on Copay Test, see the Add a New Copay Test option.

Screen 8 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. The following is a brief explanation of some of the actions listed on this screen.

DD - In order to edit the dependent demographics, the selected dependent has to be active.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Means Test.

ED - Expand Dependent will move to another screen. It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

MT - Used to enter/edit last year's marital status for the veteran.

AD - This protocol is not selectable from the registration screens.

RE - This protocol is not selectable from the registration screens.

With the installation of the Veteran Identification Card (VIC) software, the prompt “Download VIC data?” has been added which allows you to download the selected patient’s demographic data to the photo capture station. The existing “EMBOSS DATA CARD?” prompt has been changed to “EMBOSS (OLD) DATA CARD?”.

Catastrophically Disabled Review Date displays after patient demographic and eligibility data.

Load/Edit Patient Data

A query is automatically sent to the Health Eligibility Center (HEC) when this option is utilized. This query will determine if a Means Test or Copay Exemption Test (with Income Screening information) has been completed for the veteran for a specified income year. The HEC will process the query, and if there is a completed Means Test or Copay Exemption Test (with Income Screening information), the HEC will transmit the Primary test and any Hardship determinations to the VAMC that sent the query.

The veteran’s Long Term Care (LTC) copayment status and last test date will be displayed when using this option. If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” will be displayed. If the veteran did not agree to pay the copayments, the following ineligible message will be displayed.

Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Add a New Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With the installation of the Enrollment VistA Changes Release 2 (EVC R2) software (DG\*5.3\*688, IVM\*2.0\*115, and EAS\*1.0\*70), all Means Tests added with this option are created in the FEB 2005 format.

The Add a New Means Test option is used to enter a new Means Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Means Test.

the date of test cannot be before 7/1/86

the date of test cannot be before the last date of test

a new date of test cannot be added if one exists in the last 365 days unless it is a new calendar year

Reasons a Copay Test cannot be added:

- primary eligibility is NOT NSC or 0% service-connected non-compensable
- receives disability retirement from the military
- is eligible for Medicaid
- is on a domiciliary ward
- has been Means Tested in the past year
- is a Purple Heart recipient
- is Catastrophically Disabled

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

Determines the appropriate Means Test status for the patient

Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

Bypasses the means test screens

Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment

Means Test User MenuAdd a New Means Test

Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If it is necessary to refer the case to adjudication, the system will prompt “Do you wish to send this case to adjudication?”. If YES is entered, the veteran will be placed in MT Copay Required status until determination is returned from adjudication. If NO is entered, the system makes the final determination that the veteran is MT Copay Required.

Means Test User MenuAdd a New Means Test

If the veteran's Means Test status is PENDING ADJUDICATION, he/she is tentatively placed in MT Copay Required status and must agree to pay the deductible.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Screen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed at least \$600 to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions which may be taken.

DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Means Test (using the RE protocol).

Means Test User MenuAdd a New Means Test

ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).

It may also used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Screen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Means Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

*Please note: The same rules apply to the printed 10-10EZR and 10-10EZ forms whereas the system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk as included in the Means Test regardless of whether or not the child(ren)’s income has been marked as available to the veteran.*

The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data has been updated by the Enrollment System Redesign application, the Total Reimbursed Medical Expenses amount and all Means Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

Means Test User MenuAdd a New Means TestScreen4-PreviousCalendarYearNetWorth is used to enter such information as stocks and bonds, real property, bank accounts, and debts. Depending on the information entered on Screen 1, this screen may appear with one column (veteran) or up to three columns (veteran/spouse/dependent children). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Means Test, the system will display the Spouse and/or Dependent Child(ren) column on the screen. If they have not been marked (no asterisk), it will not display. The same rules apply to the printed 10-10EZ and 10-10EZR forms whereas the system will not print the Previous Calendar Year Net Worth amount~~s~~ for the Spouse and/or Dependent Children when they have not been marked with an asterisk as included in the Means Test.

The item number(s) you select for editing may be preceded by V (veteran) or S (spouse) or C (Children) to select those specific fields; otherwise, the fields for all will be displayed. The required information will be prompted for each column shown.

When adding a Means Test, completion of the test is optional; however, the marital and dependent children sections must be completed in order to complete the Means Test. For MT Copay Exempt veterans, the net worth must also be entered. If you choose not to complete the Means Test, it may be completed later through either the Complete a Required Means Test or Edit an Existing Means Test options.

You may choose to print the 10-10EZR form when the Means Test is completed or print the prior Means Test (if one exists) at the beginning of the option.

*Please note: To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.*

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Adjudicate a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Adjudicate a Means Test option is used to enter the patient's Means Test category into the system when the determination is returned from Adjudication. Only patients who currently have the Means Test status of PENDING ADJUDICATION and less than 1 year old from the means test effective date may be selected.

A patient's Means Test may be referred to Adjudication for Means Test Category determination when income alone places the veteran in MT Copay Exempt status, but income plus net worth (property) is equal to or greater than the allowable threshold.

If a change is made which involves the MT Copay Required Means Test status, a bulletin may be generated informing the user and advising review of the MT Copay Required charges for the selected patient.

Access to this option is limited to holders of the DG MEANSTEST security key.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Complete a Required Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Complete a Required Means Test option is used to complete Means Tests generated through registration or by other circumstances. Only Means Test records with a status of REQUIRED and less than 1 year old from the effective date may be completed.

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

Determines the appropriate Means Test status for the patient

Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

Bypasses the means test screens

Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment

Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If it is necessary to refer the case to adjudication, the system will prompt “Do you wish to send this case to adjudication?”. If YES is entered, the veteran will be placed in MT Copay Required status until determination is returned from adjudication. If NO is entered, the system makes the final determination that the veteran is MT Copay Required.

If the veteran's Means Test status is PENDING ADJUDICATION, he/she is tentatively placed in MT Copay Required status and must agree to pay the deductible. If the veteran does not agree to pay the deductible, a message is printed in the signature block for the deductible on the 10-10EZ.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Means Test User MenuComplete a Required Means TestScreen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran during the last calendar year or, if they did not live together, the veteran contributed at least \$600 to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Means Test (using the RE protocol).

ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Means Test User MenuComplete a Required Means TestScreen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from the information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) have been marked as being included in the Means Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

*Please note: The same rules apply to the printed 10-10EZR and 10-10EZ forms whereas the system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk as included in the Means Test regardless of whether or not the child(ren)’s income has been marked as available to the veteran.*

The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed. The required information will be prompted for each column shown.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income available.

The Gross Medical Expenses amount (Before FEB 2005 format) or Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable only by the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data has been updated by the Enrollment System Redesign (ESR) application, the Gross Medical Expenses amount or Total Non-Reimbursed Medical Expenses amount and all Means Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

Means Test User MenuComplete a Required Means Test

For Means Tests done prior to the existence of the Gross Medical Expenses amount, the system <u>will re-calculate and present the Gross Medical Expenses amount from the patient’s existing Medical Expenses amount</u>. <u>For these historical Means Tests, the existing Medical Expenses amount becomes the Adjusted Medical Expenses amount.</u> And, if and when the Gross Medical Expenses amount is updated, the system will automatically re-calculate the Adjusted Medical Expenses amount.

Screen4-PreviousCalendarYearNetWorth is used to enter such information as stocks and bonds, real property, bank accounts, and debts. Depending on the information entered on Screen 1, this screen may appear with one column (veteran) or up to three columns (veteran/spouse/dependent children). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Means Test, the system will display the Spouse and/or Dependent Child(ren) column on the screen. If they have not been marked (no asterisk), it will not display. The same rules apply to the printed 10-10EZ and 10-10EZR forms whereas the system will not print the Previous Calendar Year Net Worth amount~~s~~ for the Spouse and/or Dependent Children when they have not been marked with an asterisk as included in the Means Test.

*Please note: The Previous Calendar Year Net Worth screen (Before FEB 2005 format) does not support the entry of separate Dependent Child(ren) net worth dollar amounts (i.e., have a column for Children). Consequently, a negative Income Available response does not affect the display or printing of the Net Worth dollar amounts on the printed 10-10EZ/EZR forms.*

> *Any Means Test data collected from a mailed registration form or during a walk-in/face-to-face presentation of a veteran for Dependent Child(ren) Net Worth is manually added into the Veteran amounts and entered as a totaled dollar amount.*

> *Any Means Test data collected from an on-line submission of a 10-10EZ application of a veteran for Dependent Child(ren) Net Worth is automatically added into the Veteran totaled Net Worth amounts by the EAS software.*

The item number(s) you select for editing may be preceded by V (veteran), S (spouse) and C (children) to select those specific fields; otherwise, the fields for all will be displayed. The required information will be prompted for each column shown.

Means Test User MenuComplete a Required Means Test

Completion of the Means Test through this option is mandatory. The Means Test status will automatically be updated once editing is complete.

You may choose to print the 10-10EZR form when the Means Test is completed.

*Please note: To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.*

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

- Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social
- Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Social Security (Not SSI) +
  - \[2\] U.S. Civil Service +
  - \[3\] U.S. Railroad Retirement +
  - \[4\] Military Retirement +
  - \[5\] Unemployment Compensation +
  - \[6\] Other Retirement +
  - \[8\] Interest, Dividend, Annuity +
  - \[9\] Worker’s Comp or Black Lung
- Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Cash, Amts in Bank Accts +
  - \[2\] Stocks and Bonds

Means Test User MenuComplete a Required Means Test

- Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[4\] Other Property or Assets –
  - \[5\] Debts

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Document Comments on a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Document Comments on a Means Test option is used to add/edit/delete comments to an existing Means Test. This allows the user to enter any pertinent information concerning the selected Means Test such as efforts made to obtain Means Test information.

You will be prompted for the patient name and the Means Test date. The latest Means Test date will appear as the default. A question mark (?) may be entered to obtain a list of Means Test dates for that patient. Comments may then be added through a word-processing field. Existing comments can be edited or deleted.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Edit an Existing Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Existing Means Test option is used to make changes to data in existing Means Tests less than 1 year old from the effective date. It may also be used to complete Means Tests on patients identified through Registration as requiring Means Testing. Only the latest Means Test may be edited. A Means Test that has been verified by the HEC and its corresponding original VAMC Means Test are both uneditable. If you choose such a Means Test, the system will display a message containing this information. However, this option will let you view or print such a test.

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

Determines the appropriate Means Test status for the patient

Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

Bypasses the means test screens

Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment

Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit an Existing Means Test option operates similarly to the Add a New Means Test and Complete a Required Means Test options; however, it is the only option which allows changes to completed Means Tests. After these changes are entered, the system redetermines the patient's Means Test category and changes it, if necessary. If additional information is needed to make a determination or if it is necessary to refer the case to adjudication, the system prompts accordingly.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Means Test Editing Activity option.

Means Test User MenuEdit an Existing Means Test

A Means Test is required under the following conditions.

- primary eligibility is NSC or 0% service-connected non-compensable
- does not receive disability retirement from the military
- is not eligible for Medicaid
- is not on a domiciliary ward
- has not been Means Tested in the past year
- is NOT a Purple Heart recipient
- is NOT catastrophically disabled

Should these criteria change (excluding the last two), a Means Test status of NO LONGER REQUIRED will be assigned to the Means Test. Tests with this status cannot be edited.

Depending on the information entered on Screen 1, Screen 2 may appear with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen 4 may appear with one or two columns (Before FEB 2005 format) or three columns (FEB 2005 format). The item number(s) you select for editing may be preceded by V (veteran) or S (spouse) or C (children) to select those specific fields; otherwise, the fields for all will be displayed. The required information will be prompted for each column shown.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

You may print the 10-10EZR form when the Means Test is complete.

*Please note: To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.*

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

Means Test User MenuEdit an Existing Means Test

- Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Social Security (Not SSI) +
  - \[2\] U.S. Civil Service +
  - \[3\] U.S. Railroad Retirement +
  - \[4\] Military Retirement +
  - \[5\] Unemployment Compensation +
  - \[6\] Other Retirement +
  - \[8\] Interest, Dividend, Annuity +
  - \[9\] Worker’s Comp or Black Lung
- Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[1\] Cash, Amts in Bank Accts +
  - \[2\] Stocks and Bonds
- Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
  - \[4\] Other Property or Assets –
  - \[5\] Debts

Access to this option is limited to holders of the DG MEANSTEST security key.

Means Test User MenuEdit an Existing Means TestHow to Correct Means Test Inconsistency Errors

There are two types of conditions that cause the inconsistency messages:

1.  Data entry omissions or mistakes (error numbers 1-4 in Table 1)
2.  Erroneous or corrupted data filed in the records (error numbers 5-17 in Table 2)

IMPORTANT NOTE: Only the Primary site for the Means Test can correct the inconsistent data.

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
<td>Data values in the SOCIAL SECURITY NUMBER field (#.09) in the INCOME PERSON file (#408.13) for at least two dependents are identical.</td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to check the SSN for each of the dependents listed on the test.</p>
<p>3. Update the invalid SSN for the dependent who generated the inconsistency message.</p>
<p>4. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

Means Test User MenuEdit an Existing Means Test

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 38%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th>3. Shouldn't have income data if Child Had Income is NO</th>
<th><ul>
<li><blockquote>
<p>The dependent is not the spouse, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>The INCOME AVAILABLE TO YOU field (#.12) in the INCOME RELATION file (#408.22) is No, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>Any of the income or net worth fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the dependent contain any amount. (Any entry including a zero [$0] is a valid amount.)</p>
</blockquote></li>
</ul>
<p>When the INCOME AVAILABLE TO YOU field (#.12) is set to No, and there are income and net worth entries for the dependent, the amounts are not visible on either the INCOME or NET WORTH screens.</p></th>
<th><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field to YES.</p>
<p>3. Go to the GROSS INCOME (#2) and NET WORTH (#4) screens and delete the amounts entered for the dependent.</p>
<p>4. Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1); use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field (#.12) back to NO.</p>
<p>5. Re-complete the test.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4. No income data allowed if spouse didn't live w/vet &amp; amt contributed &lt;$600</td>
<td><ul>
<li><blockquote>
<p>The data value in the INCOME RELATION file (#408.22) LIVED WITH PATIENT field (#.06) is "NO", and</p>
</blockquote></li>
<li><blockquote>
<p>The AMOUNT CONTRIBUTED TO SPOUSE field (#.07) is less than $600, and</p>
</blockquote></li>
<li><blockquote>
<p>Any of the income or net worth fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the spouse contain any amount. Any entry including a zero ($0) is a valid amount.</p>
</blockquote></li>
</ul>
<p>When the LIVED WITH PATIENT field is set to No, and the AMOUNT CONTRIBUTED TO SPOUSE field is less than $600, and there are income and net worth entries for the dependent, the amounts are not visible on either the INCOME or NET WORTH screens.</p></td>
<td><p>1. Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p>
<p>2. From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to YES.</p>
<p>3. Go to the GROSS INCOME (#2) and NET WORTH (#4) screens and delete the amounts entered for the spouse.</p>
<p>4. Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1) and use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to NO.</p>
<p>5. Re-complete the test.</p></td>
</tr>
</tbody>
</table>

Means Test User MenuEdit an Existing Means TestTable 2 - Inconsistency Messages Caused by Erroneous or Corrupted Data

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
<td><p>1. From the Means Test User Menu, use the Hardships option to edit the veteran's record on the Hardship Determinations Screen (#1).</p>
<p>2. Use the Edit Hardship (EH) action to enter the missing data.</p></td>
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
<td><p>1. From the Means Test User Menu, use the Hardships option to edit the veteran's record on the Hardship Determinations Screen (#1).</p>
<p>2. Use the Edit Hardship (EH) action to enter the missing data.</p></td>
</tr>
</tbody>
</table>

Means Test User MenuEdit an Existing Means Test

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>7. Missing Hardship Effective Date</th>
<th><ul>
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
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></th>
<th><p>1. From the Means Test User Menu, use the Hardships option to edit the veteran's record on the Hardship Determinations Screen (#1).</p>
<p>2. Use the Edit Hardship (EH) action to enter the missing data.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8. Invalid Hardship Effective Date</td>
<td><ul>
<li><blockquote>
<p>The date in the HARDSHIP EFFECTIVE DATE field (#2.01) could not be converted into FileMan format, <strong>and</strong></p>
</blockquote></li>
<li><blockquote>
<p>At least one of the other Hardship-related fields contains data.</p>
</blockquote></li>
</ul></td>
<td><p>1. From the Means Test User Menu, use the Hardships option to edit the veteran's record on the Hardship Determinations Screen (#1).</p>
<p>2. Use the Edit Hardship (EH) action to either enter (if NULL) or re-enter the HARDSHIP EFFECTIVE DATE.</p></td>
</tr>
<tr class="even">
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
<td><p>1. From the Means Test User Menu, use the Hardships option to edit the veteran's record on the Hardship Determinations Screen (#1).</p>
<p>2. Use the Edit Hardship (EH) action to enter a date for the HARDSHIP EFFECTIVE DATE that is no earlier than the effective date of the Means Test.</p>
<p>3. At least one of the other hardship-related fields (HARDSHIP?, SITE GRANTING HARDSHIP, or HARDSHIP EFFECTIVE DATE) is also missing and must be entered to remove this inconsistency.</p></td>
</tr>
</tbody>
</table>

Means Test User MenuEdit an Existing Means Test

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>10. Source of Test must be identified</th>
<th><p>The SOURCE OF INCOME TEST field (#.23) in the ANNUAL MEANS TEST file (#408.31) does <strong>not</strong> contain one of the following values found in the SOURCE OF INCOME TEST file (#408.34):</p>
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
</ul></th>
<th><p>1. From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11. Site Conducting Test must be identified</td>
<td>The SITE CONDUCTING TEST field (#2.05) in the ANNUAL MEANS TEST file (#408.31) is NULL <strong>and</strong> the SOURCE OF INCOME TEST field (#.23) is OTHER FACILITY.</td>
<td>The means test can only be corrected at the site where it was entered/completed.</td>
</tr>
<tr class="even">
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
<tr class="odd">
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
<tr class="even">
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

  
Means Test User MenuEdit an Existing Means Test

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 39%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>15. Copay Test Status should be &lt;calculated status&gt;</th>
<th>The Copay Exemption Status is calculated based on income and net worth, then compared to the TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31). This message is returned when the calculated status does not equal the TEST-DETERMINED STATUS.</th>
<th><p>1. From the Copay Exemption Test Menu, use the Edit an Existing Copay Exemption Test option to view the data on each of the Income Test screens.</p>
<p>2. Press &lt;Enter&gt;.</p>
<p>3. Re-complete the test.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<tr class="even">
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

## GMT Thresholds Lookup by ZIP Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, former President Bush signed into law H.R. 3477, The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001. Section 202 of this Act requires the implementation of U.S. Department of Housing and Urban Development (HUD) Indices to determine geographic income thresholds in support of more discrete Means Testing. A new GMT copayment status identifies veterans who qualify for a reduced inpatient copayment rate. The effective date of the regulation to support this legislation is October 1, 2002. Like traditional Means Test thresholds, the GMT Thresholds will be applied in a retrospective manner (i.e., HUD Indices published in Calendar Year 2002 will be used for Means Tests performed in Calendar Year 2003). Information about HUD income limits is available on the Data Sets Page of the HUD User Web Site at <u>http://www.huduser.org/datasets/il.html.</u>

The GMT Thresholds will be uploaded into V*IST*A annually, along with the traditional Means Test threshold values, in a patch released in December of each year. They will be activated on January 1<sup>st</sup> of each year. The indices from previous years will be stored indefinitely in both V*IST*A and HEC systems. For information about the implementation of HUD Indices, refer to the GMT Installation Guide and GMT Technical Manual.

> **NOTE:** On January 17, 2003, VA discontinued enrolling new Priority Group 8 veterans into the VA health care system based on VA’s inability to provide timely and quality health care to all enrolled veterans. The new relaxed Priority Group 8 enrollment restrictions allow certain PG8 veterans to be enrolled in the VA health care system if their household income does not exceed the current VA income thresholds (Means Test threshold and/or Geographical Means Test threshold) by more than 10%. These changes do not open enrollment to all PG8 veterans, however. For more details, visit the VA Health Care Eligibility & Enrollment Web Site at <http://www.va.gov/healtheligibility>.

The GMT software provides the following functionality.

- Automatically populates City, State, and County fields of the Patient Demographics Screen when ZIP Code is entered during patient registration or edit of patient demographic data (load/edit), unless the Bad Address Indicator is set. (Refer to Screen 1, Data Group 4, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
- State and County fields can only be edited by users who hold the EAS GMT COUNTY EDIT security key.

Means Test User MenuGMT Thresholds Lookup by ZIP Code

- Automatic Address Changes from HEC will clear the Bad Address Indicator field (if it was set). (Refer to Screen 1, Data Group 4, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
- A conversion of veterans based on their existing financial assessment information will be run at the HEC. An ongoing process assigns veterans to the appropriate medical care copayment and enrollment priority group upon completion of a financial assessment.
1.  NSC and non-compensable 0% SC veterans with current income above the MT Threshold and below the applicable GMT Threshold will be placed in the new Means Test status “GMT Copayment Required”. These veterans will be assigned to Enrollment Priority Group 7 (unless Catastrophically Disabled \[CD\] or exposed to Agent Orange[^1], Ionizing Radiation, or SW Asia Conditions[^2]). Veterans who are in GMT Copay Required status must submit income for yearly testing.
- Veterans who are subject to the full inpatient medical care copayment and placed in Enrollment Priority Group 8 (unless CD or exposed to toxic substances) include:
  - Veterans with income greater than the GMT threshold plus 10% where GMTT\>MTT
  - Veterans declining to provide income info
  - Veterans with income greater than the MT threshold plus 10% who live in an area where the GMT threshold is less than or equal to the MT threshold
  - Veterans with income less than the MTT threshold but with a Net Worth greater than \$80K
  - Veterans with income above the MT threshold plus 10% whose income info is over one year old at the time the GMT software is installed.
- Although this does not affect the GMT functionality, all user viewable references to Category A and Category C Means Test statuses in enrollment-related software have been modified to reflect the following changes:
  - Category A (Cat A) is now MT Copay Exempt

Means Test User MenuGMT Thresholds Lookup by ZIP Code

- Category C (Cat C) is now MT Copay Required.
- A variety of reports and data screens have been modified to display the new subcategories ‘b’ and ‘d’ for Enrollment Priority Group 8 and GMT Copayment Required status.
- Provides a new user option, GMT Thresholds Lookup by ZIP Code, which displays GMT Threshold values for a valid user-specified ZIP Code.
- Adds a new field, Hardship Reason, to the Hardship Determinations Screen.

Means Test User MenuGMT Thresholds Lookup by ZIP Code

This option is used to display GMT Threshold values for a valid Postal Code (a.k.a. ZIP Code). The only user prompt is “ZIP Code:”, and a response is required. You must enter a ZIP Code or a city name to generate an output, or a caret (^) to return to the menu. If you enter a city name and the software finds multiple cities with the same name, it returns a list of the cities with their corresponding ZIP Codes from which you can make your selection.

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

## Hardships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option replaces the Change a Patient’s Means Test Category option. It allows the user to grant, edit, and delete hardships for the current Means Test when the test is less than 1 year old from the effective date..

Hardship Determinations continue to be the responsibility of the VAMCs; however, they will be sent to the HEC and distributed nationally along with the Primary Means Test to all VAMCs that the veteran has visited. Once granted, a Hardship is in effect until a new Means Test is required. The VAMC that granted the hardship will retain the original Means Test Status when the status changes. For example, if a Hardship determination changes the original status from MT Copay Required to MT Copay Exempt, the new status (Exempt) is stored as the Means Test status. The original status (MT Copay Required) is then stored as Test Determined Status.

After the GMT conversion runs at the HEC, if a veteran's Means Test status is MT Copay Required, the user is prompted to enter the status (GMT Copay Required or MT Copay Exempt) and a Hardship Reason.

The Hardship Determinations screen provides the following List Manager actions.

*Grant Hardship*

Allows you to grant hardships for current Means Tests for the selected patient. Prompts for Hardship Effective Date and Hardship Review Date. Once granted a hardship remains in effect until a new Means Test is completed.

*Edit Hardship*

Allows you to edit hardships for current Means Tests for the selected patient. Prompts for Hardship Effective Date and Hardship Review Date. Only the VAMC that determines the hardship can edit or delete it*.Delete Hardship*

Allows you to delete hardships for current Means Tests for the selected patient. Only the VAMC that determines the hardship can edit or delete it. When a hardship is deleted, no record of it is retained in the database.

*Edit Comments*

Allows you to add, edit, and delete comments related to hardships for current Means Tests for the selected patient.

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pseudo SSN Report for Means Test Dependents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pseudo SSN Report for Means Test Dependents is used to print a report of spouses and/or dependents, sorted by patient, who have Pseudo SSNs. You can choose to print the report for one or all Pseudo SSN reasons.

The output includes:

- Report title and page number
- Whether the report includes one or all Pseudo SSN reasons
- Report date
- Patient name and SSN
- Dependent/spouse name and relationship to patient
- Dependent/spouse Pseudo SSN
- Dependent/spouse Pseudo SSN reason
- A summary at the end of the report provides the following information:
- If you chose to print the report for a specific Pseudo SSN reason, the summary provides the total number of dependents with Pseudo SSNs.
- If you chose to print the report for all Pseudo SSN reasons, the summary provides the total number of dependents with Pseudo SSNs *and* the number of dependents/spouses for each of the reason(s) selected.

## <u> </u>Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## View a Past Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View a Past Means Test option is used to view past Means Tests data. The option does not allow editing. You will be prompted for the patient's name and the date of the Means Test you wish to view. Double question marks (??) entered at the date prompt will provide you with a list of the patient's Means Test dates from which to choose.

If certain circumstances exist for the selected patient, messages may be displayed. A message will be printed if no detailed income information is on file for the veteran, or if the veteran's Means Test status is NO LONGER REQUIRED. Since income data can be entered/edited through registration, once a Means Test has this status, the income data being viewed may differ from that originally entered as part of the Means Test.

You will be able to view the following four Means Test screens through this option.

Screen 1 Marital Status/Dependents

Screen 2 Previous Calendar Year Gross Income

Screen 3 Deductible Expenses

Screen 4 Previous Calendar Year Net Worth

The option may display the dependent totals not converted. Totals not converted will only be displayed under the following conditions.

Converted totals exist and Means Test income is 0 or greater

For a spouse - the veteran is married but detailed income information is not

available

For dependent children - the veteran has dependent children but detailed

income information is not available

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Patient Address Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Address Update option is used to update a patient’s permanent address, temporary address, or both. If you choose to update both, you must update the permanent address first, then the temporary address.

After each permanent address update, both the old and new address information displays, and you are asked if you want to save the changes. To update the temporary address, you can accept the default information or enter new information for each field. You will return to the “Veteran Name/SSN:” prompt after each address update.

This option will not update the ADDRESS CHANGE DT/TM field (#.118) of the PATIENT file (#2) if no changes were made to the Permanent Address. It may be placed on other applications’ menus so users can update the patient’s permanent address, temporary address, or both, directly from their own applications’ menus.

## Patient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Inquiry option is used to view the following kinds of information for a selected patient: demographic, primary care, enrollment, preregistration, and such items as bad address indicator, foreign address, and date of death (including source of notification for date of death, date of last entry or update, and local submitter/user information).

A full or abbreviated inquiry may be displayed depending upon how the PIMS parameter, ABBREVIATED INQUIRY, is set at your facility.

Editing of the information is not allowed through this option.

The veteran’s Long Term Care (LTC) copayment status and last test date will be displayed when using this option. If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” will be displayed. If the veteran did not agree to pay the copayments, the following ineligible message will be displayed.

Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Display Preregistration Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Preregistration Call List in List Manager screen format. This is a list of the patients to be contacted before their clinic appointments for the purpose of updating their patient information. The information displayed might vary depending on how certain parameters in the MAS PARAMETERS file (#43) (e.g., Multidivisional, Sort Method, etc.) are set at your facility. (Use the MAS Parameter Entry/Edit option to set the applicable parameters for your facility.)

This option is locked with the DGPRE EDIT security key.

In addition to PATIENT NAME, PHONE, and SSN, the following columns are displayed in the Preregistration Call List:

HIST Provides a history of whether or not the patient has been contacted

successfully by telephone. (Enter ? at the “STATUS OF CALL:

CONNECTED//” prompt for a list of acceptable codes.) The codes for

as many as the last four calls are displayed.

SVC Indicates the hospital service (e.g., Medicine, Surgery, Psychiatry, etc.)

associated with the clinic in which the patient has an appointment.

STAMP Contains the date/time on which the patient information was last

updated in the Load/Edit screens through the use of the various

preregistration options. The date/time is displayed in this column only

if you answered YES to the “Date/Time stamp this patient? YES//”

prompt.

DIVISION Contains the name of the division associated with the patient’s clinic

appointment. The division name will be displayed only if the

Multidivisional parameter is set to YES. This column is not visible on

the initial Preregistration Call List screen. If greater than signs (\>\>\>)

appear on the status bar, you can scroll to the right of the screen using

your right arrow key (→) to view this column.

Preregistration MenuDisplay Preregistration Call List

The following user actions are available at the bottom of the screen.

CP Call Patient - Lets you edit patient information via Load/Edit Screens 1

through 5 and enter the call status for a selected patient. (If you need

assistance with editing the information on these screens, please refer to the

user documentation for the Load/Edit Patient Data option.) You also have

the option to apply a date/time stamp to the selected patient before returning

> to the Preregistration Call List screen. This action works the same as the Preregister a Patient menu option.

EH Edit History - Lets you edit information pertaining to whether or not

the patient was successfully contacted by telephone and edit the call

status. You can use this action to change, but not delete, log entries.

*Please note: You can only use this action after using the CP action.*

XH Expand History - Displays information pertaining to the calling

history for a selected patient, including the date and time of the call,

name of the person who made the call, and call status. *Please note:You can only use this action after using the CP action.*

IN Patient Inquiry - Lets you enter an inquiry for a selected patient

without leaving the Preregistration Call List screen. Works the same

as the Patient Inquiry menu option.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Calling Statistics Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates the Preregistration Call Statistics report which provides a breakdown of the current entries in the PRE-REGISTRATION CALL LOG file (#41.43) by call status. The prompts ask for beginning and ending dates and a device if the Multidivisional parameter in the MAS PARAMETERS file (#43) is set to NO. (Use the MAS Parameter Entry/Edit option to set this parameter.)

If the Multidivisional parameter is set to YES, the “Select division: ALL//” prompt will also appear. If you accept the ALL default, the next prompt will ask for a device. If you select a specific division, the “Select another division:” prompt will appear and will repeat after your entry, allowing you to select multiple divisions (up to a maximum of 20). Press \<RET\> to indicate that you are finished making your selections and proceed to the “DEVICE: HOME//” prompt.

Before using this option, multidivisional facilities should ensure that each clinic has an associated division. (You can do this by entering a division name at the “DIVISION:” prompt while using the Set up a Clinic option in the Scheduling Supervisor Menu.)

This option uses NO DIVISION SPECIFIED as a sort value. If you accept the ALL default at the “Select division: ALL//” prompt, the output will show NO DIVISION SPECIFIED as the division name for statistics whose clinics are NOT associated with a division.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Percentage of Patients Pre-Registered Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Percentage of Patients Pre-Registered Report prints the following data for a user-defined date range.

- Number of unique outpatients treated
- Number of unique outpatients pre-registered within the pre-registration time frame
- Percentage of unique outpatients pre-registered within the pre-registration time frame
- Number of unique outpatients pre-registered past the pre-registration time frame
- Number of unique outpatients never pre-registered
- Number of clinic exclusions and eligibility exclusions

It is recommended this report be queued to run after normal business hours.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Registration Source Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the Pre-Registration Source Report which lists the following information for a user-specified date range:

- Patient insurance policies that were added using the preregistration options and have a source of information equal to PRE-REGISTRATION (on Screen 5 of the Load/Edit Patient Data option).
- Inpatient and outpatient bills generated during the user-specified date range based on preregistration insurance policies and payments collected during the user-specified date range against those bills. Please note that bills and payments listed in the report could be against preregistration policies that were added outside of the user-specified date range.

The output generated by this option will vary depending on which of the following report formats you select at the “Type of report to print: summary//” prompt.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Detailed</td>
<td><ul>
<li><p>Provides detailed information for the following activities during the user-specified date range:</p></li>
<li><blockquote>
<p>Patient insurance policies added through preregistration options</p>
</blockquote></li>
<li><blockquote>
<p>Inpatient bills entered against preregistration policies</p>
</blockquote></li>
<li><blockquote>
<p>Inpatient payments collected against preregistration policies</p>
</blockquote></li>
<li><blockquote>
<p>Outpatient bills entered against preregistration policies</p>
</blockquote></li>
<li><blockquote>
<p>Outpatient payments collected against preregistration policies</p>
</blockquote></li>
<li><p>Provides total count for each activity.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Summary</td>
<td><ul>
<li><p>Prints a one-page report showing only the totals. No patient-specific information is provided.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Print Preregistration Audits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the number of changes to patient demographic and insurance data which were made during the preregistration process for a user-specified date range. The applicable audits in the PATIENT file (#2) must be turned on for this option to work. The MCCR Reengineering Group recommends that you ask your IRM Service to turn on the audits for the following fields:

> .05 MARITAL STATUS

> .111 STREET ADDRESS \[LINE 1\]

> .112 STREET ADDRESS \[LINE 2\]

> .114 CITY

> .115 STATE

> .117 COUNTY

> .131 PHONE NUMBER \[RESIDENCE\]

> .132 PHONE NUMBER \[WORK\]

> .211 K-NAME OF PRIMARY NOK

> .2191 K2-NAME OF SECONDARY NOK

> .3111 EMPLOYER NAME

> .31115 EMPLOYMENT STATUS

> .351 DATE OF DEATH

> .361 PRIMARY ELIGIBILITY CODE

The output will include the fields that have been changed, the name of the user(s) who made the changes, and the number of changes made by each user.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Add New Appointments to Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you add patients to the Preregistration Call List based on patient appointments for a user-specified search date. The default response to the “Enter Appointment date to search:” prompt is TODAY plus the value of the DAYS TO PULL APPOINTMENT field (#1100.05) in the MAS PARAMETERS file (#43). (Use the MAS Parameter Entry/Edit option to set the value of this field.)

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Clear the Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option deletes all entries in the PRE-REGISTRATION CALL LIST file (#41.42) regardless of the call status. There are no prompts associated with this option. Once the option is selected, the number of entries deleted will be displayed.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purge Call Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option purges all entries prior to a user-specified date from the PRE-REGISTRATION CALL LOG file (#41.43). You are asked to enter a purge date and to verify that you want to purge all entries prior to the date you entered.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purge Contacted Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option purges patients who have already been contacted and who have a call status of CONNECTED from the Preregistration Call List. There are no prompts associated with this option. Once the option is selected, the number of entries purged will be displayed.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays registration information for a selected patient including any preregistration items, bad address indicator, foreign address, emergency response indicator, and date of death (including source of notification for date of death, date of last entry or update, and local submitter/user information). The date of death information is READ ONLY.

The patient selected does not have to be in the PRE-REGISTRATION CALL LIST file (#41.42) to be selected.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Preregister a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to perform the following tasks:

- Preregister any selected patient in the PATIENT file (#2) through the use of the Load/Edit process (without using the Preregistration Call List).
- Enter the call status for a selected patient. (If you enter a status of CONNECTED, you can edit patient information via Load/Edit Screens 1 through 5. If you need assistance with editing the information on these screens, please refer to the user documentation for the Load/Edit Patient Data option.)
- Apply a date/time stamp to the selected patient before returning to the Preregistration Call List screen.

Edit the patient’s permanent address information. Prior to entering patient data, the permanent address is displayed and the user is asked, “<u>Do you want to edit the Patient's Address?</u>”.

- If the user answers YES, the system will prompt each address field and the user will be allowed to update the patient’s permanent address information. The old and the new address information is displayed and the system will ask the user “<u>Are you sure that you want to save the above changes?</u>”
  - If the user answers YES, the system displays “Change saved”, the patient’s permanent address change date/time stamp will be updated, and a trigger is set to send a message to the HEC.

> *Please note: It takes a actual change to the permanent address to update the permanent address change date/time stamp. If there were no changes to the permanent address information, and the user responds YES; no updates are made to the permanent address fields or permanent address change date/time stamp and a message is <u>NOT</u> triggered to the HEC.*

- If the user answers NO, the system displays “Change aborted”. Neither the patient’s permanent address information nor the permanent address change date/time stamp is updated and a message is <u>NOT</u> triggered to the HEC.
- If the user answers NO at the “<u>Do you want to edit the Patient's Address?</u>” prompt, the system will not prompt the user for address information and the system will continue the Preregister a Patient process.

Preregistration MenuPreregister a Patient

When using this option, the primary medical center division will be used as the division. This option is locked with the DGPRE EDIT security key.

*(Please note: This option works the same as the CP action on the Preregistration Call List screen in the Display Preregistration Call List option.)*

## Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Patient Wristband option is used to generate a patient wristband with barcoded social security number. The wristband will contain the patient name, primary long ID (usually the social security number), date of birth, religion, and an allergy flag (YES or a blank line for NO). Whether or not wristbands will print for a division and whether or not the ward location will print on the wristband is determined by site parameters.

If you choose to print a wristband, you will be prompted for a device and if you wish to queue your request. Requests must be sent to a bar code printer.

Wristbands may only be printed for inpatients. The print wristband functionality is also available in the Admit a Patient and Transfer a Patient options.

## Pseudo SSN Report (Patient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pseudo SSN Report (Patient) option is used to print a report of patients with Pseudo SSNs. You can choose to print the report for the following:

- All veterans, all non-veterans, or both

> AND

- One or all Pseudo SSN reasons

If you chose to print the report for both veterans and non-veterans, they will display in the following sub-reports, sorted by Pseudo SSN Reason:

- Report for Non-Veterans
- Report for Veterans

The report *does not* include:

- Deceased patients
- Non-user enrollees
- Patients with no Integration Control Number (ICN)

The output includes:

- Report title and page number
- Whether the report is for veterans, non-veterans, or both
- Report date
- Patient name
- Pseudo SSN
- Birth date
- Primary eligibility code
- Pseudo SSN reason
- Subtotal for each Pseudo SSN Reason
- Total number of patients with a Pseudo SSN

## Register a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Register a Patient option is used to process a patient’s application for health benefits, enter/edit information in their file, and perform a variety of registration-related functions. Necessary registration data is gathered and a corresponding entry is automatically made in the Disposition Log. This entry must receive subsequent dispositioning through the Disposition an Application option or the registration should be deleted through the Delete a Registration option. A new patient's record may be established or an existing one edited. Should you wish to enter a new patient into the database or edit an existing patient's record without creating an entry in the Disposition Log, you should use the Load/Edit Patient Data option.

After you select this option, patient demographic, enrollment, eligibility, and emergency response indicator(s) information is displayed. If the patient record contains a date of death, the following prompt appears: “PATIENT EXPIRED \[date\]...WANT TO CONTINUE? No//”. This prompt requires a response. If you respond with “No”, you return to the menu. If you respond with “Yes”, date of death information (including source of notification for date of death, date of last entry or update, and local submitter/user information) is also displayed. The date of death information is READ ONLY.

When a veteran's Enrollment Status is deceased and there is no date of death on file in VistA, a message displays asking the user to either add the date of death information or contact the HEC to remove an incorrect date of death.

For existing patients in the PATIENT (#2) file; prior to entering patient data, the permanent address is displayed and the user is asked, “<u>Do you want to edit the Patient's Address?</u>”.

- If the user answers YES, the system will prompt each address field and the user will be allowed to update the patient’s permanent address information. The old and the new address information is displayed and the system will ask the user “<u>Are you sure that you want to save the above changes?</u>”
  - If the user answers YES, the system displays “Change saved”, the patient’s permanent address change date/time stamp will be updated, and a trigger is set to send a message to the HEC.

Register a Patient

> *Please Note: It takes an actual change to the permanent address to update the permanent address change date/time stamp. If there were no changes to the permanent address information, and the user responds YES; no updates are made to the permanent address fields or permanent address change date/time stamp and a message is <u>NOT</u> triggered to the HEC.*

- If the user answers NO, the system displays “Change aborted”. Neither the patient’s permanent address information nor the permanent address change date/time stamp is updated and a message is <u>NOT</u> triggered to the HEC.
- If the user answers NO at the “<u>Do you want to edit the Patient's Address?</u>” prompt, the system will not prompt the user for address information and the system will continue the Register a Patient process.

Register a Patient

Entry/edit of a patient's record is done via a series of formatted data screens. There are a total of fifteen screens distributed with the PIMS package. Screens 12-14 are informational only. The enter/edit process will not be the same for every patient, nor for every user due to several variables which exist in the system. Your site has the ability to create its own additional screen in order to capture certain information it may need or to capture information in a different format. It has the ability to turn certain data screens ON and OFF according to patient type. Within the screens, it may specify which data groups may be entered/edited. The DG ELIGIBILITY security key also plays a role in your ability to enter/edit data. Depending upon whether eligibility has been verified, certain information may only be edited by a user holding this security key.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields have been established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert will be displayed. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields will display an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts will remain on file for one year.

The HIGH INTENSITY field in the MAS parameters has been provided to assist you in the identification of those fields which may/may not be edited. If this field has been set to YES at your facility, the number next to those data groups which may be edited will be in boldface type; those which are uneditable will not (excluding Screen 8). For those sites not using High Intensity, numbers of data groups which may be edited will be enclosed in \[ \]s, while those which are uneditable will be enclosed in \< \>s (excluding Screen 8).

The Registration Supplement provides an example of each data screen and a description of each associated field. Please refer to this Supplement when entering or editing patient information, if necessary.

If your site has the Consistency Checker turned ON, the system will perform a check for inconsistent/unspecified data elements at the conclusion of the entry/edit process. If any are found, you will be given the opportunity to make the necessary corrections.

You may now register a patient without the eligibility code or period of service being entered. These elements will be checked for at disposition.

Register a Patient

As previously mentioned, this option also allows you to perform several registration-related functions.

- You may make a HINQ inquiry and emboss a patient data card. With the installation of the Veteran Identification Card (VIC) software, the prompt “Download VIC data?” has been added which allows you to download the selected patient’s demographic data to the photo capture station. The existing “EMBOSS DATA CARD?” prompt has been changed to “EMBOSS (OLD) DATA CARD?”.
- If Record Tracking is running at your facility, you will be able to create records for new patients and print corresponding barcode labels. If the patient already has records in the Record Tracking system, you will be able to issue a request for these records to the file room. The “Select Admitting Area” prompt must be answered in order to request records.
- The system will determine a patient's need for Means Testing and Copay Testing and, if necessary, allow you to complete the required test. For the Copay Test, the veteran has to request the test be completed. For instructions on Means Test, see the Add a New Means Test or Complete a Required Means Test options. For instructions on Copay Test, see the Add a New Copay Test option.
- At the conclusion of the registration process, you will be prompted to print the 10-10EZ form.
- Since the financial information that is printed on the 10-10EZ or 10-10EZR form is taken from a means test associated with the patient. And, since a patient may have several means test entries during his/her course of care, the ‘PRINT 10-10EZ?’ and ‘PRINT 10-10EZR?’ prompts will present a selection list of means test entries associated with the patient. The selection list of means test entries will contain future Means Tests and future Co-Pay Exemption Tests that are not Primary. The selection list will also contain the most current Means Test, Co-Pay Exemption Test, and LTC Co-Pay Exemption Test that are Primary.
- If data for the patient does not exist in the VISTA patient database, a message displays informing the user that the forms will not be printed.

The system assigns a status to every patient registration. Available statuses are: 10-10 VISIT, UNSCHEDULED, and APPLICATION WITHOUT EXAM. Determination of the status is based upon whether the patient is currently being followed in a clinic for the same condition and if the patient is to be examined in the medical center that day.

Register a Patient

All necessary data from a registration is collected for entry into the AMIS 400 series reports. The REGISTRATION ELIGIBILITY CODE and SC% AT REGISTRATION fields have been included to allow sites flexibility in the grouping of their AMIS 400 series reports.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may be displayed with v2.5 of Order Entry/Results Reporting. The patient must have been examined. The notification will only be displayed for patients who are defined in an OE/RR LIST entry and will only be displayed to users defined in that list entry. Please refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

Screen 8 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. The following is a brief explanation of some of the actions listed on this screen.

DD - In order to edit the dependent demographics, the selected dependent has to be active.

DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from <u>every</u> Means Test.

ED - Expand Dependent will move to another screen. It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

MT - Used to enter/edit last year's marital status for the veteran.

AD - This protocol is not selectable from the registration screens.

RE - This protocol is not selectable from the registration screens.

Register a Patient

At the beginnin*g* of the registration process, “Enrollment/Eligibility Query sent ...” displays on your screen to notify you that the software sent an enrollment query for the selected patient to the patient database at the Health Eligibility Center (HEC). If the enrollment information for the selected patient is not returned by the end of the registration process, you can enroll the patient via the Patient Enrollment option.

If the patient you are registering is presenting for care at your facility for the first time, but has been seen by at least one other VAMC, a notification such as “Query to Patient's Last Site Treated, Facility Number \<Facility Number\>, is being initiated...” will display on your screen. This Register Once Messaging (ROM) solution was adopted to satisfy VHA’s strategic objective of reducing both the amount of information that a veteran must supply at each treatment encounter and the amount of data entry a Registration Intake Clerk must perform during the veteran’s intake process. The data elements that are retrieved from the Last Site Treated (LST) correspond to the patient’s demographic and insurance data.

When patient demographic data is retrieved for a patient who has been marked as “Sensitive” either by the HEC or the LST, the following table describes the actions that are taken at both the Requesting Site (RS) and the LST.

Register a Patient

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Scenario</strong></th>
<th><strong>Actions Taken at RS</strong></th>
<th><strong>Actions Taken at LST</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><blockquote>
<p><em>Sensitive Patient Flag (SPF) received from HEC &amp; flagged “Sensitive” at LST</em></p>
</blockquote></li>
</ol></td>
<td><ol type="1">
<li><p>Patient demographic data for “Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <u>not</u> retrieved.</p></li>
</ol></td>
<td><ol type="1">
<li><p><strong>V</strong><em>IST</em><strong>A</strong> automatically creates an entry in the New Person File (#200) representing the user performing the patient registration at the RS.</p></li>
<li><p><strong>V</strong><em>IST</em><strong>A</strong> creates a Security Log File (#38.1) entry with the user’s system user number (DUZ).</p></li>
<li><p>A mail bulletin is sent to the Information Security Officer (ISO) to provide notification that a sensitive patient record has been accessed, including the requesting site’s User Name.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><blockquote>
<p><em>SPF received from HEC &amp; not flagged “Sensitive” at LST</em></p>
</blockquote></li>
</ol></td>
<td><ol type="1">
<li><p>Patient demographic data for “Non-Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <u>not</u> retrieved.</p></li>
</ol></td>
<td><ol type="1">
<li><p>No New Person File (#200) or Security Log File (#38.1) entries are created.</p></li>
<li><p>Sensitive Patient notifications are <u>not</u> generated to the ISO.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li><blockquote>
<p><em>SPF not received from HEC &amp; flagged “Sensitive” at LST</em></p>
</blockquote></li>
</ol></td>
<td><ol type="1">
<li><p>Patient demographic data for “Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are retrieved and filed at the RS.</p></li>
<li><p>A “Sensitive Patient Data Retrieved” notification mail message is automatically sent to a new mail group and to the local user at the RS who registered the patient.</p></li>
<li><p>A mail bulletin is also sent to the ISO to provide notification that a sensitive patient record has been accessed and create the appropriate entry in the existing Security Log File audit trail.</p></li>
</ol></td>
<td><ol type="1">
<li><p><strong>V</strong><em>IST</em><strong>A</strong> automatically creates an entry in the New Person File (#200) representing the user performing the patient registration at the RS.</p></li>
<li><p><strong>V</strong><em>IST</em><strong>A</strong> creates a Security Log File (#38.1) entry with the user’s system user number (DUZ).</p></li>
<li><p>A mail bulletin is sent to the Information Security Officer (ISO) to provide notification that a sensitive patient record has been accessed, including the requesting site’s User Name.</p></li>
</ol></td>
</tr>
</tbody>
</table>

Register a Patient

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ol start="4" type="1">
<li><blockquote>
<p><em>SPF not received from HEC &amp; not flagged “Sensitive” at LST</em></p>
</blockquote></li>
</ol></td>
<td><ol type="1">
<li><p>Patient demographic data for “Non-Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <u>not</u> retrieved.</p></li>
</ol></td>
<td><ol type="1">
<li><p>No New Person File (#200) or Security Log File (#38.1) entries are created.</p></li>
<li><p>Sensitive Patient notifications are <u>not</u> generated to the ISO.</p></li>
</ol></td>
</tr>
</tbody>
</table>

When patient demographic data is retrieved for a patient who has a Date of Death recorded at the LST, a message displays on the screen that Date of Death information has been retrieved. The Date of Death information is not automatically filed into the requesting site’s database; instead, it is placed into a mail message and sent to the RO mail group.

The query to the LST will not process successfully if:

- The patient’s National Internal Control Number (ICN) and Treating Facility List are not provided through the connection to the MPI
- The query time exceeds 60 seconds
- The user information of the Registration Clerk is determined to be invalid

The Veterans Healthcare Eligibility Reform Act of 1996, PL 104-262, prohibits providing care for veterans who are not enrolled after October 1, 1998 (with limited exceptions). The Register a Patient option displays enrollment information and provides the ability to enroll the patient in the VA Patient Enrollment System.

A preliminary priority value is calculated on an initial enrollment application. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is *at or below* the latest EGT setting for a new enrollee or *below* the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is *below* the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” shall be assigned. At verification, the HEC will recalculate these fields based on a Master Veteran Record containing all nationally available patient data.

Register a Patient

A query is automatically sent to the Health Eligibility Center (HEC) when a patient registration is completed through this option. This query will determine if a Means Test or Copay Exemption Test (with Income Screening information) has been completed for the veteran for a specified income year. The HEC will process the query, and if there is a completed Means Test or Copay Exemption Test (with Income Screening information), the HEC will transmit the Primary test and any Hardship determinations to the VAMC that sent the query.

The veteran’s Long Term Care (LTC) copayment status and last test date will be displayed when using this option. If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” will be displayed. If the veteran did not agree to pay the copayments, the following ineligible message will be displayed.

Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Report - All Address Change with Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Report - All Address Change with Rx option lists those patients with active pharmacy prescriptions whose primary address fields have been changed during the previous 24 hours.

The output is sent to the DG DAILY ADDRESS CHANGE mail group. If the mail group is not populated, the following message will appear when running the option.

“DG DAILY ADDRESS CHANGE does not have a member. Report not sent.”

The output may contain the following information.

- Patient’s name and last four numbers of SSN
- Name of the user who made the last change(s) and date/time the last change(s) were made
- Source of change (VAMC, HEC, etc.)
- Permanent address as of 24 hours ago
- Permanent address as of now
- Foreign address changes
- Home and work phone numbers
- Count indicating total number of records listed on the report

It is recommended this report be queued to run after normal business hours.

## Report - All Address Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient’s permanent address is changed during the previous 24 hours, this report will list the patient permanent address as of now and the patient permanent address as of 24 hours ago. It can be run from the Registration Menu, or scheduled via Task Manager (TaskMan). If run from the Registration Menu, you will be prompted to enter a start time (or accept the default “NOW”); the task will be queued to run at that time.

<u>From the Registration Me</u><u>nu</u>

Select the Report - All Address Changes option. You will be prompted to enter a start time (or accept the default “NOW”); the task will be queued to run at that time.

<u>From Task Manager</u>

1.  Select the TaskMan Management Menu
2.  Select Schedule/Unschedule Options.
3.  Enter DG ALL ADDRESS CHANGE REPORT as the option to schedule or reschedule. Verify that this is the correct option.
4.  In the Edit Option Schedule Screen, press enter to navigate between fields.
5.  In the QUEUED TO RUN AT WHAT TIME: field, enter the date/time you want this option to be started by TaskMan.
6.  In the RESCHEDULING FREQUENCY: field, enter the value that represents how frequently you want TaskMan to automatically reschedule the report. For example, enter 24H if you want the report to run every 24 hours, 1D if you want the report to run at the same time every day, etc.
7.  In the COMMAND: field, enter SAVE to save your changes, then EXIT to return to the “Select OPTION to schedule or reschedule:” prompt.

The output is sent to the DG DAILY ADDRESS CHANGE mail group (but will not be annotated as a new message). Remember to populate this mail group with the staff that should receive this mail message. The output will contain the following information:

- Patient’s name and last four numbers of SSN
- Name of the user who made the last change(s) and date/time the last change(s) were made
- Source of change (VAMC, HEC, etc.)
- Permanent address as of 24 hours ago.
- Permanent address as of now.
- Foreign address changes
- Notification if patient has active pharmacy prescription(s)

## Report - All Patients flagged with a Bad Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report listing all patients for whom a Bad Address Indicator (Undeliverable, Homeless, or Other) is entered. It includes the patient’s name and the last four digits of the patient’s social security number.

The Bad Address Indicator applies to the address at which the patient resides. It is entered during the patient registration process on Screen 1 - Patient Demographic Data. Setting this field prevents a bad address from being shared with HEC and other VAMC facilities. It is also used to block Means Test Renewal Letters from being sent.

> **NOTE:** The Veterans Financial Assessment Project removed the requirement for veterans to complete an annual means test. The Means Test Renewal Letter options were disabled with EAS\*1\*106 released in host file DG_53_P858.

Once the Bad Address Indicator is set, incoming “newer” addresses and/or address updates manually entered by VAMC site staff will automatically remove the Bad Address Indicator and allow the “updated” address to be transmitted to HEC and other VAMC facilities.

The only prompt is for Device. It is recommended you queue this report to print as it may be quite lengthy.

## Report - Patient Catastrophic Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a report for a user-selected date range (up to one year) which provides a listing of patients who were flagged as having a potential catastrophic edit alert created for supervisory review.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields have been established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert will be displayed. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. The DG CATASTROPHIC EDIT security key is required in order to receive and review the alerts. If this key is not assigned, the alerts will be forwarded to personnel holding the DG SUPERVISOR security key. The alerts will remain on file for one year.

You may choose to print a detailed or summary report. The summary report includes the number of potential catastrophic edit alerts posted, alerts reviewed, and alerts determined to be catastrophic. In the detailed report you may choose to display all alerts, only those not reviewed, or only those with catastrophic edit. In the detailed report each applicable patient’s data is displayed

You must hold the DG SUPERVISOR security key to access this option.

## Unsupported CV End Date Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Eligibility Center (HEC) calculates and shares the CV End Date with the VAMCs to support the CV determination. This option runs a report that helps the VAMCs to identify CV End Dates without the supporting MSD.

The report has the following fields:

- Veteran’s DFN
- Veteran’s Name and SSN
- CV End Date

The report may be sorted by:

- Veteran’s DFN
- Veteran’s Name

A bulletin is sent to the members of the DGEN ELIGIBILITY ALERT mail group at the veteran’s VAMCs of record to update the veteran’s CV Eligibility information when there’s a change to the CV Eligibility End Date at the HEC.

The following is an example of the Unsupported CV End Date Bulletin. Note that the Veteran’s DFN is displayed in the Subject line to help you correlate the data in the bulletin to the data in the Unsupported CV End Date Report.

Subj: DFN: 7171686 - CV END DATE IS UNSUPPORTED \[#33613\]

25 Jun 2004 12:56:20 -0500 (EST) 23 lines

From: \<ADTEMPLOYEE,ONE@PENMGR.IVM.MED.VA.GOV\> In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

A New Combat Vet Eligibility End Date has been determined at HEC for

the following patient:

Name: ADTpatient,One

SSN: 000168000

CV End Dt: Jun 20, 2006

This new Combat Vet Eligibility End was determined using the following

Military Service and Conflict Information from Site \# 500:

Branch of Service\[Last\]: ARMY

Service Number\[Last\]: 000168000

Service Entry Date\[Last\]: Feb 01, 2002

Service Separation Date\[Last\]: Jun 21, 2004

Service Discharge Type\[Last\]: HONORABLE

Conflict Location: PERSIAN GULF WAR

Conflict Indicator: YES

Conflict From Date: Aug 02, 2002

Conflict To Date: Feb 21, 2004

Please update your records to reflect the above information or contact the

site listed above if this information is inaccurate.

## View Patient Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view a patient's address and address change information. The user is prompted to select a patient's name and print device. The output includes the following information:

- Patient Name
- Patient Address
- If the selected patient has a temporary and/or confidential address, the system asks if you would like to view it.
- If the selected patient only has a permanent address on file, the screen display includes verification that the patient has no temporary or confidential address on file.
- Address Change Date
- Address Change Source
- Address Change Site
- Bad Address Indicator (Refer to Screen 1, Data Group 4, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)

## View Registration Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Registration Data option allows you to view the registration information contained in a patient's record. You will not be able to edit a patient's data using this option.

As with the entry/edit of this information, viewing is accomplished in a series of screens. There are fifteen screens distributed with the PIMS package. Your site has the ability to create its own screen in order to collect certain needed data or capture data in a different format. You may turn certain data screens ON and OFF according to patient type. Within the screens, you may specify which data groups should be editable.

You may move from screen to screen either by entering \<^#\> to specify the screen number you wish to move to, \<RET\> to move to the next screen, \<?\> to access its HELP screen, or \<^\> to quit.

## Registration Supplement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The collection of patient registration data is done via a series of formatted data screens. There are fifteen of these screens distributed with the Patient Information Management System (PIMS) package. The first eleven are dedicated to gathering the patient's registration information. This information makes up the patient's "file" in your computer. Screens 12-14 are for information purposes only and the data contained on them is not editable. They provide past admission and application information as well as the patient's clinic enrollments and a listing of future appointments. Each screen also has an associated HELP screen which may be accessed by entering a \<?\> at the prompt which appears on each screen. Following is a list of the fifteen screens.

> Screen \#1 PATIENT DEMOGRAPHIC DATA

> Screen \#1.1 ADDITIONAL PATIENT DEMOGRAPHIC DATA

> Screen \#2 PATIENT DATA

> Screen \#3 EMERGENCY CONTACT DATA

> Screen \#4 APPLICANT/SPOUSE EMPLOYMENT DATA

> Screen \#5 INSURANCE DATA

> Screen \#6 MILITARY SERVICE DATA

> Screen \#7 ELIGIBILITY STATUS DATA

> Screen \#8 FAMILY DEMOGRAPHIC DATA

> Screen \#9 INCOME SCREENING DATA

> Screen \#10 INELIGIBLE/MISSING DATA

> Screen \#11 ELIGIBILITY VERIFICATION DATA

> Screen \#12 ADMISSION INFORMATION

> Screen \#13 APPLICATION INFORMATION

> Screen \#14 APPOINTMENT INFORMATION

> Screen \#15 SPONSOR DEMOGRAPHIC INFORMATION

The registration or load/editing process will vary from patient to patient and user to user. This is due to several factors: the patient type, your site parameters, whether certain data has been verified, and whether you hold the DG ELIGIBILITY security key.

For each new patient entered into the system, you will be prompted to enter a patient type. Patient types are distributed with the package. Patient type will determine (in part) which screens are presented during the registration process, as well as which data items on the screens will be available for entry/edit. Screens 1, 1.1, 2, 4, 5, 7, 12, 13, 14, and 15 will always be presented. The presentation of Screens 3, 6, 8, 9, 10, and 11 will vary as your site has the ability to turn these screens OFF and ON according to patient type. This has been done to allow sites flexibility in the collection of their patient data. For example, a site may not wish to collect military service data for a collateral patient. The Military Service Data Screen would then be turned OFF for that patient type.

Your site is also able to set up an additional registration screen should it wish to capture certain data in a different format. The fields displayed on this screen must already exist in the system (PATIENT file (#2)) so the data prompts associated with such a screen would be familiar to you. This screen, if set up, will always appear at the end of the registration process.

Certain data such as an applicant's name, SSN, date of birth, eligibility, monetary benefits, and service record are subject to verification. The verification must be performed by someone who holds the DG ELIGIBILITY security key. Up until the time of verification, any user will be able to enter/edit data pertaining to these categories. After verification, the data may be viewed by all users; however, only those who hold the DG ELIGIBILITY security key will be able to edit this data.

Registration Supplement

PSEUDO SSN NOTE: For every option that displays the patient’s SSN, if the patient has a Pseudo SSN on file, the message “\*\*Pseudo SSN\*\*" will be displayed next to the SSN.

Each screen (excluding Screen 8) is set up in numbered data groups. If the number of the data group is displayed in brackets \[ \], you will be able to enter/edit its data. If it is displayed in arrows \< \>, you will not be able to enter/edit. A High Intensity feature has also been supplied. If this feature is turned ON (through the MAS Parameter Entry/Edit option of the ADT System Definition menu), those data groups that you may edit will be highlighted on your screen while those that are not editable will not be highlighted. The system determines which information is editable by user and patient type.

Screen 8 uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

For the purposes of this Supplement, all non-informational screens and data groups are shown as being "available"; that is, their corresponding numbers are surrounded by brackets \[ \]. Keep in mind that this may not be the case when you are actually working on the system.

No defaults are shown in this Supplement. If you are editing the record of an existing patient, previously entered information will appear as a default. You may enter a \<RET\> to accept the default value.

What follows are examples of each Registration Data Screen along with definitions of each of the data groups and associated fields. Information that is subject to verification is so indicated. Fields that are indented are prompted based upon the entry made at the primary prompt (the prompt under which that field is indented). Much of the time, data entered into these fields will be deleted upon changing or deleting the entry at the primary prompt. This is explained for each appropriate data grouping or field.

Registration Supplement

PATIENT DEMOGRAPHIC DATA SCREEN \<1\>

PATIENT NAME;SSN TYPE

==================================================================

INELIGIBLE/MISSING MESSAGE MAY BE DISPLAYED HERE

\[1\] Name: SS:

DOB:

Family: Sex: MBI:

Given: \[2\] Alias:

Middle:

Prefix:

Suffix:

Degree:

\[3\] Remarks:

\[4\] Permanent Address: \[5\] Temporary Address:

County: County:

Phone: Phone:

Office: From/To:

Bad Addr:

\<RET\> to CONTINUE, 1-5 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

Once a patient's eligibility has been verified, the information contained in this data group may not be edited by anyone not holding the DG ELIGIBILITY security key. Up until the time of eligibility verification, any user may enter/edit these fields. After verification, it will be available for viewing to all users; however, only holders of the DG ELIGIBILITY security key will be able to enter/edit the information.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields have been established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert will be displayed. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields will display an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts will remain on file for one year.

FAMILY (LAST) NAME - Enter the applicant's last name.

GIVEN (FIRST) NAME - Enter the applicant's first name.

MIDDLE NAME - Enter the applicant's middle name.

PREFIX - Enter applicant’s name prefix such as Mr. or Mrs.

SUFFIX - Enter applicant’s name suffix such as JR, SR, II, III.

DEGREE - Enter applicant’s academic degree, such as BA, BS, MD, or PhD.

Registration Supplement

SCREEN 1, cont.

DATAGROUP1, cont.

SOCIAL SECURITY NUMBER – Answer with the individual’s social security number (must be 9 numbers in length). The SSN will be sent to the Social Security Administration (SSA) for verification. After the SSN status is verified by the SSA, it can only be edited by members of the Identity Management Data Quality Team, and VERIFIED is displayed next to the SSN. If the SSN status is Invalid per SSA, INVALID is displayed next to the SSN.

If a valid SSN is not known, enter P at the “SOCIAL SECURITY NUMBER” prompt for the system to automatically assign a Pseudo SSN. You must then enter a Pseudo SSN reason. You should make every effort to obtain the patient’s actual SSN.

DATE OF BIRTH - Enter the applicant's date of birth. Date of Birth cannot be a date after the Ineligible date and cannot be a date after the Enrollment Application Date.

SEX - M for MALE (default), F for FEMALE

MULTIPLE BIRTH INDICATOR (MBI): - Is this applicant part of a multiple birth? N for NO (default), Y for YES - part of multiple birth.

DATAGROUP2

ALIAS - Alternate name (if any) the applicant uses (2-30 characters). An entry in this field will be automatically cross-referenced and the applicant may be called up using this alias. This is a multiple field; you will be returned to this prompt repeatedly until no more entries are made. For each entry, the following will be prompted.

ALIAS SSN - Alternate social security number applicant uses, if any.

DATAGROUP3

REMARKS - You may enter a free text comment (3-60 characters) regarding the patient. If a patient has been declared ineligible, a remark to indicate this will automatically be inserted into this field. If a patient's enrollment status is REJECTED, a remark to indicate this will automatically be inserted into this field.

DATA GROUP 4

The following rules apply when editing patient permanent address information via the following options:

- Load/Edit Patient Data
- Register a Patient
- Preregister a Patient
- Patient Address Update

Manila, Philippines will be exempt from these rules; you will be able to edit all the patient permanent address fields without the ZIP Code linking features.

Registration Supplement

SCREEN 1, cont.

DATAGROUP4, cont.

- If a specific ZIP Code corresponds to a geographical location on file, a list of city choices will be provided; an asterisk (\*) will indicate the USPS default city for that ZIP Code.
- If a city name has a standard United States Postal Service (USPS) abbreviation, the standard abbreviation will be listed (and saved when chosen).
- Users with the EAS GMT COUNTY EDIT key will be allowed to edit state and county and/or enter a ZIP Code that is not currently in File \#5.12 as the patient's ZIP Code (without adding the ZIP Code to File \#5.12), or enter free text city name. \*
- If more than one state and county correspond to a ZIP Code, the user will be allowed to edit the STATE and COUNTY fields (even if the user does not have the \*EAS GMT COUNTY EDIT key).

\*Please note: The EAS GMT COUNTY EDIT security key should be assigned to the appropriate individuals at your facility.

After address edits are completed via the Load/Edit Patient Data, Register a Patient, Preregister a Patient, or Patient Address Update options, “before change” and “after change” values for the patient permanent address fields will display to your screen. The changes will be saved only after you confirm their accuracy. If you time out, answer “NO”, or enter a single caret (^) or double caret (^^) in response to the confirmation question, all changes will be aborted. If you enter single caret (^) or double caret (^^) during the editing of any field in the patient permanent address, “EXIT NOT ALLOWED ??” will be displayed, and the same field will be prompted until the you provide a valid input.

COUNTRY – Enter the country code, postal code, or description of the country where the patient’s permanent address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Province and Postal Code vice Zip+4, or State. Both Province and Postal Code are free text fields.

STREET ADDRESS \[LINE 1\], \[LINE 2\] \[LINE 3\] – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required. Line 3 will appear only if an entry exists in Line 2.

ZIP+4 – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.

CITY – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.

STATE – Prepopulated by the zip-linking feature, following the zip-linking rules; no user entry required.

COUNTY - Prepopulated by the zip-linking feature, following the zip-linking rules; no user entry required.

PHONE NUMBER \[RESIDENCE\] - Enter applicant's residence telephone number.

Registration Supplement

SCREEN 1, cont.

DATAGROUP4, cont.

PHONE NUMBER \[WORK\] - Enter applicant's business telephone number (4-20 characters).

BAD ADDRESS INDICATOR - Applies to the address at which the patient resides. Setting this field will prevent a bad address from being shared with HEC and other VAMC facilities. It will also be used to block Means Test Renewal Letters from being sent.

> **NOTE:** The Veterans Financial Assessment Project removed the requirement for veterans to complete an annual means test. The Means Test Renewal Letter options were disabled with EAS\*1\*106 released in host file DG_53_P858.

Once the Bad Address Indicator is set, incoming “newer” addresses and/or address updates manually entered by VAMC site staff will automatically remove the Bad Address Indicator and allow the “updated” address to be transmitted to HEC and other VAMC facilities.

When a bad address is indicated at the LST, no address information will be returned from the LST to the local site.

This field should be manually set as follows (if applicable):

- NULL – indicating the veteran’s address is assumed to be good
- UNDELIVERABLE – mail sent to this address was returned or is otherwise known to be undeliverable
- HOMELESS – veteran has no known address
- ADDRESS NOT FOUND – for use by ESR only
- OTHER – reason other than Undeliverable, Homeless, or Address Not Found

DATAGROUP5

This data group allows you to enter a temporary address for the applicant. If a temporary address is already on file and NO is answered at the first prompt, the START DATE and END DATE will automatically be deleted. The address will remain on file but may only be viewed/edited when YES is answered at the first prompt. To delete all temporary address data, answer NO at the first prompt and YES at the following prompt: "Do you want to delete all temporary address data?". To retain all data on file, enter an up-arrow \<^\> at the primary prompt.

> TEMPORARY ADDRESS ACTIVE? - YES/NO - If YES, the following fields will also be prompted.

> TEMPORARY ADDRESS START DATE - Beginning date at temporary address.

> TEMPORARY ADDRESS END DATE - Ending date applicant will be at temporary address.

> TEMPORARY ADDRESS COUNTRY: UNITED STATES// - Enter the country code, postal code, or description of the country where the patient’s temporary address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Temporary Province and Temporary Postal Code vice Temporary Zip+4, or Temporary State. Both Temporary Province and Temporary Postal Code are free text fields.

Registration Supplement

SCREEN 1, cont.

DATAGROUP5, cont.

> TEMPORARY STREET \[LINE 1\] \|

> TEMPORARY STREET \[LINE 2\] \|

> TEMPORARY STREET \[LINE 3\] \| Enter applicant's temporary address/phone

> TEMPORARY ZIP+4 If a specific ZIPCode corresponds to a geographical location on file, a list of city choices will be provided; an asterisk (\*) will indicate the USPS default city for that ZIP Code.

> TEMPORARY CITY \|

> TEMPORARY STATE \|

> \|

> TEMPORARY ADDRESS COUNTY \|

> TEMPORARY PHONE NUMBER \|

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Required fields for DOMESTIC address</th>
<th>Required fields for FOREIGN address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>STATE</p></li>
<li><p>ZIP</p></li>
<li><p>COUNTY</p></li>
<li><p>COUNTRY</p></li>
</ul></td>
<td><ul>
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>COUNTRY</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Note: You cannot exit these fields or jump to another field using the caret (^); you must enter the required information.</td>
</tr>
</tbody>
</table>

Registration Supplement

ADDITIONAL PATIENT DEMOGRAPHIC DATA SCREEN \<1.1\>

PATIENT NAME; SSN TYPE

===========================================================++++++======

\[1\] Confidential Address

Phone:

From/To:

\[2\] Cell Phone:

Pager \#:

Email Address:

\<RET\> to CONTINUE, 1-2 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

This data group allows you to enter a confidential address for the applicant. A confidential address is an alternative mailing address to be used for the mailing of confidential correspondence types designated by the veteran. If a confidential address is already on file and NO is answered at the first prompt, the START DATE and END DATE will automatically be deleted. The address will remain on file but may only be viewed/edited when YES is answered at the first prompt. To delete all confidential address data, answer NO at the first prompt and YES at the following prompt: "Do you want to delete all confidential address data?". To retain all data on file, enter an up-arrow \<^\> at the primary prompt.

CONFIDENTIAL ADDRESS ACTIVE? - YES/NO - If YES, the following fields will also be prompted.

> CONFIDENTIAL ADDRESS START DATE - Date to start using confidential address.

> CONFIDENTIAL ADDRESS END DATE - Date to stop using confidential address.

> CONFIDENTIAL ADDRESS CATEGORY - Enter the category type of mail veteran wishes to be sent to the confidential address. This is a multiple field. You will be returned to this prompt repeatedly until no more categories are entered. You may enter a \<?\> to select from a list of available entries.

> CONFIDENTIAL ADDRESS COUNTRY: UNITED STATES// - Enter the country code, postal code, or description of the country where the patient’s confidential address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Confidential Province and Confidential Postal Code vice Confidential Zip+4, or Confidential State. Both Confidential Province and Confidential Postal Code are free text fields.

> CONFIDENTIAL STREET \[LINE 1\] \|

> CONFIDENTIAL STREET \[LINE 2\] \| Enter applicant's confidential address.

> CONFIDENTIAL STREET \[LINE 3\] \|

Registration Supplement

SCREEN 1.1, cont.

> DATAGROUP1, cont.

> CONFIDENTIAL ADDRESS ZIP CODE If a specific ZIPCode corresponds to a geographical location on file, a list of city choices will be provided; an asterisk (\*) will indicate the USPS default city for that ZIP Code.

> CONFIDENTIAL ADDRESS CITY \|

> CONFIDENTIAL ADDRESS STATE \|

> \|

> CONFIDENTIAL ADDRESS COUNTY \|

> CONFIDENTIAL PHONE NUMBER \|

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Required fields for DOMESTIC address</th>
<th>Required fields for FOREIGN address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>STATE</p></li>
<li><p>ZIP</p></li>
<li><p>COUNTY</p></li>
<li><p>COUNTRY</p></li>
</ul></td>
<td><ul>
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>COUNTRY</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Note: You cannot exit these fields or jump to another field using the caret (^); you must enter the required information.</td>
</tr>
</tbody>
</table>

DATAGROUP2

This data group allows you to enter, edit and delete a veteran’s Cell Phone Number, Pager Number and E-Mail Address. Although not required, if entered, an “@” character is required in order for the E-Mail Address to be accepted and stored.

> PHONE NUMBER \[CELLULAR\] – Enter the telephone number \[4 – 20 characters\] for this applicant’s cellular phone. The entry may contain numbers \[0-9\], parentheses \[( )\], dashes \[-\], periods \[.\] and spaces. Alpha characters \[A-Z\] are not allowed. Cellular phone number is not required.

> PAGER NUMBER – Enter the applicant’s pager number \[4 – 20 characters\]. The entry may contain numbers \[0-9\], parentheses \[( )\], dashes \[-\], periods \[.\] and spaces. Alpha characters \[A-Z\] are not allowed. Pager number is not required.

> EMAIL ADDRESS - Enter the applicant’s email address \[1 – NN characters\]. If entered, the address must contain an “@”. Email Address is not required.

Registration Supplement

PATIENT DATA SCREEN \<2\>

PATIENT NAME;SSN TYPE

=================================================================

\[1\] Marital: POB:

Religion: Father:

SCI: Mother:

Mom's Maiden:

\[2\] Previous Care Date Location of Previous Care

------------------ -------------------------

\[3\] Ethnicity:

Race:

\<4\> Date of Death Information

Date of Death: Source of Notification:

Updated Date/Time: Last Edited By:

\[5\] Emergency Response:

\<RET\> to CONTINUE, 1,2,3,5 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

MARITAL STATUS - Enter the appropriate marital status for the applicant. You may enter a \<?\> to obtain a list of choices.

RELIGIOUS PREFERENCE - Enter applicant's religion or code. You may enter a \<?\> to obtain a list of choices.

PLACE OF BIRTH \[CITY\] - Enter city (or foreign country if born outside U.S.) where applicant was born (2-20 characters).

PLACE OF BIRTH \[STATE\] - Enter state or state code where applicant was born. You may enter a \<?\> to select from available list.

FATHER'S NAME - Enter name of applicant's father in “LAST,FIRST MIDDLE SUFFIX” format.

MOTHER'S NAME - Enter name of applicant's mother in “LAST,FIRST MIDDLE SUFFIX” format.

MOTHER'S MAIDEN NAME - Enter maiden name (last name prior to marriage) of applicant's mother (3-35 characters).

SPINAL CORD INJURY - Is the applicant a spinal cord injury patient? Enter the appropriate value.

You may enter a \<?\> to obtain a current list of choices.

Registration Supplement

SCREEN 2, cont.

DATAGROUP2

This group is used to enter the past two dates and locations of the applicant's last VA care (aside from the facility to which he/she is applying). When YES is answered at the initial prompt (REC'D VA CARE PREVIOUSLY), the locations/dates are prompted. Deletion of data in these two fields is automatic if NO is subsequently entered at the initial prompt.

REC'D VA CARE PREVIOUSLY - YES/NO - Has applicant received care previously in a VA facility? If YES, the following will be prompted.

> MOST RECENT LOCATION OF CARE - Name or number of VA facility at which patient received most recent episode of care (other than facility to which he/she is applying). Enter a \<?\> for a list of selectable names/numbers.

> MOST RECENT DATE OF CARE - Date of most recent episode of care in other VA facility.

> 2ND MOST RECENT LOCATION - Name or number of VA facility at which patient received 2nd most recent episode of care (other than facility to which he/she is applying). If an entry is made, the following will also be prompted.

> 2ND MOST RECENT DATE OF CARE - Date of 2nd most recent episode of care in other VA facility.

DATAGROUP3

ETHNICITY INFORMATION - From available list, the ethnicity which best identifies the patient.

RACE INFORMATION - From available list, the race which best identifies the patient.

DATAGROUP4

DATE OF DEATH INFORMATION

The following date of death information will be displayed if applicable and is for display purposes only. Data entry/edit is through the Discharge a Patient and Death Entry options.

> DATE OF DEATH - Date and time of death

> SOURCE OF NOTIFICATION - Source who made notification of date of death.

> UPDATED DATE/TIME - Date and time date of death information last updated.

> LAST EDITED BY - Name of local user who last edited date of death information.

DATAGROUP5

EMERGENCY RESPONSE INDICATOR - Select the appropriate emergency response indicator. Currently, the only available selection is K (for Hurricane Katrina). This field is optional and may be left blank.  
Registration Supplement

EMERGENCY CONTACT DATA SCREEN \<3\>

PATIENT NAME;SSN TYPE

==================================================================

\[1\] NOK: \[2\] NOK-2:

Relation: Relation:

Phone: Phone:

Work Phone: Work Phone:

\[3\] E-Cont.: \[4\] E2-Cont.:

Relation: Relation:

Phone: Phone:

Work Phone: Work Phone:

\[5\] Designee: Relation:

Phone: Work Phone:

\<RET\> to CONTINUE, 1-5 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

K-NAME OF PRIMARY NOK - Name of applicant's next-of-kin (3-35 characters). If an entry is made in this field, the following fields will also be prompted. When the entry in this field is deleted, all entries in the following fields are also deleted. Deletion of data in the following fields may not be accomplished unless the entry in this field is first deleted.

> K-RELATIONSHIP TO PATIENT - Relationship of patient's next of kin (1-30 characters)

> K-ADDRESS SAME AS PATIENT'S - YES/NO - If YES, the applicant's information will automatically be inserted in the next-of-kin address fields and automatically updated upon update of the applicant's address. If NO, the following fields will be prompted.

> K-STREET ADDRESS \[LINE 1\] \|

> K-STREET ADDRESS \[LINE 2\] \|

> K-STREET ADDRESS \[LINE 3\] \| Address/telephone number of

> K-CITY \| applicant's primary next-of-kin

> K-STATE \|

> K-ZIP+4 \|

> K-PHONE NUMBER \|

> K-WORK PHONE \|

DATAGROUP2

No entry may be made into this data group unless a primary next-of-kin has been entered (Data Group 1).

K2-NAME OF SECONDARY NOK - Name of applicant's secondary next-of-kin (3-35 characters). If an entry is made in this field, the following fields will also be prompted and data contained in them will automatically be deleted upon deletion of the entry in this field.

> K2-RELATIONSHIP TO PATIENT - Relationship of applicant's secondary next-of-kin (1-30 characters).

Registration Supplement

SCREEN 3, cont.

DATAGROUP2, cont.

> K2-ADDRESS SAME AS PATIENT'S - YES/NO - If YES, the applicant's address information will automatically be inserted in the following fields and updated accordingly as the applicant's address is updated. If NO, the following fields will be prompted.

> K2-STREET ADDRESS \[LINE 1\] \|

> K2-STREET ADDRESS \[LINE 2\] \|

> K3-STREET ADDRESS \[LINE 3\] \|

> K2-CITY \| Address/phone of applicant’s secondary

> K2-STATE \| next-of-kin

> K2-ZIP+4 \|

> K2-PHONE NUMBER \|

> K-WORK PHONE \|

DATAGROUP3

E-EMER. CONTACT SAME AS NOK - YES/NO - Is the person to contact in the event of emergency the same as the patient's next-of-kin? If YES, the information on file for the applicant's primary next-of-kin will automatically be inserted in the following fields and updated accordingly as the next-of-kin information is updated. If NO, the following fields will also be prompted.

> E-NAME

> E-RELATIONSHIP TO PATIENT \|

> E-STREET ADDRESS \[LINE 1\] \|

> E-STREET ADDRESS \[LINE 2\] \| Name/relationship/address/phone number of

> E-STREET ADDRESS \[LINE 3\] \| primary individual to contact in event of

> E-CITY \| emergency

> E-STATE \|

> E-ZIP+4 \|

> E-PHONE NUMBER \|

> E-WORK PHONE \|

DATAGROUP4

No entry may be made in this data group unless a primary emergency contact has been specified in Data Group 3.

E2-NAME OF SECONDARY CONTACT - Name of secondary individual to contact in the event of an emergency. If an entry is made in this field, the following fields will also be prompted.

Registration Supplement

SCREEN 3, cont.

DATAGROUP4, cont.

> E2-RELATIONSHIP TO PATIENT \|

> E2-STREET ADDRESS \[LINE 1\] \|

> E2-STREET ADDRESS \[LINE 2\] \|

> E2-STREET ADDRESS \[LINE 3\] \| Name/relationship/address/telephone number of

> E2-CITY \| secondary individual to contact in the event of an

> E2-STATE \| emergency

> E2-ZIP+4 \|

> E2-PHONE NUMBER \|

> E2-WORK PHONE \|

DATAGROUP5

D-DESIGNEE SAME AS NOK - YES/NO - Is the individual designated to receive patient's funds and effects the same as the next-of-kin? If YES, the next-of-kin information will be automatically inserted in the following fields and updated accordingly as the next-of-kin information is updated. If NO, the following fields will be prompted.

> D-NAME OF DESIGNEE

> D-RELATIONSHIP TO PATIENT \|

> D-STREET ADDRESS \[LINE 1\] \|

> D-STREET ADDRESS \[LINE 2\] \| Name/relationship/address/telephone number of

> D-STREET ADDRESS \[LINE 3\] \| individual designated to receive patient’s funds

> D-CITY \| and effects

> D-STATE \|

> D-ZIP+4 \|

> D-PHONE NUMBER \|

> D-WORK PHONE \|

Registration Supplement

APPLICANT/SPOUSE EMPLOYMENT DATA SCREEN \<4\>

PATIENT NAME;SSN TYPE

==================================================================

\[1\] Employer: \[2\] Spouse's:

Occupation:

Status:

Retired Dt.: Retired Dt.:

\<RET\> to CONTINUE, 1-2 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

OCCUPATION - Enter the applicant's occupation (1-30 characters)

EMPLOYMENT STATUS - If an entry other than NOT EMPLOYED, UNKNOWN, RETIRED, or no entry at all is made, the following fields will also be prompted. The data contained in these fields will automatically be deleted if the entry in this field is changed to UNEMPLOYED or no entry. You may enter a \<?\> to obtain a current list of choices.

> EMPLOYER NAME - Name of applicant's employer (1-30 characters). If an entry is made in this field, the following fields will also be prompted. The data contained in these fields will automatically be deleted upon deletion of the entry in this field. If no entry is made in this field, you will return to the screen.

> EMPLOYER STREET \[LINE 1\] \|

> EMPLOYER STREET \[LINE 2\] \|

> EMPLOYER STREET \[LINE 3\] \|

> EMPLOYER CITY \| Name/address/phone of employer

> EMPLOYER STATE \|

> EMPLOYER ZIP+4 \|

> EMPLOYER PHONE NUMBER \|

EMPLOYMENT RETIREMENT DATE – The optional Veteran Date of Retirement will only be prompted when the Employment Status value is ‘RETIRED’. Enter the date the veteran applicant retired from his/her place of employment. The data contained in this field will automatically be deleted if the entry in the veteran applicant’s Employment Status field is changed from ‘RETIRED’ to any other valid response.

DATAGROUP2

This data group will not be editable if the applicant does not have a marital status of MARRIED.

SPOUSE'S OCCUPATION - Enter the spouse's occupation (1-30 characters).

SPOUSE'S EMPLOYMENT STATUS - If an entry other than NOT EMPLOYED, UNKNOWN, RETIRED, or no entry is made, the following fields will also be prompted. The data contained in these fields will automatically be deleted if the entry in this field is changed to UNEMPLOYED or no entry. You may enter a \<?\> to obtain a current list of choices.

Registration Supplement

SCREEN 4, cont.

DATAGROUP2, cont.

> SPOUSE'S EMPLOYER NAME - Name of spouse's employer (3-20 characters). If an entry is made in this field, the following fields will also be prompted. The data contained in these fields will automatically be deleted upon deletion of the entry in this field.

> SPOUSE'S EMP STREET \[LINE 1\] \|

> SPOUSE'S EMP STREET \[LINE 2\] \|

> SPOUSE'S EMP STREET \[LINE 3\] \|

> SPOUSE'S EMP CITY \| Address/telephone number of spouse’s employer

> SPOUSE'S EMP STATE \|

> SPOUSE'S EMP ZIP+4 \|

> SPOUSE'S EMP PHONE NUMBER \|

SPOUSE’S EMPLOYMENT RETIREMENT DATE – The optional Spouse’s Date of Retirement will only be prompted when the Employment Status value is ‘RETIRED’. Enter the date the veteran’s spouse retired from his/her place of employment. The data contained in this field will automatically be deleted if the entry in the Spouse’s Employment Status field is changed from ‘RETIRED’ to any other valid response.

Registration Supplement

INSURANCE DATA SCREEN \<5\>

PATIENT NAME; SSN TYPE

============================================================================

\[1\] Covered by Health Insurance:

Insurance Co. Subscriber ID Group Holder Effective Expires

========================================================================

\[2\] Eligible for MEDICAID:

\[3\] Medicaid Number:

\<RET\> to CONTINUE, 1-3 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

Entry of insurance policy information for the patient uses the Integrated Billing package software.

COVERED BY HEALTH INSURANCE - YES/NO/UNKNOWN – If YES is answered, the following will appear.

> COVERED BY HEALTH INSURANCE changed to “NO”.

> This option adds or edits insurance information in the Insurance Buffer File. This is a temporary file that will hold all new insurance information until authorized insurance personnel can coordinate this new information with the patient’s existing insurance. You may add a new Buffer entry or edit a Buffer entry that you previously created for this patient if that entry has not yet been processed by insurance personnel.

> Please enter all available insurance information.

> Select INSURANCE COMPANY - Enter the name of the applicant's health insurance company. The insurance company must be active in your site's INSURANCE COMPANY file.

> Add a new Insurance Buffer entry for this patient? YES//

> PHONE NUMBER - Company phone number.

> BILLING PHONE NUMBER - Phone number of the company’s billing office.

> PRECERTIFICATION PHONE NUMBER - If this company requires pre-certification of insurance coverage to be completed prior to a patient being treated, enter the phone number of the pre-cert office.

> STREET ADDRESS \[LINE 1\] - Address of insurance company.

> STREET ADDRESS \[LINE 2\]

> CITY

> STATE

> ZIP CODE

Registration Supplement

SCREEN 5, cont.

DATAGROUP1,cont.

> GROUP NAME - Name the insurance company uses to identify the group plan (2-20 characters).

> GROUP NUMBER - Number that identifies this group policy (2-17 characters).

> BANKING IDENTIFICATION NUMBER - Enter the plan’s banking identification number (BIN) (1-10 characters).

> PROCESSOR CONTROL NUMBER (PCN) - Enter the plan’s processor control number (PCN) (1-20 characters).

> TYPE OF PLAN - Enter the type of insurance that best describes this policy. You may enter a \<?\> to obtain a current list of choices.

> EFFECTIVE DATE - Enter effective date of insurance policy for this patient.

> EXPIRATION DATE - Enter expiration date of insurance policy (leave blank if policy does not expire on a specific date).

> PT. RELATIONSHIP TO INSURED - Relationship of the patient to person holding insurance policy. You may enter a \<?\> to obtain a current list of choices.

> SUBSCRIBER PRIMARY ID - Enter the unique identification number assigned by the company (3-20 characters). You may enter \<??\> for an explanation of what number may be required here.

> NAME OF INSURED - Enter the name of the individual for which this policy was issued. If the “PT. Relationship to the Insured” is 'Patient', this field will default to the patient’s name.

> INSURED’S DOB: - Enter the date of birth of the person who holds the policy. Leave blank if the veteran is the patient and holds the policy.

> INSURED’S SEX: - Enter the sex of the person who holds the policy.

> PATIENT PRIMARY ID - This is the patient's primary ID number for this insurance company. Enter this field when the patient and the subscriber are different and the patient has a unique ID number.

DATAGROUP2

Eligible for MEDICAID - YES/NO - Is the patient eligible for Medicaid coverage?

DATAGROUP3

MEDICAID NUMBER - Enter the patient’s assigned Medicaid number, 3-30 characters.

Registration Supplement

With the release of DG\*5.3\*797, Military Service Data Sharing (MSDS) Project, the Military Service Data Screens have changed. ESR becomes the authoritative source for Military Service Episode (MSE) data. The verified data will be shared from ESR to all VistA sites of record for the veteran. The ESR-verified MSE cannot be edited by VistA except to add new episodes. A new MILITARY SERVICE EPISODE sub-file (#2.3216) was added to the PATIENT file (#2) to support an unlimited number of MSEs per veteran. MSEs already on file for a veteran when the new MSE sub-file is added, will remain in the patient record in the old locations in the data dictionary for historical purposes. A new screen 6.2 was added to display these old MSEs by selecting the View History action on Screen 6.1.

Whereas selecting “1” was previously used to enter MSEs, the user will now be taken to Screen 6.1 to Add/Edit/Delete or View History. The ESR-verified MSEs sent to VistA cannot be edited or deleted by VistA users. MSEs received from ESR are identified by \<\> on Screen 6.1 and cannot be selected to edit or delete. MSEs entered by the VistA site are identified by \[ \] on Screen 6.1 and can be edited or deleted. MSEs are no longer required to be entered in date order but still cannot overlap. All required data entry and Registration consistency checks still pertain to VistA entered MSEs. Consistency checks are not performed on ESR-verified MSEs.

MILITARY SERVICE DATA SCREEN \<6\>

PATIENT; SSN TYPE

===============================================================================

\[1\] Service Branch/Component Service# Entered Separated Discharge

------------------------ --------- ------- --------- --------

MARINE CORPS/REGULAR xxxxxxxxx 12/02/1990 05/04/1995 HONORABLE

MARINE CORPS/REGULAR xxxxxxxxx 10/11/1989 12/01/1990 HONORABLE

ARMY/REGULAR xxxxxxxxx 06/06/1986 10/10/1989 HONORABLE

\<more episodes\> selecting 1 at the prompt below will display all military service episodes

\[2\] Conflict Locations:

\[3\] Environment Factors:

\[4\] POW: From: To: War:

\[5\] Combat: From: To: Loc:

\[6\] Mil Disab Retirement: Dischrg Due to Disab:

\[7\] Dent Inj: Teeth Extracted:

\[8\] Purple Heart:

\<9\> Medal of Honor: YES

\<10\> Class II Dental Indicator: YES Dental Appl Due Before Date: 07/02/2011

\<RET\> to CONTINUE, 1-8 or ALL to EDIT, ^N for screen N or '^' to QUIT: selecting 1 will take the user to the new Screen 6.1

...SORRY, THIS MAY TAKE A FEW MOMENTS...

MILITARY SERVICE DATA, SCREEN \<6.1\>

Patient; SSN NSC VETERAN

Service Branch/Component Service \# Entered Separated Discharge

Enter ?? for more actions

AD Add DE Delete

ED Edit VH View History

Select Action:Quit//

Registration Supplement

SCREEN 6, cont.

To add a new Military Service Episode, select AD to add

Select Action:Quit// AD Add

SERVICE BRANCH: ARMY

SERVICE COMPONENT: REG REGULAR

SERVICE NUMBER: SS 666438928

SERVICE ENTRY DATE: 6/5/1986 (JUN 05, 1986)

SERVICE SEPARATION DATE: 7/10/1989 (JUL 10, 1989)

SERVICE DISCHARGE TYPE: HON

1 HONORABLE

2 HONORABLE-VA

CHOOSE 1-2: 1 HONORABLE

To Edit a VistA entered Military Service Episode, select ED to edit

Select Action:Quit// ED Edit

Select Episode: 1

SERVICE BRANCH: ARMY// NAVY

\*\* WARNING - BRANCH OF SERVICE WAS CHANGED SO THE COMPONENT WAS DELETED

SERVICE COMPONENT: REG REGULAR

SERVICE NUMBER: 666438928//

SERVICE ENTRY DATE: JUN 5,1986// 6/6/1986 (JUN 06, 1986)

SERVICE SEPARATION DATE: JUL 10,1989// 7/11/1989 (JUL 11, 1989)

SERVICE DISCHARGE TYPE: HONORABLE//

If a user selects an ESR-verified military service episode to edit, the following message is displayed:

“Select an episode to edit.

Only numbers in square brackets \[ \] are selectable.”

Please contact the HECAlert mail group or the HEC if you need to update

this information.

To Delete a VistA entered Military Service Episode, select DE to delete

Select Action:Quit// DE Delete

Select Episode: 1

Are you sure you want to delete this military service episode? NO// YES

If a user selects an ESR-verified military service episode to delete, the following message is displayed:

Select an episode to delete.

Only numbers in square brackets \[ \] are selectable.

Please contact the HECAlert mail group or the HEC if you need to update

this information.  
Registration Supplement

SCREEN 6, cont.

Selecting VH View History, will take the user to Screen 6.2

VISTA MILITARY SERVICE DATA, SCREEN \<6.2\>

Patient; SSN NSC VETERAN

Service Branch/Component Service \# Entered Separated Discharge

Select Action:Quit//

When entering ?, ??, ??? or an invalid value at the prompt, help for Screen 6 is displayed.

MILITARY SERVICE DATA SCREEN \<6\>

PATIENT; SSN TYPE

===============================================================================

\[1\] Service Branch/Component Service# Entered Separated Discharge

------------------------ --------- ------- --------- --------

MARINE CORPS/REGULAR xxxxxxxxx 12/02/1990 05/04/1995 HONORABLE

MARINE CORPS/REGULAR xxxxxxxxx 10/11/1989 12/01/1990 HONORABLE

ARMY/REGULAR xxxxxxxxx 06/06/1986 10/10/1989 HONORABLE

\<more episodes\> selecting 1 at the prompt below will display all military service episodes

\[2\] Conflict Locations:

\[3\] Environment Factors:

\[4\] POW: From: To: War:

\[5\] Combat: From: To: Loc:

\[6\] Mil Disab Retirement: Dischrg Due to Disab:

\[7\] Dent Inj: Teeth Extracted:

\[8\] Purple Heart:

\<9\> Medal of Honor: YES

\<10\> Class II Dental Indicator: YES Dental Appl Due Before Date: 07/02/2011

\<RET\> to CONTINUE, 1-8 or ALL to EDIT, ^N for screen N or '^' to QUIT: ??

                    MILITARY SERVICE DATA, SCREEN \<6\> HELP

===============================================================================

Enter '^' to stop the display and edit of data, '^N' to jump to screen \#N (see

listing below), \<RET\> to continue on to the next available screen or enter

the field group number(s) you wish to edit using commas and dashes as

delimiters.  Those groups enclosed in brackets "\[\]" are editable while those

enclosed in arrows "\<\>" are not.  Enter 'ALL' to edit all editable data

elements on the screen.

DATA GROUPS ON SCREEN 6

\[1\]  Service History                    \[2\]  Conflict Locations

\[3\]  Exposure Factors                   \[4\]  Prisoner of War

\[5\]  Combat                             \[6\]  Military Retirement/Disability

\[7\]  Dental History                     \[8\]  Purple Heart Recipient

\<9\>  Medal of Honor                     \<10\> Class II Dental Indicator

AVAILABLE SCREENS

\[^1\]  Demographic Data                  \[^1.1\] Confidential Address Data

\[^2\]  Patient Data                      \[^3\]  Contact Data

\[^4\]  Employment Data                   \[^5\]  Insurance Data

Registration Supplement

SCREEN 6, cont.

\[^6\]  Service Record Data               \[^7\]  Eligibility Data

\[^8\]  Family Demographic Data           \[^9\]  Income Screening Data

\[^10\] Missing/Ineligible Data           \[^11\] Eligibility Verification Data

\[^12\] Admission Info Data               \[^13\] Application Info Data

\[^14\] Appointment Info Data             \[^15\] Sponsor Demographics Data

Press \<RETURN\> KEY TO EXIT SCREEN 6 HELP

Entry/edit of data contained in the various data groups of this screen will be restricted to holders of the DG ELIGIBILITY security key once the applicant's eligibility has been verified. Prior to eligibility verification, any user may enter/edit data on this screen. After verification, the data may be viewed by all users but only edited by holders of the DG ELIGIBILITY security key. All date fields entered must include, at a minimum, a month and a year. Any changes to existing dates to less precise dates is not allowed.

DATAGROUP1

SERVICE BRANCH - Name, number or abbreviation of applicant's branch of service. Enter a \<?\> for a list from which to select. If no entry is made in this field, you will return to the screen. All fields (except service number) are required to complete Data Group 1.

SERVICE COMPONENT - Name, number or abbreviation of veteran’s service component relating to the veteran’s most current branch of service. Enter a \<?\> for a list from which to select. All fields (except service number and service component) are required to complete Data Group 1. If a branch of service is changed or deleted, its associated service component is also deleted, and a warning displays on your screen.

- You may choose to enter a service component after selecting a branch of service if it pertains to one of the following groups:
  - Army
  - Navy
  - Marine Corps
  - Air Force
  - Coast Guard
  - Public Health Service
  - NOAA.
- A Service Component is based upon one of the following factors:
  - Regular
  - Activated Reserve
  - Activated National Guard

Registration Supplement

SCREEN 6, cont.

DATAGROUP1, cont.

- Activated Reserve is accepted only if the branch of service is one of the following:
  - Army
  - Navy
  - Marine Corps
  - Air Force
  - Coast Guard
- Activated National Guard is accepted only if the branch of service is one of the following:
  - Army
  - Air Force

> FILIPINO VETERAN PROOF - (This prompt appears only if branch of service entered was Filipino Commonwealth (F. Commonwealth), Filipino Guerilla Forces (F. Guerilla,) or New Filipino Scout (F. Scout New). Documentation provided to establish US Citizenship, lawful permanent residency, and/or VA Compensation at full-dollar rate for a Filipino Veteran. Enter a \<?\> for a list from which to select. The proof (abbreviated) displays in parenthesis to the right of the Service Branch field.

> SERVICE NUMBER - Applicant's service number (1-15 characters).

> If same as social security number, enter SS.

> SERVICE ENTRY DATE - Entry date for episode of service.

> SERVICE SEPARATION DATE - Separation date for episode of service.

> SERVICE DISCHARGE TYPE - Discharge Type for episode of service.

> You may enter a \<?\> to obtain a current list of choices. . With the release of DG\*5.3\*797, MSDS Project, two new Discharge Types were added to the TYPE OF DISCHARGE file (#25) to be consistent with the discharge types sent to ESR from VADIR/BIRLS.

- Honorable
- Dishonorable
- General
- Other Than Honorable
- Undesirable
- Bad Conduct
- Dishonorable-VA – Dishonorable for VA purposes means that for the VBA, there is another reason or circumstance that the VBA has determined that makes the Veteran “Dishonorable” for VA purposes. The Veteran is not eligible for enrollment in the VA Health Care Program.  If SC conditions exist, they may be treated for the SC conditions only.
- Honorable-VA – Honorable for VA purposes means that for the VBA, even though their DD-214 says “General” or “Other Than Honorable”, there is another reason or circumstance that the VBA has determined that makes the Veteran “Honorable” for VA purposes.

Registration Supplement

SCREEN 6, cont.

DATAGROUP2

CONFLICT LOCATIONS - This data group provides a collection of data fields that allow you to enter conflict FROM and TO dates and Operation Enduring and Iraqi Freedom (OEF/OIF) source. When you select this data group from Screen 6, you can add/edit/delete the conflict information via the CONFLICT LOCATIONS sub screen. You can only edit OEF/OIF data entered by your site; you cannot edit any OEF/OIF data received from the HEC. You can add multiple OEF and OIF Conflict Locations to a patient’s record.

- The following rules apply to OEF/OIF Conflict Locations start and end dates:
  - The Start date for each OEF Conflict Location must be greater than or equal to 09/01/2001.
  - The End date for each OEF Conflict Location must be greater than 09/11/2001.
  - The Start date for each OIF Conflict Location must be greater or equal to 03/01/2003.
  - The End for each OIF Conflict Location date must be greater than 03/19/2003.
  - The Start date for each UNKNOWN OEF/OIF Conflict Location must be greater than or equal to 09/01/2001.
  - The End date for each UNKNOWN OEF/OIF Conflict Location must be greater than 09/11/2001.
- OEF/OIF Start and End dates entered at the site must fall within the patient’s dates of military service, and cannot overlap any other OEF, OIF, or UNKNOWN OEF/OIF conflict, with the following exception:
  - OEF or OIF Conflict Location may be entered if the Start and End dates match exactly to those of an UNKNOWN OEF/OIF Conflict Location on file. This will trigger the HEC system to automatically change the UNKNOWN OEF/OIF to the corresponding OEF or OIF episode when processing the HL7 Z07 transmission from VistA to HEC. The results are sent to all sites of record and the UNKNOWN OEF/OIF episode is deleted from VistA.
- When OEF or OIF Conflict Location is added to a patient’s record, the DATE/TIME STAMP is recorded.

Registration Supplement

SCREEN 6, cont.

DATAGROUP2, cont.

> LEBANON SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the LEBANON SERVICE

> INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be after 10/1/83.

> LEBANON FROM DATE - Beginning date of service in Lebanon.

> LEBANON TO DATE - Ending date of service in Lebanon.

> GRENADA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the GRENADA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be between 10/23/83 and 11/21/83.

> GRENADA FROM DATE - Beginning date of service in Grenada.

> GRENADA TO DATE - Ending date of service in Grenada.

> PANAMA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the PANAMA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be between 12/20/89 and 1/31/90.

> PANAMA FROM DATE - Beginning date of service in Panama.

> PANAMA TO DATE - Ending date of service in Panama.

> SOMALIA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the SOMALIA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be after 09/28/92.

> SOMALIA FROM DATE - Beginning date of service in Somalia.

> SOMALIA TO DATE - Ending date of service in Somalia.

Registration Supplement

SCREEN 6, cont.

DATAGROUP2, cont.

> YUGOSLAVIA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the YUGOSLAVIA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be 6/22/92 or later.

> YUGOSLAVIA FROM DATE - Beginning date of service in Yugoslavia.

> YUGOSLAVIA TO DATE - Ending date of service in Yugoslavia.

> VIETNAM SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the VIETNAM SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be between 02/28/61 and 05/07/75.

> VIETNAM FROM DATE - Beginning date of service in Vietnam.

> VIETNAM TO DATE - Ending date of service in Vietnam.

> PERSIAN GULF SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the PERSIAN GULF SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. Entries in the following fields must be 8/2/90 or later.

> PERSIAN GULF FROM DATE - Beginning date of service in Persian Gulf.

> PERSIAN GULF TO DATE - Ending date of service in Persian Gulf.

DATAGROUP3

ENVIRONMENT FACTORS - This data group provides a collection of data fields that allow you to enter environmental factor exposure methods. When you select this data group from Screen 6, you can add/edit/delete the following environmental factors exposure methods via the ENVIRONMENTAL FACTORS sub screen.

> AGENT ORANGE EXPOS. INDICATED - YES/NO/UNKNOWN - If YES, only AO Exposure Location is required. All remaining fields are optional. Entries cannot be deleted as long as the AGENT ORANGE EXPOS. INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted.

Registration Supplement

SCREEN 6, cont.

DATAGROUP3, cont.

> AGENT ORANGE REGISTRATION DATE - Date applicant registered as having been exposed to Agent Orange.

> AGENT ORANGE EXAM DATE - Date applicant was examined for Agent Orange exposure.

> AGENT ORANGE REGISTRATION \# - Agent Orange Registration \# assigned to applicant.

> AGENT ORANGE EXPOSURE LOCATION - Location where patient was exposed to Agent Orange; Vietnam or Korean DMZ.

> RADIATION EXPOSURE INDICATED - YES/NO/UNKNOWN - Only RADIATION EXPOSURE INDICATED is required. All remaining fields are optional. Entries cannot be deleted as long as the RADIATION EXPOSURE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted.

> RADIATION EXPOSURE METHOD 2 for HIROSHIMA/NAGASAKI

> 3 for ATMOSPHERIC NUCLEAR TESTING

> 4 for H/N AND ATMOSPHERIC TESTING

> 5 for UNDERGROUND NUCLEAR TESTING

> 6 for EXPOSURE AT NUCLEAR FACILITY

> 7 for OTHER

> RADIATION REGISTRATION DATE - Date applicant registered as having been exposed to radiation.

> SW ASIA CONDITIONS - YES/NO/UNKNOWN – If YES, veteran claims need for care of conditions related to service in SW Asia. If NO, veteran did not serve in SW Asia or does not claim need for care of conditions related to service in SW Asia. If UNKNOWN, veteran served in SW Asia but is unsure of whether conditions may be related to that service. If YES, the following two prompts will appear.

> SW ASIA COND. REGISTRATION DATE: Date on which this patient was registered as being exposed to conditions related to service in SW Asia (must be after 8/1/90). If the year is omitted, the system uses the current year.

> SW ASIA COND. EXAM DATE: Date patient was examined for exposure to conditions related to service in SW Asia. Date must be before current date.

> *SW Asia Theater of Operations is defined as Iraq, Kuwait, Saudi Arabia, the neutral zone between Iraq and Saudi Arabia, Bahrain, Qatar, the United Arab Emirates, Oman, the Gulf of Aden, the Gulf of Oman, the Persian Gulf, the Arabian Sea, the Red Sea, and the airspace above these locations.*Registration Supplement

SCREEN 6, cont.

DATAGROUP3, cont.

> DID YOU RECEIVE NOSE OR THROAT RADIUM TREATMENTS IN THE MILITARY? - YES/NO/UNKNOWN - Does this patient claim to have received nose and/or throat radium treatment while in the military? If YES, the following two prompts will appear if the veteran's service entry dates precede the dates in the question text.

> DID YOU SERVE AS AN AVIATOR IN THE MILITARY BEFORE JAN 31, 1955? - YES/NO.

> DID YOU HAVE SUBMARINE TRAINING IN THE MILITARY BEFORE JAN 1, 1965? - YES/NO.

> If the user holds the DGNT VERIFY security key, the following will be prompted.

> DO YOU WANT TO VERIFY NOW? - YES/NO - If YES, the following will be prompted.

> NOSE AND THROAT RADIUM TREATMENT VERIFIED BY: - (M) Military Medical Record, (S) Qualifying Military Service, (N) Not Qualified. If "M" or "S", the following will be prompted.

HAS VETERAN BEEN DIAGNOSED WITH CANCER OF THE HEAD AND/OR

NECK? - YES/NO

DATAGROUP4

POW STATUS INDICATED - YES/NO/UNKNOWN - If YES, all POW fields are required to complete the POW data group. Entries cannot be deleted as long as the POW STATUS INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted. These fields cannot be edited after the patient’s eligibility is verified by the HEC. If NO is received from ESR, the POW fields are deleted and the veteran will be reevaluated for enrollment.

> POW CONFINEMENT LOCATION - War in which applicant was a POW.

> POW FROM DATE - Beginning date applicant was a POW.

> POW TO DATE - Ending date applicant was a POW.

DATAGROUP5

COMBAT SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the COMBAT SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields will automatically be deleted.

> COMBAT SERVICE LOCATION - War in which applicant saw combat.

> COMBAT FROM DATE - Beginning date applicant was in combat.

COMBAT TO DATE - Ending date applicant was in combat.

Registration Supplement

SCREEN 6, cont.

DATAGROUP6

MILITARY DISABILITY RETIREMENT: Enter ‘Y’ if this veteran applicant is receiving disability retirement pay from the Military instead of VA compensation. Enter ‘N’ if this veteran applicant is not receiving disability retirement pay from the Military instead of VA compensation. Once eligibility has been verified by the HEC, this field will no longer be editable by VistA users. Send updates and/or requests to the HEC. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

DISCHARGE DUE TO DISABILITY: Enter ‘Y’ if this veteran applicant was discharged from the military for a disability incurred or aggravated in the line of duty. Enter ‘N’ if this veteran applicant was not discharged from the military for a disability incurred or aggravated in the line of duty. Once eligibility has been verified by the HEC, this field will no longer be editable by VistA users. Send updates and/or requests to the HEC. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

DATAGROUP7

SERVICE DENTAL INJURY - YES/NO - Did the applicant have a dental injury while in service? If YES, SERVICE TEETH EXTRACTED is defaulted to NO. The remaining fields are optional.

SERVICE TEETH EXTRACTED - YES/NO - Did the applicant have teeth extracted while in service?

> Select DATE OF DENTAL TREATMENT - At this field, the date of the applicant's dental treatment should be entered. If it is a date that has not been entered in the past for the applicant, you will be prompted for confirmation that you are entering a new date of dental treatment. This is a multiple field. You will be returned to this prompt repeatedly until no more dates are entered. For each date entered, the following two fields will be prompted before returning you to this prompt.

> CONDITION - Dental condition treated, place of treatment, and from whom the treatment was received.

> DATE CONDITION FIRST NOTICED - Date the dental condition was first noticed.

Registration Supplement

SCREEN 6, cont.

DATAGROUP8

CURRENT PH (purple heart) INDICATOR - YES/NO/NULL - If YES, the STATUS field is automatically set to PENDING and further display of Screen 6 will add this field to the display. If NO, the REMARKS field is automatically set to VAMC and further display of Screen 6 will add this field to the display. If YES or NO is entered, you will be prompted for DIVISION at multi-divisional sites.

This data group becomes inactive if the CURRENT PH INDICATOR field is answered and the consistency check is completed.

> STATUS - Values include Pending, In Process, Confirmed. This field is not editable by the user.

> REMARKS - Values include Unacceptable Documentation, No Documentation Received, Entered in Error, Unsupported Purple Heart, VAMC, Undeliverable Mail. This field is not editable by the user. This field will only contain a value if the CURRENT PH INDICATOR field is NO.

DATAGROUP9

> CURRENT MOH Indicator – YES/NO/NULL – The Current MOH Indicator field will be received by VistA from ESR. It is only displayed on Screen 6 if the value is YES and is not editable by the user.

DATAGROUP10

The Class II Dental Indicator is “display only”.

The Class II Dental Application Due Before Date is “display only”.

> The Class II Dental Application Due Before Date is displayed, only if the Class II Dental Indicator field is YES.

Registration Supplement

Users may enter the following VA Pension data:

- Receiving a VA Pension?
- Pension Award Effective Date
- Pension Award Effective Reason

ELIGIBILITY STATUS DATA, SCREEN \<7\>

PATIENT; SSN TYPE

===============================================================================

\[1\] Patient Type: NSC VETERAN Veteran: YES

Svc Connected: NO SC Percent: N/A

Rated Incomp.: UNANSWERED

Claim Number: UNANSWERED

Folder Loc.: UNANSWERED

\[2\] Aid & Attendance: NO Housebound: NO

VA Pension: YES

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED Amount: UNANSWERED

\[3\] Primary Elig Code: NSC, VA PENSION

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: PERSIAN GULF WAR

\[4\] Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT: 2

COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

PATIENT; SSN TYPE

===============================================================================

Aid & Attendance: NO

Housebound: NO

VA Pension: YES

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?: NO//

RECEIVING HOUSEBOUND BENEFITS?: NO//

RECEIVING A VA PENSION?: YES//

PENSION AWARD EFFECTIVE DATE: 1/1/2008 (JAN 01, 2008)

PENSION AWARD REASON: ??

Enter the Pension Award Reason only if VA Pension (#.36235) field

is equal to "Yes". VistA users are only allowed to enter a

Pension Award Reason of "Original Award" (106). This field is

optional. If Pension Award Reason is entered, an Award Date

must be entered.

Choose from:

Original Award

PENSION AWARD REASON: Original Award

RECEIVING VA DISABILITY?:

Registration Supplement

SCREEN 7, cont.

TOTAL ANNUAL VA CHECK AMOUNT:

GI INSURANCE POLICY?:

ELIGIBILITY STATUS DATA, SCREEN \<7\>

PATIENT; SSN TYPE

===============================================================================

\[1\] Patient Type: NSC VETERAN Veteran: YES

Svc Connected: NO SC Percent: N/A

Rated Incomp.: UNANSWERED

Claim Number: UNANSWERED

Folder Loc.: UNANSWERED

\[2\] Aid & Attendance: NO Housebound: NO

VA Pension: YES Pension A/T Date: JAN 1,2008

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED Amount: UNANSWERED

\[3\] Primary Elig Code: NSC, VA PENSION

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: PERSIAN GULF WAR

\[4\] Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT:

When the HEC sends authoritative VA Pension data, it will lock the record from editing and display a message to the user.

The following rules apply to locking the VA Pension Data:

If no Pension Award Termination information is received and the Pension Award Reason is null or any value other than “Original Award”, the VA Pension Indicator will be locked from editing however, the user will be able to edit the Pension Award Effective Date and Pension Award Reason”. Only “Original Award” may be selected by the user.

COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

PATIENT; SSN TYPE

===============================================================================

Aid & Attendance: UNANSWERED

Housebound: UNANSWERED

VA Pension: YES

Pension Award Effective Date: AUG 1,2010

Pension Award Reason: Benefit Change to Compensation

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

Registration Supplement

SCREEN 7, cont.

RECEIVING A&A BENEFITS?:

RECEIVING HOUSEBOUND BENEFITS?:

Pension Award Date and Pension Award Reason are editable only if VA Pension Indicator is Yes and Pension Award Reason is not 'Original Award'. For any other assistance, use the HEC Alert process.

PENSION AWARD EFFECTIVE DATE: AUG 1,2010// 12/01/09 (DEC 01, 2009)

PENSION AWARD REASON: Benefit Change to Compensation // Original Award

RECEIVING VA DISABILITY?: NO//

TOTAL ANNUAL VA CHECK AMOUNT: 12000//

GI INSURANCE POLICY?:

When VA Pension termination information is received from HEC, it will be displayed on the Screen 7 Expansion screen and locked from editing.

COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

PATIENT; SSN TYPE

===============================================================================

Aid & Attendance: NO

Housebound: NO

VA Pension: NO

Pension Terminated Date: SEP 9,2011

Pension Terminated Reason 1: Apportionment Terminated

Pension Terminated Reason 2: CONV - Disability Not Shown by Evidence

Pension Terminated Reason 3: Failed to Furnish Requested Evidence

Pension Terminated Reason 4: Terminated-Other

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?: NO//

RECEIVING HOUSEBOUND BENEFITS?: NO//

Pension Award Date and Pension Award Reason are editable only if VA Pension Indicator is Yes and Pension Award Reason is not 'Original Award'. For any other assistance, use the HEC Alert process.

RECEIVING VA DISABILITY?:

GI INSURANCE POLICY?:

Entry/edit of data contained in the various data groups of this screen will be restricted to holders of the DG ELIGIBILITY security key once the applicant's eligibility has been verified. (The PERIOD OF SERVICE field of Data Group 3 may not be edited by a user not holding the DG ELIGIBILITY security key if either the applicant's eligibility or service record (or both) have been verified.) Prior to eligibility verification, any user may enter/edit data on this screen. After verification, the data may be viewed by all users but only edited by holders of the DG ELIGIBILITY security key.

  
Registration Supplement

SCREEN 7, cont.

DATAGROUP1

TYPE - This field will always contain a default; that entry which was made initially upon entering the patient into the data base or when the MAS V. 4.0 conversion was run which automatically assigned a patient type to each existing patient. You may change the patient's type at this prompt. Any changes may alter the availability of certain screens and/or editing of certain data depending upon site parameters. Enter a \<?\> for a list of patient types from which to select. When the VETERAN (Y/N) field is changed from YES to NO, the data values in some fields will be deleted (set to null); however, this field will not be changed automatically.

VETERAN (Y/N) - This field will always contain a default; that entry which was made when the patient was initially entered into the data base. You may change the patient's veteran status at this prompt. Such a change may alter the availability of certain screens and/or editing of certain data depending upon site parameters.

SERVICE CONNECTED - YES/NO - Does the patient have any conditions for which he has received a service-connected rating from the Dept. of Veterans Affairs? If YES, the following will also be prompted. The data contained in the following field will automatically be deleted if this field is changed to NO. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

Registration Supplement

SCREEN 7, cont.

DATAGROUP1, cont.

SERVICE CONNECTED PERCENTAGE - Applicant's total combined sc percentage. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

> P&T - YES/NO - Is the patient rated permanently and totally disabled by the VA due to a service-connected condition?

> P&T Effective Date – Enter the effective date the patient was awarded P&T disability status by VARO. This field is optional; however, if a date is entered, it must be a precise date (day/month/year must be included) and cannot be after the date of death. If P&T is changed from YES to NO or it is deleted, this field is deleted. This field cannot be edited after the patient’s eligibility has been verified by the HEC.

> SC AWARD DATE: - Date on which service connection is effective based on VBA decision. Can be obtained from either HINQ or the award letter. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

RATED INCOMPETENT?: - YES/NO - Used by AMIE. If YES, the following will also be prompted. The data contained in the following fields will automatically be deleted if this field is changed to NO. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in all fields in this data group.

> DATE RULED INCOMPETENT (CIVIL) - Enter the date the patient was ruled incompetent to handle his funds by civil authorities. Date Ruled Incompetent (Civil) cannot be after the Date of Death.

> DATE RULED INCOMPETENT (VA) - Enter the date the patient was ruled incompetent to handle his funds by the VA. Date Ruled Incompetent (VA) cannot be after the Date of Death.

CLAIM NUMBER - Applicant's claim number, if any. If same as social security number, you may enter SS.

CLAIM FOLDER LOCATION – Enter the location of the applicant's claim folder (institution name or station number) only if it is an active facility and it has one of the following facility types in support of ESR:

RO (Regional Office)

RO&IC (Regional Office and Insurance Center)

RO-OC (Regional Office - Outpatient Clinic)

RPC (Record Processing Center)

M&ROC (Medical and Regional Office Center)

M&ROC (M&RO) (Medical and Regional Office Center)

  
Registration Supplement

SCREEN 7, cont.

DATAGROUP2

Depending upon site parameters set forth in the Patient Type Update option, Supervisor ADT menu, the system may require the applicant to be a veteran in order to make entries into these fields.

RECEIVING A&A BENEFITS - YES/NO/UNKNOWN - Is applicant in receipt of Aid and Attendance? When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

RECEIVING HOUSEBOUND BENEFITS - YES/NO/UNKNOWN - Is applicant in receipt of Housebound benefits? When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

RECEIVING A VA PENSION - YES/NO/UNKNOWN - Is applicant in receipt of a VA pension? When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

PENSION AWARD EFFECTIVE DATE - What is the effective date of the original award of the VA Pension Benefit or the latest date of change to the VA Pension Award?

Editing of The Pension Award Effective Date is allowed only if the VA Pension Indicator is set to YES. Users are allowed to change the “Pension Award Effective Date” only if the “Pension Award Reason” is being changed to “Original Award” from some other value. Pension Award Effective Date must be less than or equal to the current system date. The Pension Award Effective Date is not a required field (even if Pension Indicator is set to YES)

PENSION AWARD REASON - What is the reason for the Pension Award? Select from the available choices. The Pension Award Reason is not a required field.

PENSION TERMINATION DATE – This field is displayed when updated by the HEC and is not editable by the user.

PENSION TERMINATION REASON 1 through 4 – These fields are displayed when updated by the HEC and is not editable by the user.

RECEIVING VA DISABILITY - YES/NO/UNKNOWN - Is applicant in receipt of VA disability monies? When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

TOTAL ANNUAL VA CHECK AMOUNT: - If this applicant is receiving A&A, Housebound, Pension, and/or disability payments from the VA (at least one of the questions relating to the above must be answered YES), enter the annual amount received. Once monetary benefits are verified, only users who hold the designated security key may enter/edit this field. This field may not be deleted as long as receipt of VA funds is indicated and will automatically be deleted if all of the above are changed to NO. If you wish to enter a monthly amount either precede or follow it with an asterisk (\*) and it will be multiplied out by the system. When the VETERAN (Y/N)? field is changed from YES to NO, the data values will be deleted (set to Null) in this field.

  
Registration Supplement

SCREEN 7, cont.

DATAGROUP2, cont.

GI INSURANCE POLICY - YES/NO/UNKNOWN - Does applicant have GI Insurance? If YES, the following field will be prompted. The data entered will automatically be deleted if NO is later entered in this field.

> AMOUNT OF GI INSURANCE - Dollar/cents amount of GI Insurance (between 0-9999999).

DATAGROUP3

PRIMARY ELIGIBILITY CODE - Eligibility code based on the applicant's veteran/non-veteran status. System only allows entry of eligibility codes compatible with previously entered data. A \<?\> may be entered for a list of selectable eligibility codes for the patient being entered. An entry in this field is required in order to process a patient's application for health benefits. If an entry of "Allied Veteran" or "Other Federal Agency" is made, the following will be prompted. When the VETERAN (Y/N) field is changed from YES to NO, the data values in some fields will be deleted (set to null); however, this field will not be changed automatically. It's possible that the ELIGIBILITY TYPE field (#4) of the ELIGIBILITY CODE file (#8) will still refer to a veteran. This will result in an Inconsistency \# 19 - ELIG/NONVET STAT INCONSISTENT. You must assign the correct PRIMARY ELIGIBILITY to remove the inconsistency.

Also, if the PATIENT ELIGIBILITIES multiple (#361) contains any of the following, that eligibility will be removed:

- SC LESS THAN 50%
- SERVICE CONNECTED 50% to 100%
- NSC, VA PENSION
- AID & ATTENDANCE
- HOUSEBOUND
- ALLIED VETERAN

> AGENCY/ALLIED COUNTRY - Name of federal agency or allied country under whose auspices applicant is applying for care. Enter a \<?\> for a list of choices.

Select ELIGIBILITY - This entry will always contain a default, the entry made at the PRIMARY ELIGIBILITY field. Enter any other eligibility code(s) under which applicant is entitled to care. Entry must be compatible with previously entered data. You may enter a \<?\> for a list from which to select.

> ELIGIBILITY - This entry will always contain a default, the entry at the Select ELIGIBILITY field. Edit the eligibility code here, if necessary.

PERIOD OF SERVICE - Applicant's period of service eligibility code must be answered in order to respond to this prompt. Response must be compatible with eligibility code. Enter a \<?\> for a list of applicable periods of service from which to choose. Only holders of the DG ELIGIBILITY security key may edit this field. Once eligibility verification has been completed, you will be unable to edit this field if the applicant's service record has been verified.

Registration Supplement

SCREEN 7, cont.

DATA GROUP 3.2

If the SHAD Exposure Indicator is set to “YES”, Data Group 3.2 is displayed. This indicator can be modified by the HEC only. If the indicator is changed to “NO” or deleted by the HEC, Data Group 3.2 will no longer be displayed.

DATAGROUP4

Select SERVICE CONNECTED CONDITIONS - Enter the conditions for which the applicant claims service connection.

> SERVICE CONNECTED CONDITIONS - This entry will always contain a default, the entry at the Select SERVICE CONNECTED CONDITIONS field. Edit the eligibility code here, if necessary.

> PERCENTAGE: - Enter percent of service connection.

The INCOME DATA MISSING field (#.301) will no longer be generated for the following conditions:

- SERVICE CONNECTED less than 50%
- SERVICE CONNECTED PERCENTAGE is 10% or greater
- NSC VA PENSION
- AID & ATTENDANCE

Registration Supplement

<u>Dependents Module Date/Time Page: 1 of 1</u>

FAMILY DEMOGRAPHIC DATA, SCREEN \<8\>

Patient Name; (SSN)

<u>MT Patient/Dependent Relationship Active Address</u>

1 Patient Name SELF \* \*

Married Last Year:

Enter ?? for more actions

DA Spouse/Dependent Add MT Marital/Dependent Info

ES Spouse Demographic AD Add to Means/Copay Test

DD Dependent Demographic RE Remove from Means/Copay Test

DP Delete Dependent ED Expand Dependent

Select Action: Quit//

An asterisk in the "Active" column indicates the individual is an active dependent.

An asterisk in the "MT" column identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

SSN – After the SSN status is verified by the SSA, it can only be edited by members of the Identity Management Data Quality Team, and VERIFIED is displayed next to the SSN. If the SSN status is INVALID per SSA, INVALID is displayed next to the SSN.

DA Spouse/Dependent Add - Allows the user to add a new dependent (spouse or other).

Do you want to add (S)pouse or (D)ependent: - If spouse selected, the following fields will be prompted.

> SPOUSE'S NAME \| Demographic information for the veteran’s spouse

> SPOUSE'S SEX \|

> SPOUSE'S DATE OF BIRTH \|

> SPOUSE'S SSN \| If entering a Pseudo SSN, you must also enter a Pseudo

> \| SSN Reason.

> EFFECTIVE DATE \| Date this individual became a dependent of the veteran.

> \| For spouse, date of marriage.

> SPOUSE’S MAIDEN NAME

> SPOUSE’S STREET ADDRESS SAME AS PATIENT’S

> SPOUSE’S STREET ADDRESS \[LINE 1\]

> SPOUSE’S STREET ADDRESS \[LINE 2\]

> SPOUSE’S STREET ADDRESS \[LINE 3\]

> SPOUSE’S CITY

> SPOUSE’S STATE

> SPOUSE’S ZIP+4

> SPOUSE’S PHONE NUMBER

Registration Supplement

SCREEN 8, cont.

> Changes were made to the INCOMPLETE PHONE NUMBER field (#61). The system will automatically check for the following fields: NULL PHONE NUMBER \[RESIDENCE\] (#131), NULL PHONE \[WORK\] NUMBER (#132).

> The information generated from this field will display the following options.

> Patient is EMPLOYED FULL TIME

> Patient is EMPLOYED PART TIME

> Patient is SELF EMPLOYED

If Dependent selected, the following fields will be prompted.

> CHILD'S NAME \| Demographic information for each

> CHILD'S SEX \| of the veteran's dependents.

> CHILD'S DATE OF BIRTH \|

> CHILD'S SSN \| If entering a Pseudo SSN, you must also enter a Pseudo

> \| SSN Reason.

> RELATIONSHIP \|

> EFFECTIVE DATE \| For a child, date of birth or adoption.

> \| For a stepchild, date of marriage to the child’s parent.

> CHILD’S STREET ADDRESS SAME AS PATIENT’S

> CHILD’S STREET ADDRESS SAME AS SPOUSE’S

> CHILD’S STREET ADDRESS \[LINE 1\]

> CHILD’S STREET ADDRESS \[LINE 2\]

> CHILD’S STREET ADDRESS \[LINE 3\]

> CHILD’S CITY

> CHILD’S STATE

> CHILD’S ZIP+4

ES Spouse Demographic - Allows the user to edit demographic data related to the spouse.

> NAME

> SEX

> DATE OF BIRTH

> SOCIAL SECURITY NUMBER

> EFFECTIVE DATE: (date - date)

> Date {dependent name} no longer a dependent: (date - date)

> SPOUSE’S MAIDEN NAME

> SPOUSE’S STREET ADDRESS SAME AS PATIENT’S

> SPOUSE’S STREET ADDRESS \[LINE 1\]

> SPOUSE’S STREET ADDRESS \[LINE 2\]

> SPOUSE’S STREET ADDRESS \[LINE 3\]

> SPOUSE’S CITY

> SPOUSE’S STATE

> SPOUSE’S ZIP+4

> SPOUSE’S PHONE NUMBER

Registration Supplement

SCREEN 8, cont.

DD Dependent Demographic - Allows the user to edit demographic data related to dependents. There must be an existing dependent on file (other than the spouse) to select this protocol. The selected dependent has to be active.

> NAME

> SEX

> DATE OF BIRTH

> SOCIAL SECURITY NUMBER

> RELATIONSHIP

> EFFECTIVE DATE: (date - date)

> DEPENDENT’S STREET ADDRESS SAME AS PATIENT’S

> DEPENDENT’S STREET ADDRESS SAME AS SPOUSE’S

> DEPENDENT’S STREET ADDRESS \[LINE 1\]

> DEPENDENT’S STREET ADDRESS \[LINE 2\]

> DEPENDENT’S STREET ADDRESS \[LINE 3\]

> DEPENDENT’S CITY

> DEPENDENT’S STATE

> DEPENDENT’S ZIP+4

DP Delete Dependent - Allows the user to delete a dependent (mainly duplicate dependents). You must hold the DG DEPDELETE security key to use this protocol. In order to delete a dependent, they must be removed from <u>every</u> Means Test (using the RE protocol). There are no prompts associated with this protocol.

MT Marital/Dependent Info - Allows the user to enter/edit last year's marital status.

> MARRIED LAST CALENDAR YEAR (Y/N)

AD Add to Means/Copay TestRE Remove from Means/Copay Test

These protocols are not selectable from the registration screens.

Registration Supplement

SCREEN 8, cont.

ED Expand Dependent - This protocol will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).

> Select EFFECTIVE DATE - Select the effective date you wish to edit.

> EFFECTIVE DATE: {date}// - Enter correct date.

> ACTIVE - If this change in status makes the dependent effective, enter 1 or YES for active. If the change makes the individual no longer dependent, enter 0 or NO.

> SPOUSE’S MAIDEN NAME

> SPOUSE’S STREET ADDRESS SAME AS PATIENT’S

> SPOUSE’S STREET ADDRESS \[LINE 1\]

> SPOUSE’S STREET ADDRESS \[LINE 2\]

> SPOUSE’S STREET ADDRESS \[LINE 3\]

> SPOUSE’S CITY

> SPOUSE’S STATE

> SPOUSE’S ZIP+4

> SPOUSE’S PHONE NUMBER

> DEPENDENT’S STREET ADDRESS SAME AS PATIENT’S

> DEPENDENT’S STREET ADDRESS SAME AS SPOUSE’S \| <u>When Veteran has Spouse flagged as Active</u>

> DEPENDENT’S STREET ADDRESS \[LINE 1\]

> DEPENDENT’S STREET ADDRESS \[LINE 2\]

> DEPENDENT’S STREET ADDRESS \[LINE 3\]

> DEPENDENT’S CITY

> DEPENDENT’S STATE

> DEPENDENT’S ZIP+4

Registration Supplement

How Screen 9 is displayed is dependent on the Means Test version.

For patients with their last Means Test in the “FEB 2005 format”, Screen 9 displays as follows.

INCOME SCREENING DATA, SCREEN \<9\>

PATIENT NAME; SSN TYPE===============================================================================Income data for (YEAR). Means Test is complete for that calendar year!This data must be edited through the Means test module!Veteran Total-----------------------------------------------\[1\] Total Employment Income(Wages, Bonuses, Tips): - -\[2\] Net Income from Farm,Ranch, Property, Bus.: - -\[3\] Other Income Amounts(Soc. Sec., Compensation,Pension, Interest, Div.): - -Total 1-3 --\> \$0.00(YEAR) Estimated "Household" Taxable Income:\<RET\> to CONTINUE, ^N for screen N or '^' to QUIT: ^DATA GROUP 1

Total Employment Income (Wages, Bonuses, Tips) - Gross annual income during the last calendar year from employment (wages, bonuses, tips, etc.) excluding income from farm, ranch, property, or business.

DATE GROUP 2

Net Income from Farm, Ranch, Property, Bus. - Net income from farm, ranch, property, or business received during the last calendar year.

DATA GROUP 3

Other Income Amounts (Soc. Sec., Compensation, Pension, Interest, Div.) - Income from Social Security, compensation, pension, interest, dividends (excluding welfare).

Registration Supplement

SCREEN 9, cont.

For patients with their last Means Test in the “Before FEB 2005 format”, Screen 9 displays as follows.

INCOME SCREENING DATA SCREEN \<9\>

PATIENT NAME; SSN TYPE

===============================================================================

> **NOTE:** Income data for (YEAR). Means Test is complete for that calendar year!This data must be edited through the Means Test module!

Veteran Total

------------------------------------------

\[1\] Social Security (Not SSI) - -

\[2\] U.S. Civil Service - -

\[3\] U.S. Railroad Retirement - -

\[4\] Military Retirement - -

\[5\] Unemployment Compensation - -

\[6\] Other Retirement - -

\[7\] Total Employment Income - -

\[8\] Interest,Dividend,Annuity - -

\[9\] Workers Comp or Black Lung - -

\[10\] All Other Income - -

Total 1-10 --\> \$0.00

{YEAR} Estimated “Household” Taxable Income: \$

\<RET\> to CONTINUE, 1-10 or ALL to EDIT, ^N for screen N, or '^' to QUIT

(To edit only veteran income, precede selection with 'V' \[ex. 'V1-3'\]):

Entries may be made in the fields contained on this screen up until monetary benefits are verified. Once monetary benefits have been verified, a user must hold the DG ELIGIBILITY security key in order to enter/edit these fields. This screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents) depending on previously entered information. The appropriate fields will be prompted for each column shown.

The “{YEAR} Estimated “Household” Taxable Income: \$” field will be filled in if the information has been entered through the 10-10EZ or 1010EZR form. This information is used to make preliminary or prima facie financial eligibility determinations.

DATAGROUP1

SOCIAL SECURITY (NOT SSI) - Annual amount of social security received during the previous calendar year. Do not include SSI.

DATAGROUP2

U.S. CIVIL SERVICE - Annual amount of U.S. Civil Service received during the previous calendar year.

Registration Supplement

SCREEN 9, cont.

DATAGROUP3

U.S. RAILROAD RETIREMENT - Annual amount of U.S. Railroad Retirement received during the previous calendar year.

DATAGROUP4

MILITARY RETIREMENT - Annual amount of military retirement received during the previous calendar year.

DATAGROUP5

UNEMPLOYMENT COMPENSATION - Annual amount of unemployment compensation received during the previous calendar year.

DATAGROUP6

OTHER RETIREMENT - Annual amount of other retirement received during the previous calendar year. Includes company, state, local, etc.

DATAGROUP7

TOTAL INCOME FROM EMPLOYMENT - Total annual amount of income from employment received during the previous calendar year. This includes wages, salary, earnings, and tips.

DATAGROUP8

INTEREST, DIVIDEND, ANNUITY - Annual amount of interest, dividend, or annuity income received during the previous calendar year.

DATAGROUP9

WORKERS COMP. OR BLACK LUNG - Annual amount of worker's compensation or Black Lung benefits received during the previous calendar year.

DATAGROUP10

ALL OTHER INCOME - Annual amount of all other income received during the previous calendar year. Net income from operation of a farm or other business is countable. If the veteran, veteran's spouse, or children receive a salary from the business, it should be reported in Data Group 7 - TOTAL INCOME FROM EMPLOYMENT. Also, note that depreciation is not a deductible expense.

Registration Supplement

INELIGIBLE/MISSING DATA SCREEN \<10\>

PATIENT NAME; SSN TYPE

==================================================================

\[1\] Ineligible Date: TWX Source:

TWX City: TWX State:

Reason:

VARO Decision:

\[2\] Missing Date: TWX Source:

TWX City: TWX State:

Reason:

\<RET\> to CONTINUE, 1-2 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATAGROUP1

You must hold the DG ELIGIBILITY security key in order to enter/edit any of the fields in this data group.

INELIGIBLE DATE - Effective date applicant was ineligible for care. The ineligible date cannot be prior to the date of birth. If an entry is made in this field, the following fields will also be prompted. The data contained in the following fields will automatically be deleted upon deleting the entry in this one.

> INELIGIBLE TWX SOURCE - Source of ineligible TWX. You may enter a \<?\> to obtain a current list of choices.

> INELIGIBLE TWX CITY - City from which ineligible TWX came (3-30 characters).

> INELIGIBLE TWX STATE - State or state code from which ineligible TWX came. Must be in STATE file. You may enter a \<?\> for a list.

> INELIGIBLE REASON - Reason for applicant's ineligibility.

> INELIGIBLE VARO DECISION - VA Regional Office decision concerning applicant's ineligibility for care (3-75 characters).

DATAGROUP2

Entry/edit of the fields on this screen may be accomplished by any user up until the applicant's eligibility has been verified. Following verification of the applicant's eligibility, you must hold the DG ELIGIBILITY security key in order to enter/edit these fields. Viewing of the information will be possible by all users.

MISSING PERSON DATE - Date individual was declared "missing". If an entry is made in this field, the following fields will also be prompted. Data contained in the following fields is automatically deleted if the entry in this field is deleted.

> MP TWX SOURCE - Source of TWX declaring individual "missing". You may enter a \<?\> to obtain a current list of choices.

Registration Supplement

SCREEN 10, cont.

DATA GROUP 2, cont.

> MP TWX CITY - City from which "missing" TWX came (3-30 characters).

> MP TWX STATE - State or state code from which "missing" TWX came. Must be in STATE file. Enter a \<?\> for a list.

> MISSING OR INELIGIBLE - Free text comment concerning ineligible/missing individual.

Registration Supplement

ELIGIBILITY VERIFICATION DATA SCREEN \<11\>

PATIENT NAME; SSN TYPE

==================================================================

\[1\] Eligibility Status: Status Date:

Status Entered By:

Interim Response:

Verif. Method:

\[2\] Money Verified:

\[3\] Service Verified:

\[4\] Rated Disabilities:

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

The purpose of this screen is to allow verification of an applicant's eligibility, monetary benefits and service record. Accordingly, you must hold the DG ELIGIBILITY security key in order to enter/edit any of the fields contained on it. Depending upon site parameters, this screen may be available for viewing to all users.

DATAGROUP1

ELIG. STATUS - Status of patient’s eligibility. You may enter a \<?\> to obtain a current list of choices. You can edit this field if the Eligibility Status is PENDING VERIFICATION or PENDING REVERIFICATION, regardless of the Verification Source. You cannot edit this field when the Eligibility Status is VERIFIED and the Verification Source is HEC.

ELIG. STATUS DATE - Effective date of eligibility status.

ELIG. INTERIM RESPONSE - If an interim response has been received concerning applicant's eligibility, enter date of receipt.

ELIG. VERIF. METHOD - Enter method in which applicant's eligibility was verified. This is a free text field (2-50 characters).

DATAGROUP2

MONETARY BEN. VERIFY DATE - An entry in this field indicates that the applicant's monetary benefits have been verified. Enter the date monetary benefits were verified.

DATAGROUP3

SERVICE VERIFICATION DATE - An entry in this field indicates the applicant's service record has been verified. Enter the date the service record was verified.

Registration Supplement

SCREEN 11, cont.

DATAGROUP4

Select RATED DISABILITIES (VA) - Enter the condition(s) or corresponding VA code(s) for which the applicant has been verified as being service connected. This is a multiple field which will repeat until no more entries are made. For each entry made, the following fields will also be prompted. If the patient is non-service connected, you may still make entries into this field to record any disabilities the patient may have which have been rated by the VA.

VistA users with the appropriate security key may edit the Rated Disabilities field.

The screen display for this entry will reflect the disability followed by the SC/NSC percentage, whichever is appropriate.

> DISABILITY % - Enter the rating percentage for this disability. An entry of YES will not be allowed for applicants with a patient type of non-service-connecteD.

> SERVICE CONNECTED - Choose from: 0 NO

> 1 YES

Registration Supplement

ADMISSION INFORMATION SCREEN \<12\>

PATIENT NAME; SSN TYPE

==================================================================

\<1\> Admission Date: Admit Ward:

Admit Diagnosis:

Discharge Date:

Discharge Type:

\<RET\> to CONTINUE, ^N for screen N, or '^' to QUIT:

This screen displays the patient's four most recent admissions in reverse order. For each admission, the following data will be shown: Admission Date

Admission Diagnosis

Discharge Date

Discharge Type

Admission Ward

If the applicant has no admission data - he/she either has never been admitted or previous admissions occurred prior to use of the VistA software - the following message will be displayed:

"NO ADMISSION DATA ON FILE FOR THIS PATIENT!!"

Registration Supplement

APPLICATION INFORMATION SCREEN \<13\>

PATIENT NAME; SSN TYPE

==================================================================

\<1\> Registered:

Applied for:

Dispositioned:

Type of Disp.:

\<RET\> to CONTINUE, ^N for Screen N, or '^' to QUIT:

This screen displays the applicant's four most recent applications for care in reverse order. For each application, the following data will be shown:

- date/time of registration; employee who registered the applicant; employee's DUZ number (unique number which identifies a user to the system)
- type of benefit applied for
- date/time of disposition; employee who dispositioned the applicant and their DUZ number
- type of disposition

If the applicant has no application data - he/she either has never applied for care or previous applications occurred prior to use of the VistA software - the following message will be displayed:

"NO APPLICATION DATA ON FILE FOR THIS PATIENT!"

Registration Supplement

APPOINTMENT INFORMATION SCREEN \<14\>

PATIENT NAME; SSN TYPE

==================================================================

\<1\> Enrollment Clinics:

\<2\> Pending Appts:

\<RET\> to CONTINUE, ^N for screen N, or '^' to QUIT:

This screen displays each clinic in which the patient is actively enrolled and the clinic name and date/time of all pending appointments.

If the applicant is not actively enrolled in any clinics or has no pending appointments, one of the following messages will be displayed next to the appropriate data group:

"NOT ACTIVELY ENROLLED IN ANY CLINICS AT THIS TIME"

"NO PENDING APPOINTMENTS ON FILE"

Registration Supplement

SPONSOR DEMOGRAPHIC INFORMATION SCREEN \<15\>

PATIENT NAME; SSN TYPE

==================================================================

\[1\] Sponsor Information:

Primary Care Team: Phone \#:

\<RET\> to QUIT, 1 or ALL to EDIT, ^N for Screen N, or '^' to QUIT:

This screen displays sponsor information. It will appear for every patient although the purpose of the screen is to enter sponsorship information for those patients who are being treated under the coverage of someone else (the sponsor). This would usually be through the Tricare Program or CHAMPVA Program. These patients are usually dependents of active duty military personnel, survivors of military personnel, or military retirees.

If a sponsor is already in the PATIENT file (#2), you may not edit the sponsor name and date of birth. For new sponsors, you will be prompted to first add the person as a sponsor and then as the sponsor of the patient. For existing sponsors, you will only be asked if you wish to make that person the sponsor of the patient.

The primary care team and phone# data elements are not entered through this screen. If available, this information is automatically filled in from the Primary Care Management Module of the Scheduling software. This is the name and phone number of the patient’s primary care provider.

If sponsor or team information is not found, the following messages will be displayed:

"No Sponsor Information Available."

"No team assignment information found"

DATAGROUP1

Select SPONSOR - Enter the name of the person who has the coverage under which the patient will be treated. This is a multiple field; you will be returned to this field repeatedly until no more sponsors are entered. (A patient may have more than one sponsor; e.g., both parents are military retirees.) The first two indented fields will only be prompted for if the sponsor is a non-patient (not in the PATIENT file (#2)).

> SPONSOR PERSON DATE OF BIRTH - Enter the sponsor’s date of birth.

> SPONSOR PERSON SOCIAL SECURITY NUMBER - Enter the sponsor’s SSN.

> MILITARY STATUS - Choose A (Active Duty) or R (Retired).

> BRANCH - Enter the branch of service for the sponsor. You may enter a \<?\> for a current list of choices.

> RANK - Enter the military rank of the sponsor (3-20 characters).

Registration Supplement

SCREEN 15, cont.

DATAGROUP1, cont.

> FAMILY PREFIX - The patient’s relationship to the sponsor. This is a free text field; however, it is recommended you use the DOD convention for sponsor relationship codes. You may enter \<??\> for HELP which contains a list of choices.

> SPONSOR TYPE - Choose T (TRICARE) or C (CHAMPVA).

> EFFECTIVE DATE - Effective date of sponsorship.

> EXPIRATION DATE - Expiration date of sponsorship.

Registration Supplement for Newborns

The following items are to be noted when entering data into the Load/Edit Patient Data or Register a Patient screens for newborn infants of women veterans.

Please refer to the Care for Newborn of Women Veterans, procedure guide, for detailed information regarding the entry of newborn patients.

- When screen 2 is displayed the system will automatically default the value for Marital to “NEVER MARRIED”. The default value will display only for a patient with a date of birth that is less than one year prior to the current date.
- When screen 4 is displayed the system will automatically default the value for Status to “NOT EMPLOYED”. The default value will display only for a patient with a date of birth that is less than one year prior to the current date.
- On screen 7 the following values are to be entered:
- Patient Type: NEWBORN OF VETERAN
- Primary Elig Code: COLLATERAL OF VET
- Period of Service: OTHER NON-VETERANS
- When screen 8 is displayed the system will automatically default the value for Married Last Year to “No”. The default value will display only for a patient with a date of birth that is less than one year prior to the current date.
- The inconsistency check process will verify whether a sponsor has been entered for the newborn.. If no sponsor has been entered for the newborn, the following inconsistency will display and the user will be given the opportunity to return to screen 15 to correct the data:
- 313- NEWBORN REQUIRES SPONSOR
- The inconsistency check process will verify whether the newborn’s sponsor has an appropriate eligibility status. . If the newborn’s sponsor does not have an appropriate eligibility status, the following inconsistency will display:
- 314- NEWBORN NEEDS ELIGIBLE SPONSOR

[^1]: ∗ New Special Treatment Authority Expiration date fields for both Agent Orange and SW Asia Conditions were added to the MAS PARAMETERS file (#43). The initial value of these fields will be null or empty. A subsequent patch will be released to populate the date fields once the expiration of the Special Treatment Authority is scheduled to expire. The assigning of Priority Group 6 determination rules to these newly enrolled veterans whose AO Indicator is "Y" and Location is *Vietnam* and/or their SWAC exposure indicator is "Y" will be ignored if the Special Treatment Authority Expiration Date fields are not null.

    A subsequent patch will be released to populate these date fields once the expiration of the Special Treatment Authority is scheduled to expire.

[^2]: