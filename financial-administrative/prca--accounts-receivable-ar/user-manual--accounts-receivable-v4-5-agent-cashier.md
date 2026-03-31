---
title: Accounts Receivable Version 4.5 User Manual - Agent Cashier
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Agent Cashier
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
menu_options: 16
description: - [![](accounts-receivable-version-4-5-user-manual-agent-cashier/001.png) Agent Cashier Menu](#accounts-receivable-version-4-5-user-manual-agent-cashier001png-agent-cashier-menu) - [Cash Payment](#cash-payment) - [Check/MO Payment](#checkmo-payment) - [Credit Card Payment](#credit-card-payment) - [O
audience: 
keywords: 
  - payment
  - receipt
  - deposit
  - table
  - contents
  - test
  - ticket
  - number
  - transaction
  - date
page_count: 0
word_count: 5248
section_count: 23
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/1agentca_r0515.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/1agentca_r0515.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

# ![](accounts-receivable-version-4-5-user-manual-agent-cashier/001.png) Agent Cashier Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [![](accounts-receivable-version-4-5-user-manual-agent-cashier/001.png) Agent Cashier Menu](#accounts-receivable-version-4-5-user-manual-agent-cashier001png-agent-cashier-menu)
  - [Cash Payment](#cash-payment)
  - [Check/MO Payment](#checkmo-payment)
  - [Credit Card Payment](#credit-card-payment)
  - [OTHER PAYMENT](#other-payment)
  - [Cancel a Payment Transaction](#cancel-a-payment-transaction)
  - [MOVE A PAYMENT TRANSACTION](#move-a-payment-transaction)
  - [Patient payment/refund transaction history report](#patient-paymentrefund-transaction-history-report)
  - [BRIEF ACCOUNT PROFILE](#brief-account-profile)
  - [DEPOSIT MANAGEMENT](#deposit-management)
  - [CREATE DEPOSIT TICKET](#create-deposit-ticket)
  - [DEPOSIT MONEY TO BANK](#deposit-money-to-bank)
  - [EDIT A DEPOSIT TICKET](#edit-a-deposit-ticket)
  - [RECEIPT LIST FOR DEPOSIT](#receipt-list-for-deposit)
  - [SUMMARY LISTING OF DEPOSITS](#summary-listing-of-deposits)
  - [VIEW A DEPOSIT](#view-a-deposit)
  - [VOID A DEPOSIT](#void-a-deposit)
  - [FULL ACCOUNT PROFILE](#full-account-profile)
  - [Print 215 Report](#print-215-report)
  - [Profile of Accounts Receivable](#profile-of-accounts-receivable)
  - [Release Holds on AR](#release-holds-on-ar)
  - [RECEIPT MANAGEMENT](#receipt-management)
    - [Approve a Receipt](#approve-a-receipt)
    - [EDIT A RECEIPT](#edit-a-receipt)
    - [LIST OF RECEIPTS](#list-of-receipts)
    - [Post an Approved Receipt to Accounts](#post-an-approved-receipt-to-accounts)
    - [Receipt Number Reconciliation Report](#receipt-number-reconciliation-report)
    - [REPRINT A CUSTOMER'S RECEIPT](#reprint-a-customers-receipt)
    - [Summary of Current Receipts](#summary-of-current-receipts)
    - [VOID A RECEIPT](#void-a-receipt)
  - [Transaction Profile](#transaction-profile)

## Cash Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option logs cash payments for posting at the end of the day. Payments must be made by cash, either mailed or at the window to be entered under this option. These payments are batched, or grouped, under a receipt number to be posted to the accounts at a later time. The receipt number under which these payments are logged exists in the system for a period of time. Within this time period you should (1) approve the receipt, (2) post the receipt, and (3) reconcile the posted receipts.

Your response to the "Patient Name" or "Bill Number" prompt is used to store where the payment should be applied. If the payment is associated to a specific bill, then the payment will be applied to that bill first and any money left over will be applied to the oldest bills the patient has remaining. If the bill is not a patient bill, then the money will be applied to the specific bill and any money left over will not be posted but flagged in a message on the reconciliation report as an overpayment. A message will also be displayed if the following is true:

- The patient is exempt from co-payment charges.
- The patient has arranged to pay for prescriptions before the prescriptions have been filled.

If this field is associated with a patient name, then the software will automatically search the patient’s bills and apply payments, beginning with the oldest bill, until the payment is exhausted. A prepayment will be created when the payment is not exhausted.

When prompted for the payment amount, you can view the account balance for which you are applying the payment; for example, \<25.00\>. This allows you to inform the customer about their current balance without extensive research for account information.

Select Agent Cashier Option: CS Cash Payment

RECEIPT \#: CASH001 ONE,TEST. 10-21-94 CASH

DEPOSIT TICKET:888888//\<ret\> 10-21-94 JOE \$0.00 OPEN

Receipt \#CASH001 Payment Type: CASH

---------------------------------------------

PATIENT NAME OR BILL NUMBER: ARpatient,ONE

PAYMENT AMOUNT: \<50.00\>// 20.00

DATE OF PAYMENT: TODAY//\<ret\> (OCT 22, 1994)

Is the data entered correct? YES//\<ret\>

Do you want to print a RECEIPT? YES//\<ret\>

## Check/MO Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option logs a customer's payment for posting at the end of the day. The payment must be made by check or money order for it to be entered under this option.

Typical uses are entering mail-in or window payments by check or money orders. The information necessary to successfully log this type of payment transaction include the check number, bank number, and the date of the check.

Select Agent Cashier Option: CHECK/MO Payment

RECEIPT \#: CHECK001 ARpatient,ONE 10-21-94 CHECK/MO PAYMENT

DEPOSIT TICKET:888888//\<ret\> 10-21-94 JOE \$0.00 OPEN

Receipt \#CHECK001 Type: CHECK/MO

---------------------------------------------

PATIENT NAME OR BILL NUMBER: ARpatient,ONE

PAYMENT AMOUNT: \<30.00\>// 15.00

DATE OF PAYMENT: TODAY//\<ret\> (OCT 22, 1994)

CHECK \#: 1002034

BANK \#: 12345678

DATE OF CHECK: T (OCT 22, 1994)

Is the data entered correct? YES//\<ret\>

Do you want to print a RECEIPT? NO//\<ret\>

## Credit Card Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option logs a customer's payment for posting at the end of the day. The payment must be made by credit card for it to be entered under this option.

Typical uses for this option include window payments by credit card. Necessary information for logging this transaction is the same basic information required when entering cash payments, but instead of asking for a field service receipt, it asks for a batch summary number, the credit card number, and the confirmation number.

Select Agent Cashier Option: credit Card Payment

BATCH SUMMARY \#: PLASTIC01

ARE YOU ADDING 'PLASTIC01' AS A NEW AR BATCH PAYMENT? Y (YES)

Receipt \#PLASTIC01 Type: CREDIT CARD

---------------------------------------------

PATIENT NAME OR BILL NUMBER: ARpatient,ONE

PAYMENT AMOUNT: \<15.00\>// 10.00

DATE OF PAYMENT: TODAY//\<ret\> (OCT 22, 1994)

CREDIT CARD \#: 1234567890

CONFIRMATION \#: OK

Is the data entered correct? YES//\<ret\>

Do you want to print a RECEIPT? NO// YES

## OTHER PAYMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option logs a payment transaction for payments other than cash, check/money order, or credit card. When selected, the system will prompt you for one of the following.

IRS Payment

District Counsel Payment

Department of Justice Payment

Transfer of Disbursing Authority (TDA) payment.

The following prompts for each payment type include:

| System Prompts              |
|---------------------------------|
| Receipt \# (Summary \# for TDA) |
| Deposit Ticket                  |
| Patient Name or Bill \#         |
| Payment Amount                  |
| Date of Payment                 |
| Check \#                        |
| Bank \#                         |
| Date of Check                   |

Select Agent Cashier Option: OP Other Payment

TYPE OF PAYMENT: ??

CHOOSE FROM:

DEPT OF JUSTICE PAYMENT

DISTRICT COUNSEL PAYMENT

IRS PAYMENT

TDA PAYMENT

TYPE OF PAYMENT: IRS PAYMENT

RECEIPT \#: IRSPAY01

ARE YOU ADDING 'IRSPAY01' AS A NEW AR BATCH PAYMENT? Y (YES)

DEPOSIT TICKET:888888//\<ret\> 10-21-94 TEST,ONE \$0.00 OPEN

Receipt \#IRSPAY01 Type: INTERNAL REVENUE SERVICE

---------------------------------------------

PATIENT NAME OR BILL NUMBER: ARpatient,ONE

PAYMENT AMOUNT: \<150.00\>// 130.00

DATE OF PAYMENT: TODAY//\<ret\> (OCT 22, 1994)

CHECK \#: 123456578

BANK \#: 123456769

DATE OF CHECK: T (OCT 22, 1994)

Is the data entered correct? YES//\<ret\>

Do you want to print a RECEIPT? NO//\<ret\>

## Cancel a Payment Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option cancels a payment transaction that was entered under a cashiers receipt.

This option is often used to correct payments made in error. For example, entering the wrong information accidentally. This will not remove the transaction, but reverses it out, thereby leaving an audit trail of the entry of the first transaction.

To complete the correction process, the cashier returns to the payment entry option and enters the correct payment. This should be done before posting to ensure correct reconciliation reports.

Select Agent Cashier Option: CANCEL a Payment Transaction

RECEIPT \#: IRSPAY01 RANDY 10-22-93 IRS PAYMENT

Select TRANSACTION: ??

CHOOSE FROM:

1 ARpatient,ONE \$3.00

2 ARpatient,TWO \$50.00

Select TRANSACTION: 2 ARpatient,TWO \$50.00

Are you sure you want to cancel transaction \#2 ? NO// YES

CANCELLATION COMMENT: Check amount was in error!!

## MOVE A PAYMENT TRANSACTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option moves a cash payment transaction from a cash receipt to check/money order receipt. The only requirement is that the receipt must be a cash receipt and it can not have been approved.

An example for using this option is the case that a customer says they wish to pay by cash. You may have all the information entered under your cash receipt, but the customer realizes they have no cash and therefore must pay by check. You can use this option to facilitate the process of canceling the transaction from one receipt and re-entering the information in a different receipt.

Select Agent Cashier Option: MOVE A Payment Transaction

OK, Enter the Receipt \# and then payment transaction you want to move ...

RECEIPT \#: CASH001 ARpatient,ONE 10-21-94 CASH PAYMENT

Select TRANSACTION: 2// ??

CHOOSE FROM:

1 ARpatient,TWO \$0.00

2 ARpatient,THREE \$20.00

Select TRANSACTION: 2// 2 ARpatient,THREE \$20.00

OK, now enter the receipt you want to move this transaction to ...

RECEIPT \#: CHECK001 ONE,TEST 10-21-93 CHECK/MO PAYMENT ...OK, New transaction \#4 created!

OK, you are in Receipt \#CHECK001 editing your new transaction ...

Receipt \#CHECK001 Type: CHECK/MO

---------------------------------------------

PATIENT NAME OR BILL NUMBER: ARpatient,ONE //\<ret\>

PAYMENT AMOUNT: 20.00//\<ret\>

DATE OF PAYMENT: OCT 22,1994//\<ret\>

CHECK \#: 1234567

BANK \#: 123456789

DATE OF CHECK: T (OCT 22, 1994)

Is the data entered correct? YES//\<ret\>

Do you want to print a RECEIPT? NO//\<ret\>

## Patient payment/refund transaction history report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists a history of payment/refund transactions for a patient and a given date range.

Use this report to respond to patient questions concerning their payments or refunds. It will provide information about the amount applied towards fees, charges, and services.

Select Agent Cashier Option: PATIENT Payment/Refund Transaction

Select Patient : ARpatient,ONE

...OK? YES//\<ret\> (YES)

Payment history beginning date: (1/1/88 - 10/22/93): Sep 22, 1994//\<ret\>

Payment history ending date: (9/22/93 - 10/22/93): Oct 22, 1994//\<ret\>

DEVICE: HOME//\<ret\> VIRTUAL

Patient Payment History Report

------------------------------

For Patient: ARpatient,ONE

SSN : 000111111

For dates: Sep 22, 1993-Oct 22, 1994

DATE OF

PAYMENT/REFUND BILL \# REFUND RECEIPT \# AMOUNT PRIN. INT ADM

------------------------------------------------------------------------------

Oct 22, 1993 000-K420188 CHECK001 15.00 15.00 0.00 0.00

Oct 22, 1993 000-K420188 CHECK001 20.00 20.00 0.00 0.00

Oct 22, 1993 000-K420188 IRSPAY01 3.00 3.00 0.00 0.00

Total Principal Paid: 38.00

Total Interest Paid: 0.00

Total Admin Paid: 0.00

Total Paid: 38.00

Total Refund: 0.00

## BRIEF ACCOUNT PROFILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays all *outstanding* bills and payments for a given account. Outstanding bills include bills with a status of *Open, Active, or Refund Review.* The profile groups bills by their status and includes a total balance of all bills with that status. The option also allows you to view a bill and any of its associated transactions.

This profile is helpful when quickly searching a patient's account for bills and viewing transactions. After viewing the profile, the system will prompt for a transaction that appears on the profile. Simply enter the number of the transaction and view a descriptive profile for that transaction.

Payments that appear in the profile indicate that they are applied to the account but haven't been posted against a bill. Once their respective receipt is approved, those payments will be applied to outstanding bills or a prepayment bill.

=================== A c c o u n t P r o f i l e ===================

ARpatient,ONE (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 1.00

Phone \#: N/A RX Copay Exempt: NO

\# Bill \# Est Type Paid Prin Int Adm Balance

------------------------------- PAYMENTS (-1.00) --------------------------

\* CHECK002-1 PAYMENT -1.00 0.00 0.00 0.00 -1.00

--------------------------------- OPEN (2.00) -----------------------------

1 000-K420188 10/22/93 RX CO-P 48.00 2.00 0.00 0.00 2.00

Select 1-1: 1

==================== A c c o u n t P r o f i l e ===================

ARpatient,ONE (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 1.00

Phone \#: N/A RX Copay Exempt: YES

Bill \#: 000-K420188

\# Tr \# Type Date Amount

---------------------------------------------------------------------------

Original Amount 10/22/93 0.00

1 1202 INCREASE ADJUSTMENT 10/22/93 50.00

2 1205 PAYMENT (IN PART) 10/22/93 15.00

3 1206 PAYMENT (IN PART) 10/22/93 20.00

4 1207 PAYMENT (IN PART) 10/22/93 3.00

5 1208 PAYMENT (IN PART) 10/22/93 10.00

------

\$ 2.00

Select 1-5 or 'P' to Print:

> **NOTE:** All bills are categorized by their status. Also, note the asterisk beside the payment in the profile of the account (top). This indicates that the payment has not been posted. Once posted against an active bill, this transaction will appear under the profile of that bill.

![](accounts-receivable-version-4-5-user-manual-agent-cashier/002.png)

## DEPOSIT MANAGEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains a list of options necessary for managing deposits. This menu can only be used for payments against accounts/bills. This menu should not be used for deposits to Patient Funds, General Post Funds, Supply Funds, Suspense, or Compensated Work Therapy (CWT) Programs. Deposits to these funds must be done manually or on-line with FMS.

## CREATE DEPOSIT TICKET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to create a deposit ticket on which receipts can be applied. The ticket number must be formatted to begin with 1 alpha character followed by 6 numeric digit characters a total of 7 characters in length and may not be repetitive. (Cannot use a previous ticket number.) Immediately after creating a ticket number the user is asked if they wish to edit the Deposit Ticket. The default is NO and will then exit the user and allow receipts to be applied to that ticket number.

The alpha prefix is required when entering deposit ticket numbers in VistA. Transactions for any given deposit ticket number must be recorded using the same alpha prefix.

Alpha prefixes A through O are available for OTCnet deposits generated by individual stations.

Alpha prefixes P through X are available for OTCnet deposits generated by and recorded by CPACs

The Y prefix is reserved for credit card deposits generated by and recorded by CPACs on behalf of other stations.

The Z prefix is reserved for credit card deposits generated by and recorded by the station.

The below procedures explain how to create the 6-digit deposit ticket number for recording credit card deposit.

- The first 2 digits = 99
- The third digit = The current FISCAL year
- The fourth through sixth digits = The Julian date of the deposit.

Deposit Ticket Number: A213456

\*\*\* OK, Deposit Ticket 'A213456' Created \*\*\*

Do you want to EDIT this Deposit Ticket? NO//\<ret\>

## DEPOSIT MONEY TO BANK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to approve a ticket for deposit to a bank. If a deposit ticket has no receipts associated with it, a message will appear indicating such.

Select Deposit Management Option: DEPosit Money to Bank

Select TICKET NUMBER to DEPOSIT: 312321// 06-14-94 ONE,TEST \$50.00 OPEN

DEPOSIT TICKET

Ticket \#: 312321 AUG 16,1994 09:55

=============================================================================

Opened By: ONE,TEST JUN 14,1994 13:18

Deposited By:

Confirmed By:

Agency Title: SITE (DEPOSIT) Bank Name: TEST BANK (CENTRAL)

Status of Ticket: OPEN Agency Loc. Code: 1090000-1

Bank Trace Number: Presented to Bank: JUN 14,1994

Number of Receipts: 3 Bank Deposit Date:

Deposit Amount: \$50.00

-----------------------------------------------------------------------------

Comment:

Is this OK? YES// ... Approved for Deposit

## EDIT A DEPOSIT TICKET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to change information on a deposit ticket. Information that can be changed includes the Date Presented to Bank, Amount of Deposit, Bank name, Agency Title, ALC, and any Comments associated with the Deposit Ticket. A deposit ticket which has been approved and deposited cannot be edited.

Select Deposit Management Option: EDIT a Deposit Ticket

Select TICKET NUMBER to DEPOSIT: 654332// 06-14-94 ONE,TEST \$30.00 OPEN

DEPOSIT TICKET

Ticket \#: 654332 AUG 16,1994 13:24

=============================================================================

Opened By: ONE,TEST AUG 16,1994 13:19

Deposited By:

Confirmed By:

Agency Title: Bank Name:Mid-State

Status of Ticket: OPEN Agency Loc. Code:

Bank Trace Number: Presented to Bank:

Number of Receipts: 3 Bank Deposit Date:

Deposit Amount: \$30.00

-----------------------------------------------------------------------------

Comment:

DATE PRESENTED TO BANK: TODAY// (AUG 16, 1994)

AMOUNT OF DEPOSIT: 50.00

BANK: TEST BANK (CENTRAL)// TEST BNK BANK (DEPOSIT)

AGENCY TITLE: SITE (DEPOSIT)// SITE (DEPOSIT)

AGENCY LOCATION CODE: 1090000-1//

COMMENTS:

Edit? NO//

*The Deposit Ticket screen appears again to show changes...*

DEPOSIT TICKET

Ticket \#: 654332 AUG 16,1994 13:24

=============================================================================

Opened By: ONE,TEST AUG 16,1994 13:19

Deposited By:

Confirmed By:

Agency Title: SITE (DEPOSIT) Bank Name: TEST BNK

Status of Ticket: OPEN Agency Loc. Code: 1090000-1

Bank Trace Number: Presented to Bank: AUG 16,1994

Number of Receipts: 0 Bank Deposit Date:

Deposit Amount: \$50.00

-----------------------------------------------------------------------------

Comment:

Is this OK? YES//

## RECEIPT LIST FOR DEPOSIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option shows information associated with receipts that are attached to selected deposit tickets. The user is prompted for a specific deposit ticket and then whether or not they wish to see the information displayed to the screen or reproduced on hard copy. An example of this follows.

Select Deposit Management Option: RECeipt List for Deposit

Select AR DEPOSIT TICKET \#: 4321 05-26-94 ONE,TEST \$50.25 PROCESSED

DEVICE: VIRTUAL RIGHT MARGIN: 80//

Receipt List for Deposits

=============================================================================

Ticket \#: 4321

Bank: TEST BANK (CENTRAL) Bank Trace \#: 000111111

Deposited By: ONE,TEST. Status: PROCESSED

Bank Deposit Date: MAY 26,1994 Agency Loc. Code: 1090000-1

Amount of Deposit: \$50.25 Total Receipts: 1

-----------------------------------------------------------------------------

Date Opened Approved \# of

Receipt \# Opened Type By By Trans. Status

1234321 05/26/94 CHECK/MO ONE,TEST ONE,TEST 2 POSTED

Select AR DEPOSIT TICKET \#:

## SUMMARY LISTING OF DEPOSITS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By choosing this option, the user is able to view information about past and current deposit tickets. This information can be viewed both in brief and in expanded format as the example will show. The expanded format allows the user to view any comments that are associated with a deposit ticket number. In both cases the report can be sorted by date.

Select Deposit Management Option: SUMmary Listing of Deposits

Do you want a BRIEF or EXPANDED Listing? BRIEF//

START WITH DATE/TIME OPENED: FIRST//

DEVICE: VIRTUAL RIGHT MARGIN: 80//

AR DEPOSIT LIST AUG 17,1994 06:44 PAGE 1

TICKET DATE DEPOSITED CONFIRMED TOTAL

\# OPENED OPENED BY BY BY RECEIPTS STATUS

-----------------------------------------------------------------------------

4321 05/26/94 ONE,TEST ONE,TEST ONE,TEST 1 PROCESSED

9876 07/06/94 TWO,TEST TWO,TEST 0 DEPOSITED

9999 07/06/94 THREE,TEST 1 OPEN

## VIEW A DEPOSIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By using the VIEW option of the deposit menu, the user can view detailed information about a specific deposit ticket.

Select Deposit Management Option: VIEW a Deposit

Select AR DEPOSIT TICKET \#: 4321 05-26-94 ONE,TEST \$50.25 PROCESSED

DEPOSIT TICKET

Ticket \#: 4321 AUG 17,1994 06:52

=============================================================================

Opened By: ONE,TEST MAY 26,1994 15:03

Deposited By: ONE,TEST MAY 26,1994 15:06

Confirmed By: ONE,TEST MAY 26,1994 15:06

Agency Title: Bank Name: TEST BANK (CENTRAL)

Status of Ticket: PROCESSED Agency Loc. Code: 1090000-1

Bank Trace Number: 000111111 Presented to Bank: MAY 26,1994

Number of Receipts: 1 Bank Deposit Date: MAY 26,1994

Deposit Amount: \$50.25

-----------------------------------------------------------------------------

Comment:

Select AR DEPOSIT TICKET \#:

## VOID A DEPOSIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to void a deposit ticket. A ticket cannot be voided if receipts are associated with it. In such a case, the receipts must first be transferred to another deposit ticket using the Edit a Receipt Option.

Select Deposit Management Option: VOID a Deposit

Select AR DEPOSIT TICKET \#: 77777 07-06-94 ONE,TEST \$0.00

OPEN

Do you want to void this deposit? NO// YES ...Done

## FULL ACCOUNT PROFILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays all *non-outstanding* and *outstanding* bills and payments for a given account. This means bills with any status. The profile groups bills by their status and includes a total balance of all bills with that status. The option also allows you to view a bill and any of its associated transactions. The header information includes the Service-Connected (SC %) percentage and any Special Authorities (SA) for the patient to provide a better understanding of the whole account.

This profile is helpful when quickly searching a patient's account for bills and viewing transactions. After viewing the profile, the system will prompt for a transaction that appears on the profile. Simply enter the number of the transaction and view a descriptive profile for that transaction.

Payments that appear in the profile indicate that they are applied to the account but haven't been posted against a bill. Once their respective receipt is approved, those payments will be applied to outstanding bills or a prepayment bill.

================ A c c o u n t P r o f i l e ==================

ARpatient,ONE (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: YES

SC Combined %: 80%

SC / SA: Agent Orange

(SC\>50)

\# Bill \# Est Type Paid Prin Int Adm Balance

--------------------------- COLLECTED/CLOSED (0.00) ----------------------

1 000-K400145 08/31/92 RX CO-P 54.50 0.00 0.00 0.00 0.00

2 000-K400155 09/01/92 RX CO-P 58.00 0.00 0.00 0.00 0.00

3 000-K401314 07/21/93 RX CO-P 2.00 0.00 0.00 0.00 0.00

----------------------------- CANCELLATION (0.00) ------------------------

4 000-K400201 11/18/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

--------------------------------- OPEN (2.00) ----------------------------

5 000-K401883 10/22/93 RX CO-P 48.00 2.00 0.00 0.00 2.00

------------------------------- REFUNDED (0.00) --------------------------

6 000-K400042 08/20/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

Select 1-6 or return to continue: 2

================ A c c o u n t P r o f i l e ==================

ARpatient,ONE (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: NO

Bill \#: 000-K400155

SC Combined %: 80%

SC / SA: Agent Orange

(SC\>50)

\# Tr \# Type Date Amount

--------------------------------------------------------------------------

Original Amount 09/01/92 0.00

1 65 INCREASE ADJUSTMENT 09/01/92 4.50

2 66 INCREASE ADJUSTMENT 07/01/92 50.00

## Print 215 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a 215 Report for a given receipt number entered by the user. This report shows, in order of appropriation, how payments included in the receipt were posted during the automatic batch posting of payments process. Additionally, it identifies errors that took place during the posting process, as well as any payments that were made without an appropriation.

Since every cashier receipt contains a 215 Report, select this option and enter the receipt number for the 215 Report you wish to view. You may also select the type of report, accrued or detailed. A detailed report will show the patient or debtor name along with charges applied (interest, court cost, admin. charge, marshall fee) for each bill.

Select Agent Cashier Option: PRINT 215 Report

RECEIPT \#: CHECK001 ONE,TEST 10-21-93 CHECK/MO PAYMENT

Select one of the following:

A ACCRUED

D DETAILED

ACCRUED OR DETAILED REPORT: ACCRUED//\<ret\>

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

Pg. 1 OCT 22,1994@16:07:18

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 215 REPORT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

RECEIPT \#: CHECK001

--------------------------------------------------------------------------

Appropriation: 36X5014

1\) 000-K410008 19.01

2\) 000-K420188 35.00

----------

54.51

INTEREST: (APP:36X1435) 0.08

ADMIN: (APP:36 3220) 0.91

MARSHALL: 0.00

COURT COSTS: 0.00

----------

0.99

PREPAYMENTS:

TOTAL PREPAYMENTS POSTED: 0.00

ERRORS:

TOTALS:

TOTAL AMOUNT POSTED: 55.00

TOTAL UNAPPLIED AMOUNT: 0.00

## Profile of Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays a summary of activity on a patient's account (refer to Transaction Profile for a view of a single transaction on an account). The first level of information displayed is a list of all of the bills associated with that account. By choosing one of the bills, the second level of information displays all transactions associated with that bill or the profile of any activity that occurred on an account.

This option is similar to the full/brief profiles, except its use is not as flexible. Since the printout displays the bills by their bill number, you must know the number of the bill for which you are looking. Entering the bill number gives a profile showing all relevant data concerning the bill.

OCT 22,1994 16:11 ACCOUNTS RECEIVABLE PROFILE

===========================================================================

NAME: ONE,TEST BILL \#: 000-AA0014

101 TEST ROAD SOC.SEC.NO.: 000-11-1111

ORLANDO, FL 43434 DATE OF BIRTH: 03-04-34

PHONE NO.: DATE POSTED: AUG 31,1992 17:45:58

CURRENT STATUS: COLLECTED/CLOSED CATEGORY: RX CO-PAYMENT/NSC VET

GL \#: DATE BILL PREPARED: AUG 31,1992

INTEREST EFFECTIVE RATE DATE: JUL 1,1991 ANNUAL INTEREST RATE: .085

ADMIN EFFECTIVE RATE DATE: JUL 1,1991 MONTHLY ADMIN RATE: .91

ORIGINAL AMOUNT: 0.00

FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

---------- ------------ ------------- ------

92 0.00

BALANCES PAID LETTER1/ICD:

PRINCIPAL: 0.00 54.50 LETTER2:

INTEREST: 0.00 0.00 LETTER3:

ADMINISTRATIVE: 0.00 0.00 IRS LETTER:

DC/DOJ REF.DATE:

CURRENT: 0.00 54.50

TRANSACTIONS:

62 1 INCREASE ADJUSTMENT 08/31/92 50.00

63 2 INCREASE ADJUSTMENT 08/26/92 4.50

79 B2222222 PAYMENT (IN PART) 08/31/92 2.00

80 B2222222 PAYMENT (IN PART) 08/31/92 5.00

86 B3333333 PAYMENT (IN FULL) 09/03/92 47.00

BILL RESULTING FROM: UNEARNED MD/DD BONUS

Statement date: NOV 8,1994

OTHER BILLS:

000-K400044 (PREP/REFU) 000-AA0015 (RX C/COLL) 000-AB0020 (PREP/CANC)

## Release Holds on AR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option releases a hold on Means Test bills. This allows the user to forward the bills from IB to AR to start the collection process. There may be some instances which require the VA to hold off billing the patient until payment is received from the insurance company. When a payment is received from an insurance company, any holds on bills to be sent to the patient need to be removed and the patient should be billed.

![](accounts-receivable-version-4-5-user-manual-agent-cashier/003.png)

## RECEIPT MANAGEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains a list of options necessary for managing cashier and customer receipts.

### Approve a Receipt 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will mark a payment batch (identifiable by receipt number) as approved.

The security key PRCAY PAYMENT SUP is required to approve a receipt unless an individual is approving their own receipt. Once approved, a batch is ready for posting to the AR Transaction file. To post the payment batch, you should queue the batch for posting. See Post An Approved Receipt To Accounts.

Select Receipt Management Option: APPROVE a Receipt

RECEIPT \#: CASH001

Have you reviewed this RECEIPT? YES

Do you want to approve this RECEIPT at this time? YES

RECEIPT \#CASH001 approved.

QUEUE TO PRINT ON

DEVICE: HOME//ISC11 ROOM 730/10 RIGHT MARGIN: 132//\<ret\>

Request time to post payments: NOW//\<ret\> (OCT 22, 1994@20:09)

\*\*\* REQUEST QUEUED \*\*\*

### EDIT A RECEIPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to move a receipt from one deposit ticket to another. The user can also change the type of payment to CHECK/MO PAYMENT if the receipt status is open and the current value is EDI LOCKBOX and vice versa. If the new type is CHECK/MO PAYMENT, the system marks the EFT as unmatched. This option does not allow the user to edit other information contained on the receipt.

Select Receipt Management Option: EDIT A Receipt

RECEIPT \#: 8473625 ONE,TEST 08-16-94 CASH PAYMENT

DEPOSIT TICKET: 234432// 9999 07-06-94 TWO,TEST \$0.00 OPEN

RECEIPT \#:

### LIST OF RECEIPTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print a report of all receipts recorded with unarchived payments. The report is sorted by date and shows the receipt number, date posted, amount of payment, the bill that reflects the payment, and the user who posted the payment. The processing time for this report is the same for any given date range regardless of length or receipt type. An asterisk next to any receipt number indicates that the receipt number is out of numeric sequential order. This report may take a long time to compile- queue to a printer when the printer will not be needed immediately.

Select Receipt Management Option: List of Receipts

Enter the beginning DATE : FIRST// 9-1-94

Enter the ending DATE : LAST// T

DEVICE: HOME// VIRTUAL

LIST OF RECEIPTS

-----------------------------------------------------------------------------

Date

Receipt \# Posted Bill Amount Pd. By

-----------------------------------------------------------------------------

\* 888888888 09/22/94 000-K400105 4.00 ONE,TEST

-----------

4.00

### Post an Approved Receipt to Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option posts the transactions in an approved batch to the AR Transaction file. Users can only post a batch which they approved, unless they hold the supervisor’s key, PRCAY PAYMENT SUP.

Payments in the batch will be applied to the oldest bill first. Once the oldest bill is determined, if the status of the bill is Active or Open, the payment will be credited in the following order: marshal fees, court fees, administrative charges, interest charges, and finally, the principal balance of the bill. If the patient has bills that are on a repayment plan, the agreed repayment plan amount will be applied to the bills included on the repayment plan. Any amount paid over the agreed repayment plan amount will be applied according to the rules for automatic posting described above. If the payment is made in full, the status of the bill will be changed to Collected/Closed. If the payment made does not clear the balance of the bill, the status will not be changed. If the payment exceeds the total balance of the oldest bill, the remaining balance will be applied to any remaining bills. The process will repeat until all bills have been paid in full, or until the payment is exhausted. If the payment made exceeds the total of all outstanding bills, the remaining portion of the payment will be treated as a prepayment.

If a patient has specified that payment is for a particular bill, the payment can be applied to that bill by entering the bill number at the Patient name and Bill number prompt when entering a payment. If the payment exceeds the balance, the system will pay off the bill specified by the patient. It will apply the remaining portion of the payment automatically as described above.

> **NOTE:** This is only applicable for patient debts. For non-patient debts the system will notify the user that an overpayment was made and that a refund should be made. This will be reflected on the 215 Report as an error message.

Select Receipt Management Option: POST an Approved Receipt to Accounts

RECEIPT \#: CASH0002

Is this the correct RECEIPT? YES

QUEUE TO PRINT ON

DEVICE: HOME// ISC11 ROOM 730/10 PITCH RIGHT MARGIN: 132//\<ret\>

Request time to post payments: NOW//\<ret\> (OCT 22, 1994@20:14)

### Receipt Number Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints, by receipt number, the Receipt Number Reconciliation Report, which compares the total of payments on a given receipt entered during the day by an Agent Cashier with the actual funds collected. This report shows a list of payments received for a specific receipt, by bill number, and the amounts of each payment. Totals for each receipt or batch summary number (in the case of credit cards) appear at the end of the report. (The receipt batches are purged after sixty (60) days.) The Cashier may print this report after the receipt was posted to detect any posting errors that occurred during the night.

Select Receipt Management Option: RECeipt Number Reconciliation Report

RECEIPT \#: CHECK001 ONE,TEST 10-21-93 CHECK/MO PAYMENT

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

Receipt Status Report OCT 23,1994 12:11 Pa

Receipt \#: CHECK001 Starting Time: OCT 22,1994 13:29

Type: CHECK/MO PAYMENT Ending Time: OCT 22,1994 13:29

Deposit Date: OCT 22,1994 Queued to Post: OCT 22,1994 13:29

Opened By: ONE,TEST Date/Time Opened: OCT 21,1994 19:38

Approved By: TWO,TEST Date/Time Approved: OCT 22,1994 13:28

Last Edited: TWO,TEST

Date/Time Last Edit: OCT 22,1994 13:09

Payment Payment Amount

Trans \# Account Amount Date Processed

--------------------------------------------------------------------------

1 ARpatient,ONE 10.00 10/21/93 10.00

Check/MO \#: Bank \#: Date of Check:

2 ARpatient,ONE 10.00 10/21/93 10.00

Check/MO \#: Bank \#: Date of Check:

3 ARpatient,TWO 15.00 10/22/93 15.00

Check/MO \#: 1002034 Bank \#: 12345678 Date of Check: 10/22/93

--------- ---------

TOTAL 35 35

COUNT 3 3

MEAN 13.75 13.75

### REPRINT A CUSTOMER'S RECEIPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a second copy of a customer's receipt. Use this option to obtain a second copy if, for some reason, the first copy does not print correctly.

Select Receipt Management Option: REPrint a Customer's Receipt

RECEIPT \#: CHECK001 ONE,TEST 10-21-93 CHECK/MO PAYMENT

Select TRANSACTION: ??

CHOOSE FROM:

1 ARpatient,ONE \$10.00

2 ARpatient,TWO \$15.00

Select TRANSACTION: 2 ARpatient,TWO \$15.00

Are you sure you want to REPRINT this receipt? YES//\<ret\>

### Summary of Current Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print out a summary of current receipts in the system, sorted by receipt number. This report will show the following:

- who opened a receipt batch,
- when the batch was opened,
- the type of batch payment,
- number of transactions in the batch,
- whether the batch was posted, and
- who approved the batch for posting to patient accounts.

BATCH PAYMENT LIST OCT 23,1994 12:14 PAGE 1

DATE TYPE OF \# OF

RECEIPT \# OPENED PAYMENT OPENED BY APPROVED BY TRANS. POSTED

--------------------------------------------------------------------------

CASH0002 10/22/93 CASH PAY ONE,TEST ONE,TEST 1 YES

CASH0003 10/22/93 CASH PAY ONE,TEST ONE,TEST 0 YES

CASH001 10/21/93 CASH PAY TWO,TEST ONE,TEST 2 YES

CHECK001 10/21/93 CHECK/MO TWO,TEST ONE,TEST 4 YES

IRSPAY01 10/22/93 IRS PAYM ONE,TEST ONE,TEST 2 YES

PLASTIC01 10/22/93 CREDIT C ONE,TEST ONE,TEST 1 YES

### VOID A RECEIPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option cancels an empty receipt, i.e., a receipt that has no payment transaction associated with it. Use this option to facilitate voiding receipts that have been wrongly entered or are invalid.

Select Receipt Management Option: Void A Receipt

RECEIPT \#: 888888888 ONE,TEST 09-22-94 CASH PAYMENT

\*\*\* Receipt Voided \*\*\*

RECEIPT \#:

## Transaction Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view or print all information associated with a single transaction.

This option displays a summary of the bill number for the transaction, the transaction date, the type of transaction, and whether or not a code sheet was generated and sent to CALM. At the end of this list, enter the appropriate transaction number and all information for this transaction will be printed.

This option is often used in conjunction with the Profile of Accounts Receivable option. Transactions that appear on that profile can be viewed using the Transaction Profile option.

Select Agent Cashier Option: TRANSACTION Profile

ENTER AR TRANSACTION NO. OR BILL NO.: 000-AA0014 RX CO-PAYMENT/NSC VET

08-31-92 ONE,TEST COLLECTED/CLOSED \$0.00

1 62 000-K400141 08-31-92 INCREASE ADJUSTMENT

2 63 000-K400141 08-26-92 INCREASE ADJUSTMENT

3 79 000-K400141 08-31-92 PAYMENT (IN PART)

4 80 000-K400141 08-31-92 PAYMENT (IN PART)

5 86 000-K400141 09-03-92 PAYMENT (IN FULL)

CHOOSE 1-5: 1 62

Do you want to queue this output ? NO//\<ret\> (NO)

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

TRANSACTION PROFILE

============================================================================

ACCOUNT: ARpatient,ONE SSN: 000111111

TRANS. NO: 62 BILL NO: 000-K400141

TRANS. DATE: AUG 31,1992 TRANS. TYPE: INCREASE ADJUSTMENT

TRANS. AMOUNT: \$50.00 DATE POSTED: AUG 31,1992 17:45:58

ADJUSTMENT \#: 1

FISCAL YEAR PAT REFERENCE \# PRINCIPAL AMOUNT FY TRANS. AMOUNT

----------- ------------- ---------------- --------------

92 50.00 50.00

Brief Comment: Follow-up Date:

COMMENTS:

RECEIPT \#:

PROCESSED BY: TWO,TEST