---
title: Accounts Receivable Version 4.5 Technical Manual/Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: archive
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5
group_key: "PRCA:PRCA:4.5"
file_numbers: 
  - 200
  - 340
  - 430
  - 433
security_keys: []
menu_options: 1
description: "<table> <caption><p><span id=\\"_Toc67391128\\" class=\\"anchor\\"></span>Table 1: AR Routines</p></caption> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 39%\\" /> <col style=\\"width: 21%\\" /> <col style=\\"width: 21%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong>Date</strong></th> <th><stro"
audience: 
keywords: 
  - class
  - even
  - bill
  - cross
  - report
  - accounts
  - receivable
  - table
  - reference
  - span
page_count: 0
word_count: 33545
section_count: 8
table_count: 50
figure_count: 3
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)_Archive/prca_4_5_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)_Archive/prca_4_5_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=244"
---

---
title: |
  Accounts Receivable

  Technical Manual/Security Guide
---

![](accounts-receivable-version-4-5-technical-manual-security-guide/001.png)

March 1995

Veterans Affairs

Enterprise Program Management Office

Revision History

Initiated on 12/29/04

<table>
<caption><p><span id="_Toc67391128" class="anchor"></span>Table 1: AR Routines</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 39%" />
<col style="width: 21%" />
<col style="width: 21%" />
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
<td>August 2021</td>
<td>Added new RCHRFS, RCHRFS1, RCHRFS2, and RCHRFSUT routines to the section <strong>Accounts Receivable Routines and Templates</strong> for PRCA*4.5*379</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2021</td>
<td><p>Updates for PRCA*4.5*387:</p>
<p>Updated the PRCA NIGHTLY PROCESS Option definition.</p></td>
<td>REDACTED</td>
<td>CCDSO IBAR Development Team</td>
</tr>
<tr class="odd">
<td>July 2021</td>
<td><p>Updates for PRCA*4.5*381</p>
<ul>
<li><p>Added new RCRP series routines to the Routines Section.</p></li>
<li><p>Updated the Repayment Plan portion of the Accounts Receivable Menus section.</p></li>
</ul></td>
<td>REDACTED</td>
<td>CCDSO IBAR Development Team</td>
</tr>
<tr class="even">
<td>May 2021</td>
<td><p>Updates for PRCA*4.5*377</p>
<ul>
<li><p>Added new RCRP series routines to the Routines Section.</p></li>
<li><p>Updated the Repayment Plan portion of the Accounts Receivable Menus section.</p></li>
</ul></td>
<td>REDACTED</td>
<td>CCDSO IBAR Development Team</td>
</tr>
<tr class="odd">
<td>March 2021</td>
<td>Updated section <strong>Accounts Receivable Routines and Templates</strong> with RCVCR1 and RCVCR2 routines for PRCA*4.5*373</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>January 2021</td>
<td><p>Updates for PRCA*4.5*376</p>
<ul>
<li><p>Added a new File (340.5)</p></li>
<li><p>Moved the Accounts Receivable Files section to its own section</p></li>
<li><p>Updated the indexes</p></li>
</ul></td>
<td>REDACTED</td>
<td>CCAD IBAR DEVELOPMENT TEAM</td>
</tr>
<tr class="odd">
<td>October 2020</td>
<td>Updated for PRCA*4.5*345</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>September 2020</td>
<td><p>Updated for patch PRCA*4.5*361</p>
<p>This patch includes updates to the DMC First Party Charge IB Cancellation Recon Report to include updated IA references.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>December 2019</td>
<td><p>Updated for patch, PRCA*4.5*350</p>
<p>This patch features functionality that allows TCSP rereferral of previously referred bills, as well as suspension and resumption of referrals at debtor and site levels.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2019</td>
<td>Updates for patch PRCA*4.5*338 to align existing and new AR categories with new CC and CHOICE IB codes to be mapped to new Revenue Source Codes (RSC) and be externally reported within FMS systems using the RSC.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>July 2019</td>
<td><p>Updated for patch PRCA*4.5*347</p>
<p>This patch features functionality that allows accounts receivable personnel to run new debt reconciliation reports.</p>
<p>Updated to current documentation standards.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June 2019</td>
<td>Updates for PRCA*4.5*332</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>November 2018</td>
<td>Updates for PRCA*4.5*326</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June 2018</td>
<td>Updates for PRCA*4.5*321</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>May 2018</td>
<td>Added updates for PRCA*4.5*320 and Added updates for PRCA*4.5*315</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>March 2018</td>
<td>Update for patch PRCA*4.5*335 to include new ARDC Monthly Reconciliation Report [PRCA ARDC MONTHLY REPORT] report. See pages: 48, 64, 97</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>October 2017</td>
<td><p>Updated for patch PRCA*4.5*318</p>
<p>This patch removed a lock from the option RCDPE EDI NATIONAL REPORTS. Added locks to several options under the RCDPE NR EXTRACT MENU. Added routines associated with the “Auto Decrease Report”, “Daily Activity Report”, and a new report “Auto Posted Receipt Report”. Added new DBIA #6747. Added description for “Unapplied EFT Deposit Report” (that was removed previously by accident) and the new report referenced above.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>September 2017</td>
<td><p>Updated for patch, PRCA*4.5*327:</p>
<p>This patch features functionality that sends two new mail messages to the 'TCSP' mail group when a batch run is completed and when a corrupt debt occurs. See pages: 4, 5, 19, 19</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>July 2017</td>
<td><p>Updated for patch PRCA*4.5*325:</p>
<p>This patch converts all scripts for handling Treasury Cross Service Project (TCSP) exceptions between Vista and Treasury to user option with improved controls. These scripts were provided to sites by the TCSP developers to handle mismatched Vista debtor/bills with the Treasury status for the same debtor/bills. See pages: 14, 71, 142</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>March 2017</td>
<td><p>Updated for patch PRCA*4.5*310</p>
<p>This patch includes entries in several AR files to support the new Rate Type of FEE REIMB INS. This new rate type is similar to REIMBUR. INS. and is used to segregate revenue generated by third party reimbursement of fee based Non-VA Care.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>October 2016</td>
<td>Additional updates for PRCA*4.5*301. See pages: 8, 18, 27, 29, 44, 76, and 87. Technical edit.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June 2016</td>
<td>Added updates for PRCA*4.5*303 and PRCA*4.5*304</td>
<td>REDACTED</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>February 2015</td>
<td>Added update for PRCA*4.5*298</td>
<td>REDACTED</td>
<td>FirstView</td>
</tr>
<tr class="even">
<td>September 2014</td>
<td>Technical edit.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>April 2012</td>
<td>Added update for PRCA*4.5*284</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>March 2012</td>
<td>Added update for PRCA*4.5*275</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Dec 2011</td>
<td>Updated for EDI Lockbox – Patch PRCA*4.5*276</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Oct 2011</td>
<td>Copied from PDF to Microsoft Word</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/29/2004</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/29/2004</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc67391128" class="anchor"></span>Table 1: AR Routines

Preface

This Technical Manual is designed to provide the Site Manager with information necessary to install, maintain, and troubleshoot Version 4.5 of the Accounts Receivable package. The Accounts Receivable package automates the Fiscal functions related to the management of Accounts Receivable and is integrated with the Integrated Billing (IB) package process of preparing patient Bills on the UB-92. The Accounts Receivable package is also integrated with the National Roll-Up database.

Table of Contents

List of Tables

# Introduction – Overview of Accounts Receivable


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction – Overview of Accounts Receivable](#introduction-overview-of-accounts-receivable)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Other Maintenance Issues](#other-maintenance-issues)
- [Accounts Receivable Routines and Templates](#accounts-receivable-routines-and-templates)
  - [Accounts Receivable Routines](#accounts-receivable-routines)
  - [Accounts Receivable Mapped Routines](#accounts-receivable-mapped-routines)
- [Accounts Receivable Integration with Integrated Billing and National Roll-Up](#accounts-receivable-integration-with-integrated-billing-and-national-roll-up)
  - [References](#references)
  - [AR Integration with National Roll-Up](#ar-integration-with-national-roll-up)
- [Scope of Accounts Receivable 4.5](#scope-of-accounts-receivable-45)
- [Accounts Receivable Files](#accounts-receivable-files)
- [Accounts Receivable Menu Structure and Option Definitions](#accounts-receivable-menu-structure-and-option-definitions)
  - [<u>Accounts Receivable Menu \[PRCAT USER\]</u>](#uaccounts-receivable-menu-prcat-useru)
  - [EDI Lockbox \[RCDPE EDI LOCKBOX MENU\]](#edi-lockbox-rcdpe-edi-lockbox-menu)
- [Accounts Receivable Cross-References](#accounts-receivable-cross-references)
- [Operating Specifics](#operating-specifics)
- [On-line Documentation](#on-line-documentation)
- [Appendix 1: AR Archiving Checklist and Troubleshooting Guide](#appendix-1-ar-archiving-checklist-and-troubleshooting-guide)
- [Appendix 2: FMS Documents](#appendix-2-fms-documents)
- [Glossary](#glossary)
This Accounts Receivable (AR) software has resulted from a separation of Accounts Receivable functions from the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) package. It allows Fiscal Service to manage the debt collection process at a VA facility.
BILLING/ESTABLISHING ACCOUNTS RECEIVABLE
Bills are generated using either the AR billing module, or the Integrated Billing (IB) package. Once approved at the service level, these bills are processed by an Accounts Receivable Clerk, and an Accounting Technician (exception: accrued bills such as Pharmacy Copay and Means Test bills are not audited by the Accounting Technician). Once the new Accounts Receivable processing of bills is completed, bills are automatically transmitted to the FMS system in Austin, Texas. It is at this point that the bills are considered "active" and subject to the debt collection process. All calculations of interest charges, administrative costs and payment schedules are handled by the AR system, as is the printing of patient statements and follow-up letters.
COLLECTIONS OF ACCOUNTS RECEIVABLE
Payments are entered via the Agent Cashier's menu. There are options to enter cash, check/money order, or credit card payments, and prepayments are easily accommodated. The AR system provides the Receipt Number Reconciliation Report option to allow the Agent Cashier to reconcile the payments recorded for a given day against funds actually collected. When reconciliation is completed, the Agent Cashier can then approve a payment batch. Once a payment batch is approved, it will be posted automatically overnight in a batch process. Any errors occurring during posting will be identified on the 215 Report.
PATIENT ACCOUNT PROFILING
The Agent Cashier menu also includes the ability to profile a patient type debtor's account. Rather than having to profile an individual Bill to determine the number and amounts of outstanding bills for a patient, the Agent Cashier can enter a patient's name, social security number, or a Bill number to view the profile of the entire patient account.
EDI LOCKBOX
This module was added in 2003 and updated for HIPAA 5010 in 2011. Electronic payment and remittance information is received from third party payers via the Financial Services Center (FSC). Processing of these payments is performed within the EDI Lockbox menu. This module is also referred to as ePayments.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPLEMENTATION

Before the Accounts Receivable software can run properly at your site, it requires certain start-up information. Once the software has been installed, setup your system by defining the following:

<u>Site Parameter Edit Menu \[PRCAF Supervisor Menu\]</u>

Use the following options in this sub -menu to define parameters for your site:

CBO Data Extract Parameters

EDI Lockbox Parameters

Group Parameters

Interest/Admin/Penalty Rates

RC Parameters

Statement Parameters

<u>Agency Location Code \[PRCAF Supervisor Menu\]</u>

Use this option to establish the Agency Location Code (ALC) for your site.

<u>Mail Groups</u>

The following mail groups should already be setup from previous versions of Accounts Receivable. If they are not, they need to be created for proper usage of version 4.5.

> *PRCA Adjustment Trans*

Enter appropriate users to this mail group who will receive electronic mail messages regarding Automatic Decrease Adjustment to Bills, balance discrepancies, and patient deaths.

> *IRS*

Enter appropriate users to this mail group necessary to monitor IRS transactions.

> *MDA*

This is the Medicare Deductible Alert (MDA) queue that will receive all the MDA transmissions from Austin.

> *PRCA ERROR*

This group is for the background job when it finds any corruption in the table files.

> *FMS*

Information from FMS in reference to FMS documents is sent to this fiscal mail group.

> *CARC_RARC_DATA*

This mail group receives and processes Claim Adjustment Reason Codes (CARC) and Remittance Advice Remark Codes (RARC) table updates.

> *RCDPE PAYMENTS*

This group receives bulletins and reports from AR Nightly Process and all EDI Lockbox jobs apart from exception processing.

> *RCDPE PAYMENTS EXCEPTIONS*

This group receives bulletins generated when errors are detected in incoming payment messages.

> *RCDPE PAYMENTS MGMT*

This group receives bulletins that are sent when a transferred message is accepted by another site.

> *RCDPE AUDIT*

This group receives bulletins from audited options within the EDI Lockbox menu and workload notifications for outstanding unprocessed EDI transaction from the AR Nightly Process.

> *RCDPE MOVE COPY*

This group receives bulletins from the AR Nightly Process of any inactive claim explanation of benefits (EOB) moved or copied in the prior 24 hours.

> *TCSP*

This mail group will receive confirmation and reject messages from AITC for Cross-Servicing transmissions. Three new domains have been added to support Cross-Servicing messaging. The Q‑TPC.VA.GOV domain will be used to transmit Cross-Servicing debt/bill referral transmissions from VistA to the AITC. The Q-TPL.VA.GOV domain will be used to transmit Due Process Notification (DPN) transmissions from VistA to the AITC. The Q-TPU.VA.GOV domain will be used for Un-processable file transmissions.

The TCSP mail group will also receive notifications when the batch run is completed and when a corrupted debtor record is found during the batch run. This functionality was created with Accounts Receivable patch, PRCA\*4.5\*327. See figures 1 – 3 below.

Figure 1: New mail messages created with PRCA\*4.5\*327

![](accounts-receivable-version-4-5-technical-manual-security-guide/002.png)

Figure 2: Batch Completion Notice

![](accounts-receivable-version-4-5-technical-manual-security-guide/003.png)

Figure 3: Failed Debtor Action Notice

![](accounts-receivable-version-4-5-technical-manual-security-guide/004.png)

<u>Accounts Receivable Nightly Process Background Job – PRCA NIGHTLY PROCESS</u>

The PRCA NIGHTLY PROCESS option should be queued to run daily at a recommended time of 2am. The following jobs are driven by the process.

1.  Verification of the following Accounts Receivable files.

> AR EVENT TYPE (#341.1)

> ACCOUNTS RECEIVABLE CATEGORY (#430.2)

> ACCOUNTS RECEIVABLE TRANS.TYPE (#430.3)

> If these files do not match what was distributed by the Accounts Receivable package, a MailMan bulletin, PRCA NIGHTLY PROCESS ABORT, is sent to the mail groups defined in the bulletin and the PRCA NIGHTLY PROCESS will stop.

2.  Interest and administrative charges are added to non -patient type bills.
3.  The CCPC Patient Statements are processed if it is five days before the site’s statement day. This includes setting OPEN status bills to a status of ACTIVE and setting OPEN prepayments to REFUND REVIEW if the bills are ready for REFUND REVIEW.
4.  Transmits Cross-Servicing documents.
5.  Statement days for non-patient type bills are set or reset.
6.  Receipts are checked for the following conditions:

> Receipt errored out during posting.

> Receipt has not been processed.

> Receipt is ready for posting.

> If any of these conditions exist, a MailMan message is sent to the PRCA ERROR mail group.

7.  Receipts older than seven years are purged.
8.  The IRS Master Code Sheets are created if the date is between November 21st and December 6th.
9.  The IRS Master Weekly Code Sheets are created if it is a Monday and it is not between July 24th and August 5th, or it is not between November 15th and January 21st.
10. IRS Pre-Offset Code Sheets will be created on July 25th.
11. Patient Statement events previous to the last two statements will be purged from the AR EVENT file.
12. A check will be made on the bill numbering series.
13. A check will be made on the event numbering series.
14. Deposit tickets are checked for errors and not being processed.
15. Deposit tickets are purged if processed and older than seven years.
16. AR FMS DOCUMENTS (#347) will be purged if ACCEPTED and older than 34 days.
17. OBRs over sixty days old are deleted.
18. The AR DATA COLLECTOR is run if it is the first day of the month.
19. The BAD DEBT REPORT is sent if it is the third workday of the month.
20. IG QUARTERLY REPORTS are sent on the 1st and 15th each quarter.
21. DMC 90 Day Masters are sent on the last Thursday of the month.
22. DMC 90 Day Weekly updates are sent on every Tuesday.
23. Uniform Billing forms and HCFA forms for the Reimbursable Health Insurance bills are printed after the first 45 days and 30 days and 60 days after the first 45 days on the device defined in Integrated Billing as the device for that form type.
24. Non-patient type bills are printed (e.g., ex-employee, employee, and vendor) on the device defined in the Report Printer in the AR Site Parameters.
25. IRS OFFSET letters are printed between Sept. 1st and Sept. 20th according to the DATE OF IRS OFFSET LETTER field (#3.02) in the AR SITE PARAMETER file (#342).
26. The Unprocessed Document List is printed on the Report Printer defined in the AR Site Parameters.
27. The Follow-up List is printed on the Report Printer defined in the AR Site Parameters.
28. The Comment List is printed on the Report Printer defined in the AR Site Parameters.

> If the process fails to complete, the user is notified when entering the Clerk’s AR Menu, and a MailMan message is sent to the PRCA ERROR and RCCPC STATEMENTS mail groups. To run the PRCA NIGHTLY PROCESS again, the user can enter the One-time Option Queue \[XU OPTION

> QUEUE\] option under the TaskMan Management menu \[XUTM MGR\]. The job should be run when no one is on the system.

29. EDI transactions are auto matched, and receipts created for processing to FMS. Payment deposit transactions (EFT) are matched to remittance advice transactions (ERA). Unmatched transactions are reported by bulletin to RCDPE PAYMENTS mail group.
30. EDI transactions are auto posted if the auto-posting parameter is on and ERAs meet certain criteria.
31. EDI transactions are auto-decreased if the auto-decrease parameter is on and ERAs meet certain criteria.
32. Workload Notification bulletins are reported to the RCDPE AUDIT mail group.
33. Moved or copied EOB transactions in the prior 24 hours are reported to the RCDPE MOVE COPY mail group.
34. Auto auditing of paper and electronic bills that meet specific criteria.

MAINTENANCE

Updating System Information

Once the implementation information has been defined for your system, the following Supervisor's AR options will allow you to maintain this information:

<u>Site Parameter Edit Menu</u>

> Use the options in this menu to define the following for your site:

CBO Data Extract Parameters Edit

Deactivate Group

EDI Lockbox Parameters

Group Parameters

Interest/Admin/Penalty Rates

RC Parameters Edit

Statement Parameters

## Other Maintenance Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Edit/Add ‘Bill Resulting From’ List</u>

An initial ‘Bill Resulting From’ list should be included with your software. Use this option to edit existing entries or add new ones.

<u>Delete an Incomplete Transaction</u>

Occasionally system failure may result in incomplete AR transactions. Use this option to remove such transactions and maintain system integrity.

<u>Edit Form Letters</u>

Under the Form Letter Menu, this option allows you to edit the text of a form letter. This is to be used only in the instance where District Counsel or VACO changes the wording or format before a scheduled release of Accounts Receivable.

<u>Bulletin</u>

This process runs nightly checking files 341.1(AR Event Type), 430.2 (Accounts Receivable Category), and 430.3 (Accounts Receivable Trans. Type). If errors are detected an error message is sent to users of the PRCA ERROR mail group and the background is prevented from running.

# Accounts Receivable Routines and Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accounts Receivable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accounts Receivable routines use the namespaces PRCA and RC. For all Accounts Receivable routines, the next letter(s) in the routine name also provide guidance as to the module to which that routine belongs. The breakdown of the Accounts Receivable internal namespaces is as follows:

| Routine | Description                                           |
|---------|-------------------------------------------------------|
| PRCA    | Accounts Receivable                                   |
| PRCAB   | Billing Routines                                      |
| PRCADR  | Address Routines                                      |
| PRCAF   | IB/FMS Routines                                       |
| PRCAG   | Patient Statement Routines                            |
| PRCAHIS | Transaction History Routines                          |
| PRCALT  | Collection Letter Routines                            |
| PRCANRU | National Roll-Up Routines for current NDB Software    |
| PRCAOFF | IRS Offset Routines                                   |
| PRCAPAY | Payment Routines                                      |
| PRCAT   | Compiled Template Routines                            |
| PRCAUT  | Utility Routines                                      |
| PRCAW   | Write off Routines                                    |
| PRCAX   | Medical Co-Pay Exemptions                             |
| PRCAY   | Agent Cashier Routines                                |
| PRY     | Accounts Receivable Patches, Conversions and Installs |
| RCAM    | Account Management Module                             |
| RCDP    | EDI Lockbox Module                                    |
| RCEV    | Event Driver Module                                   |
| RCMS    | Site Parameter Module                                 |
| RCTCS   | Cross Servicing Routines                              |
| RCY     | Agent Cashier Module                                  |

<span id="_Toc67391129" class="anchor"></span>Table 2: AR v4.5 Routines

The routines distributed with Accounts Receivable Version 4 .5 are listed and briefly described below.

<table>
<caption><p><span id="_Toc67391130" class="anchor"></span>Table 3: AR Mapped Routines</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCAACC</td>
<td>Calculates AR accrual totals</td>
</tr>
<tr class="even">
<td>PRCAADBO</td>
<td>This routine calculates admin/interest charges</td>
</tr>
<tr class="odd">
<td>PRCAADIN</td>
<td>This routine calculates admin/interest charges</td>
</tr>
<tr class="even">
<td>PRCAAPI</td>
<td>API for ASCD Project</td>
</tr>
<tr class="odd">
<td>PRCAAPR</td>
<td>This routine generates an account profile for an AR debtor.</td>
</tr>
<tr class="even">
<td>PRCAAPR1</td>
<td>Continuation of PRCAAPR</td>
</tr>
<tr class="odd">
<td>PRCAATR</td>
<td>This routine displays the transaction profile for a Bill.</td>
</tr>
<tr class="even">
<td>PRCABD</td>
<td>This routine displays/prints the Bill (1114, 1080, and 1081) generated by a service.</td>
</tr>
<tr class="odd">
<td>PRCABIL</td>
<td>This routine is used to create various cross-references for file 430.</td>
</tr>
<tr class="even">
<td>PRCABIL1</td>
<td>This routine is used to process the billing options -New Bill (Enter), Edit Bill, Cancel Bill, Pending Bills List, and Incomplete Bills List.</td>
</tr>
<tr class="odd">
<td>PRCABIL2</td>
<td>Continuation of PRCABIL1</td>
</tr>
<tr class="even">
<td>PRCABIL3</td>
<td>This routine is used to approve a Bill.</td>
</tr>
<tr class="odd">
<td>PRCABIL4</td>
<td>DELETE BILL LEAVING AUDIT TRAIL</td>
</tr>
<tr class="even">
<td>PRCABJ</td>
<td>Nightly process for accounts receivable</td>
</tr>
<tr class="odd">
<td>PRCABJ1</td>
<td>Nightly process for open Bill update</td>
</tr>
<tr class="even">
<td>PRCABJ2</td>
<td>Nightly process for open Bill update</td>
</tr>
<tr class="odd">
<td>PRCABJV</td>
<td>Verification for background</td>
</tr>
<tr class="even">
<td>PRCABP1</td>
<td>This routine prints a 1081 Bill</td>
</tr>
<tr class="odd">
<td>PRCABP2</td>
<td>This routine prints a 1080 Bill</td>
</tr>
<tr class="even">
<td>PRCABPF</td>
<td>This routine prints Bill forms</td>
</tr>
<tr class="odd">
<td>PRCACDRP</td>
<td>This routine shows PRCA Catastrophic Disability report</td>
</tr>
<tr class="even">
<td>PRCACLM</td>
<td>CALM code sheet generator</td>
</tr>
<tr class="odd">
<td>PRCACM</td>
<td>Comment adjustment transaction</td>
</tr>
<tr class="even">
<td>PRCACOL</td>
<td>Payment history report</td>
</tr>
<tr class="odd">
<td>PRCACV10</td>
<td>Compiles all print and input templates and cross references</td>
</tr>
<tr class="even">
<td>PRCADCDJ</td>
<td>This routine is a main routine to process District Counsel (DC) and Department of Justice (DOJ) transactions - Refer to DC/DOJ, Re-refer to DC/DOJ, and Returned from DC/DOJ.</td>
</tr>
<tr class="odd">
<td>PRCADCJ1</td>
<td>Continuation of PRCADCDJ</td>
</tr>
<tr class="even">
<td>PRCADEL</td>
<td>This routine prints the delinquent Accounts Receivable</td>
</tr>
<tr class="odd">
<td>PRCADIN</td>
<td>This routine deletes an incomplete transaction</td>
</tr>
<tr class="even">
<td>PRCADJ</td>
<td>This routine is used to adjust the principal balance Adjustment to AR</td>
</tr>
<tr class="odd">
<td>PRCADR</td>
<td>This routine displays items for the Accounts Receivable profile</td>
</tr>
<tr class="even">
<td>PRCADR1</td>
<td>Continuation of PRCADR</td>
</tr>
<tr class="odd">
<td>PRCADR2</td>
<td>Continuation of PRCADR1</td>
</tr>
<tr class="even">
<td>PRCADR3</td>
<td>This routine displays items for a Transaction Profile</td>
</tr>
<tr class="odd">
<td>PRCAEA</td>
<td>This routine acts as a lock for inactivate/reactivate vendors</td>
</tr>
<tr class="even">
<td>PRCAEA1</td>
<td>Continuation of PRCAEA</td>
</tr>
<tr class="odd">
<td>PRCAEIN</td>
<td>This routine is used to edit incomplete Accounts Receivable</td>
</tr>
<tr class="even">
<td>PRCAEOL</td>
<td>This routine is used to edit an incomplete old Accounts Receivable</td>
</tr>
<tr class="odd">
<td>PRCAEXM</td>
<td>This routine is used to adjust administrative costs</td>
</tr>
<tr class="even">
<td>PRCAFBD</td>
<td>Builds the FMS Billing Document</td>
</tr>
<tr class="odd">
<td>PRCAFBD1</td>
<td>FMS Billing Document utilities</td>
</tr>
<tr class="even">
<td>PRCAFBDM</td>
<td>Builds the FMS Modified Billing Document</td>
</tr>
<tr class="odd">
<td>PRCAFBDU</td>
<td>FMS utilities</td>
</tr>
<tr class="even">
<td>PRCAFDCT</td>
<td>View stacker information</td>
</tr>
<tr class="odd">
<td>PRCAFN</td>
<td>This routine supports various functions for IB package</td>
</tr>
<tr class="even">
<td>PRCAFN1</td>
<td>Functions to return AR data</td>
</tr>
<tr class="odd">
<td>PRCAFOR</td>
<td>Via a form from billing module</td>
</tr>
<tr class="even">
<td>PRCAFUT</td>
<td>FMS utilities</td>
</tr>
<tr class="odd">
<td>PRCAFUT1</td>
<td>FMS Utilities</td>
</tr>
<tr class="even">
<td>PRCAFWO</td>
<td>Builds the FMS Write-Off Document</td>
</tr>
<tr class="odd">
<td>PRCAG</td>
<td>This function reprints statement/letter option entries</td>
</tr>
<tr class="even">
<td>PRCAGD</td>
<td>Balance discrepancy message</td>
</tr>
<tr class="odd">
<td>PRCAGDR</td>
<td>Balance discrepancy report</td>
</tr>
<tr class="even">
<td>PRCAGDT</td>
<td>Balance discrepancy report text</td>
</tr>
<tr class="odd">
<td>PRCAGF</td>
<td>Prints form letters</td>
</tr>
<tr class="even">
<td>PRCAGF1</td>
<td>Continuation of PRCAGF</td>
</tr>
<tr class="odd">
<td>PRCAGP</td>
<td>Prints patient statement/letters</td>
</tr>
<tr class="even">
<td>PRCAGS</td>
<td>Patient statement</td>
</tr>
<tr class="odd">
<td>PRCAGST</td>
<td>Prints patient statements</td>
</tr>
<tr class="even">
<td>PRCAGST1</td>
<td>Prints patient statement bottom</td>
</tr>
<tr class="odd">
<td>PRCAGST2</td>
<td>Prints patient statement summary</td>
</tr>
<tr class="even">
<td>PRCAGT</td>
<td>Builds patient statement transaction list</td>
</tr>
<tr class="odd">
<td>PRCAGU</td>
<td>Patient statement utility</td>
</tr>
<tr class="even">
<td>PRCAHIS</td>
<td>Transaction history report</td>
</tr>
<tr class="odd">
<td>PRCAHIS1</td>
<td>Continuation of PRCAHIS</td>
</tr>
<tr class="even">
<td>PRCAHOL</td>
<td>This routine is used to place a hold on sending collection letters and removes the hold.</td>
</tr>
<tr class="odd">
<td>PRCAHV</td>
<td>API for My HealtheVet</td>
</tr>
<tr class="even">
<td>PRCAKBT</td>
<td>Builds temporary archive file</td>
</tr>
<tr class="odd">
<td>PRCAKBT1</td>
<td>Continuation of PRCAKBT</td>
</tr>
<tr class="even">
<td>PRCAKM</td>
<td>Marks as pending archive</td>
</tr>
<tr class="odd">
<td>PRCAKMR</td>
<td>Prints status of pending archive</td>
</tr>
<tr class="even">
<td>PRCAKS</td>
<td>Remove records-marked as archived</td>
</tr>
<tr class="odd">
<td>PRCAKTP</td>
<td>Purges temporary archive file</td>
</tr>
<tr class="even">
<td>PRCAKUN</td>
<td>Unmark pending archive</td>
</tr>
<tr class="odd">
<td>PRCALET</td>
<td>This routine is used to edit or print form letters</td>
</tr>
<tr class="even">
<td>PRCALM</td>
<td>Creates CALM code sheet for new transactions</td>
</tr>
<tr class="odd">
<td>PRCALST</td>
<td><p>This routine is used to print the following AR output:</p>
<p>Incomplete, Active, Written-Off, Returned, Referred to DC/DOJ, Referred to COWC.</p></td>
</tr>
<tr class="even">
<td>PRCALST1</td>
<td>This routine prints AR Category lists upon request. It includes an entry point to print just the C Means AR Category list.</td>
</tr>
<tr class="odd">
<td>PRCALT2</td>
<td>Continuation of PRCALT1A</td>
</tr>
<tr class="even">
<td>PRCAMARK</td>
<td>This routine marks a transaction as valid or invalid. Marking a transaction as invalid will prevent it from appearing on the patient statement.</td>
</tr>
<tr class="odd">
<td>PRCAMAS</td>
<td>This routine is used to print Fiscal/MAS reconciliation reports - Bill Incomplete, Suspended, and Complete (other than 3rd party Bill).</td>
</tr>
<tr class="even">
<td>PRCAMDA1</td>
<td>PRCA MDA WORKLIST SCREEN</td>
</tr>
<tr class="odd">
<td>PRCAMDA2</td>
<td>PRCA MDA MANAGEMENT WORKLIST SCREEN</td>
</tr>
<tr class="even">
<td>PRCAMDA3</td>
<td>PRCA MDA MANAGEMENT WORKLIST SCREEN</td>
</tr>
<tr class="odd">
<td>PRCAMDS</td>
<td>Server interface to AR from Austin</td>
</tr>
<tr class="even">
<td>PRCAMESG</td>
<td>This routine provides answers for “?” from Accounts Receivable routines</td>
</tr>
<tr class="odd">
<td>PRCAMRG</td>
<td>ROUTINE TO MERGE ENTRIES IN AR DEBTOR FILE FOR PATIENT MERGE</td>
</tr>
<tr class="even">
<td>PRCAMRKC</td>
<td>Checks mark/unmark transaction for account balance.</td>
</tr>
<tr class="odd">
<td>PRCANRU</td>
<td>This routine compiles and sends data to the National Roll-Up interface.</td>
</tr>
<tr class="even">
<td>PRCANRU0</td>
<td>Continuation of PRCANRU</td>
</tr>
<tr class="odd">
<td>PRCAOFF</td>
<td>This routine prints IRS Offset letters</td>
</tr>
<tr class="even">
<td>PRCAOFF1</td>
<td>This routine forwards IRS Offset letters to Austin</td>
</tr>
<tr class="odd">
<td>PRCAOFF2</td>
<td>This routine is a continuation of PRCAOFF1</td>
</tr>
<tr class="even">
<td>PRCAOFF3</td>
<td>This routine prints reports of IRS offset amounts</td>
</tr>
<tr class="odd">
<td>PRCAOLD</td>
<td>This routine establishes an old Accounts Receivable</td>
</tr>
<tr class="even">
<td>PRCAPAT</td>
<td>Assigns PAT ref #</td>
</tr>
<tr class="odd">
<td>PRCAPAT1</td>
<td>Continuation of PRCAPAT</td>
</tr>
<tr class="even">
<td>PRCAPAY</td>
<td>This routine is used to process payment transactions</td>
</tr>
<tr class="odd">
<td>PRCAPAY1</td>
<td>Continuation of PRCAPAY</td>
</tr>
<tr class="even">
<td>PRCAPAY2</td>
<td>Continuation of PRCAPAY1</td>
</tr>
<tr class="odd">
<td>PRCAPAY3</td>
<td>Continuation of PRCAPAY2</td>
</tr>
<tr class="even">
<td>PRCAPCL</td>
<td>Prints pending CALM code report</td>
</tr>
<tr class="odd">
<td>PRCAPRO</td>
<td>This routine is used to display/print a profile of an Accounts Receivable.</td>
</tr>
<tr class="even">
<td>PRCAPTR</td>
<td>Prints pending transaction</td>
</tr>
<tr class="odd">
<td>PRCAQUE</td>
<td>This routine is used to queue Accounts Receivable output and provides calls for date input</td>
</tr>
<tr class="even">
<td>PRCAREP</td>
<td>This routine prints the repayment profile</td>
</tr>
<tr class="odd">
<td>PRCAREPC</td>
<td>CATEGORY LIST-BILLS</td>
</tr>
<tr class="even">
<td>PRCAREPT</td>
<td>This routine prints the following AR reports: MAS Reconciliation Report, 3rd Party, Referred to DC/DOJ, DC Debt Collection and Contingent 3rd Party.</td>
</tr>
<tr class="odd">
<td>PRCARETN</td>
<td>This routine is used to return a Bill to service</td>
</tr>
<tr class="even">
<td>PRCARFD</td>
<td>This routine is used to review and approve bills with credit balances under the Refund, Review, and Approve menu option.</td>
</tr>
<tr class="odd">
<td>PRCARFD1</td>
<td>Approve refund and generate FMS document</td>
</tr>
<tr class="even">
<td>PRCARFD2</td>
<td>Generate FMS Document</td>
</tr>
<tr class="odd">
<td>PRCARFD3</td>
<td>List refunds to be approved</td>
</tr>
<tr class="even">
<td>PRCARFP</td>
<td>This routine prints the payments posted from the prepayment report</td>
</tr>
<tr class="odd">
<td>PRCARFU</td>
<td>This routine is the main utility routine for processing credit balances to a patient's account</td>
</tr>
<tr class="even">
<td>PRCARPM</td>
<td>This routine creates a multiple bill repayment schedule</td>
</tr>
<tr class="odd">
<td>PRCARPS</td>
<td>This routine prints a payment statement for AR with a repayment plan</td>
</tr>
<tr class="even">
<td>PRCARPS1</td>
<td>Continuation of PRCARPS</td>
</tr>
<tr class="odd">
<td>PRCARPU</td>
<td>Create multiple bill repayment schedule, part 2</td>
</tr>
<tr class="even">
<td>PRCASER</td>
<td>This routine accepts bills from the Integrated Billing package</td>
</tr>
<tr class="odd">
<td>PRCASER1</td>
<td>This routine accepts transactions from the Integrated Billing package</td>
</tr>
<tr class="even">
<td>PRCASET</td>
<td>This routine establishes a new Accounts Receivable</td>
</tr>
<tr class="odd">
<td>PRCASIG</td>
<td>This routine processes the electronic signature codes for AR</td>
</tr>
<tr class="even">
<td>PRCASVC</td>
<td>This routine is used to pass billing information from IB into the AR system</td>
</tr>
<tr class="odd">
<td>PRCASVC1</td>
<td>Continuation of PRCASVC.</td>
</tr>
<tr class="even">
<td>PRCASVC3</td>
<td>Continuation of PRCASVC2</td>
</tr>
<tr class="odd">
<td>PRCASVC6</td>
<td>Check out AR Bill</td>
</tr>
<tr class="even">
<td>PRCAUDT</td>
<td>This routine is used to audit a new electronic Bill</td>
</tr>
<tr class="odd">
<td>PRCAUDT1</td>
<td>Continuation of PRCAUDT</td>
</tr>
<tr class="even">
<td>PRCAUPD</td>
<td>This routine is used to update the following Accounts Receivable data -- Debtor's address, 3rd Party Information, and Locate the Debtor. This routine also runs the Refer to COWC option.</td>
</tr>
<tr class="odd">
<td>PRCAUT1</td>
<td>This is an AR utility routine that performs the following tasks applies a payment to multiple appropriations, edits Bill common numbering series, establishes a cross-reference for debtor and counts new bills.</td>
</tr>
<tr class="even">
<td>PRCAUT2</td>
<td>This routine calculates interest and administrative costs; updates interest and administrative balance, current status, and the maximum numbers of letters to be printed daily; and provides a count of bills returned from Fiscal.</td>
</tr>
<tr class="odd">
<td>PRCAUT3</td>
<td>This routine is used to enter/print a comment for an Accounts Receivable</td>
</tr>
<tr class="even">
<td>PRCAUTL</td>
<td>This routine is used to look up a Bill, check a debtor's active address, transfer fiscal year data between File #430 and File #433, and ask electronic signature.</td>
</tr>
<tr class="odd">
<td>PRCAWO</td>
<td>This routine is used to process a Full Waiver/Termination transaction</td>
</tr>
<tr class="even">
<td>PRCAWO1</td>
<td>This routine is used to charge administrative costs</td>
</tr>
<tr class="odd">
<td>PRCAWOF</td>
<td>This routine generates the AR Write-off report</td>
</tr>
<tr class="even">
<td>PRCAWREA</td>
<td>This routine reestablishes written-off bills</td>
</tr>
<tr class="odd">
<td>PRCAWV</td>
<td>This routine processes a Partial Waiver transaction</td>
</tr>
<tr class="even">
<td>PRCAX</td>
<td>Medication copay exemption</td>
</tr>
<tr class="odd">
<td>PRCAX1</td>
<td>Continuation of PRCAX</td>
</tr>
<tr class="even">
<td>PRCAXP</td>
<td>Prints RX copay exemption report</td>
</tr>
<tr class="odd">
<td>RCAEOB</td>
<td>AEOB FILE 433 CROSS-REF ROUTINE</td>
</tr>
<tr class="even">
<td>RCAM</td>
<td>Manager debtor information</td>
</tr>
<tr class="odd">
<td>RCAMADD</td>
<td>Gets debtor address</td>
</tr>
<tr class="even">
<td>RCAMDTH</td>
<td>Death notification for accounts receivable</td>
</tr>
<tr class="odd">
<td>RCAMFN01</td>
<td>Miscellaneous AR functions</td>
</tr>
<tr class="even">
<td>RCAMINS</td>
<td>CHECK FOR INSURANCE COMPANY AS DEBTOR,SECONDARY, OR TERTIARY CO</td>
</tr>
<tr class="odd">
<td>RCAMINS1</td>
<td>CHECK FOR INSURANCE COMPANY AS DEBTOR,SECONDARY, OR TERTIARY CO</td>
</tr>
<tr class="even">
<td>RCAMLET</td>
<td>Edits AR form letters</td>
</tr>
<tr class="odd">
<td>RCBDBBAL</td>
<td>bill balances check</td>
</tr>
<tr class="even">
<td>RCBDFST1</td>
<td>patient statement utilities continued</td>
</tr>
<tr class="odd">
<td>RCBDPSL1</td>
<td>patient statement top list manager routine</td>
</tr>
<tr class="even">
<td>RCBDPSLM</td>
<td>patient statement top list manager routine</td>
</tr>
<tr class="odd">
<td>RCBDPSNO</td>
<td>patient statement (remove transaction)</td>
</tr>
<tr class="even">
<td>RCBDXREF</td>
<td>fix cross references</td>
</tr>
<tr class="odd">
<td>RCBEADJ</td>
<td>Adjustment</td>
</tr>
<tr class="even">
<td>RCBEADJI</td>
<td>API FOR IB IN SETTLEMENT</td>
</tr>
<tr class="odd">
<td>RCBECHGA</td>
<td>add admin charges to account (called by rcbechgs)</td>
</tr>
<tr class="even">
<td>RCBECHGE</td>
<td>exempt interest/admin/penalty from bill</td>
</tr>
<tr class="odd">
<td>RCBECHGI</td>
<td>add interest charges to bill (called by rcbechgs)</td>
</tr>
<tr class="even">
<td>RCBECHGP</td>
<td>add penalty charges to bills (called by rcbechgs)</td>
</tr>
<tr class="odd">
<td>RCBECHGS</td>
<td>add charges to an account or bill (top routine)</td>
</tr>
<tr class="even">
<td>RCBECHGU</td>
<td>process the charges to bill (called by rcbechgs)</td>
</tr>
<tr class="odd">
<td>RCBEIB</td>
<td>integrated billing entry points</td>
</tr>
<tr class="even">
<td>RCBEPAY</td>
<td>payment processing (top routine)</td>
</tr>
<tr class="odd">
<td>RCBEPAY1</td>
<td>create a payment transaction cont</td>
</tr>
<tr class="even">
<td>RCBEPAY2</td>
<td>create a payment transaction cont</td>
</tr>
<tr class="odd">
<td>RCBEPAYC</td>
<td>check a payment before processing</td>
</tr>
<tr class="even">
<td>RCBEPAYF</td>
<td>first party payment processing (called by rcbepay)</td>
</tr>
<tr class="odd">
<td>RCBEPAYP</td>
<td>check and apply prepayment to bill</td>
</tr>
<tr class="even">
<td>RCBEREFU</td>
<td>refund utilities</td>
</tr>
<tr class="odd">
<td>RCBEUBI1</td>
<td>utilities for bills (in file 430)</td>
</tr>
<tr class="even">
<td>RCBEUBIL</td>
<td>utilities for bills (in file 430)</td>
</tr>
<tr class="odd">
<td>RCBEUDEB</td>
<td>utilities for debtors (in file 340)</td>
</tr>
<tr class="even">
<td>RCBEUTR1</td>
<td>add interest, admin charge or increase, decrease principal</td>
</tr>
<tr class="odd">
<td>RCBEUTR2</td>
<td>create an exempt transaction</td>
</tr>
<tr class="even">
<td>RCBEUTRA</td>
<td>utilities for transactions (in file 433)</td>
</tr>
<tr class="odd">
<td>RCBMILL</td>
<td>millennium bill report (generator)</td>
</tr>
<tr class="even">
<td>RCBMILL1</td>
<td>millennium bill report (payment detail)</td>
</tr>
<tr class="odd">
<td>RCBMILL2</td>
<td>millennium bill report (transactions)</td>
</tr>
<tr class="even">
<td>RCBMILL3</td>
<td>millennium bill report (summary)</td>
</tr>
<tr class="odd">
<td>RCBMILL4</td>
<td>millennium bill report (print history for date range)</td>
</tr>
<tr class="even">
<td>RCBMILLC</td>
<td>millennium bill (calculations top routine)</td>
</tr>
<tr class="odd">
<td>RCBMILLD</td>
<td>millennium bill (calculations internal set tmp)</td>
</tr>
<tr class="even">
<td>RCBMILLT</td>
<td>millennium bill (get TR data)</td>
</tr>
<tr class="odd">
<td>RCCPC0</td>
<td>Setup statement days for CCPC</td>
</tr>
<tr class="even">
<td>RCCPC1</td>
<td>Setups for CCPC</td>
</tr>
<tr class="odd">
<td>RCCPC2</td>
<td>Environment check for CCPC</td>
</tr>
<tr class="even">
<td>RCCPCBAK</td>
<td>AR UTILITY ROUTINE</td>
</tr>
<tr class="odd">
<td>RCCPCBJ</td>
<td>Background Driver for CCPC</td>
</tr>
<tr class="even">
<td>RCCPCFN</td>
<td>Function calls for CCPC</td>
</tr>
<tr class="odd">
<td>RCCPCML</td>
<td>Send CCPC transmission</td>
</tr>
<tr class="even">
<td>RCCPCML1</td>
<td>Send CCPC transmission (cont.)</td>
</tr>
<tr class="odd">
<td>RCCPCPS</td>
<td>Build Patient Statement File</td>
</tr>
<tr class="even">
<td>RCCPCPS1</td>
<td>build description for patient statement</td>
</tr>
<tr class="odd">
<td>RCCPCSE</td>
<td>CCPC Statements Errors</td>
</tr>
<tr class="even">
<td>RCCPCSTM</td>
<td>Patient Statement</td>
</tr>
<tr class="odd">
<td>RCCPCSV</td>
<td>Receive and Process CCPC messages</td>
</tr>
<tr class="even">
<td>RCCPCSV1</td>
<td>Receive and Process CCPC messages</td>
</tr>
<tr class="odd">
<td>RCCPCT</td>
<td>CCPC Statements totals</td>
</tr>
<tr class="even">
<td>RCCPW</td>
<td>Co-Pay waiver</td>
</tr>
<tr class="odd">
<td>RCCPW1</td>
<td>Co-Pay waiver background</td>
</tr>
<tr class="even">
<td>RCDMB1MT</td>
<td>REPAYMENT PLAN MONITOR</td>
</tr>
<tr class="odd">
<td>RCDMBWL1</td>
<td>diagnostic measures workload report (to clerk)</td>
</tr>
<tr class="even">
<td>RCDMBWL2</td>
<td>diagnostic measures workload report (to super)</td>
</tr>
<tr class="odd">
<td>RCDMBWLA</td>
<td>diagnostic measures workload report (build it) (Cont.)</td>
</tr>
<tr class="even">
<td>RCDMBWLR</td>
<td>diagnostic measures workload report (build it)</td>
</tr>
<tr class="odd">
<td>RCDMC90</td>
<td>DMC 90 DAY</td>
</tr>
<tr class="even">
<td>RCDMC90S</td>
<td>DMC 90 DAY (SERVER)</td>
</tr>
<tr class="odd">
<td>RCDMC90U</td>
<td>DMC 90 DAY</td>
</tr>
<tr class="even">
<td>RCDMCEDT</td>
<td>Enter/Edit DMC Debt Valid Field</td>
</tr>
<tr class="odd">
<td>RCDMCR1A</td>
<td>DMC Debt Validity Report</td>
</tr>
<tr class="even">
<td>RCDMCR1B</td>
<td>DMC Debt Validity Report - Collect Data</td>
</tr>
<tr class="odd">
<td>RCDMCR2A</td>
<td>DMC Debt Validity Management Report</td>
</tr>
<tr class="even">
<td>RCDMCR2B</td>
<td>DMC Debt Validity Management Report - Collect Data</td>
</tr>
<tr class="odd">
<td>RCDMCR3A</td>
<td>DMC Rated Disability Eligibility Change Report</td>
</tr>
<tr class="even">
<td>RCDMCR3B</td>
<td>DMC Rated Disability Elig Change - Collect Data</td>
</tr>
<tr class="odd">
<td>RCDMCR4A</td>
<td>DMC 0-40 Percent SC Change Reconciliation Report</td>
</tr>
<tr class="even">
<td>RCDMCR4B</td>
<td>DMC 0-40 Percent SC Change Reconciliation Report</td>
</tr>
<tr class="odd">
<td>RCDMCR5A</td>
<td>DMC First Party Charge IB Cancellation Recon Report</td>
</tr>
<tr class="even">
<td>RCDMCR5B</td>
<td>DMC First Party Charge IB Cancellation Recon Report</td>
</tr>
<tr class="odd">
<td>RCDMCR6A</td>
<td>50-100 Percent SC Exempt Charge Reconciliation Report</td>
</tr>
<tr class="even">
<td>RCDMCR6B</td>
<td>50-100 Percent SC Exempt Charge Reconciliation Report</td>
</tr>
<tr class="odd">
<td>RCDMCR7A</td>
<td>10-40% SC Medical Care Copayment Exempt Charge Reconciliation Report</td>
</tr>
<tr class="even">
<td>RCDMCR7B</td>
<td>10-40% SC Medical Care Copayment Exempt Charge Reconciliation Report</td>
</tr>
<tr class="odd">
<td>RCDMCUT1</td>
<td>Utility Functions for Hold Debt to DMC Project</td>
</tr>
<tr class="even">
<td>RCDMCUT2</td>
<td>Utility Functions for Hold Debt to DMC Project</td>
</tr>
<tr class="odd">
<td>RCDPAPL1</td>
<td>account profile list manager options</td>
</tr>
<tr class="even">
<td>RCDPAPLI</td>
<td>account profile top list manager init</td>
</tr>
<tr class="odd">
<td>RCDPAPLM</td>
<td>account profile top list manager routine</td>
</tr>
<tr class="even">
<td>RCDPAPST</td>
<td>account profile bill status select</td>
</tr>
<tr class="odd">
<td>RCDPARC</td>
<td>CARC Report on Payer OR CARC Code</td>
</tr>
<tr class="even">
<td>RCDPARC1</td>
<td>CARC Report on Payer OR CARC Code</td>
</tr>
<tr class="odd">
<td>RCDPAYER</td>
<td>TPJI Utility</td>
</tr>
<tr class="even">
<td>RCDPBPL1</td>
<td>bill profile options</td>
</tr>
<tr class="odd">
<td>RCDPBPLI</td>
<td>bill profile (build array contract/employee/vendor)</td>
</tr>
<tr class="even">
<td>RCDPBPLM</td>
<td>bill profile</td>
</tr>
<tr class="odd">
<td>RCDPBTL1</td>
<td>bill transaction options</td>
</tr>
<tr class="even">
<td>RCDPBTLM</td>
<td>bill transactions List Manager top routine</td>
</tr>
<tr class="odd">
<td>RCDPCON</td>
<td>Confirm a Deposit Ticket</td>
</tr>
<tr class="even">
<td>RCDPCRE</td>
<td>Create a Deposit Ticket</td>
</tr>
<tr class="odd">
<td>RCDPCSA</td>
<td>TCSP FLAG CONTROL menu option &amp; RCDP TCSP FLAG security key (PRCA*4.5*325)</td>
</tr>
<tr class="even">
<td>RCDPDEP</td>
<td>Deposit Ticket</td>
</tr>
<tr class="odd">
<td>RCDPDPL1</td>
<td>deposit profile list manager options</td>
</tr>
<tr class="even">
<td>RCDPDPLM</td>
<td>deposit profile list manager top routine</td>
</tr>
<tr class="odd">
<td>RCDPDPLU</td>
<td>deposit profile utilities</td>
</tr>
<tr class="even">
<td>RCDPDRV1</td>
<td>Add alert</td>
</tr>
<tr class="odd">
<td>RCDPE215</td>
<td>SF215 EDI Lockbox Summary Report</td>
</tr>
<tr class="even">
<td>RCDPE8NZ</td>
<td>Unapplied EFT Deposits report</td>
</tr>
<tr class="odd">
<td>RCDPEAA1</td>
<td>AUTO POST AWAITING RESOLUTION (APAR) - LIST OF UNPOSTED EEOBs</td>
</tr>
<tr class="even">
<td>RCDPEAA2</td>
<td>APAR Screen - SELECTED EOB</td>
</tr>
<tr class="odd">
<td>RCDPEAA3</td>
<td>APAR Screen - callable entry points</td>
</tr>
<tr class="even">
<td>RCDPEAC</td>
<td>ACTIVE BILLS WITH EEOB ON FILE</td>
</tr>
<tr class="odd">
<td>RCDPEAD</td>
<td>AUTO DECREASE</td>
</tr>
<tr class="even">
<td>RCDPEAD1</td>
<td>AUTO DECREASE REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEAD2</td>
<td>AUTO DECREASE REPORT</td>
</tr>
<tr class="even">
<td>RCDPEAD3</td>
<td>AUTO DECREASE REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEADP</td>
<td>AUTO-DECREASE REPORT</td>
</tr>
<tr class="even">
<td>RCDPEAP</td>
<td>AUTO POST MATCHING EFT ERA PAIR</td>
</tr>
<tr class="odd">
<td>RCDPEAP1</td>
<td>AUTO POST MATCHING EFT ERA PAIR - CONT</td>
</tr>
<tr class="even">
<td>RCDPEAPP</td>
<td>AUTO POST REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEAPQ</td>
<td>AUTO POST REPORT</td>
</tr>
<tr class="even">
<td>RCDPEAPS</td>
<td>ERA STATUS CHANGE AUDIT REPORTR</td>
</tr>
<tr class="odd">
<td>RCDPEAR</td>
<td>ELECTRONIC ERA AGING REPORTS FROM NIGHTLY JOB</td>
</tr>
<tr class="even">
<td>RCDPEAR1</td>
<td>ELECTRONIC ERA AGING REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEAR2</td>
<td>EFT Unmatched Aging Report</td>
</tr>
<tr class="even">
<td>RCDPEAR3</td>
<td>ERA Unmatched Aging Report</td>
</tr>
<tr class="odd">
<td>RCDPEARL</td>
<td>Misc. Report utilities for List Manager</td>
</tr>
<tr class="even">
<td>RCDPECH</td>
<td>Receipt Comment History</td>
</tr>
<tr class="odd">
<td>RCDPEDA1</td>
<td>DAILY ACTIVITY REPORT HEADER</td>
</tr>
<tr class="even">
<td>RCDPEDA2</td>
<td>DAILY ACTIVITY REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEDA3</td>
<td>DAILY ACTIVITY REPORT</td>
</tr>
<tr class="even">
<td>RCDPEDA4</td>
<td>DAILY ACTIVITY REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEDAR</td>
<td>DAILY ACTIVITY REPORT</td>
</tr>
<tr class="even">
<td>RCDPEDS</td>
<td>Display EEOB detail from receipt</td>
</tr>
<tr class="odd">
<td>RCDPEDT</td>
<td>Edit Deposit Ticket.</td>
</tr>
<tr class="even">
<td>RCDPEE</td>
<td>Select Partially Matched EFTs</td>
</tr>
<tr class="odd">
<td>RCDPEFA1</td>
<td>First Party Auto-Decrease Adjustment Report</td>
</tr>
<tr class="even">
<td>RCDPEFA2</td>
<td>First Party Auto-Decrease Adjustment Report</td>
</tr>
<tr class="odd">
<td>RCDPEFA3</td>
<td>1ST PARTY AUTO DECREASE VS MANUAL DECREASE REPORT</td>
</tr>
<tr class="even">
<td>RCDPEFA4</td>
<td>1ST PARTY AUTO DECREASE VS MANUAL DECREASE REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEFTL</td>
<td>Locked EFT Report</td>
</tr>
<tr class="even">
<td>RCDPELA1</td>
<td>AUTO POSTED RECEIPT REPORT</td>
</tr>
<tr class="odd">
<td>RCDPELAR</td>
<td>AUTO POSTED RECEIPT REPORT</td>
</tr>
<tr class="even">
<td>RCDPEM</td>
<td>POST EFT, ERA MATCHING TO EFT</td>
</tr>
<tr class="odd">
<td>RCDPEM0</td>
<td>ERA MATCHING TO EFT (continued)</td>
</tr>
<tr class="even">
<td>RCDPEM1</td>
<td>ERA MATCH TO EFT (continued)</td>
</tr>
<tr class="odd">
<td>RCDPEM2</td>
<td>MANUAL ERA AND EFT MATCHING</td>
</tr>
<tr class="even">
<td>RCDPEM21</td>
<td>MANUAL ERA AND EFT MATCHING</td>
</tr>
<tr class="odd">
<td>RCDPEM3</td>
<td>ERA AUDIT REPORT and return EFT function</td>
</tr>
<tr class="even">
<td>RCDPEM4</td>
<td>EPAYMENTS AUDIT REPORTS</td>
</tr>
<tr class="odd">
<td>RCDPEM41</td>
<td>EPAYMENTS AUDIT REPORTS - Cont.</td>
</tr>
<tr class="even">
<td>RCDPEM5</td>
<td>EPAYMENTS MOVE EEOB TO NEW CLAIMS</td>
</tr>
<tr class="odd">
<td>RCDPEM6</td>
<td>DUPLICATE EFT DEPOSITS AUDIT REPORTS</td>
</tr>
<tr class="even">
<td>RCDPEM7</td>
<td>OVERDUE EFT AND ERA BULLETINS</td>
</tr>
<tr class="odd">
<td>RCDPEM8</td>
<td>EOB MOVE/COPY BULLETINS</td>
</tr>
<tr class="even">
<td>RCDPEM9</td>
<td>PAYER SELECTION</td>
</tr>
<tr class="odd">
<td>RCDPEMA</td>
<td>AUTO-POSTING RECEIPT CREATION</td>
</tr>
<tr class="even">
<td>RCDPEMA1</td>
<td>LIST ALL AUTO-POSTED RECEIPTS REPORT</td>
</tr>
<tr class="odd">
<td>RCDPEMAP</td>
<td>AUTO-POSTED RECEIPT REPORT</td>
</tr>
<tr class="even">
<td>RCDPEMB</td>
<td>AUTO-POSTING RECEIPT CREATION</td>
</tr>
<tr class="odd">
<td>RCDPENR1</td>
<td>835-837 Summary Report</td>
</tr>
<tr class="even">
<td>RCDPENR2</td>
<td>EFT/ERA Trending Report</td>
</tr>
<tr class="odd">
<td>RCDPENR3</td>
<td>EFT/ERA Trending Report</td>
</tr>
<tr class="even">
<td>RCDPENR4</td>
<td>EFT/ERA Trending Report</td>
</tr>
<tr class="odd">
<td>RCDPENRU</td>
<td>AR DM Data Extraction</td>
</tr>
<tr class="even">
<td>RCDPEP</td>
<td>Flag Payers as Pharmacy</td>
</tr>
<tr class="odd">
<td>RCDPEREC</td>
<td>RECONCILIATION REPORT FOR EDI LOCKBOX FMS DOCS</td>
</tr>
<tr class="even">
<td>RCDPES10</td>
<td>ERA return file field captions</td>
</tr>
<tr class="odd">
<td>RCDPESP</td>
<td>ePayment Lockbox Site Parameters Definition</td>
</tr>
<tr class="even">
<td>RCDPESP1</td>
<td>ePayment Lockbox Site Parameter Reports</td>
</tr>
<tr class="odd">
<td>RCDPESP2</td>
<td>ePayment Lockbox Parameter Audit and Exclusion Reports</td>
</tr>
<tr class="even">
<td>RCDPESP3</td>
<td>ePayment Lockbox Exclusion Audit Report</td>
</tr>
<tr class="odd">
<td>RCDPESP4</td>
<td>ePayment Auto-post/Decrease for IOC testing</td>
</tr>
<tr class="even">
<td>RCDPESP5</td>
<td>ePayment Lockbox Site Parameter Definition – Files 344.71</td>
</tr>
<tr class="odd">
<td>RCDPESP6</td>
<td>ePayment Lockbox Site Parameter Definition – Notify Changes</td>
</tr>
<tr class="even">
<td>RCDPESP7</td>
<td>ePayment Lockbox Site Parameter Definition – Auto-Decrease</td>
</tr>
<tr class="odd">
<td>RCDPESP8</td>
<td>EDI Lockbox Site Parameter History Report</td>
</tr>
<tr class="even">
<td>RCDPESPA</td>
<td>EDI Lockbox Parameter Audit Report</td>
</tr>
<tr class="odd">
<td>RCDPESPB</td>
<td>ePayment Lockbox Site Parameter Definition</td>
</tr>
<tr class="even">
<td>RCDPESR0</td>
<td>Server auto-update utilities - EDI Lockbox</td>
</tr>
<tr class="odd">
<td>RCDPESR1</td>
<td>Server interface to AR from Austin</td>
</tr>
<tr class="even">
<td>RCDPESR2</td>
<td>Server auto-upd - EDI Lockbox</td>
</tr>
<tr class="odd">
<td>RCDPESR3</td>
<td>Server auto-update utilities - EDI Lockbox</td>
</tr>
<tr class="even">
<td>RCDPESR4</td>
<td>Server interface 835ERA processing</td>
</tr>
<tr class="odd">
<td>RCDPESR5</td>
<td>Server interface 835XFR processing</td>
</tr>
<tr class="even">
<td>RCDPESR6</td>
<td>Server auto-update file 344.4</td>
</tr>
<tr class="odd">
<td>RCDPESR8</td>
<td>EFT return file field captions</td>
</tr>
<tr class="even">
<td>RCDPESR9</td>
<td>ERA return file field captions</td>
</tr>
<tr class="odd">
<td>RCDPESRM</td>
<td>835ERA matching</td>
</tr>
<tr class="even">
<td>RCDPESRV</td>
<td>Server interface to AR from Austin</td>
</tr>
<tr class="odd">
<td>RCDPETR</td>
<td>EOB TRANSFER IN/TRANSFER OUT REPORTS</td>
</tr>
<tr class="even">
<td>RCDPETT</td>
<td>payments Testing Tool</td>
</tr>
<tr class="odd">
<td>RCDPETTE</td>
<td>EDI Testing Tool ERA actions</td>
</tr>
<tr class="even">
<td>RCDPETTF</td>
<td>EDI Testing Tool EFT actions</td>
</tr>
<tr class="odd">
<td>RCDPETTM</td>
<td>EDI Testing Tool MRA actions</td>
</tr>
<tr class="even">
<td>RCDPETTP</td>
<td>EDI Testing Tool</td>
</tr>
<tr class="odd">
<td>RCDPETTQ</td>
<td>EDI Testing Tool QUICK actions</td>
</tr>
<tr class="even">
<td>RCDPETTU</td>
<td>EDI Testing Tool Utilities</td>
</tr>
<tr class="odd">
<td>RCDPEUPO</td>
<td>Unposted EFT Override</td>
</tr>
<tr class="even">
<td>RCDPEU</td>
<td>ELECTRONIC ERA UTILITIES</td>
</tr>
<tr class="odd">
<td>RCDPEU1</td>
<td>Electronic Payer Utilities</td>
</tr>
<tr class="even">
<td>RCDPEU2</td>
<td>Electronic Payer Utilities</td>
</tr>
<tr class="odd">
<td>RCDPEV</td>
<td>EDI LOCKBOX WORKLIST VERIFY PAYMENTS</td>
</tr>
<tr class="even">
<td>RCDPEV0</td>
<td>EDI LOCKBOX WORKLIST VERIFY PAYMENTS</td>
</tr>
<tr class="odd">
<td>RCDPEWL</td>
<td>ELECTRONIC EOB MESSAGE WORKLIST</td>
</tr>
<tr class="even">
<td>RCDPEWL0</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="odd">
<td>RCDPEWL1</td>
<td>ELECTRONIC EOB WORKLIST SCREEN</td>
</tr>
<tr class="even">
<td>RCDPEWL2</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="odd">
<td>RCDPEWL3</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="even">
<td>RCDPEWL4</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="odd">
<td>RCDPEWL5</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="even">
<td>RCDPEWL6</td>
<td>ELECTRONIC EOB WORKLIST ACTIONS</td>
</tr>
<tr class="odd">
<td>RCDPEWL7</td>
<td>EDI LOCKBOX WORKLIST ERA DISPLAY SCREEN</td>
</tr>
<tr class="even">
<td>RCDPEWL8</td>
<td>EDI LOCKBOX WORKLIST ERA LEVEL</td>
</tr>
<tr class="odd">
<td>RCDPEWLA</td>
<td>ELECTRONIC EOB MESSAGE WORKLIST</td>
</tr>
<tr class="even">
<td>RCDPEWLB</td>
<td>EEOB WORKLIST BATCH PROCESSING</td>
</tr>
<tr class="odd">
<td>RCDPEWLP</td>
<td>EDI LOCKBOX ERA and EEOB WORKLIST procedures</td>
</tr>
<tr class="even">
<td>RCDPEWLC</td>
<td>EEOB WORKLIST BATCH PROCESSING</td>
</tr>
<tr class="odd">
<td>RCDPEWLD</td>
<td>Continuation of routine RCDPEWL0</td>
</tr>
<tr class="even">
<td>RCDPEWLZ</td>
<td>Block Auto-Decrease Protocol</td>
</tr>
<tr class="odd">
<td>RCDPEX</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING – FILE 344.5</td>
</tr>
<tr class="even">
<td>RCDPEX0</td>
<td>837 EDI RETURN MSG EXTRACT MAIN LIST TEMPLATE</td>
</tr>
<tr class="odd">
<td>RCDPEX1</td>
<td>ELECTRONIC EOB MESSAGE EXCEPTIONS PROCESS</td>
</tr>
<tr class="even">
<td>RCDPEX2</td>
<td>ELECTRONIC EOB DETAIL EXCEPTION MAIN LIST TEMPLATE</td>
</tr>
<tr class="odd">
<td>RCDPEX3</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING – FILE 344.4</td>
</tr>
<tr class="even">
<td>RCDPEX31</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING – FILE 344.4</td>
</tr>
<tr class="odd">
<td>RCDPEX32</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING – FILE 344.4</td>
</tr>
<tr class="even">
<td>RCDPEX4</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING</td>
</tr>
<tr class="odd">
<td>RCDPEX5</td>
<td>ELECTRONIC EOB EXCEPTION PROCESSING</td>
</tr>
<tr class="even">
<td>RCDPFMS</td>
<td>Post Deposit Ticket to FMS</td>
</tr>
<tr class="odd">
<td>RCDPFN01</td>
<td>Miscellaneous Deposit functions</td>
</tr>
<tr class="even">
<td>RCDPLPL1</td>
<td>link payments list manager options</td>
</tr>
<tr class="odd">
<td>RCDPLPL2</td>
<td>link payments list manager options</td>
</tr>
<tr class="even">
<td>RCDPLPL3</td>
<td>link payments list manager options (link payment)</td>
</tr>
<tr class="odd">
<td>RCDPLPL4</td>
<td>Multiple Bill Link Payments</td>
</tr>
<tr class="even">
<td>RCDPLPLM</td>
<td>link payments list manager top routine</td>
</tr>
<tr class="odd">
<td>RCDPLPS2</td>
<td>Link Payment Tracking Report</td>
</tr>
<tr class="even">
<td>RCDPLPSR</td>
<td>link payments suspense report</td>
</tr>
<tr class="odd">
<td>RCDPLST</td>
<td>Listing for Deposit Tickets.</td>
</tr>
<tr class="even">
<td>RCDPPLB</td>
<td>ERA/Provider Level Adjustment Report</td>
</tr>
<tr class="odd">
<td>RCDPR215</td>
<td>receipt processing sf215 report</td>
</tr>
<tr class="even">
<td>RCDPRECT</td>
<td>print a receipt</td>
</tr>
<tr class="odd">
<td>RCDPRLIS</td>
<td>list of receipts report</td>
</tr>
<tr class="even">
<td>RCDPRPL1</td>
<td>receipt profile list manager options</td>
</tr>
<tr class="odd">
<td>RCDPRPL2</td>
<td>receipt profile list manager options</td>
</tr>
<tr class="even">
<td>RCDPRPL3</td>
<td>receipt profile list manager options</td>
</tr>
<tr class="odd">
<td>RCDPRPL4</td>
<td>receipt profile list manager options</td>
</tr>
<tr class="even">
<td>RCDPRPLM</td>
<td>receipt profile list manager top routine</td>
</tr>
<tr class="odd">
<td>RCDPRPLU</td>
<td>receipt profile utilities</td>
</tr>
<tr class="even">
<td>RCDPRSEA</td>
<td>extended search</td>
</tr>
<tr class="odd">
<td>RCDPRTP</td>
<td>CLAIMS MATCHING REPORT</td>
</tr>
<tr class="even">
<td>RCDPRTP0</td>
<td>CLAIMS MATCHING REPORT</td>
</tr>
<tr class="odd">
<td>RCDPRTP1</td>
<td>CLAIMS MATCHING REPORT (PRINT)</td>
</tr>
<tr class="even">
<td>RCDPRTP2</td>
<td>CLAIMS MATCHING REPORT</td>
</tr>
<tr class="odd">
<td>RCDPRU</td>
<td>CARC Report on Payer or CARC Code</td>
</tr>
<tr class="even">
<td>RCDPRU2</td>
<td>CARC Report on Payer or CARC Code</td>
</tr>
<tr class="odd">
<td>RCDPTAR</td>
<td>EFT Transaction Audit Report</td>
</tr>
<tr class="even">
<td>RCDPTAR1</td>
<td>EFT Transaction Audit Report</td>
</tr>
<tr class="odd">
<td>RCDPTPLI</td>
<td>transaction profile init to build array</td>
</tr>
<tr class="even">
<td>RCDPTPLM</td>
<td>transaction profile list manager top routine</td>
</tr>
<tr class="odd">
<td>RCDPUDEP</td>
<td>deposit utilities</td>
</tr>
<tr class="even">
<td>RCDPURE1</td>
<td>process a receipt</td>
</tr>
<tr class="odd">
<td>RCDPUREC</td>
<td>receipt utilities</td>
</tr>
<tr class="even">
<td>RCDPURED</td>
<td>file 344 receipt/payment dd calls</td>
</tr>
<tr class="odd">
<td>RCDPURET</td>
<td>receipt utilities (transactions)</td>
</tr>
<tr class="even">
<td>RCDPUT</td>
<td>Utilities</td>
</tr>
<tr class="odd">
<td>RCDPVDP</td>
<td>Void a Deposit</td>
</tr>
<tr class="even">
<td>RCDPVW</td>
<td>View a Deposit Ticket</td>
</tr>
<tr class="odd">
<td>RCDPXFIM</td>
<td>generate mail message for removing duplicate deposit</td>
</tr>
<tr class="even">
<td>RCDPXFIX</td>
<td>fix duplicate deposits</td>
</tr>
<tr class="odd">
<td>RCDPXPA1</td>
<td>server, utilities for transmission file 344.2</td>
</tr>
<tr class="even">
<td>RCDPXPAM</td>
<td>auto process payments, message generation</td>
</tr>
<tr class="odd">
<td>RCDPXPAP</td>
<td>automatically process the deposits</td>
</tr>
<tr class="even">
<td>RCDPXPAY</td>
<td>server top to receive electronic payments</td>
</tr>
<tr class="odd">
<td>RCEVDD1</td>
<td>Process event driver DD fields</td>
</tr>
<tr class="even">
<td>RCEVDRV1</td>
<td>Adds event to enter file driver</td>
</tr>
<tr class="odd">
<td>RCEVGEN</td>
<td>Account management adjustment</td>
</tr>
<tr class="even">
<td>RCEVUTL</td>
<td>Generic event utilities</td>
</tr>
<tr class="odd">
<td>RCEVUTL1</td>
<td>Generic event utilities</td>
</tr>
<tr class="even">
<td>RCEXINAD</td>
<td>Exempt int/admin for Katrina victims from 9/1/05</td>
</tr>
<tr class="odd">
<td>RCFMCAF</td>
<td>Conversion AR ACCTG Fields RPT</td>
</tr>
<tr class="even">
<td>RCFMDRV1</td>
<td>Add FMS Document</td>
</tr>
<tr class="odd">
<td>RCFMFN02</td>
<td>Return information for FMS Document processing</td>
</tr>
<tr class="even">
<td>RCFMOBR</td>
<td>Bill reconciliation list</td>
</tr>
<tr class="odd">
<td>RCFMOBR1</td>
<td>BILL RECONCILIATIONS LIST</td>
</tr>
<tr class="even">
<td>RCFMOBR2</td>
<td>BILL RECONCILIATIONS LIST</td>
</tr>
<tr class="odd">
<td>RCFMOBR3</td>
<td>BILL RECONCILIATIONS LIST</td>
</tr>
<tr class="even">
<td>RCFMPUR</td>
<td>Purge AR Documents to FMS</td>
</tr>
<tr class="odd">
<td>RCFMUDL</td>
<td>Unprocessed document list</td>
</tr>
<tr class="even">
<td>RCFN01</td>
<td>Miscellaneous AR functions</td>
</tr>
<tr class="odd">
<td>RCHRFS</td>
<td>High Risk for Suicide Patients Report</td>
</tr>
<tr class="even">
<td>RCHRFS1</td>
<td>High Risk for Suicide Patients Report</td>
</tr>
<tr class="odd">
<td>RCHRFS2</td>
<td>High Risk for Suicide Patients Report</td>
</tr>
<tr class="even">
<td>RCHRFSUT</td>
<td>High Risk for Suicide Patients Report Utilities</td>
</tr>
<tr class="odd">
<td>RCJIBFN1</td>
<td>FUNC. CALLS FOR JOINT IB/AR</td>
</tr>
<tr class="even">
<td>RCJIBFN2</td>
<td>FUNC. CALLS FOR JOINT IB/AR</td>
</tr>
<tr class="odd">
<td>RCJIBFN3</td>
<td>COMMENT ADJUSTMENT TRANSACTION</td>
</tr>
<tr class="even">
<td>RCKATP</td>
<td>ADJUST ACCOUNTS FOR KATRINA VETS</td>
</tr>
<tr class="odd">
<td>RCKATPD</td>
<td>ADJUST ACCOUNTS FOR KATRINA VETS (CON'T)</td>
</tr>
<tr class="even">
<td>RCKATRPT</td>
<td>KATRINA FINANCIAL STATEMENT REPORT</td>
</tr>
<tr class="odd">
<td>RCMRGFIX</td>
<td>ROUTINE TO FIX DUPLICATE ENTRIES IN DEBTOR FILE</td>
</tr>
<tr class="even">
<td>RCMSDD1</td>
<td>Process DD site fields</td>
</tr>
<tr class="odd">
<td>RCMSFN01</td>
<td>Miscellaneous site functions</td>
</tr>
<tr class="even">
<td>RCMSITE</td>
<td>Edit site parameters</td>
</tr>
<tr class="odd">
<td>RCMSNUM</td>
<td>Assign Common Numbering Series</td>
</tr>
<tr class="even">
<td>RCNRIG</td>
<td>IG REPORTS</td>
</tr>
<tr class="odd">
<td>RCNR4</td>
<td>National Roll-up count bill</td>
</tr>
<tr class="even">
<td>RCNR4A</td>
<td>NRU data collector 2</td>
</tr>
<tr class="odd">
<td>RCNR4P</td>
<td>National Roll-Up report</td>
</tr>
<tr class="even">
<td>RCNR4T</td>
<td>National Roll-Up (Count transactions)</td>
</tr>
<tr class="odd">
<td>RCNRBD</td>
<td>Performs calculations for current bad debt allowance</td>
</tr>
<tr class="even">
<td>RCNRBD1</td>
<td>Performs calculations for current bad debt allowance</td>
</tr>
<tr class="odd">
<td>RCNRSUM</td>
<td>National Roll-Up Summary Documents</td>
</tr>
<tr class="even">
<td>RCNRSUM1</td>
<td>Retransmit NDB to FMS</td>
</tr>
<tr class="odd">
<td>RCRCAC</td>
<td>RC TRANSACTION CODE LIST</td>
</tr>
<tr class="even">
<td>RCRCACP</td>
<td>RC THIRD PARTY REFERRAL ACTION CODE LIST</td>
</tr>
<tr class="odd">
<td>RCRCAL</td>
<td>RC VIEW BILL LIST</td>
</tr>
<tr class="even">
<td>RCRCAL1</td>
<td>TP REFERRAL ACTION LIST BUILD</td>
</tr>
<tr class="odd">
<td>RCRCAL2</td>
<td>RC ACTION BILL LIST SORT BUILD</td>
</tr>
<tr class="even">
<td>RCRCALB</td>
<td>RC FOLLOW-UP ACTION LIST BUILD</td>
</tr>
<tr class="odd">
<td>RCRCALE</td>
<td>TP REFERRAL ACTION SEL/MOD LIST BUILD</td>
</tr>
<tr class="even">
<td>RCRCAT</td>
<td>AR/RC AR TRANSACTION TRANSMISSION</td>
</tr>
<tr class="odd">
<td>RCRCAT1</td>
<td>AR/RC SEND AR TRANSACTION TO RC</td>
</tr>
<tr class="even">
<td>RCRCBL</td>
<td>RC VIEW BILL LIST</td>
</tr>
<tr class="odd">
<td>RCRCBL1</td>
<td>EOB PROCESSING LIST BUILD</td>
</tr>
<tr class="even">
<td>RCRCBLE</td>
<td>TP REFERRAL ACTION SEL/MOD LIST BUILD</td>
</tr>
<tr class="odd">
<td>RCRCDIV</td>
<td>RC REFERRAL DIVISION UTILITY PROGRAM</td>
</tr>
<tr class="even">
<td>RCRCEL</td>
<td>RCRC TRANSMISISON LOG</td>
</tr>
<tr class="odd">
<td>RCRCELE</td>
<td>TRANSMISSION LOG SEL/RESEQ LIST BUILD</td>
</tr>
<tr class="even">
<td>RCRCREC</td>
<td>RC AND DHCP RECONCILIATION REPORTS</td>
</tr>
<tr class="odd">
<td>RCRCREC2</td>
<td>RC AND DHCP RECONCILIATION REP LOOP</td>
</tr>
<tr class="even">
<td>RCRCREC3</td>
<td>PARSE RC/AR DATA FOR RECONCILIATION</td>
</tr>
<tr class="odd">
<td>RCRCRR</td>
<td>RC RECONCILIATION DRIVER</td>
</tr>
<tr class="even">
<td>RCRCRT</td>
<td>RC TRANSACTION PROC OVER INTERFACE</td>
</tr>
<tr class="odd">
<td>RCRCRT1</td>
<td>RC AND DOJ TRANSACTION ROU 1</td>
</tr>
<tr class="even">
<td>RCRCRT2</td>
<td>RC AND DOJ TRANSACTION ROU 2</td>
</tr>
<tr class="odd">
<td>RCRCSRV</td>
<td>RC SERVER DRIVER</td>
</tr>
<tr class="even">
<td>RCRCUIB</td>
<td>RC REFERRAL UTILITY IB INTERFACE PROGRAM</td>
</tr>
<tr class="odd">
<td>RCRCUTL</td>
<td>RC REFERRAL UTILITY PROGRAM</td>
</tr>
<tr class="even">
<td>RCRCVAR</td>
<td>RC SERVER TYPE DRIVER VARIABLES</td>
</tr>
<tr class="odd">
<td>RCRCVC</td>
<td>RC VIEW REFERRAL CHECK LIST</td>
</tr>
<tr class="even">
<td>RCRCVCK</td>
<td>TP POSSIBLE REFERRAL LIST CHECK</td>
</tr>
<tr class="odd">
<td>RCRCVCP</td>
<td>THIRD PARTY REFERRAL CHECK LIST</td>
</tr>
<tr class="even">
<td>RCRCVL</td>
<td>RC VIEW BILL LIST</td>
</tr>
<tr class="odd">
<td>RCRCVL1</td>
<td>TP POSSIBLE REFERRAL LIST BUILD</td>
</tr>
<tr class="even">
<td>RCRCVL2</td>
<td>RC VIEW BILL LIST SORT BUILD</td>
</tr>
<tr class="odd">
<td>RCRCVLB</td>
<td>RC VIEW ACTIVE LIST BUILD</td>
</tr>
<tr class="even">
<td>RCRCVLE</td>
<td>TP POSSIBLE REFERRAL SEL/MOD LIST BUILD</td>
</tr>
<tr class="odd">
<td>RCRCVXM</td>
<td>AR/RC ORIG BILL TRANSMISSION</td>
</tr>
<tr class="even">
<td>RCRCXM1</td>
<td>AR/RC ORIGINAL TRANSMISSION SET</td>
</tr>
<tr class="odd">
<td>RCRCXMS</td>
<td>RC TRANSMISSION MESSAGE HANDLER</td>
</tr>
<tr class="even">
<td>RCRJR</td>
<td>nightly process, monthly data extractors</td>
</tr>
<tr class="odd">
<td>RCRJRBD</td>
<td>bad debt extractor and report</td>
</tr>
<tr class="even">
<td>RCRJRBDE</td>
<td>bad debt edit the report</td>
</tr>
<tr class="odd">
<td>RCRJRBDR</td>
<td>bad debt report generator</td>
</tr>
<tr class="even">
<td>RCRJRBDT</td>
<td>bad debt retransmit</td>
</tr>
<tr class="odd">
<td>RCRJRCO</td>
<td>control collection of monthly data</td>
</tr>
<tr class="even">
<td>RCRJRCO1</td>
<td>continuation of AR data collector</td>
</tr>
<tr class="odd">
<td>RCRJRCO2</td>
<td>start of the ar2 data collector</td>
</tr>
<tr class="even">
<td>RCRJRCOB</td>
<td>calculate a bills balance</td>
</tr>
<tr class="odd">
<td>RCRJRCOC</td>
<td>count current receivables</td>
</tr>
<tr class="even">
<td>RCRJRCOL</td>
<td>start of the AR data collector</td>
</tr>
<tr class="odd">
<td>RCRJRCOR</td>
<td>AR data collector summary report</td>
</tr>
<tr class="even">
<td>RCRJRCOT</td>
<td>calculate a transactions balance</td>
</tr>
<tr class="odd">
<td>RCRJRCOU</td>
<td>AR data collector summary report</td>
</tr>
<tr class="even">
<td>RCRJRDEP</td>
<td>Deposit Reconciliation Report</td>
</tr>
<tr class="odd">
<td>RCRJROIG</td>
<td>send data for OIG extract</td>
</tr>
<tr class="even">
<td>RCRJRTR1</td>
<td>transaction report (print)</td>
</tr>
<tr class="odd">
<td>RCRJRTRA</td>
<td>transaction report</td>
</tr>
<tr class="even">
<td>RCRPADD</td>
<td>Add Bills to an Existing Repayment Plan</td>
</tr>
<tr class="odd">
<td>RCRPENTR</td>
<td>Edit and Create Repayment Plans</td>
</tr>
<tr class="even">
<td>RCRPINQ</td>
<td>Repayment Plan Inquiry</td>
</tr>
<tr class="odd">
<td>RCRPRPU</td>
<td>Repayment Plan Inquiry Utilities</td>
</tr>
<tr class="even">
<td>RCRPSTR</td>
<td>Repayment Plan Status Report</td>
</tr>
<tr class="odd">
<td>RCRPU</td>
<td>Repayment Plan Utilities</td>
</tr>
<tr class="even">
<td>RCRPU1</td>
<td>Repayment Plan Utilities</td>
</tr>
<tr class="odd">
<td>RCRPU2</td>
<td>Repayment Plan Utilities</td>
</tr>
<tr class="even">
<td>RCTCS1</td>
<td>Stop/Reactivate Cross-Servicing</td>
</tr>
<tr class="odd">
<td>RCTCSJR</td>
<td>Cross-Servicing Debt Referral Reject Report and TCS IAI Error Code List</td>
</tr>
<tr class="even">
<td>RCTCSJS</td>
<td>Processes Cross-Servicing Reject server messages from AITC</td>
</tr>
<tr class="odd">
<td>RCTCSJS1</td>
<td>Processes and displays Cross-Servicing reject data</td>
</tr>
<tr class="even">
<td>RCTCSP1</td>
<td>Cross-Servicing Bill Report, Cross-Servicing Recall Report, Print Cross-Servicing Report</td>
</tr>
<tr class="odd">
<td>RCTCSP2</td>
<td>Cross-Servicing Transmission (Referrals)</td>
</tr>
<tr class="even">
<td>RCTCSP3</td>
<td>Cross-Servicing Due Process Notification Processing</td>
</tr>
<tr class="odd">
<td>RCTCSP3S</td>
<td>Cross-Servicing Due Process Notification Processing</td>
</tr>
<tr class="even">
<td>RCTCSP4</td>
<td>CS Debt Referral Stop Reactivate Report</td>
</tr>
<tr class="odd">
<td>RCTCSP4E</td>
<td>Continuation of RCTCSP4</td>
</tr>
<tr class="even">
<td>RCTCSP5</td>
<td>Cross-Servicing Recall Report</td>
</tr>
<tr class="odd">
<td>RCTCSP6</td>
<td>Cross-Servicing Re-Referred Bills Report</td>
</tr>
<tr class="even">
<td>RCTCSP7</td>
<td>Cross-Servicing Transmission added with PRCA*4.5*327</td>
</tr>
<tr class="odd">
<td>RCTCSPD</td>
<td>Cross-Servicing Transmission (Referrals, Updates, Recalls)</td>
</tr>
<tr class="even">
<td>RCTCSPD0</td>
<td>Cross-Servicing Transmission added with PRCA*4.5*327</td>
</tr>
<tr class="odd">
<td>RCTCSPD4</td>
<td>CS Comment Transactions (File #433)</td>
</tr>
<tr class="even">
<td>RCTCSPD5</td>
<td>CS Comment Transactions (File #433)</td>
</tr>
<tr class="odd">
<td>RCTCSPRS</td>
<td>Cross-Servicing Transmission (Process Reconciliation Server Messages from AITC)</td>
</tr>
<tr class="even">
<td>RCTCSPS</td>
<td>Cross-Servicing Transmission (Un-processable)</td>
</tr>
<tr class="odd">
<td>RCTCSPU</td>
<td>Cross-Servicing Transmission (Updates)</td>
</tr>
<tr class="even">
<td>RCTOP1</td>
<td>TOP TRANSMISSION</td>
</tr>
<tr class="odd">
<td>RCTOP2</td>
<td>TOP TRANSMISSION</td>
</tr>
<tr class="even">
<td>RCTOP4</td>
<td>TOP TRANSMISSION</td>
</tr>
<tr class="odd">
<td>RCTOPD</td>
<td>TOP TRANSMISSION</td>
</tr>
<tr class="even">
<td>RCTOPS</td>
<td>DMC 90 DAY (SERVER)</td>
</tr>
<tr class="odd">
<td>RCTOPU</td>
<td>TOP TRANSMISSION</td>
</tr>
<tr class="even">
<td>RCTRAN</td>
<td>Transaction History report.</td>
</tr>
<tr class="odd">
<td>RCTRAN1</td>
<td>Transaction History report.</td>
</tr>
<tr class="even">
<td>RCVCR1</td>
<td>First Party Veterans Charge Report</td>
</tr>
<tr class="odd">
<td>RCVCR2</td>
<td>First Party Veterans Charge Report</td>
</tr>
<tr class="even">
<td>RCWROFF</td>
<td>write off, terminated</td>
</tr>
<tr class="odd">
<td>RCWROFF1</td>
<td>partial waiver</td>
</tr>
<tr class="even">
<td>RCXFMSC1</td>
<td>FMS cash receipt (CR) build lines</td>
</tr>
<tr class="odd">
<td>RCXFMSCR</td>
<td>FMS cash receipt (CR) code sheet generator</td>
</tr>
<tr class="even">
<td>RCXFMSPR</td>
<td>print revenue source codes</td>
</tr>
<tr class="odd">
<td>RCXFMSSV</td>
<td>FMS standard voucher (SV) code sheet generator</td>
</tr>
<tr class="even">
<td>RCXFMST1</td>
<td>EDI Lockbox FMS transfer (TR) code sheet gen</td>
</tr>
<tr class="odd">
<td>RCXFMSTR</td>
<td>TRI CARE EXTRACT ROUTINE</td>
</tr>
<tr class="even">
<td>RCXFMSTX</td>
<td>FMS transfer (TR) code sheet generator</td>
</tr>
<tr class="odd">
<td>RCXFMSUF</td>
<td>calculate FMS fund code for a bill</td>
</tr>
<tr class="even">
<td>RCXFMSUR</td>
<td>revenue source codes</td>
</tr>
<tr class="odd">
<td>RCXFMSUV</td>
<td>FMS vendor id</td>
</tr>
<tr class="even">
<td>RCXFMSW1</td>
<td>FMS write-off (WR) code sheet generator for a transaction</td>
</tr>
<tr class="odd">
<td>RCXFMSWR</td>
<td>FMS write-off (WR) code sheet generator</td>
</tr>
<tr class="even">
<td>RCXVACK</td>
<td>AR Data Extraction HL7 Query/ACK</td>
</tr>
<tr class="odd">
<td>RCXVCHK</td>
<td>Check for bad records</td>
</tr>
<tr class="even">
<td>RCXVDC</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="odd">
<td>RCXVDC1</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="even">
<td>RCXVDC10</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="odd">
<td>RCXVDC2</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="even">
<td>RCXVDC3</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="odd">
<td>RCXVDC4</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="even">
<td>RCXVDC5</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="odd">
<td>RCXVDC6</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="even">
<td>RCXVDC7</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="odd">
<td>RCXVDC8</td>
<td>AR Data Extraction Data Creation</td>
</tr>
<tr class="even">
<td>RCXVDEQ</td>
<td>AR Data Extract Queue Trigger</td>
</tr>
<tr class="odd">
<td>RCXVFTC</td>
<td>FTP for Cache NT</td>
</tr>
<tr class="even">
<td>RCXVFTP</td>
<td>FTP AR Data Extract Batch Files</td>
</tr>
<tr class="odd">
<td>RCXVFTR</td>
<td>Retrieve FTP messages</td>
</tr>
<tr class="even">
<td>RCXVFTV</td>
<td>FTP for VMS</td>
</tr>
<tr class="odd">
<td>RCXVPARM</td>
<td>AR Parameter File Editor</td>
</tr>
<tr class="even">
<td>RCXVRMV</td>
<td>AR Data Extract Remove</td>
</tr>
<tr class="odd">
<td>RCXVSRV</td>
<td>AR Data Extract Server Program</td>
</tr>
<tr class="even">
<td>RCXVTSK</td>
<td>AR Data Extract Nightly Task</td>
</tr>
<tr class="odd">
<td>RCXVUTIL</td>
<td>AR Data Extract Utility Program</td>
</tr>
<tr class="even">
<td>RCY</td>
<td>Create/edit payment patch</td>
</tr>
<tr class="odd">
<td>RCY215</td>
<td>Report queue</td>
</tr>
<tr class="even">
<td>RCY21A</td>
<td>Report calculation</td>
</tr>
<tr class="odd">
<td>RCY21B</td>
<td>Report print</td>
</tr>
<tr class="even">
<td>RCYAPP</td>
<td>Approve batch</td>
</tr>
<tr class="odd">
<td>RCYCPAY</td>
<td>Calculates duplicate payment</td>
</tr>
<tr class="even">
<td>RCYDD1</td>
<td>Call utilities</td>
</tr>
<tr class="odd">
<td>RCYDD2</td>
<td>DD call utilities</td>
</tr>
<tr class="even">
<td>RCYE</td>
<td>Payment transaction processor.</td>
</tr>
<tr class="odd">
<td>RCYHLP</td>
<td>Help text processor</td>
</tr>
<tr class="even">
<td>RCYLT</td>
<td>Transaction History report</td>
</tr>
<tr class="odd">
<td>RCYPAY</td>
<td>Date Sorted Payment report</td>
</tr>
<tr class="even">
<td>RCYPT</td>
<td>Post transaction from temporary file</td>
</tr>
<tr class="odd">
<td>RCYPT2</td>
<td>Calculate data for FMS Document</td>
</tr>
<tr class="even">
<td>RCYPT3</td>
<td>Create FMS Document strings</td>
</tr>
<tr class="odd">
<td>RCYPT4</td>
<td>Check bill status and payment amount</td>
</tr>
<tr class="even">
<td>RCYREC</td>
<td>Prints receipts</td>
</tr>
<tr class="odd">
<td>RCYTRA</td>
<td>Transfer payment</td>
</tr>
<tr class="even">
<td>RCYUT</td>
<td>Utilities</td>
</tr>
<tr class="odd">
<td>RCYVOI</td>
<td>Void batch</td>
</tr>
</tbody>
</table>

<span id="_Toc67391130" class="anchor"></span>Table 3: AR Mapped Routines

## Accounts Receivable Mapped Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of Accounts Receivable routines with indications of whether routine mapping is recommended, not critical, or not recommended when using a VAX/DSM operating system.

| Routine  | Mapping Highly Recommended | Mapping Is Not Critical | Mapping Not Recommended |
|----------|----------------------------|-------------------------|-------------------------|
| PRCAACC  |                            | X                       |                         |
| PRCAADBO |                            |                         | X                       |
| PRCAADIN |                            |                         | X                       |
| PRCAAPR  | X                          |                         |                         |
| PRCAAPR1 | X                          |                         |                         |
| PRCAATR  | X                          |                         |                         |
| PRCABD   |                            | X                       |                         |
| PRCABIL  |                            |                         | X                       |
| PRCABIL1 |                            |                         | X                       |
| PRCABIL2 |                            |                         | X                       |
| PRCABIL3 |                            |                         | X                       |
| PRCABJ   |                            |                         | X                       |
| PRCABJ1  |                            |                         | X                       |
| PRCABJV  |                            |                         | X                       |
| PRCABP1  |                            |                         | X                       |
| PRCABP2  |                            |                         | X                       |
| PRCABPF  |                            |                         | X                       |
| PRCACLM  |                            |                         | X                       |
| PRCACM   |                            |                         | X                       |
| PRCACOL  |                            |                         | X                       |
| PRCACV10 |                            |                         | X                       |
| PRCADCDJ |                            |                         | X                       |
| PRCADCJ1 |                            |                         | X                       |
| PRCADEL  |                            |                         | X                       |
| PRCADIN  |                            |                         | X                       |
| PRCADJ   |                            | X                       |                         |
| PRCADR   |                            |                         | X                       |
| PRCADR1  |                            |                         | X                       |
| PRCADR2  |                            |                         | X                       |
| PRCADR3  |                            |                         | X                       |
| PRCAEA   |                            |                         | X                       |
| PRCAEA1  |                            |                         | X                       |
| PRCAEIN  |                            |                         | X                       |
| PRCAEOL  |                            |                         | X                       |
| PRCAEXM  |                            |                         | X                       |
| PRCAFBD  |                            |                         | X                       |
| PRCAFBD1 |                            |                         | X                       |
| PRCAFBDM |                            |                         | X                       |
| PRCAFBDU |                            |                         | X                       |
| PRCAFDCT |                            |                         | X                       |
| PRCAFN   | X                          |                         |                         |
| PRCAFN1  | X                          |                         |                         |
| PRCAFOR  |                            |                         | X                       |
| PRCAFUT  |                            |                         | X                       |
| PRCAFWO  |                            |                         | X                       |
| PRCAG    |                            |                         | X                       |
| PRCAGD   |                            |                         | X                       |
| PRCAGDR  |                            |                         | X                       |
| PRCAGDT  |                            |                         | X                       |
| PRCAGF   |                            |                         | X                       |
| PRCAGF1  |                            |                         | X                       |
| PRCAGP   |                            |                         | X                       |
| PRCAGS   |                            |                         | X                       |
| PRCAGST  |                            |                         | X                       |
| PRCAGST1 |                            |                         | X                       |
| PRCAGST2 |                            |                         | X                       |
| PRCAGT   |                            |                         | X                       |
| PRCAGU   |                            |                         | X                       |
| PRCAHIS  |                            |                         | X                       |
| PRCAHIS1 |                            |                         | X                       |
| PRCAHOL  |                            |                         | X                       |
| PRCAINS1 |                            |                         | X                       |
| PRCAINST |                            |                         | X                       |
| PRCAKBT  |                            |                         | X                       |
| PRCAKBT1 |                            |                         | X                       |
| PRCAKM   |                            |                         | X                       |
| PRCAKMR  |                            |                         | X                       |
| PRCAKS   |                            |                         | X                       |
| PRCAKTP  |                            |                         | X                       |
| PRCAKUN  |                            |                         | X                       |
| PRCALET  |                            |                         | X                       |
| PRCALM   |                            |                         | X                       |
| PRCALST  |                            |                         | X                       |
| PRCALST1 |                            |                         | X                       |
| PRCALT2  |                            |                         | X                       |
| PRCAMARK |                            |                         | X                       |
| PRCAMAS  |                            |                         | X                       |
| PRCAMESG |                            |                         | X                       |
| PRCAMRKC |                            |                         | X                       |
| PRCANRU  |                            |                         | X                       |
| PRCANRU0 |                            |                         | X                       |
| PRCANTE0 |                            |                         | X                       |
| PRCANTE1 |                            |                         | X                       |
| PRCANTEG |                            |                         | X                       |
| PRCAOFF  |                            |                         | X                       |
| PRCAOFF1 |                            |                         | X                       |
| PRCAOFF2 |                            |                         | X                       |
| PRCAOFF3 |                            |                         | X                       |
| PRCAOLD  |                            |                         | X                       |
| PRCAPAT  |                            |                         | X                       |
| PRCAPAT1 |                            |                         | X                       |
| PRCAPAY  | X                          |                         |                         |
| PRCAPAY1 | X                          |                         |                         |
| PRCAPAY2 | X                          |                         |                         |
| PRCAPAY3 | X                          |                         |                         |
| PRCAPCL  |                            |                         | X                       |
| PRCAPRO  |                            |                         |                         |
| PRCAPTR  |                            |                         | X                       |
| PRCAQUE  |                            | X                       |                         |
| PRCAREP  |                            |                         | X                       |
| PRCAREPT |                            |                         | X                       |
| PRCARETN |                            |                         | X                       |
| PRCARFD  |                            |                         | X                       |
| PRCARFD1 |                            |                         | X                       |
| PRCARFD2 |                            |                         | X                       |
| PRCARFD3 |                            |                         | X                       |
| PRCARFP  |                            |                         | X                       |
| PRCARFU  |                            |                         | X                       |
| PRCARPS  |                            |                         | X                       |
| PRCARPS1 |                            |                         | X                       |
| PRCASER  | X                          |                         |                         |
| PRCASER1 | X                          |                         |                         |
| PRCASET  |                            |                         | X                       |
| PRCASIG  |                            |                         | X                       |
| PRCASVC  |                            |                         | X                       |
| PRCASVC1 | X                          |                         |                         |
| PRCASVC3 | X                          |                         |                         |
| PRCASVC6 | X                          |                         |                         |
| PRCAUDT  |                            |                         | X                       |
| PRCAUDT1 |                            |                         | X                       |
| PRCAUPD  |                            |                         | X                       |
| PRCAUT1  | X                          |                         |                         |
| PRCAUT2  | X                          |                         |                         |
| PRCAUT3  | X                          |                         |                         |
| PRCAUTL  | X                          |                         |                         |
| PRCAWO   |                            |                         | X                       |
| PRCAWO1  |                            |                         | X                       |
| PRCAWOF  |                            |                         | X                       |
| PRCAWREA |                            |                         | X                       |
| PRCAWV   |                            |                         | X                       |
| PRCAX    |                            |                         | X                       |
| PRCAX1   |                            |                         | X                       |
| PRCAXP   |                            |                         | X                       |
| RCAM     |                            |                         | X                       |
| RCAMADD  | X                          |                         |                         |
| RCAMDTH  |                            |                         | X                       |
| RCAMFN01 | X                          |                         |                         |
| RCAMLET  |                            |                         | X                       |
| RCCPW    |                            |                         | X                       |
| RCCPW1   |                            |                         | X                       |
| RCDPCON  |                            |                         | X                       |
| RCDPCRE  |                            |                         | X                       |
| RCDPDEP  |                            |                         | X                       |
| RCDPDRV1 |                            |                         | X                       |
| RCDPEDT  |                            |                         | X                       |
| RCDPFMS  |                            |                         | X                       |
| RCDPEN01 |                            |                         | X                       |
| RCDPLST  |                            |                         | X                       |
| RCDPUT   |                            |                         | X                       |
| RCDPVDP  |                            |                         | X                       |
| RCDPVW   |                            |                         | X                       |
| RCEVDD1  |                            | X                       |                         |
| RCEVDRV1 | X                          |                         |                         |
| RCEVGEN  |                            |                         | X                       |
| RCEVUTL  |                            |                         | X                       |
| RCFMCAF  |                            |                         | X                       |
| RCFMDRV1 |                            |                         | X                       |
| RCFMFN02 |                            |                         | X                       |
| RCFMOBR  |                            |                         | X                       |
| RCFMPUR  |                            |                         | X                       |
| RCFMUDL  |                            |                         | X                       |
| RCFN01   | X                          |                         |                         |
| RCMSDD1  |                            |                         | X                       |
| RCMSFN01 | X                          |                         |                         |
| RCMSITE  |                            |                         | X                       |
| RCMSNUM  |                            |                         | X                       |
| RCNR4    |                            |                         | X                       |
| RCNR4A   |                            |                         | X                       |
| RCNR4P   |                            |                         | X                       |
| RCNR4T   |                            |                         | X                       |
| RCNRSUM  |                            |                         | X                       |
| RCNRSUM1 |                            |                         | X                       |
| RCTRAN   |                            | X                       |                         |
| RCTRAN1  |                            | X                       |                         |
| RCY      |                            | X                       |                         |
| RCY215   |                            |                         | X                       |
| RCY21A   |                            |                         | X                       |
| RCY21B   |                            |                         | X                       |
| RCYAPP   |                            |                         | X                       |
| RCYCPAY  |                            |                         | X                       |
| RCYDD1   |                            |                         | X                       |
| RCYDD2   |                            |                         | X                       |
| RCYE     |                            | X                       |                         |
| RCYHLP   |                            |                         | X                       |
| RCYLT    |                            |                         | X                       |
| RCYPT    |                            |                         | X                       |
| RCYPT2   |                            |                         | X                       |
| RCYPT3   |                            |                         | X                       |
| RCYPT4   |                            |                         | X                       |
| RCYREC   |                            | X                       |                         |
| RCYTRA   |                            |                         | X                       |
| RCYYUT   |                            | X                       |                         |
| RCYVOI   |                            |                         | X                       |

<span id="_Toc67391131" class="anchor"></span>Table 4: List of AR Input Templates

| Input Template Name         | File  | Compiled Routine |
|-----------------------------|-------|------------------|
| PRCA AR DEV                 | 411   |                  |
| PRCA AR2 AMIS 243-249       | 2100  |                  |
| PRCA AR2 AMIS 251-254       | 2100  |                  |
| PRCA AR2 AMIS 294-296       | 2100  |                  |
| PRCA AR2 AMIS MEDIGAP       | 2100  |                  |
| PRCA AR2 AMIS MEDIGAP VM    | 2100  |                  |
| PRCA BATCH PAYMENT          | 433   | ^PRCATB          |
| PRCA BILL 1080              | 430   |                  |
| PRCA BILL 1081              | 430   |                  |
| PRCA BILL 1114              | 430   |                  |
| PRCA CAT SET                | 430   |                  |
| PRCA CAUSED BY              | 430   |                  |
| PRCA COMMENT                | 433   |                  |
| PRCA CREATE BILL STUB       | 430   |                  |
| PRCA CREATE TRANS STUB      | 433   |                  |
| PRCA DOJ PARAM              | 430.5 |                  |
| PRCA FORM                   | 434   |                  |
| PRCA FY ADJ1                | 433   |                  |
| PRCA FY ADJ2                | 433   |                  |
| PRCA FY ADJ2 BATCH          | 433   |                  |
| PRCA FY WAIVED1             | 433   |                  |
| PRCA FY WAIVED2             | 433   |                  |
| PRCA IRS MASTER             | 423   |                  |
| PRCA IRS UPDATE             | 423   |                  |
| PRCA MONTH ADMINT           | 433   |                  |
| PRCA OLD SET                | 430   | ^PRCATA          |
| PRCA PARAMETER              | 430.5 |                  |
| PRCA PAYMENT                | 433   |                  |
| PRCA RE-ESTABLISH WRITE-OFF | 433   |                  |
| PRCA SET                    | 430   | ^PRCATE          |
| PRCABILLVEN                 | 440   |                  |
| PRCAC COWC REFER            | 430   |                  |
| PRCAC DCDOJ REFER           | 433   |                  |
| PRCAC DCDOJ REREFER         | 433   |                  |
| PRCAC DCDOJ RETN            | 433   |                  |
| PRCAC LOCATE DEBTOR         | 430   |                  |
| PRCAC RC INFO               | 430   |                  |
| PRCAC RC REFER              | 433   |                  |
| PRCAC RC TRAN               | 433   |                  |
| PRCAE ADDRESS               | 340   |                  |
| PRCAE ADM INT               | 431   |                  |
| PRCAE ADMIN                 | 433   |                  |
| PRCAE AUDIT                 | 430   |                  |
| PRCAE BILL FROM             | 430.6 |                  |
| PRCAE DC PARAM              | 430.5 |                  |
| PRCAE DEBIT                 | 433   |                  |
| PRCAE F WAIVED              | 433   |                  |
| PRCAE INSURANCE DATA        | 430   |                  |
| PRCAE TERMINATION           | 433   |                  |
| PRCAF COMMON SERIES         | 430.4 |                  |
| PRCAF MAXNUM LETTERS        | 430.5 |                  |
| PRCAF RETURN BILL           | 430   |                  |
| PRCASV REL                  | 430   | ^PRCATSE         |
| PRCASV STATUS               | 430   |                  |
| PRCAT EDIT GL               | 430   |                  |
| RCAM ADDRESS EDIT           | 340   |                  |
| RCAM COMMENT                | 341   |                  |
| RCDP OPEN DEPOSIT           | 344.1 |                  |
| RCDP TICKET CONFIRM         | 344.1 |                  |
| RCDP TICKET DEPOSIT         | 344.1 |                  |
| RCEV CLOSE EVENT            | 341   |                  |
| RCEV OPEN EVENT             | 341   |                  |
| RCFM CAF FILE ENTRIES       | 430   |                  |
| RCFM OPEN DOCUMENT          | 347   |                  |
| RCMS ACCT RECEIVABLE        | 342.1 |                  |
| RCMS BANK DEPOSIT           | 342.1 |                  |
| RCMS BILLING AGENCY         | 342.1 |                  |
| RCMS CASHIER                | 342.1 |                  |
| RCMS DEPT OF JUSTICE        | 342.1 |                  |
| RCMS DISTRICT COUNSEL       | 342.1 |                  |
| RCMS EDI LOCKBOX            | 342   |                  |
| RCMS FORM LETTER            | 343   |                  |
| RCMS GROUP 1                | 342.1 |                  |
| RCMS GROUP 2                | 342.1 |                  |
| RCMS GROUP 3                | 342.1 |                  |
| RCMS GROUP 4                | 342.1 |                  |
| RCMS GROUP 5                | 342.1 |                  |
| RCMS GROUP 6                | 342.1 |                  |
| RCMS GROUP 7                | 342.1 |                  |
| RCMS GROUP 8                | 342.1 |                  |
| RCMS IRS                    | 342   |                  |
| RCMS NOTIFICATION           | 342   |                  |
| RCMS RATES                  | 342   |                  |
| RCMS REGIONAL COUNSEL       | 342.1 |                  |
| RCMS RETURN PAYMENT         | 342.1 |                  |
| RCMS SITE                   | 342.1 |                  |
| RCMS SITE DEPOSIT           | 342.1 |                  |
| RCNR BAD DEBT EDIT          | 348.1 |                  |
| RCY COPY PAYMENT            | 344   |                  |
| RCY PAYMENT 11              | 344   |                  |
| RCY PAYMENT 3               | 344   |                  |
| RCY PAYMENT 4               | 344   |                  |
| RCY PAYMENT 5               | 344   |                  |
| RCY PAYMENT 6               | 344   |                  |
| RCY PAYMENT 7               | 344   |                  |
| RCY PAYMENT 8               | 344   |                  |

<span id="_Toc67391132" class="anchor"></span>Table 5: List of AR Print Templates

| Print Template Name        | File  | Compiled Routine |
|----------------------------|-------|------------------|
| PRCA 3RD PROFILE           | 430   | ^PRCATP5         |
| PRCA 3RD REPORT            | 430   |                  |
| PRCA ADDR LIST             | 340   | ^PRCATO1         |
| PRCA AR LIST               | 430   |                  |
| PRCA BILL LIST             | 430   |                  |
| PRCA DISCREPANCY           | 340   |                  |
| PRCA DISP ADJ              | 433   | ^PRCATO4         |
| PRCA DISP AUDIT            | 430   | ^PRCATO2         |
| PRCA DISP AUDIT2           | 430   |                  |
| PRCA DISP CARE             | 433   | ^PRCATO5         |
| PRCA FMS DRC               | 347   |                  |
| PRCA FMS STATUS            | 347   | ^PRCATF          |
| PRCA FMS TRANS STAT        | 347   | ^PRCATF2         |
| PRCA FMS UNPROCESSED LIST  | 347   |                  |
| PRCA FOLLOW-UP             | 433   |                  |
| PRCA LAST ACTIVITY         | 430   |                  |
| PRCA LIST HOLD             | 430   |                  |
| PRCA MEANS PROFILE         | 430   | ^PRCATP2         |
| PRCA NEWB LIST             | 430   |                  |
| PRCA OTHER PROFILE         | 430   | ^PRCATP4         |
| PRCA PARAMETER             | 430.5 | ^PRCATO7         |
| PRCA PROFILE               | 430   | ^PRCATP1         |
| PRCA TCSP RECALLB          | 430   |                  |
| PRCA TCSP RECALLD          | 430   |                  |
| PRCA TRANS PROFILE         | 433   | ^PRCATR3         |
| PRCA VENDOR PROFILE        | 430   | ^PRCATP3         |
| PRCAA AMEND AUDIT          | 430   | ^PRCATR2         |
| PRCAC RETURN AR            | 430   |                  |
| PRCAC TR LIST              | 433   | ^PRCATW1         |
| PRCAD COWC LIST            | 430   |                  |
| PRCAD DC DOJ               | 430   |                  |
| PRCAD DELINQ               | 430   |                  |
| PRCAL CAT LIST             | 430   |                  |
| PRCAL L DC-DOJ             | 430   |                  |
| PRCAL MEANS LIST           | 430   |                  |
| PRCAL PAYMENT LIST         | 433   |                  |
| PRCAP ADM INT              | 431   |                  |
| PRCAP AMIS                 | 433   |                  |
| PRCAP CARE WV              | 433   | ^PRCATW3         |
| PRCAP COST                 | 433   | ^PRCATO3         |
| PRCAP DC DOJ               | 430.5 | ^PRCATO6         |
| PRCAP DEBTOR LOCATE        | 430   | ^PRCATO9         |
| PRCAP ESTABLISH AMIS       | 430   |                  |
| PRCAP OUTSTAND AMIS        | 430   |                  |
| PRCAP REPAYMENT            | 430   | ^PRCATR1         |
| PRCAP RETURN BILL          | 430   | ^PRCATP6         |
| PRCAP WAIVED               | 433   | ^PRCATW2         |
| PRCAR CASH                 | 433   |                  |
| PRCAR CASH BY RECEIPT      | 433   |                  |
| PRCAR CASH BY RECEIPT TWO  | 433   |                  |
| PRCAR CASH SUMMARY         | 433   |                  |
| PRCAR CONTINGENT REPORT    | 430   |                  |
| PRCAR MAS REPORT           | 430   |                  |
| PRCARFD                    | 430   | ^PRCATRF         |
| PRCAS DC                   | 433   |                  |
| PRCAT DISP CP              | 430   | ^PRCATO8         |
| PRCAT DISP GL              | 430   | ^PRCATO8         |
| PRCAT NEW AR               | 430   | ^PRCATP7         |
| PRCAT NEW TRANS            | 433   | ^PRCATP9         |
| PRCAY BATCH STATUS         | 435   |                  |
| PRCAY RECEIPT              | 435   |                  |
| PRCAY RECEIPT LIST         | 435   |                  |
| RCAM ADDRESS UNKNOWN       | 340   |                  |
| RCAM COMMENT               | 341   |                  |
| RCCPC INQUIRE STATEMENT    | 349.2 |                  |
| RCDMC REFERRED DEBTS       | 430   |                  |
| RCDMC90A                   | 340   |                  |
| RCDMC90AH                  | 340   |                  |
| RCDMC90B                   | 340   |                  |
| RCDP 215 FORM              | 344.1 |                  |
| RCDP DEPOSIT LINE          | 344   |                  |
| RCDP DEPOSIT LINE 2        | 344   |                  |
| RCDP DEPOSIT LIST BRIEF    | 344.1 |                  |
| RCDP DEPOSIT LIST EXPAND   | 344.1 |                  |
| RCDP DEPOSIT PROFILE       | 344.1 |                  |
| RCDP RECEIPT LIST HEADER   | 344   |                  |
| RCDP RECEIPT LIST HEADER 2 | 344   |                  |
| RCMS INT/ADM/PEN           | 342   |                  |
| RCTOP REPORT               | 340   |                  |
| RCTOPH                     | 340   |                  |
| RCXV ACTIVE PRINT          | 430   |                  |
| RCY BATCH STATUS           | 344   |                  |
| RCY RECEIPT                | 344   |                  |
| RCY RECEIPT LIST           | 344   |                  |
| TCS IAI ERROR CODES        | 348.5 |                  |

<span id="_Toc67391133" class="anchor"></span>Table 6: List of AR Sort Templates

| Sort Template Name        | File  | Compiled Routine |
|---------------------------|-------|------------------|
| PRCA 3RD REPORT           | 430   |                  |
| PRCA FOLLOW-UP            | 433   |                  |
| PRCA LAST ACTIVITY        | 430   |                  |
| PRCA PAYMENT DATE         | 433   |                  |
| PRCA FMS DRC              | 347   |                  |
| PRCAR CASH                | 433   |                  |
| PRCAR CASH BY RECEIPT     | 433   |                  |
| PRCAR CASH RECPT NUM SORT | 433   |                  |
| PRCARFD                   | 430   |                  |
| PRCAS AMIS SORT           | 433   |                  |
| PRCAS DC SORT             | 433   |                  |
| PRCAS ESTABLISH AMIS      | 430   |                  |
| PRCAS OUTSTAND AMIS       | 430   |                  |
| PRCAT NEW TRANS           | 433   |                  |
| RCAM ADDRESS UNKNOWN      | 340   |                  |
| RCAM COMMENT              | 341   |                  |
| RCCPC INQUIRE STATEMENT   | 349.2 |                  |
| RCXV ACTIVE SORT          | 430   |                  |

<span id="_Toc67391134" class="anchor"></span>Table 7: List of AR List Templates

<table>
<caption><p><span id="_Toc8133443" class="anchor"></span>Table 8: Input Variables</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>List Template Name</th>
<th>Protocol</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCA TCSP ACCOUNT PROFILE</td>
<td><p>PRCA TCSP ACCOUNT PROFILE MENU</p>
<p>RCDP ACCOUNT PROFILE SELECT NEW ACCOUNT</p>
<p>RCDP ACCOUNT PROFILE SELECT STATUS</p>
<p>PRCA TCSP WORKLIST CANCEL/EDIT/ADD</p>
<p>RCDP FAST EXIT</p>
<p>RCDP ACCOUNT PROFILE BILL TRANSACTIONS</p>
<p>RCDP ACCT PROFILE STOP</p>
<p>RCDP ACCT PROFILE TERM FISCAL</p>
<p>RCDP ACCT PROFILE RECALL BILL</p>
<p>RCDP ACCT PROFILE RECALL DEBTOR</p>
<p>RCDP ACCT PROFILE DECREASE TRANS</p>
<p>RCDP ACCT PROFILE INCREASE TRANS</p>
<p>RCDP ACCT PROFILE SUSPEND</p>
<p>VALM BLANK 4</p>
<p>VALM BLANK 5</p>
<p>VALM BLANK 6</p>
<p>RCDP ACCOUNT PROFILE BILL PROFILE</p></td>
</tr>
<tr class="even">
<td>RCTCSP WORKLIST</td>
<td><p>PRCA TCSP WORKLIST MENU</p>
<p>PRCA TCSP WORKLIST EXPAND</p>
<p>PRCA TCSP WORKLIST INSURANCE</p>
<p>PRCA TCSP WORKLIST ACCOUNT PROFILE</p>
<p>PRCA TCSP WORKLIST VIEW PATIENT</p>
<p>PRCA TCSP WORKLIST PRINT STATEMENT</p>
<p>PRCA TCSP WORKLIST REMOVE</p></td>
</tr>
<tr class="odd">
<td>RCTCSP WORKLIST EXPAND</td>
<td>RCTCSP WORKLIST EXPAND MENU PROTOCOL</td>
</tr>
</tbody>
</table>

<span id="_Toc8133443" class="anchor"></span>Table 8: Input Variables

# Accounts Receivable Integration with Integrated Billing and National Roll-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accounts Receivable (AR) module, the Integrated Billing (IB), and National Roll-Up packages were designed to be integrated. The integration allows for patient billing information created in the IB module to be passed to AR for processing. The integration of these three packages requires close coordination between Fiscal and Medical Administration Services to ensure that bills created using IB will pass the validity checks included in AR. The following pages explain the routines and files used to facilitate this integration. Following that discussion, the error processing procedures and error messages are explained. Please provide this information to both your Fiscal and MAS application coordinators.

The utilities described herein are solely for the use of the IB and National Roll-Up packages. Each of these integration points affect the Fiscal controls of AR and therefore, only packages with written permission from the Development ISC for AR may employ these utilities.

AR INTEGRATION WITH INTEGRATED BILLING

The routines PRCASVC and PRCASVC1 have been created to give IB the ability to pass billing information into the AR system. There are three entry points:

SETUP^PRCASVC, REL^PRCASVC, and STATUS^PRCASVC.

Their required key variables and data formats are described below:

\[SETUP^PRCASVC\]

This entry point sets up the Accounts Receivable record in File \#430 and returns the record number in the variable PRCASV("ARREC"). Bill status is set to Bill Incomplete.

| Variable       | Description                                                                     |
|----------------|---------------------------------------------------------------------------------|
| PRCASV("SITE") | Required. The three-digit station number.                                       |
| PRCASV("BNO")  | Required. The Bill number assigned by the service. Six alphanumeric characters. |
| PRCASV("SER")  | Required. The section/service number, a pointer to File \#49.                   |

<span id="_Toc8133444" class="anchor"></span>Table 9: Output Variables

<table>
<caption><p><span id="_Toc8133445" class="anchor"></span>Table 10: Input Variables</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCASV("ARREC")</td>
<td><p>The internal record number of the entry in</p>
<p>File #430.</p></td>
</tr>
<tr class="even">
<td>PRCASV("ARBIL")</td>
<td>The Accounts Receivable Bill number (site_"-"_service Bill number).</td>
</tr>
</tbody>
</table>

<span id="_Toc8133445" class="anchor"></span>Table 10: Input Variables

These two outputs return a -1 if the inputs are improper.

\[REL^PRCASVC\]

This entry point releases the completed Bill from the Service to Fiscal. The status of the Bill will become New Bill. The call may take a few seconds to complete processing.

<table>
<caption><p><span id="_Toc67391138" class="anchor"></span>Table 11: Category/Debtor Combinations</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCASV("CAT")</td>
<td>Required. The category (type of Bill) from File #430.2, the AR Category file. The parameter "CAT" is the internal entry number for the category. If this Bill is being generated as a result of a means test, use C-type rather than Nursing Home, Outpatient, or Hospital Care.</td>
</tr>
<tr class="even">
<td>PRCASV("DEBTOR")</td>
<td><p>Required. A variable pointer to the patient, new person, insurance company, institution, or vendor files in the format:</p>
<p>record #;GLOBAL(File #,</p>
<p>Accounts Receivable needs this format to match the entry in File #340 AR Debtor File. The interrelationship of the category and debtor information requires specific global references to be used to ensure accuracy of Bill processing. Here are the possible category/debtor combinations and the correct global and format for each situation:</p></td>
</tr>
</tbody>
</table>

<span id="_Toc67391138" class="anchor"></span>Table 11: Category/Debtor Combinations

| Debtor            | AR Category File (430.2)        | Record \#:GLOBAL (File#: |
|-------------------|---------------------------------|--------------------------|
| Patient           | Ineligible                      | "4;DPT("                 |
|                   | Emergency/Humanitarian          | "4;DPT("                 |
|                   | C(Means Test)                   | "4;DPT("                 |
| Insurance Company | No-Fault Auto Acc.              | "4;DIC(36,"              |
|                   | Crime of Personal Violence      | "4;DIC(36,"              |
|                   | Reimbursable Health Insurance   | "4;DIC(36,"              |
|                   | Fee Reimbursable Insurance      | "4;DIC(36,"              |
|                   | Federal Agencies – Reimbursable | "4;DIC(36,"              |
|                   | Tort Feasor                     | "4;DIC(36,"              |
|                   | Workman's Compensation          | "4;DIC(36,"              |
| Vendor            | Military                        | "4;PRC(440,"             |
|                   | Vendor                          | "4;PRC(440,"             |
|                   | Federal Agencies – Refundable   | "4;PRC(440,"             |
| New Person        | Current Employee                | "4;VA(200,"              |
|                   | Ex-Employee                     | "4;VA(200,"              |
| Institution       | Interagency                     | "4;DIC(4,"               |
|                   | Medicare                        | "4;DIC(4,"               |
|                   | Sharing Agreements              | "4;DIC(4,"               |

<span id="_Toc8133447" class="anchor"></span>Table 12: Input Variables

<table>
<caption><p><span id="_Toc8133448" class="anchor"></span>Table 13: Input Variables</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCASV("BDT")</td>
<td>Required. The date the Bill was generated, in VA FileMan format, (e.g. 2880602).</td>
</tr>
<tr class="even">
<td>PRCASV("ARREC")</td>
<td>Required. The internal record number of the entry in File #430.</td>
</tr>
<tr class="odd">
<td>PRCASV("FY")</td>
<td><p>Required. The fiscal year and amount delimited with the up-arrow "^". Can be multiple.</p>
<p>"FY^amount^FY^amount" e.g.:</p>
<p>"88^69.50^87^150.00"</p></td>
</tr>
<tr class="even">
<td>PRCASV("APR")</td>
<td>Required. Pass the internal entry number from the NEW PERSON File #200 of the user that approved the Bill at the service level.</td>
</tr>
<tr class="odd">
<td>PRCASV("CARE")</td>
<td>Required. Type of care for Means Test/Category C bills. Pass a two-digit number. If the first digit is a "2" indicating skilled nursing, the second digit is ignored. If the first digit is other than "2" then it is ignored, and the second digit is checked: "1" or "2" for inpatient; "3" or "4" for outpatient.</td>
</tr>
<tr class="even">
<td>PRCASV("PAT")</td>
<td><p>Required for 3rd Party. An internal pointer to the</p>
<p>Patient file for 3rd party bills only, commonly called (DFN).</p></td>
</tr>
<tr class="odd">
<td>PRCASV("2NDINS")</td>
<td>If a third-party Bill has secondary insurance, pass an internal pointer to the Insurance file.</td>
</tr>
<tr class="even">
<td>PRCASV("3RDINS")</td>
<td>If a third-party Bill has tertiary insurance, pass an internal pointer to the Insurance file.</td>
</tr>
<tr class="odd">
<td>PRCASV("INPA")</td>
<td>Third party primary insurance insured's (patient) name. 3-25 characters, free text.</td>
</tr>
<tr class="even">
<td>PRCASV("INID")</td>
<td><p>Third party primary insurance policy number.</p>
<p>3 - 16 characters, free text.</p></td>
</tr>
<tr class="odd">
<td>PRCASV("GPNM")</td>
<td><p>Third party primary insurance group name.</p>
<p>3 - 17 characters, free text.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc8133448" class="anchor"></span>Table 13: Input Variables

<u>Output Variables</u>

The variable PRCASVC is set at the start of REL^PRCASVC and, if all inputs are correct, it is killed at the end and the Bill status is changed to New Bill.

If a software check of the input variables finds an error, processing stops and PRCASVC remains defined. If PRCASVC is undefined at the end of the call, a calling routine can assume that the Bill was successfully released to Fiscal.

\[STATUS^PRCASVC\]

This entry point can be used to change the current status of a Bill.

| Variable         | Description                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| PRCASV("STATUS") | Required. Pass the internal entry number corresponding to a Status Number from file \#430.3 (number range 200-299). |
| PRCASV("ARREC")  | Required. The internal record number of the entry in File \#430.                                                    |

<span id="_Toc67391141" class="anchor"></span>Table 14: Accounts Receivable References to Integrated Billing

RETURNING BILLS TO ORIGINATING SERVICE

There are two ways in which a Bill can be returned to the originating service after having been passed to the Accounts Receivable system via the PRCASVC routine. A new Bill going through the cycle for the first time can be returned during the audit in Fiscal Service if an error is discovered. In this instance it has a status of RETURNED FROM AR (NEW). This status applies only to new bills -- bills that are still within the agency and have not been sent to the debtor. It's possible for a Bill to loop through this part of the cycle several times and still remain new.

Once the Bill has been passed to the Accounting Technician and a CALM Code Sheet has been sent to Austin, the Bill is assigned the ACTIVE status and is sent to the debtor. If subsequent correspondence shows that there is an error in the Bill, it is returned to the originating service with a status of RETURNED FOR AMENDMENT.

The Accounts Receivable system provides a means of notifying the Billing Clerk in the service when a Bill has been returned. Two steps are required to activate this notification:

1.  A call to COUNT^PRCAUT2 must be included in the Action field of the Service Billing Clerk's Menu Option. When the clerk begins a session, this will produce an on-screen message if bills have been returned. Only the services own bills are reflected in this message.
2.  The option PRCAL RETURNED BILL must be included in the Service Billing Clerk's menu. Choosing this option will produce a Returned Bill List that can be queued to a printer or viewed on the terminal. The listing is service-specific; bills from other services will not be seen.

When the returned Bill has a status of RETURNED FROM AR (NEW), corrective action should be taken, and the Bill passed back to the Accounts Receivable system by again calling REL^PRCASVC and providing the required variables that have been described. Processing proceeds as if the Bill were new.

If the decision has been made to cancel the Bill, the variable PRCASV("ARREC") must be set to the internal record number of the Bill and a call made to CANCEL^PRCASV1.

> NOTE: Only new bills can be canceled in this manner. Once a Bill has been sent to the debtor, the Amend Bill process must be followed, even if a decision is made to stop further action on the Bill.

When the service has made a decision regarding further action on bills that have been RETURNED FOR AMENDMENT, the Bill is passed back to the Accounts Receivable system by calling AMEND^PRCASVC1. The variables described are required, even if no further action will be taken on the Bill, because a permanent record is kept of Bill activity and status.

AR INTEGRATION WITH INTEGRATED BILLING

The following Accounts Receivable options require integration with Integrated Billing:

The Accounts Receivable Transaction Profile option calls Integrated Billing for FULL and BRIEF views. When doing a FULL or BRIEF profile, AR calls Integrated Billing for pharmacy prescription information. The routines ENB^IBOLK and ENF^IBOLK are called by Accounts Receivable which provides a brief and full inquiry into Integrated Billing by an Accounts Receivable transaction number.

During entry of payments by the Agent Cashier to reimbursable health insurance bills, AR is required to notify the user of holds on existing IB bills related to the same billable services. This requires the Agent Cashier to determine if the insurance company has paid the patient's portion of the Bill. The function \$\$IB^IBRUTL(IEN OF BILL) is used to check if other patient bills are on hold. The routine IBRREL allows the user to remove holds in the IB package. (This is the Agent Cashier's menu option: Release Holds on AR \[PRCAY RELEASE HOLDS\]).

PRCASER

The Accounts Receivable routine PRCASER is used for establishing a new charge (a Bill) for a debtor. When calling this routine, a new charge (Pharmacy Co-Pay, etc.), will be added to the patient's account.

<u>Input Variable:</u> X (delimited by "^")

> \$P1: Site. This is the site number of the facility the charge is being created by. Example: 503, 516, etc. This is the station number field from the Institution File \#4.

> \$P2: Service. This is the service that is creating the Bill. This is the pointer to the Service/Section File \#49.

> \$P3: Category Number. This is the Accounts Receivable category that the charge should fall under.

> \$P4: Debtor. This is the debtor that the charge should fall under. This is a variable pointer to the following files: Vendor, New Person, Institution, and Insurance. For Pharmacy Co-Pay, the debtor should be the patient in the format of "36;DPT(" (where 36 is the internal number of the patient in the Patient file).

> \$P5: Fiscal Year. Fiscal year that the charge should be charged to (in 2-digit format).

> \$P6: Amount. Must be zero or greater and less than 9999999.99.

> \$P7: User. This is the person who created the charge. This is a pointer to the NEW PERSON File \#200.

> \$P8: Date Charge Generated. This is the internal VA FileMan date the charge was issued.

<u>Output Variable:</u> Y - if no errors are encountered (delimited by "^")

> \$P1: Internal Bill Number. This is the internal file number from the Accounts Receivable File \#430.

> \$P2: Charge ID. This is the Bill number (.01 field) from the Accounts Receivable File \#430. It must be 10 characters. For example, 501K000001.

> \$P3: Transaction Number. Since an OPEN Bill may already exist and can be used, it may be necessary to add this charge to an already existing Bill as a transaction. Hence, this would be the pointer value to the AR TRANSACTION File \#433. However, if a new Bill is set up for the current charges, then this piece is equal to zero.

<u>Output Variable:</u> Y - if errors are encountered (delimited by "^")

> \$P1: Error Flag. This = -1 if unsuccessful.

> \$P2: Error Code. This is the error code from the Integrated Billing

> Error file.

PRCASER1

The Accounts Receivable routine PRCASER1 is used to make transactions to an already existing Bill. For example, a Pharmacy Co-Pay was charged and later canceled because the patient did not receive the prescription.

<u>Input Variable:</u> X (delimited by "^")

> \$P1: Transaction Type. This is the field where the transaction number is assigned to each transaction in the Accounts Receivable

> Transaction Type File \#430.3. Currently this program will support only decrease adjustments:

> DECREASE ADJUSTMENT TRAN NUMBER:21

> \$P2: Amount. This is the amount of the transaction. This number must be greater than zero and less than 9999999.99.

> \$P3: Bill Number. This must be the .01 value of the Bill from the Accounts Receivable File \#430 and must be 10 characters in length. (Example: 503-K10001).

> \$P4: User. This is the person who is making the adjustment. Pointer to the NEW PERSON File \#200.

> \$P5: Adjustment Date. This is the internal VA FileMan date when the adjustment occurred.

> \$P6: Reason. This is a free-text field (up to 80 characters) used to add the reason the adjustment took place. (optional).

<u>Output Variable:</u> Y (delimited by "^")

> \$P1: Success Flag. Equals 0 if successful, -1 if unsuccessful.

> \$P2: Error Code. This is the error code from the Integrated Billing

> Error file.

> \$P3: Addition Text. If additional text is required to describe the error, then it is in the third piece (up to 80 characters).

PRCAFN

This routine supports functions for the Integrated Billing package. These functions are valid only for non-patient bills. The category type of the Bill must not be PATIENT or MEANS TEST PATIENT for these functions to work, except for the PST and CATN functions.

<u>Function</u> \$\$BN^PRCAFN(Y):

This function returns the Bill number. Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist, or the Bill does not have a Bill number.

<u>Function</u> \$\$CAT^PRCAFN(Y):

This function returns the category number, category name, and category type, separated by "^". Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist, or the Bill does not have a category.

<u>Function</u> \$\$CATN^PRCAFN(Y):

This function returns the category number, category name, and category type, separated by "^". Input to this function must be the internal entry number of a category, File \#430.2. If -1 is returned, the category does not exist.

<u>Function</u> \$\$TPR^PRCAFN(Y):

This function returns the total paid principal for a specific Bill. Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist.

<u>Function</u> \$\$ORI^PRCAFN(Y):

This function returns the original amount for a specific Bill. Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist.

<u>Function</u> \$\$STA^PRCAFN(Y):

This function returns the status number and status name for a specific Bill. Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist, or the Bill does not have a status.

<u>Function</u> \$\$CLO^PRCAFN(Y):

This function returns the date the Bill was closed, in VA FileMan format. Input to this function must be the internal entry number of the Bill. If -1 is returned, the Bill does not exist, or the Bill does not have a status. If -2 is returned, the Bill is not closed.

<u>Function</u> \$\$PST^PRCAFN(Y):

This function returns the statement day for a debtor. This function is only good for patient type debtors. Input to this function must be in VA FileMan variable pointer format, for example: "1438;DPT(" . If -1 is returned, the patient is not an AR debtor or does not have a statement date assigned.

<u>Function</u> \$\$PUR^PRCAFN(Y):

This function returns the date that a Bill can be considered "closed" for purging purposes. The date will be returned in VA FileMan format. Input to this function must be the internal entry number of a Bill. If a -1 is returned, information regarding the Bill should not be purged.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AR Routine/Option Calls | IB Routine           | IB File or Global Reference | Integration Agreement |
|-------------------------|----------------------|-----------------------------|-----------------------|
| PRCAATR                 | ENF^IBOLK            |                             | DBIA \#126            |
| PRCAEOL                 | IBCAMS               | ‘\$D(^DGCR(399,PRCABN))     | DBIA \#309            |
| PRCAY RELEASE HOLDS     | IBRREL               |                             | DBIA \#306            |
| PRCAD REV CODE TOTALS   | IBOAMS               |                             | DBIA \#308            |
| PRCALT2, PRCAGS         | REPRNT^IBCF13        |                             | DBIA \#307            |
| PRCAPAY3                | \$\$MESS^IBRFN       |                             | DBIA \#310            |
| PRCAPRO                 | ENB^IBOLK ENF^IBOLK  |                             | DBIA \#126            |
| RCYDD1                  | \$\$IB^IBRUTL        |                             | DBIA \#304            |
| PRCAGST1,PRCAPRO        | STMT^IBRFN1(TRAN)    |                             | DBIA \#301            |
| PRCASVC3                |                      | '\$D(^DGCR(399,PRCABN))     |                       |
| PRCADR                  | SVDT^IBRFN(BILL      |                             | DBIA \#300            |
| PRCAUDT                 | IBCAMS               | '\$D(^DGCR(399,PRCABN))     | DBIA \#309            |
| PRCAAPR1, RCYDD1        | \$\$RXST^IBARXEU     |                             | DBIA \#1194           |
| RCRJRCOU                | MRATYPE^IBCEMU2      | ^PRCA(430,^PRCA(430.3       | DBIA \#4385           |
| RCNR4                   | \$\$CRIT^IBRFN2      |                             | DBIA \#1182           |
| RCDMCR5B                | GETS^DIQ(350,        |                             | DBIA \#4541           |
| RCDMCR5B                | \$\$GET1^DIQ(350.1,+ | \$G(^IBE(350.1,ACTTYPE,0))  | DBIA \#4538           |
<span id="_Toc67391142" class="anchor"></span>Table 15: Accounts Receivable References to Kernel
| AR Routine/Option Calls | Global Reference       | Integration Agreement |
|-------------------------|------------------------|-----------------------|
| PRCAP318                | ^DIC(19) – delete LOCK | DBIA \#6747           |
<span id="_Toc67391143" class="anchor"></span>Table 16: Integrated Billing References to Accounts Receivable
<table>
<caption><p><span id="_Toc67391144" class="anchor"></span>Table 17: Integrated Billing Options</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 37%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Integrated Billing Routine Calls</th>
<th>AR Routine</th>
<th>AR File or Global References</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IBCA2</td>
<td>SETUP^PRCASVC3</td>
<td></td>
</tr>
<tr class="even">
<td>IBCB1</td>
<td><p>PRCASVC6</p>
<p>REL^PRCASVC</p></td>
<td></td>
</tr>
<tr class="odd">
<td>IBCB2</td>
<td>PRCASVC6</td>
<td></td>
</tr>
<tr class="even">
<td>IBCBB</td>
<td>$$CATN^PRCAFN</td>
<td></td>
</tr>
<tr class="odd">
<td>IBCBB1</td>
<td><p>$$BN^PRCAFN</p>
<p>$$STA^PRCAFN</p></td>
<td></td>
</tr>
<tr class="even">
<td>IBCCC</td>
<td>SETUP^PRCASVC3</td>
<td></td>
</tr>
<tr class="odd">
<td>IBCNQ</td>
<td><p>$$TPR^PRCAFN,</p>
<p>$$BN^PRCAFN,</p>
<p>$$STA^PRCAFN</p></td>
<td></td>
</tr>
<tr class="even">
<td>IBCC</td>
<td><p>$$STA^PRCAFN</p>
<p>CANCEL^PRCASVC1</p>
<p>AMEND^PRCASVC1</p></td>
<td></td>
</tr>
<tr class="odd">
<td>IBOTR2</td>
<td><p>$$TPR^PRCAFN,</p>
<p>$$CLO^PRCAFN,</p>
<p>$$ORI^PRCAFN</p></td>
<td></td>
</tr>
<tr class="even">
<td>IBCRTN</td>
<td><p>$$RETN^PRCAFN</p>
<p>PRCASVC6</p>
<p>REL^PRCASVC</p></td>
<td></td>
</tr>
<tr class="odd">
<td>IBCU61</td>
<td>$$CATN^PRCAFN</td>
<td></td>
</tr>
<tr class="even">
<td>IBCU</td>
<td><p>$$STA^PRCAFN</p>
<p>$$CATN^PRCAFN</p></td>
<td></td>
</tr>
<tr class="odd">
<td>IBCAMS</td>
<td>$$CAT^PRCAFN</td>
<td>^PRCA(430.2</td>
</tr>
<tr class="even">
<td>IBCORCI</td>
<td>$$ORI^PRCAFN</td>
<td></td>
</tr>
</tbody>
</table>
<span id="_Toc67391144" class="anchor"></span>Table 17: Integrated Billing Options
| IB Option                  | Calls AR Routine |
|----------------------------|------------------|
| IB BILLING CLERK MENU      | COUNT^PRCAUT2    |
| IB BILLING SUPERVISOR MENU | COUNT^PRCAUT2    |
| IB RETURN BILL LIST        | RETN^PRCALST     |
| IB RETURN BILL MENU        | COUNT^PRCAUT2    |
<span id="_Toc67391145" class="anchor"></span>Table 18: Integrated Billing Data Dictionary
<table>
<caption><p><span id="_Toc67391146" class="anchor"></span>Table 19: Accounts Receivable References to Outpatient Pharmacy</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>IB Data Dictionary</th>
<th>AR File/Global Reference</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^DD(350.1,.03,0) CHARGE CATEGORY</td>
<td>^PRCA(430.2) AR CATEGORY</td>
</tr>
<tr class="even">
<td><p>^DD(399.3,.06,0)</p>
<p>ACCOUNTS RECEIVABLE CATEGORY</p></td>
<td>^PRCA(430.2) AR CATEGORY</td>
</tr>
</tbody>
</table>
<span id="_Toc67391146" class="anchor"></span>Table 19: Accounts Receivable References to Outpatient Pharmacy
| AR Routine/Option Calls | PSO Routine    | PSO File or Global Reference | Integration Agreement |
|-------------------------|----------------|------------------------------|-----------------------|
| RCDMCR5B                | \$\$GET1^PSODI | ^DIC(52,IENS                 | DBIA \#4858           |
<span id="_Toc67391147" class="anchor"></span>Table 20: Accounts Receivable References to Scheduling
| AR Routine/Option Calls | SD Routine                             | SD File or Global Reference | Integration Agreement |
|-------------------------|----------------------------------------|-----------------------------|-----------------------|
| RCDMCR5B                | \$\$GET1^DIQ(409.68,+\$P(RESULT,":",2) |                             | DBIA \#5040           |
<span id="_Toc67391148" class="anchor"></span>Table 21: Facility Positions Correspond to AR Menus

## AR Integration with National Roll-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Roll-Up routines are in the namespace RCNR\* and run as a background job called by the National Roll-Up software. National Roll-Up is a procedure to collect data from field stations and transfer it from the AR system to a National Roll-Up interface. The National Roll-Up interface resides at each field station and transmits information from the field stations to the National Roll-Up database located at the San Francisco ISC (SF ISC).

The SF ISC is responsible for the design of the National Roll-Up database and interface. Additionally, the SF ISC is responsible for generating reports, such as the Schedule 9 report, from the roll-up database.

The Accounts Receivable system compiles data and transfers it to the roll-up database without user interaction. Reports of stations’ input are returned as confirmation messages. All reports derived from the National Roll-Up database are generated at the SF ISC and then transmitted to field stations, RD, OFM, and MCCR, where they are printed.

Summary Write-offs and Standard Voucher FMS documents for appropriations 5014 and 2431 are created and transmitted to FMS from the compiled data. This occurs automatically upon completion of the running of the AR component.

# Scope of Accounts Receivable 4.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CALLABLE ROUTINES

AR contains callable routines to support integration with specific modules of the Integrated Billing package. See External Relations for further information on the relationship of AR to other DHCP packages.

JOURNALING

It is recommended that the ^PRCA, ^PRC, ^RC, ^RCY, and ^RCD globals be journaled. Do not journal ^PRCAK.

PURGING/ARCHIVING

AR automatically purges processed payment batches in the Payment Batch File \#344, if the batches are 60 days old or older. See appendix for archiving checklist and procedure.

EXTERNAL RELATIONS

Your system must be running the following software to successfully operate AR Version 4.5. Versions running must be those stated or later:

- KERNEL Version 7.1
- VA FileMan Version 20
- MAS Version 5.3 (PIMS)
- IFCAP Version 5.0
- IB Version 2.0
- Generic Code Sheet 2.0
- MailMan Version 8.0

Currently, the Integrated Billing (IB) package interfaces with AR routines, files, and utilities. AR also interfaces with the IB package. (See "References" of the Integrated Billing section of this manual for integration agreement numbers.)

With this version of AR, it is necessary to be running IFCAP for generation of documents to FMS and site parameter information.

INTERNAL RELATIONS

AR is an integrated system. All components must be in place for proper operation and all menus are stand alone.

PACKAGE WIDE VARIABLES

AR contains no package wide variables.

File Definitions and Key Variables

This section of the Technical Manual provides a listing of the AR files, their VA FileMan access codes, and a description of the data stored there. Also included in this section are descriptions of the exported AR primary menus which are based on specific positions within Fiscal. Another section lists AR primary options and their descriptions. There are no key variables within AR.

# Accounts Receivable Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

340. <u>- AR DEBTOR</u> This file should NEVER be edited directly by VA FileMan. By editing this file directly data corruption can occur. This file holds information pertaining to debtor accounts. A debtor can be an insurance company, patient, person, institution, or vendor.

<u>340.5 - AR REPAYMENT PLAN</u> This file contains the data needed to create and administer Repayment Plans for Debtors.

*Structure:*

> Node 0: Basic Information regarding the Repayment Plan (ID, Debtor, Terms, etc.)

> Node 1: Report Processing flags

> Node 2: Payment Schedule

> Node 3: Payment History

> Node 4: Audit Trail for the individual Plan (Creation, edits, and closings)

> Node 5: Forbearance History

> Node 6: A list of AR Bills included in the Plan

341. <u>- AR EVENT</u> This file contains events that occurred to a debtor's account. This file should NEVER be edited directly. Eventually all types of events will be stored in this file as the Accounts Receivable package moves to a transaction-based system. New data will overwrite existing data.
     1.  <u>- AR EVENT TYPE</u> This file is a table that allows the AR package to manage events throughout the AR package. This file must NEVER be edited by sites or any users. By editing this file, data corruption can occur and functionality in the AR package may be compromised. The contents of this file are verified by the AR Background job, routine PRCABJV. If the entries in this routine do not match the contents of the file, the background job will not run. Make certain you edit this routine if you add or delete entries in this file.
342. <u>- AR SITE PARAMETER</u> This file holds parameters that allows the site to customize certain functionality of the AR package.
     1.  <u>- AR GROUP</u> This file allows sites to define a "group", such as: Billing Agencies, Agent Cashier, Return Payment, etc. These groups represent a person, institution, or entity. Within each group, information can be defined that is used in the AR package. The main purpose for this file is for tracking address information.
     2.  <u>- AR GROUP TYPE</u> This file allows the user to define a group type name which can further defined in the AR GROUP file.
     3.  <u>– AR USER CUSTOMIZE FILE</u> This file stores the most recently selected parameters and the printer to be called by a user when customizing the screen and the printer options.
343. <u>- AR FORM LETTER</u> This file holds all the follow-up letters that the AR package supports. These letters can either be manually generated by the user or automatically generated by the AR package. New data will overwrite existing data. This file is not to be edited unless directed by Central Office.
344. <u>- AR BATCH PAYMENT</u> This file holds batch payment information. Payments no longer are posted directly to patient bills, but rather, entered into this file. Once the entries in this file are reconciled with cash on-hand and verified to be correct, they are then 'posted' to the patient bills during a background job. This file should NEVER be edited directly via VA FileMan. Information in this file should only be modified via the AR package options.
     1.  <u>- AR DEPOSIT</u> This file allows the user to create and define AR Deposit Tickets.
     2.  <u>– AR PAYMENT TRANSACTIONS FILE</u> This file is used to store payments received for automatic processing.
     3.  <u>- EDI LOCKBOX DEPOSIT</u> This file is used by EDI Lockbox module to store electronic deposit (EFT) summary information received as X12 835 messages via MailMan.

<u>344.31 – EDI THIRD PARTY EFT DETAIL</u> This file is used by EDI Lockbox module to store electronic deposit detail information from EFT messages.

<u>344.4 – ELECTRONIC REMITTANCE ADVICE</u> This file is used by EDI Lockbox module to store electronic remittance advice (ERA) information received as X12 835 messages via MailMan.

<u>344.49 – EDI LOCKBOX EOB WORKLIST</u> This work file or scratch pad is used by EDI Lockbox module to store manual adjustments made to ERA and is then used to create receipts.

5.  <u>– AR EDI LOCKBOX MESSAGE:</u> This file is used by EDI Lockbox module to store message exceptions. The EDI Lockbox Exceptions option is used to process exception manually.
6.  <u>- RCDPE AUTO-PAY EXCLUSION:</u> This file is populated based on the data in the ELECTRONIC REMITTANCE ADVICE file (#344.4). Whenever the nightly batch job encounters a new PAYER NAME/PAYER ID combination, a new record will be added to this file. The file will be maintained via the EDI Lockbox Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] option.
61. <u>- RCDPE PARAMETER</u> -: This file holds the parameters specific to the EDI Lockbox processes (ePayments).

<u>344.62- RCDPE CARC-RARC AUTO DEC:</u> This file will store all of the CARCs or RARCs that can be used during auto-decrease of a patient's bill.

<u>344.7 - RCDPE PARAMETER AUDIT</u> -: This file is for auditing changes to the RCDPE PARAMETER file (#344.61).

71. <u>- RCDPE SUSPENSE AUDIT:</u> This file will store all of the audit entries when an ERA line item is placed in suspense. Once in suspense, the suspended item will update the audit log whenever the suspended item is refunded or paid.
72. <u>- RCDPE AUTO-POST AUDIT:</u> This file will store the processing history of an ERA if the ERA can be auto-posted. Once the PRCA NIGHTLY PROCESS determines that an ERA can be auto-posted, an entry will be filed for every Auto-Post Status change (file 344, field 4.02).

<u>344.73 – RCDPE COMMENT HISTORY</u> – This file holds the history of receipt line comments from the AR BATCH PAYMENTS file (#344)

<u>344.9 - RCDPE DM REPORT PARAMETERS:</u> This file stores the parameters necessary for generating and if necessary, transmitting the AR Diagnostic Measures reports.

<u>344.91 - RCDPE DM REPORT ARCHIVE</u>: This file will store a copy of the AR Diagnostic Measures Reports generated as part of the Nightly Process.

345. <u>- AR EDI CARC DATA:</u> This file stores the codes and descriptions of the Claim Adjustment Remittance Codes (CARC) file published by the Washington Publishing Company. The CARC data is updated by the FSC, which has a subscription from WPC to obtain updated codes and descriptions.
     1.  <u>- AR PLB ADJUST CODE:</u> This file stores the codes and descriptions of the Provider Level Balance Codes (PLB Codes). The PLB Codes are published by CMS and originate from their Healthcare Integrated General Ledger Accounting System (HIGLAS).
346. <u>- AR EDI RARC DATA:</u> This file stores the codes and descriptions of the Remittance Advice Remark Codes (RARC) file published by the Washington Publishing Company. The RARC data is updated by the FSC that has a subscription to WPC for these codes.
347. <u>- AR FMS DOCUMENT</u> This file is invoked when an FMS Document is created by a user. It contains all the necessary information for the FMS Document transmission.
     1.  <u>- AR FMS DOCUMENT TYPE</u> This file is a pointer file to file 347 (AR FMS DOCUMENT). The document type is defined and created in this file.
     2.  <u>- AR FMS NDB TOTALS</u> This file holds the totals transmitted in summary to FMS with the running of the National Data Base. Currently, this includes Standard Vouchers and Summary Write-Offs.
     3.  <u>- REVENUE SOURCE CODES</u> This file contains the revenue source codes required for detail FMS documents. The revenue source code is used for the Reimbursable earnings report generated by FMS.
     4.  <u>- AR/FMS DOCUMENTS</u> This file contains the Transaction codes sent to FMS and the transaction code for related document. IE. BD 01 is sent to FMS, any other document that references the BD 01 must contain a related trans code.

<u>348 - AR NATIONAL DATA BASE CRITERIA</u> This file holds the data points for the Accounts Receivable Data collectors that transmit data to the National Data Base in San Francisco.

<u>348.1 - BAD DEBT ALLOWANCE</u> This file is used to store figures used in the bad debt allowance calculation.

<u>348.2 – TOP REFUND/REVERSAL CODES FILE</u> This file is used to store the Refund and Refund Reversal codes to be placed on the corresponding TOP documents. The codes are stored by calendar year. This file is updated through a menu option, whenever Treasury advises the VA of the codes for the next year.

<u>348.4 – AR DATA QUEUE FILE</u> This file contains bill entries which based upon certain criteria have been triggered into this file. These bill entries are used to export data information for CBO to the Boston Allocation Resource Center (ARC).

<u>348.5 – TCS IAI ERROR CODES FILE</u> This file holds the Cross-Servicing error codes for the Integrated Agency Interface (IAI) file transmission of debt/debtor records into FedDebt.

<u>348.6 - TCS IAI ACTION CODES FILE</u> This file holds the Cross-Servicing action codes for the Integrated Agency Interface (IAI) file transmission of debt/debtor records into FedDebt.

<u>348.7 – TCS IAI RECORD TYPES FILE</u> This file holds the Cross-Servicing record types for the Integrated Agency Interface (IAI) file transmission of debt/debtor records into FedDebt.

<u>349 - AR TRANSMISSION RECORDS FILE</u> This file is used to store transmission records that are sent by the Accounts Receivable software.

<u>349.1 - AR TRANSMISSION TYPE FILE</u> This file stores the transmission types used in file 349 AR TRANSMISSION RECORDS.

<u>349.2 - AR CCPC STATEMENTS FILE</u> This file stores the patient statement information that is sent from AR to CCPC.

<u>349.3 - AR RC TRANSMISSIONS FILE</u> This file keeps a record of the electronic AR Transmissions sent via the Regional Counsel Interface. Entries in this file will be purged routinely. This file may grow to be very large.

<u>349.4 - AR RC TRANSACTION CODES FILE</u> This file contains the transaction codes sent from the Regional Counsel Office for Third Party bills that are referred. Transmissions containing these codes will be applied to the bill as the AR action that is associated with the code. These associations were predetermined by the General Counsel Office and VACO MCCR. Modification of these codes is prohibited.

<u>348.5 - TCS IAI ERROR CODES FILE</u> This file contains the error code ID, field name/action, record type, and error message in the IAI error code file for Cross-Servicing.

<u>348.6 - TCS IAI ACTION CODE FILE</u> This file contains the action code, action description, and record type in the IAI action code file for Cross-Servicing.

<u>348.7 – TCS IAI RECORD TYPES FILE</u> This file contains the record type ID, record type description, and data type in the IAI transmission for Cross-Servicing.

<u>349.7 - CCPC STATEMENT ERRORS FILE</u> This file is a list of the errors that may be returned from CCPC as reasons for a patient statement not printing.

<u>349.8 - CCPC ERROR TYPE FILE</u> This file has all the error code types for CCPC.

<u>349.9 - AR TRANSMISSION SEGMENTS FILE</u> This file holds the information for AR transmission routers based on type.

<u>430 - ACCOUNTS RECEIVABLE</u> This is the main file of the Accounts Receivable system. It holds a permanent record, by Bill number, of the receivable. DO NOT USE FILEMAN TO EDIT THIS FILE DIRECTLY! Using VA FileMan will compromise system integrity. Use the AR menu options.

<u>430.2 - ACCOUNTS RECEIVABLE CATEGORY</u> This file stores the categories used for billing purposes. DO NOT EDIT THIS FILE! New data will overwrite existing data. The contents of this file are verified by the AR Background job, routine PRCABJV. If the entries in this routine do not match the contents of this file, the background job will not run. Make certain you edit this routine if you add or delete entries in this file.

<u>430.3 - ACCOUNTS RECEIVABLE TRANS.TYPE</u> This file stores the type categories used to identify transactions in the AR Transaction file (No. 433) along with flags that are set to control their use. DO NOT EDIT THIS FILE! New data will overwrite existing data. The contents of this file are verified by the AR Background job, routine PRCABJV. If the entries in this routine do not match the contents of the file, the background job will not run. Make certain you edit this routine if you add or delete entries in this file.

<u>430.4 – AR BILL NUMBER FILE</u> This file contains the established common numbering series for billing purposes. DO NOT USE FILEMAN TO EDIT THIS FILE DIRECTLY! Using FileMan will compromise system integrity. Use the AR menu options.

<u>430.5 – AR PARAMETER FILE</u> This file holds the station-specific parameters for the Billing and Accounts Receivable modules. Addresses, phone numbers, referral amounts, etc. are stored. This information is used throughout the AR system. DO NOT USE FIELMAN TO EDIT THIS FILE DIRECTLY! Using Fileman will compromise system integrity. Use the AR menu options.

<u>430.6 - AR DEBT LIST</u> This file holds short text entries that are used in the debt collection letters to identify the source of the Bill. DO NOT USE FILEMAN TO EDIT THIS FILE DIRECTLY! Using VA FileMan will compromise system integrity. Use the AR menu options.

<u>430.7 – AR BILLING ERROR HANDLING FILE</u> This file holds the error messages that appear in the bulletin that is sent when billing errors are detected by the AR package.

<u>430.8 - AR ARCHIVE</u> This file serves as a temporary storage file for archived AR Records. Entries in this file are populated by the AR Archive Module. DO NOT USE FILEMAN TO EDIT THIS FILE DIRECTLY!

<u>430.9 – AR CONVERSIONS FILE</u> This file will be used to store Account Receivable conversion data items. DO NOT USE VA FILEMANAGER TO EDIT THIS FILE DIRECTLY!

<u>431 – AR INTEREST RATE FILE</u> This file stores the effective dates and rates for interest and administrative charges levied on past due accounts. DO NOT USE FILEMAN TO EDIT THIS FILE DIRECTLY! Using Fileman will compromise system integrity. Use the AR menu options.

<u>433 - AR TRANSACTION</u> This file holds the Accounts Receivable transactions and all related information. DO NOT USE VA FILEMAN TO EDIT THIS FILE DIRECTLY! Using VA FileMan will compromise system integrity. Use the AR options.

<u>434 - ACCOUNTS RECEIVABLE FORM LETTER FILE</u> This file holds the text of the standardized Form Letters that must be mailed to the debtor. The text of the letters may be edited, but extreme care should be taken to not alter the formatting windows.

<u>435 - BATCH PAYMENT FILE</u> This file holds batch payments information. Payments no longer are posted directly to patient bills, but rather, entered into this file. Once the entries in this file are reconciled with cash on-hand and verified to be correct, they are then 'posted' to the patient bills during a background job.

<u>436.1 - AR MEDICARE DEDUCTIBLE ALERTS PART A FILE</u> This file is used to store Medicare Part A Deductible Alerts (MDA) that are received by the Financial Services Center (FSC) in Austin and sent to the individual sites. This data will be used by the new MDA work list so that Accounts Receivable personnel can take any necessary action.

# Accounts Receivable Menu Structure and Option Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pages are descriptions of the exported AR primary menus. There are main Accounts Receivable menus. They are as follows:

> Agent Cashier Menu

> AR Processing Menu

> Billing Menu

> Clerk Menu

> Supervisor Menu

> EDI Lockbox Menu

These menus were devised to follow the actual positions at a facility. Facility positions correspond to AR menus as follows:

| Primary Menu       | Brief Description                       | User’s Position          |
|--------------------|-----------------------------------------|--------------------------|
| Agent Cashier Menu | Manage the collection of patient debts  | Agent Cashier            |
| AR Processing Menu | Process debts for remote Acct System    | Accounting Technician    |
| Clerk’s Menu       | Manage the billing of MCCR debts        | Fiscal Clerk             |
| Billing Menu       | Manage the billing of Non-MCCR debts    | Billing Supervisor/Clerk |
| Payments Menu      | Manage 3rd Party payments               | ePayments Clerk          |
| Supervisor Menu    | Adjust debts and manage the AR software | AR Supervisor            |

<span id="_Toc67391149" class="anchor"></span>Table 22: Problem / Solution

There are several security keys which accompany this package and should be assigned to those individuals with a high level of authority (i.e., Fiscal Officer/Certifying Officer, Accounts Receivable Supervisor, Billing Supervisor, and certain AR Clerks.

Please note that these are only suggested menus. Your facility has the ability to create individualized menus, based on specific needs, using Menu Management. Please use the Diagram Options features of the Kernel to print copies of the full menus provided by AR. It is important that you work with the AR Application Coordinators in deciding the assignment of these menus and keys.

The following pages outline the Accounts Receivable Menu structure, along with descriptions of the menus and options.

## <u>Accounts Receivable Menu \[PRCAT USER\]</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Accounts Receivable Menu for the Accounting Technician.

> <u>Agent Cashier Menu \[RCDP AGENT CASHIER MENU\]:</u>

> This menu is the top-level menu for processing payments.

> <u>Account Profile \[RCDP ACCOUNT PROFILE\]</u>

> This option will allow you to profile a patient’s account.

> <u>Auto-Posted Receipt Report \[RCDPE AUTO-POST RECEIPT REPORT\]</u>

> This report displays receipt details associated with auto-posted ERA/EFT, including totals.

> <u>Bill Profile \[RCDP BILL PROFILE\]</u>

> This option will allow you to profile a bill.

> <u>Bill Transactions \[RCDP BILL TRANSACTIONS\]</u>

> This option will allow you to list all the transactions for a bill.

> <u>Deposit Processing \[RCDP DEPOSIT PROCESSING\]</u>

> This option will allow you to process deposits.

> <u>Extended Check/Trace/Credit Card Search</u>

> <u>\[RCDP EXTENDED CHECK/CC SEARCH\]</u>

> This option will search all payments for a check, trace \#, or credit card number.

> <u>Link Payment to Account \[RCDP LINK PAYMENT TO ACCOUNT\]</u>

> This option will allow you to link an unmatched payment to an account.

> <u>Link Payment Tracking Report \[RCDPE SUSPENSE AUDIT REPORT\]</u>

> This report displays the processing audit trail for all receipts that were placed in suspense.

> <u>List of Receipts Report \[RCDP LIST OF RECEIPTS REPORT\]</u>

> This option will print a list of receipts opened between selected date ranges.

> <u>Patient Payment/Refund Transaction History Inquiry</u>

> \[PRCA PAYMENT TRANS HISTORY\]

> This report lists a history of payment/refund transactions for a patient for a specified date range.

> <u>Receipt Processing \[RCDP RECEIPT PROCESSING\]</u>

> This option will allow you to process receipts.

> <u>Release Holds on AR \[PRCAY RELEASE HOLDS\]</u>

> This option allows the agent cashier to release holds on Means Test bills. There may be some requirements for the VA to "hold-off" billing the patient until payment is received from the insurance company. When a payment is received from an insurance company, any "holds" on bills to be sent to the patient need to be removed and the patient should be billed. This option allows the user to forward the bills from MCCR to AR to start the collection process.

> <u>Summary SF215 Report \[RCDP SUMMARY 215 REPORT\]</u>

> This option will print the summary 215 report for a selected deposit. It consists of an SF215 for each receipt in the deposit and a grand totals page summarizing all the receipt totals.

> <u>Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]</u>

> Set of actions and screens for Third Party AR/IB Joint Inquiry. Provides detailed information on any Third-Party Claim.

> <u>Transaction Profile \[RCDP TRANSACTION PROFILE\]</u>

> This option will allow you to profile a transaction recorded against a bill.

> <u>Bill Status Edit \[452 EDIT BILL STATUS\]</u>

> <u>Brief Account Profile \[PRCAY ACCOUNT PROFILE\]:</u>

> This option will display an Account Profile for Patient, Vendors, Insurance Companies, etc.

> <u>FMS Utilities Menu \[PRCA FMS UTILITIES\]</u>

> This top-level menu contains all the options to resend, edit and view FMS documents.

> <u>Document Status Inquiry \[PRCA FMS DOCUMENT INQUIRY\]</u>

> This main option contains the options for viewing an FMS document, for example a billing document, write-off, etc. that was sent to FMS.

> <u>Billing Document Inquiry \[PRCA FMS BILL INQ\]</u>

> This option is used to view the status of a detail bill sent to FMS.

> <u>Regenerate Prior Month OBR \[PRCA FMS OBR MANUAL TRANS\]</u>

> This option is used to regenerate the prior month Outstanding Bill Reconciliation report.

> <u>Transaction Inquiry \[PRCA FMS TRANS INQ\]</u>

> This option is used display the FMS status for an A/R transaction.

> <u>Unprocessed Document List \[PRCA FMS UNPROCESSED LIST\]</u>

> This option will print a list of FMS documents that have been updated three or more days ago.

> <u>FMS Cash Receipt Reconciliation (132 column.)\[ PRCA FMS DOC/RECPT COMPAR\]</u>

> This report allows the user to view Cash Receipt documents from a specified ticket number or range of numbers and dates. The receipts are categorized by appropriation. Each appropriation is totaled with a grand total of all receipts shown at the end.

> <u>FMS Regeneration Menu \[PRCA FMS REGENERATION\]</u>

> This option is the top-level menu for regenerating FMS documents to Austin.

> <u>Billing Document Regeneration \[PRCA FMS BD REGEN\]</u>

> This option regenerates an FMS document rejected in Austin.

> <u>Edit FMS Accounting Elements \[PRCA FMS ACCT EDIT\]</u>

> This option is used to edit the accounting line information on FMS billing documents.

> <u>Modified Billing Document Regeneration \[PRCA FMS MBD REGEN\]</u>

> This option regenerates a modified billing document that rejected in Austin.

> <u>National Data Base Document Regeneration \[PRCA FMS NDB REGEN\]</u>

> This option is used to regenerate FMS national data base documents.

> <u>Overpayment (OP) Document Regeneration \[PRCAT FMS OP REGEN\]</u>

> This option will allow a user to retransmit a "rejected" OP document. It will only allow the retransmission of an OP document that has actually been refunded in the AR package and has been rejected by FMS.

> <u>Regenerate FMS Cash Receipt Document \[PRCA FMS CASH RECEIPT\].</u>

> This option is to re-create and re-transmit the Cash Receipt Documents.

> <u>Remove invalid SUB BOC \[PRCA FMS SBOC\]</u>

> This option is used to remove an INVALID SUB BOC from a rejected FMS document.

> <u>Write-Off Document Regeneration \[PRCA FMS WRITE-OFF\]</u>

> This option is used to regenerate a rejected write-off document.

> <u>Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]</u>

> This option will display a full account profile of all bills for a debtor regardless of the status of the Bill.

> <u>Patient Payment/Refund Transaction History Inquiry \[PRCA PAYMENT TRANS HISTORY\]</u>

> This report lists a history of payment/refund transactions for a patient for a specified date range.

> <u>Payments posted from Prepayment \[PRCA PREPAY POST\]</u>

> This option lists, by date selected, the AR transactions that are decreases from prepayment bills, and their corresponding Accounts Receivable transactions that are either payments in full, or payments in part. An error will display if the decrease transaction and the payment transaction do not balance.

> <u>Profile of Accounts Receivable \[PRCAC PROFILE\]</u>

> This option displays all the AR data the user needs. He may see the data on his terminal screen or print the profile on a designated printer. The profile is classified by category: patient, vendor, or 3rd party.

> <u>Status Listing for Bills \[PRCAL STATUS LIST\]</u>

> This report will allow users to view bills by a particular status.

> <u>Transaction Profile \[PRCAC TRANS PROFILE\]</u>

> Use this option to see a profile of a single transaction. More complete information on an account is available with the PRCAC PROFILE option.

<u>Deposit Management \[PRCA DEPOSIT MGR\]</u>

This submenu allows the user access to the Deposit options.

> <u>Create Deposit Ticket \[PRCA CREATE DEPOSIT\]:</u> This option enables the user to create a new Deposit Ticket.

> <u>Deposit Money to Bank \[PRCA DEPOSIT MONEY\]:</u> This option allows the user to approve a ticket for deposit to a bank. If a deposit ticket has no receipt associated with it, the user will be asked to provide necessary information before the ticket can be approved.

> <u>Confirm Deposit from Bank \[PRCA CONFIRM DEPOSIT\]:</u> This option allows the user to select and summarily enter a confirmation that a deposit ticket number has been deposited to the bank.

> <u>Summary Listing of Deposits \[PRCA SUMMARY DEPOSIT\]:</u> By choosing this option, the user is able to view information about past and current deposit tickets.

> <u>Edit a Deposit Ticket \[PRCA EDIT A DEPOSIT\]:</u> This option allows the user to change information on a deposit ticket.

> <u>Process Deposit \[PRCA PROCESS DEPOSIT\]:</u> This option allows the user to transmit or *process* a deposit ticket to FMS.

> <u>Receipt List for Deposit \[PRCA RECEIPT LIST\]:</u> This option shows information associated with receipts that are attached to selected deposit tickets.

> <u>View a Deposit \[PRCA VIEW A DEPOSIT\]:</u> By using this option, the user can view detailed information about a specific deposit ticket.

> <u>Void a Deposit \[PRCAY VOID DEPOSIT\]:</u> This option allows the user to void a Deposit Ticket. The ticket must first be “emptied” of all receipts.

> <u>Print 215 Report \[PRCAY PRINT 215\]</u>

> This option will print a 215 Report, sorted by appropriation number for a given receipt number entered by the user. It will also show errors of payment (a payment entered without an appropriation) and posting errors.

<u>BILLING \[PRCA BILL\]</u>

This is the main menu for the Billing module. It is used by Billing Clerks and Billing Supervisors. The options on this menu that are locked with the PRCASVC key are available to and seen by Billing Supervisors, but not by Billing Clerks.

<u>New Bill (Enter) \[PRCA BIL ENTER\]</u>

This option is used to enter a new Bill. The Bill number is assigned by the system from the series established for each service. After entering all the information, the user can display or print the Bill.

<u>Display Pending Bill \[PRCA BIL PRNT\]</u>

This option allows the user to display a Bill on the current terminal or print the Bill on a printer.

<u>Approve/Print Pending Bill \[PRCA BIL APPROVE\]</u>

This option allows the user to electronically sign a Bill and send it to Fiscal.

<u>Edit Bill \[PRCA BIL EDIT\]</u>

This option allows the user to edit all information in a Bill.

<u>Cancel Bill \[PRCA BIL CANCEL\]</u>

This option allows the user to cancel a Bill that has not been approved.

<u>Amend Bill Returned from AR \[PRCA BIL AMEND\]</u>

Users at the Service/Section level can use this option to correct a Bill that has been returned for amendment.

<u>Bill Status Listing \[PRCA BILL STATUS LISTING\]</u>

This option will allow a service to list Bills in a certain status for their respective service.

<u>List All Bills \[PRCA LIST ALL BILLS\]</u>

This option will list all bills for the service of the person that has generated the report. The report will display information, such as Form Type, Original Amount, Current Balance, Debtor, and Bill \# sort by Status.

<u>View a Bill \[PRCA VIEW A BILL\]</u>

This option allows the service to view a Bill that was entered. The information displayed will show the current status and follow-up action taken and the final results (Written-off, collected, canceled, etc.).

<u>FINANCE AR MANAGER MENU \[PRCA MANAGER MENU\]</u>

This menu contains both the Clerk's AR and Supervisor's AR menus. This menu is available to and used by Fiscal Officers.

<u>Clerk's AR Menu \[PRCA CLERK MENU\]</u>

This is the menu for the Accounts Receivable Clerk. It also contains the Agent Cashier Menu, which contains options available to the Agent Cashiers. Note that the locked options are seen by and accessible to only those AR Clerks and/or Agent Cashiers holding the PRCAY PAYMENT SUP security key.

<u>Supervisor's AR Menu \[PRCAF SUPERVISOR MENU\]</u>

This is the menu for the Accounts Receivable Supervisor.

<u>EDI Diagnostic Measures Reports … \[RCDPE EDI NATIONAL REPORTS\]</u>

This is a menu for AR's EDI Diagnostic Measures National Reports. These reports allow a facility to measure the current usage rates of electronic billing to and electronic payments from third party insurers.

<u>CLERK'S AR MENU \[PRCA CLERK MENU\]</u>

This is the menu for the Accounts Receivable Clerk. It also contains the Agent Cashier Menu, which contains options available to the Agent Cashiers. Note that the locked options are seen by and accessible to only those AR Clerks and/or Agent Cashiers holding the PRCAY PAYMENT SUP security key.

<u>Audit/Set up a New Accounts Receivable \[PRCAA SET/AUDIT NEW BILL\]</u>

This menu has options that allow the AR Clerk to audit bills and establish new accounts. An account for the debtor must exist before the audit of a Bill can be completed. The system will prompt for account information if necessary.

> <u>Audit an Electronic Bill \[PRCAA AUDIT\]</u>

> Audit a new Accounts Receivable from generating services such as MAS, Supply service, and Library. You may return this Bill to the originating service.

> <u>Set up and Audit New Accounts Receivable \[PRCAA SETUP BILL\]</u>

> This option establishes a new account for bills entered by a service. The bills will be classified by category.

> <u>Amended Bill Audit \[PRCAA AMEND AUDIT\]</u>

> Fiscal uses this option to audit a Bill that was returned for amendment and is on its second or subsequent pass through the system.

> <u>Edit an Incomplete Accounts Receivable \[PRCAA INCOMPLETE\]</u>

> This edits an incomplete accounts receivable. The current status of this account is "I"-incomplete. This account will be inactive until the status is changed to active.

<u>New Bill Forms Print \[PRCAB PRINT BILLS\]</u>

Use this option to print the newly arrived Bill forms generated by services. The Bill forms are UB-92, 1080 and 1081.

> <u>Other Bill Form Print \[PRCAB PRINT OTHER BILLS\]</u>

> Use this option to print the new 1080 and 1081 free form bills generated by the services.

> <u>Reprint "Other" Bill \[PRCAB REPRINT OTHER BILL\]</u>

> This is used to reprint 1080 and 1081 bills.

> <u>Profile of Accounts Receivable \[PRCAC PROFILE\]</u>

> This displays all the AR data the user needs. The user may see this data on the terminal screen or print the profile on a designated printer. The profile is classified by category, e.g. patient, vendor, or 3rd party.

<u>Update Accounts Receivable \[PRCAC CHANGE\]</u>

This supervisory menu contains the options for changing/editing accounts and accounts receivable.

> <u>Locate Debtor's Address \[PRCAC LOCATE DEBTOR\]</u>

> This option maintains a record of attempts to track the debtor's current address through the State Department of Motor Vehicles (or equivalent), Internal Revenue Service, Credit Agency Check, Patient Folder, etc.

> <u>DC/DOJ Action Menu \[PRCAC DCDOJ ACTION MENU\]</u>

> This menu contains options that create and maintain records of all accounts that are referred to the District Counsel or the Department of Justice.

> <u>Refer to DC/DOJ \[PRCAC DCDOJ REFER\]</u>

> Use this option to record the date and amount data for an account which is being referred to the District Counsel or Department of Justice.

> <u>Returned by DC/DOJ \[PRCAC DCDOJ RETURNED\]</u>

> Use this option to record the date returned by DC/DOJ for an account that was referred. This option should be used for recording accounts that are returned by DC/DOJ because the debt has been cleared as a result of corrective award action, or accounts that are returned and will be cleared by appropriate write-off because of death, bankruptcy, etc.

> <u>Re-Refer to DC/DOJ \[PRCAC DCDOJ REREFER\]</u>

> Use this option to re-refer an account to the District Counsel or the Department of Justice.

> <u>Debit Voucher (SF 5515) \[PRCAC DCDOJ DEBIT\]</u>

> Use this option to apply a debit voucher transaction from the District Counsel or the Department of Justice.

> <u>Waived by DC/DOJ \[PRCAC DCDOJ WAIVER\]</u>

> Use this option to apply the transaction for an account that is being waived by the District Counsel or Department of Justice. The account should have already been referred to the DC/DOJ for this option to function.

> <u>Terminated by DC/DOJ \[PRCAC DCDOJ TERM\]</u>

> Use this option to terminate an account that has been sent to the District Counsel or Department of Justice when it has been determined that the debt is not collectible, and the DC/DOJ file has been closed.

> <u>Compromised by DC/DOJ \[PRCAC DCDOJ COMPROMISE\]</u>

> Use this option to apply a compromise transaction to an account that was referred to the District Counsel or Department of Justice for collection.

> <u>Repayment Plan Menu \[PRCAC REPAYMENT MENU\]</u>

> This is the Repayment Plan Menu.

> <u>Edit Existing Repayment Plan \[RCRP EDIT REPAYMENT PLAN\]</u>

> This option allows users to modify the terms of an existing Repayment Plan or close the plan.

> <u>Add New Bill to a Repayment Plan \[RCAC REPAY ADD\]</u>

> This option allows users to add new bills to an existing Repayment Plan.

> <u>Enter a New Repayment Plan \[RCRP ENTER PAYMENT PLAN\]</u>

> This option allows a user to create a new Repayment Plan for a Debtor by identifying the bills eligible for inclusion in a Repayment Plan, set the Monthly Payment (and by calculation, the length of the plan), and the date the first payment is due.

> <u>Repayment Plan Inquiry \[PRCAC PLAN INQUIRY\]</u>

> This option is used to run repayment plan inquiry.

> <u>Repayment Plan Status Report \[PRCAC PLAN STATUS REPORT\]</u>

> This option is used to run the Repayment Plan Status Report.

> <u>Add an Administrative Cost \[PRCAC TR ADM\]</u>

> This option adds an administrative cost to the accounts receivable. The cost could be marshal fee, court cost, IRS Loc. cost, Credit Rep. cost, Dept. of Motor Vehicles Loc. cost, Consumer Rep. Agency cost, etc. These costs are accrued to the administrative cost balance automatically.

> <u>3rd Party Information Data Edit \[PRCAC 3RD DATA\]</u>

> Edit 3rd party information data - insurer's name, ID number, group name, group number and employer's information.

> <u>Update 'Bill Resulting From' Data \[PRCAC BILL RESULTING\]</u>

> Use this option to update the 'BILL RESULTING FROM' information. These are brief statements that are used in the follow-up letters to identify the source/cause of the bill.

> <u>COWC Referral \[PRCAC COWC REFER\]</u>

> Use this option to keep a record of an account that is being referred to the DVB Committee on Waivers and Compromise. The referral date may be changed if found to be incorrect.

> <u>Adjustment to Accounts Receivable \[PRCAC TRANSACTION\]</u>

> This is a menu option that contains the adjustment, waiver, suspend, reestablish, and termination transaction options.

> <u>Adjustment to an AR record \[PRCAC TR ADJUSTMENT\]</u>

> This option is used to make adjustments to an account. An adjustment is used to reflect revision to the principal balance. A decrease adjustment will cause a negative adjustment to principal balance.

> <u>Decrease Adjustment \[PRCAC TR DECREASE\]</u>

> This option enters an adjustment that decreases an account's principal balance.

> <u>Increase Adjustment \[PRCAC TR INCREASE\]</u>

> This option enters an adjustment that increases an account's principal balance.

> <u>Waive an Accounts Receivable \[PRCAC TR WAIVED\]</u>

> This option is used to waive an accounts receivable. There are two types of waiver transactions- Waived in full and waived in part. In case of waived in full, the current status of the accounts will be changed to inactive. In the case of a partial waiver, the amount will be applied to the principal balance.

> <u>Partial Waiver \[PRCAC WAIVED PART\]</u>

> Use this option when the AR is waived in part. The account remains active.

> <u>Full Waiver \[PRCAC WAIVED FULL\]</u>

> Use this option when the AR is waived in full. The account will be written-off, and its status changed to "Write-Off".

> <u>Terminate an Accounts Receivable \[PRCAC TR TERMINATION\]</u>

> This option is used to terminate an accounts receivable at the user's request. There are two types of Termination transactions: Terminated by Fiscal Officer and Terminated by compromise with DC/DOJ. This termination changes the current status of the account to “Write-Off”.

> <u>Fiscal Officer Terminated \[PRCAC TR TERM-FISCAL\]</u>

> Use this option to process the account terminated by fiscal officer. This changes the account's status to "Write-Off".

> <u>Compromise Termination \[PRCAC TR TERMCOMPROMISE\]</u>

> Use this option to process the account terminated by compromise. This changes the account's status to "Write-Off".

> <u>Re-Establish Bill \[PRCAC TR RE-ESTABLISH BILL\]</u>

> This option is used to re-activate a Bill that is in the Write-Off, Suspended, Cancellation or Collected/Closed status. This will create a Re-establish Transaction and change the status of the Bill to Active (not prepayment Bill). If the Bill has no balance, you must enter in the re-establish amount of the Bill which will be the principal balance of the Bill.

> <u>Suspend an AR Bill \[PRCAC TR SUSPENDED\]</u>

> This option will allow the user to place a selected AR Bill that has a principal balance into the Suspended status. A Bill in this status will not print on the patient's statement but it does accrue administrative charges. The status of the selected Bill will change to Suspended and create a SUSPENSE transaction for the current outstanding amount.

<u>Report Menu for Accounts Receivable \[PRCAD REPORT MENU\]</u>

This is a menu of options for printing formal reports for AMIS Reports, 3rd Party Bills, Delinquent Accounts, etc.

> <u>Accounts Receivable Status Reports \[PRCAL LIST MENU\]</u>

> This is a menu of options to display lists of bills by status (new, incomplete, active, and written- off) or referral action (District Counsel or Department of Justice).

> <u>DC Pending Referral AR Listing \[PRCAL REFER DC\]</u>

> This option prints a list of accounts pending referral to the District Counsel based on a principal balance within the ranges set by the PRCAF PARM DC option and showing no account activity for thirty days after the third follow-up letter.

> <u>DOJ Pending Referral AR Listing \[PRCAL REFER DOJ\]</u>

> This option prints a list of accounts pending referral to the Department of Justice based on a principal balance exceeding the minimum set by the PRCAF PARM DOJ option and showing no account activity for thirty days after the third follow-up letter.

> <u>Medicare Deductible Alert Worklist \[PRCA MDA WORKLIST\]</u>

> This option is the work list for processing Medicare Deductible Alerts.

> <u>Category Listing for Bills \[PRCAL OTHER LIST\]</u>

> Use this option to print a listing of receivables other than Category C. You will need to select the current status and category.

> <u>Status Listing For Bills \[PRCAL STATUS LIST\]</u>

> This report will allow users to view bills by a particular status.

> <u>Refunds to be Approved by Certifying Official \[PRCA REFUND REVIEW LIST\]</u>

> This option is used to print all refunds that have been REFUNDED, but that have not been approved by the certifying official to be transmitted to FMS.

> <u>Delinquent AR Reports \[PRCAD R DELINQUENT MENU\]</u>

> This is a menu of options for printing delinquent account reports.

> <u>31-90 Delinquent Accounts \[PRCAD RDL 90\]</u>

> This prints a list of accounts delinquent 31-90 days.

> <u>91-180 days Delinquent Accounts \[PRCAD RDL 180\]</u>

> This prints a list of accounts delinquent 91-180 days.

> <u>181-365 days Delinquent Accounts \[PRCAD RDL 365\]</u>

> This prints a list of accounts delinquent 181-365 days.

> <u>Over 365 days Delinquent Accounts \[PRCAD RDL OVER365\]</u>

> This prints a list of accounts delinquent more than 365 days.

> <u>Print All Delinquent Accounts \[PRCAD RDL ALL\]</u>

> This prints a list of all accounts delinquent more than 30 days.

> <u>Report of AR by Last Activity Date \[PRCA LAST ACTIVITY\]</u>

> This report will print bills, sorted by category, by the date of last activity. The date of last activity is defined as the date of when the bills were last "looked" at or had some activity. This date is derived by finding the most recent date of the following:

1.  Last time a letter printed (LETTER1, LETTER2, LETTER3)
2.  Date Bill was prepared
3.  Date status was last updated
4.  Date the last transaction was entered into the system or Transaction date

> If none of these dates are found, then the default date is 01/01/91. Only those bills in an "unresolved" status (Active, Suspense, etc.) are printed. Those bills that have been resolved are not displayed.

<u>Management Reports \[PRCAD MANAGEMENT REPORT MENU\]</u>

This is a menu of options used to print reports on 3rd Party Accounts, Admin/Interest Rates, AMIS Reports, etc.

> <u>3rd Party Accounts Report Print \[PRCAD R 3RD\]</u>

> This prints the active 3rd Party Accounts, sorted by Debtor.

> <u>Admin/Interest Rates Print \[PRCAD R INT RATE\]</u>

> This prints a list of Admin/Interest Rates -- daily, monthly, and annual rates are displayed.

> <u>DC/DOJ Debt Collection Report \[PRCAD DCDOJ COLLECTION\]</u>

> This is a menu for the DC/DOJ debt collection report, RCS 04-0462/0464.

> <u>DC Debt Collection Report \[PRCAD DC COLLECT\]</u>

> Use this option to print the District Counsel debt collection report. This is needed to prepare the VA Form 4-5320a/b.

> <u>DOJ Debt Collection Report \[PRCAD DOJ COLLECTION\]</u>

> Use this print-out to prepare the VA Form 4-5320a/b, Department of Justice Debt Collection Report.

> <u>Co-Pay Waiver Report \[PRCA CO-PAY WAIVER REPORT\]</u>

> This option allows the user to enter data for lines 9-20 of the co-pay waiver report. After the user accepts this data entry, a background job is queued to compile data for lines 1-8. After compilation of the data, the report is sent to G.PCWMCCR at FORUM (in string format). The report also is delivered to the sender’s IN box in a printed format.

> <u>Contingent 3rd party AR Report \[PRCAD CONTINGENT 3RD\]</u>

> This option prints the contingent 3rd Party Accounts referred to the District Counsel or Department of Justice for collection.

> <u>IRS Offset Report \[PRCA IRS OFFSET\]</u>

> This report is run monthly and provides a snapshot of the current status of AR's referred to IRS for offset. It shows, as of a point in time, the number of IRS Offset letters that were printed since the last IRS Offset report and the total amount of debt corresponding to those letters, as well as the number and value of debts actually referred to the IRS, and the amount of collections on debts that have received by IRS for offset.

> <u>Medication Co-pay Exemption Report \[PRCAX CO-PAY EXEMPTION REPORT\]</u>

> This option produces a report showing the medication co-pay exemption adjustments applied to the system for a given time period selected by the user. The report will display the patient name, patient ID, Bill number, transaction number, and transaction amount for the adjustment.

> <u>Payments with Write-offs Report \[PRCA PAYMENTS WITH WRITE-OFFS\]</u>

> This report will show patients that have made payments and have bills in the write-off status. This report would be used to re-evaluate if bills in the write-off status should be made active for collection purposes. Written-off bills are still collectable and follow-up action should be activated for these bills if the patient is making payments.

> <u>Revenue Code Totals by Rate Type \[PRCAD REV CODE TOTALS\]</u>

> Prints totals of Revenue Code amounts by Rate Type. To collect data for AMIS Segments 295 and 296.

> <u>Transaction History \[PRCA TRAN TYPE HISTORY\]</u>

> This option will create a report that will list all transactions sorted by type of transaction, category of bill and date for the specified type of transaction, category of bill and date range.

<u>Reconciliation Reports \[PRCAD RECONCILE MENU\]</u>

This is a menu of options for printing reconciliation reports for District Counsel, Department of Justice, Committee on Waivers and Compromise, MAS, other services, Agent Cashier, etc.

> <u>Date Sorted Payment Report \[PRCAD RECON CASHIER\]</u>

> This option prints the agent cashier reconciliation report. Choose the time period for the report. The Bill \#, Payment Receipt \#, Payment date and Payment amount will be shown.

> <u>MAS Reconciliation Report ... \[PRCAD MAS REPORT\]</u>

> This is a menu for bills generated by MAS to reconcile between Fiscal and MAS.

> <u>Third Party Completed \[PRCAD RECON MAS\]</u>

> This option prints the MAS reconciliation report. Choose the time period for the report. This report prints the 3rd party accounts only. The Bill \#, Date bill prepared, and Original amount will be shown.

> <u>Other Completed \[PRCAD MAS COMPLETE\]</u>

> This prints the bills accepted by Fiscal for the designated period. This prints only MAS bills.

> <u>Incomplete \[PRCAD MAS INCOMPLETE\]</u>

> This prints the bills with 'Bill Incomplete' status generated by Service.

> <u>DC Referred Report Print \[PRCAD R DC\]</u>

> This option prints a list of the Accounts which have been referred to the District Counsel.

> <u>DOJ Referred Report Print \[PRCAD R DOJ\]</u>

> This option prints a listing of the Accounts which have been referred to the Department of Justice. The principal balance on the account is greater than \$1200 unless otherwise set.

> <u>COWC Referred Report Print \[PRCAD COWC LIST\]</u>

> Use this option to get a listing of the accounts referred to the DVB Committee of Waivers and Compromise.

> <u>ARDC Monthly Reconciliation Report \[PRCA ARDC MONTHLY REPORT\]</u> This report will provide a capture of the data sent to FMS on the monthly roll-up basis and will include detail of the bills and associated data at the time the roll up was completed.

> <u>Payments Posted from Prepayment \[PRCA PREPAY POST\]</u>

> This option will list by date selected, the AR Transactions that are Decreases from Prepayment bills and their corresponding AR Transaction that is a Payment in Full or Payment in Part to an Account Receivable bill. An error will display if the decrease transaction and the payment transaction don't balance.

> Payment transactions that are applied to bills that are not in the 36x5014 Appropriation will be flagged, in order to notify the AR Tech. to include that payment amount on a 928.23 transaction type code sheet.

<u>Follow-up Letter Menu \[PRCAE FOLLOW-UP\]</u>

This is a menu that contains options for Follow-up letters, Form letters, Patient Statements, and IRS Letters.

> <u>Hold Printing a Follow-up Letter \[PRCAE L HOLD\]</u>

> This option holds the printing of a follow-up letter until the letter is released.

> NOTE: This option does not hold the printing of bills or charges on the patient statement.

> <u>Remove Hold on Follow-Up Letter \[PRCAE LET REL\]</u>

> This release held letters for printing.

> <u>Print Statements/Letters by Date \[PRCAE PR LETTERS\]</u>

> This option will print Patient Statements and Follow-up Letters that should have printed on the selected date but didn't. All statements and letters will print if no patient is selected.

> NOTE: Enter a patient name to print a Patient Statement for one patient. If no statement prints and an Account Balance Discrepancy bulletin is not generated, it may be because the account has no new activity other than interest charges.

> <u>IRS offset letters (print/reprint) \[PRCAE IRS OFFSET\]</u>

> This option will print IRS OFFSET demand letters for ARs that are eligible for referral to IRS. This option should be run at least once a year around the third week in September. However, it can be run more than once per year, for example, at the beg inning of September and at the end of September. It is recommended to run this option at least once during the end of September, since this will find the maximum number of ARs eligible for IRS OFFSET.

> NOTE: This option can only be run during 9/1 through 9/20 of each year.

> <u>List of Accounts Receivable with Holds \[PRCAE LIST HOLD\]</u>

> This prints the list of follow-up letters being held.

> <u>Reprint Patient Statements \[PRCAE PR STATEMENT\]</u>

> This option will reprint Patient Statements for the selected date. Enter a patient range in print order to have only the statements I that sequence reprint or do not select a range to reprint all statements for the selected date.

> NOTE: This option will not reprint Follow-up Letters.

> <u>Reprint the Follow-up Letters \[PRCAE REPRINT LETTERS\]</u>

> This option allows you to reprint a Follow-up Letter for the selected date. You may enter a range of bills to print (print order range) or have all the Follow-up Letters reprint for that date by not selecting a Bill to start or end the sort.

> NOTE: This option will not reprint Patient Statements.

> <u>Reprint UB Letters \[PRCAE REPRINT UB\]</u>

> This option allows you to reprint a UB Letter for the selected date. You may enter a range of bills to print (print order range) or have all the UB Letters reprint for that date by not selecting a Bill to start or end the sort.

<u>Establish/Edit Old Bills \[PRCAA OLD BILL\]</u>

Use this menu to establish or edit old bills. The process is called "back-loading" paper bills into the system bills that have already been forwarded to the Accounting Technician.

> <u>Set Up Old Bills \[PRCAA OLD SETUP\]</u>

> Use this option to enter old bills into the Accounts Receivable File. The user can back-load bills that existed before installation of the AR Package.

> <u>Edit Incomplete Old Bills \[PRCAA OLD EDIT\]</u>

> Use this to update the incomplete old bills. If the current status of the account is "OLD BILL", the Bill should be edited with this option.

<u>Transaction Profile \[PRCAC TRANS PROFILE\]</u>

Use this option to see a profile of a single transaction. More complete information on an account is available with the PRCAC PROFILE option.

<u>Account Management \[PRCA ACCOUNT MANAGEMENT\]</u>

This option allows the user to enter or log information specific to a debtor account, such as, address information and comments.

> <u>Account Information \[PRCA ACCOUNT INFORMATION\]</u>

> This option will allow the user to edit AR Debtor Information.

> <u>Address Display/Edit \[PRCA VEN BIL\]</u>

> This option edits the billing address of debtors.

> <u>Bill Comment Log \[PRCA BILL COMMENT\]</u>

> This option will allow the user to enter a COMMENT type transaction for a Bill. This allows follow-up action or patient contact to be logged against the Bill for documenting follow-up activity.

> <u>Brief Account Profile \[PRCAY ACCOUNT PROFILE\]</u>

> This option will display an Account Profile for Patient, Vendors, Insurance Companies, etc.

> <u>Check Patient Account Balance \[PRCA ACCOUNT CHECK\]</u>

> This option will check a selected patient's account and display information regarding the printing of the patient's statement. This option should be used when a discrepancy is found. This option should also be used to review a patient's statement before it prints.

> <u>Debtor Comment Log \[PRCA DEBTOR COMMENT\]</u>

> This option will allow the user to enter a comment for a debtor that can be later profiled.

> <u>Follow-up Reports \[PRCA FOLLOW-UP REPORTS\]</u>

> This option will print a report of the follow-up transactions for bills and follow-up actions for a debtor. The report will prompt the user for date range and any comment "flagged" for follow-up within the date range will display on the report.

> <u>Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]</u>

> This option will display a full account profile of all bills for a debtor regardless of the status of the Bill.

> <u>Mark/Unmark Invalid Transaction \[PRCA MARK INVALID TRANS.\]</u>

> This option is used to flag a transaction so that it does not appear on the patient statement.

> <u>Statement Discrepancy Listing \[PRCA DISC LIST\]</u>

> This option will list all the AR Debtors whose accounts do not balance. Use this option to generate a list of debtors who are not receiving statements because of balance discrepancies. This option takes a while to run. You should queue this report to a printer.

> <u>Transaction History for a Patient \[PRCA TRANS HISTORY\]</u>

> This option will allow the user to print a type of transaction or all transactions for a patient for a selected date range.

<u>Agent Cashier \[PRCAY MASTER\]</u>

This option is the top -level menu for Payment processing.

> <u>Cash Payment \[PRCAY CASH PAYMENT Synonym: CS\]</u>

> This option is used to enter a cash payment for both mail-in and window payments. This option batches payments to be posted to the accounts at a later time.

> <u>Check/MO Payment \[PRCAY CHECK/MO PAYMENT Synonym: CM\]</u>

> This option is used to enter mail-in and window check and money order payments. This option batches payments to be posted to the accounts at a later time.

> <u>Credit Card Payment \[PRCAY CREDIT CARD PAYMENT Synonym: CC\]</u>

> This option is used for mail-in and window credit card payments. This option batches payments that will be posted to the accounts at a later time.

> <u>Other Payment \[PRCAY OTHER PAYMENT Synonym: OP\]</u>

> This option allows the user to enter payment for TDA type payments. This option is very similar to the cash payment option but allows a different receipt to be open and used for TDA payments.

> <u>Cancel a Payment Transaction \[PRCAY CANCEL PAYMENT Synonym: CP\]</u>

> This option will allow the Agent Cashier to cancel a payment transaction and re-enter the payment as a new transaction.

> <u>Move A Payment Transaction \[PRCAY MOVE A PAYMENT Synonym: MV\]</u>

> This option will allow the agent cashier to copy a payment transaction from one receipt to another, provided that the receipt being copied from is cash and the receipt or payment has not already been processed.

> <u>Patient Payment/Refund Transaction History Inquiry</u>

> <u>\[PRCA PAYMENT TRANS HISTORY</u> <u>Synonym: PD\]</u>

> This report lists a history of payment/refund transactions for a patient for a specified date range.

> <u>Brief Account Profile \[PRCAY ACCOUNT PROFILE Synonym: BR\]</u>

> This option will display an Account Profile for Patient, Vendors, Insurance Companies, etc.

> <u>Deposit Management \[PRCAY DEPOSIT MANAGEMENT Synonym: DM\]</u>

> This sub-menu allows the user access to the Deposit options.

> <u>Create Deposit Ticket \[PRCA CREATE DEPOSIT\]</u>

> This option enables the user to create a new Deposit Ticket.

> <u>Deposit Money to Bank \[PRCA DEPOSIT MONEY\]</u>

> This option allows the user to approve a ticket for deposit to a bank. If a deposit ticket has no receipt associated with it, the user will be asked to provide necessary information before the ticket can be approved.

> <u>Edit a Deposit Ticket \[PRCA EDIT A DEPOSIT\]</u>

> This option allows the user to change information on a deposit ticket.

> <u>Receipt List for Deposit \[PRCA RECEIPT LIST\]</u>

> This option shows information associated with receipts that are attached to selected deposit tickets.

> <u>Summary Listing of Deposits \[PRCA SUMMARY DEPOSIT\]</u>

> By choosing this option, the user is able to view information about past and current deposit tickets.

> <u>View a Deposit \[PRCA VIEW A DEPOSIT\]</u>

> By using this option, the user can view detailed information about a specific deposit ticket.

> <u>Void a Deposit \[PRCAY VOID DEPOSIT\]</u>

> This option allows the user to void a Deposit Ticket. The ticket must first be “emptied” of all receipts.

> <u>Full Account Profile \[PRCAY FULL ACCOUNT PROFILE Synonym: FU\]</u>

> This option will display a full account profile of all bills for a debtor regardless of the status of the Bill.

> <u>Print 215 Report \[PRCAY PRINT 215 Synonym: P2\]</u>

> This option will print a 215 report, sorted by appropriation number for a given receipt number entered by the user. It will also show errors of payment (a payment entered without an appropriation) and posting errors.

> <u>Profile of Accounts Receivable \[PRCAC PROFILE\]</u>

> This displays all the AR data the user needs. He may see the data on his terminal screen or print the profile on a designated printer. The profile is classified by category: patient, vendor or 3rd party.

> <u>Release Holds on AR \[PRCAY RELEASE HOLDS Synonym: RH\]</u>

> This option allows the agent cashier to release "holds" on Means Test bills. There may be some requirements for the VA to "hold-off" billing the patient until payment is received from the insurance company. When a payment is received from an insurance company, any "holds" on bills to be sent to the patient need to be removed and the patient should be billed. This option allows the user to forward the bills from MCCR to AR to start the collection process.

> <u>Receipt Management \[PRCAY RECEIPT MANAGEMENT Synonym: RM\]</u>

> This menu will allow the user to manage receipts. This includes posting, approving, reviewing, etc. type options for receipts.

> <u>Approve a Receipt \[PRCAY APPROVE BATCH\]</u>

> This option will mark a batch as approved and ready for posting to the A/R Transaction File.

> <u>Edit A Receipt \[PRCAY EDIT A RECEIPT\]</u>

> This option allows the user to edit a receipt.

> <u>List of Receipts \[PRCAY LIST RECEIPTS\]</u>

> This option will print a report of all receipts recorded with un-archived payments. The report is sorted by date and shows the receipt number, date posted, amount of payment, the bill that reflects the payment, and the user who posted the payment.

> <u>Post an Approved Receipt to Accounts \[PRCAY POST TRANS\]</u>

> This option will post the transactions in an approved batch to the A/R Transaction File. Users can only post a batch which they approved, unless they hold the supervisor’s key.

> <u>Receipt Number Reconciliation Report \[PRCAD RECON CASH RECEIPT\]</u>

> This will print the Agent Cashier Reconciliation Report sorted by the Receipt Number.

> <u>Reprint a Customer's Receipt \[PRCAY REPRINT A RECEIPT\]</u>

> This option will allow an Agent Cashier to reprint a receipt for a payment transaction. If a payment was canceled, the amount printed on the receipt will be zero.

> <u>Summary of Current Receipts \[PRCAY SUMMARY OF CURRENT\]</u>

> This option will list a summary of current receipts in the system. This report will show who opened a receipt batch, when the batch was opened, number of transactions in the batch, and who approved the batch for posting to patient accounts.

> <u>Void A Receipt \[PRCAY VOID A RECEIPT\]</u>

> This option will allow a receipt that was entered in error and has not had any payment transactions entered to be voided. The receipt will be purged with the other receipts.

> <u>Transaction Profile \[PRCAC TRANS PROFILE Synonym: TP\]</u>

> Use this option to see a profile of a single transaction. More complete information on an account is available with the PRCAC PROFILE option.

<u>FMS Utilities Menu \[PRCA FMS UTILTIES\]</u>

This top level menu contains all the options to resend, edit and view FMS documents.

> <u>Document Status Inquiry \[PRCA FMS DOCUMENT INQUIRY\]</u>

> This main option contains the options for viewing an FMS doc, for example billing document, write-off, etc. that was sent to FMS

> <u>Billing Document Inquiry \[PRCA FMS BILL INQ\]</u>

> This option is used to view the status of a detail bill sent to FMS

> <u>Regenerate Prior Month OBR \[PRCA FMS OBR MANUAL TRANS\]</u>

> This option recreates and sends the Outstanding Bill Reconciliation report to the local user’s group.

> <u>Transaction Inquiry \[PRCA FMS TRANS INQ\]</u>

> This option is used display the FMS status for an A/R transaction.

> <u>Unprocessed Document List \[PRCA FMS UNPROCESSED LIST\]</u>

> This option will print a list of FMS documents that have been updated three or more days ago.

> <u>FMS Cash Receipt Reconciliation (132 column) \[PRCA FMS DOC/RECPT COMPAR\]</u>

> This report is to print all receipts for a deposit and gives total for each fund under the deposit within a particular status.

> <u>FMS Regeneration Menu \[PRCA FMS REGENERATION\]</u>

> This option is the top-level menu for regenerating FMS documents to Austin.

> <u>Billing Document Regeneration \[PRCA FMS BD REGEN\]</u>

> This option regenerates an FMS document rejected in Austin.

> <u>Edit FMS Accounting Elements \[PRCA FMS ACCT EDIT\]</u>

> This option is used to edit the accounting line information on FMS billing documents.

> <u>Modified Billing Document Regeneration \[PRCA FMS MBD REGEN\]</u>

> This option regenerates a modified billing document that rejected in Austin

> <u>National Data Base Document Regeneration \[PRCA FMS NDB REGEN\]</u>

> This option is used to regenerate FMS national data base documents.

> <u>Overpayment (OP) Document Regeneration \[PRCAT FMS OP REGEN\]</u>

> This option will allow a user to retransmit a "rejected" OP document. It will only allow the retransmission of an OP document that has actually been refunded in the AR package and has been rejected by FMS.

> <u>Regenerate FMS Cash Receipt Document \[PRCA FMS CASH RECEIPT\]</u>

> This option is to re-create and re-transmit the Cash Receipt Documents.

> <u>Remove invalid SUB BOC \[PRCA FMS SBOC\]</u>

> This option is used to remove an INVALID SUB BOC from a rejected FMS document.

> <u>Regenerate FMS Cash Receipt Document \[PRCA FMS CASH RECEIPT\]</u>

> This option is to re-create and re-transmit the Cash Receipt Documents.

> <u>Write-Off Document Regeneration \[PRCA FMS WRITE-OFF\]</u>

> This option is used to regenerate a rejected write-off document.

<u>Forward IRS OFFSETs to Austin \[PRCA FORWARD IRS OFFSETS\]</u>

This option forwards IRS Offset data to Austin, where it will be collected for transmission to the IRS.

> <u>Refund Review and Approve \[PRCA REFUND REVIEW\]</u>

> This option will allow a user to select a Prepayment Bill in the Open or Refund Review status, review the Bill and, approve the Bill by entering their Electronic Signature. The refund must be signed by a Certifying Officer, holder of the PRCAY PAYMENT SUP security key. Two signatures are needed in order for it to be processed by the Accounting Tech.

> NOTE: Prepayments under \$1.00 cannot be refunded.

<u>EDI DIAGNOSTIC MEASURES REPORTS \[RCDPE EDI NATIONAL REPORTS\]</u>

This is a menu for AR's EDI Diagnostic Measures National Reports. These reports allow a facility to measure the current usage rates of electronic billing to and electronic payments from third party insurers.

> <u>EX - EDI Diagnostic Measures Extracts Menu \[RCDPE NR EXTRACT MENU\]</u>

> This menu contains options related to the AR National Reports Extraction.

> <u>DE - Disable-Enable DM Background Job/Reports \[RCDPE NR DISABLE/ENABLE\]</u>

> This option allows a user to disable or re-enable the AR National Reports background job. Once a report is disabled, it won't re-queue to run via the AR National Reports process. Note that this locked option is seen by and accessible to only those holding the PRCFA SUPERVISOR security key.

> <u>RN - Manually Start DM Extract \[RCDPE NR MANUAL START\]</u>

> This option allows a user to restart the AR National Reports Extraction background job if the report is not running. Note that this locked option is seen by and accessible to only those holding the PRCFA SUPERVISOR security key.

> <u>TR - Manually Transmit DM Extract \[RCDPE NR MANUAL TRANSMIT\]</u>

> This option allows a user to retransmit an AR National Report file to FORUM for a particular month if that month's report data did not successfully transmit the first time. Note that this locked option is seen by and accessible to only those holding the PRCFA SUPERVISOR security key.

> <u>VP - View/Print Extracted Reports \[RCDPE NR VIEW/PRINT EXTRACTS\]</u>

> This option allows a user to see the results of previous AR National Report extractions. It shows whether or not certain reports made it through the extraction process.

> <u>VS - EDI VOLUME STATISTICS Report \[RCDPE EDI VOLUME STATISTICS\]</u>

> This report compiles and prints out statistical metrics for Medical (837) and Pharmacy (NCPDP) electronic claims, and the payments (835s) received for those claims. This information can either be reviewed locally or sent to the National reporting group.

> <u>TD - EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\]</u>

> This report contains the metrics for the \# of ERAs, \# of EEOBs, and \# of EFTs processed during a given time period. It will also calculate the \# of days between each step in the electronic payments process.

<u>SUPERVISOR'S AR MENU \[PRCAF SUPERVISOR MENU\]</u>

This is the menu for the Accounts Receivable Supervisor.

<u>Edit/Add ‘Bill Resulting From’ List \[PRCAF EDIT BILL FROM\]</u>

Use this option to edit the entries in the "Bill Resulting From" file or entries to the list. The data appears in each debt collection letter.

<u>Delete an Incomplete Transaction \[PRCAF TR DELETE\]</u>

Delete incomplete transactions with this option. Enter the AR Bill number associated with the transaction that is flagged as incomplete.

<u>Administrative Cost Adjustment \[PRCAF ADJ ADMIN\]</u>

Use this option to adjust the administrative costs, IRS cost, DMV cost, etc.

<u>Form Letter Menu (Edit/Print) \[PRCAF U FORM MENU\]</u>

This is a menu of options for editing and printing form letters. The user may edit a letter or print it to check for proper format.

> <u>Edit Form Letters \[PRCAF U FORM ED\]</u>

> The Supervisor can use this option to edit the text of a form letter. Great caution should be taken NOT to alter the contents of the window functions contained in vertical bars -- \| \|. Formatting of the printed letter will be adversely affected.

> <u>Print Form Letter \[PRCAF U PRINT FORM\]</u>

> Use this option to test the printed format of a letter. The user can select any form letter/Bill combination. Data stored for the account will not be affected.

<u>Return Bill to Service \[PRCAF RETURN BILL\]</u>

Use this option to return a Bill needing amendment to the originating Service/Section.

<u>Agency Location Code (Deposits) \[PRCA AGENCY LOCATION\]</u>

This option allows the user to enter the ALC upon package installation or to edit an already existing ALC.

<u>Archive Menu \[PRCAK AR SUPERVISOR\]</u>

This option allows the AR Supervisor access to the Archive menu. The Archive process should be coordinated between IRM and Fiscal. The options available will allow Fiscal service to list all bills that are pending Archive and also removes the Bill from the list before IRM archives the Bill.

> <u>Detailed Report of Pending Archive Records \[PRCAK ARCHIVE MARK PRINT\]</u>

> This option will print a report of all the AR records that are flagged for Archive. (The status is "PENDING ARCHIVE"). This report includes the Bill no., Debtor name and category, the previous status before it was marked for Archive, the balance, and the date of the last activity. A total of entries marked as ARCHIVE will print at the end of the report. This total may be very useful in determining the amount of systems' activity the archive processes will create.

> Unmark Records Marked for Archival \[PRCAK UNMARK ARCHIVE\]

> This option will allow the user to change the status of a record from PENDING ARCHIVE back to the previous status. This will prevent the record from being archived. The user may unmark ALL records or select each record. If the records marked for archiving were moved to the temporary storage file, the status cannot be changed.

<u>Bad Debt Accrual Over-Ride \[RCNR BAD DEBT ACCR. EDIT\]</u>

This menu option will allow the user to over-ride the calculated write-off and contract adjustment totals.

<u>Cross-Servicing Menu \[RCTCSP MENU\]</u>

This menu option will allow the user to access the Cross-Servicing functionality.

<u>Bill Recall/Reactivate TCSP Referral \[RCTCSP RECALLB\]</u>

> This option is used to allow the user to recall a bill from Cross-Servicing. It is also used to delete the recall if the recall has not taken place.

> <u>Cross-Servicing Bill Report \[RCTCSP BILL REPORT\]</u>

> This report lists the bills for the individual debtor who has been forwarded to Cross-Servicing. For each bill, the report displays the status code, the original amount of the bill, the current amount of the bill, the principle, interest, administrative cost, court cost, and the Cross-Servicing referral date.

> <u>Cross-Servicing Re-Referred Bills Report \[RCTCSP REREFER BILL REPORT\]</u>

> This report lists the bills for the individual debtor which have been re-referred to Cross-Servicing.

<u>Cross-Servicing Recall Report \[RCTCSP RECALL REPORT\]</u>

> This report lists the bills that have been recalled from Cross-Servicing. The user has the option to sort by bill number or debtor name.

<u>Cross-Servicing Stop Reactivate Report \[RCTCSP STOP REACTIVATE REPORT\]</u>

The Cross-Servicing Stop Reactivate Report lists the bills that have been

stopped from Cross-Servicing, or Reactivated, or both. The user may select

> a range of Debtors or all Debtors, and a range of dates or all dates. Excel CSV output is also supported.

<u>Debt Referral Reject Report \[RCTCSP REJECT REPORT\]</u>

> This report allows the user to report debt rejected by Cross-Servicing. The report prints out based on the following user defined parameters: Range of Dates (Brief or Detail mode), sorted by Bill Number, Debtor Name or CS Referred Date, for a given Reject Origination Source (or All), and in either Ascending or Descending print order.)

<u>Debtor Recall/Re-activate TCSP Referral \[RCTCSP RECALLD\]</u>

> This option is used to allow the user to recall a debtor from Cross-Servicing. It is also used to delete the recall if the recall has not taken place. Recalls all bills referred to Cross-Servicing at the same time for the selected debtor.

<u>List IAI Error Codes \[RCTCSP IAI ERROR CODES LIST\]</u>

> This option is a listing of the IAI Error Codes, in error code order. The display contains a) Error Code, b) Field Name, c) associated Record Types and d) Description.

<u>Print Cross-Servicing Report \[RCTCSP REPORT\]</u>

> For each bill that has been referred to Cross-Servicing, this report displays the debtor’s name and SSN, the original amount referred, and Cross-Servicing referred date. The user has the option to sort by bill number, debtor’s name, or the Cross-Servicing referred date.

<u>Reconciliation List Manager \[RCTCSP RECONCILIATION WORKLIST\]</u>

> List Manager for VistA AR Cross-servicing reconciliation. This option is used to work debts that are returned from Treasury.

<u>Reconciliation Report \[RCTCSP RECONCIL REPORT\]</u>

> This option is used to print a Reconciliation Report. For each bill which has been returned from Treasury by reconciliation, the report will display the Debtor's name, Bill Number, Returned Date, and Closed Date. A second text line will display the Returned Code Description. If there is a Date of Death, a Date of Bankruptcy, or a Date of Dissolution, then this date will appear on a new line with a text description and the date.

<u>Stop/Re-activate TCSP Referral \[RCTCSP STOP\]</u>

> This option is used to allow the user to stop a Cross-Servicing referral for a bill or debtor. It is also used to re-activate the Cross-Servicing referral for a bill or debtor that had been previously stopped.

<u>TCSP Flag Control \[RCDP TCSP FLAG CONTROL\]</u>

> The options included in this menu are used to correct the bill or debtor data attributes (or flags) as needed because of a variance in the bill or debtor data between the VistA system and the Treasury system. Note that this option is only seen by and accessible to those users assigned the RCDP TCSP FLAG security key which should ONLY be allocated by CPAC IT and given ONLY to Veteran Services Supervisors and/or Veteran Services Leads (One, Two or Three).

This option will allow TCSP flag control to the following options:

> 1\) Set cross-service flag on BILL

> 2\) Clear cross-service flag on BILL

> 3\) Clear cross-service flag on DEBTOR (AND ALL BILLS)

> 4\) Set cross-service flag on DEBTOR

> 5\) Fully re-establish debtor/bill as cross-serviced

<u>National Roll-up Report \[RCNR NATIONAL ROLLUP REPORT\]</u>

This report prints out information contained on the national roll-up. It allows selection of a range of dates and for a set of criteria by the user. It also gives the option of printing a 'detailed' report. A 'detailed' report will list all bills and transactions for each criteria selected with the corresponding amounts.

<u>Purge Unprocessed FMS Document File \[PRCAF PURGE UNPROC\]</u>

This option is used to purge the AR/FMS document file (347). This option will purge all entries older than the date entered by the user. This option should be used with care.

<u>Site Parameter Edit \[PRCA SITE PARAMETER\]</u>

This option will allow the AR Supervisor to edit the site parameters for the AR Package. The site parameters allow the system to tailor itself for specific site needs, such as number of days to purge Agent Cashier Receipts, when to generate IRS Offset Letters, etc.

> <u>Deactivate Group \[PRCA DEACTIVATE GROUP\]</u>

> Allows the user to deactivate the currently active “group”.

<u>Group Parameters \[PRCA BIL AGENCY\]</u>

User can add/edit the billing agency address with this option.

<u>Interest/Admin/Penalty Rates \[PRCAF U ADMIN.RATE\]</u>

This option adds/edits the administrative costs and interest rates charged on delinquent accounts. Note that this locked option is seen by and accessible to only those holding the PRCAF LATE CHARGES security key.

<u>IRS Parameters \[PRCA IRS PARAMETERS\]</u>

This option will allow the user to modify the site parameters to control IRS Offset functionality.

<u>Statement Parameters \[PRCA NOTIFICATION PARAMETERS\]</u>

This option will allow the AR Supervisor to edit parameters specific to the Patient Statements. This will allow the user to control functionality related to statements.

<u>AGENT CASHIER \[PRCAY MASTER\]</u>

This is the top-level menu for payment processing.

<u>Agent Cashier \[PRCAY MASTER\]</u>

This option is the top-level menu for Payment processing.

> <u>Cash Payment \[PRCAY CASH PAYMENT Synonym: CS\]</u>

> This option is used to enter a cash payment for both mail-in and window payments. This option batches payments to be posted to the accounts at a later time.

> <u>Check/MO Payment \[PRCAY CHECK/MO PAYMENT Synonym: CM\]</u>

> This option is used to enter mail-in and window check and money order payments. This option batches payments to be posted to the accounts at a later time.

> <u>Credit Card Payment \[PRCAY CREDIT CARD PAYMENT Synonym: CC\]</u>

> This option is used for mail -in and window credit card payments. This option batches payments that will be posted to the accounts at a later time.

> <u>Other Payment \[PRCAY OTHER PAYMENT Synonym: OP\]</u>

> This option allows the user to enter payment for TDA type payments. This option is very similar to the cash payment option but allows a different receipt to be open and used for TDA payments.

> <u>Cancel a Payment Transaction \[PRCAY CANCEL PAYMENT Synonym: CP\]</u>

> This option will allow the Agent Cashier to cancel a payment transaction and re-enter the payment as a new transaction.

> <u>Move A Payment Transaction \[PRCAY MOVE A PAYMENT Synonym: MV\]</u>

> This option will allow the agent cashier to copy a payment transaction from one receipt to another, provided that the receipt being copied from is cash and the receipt or payment has not already been processed.

<u>Patient Payment/Refund Transaction History Inquiry</u>

<u>\[PRCA PAYMENT TRANS HISTORY Synonym:</u> <u>PD\]</u>

This report lists a history of payment/refund transactions for a patient for a specified date range.

<u>Brief Account Profile \[PRCAY ACCOUNT PROFILE Synonym: BR\]</u>

This option will display an Account Profile for Patient, Vendors, Insurance Companies, etc.

<u>Deposit Management \[PRCA DEPOSIT MANAGEMENT\]</u>

This submenu allows the user access to the Deposit options.

> <u>Create Deposit Ticket \[PRCA CREATE DEPOSIT\]</u>

> This option enables the user to create a new Deposit Ticket.

> <u>Deposit Money to Bank \[PRCA DEPOSIT MONEY\]</u>

> This option allows the user to approve a ticket for deposit to a bank. If a deposit ticket has no receipt associated with it, the user will be asked to provide necessary information before the ticket can be approved.

> <u>Edit a Deposit Ticket \[PRCA EDIT A DEPOSIT\]</u>

> This option allows the user to change information on a deposit ticket.

> <u>Receipt List for Deposit \[PRCA RECEIPT LIST\]</u>

> This option shows information associated with receipts that are attached to selected deposit tickets.

> <u>Summary Listing of Deposits \[PRCA SUMMARY DEPOSIT\]</u>

> By choosing this option, the user is able to view information about past and current deposit tickets.

> <u>View a Deposit \[PRCA VIEW A DEPOSIT\]</u>

> By using this option, the user can view detailed information about a specific deposit ticket.

> <u>Void a Deposit \[PRCAY VOID DEPOSIT\]</u>

> This option allows the user to void a Deposit Ticket. The ticket must first be “emptied” of all receipts.

<u>Full Account Profile \[PRCAY FULL ACCOUNT PROFILE Synonym: FU\]</u>

This option will display a full account profile of all bills for a debtor regardless of the status of the Bill.

<u>Print 215 Report \[PRCAY PRINT 215 Synonym: P2\]</u>

This option will print a 215 report, sorted by appropriation number for a given receipt number entered by the user. It will also show errors of payment (a payment entered without an appropriation) and posting errors.

<u>Profile of Accounts Receivable \[PRCAC PROFILE\]</u>

This option displays all the AR data the user needs. He may see the data on his terminal screen or print the profile on a designated printer. The profile is classified by category: patient, vendor, or 3rd party.

<u>Release Holds on AR \[PRCAY RELEASE HOLDS Synonym: RH\]</u>

This option allows the agent cashier to release "holds" on Means Test bills. There may be some requirements for the VA to "hold-off" billing the patient until payment is received from the insurance company. When a payment is received from an insurance company, any "holds" on bills to be sent to the patient need to be removed and the patient should be billed. This option allows the user to forward the bills from MCCR to AR to start the collection process.

<u>Receipt Management \[PRCAY RECEIPT MANAGEMENT</u> Synonym: RM\]

This menu will allow the user to manage receipts. This includes posting, approving, reviewing, etc. type options for receipts.

> <u>Approve a Receipt \[PRCAY APPROVE BATCH\]</u>

> This option will mark a batch as approved and ready for posting to the A/R Transaction File.

> <u>Edit A Receipt \[PRCAY EDIT A RECEIPT\]</u>

> This option allows the user to edit a receipt.

> <u>List of Receipts \[PRCAY LIST RECEIPTS\]</u>

> This option will print a report of all receipts recorded with un-archived payments. The report is sorted by date and shows the receipt number, date posted, amount of payment, the bill that reflects the payment, and the user who posted the payment.

> <u>Post an Approved Receipt to Accounts \[PRCAY POST TRANS\]</u>

> This option will post the transactions in an approved batch to the A/R Transaction File. Users can only post a batch which they approved, unless they hold the supervisor’s key.

> <u>Receipt Number Reconciliation Report \[PRCAD RECON CASH RECEIPT\]</u>

> This will print the Agent Cashier Reconciliation Report sorted by the Receipt Number.

> <u>Reprint a Customer's Receipt \[PRCAY REPRINT A RECEIPT\]</u>

> This option will allow an Agent Cashier to reprint a receipt for a payment transaction. If a payment was canceled, the amount printed on the receipt will be zero.

> <u>Summary of Current Receipts \[PRCAY SUMMARY OF CURRENT\]</u>

> This option will list a summary of current receipts in the system. This report will show who opened a receipt batch, when the batch was opened, number of transactions in the batch, and who approved the batch for posting to patient accounts.

> <u>Void A Receipt \[PRCAY VOID A RECEIPT\]</u>

> This option will allow a receipt that was entered in error and has not had any payment transactions entered to be voided. The receipt will be purged with the other receipts.

<u>Transaction Profile \[PRCAC TRANS PROFILE</u> Synonym: TP\]

Use this option to see a profile of a single transaction. More complete information on an account is available with the PRCAC PROFILE option.

## EDI Lockbox \[RCDPE EDI LOCKBOX MENU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the EDI Lockbox Menu for the ePayments clerk.

<u>EXC - EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTIONS PROCESSING\]</u>

> This option provides a list of ERA/EOB records that are currently marked with an exception condition. The option allows you to list either the ERA messages that are unfiled in VistA (transmission exceptions) or those that were filed but have data exceptions. The records can then be viewed, and various options are provided to reconcile the exceptions.

<u>WL – EEOB Worklist \[RCDPE EDI LOCKBOX WORKLIST\]</u>

> This option provides a list of electronic EOB detail records that were included on a selected electronic remittance advice (ERA). It allows for the creation of a receipt that will post the detail contained in each EOB against the site's A/R and to FMS. To accomplish this, some manipulation of the payment data may be necessary and some of the tools for performing this manipulation are included in this function.

<u>APAR - Auto-Post Awaiting Resolution \[RCDPE APAR\]</u>

> The Auto-Post Awaiting Resolution (APAR) option displays and allows selection and editing of ERA-EEOB line items that did not pass the auto-posting validation. This means that these line items do not have a receipt and will have to be manually worked by the Accounts Receivable clerk. Once the clerk has made the necessary adjustments to each of the EEOB line items, the line items must be 'Marked for Auto-Post' in order for the EEOBs to be processed by the Nightly Auto-Posting job.

<u>MA – Automatic Match EFTs to ERAs \[RCDPE MATCH EFT TO ERA\]</u>

> This option will start the job to match the 3rd Party Lockbox EFT records that have not yet been matched to the electronic ERAs currently on file. This option runs a part of the normal nightly processing, but can be run on demand here

<u>MCR – EEOB Move/Copy/Remove \[RCDPE EEOB MOVE/COPY/REMOVE\]</u>

> This option allows an EEOB incorrectly matched to a claim to be moved to the correct claim or claims. In addition, this option allows those with the appropriate security key to remove an EEOB from a claim. This is to be used when the EEOB was matched to an incorrect claim and the EEOB does not belong to this facility. That is, the matching claim does not exist in this system of records.

<u>MM – Manual Match EFT-ERA \[RCDPE MANUAL MATCH EFT-ERA\]</u>

> This option will allow the user to choose an EFT detail record and an ERA record and will mark the 2 records as matched. This should be used only if the automatic matching function is not able to make the match. The EFT and ERA selected must both be unmatched, and the ERA must not be associated with a receipt.

MO – Move ERA Total to Suspense \[RCDPE MOVE ERA TO SUSPENSE\]

> This option will allow the user to choose an ERA record that is matched to an EFT deposit and will create a receipt to post the total amount reported as being paid on the EFT to SUSPENSE.

<u>OEFT - Unposted EFT Override \[RCDPE UNPOSTED EFT OVERRIDE\]</u>

> Provides the capability for users assigned to the RCDPE AGED PMT security key unrestricted ERA Worklist scratchpad creation for one day.

<u>REFT – Remove Duplicate EFT Deposits \[RCDPE REMOVE DUP DEPOSITS\]</u>

> Allows authorized users to mark and EFT as a duplicate. Requires that the user have the RCDPE REMOVE DUPLICATES security key.

<u>REM - Remove ERA from Active Worklist \[RCDPE REMOVE ERA FROM WORKLIST\]</u>

> This option allows you to remove an ERA from the active worklist. You may only select an ERA that is unmatched to paper and that is UNPOSTED.

<u>REP - EDI Lockbox Reports Menu \[RCDPE EDI LOCKBOX REPORTS MENU\]  
</u>This submenu allows the user access to the EDI Lockbox Report sub options.

> <u>WORK – Workload Reports \[RCPDE EDI LOCKBOX WORKLD RPRTS\]</u>

> This menu holds the Accounts Receivable/ePayments Workload reports.

> <u>DA – Daily Activity Report \[RCDP EDI LOCKBOX ACT REPORT\]</u>

> This option produces the EDI Lockbox Daily Activity Report.

> <u>EFT – EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]</u>

> This option produces the EFT aging report.

> <u>ERA – ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]</u>

> This option produces the ERA aging report.

> <u>PEO – Pending EFT Override Report \[RCDPE EFT OVERRIDE REPORT\]</u>

> This option produces the ERA aging report.

> <u>UN – Unapplied EFT Deposit Report \[RCDPE UNAPPLIED EFT DEP REPORT\]</u>

> This option produces a list of EFT deposits that have EFT detail records whose funds have not been applied to bills in A/R. These funds remain in FUND 5287, REVENUE SOURCE CODE 8NZZ.

> <u>ADJR - Adjustment Code Reports \[RCPDE EDI LOCKBOX ADJCDE RPRTS\]</u>

> This menu holds the Accounts Receivable/ePayments Workload reports

> <u>CR - 835 CARC Data Report \[RCDPE CARC CODE PAYER REPORT\]</u>

> This option will allow a user to see the full information on CARC or RARC data stored

> in the AR EDI CARC DATA and AR EDI DATA files.

> <u>PLB - Provider Level Adjustments Report \[RCDPE PROVIDER LVL ADJ REPORT\]</u>

> This report will display ERA data with PLB (Provider Level Benefits) data details. This

> is an ad- hoc report to allow the user to extract report data as well as view and manage refund requests for all PLB adjustment codes.

> <u>QS - CARC/RARC Quick Search \[RCDPE CARC/RARC QUICK SEARCH\]</u>

> This is option is a quick lookup of a CARC or RARC data. This is to be used by the user to get a full description of a single or limited set of codes.

> <u>TB - CARC/RARC Table Data Report \[RCDPE CARC/RARC TABLE REPORT\]</u>

> This report will allow a user to see the full information on CARC or RARC data stored in the AR EDI CARC DATA and AR EDI RARC DATA files

> <u>RESR – Additional Research Reports \[RCPDE EDI LOCKBOX ARSRCH RPRTS\]</u>

> This menu holds the Accounts Receivable/ePayments Workload reports

> <u>ETR – EFT/ERA TRENDING Report \[RCDPE ACTIVE WITH EEOB REPORT\]</u>

> This option produces the ACTIVE BILLS WITH EEOBs report.

> <u>AB – Active Bills with EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]</u>

> This option produces the ACTIVE BILLS WITH EEOBs report.

> <u>AUDR – Audit Reports \[RCPDE EDI LOCKBOX AUDIT RPRTS\]</u>

> This menu holds the Accounts Receivable/ePayments Workload reports

> <u>AD - Auto-Decrease Adjustment report \[RCDPE AUTO-DECREASE REPORT\]</u>

> This report lists ERA claims with residual balances for which decrease adjustments have been automatically applied by the nightly process. The report can be filtered by Station/Division and by date range.

> <u>AP - Auto-Post Report \[RCDPE AUTO-POST REPORT\]</u>

> This report lists ERAs that have been autoposted by the nightly process. The report can be filtered by Station/Division and by date range.

> <u>APR - Auto-Posted Receipt Report \[RCDPE AUTO-POST RECEIPT REPORT\]</u>

> The Auto-Posted Receipt Report (APR) option displays receipt details associated with auto-posted ERA/EFT, including totals.

> <u>APH – Auto Parameter History Report \[RCDPE AUTO PARAM HIST REPORT\]</u>

> This report lists the changes in auto parameters in the EDI Site Parameters.

> <u>DUPR –- Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]</u>

> This report lists EFTs which have been marked as duplicates.

> <u>ESC - ERA Status Change Audit Report \[RCDPE ERA STATUS CHNG AUD REP\]</u>

> This report is used to track the changes to the Auto Posting Status of a single ERA or multiple ERAs by date range

> <u>ETA - EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\]</u>

> This report will list all actions that have been performed on a single EFT. The intent of the report is to follow the EFT from cradle to grave.

> <u>MCR – EEOB Move/Copy Audit Report \[RCDPE EEOB MOVE/COPY REPORT\]</u> This report lists EOBs that have been moved or copied to new claim numbers or have been removed from a claim. The report can be filtered by Station/Division and by date range.

> <u>EMA – EEOBs Marked for Auto-Post Audit Report \[RCDPE MARKED AUTO-POST REPORT\]</u>

> This report lists EOBs that have been moved or copied to new claim numbers or have been removed from a claim. The report can be filtered by Station/Division and by date range.

> <u>POSR – ERA’s Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB REPORT\]</u>

> This report lists ERAs that have been marked as posted with paper EOB.

> <u>PX – Payer Implementation Report \[RCDPE PAYER EXCLUSION NAME\]</u>

> Launches a report to show the payers, with columns for payer name, payer TIN, and the date on which the payer was added to the database.

> <u>REMR - Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA AUDIT\]</u>

> This report lists ERAs that have been removed from the active worklist.

> <u>VP – View/Print ERA \[RCDPE VIEW/PRINT ERA\]</u>

> This option allows you to select an ERA and print or view its contents.

<u>UN – Unmatch An ERA \[RCDPE UNMATCH ERA\]</u>

This option allows you to remove the match status from an ERA if it was added in error.

<u>REM - Remove ERA from Active Worklist \[RCDPE REMOVE ERA FROM WORKLIST\]</u>

This option allows you to remove an ERA from the active worklist. You may only select an ERA that is unmatched to paper and that is UNPOSTED.

<u>UP – Update ERA Posted Using Paper EOB \[RCDPE ERA POSTED BY PAPER EOB\]</u>

This option is used to mark an ERA as posted when the paper EOB containing this ERA data was posted to your A/R and FMS and no reference to the ERA was included.

<u>ZB – Mark 0-Balance ET Matched \[RCDPE MARK 0-BAL EFT MATCHED\]</u>

This option allows the user to select an EFT detail record that has a 0-balance payment and mark it as matched to a paper EOB. This will remove it from the EFT UNMATCHED AGING REPORT.

<u>IDP – Identify Payers \[RCDPE PAYER IDENTIFY\]</u>

This option displays a list of payers from the PAYER EXCLUSION FILE (#344.6) and allows the user with the appropriate security access to flag entries as Pharmacy and/or Tricare. Entries can be either, neither or both. This option allows the user to filter the list by date added. This is important as entries are added to the file automatically by the nightly process. A user needs to be able see what entries were added recently and if they need to be flagged.

UNASSIGNED OPTIONS

<u>\[PRCA NIGHTLY PROCESS\]</u>

Use this option nightly to perform the following tasks.

1)  Update of open status bills to active
2)  Update of interest/admin charges on patients' accounts
3)  Update statement days
4)  Print of Patient Statements, Uniform Billing forms, and non-patient follow-up letters
5)  Purge of Receipts
6)  Creation of Cross-Servicing (Treasury Cross-Servicing Project) documents
7)  Creation of IRS Master Code Sheets
8)  Creation of IRS Update Code Sheets
9)  Print of IRS Offset letters
10) Print of the Follow-up list
11) Purge AR Events
12) Flag prepayments for refund review
13) Print Comment List
14) Match EDI transactions (ERA to EFT)
15) Report Overdue EDI transactions
16) Report copied EOB transaction in prior 24 hours

Process will first check and validate AR pointer files 341.1, 430.2, and 430.3. Process will terminate and send bulletin if files are not valid.

> **NOTE:** To ensure that Pandemic period copays are properly cancelled and don't appear on patient statements, as required by the American Rescue Plan Act (ARPA) of 2021, the PRCA NIGHTLY PROCESS VistA TaskMan job will need to follow the scheduling criteria below:

- Starts after midnight local time.
- Starts at least 30 minutes after the start of the IB MT NIGHT COMP nightly process.

You may need to reschedule the IB MT NIGHT COMP TaskMan job as well to ensure that it starts at least 30 minutes before the start of the PRCA NIGHTLY PROCESS TaskMan job.

<u>\[RCDPE EDI LOCKBOX SERVER\]</u>

This mail server option processes incoming mail messages containing payment and remittance information. The format of the messages is X12 835.

<u>\[RCDPE MOVE ERA TO SUSPENSE\]</u>

This option will allow the user to choose an ERA record that is matched to an EFT deposit and will create a receipt to post the total amount reported as being paid on the EFT to SUSPENSE.

<u>\[RCDPE WORKLOAD NOTIFICATION\]</u>

Use this scheduled option to scan for and generate bulletins for overdue EDI transactions. The option should be scheduled to run weekly, bi-weekly, or monthly as required by the site.

OTHER OPTIONS (NOT ASSIGNED TO USER MENUS)

PRCA FMS-CONV MENU

This menu contains options to reconcile bills with FMS after the CALM conversion.

> <u>PRCA FMS CAF LIST</u>

> During the conversion process, FMS sends a file to be processed by the IFCAP server. If the server fails to start, this option can be used to manually start the process. This option will also take FMS bill data from the Conversion AR Fields (CAF) file and place them in their corresponding AR file entries. Afterwards, a list will be transmitted to the G.FMS mail group showing FMS bills entered into the AR file and FMS bills that are not in the AR file, if any.

> <u>PRCA FMS-CONV DECREASE ADJ</u>

> This option will be used to decrease bills to bring the amounts in line with FMS after the CALM conversion. The resulting decrease transaction will not be sent to FMS.

> <u>PRCA FMS-CONV ACCOUNTING</u>

> This option is used to enter FMS accounting elements on converted records

> <u>PRCA FMS-CONV INCREASE ADJ</u>

> This option will be used to increase bills to bring the amounts in line with FMS after the CALM conversion. The resulting increase transaction will not be sent to FMS.

> <u>PRCA FMS-CONV SETUP BILL</u>

> This option will be used to enter bills that have been transmitted to FMS during the calm conversion and are not present on the local system. These bills are not re-sent to FMS.

<u>PRCAK ARCHIVE</u>

This menu contains Accounts Receivable archival options. These options should be executed in the order described in the AR Archival documentation. Because some options may cause a lot of system activity, you should coordinate the use of these options with your IRM System Manager.

> <u>PRCAK BUILD TEMP</u>

> This option will move all of the data items including the transactions for bills in the PENDING ARCHIVE status to a temporary storage file. You cannot unmark records marked for archiving once this process is started. A mail message will be sent to you when the file has successfully been populated.

> WARNING: This process may be very system intensive! Please coordinate the use of this option with your IRM System Manager. Be sure you have adequate disk and journal space available.

> <u>PRCAK MARK FOR ARCHIVE</u>

> This option will change the bill status of bills whose last date of activity falls within the selected timeframe to PENDING ARCHIVE. The previous fiscal year and current fiscal year cannot be archived. A mailman bulletin will be sent containing the total number of records marked for archival. This total should be reviewed by the IRM system manager for AR Archival system activity.

> <u>PRCAK PURGE TEMP</u>

> This option will purge ALL of the archive data items in the temporary storage archive file (AR ARCHIVE File 430.8). If there are records remaining in the Pending Archive status you will have to build this file again.

> \*\* THIS OPTION DOES NOT RESET THE RECORDS TO THE ARCHIVED STATUS \*\*

> <u>PRCAK REMOVE AR RECORD</u>

> This option will remove the AR record data from the Account Receivable File 430 and all corresponding transactions from the AR Transactions File 433. This option will change the status of the AR record in the 'Pending Archive' status to 'Archived'. The date entered by the user will be entered in the Date Bill Prepared field. The entry in the temporary storage file will be deleted after the AR records are updated.

> NOTE: The use of this option should be coordinated with IRM and MCCR.

<u>PRCA MDA SERVER</u>

This option is the server for receiving Medicare Deductible Alerts for automatic processing in AR.

# Accounts Receivable Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>340^B</u>

This is the regular VA FileMan "B" cross-reference and is used throughout the AR package for users to look-up information by debtor.

<u>^^TRIGGER^340^.03</u>

Since a patient statement day never changes, a statement day is assigned to a patient based on their internal entry number. When a new patient is added to the debtor file, this cross-reference triggers the assignment of the statement day.

<u>340^AB^MUMPS</u>

This cross-reference allows rapid lookup of debtors in the debtor file by the "type" of debtor. There are five types of debtors (Patient, Insurance Company, Institution, Vendor, and Person). This allows the AR software to scan the file for only a specific type of debtor rather than having to look at each entry.

<u>340^AC</u>

This cross-reference is used to print patient statements and Vendor, Person, and Institution follow-up letters. Since these types of debtors get notified based on their statement day, this cross-reference allows rapid look-up of which debtor is due a notification on a particular day.

<u>340^DMC</u>

This cross-reference will be sent if follow-up on an account is being done by the Debt Management Center (DMC).

<u>340^TCSP^MUMPS</u>

This cross-reference indicates whether a debtor has been sent to Cross-Servicing.

<u>340^TOP^MUMPS</u>

This Cross-Reference indicates whether a debtor has been sent to TOP and the date of the reference.

<u>340.5^B</u>

This cross-reference will allow a repayment plan look-up by Repayment Plan ID.

<u>340.5^C</u>

This cross-reference will allow a repayment plan look-up by Term Limit Exceeded Date. Used by the Repayment Plan Term Limit Exceeded Report \[PRCAC TERM LENGTH REPORT\].

<u>340.5^E</u>

This cross-reference will allow a repayment plan look-up by Debtor (file \#340).

<u>340.5^PRTDEF</u>

This cross-reference will allow a repayment plan look-up by the PRINT DEFAULT? Flag (#1.02). Used by the Print Default Report.

<u>340.5^PRTDEL</u>

This cross-reference will allow a repayment plan look-up by the PRINT DELINQUENT? Flag (#1.02). Used by the Print Delinquent Report.

<u>341^B</u>

This cross-reference will allow look-up to the event file by identifier.

<u>341^AD2^MUMPS</u>

This cross-reference is used for account profiles and for printing patient statements, letters, and bills. It stores the debtor, event-type, and date/time event was closed in reverse order.

<u>341^AC1^MUMPS</u>

This cross reference is used to store events that are in an open status. Since only one event at a time should be in an open status for a debtor, this cross reference makes sure that no two events are in an open status for a debtor.

<u>341^AD1^MUMPS</u>

This-cross reference is used for account profiles and for printing patient statements, letters, and bills. It stores the debtor, event-type, and date/time event was closed in reverse order.

<u>341^AD3^MUMPS</u>

This cross-reference is used for account profiles and for printing patient statements, letters, and bills. It stores the debtor, event-type, and date/time event was closed in reverse order.

<u>341^C</u>

This cross-reference sorts events by the date/time they are closed and allows a chronological ordering of events.

<u>341^AC2^MUMPS</u>

This cross reference is used to store events that are in an open status. Since only one event at a time should be in an open status for a debtor, this cross reference makes sure that no two events are in an open status for a debtor.

<u>341^AE</u>

This cross reference is used to sort and print events by their follow-up dates.

<u>341.1^B</u>

This cross reference is not used in the AR package, but exists for FileMan look-up on this file by the AR event type name.

<u>341.1^AC</u>

Since the AR event type file is a table file, AR event types are found by their associated event number using this cross reference.

<u>342^B</u>

This cross reference is to allow look-up on the site parameter file by the site name.

> <u>342.04^B</u>

> No Description

> <u>342.04^AC^MUMPS</u>

> This cross-reference is used to find the most recent interest, administration, and penalty rate to apply to a bill.

> <u>342.01^B</u>

> No Description

<u>^^TRIGGER^342^31</u>

No Description

<u>342.1^B</u>

An AR group is defined by the site and is assigned a "type" of group. This allows the site to look-up the AR GROUP by the name that was assigned to the AR GROUP type.

<u>342.1^AC</u>

The AR package uses this cross reference to find and return information on specific AR groups by type.

<u>342.2^B</u>

No Description.

<u>342.3^B</u>

No Description.

<u>342.31^B</u>

No Description.

<u>343^B</u>

This cross reference is used to look-up follow-up letters by name for users and also when printing follow- up letters for patient statements and bills.

<u>344^B</u>

This cross-reference is used for sorting and file look-up by receipt \#.

<u>^^TRIGGER^344.4^.08</u>

No Description.

<u>344^AA1^MUMPS</u>

This cross-reference stores the last receipt number used by a user specific to type of payment. This cross- reference is used to show the default Receipt \# when using the payment options in the Agent Cashier module.

<u>344^AA^MUMPS</u>

This cross-reference stores the last receipt number used by a user specific to type of payment. This cross- reference supports the cross-reference in field "OPENED BY".

<u>344^AD</u>

No Description.

<u>344^ASTAT</u>

No Description.

<u>344^AEFT</u>

No Description.

<u>344.01^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>344^AN01^MUMPS</u>

This cross reference is used to build the list of payments that are unlinked. An unlinked payment does not have an entry in field .03. The cross reference for field .03 will remove the cross reference when the field is populated. EDI Lockbox deposit receipts will not have an entry in the .03 field but are excluded from this xref since the funds are not deposited into suspense but are instead placed in FUND 5287/revenue source code 8NZZ.

<u>344^AC^MUMPS</u>

This cross-reference is needed to display payments not yet posted to patient accounts during the use of the "Account Profile" option.

<u>344^AACCT</u>

This cross reference is used to lookup payments by account. This is especially useful when determining the pending payments for an account.

<u>344^AN03^MUMPS</u>

This cross reference is used to build the list of payments that are unlinked. An unlinked payment does not have an entry in field .03. This cross reference is initially set when the .01 entry is added to the file.

<u>:^^TRIGGER^344.01^.03</u>

This field allows a customized look-up to the Patient file and Bill number file when prompting the user for "PATIENT NAME OR BILL NUMBER" during payment entry. Once the user selects the Patient or Bill Number, this data is then moved to the "Account" field for VA FileMan Compatibility for printing.

<u>344^ADOC</u>

This cross reference is used to lookup up the receipt number if the cash receipt document is known.

<u>344.1^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>344.1^AC</u>

This cross-reference is needed to display payments not yet to patient accounts during the use of the "Account Profile" option.

<u>344.1^ADOC</u>

This cross reference is used for the Deposit Reconciliation Report.

<u>344.2^B</u>

No Description.

> <u>344.21^B</u>

> No Description.

<u>344.3^B</u>

No Description.

<u>344.3^ALOCK^MUMPS</u>

This xref is set to allow a lock to be placed on the file so only one job that tries to match EFTs to ERAs is run at a time. This xref is set the first time an entry is added to the file.

<u>344.3^ARDEP</u>

No Description.

<u>344.3^C</u>

No Description.

<u>344.3^AD^MUMPS</u>

Xref by deposit number at the top level and payer ID at the 344.31 level.

<u>344.3^ARECDT</u>

No Description.

<u>344.31^B</u>

No Description.

<u>344.31^C</u>

This xref is used for payer names of up to 60 characters.

<u>344.31^AMATCH</u>

No Description.

<u>^^TRIGGER^344.3^.14</u>

No Description.

<u>^^TRIGGER^344.314^.02</u>

Updates to the MATCH STATUS (#.08) field will trigger updates to the MATCH STATUS HISTORY (#314.314) sub-file.

<u>344.31^AERA</u>

No Description.

<u>344.31^E</u>

This cross reference is used to sort the file by the DATE/TIME RETURNED field (#.18).

> 314.314^B

> Standard x-ref used for look-up and sorting by VA FileMan.

> ^^TRIGGER^344.314^.03

> This trigger will update the EDIT USER (#.03) field with the user who has updated the MATCH STATUS field.

<u>344.4^B</u>

No Description.

<u>^^TRIGGER^344.4^.14</u>

No Description.

<u>344.4^C</u>

No Description.

<u>344.4^I</u>

Standard x-ref on the INSURANCE CO ID (#.03) field used for look-up and sorting by VA FileMan.

<u>344.4^AFD</u>

Created to find entries to include on ERA work list pick list.

<u>344.4^AREC</u>

No Description.

<u>^^TRIGGER^344.49^.02</u>

No Description.

<u>344.4^AMATCH</u>

This xref allows easy access to unmatched or mismatched ERA records.

<u>344.4^ATRID</u>

This cross-reference is a newstyle xref. The values in the TRACE NUMBER (#.02) and INSURANCE CO ID (#.03) fields remain unchanged.

<u>344.4^ATRIDUP</u>

This cross-reference is used for claim matching without regard to case. The trace number and insurance company are converted to uppercase and the software uses this for matching claims by the trace number. The values in the TRACE NUMBER (#.02) and INSURANCE CO ID (#.03) fields remain unchanged.

<u>344.4^E</u>

The "E" cross reference is used to sort the file by DATE RETURNED.

<u>344.41^B</u>

No Description.

<u>^^TRIGGER^344.4^.11</u>

Keeps track of the number of individual EOBs in the EOB transmission.

<u>344.41^AC</u>

Cross references entire file by EOB detail pointer to file 361.1

<u>344.4^ADET</u>

Cross references entire file by EOB detail pointer to file 361.1

<u>344.41^AD</u>

No Description.

<u>^^TRIGGER^344.41^.17</u>

No Description.

<u>344.4^AEXC</u>

This xref is used to identify EOB records with exception conditions.

<u>344.4^ATOUT</u>

This cross reference allows easy access to EOBs that have been transferred out of the site to another site.

<u>344.41^ATB</u>

This xref is used to easily find reversal or take back EOBs in an ERA.

<u>344.4^AFL</u>

Created to find entries to include on ERA posted to Paper EOB report.

<u>344.49^B</u>

No Description.

<u>344.491^B</u>

No Description.

<u>344.491^ASEQ^MUMPS</u>

No Description.

<u>:^^TRIGGER^344.491^.03</u>

No Description.

344.491^ANV

No Description.

<u>344.491^ABAT</u>

No Description.

<u>344.4911^B</u>

No Description.

<u>344.4914^B</u>

No Description.

<u>344.491^AC</u>

This xref allows a quick lookup of one user's comments for the EEOB.

<u>344.492^B</u>

No Description.

<u>344.493^B</u>

No Description.

<u>344.493^C</u>

No Description.

<u>344.49^AINUSE</u>

This xref allows for a quick check to see if any batches within the ERA are in use or not.

<u>344.5^B</u>

No Description.

<u>344.5^AMSEQ</u>

This cross reference is needed to associate all 'pieces' of an ERA

<u>344.5^AEXC</u>

This is a cross reference by records with an exception condition.

<u>344.5^ATIN</u>

This is cross reference by File Date and Transferred From fields for ‘835XFR’ messages.

<u>344.53^B</u>

No Description.

<u>344.54^B</u>

No Description.

<u>344.6^B</u>

By Payer Name

<u>344.6^C</u>

By Payer ID

<u>344.6^CPID</u>

By Payer name and Payer ID

<u>344.6^EXRXPOST</u>

This x-ref is used to locate entries by Pharmacy auto-posting status.

<u>344.611^ADU</u>

This new style cross-reference by DATE and USER is used to sort the Auto Parameter History Report.

<u>344.62^B</u>

Standard x-ref used for look-up and sorting on the CARC/RARC CODE (#.01) field.

<u>344.62^ACTV</u>

Index will be used to obtain a list of the active CARC codes for automatic decrease to be applied

<u>344.71^B</u>

Standard x-ref used for look-up and sorting on the TIMESTAMP (#.01) field.

<u>344.71^C</u>

This is a search index to allow users to perform a lookup by the user(s) who place ERA line item in suspense or update any items that were in suspense.

<u>344.71^D</u>

This index allows a user to look at those entries in the Suspense audit log that have been cleared from suspense by attaching the line item (EOB) to a specific bill.

<u>344.71^E</u>

This index allows a user to research Suspense Audit Log entries by a Claim or Bill number if the line item in suspense (EOB) was linked to a Bill or Claim and cleared from suspense.

<u>344.71^F</u>

This index allows the user to search the Suspense Audit Log for all entries of a specific disposition type.

<u>344.72^B</u>

Standard x-ref used for look-up and sorting on the TIMESTAMP (#.01) field.

<u>344.72^F</u>

This index will allow for the lookup of the audit history of a specific ERA.

<u>344.9^B</u>

Standard x-ref used for look-up and sorting on the NAME (#.01) field.

<u>344.91^B</u>

Standard x-ref used for look-up and sorting on the NAME (#.01) field.

<u>344.91^C</u>

This index will allow for lookups of historical reports by date.

<u>345^B</u>

Standard x-ref used for look-up and sorting by VA FileMan.

<u>345.1^B</u>

Standard x-ref used for look-up and sorting by VA FileMan.

<u>346^B</u>

Standard x-ref used for look-up and sorting by VA FileMan.

<u>347^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>347^AD</u>

<u>347^D</u>

<u>347^C</u>

<u>347^FMS</u>

This is a cross-reference on the FMS TRANSMISSION DATE field. That field stores the date that the document was transmitted to FMS.

<u>347.1^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>347.2^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>347.3^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>347.3^C</u>

No Description.

<u>347.4^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>347.4^ACR</u>

This x-ref is used to look-up CR documents

<u>347.4^AWR</u>

This x-ref is used to look-up WR documents

<u>348^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>348^C^MUMPS</u>

This cross-reference stores the print name of the entry along with the code.

<u>348.1^B</u>

This x-ref is used for look-up and sorting by VA FileMan.

<u>348.2^B</u>

No Description.

<u>348.4^B</u>

No Description.

<u>348.4^C</u>

This cross-reference is used to look up a batch by the batch date.

<u>348.4^AC</u>

This cross-reference tells the status of the batch.

<u>348.41^B</u>

No Description.

<u>348.42^B</u>

No Description.

<u>348.43^B</u>

No Description.

<u>348.5^B</u>

No Description.

<u>348.6^B</u>

No Description.

<u>348.7^B</u>

No Description.

<u>349^B</u>

No Description.

<u>^^TRIGGER^349^.02</u>

This is the type of transmission record.

<u>349^AT2^MUMPS</u>

This cross-reference is built on TRANSMISSION TYPE and DATE CREATED.

<u>349.1^B</u>

No Description.

<u>349.11^B</u>

No Description.

<u>349.12^B</u>

No Description.

<u>^^TRIGGER^349.1^33</u>

No Description.

<u>349.161^B</u>

No Description.

<u>349.2^AKEY1^MUMPS</u>

This cross-reference is used to key the statements for CCPC.

<u>349.2^AKEY2^MUMPS</u>

This cross-reference is used to key the statements for CCPC.

<u>349.2^AD^MUMPS</u>

This is the cross-reference to find patient statement errors that are returned from CCPC.

<u>349.3^B</u>

No Description.

<u>349.3^AD</u>

This cross-ref is used to record the Purge date. Entries will be purged after this date.

<u>349.4^B</u>

No Description.

<u>349.7^B</u>

No Description.

<u>349.8^B</u>

No Description.

<u>349.9^B</u>

No Description.

<u>^^TRIGGER^349.9^12</u>

No Description.

<u>430^B</u>

This cross-reference is used for file look-up and sorting by Accounts Receivable Bill No.

<u>430^D^MUMPS</u>

This cross reference is used for lookup and sorts on the Accounts Receivable 6-digit Bill number (without the station number).

<u>430^TCSP^MUMPS</u>

This cross reference indicates whether a debt has been sent to Cross-Servicing.

<u>^^TRIGGER^430^71</u>

This cross reference triggers the Principal Balance field \#71.

<u>430^E</u>

This cross reference is set for the Third-Party type category of bills.

<u>430^AC</u>

This cross-reference is needed to find bills by status. This cross-reference is used extensively by reports and options.

<u>430^AS2^MUMPS</u>

This cross-reference allows rapid look-up of bills by status for a specific debtor.

<u>^^TRIGGER^430^60</u>

This cross-reference triggers the Date Account Activated field. When a Bill is made Active or Open for a patient, new activity needs to be logged to that it may appear on the next patient statement.

<u>430^C</u>

This cross-reference allows user look-up of bills belonging to a specific debtor.

<u>430^AS1^MUMPS</u>

This cross-reference allows rapid look-up of bills by status for a specific debtor.

<u>430^ATD^MUMPS</u>

This cross-reference is not actively used and only exists to update the activity for a debtor in the event the debtor field is ever changed, which should never happen.

<u>430^AK^MUMPS</u>

This cross-reference is used to track accounts that have been made ACTIVE. It is used by the patient statement procedures.

<u>430^AD</u>

This cross reference is used for lookup bills by Referral Date.

<u>430^TCSP^MUMPS</u>

This Cross-Reference indicates whether a debt has been sent to Cross-Servicing.

<u>430^AN</u>

Cross-servicing Returned Date Index

<u>430.01^B</u>

This cross reference is used for lookup and sorts of the Fiscal Years for the Bill.

<u>430.01^C^MUMPS</u>

This x-ref has quit to remove the previous x-ref for this field that was no longer needed.

<u>430^F^</u>

This cross reference is set for the Pat Ref No. in the Fiscal Year multiple that is not a Bill No.

<u>430^AJ^MUMPS</u>

This cross reference sets the Appropriation Symbol field 18 to the non -year appropriation symbol entered for this Fiscal Year.

<u>^^TRIGGER^430.01^1</u>

This cross reference triggers the Curr.Prin.Bal field \#1.

<u>430.02^B</u>

This cross-reference is used for lookup and sorts for the Date of Charges.

<u>430.02^AC^MUMPS</u>

This cross reference calculates and sets the Total Amount field 6.

<u>430.02^AD^MUMPS</u>

This cross-reference calculates and sets the Total Amount field 6.

<u>430.02^AE^MUMPS</u>

Obsolete version 3.7 cross-reference.

<u>430.051^B</u>

This cross-reference is used for lookup and sorts for Repayment Due Dates.

<u>430.2^B</u>

This cross-reference is used for sorting and file look-up by AR Category.

<u>430.2^C</u>

This cross-reference is used for sorting and file look-up by the Abbreviation field.

<u>430.2^AC</u>

This cross-reference is used for lookups by the Category Number field. This cross-reference is used extensively throughout the AR package and SHOULD NOT be edited. By editing this field, it may cause serious functional problems within the AR package.

<u>430.3^B</u>

This cross-reference is used for sorting and file look-up by the AR Transaction Type.

<u>430.3^C</u>

This cross-reference is used for look-up and sorting transaction types by Abbreviation.

<u>430.3^AC^MUMPS</u>

This cross-reference is used for look-up by Status Number.

<u>430.4^B</u>

This cross-reference is used for sorting and file look-up by the AR Bill Number.

<u>430.4^C^MUMPS</u>

This cross-reference is used for sorting and file look-up by AR bill number (without the station number prefix.).

<u>430.5^B</u>

This cross-reference is used for sorting and file look-up by AR Parameter.

<u>430.5^C</u>

This cross-reference is used for file look-up and sorting by the AR Parameter Type field.

<u>430.5^AC</u>

This cross-reference is used for look-up by the Number of Letters field.

<u>430.6^B</u>

This cross-reference is used for sorting and file look-up by AR Debt List.

<u>430.6^C</u>

This cross-reference is used for look-up and sorting by the Full Name field.

<u>430.6^D</u>

This cross-reference is used for look-up and sorting by the AR Debt List Type field.

<u>430.7^B</u>

This cross-reference is used for sorting and file look-up by AR Billing Error message name.

<u>430.71^B</u>

This cross-reference is used for look-up by the Error Code field.

<u>430.7^AC</u>

This cross-reference is used to sort the bills for printing the ARDC Report.

<u>430.8^B</u>

This cross-reference is used for look-up and sorting by Identifier.

<u>430.9^B</u>

This cross-reference is used for sorting and file look-up by the AR Conversion name.

<u>430.95^B</u>

This cross-reference is used for look-up and sorting by the Inconsistencies field.

<u>431^B</u>

This cross-reference is used for sorting and file look-up by effective date.

<u>433^B</u>

This cross-reference is used for sorting and file look-up by Transaction Number.

<u>433.01^B</u>

This cross-reference is used for sorting by Fiscal Year.

<u>433^C</u>

This cross-reference is used to determine the transaction entries associated with each internal Bill number (from file 430).

<u>^^TRIGGER^433^19</u>

This cross-reference is needed to log an "activity" to the patient account for printing patient statements and various reports.

<u>433^AE^MUMPS</u>

This cross-reference is used for sorting by Calm Code status.

<u>433^AG</u>

This cross-reference is used for the Follow-up List.

<u>433^AD^MUMPS</u>

This cross-reference will file the entry into the AR Data Queue file for transmission to the ARC.

<u>433^AW^MUMPS</u>

This cross-reference is set if the transaction is a 'write-off' transaction (i.e., waivers and compromises). It is used to calculate the summary write-off documents for FMS.

<u>433^AT2^MUMPS</u>

This cross reference is used by the National Database collector and by AR reports to look up transactions by transaction type and by date entered (processed).

<u>433^AEOB1^MUMPS</u>

The AEOB cross-ref will be set if the Transaction Type is Payment in Part, for a TP bill referred to RC that does not have the EOB Code field populated.

<u>433^AI^MUMPS</u>

This cross-ref will file the entry into the AR Date Queue file for transmission to the ARC.

<u>433^AF</u>

This cross-reference is used for sorting on receipt number.

<u>433^AH^MUMPS</u>

This cross-reference will file the entry into the AR Data Queue file for transmission to the ARC.

<u>433^ATD^MUMPS</u>

This cross-reference is used for the patient statement. It is sorted by the DEBTOR (field 9, file 430) and DATE ENTERED (field 19, file 433). Loop through the Debtors transactions (Date Entered) to display his transactions for a specified time period.

<u>433^AT1^MUMPS</u>

This cross reference is used by the National Database collector and by AR reports to look up transactions by transaction type and by date entered (processed).

<u>433^AC^MUMPS</u>

This cross-reference will file the entry into the AR Data Queue file for transmission to the ARC.

<u>433^AP^MUMPS</u>

This cross-reference is used for sorting by the Prepayment Trans. Date.

<u>433^AEOB^MUMPS</u>

This cross-ref is used to alert AR staff that EOB Processing should be done for a payment transaction. These payments are from Insurance Companies whose bill is referred to RC for collection action. Once the EOB Code is entered, this cross-ref can be deleted.

<u>433.061^B</u>

This cross-reference is used for sorting by Date of Charges.

The following three fields within File \#430 contain two separate cross-references, which modify a single reference level:

- field \#9, ATD x-ref, and field \#60, AK x-ref, both setup "ATD";
- field \#8, AS2 x-ref, and field \#9 AS 1 x-ref, both setup "AS";

The re-indexing of both or either cross-reference may be done to correctly establish the index.

<u>433^CA^MUMPS</u>

This x-ref identifies Contract Adjustment Transactions. It is used by the FMS data collector to compile the WR 06 document for transmission to FMS.

<u>433^ACE^MUMPS</u>

This cross-reference is set to aid in printing the medication co-pay exemption report. It is set whenever the decrease transaction or interest exemption transaction is applied as a result of an exemption from medication co-pays. It is also set for the increase transaction if a refund Bill is set up as a result of medication co-pays.

<u>434^B</u>

This cross-reference is used file look-up and sorting by AR Form Letter name field.

<u>434^C</u>

This cross-reference is used for file look-up and sorting by Full Name.

<u>435^B</u>

This cross-reference is used for sorting and file look-up by receipt \#.

<u>435^AF^MUMPS</u>

This cross-reference will kill the corresponding file 433 "AF" cross-reference when the receipt number is killed in this file.

Since the receipt number x-ref in file 433 is only needed for the printing of the 215 and requires the "Batch Payment" entry in this file, once the receipt number is purged from this file the corresponding 433 x-ref can be purged.

<u>435^AA1^MUMPS</u>

This x-ref stores the last receipt number used by a user specific to type of payment.

This x-ref is used to show the default Receipt \# when using the payment options in the Agent Cashier module.

<u>435^AA^MUMPS</u>

This x-ref stores the last receipt number used by a user specific to type of payment. This x-ref supports the x-ref in field "OPENED BY".

<u>435.01^B</u>

This x-ref is used for look-up and sorting by FileMan.

<u>435^AC^MUMPS</u>

This cross-reference is needed to display payments not yet posted to patient accounts during the use of the "Account Profile" option.

<u>^^TRIGGER^435.01^.03</u>

No Description.

<u>436.1^B</u>

No Description.

<u>436.1^C</u>

No Description.

<u>436.12^B</u>

No Description.

<u>^^TRIGGER^436.12^.02</u>

This trigger will insert the current user into ENTERED BY field of the COMMENT DATE TIME multiple.

# Operating Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INTRODUCTION

This section deals with the specific information you need to determine whether your facility can run AR effectively. The information presented here includes sizing, equipment requirements, journaling, routines, and external/internal relations with other DHCP packages.

SIZING INFORMATION

AR test sites were asked to provide the number of entries made in the three main files for Accounts Receivable using VA FileMan. In addition, the sites ran %ZTBKC to obtain the block count for the associated globals. These files represent the most active and fastest growing AR files. As a result, it is estimated that AR will require the following (note that block sizes are for DSM-11):

> ^RCD(340 - 1/5 block per entry (AR Debtor)

> ^PRCA(430 - 1/2 block per entry (Accounts Receivable)

> ^PRCA(433 - 1/4 block per entry (AR Transaction)

> ^RCD(341 - 1/4 block per entry(AR Event)

Please note these are an estimate of what is necessary for only a subset of the dynamic files of AR.

To get the estimate of the number of Accounts Receivable transactions, contact your Fiscal Service.

> **NOTE:** Please be aware that Fiscal is required to have access to this information for 6 to 10 years to meet legal requirements.

RECOMMENDED EQUIPMENT

<u>Fiscal</u>

> 1 CRT per Accounting Technician

> 1 CRT per Accounts Receivable Clerk

> 1 CRT for Agent Cashier

> 1 CRT for Application Coordinator

> 1 132 column Dot Matrix Printer (for printing free-form bills, preprinted UB92 forms, reports, and patient statements)

> 1 Letter Quality Printer (reports and letters)

> 1 Letter Quality Printer (for printing collection letters)

There are three default printer locations associated with the AR package. These printers will be associated with a device number on your DHCP system. You may be able to use the same printer for multiple types of outputs. Please consult with your Application Coordinators as to what outputs may be sent to "shared" printers, and where these printers should be located within the Fiscal Service.

TRANSLATION TABLES

The following is a list of globals that should be translated to allow access in a distributed operating system environment. All globals are accessed by all users and all AR data is stored in ^PRC\* and RC\*.

RCD - This global contains the AR Debtor file (#340).

PRCA - This global contains the Accounts Receivable files.

> NOTE: The PRCAK, PRCA, and RC globals may grow very large.

> (See the Sizing Information).

RC - Debtor.

RCY - Batch payment.

PRCAK - Archive Purge.

# On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that you print the AR Data Dictionaries immediately after you load the software. This is done through the VA FileMan option List File Attributes. The AR files include numbers 340 - 344, 347 - 348.1, and 430 - 433. You may specify a Standard or Brief Data Dictionary as your needs require. Utilizing on-line documentation is the best way to obtain the most current information available. Further information for generating On-line documentation is provided in the Kernel documentation. This can be obtained either from your IRM Service or your local ISC.

Currently AR utilizes PRCA and RC as namespaces. PRCA is in the process of being phased out. There are no special templates associated with AR V.4.5.

Upon gaining access to the system, the user is prompted to enter a menu selection for each level of the system. If no selection is listed within the prompt, or if the user is unsure of which selections are available, entering a "?" will bring up a list of available selections. Entering "??" will give additional information, and "???" will give brief descriptions of all entries. For prompts containing a selection, the user should enter a \<return\> to make this selection. If the "NO//" or "YES//" feature is included in the prompt, entering a \<return\> will indicate selection of the indicated option, and entering a "Y" for yes or "N" for no will allow the user to accept or reject the prompt selection.

# Appendix 1: AR Archiving Checklist and Troubleshooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PURPOSE

This checklist and troubleshooting guide were designed to aid Fiscal and IRM services in the archiving process. The archiving process was developed to remove old bills and transactions from on-line to off-line storage. Upon completion of the archive process, an archived Bill in file 430 is identified by a stub record consisting of the Bill number, archive date, and archived status. All corresponding transactions in file 433 are removed in their entirety from the on-line system.

HARDWARE REQUIREMENTS

Archiving records requires the use of a medium such as tape or removable disk. When selecting either of these mediums, consider that .003 megabytes of available free space is necessary for every entry in file 430 to be archived.

ARCHIVE CHECKLIST

1.  Check with Fiscal for the time period to begin archiving. Currently, it is not possible to archive data less than two fiscal years old. For example, if today is September 19, 1994, the latest date which data can be archived is October 1, 1992.
2.  From the AR Archive Records Menu, select the option Mark AR Records for Archival.

> The start date default "None", will archive the earliest inactive data that is not under the status of Active, Amended Bill, Archived, New Bill, Open, Pending Approval, Refund Review, Returned For Amendment, Returned From AR (NEW), or Suspended.

> The end date is the latest date to archive data which is not under any of the status's listed above. This date is up to the individual Fiscal service. For example, your Fiscal service may want to have records from the past four years on-line which would mean that the end date would be entered as 10/1/90.

> Upon completion of the marking process, a message is automatically generated and sent to the user who began the process regarding the number of records that were marked "Pending Archive".

3.  Fiscal should review the “Pending Archive” list using the option, Detailed Report of Pending Archive Records, to ensure the records that are marked are the desired records for archiving. If an undesired record is marked, the option Unmark Records Marked for Archival can be used to change the status from Pending Archive to its previous status.
4.  On the system where the global ^PRCAK is located, calculate the amount of disk space required by multiplying the number of records to be archived by .003. “.003” is the amount of space each record takes up in megabytes. The product of this multiplication is the number of megabytes of temporary storage that will be necessary for the archiving procedure.

> Ex. 12,000 records X .003 MB = 48 MB

> Note: This space will be freed when the archive process is complete.

5.  Select the option Build Temporary Archive File. During this process, the system will loop through all bills marked “Pending Archive” (file 430) and identify all corresponding transactions (file 433). For each Bill and transaction being archived, the “pointer-values” will be expanded and moved to the temporary archive file. Upon completion of the Building process, a message is generated indicating whether or not the process was successful and how many archive records were created.
6.  Using the operating systems global save utility (^%GS, ^%GSAVE, etc..) write the global ^PRCAK to a removable storage medium i.e. tape, disk, etc.
7.  Upon completion of step 6, use the option Remove AR Records from Files. This option will create the stub record in file 430 and remove all corresponding transactions in file 433. When this step finishes, the temporary storage space from step 5 is freed up. The date entered using this option is stored with the stub record as the “date of archival”.

> **NOTE:** The actual disk space regained will vary due to fragmentation in compression algorithms used by the operating systems. Global compression utilities should be run in accordance with operating systems “cookbook” recommendations to regain unused disk space.

TROUBLESHOOTING

<table>
<caption><p><span id="_Toc67391150" class="anchor"></span>Table 23: Detailed CR Control Segment</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>PROBLEM</th>
<th>SOLUTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>System crashes or job stops running.</td>
<td><p>Use the option Purge Temporary Archive</p>
<p>Storage File and rerun archive procedure.</p></td>
</tr>
<tr class="even">
<td>Archive process identifies few or no records.</td>
<td>Rerun the archive process using a more extensive date range.</td>
</tr>
<tr class="odd">
<td>Need to restore archive records.</td>
<td>Using the operating systems global restore utility, restore the archived global and use VA File Manager to inquire or print file entries.</td>
</tr>
</tbody>
</table>

<span id="_Toc67391150" class="anchor"></span>Table 23: Detailed CR Control Segment

> **NOTE:** Once the archive process has begun it cannot be "restarted". If an attempt is made to begin the archive process while it is still in progress, a message will appear indicating that "this process has failed because another AR archive process is already in progress".

# Appendix 2: FMS Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pages contain the document structure and the nature of the data that must be supplied from each service to the Financial Management System.

COLUMN KEYS

\# = Field Number

Field Name = Name of Field

Generating Package = Package responsible for code

Value = Default or pattern in Alpha/Numeric

Value Status = Hard Code or Variable data element

Description = Brief explanation of field

Any segments not listed in a document, are not required or not used.

DETAILED CASH RECEIPT (CR) DOCUMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment-ID          | CTL   | HC           | Segment identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction class   | DOC   | HC           | DOC indicates document transaction                  |
| 6   | Transaction code    | CR    | HC           | CR indicates cash receipt document                  |
| 7   | SEC1 code           | 4A    | VAR          | VHA = 10, VBA = 20                                  |
| 8   | Batch number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date of creation of document (YYYYMMDD)    |
| 11  | Transaction Time    | 6N    | VAR          | Calendar time of creation of document (HHMMSS)      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3A    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391151" class="anchor"></span>Table 24: Detailed CR Document Segments

| \#  | Field Name           | Value | Value Status | Description                                                     |
|-----|----------------------|-------|--------------|-----------------------------------------------------------------|
| 1   | Segment ID           | DOC   | HC           | Segment identifier                                              |
| 2   | Segment ID           | CR1   | HC           | Segment identifier                                              |
| 3   | Trans code           | CR    | HC           | CR indicates a Cash Receipt document                            |
| 4   | Trans Number         | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0             |
| 5   | Header XDivision     | 4A    | VAR          | VHA = 10, VBA = 20                                              |
| 6   | IFCAP flag           | N     | HC           | IFCAP update control point                                      |
| 7   | Segment ID           | CR2   | HC           | Segment identifier                                              |
| 8   | Record Year          | 2N    | VAR          | Calendar year of receipt deposit                                |
| 9   | Record Month         | 2N    | VAR          | Calendar month of receipt deposit                               |
| 10  | Record Day           | 2N    | VAR          | Calendar day of receipt deposit                                 |
| 11  | Fisc Month           | null  | HC           |                                                                 |
| 12  | Fisc Year            | null  | HC           |                                                                 |
| 13  | Beg Budget FY        | null  | HC           |                                                                 |
| 14  | End Budget FY        | null  | HC           |                                                                 |
| 15  | Document Type        | null  | HC           |                                                                 |
| 16  | Document Action      | E     | HC           | E is for original entry document                                |
| 17  | Acctg Trans Type     | null  | HC           |                                                                 |
| 18  | Offset Cash Account  | null  | HC           |                                                                 |
| 19  | Deposit Number       | 12A   | VAR          |                                                                 |
| 20  | Fund                 | null  | HC           |                                                                 |
| 21  | Document Total       | 15N   | VAR          | Payment amount (Each payment will generate a separate document) |
| 22  | Billed Fund          | null  | HC           |                                                                 |
| 23  | Accomplished Year    | 2N    | VAR          | Current calendar year                                           |
| 24  | Accomplished Month   | 2N    | VAR          | Current calendar month                                          |
| 25  | Accomplished Day     | 2N    | VAR          | Current day of current calendar month                           |
| 26  | Disbursing Office    | null  | HC           |                                                                 |
| 27  | HDR Ref Trans Code   | null  | HC           |                                                                 |
| 28  | HDR Ref Trans Number | null  | HC           |                                                                 |

<span id="_Toc67391152" class="anchor"></span>Table 25: Detailed CR Line Segments

| \#  | Field Name          | Value | Value Status | Description                                    |
|-----|---------------------|-------|--------------|------------------------------------------------|
| 1   | Segment ID          | LIN   | HC           | Segment identifier                             |
| 2   | Segment ID          | CRA   | HC           | Segment identifier                             |
| 3   | Line No             | 001   | HC           | Each payment will generate a separate document |
| 4   | Line Beg Budget FY  | null  | HC           |                                                |
| 5   | Line End Budget FY  | null  | HC           |                                                |
| 6   | Line Fund           | null  | HC           |                                                |
| 7   | XOrganization       | null  | HC           |                                                |
| 8   | Sat Station         | null  | HC           |                                                |
| 9   | XProgram            | null  | HC           |                                                |
| 10  | Revenue Source      | null  | HC           |                                                |
| 11  | Sub Rev Source      | null  | HC           |                                                |
| 12  | Budget Object Code  | null  | HC           |                                                |
| 13  | Sub BOC             | null  | HC           |                                                |
| 14  | Travel Type         | null  | HC           |                                                |
| 15  | Job Number          | null  | HC           |                                                |
| 16  | Report Category     | null  | HC           |                                                |
| 17  | GL Account          | null  | HC           |                                                |
| 18  | Vendor ID           | null  | HC           |                                                |
| 19  | Vendor Address Code | null  | HC           |                                                |
| 20  | Line Amount         | 15N   | VAR          | Amount of collection                           |
| 21  | Incr/Decr Indicator | I     | HC           | I for increase                                 |
| 22  | Partial Final Ind   | null  | HC           |                                                |
| 23  | Line Trans Type     | 2A    | VAR          | Refund (01) or Reimbursement (05)              |
| 24  | Ref Trans Code      | BD    | HC           | Referenced transaction code                    |
| 25  | Ref Trans Numb      | 11A   | VAR          | Bill Number                                    |
| 26  | Ref Trans Line      | 001   | HC           | Document line to which collection is applied   |
| 27  | Check Number        | null  | HC           |                                                |
| 28  | Advance Flag        | null  | HC           |                                                |
| 29  | Line Description    | null  | HC           |                                                |
| 30  | Agreement Numb      | null  | HC           |                                                |
| 31  | Travel Advance Numb | null  | HC           |                                                |
| 32  | Action Out          | null  | HC           |                                                |
| 33  | Cost Center         | null  | HC           |                                                |
| 34  | Cost Sat Station    | null  | HC           |                                                |
| 35  | Reclass Adv Ind     | null  | HC           |                                                |

<span id="_Toc67391153" class="anchor"></span>Table 26: Summary CR Control Segment

1.  SUMMARY CASH RECEIPT (CR) DOCUMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment-ID          | CTL   | HC           | Segment identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction class   | DOC   | HC           | DOC indicates document transaction                  |
| 6   | Transaction code    | CR    | HC           | CR indicates cash receipt document                  |
| 7   | SEC1 code           | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 8   | Batch number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date of creation of document (YYYYMMDD)    |
| 11  | Transaction Time    | 6N    | VAR          | Calendar time of creation of document (HHMMSS)      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3A    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391154" class="anchor"></span>Table 27: Summary CR Document Segments

| \#  | Field Name           | Value | Value Status | Description                                         |
|-----|----------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID           | DOC   | HC           | Segment identifier                                  |
| 2   | Segment ID           | CR1   | HC           | Segment identifier                                  |
| 3   | Trans code           | CR    | HC           | CR indicates a Cash Receipt document                |
| 4   | Trans Number         | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 5   | Header XDivision     | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 6   | IFCAP flag           | N     | HC           | IFCAP update control point                          |
| 7   | Segment ID           | CR2   | HC           | Segment identifier                                  |
| 8   | Record Year          | 2N    | VAR          | Calendar year of receipt deposit                    |
| 9   | Record Month         | 2N    | VAR          | Calendar month of receipt deposit                   |
| 10  | Record Day           | 2N    | VAR          | Calendar day of receipt deposit                     |
| 11  | Fisc Month           | null  | HC           |                                                     |
| 12  | Fisc Year            | null  | HC           |                                                     |
| 13  | Beg Budget FY        | null  | HC           |                                                     |
| 14  | End Budget FY        | null  | HC           |                                                     |
| 15  | Document Type        | null  | HC           |                                                     |
| 16  | Document Action      | E     | HC           | E is for original entry document                    |
| 17  | Acctg Trans Type     | null  | HC           |                                                     |
| 18  | Offset Cash Account  | null  | HC           |                                                     |
| 19  | Deposit Number       | 12A   | VAR          | SF-215 \#                                           |
| 20  | Fund                 | Null  | HC           |                                                     |
| 21  | Document Total       | 15N   | VAR          | Amount of collection for fund                       |
| 22  | Billed Fund          | null  | HC           |                                                     |
| 23  | Accomplished Year    | 2N    | VAR          | Current calendar year                               |
| 24  | Accomplished Month   | 2N    | VAR          | Current calendar month                              |
| 25  | Accomplished Day     | 2N    | VAR          | Current day of current calendar month               |
| 26  | Disbursing Office    | null  | HC           |                                                     |
| 27  | HDR Ref Trans Code   | null  | HC           |                                                     |
| 28  | HDR Ref Trans Number | null  | HC           |                                                     |

<span id="_Toc67391155" class="anchor"></span>Table 28: Summary CR Line Segments

| \#  | Field Name          | Value | Value Status | Description                                                                                                              |
|-----|---------------------|-------|--------------|--------------------------------------------------------------------------------------------------------------------------|
| 1   | Segment ID          | LIN   | HC           | Segment identifier                                                                                                       |
| 2   | Segment ID          | CRA   | HC           | Segment identifier                                                                                                       |
| 3   | Line No             | 001   | HC           | Line \#                                                                                                                  |
| 4   | Line Beg Budget FY  | 2N    |              | Current Fiscal Year                                                                                                      |
| 5   | Line End Budget FY  | null  | HC           |                                                                                                                          |
| 6   | Line Fund           | 6A    |              | Appropriation code: 5014(MCCR) 2431(CATC) 3220(ADMIN) 1435(INT) 0869(Judicial Fees)                                      |
| 7   | XOrganization       | 3N    |              | Station number                                                                                                           |
| 8   | Sat Station         | null  | HC\*         | \*If these fields are activated, it will be necessary to undertake a major reconfiguration of the current AR software... |
| 9   | XProgram            | null  | HC           |                                                                                                                          |
| 10  | Revenue Source      | ARRV  | HC\*         |                                                                                                                          |
| 11  | Sub Rev Source      | null  | HC\*         |                                                                                                                          |
| 12  | Budget Object Code  | null  | HC\*         |                                                                                                                          |
| 13  | Sub BOC             | null  | HC           |                                                                                                                          |
| 14  | Travel Type         | null  | HC\*         |                                                                                                                          |
| 15  | Job Number          | null  | HC\*         |                                                                                                                          |
| 16  | Reporting Category  | null  | HC           |                                                                                                                          |
| 17  | GL Account          | null  | HC           |                                                                                                                          |
| 18  | Vendor ID           | null  | HC           |                                                                                                                          |
| 19  | Vendor Address Code | null  | HC           |                                                                                                                          |
| 20  | Line Amount         | 15N   | VAR          | Amount of collection for appropriation                                                                                   |
| 21  | Incr/Decr Indicator | I     | HC           | I for increase                                                                                                           |
| 22  | Partial Final Ind   | null  | HC           |                                                                                                                          |
| 23  | Line Trans Type     | 23    | HC           |                                                                                                                          |
| 24  | Ref Trans Code      | null  | HC           |                                                                                                                          |
| 25  | Ref Trans Number    | null  | HC           |                                                                                                                          |
| 26  | Ref Trans Line      | null  | HC           |                                                                                                                          |
| 27  | Check Number        | null  | HC           |                                                                                                                          |
| 28  | Advance Flag        | null  | HC           |                                                                                                                          |
| 29  | Line Description    | null  | HC           |                                                                                                                          |
| 30  | Agreement Numb      | null  | HC           |                                                                                                                          |
| 31  | Travel Advance Numb | null  | HC           |                                                                                                                          |
| 32  | Action Out          | null  | HC           |                                                                                                                          |
| 33  | Cost Center         | null  | HC\*         |                                                                                                                          |
| 34  | Cost Sat Station    | null  | HC\*         |                                                                                                                          |
| 35  | Reclass Adv Ind     | null  | HC           |                                                                                                                          |

<span id="_Toc67391156" class="anchor"></span>Table 29: OP Control Segment

2.  OVERCOLLECTION PAYMENT (OP) DOCUMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID          | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class   | DOC   | HC           | Document transaction                                |
| 6   | Transaction Code    | OP    | HC           | Transaction Code                                    |
| 7   | SEC1 Code           | 10    | HC           | Security 1 Code                                     |
| 8   | Batch Number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time    | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3N    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391157" class="anchor"></span>Table 30: OP Document Segment

| \#  | Field Name            | Value   | Value Status | Description                                         |
|-----|-----------------------|---------|--------------|-----------------------------------------------------|
| 1   | Segment ID            | DOC     | HC           | Segment Identifier                                  |
| 2   | Segment ID            | PV1     | HC           | Segment Identifier                                  |
| 3   | Trans Code            | OP      | HC           | Document ID                                         |
| 4   | Trans Number          | 11A     | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 5   | Header XDivision      | 10      | HC           | DOC ID SEC1                                         |
| 6   | Segment ID            | PV2     | HC           | Segment Identifier                                  |
| 7   | Record Month          | 2N      | VAR          | Refund processed on this calendar month             |
| 8   | Record Day            | 2N      | VAR          | Refund processed on this calendar day               |
| 9   | Record Year           | 2N      | VAR          | Refund processed on this calendar year              |
| 10  | Fisc Month            | null    | HC           |                                                     |
| 11  | Fisc Year             | null    | HC           |                                                     |
| 12  | HDR Budget FY         | null    | HC           |                                                     |
| 13  | HDR End Budget FY     | null    | HC           |                                                     |
| 14  | Document Action       | E       | HC           | Original Document                                   |
| 15  | HDR Trans Type        | 01      | HC           | 01 = Payment of over collection revenue             |
| 16  | Document Type         | null    | HC           |                                                     |
| 17  | Sched Year            | 2N      | VAR          | Current calendar year                               |
| 18  | Sched Month           | 2N      | VAR          | Current calendar month                              |
| 19  | Sched Day             | 2N      | VAR          | Current calendar day                                |
| 20  | Voucher-Schedule Type | null    | HC           |                                                     |
| 21  | HDR Fund              | null    | HC           |                                                     |
| 22  | Document Desc         | null    | HC           |                                                     |
| 23  | Disbursing Office     | null    | HC           |                                                     |
| 24  | FA IND                | null    | HC           |                                                     |
| 25  | Vendor ID             | MISCVET | HC           | Vendor Code                                         |
| 26  | Vendor Address Code   | null    | HC           |                                                     |
| 27  | Document Total        | 15N     | VAR          | Amount of Refund                                    |
| 28  | Vendor Name           | 30A     | VAR          | Veteran Name                                        |
| 29  | Vendor Address Line 1 | 30A     | VAR          | Address \#1                                         |
| 30  | Vendor Address Line 2 | 30A     | VAR          | Address \#2                                         |
| 31  | City                  | 19A     | VAR          | City                                                |
| 32  | State Code            | 2A      | VAR          | State                                               |
| 33  | Zip Code              | 9A      | VAR          | Zip                                                 |
| 34  | Hand Pick CK IND      | null    | HC           |                                                     |

<span id="_Toc67391158" class="anchor"></span>Table 31: OP Line Segments

| \#  | Field Name           | Value  | Value Status | Description                                                                                                              |
|-----|----------------------|--------|--------------|--------------------------------------------------------------------------------------------------------------------------|
| 1   | Segment ID           | LIN    | HC           | Segment Identifier                                                                                                       |
|     |                      |        |              |                                                                                                                          |
| 2   | Segment ID           | PVA    | HC           | Segment Identifier                                                                                                       |
| 3   | Line No              | 001    | HC           | Line \#                                                                                                                  |
| 4   | Ref Trans Code       | Null   | HC           |                                                                                                                          |
| 5   | Ref Trans Number     | Null   | HC           |                                                                                                                          |
| 6   | Ref Trans Line       | Null   | HC           |                                                                                                                          |
| 7   | Accept Year          | Null   | HC           |                                                                                                                          |
| 8   | Accept Month         | Null   | HC           |                                                                                                                          |
| 9   | Accept Day           | Null   | HC           |                                                                                                                          |
| 10  | Vendor Invoice       | Null   | HC           |                                                                                                                          |
| 11  | Vendor Invoice Line  | Null   | HC           |                                                                                                                          |
| 12  | Line Description     | Null   | HC           |                                                                                                                          |
| 13  | Line Trans Type      | Null   | HC           |                                                                                                                          |
| 14  | Line Budget FY       | 2N     | VAR          | Fiscal Year                                                                                                              |
| 15  | Line End Budget FY   | Null   | HC           |                                                                                                                          |
| 16  | Line Fund            | 5014   | HC           | Appropriation                                                                                                            |
| 17  | XOrganization        | 3N     | VAR          | Station number                                                                                                           |
| 18  | Sat Station          | Null\* | HC           | \*If these fields are activated, it will be necessary to undertake a major reconfiguration of the current AR software... |
| 19  | Cost Center          | Null\* | HC           |                                                                                                                          |
| 20  | Cost Sat Station     | Null\* | HC           |                                                                                                                          |
| 21  | XProgram             | Null\* | HC           |                                                                                                                          |
| 22  | Budget Object Code   | Null\* | HC           |                                                                                                                          |
| 23  | Sub BOC              | Null\* | HC           |                                                                                                                          |
| 24  | Job Number           | Null\* | HC           |                                                                                                                          |
| 25  | Reporting Category   | Null\* | HC           |                                                                                                                          |
| 26  | GL Account           | Null   | HC           |                                                                                                                          |
| 27  | Quantity             | Null   | HC           |                                                                                                                          |
| 28  | Revenue Source       | ARRV   | HC           |                                                                                                                          |
| 29  | Sub Rev Source       | Null\* | HC           |                                                                                                                          |
| 30  | Vendor Invoice Year  | Null   | HC           |                                                                                                                          |
| 31  | Vendor Invoice Month | Null   | HC           |                                                                                                                          |
| 32  | Vendor Invoice Day   | Null   | HC           |                                                                                                                          |
| 33  | Int Reason Code      | Null   | HC           |                                                                                                                          |
| 34  | Line Amount          | 15N    | VAR          |                                                                                                                          |
| 35  | Incr/Decr Indicator  | I      | HC           |                                                                                                                          |
| 36  | Partial Final IND    | Null   | HC           |                                                                                                                          |
| 37  | VI Log Year          | Null   | HC           |                                                                                                                          |
| 38  | VI Log Month         | Null   | HC           |                                                                                                                          |
| 39  | VI Log Day           | Null   | HC           |                                                                                                                          |
| 40  | Line Type            | Null   | HC           |                                                                                                                          |
| 41  | Related GBL          | Null   | HC           |                                                                                                                          |

<span id="_Toc67391159" class="anchor"></span>Table 32: WR Control Segment

3.  WRITE-OFF (WR) DOCUMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID          | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class   | DOC   | HC           | Document transaction                                |
| 6   | Transaction Code    | WR    | HC           | Transaction Code                                    |
| 7   | Sec1 Code           | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 8   | Batch Number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time    | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3N    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391160" class="anchor"></span>Table 33: WR Document Segments

| \#  | Field Name                | Value  | Value Status | Description                                                                      |
|-----|---------------------------|--------|--------------|----------------------------------------------------------------------------------|
| 1   | Segment ID                | DOC    | HC           | Segment identifier                                                               |
|     |                           |        |              |                                                                                  |
| 2   | Segment ID                | CR1    | HC           | Segment identifier                                                               |
| 3   | Trans code                | WR     | HC           | WR indicates a Write Off document                                                |
| 4   | Trans Number              | 11A    | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0                              |
| 5   | Header XDivision          | 4N     | HC           | VHA = 10, VHB = 20                                                               |
|     |                           |        |              |                                                                                  |
| 6   | Segment ID                | CR2    | HC           | Segment identifier                                                               |
| 7   | Record Year               | 2N     | VAR          | Calendar year of write-off                                                       |
| 8   | Record Month              | 2N     | VAR          | Calendar year of write-off                                                       |
| 9   | Record Day                | 2N     | VAR          | Calendar year of write-off                                                       |
| 10  | Fisc Month                | null   | HC           |                                                                                  |
| 11  | Fisc Year                 | null   | HC           |                                                                                  |
| 12  | Beg Budget FY             | null   | HC           |                                                                                  |
| 13  | End Budget FY             | null   | HC           |                                                                                  |
| 14  | Document Type             | null   | HC           |                                                                                  |
| 15  | Document Action           | E      | HC           | E is for original entry document                                                 |
| 16  | Acctg Trans Type          | null   | HC           |                                                                                  |
| 17  | Offset Cash Account       | null   | HC           |                                                                                  |
| 18  | Deposit Number            | 12’9s’ | HC           | Deposit Number                                                                   |
| 19  | Fund                      | null   | HC           |                                                                                  |
| 20  | Document Total            | 15N    | VAR          | Write-off “unassigned” amount (Each write-off will generate a separate document) |
| 21  | Billed Fund               | null   | HC           |                                                                                  |
| 22  | Accomplished Year         | 2N     | VAR          | Current calendar year                                                            |
| 23  | Accomplished Month        | 2N     | VAR          | Current calendar month                                                           |
| 24  | Accomplished Day          | 2N     | VAR          | Current day of current calendar month                                            |
| 25  | Disbursing Office         | null   | HC           |                                                                                  |
| 26  | HDR Ref Trans Code        | null   | HC           |                                                                                  |
| 27  | HDR Ref Trans null Number | null   | HC           |                                                                                  |

<span id="_Toc67391161" class="anchor"></span>Table 34: WR Line Segments

| \#  | Field Name          | Value | Value Status | Description                     |
|-----|---------------------|-------|--------------|---------------------------------|
| 1   | Segment ID          | LIN   | HC           | Segment identifier              |
|     |                     |       |              |                                 |
| 2   | Segment ID          | CRA   | HC           | Segment identifier              |
| 3   | Line No             | 001   | HC           | Same line as BD line referenced |
| 4   | Line Beg Budget FY  | null  | HC           |                                 |
| 5   | Line End Budget FY  | null  | HC           |                                 |
| 6   | Line Fund           | null  | HC           |                                 |
| 7   | XOrganization       | null  | HC           |                                 |
| 8   | Sat Station         | null  | HC           |                                 |
| 9   | XProgram            | null  | HC           |                                 |
| 10  | Revenue Source      | null  | HC           |                                 |
| 11  | Sub Rev Source      | null  | HC           |                                 |
| 12  | Budget Object Code  | null  | HC           |                                 |
| 13  | Sub BOC             | null  | HC           |                                 |
| 14  | Travel Type         | null  | HC           |                                 |
| 15  | Job Number          | null  | HC           |                                 |
| 16  | Report Category     | null  | HC           |                                 |
| 17  | GL Account          | null  | HC           |                                 |
| 18  | Vendor ID           | null  | HC           |                                 |
| 19  | Vendor Address Code | null  | HC           |                                 |
| 20  | Line Amount         | 15N   | VAR          | Amount of write-off             |
| 21  | Incr/Decr Indicator | I     | HC           | I for increase                  |
| 22  | Partial Final Ind   | null  | HC           |                                 |
| 23  | Line Trans Type     | 2A    | VAR          | 01 = Refund, 02 = Reimbursement |
| 24  | Ref Trans Code      | BD    | HC           | Reference Trans code            |
| 25  | Ref Trans Numb      | 11A   | VAR          | Bill Number                     |
| 26  | Ref Trans Line      | 001   | HC           | Reference Trans line            |
| 27  | Check Number        | null  | HC           |                                 |
| 28  | Advance Flag        | null  | HC           |                                 |
| 29  | Line Description    | null  | HC           |                                 |
| 30  | Agreement Numb      | null  | HC           |                                 |
| 31  | Travel Advance Numb | null  | HC           |                                 |
| 32  | Action Out          | null  | HC           |                                 |
| 33  | Cost Center         | null  | HC           |                                 |
| 34  | Cost Sat Station    | null  | HC           |                                 |
| 35  | Reclass Adv Ind     | null  | HC           |                                 |

<span id="_Toc67391162" class="anchor"></span>Table 35: SV Control Segment

4.  STANDARD VOUCHER (SV) DOCUMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID          | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class   | DOC   | HC           | Document transaction                                |
| 6   | Transaction Code    | SV    | HC           | Transaction code                                    |
| 7   | SEC1 Code           | 10    | HC           | Security code 1                                     |
| 8   | Batch Number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time    | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3N    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391163" class="anchor"></span>Table 36: SV Document Segment

| \#  | Field Name           | Value | Value Status | Description                                         |
|-----|----------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID           | DOC   | HC           | Segment identifier                                  |
|     |                      |       |              |                                                     |
| 2   | Segment ID           | SV1   | HC           | Segment identifier                                  |
| 3   | Trans code           | SV    | HC           | SV indicates a Standard Voucher document            |
| 4   | Trans Number         | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 5   | Header XDivision     | 10    | HC           | Security 1 code                                     |
|     |                      |       |              |                                                     |
| 6   | Segment ID           | SV2   | HC           | Segment identifier                                  |
| 7   | Record Year          | 2N    | VAR          | Calendar year of summary                            |
| 8   | Record Month         | 2N    | VAR          | Calendar month of summary                           |
| 9   | Record Day           | 2N    | VAR          | Calendar day of summary                             |
| 10  | Fisc Month           | null  | HC           |                                                     |
| 11  | Fisc Year            | null  | HC           |                                                     |
| 12  | Document Action      | E     | HC           | E is for original entry document                    |
| 13  | HDR EXP REV GL IND   | null  | HC           |                                                     |
| 14  | Header Budget FY     | null  | HC           |                                                     |
| 15  | Header End Budget FY | null  | HC           |                                                     |
| 16  | Header Fund          | null  | HC           |                                                     |
| 17  | Reversal Fisc Year   | 2N    | VAR          | Fiscal year of next month                           |
| 18  | Reversal Fisc Month  | 2N    | VAR          | Fiscal month of next month                          |
| 19  | Document Description | null  | HC           |                                                     |
| 20  | Budget Override IND  | null  | HC           |                                                     |
| 21  | Document Total       | 15N   | VAR          | Accrual total                                       |
| 22  | Header Description   | null  | HC           |                                                     |

<span id="_Toc67391164" class="anchor"></span>Table 37: SV Line Segments

<table>
<caption><p><span id="_Toc67391165" class="anchor"></span>Table 38: BD Control Segments</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Field Name</th>
<th>Value</th>
<th>Value Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>LIN</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Segment ID</td>
<td>SVA</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>3</td>
<td>Line No</td>
<td>001</td>
<td>HC</td>
<td>Each payment will generate a separate document</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Acctg Trans Type</td>
<td>21</td>
<td>HC</td>
<td>Summary receivables</td>
</tr>
<tr class="even">
<td>5</td>
<td>Budget FY</td>
<td>2N</td>
<td>HC</td>
<td>Fiscal year beginning</td>
</tr>
<tr class="odd">
<td>6</td>
<td>End Budget FY</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>7</td>
<td>Fund</td>
<td>6A</td>
<td>VAR</td>
<td><p>MCCR = 5014</p>
<p>Medical Service = 2431</p></td>
</tr>
<tr class="odd">
<td>8</td>
<td>XDivision</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>XOrganization</td>
<td>3N</td>
<td>VAR</td>
<td>Station number</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Sat Station</td>
<td>null</td>
<td>HC*</td>
<td>*If these fields are activated, it will be necessary to undertake a major reconfiguration of the current AR software...</td>
</tr>
<tr class="even">
<td>11</td>
<td>Cost Center</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="odd">
<td>12</td>
<td>Cost Sat Station</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>XProgram</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="odd">
<td>14</td>
<td>OBJ Rev Srce</td>
<td>ARRV</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="even">
<td>15</td>
<td>Sub OBJ Sub Rev Srce</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>Job Number</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>Reporting Category</td>
<td>null</td>
<td>HC*</td>
<td></td>
</tr>
<tr class="odd">
<td>18</td>
<td>Vendor ID</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>19</td>
<td>Vendor Address Code</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>20</td>
<td>Vendor Name</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>21</td>
<td>Quantity</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>22</td>
<td>Voucher Schedule Type</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>23</td>
<td>Agency Schedule No</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>24</td>
<td>Disbursing Office</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td>Guest Symbol</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>26</td>
<td>Ref Trans Code</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>27</td>
<td>Ref Trans Number</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>28</td>
<td>Ref Trans Line</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>29</td>
<td>Document Type</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>30</td>
<td>Vendor Invoice</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>31</td>
<td>Vendor Invoice Year</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>32</td>
<td>Vendor Invoice Month</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>33</td>
<td>Vendor Invoice Day</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>34</td>
<td>Vendor Invoice Line</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>SVB</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>2</td>
<td>Line Amount</td>
<td>15N</td>
<td>HC</td>
<td>Accrual amount</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Incr/Decr Indicator</td>
<td>I</td>
<td>HC</td>
<td>"I" for original entry</td>
</tr>
<tr class="even">
<td>4</td>
<td>Line Description</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>EXP Rev Gl Ind</td>
<td>R</td>
<td>HC</td>
<td>"R" for revenue</td>
</tr>
<tr class="even">
<td>6</td>
<td>Treasury Schedule No</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Accomplished Year</td>
<td>2N</td>
<td>VAR</td>
<td>Current calendar year</td>
</tr>
<tr class="even">
<td>8</td>
<td>Accomplished Month</td>
<td>2N</td>
<td>VAR</td>
<td>Current calendar month</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Accomplished Day</td>
<td>2N</td>
<td>VAR</td>
<td>Current calendar day (last day of month)</td>
</tr>
<tr class="even">
<td>10</td>
<td>Agreement Number</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Advance Flag</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>Voucher Schedule Cat</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Agency Schd Fisc YR</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>Obligation Fiscal YR</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc67391165" class="anchor"></span>Table 38: BD Control Segments

5.  BILLING (BD) DOCUMENT- REFUND

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID          | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class   | DOC   | HC           | Document transaction                                |
| 6   | Transaction Code    | BD    | HC           | Transaction code                                    |
| 7   | Sec1 Code           | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 8   | Batch Number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time    | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3N    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391166" class="anchor"></span>Table 39: BD Batch Segments

| \#  | Field Name      | Value | Value Status | Description        |
|-----|-----------------|-------|--------------|--------------------|
| 1   | Segment ID      | BAT   | HC           | Segment Identifier |
|     |                 |       |              |                    |
| 1   | Segment ID      | BD0   | HC           | Segment Identifier |
| 2   | Batch Number    | 6A    | VAR          | Batch \#           |
| 3   | Net             | null  | HC           |                    |
| 4   | Batch Month     | null  | HC           |                    |
| 5   | Batch Day       | null  | HC           |                    |
| 6   | Batch Year      | null  | HC           |                    |
| 7   | Batch CTL Count | null  | HC           |                    |

<span id="_Toc67391167" class="anchor"></span>Table 40: BD Document Segments

<table>
<caption><p><span id="_Toc67391168" class="anchor"></span>Table 41: BD Line Segments</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Field Name</th>
<th>Value</th>
<th>Value Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>DOC</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Segment ID</td>
<td>BD1</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>3</td>
<td>Trans code</td>
<td>BD</td>
<td>HC</td>
<td>BD indicates a Billing document</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Trans Number</td>
<td>11A</td>
<td>VAR</td>
<td><p>Station(3) + Fiscal Year(1) + K + Sequential(5) + 0</p>
<p>Accounts Receivable billing number</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Header XDivision</td>
<td>4A</td>
<td>HC</td>
<td>VHA = 10, VBA = 20</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>Segment ID</td>
<td>BD2</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Record Month</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction month</td>
</tr>
<tr class="even">
<td>8</td>
<td>Record Day</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction day</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Record Year</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction year</td>
</tr>
<tr class="even">
<td>10</td>
<td>Fisc Month</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Fisc Year</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>Acctg Trans Type</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Beg Budget FY</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>End Budget FY</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>15</td>
<td>Document Action</td>
<td>E</td>
<td>HC</td>
<td><p>E: original entry document,</p>
<p>M: modification document.</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>Vendor ID</td>
<td>null</td>
<td>HC</td>
<td><p>Vendor code: vendors, MISCE: employees, persons</p>
<p>MISCN: insurance company, institutions, (non fed.)</p>
<p>MISCG: (federal)</p>
<p>MISCVET: patients</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Vendor Address Code</td>
<td>2A</td>
<td>VAR</td>
<td>FMS vendor code (suffix)</td>
</tr>
<tr class="even">
<td>28</td>
<td>Document Total</td>
<td>15N</td>
<td>VAR</td>
<td>Total unsigned line amounts. Decimal point- two places</td>
</tr>
<tr class="odd">
<td>29</td>
<td>Fund</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>30</td>
<td>Document Type</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>31</td>
<td>Document Description</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>32</td>
<td>Vendor Name</td>
<td>30A</td>
<td>VAR</td>
<td>Station name</td>
</tr>
<tr class="odd">
<td>33</td>
<td>Vend Address Line1</td>
<td>30A</td>
<td>VAR</td>
<td>Station address 1</td>
</tr>
<tr class="even">
<td>34</td>
<td>Vend Address Line2</td>
<td>30A</td>
<td>VAR</td>
<td>Station address 2</td>
</tr>
<tr class="odd">
<td>35</td>
<td>Vend City</td>
<td>19A</td>
<td>VAR</td>
<td>Station city</td>
</tr>
<tr class="even">
<td>36</td>
<td>Vend State Code</td>
<td>2A</td>
<td>VAR</td>
<td>Station state</td>
</tr>
<tr class="odd">
<td>37</td>
<td>Vend Zip 1</td>
<td>5A</td>
<td>VAR</td>
<td>Station zip 1</td>
</tr>
<tr class="even">
<td>38</td>
<td>Vend Zip 2</td>
<td>4A</td>
<td>VAR</td>
<td>Station zip 2</td>
</tr>
<tr class="odd">
<td>39</td>
<td>Bill Print Flag</td>
<td>N</td>
<td>HC</td>
<td>Never printed from FMS</td>
</tr>
<tr class="even">
<td>40</td>
<td>Collected Due YY</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>41</td>
<td>Collected Due MM</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>42</td>
<td>Collected Due DD</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>43</td>
<td>Interest Rate</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>44</td>
<td>Text Type</td>
<td>null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>45</td>
<td>Waiver Flag</td>
<td>A</td>
<td>HC</td>
<td>All charges waived</td>
</tr>
</tbody>
</table>

<span id="_Toc67391168" class="anchor"></span>Table 41: BD Line Segments

<table>
<caption><p><span id="_Toc67391169" class="anchor"></span>Table 42: BD Control Segment</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Field Name</th>
<th>Value</th>
<th>Value Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>LIN</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Segment ID</td>
<td>BDA</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>3</td>
<td>Line No</td>
<td>001</td>
<td>HC</td>
<td>Each payment will generate a separate document. SAME AS ORIGINAL</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Line Beg Budget FY</td>
<td>Null</td>
<td>HC</td>
<td>Fiscal year beginning</td>
</tr>
<tr class="even">
<td>5</td>
<td>Line End Budget FY</td>
<td>Null</td>
<td>HC</td>
<td>Fiscal year ending</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Line Fund</td>
<td>6A</td>
<td>VAR</td>
<td>Fund</td>
</tr>
<tr class="even">
<td>7</td>
<td>XOrganization</td>
<td><p>Null</p>
<p>*7A</p></td>
<td>VAR</td>
<td>*If spending station required, infer from station field in control point table</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Sat Station</td>
<td><p>Null</p>
<p>*2A</p></td>
<td>VAR</td>
<td>*If spending substation required, prompt user for information</td>
</tr>
<tr class="even">
<td>9</td>
<td>XProgram</td>
<td><p>Null</p>
<p>*9A</p></td>
<td>VAR</td>
<td>*If spending OCP required, infer from OCP field in control point table</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Revenue Source</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>Sub Rev Source</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>12</td>
<td>Budget Object Code</td>
<td><p>Null</p>
<p>*4A</p></td>
<td>VAR</td>
<td>*If spending BOC required, prompt user for information</td>
</tr>
<tr class="even">
<td>13</td>
<td>Sub BOC</td>
<td><p>Null</p>
<p>*2A</p></td>
<td>VAR</td>
<td>*If spending sub-BOC required, prompt user for information</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Job Number</td>
<td><p>Null</p>
<p>*8A</p></td>
<td>VAR</td>
<td>*If spending job required, infer from job field in control point table</td>
</tr>
<tr class="even">
<td>15</td>
<td>Report Category</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>GL Account</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>Line Amount</td>
<td>15N</td>
<td>VAR</td>
<td>Bill amount or transaction amount</td>
</tr>
<tr class="odd">
<td>18</td>
<td>Incr/Decr Indicator</td>
<td>1A</td>
<td>VAR</td>
<td><p>I for increase or original entry</p>
<p>D for decrease</p></td>
</tr>
<tr class="even">
<td>19</td>
<td>Line Description</td>
<td>*</td>
<td>HC</td>
<td>*AR_INTERFACE</td>
</tr>
<tr class="odd">
<td>20</td>
<td>Ref Trans Code</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>21</td>
<td>Ref Trans Line</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>22</td>
<td>Line Trans Type</td>
<td></td>
<td>HC</td>
<td>Refund receivable</td>
</tr>
<tr class="even">
<td>23</td>
<td>Text Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>24</td>
<td>Interest Rate</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td>Travel Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>26</td>
<td>Travel Advance Numb</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>27</td>
<td>Source of Overpayment</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>28</td>
<td>Overpayment Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>29</td>
<td>Action Out</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>30</td>
<td>Cost Center</td>
<td><p>Null</p>
<p>*7A</p></td>
<td>VAR</td>
<td>*If spending cost center required, infer from first four characters of the IFCAP cost center code + 00</td>
</tr>
<tr class="even">
<td>31</td>
<td>Cost Sat Station</td>
<td><p>Null</p>
<p>*7A</p></td>
<td>VAR</td>
<td>*If spending sub cost center required, infer last two characters of the IFCAP cost center code</td>
</tr>
</tbody>
</table>

<span id="_Toc67391169" class="anchor"></span>Table 42: BD Control Segment

6.  BILLING (BD) DOCUMENT- REIMBURSEMENT

| \#  | Field Name          | Value | Value Status | Description                                         |
|-----|---------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID          | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System       | ARS   | HC           | Source system identification                        |
| 3   | Destination System  | FMS   | HC           | Destination system identification                   |
| 4   | Submitting Stations | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class   | DOC   | HC           | Document transaction                                |
| 6   | Transaction Code    | BD    | HC           | Transaction code                                    |
| 7   | Sec1 Code           | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 8   | Batch Number        | null  | HC           |                                                     |
| 9   | Transaction Number  | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date    | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time    | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number     | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total      | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version             | 3N    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391170" class="anchor"></span>Table 43: BD Batch Segment

| \#  | Field Name      | Value | Value Status | Description        |
|-----|-----------------|-------|--------------|--------------------|
| 1   | Segment ID      | BAT   | HC           | Segment Identifier |
|     |                 |       |              |                    |
| 1   | Segment ID      | BD0   | HC           | Segment Identifier |
| 2   | Batch Number    | 6A    | VAR          | Batch \#           |
| 3   | Net             | null  | HC           |                    |
| 4   | Batch Month     | null  | HC           |                    |
| 5   | Batch Day       | null  | HC           |                    |
| 6   | Batch Year      | null  | HC           |                    |
| 7   | Batch CTL Count | null  | HC           |                    |

<span id="_Toc67391171" class="anchor"></span>Table 44: BD Document Segment

<table>
<caption><p><span id="_Toc67391172" class="anchor"></span>Table 45: BD Line Segments</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Field Name</th>
<th>Value</th>
<th>Value Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>DOC</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Segment ID</td>
<td>BD1</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>3</td>
<td>Trans code</td>
<td>BD</td>
<td>HC</td>
<td>BD indicates a Billing document</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Trans Number</td>
<td>11A</td>
<td>VAR</td>
<td><p>Station(3) + Fiscal Year(1) + K + Sequential(5) + 0</p>
<p>Accounts Receivable bill number</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Header XDivision</td>
<td>4A</td>
<td>HC</td>
<td>VHA = 10, VBA = 20</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>Segment ID</td>
<td>BD2</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Record Month</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction month</td>
</tr>
<tr class="even">
<td>8</td>
<td>Record Day</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction day</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Record Year</td>
<td>2N</td>
<td>VAR</td>
<td>Transaction year</td>
</tr>
<tr class="even">
<td>10</td>
<td>Fisc Month</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Fisc Year</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>Acctg Trans Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Beg Budget FY</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>End Budget FY</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>15</td>
<td>Document Action</td>
<td>E</td>
<td>HC</td>
<td><p>E is for original entry document</p>
<p>M is for modification document</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>Vendor ID</td>
<td>Null</td>
<td>HC</td>
<td><p>Vendor code: vendors, MISCE: employees, persons</p>
<p>MISCN: insurance company, institutions, (non fed.)</p>
<p>MISCG: (federal)</p>
<p>MISCVET: patients</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Vendor Address Code</td>
<td>2A</td>
<td>VAR</td>
<td>FMS vendor code (suffix)</td>
</tr>
<tr class="even">
<td>28</td>
<td>Document Total</td>
<td>15N</td>
<td>VAR</td>
<td>Total unsigned line amounts. Decimal point- two places</td>
</tr>
<tr class="odd">
<td>29</td>
<td>Fund</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>30</td>
<td>Document Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>31</td>
<td>Document Description</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>32</td>
<td>Vendor Name</td>
<td>30A</td>
<td>VAR</td>
<td>Station name</td>
</tr>
<tr class="odd">
<td>33</td>
<td>Vend Address Line1</td>
<td>30A</td>
<td>VAR</td>
<td>Station address 1</td>
</tr>
<tr class="even">
<td>34</td>
<td>Vend Address Line2</td>
<td>30A</td>
<td>VAR</td>
<td>Station address 2</td>
</tr>
<tr class="odd">
<td>35</td>
<td>Vend City</td>
<td>19A</td>
<td>VAR</td>
<td>Station city</td>
</tr>
<tr class="even">
<td>36</td>
<td>Vend State Code</td>
<td>2A</td>
<td>VAR</td>
<td>Station state</td>
</tr>
<tr class="odd">
<td>37</td>
<td>Vend Zip 1</td>
<td>5A</td>
<td>VAR</td>
<td>Station zip 1</td>
</tr>
<tr class="even">
<td>38</td>
<td>Vend Zip 2</td>
<td>4A</td>
<td>VAR</td>
<td>Station zip 2</td>
</tr>
<tr class="odd">
<td>39</td>
<td>Bill Print Flag</td>
<td>N</td>
<td>HC</td>
<td>Never printed from FMS</td>
</tr>
<tr class="even">
<td>40</td>
<td>Collected Due YY</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>41</td>
<td>Collected Due MM</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>42</td>
<td>Collected Due DD</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>43</td>
<td>Interest Rate</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>44</td>
<td>Text Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>45</td>
<td>Waiver Flag</td>
<td>A</td>
<td>HC</td>
<td>All charges waived</td>
</tr>
</tbody>
</table>

<span id="_Toc67391172" class="anchor"></span>Table 45: BD Line Segments

<table>
<caption><p><span id="_Toc67391173" class="anchor"></span>Table 46: Confirmation Document Control Segment</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Field Name</th>
<th>Value</th>
<th>Value Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Segment ID</td>
<td>LIN</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Segment ID</td>
<td>BDA</td>
<td>HC</td>
<td>Segment identifier</td>
</tr>
<tr class="even">
<td>3</td>
<td>Line No</td>
<td>001</td>
<td>HC</td>
<td>Each payment will generate a separate document. SAME AS ORIGINAL</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Line Beg Budget FY</td>
<td>Null</td>
<td>HC</td>
<td>Fiscal year beginning</td>
</tr>
<tr class="even">
<td>5</td>
<td>Line End Budget FY</td>
<td>Null</td>
<td>HC</td>
<td>Fiscal year ending</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Line Fund</td>
<td>6A</td>
<td>VAR</td>
<td>Fund</td>
</tr>
<tr class="even">
<td>7</td>
<td>XOrganization</td>
<td><p>Null</p>
<p>*7A</p></td>
<td>VAR</td>
<td>*If revenue station required, prompt user for information</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Sat Station</td>
<td><p>Null</p>
<p>2A</p></td>
<td>VAR</td>
<td>*If revenue substation required, prompt user for information</td>
</tr>
<tr class="even">
<td>9</td>
<td>XProgram</td>
<td><p>Null</p>
<p>*9A</p></td>
<td>VAR</td>
<td>*If revenue OCP required, prompt user for information</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Revenue Source</td>
<td><p>Null</p>
<p>*ARRV</p></td>
<td>VAR</td>
<td>*If revenue source required, hard code ARRV</td>
</tr>
<tr class="even">
<td>11</td>
<td>Sub Rev Source</td>
<td><p>Null</p>
<p>*4A</p></td>
<td>VAR</td>
<td>*If sub-revenue source required, prompt user for information</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Budget Object Code</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>Sub BOC</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>14</td>
<td>Job Number</td>
<td><p>Null</p>
<p>*8A</p></td>
<td>VAR</td>
<td>*If job required, prompt user for information</td>
</tr>
<tr class="even">
<td>15</td>
<td>Report Category</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>GL Account</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>Line Amount</td>
<td>15N</td>
<td>VAR</td>
<td>Bill amount or transaction amount</td>
</tr>
<tr class="odd">
<td>18</td>
<td>Incr/Decr Indicator</td>
<td>1A</td>
<td>VAR</td>
<td><p>I for increase</p>
<p>D for decrease</p></td>
</tr>
<tr class="even">
<td>19</td>
<td>Line Description</td>
<td>*</td>
<td>HC</td>
<td>*AR_INTERFACE</td>
</tr>
<tr class="odd">
<td>20</td>
<td>Ref Trans Code</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>21</td>
<td>Ref Trans Line</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>22</td>
<td>Line Trans Type</td>
<td>02</td>
<td>HC</td>
<td>Reimbursement receivable</td>
</tr>
<tr class="even">
<td>23</td>
<td>Text Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>24</td>
<td>Interest Rate</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td>Travel Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>26</td>
<td>Travel Advance Numb</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>27</td>
<td>Source of Overpayment</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>28</td>
<td>Overpayment Type</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>28</td>
<td>Action Out</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="odd">
<td>29</td>
<td>Action Out</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
<tr class="even">
<td>30</td>
<td>Cost Center</td>
<td>Null</td>
<td>HC</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc67391173" class="anchor"></span>Table 46: Confirmation Document Control Segment

7.  CONFIRMATION DOCUMENT

| \#  | Field Name         | Value | Value Status | Description                                         |
|-----|--------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID         | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System      | FMS   | HC           | Source system identification                        |
| 3   | Destination System | ARS   | HC           | Destination system identification                   |
| 4   | Submitting Station | 3A    |              | IFCAP Station                                       |
| 5   | Transaction Class  | DCT   | HC           | Document Confirmation Transaction                   |
| 6   | Transaction Code   | 2A    |              | Transaction code                                    |
| 7   | Sec1 Code          | 4A    | HC           | VHA = 10, VBA = 20                                  |
| 8   | Batch Number       | null  | HC           |                                                     |
| 9   | Transaction Number | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date   | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time   | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number    | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total     | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version            | 3A    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391174" class="anchor"></span>Table 47: Confirmation Document Batch Segment

| \#  | Field Name     | Value  | Value Status | Description                |
|-----|----------------|--------|--------------|----------------------------|
| 1   | Segment ID     | BAT    | HC           | Segment identifier         |
|     |                |        |              |                            |
| 2   | Segment ID     | DCB    | HC           | Segment identifier         |
| 3   | Station        | 3A     | VAR          | Station                    |
| 4   | Status         | A or R | VAR          | A = Accepted, R = Rejected |
| 5   | User ID        | 6A     | VAR          | User identification        |
| 6   | Batch Number   | 6A     | VAR          |                            |
| 7   | ERR Code 1     | 5A     | VAR          | First error code           |
| 8   | ERR Message 1  | 30A    | VAR          | First error message        |
| 9   | ERR Code 2     | 5A     | VAR          | Second error code          |
| 10  | ERR Message 2  | 30A    | VAR          | Second error message       |
| 11  | ERR Code 3     | 5A     | VAR          |                            |
| 12  | ERR Message 3  | 30A    | VAR          |                            |
| 13  | ERR Code 4     | 5A     | VAR          |                            |
| 14  | ERR Message 4  | 30A    | VAR          |                            |
| 15  | ERR Code 5     | 5A     | VAR          |                            |
| 16  | ERR Message 5  | 30A    | VAR          |                            |
| 17  | ERR Code 6     | 5A     | VAR          |                            |
| 18  | ERR Message 6  | 30A    | VAR          |                            |
| 19  | ERR Code 7     | 5A     | VAR          |                            |
| 20  | ERR Message 7  | 30A    | VAR          |                            |
| 21  | ERR Code 8     | 5A     | VAR          |                            |
| 22  | ERR Message 8  | 30A    | VAR          |                            |
| 23  | ERR Code 9     | 5A     | VAR          |                            |
| 24  | ERR Message 9  | 30A    | VAR          |                            |
| 25  | ERR Code 10    | 5A     | VAR          |                            |
| 26  | ERR Message 10 | 30A    | VAR          |                            |

<span id="_Toc67391175" class="anchor"></span>Table 48: Confirmation Document Segments

| \#  | Field Name                  | Value  | Value Status | Description                 |
|-----|-----------------------------|--------|--------------|-----------------------------|
| 1   | Segment ID                  | DOC    | HC           | Segment identifier          |
|     |                             |        |              |                             |
| 2   | Segment ID                  | DCD    | HC           | Segment identifier          |
| 3   | Station                     | 3A     | VAR          | Station                     |
| 4   | Status                      | A or R | VAR          | A = Accepted, R = Rejected  |
| 5   | User ID                     | 6A     | VAR          | User identification         |
| 6   | Sec1 Code                   | 4A     | VAR          | VHA = 10, VBA = 20          |
| 7   | Transaction Code            | 2A     | VAR          | Transaction code            |
| 8   | Transaction Document Number | 11A    | VAR          | Transaction document number |
| 9   | ERR Code 1                  | 5A     | VAR          | First error code            |
| 10  | ERR Message 1               | 30A    | VAR          | First error message         |
| 11  | ERR Code 2                  | 5A     | VAR          | Second error code           |
| 12  | ERR Message 2               | 30A    | VAR          | Second error message        |
| 13  | ERR Code 3                  | 5A     | VAR          |                             |
| 14  | ERR Message 3               | 30A    | VAR          |                             |
| 15  | ERR Code 4                  | 5A     | VAR          |                             |
| 16  | ERR Message 4               | 30A    | VAR          |                             |
| 17  | ERR Code 5                  | 5A     | VAR          |                             |
| 18  | ERR Message 5               | 30A    | VAR          |                             |
| 19  | ERR Code 6                  | 5A     | VAR          |                             |
| 20  | ERR Message 6               | 30A    | VAR          |                             |
| 21  | ERR Code 7                  | 5A     | VAR          |                             |
| 22  | ERR Message 7               | 30A    | VAR          |                             |
| 23  | ERR Code 8                  | 5A     | VAR          |                             |
| 24  | ERR Message 8               | 30A    | VAR          |                             |
| 25  | ERR Code 9                  | 5A     | VAR          |                             |
| 26  | ERR Message 9               | 30A    | VAR          |                             |
| 27  | ERR Code 10                 | 5A     | VAR          |                             |
| 28  | ERR Message 10              | 30A    | VAR          |                             |

<span id="_Toc67391176" class="anchor"></span>Table 49: Confirmation Document Line Segments

| \#  | Field Name     | Value | Value Status | Description          |
|-----|----------------|-------|--------------|----------------------|
| 1   | Segment ID     | LIN   | HC           | Segment identifier   |
|     |                |       |              |                      |
| 2   | Segment ID     | DCL   | HC           | Segment identifier   |
| 3   | Station        | 3A    | VAR          | Station              |
| 4   | User ID        | 6A    | VAR          | User identification  |
| 5   | Line No        | 3A    | VAR          | 001-999              |
| 6   | ERR Code 1     | 5A    | VAR          | First error code     |
| 7   | ERR Message 1  | 30A   | VAR          | First error message  |
| 8   | ERR Code 2     | 5A    | VAR          | Second error code    |
| 9   | ERR Message 2  | 30A   | VAR          | Second error message |
| 10  | ERR Code 3     | 5A    | VAR          |                      |
| 11  | ERR Message 3  | 30A   | VAR          |                      |
| 12  | ERR Code 4     | 5A    | VAR          |                      |
| 13  | ERR Message 4  | 30A   | VAR          |                      |
| 14  | ERR Code 5     | 5A    | VAR          |                      |
| 15  | ERR Message 5  | 30A   | VAR          |                      |
| 16  | ERR Code 6     | 5A    | VAR          |                      |
| 17  | ERR Message 6  | 30A   | VAR          |                      |
| 18  | ERR Code 7     | 5A    | VAR          |                      |
| 19  | ERR Message 7  | 30A   | VAR          |                      |
| 20  | ERR Code 8     | 5A    | VAR          |                      |
| 21  | ERR Message 8  | 30A   | VAR          |                      |
| 22  | ERR Code 9     | 5A    | VAR          |                      |
| 23  | ERR Message 9  | 30A   | VAR          |                      |
| 24  | ERR Code 10    | 5A    | VAR          |                      |
| 25  | ERR Message 10 | 30A   | VAR          |                      |

<span id="_Toc67391177" class="anchor"></span>Table 50: Reconciliation Document Control Segment

8.  RECONCILIATION DOCUMENT

| \#  | Field Name         | Value | Value Status | Description                                         |
|-----|--------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID         | CTL   | HC           | Segment Identifier                                  |
| 2   | Source System      | FMS   | HC           | Source system identification                        |
| 3   | Destination System | ARS   | HC           | Destination system identification                   |
| 4   | Submitting Station | 3A    | VAR          | IFCAP Station                                       |
| 5   | Transaction Class  | OBR   | HC           | Outstanding Bill Reconciliation Statement           |
| 6   | Transaction Code   | Null  | HC           |                                                     |
| 7   | Sec1 Code          | Null  | HC           |                                                     |
| 8   | Batch Number       | Null  | HC           |                                                     |
| 9   | Transaction Number | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 10  | Transaction Date   | 8N    | VAR          | Calendar date document created (YYYYMMDD)           |
| 11  | Transaction Time   | 6N    | VAR          | Time document created (HHMMSS)                      |
| 12  | Sequence Number    | 3N    | VAR          | Transaction part Sequence Number of Sequence Total  |
| 13  | Sequence Total     | 3N    | VAR          | Total number of transaction parts                   |
| 14  | Version            | 3A    | VAR          | IFCAP-FMS Interface Version                         |

<span id="_Toc67391178" class="anchor"></span>Table 51: Reconciliation Document Line Segments

| \#  | Field Name         | Value | Value Status | Description                                         |
|-----|--------------------|-------|--------------|-----------------------------------------------------|
| 1   | Segment ID         | OBR   | HC           | Segment Identifier                                  |
| 2   | Station            | 3A    | HC           | Station \#                                          |
| 6   | Transaction Code   | 2A    | VAR          | Transaction code                                    |
| 9   | Transaction Number | 11A   | VAR          | Station(3) + Fiscal Year(1) + K + Sequential(5) + 0 |
| 13  | Line No            | 3N    | VAR          | 001-999                                             |
| 14  | Line Amount        | 17N   | VAR          | Outstanding dollar amount for the line              |

<span id="_Toc67391179" class="anchor"></span>Table 52: MDA – Medicare Deductible Alert \[SEQ 1\]

| Piece | Description               | Maximum Length/Type | Comments                                     |
|-------|---------------------------|---------------------|----------------------------------------------|
| 1     | RECORD ID = ‘MDA ’        | 4 ALPHA             | None.                                        |
| 2     | Medicare Type             | 1 Alpha             | Always equal to “A” for Part A               |
| 3     | HICN                      | 19 ALPHANUM         | Medicare assigned member ID number.          |
| 4     | Claim year                | 4 NUM               | Year the claim deductible is applied against |
| 5     | Patient account number    | 11 ALPHANUM         | Claim tracking number assigned by the VA     |
| 6     | DCN                       | 25 ALPHANUM         | Document Control Number for VA claim         |
| 7     | Cash deductible submitted | 6 NUM               |                                              |
| 8     | Cash deductible available | 6 NUM               |                                              |
| 9     | Service start date        | 8 NUM               | CCYYMMDD                                     |
| 10    | Service end date          | 8 NUM               | CCYYMMDD                                     |
| 11    | Report date               | 8 NUM               | Date report created by Medicare              |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Account</u>
Records established for an individual debtor in the AR Debtor file. One account can have any number of bills, just as a VISA or Master Card account can be used for multiple purchases.
<u>Accounting Classification Code (ACC)</u>
Nine-character codes used for budget purposes. The FMS ACC’s replace CALM Fund Control Points.
<u>Accounting Technician</u>
The person in Fiscal Service who is responsible for processing accounting transactions.
<u>Account Profile</u>
A screen display or printout showing a summary of activity on an entire Accounts Receivable (refer to Transaction Profile for a view of a single transaction on an account).
<u>Accounts Receivable</u>
In the broadest sense, these are debts owed to the Department of Veterans Affairs. Throughout the documentation, this term is used interchangeably with the term "bills" for ease of expression. The Accounts Receivable section of Fiscal Service is that person or group of people whose duty it is to establish and maintain debtor account records.
<u>Accounts Receivable Clerk</u>
The person in Fiscal who establishes, audits, and maintains the station's debt collection files.
<u>Adjustment</u>
A transaction that makes an administrative change to the principal balance of a Bill or an account.
<u>Admin Charge</u>
An administrative charge incurred during the debt collection process and added to an account's principal balance. Fees for locator searches, marshal fees, and court costs are administrative charges.
<u>Agent Cashier</u>
The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.
<u>ADP Security Officer</u>
The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing who has access to which files.
<u>AMIS</u>
Automated Management Information System.
<u>AITC</u>
Austin Information Technology Center
<u>Application Coordinator</u>
The individuals responsible for the implementation, training and troubleshooting of the AR software package.
<u>AR Event File</u>
This file contains events that occurred to a debtor's account.
<u>Batch Number (this is not the FMS batch number)</u>
The number assigned to an Agent Cashier batch payment.
<u>Bill</u>
A receivable that has been generated by a billing service or section. See the Bill types 1080, 1081, 1114, or UB-82.
<u>Bill for Collection</u>
The actual Bill produced by an 1114 type billing. Formerly the second (carbon copy) page of the preprinted Form 1114 — now only accessible to the Accounts Receivable Section as an electronic Bill.
<u>Billing Clerk</u>
That person in a billing service or section that is responsible for generating bills.
<u>Billing Cycle</u>
The life cycle of a Bill. From generation through approval, transmission to AR, mailing to the debtor, and being liquidated by posted payments until the debt has been paid.
<u>Bill Number</u>
Each Bill has a unique number, tracked by service/section, which is used to identify it. It is usually assigned automatically by the system (see Common Bill Numbering Series).
<u>Billing Document (BD)</u>
An Accounts Receivable document created by using the Billing module in the AR system: an SF-1080 or and OF-1114.
<u>Budget Object Code (BOC)</u>
Four-digit number used to identify purchases. The FMS BOC’s are equivalent to CALM subaccounts.
<u>Cash Receipt (CR)</u>
An Accounts Receivable document used to record deposit information from the SF-215 Deposit Ticket into FMS.
<u>Category C (Hospital Care)</u>
Entitlement category for inpatient care in a VA Medical Center; non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.
<u>Category C (Nursing Home Care)</u>
Entitlement category for long-term care in a VA Nursing Home; non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.
<u>Category C (Outpatient Care)</u>
Entitlement category for outpatient care at a VA Medical Center; non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.
<u>CCPC</u>
Consolidated Copayment Processing Center
<u>Common Bill Numbering Series</u>
A series of numbers set aside for each billing service/section; the system uses this series to assign Bill numbers automatically whenever the billing clerk needs to generate a new Bill.
<u>Common Numbering Series</u>
Numbers used by Accounting Technicians to generate new accounting transactions for AR. The Application Coordinators will establish the Common Numbering Series used by your facility.
<u>Correction</u>
A change made to a billing record before the initial Bill is generated.
<u>COWC</u>
The Committee on Waivers and Compromise. An appellate body located in The Department of Veterans Affairs Veterans Benefits Administration Regional Offices.
<u>Credit</u>
A payment which, when posted to an account, reduces the principal balance (the debt). Scheduled payments under a repayment plan are credits.
<u>Crime of Personal Violence</u>
The result of a crime of personal violence; occurs in a state where the victim is entitled to receive health care and services at the expense of the state or a political subdivision. Billings are forwarded to the District Counsel for collection.
<u>Cross-Servicing</u>
The Cross-Servicing functionality was delivered and integrated under the VistA AR 4.5 patch, PRCA\*4.5\*301. This new functionality will allow VHA to refer a debt that has been delinquent 120 days or more to Treasury for collection.
<u>DC</u>
The Department of Veterans Affairs' Office of the District Counsel. District Counsel areas of responsibility do not correspond to the Veterans Health Service and Research Administration regions.
<u>Debit</u>
A charge or fee which when posted to an account increases the principal balance (the debt). Interest and administrative charges are debits.
<u>Debt Collection</u>
This is the official name given to the process of sending out bills and collecting payments.
<u>Debtor</u>
A patient, person, vendor, insurance company, or institution who owes the VA money.
<u>Default</u>
A normal or suggested response that is provided by the system.
<u>Demand Letter</u>
The follow-up letters that are sent to a debtor, reminding them of the outstanding debt are called demand letters.
<u>DOJ</u>
The United States Department of Justice.
<u>Electronic Signature</u>
The electronic signature replaces the written signature on all AR documents used within your facility. Documents going off-station will require a written signature as well. The electronic signature code is used by all individuals who have the authority to approve actions (approve requests, purchase orders, obligations, etc.). The electronic signature is encrypted so that no one, not even a computer programmer, can tell what it is.
<u>Federal Tax ID</u>
A unique number that identifies your station to the Internal Revenue Service.
<u>FL 4-480</u>
The first demand letter for Ineligible category debtors.
<u>FL 4-481</u>
The first demand letter for Humanitarian category debtors.
<u>FL 4-482</u>
The second demand letter for Ineligible, Humanitarian and Category C debtors.
<u>FL 4-483</u>
The third demand letter for debts under \$200 for medical care.
<u>FL 4-484</u>
The third demand letter for debts between \$200 and \$1200 for medical care.
<u>FL 4-485</u>
The third demand letter for debts over \$1200 for medical care.
<u>FL 4-513</u>
The first demand for Category C (Means Test) debts.
<u>FMS</u>
Financial Management System which handles all centralized accounting and has replaced the CALM system.
<u>FMS Document ID (DOC ID)</u>
The station number + a unique document number. Formerly called the CALM PAT number.
<u>GL</u>
The General Ledger to which all accounting transactions are posted.
<u>Hold</u>
A hold is a temporary restriction placed on mailing demand letters for a particular account. It is usually used when a debtor has made arrangements to pay the debt and letters would be redundant.
<u>Humanitarian</u>
Humanitarian billings are for non-veterans treated at a VA facility for a medical emergency. Also includes veterans treated under presumed eligibility later found to be ineligible.
<u>ICD</u>
Interest Computation Date. Usually the date of the first demand letter. (NOTE: Do not confuse this with the International Classification of Disease codes—usually referred to as the ICD-9 Codes.)
<u>Ineligible</u>
Ineligibles are veterans who have received medical care at a VA facility, but were later found not entitled to such service.
<u>Integrated Billing</u>
Integrated Billing (IB) is a software package that acts as an interface between the service that establishes a debt and the billing process in AR.
<u>Invoice Address</u>
The address printed on a purchase order to instruct the vendor where to mail his/her invoice.
<u>Insurance Company File</u>
File Number 36 holds information about the insurance companies that your station does business with. Debtor's address may be drawn from this file but is maintained separately. If the desired company is not in the file, contact MAS to have it added.
<u>Interest</u>
Amount charged to an account being paid on a repayment plan for carrying the account or on delinquent accounts.
<u>National Roll-Up</u>
The National Roll-Up software includes a central database to reside at the San Francisco ISC and interface software to reside at each field station. The interface software collects Accounts Receivable data from AR Version 4.5 and sends this data to the central database. The ISC will then process the AR data collected to centrally produce, for all sites, the VA Schedule 9 Report for the U.S. Treasury.
<u>No-fault Auto Accident</u>
Used for medical care required as the result of a motor vehicle accident in a state this has no-fault automobile insurance.
<u>OFM</u>
Office of Financial Management.
<u>Overpayment Document (OP)</u>
FMS document used to create manual refunds to veterans and insurance companies. Formerly a 972.13 CALM code sheet.
<u>PAT Number</u>
Formerly, a unique number used to identify a CALM document. FMS DOC ID replaces the CALM PAT.
<u>Patient Statement of Account</u>
The monthly statement for patient type debtors, reflecting all activity (both charges and payments) recorded for that patient since his last statement was printed.
<u>RCDP TCSP FLAG</u>
This security key allows users that are assigned to edit the TCSP flag on Debtor and/or Bill. This Security Key, RCDP TCSP FLAG, should ONLY be allocated by CPAC IT and given ONLY to Veteran Services Supervisors and/or Veteran Services Leads (One, Two or Three). Introduced with routine, RCDPCSA, in Accounts Receivable patch, PRCA\*4.5\*325.
<u>RD</u>
Regional Director.
<u>Referral Amount</u>
Threshold amounts that determine (often independently) which accounts are referred to the District Counsel or the Department of Justice.
<u>Repayment Plan</u>
If a debt is so large that the debtor can't repay it in a lump sum a Repayment Plan may be established to pay it in regularly scheduled installments. Can be established by the Fiscal Officer or as the result of negotiations with the District Counsel or Department of Justice.
<u>Schedule 9</u>
A detailed report of receivables due to the VA. It categorizes receivables by age and status. With the release of the National Roll-up software, Schedule 9 will be centrally produced in San Francisco.
<u>Site Parameters</u>
Information (such as station number, cashier's address, billing address, etc.) that is unique to your station. All of AR uses a single Site Parameter file.
<u>Tasked Job</u>
A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.
<u>Tort Feasor</u>
Used for medical care provided as the result of a crime. A type of billing in which a firm receivable is not recorded until it is paid.
<u>Transaction</u>
Any action that affects a Bill or an account. All transactions are numbered sequentially and can be examined individually.
<u>Transaction Number</u>
A number assigned by the computer for an activity against a debt (such as increase adjustment, decrease adjustment, payment, etc.)
<u>Transaction Profile</u>
A screen display or printout that shows a summary of a single transaction.
<u>UB-92</u>
Uniform Bill 92 is a statement of charges for medical care used for all patient billing. Its use is restricted to the IB portion of the Medical Administration automated system.
<u>VA Form 1080</u>
A billing form used to transfer funds from one government agency to another when a check will be issued.
<u>VA Form 1081</u>
A billing form used to Bill other government agencies.
<u>VA Form 1114</u>
This form has been discontinued and has been replaced by the electronic Bill of Collection.
<u>Vendor File</u>
An AR file of all the vendors the facility does business with. This file, File \#440, contains ordering and billing address, contract information, and telephone numbers. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added.
<u>Vendor ID Number</u>
The ID number assigned to a vendor.
<u>Workmen's Compensation</u>
Usually referred to as Worker's Comp. Medical care provided as a result of an incident/accident occurring during a veteran's employment and covered by the Office of Worker's Compensation Program (OWCP).
<u>Write-off Document (WR)</u>
FMS document created to record an Accounts Receivable write-off.
