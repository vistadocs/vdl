---
title: Accounts Receivable Version 4.5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
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
menu_options: 9
description: 
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - impact
  - processing
  - service
  - introduction
  - clerk
  - billing
  - transactions
page_count: 0
word_count: 471
section_count: 11
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/45releas.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/45releas.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

> Department of Veterans Affairs Decentralized Hospital Computer Program

ACCOUNTS RECEIVABLE RELEASE NOTES

> Version 4.5 March 1995

> Information Systems Center Washington, D.C.

[Introduction 1](#introduction)

[Overview 1](#introduction)

1.  [Impact on Accounting Technician 3](#impact-on-accounting-technician)
2.  [Impact on Clerk 7](#impact-on-clerk)

[Processing Refunds 7](#impact-on-clerk)

[Deposit Managemen.t 7](#Deposit_Management)

3.  [Impact on Superviso r 9](#impact-on-supervisor)

[Common Numbering Serie.s 9](#impact-on-supervisor)

4.  [Service Billing 11](#service-billing)

[Detail Receivables 11](#service-billing)

5.  [Reconciliation With FMS 13](#reconciliation-with-fms)
6.  [Confirmation 15](#confirmation)

> Revision History

> Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Description (Patch # if applic.)</p>
</blockquote></th>
<th><blockquote>
<p>Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Technical Writer</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192-</p>
<p>352 Displaying Sensitive Data.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Pdf file checked for accessibility to</p>
<p>readers with disabilities.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [OVERVIEW](#overview)
- [Impact on Accounting Technician](#impact-on-accounting-technician)
  - [ESTABLISHING A BILL](#establishing-a-bill)
  - [PROCESSING TRANSACTIONS](#processing-transactions)
  - [SUMMARY TRANSACTIONS](#summary-transactions)
  - [PAYMENT DEPOSITS (PROCESSING PAYMENTS)](#payment-deposits-processing-payments)
  - [AUDITOR PROCESSING](#auditor-processing)
- [Impact on Clerk](#impact-on-clerk)
  - [PROCESSING REFUNDS](#processing-refunds)
  - [DEPOSIT MANAGEMENT](#deposit-management)
- [Impact on Supervisor](#impact-on-supervisor)
  - [COMMON NUMBERING SERIES](#common-numbering-series)
- [Service Billing](#service-billing)
  - [DETAIL RECEIVABLES](#detail-receivables)
- [Reconciliation With FMS](#reconciliation-with-fms)
- [Confirmation](#confirmation)

## OVERVIEW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Accounts Receivable (AR) Version 4.0 system within the Department of Veteran Affairs previously had transmitted local transactions and receivables to the Centralized Accounting for Local Management System (CALM). The interface with the Financial Management System (FMS) improved upon CALM in the following ways.

> FMS provides a smooth, timely flow of data. Transactions between AR and CALM were initiated manually, causing unnecessary delay. This is particularly true in the process of Reconciliation. With the implementation of FMS, many of these processes, including Reconciliation, are automated. Automating these tasks allows fiscal personnel (Accounting Technicians) more time to focus on local accounting issues, prevents the proliferation of human error, and speeds up the overall process considerably.

> Using CALM had traditionally been a "one-way" procedure. Transactions were sent to CALM and the user who batched and sent them received a confirmation message that they were in fact received. FMS offers bi­ directional capabilities as part of its functionality. When transactions are sent to FMS, a confirmation message is generated as well as messages regarding the status of individual transactions. Status messages include, but are not limited to, errors in transmission and errors within the FMS documents themselves.

> CALM code sheets have been replaced by FMS "documents". These documents are the basis for sorting and sending specific types of transactions. This procedure simplifies the transmission of data and alleviates the unnecessary detail which is present in the current CALM system.

> Finally, with the advent of FMS, a more secure system has been created. Data integrity is a main concern in any accounting system, AR being no exception. The more a system is automated, the less chances that a "security" breach will occur.

> An unrelated enhancement, that of a Deposit Management menu, has also been added to AR V. 4.5 and will be discussed in the appropriate area of this manual.

> Introduction

# Impact on Accounting Technician

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ESTABLISHING A BILL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Establishing a bill begins when a service creates a new bill. Once created and approved, the bill is electronically sent to A/R. An A/R clerk audits<span id="_bookmark3" class="anchor"></span> the bill and edits the field ' Bill resulting from'. After auditing, the bill is electronically sent to accounting. In AR V. 4.0, the Accounting Technician used the option AR (New) Processing to edit GL and appropriation<span id="_bookmark2" class="anchor"></span> information, subsequently creating the CALM code sheet.

> With the integration of FMS the accounting process is eliminated. The FMS accounting line information is asked during the audit process. The Auditor is prompted for a control point, a sub-account and cost center.

> When the audit process is complete, AR builds the FMS Billing Document (BD) and passes the document to the DHCP-FMS transaction handler for transmission to Austin.

## PROCESSING TRANSACTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before AR V. 4.5, to process transactions on an active bill, the AR Clerk used the option 'Adjustment to Accounts Receivable', and adjusted the bill using an AR option. After the adjustment was complete, the AR system determined if the adjustment was to an RX copay or means test. If it was not an RX copay or means test, the adjustment was sent to Accounting for the creation of a CALM code sheet.

> With FMS, several changes occurred during bill adjustment. The following scenerio occurs when adjusting non-MCCR appropriations. Using AR options, the Accounts Receivable Clerk does an increase or decrease adjustment to an active bill. The system automatically creates a modified FMS Billing Document and sends the Billing Document to FMS eliminating the need for Accounting to create a code sheet.

## SUMMARY TRANSACTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the past, summary transactions were handled in the following manner. At the end of each month the Accounting Technician used the Accrual Totals Report option in the AR menu to generate totals for 2431 Means Tests and 5014 Pharmacy Co-Pays. The IFCAP package was then invoked using the option Create a Code Sheet, and the code sheet was constructed. Data was accessed manually and the appropriate AR records were inserted into the code sheet. Code sheets were then batched and transmission occurred.

> Impact on Accounting Technician

> Creation of code sheets is no longer necessary with the advent of FMS. A Standard Voucher (SV) document is sent to FMS which contains a summary of both 2431's and 5014's (an SV is sent for each). These documents are automatically generated as a result of the running of the National Roll Up each month. Since the National Roll Up routine that generates these documents is the same routine that extracts the data for the National Data Base (NDB), totals at FMS equal the totals at the National Data Base.

## PAYMENT DEPOSITS (PROCESSING PAYMENTS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With AR V. 4.0, the Agent Cashier received and entered each payment into the system. At the end of the day, the Agent Cashier reconciled the payments received with the amounts they had in their drawer using the Reconciliation report. The payments were posted to a patient account or an AR bill. An Accounting Technician then manually generated the 215 report using the "Print 215 Report" option in the Clerk’s menu. This report listed each collection, and it provided a summary list of total cash collected for each appropriation. An Accounting Technician used these reports to create the necessary CALM code sheets for the day. The accrued bills, such as pharmacy co-pay or a means test bill, were sent to Austin by creating a code sheet for a single transaction. However, if the bills are a third party reimbursable, CALM code sheets were done for the individual bills. Once the code sheets were created, they were then batched and transmitted to CALM.

> With the implementation of FMS, under the payment entry options for non-patient bills only, the AR software warns the user if the bill is not active or if the payment amount is greater than the bill amount. When the Agent Cashier approves a receipt that contains payments from suspense, the AR system will not transmit a Cash Receipt document. The Accounting Technician transfers money from suspense to the appropriate bill manually. Then, on the reconciliation report, three asterisks print by the bill number if the status of the bill is not active. Also, on the reconciliation report a warning is printed if the payment amount is greater than the bill amount for non-patient bills. If multiple payments are entered for the same bill and the payment amount is greater than the balance, a warning is printed. Finally, with the implementation of FMS, the Accounting Technicians no longer need to create code sheets once payments are received and posted to an account. Instead, the necessary data is automatically generated and passed to an interface, and the interface creates FMS documents. The type of document sent to FMS depends on whether the bills are accrued or detailed. For example, if the bills accrued are pharmacy co-pay or means test bills, data is automatically generated that is compatible with an FMS cash receipt

> Impact on Accounting Technician

> summary document. For detailed bills, such as vendor bills, data is automatically generated that is compatible with an FMS cash receipt detailed document. The data that is compatible to each specific document is passed to the interface. The interface software pieces the data segments together and creates the documents that are sent via mail messages to FMS.

## AUDITOR PROCESSING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During audit processing of new bills, the auditor will be asked for a Control point. If a Control point is *not* entered, a Reimbursement Billing Document will be created. If a Control Point *is* entered, the control point table will be check to determine if the control point is a supply fund. If the control point is not a supply fund control point, a Refund Billing Document will be created. If the control point is a supply fund, the auditor will be asked if the bill is to be processed as a Refund or Reimbursement, and subsequently, the appropriate billing document will be created.

> Impact on Accounting Technician

# Impact on Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PROCESSING REFUNDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Processing refunds under AR V. 4.0 was handled in the following manner: A payment was received from a patient and applied to the patient's account in which there were no outstanding bills. An initial review of the refund occurred, and an electronic signature was used to verify that the refund had passed this review. After the initial review, a final approval of the refund<span id="Deposit_Management" class="anchor"></span> was done by a second user, who then entered an electronic signature to approve the refund. Once the refund was approved, a code sheet was automatically created and passed to the Accounting Technician through the IFCAP package for processing in CALM as a 972.13 transaction to appropriation 5014. The accounting technician then processed and transmitted the code sheet to CALM in Austin, where a check was produced and sent to the patient. Once the refund had a code sheet completed, it appeared in the AR software in Refunded status and had a refunded transaction for the amount.

> In version 4.5, the process remains much the same as it was in AR V. 4.0; however, there are two significant changes in the process. The first change is in the way that the review of the refund is done. In the new version, the initial reviewer (auditor) is allowed to make increase or decrease adjustments to the bill *during* the review process which now asks the user if the amount of the refund needs to be adjusted. If the user answers 'Yes' ,the user is allowed to make either an increase or decrease transaction to the refund.

> This transaction remains on the bill even if there are data entry errors and these adjustments appear on the patient statement. Once the review is finished and all adjustments are made, the second auditor approves the refund. If any adjustments are made during the second review, the bill is no longer in approval-ready status. It will return to be reviewed by the first auditor and then needs to be approved again. It will remain in Refund Review status until it is approved by a second auditor. Once the refund is approved, no more adjustments can be made to it and it will be considered in Refunded status. Once in Refunded status, the bill is passed to FMS as a Payment Voucher (PV) document. There are no code sheets generated by the Accounting Technician and the document is not able to be edited. It is sent directly to FMS with all other FMS documents.

## DEPOSIT MANAGEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Deposit Management menu is located on the Agent Cashier’s main menu and accessible thus to the Clerks. This menu automates several formerly manual functions in relation to Deposit Tickets. New options allow the user

> Impact on Supervisor

> to automatically generate a new Deposit Ticket, deposit the money to the bank, edit an already existing Deposit Ticket, and void a Deposit Ticket. Several options have been included which allow the user to view various aspects of a Deposit Ticket and include the View a Deposit option, Summary Listing of Deposits, and an option which allows the user to view a receipt list for deposit. By automating these procedures, valuable time is being saved on the part of the Clerks and Agent Cashiers as well as making those fiscal procedures more secure and less susceptible to fraudulent activity.

# Impact on Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## COMMON NUMBERING SERIES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reference numbers were defined each year on-site by Fiscal Supervisors. These numbers were necessary in the CALM process. The number itself consisted of a three- digit site code, a letter code which designated it as AR, a one digit fiscal year indicator, and finally, a four- digit unique identifier. (e.g. 503-K40001) Accrued bills often possessed an arbitrary, locally generated letter code to identify the bill type, but detailed bills (e.g. Vendor bills) had to have a letter code which adhered to predefined guidelines.

> With the advent of V. 4.5, a number series is automatically generated which dispenses with the old manual process. An internally generated common number series which is more time efficient has been hard-coded. This will alleviate many errors in assigning the bill type indicator. The number consists of a three- digit site code, a “K” which designates it as an AR bill, a one- digit fiscal year indicator, and a five- character unique identifier. (e.g. 503-K400001) Additionally, new reporting capabilities have been added to allow financial managers to generate reports for specific billing categories.

> The unique identifier will be numeric if it is designating a transaction, and will begin with an alpha followed by four numerics if it is designating a bill.

> Impact on Supervisor

# Service Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DETAIL RECEIVABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Detail receivables consist of either refundables (monetary transactions including overpayments that can be collected and spent again) or reimbursables (funds which reflect a service rendered that can also be collected but not spent again per se).

> Detail Receivables

> Refund Reimbursement

(overpaid money) (provided care/service)

> Previously, a new bill was established by a service using the New Bill (Enter) option under the Billing menu. This bill was then approved using the Approve/Print Pending Bill option under the same menu. Fiscal service personnel used the Clerk’s menu options Audit/Set up a New Accounts Receivable and Audit an Electronic Bill to perform the audit process and then the bill went to the Accounting Technician. Using the AR (New) Processing option under the AR menu, the Accounting Technician entered the appropriation, general ledger, and other accounting information, thus creating a code sheet which, when sent to CALM, became an active receivable.

> Refund receivables are handled somewhat differently through FMS. When establishing a new bill, the user is prompted for a Control Point. Each service will have "screened" Control Points- meaning simply that they will have only the Control Points that are relevant to that service. The approval process remains basically the same with a few exceptions. The general ledger field is no longer present, and if a Control Point has not yet been assigned, the system will assume that the detail receivable is a reimbursement. In other words, if the detail receivable is a refund, this is the last chance to assign it a Control Point designating it as such before the system default assigns it's own Control Point. With this accomplished, the FMS Billing Document (BD) is automatically created and transmitted to FMS.

> Service Billing

# Reconciliation With FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In AR V. 4.0, CALM sent a reconciliation statement back to each site which was then manually compared with reconciliation reports that were generated through the Clerk’s menu- a tedious, time consuming task.

> In version 4.5, each detail Accounts Receivable transaction sent through the AR interface is processed in FMS. FMS creates a document which consists of billing information from the receivable (bill \#, dollar amount, etc.) and transmits it to each station as part of the monthly close cycle. The actual date that this report arrives at the site is no later than the day after the last day of the previous month; in other words, the first day of the current month. For example, the reconciliation report for the month of November should arrive at the site on December 1st. By having this information at the site immediately after the previous month’s cycle, all corrections can be made and no out-of-balance instances for that month will exist, leaving a “clean” month. This report is transmitted through E-Mail and does an automated reconciliation with the data at the site by comparing it to the billing information within each site’s database. A report is then generated that summarizes any and all discrepancies between what FMS received and what exists in the AR database. Three possible scenarios exist for reconciliation discrepancies: 1) if data exists within the AR database which is not present in the FMS system, 2) if data exists in the FMS system which is not present in the AR database, and finally, 3) the dollar amount on a transaction does not match between what is in the AR database and what has been reported by FMS.

> AR FMS

> <u>Condition 1</u>

> <u>Condition 3</u>

> <u>Condition 2</u>

> An option exists allowing the user to print this report for "hard copy" filing. Since data is extracted from each site for roll-up in the National Database, reconciliation with each site ensures that the database is in balance with

> Reconciliation with FMS

> FMS. This will significantly decrease discrepancies between the AR system at each site, the National Database, and FMS.

# Confirmation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before AR V. 4.5, CALM Code Sheets were processed at Austin, and an E- Mail message was generated and sent back to the user with a status of either Accepted or Rejected. If a transaction was rejected, it was accompanied by a number code which corresponded to the error condition or reason for rejection (i.e. improper vendor code = error \# 50). After the errors were corrected the user sent a new code sheet.

> Presently, each night, transactions sent through the outgoing AR/FMS interface are processed by the FMS system. At this time, an E-Mail message is sent for each FMS document to the site/user from FMS, with the status of each document. The message indicates that the documents have been either accepted or rejected. Rejected documents include error messages which allow the user to pinpoint the problem. The correction process involves creating a new document and resending this to FMS, and is done in a timely manner to prevent a potential out-of-balance situation between Austin, NDB, and the site.

> Confirmation