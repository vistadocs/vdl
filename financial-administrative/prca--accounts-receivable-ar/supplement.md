---
title: Accounts Receivable Version 4.5 Lockbox Training Guide
doc_type: TRG
doc_label: Training Guide
doc_layer: anchor
doc_subject: Lockbox
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
menu_options: 0
description: > This training guide shows how to use the Agent Cashier options released in Accounts Receivable patch PRCA\4.5\114. This patch supports the First Party Lockbox initiative.
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - colspan
  - payment
  - table
  - width
  - style
  - colgroup
  - thead
page_count: 0
word_count: 13839
section_count: 16
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/lockboxtrainingguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/lockboxtrainingguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

---
title: Lockbox Training Guide
---

![](accounts-receivable-version-4-5-lockbox-training-guide/001.png)

> Department of Veterans Affairs

> Revised September 2007

> Revised 09/07 Table of Contents ii

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This training guide shows how to use the Agent Cashier options released in Accounts Receivable patch PRCA\*4.5\*114. This patch supports the First Party Lockbox initiative.

> Accounts Receivable software was modified to be able to automatically post funds received by the Lockbox Bank, to a patients account. Some new processes were introduced, such as the ability to deposit funds to the Suspense Account 36F3875 and to Link Payments. These new processes required changes to the Agent Cashier’s Menu. Many options were removed and new options added. This training guide shows how to use these new Agent Cashier options.

> It is important to know that the information entered by cashiers when processing payments has not changed, just the screens used to enter the information. The Lockbox patch, PRCA\*4.5\*114, introduces the use of List Manager screens to make payment processing and accessing account information easier and faster.

> A new mail group called RCDP PAYMENTS was added with patch PRCA\*4.5\*114. The Accounts Receivable package uses this mail group to communicate with the agent cashiers and MCCR staff. Any problems with the automatic processing of payments, information regarding linking payments, receipt/deposit errors, and FMS Cash Receipt (CR) document reject messages will be delivered to the mail group. Make sure the appropriate users are added as members of this mail group when this patch is installed at your facility.

> Please read the Overview section to learn more about the components and activities related to the Lockbox project.

> BLANK PAGE

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Lockbox project implements a centralized collection point for processing patient payments. As usual, patients will be treated at their local VA facility. If appropriate, billing and collection information will be created and stored in V*IST*A’s Accounts Receivable (AR) software package. Each month, patient-billing information will be transmitted to the Consolidated Copayment Processing Center (CCPC) system located at the Austin Automation Center (AAC). The CCPC prints and mails billing statements to patients. Revised billing statements will instruct patients to mail their payments to the national Lockbox Bank. The Lockbox Bank will record payment information for each patient account and relay that information back to the CCPC-Lockbox system. At the same time, the Lockbox Bank will make a single, combined deposit and report the deposit amount to the U.S. Treasury. The payment information received by the CCPC- Lockbox system will be processed, verified and grouped by VA station number. Payment information will be transmitted nightly to each VA facility and to the Financial Management System (FMS) also located at the Austin Automation Center (AAC). AR will process the payment information and automatically apply payments to each specified patient account.

> The Lockbox project moves the mail-in payment processing from the local agent cashier to the Lockbox Bank and eliminates the associated manual data entry at the facility level. Of course, patients who wish to make payments in person can continue to do so.

> What is a Lockbox?

> A Lockbox is a centralized collection point for processing and depositing large volumes of payments. The collection center generally is close to a major mail-processing center to expedite the delivery of the mail. The Lockbox processes the mail and records the payments on a daily basis and a single deposit is made to the customers’ bank account. The deposits are made directly to a clearing bank and reported to Treasury at the same time. The funds are available in the customer’s account sooner than is possible using the existing manual process of depositing payments.

> The Lockbox receives mail deliveries from the post office 10 times a day and processes all mail on the day it is received (up to a specified cut-off time). By using specially coded envelopes to decrease the mail float and the expedited deposit process, the funds for a check can be in the VA’s account within three days of mailing.

> How will the Lockbox work for VA?

> On a daily basis the CCFC-Lockbox processes incoming payments and deposits the funds in the VA’s account. This deposit is recorded on-line in U.S. Treasury GOALS (an accounting system) with a pre-determined 215 number. Since the CCFC-Lockbox is the responsible party for the daily deposits they are also notified of any returned checks or credit vouchers or debit vouchers generated as a result of that deposit. This *exception* information is sent to the CCPC-Lockbox either electronically or in paper format for processing by the CCPC-Lockbox Exception Processing Section.

> If any correspondence is included with a payment, the Lockbox facility will forward these items on a daily basis to the CCPC-Lockbox Exception Processing Section for sorting and distribution to the medical centers.

> The remittance coupon on the outgoing patient statements has been designed to include the station and patient account number. During processing the Lockbox scans the account information for each payment and this enables the transmission records to include the account information. Once the payments are processed and deposited at the Lockbox site the data is summarized and transmitted to the CCPC-Lockbox. The data is verified, loaded in the database, and the receipts grouped by station number. Each night the payments are transmitted to their designated stations. AR systems at the hospitals receive the payment information via the MailMan system and automatically apply payments to the specified patient account based on an order of application.

> As is likely with any payment received via the mail, issues will arise as to where a specific payment is to be applied due to missing or incorrect account information. The CCPC-Lockbox Exception Processing Section can handle the majority of payments with missing account information. This group is responsible for identifying items that did not contain account information or where the account information was incomplete. They use supporting paper documentation provided by the Lockbox and automated tools provided within CCPC-Lockbox to identify these payments. This staff also has the initial responsibility for handling the return items, debit vouchers, and credit vouchers. Although the CCPC-Lockbox Exception Processing Section can handle most identification issues, items will still arrive at the medical centers that local personnel will need to research and determine the correct application of the item.

