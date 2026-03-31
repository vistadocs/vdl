---
title: Accounts Receivable Version 4.5 Debt Management Center (DMC) Referral Process User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Debt Management Center (DMC) Referral Process
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 4
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - date
  - report
  - class
  - debt
  - blockquote
  - table
  - span
  - veteran
  - debtor
  - amount
page_count: 0
word_count: 29240
section_count: 33
table_count: 4
figure_count: 5
appendix_count: 7
has_toc: False
is_stub: False
pub_date: June 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_dmc_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_dmc_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

---
title: |
  <span id="_Hlk12435644" class="anchor"></span>Accounts Receivable 4.5

  Debt Management Center

  User Guide
---

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/001.png)

June 2025

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc198214951" class="anchor"></span>Table 1: AR Debtor File (#304)</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 55%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/2025</td>
<td>1.9</td>
<td><p>Patch PRCA*4.5*416:</p>
<ul>
<li><p>Added the ‘Veteran Third Party Charge Report’ to the DMC Referral Menu</p></li>
</ul></td>
<td>HDM IBAR Development Team</td>
</tr>
<tr class="even">
<td>01/2025</td>
<td>1.8</td>
<td><p>Patch PCRA*4.5*412,</p>
<p>Multiple Referral Program Report</p>
<ol type="1">
<li><p>Creates new report</p></li>
<li><p>Adds the report to DMC Referral Menu</p></li>
<li><p>Adds the report to the Cross-Servicing Menu</p></li>
<li><p>Adds the report to the TOP Menu</p></li>
</ol></td>
<td>IBAR Team</td>
</tr>
<tr class="odd">
<td>05/2022</td>
<td>1.7</td>
<td>Updated all references to Repayment Plans (patch PRCA*4.5*378).</td>
<td>Grant Thornton LLP</td>
</tr>
<tr class="even">
<td>05/2022</td>
<td>1.6</td>
<td>Added the Pension Exemption Reconciliation Report (PERR) as part of PRCA*4.5*384. Also updated the screen captures of the DMC Referral Menu in the document.</td>
<td>Grant Thornton LLP</td>
</tr>
<tr class="odd">
<td>08/2021</td>
<td>1.5</td>
<td><p>PRCA*4.5*379:</p>
<p>Added reference to a new report in the PRCA namespace. The CPAC First Party Reconciliation Report.</p>
<p>Changes to First Party Veteran Charge Report:</p>
<p>Added the following prompts to page 32:</p>
<p>Do you want to see:</p>
<ol type="1">
<li><p>Letter Dates</p></li>
<li><p>Total Payments Received on Bill Number</p></li>
<li><p>Neither</p></li>
</ol>
<p>Enter Selection (1,2, or 3): 3// Neither</p>
<p>Added screen captures for</p>
<ol type="1">
<li><blockquote>
<p>Report Example without ‘Letter Dates’</p>
</blockquote></li>
<li><blockquote>
<p>Report with ‘Letter Dates’</p>
</blockquote></li>
<li><blockquote>
<p>Report with ‘Total Payments Received on Bill Number</p>
</blockquote></li>
</ol>
<p>Added note for “alternative reflections pathway” to setup 256-character display.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>03/2021</td>
<td>1.4</td>
<td><p>Changes to First Party Veteran Charge Report:</p>
<ul>
<li><p>Added IB statuses of BILLED, ON HOLD, and CANCELLED.</p></li>
<li><p>Rate type charges where the patient is responsible for payment, i.e. HUMANITARIAN, INELIGIBLE, DENTAL, and MEANS TEST.</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>09/2020</td>
<td>1.3</td>
<td>Added updates to input and print functionality for First Party Charge IB Cancellation Reconciliation Report PRCA*4.5*361.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/2019</td>
<td>1.2</td>
<td>Added Catastrophically Disabled Exempt Copay Charge Report as part of patch PRCA*4.5*350.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/2019</td>
<td>1.1</td>
<td><p>Converted from PDF and updated document to current template format as Word document was not available.</p>
<p>Four additional reports added to Patch PRCA*4.5*347:</p>
<ul>
<li><blockquote>
<p>0 to 40 Percent SC Change Reconciliation Report</p>
</blockquote></li>
<li><blockquote>
<p>First Party Charge IB Cancellation Recon Report</p>
</blockquote></li>
<li><blockquote>
<p>10-40% SC Med Care Copay Exempt Chrg Recon Report</p>
</blockquote></li>
<li><blockquote>
<p>50-100% SC Exempt Charge Reconciliation Report</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>05/2015</td>
<td>1.0</td>
<td>Initial version from VDL.</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc198214951" class="anchor"></span>Table 1: AR Debtor File (#304)

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Program Coordination](#program-coordination)
- [What Debts are Referred to the DMC?](#what-debts-are-referred-to-the-dmc)
- [DMC Referral Menu](#dmc-referral-menu)
  - [Day DMC Report](#day-dmc-report)
  - [DMC Referred Report Print](#dmc-referred-report-print)
  - [Enter Lesser DMC Withholding Amount](#enter-lesser-dmc-withholding-amount)
  - [Remove Debtor from DMC](#remove-debtor-from-dmc)
  - [Reviewing Debts for Validity](#reviewing-debts-for-validity)
    - [DMC Debt Validity Report](#dmc-debt-validity-report)
    - [Entering and Editing the DMC Debt Valid Field](#entering-and-editing-the-dmc-debt-valid-field)
    - [The DMC Debt Validity Management Report](#the-dmc-debt-validity-management-report)
  - [Rated Disability Eligibility Change Report](#rated-disability-eligibility-change-report)
  - [Entering/Editing the NUMBER OF DAYS FOR DMC REPORTS Site Parameter](#enteringediting-the-number-of-days-for-dmc-reports-site-parameter)
  - [Entering/Editing the \# OF DAYS FOR RD ELIG CHG RPT Site Parameter](#enteringediting-the-of-days-for-rd-elig-chg-rpt-site-parameter)
  - [to 40 Percent SC Change Reconciliation Report](#to-40-percent-sc-change-reconciliation-report)
  - [First Party Charge IB Cancellation Recon Report](#first-party-charge-ib-cancellation-recon-report)
  - [10-40% SC Med Care Copay Exempt Charge Recon Report](#10-40-sc-med-care-copay-exempt-charge-recon-report)
  - [50-100% SC Exempt Charge Reconciliation Report](#50-100-sc-exempt-charge-reconciliation-report)
  - [Catastrophically Disabled Exempt Copay Charge Report](#catastrophically-disabled-exempt-copay-charge-report)
  - [First Party Veteran Charge Report](#first-party-veteran-charge-report)
  - [Pension Exemption Reconciliation Report (PERR)](#pension-exemption-reconciliation-report-perr)
  - [Multiple Referral Programs Report](#multiple-referral-programs-report)
  - [Veteran Third Party Charge Report](#veteran-third-party-charge-report)
- [What does the DMC do with Monthly Master File?](#what-does-the-dmc-do-with-monthly-master-file)
- [What Happens if the Veteran Makes Payment-in-Full?](#what-happens-if-the-veteran-makes-payment-in-full)
- [What Happens when the Veteran Requests a Lesser Withholding Amount?](#what-happens-when-the-veteran-requests-a-lesser-withholding-amount)
- [How to Enter Lesser Withholding Amount in VistA](#how-to-enter-lesser-withholding-amount-in-vista)
- [What Happens when the Veteran Requests a Repayment Plan be Established?](#what-happens-when-the-veteran-requests-a-repayment-plan-be-established)
  - [How to Set up and Monitor a Repayment Plan in VistA](#how-to-set-up-and-monitor-a-repayment-plan-in-vista)
    - [Enter a New Repayment Plan](#enter-a-new-repayment-plan)
    - [Repayment Plan Inquiry](#repayment-plan-inquiry)
  - [The Debt is Not Resolved. What Happens Next?](#the-debt-is-not-resolved-what-happens-next)
- [How does the VistA Software Determine which Records get sent to the DMC in the Weekly Update Message?](#how-does-the-vista-software-determine-which-records-get-sent-to-the-dmc-in-the-weekly-update-message)
- [What does the DMC do with Weekly Update File?](#what-does-the-dmc-do-with-weekly-update-file)
- [What Happens when the Monthly Offset Occurs?](#what-happens-when-the-monthly-offset-occurs)
- [How to Process a DMC Payment in VistA](#how-to-process-a-dmc-payment-in-vista)
- [How to Remove a Debtor from DMC Referral](#how-to-remove-a-debtor-from-dmc-referral)
- [Other DMC Correspondence](#other-dmc-correspondence)
  - [1017G Forms](#1017g-forms)
  - [Death Notifications](#death-notifications)
  - [Waivers Granted on VBA Benefit Accounts Managed by the DMC](#waivers-granted-on-vba-benefit-accounts-managed-by-the-dmc)
  - [Miscellaneous Mail](#miscellaneous-mail)
- [DMC Timelines](#dmc-timelines)
- [CAROLS – Centralized Accounts Receivable On‑Line System](#carols-centralized-accounts-receivable-online-system)
  - [Instructions for Using the CAROLS](#instructions-for-using-the-carols)
    - [CAROLS Screen C11](#carols-screen-c11)
    - [CAROLS Screen C12](#carols-screen-c12)
- [Debtor Address](#debtor-address)
- [Additional VistA Information](#additional-vista-information)
- [Troubleshooting Tips](#troubleshooting-tips)
  - [E-Mail Groups](#e-mail-groups)
  - [Timing Issues](#timing-issues)
  - [Posting TDA Payments](#posting-tda-payments)
  - [Receipts](#receipts)
  - [Letters](#letters)
- [Appendix A. Sample Letter](#appendix-a-sample-letter)
- [Appendix B. CAROLS/MCCF Diary Codes](#appendix-b-carolsmccf-diary-codes)
- [Appendix C. C&P (Hines) Reason Codes](#appendix-c-cp-hines-reason-codes)
- [Appendix D. Examples of VistA Messages](#appendix-d-examples-of-vista-messages)
- [Appendix E. Master File Data Elements for Messages to DMC](#appendix-e-master-file-data-elements-for-messages-to-dmc)
- [Appendix F. Glossary](#appendix-f-glossary)
- [Appendix G. Contacts](#appendix-g-contacts)
In a 1995 report, the Office of the Inspector General identified a significant amount of potential collections if VHA utilized the Debt Management Center’s (DMC) offset processes. The Debt Collection Improvement Act (DCIA) of 1996, which established the Treasury Offset Program (TOP), also prompted VHA to pursue this method of collection. One of the requirements of TOP is that the participating agency must pursue all internal offsets prior to the Treasury referral.
To comply with these requirements, first party debts meeting specific criteria are forwarded to the Office of Finance’s Debt Management Center. Accounts eligible for referral are those that have a balance of \$25 or more (accounts can consist of single or multiple charges), 30 days have passed since the third patient statement was mailed and bills are in an active status (not in a repayment plan, suspended pending an administrative decision, or referred to Regional Counsel). These debts are then matched against the C&P Mini-Master file to identify those Veterans in receipt of VA benefits. Only accounts of those Veterans with an active award and a net check amount of greater than \$25 are loaded into the DMC’s computer system and set up for offset.
All other accounts are returned to the medical center for other collection actions and eventual referral to the Treasury Offset Program (TOP) and/or the Treasury Cross-Servicing Program (TCSP). The file of returned accounts is used by the Austin Information Technology Center (AITC) to generate letters to the Veterans informing them of impending referral to TOP/TCSP.
Offsets for VHA debts are conducted in the same manner as VBA debts. After the accounts are loaded into the DMC system a letter is generated notifying the Veteran of the impending offset. The date of the offset and the amount of the debt are indicated on the letter. The letter specifies the Veteran has 30 days to contact the servicing Consolidated Patients Accounts Center (CPAC) via the call centers to dispute the charges, enter into a repayment plan, modify the monthly amount to be offset, or pay the debt in full. DMC does not actually determine the amount to be offset monthly until approximately 15 days prior to the offset date shown on the letter. Unless informed otherwise by the CPAC via an update from VistA or contact with a DMC employee, the offset amount will be the greater of the total debt amount or the total amount of benefits available. The actual offset will occur approximately 90 days after the date of the notification letter. This process was modeled after the existing VBA process so that confusion would be kept to a minimum.
The Accounts Receivable (AR) patch that introduced the functionality needed to identify and transmit outstanding first party medical debts to the Debt Management Center for offset was released to VA Medical Centers on December 12, 1997.
The AR software automatically compiles and sends a master file to DMC via the AITC on the last Thursday of the month. This master file contains only those accounts that meet specific DMC referral criteria. Even though an account may be transmitted to the DMC, the referred account may not be accepted because the Veteran has inactive benefits or for some other reason. A VistA mail message is sent to the CPAC and the DMC referral flag is removed from these accounts. The VistA AR system will automatically process these delinquent debts to the TOP/TCSP when available.
Every Tuesday, AR sends an update file to the DMC. The only records sent in the Tuesday updates are those who are listed as having a DMC account established and where there has been a change to the balance of the account due to a payment being processed, a change to the interest or administrative costs, a lesser withholding amount entered, or suspense action indicated.
Mail messages confirming receipt of transmission are generated by the AITC. Mail messages informing CPACs the referred account was not accepted by the DMC or the Beneficiary Identification and Records Locator System (BIRLS) shows a date of death are transmitted from the AITC to two mail groups on the VistA system – G.DMX and G.DMR. It is critical that active users of AR are members of these mail groups. While some messages sent to these mail groups are information only, other messages require AR staff to take action and are very useful in researching problem areas.
The DMC establishes the offset amount in the Compensation and Pension (C&P) system 60 days after the Veteran is notified of the pending action. The DMC collects the amount established for offset approximately 90 days after the initial notification. CPACs receive payments in the form of a Transfer of Disbursing Authority (TDA) to the facility’s suspense account.
Payments are posted using Receipt Processing option located on the Agent Cashier menu. The TDA payment type is used to apply the payment to the Veteran’s AR debt.
The DMC offset stops when the debt balance is reduced to zero. Should any additional portion of the Veteran’s account become 90 days delinquent and subsequently referred to DMC while a previously referred debt is actively being offset from C&P benefits, offset from C&P benefits will continue uninterrupted to collect the newly referred amount. If a debt is referred to DMC and the C&P benefits are not currently being offset to satisfy a previously referred debt, DMC will start the cycle over.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This training guide was created to help individuals understand the Debt Management Center Referral process. It will address the activities associated with managing referred accounts. This guide will provide step-by-step instructions on how to use Accounts Receivable options and Centralized Accounts Receivables System (CARS) to monitor and process Debt Management Center (DMC) information.

Please read the Introduction section to learn more about the components and activities related to the DMC Referral process.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users of the Debt Management Center Referral process functionality are the AR Supervisors and the Veteran Services Department technicians who handle First Party AR functions for the Consolidated Patient Account Centers (CPACs).

## Program Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cross-Servicing is a joint effort between VistA AR, AITC, Debt Management Center (DMC), and Treasury. For more information on each organization, please reference the following links:

- Veterans Health Administration (VHA) Chief Business Office (CBO): REDACTED
- Austin Information Technology Center (AITC): REDACTED
- Department of Veterans Affairs (VA) [Debt Management Center (DMC)](http://www.va.gov/debtman/)
- [U.S. Department of the Treasury, Bureau of the Fiscal Service](https://www.fiscal.treasury.gov/top/)

# What Debts are Referred to the DMC?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A debt is considered delinquent and eligible for referral to the Debt Management Center when it meets all of the criteria listed here.

1.  Debtor is a patient.
2.  The Site Deletion Flag field in the AR Debtor file (#340) is blank or set to NO for this debtor.
3.  Total Amount of debt (Principal +Interest +Administrative Cost) must be \$25.00 or more.
4.  It must be at least 90 days since first notification of outstanding debt was sent to debtor.
5.  Status of bill(s) is active.
6.  Categories of Bills that can be referred:
- Ineligible Hospital
- Emergency/Humanitarian
- Adult Day Health Care
- C (Means Test)
- Domiciliary
- Geriatric Eval-Institutional
- Geriatric Eval-Non-Institutional
- Nursing Home Care-LTC
- Respite Care-Institutional
- Respite Care-Non-Institutional
- RX Co-Pay (SC)
- RX Co-Pay (NSC)
- TRICARE Patient
- CC Inpt
- CC MTF Inpt
- CC MTF Opt
- CC MTF RX Co-Payment
- CC MTF Third Party
- CC Nursing Home Care - LTC
- CC Opt
- CC Respite Care
- CC RX Co-Payment
- CC Third Party
- CC Urgent Care
- CCN Inpt
- CCN Nursing Home Care - LTC
- CCN Opt
- CCN Respite Care
- CCN RX Co-Payment
- CCN Third Party
- CHOICE Inpt
- CHOICE Nursing Home Care - LTC
- CHOICE Opt
- CHOICE Respite Care
- CHOICE RX Co-Payment
- CHOICE Third Party
7.  Bill cannot be on repayment plan.
8.  Bill has not been referred to Regional Counsel.
1.  A debt may meet the referral criteria listed above but data will NOT be transmitted to DMC if the debtor’s address information is <u>unknown</u> or <u>incorrect</u>. See [Section 17 – Debtor Address](#debtor-address) for more information on how to enter or edit address information.
2.  Debts that are associated with Veterans who are Service Connected (SC) 50% to 100% or are in receipt of a VA pension will not be referred to the DMC until they are reviewed for validity. Please see [Section 3.5 - Reviewing Debts for Validity](#_Reviewing_Debts_for) for further information on changes related to Patch PRCA\*4.5\*253.

On the last Thursday of each month, as part of the Accounts Receivable nightly job at 2 a.m., the software looks at every active debt in the Accounts Receivable file (#430) to see if it meets the referral criteria listed above. If it does, the system builds a Master File mail message and transmits the information to a queue at the AITC; the G.DMR mail group on VistA also receives a copy of this message. The subject of the message is MASTER FILE RECORDS SENT TO DMC ON MM/DD/YYYY. The AITC compiles all of the Master File messages received and prepares a data file for the DMC. To ensure Master File messages are received by the AITC prior to DMC processing accounts, the master file is not installed at the DMC until the following Monday.

# DMC Referral Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section references the reviews and reports that are completed or available for review by CPAC and Facility Revenue personnel to determine the validity of a first party Veteran debt for transfer to DMC for potential offset. The main menu, shown below, is only listed once for reference.

<span id="_Toc198214873" class="anchor"></span>Figure 1: DMC Referral Main Menu

You were last executing the 'DMC Referral Menu' menu option.

Do you wish to resume? Yes// (Yes)

 

 

1 90 Day DMC Report

2 DMC Referred Report Print

3 Enter Lesser DMC Withholding Amount

4 Remove Debtor From DMC

5 DMC Debt Validity Report

6 DMC Debt Validity Management Report

7 Rated Disability Eligibility Change Report

8 Enter/Edit DMC Debt Validation

9 Enter/Edit RD Number of Days Report Parameter

10 Enter/Edit DMC Report \# Days for Episodes of Care

11 0-40 Percent SC Change Reconciliation Report

12 First Party Charge IB Cancellation Recon Report

13 10-40% SC Med Care Copay Exempt Chrg Recon Report

14 50-100% SC Exempt Charge Reconciliation Report

15 Catastrophically Disabled Exempt Copay Charge Rpt

16 First Party Veteran Charge Report

17 Pension Exemption Reconciliation Report (PERR)

18 Multiple Referral Programs Report

19 Veteran Third Party Charge Report

 

Select DMC Referral Menu \<TEST ACCOUNT\> Option:

## Day DMC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report identifies Veterans who have debt that is at or greater than 90 days old and is eligible for referral to DMC. The report can be generated in summary or detail formats.

<span id="_Toc198214874" class="anchor"></span>Figure 2: Summary Report - 90 Day DMC

<span id="_Toc198214875" class="anchor"></span>Figure 3: Detailed Report - 90 Day DMC

## DMC Referred Report Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report identifies Veterans by each facility who have been referred to DMC and provides an overview of each bill referred, when the bill was referred and the debt information for each bill. There is a preferred period in which to pull the report to obtain the best information and a report can be generated by All Patients or a Single Patient.

<span id="_Toc198214876" class="anchor"></span>Figure 4: All Patient - DMC referred Report

## Enter Lesser DMC Withholding Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans can request a reduced rate of withholding, DMC Lesser Amount. A DMC Lesser withholding amount can only be entered when the Veteran has a current DMC debt being collected. One indicator for current DMC debt is an account banner on the ^Brief screen showing an amount due to DMC.

> **NOTE:** A Veteran can only have one DMC lesser on file, if a Veteran has multiple CPAC/VISN accounts, the Veteran Services department should suggest Debt Forgiveness or an RPP for other VISN accounts. A review of CPRS will allow the PSA to see DMC Lessors for other VISNs. Please consult a lead or supervisor for guidance.

When Veterans call the HRC to request a DMC Lesser Amount, HRC staff will create a request in CRM Dynamics. When Veterans call or write their facility or the associated CPAC to request a reduced rate of withholding, Veteran Services PSAs will review the request in CRM Dynamics.

Figure 5: DMC Lesser Withholding

<span id="_Toc198214877" class="anchor"></span>

## Remove Debtor from DMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will remove a Veteran bill or account from offset collection by the DMC. An account can be removed for various reasons such as an updated SC determination or the Veteran is deceased, etc.

Figure 6: Remove Debtor From DMC

<span id="_Toc198214878" class="anchor"></span>

## Reviewing Debts for Validity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Debts that are associated with Veterans who are Service Connected (SC) 50% to 100% or are in receipt of a VA pension will not be automatically referred to the DMC until they are reviewed for validity.

3.  CPACs will need to validate all debts for a patient. If it is decided that debts are not valid and need to be cancelled and/or refunded, once the transactions have been completed, it will be necessary to contact the DMC staff so that manual adjustments can be made to the patient’s account at DMC.

### DMC Debt Validity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DMC Debt Validity Report is provided to assist users in reviewing the legitimacy of first party bills for Veterans who are SC 50% to 100% or in receipt of VA Pension benefits. This report prints information on Veterans with Active, Open, or Suspended bills for episodes of care within a user selected time frame, minimum of 365 days (1 year) and where the DMC Debt Valid field has not been set to YES or NO.

Authorized billing staff should run this report to ensure that all bills meeting these criteria are reviewed and, if necessary, the appropriate action is taken.

- Bill is appropriate: if the bill is appropriate and all other DMC referral criteria is met, update the Debt Validity Status field to YES so that the bill is referred to DMC via the automated process.
- Bill is inappropriate: update the Debt Validity Status Field to NO (using the Enter/Edit DMC Debt Validation option) and take action to cancel the bill.
- Bill was inappropriately sent to DMC: action must be taken to cancel DMC collection and/or refund payments, as appropriate.

This report can also be setup by IRM staff as a “scheduled task” to run on a recurring basis without user intervention. When setting this report up to run as a scheduled task, use the Enter/Edit DMC Report \# Days for Episodes of Care option to select how many days in the past bills for episodes of care will be included. (A minimum of 365 days (1 year) and a maximum of 3650 days (10 years) may be selected).

This option also allows you to print the report in a detailed format or in an Excel delimited format.

It is recommended that you queue this report to a device that is 150 characters wide.

4.  When the Veteran is not Service Connected 50% to 100% and is not receiving a VA pension, the software will include the functionality to consider a Veteran as “Receiving a VA Pension” if he/she is receiving A&A (Aid & Attendance) or Housebound Benefits.

The following example shows the first and last pages of a sample report in order to show you the type of information provided, and the totals included at the end of the report, without including 365+ days of data.

<span id="_Toc198214879" class="anchor"></span>Figure 7: DMC Debt Validity Report

Select DMC Referral Menu Option: 5 DMC Debt Validity Report

\*\*\* Print the Debt Validity Report \*\*\*

Report To Include Bills For Episodes of Care Beginning With User Selected Date.

Entered Date Must be Jun 24, 2007 or older!

Enter Beginning Date: Jun 24, 2007//3/28/07 (MAR 28, 2007)

Do you want to capture report data for an Excel document? NO// \<RET\>

This report may take a while to process. It is recommended that

you Queue this report to a device that is 150 characters wide.

DEVICE: HOME// HOME;132 TELNET TERMINAL

<span id="_Toc198214880" class="anchor"></span>Figure 8: DMC Debt Validity Report Example

DMC Debt Validity Report Run Date: 27 Mar 2008 9:11 am Episode of Care Data from 28 Mar 2007 Page: 1

Claim Claim Eligibility/ Bill RX Fill/ Outpat Dischar DMC Debt DMC Ref

Veteran Name SSN Number Loc. SC Eff. Date Number ReFill Dt Visit Dt Date Valid Status Date =================================================================================================================================

ARPATIENT,ONE 0001 \#####5051 ZZZ SC90% XXX-K700EK1 14Nov07 ACTIVE

01Jun05

ARPATIENT,TWO 0002 \#####2319 XXX SC100% XXX-K600T48 05Jan07 PENDING ACTIVE 22Feb08

01Dec06

XXX-K60144C 07Feb07 PENDING ACTIVE 22Feb08

XXX-K6018ZM 23Feb07 PENDING ACTIVE 22Feb08

XXX-K7006HZ 06Nov07 ACTIVE

XXX-K700HRK 05Dec07 ACTIVE

XXX-K700PUN 03Jan08 ACTIVE

XXX-K700UQ8 03Jan08 ACTIVE

ARPATIENT,THREE 0003 \#####5873 XXX SC50% XXX-K700EP0 15Nov07 ACTIVE

01Aug06

ARPATIENT,FOUR 0004 \####3602 XXX SC100% XXX-K7010JX 18Jul07 ACTIVE

01Jul06

ARPATIENT,FIVE 0005 \####3995 XXX SC100% XXX-K6024ZP 27Jun07 ACTIVE

01Aug06

XXX-K6025YU 26Jun07 ACTIVE

Press RETURN to continue, ‘^’ to exit:

DMC Debt Validity Report Run Date: 27 Mar 2008 9:11 am Episode of Care Data from 28 Mar 2007 Page: 6

=================================================================================================================================

SUMMARY - BILLS REFERRED TO DMC

-------------------------------------------------------------

Total Number of Bills Referred: 13

Total Number of unique veterans referred: 7

Total Account Receivable Dollars referred: \$ 205.39

SUMMARY - TOTAL BILLS

--------------------------------------------------

Total Number of Bills: 59

Total Number of unique veterans: 30

Total Account Receivable Dollars: \$ 2,508.94

### Entering and Editing the DMC Debt Valid Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have reviewed the DMC Debt Validity Report and determined whether or not a debt is valid, the Enter/Edit DMC Debt Validation option allows you to enter and edit the DMC DEBT VALID? field in the ACCOUNTS RECEIVABLE file, \#430 with a value of YES or NO. (A PENDING status is assigned automatically, when appropriate, by the nightly DMC job.)

If this field is set to YES and the debt meets all other criteria to be sent to DMC, it will be referred to DMC even if the debtor is SC 50% to 100% or in Receipt of a VA Pension.

If this field is set to NO, the debt will not be referred to DMC, and the user is instructed to cancel the bill and/or refund payment, if appropriate.

If the field is empty (NULL), the nightly DMC job will prevent the debt from being referred to DMC when the debtor is SC 50% to 100% or in Receipt of a VA Pension. It will then set the status to PENDING.

You are first prompted to select a specific bill, by bill number or patient. Only bills with a status of Active, Open, or Suspended may be selected. It is not necessary for a bill to be 90 days old to be edited using this option. You may also edit bills that are already referred to the DMC.

After patient information is displayed, you will see the following prompt, Please confirm this is a valid debt based on eligibility: //. Enter YES or NO, as appropriate.

Following is an example of the field being set to NO. You can see the resulting message, Please cancel this bill and/or refund payment if appropriate.

<span id="_Toc198214881" class="anchor"></span>Figure 9: Enter/Edit DMC Debt Validation

Select DMC Referral Menu Option: 8 Enter/Edit DMC Debt Validation

Select ACCOUNTS RECEIVABLE BILL NO. or PATIENT: K700EZZ

Searching for a PATIENT, (pointed-to by DEBTOR)

Searching for a OTHER (PERSON), (pointed-to by DEBTOR)

Searching for a VENDOR, (pointed-to by DEBTOR)

Searching for a 3RD PARTY, (pointed-to by DEBTOR)

Searching for a INSTITUTION, (pointed-to by DEBTOR)

XXX-K700EZZ RX CO-PAYMENT/SC VET 11-24-06 ARPATIENT,ONE ACTIVE

\$100.62

Veteran’s Name: ARPATIENT,ONE

Veteran’s SSN: XXX-XX-0001

Category Type: RX CO-PAYMENT/SC VET

Bill Status: ACTIVE

RX/Refill Date: Jul 20, 2007

Please confirm this is a valid debt based on eligibility: // n NO

Please cancel this bill and/or refund payment if appropriate.

### The DMC Debt Validity Management Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DMC Debt Validity Management Report option is used to assist management in reviewing the processing of the bills listed on the Debt Validity Report for Veterans who are SC 50% to 100% or in receipt of VA Pension benefits and have bills for episodes of care within the previous 365 days with a current bill Status of Open, Active, Suspended, Cancellation, Refund Review or Refunded. The report can be selected based on the DMC Debt Valid status to help supervisors to identify bills that are processed or yet to be processed.

The report allows you to choose whether to print the report in a detailed format, a summary format, or in an Excel Delimited format.

Once you select your format, you will see the following prompt, Select DMC Debt Valid field value. You may enter one of the following choices:

Enter A for ALL FIELD VALUES, to include bills with all DMC Debt Valid values.

Enter B for BLANK/NULL, to include only bills not yet reviewed by the user.

5.  If current bill Status is Cancellation or Refunded, then the bill was resolved prior to this new software and the bill does not require review.

Enter P for PENDING, to include only bills excluded by the AR Nightly Background Process.

Enter Y for YES, to include only bills determined to be a valid debt that should be referred to the DMC.

Enter N for NO, to include only bills that should not be referred to the DMC.

If you choose to print the report for all DMC Debt Valid values (BLANK/NULL, PENDING, YES, and NO), the report will include a summary for each value, as well as a summary total for all values combined.

This report can also be setup by IRM staff as a “scheduled task” to run on a recurring basis without user intervention. When setting this report up to run as a scheduled task, use the Enter/Edit DMC Report \# Days for Episodes of Care option to select how many days in the past bills for episodes of care will be included. (A minimum of 365 days (1 year) and a maximum of 3650 days (10 years) may be selected).

It is recommended that you queue this report to a device that prints 150 characters wide.

6.  When the Veteran is not Service Connected 50% to 100% and is not Receiving a VA Pension, the software will also include the functionality to consider a Veteran as Receiving a VA Pension if he/she is receiving A&A or Housebound Benefits.

<span id="_Toc198214882" class="anchor"></span>Figure 10: Debt Validity Management Report

Select DMC Referral Menu Option: 6 DMC Debt Validity Management Report

\*\*\* Print the DMC Debt Validity Management Report \*\*\*

This report may take a while to process. It is recommended that

you Queue this report to a device that is 150 characters wide.

Report To Include Bills For Episodes of Care Beginning With User Selected Date.

Entered Date Must be Jun 21, 2007 or older!

Enter Beginning Date: Jun 21, 2007// 1/1/07 (JAN 01, 2007)

Select one of the following:

D DETAILED

S SUMMARY

E EXCEL DELIMITED

Select Type of Report: D DETAILED

Select one of the following:

A ALL FIELD VALUES

B BLANK/NULL

P PENDING

Y YES

N NO

Select DMC Debt Valid field value: Y YES

It is recommended that you Queue this report to a

device that is 150 characters wide.

DEVICE: HOME// home;132 TELNET TERMINAL

<span id="_Toc198214883" class="anchor"></span>Figure 11: Debt Validity Management Detailed Report Example

DMC Debt Validity Management DETAILED Report Run Date: 07 Apr 2008 Episode of Care Data from 01 Jan 2007 Page: 1

DMC Debt Valid Field Values = YES

Claim Claim Bill Receivable DMC Debt Valid DMC Debt Valid

Veteran Name SSN Number Loc. Number Amount Status Edit By Edit Date =================================================================================================================================

ARPATIENT,ONEA 0001 \####7972 XXX XXX-K700V18 \$ 15 ACTIVE AREMPLOYEE,ONE 28 Mar 2008

RPATIENT,TWO 0002 \####74735 XXX XXX-K700NMH \$ 8 ACTIVE AREMPLOYEE,ONE 28 Mar 2008

SUMMARY TOTAL - YES

---------------------------------------------------------

Total Number of Bills: 2

Total Number of unique veterans: 2

Total Account Receivable Dollars: \$ 23

Total Number of unique ACTIVE Bill Status: 2

Press RETURN to continue:

## Rated Disability Eligibility Change Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rated Disability Eligibility Change Report is used to assist users in reviewing the legitimacy of first party bills, where the Veteran is neither SC 50% to 100% nor in receipt of VA Pension benefits (Veterans not included on the DMC Debt Validity Report); and where the Veteran’s rated disability has changed during the selected timeframe.

You will be prompted to enter a Beginning and Ending date related to the rated disabilities/eligibility change. User will also be prompted to enter a beginning date of for episodes of care. Veterans who meet the above criteria, and whose rated disability eligibility has changed during the selected timeframe will be included.

Authorized billing staff can run this report to ensure that all bills meeting the above criteria are reviewed and, if necessary, the appropriate action is taken as follows.

- Bill is appropriate: there shall be no action taken.
- Bill is inappropriate: AR staff shall cancel the bill using existing functionality.
- Inappropriate bill sent to DMC: AR staff shall cancel/refund using existing functionality.

This report can also be setup by IRM staff as a “scheduled task” to run on a recurring basis without user intervention. When setting this report up to run as a scheduled task, please refer to the sections below regarding site parameters for additional information.

It is recommended that you queue this report to a device that is 150 characters wide.

7.  The RDEC Report has known flaws. The 0 to 40 Percent SC Change Reconciliation Report is designed to replace the legacy RDEC report as a CPAC operational report as part of the DMC collections processing. Further, the RDEC report was not removed or updated due to unknown or potential downstream reporting related to the legacy RDEC report.

<span id="_Toc198214884" class="anchor"></span>Figure 12: Rated Disability Eligibility Change Report

Select DMC Referral Menu Option: 7 Rated Disability Eligibility Change Report

\*\*\* Print the Rated Disability Eligibility Change Report \*\*\*

Enter the Date Range for Rated Disability Changes.

Enter Beginning Date: TODAY//1/1 (JAN 01, 2008)

Enter Ending Date: TODAY//

Report To Include Bills For Episodes of Care Beginning With User Selected Date.

Entered Date Must be Jun 25, 2007 or older!

Enter Beginning Date: Jun 25, 2007// \<RET\> (JAN 01, 2007)

Do you want to capture report data for an Excel document? NO// \<RET\>

This report may take a while to process. It is recommended thatyou Queue this report to a device that is 150 characters wide.

DEVICE: HOME// home;132 TELNET TERMINAL

<span id="_Toc198214885" class="anchor"></span>Figure 13: Rated Disability Eligibiliity Change Report Example

Rated Disability Eligibility Change Report -- Run Date: 07 Apr 2008 9:48 am -- Episode of Care Data from 01 Jan 2007 Page: 1

RD Change Dates from 01 Jan 2008 to 24 Jun 2008

Claim Claim RD Chg Extre- RD Orig BILL RX Fill Outpat Dischar Veteran Name SSN Number Loc. Date RD Name mity Date Number Date Visit Dt Date Status ================================================================================================================================

ARPATIENT,ONE 0001 \#####2999 XXX 10Jan08 OSTEOMYELITIS BU 09Sep07 XXX-K701234 04Dec07 OPEN

ARPATIENT,TWO 0002 \#####1023 XXX 15Jan08 THIGH CONDITION LL 13Sep07 XXX-K701235 04Dec07 OPEN

ARPATIENT,SIX 0006 \#####4101 01Jan08 KIDNEY CONDITION BL 13Feb07 XXX-K701236 04Dec07 OPEN

01Feb08 GOUT LU 05May07 XXX-K701237 04Dec07 OPEN

ARPATIENT,TEN 0010 \#####7717 YYY 18Feb08 ABCESS OF KIDNEY BL 13Sep07 YYY-K800001 11Dec07 OPEN

27Feb08 NARCOLEPSY BL 13Sep07 YYY-K800002 11Dec07 OPEN

01Mar08 RADIATION-INDUCED PNEUMONITIS BL 11Apr07 YYY-K800003 11Dec07 OPEN

ARPATIENT,GIVE 0005 29Mar08 LOSS OF USE OF ONE HAND AND O BL 07Dec07 YYY-K701111 03Dec07 OPEN

ARPATIENT,NINE 0009 \#####2910 20Mar08 BUTTOCKS INJURY LU 01Oct07 XXX-K701111 03Dec07 ACTIVE

05Apr08 LUNG CONDITION BL 11Sep07 XXX-K701666 03Dec07 ACTIVE

06Apr08 BENIGN GROWTH OF THE BONES BL 09Feb07 XXX-K701666 03Dec07 ACTIVE

SUMMARY

================================================

Total Number of unique veterans:Total: 6

Number of Rated Disabilities: 11

Total Number of Bills: 6

Press RETURN to continue:

## Entering/Editing the NUMBER OF DAYS FOR DMC REPORTS Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When DMC reports are set up by IRM staff to run as a “scheduled task,” the software checks the NUMBER OF DAYS FOR DMC REPORTS site parameter to determine how many days in the past to check for episodes of care.

The Enter/Edit DMC Report \# Days for Episodes of Care option allows you to enter/edit the NUMBER OF DAYS FOR DMC REPORTS parameter in the AR Site Parameter (file \#342).

The minimum value for this site parameter is 365 days (1 year) and the maximum value is 3650 days (10 years). If no value is added for this site parameter, the default value is 365 days.

The following reports use this parameter:

- DMC Debt Validity Report
- DMC Debt Validity Management Report
- Rated Disability Eligibility Change Report

<span id="_Toc198214886" class="anchor"></span>Figure 14: Enter/Edit \# Days for Episodes of Care

Select DMC Referral Menu Option: 10 Enter/Edit DMC Report \# Days for Episodes of

NUMBER OF DAYS FOR DMC REPORTS: 365// 730

## Entering/Editing the \# OF DAYS FOR RD ELIG CHG RPT Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Rated Disability Eligibility Change Report is setup by IRM staff as a “scheduled task” the software will check for rated disability data that has changed during the last 31 days. If the site would like to change this default value, they can do so using the Enter/Edit RD Number of Days Report Parameter option. It allows you to enter or edit the \# OF DAYS FOR RD ELIG CHG RPT site parameter in the AR Site Parameter file, \#342. This option will only need to be used if the site selected timeframe needs to be changed.

You are prompted to select the number of days in the past (between 1 and 365) that Rated Disability Changes will be checked when the Rated Disability Eligibility Change Report is scheduled by IRM to be run on a recurring basis. If no value is added in this field, the report defaults to 31 days.

<span id="_Toc198214887" class="anchor"></span>Figure 15: Enter/Edit RD Number of Days Report

Select DMC Referral Menu Option: 9 Enter/Edit RD Number of Days Report Parameter

\# OF DAYS FOR RD ELIG CHG RPT:

## to 40 Percent SC Change Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 0 to 40 Percent SC Change Reconciliation Report is provided to assist users in reviewing the legitimacy of first party bills for Veterans who received a new or updated change to a 0-40% SC eligibility factor and received the change in VistA during the report time frame requested. This report provides information on bills/charges without an IB Status of “Cancelled” and with an A/R Status of Active, Suspended, Open, Write-Off, Collected/Closed, Cancellation, or with an IB Bill Status of On Hold, for episodes of care within a user selected time frame.

The report *does not include* bills for:

- Debtors whose Service Connection is 50% or more
- Debtors who are receiving a VA pension (regardless of their SC%)
- Debtors receiving Aid and Attendance

Users are prompted to enter a Beginning and Ending date related to the rated disabilities/eligibility change. Users are also prompted to enter a beginning and ending date for a VistA last status date range in order to remove any false positive cases from the report dataset. Lastly, users are prompted to enter a beginning and ending date for an episodes of care date range. Only Veterans who meet the above criteria, and whose rated disability eligibility has changed during the selected timeframe will be included in the report output.

Authorized VA CPAC staff should run this report to ensure that all bills meeting these criteria are reviewed and, if necessary, the appropriate action is taken to remove exempt bills from the billing record, or to refer valid and eligible bills for further collection by DMC.

The report allows users to choose whether to print the report in a detailed format, a summary format, or in an Excel Delimited format.

It is recommended that users queue this report to a device that is 150 characters wide.

8.  The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.

This report may take a while to process. It is recommended that you Queue this report to a device that is 150 characters wide.

The following is an example of the 0 to 40 Percent SC Change Reconciliation Report input parameters when this option is selected from the DMC Referral Menu screen.

<span id="_Toc198214888" class="anchor"></span>Figure 16: 0% - 40% SC Change Reconciliation Report

Select DMC Referral Menu Option: 11 0 to 40 Percent SC Change Reconciliation Report

Enter the Date Range for Rated Disability Eligibility Changes:

Enter Begin Date: TODAY//

Enter End Date: TODAY//

Include Bills with VistA Last Status Date that fall within the Date Range for Rated Disability Changes:

Enter VistA Last Status Date Begin Date: DEFAULT IS THE SAME DATE ENTERED or SELECTED FOR RDEC BEGIN DATE ABOVE//

Enter VistA Last Status Date End Date: DEFAULT IS THE SAME DATE ENTERED or SELECTED FOR RDEC END DATE ABOVE//

Include Bills for Episodes of Care within User Selected Date Range:

Enter Episodes of Care Begin Date: Jan 01, 1988//

Enter Episodes of Care End Date: TODAY//

Select one of the following report types:

D DETAILED

S SUMMARY

Enter Report Type: DETAILED//

Do you want to capture report data for an Excel document? YES//

DEVICE: HOME// \<See note on printing on the following page\>

To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g. spoolname;256;99999). This should help avoid wrapping problems.

Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by clicking on the ‘Tools’ menu above, then click on ‘Capture Incoming Data’ to save to Desktop. To avoid undesired wrapping of the data saved to the file, please enter ‘0;256;99999’ at the ‘DEVICE:’ prompt:

<span id="_Hlk5098560" class="anchor"></span>

Figure 17: 0% - 40% SC Change Report Example (Non-Excel Format)

0-40 Percent SC Change Reconciliation Detailed Report -- Run Date: 01 Apr 2019 11:00 am -- Page 1

RD Change Dates from 01 Jan 2017 to 28 Feb 2017 VistA Change Dates from 01 Jan 2017 to 28 Feb 2017

Episode of Care Dates from 01 Jan 1988 to 01 Apr 2019

Medical

Comb VistA RD Orig Charge Care

Veteran Name SSN SC % Chd Date RD Name Date Bill Number Amount Date RXFillDT RX \# RX Name Status

====================================================================================================================================

AAAAAA,EEEEE nnnnnnnnn 20 02Feb17 DIABETES MELLI 12Feb16 442-K000008 \$50.00 04Oct16 C/C

BBBBBBBBBB,DD nnnnnnnnn 30 14Feb17 DIABETES MELLI 05Jan16 442-K000007 \$8.00 05Sep17 nnnnnnn COLON ELECTROL C/C

BBBBBBBBBB,DD nnnnnnnnn 30 14Feb17 TINNITUS 05Jan16 442-K000006 \$8.00 05Sep17 nnnnnnn COLON ELECTROL C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000001 \$8.00 25Oct11 nnnnnnn PREDNISOLONE A C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000002 \$8.00 25Oct11 nnnnnnn MOXIFLOXACIN H C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000003 \$8.00 25Oct11 nnnnnnn KETOROLAC TROM C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000004 \$8.00 23Feb12 nnnnnnn MOXIFLOXACIN H C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000004 \$8.00 21Mar12 nnnnnnn KETOROLAC TROM C/C

CCCCCCC,DDDDD nnnnnnnnn 40 27Feb17 PARALYSIS OF S 03Nov10 442-K000005 \$8.00 21Mar12 nnnnnnn PREDNISOLONE A C/C

CCCCCCCCC,VVV nnnnnnnnn 10 13Feb17 TINNITUS 22Apr16 442-K000011 \$24.00 10Aug16 nnnnnnn ATORVASTATIN C C/C

CCCCCCCCC,VVV nnnnnnnnn 10 13Feb17 TINNITUS 22Apr16 442-K000017 \$50.00 25Aug16 C/C

CCCCCCCCC,VVV nnnnnnnnn 10 13Feb17 TINNITUS 22Apr16 442-K000015 \$8.00 29Aug16 nnnnnnn DEXTRAN 70/HYP C/C

CCCCCCCCC,VVV nnnnnnnnn 10 13Feb17 TINNITUS 22Apr16 442-K000014 \$50.00 31Aug16 C/C

<span id="_Toc198214890" class="anchor"></span>Figure 18: 0% - 40% SC Change Report (Excel Format)

> Veteran Name^SSN^Comb SC %^VistA Chd Date^RD Name^RD Orig Date^Bill Number^Charge Amount^Medical Care Date^RXFillDT^RX \#^RX Name^Status

> “AAAAAA,EEEEE LLLLL”^nnnnnnnnn^20^02 Feb 2017^DIABETES MELLITUS^12 Feb 2016^442-Knnnnn8^\$50.00^04 Oct 2016^^^^C/C

> “BBBBBBBBBB,DDDDDDD RRR”^nnnnnnnnn^30^14 Feb 2017^DIABETES MELLITUS^05 Jan 2016^442-Knnnnn7^\$8.00^^05 Sep 2017^nnnnnnn^COLON ELECTROLYTE LAVAGE PWD FOR SOLN^C/C

> “BBBBBBBBBB,DDDDDDD RRR”^nnnnnnnnn^30^14 Feb 2017^TINNITUS^05 Jan 2016^442-Knnnnn6^\$8.00^^05 Sep 2017^nnnnnnn^COLON ELECTROLYTE LAVAGE PWD FOR SOLN^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000001^\$8.00^^25 Oct 2011^nnnnnnn^PREDNISOLONE ACETATE 1% OPH SUSP^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000002^\$8.00^^25 Oct 2011^nnnnnnn^MOXIFLOXACIN HCL 0.5% OPH SOLN^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000003^\$8.00^^25 Oct 2011^nnnnnnn^KETOROLAC TROMETHAMINE 0.5% OPH SOLN^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000004^\$8.00^^23 Feb 2012^nnnnnnn^MOXIFLOXACIN HCL 0.5% OPH SOLN^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000004^\$8.00^^21 Mar 2012^nnnnnnn^KETOROLAC TROMETHAMINE 0.5% OPH SOLN^C/C

> “CCCCCCC,DDDDDD J”^nnnnnnnnn^40^27 Feb 2017^PARALYSIS OF SCIATIC NERVE^03 Nov 2010^442-K000005^\$8.00^^21 Mar 2012^nnnnnnn^PREDNISOLONE ACETATE 1% OPH SUSP^C/C

> “CCCCCCCCC,VVVVV TTTTTT”^nnnnnnnnn^10^13 Feb 2017^TINNITUS^22 Apr 2016^442-K000011^\$24.00^^10 Aug 2016^nnnnnnn^ATORVASTATIN CALCIUM 40MG TAB^C/C

> “CCCCCCCCC,VVVVV TTTTTT”^nnnnnnnnn^10^13 Feb 2017^TINNITUS^22 Apr 2016^442-K000017^\$50.00^25 Aug 2016^^^^C/C

> “CCCCCCCCC,VVVVV TTTTTT”^nnnnnnnnn^10^13 Feb 2017^TINNITUS^22 Apr 2016^442-K000015^\$8.00^^29 Aug 2016^nnnnnnn^DEXTRAN 70/HYPROMELLOSE 0.3% OPH SOLN^C/C

> “CCCCCCCCC,VVVVV TTTTTT”^nnnnnnnnn^10^13 Feb 2017^TINNITUS^22 Apr 2016^442-K000014^\$50.00^31 Aug 2016^^^^C/C

## First Party Charge IB Cancellation Recon Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Party Charge IB Cancellation Recon Report is provided to assist users in reviewing first party copayments charges that received IB cancellation for the purpose of potential refund activities or charge cancellation accuracy. Further, the report provides additional operational value to identify and monitor cancellation activity productivity and accuracy. The report provides specific output for the purpose of providing refunds due to Veterans for retroactive eligibility exemptions, and/or cancelled charges. The report provides data for first party charges receiving IB cancellation for a user defined bill cancellation date range.

The report provides the option to display only bills with payments or print all cancelled charges/bills within the user specified bill cancellation date range.

If only bills with payments are printed, the report will include bills with an IB Status of Cancelled that have charges AND a payment.

If all bills are printed, the report will include bills with an IB Status of Cancelled regardless of presence of payments.

The report defaults the option to print the report in an Excel Delimited format.

Authorized billing staff should run this report to ensure that all bills meeting these criteria are reviewed and, if necessary, the appropriate action is taken.

It is recommended that you queue this report to a device that is 150 characters wide.

9.  This report does not include bills with third-party AR Category Types of “Reimbursable” or “Pre-payments”.

The following is an example showing the First Party Charge IB Cancellation Recon Report input parameters if this option is selected with Excel document default.

<span id="_Toc198214891" class="anchor"></span>Figure 19: First Party Charge IB Cancellation Report

Select DMC Referral Menu Option: 12 First Party Charge IB Cancellation Recon Report

Enter the Bill Cancellation Date Range:

Enter Beginning Date: TODAY//

Enter Ending Date: TODAY//

Do you want to see only bills with payments? YES//

Do you want to capture report data for an Excel document? YES//

This report may take a while to run. It is recommended that you Queue it.

To capture as an Excel format, it is recommended that you queue this

report to a spool device with margins of 256 and page length of 99999

(e.g. spoolname;256;99999). This should help avoid wrappint problems.

Another method would be to set up your terminal to capture the detail

report data. On some terminals, this can be done by clicking on the

‘Tools’ menu above, then click on ‘Capture Incoming Data’ to save to

Desktop. To avoid undesired wrapping of the data saved to the file,

please enter ‘0;256;99999’ at the ‘DEVICE:’ prompt.

DEVICE: HOME// 0;256;99999 HOME (CRT)

<span id="_Toc198214892" class="anchor"></span>Figure 20: First Party Charge IB Cancellation (Non-Excel)

First Party Charge IB Cancellation Reconciliation Report -- Run Date: 19 Aug 2020 12:51 pm -- Page 1

Cancellation Dates from 01 Jan 2015 to 01 Feb 2015

Charge Medical IB Cancellation

Veteran Name SSN Bill Number Amount APPR RSC Care Date RXFillDT RX \# RX Name IBCXLDT Reason Cancelled By

======================================================================================================================================================

AAAAA,BBBB nnnnnnnnn 442-K201YIU \$24.00 528701 8BZZ 03May12 2353941 GABAPENTIN 300 20Jan15 AGENT ORANGE REL DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K201YIU \$24.00 528701 8BZZ 24Jan12 2353941 GABAPENTIN 300 20Jan15 AGENT ORANGE REL DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503SFN \$15.00 528703 88ZZ 02Jan15 03Jan15 CHECK OUT DELETE DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$24.00 528701 8CZZ 20Jan15 1243678E SIMVASTATIN 40 26Jan15 RX COPAY INCOME DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$8.00 528701 8CZZ 15Dec14 6046423 HYPROMELLOSE 0 20Jan15 COMBAT VETERAN DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$8.00 528701 8CZZ 31Dec14 6046423 HYPROMELLOSE 0 20Jan15 COMBAT VETERAN DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$24.00 528701 8BZZ 30Dec14 1258276A HCTZ 25/LISINO 15Jan15 RX REFUSED DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$8.00 528701 8BZZ 18Nov14 2534514A DILTIAZEM (EQV 16Jan15 PATIENT DECEASED DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$8.00 528701 8BZZ 18Nov14 2534515A GABAPENTIN 300 16Jan15 PATIENT DECEASED DDDDDD, EEEEEE

AAAAA,BBBB nnnnnnnnn 442-K503XFQ \$8.00 528701 8BZZ 18Nov14 2534516A METOPROLOL TAR 16Jan15 PATIENT DECEASED DDDDDD, EEEEEE

<span id="_Toc198214893" class="anchor"></span>Figure 21: First Party Charge IB Cancellation (Excel Format)

Veteran Name^SSN^Bill Number^Charge Amount^APPR^RSC^Medical Care Date^RXFillDT^RX \#^RX Name^IBCXLDT^IB Cancellation Reason^Cancelled By

“AAAA,BBBB”^nnnnnnnnn^442-K201YIU^\$24.00^528701^8BZZ^^03 May 2012^2353941^GABAPENTIN 300MG CAP^20 Jan 2015^AGENT ORANGE RELATED^”DDDDDD, EEEEEE”

“AAAA,BBBB”^nnnnnnnnn^442-K201YIU^\$24.00^528701^8BZZ^^24 Jan 2012^2353941^GABAPENTIN 300MG CAP^20 Jan 2015^AGENT ORANGE RELATED^”DDDDDD, EEEEEE”

“AAAA,BBBB”^nnnnnnnnn^442-K503SFN^\$15.00^528703^88ZZ^02 Jan 2015^^^^03 Jan 2015^CHECK OUT DELETED^”DDDDDD, EEEEEE”

“AAAA,BBBB”^nnnnnnnnn^442-K503XFQ^\$24.00^528701^8CZZ^^20 Jan 2015^1243678E^SIMVASTATIN 40MG TAB^26 Jan 2015^RX COPAY INCOME EXEMPTION^

“DDDDDD, EEEEEE”

“AAAA,BBBB”^nnnnnnnnn^442-K503LW2^\$8.00^528701^8CZZ^^15 Dec 2014^6046423^HYPROMELLOSE 0.4% OPH SOLN^20 Jan 2015^COMBAT VETERAN^”DDDDDD, EEEEEE”

## 10-40% SC Med Care Copay Exempt Charge Recon Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 10-40% SC Med Care Copay Exempt Chrg Recon Report is provided to assist users in reviewing all medical care copayment bills containing charges with a distinct date of service on or after the copayment exemption effective date for Veterans with SC Percent equal to 10 to 40% and does not show prescription copayment bills.

The report captures any medical care copayment charge without an IB status of cancelled, and with an AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, Cancellation, or an IB Status of On-Hold, with a date of service on or after the exemption effective date.

The User can select to run the report for a bill status of Active, Open, Suspended, Collected/Closed, On-Hold, Write-Off, or ALL of those. If ALL is selected, then it will also include AR status of Cancellation.

The report allows users to choose whether to print the report in a non-Excel Delimited format or an Excel Delimited format. It is recommended that users queue this report to a device that is 150 characters wide.

10. The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.
11. If a Veteran has more than one bill, the report prints a row for every bill number (K#) they have that meets the report parameters.
12. If a bill has a Status of “On-Hold”, the Bill number field will be blank.
13. If the Veteran record tied to the bill does not have a Co-Payment Exemption Date, the report prints/displays “NODATE” in the EXMPTDT field.

<span id="_Toc198214894" class="anchor"></span>Figure 22: 10% - 40% SC Med Care Copay Exempt Report

Select DMC Referral Menu Option: 13 10-40% SC Med Care Copay Exempt Chrg Recon Report

<span id="_Toc198214895" class="anchor"></span>Figure 23: 10%- 40% SC Med Care Copay Exempt (Input Parameters)

\*\*\* Print the 10-40% SC Medical Care Copayment Exempt Charge Recon Report \*\*\*

Report to Include Bills for charges without an IB status of Cancelled, with an

AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, or with IB

Status of On-Hold, and date of service on or after the exemption effective date.

Select one of the following:

1 Active

2 Open

3 Suspended

4 Collected/Closed

5 On-Hold

6 Write Off

7 All

Select one of the following Bill Statuses: 7// All

Do you want to capture report data for an Excel document? NO//

This report may take a while to process. It is recommended that

you Queue this report to a device that is 150 characters wide.

DEVICE: HOME// 0;132 HOME (CRT)

<span id="_Toc198214896" class="anchor"></span>Figure 24: 10% - 40% SC Med Care Copay (non-Excel)

10-40% SC Medical Care Copayment Exempt Charge Reconciliation Report -- Run Date: 09 Apr 2019 1:34 pm -- Page 1

Veteran Name SSN SC Percent Bill \# EXMPTDT Med Care Date Status

===============================================================================================

AARRRRRR.TTTTTT H nnnnnnnnn 30% NODATE

ABBBBB,BBBBBB JJJJJ nnnnnnnnn 10% 442-K402QJX 28Oct12 07Oct13 C/C

ABBBBB,BBBBBB JJJJJ nnnnnnnnn 10% 442-K404HKN 28Oct12 17Apr14 C/C

ABDDDDDDD,BBBBBB L nnnnnnnnn 20% NODATE

BBBB,GGGGGGG nnnnnnnnn 10% NODATE

BBBB,RRRRRR E nnnnnnnnn 40% NODATE

BBRRRRRR,MMMMMM W nnnnnnnnn 10% NODATE

BRRRRRK,JJJJJ LL nnnnnnnnn 30% NODATE

BRRRRRK,PPPP EEEE nnnnnnnnn 30% NODATE

CCCCCCC,TTTTTTT W nnnnnnnnn 20% 442-K403J4J 20May13 24Dec13 C/C

CCCCCCC,TTTTTTT W nnnnnnnnn 20% 442-K403J4J 20May13 27Dec13 C/C

CCCCCCC,TTTTTTT W nnnnnnnnn 20% 442-K403J4J 20May13 20Dec13 C/C

CCCCCCC,TTTTTTT W nnnnnnnnn 20% 442-K404LHT 20May13 15Jan14 C/C

CCCCCCC,TTTTTTT W nnnnnnnnn 20% 442-K404TU9 20May13 24Feb14 C/C

CKKKKK,QQQQQQQ WWWWWW nnnnnnnnn 30% 442-K202H9H 13Jul12 20Jul12 C/C

DDDDEEEGO,DEDEDEDE RRRT nnnnnnnnn 20% 442-K404FTN 03May13 06Dec13 WRITE-OFF

DERRRRRRR,BRRRR,MMMMM nnnnnnnnn 20% NODATE

DTDTDT,SSSSSS DLXZW nnnnnnnnn 10% 442-K705RR7 01Jun17 05Jul17 C/C

<span id="_Toc198214897" class="anchor"></span>Figure 25: 10%- 40% SC Med Care Copay (Excel Format)

Veteran Name^SSN^SC Percent^Bill \#^EXMPTDT^Med Care Date^Status

AARRRRRR.TTTTTT H^nnnnnnnnn^30%^ ^NODATE^^^

ABBBBB,BBBBBB JJJJJ^nnnnnnnnn^10%^442-K402QJX^28 Oct 2012^07 Oct 2013^C/C^

ABBBBB,BBBBBB JJJJJ^nnnnnnnnn^10%^442-K404HKN^28 Oct 2012^17 Apr 2014^C/C^

ABDDDDDDD,BBBBBB L^nnnnnnnnn^20%^ ^NODATE^^^

BBBB,GGGGGGG^nnnnnnnnn^10%^ ^NODATE^^^

BBBB,RRRRRR E^nnnnnnnnn^40%^ ^NODATE^^^

BBRRRRRR,MMMMMM W^nnnnnnnnn^10%^ ^NODATE^^^

BRRRRRK,JJJJJ LL^nnnnnnnnn^30%^ ^NODATE^^^

BRRRRRK,PPPP EEEE^nnnnnnnnn^30%^ ^NODATE^^^

CCCCCCC,TTTTTTT W^nnnnnnnnn^20%^442-K403J4J^20 May 2013^24 Dec 2013^C/C^

CCCCCCC,TTTTTTT W^nnnnnnnnn^20%^442-K403J4J^20 May 2013^27 Dec 2013^C/C^

CCCCCCC,TTTTTTT W^nnnnnnnnn^20%^442-K403J4J^20 May 2013^20 Dec 2013^C/C^

CCCCCCC,TTTTTTT W^nnnnnnnnn^20%^442-K404LHT^20 May 2013^15 Jan 2014^C/C^

CCCCCCC,TTTTTTT W^nnnnnnnnn^20%^442-K404TU9^20 May 2013^24 Feb 2014^C/C^

CKKKKK,QQQQQQQ WWWWWW^nnnnnnnnn^30%^442-K202H9H^13 Jul 2012^20 Jul 2012^C/C^

DDDDEEEGO,DEDEDEDE RRRT^nnnnnnnnn^20%^442-K404FTN^03 May 2013^06 Dec 2013^WRITE-OFF^

DERRRRRRR,BRRRR,MMMMM^nnnnnnnnn^20%^ ^NODATE^^^

DTDTDT,SSSSSS DLXZW^nnnnnnnnn^10%^442-K705RR7^01 Jun 2017^05 Jul 2017^C/C^

## 50-100% SC Exempt Charge Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 50-100% SC Exempt Charge Reconciliation Report is provided to assist users in reviewing all bills containing charges with a distinct date of service on or after the co-payment exemption effective date for Veterans with Primary or Secondary Eligibility equal to 50 to 100% Service Connected.

The report captures any charges without an IB status of cancelled, and with an AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, Cancellation, or an IB Status of On-Hold, with a date of service on or after the exemption effective date.

The User can select to run the report for a bill status of Active, Open, Suspended, Collected/Closed, On-Hold, Write-Off, or ALL. The ALL option includes the six noted bill statuses plus the AR status of CANCELLATION.

The report allows users to choose whether to print the report in a non-Excel Delimited format or an Excel Delimited format.

It is recommended that users queue this report to a device that is 150 characters wide.

14. The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.
15. The Med Care Date will be blank if the charge is for a medication.
16. The RxFillDt will be blank if there is a Med Care Date.
17. The RX# and RX Name will be blank if the charge is for medical care.
18. If a Veteran has more than one bill, the report prints a row for every bill number (K#) they have that meets the report parameters.
19. If a bill has a Status of “On-Hold”, the Bill number field will be blank.
20. If the Veteran record tied to the bill does not have a Co-Payment Exemption Date, the report prints/displays “NODATE” in the EXMPTDT field and only prints one row of information if the Debtor has at least one bill matching the selected “Status” (e.g. Active, Open, Suspended, Collected/Closed, Write-Off, On-Hold).

<span id="_Toc198214898" class="anchor"></span>Figure 26: 50%- 100% SC Exempt Charge Recon Report

Select DMC Referral Menu Option: 14 50-100% SC Exempt Charge Reconciliation Report

\*\*\* Print the 50-100 Percent SC Exempt Charge Reconciliation Report \*\*\*

Report to Include Bills for charges without an IB status of Cancelled, with an

AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, or with IB

Status of On-Hold, and date of service on or after the exemption effective date.

Select one of the following:

1 Active

2 Open

3 Suspended

4 Collected/Closed

5 On-Hold

6 Write Off

7 All

Select one of the following Bill Statuses: 7// 7 All

Do you want to capture report data for an Excel document? NO//

This report may take a while to process. It is recommended that

you Queue this report to a device that is 150 characters wide.

DEVICE: HOME// 0;132 HOME (CRT)

<span id="_Toc198214899" class="anchor"></span>Figure 27: 50%- 100% - SC Exempt Report (non-Excel)

50-100 Percent SC Exempt Charge Reconciliation Report -- Run Date: 09 Apr 2019 4:06 pm -- Page 11

Veteran Name SSN Eligibility Bill \# EXMPTDT Med Care Date RXFillDT RX \# RX Name Status

====================================================================================================================================

ALVVVVV,KKKKKKKKKK AAAA nnnnnnnnn SC60 442-K701L7J 05Jan06 30Apr07 2063651 ALBUTEROL 90MCG (CFC-F C/C

ALVVVVV,KKKKKKKKKK AAAA nnnnnnnnn SC60 442-K701L7J 05Jan06 30Apr07 2063654 BPM 12/PSEUDOEPHEDRINE C/C

ALVVVVV,KKKKKKKKKK AAAA nnnnnnnnn SC60 442-K701L7J 05Jan06 30Apr07 2063652 FLUNISOLIDE 0.025% 200 C/C

ALVVVVV,KKKKKKKKKK AAAA nnnnnnnnn SC60 442-K7026P8 05Jan06 12Jul07 2063654 BPM 12/PSEUDOEPHEDRINE C/C

ALVVVVV,KKKKKKKKKK AAAA nnnnnnnnn SC60 442-K702JIP 05Jan06 05Sep07 2083786 COLON ELECTROLYTE LAVA C/C

ALVVVVV,RRRR DDDD nnnnnnnnn SC100 442-K300S4B 01Jan02 10Feb03 1133114 LEVOTHYROXINE NA (SYNT C/C

ALVVVVV,RRRR DDDD nnnnnnnnn SC100 442-K300S4B 01Jan02 10Feb03 1133116 SIMVASTATIN 40MG TAB C/C

ALVVVVV,WWWWW M nnnnnnnnn SC50 NODATE

ALWWWWW,AGUUUUU RRRRRRR nnnnnnnnn SC100 442-K705Z3C 10Aug17 14Aug17 2736131 DOCUSATE NA 100MG CAP C/C

AMODD,DDDDDDD nnnnnnnnn SC70 442-K402NVZ 22Jul13 02Oct13 C/C

AMODD,DDDDDDD nnnnnnnnn SC70 442-K403CIG 22Jul13 13Dec13 C/C

AMODD,DDDDDDD nnnnnnnnn SC70 442-K403CIG 22Jul13 20Dec13 C/C

ANN,EEEEEEE J nnnnnnnnn SC60 NODATE

ANVVV,VVVVV E nnnnnnnnn SC50 442-K404APM 01Apr13 30Dec13 C/C

ANWWWWWW,BBBBBBB TTTTTT nnnnnnnnn SC60 442-K405J98 24Jul14 14Aug14 C/C

ANYYYYY,SSSS WWWWWW nnnnnnnnn SC90 442-K500UX8 10Feb05 17Feb05 734874 QUETIAPINE FUMARATE 25 WRITE-OFF

ANYYYYY,SSSS WWWWWW nnnnnnnnn SC90 442-K500UX8 10Feb05 17Feb05 734875 VALPROIC ACID 250MG CA WRITE-OFF

ANZZZZ,AGGGGGG S nnnnnnnnn SC60 NODATE

<span id="_Toc198214900" class="anchor"></span>Figure 28: 50%- 100% SC Exempt Charge Report (Excel Format)

Veteran Name^SSN^Eligibility^Bill \#^EXMPTDT^Med Care Date^RXFillDT^RX \#^RX Name^Status

ALVVVVV,KKKKKKKKKK AAAA^nnnnnnnnn^SC60^442-K701L7J^05 Jan 2006^^30 Apr 2007^2063651^ALBUTEROL 90MCG (CFC-F) 200D ORAL INHL^C/C^

ALVVVVV,KKKKKKKKKK AAAA^nnnnnnnnn^SC60^442-K701L7J^05 Jan 2006^^30 Apr 2007^2063654^BPM 12/PSEUDOEPHEDRINE 120MG SA CAP^C/C^

ALVVVVV,KKKKKKKKKK AAAA^nnnnnnnnn^SC60^442-K701L7J^05 Jan 2006^^30 Apr 2007^2063652^FLUNISOLIDE 0.025% 200D NASAL INH SPRAY^C/C^

ALVVVVV,KKKKKKKKKK AAAA^nnnnnnnnn^SC60^442-K7026P8^05 Jan 2006^^12 Jul 2007^2063654^BPM 12/PSEUDOEPHEDRINE 120MG SA CAP^C/C^

ALVVVVV,KKKKKKKKKK AAAA^nnnnnnnnn^SC60^442-K702JIP^05 Jan 2006^^05 Sep 2007^2083786^COLON ELECTROLYTE LAVAGE PWD FOR SOLN^C/C^

ALVVVVV,RRRR DDDD^nnnnnnnnn^SC100^442-K300S4B^01 Jan 2002^^10 Feb 2003^1133114^LEVOTHYROXINE NA (SYNTHROID) 0.075MG TAB^C/C^

ALVVVVV,RRRR DDDD^nnnnnnnnn^SC100^442-K300S4B^01 Jan 2002^^10 Feb 2003^1133116^SIMVASTATIN 40MG TAB^C/C^

ALVVVVV,WWWWW M^nnnnnnnnn^SC50^ ^NODATE

ALWWWWW,AGUUUUU RRRRRRRH^nnnnnnnnn^SC100^442-K705Z3C^10 Aug 2017^^14 Aug 2017^2736131^DOCUSATE NA 100MG CAP^C/C^

AMODD,DDDDDDD^nnnnnnnnn^SC70^442-K402NVZ^22 Jul 2013^02 Oct 2013^^^^C/C^

AMODD,DDDDDDD^nnnnnnnnn^SC70^442-K403CIG^22 Jul 2013^13 Dec 2013^^^^C/C^

AMODD,DDDDDDD^nnnnnnnnn^SC70^442-K403CIG^22 Jul 2013^20 Dec 2013^^^^C/C^

ANN,EEEEEEE J^nnnnnnnnn^SC60^ ^NODATE

ANVVV,VVVVV E^nnnnnnnnn^SC50^442-K404APM^01 Apr 2013^30 Dec 2013^^^^C/C^

ANWWWWWW,BBBBBBB TTTTTT^nnnnnnnnn^SC60^442-K405J98^24 Jul 2014^14 Aug 2014^^^^C/C^

ANYYYYY,SSSS WWWWWW^nnnnnnnnn^SC90^442-K500UX8^10 Feb 2005^^17 Feb 2005^734874^QUETIAPINE FUMARATE 25MG TAB^WRITE-OFF^

ANYYYYY,SSSS WWWWWW^nnnnnnnnn^SC90^442-K500UX8^10 Feb 2005^^17 Feb 2005^734875^VALPROIC ACID 250MG CAP^WRITE-OFF^

ANZZZZ,AGGGGGG S^nnnnnnnnn^SC60^ ^NODATE

## Catastrophically Disabled Exempt Copay Charge Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Catastrophically Disabled Exempt Copay Charge Report is provided to assist users in reviewing copay charges with an appropriation fund of “528703” for medical care or an appropriation fund of “528701” for Rx copayments with a distinct date of service or Rx fill date on or after the Catastrophically Disabled (CD) exemption effective date for Veterans who are Catastrophically Disabled.

The report captures charges without an IB status of canceled, and with an AR Status of Active, Open, Suspended, Write-Off, Cancellation, Collected/Closed, or an IB Status of On-Hold with a date of service on or after the Catastrophic Disability Date. The Catastrophically Disabled legislation effective date is May 5, 2010, so only charges on or after this date qualify for the CD copay exemption.

The User is prompted to enter a start date and an end date for charges that fall within the dates of service range. If a start date that is prior to May 5, 2010 is entered, the system will automatically change it to May 5, 2010 on the output report header.

The report allows users to choose whether to print the report in a non-Excel delimited format or an Excel delimited format.

If the report is sent to the screen, it is recommended that users queue this report to a device that is 150 characters wide. For Excel, please use 256 characters wide capture.

<span id="_Toc198214901" class="anchor"></span>Figure 29: Catastrophically Disabled Exempt Copay Charge Report

Select DMC Referral Menu Option: 15 Catastrophically Disabled Exempt Copay Charge Rpt

\*\*\* Print the Catastrophically Disabled Exempt Copay Charge Report \*\*\*

The Catastrophically Disabled legislation effective date is May 5, 2010.

You should not enter a date prior to that date, any date entered before

that will be automatically changed to May 5, 2010.

This report includes bills for charges without an IB Status of Cancelled

and with an AR Status of Active, Open, Suspended, Write-Off, Cancellation,

Collected/Closed or with an IB Status of On-Hold, and an episode of care

date on or after the Catastrophically Disabled exemption effective date.

Start with DATE: May 5, 2010// (MAY 05, 2010)

Go to DATE: T// (JUL 24, 2019)

Do you want to capture report data for an Excel document? NO//

This report may take a while to process. It is recommended that you Queue

this report to a device that is 150 characters wide.

DEVICE: HOME// 0;132 HOME (CRT)

<span id="_Toc198214902" class="anchor"></span>Figure 30: Cat Disabled Report (non-Excel)

Cross-Servicing Catastrophically Disabled Exempt Copayment Charge Report --- Run Date: 24 Jul 2019 2:31 pm --- Page: 1

Episode of Care Dates from 05 May 2010 to 24 Jul 2019

Pri CD Medical RX Fill Charge

Patient Name SSN Grp Date Bill NO Care Date Date RX \# RX Name Amount IB Status AR Status

---------------------------------------------------------------------------------------------------------------------------------

OOOO,RRRRR LLL nnnnnnnnn 4 07/30/01 K002A39 05/13/10 15.00 BILLED CANCELLATION

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 05/26/10 1190814 FERROUS SULFATE 324M 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 05/28/10 2241324 GABAPENTIN 300MG CAP 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 05/28/10 1188068A THEOPHYLLINE 300MG S 24.00 BILLED C/C

CCCCCC,PPPPP AAA nnnnnnnnn 1 10/15/09 K003ZD3 05/28/10 1195691A LISINOPRIL 10MG TAB 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K0020YN 06/02/10 50.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/08/10 1204898 DIAZEPAM 5MG TAB 8.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K0020YN 06/08/10 15.00 BILLED C/C

WWWWWWWWW, QQQ C nnnnnnnnn 1 02/23/05 K006QM8 06/08/10 1181748A MOMETASONE FUROATE 2 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/08/10 2120134I CYANOCOBALAMIN 1000M 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K0020YN 06/15/10 50.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/15/10 2009266D ALENDRONATE 70MG TAB 24.00 BILLED C/C

SSSSSS,WWWWWWW WWWWW nnnnnnnnn 2 11/16/00 K001WRT 06/17/10 2255091 TERAZOSIN HCL 1MG CA 8.00 BILLED C/C

KKKK, GGGGGG nnnnnnnnn 1 09/13/02 K0072BK 06/18/10 15.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/19/10 1205485 HYDROCHLOROTHIAZIDE 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/19/10 1171790D METFORMIN HCL 1000MG 24.00 BILLED C/C

AAAAAAAA,TTTT NNNNNN nnnnnnnnn 1 05/05/10 K001YD2 06/19/10 1140193H OMEPRAZOLE 20MG EC C 24.00 BILLED C/C

Type \<Enter\> to continue or ‘^’ to exit:

## First Party Veteran Charge Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Party Veteran Charge Report is provided to assist users in reviewing medical care and outpatient copay charges for a single veteran. The report captures charges with the IB statuses of BILLED, ON HOLD, and CANCELLED.

The report also captures charges specific to rate types where the patient is responsible for payment; these rate types are HUMANITARIAN, INELIGIBLE, DENTAL, and MEANS TEST. Charges with these rate types are limited to statuses of AUTHORIZED, PRNT/TX, and CANCELLED.

The user is prompted to enter a veteran name, a from date, and a to date for charges that fall within the dates of service range. The report is designed for export to a spreadsheet and uses a 256 characters length for wide capture.

The user will use the cut/paste functionality to place the data fields in a spreadsheet. The caret (^) is the delimiter used to separate data fields in the report.

<span id="_Toc198214903" class="anchor"></span>Figure 31: First Party Veteran Charge Report

Select DMC Referral Menu Option: 16 First Party Veteran Charge Report

\*\*\* Print the First Party Veteran Charge Report \*\*\*

This report captures detailed 1st party bill information for a specific Veteran, within a user specified range of dates of service. This report output requires screen size of 256 characters wide.

Enter Veteran Name: TEST,PATIENT

Enter From Date: 010108 (JAN 01, 2008)

Enter To Date: TODAY// \<RET\>

Which type of copayment do you wish to see?

1 Medical Care Copayments

2\. Outpatient Medications

3\. Both (Medical Care Copay and Outpatient Medications)

Enter selection (1,2 or 3): 3// \<RET\>

Which IB status for the selected copayment(s) do you wish to see?

1\. Billed

2\. On Hold

3\. Cancelled

4\. ALL (Billed, On Hold, Cancelled)

Enter Status selection (1,2,3 or 4): 4// \<RET\>

Do you wish to see statement notification dates “Letter1, Letter2 etc.?” (Y/N): N// \<RET\>

The number of characters per row should be set to 256.

Please use the following path to modify the display settings:

Terminal Configuration \>\>\> Setup Display Setting \>\>\> Number of characters per row

To capture as a spreadsheet format, it is recommended that you enter the following at the DEVICE prompt: 0;256;99999. This should help avoid wrapping problems.

For pagination, please use “;256;” for the device value instead of the default.

DEVICE: 0;256;99999

<span id="_Toc198214904" class="anchor"></span>Figure 32: First Party Veteran Charge Report Example

Example of the First Party Veteran Charge Report output before pasting the data fields into a spreadsheet. The First Party Veteran Charge Report is only available in spreadsheet format.

> **NOTE:** To export to a spreadsheet, the data file type is delimited with fields separate with the caret (^).

‘RVW’ = Indicates the charge should be reviewed because there is no Appropriation fund (APPR) or Revenue Source Code (RSC) value.

<table>
<caption><p><span id="_Toc198214952" class="anchor"></span>Table 2: Accounts Receivable (AR Bill) File (#430)</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>First Party Veteran Charge Report</strong></p>
<p><strong>Run date: Jan 14, 2021 10:07 am</strong></p>
<p><strong>Service Dates From 1/1/1990 To 1/14/2021</strong></p>
<p><strong>Copayment Type Selected: Both (Medical Care and Outpatient Medication)</strong></p>
<p><strong>IB Status Selected: All (Billed, On Hold, Cancelled)</strong></p>
<p><strong>^ ^ ^ ^ Charge ^Unit^Medical^Release^ ^ ^ ^ ^Cancel ^ Cancellation ^ ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>Veteran Name ^ SSN ^Bill Number^ Category ^ Amount ^Day ^ DOS ^ RX DT ^ RX Number ^ RX Name ^ IB Status ^ AR Status ^ Date ^ Reason ^ Cancelled By ^ APPR ^RSC ^Letter1^Letter2^Letter3^Letter4</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^DG OPT COPAY NEW ^ 50.00^1 ^24Sep08^ ^ ^ ^CANCELLED ^ ^09Apr09^ENTERED IN ERR^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^DG OPT COPAY NEW ^ 15.00^1 ^02Dec08^ ^ ^ ^CANCELLED ^ ^09Apr09^ENTERED IN ERR^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^DG OPT COPAY NEW ^ 15.00^1 ^24Sep12^ ^ ^ ^CANCELLED ^ ^13Feb13^ENTERED IN ERR^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^PSO NSC RX COPAY NEW ^ 16.00^2 ^ ^30Aug17^ ^ ^CANCELLED ^ ^27Oct20^ENTERED IN ERR^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^14Sep18^2780001 ^ATROPINE 0.025 ^CANCELLED ^ ^17Sep18^CHANGE IN ELIG^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^CC URGENT CARE (OPT) NEW ^ 30.00^1 ^01Sep19^ ^ ^ ^ON HOLD ^ ^ ^ ^ ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^DG OPT COPAY NEW ^ 50.00^1 ^31Oct19^ ^ ^ ^ON HOLD ^ ^ ^ ^ ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^01Nov19^2875932 ^ATROPINE 0.025 ^ON HOLD ^ ^ ^ ^ ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^29Nov19^2909834 ^CLINDAMYCIN HCL ^ON HOLD ^ ^ ^ ^ ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^ ^DG OPT COPAY NEW ^ 50.00^1 ^29Nov19^ ^ ^ ^CANCELLED ^ ^30Dec20^CHECK OUT DELE^TEST,EMPLOYEE ^ ^ ^ ^ ^ ^</strong></p>
<p><strong>TEST,PATIENT ^000000000^K00056W ^DG OPT COPAY NEW ^ 50.00^1 ^14Oct09^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Oct09^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K00332T ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^26Aug19^2875932 ^ATROPINE 0.025 ^BILLED ^CANCELLATION ^ ^ ^ ^528701^8CZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q1U ^PSO NSC RX COPAY NEW ^ 24.00^3 ^ ^09Apr19^ ^ ^BILLED ^OPEN ^ ^ ^ ^528701^8CZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q2J ^DENTAL ^ 335.00^1 ^10Apr17^ ^ ^ ^*AUTHORIZED ^NEW BILL ^ ^ ^ ^528703^89ZZ^10Jun17^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q2K ^HUMANITARIAN ^ 335.00^1 ^29Jun17^ ^ ^ ^*PRNT/TX ^NEW BILL ^ ^ ^ ^528703^89ZZ^30Aug17^30Sep17^30Oct17^30Nov17</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q2L ^INELIGIBLE ^ 362.00^1 ^02Jan19^ ^ ^ ^*CANCELLED ^CANCELLED BILL ^17Nov20^ENTERED IN ERR^TEST,EMPLOYEE ^0160R1^RVW ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q2M ^MEANS TEST ^ 33.00^1 ^08Mar19^ ^ ^ ^*PRNT/TX ^NEW BILL ^ ^ ^ ^528703^88ZZ^30Jun19^30Jul19^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K003Q34 ^HUMANITARIAN ^ 24.86^1 ^ ^29Nov19^2909834 ^CLINDAMYCIN HCL ^*CANCELLED ^CANCELLED BILL ^30Dec20^ALREADY BILLED^TEST,EMPLOYEE ^RVW ^RVW ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K1019A3 ^DG OPT COPAY NEW ^ 50.00^1 ^13Dec10^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Mar11^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K1019A3 ^DG OPT COPAY NEW ^ 15.00^1 ^04Jan11^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Mar11^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K102XVU ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^30Aug11^2328465 ^DICYCLOMINE HCL ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Sep11^24Oct11^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K102XVU ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^30Aug11^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Sep11^24Oct11^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K2005J1 ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^18Oct11^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Oct11^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K200IJZ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^29Nov11^2328465 ^DICYCLOMINE HCL ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Dec11^24Jan12^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K200IJZ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^29Nov11^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Dec11^24Jan12^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K200UFP ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^04Jan12^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Jan12^24Feb12^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K201DVP ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^24Feb12^2328465 ^DICYCLOMINE HCL ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Mar12^24Apr12^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K201DVP ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^24Feb12^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Mar12^24Apr12^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K201SKQ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^06Apr12^2328465 ^DICYCLOMINE HCL ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Apr12^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K201SKQ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^06Apr12^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Apr12^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K202CZT ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^12Jun12^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Jun12^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K202W8Y ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^10Aug12^2328466 ^DIPHENHYDRAMINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Aug12^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K3031MN ^DG OPT COPAY NEW ^ 15.00^1 ^20Dec12^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Dec12^24Jan13^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K303N9U ^PSO NSC RX COPAY NEW ^ 24.00^3 ^ ^21Nov12^2409366 ^PANTOPRAZOLE NA ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Feb13^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K4039QG ^DG OPT COPAY NEW ^ 15.00^1 ^09Sep13^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K404G8T ^DG OPT COPAY NEW ^ 15.00^1 ^26Dec13^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Apr14^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K504M36 ^DG OPT COPAY NEW ^ 15.00^1 ^12Dec14^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Apr15^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K603ZDN ^DG OPT COPAY NEW ^ 15.00^1 ^02Nov15^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Feb16^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K60605W ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^29Aug16^2669866 ^CEPHALEXIN 250MG^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Sep16^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K703LJV ^DG OPT COPAY NEW ^ 15.00^1 ^29Sep16^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K703LK3 ^DG OPT COPAY NEW ^ 15.00^1 ^29Aug16^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K703PY7 ^DG OPT COPAY NEW ^ 15.00^1 ^27Jul16^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Dec16^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K703PY7 ^DG OPT COPAY NEW ^ 15.00^1 ^08Sep16^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Dec16^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K703ZCI ^DG OPT COPAY NEW ^ 15.00^1 ^15Nov16^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K7048VZ ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^30Dec16^2692580 ^ATROPINE 0.025 ^CANCELLED ^CANCELLATION ^28Sep20^ENTERED IN ERR^TEST,EMPLOYEE ^528701^8CZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K705EN1 ^DG OPT COPAY NEW ^ 50.00^1 ^11Apr17^ ^ ^ ^CANCELLED ^CANCELLATION ^28Sep20^ENTERED IN ERR^TEST,EMPLOYEE ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K706EKQ ^DG OPT COPAY NEW ^ 15.00^1 ^08Mar17^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^24Sep17^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K804PWN ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^21Mar18^2779999 ^ACYCLOVIR 200MG ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Apr18^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K804PWN ^PSO NSC RX COPAY NEW ^ 24.00^3 ^ ^21Mar18^2780000 ^CETIRIZINE HCL 1^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24Apr18^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K805PMS ^DG OPT COPAY NEW ^ 15.00^1 ^21Mar18^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Jun18^24Jul18^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K806B1J ^DG OPT COPAY NEW ^ 15.00^1 ^09Apr18^ ^ ^ ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528703^88ZZ^24Aug18^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K9011UM ^DG OPT COPAY NEW ^ 50.00^1 ^15Oct08^ ^ ^ ^BILLED ^CANCELLATION ^ ^ ^ ^528703^88ZZ^NO DATE^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K901RM2 ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^13May09^2186689 ^PSEUDOEPHEDRINE ^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24May09^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K901RM2 ^PSO NSC RX COPAY NEW ^ 8.00^1 ^ ^13May09^2186688 ^THROAT LOZENGE W^BILLED ^COLLECTED/CLOSED ^ ^ ^ ^528701^8CZZ^24May09^NO DATE^NO DATE^NO DATE</strong></p>
<p><strong>TEST,PATIENT ^000000000^K904WUE ^DG OPT COPAY NEW ^ 15.00^1 ^02Jan19^ ^ ^ ^CANCELLED ^COLLECTED/CLOSED ^28Sep20^ENTERED IN ERR^TEST,EMPLOYEE ^528703^88ZZ^24Apr19^24May19^24Jun19^NO DATE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc198214952" class="anchor"></span>Table 2: Accounts Receivable (AR Bill) File (#430)

Example of the First Party Veteran Charge Report output after pasting the data fields into a spreadsheet.

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/002.png)

## Pension Exemption Reconciliation Report (PERR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pension Exemption Reconciliation Report provides a list of Veterans with an eligibility of NSC,VA Pension who have bills containing charges with a distinct Date of Service that has occurred on or after the Veteran’s Co-payment Exemption Effective date.

The report criteria:

- Captures any charges WITHOUT an IB status of cancelled
- Ignores AR category of CC URGENT CARE
- Identifies charges with an AR Status of Active, Open, Suspended, Write-Off, or Collected/ Closed, or an IB Status of On Hold
- Includes a feature to include ALL, which includes all of the previously listed statuses as well as AR Cancellations
- Identifies charges with the statuses listed above, along with a date of service on or after the Veteran’s Copay Exemption effective date

The user chooses the option, and then chooses the bill Status. Choices are Active, Open, Suspended, Collected/Closed, On-Hold, Write-Off, or ALL, which includes all previously listed statuses as well as AR Cancellations. Next, the user may optionally include Veterans with a missing Exemption Date. The user may optionally configure the output format for upload to an Excel document.

<span id="_Toc198214905" class="anchor"></span>Figure 33: Pension Exemption Reconciliation Report

DMC Referral Menu \[PRCA RCDMC REFERRAL MENU\]

Select DMC Referral Menu \<TEST ACCOUNT\> Option: 17 Pension Exemption Reconcilia

tion Report (PERR)

\*\*\* Print the Pension Exempt Charge Recon Report \*\*\*

1 - Active

2 - Open

3 - Suspended

4 - Collected/Closed

5 - On-Hold;

6 - Write-Off

7 - ALL (Includes 1-6 and AR CANCELLATIONS)

Enter a list or range of numbers (1-7): 7// 7

Show veterans with missing Exempt Date? NO//

Do you want to capture report data for an Excel document? NO//

This report may take a while to process. It is recommended that

you Queue this report to a device that is 132 characters wide.

DEVICE: HOME// 0;132

63.52% done in 31 seconds

Pension Exempt Charge Reconciliation Report -- Run Date: 12 Nov 2021 2:59 pm -- Page 1

Veteran Name Pat/ID Bill \# EXMPTDT PenTermDt MedC DT RXFillDT RX \# RX Name Status Elig Type

====================================================================================================================================

AAAAA,RRRRRR DDDD A7163 442-K405MJK 01Aug19 25Aug19 6035736 FINASTERIDE 5MG TAB C/C PEN

AAAAA,RRRRRR DDDD A7163 442-K405MJK 01Aug19 25Aug19 6035742 VERAPAMIL HCL 120MG TA C/C PEN

ALLLLLLL,SSSSSS IIII A7947 442-K503Z91 01Dec19 23Jan20 1062895I DOXEPIN HCL 50MG CAP C/C PEN

ALLLLLLL,SSSSSS IIII A7947 442-K503Z91 01Dec19 18Feb20 6042549 MESALAMINE 375MG SA CA C/C PEN

ALLLLLLL,SSSSSS IIII A7947 442-K504HG3 01Dec19 17Dec19 C/C PEN

ANNNN,TTTTTT GGGG A6346 442-K201BAP 01Feb19 16Feb19 2315046A CLONAZEPAM 1MG TAB C/C PEN

ANNNN,TTTTTT GGGG A6346 442-K201CVZ 01Feb19 22Feb19 2345804 GABAPENTIN 300MG CAP C/C PEN

ANNNN,TTTTTT GGGG A6346 442-K201LWD 01Feb19 21Mar19 2315048 SIMVASTATIN 20MG TAB C/C PEN

AQQQQ,TTTTTTT EEEEEE A7165 442-K305CVB 01Jun18 20Aug18 6027903 GABAPENTIN 300MG CAP C/C PEN

BBBBBB,VVVVV FFFFFFFF B7966 442-K405IJS 01Aug18 12Aug18 1268627 ZINC OXIDE 12.8% PASTE C/C PEN

BRRRRRRR,CCCCCCCC LLL B1091 442-K503TRN 01Jan19 07Jan19 2177211G FOLIC ACID 1MG TAB C/C PEN

BRRRRRRR,CCCCCCCC LLL B1091 442-K503TRN 01Jan19 07Jan19 2362000M RISPERIDONE 3MG TAB C/C PEN

BRRRRRRR,CCCCCCCC LLL B1091 442-K503TRN 01Jan19 07Jan19 2238111G GEMFIBROZIL 600MG TAB C/C PEN

BRRRRRRR,CCCCCCCC LLL B1091 442-K5045I3 01Jan19 09Feb19 2538606A CLONAZEPAM 1MG TAB C/C PEN

BRRRRRRR,CCCCCCCC LLL B1091 442-K5045I3 01Jan19 09Feb19 2362000N RISPERIDONE 3MG TAB C/C PEN

CCCCC,SSSSSS JR C0094 442-K504NKW 01Dec18 03Apr19 1288815 LISINOPRIL 40MG TAB C/C PEN

CCCCC,SSSSSS JR C0094 442-K504NKW 01Dec18 06Apr19 2568890 SOFOSBUVIR 400MG TAB C/C PEN

CCCCC,SSSSSS JR C0094 442-K504NKW 01Dec18 06Apr19 2568892 RIBAVIRIN 200MG CAP C/C PEN

DDDDDD,VVVVV GGGGG D7382 442-K302WG0 01Dec19 05Dec19 2387760 METFORMIN HCL 1000MG T C/C PEN

Press RETURN to continue, ‘^’ to exit:

## Multiple Referral Programs Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new report called the Multiple Referral Programs Report \[PRCAC MULT REF RPT\] is created. It will identify those bills that may be referred for debt collection to multiple debt referral programs. In addition, the Multiple Referral Report is added to the DMC Referral Menu, Cross-Servicing Menu, and the TOP Menu.

DMC Referral Menu – Multiple Referral Program Report

Cross-Servicing Menu – Multiple Referral Program Report

TOP Menu – Multiple Referral Program Report

## Veteran Third Party Charge Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran Third-Party Charge Report provides the ability to have a report that will list the third-party bills for a Veteran or payer for a specific time period for review by RUR, Facility Revenue or other entities to ensure appropriate action is taken for the Veteran.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Select AR - Accounts Receivable Menu \<TEST ACCOUNT\> Option:

AR - Accounts Receivable Menu ...

Archive AR Records Menu ...

Billing ...

Clerk's AR Menu ...

Finance AR Manager Menu ...

Supervisor's AR Menu ...

Select AR Master \<TEST ACCOUNT\> Option: Supervisor's AR Menu

Edit/Add 'Bill Resulting From' List

Administrative Cost Adjustment

Form Letter Menu (Edit/Print) ...

Return Bill to Service

Agency Location Code (Deposits)

Archive Menu ...

Bad Debt Report

Cross-Servicing Menu ...

DMC Referral Menu ...

FMS Conversion Menu ...

Link Debtor To Vendor

National Roll-up Report

Purge Unprocessed FMS Document File

Site Parameter Edit ...

TOP Menu ...

Update Rate Types For Auto-audit

Select Supervisor's AR Menu \<TEST ACCOUNT\> Option: DMC Referral Menu

1 90 Day DMC Report

2 DMC Referred Report Print

3 Enter Lesser DMC Withholding Amount

4 Remove Debtor From DMC

5 DMC Debt Validity Report

6 DMC Debt Validity Management Report

7 Rated Disability Eligibility Change Report

8 Enter/Edit DMC Debt Validation

9 Enter/Edit RD Number of Days Report Parameter

10 Enter/Edit DMC Report \# Days for Episodes of Care

11 0-40 Percent SC Change Reconciliation Report

12 First Party Charge IB Cancellation Recon Report

13 10-40% SC Med Care Copay Exempt Chrg Recon Report

14 50-100% SC Exempt Charge Reconciliation Report

15 Catastrophically Disabled Exempt Copay Charge Rpt

16 First Party Veteran Charge Report

17 Pension Exemption Reconciliation Report (PERR)

18 Multiple Referral Programs Report

19 Veteran Third Party Charge Report

Select DMC Referral Menu \<TEST ACCOUNT\> Option: veteran Third Party Charge Report

Select division: ALL//

Start with Date of Service: 010123 (JAN 01, 2023)

End with Date of Service: 123124 (DEC 31, 2024)

Run Report by (P)atient or Pa(Y)er? (P/Y): P// atient

Select patient: ALL//

Display paid claims only(Y/N)? n NO

Display cancelled bills (Y/N)? y YES

Before continuing, please set up your terminal to capture the

detail report data and save the detail report data in a text file

to a local drive. This report may take a while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the file,

please enter '0;256;99999' at the 'DEVICE:' prompt.

DEVICE: 0;256;999999// HOME (CRT)

Veteran Third Party Charges Report^May 14, 2025

Filtered By: No filters; Cancelled bills included

<span id="_Toc198214906" class="anchor"></span>Figure 34: Veteran Third Party Charge Report – Excel format

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/003.png)

# What does the DMC do with Monthly Master File?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the monthly master file arrives in St. Paul, the DMC compares the account information against the compensation and pension mini-master records to see if the Veteran is receiving benefits. If the Veteran is in receipt of benefits and there is an amount available for offset, an account is established in the Centralized Accounts Receivable System (CARS). Messages are also sent to the medical center’s G.DMR mail group listing all Veterans having “inactive benefits,” which means there are no benefits available for offset at this time. The subject of these messages state Patients Deleted from DMC: SEQ. \#.01).

A debtor may not be accepted either because of an “inactive benefit” or a Death notice. In the case of a death notice being received, an individual mail message for each affected debtor will be compiled detailing this information and transmitted to the G.DMR mail group for follow-up by the local site in entering that information into the VISTA database. The Date of Death messages are based upon information found in the VBA Beneficiary Identification Records Locator Subsystem (BIRLS). Be aware of the possibility that these dates are not all correct. Make sure these messages are monitored and reviewed for accuracy prior to making any changes in VistA.

Here is an example of a Death Notice Message:

Subj: Death Notice Received from DMC \[#12345678\] 03 Apr 00 10:44 4 Line

From: AR PACKAGE in ‘DMC’ basket. Page 1

--------------------------------------------------------------------------

DMC has received a death notice for the following patient:

VHAPATIENT,ONE. 000000001 Date of Death: 01/01/00

Please follow up locally to have this information entered into the local VAMC patient file.

21. More than one message may be delivered. The medical center should process these delinquent accounts through the Treasury Offset Program when available.

The DMC can only collect for one medical center at a time. For example, if station 688 Washington, DC, and station 460 Wilmington, DE, both have debts for the same Veteran the DMC will only establish the debt for the medical center with the first referral. These debtors are included on the “Patients Deleted from DMC” messages also. The AR software will continue to set up and transmit a monthly master file for this account if it remains delinquent. After the DMC collects the debt-in-full for the first medical center, the DMC can accept and establish a new account for the debt owed to the next medical center.

A newly established DMC account holds the amount of the referral, the station number, the month and year of the oldest bill, interest, administrative costs and a two-digit number that identifies the type of debt. At this time, a letter is sent to the Veteran stating the DMC will withhold his/her benefit check unless the medical center or CPAC is contacted and alternative arrangements are made to satisfy the debt. The letter informs the Veteran if he/she has any questions regarding the debt or the amount being withheld he/she should contact the CPAC or VA Call Center.

The letter provides the address and telephone number for the medical center. This is the same address and telephone number that is printed on the Consolidated Co-payment Processing Center (CCPC) statements. This letter provides the Veteran with a list of options for satisfying the debt. They are as follows:

1.  Make payment-in-full at this time. Payment must be received within 30 days of the date of the letter or offset will begin.
9.  Take no action and the DMC will withhold the amount of the debt from the monthly VA benefit check. The withholding will begin in 60 days and will continue until the debt is paid in full.
10. If it would be a financial hardship to make payment-in-full or have the full amount of the past due debt deducted from the benefit check at this time, a repayment plan can be established or a lower withholding amount can be negotiated. Requests for these actions must be initiated within 30 days of the date of this letter in order to avoid offset.

If the Post Office returns a debt notification letter as undeliverable, the DMC takes the same position as the TOP. That is, an attempt to contact the debtor was made and even if it was not successful the DMC will still withhold the amount of the debt from the monthly VA benefit check. As stated in the DMC letter, the withholding will begin with the next check due and will continue until the debt is paid in full.

# What Happens if the Veteran Makes Payment-in-Full?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veteran’s payment that reduces the Veteran’s debt to zero is processed in VistA. The following Tuesday, as part of the Accounts Receivable nightly job, VistA looks at every debt in Accounts Receivable file (#430) that has been referred to the DMC to see if there has been a change in the balance to the account. Accounts with changes are transmitted from VistA to a queue at the AITC in a weekly update message. The G.DMX mail group on VistA will also receive this mail message. The subject of the message states WEEKLY UPDATE RECORDS SENT TO DMC ON MM/DD/YYYY. When the DMC processes the weekly update file, the zero dollar balance from VistA will clear the DMC record and a message is sent back to an Accounts Receivable server option at the medical center. Upon receipt of this message, the server option automatically deletes all the DMC data stored in the AR Debtor (#340) and the Accounts Receivable (#430) files. This includes data stored in the following fields:

| Field Number | Field Name                |
|--------------|---------------------------|
| 3.01         | ACCOUNT AT DMC?           |
| 3.02         | DATE SENT TO DMC          |
| 3.03         | DMC DISCOVERY DATE        |
| 3.05         | CURRENT TOTAL AT DMC      |
| 3.06         | CURRENT PRINCIPAL AT DMC  |
| 3.07         | CURRENT INTEREST AT DMC   |
| 3.08         | CURRENT ADMIN AT DMC      |
| 3.09         | LESSER WITHHOLDING AMOUNT |
| 3.1          | SITE DELETION FLAG        |

<span id="_Toc198214953" class="anchor"></span>Table 3: C11 Screen Key Fields

| Field Number | Field Name            |
|--------------|-----------------------|
| 121          | DATE SENT TO DMC      |
| 122          | DMC PRINCIPAL BALANCE |
| 123          | DMC INTEREST BALANCE  |
| 124          | DMC ADMIN BALANCE     |

<span id="_Toc198214954" class="anchor"></span>Table 4: AR Debtor file (#340)

22. If a lesser withholding amount had been established on DMC debt and that debt cleared DMC completely, all DMC data is deleted from VistA, including the original lesser withholding amount. Should other bills for this same Veteran become over 90 days delinquent and meet the DMC referral criteria, new DMC data fields in VistA and new DMC records will be created.  
    The Veteran will receive a new debt letter. This letter provides the Veteran with a list of options for satisfying the debt. This new debt will be established for the full debt balance unless the Veteran requests the AR Technician enter a new lesser withholding amount.

# What Happens when the Veteran Requests a Lesser Withholding Amount?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Veteran contacts the CPAC requesting a reduction in the amount of withholding the CPAC must enter the lesser withholding amount in VistA using the Accounts Receivable option of the same name. Timing is of the essence when entering lesser withholding amounts. Adjustments made prior to DMC initiating offset action from the C&P system, which is done approximately three weeks before the date of the first monthly check to be withheld, are processed automatically.

If an adjustment (lesser withholding amount, waiver, write-off, repayment plan, suspended, or decrease) is entered into VistA during the month before the offset is scheduled to begin, or after offset has already occurred, the CPAC must either call or send an encrypted e-mail message to the DMC staff so they can enter a manual adjustment. The CPAC also needs to inform the Veteran that the allotted time has been exceeded and there is no guarantee the update for the adjustments will take place. If the late data entry cannot occur, the Veteran must be informed of any options. Possible options include a portion of the payment can be refunded (the difference between the agreed upon lesser withholding amount and the offset received) if the amount offset is determined to cause undue financial hardship to the Veteran; and application of entire/partial amount to the debt. The decision to refund is made at the CPAC on a case-by-case basis.

# How to Enter Lesser Withholding Amount in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Veteran contacts the CPAC requesting a reduction in the amount of withholding the CPAC must enter the lesser withholding amount in VistA using the Accounts Receivable option of the same name and may also need to contact DMC staff via phone call or encrypted e-mail.

Select the option called Enter Lesser DMC Withholding Amount from the DMC Referral Menu.

<span id="_Toc198214907" class="anchor"></span>Figure 35: Lesser Withholding Amount

Select DMC Referral Menu Option: Enter Lesser DMC Withholding Amount

Select AR DEBTOR: VAPATIENT,TEST J

Searching for a PATIENT, (pointed-to by DEBTOR)

VAPATIENT,TEST J 1-1-XX 00000XXXX NSC VETERAN

...OK? Yes// YES

LESSER WITHHOLDING AMOUNT: 0.00// 50.00

At the Select AR Debtor prompt, enter the name of the debtor who requested a reduced amount.

The system will then display debtor information to help identify the correct debtor. Press Enter to confirm this selection.

At the LESSER WITHHOLDING AMOUNT prompt, enter the dollar amount that should be deducted monthly until the full amount is collected. If no dollar amount is entered in this field, the entire amount due is collected in one lump sum.

The lesser withholding amount entered here will be displayed on the Profile of Accounts Receivable report.

23. The lesser withholding amount entered in VistA should be the dollar amount negotiated with the Veteran. This amount should be \$25.00 or more. There is no need to alter this amount unless the Veteran has requested the withholding amount be changed (e.g., withhold \$25 rather than \$50).  
    Do *not* change this amount to equal the debt balance if it is less than \$25.00. This is not necessary and only causes more work for everyone involved.

# What Happens when the Veteran Requests a Repayment Plan be Established?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans also have the option to request a repayment plan be established in VistA for each of the outstanding debts. What is the difference between entering a lesser withholding amount and establishing a repayment plan? If there are multiple bills that make up this debt a repayment plan has to be established for each individual Bill number. These plans must be monitored to ensure the Veteran is making payments on time. With the lesser withholding amount, all debts are covered under a single action and the dollars will be sent via Transfer of Disbursing Authority TDA to the station each month.

Some facilities have established a local policy that states all Veterans with debts referred to the DMC will not be considered for repayment plans. These facilities negotiate with Veterans to have lesser withholding amounts entered; if a repayment plan is entered the month before an offset is to occur or after the debt has been set-up in DMC, it will be necessary to either call or send an encrypted e-mail message to DMC to inform them of the change so that a manual adjustment at DMC can be completed.

## How to Set up and Monitor a Repayment Plan in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Repayment Plan (RPP) menu contains options necessary to establish, track and manage repayment plans. Here are instructions on how to set up and view a Repayment Plan. Please see the Accounts Receivable Version 4.5 User Manual - Clerk’s AR Menu Part 1 (URL: [5clerk1_r0515.pdf (va.gov)](https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/5clerk1_r0515.pdf)) for complete information on Repayment Plan creation, editing and follow-up reports.

### Enter a New Repayment Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the user to create a new Repayment Plan. The option prompts for a Debtor name. Once the user confirms the entry, the system will check to see if a plan already exists. If so, the system directs the user to utilize the Edit an Existing Repayment Plan option to make any changes. If no plan exists, the system will display the list of Active bills for the user to select.

After selecting the bills to include, the system will list the bills chosen and prompt the user for confirmation (unless ALL is chosen). After selecting bills to include, the system will prompt for the payment amount—the amount the Debtor will pay each month. The minimum is usually \$25; if a lesser amount is entered, the user will be asked if their Supervisor has approved this monthly payment. If the user answers Yes, the system will save the user ID and enter an Audit Log entry (see Payment Plan Inquiry for the display) to document the approval.

The system will then calculate and display the number of payments along with the Due Date of First Payment. If the number of payments exceeds 36, the user will be asked if their Supervisor has approved the number of monthly payments. If the user answers Yes, the system will then save the user ID and enter an Audit Log entry. A summary of the created Repayment Plan is then displayed. If the number of calculated payments exceeds 60 (the maximum limit), a warning message is displayed, and the user is prompted to reenter the payment amount. Otherwise, the Repayment Plan is established. The following is an example where the Monthly Payment Amount and Number of Payments are within guidelines:

<span id="_Toc198214908" class="anchor"></span>Figure 36: Enter a New Repayment Plan

24. Do <u>NOT</u> place these bills in Suspended Status.

> Select Repayment Plan Menu \<TEST ACCOUNT\> Option: Enter a New Repayment Plan

> Select DEBTOR NAME: DDDDDDDDD,SAUL LAWRENCE

> Searching for a PATIENT, (pointed-to by DEBTOR)

> DDDDDDDDD,SAUL LAWRENCE 7-25-39 XXXXXXXXX NO NSC VETERAN

> Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

> ...OK? Yes// \<RET\> (Yes)

> Is this the correct Debtor? (Y/N) ? YES// \<RET\>

> This Debtor does not have a Repayment Plan

> List of Active Bills:

> DATE OF AMOUNT

> No. BILL NO. AR CATEGORY SERVICE STATUS OWED (\$)

> -------------------------------------------------------------------------------

> 1 442-K505Q3G C (MEANS TEST) 07-10-20 ACTIVE \$ 15.00

> 2 442-K505QGI RX CO-PAYMENT/NSC VET 07-13-20 ACTIVE \$ 45.00

> 3 442-K505TL1 RX CO-PAYMENT/NSC VET 07-21-20 ACTIVE \$ 27.00

> 4 442-K5060RN CCN INPT 08-23-20 ACTIVE \$ 1062.10

> ===============================================================================

> TOTAL OWED: \$ 1149.10

> Select bills using the following formats: (A)ll or (N)one or 1,2,3 and/or 1-3

> Choose Bills to Add to Repayment Plan: : ALL// \<RET\>

> Total Amount chosen is \$ 1149.10

> Is this correct? (Y/N) ? YES// \<RET\>

> Allow bills to be auto-added to the repayment plan? (Y/N)? NO// y YES

> Monthly Payment Amount: 50

> Number of Payments will be 23

> Summary of the Created Repayment Plan for AR Debtor: DDDDDDDDD,SAUL LAWRENCE

> -------------------------------------------------------------------------------

> Monthly Repayment Amount: \$50.00 Number of Payments: 23

> Date Plan Created: 1/13/21 Due Date of First Payment: 2/28/21

> Total Amount of Bills in Plan: \$1149.10

> -------------------------------------------------------------------------------

> Is this correct? (Y/N) ? YES// \<RET\>

> The Repayment Plan 442-RPP-01-000052 has been established.

> Type \<Enter\> to continue or ‘^’ to exit: \<RET\>

> Select DEBTOR NAME: \<RET\>

> Enter a New Repayment Plan

> Add New Bill to a Repayment Plan

> Edit Existing Repayment Plan

> Grant Forbearance to a Plan

> RPI Repayment Plan Inquiry

> STR Repayment Plan Status Report

> DEL Repayment Plan Delinquent Letter Report

> DEF Repayment Plan Default Letter Report

> TLR Repayment Plan Term Length Exceeded Report

> Select Repayment Plan Menu \<TEST ACCOUNT\> Option:

### Repayment Plan Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Repayment Plan Inquiry option will provide the user with a succinct report on a particular Repayment Plan. The user may enter the RPP Number or the Debtor name. The system will ask the user to confirm the number or name, and will then provide the output, which can be printed or displayed on-screen.

The output includes the Debtor’s demographics, Plan ID number, Status and Status date. Plan information such as the Current balance, Original and Total amounts owed, Repayment amount, the Number of payments remaining, and the Original and Total number of payments are also included. The report also includes the list of bills associated with the Plan, the schedule of payments, a list of Forbearances and a record of payments made. In addition, an Audit Log of adjustments to the Plan are listed. Information includes dates, user names, types, and standard comments related to plan adjustments made and supervisor approvals.

<span id="_Toc198214909" class="anchor"></span>Figure 37: Repayment Plan Inquiry

> Select Repayment Plan Menu \<TEST ACCOUNT\> Option: Repayment Plan Inquiry

> Select Repayment Plan: CCCCCCCC,EM

> Searching for a PATIENT, (pointed-to by DEBTOR)

> Doe, Jon 0-00-00 XXXXXXXXX NO NSC VETERAN

> Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

> ...OK? Yes// \<RET\> (Yes) 442-RPP-01-000043 NEW 02/15/2021

> DEVICE: \<enter printer device or return to display on-screen\>

> Debtor: Doe, Jon SSN/TIN: XXXXXXXXX DOB: MAY 29,1946

> Address: PO BOX 76 , GUERNSEY, WY 000000000

> Phone: (999)999-9999

> Plan \#: 442-RPP-01-000043 Status: NEW Last status date: 02/15/2021

> Current balance: \$0.0 Number of payments remaining: 53

> Orig amount owed: \$0.0 Original number of payments: 53

> Total amount owed: \$0.0 Total number of payments: 53

> Repayment amount: \$0.00 Auto-add New Bills: YES

> Plan date: 02/15/2021 First Payment Due Date: 04/28/2021

> Type \<Enter\> to continue or ‘^’ to exit:

> List of Bills in Plan

> -------------------------------------------------------------------------------

> Bill No. Bill Status Category Current Balance

> -------------------------------------------------------------------------------

> 442-K505CCA ACTIVE C (MEANS TEST) \$00.0

> 442-K505FKI ACTIVE C (MEANS TEST) \$0.0

> 442-K5061DV ACTIVE C (MEANS TEST) \$0.00

> 442-K5061DW ACTIVE C (MEANS TEST) \$0.00

> 442-K902WR0 ACTIVE RX CO-PAYMENT/ \$0.00

> 442-K902WR1 ACTIVE RX CO-PAYMENT/ \$0.00

> 442-K902WR2 ACTIVE RX CO-PAYMENT/ \$0.00

> 442-K902WR3 ACTIVE RX CO-PAYMENT/ \$0.00

> -------------------------------------------------------------------------------

> Plan Schedule

> -------------------------------------------------------------------------------

> Due Date Paid? Due Date Paid? Due Date Paid?

> -------------------------------------------------------------------------------

> 04/28/2021 N 05/28/2021 N 06/28/2021 N

> 07/28/2021 N 08/28/2021 N 09/28/2021 N

> 10/28/2021 N 11/28/2021 N 12/28/2021 N

> 01/28/2022 N 02/28/2022 N 03/28/2022 N

> 04/28/2022 N 05/28/2022 N 06/28/2022 N

> 07/28/2022 N 08/28/2022 N 09/28/2022 N

> 10/28/2022 N 11/28/2022 N 12/28/2022 N

> 01/28/2023 N 02/28/2023 N 03/28/2023 N

> 04/28/2023 N 05/28/2023 N 06/28/2023 N

> 07/28/2023 N 08/28/2023 N 09/28/2023 N

> 10/28/2023 N 11/28/2023 N 12/28/2023 N

> 01/28/2024 N 02/28/2024 N 03/28/2024 N

> 04/28/2024 N 05/28/2024 N 06/28/2024 N

> 07/28/2024 N 08/28/2024 N 09/28/2024 N

> 10/28/2024 N 11/28/2024 N 12/28/2024 N

> 01/28/2025 N 02/28/2025 N 03/28/2025 N

> 04/28/2025 N 05/28/2025 N 06/28/2025 N

> 07/28/2025 N 08/28/2025 N

> Forbearances

> -------------------------------------------------------------------------------

> Date Month/Year Forborne Month/Year Added

> -------------------------------------------------------------------------------

> Payments Applied to Plan

> -------------------------------------------------------------------------------

> Date Amount Date Amount

> -------------------------------------------------------------------------------

> Audit Log

> -------------------------------------------------------------------------------

> Date User Type Comment

> -------------------------------------------------------------------------------

> 02/15/2021 DDDDDDDDD,JJJJ A NEW NEW PLAN

> 02/15/2021 DDDDDDDDD,JJJJ A NEW SUPV APPR \<\$25

> 02/15/2021 DDDDDDDDD,JJJJ A NEW SUPV APPR \>36 MTHS

> 02/18/2021 DDDDDDDDD,JJJJ A EDIT TERMS ADJUSTMENT

> 02/18/2021 DDDDDDDDD,JJJJ A NEW SUPV APPR \<\$25

> 02/18/2021 DDDDDDDDD,JJJJ A NEW SUPV APPR \>36 MTHS

> End of Inquiry

> Press \<return\> to continue \<RET\>

> Enter a New Repayment Plan

> Add New Bill to a Repayment Plan

> Edit Existing Repayment Plan

> Grant Forbearance to a Plan

> RPI Repayment Plan Inquiry

> STR Repayment Plan Status Report

> DEL Repayment Plan Delinquent Letter Report

> DEF Repayment Plan Default Letter Report

> TLR Repayment Plan Term Length Exceeded Report

> Select Repayment Plan Menu \<TEST ACCOUNT\> Option:

## The Debt is Not Resolved. What Happens Next?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the patient does not continue to make payments and defaults, the repayment plan should be reviewed and procedures outlined in CPAC policy should be followed.

The DMC establishes the withholding (offset) in the C&P system for the amount of the debt in CARS approximately 15 days prior to the actual offset (around the 15th of the month preceding the offset). A three-digit DMC diary code is assigned to this debt and the repayment information is entered in the system withholding the full benefit check or debt amount, whichever is less, unless the CPAC has established a lesser withholding amount.

The three-digit DMC Diary Code of 090 is used when a debt is first established in CARS. This code changes when other activities occur with this account. See Appendix C to see a listing of the DMC Diary Codes.

Once DMC collects the amount established for offset in the C&P system the withholding stops automatically. Any increases received from VistA prior to the collection of the total amount established for offset in the C&P system will immediately be added to the total amount to be offset. However, if the increase to the debt is received at DMC after the amount of offset established for a previously referred debt has been collected, the DMC changes the diary code, deletes the code showing a letter had been sent previously, and treats the remaining debt as a new referral from the CPAC.

25. If a lesser withholding amount had been established on DMC debt and that debt cleared DMC completely, all DMC data is deleted from VistA, including the original lesser withholding amount. Should other bills for this same Veteran become over 90 days delinquent and meet the DMC referral criteria, new DMC data fields in VistA and new DMC records will be created.  
    The Veteran will receive a new debt letter. This letter provides the Veteran with a list of options for satisfying the debt. This new debt will be established for the full debt balance unless the Veteran requests the AR Technician enter a new lesser withholding amount.

# How does the VistA Software Determine which Records get sent to the DMC in the Weekly Update Message?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Software looks only at bills currently referred to DMC.
2.  Checks AR Debtor file for Lesser Withholding Amount. Sends that info to DMC if it exists.
3.  Checks Site Deletion Flag field in the AR Debtor file (#340). If set to YES, sends zero to DMC and sends “Deletion of Debtor from DMC” mail message to G.DMX mail group.
4.  Checks if bill is now on repayment plan. If there is a repayment plan on a specific bill, it is not included in balance transmitted to DMC.
5.  Checks to see if bill in active status has a zero principal balance, but has a balance outstanding in either the interest or administrative charges fields. Mail message sent to G.DMR mail group to enter adjustment for this bill.
6.  Total Principal + Interest + Administrative Cost for referred bills is different than the dollar amounts listed in the corresponding DMC fields of file \#340. If there is no change, nothing is sent to DMC.
26. A debt may meet the referral criteria listed above but the account will not be transmitted to DMC if the debtor’s address information is <u>unknown</u> or <u>incorrect</u>. See the Debtor address section for more information on how to enter or edit address information.

# What does the DMC do with Weekly Update File?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The weekly update information overlays the information in the CARS system. The update, which is transmitted from VistA to a queue at the AITC on Tuesday of each week, is loaded into CARS on Thursday of the same week. The DMC staff has access to a CAROLS screen (C14) that shows when the update was received, if it was a debit or credit, and the dollar amount of the update. This is how the DMC can verify if there is an update problem when the CPAC calls with questions.

If the update from the CPAC doesn’t reduce the debt in CARS, the DMC continues to collect on the debt until the AR balance at DMC is reduced to zero. In these cases, the CPAC should contact the DMC by Outlook mail message to redacted and request the DMC stop collection action until the CPAC researches why the debt was not reduced (i.e., System problems prevented the transmission of the VistA weekly update message).

27. Another way a debt may not be reduced in CARS is if the CPAC staff changes a DMC referred bill status to anything other than “Active”, including decrease adjustments, write-offs, waivers, etc. Bills must be in an “Active” status to be included in the DMC weekly update.

CPAC staff should take great care when trying to resolve questions about a patient’s DMC debt. Placing DMC bills in a suspended status tells the system to ignore this account when creating the DMC weekly update file. This means that <u>no information</u> (not even a zero transaction) will be sent to the DMC. Either a call or encrypted e-mail message should be sent to DMC staff to inform them that bill(s) have been suspended pending administrative outcome.

CPACs should check the DMC transmission messages carefully to ensure that the proper timeframe has passed before contacting the DMC. The Weekly Update transmission sent from the CPAC on Tuesday will not update the DMC database until Thursday.

# What Happens when the Monthly Offset Occurs?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Funds received from the monthly offset are transferred to the DMC before the monthly benefit checks are sent to Veterans. Offset money is usually received sometime during the last week of the month. The actual processing date varies from month-to-month based on the number of days in the month and if there are holidays in that month. The DMC creates a 1017G form that lists the Veterans and amount of offset for each medical center. This information is e-mailed to the Finance Officer and the Revenue Coordinator at each medical center/CPAC and to the AITC. The offset funds are sent to the medical centers suspense account within a few days from that date.

After the Monthly Update file from the CPACs is processed by DMC, any record in an offset status with a debt balance of less than \$25.00 is deleted from CARS. Any offset in process (BDN shows a remaining 68C balance) will be continued and the funds transferred to VHA until the debt balance has been collected.

Once the VistA mail messages with the subject Patients Deleted from DMC are received, it is a good idea to print the report called DMC Referred Report Print for all patients. This report provides an accurate, up-to-date listing that is helpful when reviewing DMC accounts.

Medical centers experiencing problems receiving the funds on their suspense list they should wait approximately three days from the date they get the offset listing, then contact REDACTED at the FSC Austin at (512) 460-5460.

Medical centers with questions concerning DMC activities should contact Business Operations at the Chief Business Office.

# How to Process a DMC Payment in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All payment processing occurs using options on the Agent Cashier menu.

<span id="_Toc198214910" class="anchor"></span>Figure 38: Process a DMC Payment

Select Agent Cashier Menu Option: RP Receipt Processing

Select RECEIPT (or add a new one): 0401DMC

Are you adding ‘0401DMC’ as a new AR BATCH PAYMENT (the 29TH)? No// YES

(Yes) AR BATCH PAYMENT TYPE OF PAYMENT: TDA PAYMENT

AR BATCH PAYMENT DEPOSIT TICKET: 123456 04-01-00 TECH,ACCT REC \$0.00 OPEN

At the Select Agent Cashier Menu Option: prompt, type RP for Receipt Processing.

At the Select RECEIPT: prompt, enter the receipt number for these payments.

Hint: Use the letters DMC in the receipt number. This makes it easy to identify these payments as being collections from DMC when using other menu options.

At the Are you adding ‘0401DMC’ as a new AR BATCH PAYMENT: NO// prompt, type YES and press Enter to confirm this action.

At the AR BATCH PAYMENT TYPE OF PAYMENT: prompt, type TDA, for TDA Payment and press Enter.

At the AR BATCH PAYMENT DEPOSIT TICKET: prompt, enter the open Deposit Ticket number and press Enter. For this example, the number used was 123456.

<span id="_Toc198214911" class="anchor"></span>Figure 39: DMC Payment Processing

<table>
<caption><p><span id="_Toc198214955" class="anchor"></span>Table 5: AR Debtor File Fields Set by DMC Referral Menu Option</p></caption>
<colgroup>
<col style="width: 83%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Receipt Profile Apr 01, 2000 11:24:50 Page:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receipt #: 0401DMC Type of Payment: TDA PAYMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Deposit #: 123456 Receipt Status: OPEN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong># Account Pay Date By Pay Amt</strong></p>
</blockquote></td>
<td><strong>Proc Amt</strong></td>
</tr>
<tr class="odd">
<td>-------­</td>
<td>-------­</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 0.00</p>
</blockquote></td>
<td>0.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong><u>Receipt History</u></strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Opened By: TECH,ACCT REC Date/Time Opened: APR 19, 2000 11:24</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Last Edit By: Date/Time Last Edit:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Processed By: Date/Time Processed:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Enter ?? for more actions</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CP Cancel Payment CU Customize EA Exit Action</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MP Move Payment ER Edit Receipt</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Select Action: Quit// NP New Payment</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc198214955" class="anchor"></span>Table 5: AR Debtor File Fields Set by DMC Referral Menu Option

The Receipt Profile screen appears. At the Select Action: Quit// prompt, type NP for New Payment.

<span id="_Toc198214912" class="anchor"></span>Figure 40: Receipt Profile

Type of payment: TDA PAYMENT

Adding a NEW payment transaction: \# 1

PATIENT NAME OR BILL NUMBER: VAPATIENT,TEST D 1-1-XX 000000001 NO

NON-SERVICE CONNECTED

Enrollment Priority: GROUP 4 Category: IN PROCESS End Date:

Amount Owed: \$663.61

PAYMENT AMOUNT: 100.00

DATE OF PAYMENT: APR 02,2000// 040100

The system then steps through the prompts that must be answered to complete this TDA payment.

At the PATIENT NAME OR BILL NUMBER: prompt, enter the name of the patient from the TDA form. The system shows information to help the user verify this is the correct debtor.

At the PAYMENT AMOUNT: prompt, enter the dollar amount from the TDA form.

At the DATE OF PAYMENT: prompt, the system will default to the current date. Be sure to enter the date on the TDA form.<span id="_Toc1557560" class="anchor"></span>

Figure 41: Receipt Profile Payment

Receipt Profile Apr 01, 2000 11:25:20 Page: 1 of 1

Receipt \#: 0401DMC Type of Payment: TDA PAYMENT

Deposit \#: 123456 Receipt Status: OPEN

FMS Document: NOTSENT FMS Doc Status: NOT ENTERED

\# Account Pay Date By Pay Amt Proc Amt

-------­ -------­

1 VAPATIENT,TEST D 04/01/00 ART 100.00 0.00

-------­ -------­

TOTAL DOLLARS FOR RECEIPT 100.00 0.00

Receipt History

Opened By: TECH,ACCT REC Date/Time Opened: APR 01, 2000 11:24 Last  
Edit By: TECH,ACCT REC Date/Time Last Edit: APR 01, 2000 11:24  
Processed By: Date/Time Processed:

FMS Cash Receipt Document: NOT SENT Status: NOT ENTERED

Transaction \#1 has been ADDED.

Enter ?? for more actions

NP New Payment AP Account Profile PR Process Receipt

EP Edit Payment RR Reprint Receipt 21 (215 Report)

CP Cancel Payment CU Customize EA Exit Action

MP Move Payment ER Edit Receipt

Select Action: Quit// NP New Payment

The Receipt Profile screen appears again, this time showing the payment that was just entered.

At the Select Action: Quit// prompt, type NP for New Payment and repeat these steps until every TDA payment has been processed.

# How to Remove a Debtor from DMC Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DMC Referral menu contains an option that allows the CPAC to remove a debtor from DMC referral. This option should be used on a <u>very limited basis</u> and only when the CPAC determines that no collection should be made from a debtor’s benefit check.

One possible reason to use this option might be that a Veteran’s account was referred to the DMC at the same time the Veteran was disputing these bills were related to treatment for a service connected condition. If the bills were not put into a suspended status when the Veteran first questioned the bills, the account would have been referred to the DMC. To stop DMC from making the collection, they must receive a \$0 (zero) transaction.

28. If the field “Account at DMC” in the AR Debtor file (340) is blank, the debtor name will not be available for selection.

Select the option called Remove Debtor from DMC located on the DMC Referral Menu.

<span id="_Toc198214914" class="anchor"></span>Figure 42: Remove Debtor from DMC

Select DMC Referral Menu Option: Remove Debtor From DMC

Deletion of Debtor From DMC

Enter Debtor To Be Removed From DMC: VAPATIENT,TEST O 1-1-XX 00000XXXX

NSC VETERAN

...OK? Yes// YES

Are you sure you wish to delete this debtor from DMC? NO// YES

Enter Debtor To Be Removed From DMC:

At the Enter Debtor To Be Removed from DMC: prompt, enter the name of the debtor to be removed.

The system will then display debtor information to help identify the correct debtor. Press the Enter key to confirm this selection.

At the Are you sure you wish to delete this debtor from DMC? NO// prompt, type YES and press Enter to confirm this action.

On the Wednesday after using this option, check the Weekly Update mail message to make sure the debtor entered is listed on the message and has \$0.00 listed in all the dollar columns.

<span id="_Toc198214915" class="anchor"></span>Figure 43: Weekly updates message

Subj: WEEKLY UPDATE RECORDS SENT TO DMC ON 01/04/00 \[#99371700\]

04 Jan 00 01:32 13 lines

From: AR PACKAGE In ‘DMC’ basket. Page 1

-------------------------------------------------------------------------------

Name Last4 Principle Interest Admin Total

---- ----- --------- -------- ----- -----

VAPATIENT,TEST O XXXX 0.00 0.00 0.00 0.00

VAPATIENT,TEST M YYYY 5.00 0.00 0.00 5.00

# Other DMC Correspondence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## 1017G Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1017G forms are sent anytime the DMC needs to send funds to the medical center. This form is also generated when a debt has been established in the C&P system and the Veteran receives a “retroactive” payment. Instead of sending the funds to the Veteran we would apply them to any debts he/she may have. Retroactive payments are benefits for the Veteran after a suspension has been lifted or if benefits have been increased. For example, a Veteran was originally paid \$400 a month from May 1, 1998 to April 30, 1999 for a total of \$4,800. The Veterans requested a review of his claim for an increase. The VBA Adjudicator reviewed the benefits and ruled they be increased by \$100 per month for that time period. The Veteran is entitled to a retroactive pay of \$1,200. VA policy states that if there is a debt established in any system for this Veteran any retroactive payment must be applied to that debt. A 1017 form is also generated and sent to the medical center when a Veteran mistakenly mails their payment directly to the DMC. The DMC deposits the funds and informs the site of the payment.

## Death Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMC’s IRM generates a report at End of Month (EOM) of all MCCR accounts where a CARS debt in a “Death Diary” also exists. This report is used by Accounting to determine whether funds offset and forwarded to VHA have to be recouped, and if so, notifies the station.

If funds were transferred to the medical center for the month in which death occurred, DMC will fax a request to the individual station requesting return of the monies. This fax notification will provide the Veterans name, social security, date of death in addition to the date, amount, and Journal voucher number that funds were originally transferred on. Included with the fax, is a Journal Voucher (1017G) that can be completed by the station that has the pertinent information completed by DMC to ensure accurate processing when funds are returned. The station should fax the completed Journal Voucher to 612 970-5687 and place the funds in suspense under station 389 36001200 fund 3875.

Death information from the monthly update should be verified. Some facilities have identified fraudulent usage of a Veteran’s SSN by investigating DMC death notifications. Medical centers that know the Veteran is not deceased, should contact the nearest VBA Regional Office. The VBA Regional Office of Jurisdiction enters death notification information in BIRLS and history has shown that it is not always correct. Do not contact the DMC staff members if a death notification is not correct. DMC staff cannot change this information in BIRLS. Again, sites should work with their respective VBA Regional Office to resolve these matters. If the account is still receiving some type of benefit, funds will be deducted from the benefit.

## Waivers Granted on VBA Benefit Accounts Managed by the DMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Veteran has a CPAC debt in benefit offset status at the DMC <u>and</u> a DMC debt, a waiver is granted on the DMC debt with a refund due the debtor, the DMC will withhold all or part of the refund to clear the debt.

The DMC notifies the Veteran that all or part of the refund was applied to a debt. The DMC advises the debtor to contact their local Business Office regarding any questions about this indebtedness. The funds are sent to the medical center via a 1017G form and an Outlook mail message is sent to the Revenue Coordinator to advise them that funds are being forwarded to their facility.

## Miscellaneous Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail received for the medical centers is forwarded to the appropriate medical center. Bankruptcy documents received where a medical center debt can be identified are forwarded also. The medical center should suspend collection action on the account and forward the bankruptcy information, along with any other pertinent data, to their local Regional Counsel for further action.

# DMC Timelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMC timelines are critical. If transactions are not processed in a timely manner, they will have a serious impact upon a Veteran’s benefit check. To illustrate this point, we will follow a debt as it goes through the DMC referral process. Please understand that the dates listed here apply to December 1999 through May 2000 only. DMC processing dates vary a few days from month-to-month based on the processing cycles of the Compensation & Pension System.

This example will step through the referral activities associated with a patient named VATEST, PATIENT A. Mr. VATEST had a debt with the Wilmington VAMC for \$475.00 that met all of the DMC referral criteria.

<span id="_Toc198214916" class="anchor"></span>Figure 44: Example of Date Master Record is Transmitted

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/004.png)

On <u>December 30, 1999</u>, the last Thursday of the month, Mr. VATEST’s debt was included in the Master Record sent to DMC (via AITC).

<span id="_Toc198214917" class="anchor"></span>Figure 45: Example of Date Account Set Up at DMC and Debt Letter Mailed

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/005.png)

On <u>January 3rd</u>, the DMC received the Master Record file from the AITC. The DMC checked the C&P mini-master records and found that Mr. VATEST is receiving benefits from VBA. The DMC established his account. A Debt letter was sent to Mr. VATEST and the 60-day clock, the clock that establishes when the offset will be set up at the DMC, started.

<span id="_Toc198214918" class="anchor"></span>Figure 46: Example of Due Date to Pay Debt in Full

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/006.png)

<u>February 6th</u> was the due date for Mr. VATEST to contact the Wilmington VAMC to pay his debt-in-full; negotiate a lesser withholding amount; or agree to a repayment plan. (This was 30- days from the DMC Letter date.) Mr. VATEST did <u>not</u> contact the medical center.

<span id="_Toc198214919" class="anchor"></span>Figure 47: Example of Multiple Calendar Dates for Actions Taken On  
or Related to the Debtor’s Account

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/007.png)

On <u>May 6th</u>, 60-days had passed since DMC letter sent to the Veteran.

On <u>May 10th</u>, the full amount of this debt was set up in the C&P system. This action usually occurs sometime between the 10th and 15th of the month.

On <u>May 15th</u>, Mr. VATEST contacted the Wilmington VAMC and requested a lesser withholding amount of \$25.00. The AR Technician entered this information into VistA.

On Tuesday, <u>May 21st</u>, two events occurred:

- Mr. VATEST ‘s lesser withholding amount was included in the weekly update message the Wilmington VAMC transmitted to the <u>AITC</u>. Remember, VistA transmissions are sent to a queue at the AITC and then to the DMC. There is usually a 24 to 48 hour delay between the time the message is sent from the medical center and when data is loaded into the DMC database.
- This is the last day the C&P system accepted any changes to the offset amount before the April 1, 2000 checks were issued. <u>Any manual adjustments DMC entered through the</u> <u>TARGET system after this date will not take effect until next month</u>.

On <u>May 23rd</u>, the DMC received the weekly update files from the AITC. (It was too late to process the automated request for a lesser withholding amount for Mr. VATEST’s check dated April 1, 2000.)

On <u>May 24th</u>, the May offset money was received at the DMC. 1017G forms listing Veterans and offset amounts were created and sent to medical centers and the AITC. Offset Vouchers are sent to medical centers before checks are sent to Veterans.

On <u>May 31st</u>, Veteran benefits checks were mailed to the Veteran or funds were deposited into the patient’s bank account. Mr. VATEST had the <u>full debt amount</u> deducted from his benefit check.

> Was there a way to process the lesser withholding amount before the offset occurred?

> YES! Update information needs to be entered into VistA in time for the automated process to work, or the AR Technician needs to contact the DMC prior to their manual adjustment cutoff date.

> Contacting the DMC after the automated processing period is a station decision. The Veteran is given ample time to respond to the offset notice. If a station does request a manual adjustment, they need to inform the Veteran that the allotted time has been exceeded and there is no guarantee the update for the lesser withholding amount will take place. The Veteran must be informed what the options are if the late data entry cannot occur (i.e., the entire offset is applied to the debt).

Anytime a medical center receives a request to adjust an account, the information <u>must</u> be entered in VistA. Adjustments made the last week of the month prior to the offset month, will be processed automatically. If an adjustment is being made the same month as the offset, the information must be made in VistA and the DMC must be contacted by phone or e-mail.

A report is generated at DMC of accounts in an offset status (Diary Code 098) where the offset amount is being changed by VHA when the MCCR Weekly Update file is processed. If the report contains data, it is provided to DMC’s Operations Division for review to determine whether the BDN monthly offset amount should be changed.

# CAROLS – Centralized Accounts Receivable On‑Line System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Centralized Accounts Receivable On-Line System (CAROLS) reflects all accounts receivable under the jurisdiction of the Debt Management Center (DMC) with the exception of Chapter 30 and Chapter 1606 debts. Types of debts include Education, Compensation, Pension, Loan Guaranty, Education Loans, and medical care debts referred for offset against C&P benefits.

CAROLS records for medical center accounts are updated once a week. Inquiries must be made for individual Veterans. There are no facility reports available. The system permits inquiry from medical centers to the CARS database that resides at the Austin Information Technology Center. It is designed to retrieve and display CARS master record data.

Facilities may request that one or two individuals receive access to CAROLS for inquiry purposes only. The Revenue Coordinator must fill out a Carols access request form (8824a) and send an electronic copy to REDACTED via Outlook mail or mail a paper copy to the following address:

ATTN: REDACTED  
VADMC  
PO Box 11930  
St. Paul, MN 55111-1930

Please mark the envelope Personal – Do Not Open in Mailroom. REDACTED will forward the form to the National Service Center (NSC). The NSC will contact the employee and assign a system password. If the employee does not hear from the NSC within 10 working days, they should contact the NSC at 612-970-5220. The caller must know the date the request for access was submitted.

CAROLS Access Request form instructions:

1.  Fill in the employee’s name.
2.  Leave blank.
3.  Type in the room number.
4.  Type in the employee’s telephone number.
5.  Type in the station number.
6.  Type in the employee’s routing number.
7.  If the employee is a Veteran, type in their file number. If the employee is not a Veteran, leave blank.
8.  Type in the employee’s job title.
9.  Put an X in the appropriate box.
10. Leave blank.
11. This box is already checked for you. Sensitive access is not given.
12. Leave blank.
13. Leave blank.
14. \(a\) Type in employee’s supervisor and their title. The supervisor should then sign above their name. (b) Enter the date it is signed by the supervisor.
15. Type in REDACTED, Security Officer. (15a.) Leave blank.
16. Leave blank.

<span id="_Hlk185860037" class="anchor"></span>Figure 48: Example of Carols Access Request Form (1 of 2)

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/008.png)

<span id="_Toc198214921" class="anchor"></span>Figure 49: Example of Carols Access Request Form (1 of 2)

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/009.png)

## Instructions for Using the CAROLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Contact your IRM/IT staff and request the communications software needed to connect to VACCESS. This is the same system individuals in Fiscal use to access FMS and payroll staff uses to access OLDE data in Austin.
11. Once connected, the screen should read Welcome to VACCESS time sharing at Austin. On this screen, press the PF11 key or type K and press Enter. The screen should show PRD 461 “COMPLETE System Logon.”
12. Enter your COMPLETE user ID. The user ID consists of the letter “r,” the three numbers of the regional office closest to your location, the letter “c,” and then a number from 0 through 10. Example: r123c1, (where 123 is the regional office number). If you are not sure which regional office number to use, please contact REDACTED.
13. After you type in your user ID, press Enter and the system will take you to Screen C00. (Screen numbers C00, C01 & C02 appear in the upper right corner, while screen number C11 and higher appear on the top center line of the screen.)
14. CAROLS screen C00 requires that you enter the logon password provided by the NSC. Then press Enter.
15. Screen C01, CARS System Menu will appear. Since medical centers have inquiry access only, select number 1 and press Enter. This will take you to the C02 screen.
16. Press the tab key twice to navigate down to the file number/SSN field and enter the file number or SSN of the case you are looking for. (Dashes and/or spaces are not allowed in this field.) Users do not have to re-enter their password on this screen.
17. After your selection is displayed, navigate from screen to screen by pressing Enter or type the screen number you wish to display. To exit from the record, type in C02 (C-zero-two) at the NEXT SCREEN -TRX field to return to the C02 screen for your next selection.
18. When you are done with CAROLS, click on the X box in the upper right-hand corner to close CAROLS.

For security reasons, there are time limits on CAROLS displays. If there is no activity within an established period, CAROLS will time out and you will have to log back into the system. To do this, press Enter and you will back at the C00 screen.

### CAROLS Screen C11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc198214922" class="anchor"></span>Figure 50: CAROLS Screen

03-23-2000 C11

FILE NUMBER PY DED STUB DC DC DATE DC INS DT TOTAL AR DISC RO

SSN or C# 00 81B VAPATIEN 090 05-30-2000 03-13-2000 60.70 04-1998 629

ORIG NOTIF DATE INT COMP DT 06-30-1999 *REPAY IND (10) 1 EMPLOYEE*

ORIG AR 77.42 INT RATE 0.00 *REPAY DT (11)09-13-1999* IND 0

COURT COSTS ORIG AR PRIN 57.23 *REPAY AMT(12)* DUTY 0000

COURT COSTS CURR INT ACCRUED 2.97 TOT PAID

MARSH FEES ORIG W-O HINES IND 7 CRA IND 0

MARSH FEES CURR PD TD HINES TP E

ADMIN COST 0.50 PD CY *HINES RC(13)1*

IRS REFUND AMT

CARS LAST ACT HINES LAST ACT INDICATORS SPECIAL IND *SSN (14)XXX-XX-XXXX*

TRX DATE TRX DATE CY PAY-ADD 2 1 41E 0 REF NO

500 02-29-2000 INTEREST 0 2 COLL-RT 0 DATE BIRTH 01-01-19XX

01A 03-09-2000 ADM COST 0 3 FRAUD 0 DATE DEATH

02E 03-09-2000 MULT AR 1 4 IRS TAX 0 ST-LIM DT 09-2005

500 03-09-2000 OFFST BEN 0 5 AUDIT 0 USER INFORMATION

02A 03-13-2000 COOB 0 6 PCA 0

01A 03-23-2000 COOB-ADD 0 7 JUDGMNT 0 (15)

02E 03-23-2000 HM# XXX-XXX-XXXX MULTI 0 8 DDEFT 0

500 03-23-2000 WK# CRRPT 0 9 CHAP 30 0 VHA# (XXX) XXX-XXXX

POA 10 JUD FOR 0 TOTAL AR 60.70

The C11 screen has the majority of the information needed to identify the account status in the DMC process. The key fields for the medical center include:

<table>
<caption><p><span id="_Toc198214956" class="anchor"></span>Table 6: Accounts Receivable file (#430)</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FILE NUMBER</td>
<td>Either the Veteran’s file number/claim number or social security number.</td>
</tr>
<tr class="even">
<td>PY 00</td>
<td>Indicates that this is a Veteran’s account. Medical debt will always be payee 00.</td>
</tr>
<tr class="odd">
<td>DED81</td>
<td>Indicates that this is a medical center debt.</td>
</tr>
<tr class="even">
<td>STUB</td>
<td>The first and middle initial and first five letters of the last name.</td>
</tr>
<tr class="odd">
<td>DC</td>
<td>Diary Code indicates the DMC status of this account. (i.e., 090, 091, 092, 093, 097 or 098) *See Appendix C</td>
</tr>
<tr class="even">
<td>DC DATE</td>
<td>Date the diary comes up to be worked (follow-up date)</td>
</tr>
<tr class="odd">
<td>DC INS DT</td>
<td>Date the diary code was input.</td>
</tr>
<tr class="even">
<td>TOTAL AR</td>
<td>(top of screen) lists the balance the DMC is currently collecting</td>
</tr>
<tr class="odd">
<td>DISC</td>
<td>Date of the oldest bill referred.</td>
</tr>
<tr class="even">
<td>RO</td>
<td>Station number of the medical center for the debt being collected.</td>
</tr>
<tr class="odd">
<td>REPAY IND (,10) REPAY DT (11)<br />
REPAY AMT (12)</td>
<td>Amount DMC will offset from Veteran check</td>
</tr>
<tr class="even">
<td>HINES RC (13)</td>
<td><p>C&amp;P (Hines) reason code is the reason for the debt. There will either be one or two digits in this field depending on the reason sent by the center for the debt.</p>
<p>*See Appendix D</p></td>
</tr>
<tr class="odd">
<td>SSN (14)</td>
<td>Veteran’s social security number, which could differ from his claim number.</td>
</tr>
<tr class="even">
<td>USER INFORMATION (15)</td>
<td>Field contains notes on the account, such as “MCCF is clearing” when diary code changed to the 097.</td>
</tr>
<tr class="odd">
<td>TOTAL AR</td>
<td>(bottom of screen) Total amount owed the medical center</td>
</tr>
</tbody>
</table>

<span id="_Toc198214956" class="anchor"></span>Table 6: Accounts Receivable file (#430)

The diary code tells if the DMC has started collection on this account or not. The diary codes used for medical center debts include 090, 091, 092, 093, 097, 098, and 914. A list of these codes and an explanation of their use is included in Appendix C. C&P (Hines) Reason Codes

In the example above, the diary code is 090. This means the account has been established but offset has not begun. The next step is to navigate to screen C12 to check the Letter fields.

### CAROLS Screen C12

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc198214923" class="anchor"></span>Figure 51: CAROLS C12

03-23-2000 C12

FILE NUMBER PY DED STUB DC DC DATE DC INS DT TOTAL AR DISC RO

SSN or C# 00 81B VAPATIEN 090 05-30-2000 03-13-2000 60.70 04-1998 629

PAY-ADD 2 PAYEE Veterans Name LETTER

MULT-ADD 0 ADDRESS 1 STREET ADDRESS . CODE DATE

COOB-ADD 0 CITY ST SPY 04-14-2000

COOB 0

CR DATE

MULTI USE

ZIP 00001

PROPERTY CO-OBLIGOR

ZIP

ZIP ZIP

CALL-IN CALL-OUT

BANK NO

TYPE OF ACCT

DEP ACCT NO

The first line of this screen is the same as the C11 screen. In this example, the letter field shows SPY 04-14-2000—SPY is the name of the letter the DMC sends for the medical center accounts, the date is the date the letter was mailed to the Veteran. The DMC withholds the benefits 60 days from that date. In this case the letter was sent 04-14-00, which means the DMC will offset the 07-01-00 benefit check.

To continue with this example, it is important to know the diary code for this account will change to 098 on or about 06-09-00. This sets the repay information if the medical center has not submitted a lesser withholding amount request. Once the account has a diary code of 098, the only way a change can be made to the offset amount is manually by DMC staff. Medical centers must contact the DMC by Outlook mail.

If there is no information in the Letter fields, this means either this is a new referral and it is too early for the notification letter to have been sent, or the account debt is under \$25.00. The DMC does not send letters on accounts with a balance under \$25.00.

As long as an account has a diary code of 090, the medical center can take action to stop the withholding or reduce the withholding, depending on when the SPY letter was sent to the Veteran. Accounts having a diary code of 097 mean someone from the medical center has contacted the DMC and requested collection be stopped because the debt is going to clear. Check the User Information field on screen C11 to see the name of the individual requesting this action. If the diary code is 914 and the DC INS DT field 11-01-00, then the zero balance was processed on that date.

The C12 screen also shows the Veteran’s address that was transmitted to the DMC by the medical center.

<span id="_Toc198214924" class="anchor"></span>Figure 52: C12 Veterans Address Screen

<table>
<caption><p><span id="_Toc198214957" class="anchor"></span>Table 7: CAROLS/MCCF Diary Codes</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>03-23-2000</p>
<p>FILE NUMBER</p>
</blockquote></th>
<th>PY</th>
<th>DED</th>
<th><blockquote>
<p>STUB</p>
</blockquote></th>
<th><blockquote>
<p>DC</p>
</blockquote></th>
<th><blockquote>
<p>DC DATE</p>
</blockquote></th>
<th><blockquote>
<p>C14</p>
<p>DC INS DT</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL AR</p>
</blockquote></th>
<th><blockquote>
<p>DISC</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>RO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SSN or C#</p>
</blockquote></td>
<td>00</td>
<td>81B</td>
<td><blockquote>
<p>VJBEVER</p>
</blockquote></td>
<td><blockquote>
<p>090</p>
</blockquote></td>
<td><blockquote>
<p>05-30-2000</p>
</blockquote>
<p>FIS</p></td>
<td colspan="2"><blockquote>
<p>03-13-2000 60.70</p>
</blockquote>
<p>CAL TRANSACTION HISTORY</p></td>
<td><blockquote>
<p>04-1998</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>629</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CARS</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>HINES</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TRX</p>
</blockquote></td>
<td><blockquote>
<p>PRIN</p>
</blockquote></td>
<td><blockquote>
<p>INT</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN</p>
</blockquote></td>
<td>COURT</td>
<td>MARSH</td>
</tr>
<tr class="odd">
<td>NO</td>
<td>TRX</td>
<td colspan="2">DATE</td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>AMT</p>
</blockquote></td>
<td><blockquote>
<p>AMT</p>
</blockquote></td>
<td><blockquote>
<p>AMT</p>
</blockquote></td>
<td><blockquote>
<p>AMT</p>
</blockquote></td>
<td>AMT</td>
<td>AMT</td>
</tr>
<tr class="even">
<td>01</td>
<td>04P</td>
<td colspan="2">12-16-1999</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.13</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>02</td>
<td>04P</td>
<td colspan="2">12-16-1999</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>03</td>
<td>04P</td>
<td colspan="2">01-13-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.13</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>04</td>
<td>04P</td>
<td colspan="2">01-13-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>05</td>
<td>04P</td>
<td colspan="2">02-01-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>8.09</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>06</td>
<td>04P</td>
<td colspan="2">02-10-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.16</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>07</td>
<td>04P</td>
<td colspan="2">02-10-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>08</td>
<td>04P</td>
<td colspan="2">03-16-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.16</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>09</td>
<td>04P</td>
<td colspan="2">03-16-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>10</td>
<td>04P</td>
<td colspan="2">04-13-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.16</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>04P</td>
<td colspan="2">04-13-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>12</td>
<td>08P</td>
<td colspan="2">04-27-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>34.56</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>08P</td>
<td colspan="2">04-27-2000</td>
<td></td>
<td colspan="2"><blockquote>
<p>9.00</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>9.00</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc198214957" class="anchor"></span>Table 7: CAROLS/MCCF Diary Codes

The C14 screen shows the debits (TRX code 04P) and credits (TRX code 08P) the DMC has received from the medical center on this account.

# Debtor Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient’s address used for billing purposes may be stored in either the AR Debtor file (#340) or the VistA Patient file (#2). The AR software first checks the ADDRESS UNKNOWN field of the AR Debtor file (#340). If this field is set to YES, the system assumes there is no valid billing address for this debtor and no debt information is sent to the DMC.

AR Technicians should use the option called List of Patients with ADDRESS UNKNOWN (AR) located on the Account Management menu to identify those patients who have ADDRESS UNKNOWN set to YES. Research should be performed to identify billing addresses for the patients listed on this report.

<span id="_Toc198214925" class="anchor"></span>Figure 53: Debtor Address

Select Account Management Option:

Account Information

Address Display/Edit Bill

Comment Log Brief Account

Profile

Check Patient Account Balance

Debtor Comment Log

Follow-up Reports Full

Account Profile

List of Patients with ADDRESS UNKNOWN (AR)

Mark/Unmark Invalid Transaction

Statement Discrepancy Listing

Transaction History for a Patient

Select Account Management Option: List of Patients with ADDRESS UNKNOWN (AR)

DEVICE:

PATIENTS WITH UNKNOWN ADDRESS APR 6,2000 12:13 PAGE 1

PATIENT SSN

----------------------------------------------------------------------------------------

TEST,VAPATIENT 00000000A

TEST,VHAPATIENT 00000000B

TEST,VHAPATIENT E 00000000C

The Address Display/Edit option on the Account Management menu is used to enter billing address information into the AR Debtor file. This option is also used to mark when a billing address is unknown.

In the example below, the screen shows address information currently stored in the Patient file for TEST,VAPATIENT E. There is no billing address stored in the AR Debtor file. At the bottom of the screen, the ADDRESS UNKNOWN field is set to YES. This means even if this patient has debts that meet the referral criteria, that data will not be sent to the DMC.

<span id="_Toc198214926" class="anchor"></span>Figure 54: Address Display/Edit

Select Account Management Option: Address Display/Edit

Select AR DEBTOR: TEST,VAPATIENT E

Address Accounts Receivable will use:

TEST,VAPATIENT E

1 STREET ADDRESS

CITY, ST 00001

Phone: XXX-XXX-XXXX

Address from Patient file:

1 AVENUE ADDRESS

CITY, ST 00001

Phone: YYY-YYY-YYYY

Address from AR Debtor file:

Phone:

ADDRESS UNKNOWN: YES//

Once a billing address is confirmed the next step is to enter this into the AR Debtor file.

Using the same option, step through the following prompts.

<span id="_Toc198214927" class="anchor"></span>Figure 55: AR Debtor File information.

ADDRESS UNKNOWN: YES// NO

STREET ADDRESS \#1: 1 ROAD ADDRESS

STREET ADDRESS \#2: APT 2B

STREET ADDRESS \#3: CITY: CITY

STATE: STATE

ZIP CODE: 00001-1234

PHONE NUMBER:

At the ADDRESS UNKNOWN: YES// prompt type NO and press the Enter key. This change indicates the address is not unknown.

Then enter the appropriate information in the address fields. The information entered with this option is saved in the AR Debtor file. Make sure this information is shared with the individuals responsible for data in the Patient file. It may be appropriate to enter this same address there also.

AR assumes that if the address fields in the AR Debtor file are blank, the system should use the address data stored in the Patient file (#2).

Before AR builds the DMC transmission message, the system checks the address for a zip code and the existence of “invalid” characters. The system specifically checks to make sure the address lines do not contain any of the following characters: a dollar sign (\$), two asterisks (\*\*), three slashes (///) or three Zs (ZZZ).

If the ADDRESS UNKNOWN field is set to YES, the zip code is missing, or the address contains any invalid characters, the DMC Transmission for that debtor is <u>not created</u>. At the same time, a mail message is sent to the members of the G.DMR mail group stating, “Master Record-Monthly was not sent because the address was invalid or unknown.

Verify and re-enter address for the patient. Use the AR option called Address Display/Edit located on the Account Management menu to enter the correct address for this debtor. Once the address is corrected, this debtor account will be included in the next Monthly Master file transmission.

The following example shows an address that would not be sent to the DMC because it contains invalid characters (two asterisks) on Street Address \#2. This address needs to be corrected.

<span id="_Toc198214928" class="anchor"></span>Figure 56: Address for DMC Correction

Select Account Management Option: Address Display/Edit

Select AR DEBTOR: TEST,VAPATIENT D

Address Accounts Receivable will use:

TEST,VAPATIENT D

STREET

ADDRESS

APT. \*\*

CITY, ST 00001

Phone:

Address from Patient file:

AVENUE ADDRESS

CITY, ST 00001

APT. \*\*

Phone:

Address from AR Debtor file:

TEST,VAPATIENT D

STREET ADDRESS

APT. \*\*

CITY, ST 00001

Phone:

ADDRESS UNKNOWN: NO//

# Additional VistA Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMC Referral information is stored in two different VistA files: the AR Debtor file (#340) and the Accounts Receivable file (#430).

When a debtor’s account is referred to the DMC, a number of fields are automatically set in the AR DEBTOR file (#340). These fields include the following.

| Field Number | Field Name               | Description                                                                                                                                                              |
|--------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.01         | ACCOUNT AT DMC?          | This field contains a ‘1’ if this account has been referred to the Debt Management Center (DMC). The AR software sets this field upon creation of the DMC Master Record. |
| 3.02         | DATE SENT TO DMC         | Date the DMC Master Record was created and transmitted.                                                                                                                  |
| 3.03         | DMC DISCOVERY DATE       | The date bill established of the oldest bill referred to DMC.                                                                                                            |
| 3.05         | CURRENT TOTAL AT DMC     | Current amount of the debt that has been referred to DMC. This field will be updated by the DMC weekly transmission.                                                     |
| 3.06         | CURRENT PRINCIPAL AT DMC | Current principal amount of the debt that has been referred to DMC. This field will be updated by the DMC weekly transmission.                                           |
| 3.07         | CURRENT INTEREST AT DMC  | Current interest amount of the debt that has been referred to DMC. This field will be updated by the DMC weekly transmission.                                            |
| 3.08         | CURRENT ADMIN AT DMC     | Current admin amount of the debt that has been referred to DMC. This field will be updated by the DMC weekly transmission.                                               |

<span id="_Toc198214958" class="anchor"></span>Table 8: Master File Data Elements for Messages to DMC

There are two other DMC fields in the AR Debtor file. Both of these fields are set when a user uses a DMC Referral Menu option.

<table>
<caption><p><span id="_Toc198214959" class="anchor"></span>Table 9: Glossary</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3.09</td>
<td>LESSER WITHHOLDING AMOUNT</td>
<td>User enters a lesser withholding amount for DMC. Currently, when a debtor is identified for withholding by DMC, the full amount that the debtor holds is withheld. An amount in this field will allow the DMC to offset a lesser amount monthly until the debt is paid in full.</td>
</tr>
<tr class="even">
<td>3.1</td>
<td>SITE DELETION FLAG</td>
<td><p>User enters YES to delete the debtor from the DMC. When the weekly update encounters this flag, a ‘$0’ balance code sheet is sent to DMC to delete the debtor from their files.</p>
<p>However, the debtor could be resent with the next master record run if the debtor has bills that meet the referral criteria.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc198214959" class="anchor"></span>Table 9: Glossary

Each individual bill that is referred is also flagged as “Referred to DMC.” This is done when the system or the user populates the DMC fields in the ACCOUNTS RECEIVABLE file (#430). These fields are as follows:

<table>
<caption>Accounts Receivable File 430Table showing Accounts Receivable file 430 fields 121 "Date Sent to DMC", 122 "DMC Prinicipal Balance", 123 "DMC Interest Balance", 124 "DMC Admin Balance", 125 "DMC Debt Valid?", 126 "DMC Debt Valid Edited By", and 127 "DMC Debt Valid Edited Date" and their respective descriptions.</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>121</td>
<td>DATE SENT TO DMC</td>
<td>Date bill was first sent to the DMC.</td>
</tr>
<tr class="even">
<td>122</td>
<td>DMC PRINCIPAL BALANCE</td>
<td>Current principal balance for the bill at the DMC.</td>
</tr>
<tr class="odd">
<td>123</td>
<td>DMC INTEREST BALANCE</td>
<td>Current interest balance for the bill at the DMC.</td>
</tr>
<tr class="even">
<td>124</td>
<td>DMC ADMIN BALANCE</td>
<td>Current administrative cost balance for the bill at the DMC.</td>
</tr>
<tr class="odd">
<td>125</td>
<td>DMC DEBT VALID?</td>
<td><p>NULL value is the initial value.</p>
<p>“Y” for YES is assigned by the user if the bill is appropriate to be referred to DMC.</p>
<p>“N” for NO is assigned by the user if the bill is not appropriate to be referred to DMC.</p>
<p>“P” for PENDING, if the nightly background process prevents the bill from referring to DMC. Users are not able to assign “PENDING” status to the “DMC Debt Valid?” field.</p></td>
</tr>
<tr class="even">
<td>126</td>
<td>DMC DEBT VALID EDITED BY</td>
<td><p>Name of user who last edited the DMC DEBT VALID?</p>
<p>Field.</p></td>
</tr>
<tr class="odd">
<td>127</td>
<td>DMC DEBT VALID EDITED DATE</td>
<td>Last date the DMC DEBT VALID? Field was edited.</td>
</tr>
</tbody>
</table>

Accounts Receivable File 430Table showing Accounts Receivable file 430 fields 121 "Date Sent to DMC", 122 "DMC Prinicipal Balance", 123 "DMC Interest Balance", 124 "DMC Admin Balance", 125 "DMC Debt Valid?", 126 "DMC Debt Valid Edited By", and 127 "DMC Debt Valid Edited Date" and their respective descriptions.

There are two mail groups specifically for receiving DMC messages: G.DMX and G.DMR. These mail groups <u>must</u> have members who are active VistA users. The DMC transmits a list of those debtors NOT accepted for offset to the G.DMR mail group. A debtor may not be accepted either because of an “inactive benefit” or a Death notice. The system automatically clears all of the DMC flags (deletes information in all DMC fields) for those debtors and bills that have not been accepted by the DMC when the message titled “Patients Deleted from DMC: (SEQ. \#” is received.

> G.DMR - Receives messages regarding DMC Master Codesheets.

> G.DMX - Receives messages regarding DMC Weekly Codesheets.

In addition, in the case of a death notice being received, an individual mail message for each affected debtor will be compiled detailing this information and transmitted to the G.DMR mail group for follow-up by the local site in entering that information into the VISTA database. The Date of Death messages are based upon information found in the VBA BIRLS system. Be aware of the possibility that these dates are not all correct.

Make sure these messages are monitored and reviewed for accuracy prior to making any changes in VistA.

# Troubleshooting Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## E-Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Both mail groups—G.DMX and G.DMR—must have active members. There should be more than one member in each group in case of absence.

It is imperative that the “Weekly Update Records Sent to DMC” and the “Master File Records Sent to DMC” messages be monitored to insure they are received, along with their respective confirmation messages. If these messages are not received (every Tuesday and the last Thursday of each month respectively) contact the IRM support person for AR immediately. Non-receipt of these messages is an indication that the job did not run to completion and action must be taken. Also, non-receipt of the confirmation messages can mean that the information was not transmitted to the DMC.

Members of these mail groups are expected to maintain at least the last quarter’s messages in a separate mail basket. It is not necessary to save the individual “Deletion of Debtor from DMC” messages, as these individuals will be listed in the “Weekly Update” message with “0” balances. Also, please save the corresponding confirmation messages in case they are needed for researching problems.

## Timing Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Timeframes are critical to the DMC process. When researching problems, make sure the DMC referral timelines are followed. It is necessary to determine what month the debtor was first referred (it is indicated when viewing account profiles) and then review the “Weekly Update” messages for any and all updates sent to DMC. Remember, when the “Master File” is run on the last Thursday, it will reflect only what the debtor currently owes. Payments that are processed later on Thursday and so on will be included in the “Weekly Update” processed the first Tuesday of the following month. Please keep in mind that the PRCA Nightly Process runs at 2 AM at the sites so any payments, repayment plans, or lesser withholding actions, must take place before that time to be included in that week’s transmission.

When checking the CAROLS screens to ensure that updates have taken place, wait until the Thursday after receipt of the “Weekly Update” message. If the update did not take place, please insure that the debtor in question was included in the last “Weekly Update” message.

Verifying that the action entered is within the indicated timeframes will assist in determining if a problem really exists.

## Posting TDA Payments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMC data is dependent on receipt of data from the site. For DMC to reflect any payments, they must receive the information from the station. This makes it crucial that these payments are posted as soon as they are received at the site. This will ensure payment information is included in the “Weekly Update” messages.

## Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the letters DMC in the receipt number it is very helpful when reviewing accounts because is identifies where the payment came from. Many debtors attempt to stop the DMC collection by paying after the timeframe and collection has already been taken from their benefit check.

## Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When speaking with debtors regarding letters they received, double check that the letter is really from the Debt Management Center. This will avoid any time wasted researching AR and DMC to only find out that they actually received a letter from the Treasury regarding the Treasury Offset Program (formerly the IRS offsets).

# Appendix A. Sample Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc198214929" class="anchor"></span>Figure 57: Sample Letter

![](accounts-receivable-version-4-5-debt-management-center-dmc-referral-process-user/010.png)

# Appendix B. CAROLS/MCCF Diary Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 090  | Code used when an account is first established in CAROLS. After a withholding has been completed on the original debt but there is still a balance in the CAROLS system. |
| 091  | DMC is sending funds to the MCCF from a DMC account where a waiver was granted and a refund is due the Veteran.                                                          |
| 092  | DMC has received bankruptcy information and has forwarded it to the MCCR.                                                                                                |
| 093  | DMC received notice that the Veteran is deceased and sent the information to the MCCR.                                                                                   |
| 097  | DMC is suspending collection because the MCCF is going to clear the account.                                                                                             |
| 098  | DMC is offsetting C&P benefits and sending them to the MCCR.                                                                                                             |
| 914  | Indicates the Total A/R balance in CAROLS is zero.                                                                                                                       |

CAROLS MCCF Diary CodesTable showing CAROLS MCCF Diary Codes and their descriptions.

# Appendix C. C&P (Hines) Reason Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an MCCF debt is referred to the DMC by a VA Medical Center, the Type of Debt is provided. The Type of Debt code(s) are stored in the C&P (Hines) Reason Code field on CAROLS. The total debt amount may be comprised of one or more of the six different debt types. If the Veteran has a debt which includes more than two of the different Types of Debt, only the first two codes provided by the AR transmission will be reflected in the CAROLS master. Types of Debt codes include:

- Ineligible Hospital Emergency/Humanitarian
- Adult Day Health Care
- C (Means Test)
- Domiciliary
- Geriatric Eval-Institutional
- Geriatric Eval-Non-Institutional
- Nursing Home Care-LTC
- Respite Care-Institutional
- Respite Care-Non-Institutional
- RX Co-Pay (SC)
- RX Co-Pay (NSC)
- TRICARE Patient

As stated above, the total amount of a debt for an individual may contain more than one “Type of Debt” codes listed above. For example, the C&P (Hines) Reason Code field in the CARS Master may show “12” which reflects a debt comprised of a Pharmacy co- payment (Code 1) and Means Testing (Code 2). If the debt includes Means Testing (Code 2) and Emergency Humanitarian (Code 4), the C&P (Hines) Reason Code field in CARS will show “24.” This is because the C&P (Hines) Reason Code field allows only two characters.

# Appendix D. Examples of VistA Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example of VistA Master File message

<span id="_Toc198214930" class="anchor"></span>Figure 58: VISTA Master File Message

Subj: MASTER FILE RECORDS SENT TO DMC ON 11/26/98 \[#95806277\] 26 Nov 98 04:32

1795 Lines

From: AR PACKAGE in ‘DMC’ basket. Page 1

---------------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Last</p>
</blockquote></th>
<th><blockquote>
<p>Principle</p>
</blockquote></th>
<th><blockquote>
<p>Interest</p>
</blockquote></th>
<th><blockquote>
<p>Admin</p>
</blockquote></th>
<th><blockquote>
<p>Total</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>---­</p>
</blockquote></td>
<td><blockquote>
<p>--­</p>
</blockquote></td>
<td><blockquote>
<p>--------­</p>
</blockquote></td>
<td><blockquote>
<p>-------­</p>
</blockquote></td>
<td><blockquote>
<p>----­</p>
</blockquote></td>
<td><blockquote>
<p>----­</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XXXXXX,XXXXXXX X.</p>
</blockquote></td>
<td><blockquote>
<p>NNNN</p>
</blockquote></td>
<td><blockquote>
<p>38.00</p>
</blockquote></td>
<td><blockquote>
<p>1.30</p>
</blockquote></td>
<td><blockquote>
<p>5.69</p>
</blockquote></td>
<td><blockquote>
<p>44.99</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XXXXXXX,XXXXXX X.</p>
</blockquote></td>
<td><blockquote>
<p>NNNN</p>
</blockquote></td>
<td><blockquote>
<p>1645.60</p>
</blockquote></td>
<td><blockquote>
<p>181.18</p>
</blockquote></td>
<td><blockquote>
<p>6.80</p>
</blockquote></td>
<td><blockquote>
<p>1833.59</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XXXXXX,XXXXX XXXXXXX</p>
</blockquote></td>
<td><blockquote>
<p>NNNN</p>
</blockquote></td>
<td><blockquote>
<p>3166.00</p>
</blockquote></td>
<td><blockquote>
<p>226.81</p>
</blockquote></td>
<td><blockquote>
<p>9.39</p>
</blockquote></td>
<td><blockquote>
<p>3402.20</p>
</blockquote></td>
</tr>
</tbody>
</table>

Example of VistA Weekly Update message<span id="_Toc1557806" class="anchor"></span>

Figure 59: VISTA Weekly Update

Subj: WEEKLY UPDATE RECORDS SENT TO DMC ON 04/04/00 \[#1231231\] 04 Apr 00 02:02 40

lines

From: AR PACKAGE in ‘DMC’ basket. Page 1

Name Last Principle Interest Admin Total

--- -- -------- ------- ---- ----

XXXXXX,XXXXX X. NNNN 52.29 0.44 1.00 53.73

XXXXXXX,XXXXXXXXX X NNNN 48.00 3.90 9.21 61.11

XXXXXX,XXXXXX X NNNN 605.40 10.50 1.95 617.85

XXXXXXX,XXXXXXX NNNN 26.30 0.22 1.00 27.52

XXXXX,XXXXX X NNNN 22.00 0.74 7.35 30.09

XXXX.XXXXXX X NNNN 12.00 0.48 4.20 16.68

XXX,XXXXXX X NNNN 20.00 0.80 11.61 32.41

Total Records Sent: 33

Total Principle: 1720.68

Total Interest: 42.12

Total Admin: 126.39

Total: 1889.19

# Appendix E. Master File Data Elements for Messages to DMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<caption>Master File Data Elements for Messages to DMCTable of Master File Data Elements showing DMC Name, VistA File Name and Number, VistA Field Name and Number, Description and an example, and the values for the field(s).</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 27%" />
<col style="width: 29%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>DMC Name</th>
<th>VistA File Name/Number</th>
<th>VistA Field Name/Number</th>
<th>Description/Example</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Social Security #</td>
<td>PATIENT (#2)</td>
<td>SOCIAL SECURITY NUMBER (#.09)</td>
<td><p>99999999</p>
<p>Excludes “test” patients (SSN begins with 00000)</p></td>
<td>9 character numeric</td>
</tr>
<tr class="even">
<td>Stub Name</td>
<td>PATIENT (#2)</td>
<td>NAME (#.01)</td>
<td><p>First Initial Middle Initial</p>
<p>First 5 characters of last name</p>
<p>(i.e., <u>T</u>EST <u>B PATIE</u>NT = ABPATIE)</p></td>
<td>7 characters</td>
</tr>
<tr class="odd">
<td>Station Number</td>
<td>AR SITE PARAMETER (#342)</td>
<td>SITE (#.01)</td>
<td>VA Facility Station number</td>
<td>3 character numeric</td>
</tr>
<tr class="even">
<td>Date of Birth</td>
<td>PATIENT (#2)</td>
<td>DATE OF BIRTH (#.03)</td>
<td>MMDDYYYY</td>
<td>8 character numeric</td>
</tr>
<tr class="odd">
<td rowspan="2">Phone Number</td>
<td>AR DEBTOR (#340)</td>
<td>PHONE (#1.07)</td>
<td rowspan="2">Area code is not mandatory – if not present, first three spaces are blank</td>
<td rowspan="2">Numeric and blank data only</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PHONE NUMBER [RESIDENCE] (#.131)</td>
</tr>
<tr class="odd">
<td>Full Name</td>
<td>PATIENT (#2)</td>
<td>NAME (#.01)</td>
<td>First name, Middle name, Last name, and “extra” name (e.g. Jr or Sr)</td>
<td>40 characters</td>
</tr>
<tr class="even">
<td>Address</td>
<td>AR DEBTOR (#340)</td>
<td><p>STREET ADDRESS #1 (#1.01)</p>
<p>STREET ADDRESS #2 (#1.02)</p>
<p>STREET ADDRESS #3 (#1.03)</p>
<p>CITY (#1.04 STATE (#1.05)</p></td>
<td>System checks AR DEBTOR file for address information first. If there is data, it uses this address. If not, it uses the address stored in the PATIENT file.</td>
<td>40 characters</td>
</tr>
<tr class="odd">
<td>Address</td>
<td>PATIENT (#2)</td>
<td><p>STREET ADDRESS [LINE 1] (#.111)</p>
<p>STREET ADDRESS [LINE 2] (#.112)</p>
<p>STREET ADDRESS [LINE 3] (#.113)</p>
<p>CITY (#.114)</p>
<p>STATE (#.115)</p></td>
<td>5 lines- 3 for street, 1 for city, 1 for state</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2">Zip Code</td>
<td>AR DEBTOR (#340)</td>
<td>ZIP CODE (#1.06)</td>
<td rowspan="2">Zip + 4</td>
<td rowspan="2">9 character numeric</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>ZIP+4 (#.1112)</td>
</tr>
<tr class="even">
<td>Discovery Date</td>
<td>ACCOUNTS RECEIVABLE (#430)</td>
<td>DATE ACCOUNT ACTIVATED (#60)</td>
<td><p>System uses the DATE ACCOUNT ACTIVATED from the oldest debt (bill) submitted to DMC.</p>
<p>If a date cannot be determined, the default will be 91 days prior to the current date</p></td>
<td>8 character numeric</td>
</tr>
<tr class="odd">
<td>Principle</td>
<td>ACCOUNTS RECEIVABLE (#430)</td>
<td>PRINCIPAL BALANCE (#71)</td>
<td><p>Total principle for all bills that meet criteria.</p>
<p>Two decimal places (None in the code sheet itself). Right justified and ZERO filled.</p></td>
<td>9 character numeric</td>
</tr>
<tr class="even">
<td>Interest</td>
<td>ACCOUNTS RECEIVABLE (#430)</td>
<td>INTEREST BALANCE (#73).</td>
<td><p>Total interest amount for all bills that meet criteria.</p>
<p>Two decimal places (None in the code sheet itself). Right justified and ZERO filled.</p></td>
<td>9 character numeric</td>
</tr>
<tr class="odd">
<td>Admin</td>
<td>ACCOUNTS RECEIVABLE (#430)</td>
<td><p>ADMINISTRATIVE COST BALANCE (#73)</p>
<p>+ MARSHAL FEE (#74)</p>
<p>+ COURT COST (#75)</p></td>
<td><p>Total administrative charges for all bills that meet criteria.</p>
<p>Two decimal places (None in the code sheet itself). Right justified and ZERO filled.</p></td>
<td>9 character numeric</td>
</tr>
<tr class="even">
<td>Transmission Date</td>
<td></td>
<td></td>
<td><p>Date Master created/transmitted</p>
<p>MMDDYYYY</p></td>
<td>8 character numeric</td>
</tr>
<tr class="odd">
<td>Type of Debt</td>
<td>ACCOUNTS RECEIVABLE (#430)</td>
<td>CATEGORY (#2)</td>
<td><p>All of the different category codes from the bills eligible to be referred</p>
<p>Pharmacy = 1</p>
<p>Means Test =2</p>
<p>Ineligible = 3</p>
<p>Emergency Humanitarian=4 CHAMPVA=5 CHAMPUS=6</p>
<p>Or any legitimate combination of the above…</p></td>
<td>Set of Codes<br />
(up to 6 characters - Left justified and blank filled)</td>
</tr>
<tr class="even">
<td>Offset Amount</td>
<td>AR DEBTOR (#340)</td>
<td>LESSER WITHHOLDING AMOUNT (#3.09)</td>
<td>Amount VHA wants to offset from Benefits</td>
<td>9 character numeric</td>
</tr>
<tr class="odd">
<td>Total Amount of Debt</td>
<td></td>
<td></td>
<td><p>Calculated dollar amount includes Principal, Interest, and all Administrative charges.</p>
<p>Total of all MCCF bills</p></td>
<td>9 character numeric</td>
</tr>
<tr class="even">
<td>Hospital ID #</td>
<td>AR DEBTOR (#340)</td>
<td>DEBTOR (#.01)</td>
<td>Internal entry number of AR Debtor.</td>
<td>10 character numeric</td>
</tr>
</tbody>
</table>

Master File Data Elements for Messages to DMCTable of Master File Data Elements showing DMC Name, VistA File Name and Number, VistA Field Name and Number, Description and an example, and the values for the field(s).

# Appendix F. Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1017G Form</td>
<td>Financial form used to send funds to a medical center.</td>
</tr>
<tr class="even">
<td>Account</td>
<td>A record established for a debtor in the AR Debtor file (#340). The account can contain multiple bills for an individual debtor.</td>
</tr>
<tr class="odd">
<td>Account Profile</td>
<td>A screen display or printout showing an activity summary for an entire account.</td>
</tr>
<tr class="even">
<td>Accounting Technician</td>
<td>A person with who is responsible for processing accounting transactions.</td>
</tr>
<tr class="odd">
<td>Accounts Receivable</td>
<td><p>In the broadest sense, debts owed to the Department of Veterans Affair are referred to as Accounts Receivable.</p>
<ol type="1">
<li><p>Synonymous with the abbreviation ‘AR’</p></li>
<li><p>In this document, AR also refers to VA’s automated system designed to process first party medical co- payment debt referred electronically to the Debt Management Center. This software is developed and maintained by the VHA Office of Information.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Accounts Receivable Clerk</td>
<td>A person who establishes, audits, and maintains the debt collection files of the medical center.</td>
</tr>
<tr class="odd">
<td>Accounts Receivable Section</td>
<td>The staff responsible, as a group, for establishment and maintenance of debtor account records.</td>
</tr>
<tr class="even">
<td>Active Bill</td>
<td>Bills that are in an “active” status are available for collection. Bills must be in an active status in order to be forwarded for collection.</td>
</tr>
<tr class="odd">
<td>Address Unknown</td>
<td>This field is set in the AR Debtor file (#340) to indicate that site has not been able to obtain a correct address for the debtor. If this field is set to YES, the debtor’s account will NOT be forwarded for offset.</td>
</tr>
<tr class="even">
<td>Adjustment</td>
<td>A transaction that makes an administrative change to the principal balance of a bill or an account.</td>
</tr>
<tr class="odd">
<td>Admin Charge</td>
<td>An administrative charge incurred during the debt collection process and added to an account’s principal balance. Fees for locator searches, marshal fees, and court costs are administrative charges.</td>
</tr>
<tr class="even">
<td>Agent Cashier</td>
<td>A person who receives and applies payments to debtor accounts and issues official receipts.</td>
</tr>
<tr class="odd">
<td>Aid and Attendance (A&amp;A)</td>
<td><p>A VA compensation or pension benefit awarded to a Veteran determined to be in need of the regular aid and attendance of another person to perform basic functions of everyday life. A Veteran may qualify for aid and attendance benefits if he or she:</p>
<ul>
<li><p>Is blind or so nearly blind as to have corrected visual acuity of 5/200 or less, in both eyes, or concentric contraction of the visual field to 5 degrees or less; or</p></li>
<li><p>Is a patient in a nursing home because of mental or physical incapacity; or</p></li>
<li><p>Proves a need for aid and attendance under established criteria</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AITC</td>
<td>See Austin Information Technology Center</td>
</tr>
<tr class="odd">
<td>AR</td>
<td>See Accounts Receivable</td>
</tr>
<tr class="even">
<td>Austin Information Technology Center (AITC)</td>
<td>The AITC (formerly the Corporate Franchise Data Center) is VA’s data center site located in Austin, Texas. The AITC receives the transmission files for referred debts and updates to existing referrals from the VistA Accounts Receivable system on a scheduled basis. The AITC compiles this information and forwards it to the Debt Management Center (DMC). The AITC also transmits both confirmation and reject messages to the AR system at each medical center via Mailman.</td>
</tr>
<tr class="odd">
<td>Bill</td>
<td>A receivable.</td>
</tr>
<tr class="even">
<td>BIRLS</td>
<td>Beneficiary Identification and Records Locator System is located at the Austin Data Processing Center. This system contains basic identification and related data for millions of Veterans and beneficiaries and, also, provides information on the location of records. The system assigns claims numbers; processes death notices and manages the transfer of records.</td>
</tr>
<tr class="odd">
<td>C&amp;P Mini-Master file</td>
<td>Compensation and Pension mini-master file contains VBA compensation, pension, and education claims information.</td>
</tr>
<tr class="even">
<td>C&amp;P Reason Codes</td>
<td>Set of codes that relate to the type of debt being referred to the DMC. (i.e., Pharmacy Co-Pay, Means Testing, etc.)</td>
</tr>
<tr class="odd">
<td>CAROLS</td>
<td>See CARS</td>
</tr>
<tr class="even">
<td>CARS</td>
<td>Centralized Accounts Receivables System for Veterans Benefit Administration (VBA) provides information on the status of compensation, pension, education, and loan guaranty accounts receivable.</td>
</tr>
<tr class="odd">
<td>Catastrophically Disabled</td>
<td>A Veteran is classified as Catastrophically Disabled if a medical evaluation determines they have a severely disabling injury, disorder, or disease that permanently compromises their ability to perform daily living activities. The disability must also require personal or mechanical assistance for the Veteran to leave their home or bed.</td>
</tr>
<tr class="even">
<td>CCPC</td>
<td>Consolidated Copayment Processing Center System located at the Austin. CCPC receives station data from which monthly statements are generated and mailed to patients who incur first party debts.</td>
</tr>
<tr class="odd">
<td>Debt Collection</td>
<td>This is the official name given to the process of sending out bills and collecting payments.</td>
</tr>
<tr class="even">
<td>Debt Management Center</td>
<td>The nationwide debt collection operation for VA located at the St. Paul VA Regional Office.</td>
</tr>
<tr class="odd">
<td>Debtor</td>
<td>A patient, person, vendor, insurance company, or institution that owes the VA money.</td>
</tr>
<tr class="even">
<td>Default</td>
<td>A suggested response provided by the system.</td>
</tr>
<tr class="odd">
<td>Diary Code</td>
<td>Set of codes assigned to a debt in CARS to convey the status of the debt. (Debt established, waiver granted, Veteran is deceased, etc.)</td>
</tr>
<tr class="even">
<td>DMC</td>
<td>See Debt Management Center</td>
</tr>
<tr class="odd">
<td>Full Debt Balance</td>
<td>Amount that the DMC will set up for collection/offset. This includes the principal amount of bill(s) plus interest and administrative costs.</td>
</tr>
<tr class="even">
<td>G.DMR</td>
<td>Mail group that receives the entire monthly master account information that is transmitted to DMC. Also receives the Patient Deleted from DMC, Death notice, and Address Unknown/Corrected messages.</td>
</tr>
<tr class="odd">
<td>G.DMX</td>
<td>Mail group that receives the all the weekly update information on accounts that have been referred to DMC for collection.</td>
</tr>
<tr class="even">
<td>Housebound Benefit</td>
<td>The VA’s Housebound benefit is an additional amount available to eligible Veterans and dependents who are entitled to VA pension or VA compensation. The housebound allowance may be paid to Veterans, dependent spouses, or surviving spouses who because of their physical limitations, are unable to walk or travel beyond their home and are reasonably certain the disabilities or confinement will continue throughout his or her lifetime. Certain restrictions apply. For more information and eligibility criteria on this benefit call REDACTED or go to REDACTED</td>
</tr>
<tr class="odd">
<td>Interest</td>
<td>Amount charged to an account being paid on a repayment plan for carrying the account or on delinquent accounts.</td>
</tr>
<tr class="even">
<td>Lesser Withholding Amount</td>
<td>If it would be a financial hardship for a patient to make a payment-in-full or have the full amount of the past due debt deducted from the benefit check, the Veteran may negotiate a lesser withholding amount be entered for the DMC debt. (The amount cannot less than $25.) This information is recorded in VistA and the DMC.</td>
</tr>
<tr class="odd">
<td>Mail Groups</td>
<td>List of e-mail recipients who can all be addressed at once by reference to a mail group name defined in VistA. DMC messages are sent to the G.DMX and G.DMR mail groups.</td>
</tr>
<tr class="even">
<td>Master File</td>
<td>Mail message containing all the delinquent accounts that are eligible for referral to the DMC. The master file compiled on the last Thursday of each month and transmitted from the VistA system to the DMC via the AITC.</td>
</tr>
<tr class="odd">
<td>Master Record Printout (RPO)</td>
<td>BIRLS master records used by DMC staff.</td>
</tr>
<tr class="even">
<td>National Service Center</td>
<td>Processes requests to Centralized Accounts Receivables System (CARS/CAROLS).</td>
</tr>
<tr class="odd">
<td>Patient Statement of Account</td>
<td>The monthly statement for patient type debtors, reflecting all activity (both charges and payments) recorded for that patient since his last statement was printed.</td>
</tr>
<tr class="even">
<td>Pension Benefit</td>
<td>VA pension is a monetary award paid on a monthly basis to Veterans with low income who are permanently and totally disabled, or are age 65 and older, may be eligible for monetary support if they have 90 days or more of active military service, at least one day of which was during a period or war. Payments are made to qualified Veterans to bring their total income, including other retirement or social security income, to a level set by Congress annually. Veterans of a period of war who are age 65 or older and meet service and income requirements are also eligible to receive a pension, regardless of current physical condition.</td>
</tr>
<tr class="odd">
<td>PRCA Nightly Process</td>
<td>Set of AR routines scheduled to run at the same time every night. These routines update all actions completed through the AR VistA software. In addition, this set of routines includes those that create, record, and transmit the DMC Weekly Update and Monthly Master information to the AITC and the local VistA mail groups (G.DMR and G.DMX).</td>
</tr>
<tr class="even">
<td>Processing Date</td>
<td>The date when benefit checks are actually debited for the amount owed. This date varies from month-to- month based on the number of days in the month and if there are holidays in that month.</td>
</tr>
<tr class="odd">
<td>Profile of Accounts Receivable</td>
<td>Accounts Receivable option that displays information on debtor accounts. This profile shows if an account has been forwarded to the DMC.</td>
</tr>
<tr class="even">
<td>Regional Counsel</td>
<td>VA office responsible for all account receivables requiring litigation.</td>
</tr>
<tr class="odd">
<td>Repayment Plan</td>
<td>If a debt is so large that the debtor can’t repay it in a lump sum a repayment plan may be established to pay it in regularly scheduled installments. Can be established by the fiscal officer, or designee, as the result of negotiations with the District Counsel or Department of Justice.</td>
</tr>
<tr class="even">
<td>Revenue Coordinator</td>
<td>Individual at a medical center who provides leadership, supervision, and expertise for all aspects of administrative operations that directly affect reimbursement for medical services. (Also known as MCCF Coordinator or Business Office Coordinator.)</td>
</tr>
<tr class="odd">
<td>Service Connected</td>
<td>A disability that VA determines was incurred or aggravated while on active duty in the military and in the line of duty. A service-connected rating is an official ruling by VA that your illness/condition is directly related to your active military service. Service-connected ratings are established by VA Regional Offices located throughout the country.</td>
</tr>
<tr class="even">
<td>Service Connected Veteran</td>
<td>A Veteran who has an illness or injury incurred in or aggravated by military service as determined by VA.</td>
</tr>
<tr class="odd">
<td>Site Deletion Flag</td>
<td>Field in AR Debtor file (#340) that is set to ‘1’ when the Accounts Receivable option called Remove Debtor from DMC is used to stop any collection by the DMC.</td>
</tr>
<tr class="even">
<td>SPY</td>
<td>Letter sent by DMC notifying debtor of delinquent account and subsequent offset of benefit check.</td>
</tr>
<tr class="odd">
<td>Suspended Status</td>
<td>AR status that will prevent transmission of bill information to DMC for collection. Sites are cautioned NOT to place bills in this status. (This action is usually performed when setting up repayment plans, etc.)</td>
</tr>
<tr class="even">
<td>Suspense Account</td>
<td>A general ledger account designed to hold payments where the specific account number is unknown. In the case of DMC payments, payments are received via Transfer of Disbursing Authority (TDA) to the facility suspense account, and the facility is responsible for posting the payment amount to the debtor’s account.</td>
</tr>
<tr class="odd">
<td>TDA</td>
<td>See Transfer of Disbursing Authority</td>
</tr>
<tr class="even">
<td>TOP</td>
<td>See Treasury Offset Program</td>
</tr>
<tr class="odd">
<td>Transaction</td>
<td>Any action that affects a bill or an account. All transactions are numbered sequentially and can be examined individually.</td>
</tr>
<tr class="even">
<td>Transaction Number</td>
<td>A number assigned by the computer for an activity against a debt (such as increase adjustment, decrease adjustment, payment, etc.)</td>
</tr>
<tr class="odd">
<td>Transaction Profile</td>
<td>A screen display or printout that shows a summary of a single transaction.</td>
</tr>
<tr class="even">
<td>Transfer of Disbursing Authority (TDA)</td>
<td>Official notification sent to medical center that a certain amount of funding has been forwarded to them. In the case of the DMC payments, the date of the TDA is the actual date payments were received and should be used when posting payments to debtor accounts.</td>
</tr>
<tr class="odd">
<td>Treasury Offset Program (TOP)</td>
<td>Mandatory government wide delinquent debt matching and payment offset system. Debts that cannot be collected by the DMC must be forwarded to this collection program where delinquent debts may be recovered by offset of income tax refunds; Federal salary pay, including military pay; Federal retirement, including military retirement pay; Federal benefit payments; and other Federal payments.</td>
</tr>
<tr class="even">
<td>VACCESS</td>
<td>Database located at the Austin Automation Center where financial information is stored. Special software and access codes are required to access this database.</td>
</tr>
<tr class="odd">
<td>VAVBASPL/DMC/MCCR</td>
<td>Outlook mail group designated to send and receive messages regarding DMC accounts.</td>
</tr>
<tr class="even">
<td>VBA Regional Office of Jurisdiction</td>
<td>The VBA Regional Office that is the “owner” of the Veteran’s VBA record.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><p>Veterans Health Information Systems and Technology Architecture.</p>
<p>The VA developed computer system that supports day-to-day operations at local VA health care facilities.</p></td>
</tr>
<tr class="even">
<td>Waiver</td>
<td>Waivers are only given by the DMC for debts other than those sent by the medical centers. If a debtor receives a waiver on a DMC debt and then is owed a refund on this debt – this amount will be applied to any outstanding VAMC debts that they may have.</td>
</tr>
<tr class="odd">
<td>Weekly Update File</td>
<td>Each Tuesday, Accounts Receivable software looks at accounts currently referred to the DMC and sends an update message for those accounts where the total principal, interest, and administrative costs for referred bills is different than the amounts currently on file in the DMC or if a message was received that the debtor’s account was reduced to $0 (zero) at the DMC.</td>
</tr>
<tr class="even">
<td>Withholding</td>
<td>Action performed by the DMC which deducts the amount owed from a debtor’s benefit check.</td>
</tr>
</tbody>
</table>

# Appendix G. Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMCOutlook Mail Group: vavbaspl/dmc/mccr

To request the following:

- DMC Lesser Amounts
- Stop collection action on referred accounts

Office of Community Care Revenue OperationsREDACTEDPhone: REDACTED

Email: REDACTED

Contact the Office of Community Care Revenue Operations to:

- Request assistance or information about the DMC program

Austin Information Technology Center (AITC)REDACTEDPhone: REDACTED

Email: REDACTED

- To request technical assistance about the DMC program

VA Service DeskPhone: REDACTED

Contact the VA Service Desk to request the following:

- Log a Remedy Ticket.
- Assistance with DMC software problem. An Enterprise Product Support (EPS) person will contact the submitter and investigate the technical problem.