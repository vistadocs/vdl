---
title: IB*2 Diagnostic Measures Reports User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: IB*2 Diagnostic Measures Reports
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2.0
patch_id: IB*2.0
group_key: "IB:IB:2.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - report
  - date
  - number
  - summary
  - bill
  - reports
  - patients
  - unbilled
  - table
  - contents
page_count: 0
word_count: 12139
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_dmr_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_dmr_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Diagnostic Measures Reports

  User Guide
---

![](ib-2-diagnostic-measures-reports-user-guide/001.png)

May 2023

Office of Information and Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>May 2023</td>
<td>1.0</td>
<td><p>The original Diagnostic Measures Reports manual (version from 08/06/2018) has been rehosted and updated.</p>
<p>This manual also contains updates related to the latest patches:</p>
<ul>
<li><p>IB*2*705 (October 2021)</p></li>
<li><p>IB*2*739 (May 2023)</p></li>
</ul></td>
<td>CC DSO Development Team</td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
- [Diagnostic Measures Reports](#diagnostic-measures-reports)
  - [Intake Reports](#intake-reports)
    - [Patients with Unidentified Insurance](#patients-with-unidentified-insurance)
    - [No Employer Listing](#no-employer-listing)
    - [Outpatient Workload Report](#outpatient-workload-report)
    - [Percentage of Completed Registrations](#percentage-of-completed-registrations)
    - [Insurance Policies Not Verified](#insurance-policies-not-verified)
    - [Percentage of Patients Pre-Registered Report](#percentage-of-patients-pre-registered-report)
    - [SC Vets w/ NSC Episodes of Care Not Billed (Inpt)](#sc-vets-w-nsc-episodes-of-care-not-billed-inpt)
    - [Veterans with Verified/Unverified Eligibility](#veterans-with-verifiedunverified-eligibility)
  - [Billing Reports](#billing-reports)
    - [Clerk Productivity](#clerk-productivity)
    - [### Bill Status Report](#bill-status-report)
    - [Reasons Not Billable Report](#reasons-not-billable-report)
    - [Unbilled Amounts Menu](#unbilled-amounts-menu)
    - [Modified Billing Lag Time Report](#modified-billing-lag-time-report)
    - [Billing Lag Time Report](#billing-lag-time-report)
  - [Follow-Up Reports](#follow-up-reports)
    - [Bad Debt Report](#bad-debt-report)
    - [Insurance Payment Trend Report](#insurance-payment-trend-report)
    - [First Party Follow-Up Report](#first-party-follow-up-report)
    - [CHAMPVA/TRICARE Follow-Up Report](#champvatricare-follow-up-report)
    - [Miscellaneous Bills Follow-Up Report](#miscellaneous-bills-follow-up-report)
    - [Workload Assignment Print](#workload-assignment-print)
    - [Third Party Follow-Up Report](#third-party-follow-up-report)
    - [AR Productivity Report](#ar-productivity-report)
    - [Repayment Plan Follow-up Report](#repayment-plan-follow-up-report)
    - [Third Party Follow-Up Summary Report](#third-party-follow-up-summary-report)
    - [Repayment Plan Status Report](#repayment-plan-status-report)
    - [Workload Assignment Enter/Edit](#workload-assignment-enteredit)
  - [Utilization Management Reports](#utilization-management-reports)
    - [UR Activity Report](#ur-activity-report)
    - [MCCR/UR Summary Report](#mccrur-summary-report)
- [APPENDIX A – Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Diagnostic Measures were originally developed in response to requests from Medical Centers for automated methods of tracking and trending the success of Medical Care Cost Recovery (MCCR) program operations. In 1999, MCCR was reorganized into the Veterans Health Administration (VHA) Office of Finance Revenue Program. The title MCCR still appears on the Integrated Billing (IB) and Accounts Receivable (AR) menus.

VHA moved to a consolidated revenue cycle process via implementation of seven Consolidated Patient Accounts Centers (CPACs). The initiative was designed to consolidate functions for consistency, decrease costs, and increase revenue. This effort was started in 2007 and was completed in 2012.

Diagnostic Measures are indicators of how each part of the revenue process is performing. They can be used to analyze changes in the revenue process over a period of time and to evaluate the bottom line results of the revenue process from registration/enrollment through collection.

The IB and AR packages contain a wealth of information for Facility Revenue Managers (FRM) and CPAC Department Managers. Most of the Diagnostic Measures can be found on the CPAC FRM Menu. Reports developed prior to the Diagnostic Measures can still be found in the IB and AR Packages, as well as in the CPAC FRM Menu.

Internet access is required for all employees involved in the revenue generation process.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Diagnostic Measures Reports are designed to provide CPAC FRMs at each VA facility with specific information that can be used to improve daily program operations, and thereby improve collections. They can be used by anyone involved in the collection process. They can be run at any time, but the resulting output may (and likely will) differ when run at different times of the month.

Diagnostic Measures can be used to:

- Identify program strengths and weaknesses
- Identify areas for improvement
- Establish key performance benchmarks
- Trend program performance
- Manage and monitor processes that affect the Revenue Program
- Measure performance of staff

Diagnostic Measures will be most effective when used consistently. Tracking and trending information from these reports will provide data for use in evaluating the Revenue Program. These reports will provide the user with information which may be used for training, staff development, and follow-up action at the medical center level. They may also be analyzed by CPAC or Veterans Integrated Service Network (VISN) managers to provide indicators of CPAC/VISN performance or facility performance compared to like facilities.

# Diagnostic Measures Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Diagnostic Measures Reports Menu contains five sub-menus with the reports organized by their purpose. The main menu is listed below:

1.  Intake Reports ...
2.  Billing Reports ...
3.  Follow-Up Reports ...
4.  Utilization Management Reports ...
5.  Diagnostic Measures Extract Menu ...

This User Guide provides information on items 1-4 in the menu above.

## Intake Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Intake Reports provide tools to obtain measurements of Registration processes and workload reporting. Patient demographic and eligibility-based reports can be used to measure and trend important actions that translate into Veterans Equitable Resource Allocation (VERA) reimbursement as well as first and third party billing. These include Insurance verification, Outpatient workload reporting and patient employment status.

The Intake Reports Menu:

IN Patients with Unidentified Insurance

NE No Employer Listing

OW Outpatient Workload Report

PC Percentage of Completed Registrations

PO Insurance Policies Not Verified

PR Percentage of Patients Pre-Registered Report

SC SC Vets w/ NSC Episodes of Care Not Billed (Inpt)

UE Veterans with Verified/Unverified Eligibility

### Patients with Unidentified Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As mentioned in the output below, this report provides the number of patients who have been treated but not identified as having or not having insurance. Users may print the detailed output to follow up with Insurance data collection.

Select Intake Reports \<TEST ACCOUNT\> Option: IN Patients with Unidentified Insurance

This report provides the number of patients who have been treated, but not

identified as having or not having insurance.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to sort this report by division? NO//

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

This report only requires an 80 column printer.

(E)xcel Format or (R)eport Format: Report//

> **NOTE:** This report may take a while to run. You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

PATIENT INSURANCE STATISTICS

SUMMARY REPORT

Patients treated from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@17:08:18

========================================

Number of Patients Treated: 8475

Number of Patients Covered by Insurance: 5247 (61.91%)

No. of Patients Covered by Billable Insurance: 2854 (33.68%-54.39%)\*

Number of Patients Covered by an HMO: 214 (2.53%-4.08%-7.50%)\*\*

Number of Patients Covered by Medicare: 4341 (51.22%-82.73%)\*

Number of Patients Covered by Medigap: 361 (4.26%-6.88%-12.65%)\*\*

No. of Patients Covered by an Indemnity Policy: 13 (0.15%)

Number of Patients Not Covered by Insurance: 3210 (37.88%)

Number of Patients with Unknown Insurance: 18 (0.21%)

No. of Patients w/Insurance Question Unanswered: 0 (0.00%)

Number of Deceased Patients: 1621 (19.13%)

\*(% from patients treated-% from patients with insurance)

\*\*(% from patients treated-% from patients w/ins-% from patients w/billable ins)

Type \<Enter\> to continue or '^' to exit:

### No Employer Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report identifies patients that are listed as employed, but there is no employer information in the database. The report will prompt the user for a date range and can be run in detail or summary. The report now excludes patients seen for Compensation & Pension (C&P) Exams, Employee Visits, Collateral visits, and non-count clinic visits. Additionally, the report now will be compiled by unique patients treated within the user-specified date range and may also be run by division. The detailed report can be used as a worksheet to contact patients and update their records accordingly.

Select Intake Reports \<TEST ACCOUNT\> Option: NE No Employer Listing

This report provides a measure of the number of Veteran patients who

have been identified as being employed, but have no employer on file.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to sort this report by division? NO//

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run. You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

NO EMPLOYER LISTING Page: 1

SUMMARY REPORT

Patients treated from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@17:21:48

=============================================

Number of Patients Treated: 8475

Number of Deceased Patients: 1621 (19.13%)

Number of Patients Employed without an Employer: 2955\* (34.87%)

Number of Patients Unemployed or with an Employer: 5520 (65.13%)

\*This is the total number of Veterans who have no employer on file, but

have an employment status of Full-Time, Part-Time, Retired, Unknown or

null.

Type \<Enter\> to continue or '^' to exit:

### Outpatient Workload Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides a breakdown of the number of outpatient encounters by eligibility. The report prompts the user for a date range and is available in summary only. The report now excludes patients seen for C&P Exams, Employee Visits, Collateral visits, and non-count clinic visits. Additionally, the report now will be compiled by unique patients treated within the user-specified date range.

There are two summary reports. The first provides information on all Out Patient Treatment (OPT) encounters; the second provides information on OPT encounters for patients who have billable insurance.

Select Intake Reports \<TEST ACCOUNT\> Option: ow Outpatient Workload Report

This report provides a measure of the number and types of

Outpatient Services that are provided in the Medical Center.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to sort this report by division? NO//

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run. You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

OUTPATIENT ENCOUNTER WORKLOAD - ALL ENCOUNTERS

SUMMARY REPORT FOR ALL DIVISIONS

For Outpatient Encounters from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@21:26:35

==============================================

Number of Outpatient Encounters: 34227

Number of Encounters for NSC Veterans: 10591 (30.94%)

Number of Encounters for SC Veterans: 23636 (69.06%)

Number of Service Connected Encounters for SC Veterans: 4982 (21.08%)

Number of Non-Svc. Connected Encounters for SC Veterans: 18654 (78.92%)

Type \<Enter\> to continue or '^' to exit:

OUTPATIENT ENCOUNTER WORKLOAD - INSURED ENCOUNTERS ONLY

SUMMARY REPORT FOR ALL DIVISIONS

For Insured Outpatient Encounters from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@21:26:35

=======================================================

Number of Outpatient Encounters: 1174

Number of Encounters for NSC Veterans: 372 (31.69%)

Number of Encounters for SC Veterans: 802 (68.31%)

Percentage of Insured Outpatient Encounters for All Divisions: 3.43%

### Percentage of Completed Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is designed to identify inconsistencies in the patient registration process, including the fields requiring additional data for completion. The report includes a breakout between Veteran patients and non-Veteran patients registered within the timeframe the report was generated. The report will also provide the number of incomplete registrations with treatment rendered in the given timeframe. The report prompts the user for a date range and can be run in detail or summary. It may also be run by division. If desired, the detail report may be run to identify the person who first registered the patient for care. The detailed report has improved to show type of care and primary eligibility. It also may be used as a worksheet to contact patients and update records.

Select Intake Reports \<TEST ACCOUNT\> Option: PC Percentage of Completed Registrations

This report measures the number of registrations which are being entered

without inconsistencies. Please enter a date range representing the dates

that patients were first entered into the system.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to sort this report by division? NO//

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

This report only requires an 80 column printer.

> **NOTE:** This report requires a search through the entire Patient file.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

PERCENTAGE OF COMPLETED REGISTRATIONS

SUMMARY REPORT

For the Period 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@21:36:31

================================================================

Number of Registrations: 300

Number of Regs with Treatment Rendered: 205 (68.33%)

Number of Regs with No Treatment Rendered: 95 (31.67%)

================================================================

Number of Complete Registrations: 157 (76.59%)

Number of Complete Veteran Regs: 152 (96.82%)

Number of Complete Non-Veteran Regs: 5 (3.18%)

================================================================

Number of Incomplete Registrations: 48 (23.41%)

Number of Incomplete Veteran Regs: 34 (70.83%)

Number of Incomplete Non-Veteran Regs: 14 (29.17%)

================================================================

Number of Deceased Patients: 28 (9.33%)

Type \<Enter\> to continue or '^' to exit:

### Insurance Policies Not Verified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is used to identify patients with insurance policies that require verification or verification that was done over a year ago. This report prompts the user by date range and will print in detail or summary, excluding those policies who are designated as Will Not Reimburse. The report now excludes patients seen for C&P Exams, Employee Visits, Collateral visits, and non-count clinic visits. Additionally, the report now will be compiled by unique patients treated within the user-specified date range. The detailed report will identify unverified policies as well as policies verified over one year ago. Verification of insurance benefits ensures the efficiency and effectiveness of the program.

Select Intake Reports \<TEST ACCOUNT\> Option: PO Insurance Policies Not Verified

This report provides a number of the insurance policies which were

entered into the system within a given timeframe, but were never verified.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

Do you want to print a total number of policies that were verified

over a year ago? NO//

(E)xcel Format or (R)eport Format: Report//

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

INSURANCE POLICIES NOT VERIFIED

SUMMARY REPORT

For Patients treated from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@21:41:56

===============================

Number of Patients Treated: 4851

Number of Policies Verified: 4851 (100.00%)

Number of Policies Not Verified: 0 (0.00%)

Type \<Enter\> to continue or '^' to exit:

### Percentage of Patients Pre-Registered Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides the number of patients treated, the number of patients pre-registered, the percentage of patients that were pre-registered, the number of patients pre-registered past the pre-registration time frame, the number of patients never pre-registered, the number of clinic exclusions, and the number of eligibility exclusions.

Select Intake Reports \<TEST ACCOUNT\> Option: PR Percentage of Patients Pre-Registered Report

This report provides number of patients treated, the number of

patients pre-registered, % of patients pre-registered, number of

patients pre-registered past the pre-registration time frame,

number of patients never pre-registered, the clinic exclusions,

and the eligibility exclusions.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Pre-Registration time frame (days): 180//

Detailed list of Exclusions (Y/N)? NO//

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

PERCENTAGE OF PATIENTS PRE-REGISTERED Page: 1

SUMMARY REPORT

Patients pre-registered from 01/01/23 - 01/31/23

Pre-registration time frame: 180 days

Run Date: MAY 01, 2023@21:51:06

=======================================================

\*Number of Unique Patients Treated: 8144

Unique Outpatients Pre-registered within pre-registration time frame: 7826

Percent Pre-registered: 96.10%

Unique Outpatients Pre-registered past pre-registration time frame: 295

Unique Outpatients never Pre-registered: 23

\*Counts may not include all patients because of exclusions.

Number of Eligibility Exclusions: 9

Number of Clinic Exclusions: 209

Type \<Enter\> to continue or '^' to exit:

### SC Vets w/ NSC Episodes of Care Not Billed (Inpt)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides the number of Non-Service-Connected (NSC) inpatient episodes for Service-Connected (SC) Veterans which have and have not been billed. The detailed version of the report lists the patient name, the Social Security Number (SSN), the Patient Treatment File (PTF) Status (Open, Closed, Released, or Transmitted), the admission date, and the discharge date.

Select Intake Reports \<TEST ACCOUNT\> Option: SC SC Vets w/ NSC Episodes of Care

Not Billed (Inpt)

This report provides a number of the NSC inpatient episodes for SC Veterans

which have and have not been billed.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to print a (S)ummary or (D)etailed Report? s SUMMARY

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

INSURED SC VETERANS W/ UNBILLED NSC INPATIENT EPISODES

SUMMARY REPORT

For Patients discharged from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@21:58:08

===============================

Number of Discharges of Insured SC Veterans: 21

Discharges Which were totally Service-Connected: 0 (0.00%)

Discharges Which included Non-Service Connected Care: 21 (100.00%)

Number of NSC Discharges Which were Billed: 10 (47.62%)

Number of NSC Discharges Flagged as Non-Billable: 7 (33.33%)

Number of Unbilled NSC Discharges: 4 (19.05%)

----

Unbilled NSC Discharges w/ PTF Status of Open: 0 (0.00%)

Closed: 0 (0.00%)

Released: 0 (0.00%)

Transmitted: 4 (100.00%)

Type \<Enter\> to continue or '^' to exit:

### Veterans with Verified/Unverified Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will provide information on patients who have been treated at a facility and whose eligibility has not been verified or whose eligibility has not been verified for at least two years. The report will prompt the user for a date range and can be run in detail or summary. The report now excludes patient encounters for C&P Exams, Employee Visits, Collateral visits, and non-count clinic visits. Additionally, the report now will be compiled by unique patients treated within the user-specified date range and may be run by division. The detailed report can be used as a worksheet to contact patients, send Hospital Inquiries (HINQs) or 7131s to VA Regional Offices and update records as required.

Select Intake Reports \<TEST ACCOUNT\> Option: UE Veterans with Verified/Unverified Eligibility

This report measures the number of patients who have been treated at the

facility but whose eligibility has not been verified. This report will

also list patients with verified eligibility for at least 2 years, if any.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to sort this report by division? NO//

Do you wish to print a (S)ummary or (D)etailed Report? s SUMMARY

This report only requires an 80 column printer.

> **NOTE:** This report may take a while to run.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

VETERANS WITH UNVERIFIED ELIGIBILITY

SUMMARY REPORT

Patients treated from 01/01/23 - 01/31/23

Run Date: MAY 01, 2023@22:06:14

=====================================================

Number of Patients Treated: 8475

Number of Deceased Patients: 1621 (19.13%)

Number of Patients with Verified Eligibility: 8473 (99.98%)

Number of Patients Whose Verified Eligibility Date

is At Least 2 Years Old (from above total): 8473 (100.00%)

Number of Patients with a Pending Eligibility: 1 (0.01%)

Number of Patients Not Verified: 1 (0.01%)

Type \<Enter\> to continue or '^' to exit:

## Billing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Billing Reports Menu contains a number of reports designed to monitor the billing process and track the progress of the billing effort. Reports on Clerk Productivity, the Status of bills, Reasons Not Billable, and Lag Time all assist in monitoring billing workload and productivity.

The Billing Reports Menu:

CP Clerk Productivity

SR Bill Status Report

NB Reasons Not Billable Report

UA Unbilled Amounts Menu ...

LAG Modified Billing lag time rept

LT Billing Lag Time Report

\*\*\> Out of order: Use New Menu Option

### Clerk Productivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report allows monitoring of workload and clerk productivity. The option prints a report of the clerk’s activity by claims entered, authorized, or printed. This report prompts the user for a date range and can be run in full or summary. For both of these reports, a subtotal is provided for each clerk. The total amount for this report is also displayed. If Autobiller is turned on, print this report by individual who authorized bills.

Select Billing Reports \<TEST ACCOUNT\> Option: CP Clerk Productivity

Select one of the following:

F FULL CLERK PRODUCTIVITY REPORT

S SUMMARY OF CLERK PRODUCTIVITY REPORT

Enter response: s SUMMARY OF CLERK PRODUCTIVITY REPORT

Select one of the following:

E WHO ENTERED BILL

A WHO AUTHORIZED BILL

P WHO FIRST PRINTED BILL

REPORT BY WHICH CLERK FUNCTION: A// WHO AUTHORIZED BILL

CLERK PRODUCTIVITY SUMMARY REPORT

START WITH Date Authorized: 010123 (JAN 01, 2023)

GO TO Date Authorized: (JAN 01, 2023-MAY 01, 2023@23:35:22): TODAY// 013123 (JAN 31, 2014)

Do you want to print the summary without the clerks' names? NO//

Report requires 132 columns.

OUTPUT DEVICE: HOME// 0;132 HOME (CRT)

CLERK PRODUCTIVITY SUMMARY FOR BILLS AUTHORIZED JAN 1,2023 - JAN 31,2023 MAY 01, 2023 23:38 PAGE 1

---TOTAL AUTHORIZED--- -AUTHORIZED CANCELLED- -----MRA REQUESTS-----

AUTHORIZED BY RATE TYPE COUNT AMOUNT COUNT AMOUNT COUNT AMOUNT

--------------------------------------------------------------------------------------------------------------------------------

ADDDDDD,LLLL D REIMBURSABLE INS. 90 32010.47 10 4616.49 102 4907.70

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 90 32010.47 10 4616.49 102 4907.70

ANNNNN,SSSSSS R REIMBURSABLE INS. 0 0.00 0 0.00 26 931.36

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 0 0.00 0 0.00 26 931.36

ARRRRRRRRR,III R REIMBURSABLE INS. 2 131.34 0 0.00 0 0.00

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 2 131.34 0 0.00 0 0.00

BBBBBBBBBB,AAA O REIMBURSABLE INS. 26 7218.97 2 370.51 28 706.63

Type \<Enter\> to continue or '^' to exit:

CLERK PRODUCTIVITY SUMMARY FOR BILLS AUTHORIZED JAN 1,2023 - JAN 31,2023 MAY 01, 2023 23:38 PAGE 2

---TOTAL AUTHORIZED--- -AUTHORIZED CANCELLED- -----MRA REQUESTS-----

AUTHORIZED BY RATE TYPE COUNT AMOUNT COUNT AMOUNT COUNT AMOUNT

--------------------------------------------------------------------------------------------------------------------------------

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 26 7218.97 2 370.51 28 706.63

BDDDD,JJJJJJJ M REIMBURSABLE INS. 310 372661.46 60 90590.92 112 78167.42

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 310 372661.46 60 90590.92 112 78167.42

BRRRR,LLLLLL MMM REIMBURSABLE INS. 1018 27418.31 7 433.60 0 0.00

----- ----------- ----- ----------- ----- -----------

SUBTOTAL: 1018 27418.31 7 433.60 0 0.00

CCCCCCCC,EEEEEE A REIMBURSABLE INS. 41 25203.50 2 346.50 21 630.40

Type \<Enter\> to continue or '^' to exit:

### ### Bill Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bill Status Report option is used to print a listing of bills and bill status for a specified date range. The user can opt to include all statuses or a single status. The report may be sorted by the event date (date beginning the bill's episode of care), bill date (date the bill was initially printed), or entered date (date the bill was first entered).

The following data items will be provided in the first portion of the report for each bill listed: bill number, patient name and patient ID#, event date, initials of the person who entered the bill, rate type, Means Test category, charges, and bill status with date of that status. If the user opts to sort by bill date or entered date, the bills are grouped for each date (billed or entered) of the selected range.

The second portion of the report provides summary totals. The dollar amount and total number of bills for each bill type and for each status are included. Grand totals are also provided. For bills that have been disapproved during the authorization process, the report will show \*REVIEWED/DISAPP (appears only for bills prior to this version of the IB software) or \*AUTHORIZED/DISAPP after the status. The bill status will be followed by the initials of the user responsible for that status and his/her Designated User (DUZ) number. This is a number that uniquely identifies the user to the system. If a bill is pending (i.e., not printed or cancelled), the bill status will be preceded by an asterisk (\*) on the report.

Select Billing Reports \<TEST ACCOUNT\> Option: sr Bill Status Report

Do you want to print the status of ALL bills? YES//

Select one of the following:

1 EVENT DATE

2 BILL DATE

3 ENTERED DATE

4 MRA REQUEST DATE

SORT BY: 1// EVENT DATE

Start with Event DATE: 010123 (JAN 01, 2023)

Go to Event DATE: TODAY// 013123 (JAN 31, 2023)

Do you want to print the summary ONLY? NO// y YES

\*\*\* Margin width of this output is 80 \*\*\*

DEVICE: HOME// HOME (CRT) Right Margin: 80//

MCCR Bill Status Statistics for period covering JAN 1,2023 thru JAN 31,2023

Run Date: MAY 1,2023@21:21

===============================================================================

CHAMPVA-OPT .................... \$311.18 3 BILLS

NO FAULT-OPT .................... \$15.43 1 BILLS

REIM INS-INPT .................... \$548,503.32 129 BILLS

REIM INS-OPT .................... \$1,946,053.90 6196 BILLS

SHARING-OPT .................... \$0.00 2 BILLS

TORT-INPT .................... \$1,993.15 4 BILLS

TORT-OPT .................... \$26,066.97 70 BILLS

TRICARE-OPT .................... \$42,291.03 108 BILLS

WORKERS-OPT .................... \$10,177.82 11 BILLS

----------------- -------------

\$2,575,412.80 6524 BILLS

AUTHORIZED .................... \$612.56 1 BILLS

CANCELLED .................... \$760,824.33 1305 BILLS

ENTERED .................... \$7,466.14 5 BILLS

PRNT/TXMT .................... \$1,806,509.77 5213 BILLS

----------------- -------------

\$2,575,412.80 6524 BILLS

### Reasons Not Billable Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report identifies all claims tracking entries which have been assigned a Reason Not Billable. The report will prompt the user for a date range and can be run in detail or summary formats, as well as provide a breakdown by specialty and provider.

Select Billing Reports \<TEST ACCOUNT\> Option: NB Reasons Not Billable Report

Do you wish to sort this report by division? NO//

Run report for (D)ATE ENTERED or (E)PISODE DATE: D// DATE ENTERED

Start with DATE ENTERED: 010123 (JAN 01, 2023)

Go to DATE ENTERED: 013123 (JAN 31, 2023)

Run report for (A)LL or (S)PECIFIC Reasons Not Billable: A// ALL

Run report for (A)LL or (S)PECIFIC Providers: A// ALL

Do you wish to print a (S)ummary or (D)etailed Report? s SUMMARY

Choose which episode to print:

1 - INPATIENT

2 - OUTPATIENT

3 - PROSTHETICS

4 - PHARMACY

5 - ALL RECEIVABLES

Select: (1-5): 5//

You have selected

5 - ALL RECEIVABLES

Are you sure? NO// y YES

Run report for (A)LL or (S)PECIFIC Inpatient Specialties: A// ALL

Run report for (A)LL or (S)PECIFIC Outpatient Specialties: A// ALL

You will need a 80 column printer for this report!

> **NOTE:** This report may take a while to run. You should queue it

to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Page: 1

REASONS NOT BILLABLE SUMMARY/INPATIENT

Period : from 01/01/23 thru 01/31/23

Run Date: MAY 01, 2023@22:33:33

No. of Total

RNB Category Entries Amount

====================================================

SC TREATMENT 3 98362.35

OTHER COMPLIANCE 2 21048.28

MRA REC'D. NO SEC RESP EXISTS 3 107184.38

FILING TIMEFRAME NOT MET 1 38569.90

OBSERVATION-OP BILLED 2 3181.64

NO OUTPATIENT COVERAGE 1 1711.70

ALL BILLABLE CPT CODES BILLED 1 1513.43

-------------------

Grand Totals: 13 271571.68

Type \<Enter\> to continue or '^' to exit:

Page: 2

REASONS NOT BILLABLE SUMMARY/OUTPATIENT

Period : from 01/01/23 thru 01/31/23

Run Date: MAY 01, 2023@22:33:33

No. of Total

RNB Category Entries Amount

====================================================

NOT INSURED 16 10216.40

SC TREATMENT 145 76549.53

COVERAGE CANCELED 22 12667.97

NON-BILLABLE APPOINTMENT TYPE 798 192088.45

HMO POLICY 2 602.46

REFUSES TO SIGN RELEASE (ROI) 14 5671.12

NON-BILLABLE STOP CODE 120 28226.84

NON-BILLABLE CLINIC 176 55434.78

NO DOCUMENTATION 6 1747.62

OTHER COMPLIANCE 4 1973.08

OUT OF NETWORK (PPO) 1 767.26

COMBAT VETERAN 10 3927.62

MRA REC'D. NO SEC RESP EXISTS 6 2922.35

FILING TIMEFRAME NOT MET 29 19719.46

GLOBAL SURGERY 14 3401.64

DUPLICATE ENCOUNTER 7 2245.54

MEDICARE REPLACEMENT POLICY 276 145801.71

COVERED BY MEDICARE AT 100% 24 8792.02

BENEFITS MAXED 2 5301.89

C&P EXAM/REGISTRY EXAM 108 77010.11

TELEPHONE ENCOUNTER 1300 46415.28

NO TX PROVIDED/ADVICE ONLY 5 1735.04

ROI NOT OBTAINED 11 4070.82

CONCURRENT CARE 3 1427.36

BILLED INSTITUTIONAL ONLY 51 7073.22

BILLED PROFESSIONAL ONLY 13 2635.90

NO OUTPATIENT COVERAGE 308 197880.29

NO DENTAL COVERAGE 53 28671.03

MED NEC-DX NOT COVERED 14 9335.48

MED NEC-CPT NOT COVERED 79 23790.04

MED NEC-LCD EDIT 2 1173.79

MEDICARE EXCLUDED SERVICE 449 107013.26

NON-COVERED PROVIDER 174 49537.41

NO PHYSICIAN ORDER 1 386.19

NO PLAN OF CARE 1 319.73

STUDENT NOTE ONLY 5 1079.18

ALL BILLABLE CPT CODES BILLED 138 36119.90

PENDING CODE SET UPDATE 11 2057.87

NPI/TAXONOMY/PPN ISSUES 1 11.36

NEW PT/NO EXAM 2 639.46

NO VISION COVERAGE 3 469.83

NON-BILLABLE PROCEDURE 52 14901.17

EMPLOYEE HEALTH 1 235.33

NOT RELATED TO WC/TORT/NF 35 24648.67

TRICARE PT SEEN AS VETERAN 586 418302.45

OTHER 32 26220.71

-------------------

Grand Totals: 5110 1661218.62

Type \<Enter\> to continue or '^' to exit:

Page: 3

REASONS NOT BILLABLE SUMMARY/PROSTHETICS

Period : from 01/01/23 thru 01/31/23

Run Date: MAY 01, 2023@22:33:33

No. of Total

RNB Category Entries Amount

====================================================

NOT INSURED 2 349.74

SC TREATMENT 90 8286.13

NEEDS SC DETERMINATION 840 87338.25

HMO POLICY 2 167.74

OUT OF NETWORK (PPO) 3 251.61

DUPLICATE ENCOUNTER 8 1300.10

MEDICARE REPLACEMENT POLICY 60 11719.95

COVERED BY MEDICARE AT 100% 3 604.21

BENEFITS MAXED 4 335.48

NO OUTPATIENT COVERAGE 18 1815.59

MED NEC-DX NOT COVERED 3 121.75

MED NEC-CPT NOT COVERED 129 15474.21

MEDICARE EXCLUDED SERVICE 47 3491.51

ALL BILLABLE CPT CODES BILLED 396 36886.71

NO VISION COVERAGE 7 318.75

NON-BILLABLE DME/PROSTHETIC 19 2538.14

NO PROSTHETIC COVERAGE 4 260.12

NOT RELATED TO WC/TORT/NF 6 473.98

TRICARE PT SEEN AS VETERAN 36 3906.79

OTHER 2 218.02

-------------------

Grand Totals: 1679 175858.78

Type \<Enter\> to continue or '^' to exit:

Page: 4

REASONS NOT BILLABLE SUMMARY/PHARMACY

Period : from 01/01/23 thru 01/31/23

Run Date: MAY 01, 2023@22:33:33

No. of Total

RNB Category Entries Amount

====================================================

SC TREATMENT 1701 61262.30

AGENT ORANGE 27 2293.95

SOUTHWEST ASIA 14 307.71

NEEDS SC DETERMINATION 1 18.73

INVALID PRESCRIPTION ENTRY 12 403.44

PRESCRIPTION DELETED 40 1356.70

PRESCRIPTION NOT RELEASED 28 935.78

DRUG NOT BILLABLE 1050 29613.48

MILITARY SEXUAL TRAUMA 99 3797.09

COMBAT VETERAN 230 6565.69

90 DAY RX FILL NOT COVERED 93 4604.11

NOT A CONTRACTED PROVIDER 15 5019.10

INVALID MULTIPLES PER DAY SUPP 1 13.21

REFILL TOO SOON 12 751.37

INVALID NDC FROM CMOP 36 1538.99

PROJECT 112/SHAD 1 15.56

NON COVERED DRUG PER PLAN 159 7550.51

FILING TIMEFRAME NOT MET 66 1788.10

NO PHARMACY COVERAGE 4226 165585.63

ALL BILLABLE CPT CODES BILLED 1 28.37

NPI/TAXONOMY/PPN ISSUES 1 82.22

RX DUR REJECT 6 620.43

RX PRIOR AUTH NOT OBTAINED 2 118.63

RX MEDICARE PART D 59 1315.83

DATE OF BIRTH MISMATCH 2 32.34

NOT RELATED TO WC/TORT/NF 7 168.12

TRICARE PT SEEN AS VETERAN 882 28552.22

OTHER 98 2832.71

-------------------

Grand Totals: 8869 327172.32

Type \<Enter\> to continue or '^' to exit:

### Unbilled Amounts Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains the four user options available to regenerate and view the Unbilled Amounts report.

Unbilled Amounts Menu:

Re-Generate Average Bill Amounts

Re-Generate Unbilled Amounts Report

Send Test Unbilled Amounts Bulletin

View Unbilled Amounts

#### Re-Generate Average Bill Amounts

This option can be used to re-generate the monthly and yearly counts and amounts of inpatient and outpatient bills for a single month. If the month selected for input requires the calculation of previous months data in order to obtain its yearly values, this will be done when the option is executed. If the month selected has 12 prior months’ worth of data, the month selected will be recalculated. The months subsequent to the month selected (up to 12) will have their yearly data recalculated. This information is used to compute the average bill amount for the Unbilled Amounts Report. The unbilled amount report is automatically generated for only the month selected after the average bill amounts are calculated.

Select Unbilled Amounts Menu \<TEST ACCOUNT\> Option: Re-Generate Average Bill Amounts

Re-compile Average Bill Amounts through MONTH/YEAR: APR 2023//

This will automatically be tasked to run and needs no device.

A mail Message will be sent when the process completes.

Use the option View Unbilled Amounts to see cumulative totals.

Requested Start Time: NOW// (MAY 04, 2023@00:14:22)

MailMan message:

Subj: UNBILLED AMOUNTS JOB FOR APR 2023 \[#472300\] 05/04/23@00:14 32 lines

From: INTEGRATED BILLING PACKAGE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

The background job responsible for calculating and updating MONTHLY and

YEARLY Average Bill Amounts and Bill numbers for inpatient episodes has

successfully completed.

Monthly totals calculated for APR 2022

Monthly totals calculated for MAY 2022

Monthly totals calculated for JUN 2022

Monthly totals calculated for JUL 2022

Monthly totals calculated for AUG 2022

Monthly totals calculated for SEP 2022

Monthly totals calculated for OCT 2022

Monthly totals calculated for NOV 2022

Monthly totals calculated for DEC 2022

Monthly totals calculated for JAN 2023

Monthly totals calculated for FEB 2023

Monthly totals calculated for MAR 2023

Monthly totals calculated for APR 2023

Yearly totals calculated for APR 2022

Type \<Enter\> to continue or '^' to exit:

Subj: UNBILLED AMOUNTS JOB FOR APR 2023 \[#472300\] Page 2

-----------------------------------------------------------------------------

Yearly totals calculated for MAY 2022

Yearly totals calculated for JUN 2022

Yearly totals calculated for JUL 2022

Yearly totals calculated for AUG 2022

Yearly totals calculated for SEP 2022

Yearly totals calculated for OCT 2022

Yearly totals calculated for NOV 2022

Yearly totals calculated for DEC 2022

Yearly totals calculated for JAN 2023

Yearly totals calculated for FEB 2023

Yearly totals calculated for MAR 2023

Yearly totals calculated for APR 2023

Enter message action (in IN basket): Ignore//

#### Re-Generate Unbilled Amounts Report

This option can be used to re-generate the Unbilled Amounts Report for a single month. This will re-compute the unbilled care for the month and update the unbilled amounts. To simply view previously computed data, use the View option.

Select Unbilled Amounts Menu \<TEST ACCOUNT\> Option: Re-Generate Unbilled Amounts Report

Re-Generate Unbilled Amounts Report

Do you want to store Unbilled Amounts figures? NO// ??

Enter 'YES' if you wish to store the Unbilled Amounts summary

figures in your system for a specific month/year in the past.

Once stored, these figures will be available for inquiry through

the View Unbilled Amounts option \[IBT VIEW UNBILLED AMOUNTS\].

These summary figures are normally calculated and stored

automatically by the system at the beginning of each month for

the previous month.

If you enter 'NO', the Unbilled Amounts summary figures will

NOT be stored in your system, and the report may be run for

any date range.

Do you want to store Unbilled Amounts figures? NO// YES

Re-compile Unbilled Amounts through MONTH/YEAR: APR 2023// (APR 2023)

> **NOTE:** Just a reminder that by entering the above month/year this

report will re-calculate and update the Unbilled Amounts

data on file in your system.

> **NOTE:** After this report is run, the Unbilled Amounts totals for

the month of APR 2023 will be updated.

Print detail report with the Unbilled Amounts summary? NO//

Requested Start Time: NOW//

#### Send Test Unbilled Amounts Bulletin

This option allows for sending a test mail message to the mail group to receive the Unbilled Amounts messages. Using this prior to reporting problems can assist sites in determining whether the mail groups are set up correctly. The mail group to get the message should be specified in field UNBILLED MAIL GROUP (# 6.25) in the IB SITE PARAMETERS file (# 350.9).

Select Unbilled Amounts Menu \<TEST ACCOUNT\> Option: send Test Unbilled Amounts Bulletin

\<after choosing the option, the system returns the User to the Unbilled Amounts Menu\>

Re-Generate Average Bill Amounts

Re-Generate Unbilled Amounts Report

Send Test Unbilled Amounts Bulletin

View Unbilled Amounts

Test MailMan message:

Subj: UNBILLED AMOUNTS SUMMARY REPORT (TEST) \[#472304\] 05/04/23@00:30 35 lines

From: INTEGRATED BILLING PACKAGE In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

SUMMARY UNBILLED AMOUNTS FOR CHEYENNE VA MEDICAL (442).

PERIOD: FROM 05/04/23 TO 05/04/23

GRAND TOTALS

Inpatient Care:

Number of Unbilled Inpatient Admissions : 0

Number of MRA Unbilled Inpt Admissions : 0

Number of Inpt. Institutional Cases : 0

Average Inpt. Institutional Bill Amount : 25029.11

Number of Inpt. Professional Cases : 0

Average Inpt. Professional Bill Amount : 123.15

Total Unbilled Inpatient Care : 0.00

Total MRA Unbilled Inpatient Care : 0.00

MCCF & Non-MCCF Claims - Outpatient Care:

Number of Unbilled Outpatient Cases : 0

Number of Unbilled CPT Codes : 0

Number of MRA Unbilled CPT Codes : 0

Type \<Enter\> to continue or '^' to exit:

Subj: UNBILLED AMOUNTS SUMMARY REPORT (TEST) \[#472304\] Page 2

-----------------------------------------------------------------------------

Total Unbilled Outpatient Care : 0.00

Total MRA Unbilled Outpatient Care : 0.00

Prescriptions:

Number of Unbilled Prescriptions : 0

Number of MRA Unbilled Prescriptions : 0

Total Unbilled Prescriptions : 0.00

Total MRA Unbilled Prescriptions : 0.00

Total Unbilled Amount (all care) : 99999.99

Total MRA Unbilled Amount (all care) : 77777.77

> **NOTE:** Average bill Amount is based on Bills Authorized during the 12

months preceding the month of this report.

> **NOTE:** Number of cases is insured cases in Claims Tracking that are

not billed (or bill not authorized/req MRA) but appear to be billable.

Enter message action (in IN basket): Ignore//

#### View Unbilled Amounts

This option can be used to view previously computed unbilled amounts without having to re-compile the data.

Select Unbilled Amounts Menu \<TEST ACCOUNT\> Option: View Unbilled Amounts

View unbilled amounts

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Unbilled Amounts Report Page 1 May 04, 2023@00:39:08

--------------------------------------------------------------------------------

Inpatient Care: 04/23

Number of Unbilled Inpatient Cases: 10

Number of Unbilled MRA Admissions: 0

Average Inpt. Institutional Bill Amount: 0.00

Average Inpt. Professional Bill Amount: 0.00

Total Unbilled Inpatient Care: 125761.30

Total MRA Unbilled Inpatient Care: 0.00

Outpatient Care: 04/23

Number of Unbilled Outpatient Cases: 8

Number of Unbilled CPT Codes: 0

Number of MRA Unbilled CPT Codes: 0

Total Unbilled Outpatient Care: 8399.34

Total MRA Unbilled Outpatient Care: 0.00

Prescriptions: 04/23

Number of Unbilled Prescriptions: 6

Number of MRA Unbilled Prescriptions: 0

Total Unbilled Prescriptions: 229397.19

Total MRA Unbilled Prescriptions: 0.00

Type \<Enter\> to continue or '^' to exit:

### Modified Billing Lag Time Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Modified Billing Lag Time Report provides a measure of the amount of time between significant milestones which occur during the claim submission and receivables management processes. These milestones are grouped by Inpatient and Outpatient activity.

Select Billing Reports \<TEST ACCOUNT\> Option: LAG Modified Billing lag time rept

This report measures the amount of time between significant milestones

which occur from the time treatment has been provided to the time that

the claim to the insurer for that treatment has been closed out.

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

Do you wish to print a (S)ummary or (D)etailed Report? s SUMMARY

This report only requires an 80 column printer.

> **NOTE:** This report searches through all Reimbursable Insurance claims.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

MODIFIED BILLING LAG TIME

OUTPATIENT SUMMARY REPORT

For Receivables with activity from 01/01/23 - 01/31/23

Run Date: MAY 04, 2023@10:51:54

======================================================

Time Period Average Number of days

----------- ----------------------

Date of Care to Date Claim Authorized 64.20

Date Claim Authorized to Date Claim Printed 0.05

Date Claim Printed to Date Claim Activated 1.97

Date Claim Activated to First Payment Date 27.54 (68 episodes)

Date of Care to Date of First Payment 92.47 (68 episodes)

Date of Care to Date Receivable Closed 96.79 (75 episodes)

First Payment Date to Date Receivable Closed 4.63 (68 episodes)

Type \<Enter\> to continue or '^' to exit:

MODIFIED BILLING LAG TIME

INPATIENT SUMMARY REPORT

For Receivables with activity from 01/01/23 - 01/31/23

======================================================

Time Period Average Number of days

----------- ----------------------

Date of Care to Date PTF Closed 0.00

Date PTF Closed to Date Claim Authorized 0.00

Date Claim Authorized to Date Claim Printed 0.00

Date Claim Printed to Date Claim Activated 0.00

Date Claim Activated to First Payment Date 0.00 (0 episodes)

Date of Care to Date of First Payment 0.00 (0 episodes)

Date of Care to Date Receivable Closed 0.00 (0 episodes)

First Payment Date to Date Receivable Closed 0.00 (0 episodes)

The total entries ignored......................... 5326

Type \<Enter\> to continue or '^' to exit:

### Billing Lag Time Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\> Out of order: Use New Menu Option

The Modified Billing Lag Time Report has replaced this report. This report option is obsolete and has been placed Out of Order.

## Follow-Up Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Follow-Up Reports provide a number of tools for monitoring receivables and following up on receivables processing and collections. These reports facilitate follow-up activities in a number of areas: First and Third Party Billing, Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA)/TRICARE Billing and Miscellaneous Billing. Options also allow for the assignment of cases/bills to clerks by a supervisor and productivity reporting of those assigned cases/bills. The Repayment Plan Status Report provides the ability to track and follow up on repayment plans.

The Follow-Up Reports Menu:

BD Bad Debt Report

PT Insurance Payment Trend Report

FP First Party Follow-Up Report

CH CHAMPVA/TRICARE Follow-Up Report

MB Miscellaneous Bills Follow-Up Report

AP Workload Assignment Print

FR Third Party Follow-Up Report

PR AR Productivity Report

RP Repayment Plan Follow-up Report

\*\*\> Out of order: This option is obsolete.

SR Third Party Follow-Up Summary Report

STR Repayment Plan Status Report

WL Workload Assignment Enter/Edit

### Bad Debt Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is delivered automatically to members of the CPAC’s local RC AR DATA COLLECTOR mail group *on the day after the last accounting day of the month*. It provides an <u>estimated</u> allowance for bad debts and contractual adjustments based on historical data. The report generates an automated Financial Management System (FMS) transaction to adjust allowance accounts in the general ledger. See the AR Asset Valuation Guide for more information about this report.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: BD Bad Debt Report

This option will print the Bad Debt Report. The Bad Debt allowance

estimates are computed by the AR Data Collector at the end of the

accounting month, and sent to FMS at that time. The allowance

estimate is no longer editable prior to transmission to FMS.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

please wait

Bad Debt Report

Allowance for Bad Debt and Contract Adjustment Report

for the month of APR 2023

Medical Care Collection Fund

Funds 528701; 528703; 528704; 528709; 528711; 528713; and 528714

----------------------------------------------------------------

Contract EOM

FUND - SGL Account Collection% Write-Off% Adjustment% Allowance

528701 - 1319 0.00 100.00 0.00 787,708.05

528703 - 1319 0.00 100.00 0.00 539,291.39

528704 - 1319 0.00 100.00 0.00 1,612,729.30

528704 - 1339 0.00 0.00 100.00 6,492.18

528704 - 133N 100.00 0.00 0.00 0.00

528704 - 1338 0.00 100.00 0.00 1,640,693.22

528709 - 1319 0.00 100.00 0.00 77,300.84

528711 - 1319 0.00 100.00 0.00 11,100.85

Press RETURN to continue, '^' to exit:

Bad Debt Report

Allowance for Bad Debt and Contract Adjustment Report

for the month of APR 2023

528711 - 133N 17.12 0.00 82.88 32,759.41

528711 - 1338 0.00 100.00 0.00 19,468.90

528713 - 1319 0.00 100.00 0.00 0.00

528713 - 1339 0.00 0.00 100.00 0.00

528713 - 133N 0.00 0.00 100.00 1,266,742.42

528713 - 1338 0.00 100.00 0.00 20,630.64

528714 - 1319.7 0.43 99.57 0.00 104,961.35

528714 - 1319.8 0.00 100.00 0.00 3,287.00

528714 - 1319.9 0.00 100.00 0.00 8,081.00

SGL Definitions

1319 Allowance for Bad Debt

1319.7 Allowance Community Care Inpatient/Outpatient/Urgent Care copayments

1319.8 Allowance Community Care RX copayments

Press RETURN to continue, '^' to exit:

Bad Debt Report

Allowance for Bad Debt and Contract Adjustment Report

for the month of APR 2023

1319.9 Allowance Community Care LTC copayments

1338 Allowance for Tort Feasors

1339 Allowance for Contract Adjustments pre-MRA (Medicare Remittance Advice)

133N Allowance for Contract Adjustments post-MRA

Only members in the facility's local RC AR DATA COLLECTOR mail group

will receive this report.

\<end of report, press return to continue\>

### Insurance Payment Trend Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to analyze payment trends among insurance companies and track receivables that are due to the facility. Many different criteria may be specified to limit the selection of bills such as rate type, inpatient or outpatient bills, open or closed bills, treatment dates, bill printed dates, and insurance companies.

The report may be run for a single insurance company or a range of companies. In addition, the user may analyze any specialized subset of bills by selecting an additional field from the BILL/CLAIMS file (#399) and specifying a range of values for that field.

The Insurance Payment Trend Report displays the Payer’s Name/Tax Identification Number (TIN) in the Header on the Summary and Main reports using the Payer TIN and Name stored in the 835.

The Insurance Payment Trend Report displays the 835 indicator (%) in front of the Patient Name if an 835 Electronic Remittance Advice (ERA) is attached to the reported claim.

The user has the option to run a detailed report for all claims that meet the report criteria, or to print summary statistics only. The detailed report includes the bill number, patient name and age (as of the bill event date), bill from and to dates, date the bill was printed (authorized), date the bill closed, the number of days the bill has been open (the difference between the DATE PRINTED and the DATE BILL CLOSED fields), the amounts billed, collected, unpaid, remaining open, and percentage collected. The AMOUNT PENDING column has been added to differentiate the number of unpaid dollars and the number of dollars that are still pending collection. If the bill is not closed, the amount pending is the same as the amount unpaid. If the bill is closed (signified by an asterisk next to the bill number), the amount pending is zero.

The report is sorted alphabetically by insurance company name and a subtotal for number of bills, amount billed, amount collected, amount unpaid, amount pending, and percentage collected is given for each company. If the user opts only to print summary statistics, only these subtotals are printed. Also included, for either the detailed or summary report, are the grand totals for these categories. A margin width of 132 columns is required for this output.

The DATE BILL CLOSED field will always have an entry. If the bill is not actually closed, the Accounts Receivable status of the bill will appear on the report in the DATE BILL CLOSED column. If a bill is closed, an asterisk (\*) will appear after the bill number. If a bill is rejected a c will display next to that bill number.

This report will identify insurance payment trends over a given period of time. The report should be generated beginning five months prior to the current date, then run for a three-month time period from that date to provide a more accurate picture of payment trends. The report is queued by rate type, bill status, treatment date, date bill printed, or insurance company. The report can be run in detail or summary, by division, and for specific carriers.

This report can be used to identify insurance payment trends and the effectiveness of facilities' billing and collection processes. The report needs to be reviewed in conjunction with the Billing Lag Time Reports. Direct correlation to poor billing and collection follow-up processes can be easily identified.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: PT Insurance Payment Trend Report

Do you wish to sort this report by division? NO//

Select RATE TYPE NAME: ?

Answer with RATE TYPE NUMBER, or NAME

Do you want the entire RATE TYPE List? y (Yes)

Choose from:

1 CRIME VICTIM Who's Responsible: INSURER

7 NO FAULT INS. Who's Responsible: INSURER

8 REIMBURSABLE INS. Who's Responsible: INSURER

10 TORT FEASOR Who's Responsible: INSURER

11 WORKERS' COMP. Who's Responsible: INSURER

13 CHAMPVA REIMB. INS. Who's Responsible: INSURER

14 CHAMPVA Who's Responsible: INSURER

15 TRICARE REIMB. INS. Who's Responsible: INSURER

16 TRICARE Who's Responsible: INSURER

18 FEE REIMB INS Who's Responsible: INSURER

19 HUMANITARIAN REIMB. INS. Who's Responsible: INSURER

20 INELIGIBLE REIMB. INS. Who's Responsible: INSURER

21 DENTAL REIMB. INS. Who's Responsible: INSURER

22 CC WORKERS' COMP Who's Responsible: INSURER

23 CC NO-FAULT AUTO Who's Responsible: INSURER

24 CC TORT FEASOR Who's Responsible: INSURER

25 CHOICE WORKERS' COMP Who's Responsible: INSURER

26 CHOICE NO-FAULT AUTO Who's Responsible: INSURER

27 CHOICE TORT FEASOR Who's Responsible: INSURER

28 CCN WORKERS' COMP Who's Responsible: INSURER

29 CCN NO-FAULT AUTO Who's Responsible: INSURER

30 CCN TORT FEASOR Who's Responsible: INSURER

31 CHOICE REIMB INS Who's Responsible: INSURER

32 CC REIMB INS Who's Responsible: INSURER

33 CCN REIMB INS Who's Responsible: INSURER

34 CC MTF REIMB INS Who's Responsible: INSURER

35 DOD DISABILITY EVALUATION Who's Responsible: INSURER

36 DOD SPINAL CORD INJURY Who's Responsible: INSURER

37 DOD TRAUMATIC BRAIN INJURY Who's Responsible: INSURER

38 DOD BLIND REHABILITATION Who's Responsible: INSURER

39 TRICARE DENTAL Who's Responsible: INSURER

40 TRICARE PHARMACY Who's Responsible: INSURER

42 OWCP Who's Responsible: INSURER

Select RATE TYPE NAME: 8 REIMBURSABLE INS. Who's Responsible: INSURER

You may select a field from the BILL/CLAIMS file which you may

use to limit the selection of records to appear on the report.

Do you wish to choose such a field? NO//

Select (I)NPATIENT, (O)UTPATIENT, or (B)OTH bill records: BOTH// BOTH

Print (C)OMBINED or (S)EPARATE reports: COMBINED// COMBINED

Select (O)PEN, (C)LOSED, or (B)OTH types of bills: BOTH// BOTH

Do you want to include cancelled bills? NO//

Print report by 1-DATE BILL PRINTED or 2-TREATMENT DATE: 1// DATE BILL PRINTED

Start with DATE BILL PRINTED: 010114 (JAN 01, 2014)

Go to DATE BILL PRINTED: 013114 (JAN 31, 2014)

Print (M)AIN REPORT, (S)UMMARY, or (G)RAND TOTALS: M// MAIN REPORT

Run report for (S)PECIFIC insurance companies or a (R)ANGE: RANGE// RANGE

Start with INSURANCE COMPANY: FIRST//

Go to INSURANCE COMPANY: LAST//

Sort by AMOUNT (O)WED, AMOUNT (P)AID, or (I)NSURANCE CO.: I// INSURANCE CO.

Do you want to include receivables referred to Reg. Counsel? NO//

(E)xcel Format or (R)eport Format: Report//

You will need a 132 column printer for this report!

DEVICE: HOME// 0;132

REIMBURSABLE INS. PAYMENT TREND REPORT - COMBINED INPATIENT AND OUTPATIENT BILLING MAY 04, 2023 PAGE 1

DATE BILL PRINTED: 01/01/14 - 01/31/14 Note: '\*' after the Bill No. denotes a CLOSED bill

BILL PATIENT DATE DATE BILL \# AMOUNT AMOUNT AMOUNT AMOUNT PERC

NUMBER NAME (AGE) BILL FROM - TO PRINTED CLOSED DAYS BILLED COLLECTED UNPAID PENDING COLL

------------------------------------------------------------------------------------------------------------------------------------

M A I N R E P O R T

INSURANCE CARRIER: AARP UNITEDHEALTHCARE/120201012

AARP HEALTHCARE OPTIONS

PO BOX 87654

ATLANTA, GEORGIA 303740819 Phone: 800 222-7777

Group \#: GRP NUM 23

%K403HYZ\* GGGG,MMMMMM (86) 05/21/13 05/21/13 01/13/14 01/27/14 14 8.54 8.54 0.00 0.00 100.00

%K403HZG\* GGGG,MMMMMM (87) 07/02/13 07/02/13 01/15/14 02/05/14 21 21.70 21.70 0.00 0.00 100.00

%K40386F\* QQQQQQQ,AAAAAAA (86) 10/01/13 10/01/13 01/14/14 01/27/14 13 14.74 14.74 0.00 0.00 100.00

%K403HG6\* QQQQQQQ,AAAAAAA (86) 11/19/13 11/19/13 01/13/14 01/27/14 14 25.22 25.22 0.00 0.00 100.00

%K403KBW\* QQQQQQQ,AAAAAAA (86) 10/01/13 10/01/13 01/22/14 02/05/14 14 8.54 8.54 0.00 0.00 100.00

%K403JT5\* RRRRRRRRRR,DDDDD (82) 12/20/13 12/20/13 01/14/14 02/05/14 22 114.37 114.37 0.00 0.00 100.00

%K403JUS\* RRRRRRRRRR,DDDDD (82) 12/17/13 12/17/13 01/14/14 02/05/14 22 14.74 14.74 0.00 0.00 100.00

%K403JUT\* RRRRRRRRRR,DDDDD (82) 12/17/13 12/17/13 01/14/14 02/05/14 22 4.96 4.96 0.00 0.00 100.00

Group \#: GRP NUM 335

%K403HTC\* HHHHH,EEE LLLLL (86) 12/12/13 12/12/13 01/10/14 02/05/14 26 25.22 25.22 0.00 0.00 100.00

%K4031T1\* RRRRRRRRRR,DDDDD (82) 09/10/13 09/10/13 01/14/14 02/05/14 22 14.74 14.74 0.00 0.00 100.00

%K403IRF\* RRRRRRRRRR,DDDDD (82) 09/10/13 09/10/13 01/14/14 02/05/14 22 8.54 8.54 0.00 0.00 100.00

Group \#: GRP NUM 449

%K403D32\* FFFFFFF,AAAAAA E (91) 12/11/13 12/12/13 01/02/14 01/17/14 15 1184.00 1184.00 0.00 0.00 100.00

%K403DAA\* FFFFFFF,AAAAAA E (91) 12/11/13 12/12/13 01/02/14 01/17/14 15 26.15 26.15 0.00 0.00 100.00

%K403DAF\* FFFFFFF,AAAAAA E (91) 10/07/13 10/12/13 01/02/14 01/17/14 15 1184.00 1184.00 0.00 0.00 100.00

%K403NNW\* FFFFFFF,AAAAAA E (91) 12/26/13 01/13/14 01/28/14 02/14/14 17 7.70 7.70 0.00 0.00 100.00

%K403NP0\* FFFFFFF,AAAAAA E (91) 12/26/13 01/13/14 01/28/14 02/25/14 28 73.01 14.60 58.41 0.00 20.00

%K403NPH\* FFFFFFF,AAAAAA E (91) 12/26/13 01/13/14 01/28/14 02/14/14 17 14.60 14.60 0.00 0.00 100.00

%K403NPI\* FFFFFFF,AAAAAA E (91) 01/10/14 01/13/14 01/28/14 02/14/14 17 1.88 1.88 0.00 0.00 100.00

%K403NPN\* FFFFFFF,AAAAAA E (91) 01/10/14 01/13/14 01/28/14 02/14/14 17 29.20 29.20 0.00 0.00 100.00

%K403NPQ\* FFFFFFF,AAAAAA E (91) 01/10/14 01/13/14 01/28/14 02/14/14 17 14.66 14.66 0.00 0.00 100.00

Group \#: GRP NUM 564

%K403JMD\* GGGGG,SSSSSSSSS (89) 12/11/13 12/11/13 01/14/14 01/27/14 13 22.81 22.81 0.00 0.00 100.00

%K403JMH\* GGGGG,SSSSSSSSS (89) 12/11/13 12/11/13 01/14/14 01/27/14 13 41.93 41.93 0.00 0.00 100.00

%K403L2K\* GGGGG,SSSSSSSSS (89) 12/13/13 12/13/13 01/15/14 02/05/14 21 22.05 22.05 0.00 0.00 100.00

%K403L2Q\* GGGGG,SSSSSSSSS (89) 12/13/13 12/13/13 01/16/14 02/05/14 20 24.43 24.43 0.00 0.00 100.00

%K403HD8\* PPPPPPPP,RRRRR W (89) 12/05/13 12/05/13 01/13/14 02/04/14 22 508.84 19.40 489.44 0.00 3.81

%K403HD9\* PPPPPPPP,RRRRR W (89) 12/05/13 12/05/13 01/10/14 01/31/14 21 80.81 13.15 67.66 0.00 16.27

%K403HH1\* SSSSSSS,SSSS OOO (88) 11/06/13 11/06/13 01/13/14 01/27/14 14 25.22 25.22 0.00 0.00 100.00

%K403IQG\* ZZZZZZ,TTTTTTT W (87) 12/11/13 12/11/13 01/14/14 01/27/14 13 7.02 7.02 0.00 0.00 100.00

Group \#: GRP NUM 1736

%K403HXA\* DDDDDDDD,MMMMMM (87) 11/15/13 11/15/13 01/09/14 01/23/14 14 11.36 11.36 0.00 0.00 100.00

%K403JVP\* LLLLLLLL,GGGGGGG (86) 11/19/13 11/19/13 01/16/14 02/06/14 21 9.89 9.89 0.00 0.00 100.00

%K403CC7\* RRRRRRRR,NNNNN L (88) 11/19/13 11/19/13 01/02/14 02/14/14 43 24.93 24.93 0.00 0.00 100.00

K403ANJ\* RRRRRRRR,NNNNN L (88) 10/25/13 10/25/13 01/02/14 02/14/14 43 23.28 23.28 0.00 0.00 100.00

Group \#: GRP NUM 2413

%K403JWK\* WWWWWWWWWWW,PPPP (89) 12/20/13 12/20/13 01/29/14 02/14/14 16 19.40 19.40 0.00 0.00 100.00

%K403NJ1\* WWWWWWWWWWW,PPPP (89) 12/20/13 12/20/13 01/28/14 02/14/14 17 13.15 13.15 0.00 0.00 100.00

### First Party Follow-Up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides account information necessary for efficient follow-up on active and suspended first party accounts. The report will prompt the user to select the first party receivables that are to be included in the report: a date range and various other sort and print criteria. This report can be run in detail, summary, or overall summary formats. There are five AR categories included in this report: (1) Emergency/Humanitarian, (2) Ineligible, (3) C (Means Test) and Rx Co-Payment, (4) Long Term Care Copay, (5) Community Care Copay and (6) All of the Above. In addition, this report is Excel ready for easy transfer of information to a spreadsheet format.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: FP First Party Follow-Up Report

Choose which type of receivables to print:

1 - EMERGENCY/HUMANITARIAN

2 - INELIGIBLE

3 - C-MEANS TEST & RX COPAY

4 - LONG TERM CARE COPAY

5 - COMMUNITY CARE COPAY

6 - ALL OF THE ABOVE

Select: (1-6): 6//

You have selected

6 - ALL OF THE ABOVE

Are you sure? NO// YES

Run report for (A)CTIVE ARs, (S)USPENDED ARs, or (B)OTH: B// BOTH

Do you wish to print a (S)ummary, (O)verall Summary or (D)etailed Report? SUMMARY

Include ARs referred to Regional Counsel? NO//

> **NOTE:** This report will search through all active & suspended receivables.

It is recommended that you queue it to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

FIRST PARTY FOLLOW-UP SUMMARY REPORT Run Date: MAY 04, 2023@23:42:03 Page: 1

RECEIVABLES REFERRED TO RC NOT INCLUDED

ACTIVE INELIGIBLE HOSP.

=======================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 1 (100.00%) 453.00 (100.00%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 0 (0.00%) 0.00 (0.00%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 0 (0.00%) 0.00 (0.00%)

Over 365 days 0 (0.00%) 0.00 (0.00%)

Total First Party Receivables 1 (100%) \$453.00 (100%)

Type \<Enter\> to continue or '^' to exit:

FIRST PARTY FOLLOW-UP SUMMARY REPORT Run Date: MAY 04, 2023@23:42:03 Page: 2

RECEIVABLES REFERRED TO RC NOT INCLUDED

SUSPENDED INELIGIBLE HOSP.

==========================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

There are no statistics for this category.

Type \<Enter\> to continue or '^' to exit:

\<Report output truncated

### CHAMPVA/TRICARE Follow-Up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Reports include CHAMPVA, CHAMPVA Reimbursable Tricare Patient, Tricare, Tricare Reimbursable and Sharing Agreement Bills printed on UB-92 and HCFA 1500s.

1.  Other types of Sharing Agreement Bills completed on 1114s or 1080s will be located under the Miscellaneous Bills Follow-up Reports.

These reports provide current data as of the date printed. The report may be customized by:

- Category of Bill
- Division
- Detail or Summary Reports
- Choice of Inpatient, Outpatient, Prescriptions or All
- Specify Patient Name/SSN Range
- Minimum Age of Bills
- Minimum Age Since Last Comment

Included with these reports is the option to have the detailed reports in a format for downloading to Excel. Most of the options above are available on the Excel spreadsheet with the exception of the Bill Comments; it will only print the last comment date.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: CHAMPVA/TRICARE Follow-Up Report

Choose which category of receivables to print:

1 - TRICARE PATIENT

2 - SHARING AGREEMENTS

3 - TRICARE

4 - TRICARE THIRD PARTY

5 - CHAMPVA

6 - CHAMPVA THIRD PARTY

7 - ALL OF THE ABOVE

Select: (1-7): 7// 1

You have selected

1 - TRICARE PATIENT

Are you sure? NO// y YES

Choose which type of receivables to print:

1 - INPATIENT

2 - OUTPATIENT

3 - PHARMACY REFILL

4 - ALL RECEIVABLES

Select: (1-4): 4// 4

You have selected

4 - ALL RECEIVABLES

Are you sure? NO// y YES

Do you wish to print a (S)ummary or (D)etailed Report? s SUMMARY

You will need a 80 column printer for this report!

> **NOTE:** This report will search through all active receivables.

You should queue it to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

CHAMPVA/TRICARE FOLLOW-UP SUMMARY REPORT Page: 1

Run Date: MAY 05, 2023@00:07:22

TRICARE PATIENT RECEIVABLES (INPATIENT)

=======================================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 0 (0.00%) 0.00 (0.00%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 0 (0.00%) 0.00 (0.00%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 18 (75.00%) 10,739.00 (76.48%)

Over 365 days 6 (25.00%) 3,302.21 (23.52%)

Total 24 (100%) 14,041.21 (100%)

Type \<Enter\> to continue or '^' to exit:

CHAMPVA/TRICARE FOLLOW-UP SUMMARY REPORT Page: 2

Run Date: MAY 05, 2023@00:07:22

TRICARE PATIENT RECEIVABLES (OUTPATIENT)

========================================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 2 (6.67%) 60.00 (2.75%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 1 (3.33%) 27.00 (1.24%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 15 (50.00%) 618.00 (28.35%)

Over 365 days 12 (40.00%) 1,474.99 (67.66%)

Total 30 (100%) 2,179.99 (100%)

Type \<Enter\> to continue or '^' to exit:

CHAMPVA/TRICARE FOLLOW-UP SUMMARY REPORT Page: 3

Run Date: MAY 05, 2023@00:07:22

TRICARE PATIENT RECEIVABLES (PHARMACY REFILL)

=============================================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 0 (0.00%) 0.00 (0.00%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 0 (0.00%) 0.00 (0.00%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 20 (68.97%) 477.00 (70.67%)

Over 365 days 9 (31.03%) 198.00 (29.33%)

Total 29 (100%) 675.00 (100%)

Type \<Enter\> to continue or '^' to exit:

### Miscellaneous Bills Follow-Up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Miscellaneous Bills Follow-up Report contains the following categories of bills:

Group 1 contains Medicare, No-Fault Auto, Tort Feasor, Workman’s Compensation.

Group 2 contains Current Employee, Ex-Employee, Federal Agencies-Reimbursement, Interagency, Military, and Vendor.

There will be a separate summary report for No-Fault, Workers’ Compensation, and Tort Feasors. A second summary report will be for the remaining categories.

There are two detailed reports: The first will have Medicare, No-Fault, Workers’ Compensation, and Tort Feasors, as these claims are billed on UB-92 and Health Care Financing Administration (HCFA) 1500s for medical treatment rendered. A second summary report will be for the remaining categories.

The reports will provide current data was of the date printed and is in detail. The reports may be customized by:

- Choice of Category of Bill
- Specified Patient Name or SSN ranges
- Including Bill Comments or Last Comment Only
- Minimum Age of Bills
- Division
- Detail or Summary Reports
- Minimum Age Since Last Comment
- Include or Exclude Bills Referred to Regional Counsel

Included with these reports is the option to have the detailed reports download for Excel. Most of the options above are available on the Excel spreadsheet with the exception of the Bill Comments; it will only print the last comment date.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: MB Miscellaneous Bills Follow-Up Report

Choose which type of receivables to print:

1 - MEDICARE

2 - NO-FAULT AUTO ACCIDENT

3 - COMMUNITY CARE NO-FAULT AUTO ACCIDENT

4 - TORT FEASOR

5 - COMMUNITY CARE TORT FEASOR

6 - WORKMEN'S COMP

7 - COMMUNITY CARE WORKMEN'S COMP

8 - CURRENT EMPLOYEE

9 - EX-EMPLOYEE

10 - FEDERAL AGENCIES-REFUND

11 - FEDERAL AGENCIES-REIMBURSEMENT

12 - MILITARY

13 - INTERAGENCY

14 - VENDOR

15 - FEDERAL OWCP

16 - ALL OF THE ABOVE

Select: (1-16): 16// 9

You have selected

9 - EX-EMPLOYEE

Are you sure? NO// YES

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

You will need a 80 column printer for this report!

> **NOTE:** This report will search through all active receivables.

You should queue it to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

MISCELLANEOUS BILLS FOLLOW-UP SUMMARY REPORT Page: 1

Run Date: MAY 05, 2023@00:12:03

EX-EMPLOYEE RECEIVABLES

=======================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 0 (0.00%) 0.00 (0.00%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 0 (0.00%) 0.00 (0.00%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 0 (0.00%) 0.00 (0.00%)

Over 365 days 26 (100.00%) 31,274.09 (100.00%)

Total 26 (100%) 31,274.09 (100%)

Type \<Enter\> to continue or '^' to exit:

### Workload Assignment Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the printing of selected or all Workload Assignments stored in file \#351.73. Assignments are made using the Workload Assignment Enter/Edit option, which is also in the same menu. After the option is chosen, the user is asked to run the report for (S)pecific clerks or (A)ll clerks. The user is then prompted for the printer/device.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: AP Workload Assignment Print

Run list for (S)pecific clerks or (A)ll clerks: ALL// ALL

This report requires an 80 column printer.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

AR Workload Assignments List Run Date: MAY 08, 2023@14:23:48 Page: 1

=============================================================================

WWWW,MMMMM S Productivity report only? NO

SSSSSSSSS,III A Productivity report only? YES

OOOOOOO,TTTTTT H Productivity report only? NO

CCCCCCCC,GGGGGGG A Productivity report only? NO

Assignment \#: 1 Bill Category: ADULT DAY HEALTH C Min Acct Bal: 0.00

Supervisor: WWWWWW,MMMMM H Exclude Reg Counsel: YES

FIRST PARTY PARAMETERS:

Days Since Last Payment : 45

First Patient Name :

Last Patient Name :

Type \<Enter\> to continue or '^' to exit:

AR Workload Assignments List Run Date: MAY 08, 2023@14:23:48 Page: 2

================================================================================

Assignment \#: 2 Bill Category: C (MEANS TEST) Min Acct Bal: 0.00

Supervisor: WWWWWW,MMMMM H Exclude Reg Counsel: YES

FIRST PARTY PARAMETERS:

Days Since Last Payment : 45

First Patient Name :

Last Patient Name :

Assignment \#: 3 Bill Category: CHAMPVA Min Acct Bal: 0.00

Supervisor: WWWWWW,MMMMM H Exclude Reg Counsel: YES

THIRD PARTY PARAMETERS:

Days Since Last Transaction : 45

First Insurance Carrier :

Last Insurance Carrier :

First Patient Name :

Last Patient Name :

Type of Receivable :

Assignment \#: 4 Bill Category: CHAMPVA SUBSISTENC Min Acct Bal: 0.00

Supervisor: WWWWWW,MMMMM H Exclude Reg Counsel: YES

Type \<Enter\> to continue or '^' to exit:

### Third Party Follow-Up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Third Party Follow-Up report provides pertinent data for follow-up with reimbursable insurance carriers and includes all active reimbursable bills. The report provides current data as of the date printed and is detail only. The report may be customized by:

- A specified patient name range
- Including Bill Comment Log
- Including referrals to Regional Counsel
- All claims OR broken down by inpatient, outpatient, pharmacy, or a combination of the four
- All active ARs or those within a certain date range
- Specifying a minimum dollar amount

Select Follow-Up Reports \<TEST ACCOUNT\> Option: Third Party Follow-Up Report

This report provides a tool for sites to use to perform follow-up

activities for Third Party receivables.

Calculate report using (D)ATE OF CARE or (A)CTIVE IN AR (days): (A)CTIVE IN AR// D DATE OF CARE

Do you wish to sort this report by division? NO//

Run report for (S)PECIFIC insurance companies or a (R)ANGE: RANGE// RANGE

START WITH INSURANCE COMPANY: FIRST// AAAA \< == Please CAPITALIZE entry

GO TO INSURANCE COMPANY: LAST// ZZZZ \< == Please CAPITALIZE entry

START WITH PATIENT NAME: FIRST// \< == Please CAPITALIZE entry

GO TO PATIENT NAME: LAST// \< == Please CAPITALIZE entry

Choose which type of receivables to print:

1 - INPATIENT

2 - OUTPATIENT

3 - PHARMACY REFILL

4 - COMMUNITY CARE RECEIVABLES

5 - ALL RECEIVABLES

Select: (1-5): 5//

Include (A)LL active AR's or those within an AGE (R)ANGE: ALL// ALL

Print receivables with a minimum balance? NO//

Include the Bill Comment history with each receivable? NO//

Include receivables referred to Regional Counsel? NO//

This report requires a 132 column printer.

> **NOTE:** This report will search through all active receivables.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80// 132

Third Party Follow-Up Report ( date of care ) Run Date: MAY 05, 2023@00:19:36 Page: 1

All active receivables

Other Date Original Current

Patient (Age) Carrier Prepared Bill No. Bill Fr. Bill To Amount Balance Subscriber ID

====================================================================================================================================

Carrier: AARP UNITEDHEALTHCARE, AARP HEALTHCARE OPTIONS, ATLANTA, GA 303740819 Billing Phone: 800 227-7789

ABBB,VVVVV DDDD (84) 12/04/19 442-K003I2R 04/09/19 04/09/19 64.74 64.74

ATTTTTTT,MMMMMMM (84) 10/07/19 %442-K0031PZ 08/13/19 08/13/19 77.12 77.12

10/11/19 %442-K0033JQ 03/18/19 03/18/19 236.43 87.70

11/19/19 %442-K003DLQ 10/23/19 10/23/19 238.66 238.66

11/19/19 %442-K003DLU 10/23/19 10/23/19 26.83 26.83

11/19/19 %442-K003DLV 10/23/19 10/23/19 34.94 34.94

BAAAAAAAA,AAAAAAA (90) 11/20/19 %442-K003EET 10/23/19 10/23/19 21.42 21.42

11/21/19 %442-K003EES 10/23/19 10/23/19 23.17 23.17

BBBBBBBB,RRRRRR W (74) 11/21/19 %442-K003FLE 10/24/19 10/24/19 15.91 15.91

11/27/19 442-K003FLJ 10/24/19 10/24/19 23.17 23.17

BCCCCC,PPPP AAAAA (88) 11/27/19 442-K906TJ4 06/13/19 06/13/19 11.18 11.18

Type \<Enter\> to continue or '^' to exit:

Third Party Follow-Up Report ( date of care ) Run Date: MAY 05, 2023@00:19:36 Page: 2

All active receivables

Other Date Original Current

Patient (Age) Carrier Prepared Bill No. Bill Fr. Bill To Amount Balance Subscriber ID

====================================================================================================================================

Carrier: AARP UNITEDHEALTHCARE, AARP HEALTHCARE OPTIONS, ATLANTA, GA 303740819 Billing Phone: 800 227-7789

BDDDDDDDDD,VVVVV (93) 12/09/19 442-K003L4Q 11/08/19 11/08/19 99.50 99.50

12/09/19 442-K003L4R 11/08/19 11/08/19 14.95 14.95

BEEEEE,DDDDD (80) 11/20/19 %442-K003E0F 10/23/19 10/23/19 13.91 13.91

11/20/19 %442-K003E0G 10/23/19 10/23/19 3.44 3.44

11/21/19 %442-K003E0E 10/23/19 10/23/19 46.12 46.12

12/10/19 442-K003L78 11/13/19 11/13/19 10.24 10.24

12/10/19 442-K003L79 11/13/19 11/13/19 23.17 23.17

BFFFFFFF,CCCCC CC (75) 11/26/19 %442-K003H8X 11/01/19 11/01/19 23.17 23.17

11/26/19 %442-K003H8Y 11/01/19 11/01/19 20.39 20.39

BGGGG,AAAAAAA PPP (96) 12/10/19 442-K003L44 11/06/19 11/06/19 53.11 53.11

12/10/19 442-K003L8D 11/08/19 11/08/19 40.82 40.82

Type \<Enter\> to continue or '^' to exit:

### AR Productivity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report shows clerk activity based on transaction types and timeframes. The user is prompted for a transaction date range, and whether to run the report for (A)LL or (S)PECIFIC Clerks. A summary or detailed output is then chosen. The user may print the summary by Clerk and then print with the Clerk’s (N)ame or (I)dentifier. The output is an 80-column output.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: PR AR Productivity Report

FROM Transaction Date: 010123 (JAN 01, 2023)

TO Transaction Date: 013123 (JAN 31, 2023)

Run report for (A)LL or (S)PECIFIC Clerks: A// ALL

Do you wish to print a (S)ummary or (D)etailed Report? SUMMARY

Do you want to print the summary by Clerk? YES//

Do you wish to print with Clerk (N)ame or (I)dentifier? NAME

This report requires a 80 column printer.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

SUMMARY AR PRODUCTIVITY REPORT

From JAN 1,2023 to JAN 31,2023

MAY 08, 2023@14:42:09

====================

Clerk Transaction Category Total Number Total Dollar Amt

================================================================================

BBBBBBBB,LLLLLLL N COMMENT 36 0.00

AUDIT 1 105.66

DEC.ADJ./CONTR 15 170.67

--------- -------------

52 276.33

BCCCCC,LLLL D COMMENT 12 0.00

--------- -------------

12 0.00

Type \<Enter\> to continue or '^' to exit:

SUMMARY AR PRODUCTIVITY REPORT

From JAN 1,2023 to JAN 31,2023

MAY 08, 2023@14:42:09

====================

Clerk Transaction Category Total Number Total Dollar Amt

================================================================================

CCCCCCCC,III M COMMENT 1 0.00

PAYMENT 425 68,374.24

DEC.ADJ./CONTR 467 155,981.05

DEC.ADJ./NON-CONTR 39 38,211.45

EXEMPTION 31 61.54

--------- -------------

963 262,628.28

CDDDDD,WWWWWWW A COMMENT 2 0.00

DEC.ADJ./CONTR 31 5,794.93

--------- -------------

33 5,794.93

Type \<Enter\> to continue or '^' to exit:

SUMMARY AR PRODUCTIVITY REPORT

From JAN 1,2023 to JAN 31,2023

MAY 08, 2023@14:42:09

====================

Clerk Transaction Category Total Number Total Dollar Amt

================================================================================

CGGGG,RRRRRR L DEC.ADJ./NON-CONTR 1 24,434.76

CHHHHH,CCCCCCC A COMMENT 1 0.00

CMMMMMM,EEEEEEEEE S PAYMENT 1 15.00

DEC.ADJ./NON-CONTR 21 500.29

EXEMPTION 6 28.60

OTHER 129 5,579.40

--------- -------------

157 6,123.29

Type \<Enter\> to continue or '^' to exit:

### Repayment Plan Follow-up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\> Out of order: This option is obsolete.

This option is obsolete and has been placed Out of Order. Please use the new Repayment Plan Status Report.

### Third Party Follow-Up Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides a summary of all outstanding third party receivables and can be used as a tool for sites to use to perform follow-up activities for third party receivables.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: SR Third Party Follow-Up Summary Report

This report provides a summary of all outstanding Third Party receivables.

Calculate report using (D)ATE OF CARE or (A)CTIVE IN AR (days): (A)CTIVE IN AR// DA DATE OF CARE

Do you wish to sort this report by division? NO//

Choose which type of summaries to print:

1 - INPATIENT RECEIVABLES

2 - OUTPATIENT RECEIVABLES

3 - PHARMACY REFILL RECEIVABLES

4 - COMMUNITY CARE RECEIVABLES

5 - ALL RECEIVABLES

Select: (1-5): 5//

This report only requires an 80 column printer.

> **NOTE:** This report requires a search through all active receivables.

You should queue this report to run after normal business hours.

DEVICE: HOME// HOME (CRT) Right Margin: 80//

THIRD PARTY FOLLOW-UP SUMMARY REPORT

ALL REIMBURSABLE RECEIVABLES ( date of care )

Run Date: MAY 05, 2023@10:29:03

===============================

AR Category \# Receivables Total Outstanding Balance

----------- ------------- -------------------------

Less than 30 days old 0 (0.00%) \$0.00 (0.00%)

31-60 days 0 (0.00%) 0.00 (0.00%)

61-90 days 0 (0.00%) 0.00 (0.00%)

91-120 days 0 (0.00%) 0.00 (0.00%)

121-180 days 0 (0.00%) 0.00 (0.00%)

181-365 days 4 (0.06%) 877.13 (0.02%)

Over 365 days 6671 (94.02%) 4,525,962.11 (96.90%)

Referred to Regional Counsel 420 (5.92%) 143,906.75 (3.08%)

Total Third Party Receivables 7095 (100%) \$4,670,745.99 (100%)

Type \<Enter\> to continue or '^' to exit:

### Repayment Plan Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows users to generate the Repayment Plan Status Report. The report provides a list of Repayment Plans which can be sorted and filtered by the user. The user is first asked to sort by Debtor (N)ame, (S)tatus, or (A)ccount Balance. The user may then filter by Debtor (N)ame, (S)tatus, or produce the output (U)nfiltered. For the example below, the user sorts by Debtor Name, and then filters for those Repayment plans that are New. Statuses available for user choice include (A)ll, (N)ew, (C)urrent, (L)ate, (D)elinquent, (P)aid in Full, and Clo(S)ed. The user may select one, many, or all.

Next, the user chooses the minimum number of days the Plan is in that status; entering a zero would provide a list of those added that day. The next prompt asks whether the output is to be exported to Excel. The Device prompt is then displayed; note that the report output is 132 columns.

This report should be used to track repayment plans, both current and defaulted. The user has the ability to generate a list of repayment plans which can be sorted and filtered. The user can, for example, generate a list of plans that have the status of Late and Delinquent. Statuses available for user choice include (A)ll, (N)ew, (C)urrent, (L)ate, (D)elinquent, (P)aid in Full, and Clo(S)ed. The user may select one, many, or all.

A nightly MailMan bulletin will also be sent during the PRCA Nightly Background Job processing. This bulletin will be sent to the RC REPAY PLANS mail group. It will report on (1) any debtors who defaulted on their repayment plan and (2) debtors with repayment plans who had new active bills.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: Repayment Plan Status Report

Repayment Plan Status Report

Sort By Debtor (N)ame, (S)tatus or (A)ccount Balance: N// ame

Filter By Debtor (N)ame, (S)tatus or (U)nfiltered: S// s Status

Statuses available:

(A)ll, (N)ew, (C)urrent, (L)ate, (D)elinquent, (P)aid in Full, Clo(S)ed,

Statuses currently selected: None

Select Status to add, Enter to continue or (Q)uit? New

Statuses available:

(A)ll, (N)ew, (C)urrent, (L)ate, (D)elinquent, (P)aid in Full, Clo(S)ed,

Statuses currently selected: New

Select Status to add, Enter to continue or (Q)uit?

Enter the Minimum \# of Days in Status or ^ to quit: 0

Export to Excel (Y/N)? YES// N NO

This report requires 132 column display.

DEVICE: 0;132 HOME (CRT)

Repayment Plan Status Report Sep 21, 2021 Page: 1

Filtered by: Status (NEW), at least 0 days in status

Sorted by: Debtor name

For-

Original Status Days in Last Cur plan Remaining bear-

Name SSN RPP ID Plan Dt Stat date status payment length balance CS ances

------------------------------------------------------------------------------------------------------------------------------------

AAAA,RRRRRR E XXXX 442-RPP-02-000066 06/29/21 NEW 06/29/21 84 5 \$114.00 Y

DDDDD,RRRRRRR A XXXX 442-RPP-01-000070 08/31/21 NEW 08/31/21 21 40 \$197.00 N

EEEEEEE MM VENDOR N/A 442-RPP-01-000060 06/11/21 NEW 06/11/21 102 53 \$2604.28 N

IIIIII,DDDDDDD RRR XXXX 442-RPP-01-000071 08/31/21 NEW 08/31/21 21 39 \$730.00 N

SSSSS,QQQQQQQ MMMMMM XXXX 442-RPP-01-000044 05/12/21 NEW 05/12/21 132 10 \$498.82 Y

TTTTTTTT,BBBBBB LLLLLLLL XXXX 442-RPP-01-000056 06/10/21 NEW 06/10/21 103 6 \$65.10 Y

Press \<return\> to continue

2.  When using the filter by Debtor (N)ame, please ensure the entries for the START WITH NAME and GO TO NAME fields are capitalized.  
    The example that follows generates a report of Repayment Plans where the Debtor’s last name begins with the letter ‘M.’

Select Repayment Plan Menu \<TEST ACCOUNT\> Option: STR Repayment Plan Status Report

Repayment Plan Status Report

Sort By Debtor (N)ame, (S)tatus or (A)ccount Balance: N// ame

Filter By Debtor (N)ame, (S)tatus or (U)nfiltered: S// Name

START WITH NAME: FIRST// MAAA \< == Please CAPITALIZE entry

GO TO NAME: LAST// MZZZ \< == Please CAPITALIZE entry

Export to Excel (Y/N)? YES// NO

This report requires 132 column display.

DEVICE: 0;132;999 HOME (CRT)

Repayment Plan Status Report Sep 21, 2021 Page: 1

Filtered by: Debtor name (from MAA to MZZ)

Sorted by: Debtor name

For-

Original Status Days in Last Cur plan Remaining bear-

Name SSN RPP ID Plan Dt Stat date status payment length balance CS ances

------------------------------------------------------------------------------------------------------------------------------------

MAAAAAA,VVVVV EEEEEE XXXX 442-RPP-01-000052 06/09/21 NEW 06/09/21 104 11 \$101.00 N

MDDDD,EEE RRR XXXX 442-RPP-01-000021 04/28/21 CURR 04/28/21 146 3 \$60.25 N 0

MHHHHH,BBBBBB KKK XXXX 442-RPP-01-000048 06/08/21 NEW 06/08/21 105 15 \$1456.01 Y

MNNNNNN,RRRR DDDD XXXX 442-RPP-01-000006 04/28/21 CURR 04/28/21 146 11 \$257.68 N 0

MYYYY,SSSS RRRRRR XXXX 442-RPP-01-000035 04/28/21 CURR 04/28/21 146 5 \$226.11 N 0

Press \<return\> to continue

### Workload Assignment Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the entering/editing of Workload Assignments for clerks. This information is stored in file \#351.73. The user chooses the option and then selects a clerk. The system will then ask if the clerk should appear on Workload reports and Productivity reports, or just on the Productivity reports. Next, the clerk’s assignments will be displayed, and the user is allowed to (A)dd, (E)dit, or (D)elete an assignment. The user is then prompted to choose an Accounts Receivable Category, the Minimum Account Balance, whether to exclude Receivables referred to RC, and the number of days since the last payment. Finally, the system allows the user to sort patients by (N)ame or (L)ast 4 of the SSN, and then choose a range of patients to include.

Select Follow-Up Reports \<TEST ACCOUNT\> Option: WL Workload Assignment Enter/Edit

Select Clerk: CCCCCCCC,III M IMC 04 ACCOUNTS RECEIVABLE TECH

...OK? Yes// (Yes)

PRODUCTIVITY REPORT ONLY?: NO// ??

The flag that determines if Workload reports and Productivity reports will be

produced for this clerk OR if the clerk will only appear on Productivity reports.

Choose from:

0 NO

1 YES

PRODUCTIVITY REPORT ONLY?: NO// NO

EXCLUDE REFER

ASSIGNMENT CATEGORY MIN BALANCE TO REG COUNSEL LIMITED BY CARRIER/NAME/SSN

1 ADULT DAY HEA 0.00 NO LAST PMT

2 C (MEANS TEST 0.00 NO LAST PMT

3 CHAMPVA 0.00 NO LAST TRX/REC.TYPE

4 CHAMPVA SUBSI 0.00 NO LAST PMT

5 CHAMPVA THIRD 0.00 NO LAST TRX/REC.TYPE

6 COMP & PEN PR 0.00 NO LAST TRX/REC.TYPE

7 CRIME OF PER. 0.00 NO LAST TRX/REC.TYPE

8 CURRENT EMP. 0.00 NO LAST PMT

9 CWT PROCEEDS 0.00 NO LAST TRX/REC.TYPE

10 DOMICILIARY 0.00 NO LAST PMT

11 EMERGENCY/HUM 0.00 NO LAST PMT

12 ENHANCED USE 0.00 NO LAST TRX/REC.TYPE

13 EX-EMPLOYEE 0.00 NO LAST PMT

14 FEDERAL AGENC 0.00 NO LAST TRX/REC.TYPE

15 FEDERAL AGENC 0.00 NO LAST TRX/REC.TYPE

16 GERIATRIC EVA 0.00 NO LAST PMT

17 GERIATRIC EVA 0.00 NO LAST PMT

18 INELIGIBLE HO 0.00 NO LAST PMT

19 INTERAGENCY 0.00 NO LAST TRX/REC.TYPE

20 MEDICARE 0.00 NO LAST TRX/REC.TYPE

21 MILITARY 0.00 NO LAST TRX/REC.TYPE

(A)dd, (E)dit, or (D)elete Assignment: (A/E/D): ADD

Adding new assignment - \# 22 - for CCCCCCCC,III M

Select ACCOUNTS RECEIVABLE CATEGORY: ??

Choose from:

ADULT DAY HEALTH CARE AD

C (MEANS TEST) C

CC INPT CJ

CC MTF INPT CX

CC MTF OPT D3

CC MTF RX CO-PAYMENT CY

CC MTF THIRD PARTY C4

CC NO-FAULT AUTO C8

CC NURSING HOME CARE - LTC CL

CC OPT D1

CC RESPITE CARE CN

CC RX CO-PAYMENT CK

CC THIRD PARTY C2

CC TORT FEASOR C9

CC URGENT CARE U1

CC WORKERS' COMP CA

CCN INPT CO

CCN NO-FAULT AUTO CB

CCN NURSING HOME CARE - LTC CR

^

Select ACCOUNTS RECEIVABLE CATEGORY: C (MEANS TEST) C

MINIMUM ACCOUNT BALANCE: 20

EXCLUDE RECEIVABLES REFERRED TO RC? YES//

DAYS SINCE LAST PAYMENT: 45//

Sort Patients by (N)ame or (L)ast 4 of the SSN: NAME

START WITH PATIENT NAME: FIRST// DAAA \< == Please CAPITALIZE entry

GO TO PATIENT NAME: LAST// DZZZ \< == Please CAPITALIZE entry

Select Clerk:

<u>One Note</u>: When using the filter by Patient Name, please ensure the entries for the START WITH NAME and GO TO NAME fields are capitalized. The example that follows generates a report of Repayment Plans where the Debtor’s last name begins with the letter ‘D.’

## Utilization Management Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Utilization Management Reports allow for the measurement of the Utilization Management process. This process is performed by Revenue Utilization Review (RUR) nurses and other allied health personnel at predetermined times during the hospital stay to assess the appropriateness of care via Hospital stay and Insurance reviews.

The Utilization Management Reports Menu:

AR UR Activity Report

SR MCCR/UR Summary Report

### UR Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Utilization Review (UR) Activity Report provides summary and detailed reports on important aspects of the Utilization Management process. It allows the user to include \[H\]ospital Reviews and/or \[I\]nsurance Reviews, as well as provides activity counts and details in the areas of Admissions (to Acute Care, Nursing Home Care Unit \[NHCU\], and Domiciliary), pre-certifications, required reviews, Reasons Not Billable (RNBs), and approval days/dollars by treating specialty. The user chooses whether to include \[H\]ospital Reviews, \[I\]nsurance Reviews, or \[B\]oth, whether to print only a Summary, and specify a date range.

Select Utilization Management Reports \<TEST ACCOUNT\> Option: AR UR Activity Report

UR Activity Report

Include \[H\]ospital Reviews \[I\]nsurance Reviews \[B\]oth: B// OTH

Print Summary Only? YES// ??

Answer YES if you only want to print a summary or answer NO if you want

a detailed listing plus the summary.

Print Summary Only? YES//

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

UR ACTIVITY SUMMARY REPORT

for Insurance Reviews

Your VAMC (444)

From: JAN 01, 2023

To: JAN 31, 2023

Date Printed: May 08, 2023@15:41:17

Page: 1

--------------------------

Total Admissions: 100

Total Admissions to NHCU: 9

Total Admissions to Domiciliary: 0

Total Admissions Requiring Reviews: 12

Number of Scheduled Adm. Reviewed: 0

Total Admissions with Insurance: 28

Total Billable Admissions: 13

Type \<Enter\> to continue or '^' to exit:

Cases with Pre-Cert and Follow-up: 4

Cases with Pre-Cert no Follow-up: 0

Number of Closed Cases: 15

Number of Billable Closed Cases: 12

Number of Unbillable Closed Cases: 3

Number of New Cases Still Open: 0

Number of Previous Cases: 0

Number of Previous Cases Closed and Billable: 0

Number of Previous Cases Closed, not Billable: 0

Number of Previous Cases still Open: 0

Number of Outpatient Cases Reviewed: 0

Reason Not Billable Report: Reason Count

--------------------------- ------------------------------

SC TREATMENT 3

OTHER COMPLIANCE 2

MRA REC'D. NO SEC RESP 3

FILING TIMEFRAME NOT M 3

OBSERVATION-OP BILLED 2

NO OUTPATIENT COVERAGE 1

ALL BILLABLE CPT CODES 1

Type \<Enter\> to continue or '^' to exit:

INSURANCE REVIEW SPECIALTY SUMMARY REPORT May 08, 2023@15:41:17 Page 2

For Insurance Reviews Dated 01/01/23 to 01/31/23

Days Days Amount Amount

Specialty Approved Denied Approved Denied

--------------------------------------------------------------------------------

GENERAL SURGERY 18 0 \$81,594 \$0

MEDICINE 3 0 \$7,152 \$0

--------------------------------------------------------------------------------

21 0 \$88,746 \$0

Type \<Enter\> to continue or '^' to exit:

UR ACTIVITY SUMMARY REPORT

for Hospital Reviews

Your VAMC (444)

From: JAN 01, 2023

To: JAN 31, 2023

Date Printed: May 08, 2023@15:41:17

Page: 3

--------------------------

Total Admissions: 100

Total Admissions to NHCU: 9

Total Admissions to Domiciliary: 0

Total Cases Reviewed: 0

Number of New Case Still Open: 0

Number of Previous Cases: 0

Number of Previous Cases still Open: 0

Type \<Enter\> to continue or '^' to exit:

Total Random Sample Cases: 0

Total Special Condition Cases: 0

COPD: 0

CVD: 0

TURP: 0

Total Locally Added Cases: 0

Total Cases Meeting Criteria on Adm.: 0

Total Cases Not Meeting Crit. on Adm.: 0

Total Days Reviewed: 0

Total Days Meeting Criteria: 0

Total Days Not Meeting Criteria: 0

Type \<Enter\> to continue or '^' to exit:

### MCCR/UR Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may run this report for either admissions or discharges, and enters a date range for the report. It will summarize totals by admission or discharge, cases with insurance, billable inpatient cases, cases requiring reviews, days approved, amount collectible approved for billing, number of days denied, amount denied, and penalty dollars. It also includes a section on Reasons Not Billable (RNBs) and Days Approved by Specialty.

Select Utilization Management Reports \<TEST ACCOUNT\> Option: SR MCCR/UR Summary Report

MCCR/UR Summary Report

Print Report By \[A\]dmissions \[D\]ischarges: D// ischarges

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: 013123 (JAN 31, 2023)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

MCCR/UR SUMMARY REPORT

for

Your VAMC (444)

for Discharges

From: JAN 01, 2023

To: JAN 31, 2023

Date Printed: MAY 08, 2023

Page: 1

--------------------------

Total Discharges: 128

Total Discharges with Insurance: 29 (22.66%)

Total Billable Discharges: 16 (12.50%)

Total Discharges Requiring Reviews: 16 (12.50%)

Total Discharges Reviewed: 6 (4.69%)

Total Discharges Reviewed-Multi Carrier: 1 (0.78%)

Type \<Enter\> to continue or '^' to exit:

Total Reviews Done: 7

Number of Days Approved: 32

Amount Collectible Approved for Billing: \$78,437

Number of Days Denied: 0

Amount Denied for Billing: \$0

Total Cases Appealed: 0

Number of Initial Appeals: 0

Number of Subsequent Appeals: 0

Penalty Report: Number of cases Dollars

--------------- ------------------------------------

No Pre Admission Certification: 0 \$0

Untimely Pre Admission Certification: 0 \$0

VA a Non-Provider: 0 \$0

Type \<Enter\> to continue or '^' to exit:

Reason Not Billable Report: Reason Count

--------------------------- ------------------------------------

SC TREATMENT 1 (7.69%)

MRA REC'D. NO SEC RE 3 (23.08%)

FILING TIMEFRAME NOT 1 (7.69%)

NO INPATIENT COVERAG 3 (23.08%)

ALL BILLABLE CPT COD 5 (38.46%)

-------

Total: 13

Days Approved by Specialty: Specialty No. Days Dollars

--------------------------- ------------------------------------

MEDICINE 11 \$26,224

GENERAL SURGERY 1 \$4,533

ICU-M 20 \$47,680

Type \<Enter\> to continue or '^' to exit:

# APPENDIX A – Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym or Term | Definition / Explanation                                                  |
|-----------------|---------------------------------------------------------------------------|
| AR              | Accounts Receivable                                                       |
| C&P             | Compensation and Pension                                                  |
| CHAMPVA         | Civilian Health and Medical Program of the Department of Veterans Affairs |
| CPAC            | Consolidated Patient Account Center                                       |
| DUZ             | Designated User                                                           |
| ERA             | Electronic Remittance Advice                                              |
| FMS             | Financial Management System                                               |
| FRM             | Facility Revenue Managers                                                 |
| HCFA            | Health Care Financing Administration                                      |
| HINQ            | Hospital Inquiry                                                          |
| IB              | Integrated Billing                                                        |
| MCCR            | Medical Care Cost Recovery                                                |
| NHCU            | Nursing Home Care Unit                                                    |
| NSC             | Non-Service-Connected                                                     |
| OPT             | Out Patient Treatment                                                     |
| PTF             | Patient Treatment File                                                    |
| RNB             | Reasons Not Billable                                                      |
| SC              | Service-Connected                                                         |
| SSN             | Social Security Number                                                    |
| TIN             | Tax Identification Number                                                 |
| UR              | Utilization Review                                                        |
| VERA            | Veterans Equitable Resource Allocation                                    |
| VHA             | Veterans Health Administration                                            |
| VISN            | Veterans Integrated Service Network                                       |