# ![](accounts-receivable-version-4-5-lockbox-training-guide/002.png)![](accounts-receivable-version-4-5-lockbox-training-guide/003.png)![](accounts-receivable-version-4-5-lockbox-training-guide/004.png)![](accounts-receivable-version-4-5-lockbox-training-guide/005.png)FMS/AAC


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Purpose](#purpose)
  - [Overview](#overview)
- [![](accounts-receivable-version-4-5-lockbox-training-guide/002.png)![](accounts-receivable-version-4-5-lockbox-training-guide/003.png)![](accounts-receivable-version-4-5-lockbox-training-guide/004.png)![](accounts-receivable-version-4-5-lockbox-training-guide/005.png)FMS/AAC](#accounts-receivable-version-4-5-lockbox-training-guide002pngaccounts-receivable-version-4-5-lockbox-training-guide003pngaccounts-receivable-version-4-5-lockbox-training-guide004pngaccounts-receivable-version-4-5-lockbox-training-guide005pngfmsaac)
- [Pat ients](#pat-ients)
  - [Getting Started](#getting-started)
  - [New Menu and the List Manager](#new-menu-and-the-list-manager)
  - [Deposit/Receipt/Payment Processing](#depositreceiptpayment-processing)
  - [Suspense Account](#suspense-account)
  - [Link Payment to Account](#link-payment-to-account)
  - [Exception Processing Due to Lockbox at the Station Level](#exception-processing-due-to-lockbox-at-the-station-level)
  - [Unlinked Payments Created by Lockbox Processing](#unlinked-payments-created-by-lockbox-processing)
  - [Profiles](#profiles)
  - [Reports](#reports)
  - [Appendix](#appendix)
  - [Sample Patient Statement and Mail Messages](#sample-patient-statement-and-mail-messages)
  - [Frequently Asked Questions](#frequently-asked-questions)
  - [Troubleshooting Tips](#troubleshooting-tips)
> Overview Lockbox System

# Pat ients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lockbox Bank

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> STEP 1: Select DP for opening up a deposit ticket.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Agent Cashier Menu Option:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DP Deposit Processing</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RP Receipt Processing</p>
<p>LP Link Payment To Account</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Deposit Processing screen will display.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 26%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Deposit Processing Jul 27, 1999 13:12:02 Page:</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Deposit #: 111111 Deposit Status: OPEN Deposit Date: JUL 27, 1999</p>
<p>Opened By: VALOCKBOX,ONE Date/Time Opened: JUL 27, 19</p>
<p>Confirmed By: Date/Time Confirmed:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>99 13:12</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Receipt Payment Type OpenDate By</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ProcDate By Count</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Total</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Paid</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>* No RECEIPTS for this deposit * TOTAL DOLLARS FOR DEPOSIT</p>
<p>Bank: Bank Trace Number: Agency Location Code:</p>
</blockquote>
<p>Agency Title:</p>
<blockquote>
<p>FMS CR Documents</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ED Edit Deposit AR Add Receipt</p>
<p>CD Confirm Deposit RP Receipt Profile</p>
<p>Select Action: Quit//<strong>AR Add Receipt</strong></p>
</blockquote></td>
<td><blockquote>
<p>CU Customize EA Exit Action</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

> STEP 2: Type AR to Add a new receipt.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Receipt Profile Jul 27, 1999 13:13:54 Page: 1 of 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receipt #: 11111111 Type of Payment: CASH PAYMENT</p>
<p>Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong># Account Pay Date By Pay Amt Proc Amt</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 0.00 0.00</p>
<p>Receipt History</p>
<p>Opened By: VALOCKBOX,ONE Date/Time Opened: JUL 27, 1999 13:13</p>
<p>Last Edit By: Date/Time Last Edit:</p>
<p>Processed By: Date/Time Processed:</p>
<p>FMS Cash Receipt Document: NOT SENT Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
<p>CP Cancel Payment CU Customize EA Exit Action MP Move Payment ER Edit Receipt</p>
<p>Select Action: Quit//NP <strong>New Payment</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> STEP 3: Type NP to record a payment. Complete the prompts needed to process a payment.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT NAME OR BILL NUMBER: PAYMENT AMOUNT:</p>
<p>DATE OF PAYMENT:</p>
<p>CHECK #:</p>
<p>CHECK BANK/ROUTING #:</p>
<p>DATE OF CHECK:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Account Profile screen

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 5%" />
<col style="width: 29%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Account Profile</strong></p>
</blockquote></th>
<th colspan="5"><blockquote>
<p><strong>Aug 24, 1999 16:00:40 Page: 1 of</strong></p>
</blockquote></th>
<th><strong>1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Account: ONE,ARPATIENT Addr: 1 STREET ADDR</p>
<p>RX Copay Exempt: NO</p>
<p><strong>ACCOUNT BALANCE: 36</strong></p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>(000000001) DOB: JAN 01,</p>
<p>ESS, CITY, ST 00011 Phone: 555 555</p>
<p><strong>.21</strong> Pending Payments: 0.00</p>
</blockquote></td>
<td><blockquote>
<p>1700</p>
<p>5555</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>BillNum CareDate</strong></p>
</blockquote></td>
<td><strong>Stat</strong></td>
<td><blockquote>
<p><strong>Bill Type</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Prin</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>cipal</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Interest</strong></p>
</blockquote></td>
<td><strong>Admin</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 K941719 04/05/99</p>
</blockquote></td>
<td>OPEN</td>
<td><blockquote>
<p>C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>13.74</p>
</blockquote></td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 K936439 03/12/99</p>
</blockquote></td>
<td>ACTI</td>
<td><blockquote>
<p>RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>7.47</p>
</blockquote></td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>21.21</p>
</blockquote></td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BP Bill Profile</p>
<p>BT Bill Transactions</p>
<p>Select Action: Quit//</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NA Select New Account SS Select Status</p>
</blockquote></td>
<td><blockquote>
<p>EA</p>
</blockquote></td>
<td><blockquote>
<p>Exit</p>
</blockquote></td>
<td><blockquote>
<p>Action</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Use Select Status to change the list of bills that will display on the Account Profile. This example only shows bills in Open and Active status. That is why the Account Balance and the Total Balance Owed for All Bills displayed do not match.

> Bill Profile screen

<table>
<colgroup>
<col style="width: 74%" />
<col style="width: 21%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Bill Profile Aug 24, 1999 16:01:43</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page: 1 of 3</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>* ACCOUNTS RECEIVABLE BILL PROFILE FOR 111-K941719 *</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Account: ONE,ARPATIENT(00000001) DOB: JAN 01, 1700 Addr: 1 STREET ADDRESS, CITY, ST 00011</p>
<p>Phone: 555 555 5555</p>
<p><strong>Bill Number: 111-K941719</strong> Category: C (MEANS TEST) Date Prepared: APR 05, 1999 Status: OPEN</p>
<p>Date Activated: APR 05, 1999@15:34:07</p>
<p>Date Status Up: APR 05, 1999 By:</p>
<p>Resulting From:</p>
<p>Type of Care: OUTPATIENT CARE(NSC)</p>
<p>Remark:</p>
<p>Interest Effective Rate Date: JAN 01, 1999 Annual Rate: .05 Admin Effective Rate Date: JAN 01, 1999 Monthly Rate: .45</p>
<p>Last Int/Admin Charge Date:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>BT Bill Transactions NB Select New Bill EA Exit Action</p>
<p>Select Action: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> There are three screens of information for this bill profile. Screen 2 shows the bill balance and collection follow up data. Screen 3 lists the transactions associated with this bill. Press Enter to see the additional screens.

> Automated payment and deposit processing

> In order for a station to begin using the centralized collection process, a number of simple steps must first be accomplished. Stations will begin using the payment processing in a phased implementation and each station will be assigned an implementation date based on their current statement processing date for CCPC.

> Prerequisites to implementation:

- Successful installation of the AR portion of the software and notification to the VACO staff and the Austin Automation Center.
- Provide Austin Automation Center personnel with a Federal Express address for mailing purposes. This address will be used for mailing any checks, correspondence, and other hard copy items received at the Lockbox collection site that are required at the medical centers. The address may be provided via e-mail (MS Exchange or V*IST*A MailMan) or fax. E-mails should be sent to the following names: Perry, Jenie; White, Karen M.; Floyd, Jenifer; Simpson, Jerry W; and Falcon, Sergio. Faxed information may be faxed to (512) 326-6738.
  - Refer to the same names and fax numbers after implementation to change the Federal Express information.
  - Provide the following with the Federal Express information:
    - Contact information, including routing indicator
    - Street address
    - City, state, zip code
    - Contact phone number

> Sites must complete steps at least three days before the implementation date.

> Upon completion of these steps, AAC will update the address information and change a flag in the Lockbox system to modify the remittance address on the outgoing patient statements for that station to the collection site. About 10 days after the station’s statement date, the station will begin receiving automatic payment transmissions and AR updates.

> Additional information related to implementation:

- The current “remit to” station address will continue to be maintained in the CCPC system. This address will be used to send information received by lockbox, that does not require Fed-X priority, to the stations. It is important that stations keep this address current.
- Stations can add a comment to the Special Notice field in the AR system that will allow the notification of veterans of a new payment mailing address. This should be done six days prior to the implementation date. During testing of this patch some stations elected to add a comment and some did not. Neither adding a comment nor not adding a comment resulted in a large number of phone calls about the address change.

## New Menu and the List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New Agent Cashier menu

> The Agent Cashier menu has changed, and, in fact, most of the options on this menu have changed. All of these changes were made to provide the agent cashiers with more information and to make payment processing an easier, more logical operation.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Clerk's AR Menu Option: Agent Cashier Menu</p>
<p>DP Deposit Processing RP Receipt Processing</p>
<p>LP Link Payment To Account</p>
<p>AP Account Profile</p>
<p>BP Bill Profile</p>
<p>BT Bill Transactions TP Transaction Profile</p>
<p>LR List Of Receipts Report</p>
<p>EX Extended Check/Credit Card Search</p>
<p>PD Patient Payment/Refund Transaction History Inquiry RH Release Holds on AR</p>
<p>TPJI Third Party Joint Inquiry</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>AR Menu Option</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Deposit Processing</p>
</blockquote></td>
<td><blockquote>
<p>Select to process deposits.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Receipt Processing</p>
</blockquote></td>
<td><blockquote>
<p>Select to process receipts.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Link Payment To Account</p>
</blockquote></td>
<td><blockquote>
<p>Select to link an unmatched payment to an account.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Account Profile</p>
</blockquote></td>
<td><blockquote>
<p>Profile a patient's account.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Bill Profile</p>
</blockquote></td>
<td><blockquote>
<p>Profile a bill.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Bill Transactions</p>
</blockquote></td>
<td><blockquote>
<p>List all the transactions for a bill.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transaction Profile</p>
</blockquote></td>
<td><blockquote>
<p>Profile a transaction recorded against a bill.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List Of Receipts Report</p>
</blockquote></td>
<td><blockquote>
<p>Print a list of receipts opened between selected date ranges.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Extended Check/Credit Card Search</p>
</blockquote></td>
<td><blockquote>
<p>Search all payments for a check or credit card number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Payment/Refund Transaction History Inquiry</p>
</blockquote></td>
<td><blockquote>
<p>Lists a history of payment/refund transactions for a patient for a specified date range.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Release Holds on AR</p>
</blockquote></td>
<td><blockquote>
<p>Select to release holds on Means Test bills. When a payment is received from an insurance company, any holds on bills to be sent to the patient need to be removed and the patient should be billed. This option allows the user to forward the bills from MCCR to AR to start the collection process.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Third Party Joint Inquiry</p>
</blockquote></td>
<td><blockquote>
<p>Set of actions and screens for Third Party AR/IB Joint Inquiry. Provides detailed information on any third party claim.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> List Manager

> The Lockbox patch introduces a new way to view and edit information called the List Manager. The List Manager is a tool that enables a user to do the following:

> \[ Display a list of related items

> \[ Browse back and forth through the items one at a time or by screen

> \[ Perform an action on a selected item from the list

> \[ Move to a related menu function without having to exit and enter a new menu option.

> This section of the Training Guide identifies the different sections of a List Manager screen, and show how to display and print information. A List Manager screen is divided into three sections; the header, the list and the action areas.

> Account Profile Aug 24, 1999 16:00:40 Page: 1 of 3

Account: ONE,ARPATIENT(000000001) DOB: JAN 01, 1700

Addr: 1 STREET ADDRESS, CITY, ST 00011 Phone: 555 555 5555

> RX Copay Exempt: NO

> ACCOUNT BALANCE: 21.21 Pending Payments: 0.00

> BillNum CareDate Stat Bill Type Principal Interest Admin

> 1 K941719 04/05/99 OPEN C (MEANS TEST) 13.74 0.00 0.00

> 2 K936439 03/12/99 ACTI RX CO-PAYMENT/NSC VET 7.47 0.00 0.00

> 3 K927498 02/02/99 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 4 K924944 01/19/99 COLL C (MEANS TEST) 0.00 0.00 0.00

> 5 K920091 01/04/99 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 6 K917790 12/18/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 7 K917835 12/18/98 COLL C (MEANS TEST) 0.00 0.00 0.00

> 8 K909807 11/15/98 COLL C (MEANS TEST) 0.00 0.00 0.00

> 9 K906926 11/04/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 10 K906212 11/02/98 COLL C (MEANS TEST) 0.00 0.00 0.00

> 11 K901135 10/06/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 12 K865354 09/09/98 COLL C (MEANS TEST) 0.00 0.00 0.00

> 13 K850271 06/25/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00 0.00

> 14 K838044 06/02/98 COLL C (MEANS TEST) 0.00 0.00 0.00

> + Enter ?? for more actions

> BP Bill Profile NA Select New Account EA Exit Action BT Bill Transactions SS Select Status

> Select Action: Next Screen//

> Header Area

> List Area

> Action Area

> The first line of the header area shows the screen title, the current date and time, and which page of information is being displayed in the list area. For the example above, the screen title is Account Profile and the first of three pages of information is being displayed. Below that is the demographic information that pertains to the entry selected.

> The list area displays all of the information relating to the entry selected. In this example, it shows a list of bills for this account. The list area includes the heading for each column in this display. Be sure to look at the Page area of the header to see how many pages of information is part of the display.

> Another place to look to see if there is more than one screen of information is on the line (or message window) that separates the list area from the action area.

> On the far left side of the message window is a plus sign (+). This indicates that there is more information available to display. There are times when there are left or right arrows (\<\<\< or

> \>\>\>) displayed on this line. This indicates the screen is wider than 80 characters and there is additional information to the left or right of the screen hidden from view.

> It is important to pay attention to the text displayed in this message window. When viewing a Receipt Profile, this area of the screen will show when a receipt was processed.

> The action area displays just some of the actions that can be performed from the display screen. Most times there is a default action listed. In the example below, the default action is Next Screen. Press the Enter key to display the next screen of information. When there is no more information to display in the list area, the default usually changes to Quit.

> Each List Manager screen has actions that can be performed upon the items listed. Or there may be actions that will allow the user to perform a related function without having to exit and enter a new option. Actions that appear in parentheses ( ) are not available for selection.

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Account Profile Aug 24, 1999 16:00:40</strong></p>
</blockquote></th>
<th></th>
<th colspan="2"><blockquote>
<p><strong>Page:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>of</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><p>Account: ONE,ARPATIENT(000000001) DOB: JAN 01, 1700</p>
<p>Addr: 1 STREET ADDRESS, CITY, ST 00011 Phone: 555 555 5555</p>
<blockquote>
<p>RX Copay Exempt: NO</p>
<p>ACCOUNT BALANCE: 21.21 Pending Payments: 0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p><strong>BillNum CareDate Stat Bill Type Principal Interest Admin</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 K941719 04/05/99 OPEN C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>13.74</p>
</blockquote></td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 K936439 03/12/99 ACTI RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>7.47</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 K927498 02/02/99 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4 K924944 01/19/99 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5 K920091 01/04/99 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6 K917790 12/18/98 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7 K917835 12/18/98 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8 K909807 11/15/98 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9 K906926 11/04/98 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10 K906212 11/02/98 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11 K901135 10/06/98 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12 K865354 09/09/98 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13 K850271 06/25/98 COLL RX CO-PAYMENT/NSC VET</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14 K838044 06/02/98 COLL C (MEANS TEST)</p>
</blockquote></td>
<td></td>
<td>0.00</td>
<td>0.00</td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BP Bill Profile NA Select New Account</p>
</blockquote></td>
<td><blockquote>
<p>EA</p>
</blockquote></td>
<td><blockquote>
<p>Exit</p>
</blockquote></td>
<td><blockquote>
<p>Action</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BT Bill Transactions SS Select Status</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Action: Next Screen// <strong>BP</strong> Bill Profile</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Bill: (1-33):</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
</tbody>
</table>

> Actions are selected by typing the action name or abbreviation at the Select Action: prompt. In the example above, the abbreviation BP was typed. The system then prompts the user to enter the number of the bill from the list area.

> Users can also use a shortcut to perform an action on a selected item by typing in the action abbreviation, an equals sign and the list number.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BP Bill Profile NA Select New Account EA Exit Action BT Bill Transactions SS Select Status</p>
<p>Select Action: Next Screen// <strong>BP=14</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark4" class="anchor"></span>There are additional common actions that can be performed that are hidden from view. Type two question marks (??) at the Select Action: prompt, to see the list of the hidden actions that can be used.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Action: Next Screen// <strong>??</strong></p>
<p>The following actions are also available:</p>
<p>+ Next Screen &lt; Shift View to Left PS Print Screen</p>
<p>- Previous Screen FS First Screen PL Print List UP Up a Line LS Last Screen SL Search List</p>
<p>DN Down a Line GO Go to Page ADPL Auto Display(On/Off)</p>
<p>&gt; Shift View to Right RD Re Display Screen Q Quit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Here is a list of the common List Manager actions with a brief description. There is also the abbreviation for each action. Typing the abbreviation is the quickest way to select an action.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 15%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Abbreviation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Next Screen</p>
</blockquote></td>
<td><blockquote>
<p>+</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Previous Screen</p>
</blockquote></td>
<td><blockquote>
<p>-</p>
</blockquote></td>
<td><blockquote>
<p>Move to the previous screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Up a Line</p>
</blockquote></td>
<td><blockquote>
<p>UP</p>
</blockquote></td>
<td><blockquote>
<p>Move up one line in the list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Down a Line</p>
</blockquote></td>
<td><blockquote>
<p>DN</p>
</blockquote></td>
<td><blockquote>
<p>Move down one line in the list</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Shift View to Right</p>
</blockquote></td>
<td><blockquote>
<p>&gt;</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to right if the screen width is more then 80 characters</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Left</p>
</blockquote></td>
<td><blockquote>
<p>&lt;</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to left if the screen width is more then 80 characters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>First Screen</p>
</blockquote></td>
<td><blockquote>
<p>FS</p>
</blockquote></td>
<td><blockquote>
<p>Move to the first screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Last Screen</p>
</blockquote></td>
<td><blockquote>
<p>LS</p>
</blockquote></td>
<td><blockquote>
<p>Move to the last screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Go to Page</p>
</blockquote></td>
<td><blockquote>
<p>GO</p>
</blockquote></td>
<td><blockquote>
<p>Go to a selected page in the list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Re-Display Screen</p>
</blockquote></td>
<td><blockquote>
<p>RD</p>
</blockquote></td>
<td><blockquote>
<p>Clear and re-display the current screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print Screen</p>
</blockquote></td>
<td><blockquote>
<p>PS</p>
</blockquote></td>
<td><blockquote>
<p>Print the header area and the portion of the list currently displayed</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print</p>
</blockquote></td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>Print the header area and all the items on the list</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Search List</p>
</blockquote></td>
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Search for text in list area</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Auto-Display(On/Off)</p>
</blockquote></td>
<td><blockquote>
<p>ADPL</p>
</blockquote></td>
<td><blockquote>
<p>Turns on/off display of actions at bottom of screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Quit</p>
</blockquote></td>
<td><blockquote>
<p>Q</p>
</blockquote></td>
<td><blockquote>
<p>Quit this screen</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Some actions are used to print information; type PS to print what appears on the screen and type PL to print <u>all of the screens</u> of information for the entry. Other actions are used to navigate through the list area. For example, type LS to move to the Last Screen of information. The List Manager can also recognize the navigation keys located on the keyboard. This includes the Page Up and Page Down keys as well as the up and down arrow keys.

> .

## Deposit/Receipt/Payment Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deposit processing

> Begin posting payments by creating a deposit ticket. At the Select Agent Cashier Menu Option: prompt, type DP for Deposit Processing and press the Return key. The Deposit Processing screen will appear.

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 15%" />
<col style="width: 32%" />
<col style="width: 4%" />
<col style="width: 24%" />
<col style="width: 1%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p><strong>Deposit Processing Aug 19, 1999 09:56:11 Page:</strong></p>
</blockquote></th>
<th><strong>1 of 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Deposit #: 111111 Deposit Status: OPEN Deposit Date: JUL 27, 1999</p>
<p>Opened By: VALOCKBOXM,ONE Date/Time Opened: JUL 27, 19</p>
<p>Confirmed By: Date/Time Confirmed:</p>
</blockquote></td>
<td>99 13:12</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Receipt</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Payment Type OpenDate</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>By</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>ProcDate By Count</strong></p>
</blockquote></td>
<td><strong>Total Paid</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>11111111</p>
</blockquote></td>
<td><blockquote>
<p>CASH PAYMENT 07/27/99</p>
</blockquote></td>
<td><blockquote>
<p>LT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>5.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>LOCKBOXTST</p>
</blockquote></td>
<td><blockquote>
<p>CHECK/MO PAYMENT 08/19/99</p>
</blockquote></td>
<td><blockquote>
<p>DS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>86.50</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>TOTAL DOLLARS FOR DEPOSIT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>91.50</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Bank:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Bank Trace Number:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Agency Location Code:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Agency Title:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>ED Edit Deposit AR Add Receipt</p>
<p>CD Confirm Deposit RP Receipt Profile</p>
<p>Select Action: Quit//<strong>AR Add Receipt</strong></p>
</blockquote></td>
<td><blockquote>
<p>CU Customize EA Exit Action</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> There are a number of actions related to deposit processing that can be performed from this screen. These actions include edit deposit information, confirm the deposit, view a receipt profile, customize the data on the screen, or exit this screen.

> At the Select Action: prompt, type AR to Add a Receipt and begin posting payments from this option. Another option would be to post payments using the RP - Receipt Processing menu.

> Receipt – payment processing

> At the Select Agent Cashier Menu Option: prompt, type RP for Receipt Processing and press Enter. Enter a new receipt number or choose an existing receipt number to begin posting payments. If adding a new receipt number, the user must identify the type of payment.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Receipt Profile Aug 19, 1999 09:05:19 Page: 1 of 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT</p>
<p>Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong># Account Pay Date By Pay Amt Proc Amt</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 0.00 0.00</p>
<p>Receipt History</p>
<p>Opened By: Date/Time Opened: AUG 19, 1999 09:04</p>
<p>Last Edit By: Date/Time Last Edit:</p>
<p>Processed By: Date/Time Processed:</p>
<p>FMS Cash Receipt Document: NOT SENT Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
<p>CP Cancel Payment <strong>CU Customize</strong> EA Exit Action MP Move Payment ER Edit Receipt</p>
<p>Select Action: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *HINT:* Before posting payments for the first time, you may want to change how the Receipt- Processing screen looks. The Customize action allows you to decide what information you want shown on your screen, such as the check number, FMS details, comments, if you want a receipt printed after each transaction, and how to designate the 215 printer. The customize action is usually only performed once.

> At the Select Action: prompt, type CU to customize the screen display and options used when processing receipts.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Do you want to show check and credit card information? YES//</p>
<p>Do you want to show acct lookup, batch and sequence information? NO// Do you want to show comments? YES//</p>
<p>Do you want to show the FMS cash receipt documents? YES//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The next series of prompts allow the user to individually set up the way receipts print when entering payment transactions. The user can set up the software to automatically print a receipt to a device, never print the receipt, or ask each time to print the receipt. The user can also specify the printer to be used for printing receipts and eliminate the need to enter the device name each time.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select one of the following:</p>
</blockquote>
<ol type="1">
<li><p>Never Print the Receipt</p></li>
<li><p>Always Print the Receipt</p></li>
<li><blockquote>
<p>Maybe, Ask to Print the Receipt Print Receipt: NEVER//</p>
</blockquote></li>
</ol>
<blockquote>
<p>You now have the option of setting up the default printer for automatically printing the 215 report when a receipt is processed.</p>
<p>Enter the Default Printer for Printing the 215 Report:<u>&lt;enter device or leave</u> <u>blank&gt;</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Receipt Profile screen shows the receipt number, type of payment, deposit number, receipt status and FMS document information.

> At the Select Action: prompt, type NP for New Payment to begin entering payments.

<table>
<colgroup>
<col style="width: 88%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 09:09:31 Page: 1 of 2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT</p>
<p>Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong># Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99 DS 32.50</p>
</blockquote></td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: PP-7 Date: 08/17/99 Bank #: 63/352</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 ONE,ARPATIENT B 08/19/99 DS 25.00</p>
</blockquote></td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 57.50</p>
</blockquote></td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Receipt History</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Opened By: Date/Time Opened: AUG 19, 1999</p>
</blockquote></td>
<td>09:04</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Last Edit By: Date/Time Last Edit: AUG 19, 1999</p>
</blockquote></td>
<td>09:09</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Processed By: Date/Time Processed:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>+ Transaction # 2 has been ADDED.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>NP New Payment</strong> AP Account Profile PR Process Receipt</p>
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
<p>Select Action: Next Screen// <strong>NP New Payment</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> The prompts displayed when entering a payment have not changed. The (space-bar-Enter) option is still available to use when recording multiple transactions from one check.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT NAME OR BILL NUMBER: PAYMENT AMOUNT:</p>
<p>DATE OF PAYMENT:</p>
<p>CHECK #:</p>
<p>CHECK BANK/ROUTING #:</p>
<p>DATE OF CHECK:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The display returns to the Receipt Profile screen as each payment is completed. The profile screen is helpful because it displays all of the payments attached to this receipt. This new screen also provides users with the ability to view the transactions previously entered on this receipt to prevent duplication of payments. As the list of payments grows, press the + (plus) or – (minus) keys to scroll up and down the transaction list.

<table>
<colgroup>
<col style="width: 88%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 09:11:13 Page: 1 of 2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong># Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99 DS 32.50</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: PP-7 Date: 08/17/99 Bank #: 63/352</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 ONE,ARPATIENT B 08/19/99 DS 25.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 ONE,ARPATIENT C 08/19/99 DS 14.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 ONE,ARPATIENT D 08/19/99 DS 15.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 86.50</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>+ Transaction # 4 has been ADDED.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
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
<p>Select Action: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> If a discrepancy occurs in the posting of payments a warning will be created to alert the clerk of a possible error being made.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Receipt Profile Aug 19, 1999 10:46:13 Page: 1 of 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT</p>
<p>Deposit #: 123456 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong># Account Pay Date By Pay Amt Proc Amt</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 111-K942688 08/19/99 DS 183.20 0.00</p>
<p><strong>WARNING: Amount paid greater than amount billed ($ 45.80) Check #: 1234 Date: 08/17/99 Bank #: 62/356</strong></p>
<p>TOTAL DOLLARS FOR RECEIPT <em>Warning messages display on</em> - --------</p>
</blockquote>
<p>0.00</p>
<blockquote>
<p><em>Receipt Profile screen.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
<p>CP Cancel Payment CU Customize EA Exit Action MP Move Payment ER Edit Receipt</p>
<p>Select Action: Next Screen// <strong>EP Edit Payment</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Use the action, EP (Edit Payment) to edit the payment and post the correct amount. Note that a comment is added showing the edit was done.

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 28%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 11:26:07 Page: 1 of 2</strong></p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT</p>
<p>Deposit #: 123456 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong># Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99 DS 45.80 0.00</p>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
<p>2 ONE,ARPATIENT A 08/19/99 DS 0.00 0.00</p>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
<p><strong>Cancel Data: Amount $183.20 decreased in original trans#1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT</p>
<p>indicates payment is CANCELLED</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><em>Message indicates change was made to transaction.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
<p>CP Cancel Payment CU Customize EA Exit Action MP Move Payment ER Edit Receipt</p>
<p>Select Action: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Another new warning message may display when processing third-party payments for patients with Cat C bills on hold. If the patient has patient bills on hold, an alert will appear to notify the clerk of the situation. The clerk can make a determination if the payment should have gone to the Cat C charge.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Type of payment: CHECK/MO PAYMENT Adding a NEW payment transaction: # 3</p>
<p>PATIENT NAME OR BILL NUMBER: K942688 BC/BS OF NJ ACTIVE $45.80 ... <strong>This</strong></p>
<p><strong>bill appears to have other patient bills on 'hold'.</strong></p>
<p>Amount Owed: $45.80</p>
<p>PAYMENT AMOUNT:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> After entering all payments, the next step is to process the receipt. Some cashiers use the PL (Print List) action to print and review the entries on this receipt before processing.

<table>
<colgroup>
<col style="width: 88%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 09:11:13 Page: 1 of 2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong># Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99 DS 32.50</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: PP-7 Date: 08/17/99 Bank #: 63/352</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 ONE,ARPATIENT B 08/19/99 DS 25.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 ONE,ARPATIENT D 08/19/99 DS 14.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 ONE,ARPATIENT G 08/19/99 DS 15.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL DOLLARS FOR RECEIPT 86.50</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>+ Transaction # 4 has been ADDED.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NP New Payment AP Account Profile <strong>PR Process Receipt</strong></p>
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
<p>Select Action: Next Screen// <strong>PR Process Receipt</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> At the Select Action: prompt, type PR for Process Receipt to post payments. The system automatically checks for posting errors.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Checking payment amounts versus billed amounts ... payments okay.</strong></p>
<p>BANK DEPOSIT DATE: <strong>AUG 19, 1999</strong></p>
<p>Are you sure you want to PROCESS this receipt? NO// <strong>YES</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> At the BANK DEPOSIT DATE: prompt, enter in the date typed on the hardcopy SF215 Deposit Ticket. The bank deposit date in AR should match the date on the deposit ticket.

> At the Are you sure you want to PROCESS this receipt?: prompt, type Y for yes if this receipt is complete and correct.

> If a discrepancy occurs while trying to process a receipt, a warning will appear on the screen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>WARNING: Transaction 9 payment of $ 229.00 exceeds billed amount $ 209.00 Adjust payments listed above before processing.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Use the EP (Edit Payment) action to correct the payment transaction. Once all transactions are correct, continue to Process Receipt (PR).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Updating AR accounts... Done.</p>
<p>Transmitting CR document to FMS... Done. FMS document number CR-111K9A0467 Queuing 215 report... Use Customize Option to set up the default printer.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Again, the system reviews all transactions for any discrepancies, imbalances or inconsistencies. If no warnings appear the receipt is closed and payments are posted to accounts. An FMS document is generated, if appropriate. The document number is displayed. If a default 215 printer was defined (using the Customize action), the 215 will print at this time.

> Please note that a deposit can have multiple receipts and multiple cash receipt (CR) documents sent to FMS.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 20%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 12:38:18 Page: 3 of 4</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT</p>
<p>Deposit #: 123456 Receipt Status: CLOSED</p>
<p>FMS Document: CR-111K9A0468 FMS Doc Status: QUEUED FOR TRANSMISSION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><strong>+# Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99 DS 32.50 0.00</p>
<p>Check #: PP-7 Date: 08/17/99 Bank #: 63/352</p>
<p>2 ONE,ARPATIENT B 08/19/99 DS 25.00 0.00</p>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
<p>3 ONE,ARPATIENT D 08/19/99 DS 14.00 0.00</p>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
<p>4 ONE,ARPATIENT G 08/19/99 DS 15.00 0.00</p>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
<p>TOTAL DOLLARS FOR RECEIPT 86.50 0.00</p>
<p>Receipt History</p>
<p>Opened By: Date/Time Opened: AUG 19, 1999 10:25</p>
<p>Last Edit By: Date/Time Last Edit: AUG 19, 1999 11:38</p>
<p>Processed By: Date/Time Processed: AUG 19, 1999 12:36</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>Receipt PROCESSED</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>NP (New Payment) AP Account Profile PR Process Receipt EP (Edit Payment) RR Reprint Receipt 21 215 Report</p>
<p>CP (Cancel Payment) CU Customize EA Exit Action MP (Move Payment) ER (Edit Receipt)</p>
<p>Select Action: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The transmission is queued to go to FMS. The agent cashier now manually performs the actions required to process the deposit ticket. No further action is required until the confirmed deposit ticket is returned.

> The following is a sample of what is displayed when the Customize screen is set to display the FMS cash receipt.

<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>FMS Cash Receipt Document: CR-111K9A0468 Status: QUEUED FOR TRANSMI</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CTL^ARS^FMS^111^DOC^CR^10 ^ ^111K9A0468 ^19990819^123619^001^001^001^~</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DOC^~CR1^CR^111K9A0468 ^10 ^N^~</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CR2^99^08^19^^^^^^E^^^123456^^86.50^^99^08^19^~</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>LIN^~CRA^001^99^^5287^111^^^85CZ^^^^^^^^MCCFVALUE^^86.50^I^^23^~</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Receipt processed on AUG 19, 1999@12:36</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NP (New Payment) AP Account Profile</p>
</blockquote></td>
<td><blockquote>
<p>PR Process Receipt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EP (Edit Payment) RR Reprint Receipt</p>
</blockquote></td>
<td><blockquote>
<p>21 215 Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CP (Cancel Payment) CU Customize</p>
</blockquote></td>
<td><blockquote>
<p>EA Exit Action</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MP (Move Payment) ER (Edit Receipt)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Action: Quit//</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Receipts do not have to be pre-approved before processing. Patch PRCA\*4.5\*114 allows the receipt to be processed as soon as all payments have been entered. A deposit or receipt can no longer be voided. If a deposit is entered in error, confirm the deposit to close it. If a receipt is entered in error, process the receipt and it will be closed. If there are no payments on the receipt, no data will be processed in Accounts Receivable or sent to FMS.

> BLANK PAGE

## Suspense Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Accounts Receivable patch PRCA\*4.5\*114 introduces the functionality to deposit funds to Suspense account 36F3875. This account is used when there is a discrepancy in payments, normally due to an overpayment, an unidentifiable payment, or a duplicate payment. Funds that cannot be applied to a bill or account number should be recorded to Suspense. This action is accomplished when recording payments as shown below.

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Enter ?? for more</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>actions</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NP New Payment AP Account Profile</p>
</blockquote></td>
<td><blockquote>
<p><strong>PR Process Receipt</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EP Edit Payment RR Reprint Receipt</p>
</blockquote></td>
<td><blockquote>
<p>21 (215 Report)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CP Cancel Payment CU Customize</p>
</blockquote></td>
<td><blockquote>
<p>EA Exit Action</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MP Move Payment ER Edit Receipt</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Action: Next Screen// <strong>NP New Payment</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> At the Select Action: prompt, type NP for New Payment.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Type of payment: CHECK/MO PAYMENT Adding a NEW payment transaction: # 5</p>
<p>PATIENT NAME OR BILL NUMBER: <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>NOTE: This payment will be posted to the station's suspense fund.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMMENT: <strong>CAN'T ID PT-ONE,ARPATIENT Z-DOS 061599</strong></p>
<p>PAYMENT AMOUNT: <strong>10.00</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> At the Patient Name or Bill Number: prompt, *press Enter* instead of entering a patient’s name or bill number. This action creates a note on the screen stating the payment will be applied to the station’s suspense fund.

> At the Comment: prompt, enter the reason this payment is being placed in suspense. For this example, the reason is the cashier cannot identify the patient and needs to perform research related to the date of service of June 15, 1999 in order to apply the payment correctly.

> Once the payment information has been entered a transaction will appear on the Receipt Profile screen. This transaction displays a system generated suspense number, which will be the unapplied deposit number in FMS, in place of the account name. The comments entered are displayed also.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 53%" />
<col style="width: 16%" />
<col style="width: 0%" />
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>Receipt Profile Aug 19, 1999 09:11:13 Page: 1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>of</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="8"><blockquote>
<p>Receipt #: LOCKBOXTST Type of Payment: CHECK/MO PAYMENT Deposit #: 111111 Receipt Status: OPEN</p>
<p>FMS Document: NOTSENT FMS Doc Status: NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p><strong># Account Pay Date By Pay Amt Proc Amt</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1 ONE,ARPATIENT A 08/19/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DS 32.50</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Check #: PP-7 Date: 08/17/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Bank #: 63/352</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>2 ONE,ARPATIENT B 08/19/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DS 25.00</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Check #: 1234 Date: 08/17/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Bank #: 62/356</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>3 ONE,ARPATIENT D 08/19/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DS 14.00</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Check #: 1234 Date: 08/17/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Bank #: 62/356</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>4 ONE,ARPATIENT G 08/19/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DS 15.00</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Check #: 1234 Date: 08/17/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Bank #: 62/356</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5 [ suspense LOCKBOXTST0005 ] 08/20/99</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DS 22.00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"><blockquote>
<p>Check #: 1234 Date: 08/17/99 Bank #: 62/356</p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>Comment: CAN'T ID PT-ONE,ARPATIENT Z-DOS 061599</p>
</blockquote></td>
<td colspan="5"></td>
</tr>
<tr class="even">
<td colspan="8"></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p><strong>+ Transaction # 5 has been ADDED.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>NP New Payment AP Account Profile PR Process Receipt EP Edit Payment RR Reprint Receipt 21 (215 Report)</p>
<p>CP Cancel Payment CU Customize EA Exit Action MP Move Payment ER Edit Receipt</p>
<p>Select Action: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> See the Link Payment to Account section for information about clearing suspense issues.

## Link Payment to Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Agent Cashier functionality provides the ability of stations to use Accounts Receivable to deposit funds to Suspense account 36F3875 (see section on Receipt Processing). These unapplied payments can be found under the option Link Payment To Account. When entering this option, the system will prompt the station for a beginning date to start the search. The screen will display a listing of all transactions that require action. Stations have the option of either linking these payments to an account (LP) or clearing these payments from the listing due to refunds to the original payee and/or transfers to other stations (CS).

> NOTE: The Accounts Receivable package will not create the FMS document to either move the funds or make payment to an entity. If the CR document has rejected and the station links the payment before re-processing the receipt, then the funds will be applied to the proper appropriation/fund and not to suspense. Also available under this option is a Suspense Report that shows what action the station took to move these funds from Suspense.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>Select Agent Cashier Menu Option:</p>
<p>DP Deposit Processing RP Receipt Processing</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Link</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Payment</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>To</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Account</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Link Payment - scenario \#1

> This scenario shows how to process a suspense payment that has been identified as belonging to a veteran's account. Select the Link Payment to Account option located on the Agent Cashier menu. Next, enter the payment date. Press Enter to list all unapplied payments.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Agent Cashier Menu Option: <strong>LP Link Payment To Account</strong></p>
<p>Start with Payment Date (press RETURN for FIRST): <strong>0707</strong> (JUL 07, 1999)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Link Payments to Accounts screen will appear. At the Select Action: prompt, type LP

> for Link Payment.

<table>
<colgroup>
<col style="width: 89%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Link Payments To Accounts Jul 21, 1999 17:26:36 Page: 1 of 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Transactions for Unapplied Payments After JUL 12, 1999</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Receipt Tran Unapplied Dep Stat Pay Date Type Chk/Crd# Amt Paid</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 L99070700 22 L990707000022 CLOS 07/07/99 CHEC 1875</p>
</blockquote></td>
<td>10.00</td>
</tr>
<tr class="even">
<td>AcctLU: 111111111XXXXX CRdoc: CR-111K9A0695 ACCEPT</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 L99071300 20 L990713000020 CLOS 07/13/99 CHEC 8138</p>
</blockquote></td>
<td>12.00</td>
</tr>
<tr class="even">
<td>AcctLU: 99999999999999 CRdoc: CR-111K9A1034 ACCEPT</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 L99071300 21 L990713000021 CLOS 07/13/99 CHEC 2521260</p>
</blockquote></td>
<td>19.00</td>
</tr>
<tr class="even">
<td>AcctLU: 99999999999999 CRdoc: CR-111K9A1034 ACCEPT</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 L99071300 22 L990713000022 CLOS 07/13/99 CHEC 995011</p>
</blockquote></td>
<td>2.00</td>
</tr>
<tr class="even">
<td>AcctLU: 99999999999999 CRdoc: CR-111K9A1034 ACCEPT</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>S1 Search Check CS Clear Suspense AP Account Profile</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>S2 Search Credit Card SR Suspense Report RP Receipt Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>LP Link Payment SP Show Payment EA Exit Action</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select Action: Next Screen//<strong>LP Link Payment</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> The system provides help screens to guide the user through the process. For this example, payment number 3 is selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>This option will allow the account to be entered for an unapplied payment transaction selected from the above list. If the selected receipt has been previously processed, the selected account in the accounts receivable package will be updated with the payment.</p>
<p>Select Payment: (1-4): <strong>3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The system checks the document status. If the document status is Transmitted or Queued for Transmission, the Link Payment action cannot proceed. Instructions are displayed to the user. In this example, the document status is Accepted by FMS and the Link Payment action continues.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong><u>Document Status</u></strong></p>
<p><em>Queued For Transmission</em>: Option is locked.</p>
<p><em>Transmitted</em>: Option is locked.</p>
<p><em>Rejected By FMS</em>: Option may be used to link the payment and then use the option PR Process Receipt to regenerate the CR document. Funds will not go to Suspense but to the appropriate accounts.</p>
<p><em>Accepted By FMS</em>: Option may be used to link the payment (LP) or clear the suspense record (CS). Station will have to manually input FMS transaction to move the funds from Suspense to the appropriate accounts.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The system shows when the update is complete. It is critical that you read the notification message on the screen and follow the instructions provided.

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 30%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Updating the Linked Account with the payment ... done.</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p><strong>Since the FMS cash receipt document is Accepted in FMS, you need to go online in FMS and transfer the amount paid out of the station's suspense</strong></p>
<p><strong>account.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Sending mail message to RCDP PAYMENTS mail group. ...</p>
<p>Payment linked and removed from list.</p>
<p>press RETURN to continue:</p>
</blockquote></td>
<td colspan="2" rowspan="2"><blockquote>
<p><em>Very important step needs to be accomplished by the station if the CR document has already been accepted in FMS.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

> Here is an example of the MailMan message received after initial load of the software. The mail message includes instructions on how to proceed. The hint portion of this message is scheduled to disappear 30 days after the software is installed.

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 32%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Subj: Transfer Payment From Suspense Rec/# L99071300/21 [#7970030] 21 Jul 99 17:29 19 Lines</p>
<p>From: AR Package in 'IN' basket. Page 1 NEW</p>
<p>The following payment has been processed to an Account in AR and needs to be moved from the station's suspense account 3875 to</p>
<p>the <strong>appropriation/fund identified for this account online in FMS</strong>.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receipt Number: L99071300 Payment Transaction Number: 21</p>
<p>Unapplied Deposit Number: L99071300021 FMS CR document ID: CR-111K9A1034</p>
<p>Amount Paid: 19.00</p>
<p>Process Date: JUL 14, 1999</p>
</blockquote></td>
<td><blockquote>
<p><em>To identify the proper breakdown of payment to an account, the user shou use the option SP Show Payment. Th option shows the amount applied to principal, interest, admin, etc.</em></p>
</blockquote></td>
<td><blockquote>
<p><em>this ld is</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>HINT: (Make a note, this hint will soon disappear)</strong></p>
<p><strong>Once the payment has been moved from suspense in FMS, you can use the Clear Suspense option under the Link Payment ListManager</strong> <strong>screen to track the FMS document used to transfer the payment.</strong></p>
<p><strong>Since the payment no longer appears on the Link Payment ListManager screen, at the Select Payment option, press return with out selecting a payment and you will have the option to enter the receipt and</strong></p>
<p><strong>transaction number (listed above).</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
<p>S1 Search Check CS Clear Suspense AP Account Profile S2 Search Credit Card SR Suspense Report RP Receipt Profile LP Link Payment SP Show Payment EA Exit Action Select Action: Next Screen// <strong>SP Show Payment</strong></p>
<p>Select RECEIPT: <strong>l99071300</strong> by: POSTMASTER on: 07/13/99 LOCKBOX CLOSED Select Receipt TRANSACTION #: 21 ONE,ARPATIENT J $ 19.00</p>
<p>Receipt: L99071300 Transaction: 21</p>
<p>Unapplied Deposit Number: L990713000021 Total Paid Amount: 19.00</p>
<p>Transaction: 3011768</p>
<p>Principal Collected: 19.00</p>
<p>Interest Collected: 0.00</p>
<p>Admin Collected: 0.00</p>
<p>Marshal Fee Collected: 0.00</p>
<p>Court Cost Collected: 0.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The following is an example of the same MailMan message after the hint disappears.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: Transfer Payment From Suspense Rec/# L99071300/21 [#7970030] 21 Jul 99 17:29 10 Lines</p>
<p>From: AR Package in 'IN' basket. Page 1 NEW</p>
<p>The following payment has been processed to an Account in AR and needs to be moved from the station's suspense account 3875 to</p>
<p>the appropriation/fund identified for this account online in FMS.</p>
<p>Receipt Number: L99071300 Payment Transaction Number: 21</p>
<p>Unapplied Deposit Number: L990713000021 FMS CR document ID: CR-111K9A1034</p>
<p>Amount Paid: 19.00</p>
<p>Process Date: JUL 14, 1999</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> To move the funds from Suspense to the appropriate fund(s) in FMS, the station needs to sign on to FMS and manually create a TR document. An example of this document follows:

> *FMS Screen 1 - Header*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COMMND: DOCID: TR 10 111L990713 STATUS: ACCPT BATID: SUB STN: 07/21/99</p>
<p>CASH RECEIPT INPUT SCREEN</p>
<p>BATCH DATE: NUM DOCS: NET:</p>
<p>CR DATE: ACCTG PRD: ACTION: SUB STN: 111 TRANS TYPE: BFYS: FUND:</p>
<p>CASH ACCT: DEP NUMBER: <strong>L990713</strong> DOC TYPE:</p>
<p>BILL FUND: DOC TOTAL: <strong>0.00</strong></p>
<p>DISB OFFICE: 220 ACCOMPLISHED DATE: <strong>07 21 99</strong></p>
<p>REF DOC:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *FMS Screen 2 - Line Information*

> Link Payment - scenario \#2

> This scenario refers to an unapplied payment that belongs to another station. When a station transfers funds to another facility from their suspense, then an OF 1017-G, Journal Voucher, should be initiated by the transferring site.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Optional Form 1017-G (9-79) Title 7, GAO Manual</p>
<p>501017-810</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>JOURNAL VOUCHER</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="2"></td>
<td colspan="2"><blockquote>
<p>J.V. NO. 111-F-077</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DATE 7/19/99</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="6"></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td colspan="3"><blockquote>
<p>WITHDRAW FROM: <u>Station 111</u> <u>36F3875</u></p>
<p>2400</p>
<p>1021</p>
<p>EB 03 “I” 111ET9077</p>
<p>Vendor Code 222VAH000 Unapplied Deposit #L990707000022</p>
<p>PAY TO: <u>Station 222</u> 1021</p>
<p>2400</p>
<p>EB 03 “D” 111ET9077</p>
<p>Vendor Code 222VAH000 Unapplied Deposit #L990707000022</p>
<p>To transfer funds received at <em>VA name</em> due to lockbox processing for XXX-XX-XXXX ONE, ARPATIENT B on check number 1876.</p>
</blockquote></td>
<td><blockquote>
<p>10.00</p>
<p>10.00</p>
</blockquote></td>
<td><blockquote>
<p>10.00</p>
<p>10.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p><strong>TOTAL</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>PREPARED BY (Signature)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>APPROVED BY (Signature)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>TITLE OF PREPARING OFFICIAL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>TITLE OF APPROVING OFFICIAL</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark8" class="anchor"></span>Once the station has a journal voucher number, an expenditure transfer (EB) document can be created in FMS. This transaction will remove the unapplied deposit transaction from the transferring station's Suspense and deposit to the receiving station's Suspense. To verify the transaction is there for moving, the station would go to the UDST table. After the EB is processed, the station could return to this table to verify the record has been removed from their account and deposited to the other station. Station should fax the Journal Voucher to the receiving station for their action.

> *FMS screen*

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 39%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>ACTION: R TABLEID: <strong>UDST</strong> USERID: S111 ZZZ</p>
<p>OUTSTANDING UNAPPLIED DEPOSIT SUMMARY INQUIRY SCREEN KEY IS STATION, FUND, UNAPPLIED DEPOSIT NO</p>
<p>STATION: 111 FUND: 3875 TRANSFERS IN: 43.00</p>
<p>TRANSFERS OUT: 0.00</p>
<p>BALANCE: 43.00</p>
<p>UNAPPLIED DATE LST ACT</p>
<p>DEPOSIT NO ESTBLH DATE TRANSFERS IN TRANSFERS OUT BALANCE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>01- L990707000022 070799 070799</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>10.00</strong></p>
</blockquote></td>
<td><strong>0.00</strong></td>
<td><blockquote>
<p><strong>10.00</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>02- L990713000020 071399 071499</p>
</blockquote></td>
<td><blockquote>
<p>12.00</p>
</blockquote></td>
<td>0.00</td>
<td colspan="2"><blockquote>
<p>12.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03- L990713000021 071399 071499</p>
</blockquote></td>
<td><blockquote>
<p>19.00</p>
</blockquote></td>
<td>0.00</td>
<td colspan="2"><blockquote>
<p>19.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> An example of the EB document for the highlighted record is as follows.

> *FMS screen - header*

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>COMMND: DOCID: <strong>EB 10 111ET9077</strong> STATUS: ACCPT BATID: SUB STN: 07/19/99</p>
<p>STANDARD VOUCHER INPUT SCREEN</p>
<p>SV DATE: ACCT PRD: SUB STN: 111 ACTION: EXPENSE(E), REVENUE(R), GL(G), BUDGET(B):</p>
<p>BFYS: FUND:</p>
<p>REVERSAL PERIOD:</p>
<p>COMMENT: BUDGET OVERRIDE IND:</p>
<p>DOC TOTAL: <strong>0.00</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DESCRIPTION:</p>
</blockquote></td>
<td><blockquote>
<p><strong>TRF</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>L990707000022</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>STA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>222</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *FMS screen 2 - line 001*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COMMND: DOCID: EB 10 111ET9077 STATUS: ACCPT 001-001 OF 002 BATID: SUB STN: 07/19/99</p>
<p>01-</p>
<p>LINE: <strong>001</strong> TRANS TYPE: <strong>03</strong> EXP/REV/GL/BG: <strong>G</strong> A/O: BFYS: <strong>99</strong> FUND: <strong>3875</strong> STATION/SAT: <strong>111</strong> FCP/PRJ: JOB NO: COST CTR/SUB: BOC/REV SOURCE/SUB: REPT CATG: CLSD BFYS: CLSD FUND:</p>
<p>VENDOR: <strong>222VAH000</strong> NAME: VETERANS ADMINISTRATION SCHD FY: SCHD CAT: SCHD TYP: SCHD NO: <strong>071999</strong></p>
<p>D.O.: GUEST SYMBOL: QTY: REF DOC ID: DOC TYP: AGR NO:</p>
<p>AMOUNT: <strong>10.00</strong> I/D: OBL FY: ACCP DATE: <strong>07 19 99</strong> ADV: INVOICE NO: INV LINE: INV DATE:</p>
<p>DESCRIPTION: TREAS NO:</p>
<p>UNAPPLIED DEP NO: <strong>L990707000022</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="_FMS_screen_2_-_line_002" class="anchor"></span>*FMS screen 2 - line 002*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COMMND: DOCID: EB 10 111ET9077 STATUS: ACCPT 002-002 OF 002 BATID: SUB STN: 07/19/99</p>
<p>01-</p>
<p>LINE: <strong>002</strong> TRANS TYPE: <strong>03</strong> EXP/REV/GL/BG: <strong>G</strong> A/O: BFYS: <strong>99</strong> FUND: <strong>3875</strong> STATION/SAT: <strong>222</strong> FCP/PRJ: JOB NO: COST CTR/SUB: BOC/REV SOURCE/SUB: REPT CATG: CLSD BFYS: CLSD FUND:</p>
<p>VENDOR: <strong>222VAH000</strong> NAME: VETERANS ADMINISTRATION SCHD FY: SCHD CAT: SCHD TYP: SCHD NO: <strong>071999</strong></p>
<p>D.O.: GUEST SYMBOL: QTY: REF DOC ID: DOC TYP: AGR NO:</p>
<p>AMOUNT: <strong>10.00</strong> I/D: D OBL FY: ACCP DATE: <strong>07 19 99</strong> ADV: INVOICE NO: INV LINE: INV DATE:</p>
<p>DESCRIPTION: TREAS NO:</p>
<p>UNAPPLIED DEP NO: <strong>L990707000022</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The receiving station will now have this transaction appear in their FMS suspense account, not in the AR suspense account. The receiving station must revert to manual procedure such as when you receive IRS or DMC payments.

> In order for the station to clear the suspense record from Accounts Receivable, the option CS Clear Suspense must be used.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 30%" />
<col style="width: 29%" />
<col style="width: 7%" />
<col style="width: 27%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="4"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>S1 Search Check</p>
<p>S2 Search Credit Card LP Link Payment</p>
<p>Select Action: Quit// <strong>CS</strong></p>
</blockquote></td>
<td><blockquote>
<p>CS Clear Suspense SR Suspense Report SP Show Payment</p>
<p><strong>Clear Suspense</strong></p>
</blockquote></td>
<td><blockquote>
<p>AP RP EA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Account Profile Receipt Profile Exit Action</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This option will allow you to enter the FMS document number used to clear the payment from the suspense account in FMS. Once an FMS document number is entered, the payment will no longer appear on the list as Unlinked.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Payment: (1-4): <strong>1</strong></p>
<p>Receipt: L99070700 <em>Enter FMS transaction/DOC ID.</em></p>
<p>Transaction: 22</p>
<p>Unapplied Deposit Number: L990707000022 CLEAR SUSPENSE FMS DOC ID#: <strong>ET 111ET9077</strong></p>
<p>please wait, building list of unlinked payments...</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> NOTE: If a payment has been linked to another account but the station had to do FMS input to move the funds from Suspense to the proper appropriation/fund, then this option would be used, also, to record that FMS action.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 6%" />
<col style="width: 27%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="4"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>S1 Search Check CS S2 Search Credit Card SR LP Link Payment SP Select Action: Next Screen//</p>
</blockquote></td>
<td><blockquote>
<p>Clear Suspense Suspense Report Show Payment</p>
<p><strong>CS Clear Suspense</strong></p>
</blockquote></td>
<td><blockquote>
<p>AP RP EA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Account Profile Receipt Profile Exit Action</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This option will allow you to enter the FMS document number used to clear the payment from the suspense account in FMS. Once an FMS document number is entered, the payment will no longer appear on the list as Unlinked.

> Link Payment - scenario \#3

> This outlines a suspense payment that goes to more than one account and/or is a combination of part account and part refund. The current functionality will not let you do partial postings for a Suspense record in the AR package. An example of this type situation would be that the station decides that of a \$100 payment that was recorded in Suspense that \$45.80 should be applied to the veteran’s account and the balance of \$54.20 should be refunded to the insurance company. The Link Payment (LP) option does not allow you to change the money amount from \$100 to

> \$45.80 – it would link the whole \$100 to the veteran’s account. This situation raises the question: What should a station do to clear the item from the Suspense listing? The following steps are suggested as one way to accomplish this plus provide a tracking document that will answer future questions as to how the amount was applied.

1.  Obtain a journal voucher number.
2.  Create a dummy receipt using the journal voucher number (RP Receipt Processing) making sure not to reference a deposit ticket number.
3.  Post the payment amount (NP New Payment) to the veteran’s account.
4.  Process the receipt (PR Process Receipt). Since this receipt is not linked to a deposit, a code sheet will not be generated to FMS. See step 6.
5.  Prepare a public voucher to pay the insurance company, again using the journal voucher number.
6.  Go online to FMS to create the appropriate FMS documents:
    - TR transaction to process the amount posted to the veteran’s account
    - PS transaction to process the payment to the insurance company
7.  Prepare the journal voucher annotating the different transactions accomplished to move/pay the Suspense funds.
8.  Record in the AR package under the Clear Suspense (CS) option TR/PS XXXXXX where XXXXXX represent the journal voucher number.

> Suspense Report

> The Suspense Report provides the station with a listing of those transactions that have been acted upon. The report can be useful for inquiries as to the action taken on unapplied amounts. The station will have a record as to the type of FMS transaction input, which indicates whether the amount was linked, transferred out, or paid to an entity. Unapplied amounts that were linked to an account will show on this report as "x" under CLEAR FMS DOC ID#. In order to record the FMS transaction, the station would use the Clear Suspense (CS) option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
<p>S1 Search Check CS Clear Suspense AP Account Profile S2 Search Credit Card SR Suspense Report RP Receipt Profile LP Link Payment SP Show Payment EA Exit Action Select Action: Quit//<strong>SR Suspense Report</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This action will print a report showing all unlinked payments received between selected dates that were processed to the station's suspense account and later cleared by on-line FMS input.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Start with PAYMENT Date: JUL 01, 1999// (JUL 01, 1999) End with PAYMENT Date: JUL 19, 1999// (JUL 19, 1999)</p>
<p>* Selected date range from JUL 01, 1999 to JUL 19, 1999 *</p>
<p>DEVICE: HOME//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AR CLEARED SUSPENSE REPORT JUL 19, 1999@18:07:12 PAGE 1 FOR THE DATE RANGE: JUL 01, 1999 TO JUL 19, 1999</p>
<p>RECEIPT TRAN# UNAPPLIED DEPOSIT# CLEAR FMS DOC ID# AMOUNT</p>
<p><strong>L99070700 22 L990707000022 ET 111ET9077 10.00</strong></p>
<p>L99071300 21 L990713000021 TR 111L990713 19.00</p>
<p>Press RETURN to continue:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> BLANK PAGE

## Exception Processing Due to Lockbox at the Station Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As to be expected, there will be payments received at the Lockbox that will not contain all the proper account information that will lead to same day transmission to the appropriate station. Although Exception Processing Section (EPS) staff at the Financial Services Center (FSC) will handle the majority of these payments, there will still be instances where the EPS will make a judgment call as to which station should receive these payments and forward all documentation to the station for action.

> Below is a table that lists some of the most common exceptions that the station may encounter. If a station needs further information or copies of checks, then a call should be placed to the EPS for assistance. Stations are not to call the CCPC-Lockbox unless instructed by EPS.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Exception</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EPS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Station</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Check with unacceptable payee</p>
</blockquote></td>
<td><blockquote>
<p>EPS mails check to station.</p>
</blockquote></td>
<td><blockquote>
<p>Station should deposit the check.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mangled checks/coupons</p>
</blockquote></td>
<td><blockquote>
<p>EPS mails documents to the station</p>
</blockquote></td>
<td><blockquote>
<p>Station sends mangled check to payee and requests new check.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>One check/Two or more coupons for different accounts and/or stations</p>
<p><em>If the payment is more or less than the total amount of the multiple coupons the Lockbox Bank will <u>not</u> deposit the payment. The undeposited check and coupons will be sent to EPS.</em></p>
</blockquote></td>
<td><blockquote>
<p>EPS will send the unprocessed check and all coupons to the station.</p>
</blockquote></td>
<td><blockquote>
<p>Station deposits check and processes the payment. If the payment involves another VA, station will perform transfer of funds to other station.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>One check/no coupon</p>
</blockquote></td>
<td><blockquote>
<p>EPS will review copy of check for any information recorded on the check and if station is determined, will update the file, transmit, and send correspondence to the station.</p>
</blockquote></td>
<td><blockquote>
<p>If EPS can only identify the station number, then the item will end up in the station’s suspense account.</p>
<p>From there, the station needs to follow the Link Payment instructions. If it is determined that the payment belongs to another VA, follow the Link Payment instructions for transferring payment from Suspense to the other station.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> BLANK PAGE

## Unlinked Payments Created by Lockbox Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Stations will receive a daily MailMan message informing them of what was processed through Lockbox. This message will go to members of the RCDP PAYMENTS mail group. This message gives the deposit ticket number, the receipt number, the FMS document ID number created, the total amount of the deposit, and the number of unlinked payments. Unlinked payments will be deposited to Suspense with an unapplied deposit number of L+YYMMDD+Tranasaction number where L stands for Lockbox and YYMMDD is the date of the deposit.

> Stations should review the unlinked payments under the LP Link Payments option on the Agent Cashier menu. The most common reason as to why a payment will not link is the account number (SSN) does not match an account in the station’s file. Account numbers can be off due to Lockbox scanner not reading the coupon correctly, the station has updated an account number after generation of the letters/coupons, or the payment belongs to another station for which the station number was misread by the Lockbox scanner.

> If the station cannot determine the account based on the account number and stub name given, then the EPS in Austin should be contacted for getting copies of the check(s).

> The batch and sequence number assigned by the Lockbox Bank is helpful when identifying the item(s) in question. This information is available using the Receipt Processing option. The user needs to use the Customize action and answer yes to the prompt, Do you want to show acct lookup, batch and sequence information?.

> Once the station has determined the proper account or station that the payment applies to, the station should refer back to the section, Link Payment to Account for clearing the items from Suspense.

> *Example of Lockbox MailMan message*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: Auto Payment Processing Completed [#7940488] 14 Jul 99 19:05 5 Lines From: AR Package in 'lockbox' basket. Page 1</p>
<p>The following Automatic Payment(s) have been processed by the Automatic Payment Processing Server.</p>
<p>Deposit# Receipt# FMS Document# Total Amount Unlinked Accts 003161 L99071300 CR-111K9A1034 604.92 3</p>
<p>Select MESSAGE Action: IGNORE (in lockbox basket)//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> BLANK PAGE

## Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Account Profile option

> This option allows you to profile a patient's account using List Manager screens. Once you access the Account Profile screen, you can display account, bill, and transaction information through the following List Manager actions: Bill Profile, Bill Transactions, Select New Account, and Select Status. Refer to the following examples for information about these screens.

> There are also several List Manager actions available that allow you to navigate through the screens, print information, etc. A double ?? entered at the Select Action: prompt displays these actions for selection.

> Account Profile screen

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p><strong>Account Profile Aug 24, 1999 16:00</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>:40</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Page: 1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Account: ONE,ARPATIENT(000000001)</p>
<p>Addr: 1 STREET ADDRESS, CITY, ST 00011</p>
<p>RX Copay Exempt: NO</p>
<p>ACCOUNT BALANCE: 36.21 Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DOB: JAN</p>
<p>Phone: 555</p>
<p>Payments: 0.00</p>
</blockquote></td>
<td><blockquote>
<p>01, 1700</p>
<p>555 5555</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>BillNum CareDate</strong></td>
<td><strong>Stat</strong></td>
<td><blockquote>
<p><strong>Bill Type</strong></p>
</blockquote></td>
<td><strong>Principal</strong></td>
<td><strong>Interest</strong></td>
<td><strong>Admin</strong></td>
</tr>
<tr class="odd">
<td>1 K941719 04/05/99</td>
<td>OPEN</td>
<td><blockquote>
<p>C (MEANS TEST)</p>
</blockquote></td>
<td>13.74</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED</p>
</blockquote></td>
<td>13.74</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BP Bill Profile</p>
<p>BT Bill Transactions</p>
<p>Select Action: Quit//</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NA Select New Account SS Select Status</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EA Exit Action</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> This screen displays account information such as patient demographic and billing information, and whether the patient is RX Copay Exempt.

> Bill Profile screen

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Bill Profile Aug 24, 1999 16:01:43 Page: 1 of 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>* ACCOUNTS RECEIVABLE BILL PROFILE FOR 111-K941719 *</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Account: ONE,ARPATIENT(000000001) DOB: JAN 01, 1700</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Addr: 1 STREET ADDRESS, CITY, ST 00011</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Phone: 555 555 5555</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Bill Number: 111-K941719</strong> Category: C (MEANS TEST)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Date Prepared: APR 05, 1999 Status: OPEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Date Activated: APR 05, 1999@15:34:07</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Date Status Up: APR 05, 1999 By:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Resulting From:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Type of Care: OUTPATIENT CARE(NSC)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Remark:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Interest Effective Rate Date: JAN 01, 1999 Annual Rate: .05</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Admin Effective Rate Date: JAN 01, 1999 Monthly Rate: .45</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Last Int/Admin Charge Date:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BT Bill Transactions NB Select New Bill</p>
<p>Select Action: Next Screen//</p>
</blockquote></td>
<td><blockquote>
<p>EA Exit Action</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This screen provides bill information such as patient demographics, the dates the bill was prepared and activated, the category and status.

> Bill Transactions Display

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Bill Transactions Display Aug 24, 1999 16:02:17</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Page: 1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Bill #: 111-K941719 Account: ONE,ARPATIENT(000000001) Status: OPEN Addr: 1 STREET ADDRESS, CITY, ST</p>
<p>Bill Balance: 13.74 Phone: 555 555 5555</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>00011</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Trans # TranDate Trans Type</strong></p>
</blockquote></td>
<td><strong>Principal</strong></td>
<td><strong>Interest</strong></td>
<td><strong>Admin</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/05/99 original amount</p>
</blockquote></td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 2186957 04/05/99 increase adjustment</p>
</blockquote></td>
<td>45.80</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 2187513 04/06/99 payment (in part)</p>
</blockquote></td>
<td>-32.06</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL BALANCE FOR BILL</p>
</blockquote></td>
<td>13.74</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>BP (Bill Profile) NB Select New Bill TP Transaction Profile EA Exit Action</p>
<p>Select Action: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This screen provides information such as bill and account numbers, patient demographics, and transaction information such as transaction \#, date, type, and principle, interest and administrative charges.

> Select Status action

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Account Profile Aug 24, 1999 16:00</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>:40</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Page: 1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Account: ONE,ARPATIENT(000000001)</p>
<p>Addr: 1 STREET ADDRESS, CITY, ST 00011</p>
<p>RX Copay Exempt: NO</p>
<p><strong>ACCOUNT BALANCE: 36.21</strong> Pending</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DOB: JAN</p>
<p>Phone: 555</p>
<p>Payments: 0.00</p>
</blockquote></td>
<td><blockquote>
<p>01, 1700</p>
<p>555 5555</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>BillNum CareDate Stat Bill Type</strong></p>
</blockquote></td>
<td><strong>Principal</strong></td>
<td><strong>Interest</strong></td>
<td><strong>Admin</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 K941719 04/05/99 OPEN C (MEANS TEST)</p>
</blockquote></td>
<td>13.74</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED</p>
</blockquote></td>
<td>13.74</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BP Bill Profile NA Select New Account BT Bill Transactions SS Select Status</p>
<p>Select Action: Quit// <strong>SS Select Status</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EA Exit Action</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> The Select Status action allows you to display bills for a specific status or multiple statuses. At this time, the only bills displayed are those in an Open status.

> At the Select Action: prompt, type SS to select status of bills to display.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>This option will allow you to specify which bill statuses to display.</p>
<p>The following is a list of available statuses for bills:</p>
<p>15 INCOMPLETE <strong></strong> 16 ACTIVE</p>
<p>20 PENDING APPROVAL <strong></strong> 22 COLLECTED/CLOSED</p>
<p>23 WRITE-OFF 26 CANCELLED BILL</p>
<p>27 BILL INCOMPLETE 31 RETURNED FROM AR</p>
<p><strong></strong> 39 CANCELLATION 40 SUSPENDED</p>
<p>41 REFUNDED <strong></strong> 42 OPEN</p>
<p>44 REFUND REVIEW</p>
<p> indicates account has bills under status </p>
<p>Select STATUS of bills to display:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Select Status action allows you to display bills for a specific status or multiple statuses. The list of available statuses for bills is displayed. A double asterisk \[\*\*\] next to the status indicates the account has bills with that status. You can also select all statuses by entering an asterisk \[\*\] or no statuses by entering a minus \[-\].

> To de-select a status, enter the status number again.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select STATUS of bills to display: <strong>42</strong> OPEN selected</p>
<p>The following is a list of available statuses for bills:</p>
<p>15 INCOMPLETE <strong></strong> 16 ACTIVE selected</p>
<p>20 PENDING APPROVAL <strong></strong> 22 COLLECTED/CLOSED selected</p>
<p>23 WRITE-OFF 26 CANCELLED BILL</p>
<p>27 BILL INCOMPLETE 31 RETURNED FROM AR</p>
<p><strong></strong> 39 CANCELLATION selected 40 SUSPENDED</p>
<p>41 REFUNDED <strong></strong> 42 OPEN selected</p>
<p>44 REFUND REVIEW</p>
<p> indicates account has bills under status </p>
<p>Select STATUS of bills to display: <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> As each status is selected, the word selected appears next to the status. Once you've entered all statuses you want displayed, press the Return key at the Select STATUS of bills to display: prompt.

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Account Profile Aug 24, 1999 16:00:40 Page: 1 of 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Account: ONE,ARPATIENT(000000001) DOB: JAN Addr: 1 STREET ADDRESS, CITY, ST 00011 Phone: 555</p>
<p>RX Copay Exempt: NO</p>
<p><strong>ACCOUNT BALANCE: 36.21</strong> Pending Payments: 0.00</p>
</blockquote></td>
<td><blockquote>
<p>01, 1700</p>
<p>555 5555</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>BillNum CareDate Stat Bill Type Principal Interest</strong></td>
<td><strong>Admin</strong></td>
</tr>
<tr class="odd">
<td>1 K941719 04/05/99 OPEN C (MEANS TEST) 13.74 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>2 K936439 03/12/99 ACTI RX CO-PAYMENT/NSC VET 12.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>3 K927498 02/02/99 ACTI RX CO-PAYMENT/NSC VET 8.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>4 K924944 01/19/99 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>5 K920091 01/04/99 ACTI RX CO-PAYMENT/NSC VET 2.00 0.02</td>
<td>0.45</td>
</tr>
<tr class="even">
<td>6 K917790 12/18/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>7 K917835 12/18/98 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>8 K909807 11/15/98 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>9 K906926 11/04/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>10 K906212 11/02/98 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>11 K901135 10/06/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>12 K865354 09/09/98 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td>13 K850271 06/25/98 COLL RX CO-PAYMENT/NSC VET 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="even">
<td>14 K838044 06/02/98 COLL C (MEANS TEST) 0.00 0.00</td>
<td>0.00</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>BP Bill Profile NA Select New Account EA Exit Action BT Bill Transactions SS Select Status</p>
<p>Select Action: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Account Profile screen now shows all of the bills with the statuses selected. This is a powerful tool. There is no default display.

> *The system will always display only those statuses that you select*. If the display doesn’t look right, be sure to use the Select Status action to make sure the correct statuses are selected. This action will not change any other user’s display.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> List of Receipts Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Agent Cashier Menu Option: <strong>List Of Receipts Report</strong></p>
<p>Start with RECEIPT Opened Date: AUG 01, 1999// <strong>&lt;RET&gt;</strong> (AUG 01, 1999) End with RECEIPT Opened Date: AUG 20, 1999// <strong>&lt;RET&gt;</strong> (AUG 20, 1999)</p>
<p>* Selected date range from AUG 01, 1999 to AUG 20, 1999 * DEVICE: HOME// <strong>&lt;RET&gt;</strong> TELNET</p>
<p>&lt;*&gt; please wait &lt;*&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This option prints a list of receipts opened during a selected date range.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>LIST OF RECEIPTS REPORT SEP 29, 1999@13:56:19 PAGE 2 FOR THE DATE RANGE: SEP 01, 1999 TO SEP 30, 1999</p>
<p>DATE RECEIPT TYPE US COUNT AMOUNT FMS CR DOC STATUS</p>
<p>09/29/99 SECPC9149 CASH SC 1 10.00 NOT SENT NOT ENTER</p>
<p>09/29/99 JAJIRS0046 IRS JJ 1 80.76 CR-111K9C7914 ACCEPTED</p>
<p>09/29/99 12769448 CHECK/MO FC 9 1217.46 CR-111K9C8329 ACCEPTED</p>
<p>09/29/99 JAJCWT9080 CASH JJ 1 91.43 NOT SENT NOT ENTER</p>
<p>09/29/99 L99092900 LOCKBOX ar 42 915.33 CR-111K9C7970 ACCEPTED</p>
<p>09/30/99 12769449 CASH FC 25 400.74 CR-111K0A0003 TRANSMITT</p>
<p>09/30/99 12769450 CHECK/MO FC 13 397.31 CR-111K0A0004 TRANSMITT</p>
<p>09/30/99 12769451 CHECK/MO FC 63 19483.13 CR-111K9C8461 ACCEPTED</p>
<p>09/30/99 12769452 CHECK/MO JW 70 4616.25 CR-111K9C8483 ACCEPTED</p>
<p>09/30/99 L99093000 LOCKBOX ar 92 2177.46 CR-111K9C8437 ACCEPTED</p>
<p>8856 527377.02</p>
<p>TOTALS BY TYPE OF PAYMENT</p>
<p>CASH PAYMENT 675 32127.51</p>
<p>CHECK/MO PAYMENT 5247 434443.06</p>
<p>CREDIT CARD PAYMENT 1 539.94</p>
<p>IRS PAYMENT 1 80.76</p>
<p>LOCKBOX 2929 60051.50</p>
<p>REGIONAL COUNSEL PAYMENT 3 134.25</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This report provides the date the receipt was opened, receipt number, type of payment, the user who processed the receipt, the count of payments on the receipt, the amount, the cash receipt transaction number, if applicable, and status. Counts and totals by type of payment (i.e., cash, check, money order, LBX (lockbox), TDA, DMC, IRS) are also provided. This report allows the user to compare the amount of manual transactions to those made by lockbox.

> Deposit Reconciliation Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select FMS Utilities Menu Option: <strong>Deposit Reconciliation Report</strong></p>
<p>This option will print the Deposit Reconciliation Report. The report will display the data on the code sheets sent to FMS on the CR document. Only deposits processed after patch PRCA*4.5*90 was installed can be displayed. Select the starting and ending FMS Document Number without the station number, example: K8A0346.</p>
</blockquote>
<p>START WITH CR DOCUMENT: FIRST// <strong>K9A0072</strong></p>
<p>END WITH CR DOCUMENT: K9A0072// <strong>&lt;RET&gt;</strong></p>
<blockquote>
<p>Type of report to print: summary// <strong>??</strong></p>
<p>Enter a code from the list.</p>
<p>Select one of the following: D detailed</p>
<p>S summary</p>
<p>Type of report to print: summary//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This report shows all cash receipt documents sent to FMS for a selected range. You can print a summary or detailed report.

> Deposit Reconciliation - Summary Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEPOSIT RECONCILIATION REPORT AUG 26, 1999@15:11:09 PAGE 1 START WITH DEPOSIT: K9A0072 END WITH DEPOSIT: K9A0072 TYPE: SUMMARY</p>
<p>TOTAL DEPOSITS BY FUND:</p>
<p>FUND: 1435 0.43</p>
<p>FUND: 3220 1.80</p>
<p>FUND: 5287 171.64</p>
<p>TOTAL DEPOSITS BY REVENUE SOURCE CODE FOR FUND 5287:</p>
<p>RSC: 88ZZ C (Means Test) 2.74</p>
<p>RSC: 8BZZ Pharmacy Co-Pay (SC Vet) 38.00</p>
<p>RSC: 8CZZ Pharmacy Co-Pay (NSC Vet) 126.90</p>
<p>RSC: ARRV Miscellaneous 4.00</p>
<p>Press RETURN to continue, '^' to exit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The summary report shows the total cash receipt dollars sent to FMS.

> Deposit Reconciliation - Detailed Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEPOSIT RECONCILIATION REPORT AUG 26, 1999@15:13:17 PAGE 1 START WITH DEPOSIT: K9A0072 END WITH DEPOSIT: K9A0072 TYPE: DETAILED</p>
<p>FMS DOCUMENT: CR-111K9A0072 DEPOSIT TICKET: 659501 DATE: NOV 06, 1998 LINE BFY FUND RSC PROVIDER BILL AMOUNT TRAN TYPE</p>
<p>001 99 1435 88ZZ MISCVET 0.04 23</p>
<p>002 99 1435 8BZZ MISCVET 0.39 23</p>
<p>003 99 3220 88ZZ MISCVET 1.80 23</p>
<p>004 99 5287 88ZZ MISCVET 2.74 23</p>
<p>005 99 5287 8BZZ MISCVET 38.00 23</p>
<p>006 99 5287 8CZZ MISCVET 126.90 23</p>
<p>007 99 5287 ARRV MISCVET 4.00 23</p>
<p>LINE TOTAL/DOCUMENT TOTAL: 173.87</p>
<p>DEPOSIT TOTAL: 173.87</p>
<p>Press RETURN to continue, '^' to exit:</p>
<p>DEPOSIT RECONCILIATION REPORT AUG 26, 1999@15:13:17 PAGE 2 START WITH DEPOSIT: K9A0072 END WITH DEPOSIT: K9A0072 TYPE: DETAILED</p>
<p>TOTAL DEPOSITS BY FUND:</p>
<p>FUND: 1435 0.43</p>
<p>FUND: 3220 1.80</p>
<p>FUND: 5287 171.64</p>
<p>TOTAL DEPOSITS BY REVENUE SOURCE CODE FOR FUND 5287:</p>
<p>RSC: 88ZZ C (Means Test) 2.74</p>
<p>RSC: 8BZZ Pharmacy Co-Pay (SC Vet) 38.00</p>
<p>RSC: 8CZZ Pharmacy Co-Pay (NSC Vet) 126.90</p>
<p>RSC: ARRV Miscellaneous 4.00</p>
<p>Press RETURN to continue:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The detailed report shows the individual lines in the cash receipt document sent to FMS.

> Extended Check/Credit Card Search

> This option searches all payments within a specified date range for a check or credit card number. First, specify whether the search is for a check or credit card. Then enter the number the system should look for. Next, select the Type of Match that should be performed. Choose either Exact Match - the number entered is an exact match to the check or credit card number, or Contains - the numbers entered are contained in the check or credit card number but may not be the complete number. The Contains feature is helpful if the complete check/credit card number is not available or cannot be read.

> This screen below shows how to search for a check number with a match type of contains.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Agent Cashier Menu Option: <strong>Extended Check/Credit Card Search</strong></p>
<p>Search for Check or Credit Card: Check// <strong>&lt;RET&gt;</strong> Enter the Check Number to Search for: <strong>0965</strong> Type of Match: Contains// <strong>?</strong></p>
<p>Enter a code from the list.</p>
<p>Select one of the following:</p>
</blockquote>
<ol type="1">
<li><p>Exact Match</p></li>
<li><blockquote>
<p>Contains Type of Match: Contains// <strong>&lt;RET&gt;</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Start with RECEIPT Opened Date: SEP 01, 1999//<strong>1/1</strong> (JAN 01, 1999) End with RECEIPT Opened Date: SEP 21, 1999//<strong>&lt;RET&gt;</strong> (SEP 21, 1999)</p>
<p>* Selected date range from JAN 01, 1999 to SEP 21, 1999 * DEVICE: HOME//<strong>&lt;RET&gt;</strong> TELNET</p>
<p>&lt;*&gt; please wait &lt;*&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> If the user prints this report to their screen, the date range of the search as well as the search criteria is displayed. The message PRESS ^ at anytime to STOP search will appear. This allows the user to stop the search.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>12137256</p>
</blockquote></th>
<th>04/08/99</th>
<th><blockquote>
<p>55</p>
</blockquote></th>
<th><blockquote>
<p>111-K931815</p>
</blockquote></th>
<th>80.00</th>
<th>09657923</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>12137256</p>
</blockquote></td>
<td>04/08/99</td>
<td><blockquote>
<p>56</p>
</blockquote></td>
<td><blockquote>
<p>111-K942404</p>
</blockquote></td>
<td>91.60</td>
<td>09657923</td>
</tr>
<tr class="even">
<td><blockquote>
<p>12137419</p>
</blockquote></td>
<td>04/06/99</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>111-K941901</p>
</blockquote></td>
<td>45.80</td>
<td>09654926</td>
</tr>
</tbody>
</table>

> For this example, three matches are found.

> The second example shows how to search for a credit card number with a match type of equals.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Agent Cashier Menu Option: <strong>Extended Check/Credit Card Search</strong></p>
<p>Search for Check or Credit Card: Check// <strong>Credit Card</strong></p>
<p>Enter the Credit Card Number to Search for: <strong>4098000010237183</strong></p>
<p>Type of Match: Contains// <strong>E</strong>xact Match</p>
<p>Start with RECEIPT Opened Date: SEP 01, 1999//<strong>3/1</strong> (MAR 01, 1999) End with RECEIPT Opened Date: SEP 22, 1999//<strong>3/30</strong> (MAR 30, 1999)</p>
<p>* Selected date range from MAR 01, 1999 to MAR 30, 1999 * DEVICE: HOME//<strong>&lt;RET&gt;</strong> TELNET</p>
<p>&lt;*&gt; please wait &lt;*&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Again, if the user prints this report to their screen, the date range of the search as well as the search criteria is displayed. The message PRESS ^ at anytime to STOP search will appear. This allows the user to stop the search.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EXTENDED CHECK/CREDIT CARD SEARCH SEP 22, 1999@14:39:53 PAGE 1 FOR THE DATE RANGE: <strong>MAR 01, 1999 TO MAR 30, 1999</strong></p>
<p>SEARCHING FOR: <strong>CREDIT CARD EQUALS 4098000010237183</strong></p>
<p>RECEIPT OPENDATE TRANS ACCOUNT AMOUNT CREIDTCARD#</p>
<p> PRESS ^ at anytime to STOP search </p>
<p>1717535 03/10/99 2 ONE,ARPATIENT E 12.00 4098000010237183</p>
<p>Press RETURN to continue:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> For this example, one match is found.

> BLANK PAGE

## Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Glossary

> AAC

> Austin Automation Center. VA’s data center site where CCPC resides and CCPC-Lockbox design, development and implementation occur.

> AR

> Accounts Receivable. In this context, refers to VA’s automated system designed to further process first party medical debt co-payments received electronically from CCPC-Lockbox; developed and maintained by the VHA Chief Information Office.

> Account

> Records established for an individual debtor in the AR Debtor file. One account can have any number of bills, just as a VISA or Master Card account can be used for multiple purchases.

> Accounting Classification Code (ACC)

> Nine-character codes used for budget purposes. The FMS ACC’s replace CALM fund control points.

> Accounting Technician

> The person in Fiscal Service who is responsible for processing accounting transactions.

> Account Profile

> A screen display or printout showing a summary of activity on an entire Accounts Receivable (refer to Transaction Profile for a view of a single transaction on an account).

> Accounts Receivable

> In the broadest sense, these are debts owed to the Department of Veterans Affairs. Throughout the documentation, this term is used interchangeably with the term bills for ease of expression. The Accounts Receivable section of Fiscal Service is that person or group of people whose duty it is to establish and maintain debtor account records.

> Accounts Receivable Clerk

> The person in Fiscal Service who establishes, audits and maintains the station's debt collection files.

> Adjustment

> A transaction that makes an administrative change to the principal balance of a bill or an account.

> Admin Charge

> An administrative charge incurred during the debt collection process and added to an account's principal balance. Fees for locator searches, marshal fees, and court costs are administrative charges.

> Aged Unmatched Payments

> Payments that are unmatched because station number and/or patient account number are missing and meet an age criteria of 30 days. Aged unmatched payments are recorded in the FSC FMS suspense account during the next processing of the suspense transfer and are no longer available for online matching.

> Agent Cashier

> The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.

> ADP Security Officer

> The person responsible for the security of the computer systems. This person is responsible for the computer's physical integrity and the integrity of the records stored in it. Includes overseeing who has access to which files.

> AMIS

> Automated Management Information System.

> Application Coordinator

> The individual responsible for the implementation, training and troubleshooting of the AR software package.

> Batches, Batch Types

> Groupings of payments that are related because of the form of payment, amount of payment and/or the number of documents mailed with the form of payment.

> Bill

> A receivable that has been generated by a billing service or section. See the bill types 1080, 1081, OTHER (1114), or UB-92.

> Bill for Collection

> The actual bill produced by an 1114 type billing. Formerly the second (carbon copy) page of the preprinted Form 1114 now only accessible to the Accounts Receivable Section as an electronic bill.

> Billing Clerk

> That person in a billing service or section that is responsible for generating bills.

> Billing Cycle

> The life cycle of a Bill, from generation through approval, transmission to AR, mailing to the debtor, and being liquidated by posted payments until the debt has been paid.

> Billing Document (BD)

> An FMS document created for detailed receivables by Accounts Receivable during the audit process.

> Bill Number

> Each bill has a unique number, tracked by service/section, which is used to identify it. It is usually assigned automatically by the system (see Common Bill Numbering Series).

> Budget Object Code (BOC)

> Four-digit number used to identify purchases. The FMS BOCs are equivalent to CALM subaccounts.

> Cash Receipt (CR)

> An Accounts Receivable document used to record deposit information from the SF-215 deposit ticket into FMS.

> Category C (Hospital Care)

> Entitlement category for inpatient care in a VA medical center, non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.

> Category C (Nursing Home Care)

> Entitlement category for long-term care in a VA nursing home, non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.

> Category C (Outpatient Care)

> Entitlement category for outpatient care at a VA medical center, non-service connected veterans whose income level exceeds certain minimums as determined by the MAS eligibility unit.

> CCPC

> Consolidated Copayment Processing Center System maintained at the Austin Automation Center; CCPC receives station input and generates monthly billing statements to collect first party medical debt copayments.

> Common Numbering Series

> This is a preset series of procurement DOC ID used by accounting technicians to generate new accounting transactions for AR. Application coordinators establish the common numbering series used by a facility.

> Correction

> A change made to a billing record before the initial bill is generated.

> Coupon *Synonyms: Remittance Coupon, Remittance Slip, Stub*

> The lower portion of the CCPC billing statement that is perforated for return with the payment in cash, check or credit card.

> COWC

> The Committee on Waivers and Compromises. An appellate body, located in The Department of Veterans Affairs Veterans Benefits Administration Regional Offices.

> Credit

> A payment which, when posted to an account, reduces the principal balance (the debt). Scheduled payments under a repayment plan are credits.

> Credit Card Items

> Payments processed through the Lockbox on credit cards. Due to the business rules requiring a printed remittance coupon with credit card payments, all credit card items should contain a patient account number and facility number.

> Credit/Debit Memos

> Miscellaneous adjustments to the VA account for anything other than return check items. These items are not included in the electronic transmission and are processed manually. As they are a type of payment data, manual procedures for their processing will be defined as part of the scope of the Lockbox.

> CR – *See Cash Receipt*

> Crime of Personal Violence

> The result of a crime of personal violence; occurs in a state where the victim is entitled to receive health care and services at the expense of the state or a political subdivision. Billings are forwarded to the District Counsel for collection.

> DC

> Department of Veterans Affairs' Office of the District Counsel. District Counsel areas of responsibility do not correspond to the Veterans Health Service and Research Administration regions.

> Debit

> A charge or fee which when posted to an account increases the principal balance (the debt). Interest and administrative charges are debits.

> Debit Voucher – *See SF 5515*

> Debt Collection

> This is the official name given to the process of sending out bills and collecting payments.

> Debtor

> A patient, person, vendor, insurance company or institution that owes the VA money.

> Default

> A suggested response provided by the system.

> Demand Letter

> The follow-up letters that are sent to a debtor, reminding him/her of the outstanding debt are called demand letters.

> Deposit Ticket – *See SF 215*

> Disputed Credit Card Items

> Debit transactions processed by the Lockbox for credit card transactions that were disputed by the customer and the funds returned to that person. These items are not included in the electronic transmission and are processed manually. As they are a type of payment data, manual procedures for their processing will be defined as part of the scope of the Lockbox.

> DOJ

> The United States Department of Justice.

> Electronic Signature

> The electronic signature replaces the written signature on all AR documents used within your facility. Documents going off-station will require a written signature as well. The electronic signature code is used by all individuals who have the authority to approve actions (approve requests, purchase orders, obligations, etc.). The electronic signature is encrypted so that no one, not even a computer programmer, can tell what it is.

> EPS – *See Exception Processing Section*

> Exception Processing Section, EPS

> An organization within the VA Financial Services Center in Austin established to handle CCPC- Lockbox payment resolution through queries and updates, and mail from the Lockbox bank.

> Federal Tax ID

> A unique number that identifies your station to the Internal Revenue Service.

> Financial Services Center

> VA organization in Austin; site where EPS staff resides and online CCPC-Lockbox tools will be used to resolve CCPC-Lockbox payment issues.

> FMS

> The Financial Management System that is responsible for centralized accounting.

> FMS Document ID (DOC ID)

> The station number plus a unique document number. Formerly called the CALM PAT number.

> FL 4-480

> The first demand letter for ineligible category debtors.

> FL 4-481

> The first demand letter for humanitarian category debtors.

> FL 4-482

> The second demand letter for ineligible, humanitarian and category C debtors.

> FL 4-483

> The third demand letter for debts under \$200 for medical care.

> FL 4-484

> The third demand letter for debts between \$200 and \$1200 for medical care.

> FL 4-485

> The third demand letter for debts over \$1200 for medical care.

> FL 4-513

> The first demand for category C (Means Test) debts.

> FSC – *See Financial Services Center*

> GL

> The general ledger to which all accounting transactions are posted.

> Hold

> A hold is a temporary restriction placed on mailing demand letters for a particular account. It is usually used when a debtor has made arrangements to pay the debt and letters would be redundant.

> Humanitarian

> Humanitarian billings are for non-veterans treated at a VA facility for a medical emergency. Also includes veterans treated under presumed eligibility later found to be ineligible.

> ICD

> Interest computation date. Usually the date of the first demand letter. (NOTE: Do not confuse this with the International Classification of Disease codes — usually referred to as the ICD-9 Codes.)

> Identified Return Items

> Return items for which the EPS staff was able to associate account and station number. Once identified, hardcopies of these items are sent to the appropriate station.

> Ineligible

> Ineligibles are veterans who have received medical care at a VA facility, but were later found not entitled to such service.

> Integrated Billing

> Integrated Billing (IB) is a software package that acts as an interface between the service that establishes a debt and the billing process in AR.

> Invoice Address

> The address printed on a purchase order to instruct the vendor where to mail his/her invoice.

> Insurance Company File

> File Number 36 holds information about the insurance companies that your station does business with. Debtor's address may be drawn from this file but is maintained separately. If the desired company is not in the file, contact MAS to have it added.

> Interest

> Amount charged to an account being paid on a repayment plan for carrying the account or on delinquent accounts.

> Matched Payments *Synonym: Original Receipts; Original Messages; Matched Receipts.* Electronic payments for which the Lockbox bank information identifies the station to which a payment applies; typically also identifies to which patient account a payment applies; forms of payment may be cash, check or charge.

> National Roll-Up

> The National Roll-Up software includes a central database to reside at the San Francisco CIO Field Office and interface software to reside at each field station. The interface software collects Accounts Receivable data from AR Version 4.5 and sends this data to the central database. The CIO field office will then process the AR data collected to centrally produce, for all sites, the VA Schedule 9 Report for the U.S. Treasury.

> No-fault Auto Accident

> Used for medical care required as the result of a motor vehicle accident in a state that has no- fault automobile insurance.

> Non-Cash CR

> A CR document automatically created by the AR system to reflect the electronic receipt of funds via the Lockbox. No cash is actually received at the sites for these credit amounts to their account but they must still record the electronic deposit of the money to FMS. Each station that receives money for each fund the money is applied to will create one document.

> OFM

> Office of Financial Management.

> Overpayment Document (OP)

> FMS document used to create manual refunds to veterans, insurance companies, etc. Formerly a

> 972.13 CALM code sheet.

> PAT Number

> Formerly, a unique number used to identify a CALM document. FMS DOC ID replaces the CALM PAT.

> Patient Statement of Account

> The monthly statement for patient type debtors, reflecting all activity (both charges and payments) recorded for that patient since his last statement was printed.

> Premature Payments

> Lockbox payments for VA facilities that are not yet capable of accepting electronic payments from the CCPC-Lockbox application. Premature payment amounts are recorded in FSC suspense via the CR transaction. EPS is required to review premature payment records in Lockbox and to

> take action outside Lockbox to transfer the funds to the VA facility. Following full-scale implementation of CCPC-Lockbox, occurrence of this condition should be rare.

> RD

> Regional Director.

> Referral Amount

> Threshold amounts that determine (often independently) which accounts are referred to the District Counsel or the Department of Justice.

> Repayment Plan

> If a debt is so large that the debtor can't repay it in a lump sum a repayment plan may be established to pay it in regularly scheduled installments. Can be established by the fiscal officer or as the result of negotiations with the District Counsel or Department of Justice.

> Return Items

> Checks that have been returned to the Lockbox for insufficient funds and have been debited from the VA bank account. These items are included in the daily Federal Express package. For the purposes of this document, Return Items will be treated as a distinct activity for payments made by check, which is different than other debit voucher adjustments.

> Schedule 9

> A detailed report of receivables due to the VA. It categorizes receivables by age and status. With the release of the National Roll-up software, Schedule 9 will be centrally produced in San Francisco.

> Site Parameters

> Information (such as station number, cashier's address, billing address, etc.) that is unique to your station. All of AR uses a single Site Parameter file.

> SF 215, Standard Form 215, Deposit Ticket

> A standard government form used to record monetary deposits to VA, processed through the

> U.S. Treasury Department. Each deposit ticket is numbered and dated; together, the number and date make a document unique.

> SF 5515, Standard Form 5515; Debit Voucher

> A standard government form used to record debits to VA, processed through the U.S. Treasury Department. Each debit voucher is numbered and dated; together, number and date make a document unique.

> Stub *See Coupon.*

> Sub-BOC

> Two-digit code used with payroll BOCs.

> Tasked Job

> A job, usually a printout, which has been scheduled to run at a predetermined time in the future. Tasked jobs are set up to run without having a person watching over them.

> Tort Feasor

> Used for medical care provided as the result of a crime. A type of billing in which a firm receivable is not recorded until it is paid.

> Transaction

> Any action that affects a bill or an account. All transactions are numbered sequentially and can be examined individually.

> Transaction Number

> A number assigned by the computer for an activity against a debt (such as increase adjustment, decrease adjustment, payment, etc.)

> Transaction Profile

> A screen display or printout that shows a summary of a single transaction.

> UB-92

> Uniform Bill 92 is a statement of charges for medical care used for all patient billing. Its use is restricted to the IB portion of the medical administration automated system.

> Unmatched Payment *Synonym: Secondary Receipts; Secondary Messages; Secondary Payments.*

> Check and cash payments that are transmitted to AAC CCPC-Lockbox that lack enough information to identify to which station and/or which patient account they apply; require manual intervention of EPS staff to resolve using Lockbox-supplied queries and related pieces of mail; may require AR personnel to resolve once the station is identified. A payment could be considered unmatched for a number of reasons, including but not limited to the following items:

- payments received without a remittance slip and no or only a partial account number written on the check
- cash received with no remittance coupon
- remittance coupon unreadable

> VA Form 1080

> A billing form used to transfer funds from one government agency to another when a check will be issued.

> VA Form 1081

> A billing form used to bill other government agencies.

> VA Form 1114

> This form has been discontinued and has been replaced by the electronic bill of collection.

> Vendor File

> An AR file of all the vendors the facility does business with. This file, File \#440, contains ordering and billing address, contract information, and telephone numbers. The debtor's address may be drawn from this file, but is maintained separately. The vendor must be established by Austin to be added to FMS files.

> Worker's Compensation

> Usually referred to as Worker's Comp. Medical care provided as a result of an incident/accident occurring during a veteran's employment and covered by the Office of Worker's Compensation Program (OWCP).

> Write-off Document (WR)

> FMS document created to record an Accounts Receivable write-off.

## Sample Patient Statement and Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](accounts-receivable-version-4-5-lockbox-training-guide/006.png)

> Transfer payment from Suspense message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: Transfer Payment From Suspense Rec/# L99071300/21 [#7970030] 21 Jul 99 17:29 19 Lines</p>
<p>From: AR Package in 'IN' basket. Page 1 NEW</p>
<p>The following payment has been processed to an Account in AR and needs to be moved from the station's suspense account 3875 to</p>
<p>the appropriation/fund identified for this account online in FMS.</p>
<p>Receipt Number: L99071300 Payment Transaction Number: 21</p>
<p>Unapplied Deposit Number: L99071300021 FMS CR document ID: CR-111K9A1034</p>
<p>Amount Paid: 19.00</p>
<p>Process Date: JUL 14, 1999</p>
<p>Select MESSAGE Action: IGNORE (in lockbox basket)//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Lockbox Auto Payment Processing Completed message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: Auto Payment Processing Completed [#7940488] 14 Jul 99 19:05 5 Lines From: AR Package in 'lockbox' basket. Page 1</p>
<p>The following Automatic Payment(s) have been processed by the Automatic Payment Processing Server.</p>
<p>Deposit# Receipt# FMS Document# Total Amount Unlinked Accts 003161 L99071300 CR-111K9A1034 604.92 3</p>
<p>Select MESSAGE Action: IGNORE (in lockbox basket)//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> FMS Cash Receipt Document Rejected message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: FMS Cash Receipt Document Rejected [#1234488] 11 Jul 99 17:55 9 Lines From: AR Package in 'lockbox' basket. Page 1</p>
<p>The following CR FMS document rejected and needs to be retransmitted.</p>
<p>Document: CR-111K9A0616</p>
<p>You may regenerate this cash receipt document by selecting the Option Process Receipt (PR) located under the Receipt Processing Listmanager screen.</p>
<p>This cash receipt document was generated by receipt 12768927. Select MESSAGE Action: IGNORE (in lockbox basket)//</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> How will the stations record the amounts received at the Lockbox?

> Receipt and deposit data will be transmitted to the medical centers on a daily basis. The transmission records will be automatically posted to a patient’s account.

> Can the agent cashier at the medical center still receive payments against a patient’s account?

> Yes, it will still be possible to receive payment information at the medical centers.

> What about patients who send back prescription refills with their payment?

> Prescription refills, letters, address changes and other correspondence received at the Lockbox site will be sent to the Austin Automation Center. These items will be sorted and sent to the appropriate station.

> Why I am not receiving the MailMan messages?

> Users should check to see if they are a member of the RCDP PAYMENTS mail group.

> I need to get a copy of the check processed by Lockbox. Who do I call and what information will they need?

> The user will call the EPS and provide the deposit number, deposit date, batch number, sequence number, and amount.

> I called EPS for assistance and they are asking me for a batch and sequence number. Where can I find this information?

> This information is available under Receipt Processing. The use needs to use the customize action and answer YES when prompted to display account lookup, batch and sequence information.

> How do I deposit funds to the bank?

> Before this software update, users would approve a receipt (step 1) and then deposit to the bank (step 2) in order to generate the FMS CR document. These steps are now accomplished with the Process Receipt (PR) option that posts the payments to the accounts plus generates the FMS document.

> I have posted a payment on the wrong receipt. Can I correct this?

> As long as the receipt has not been processed, the user can move the payment from one type receipt to another. In the past, the user could only move a cash payment to a check payment. With this new software, the user can move any type payment from one receipt to another.

> I linked a payment to an account but the funds are still in my station's FMS suspense account. Why?

> Stations are required to do on-line input for items that have posted to Suspense in FMS. The software will not generate an FMS document to clear these funds from Suspense.

> I What portion of my workload will lockbox process?

> During testing, the lockbox processed an average of 45% of all the transactions for the stations. The List of Receipts Reports option provides information on all types of receipts. It summarizes volumes and dollar values for the date range selected.

## Troubleshooting Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Account Profile screen doesn’t display all the bills for an account.

> Use the Select Status action to change the list of bills that will display on the Account Profile. See the Profiles section of this guide to see how to use the Select Status action.

> The Receipt Profile screen doesn’t display the check and credit card information for a payment.

> Use the Customize action to customize the screen display and options used when processing receipts.