---
title: Accounts Receivable Version 4.5 User Manual
doc_type: UM
doc_label: User Manual
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
menu_options: 13
description: - [AR - Accounts Receivable Menu](#ar-accounts-receivable-menu) - [BRIEF ACCOUNT PROFILE](#brief-account-profile) - [DEPOSIT MANAGEMENT MENU](#deposit-management-menu) - [CONFIRM DEPOSIT FROM BANK](#confirm-deposit-from-bank) - [PROCESS DEPOSIT](#process-deposit) - [FMS UTILITIES MENU](accounts-rece
audience: 
keywords: 
  - document
  - bill
  - deposit
  - status
  - table
  - number
  - contents
  - date
  - transaction
  - profile
page_count: 0
word_count: 3678
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/2acc_rec.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/2acc_rec.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![Figure 1 AR](accounts-receivable-version-4-5-user-manual/001.png)

*Figure 1 AR*

# AR - Accounts Receivable Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [AR - Accounts Receivable Menu](#ar-accounts-receivable-menu)
  - [BRIEF ACCOUNT PROFILE](#brief-account-profile)
  - [DEPOSIT MANAGEMENT MENU](#deposit-management-menu)
    - [CONFIRM DEPOSIT FROM BANK](#confirm-deposit-from-bank)
    - [PROCESS DEPOSIT](#process-deposit)
  - [FMS UTILITIES MENU](accounts-receivable-version-4-5-user-manual/003.png)](#fms-utilities-menuaccounts-receivable-version-4-5-user-manual003png)
  - [FMS UTILITIES MENU](#fms-utilities-menu)
    - [DOCUMENT STATUS INQUIRY](#document-status-inquiry)
    - [FMS CASH RECEIPT RECONCILIATION (132 COL.)](#fms-cash-receipt-reconciliation-132-col)
    - [FMS REGENERATION MENU](#fms-regeneration-menu)
  - [FULL ACCOUNT PROFILE](#full-account-profile)
  - [PATIENT PAYMENT/REFUND TRANSACTION HISTORY INQUIRY](#patient-paymentrefund-transaction-history-inquiry)
  - [PAYMENTS POSTED FROM PREPAYMENT](#payments-posted-from-prepayment)
  - [PRINT 215 REPORT](#print-215-report)
  - [PROFILE OF ACCOUNTS RECEIVABLE](#profile-of-accounts-receivable)
  - [STATUS LISTING FOR BILLS](#status-listing-for-bills)
  - [TRANSACTION PROFILE](#transaction-profile)

## BRIEF ACCOUNT PROFILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays all *outstanding* bills and payments for a given account. Outstanding bills include bills with a status of *Open, Active,* or *Refund Review.* The profile groups bills by their status and includes a total balance of all bills with that status. The option also allows you to view a bill and any of its associated transactions.

This profile is helpful when quickly searching a patient's account for bills and viewing transactions. After viewing the profile, the system will prompt for a transaction that appears on the profile. Simply enter the number of the transaction and view a descriptive profile for that transaction.

Payments that appear in the profile indicate that they are applied to the account but haven't been posted against a bill. Once their respective receipt is approved, those payments will be applied to outstanding bills or a prepayment bill.

================ A c c o u n t P r o f i l e ==================

ARpatient,one (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: YES

\# Bill \# Est Type Paid Prin Int Adm Balance

------------------------------ PAYMENTS (-10.00) --------------------------

\* PLASTIC01-1 PAYMENT -10.00 0.00 0.00 0.00 -10.00

--------------------------------- OPEN (12.00) ----------------------------

1 000-K401881 10/22/93 RX CO-P 38.00 12.00 0.00 0.00 12.00

Select 1-1: 1

================== A c c o u n t P r o f i l e ======================

ARpatient,one (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: YES

Bill \#: 000-K401881

\# Tr \# Type Date Amount

---------------------------------------------------------------------------

Original Amount 10/22/93 0.00

1 1202 INCREASE ADJUSTMENT 10/22/93 50.00

2 1205 PAYMENT (IN PART) 10/22/93 15.00

3 1206 PAYMENT (IN PART) 10/22/93 20.00

4 1207 PAYMENT (IN PART) 10/22/93 3.00

------

\$ 12.00

Select 1-4 or 'P' to Print:

![](accounts-receivable-version-4-5-user-manual/002.png)

## DEPOSIT MANAGEMENT MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options within the Deposit Management sub-menu under the Accounts Receivable main menu are identical to those found in the Deposit Management sub-menu of the Agent Cashier’s menu with the exception of the additions described in the following sections.

### CONFIRM DEPOSIT FROM BANK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to select and summarily enter a confirmation that a deposit ticket number has been deposited to the bank. (The ticket must have been deposited first!) If there are no receipts associated with a ticket, the user will be informed with a message before it can be confirmed. The confirmation data consists of entering the Bank Deposit Date (the date the bank actually recorded the deposit- not the date the deposit was presented to the bank) and the Bank Trace Number. The Bank Trace number, unlike the Bank Deposit Date, is not required for confirmation to occur. Upon entering the confirmation information, the user is prompted to accept the data. If a mistake has been made while entering the data, the user answers NO to the prompt and will be able to edit the information. When confirmation has taken place, the deposit ticket is marked as processed and the appropriate document is sent to FMS.

Select Deposit Management Option: CONfirm Deposit from Bank

Select TICKET NUMBER to CONFIRM: 312321// 08-14-94 ONE,TEST \$50.00 DEPOSITED

BANK DEPOSIT DATE: T (AUG 17, 1994)

BANK TRACE NUMBER: 43256

DEPOSIT TICKET

Ticket \#: 312321 AUG 17,1994 13:55

=============================================================================

Opened By: ONE,TEST JUN 14,1994 13:18

Deposited By: TWO,TEST AUG 16,1994 09:55

Confirmed By:

Agency Title: SITE (DEPOSIT) Bank Name: MELLON BANK (CENTRAL)

Status of Ticket: DEPOSITED Agency Loc. Code: 1090000-1

Bank Trace Number: 43256 Presented to Bank: AUG 16,1994

Number of Receipts: 4 Bank Deposit Date: AUG 17,1994

Deposit Amount: \$50.00

-----------------------------------------------------------------------------

Comment:

TEST

Is this OK? YES//

... Deposit confirmation accepted

... Deposit marked as processed

### PROCESS DEPOSIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to “manually” mark a deposit ticket for transmitting to FMS. The deposit ticket must be in either processed or confirmed status to be marked. A deposit ticket with no receipts associated with it can be marked but will not be transmitted. This option should be used only if the confirmation processed error was aborted.

Select AR MASTER MENU Option: AR - Accounts Receivable Menu

Select AR - Accounts Receivable Menu Option: Deposit Management

Select Deposit Management Option: Process Deposit

Select TICKET NUMBER to PROCESS: 12345 05-20-94 ONE,TEST

\$10012.10 CONFIRMED

DEPOSIT TICKET

Ticket \#: 12345 AUG 17,1994 14:20

=============================================================================

Opened By: ONE,TEST MAY 20,1994 13:56

Deposited By: TWO,TEST MAY 20,1994 14:03

Confirmed By: THREE,TEST JUN 14,1994 13:32

Agency Title: Bank Name: MELLON BANK (CENTRAL)

Status of Ticket: CONFIRMED Agency Loc. Code: 1090000-1

Bank Trace Number: 000-4949 Presented to Bank: MAY 20,1994

Number of Receipts: 2 Bank Deposit Date: MAY 27,1994

Deposit Amount: \$10012.10

-----------------------------------------------------------------------------

Comment:

Are you sure you want to post to FMS? NO// YES

... Deposit queued for transmission to FMS

![Figure 2Utilities

## FMS UTILITIES MENU](accounts-receivable-version-4-5-user-manual/003.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Figure 2Utilities

## FMS UTILITIES MENU*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FMS Utilities Menu contains the options which are necessary to manage data being sent to the Financial Management System in Austin.

### DOCUMENT STATUS INQUIRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](accounts-receivable-version-4-5-user-manual/004.png)

This sub-menu allows the user to check the status of FMS documents

#### Billing Document Inquiry

This option is used to view the status of a detail bill that had been sent to FMS. The status’s include sent, not sent, rejected, and accepted.

Select Document Status Inquiry Option: Bill Inquiry

Select A/R BILL: 000-4K0005B VENDOR 04-29-94 SAM'S SUPPLY STORE

ACTIVE \$100.00

A/R Document Status Inquiry

Bill Number: 000-4K0005B Amount: 50.00 Debtor: SAM'S SUPPLY STORE

Last Update: JUL 26,1994 15:55 STATUS: SENT

#### Transaction Inquiry

This option enables a user to display the FMS status for a user-specified AR transaction. Such information would be useful in determining the cause of inconsistencies that may exist in the OBR report.

#### Regenerate Prior Month Obr

This option regenerates the previous month’s outstanding bill reconciliation report and sends it to the local FMS mail group. The OBR prints routinely at the end of each month and lists all open receivable sent to FMS. This option is the “manual” queue in the event that the OBR doesn’t run automatically. Should a discrepancy occur between FMS and AR, it would be listed on the OBR as an error. Some typical errors would include balance discrepancies between FMS and AR, or transactions being listed in FMS and not AR (or vice- versa).

After answering YES to the prompt which asks if the user wishes to regenerate the prior month’s OBR, the user is returned to the Document Status Inquiry menu. The OBR will appear in the user’s local mailman.

#### Unprocessed Document List

This option will print a list of FMS documents that have an FMS status other than accepted. This report will show documents that are three or more days old. FMS status’s include: Accepted- document was accepted at FMS, Sent- document was passed from AR to the Generic Code Sheet package and are awaiting transmission to FMS, Not Sent- document is being processed by AR, Rejected- document has been sent to FMS and was rejected due to an error.

Select Document Status Inquiry Option: Unprocessed Document List

START WITH DOCUMENT DATE: FIRST// 8-1

GO TO DOCUMENT DATE: LAST// 8-10

DEVICE: VIRTUAL RIGHT MARGIN: 80//

FMS UNPROCESSED DOCUMENT LIST AUG 31,1994 15:30 PAGE 1

Type of Document FMS Doc. \# Doc. Dt. Status AR Bill \#

-----------------------------------------------------------------------------

BILLING-DOCUMENT ESTABL BD000K400095 08/17/94 NOT-SENT 000-K400095

BILLING-DOCUMENT ESTABL BD000K400058 08/18/94 NOT-SENT 000-K400058

BILLING-DOCUMENT ESTABL 000K400055 08/01/94 SENT 000-K400055

CASH-RECEIPT DETAIL 000K4A0253 08/09/94 SENT 000-K400022

CASH-RECEIPT SUMMARY 000K4A0254 08/09/94 SENT 000-K400023

CASH-RECEIPT SUMMARY 000K4A0255 08/09/94 SENT 000-4K00069

### FMS CASH RECEIPT RECONCILIATION (132 COL.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report allows the user to view Cash Receipt documents from a specified ticket number or range of numbers and dates. The receipts are categorized by appropriation. Each appropriation is totaled with a grand total of all receipts shown at the end.

Select FMS Utilities Menu Option: FMS DOCument Comparison Report (132 col.)

START WITH DEPOSIT TICKET: FIRST//

START WITH DATE LAST UPDATE: : FIRST//

DEVICE: VIRTUAL RIGHT MARGIN: 80//

AR FMS DOCUMENT LIST NOV 14,1994 11:55 PAGE 1

RECEIPT \# FMS DOCUMENT NUMBER FUND AMOUNT

AR BILL NUMBER

-----------------------------------------------------------------------------

DEPOSIT TICKET: 387435

DATE LAST UPDATE: OCT 13, 1994

STATUS: ACCEPTED

11446119 CR-000K5A0158 1435 0.09

11446120 CR-000K5A0162 1435 0.66

11446121 CR-000K5A0166 1435 2.14

-----------

SUBTOTAL 2.89

11446121 CR-000K5A0165 2431 37.37

-----------

SUBTOTAL 37.37

11446119 CR-000K5A0159 3220 1.80

11446120 CR-000K5A0163 3220 4.20

11446121 CR-000K5A0167 3220 6.45

-----------

SUBTOTAL 12.45

DATE LAST UPDATE: OCT 25, 1994

STATUS: ACCEPTED

11446118 CR-000K5A0286 5014 42.00

11446118 CR-000K5A0287 5014 22.00

11446119 CR-000K5A0288 5014 351.54

11446119 CR-000K5A0289 5014 4.00

-----------

SUBTOTAL 419.54

-----------

TOTAL 472.16

![](accounts-receivable-version-4-5-user-manual/005.png)

### FMS REGENERATION MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sub-menu of the FMS utilities contains the options that allow the regeneration and subsequent re-transmission of the various FMS document types to Austin.

#### Billing Document Regeneration

This option regenerates and re-transmits a billing document that has been rejected in FMS and subsequently corrected by the user. The initial prompt requires a *bill number*. (See reject list from FMS that is sent daily to your site.)

Select FMS Regeneration Menu Option: BILLing Document Regeneration

Select BILL NUMBER: 000-K400084 VENDOR 06-16-94 SAM'S SUPPLY STORE ACTIVE \$110.00

This will RESEND the selected Billing Document to FMS.

Are you sure? NO// YES

Building FMS Billing Document. Please hold...

#### Edit FMS Accounting Elements

This option is used to edit the accounting line information on rejected FMS Billing Documents. Once the edit is made, the FMS Billing Document is re-translated.

Select FMS Regeneration Menu Option: EDIT FMS Accounting Elements

Select BILL NUMBER: 000-4K0005D VENDOR 04-29-94 SAM'S SUPPLY STORE ACTIVE \$25.00

=============================================================================

BILL \# : 000-4K0005D DEBTOR : SAM'S SUPPLY STORE

FISCAL YEAR FUND (APPROPRIATION) ORIGINAL AMOUNT

94 0151A1 50.00

=============================================================================

\*\*\* REFUND \*\*\*

CONTROL POINT : 301

BUDGET OBJECT : 2660 COST CENTER : 800100

SUB : SUB : 00

=============================================================================

\*\*\* REIMBURSEMENT \*\*\*

REVENUE SOURCE : SUB :

Select one of the following:

1 REFUND

2 REIMBURSEMENT

BILL TYPE: REIMBURSEMENT// 1 REFUND

CONTROL POINT: 301// 101

101 LAB TESTING 101//

SAT STATION:

COST CENTER: 800100//

BOC (SUB ACCOUNT): 2660// 2696 LAB TEST BOC

Building FMS Billing Document. Please hold...

#### Modified Billing Document Regeneration

This option regenerates and re-transmits a modified billing document that has been rejected in Austin. The initial prompt requires a *transaction number but will accept a bill number*. (See reject list from FMS that is printed daily at your site.)

Select FMS Regeneration Menu Option: Modified Billing Document Regeneration

Select A/R TRANSACTION NUMBER: 136 000-K400025 08-26-94 INCREASE

ADJUSTMENT CALM CODE: NOT DONE

This will RESEND the selected Billing Document to FMS.

Are you sure? NO// YES

Creating FMS Modified Billing Document...

Document \#43 Created.

#### National Data Base Document Regeneration

This option is used to regenerate and re-transmit National Data Base Documents that have been rejected by FMS.

Select FMS Regeneration Menu Option: NATional Data Base Document Regeneration

Select NDB Document to Retransmit: ??

CHOOSE FROM:

27 SUMMARY VOUCHER 07-06-94 REJECTED NDB0630SV5014

30 WRITE-OFF SUMMARY 07-06-94 REJECTED NDB0630WR5014

Select NDB Document to Retransmit: 27 SUMMARY VOUCHER 07-06-94 REJECTED NDB0630SV5014

Code Sheet Retransmitted

#### Overpayment (OP) Document Regeneration

This option will allow a user to regenerate and re-transmit a rejected OP Document. It will only allow the re-transmission of an OP document that has actually been refunded in the AR package and has been rejected by FMS. The initial prompt requires a *bill number*. (See reject list from FMS that is printed daily at your site.)

Select FMS Regeneration Menu Option: Overpayment (OP) Document Retransmit

Select ACCOUNTS RECEIVABLE BILL NO.: 000-K400044 PREPAYMENT 05-20-94

FOUR,PATIENT REFUNDED \$0.00

Creating an FMS Overcollection Payment Voucher . . .

#### Regenerate Fms Cash Receipt Document

This option is to re-create and re-transmit the Cash Receipt Documents.

Select FMS Regeneration Menu Option: REG

RECEIPT \#: 88888888 ONE,TEST 09-22-94 CASH PAYMENT

Is this the correct RECEIPT to regenerate? y YES

Cash Receipt Document/s were REGENERATED and sent to FMS!!!

#### Remove Invalid Sub BOC

This option is used to remove an invalid Sub Budget Object Code (BOC). *For salary receivables only.*

Select FMS Regeneration Menu Option: REMOve invalid SUB BOC

Select ACCOUNTS RECEIVABLE BILL NO.: 000-K400044 PREPAYMENT 05-20-94 ARpatient,one REFUNDED \$0.00

SUB BOC removed.

#### Write-Off Document Regeneration

This option is used to regenerate and re-transmit a rejected FMS Write-Off Document. The initial prompt requires a *transaction number*. (See reject list from FMS that is printed daily at your site.)

Select FMS Regeneration Menu Option: Write-Off Document Regeneration

Select A/R TRANSACTION NUMBER: 30 000-4K00082 05-06-94 INCREASE

ADJUSTMENT CALM CODE: DONE

This will RESEND the selected Billing Document to FMS.

Are you sure? NO// YES

Creating FMS Write-Off Document...

Document \#43 Created.

## FULL ACCOUNT PROFILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays all *non-outstanding* and *outstanding* bills and payments for a given account. This means bills with any status. The profile groups bills by their status and includes a total balance of all bills with that status. The option also allows you to view a bill and any of its associated transactions.

This profile is helpful when quickly searching a patient's account for bills and viewing transactions. After viewing the profile, the system will prompt for a transaction that appears on the profile. Simply enter the number of the transaction and view a descriptive profile for that transaction. Payments that appear in the profile indicate that they are applied to the account but haven't been posted against a bill. Once their respective receipt is approved, those payments will be applied to outstanding bills or a prepayment bill.

================ A c c o u n t P r o f i l e ==================

ARpatient,one (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: YES

\# Bill \# Est Type Paid Prin Int Adm Balance

--------------------------- COLLECTED/CLOSED (0.00) -----------------------

1 000-K400141 08/31/92 RX CO-P 54.50 0.00 0.00 0.00 0.00

2 000-K400151 09/01/92 RX CO-P 68.00 0.00 0.00 0.00 0.00

3 000-K401311 07/21/93 RX CO-P 2.00 0.00 0.00 0.00 0.00

----------------------------- CANCELLATION (0.00) -------------------------

4 000-K400201 11/18/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

--------------------------------- OPEN (2.00) -----------------------------

5 000-K401881 10/22/93 RX CO-P 48.00 2.00 0.00 0.00 2.00

------------------------------- REFUNDED (0.00) ---------------------------

6 000-K400041 08/20/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

7 000-K400292 12/15/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

8 000-K400493 12/17/92 PREPAYM 0.00 -0.00 0.00 0.00 -0.00

---------------------------- BILL INCOMPLETE (0.00) -----------------------

Select 1-8 or return to continue: 2

================ A c c o u n t P r o f i l e ==================

ARpatient,one (000-11-1111) Statement Day: 8

101 TEST ROAD Last Statement: N/A

ORLANDO, FL 43434 Amount Owed: 2.00

Phone \#: N/A RX Copay Exempt: NO

Bill \#: 000-K400151

\# Tr \# Type Date Amount

---------------------------------------------------------------------------

Original Amount 09/01/92 0.00

1 65 INCREASE ADJUSTMENT 09/01/92 4.50

2 66 INCREASE ADJUSTMENT 07/01/92 50.00

3 67 INCREASE ADJUSTMENT 06/05/92 44.50

4 87 PAYMENT (IN PART) 09/03/92 3.00

5 195 PAYMENT (IN PART) 11/12/92 45.00

6 208 INCREASE ADJUSTMENT 12/01/92 2.00

7(I) 209 PAYMENT (IN PART) 12/01/92 10.00

8 218 DECREASE ADJUSTMENT 12/03/92 2.00

9 234 DECREASE ADJUSTMENT 12/22/92 0.01

Select 1-9 or 'P' to Print or return to continue:

## PATIENT PAYMENT/REFUND TRANSACTION HISTORY INQUIRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists a history of payment/refund transactions for a patient and a given date range. Use this report to respond to patient questions concerning their payments or refunds. It will provide information about the amount applied towards fees, charges, and services.

When the system prompts for the beginning date, the default response is the last statement date if it exists or T-30 if the last statement date does not exit.

Patient Payment History Report Page 1

------------------------------

For Patient: ARpatient,one

SSN : 000111111

For dates: Sep 22, 1994-Oct 22, 1994

DATE OF

PAYMENT/REFUND BILL \# REFUND RECEIPT \# AMOUNT PRIN. INT. ADMIN.

---------------------------------------------------------------------------

Oct 22, 1994 000-K401883 CHECK001 15.00 15.00 0.00 0.00

Oct 22, 1994 000-K401883 CHECK001 20.00 20.00 0.00 0.00

Oct 22, 1994 000-K401883 IRSPAY01 3.00 3.00 0.00 0.00

Oct 22, 1994 000-K401883 PLASTIC01 10.00 10.00 0.00 0.00

Total Principal Paid: 48.00

Total Interest Paid: 0.00

Total Admin Paid: 0.00

Total Paid: 48.00

Total Refund: 0.00

## PAYMENTS POSTED FROM PREPAYMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists, by date selected, the AR transactions that are decreases from prepayment bills and their corresponding Accounts Receivable transactions that are either payments in full or payments in part. Two types of error messages will be displayed based on the following conditions:

- If the corresponding transaction is not found
- If the decrease transaction and the payment transaction do not balance

This is often used to identify monies that should be transferred from one appropriation to another, such as an MCCR appropriation to a non-MCCR appropriation. An asterisk (\*) will appear beside any transaction that should be transferred.

Background Payment Posting from Prepayment Receivables Page 1 22-OCT-93

Reporting period: AUG 23,1994 thru OCT 22,1994

==============================================================================

Tran. Tran. Tran. Tran. Corresponding Patient Bill

Date No. Type Amount Tran. No. Name No.

09/17/94 1127 DECREASE \$10.00 1126 ARpatient,one 000-K400554

09/17/94 1126 PAYMNT (FULL) \$10.00 1127 ARpatient,one 000-K400605

09/17/94 1130 DECREASE \$76.45 1129 ARpatient,one 000-K400554

09/17/94 1129 PAYMNT (PART) \$76.45 1130 ARpatient,one 000-K400605

\* - Include the payment amount on a 928.23

## PRINT 215 REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a 215 Report for a given receipt number entered by the user. This report shows, in order of appropriation, how payments included in the receipt were posted during the automatic batch posting of payments process. Additionally, it identifies errors that took place during the posting process, as well as any payments that were made without an appropriation.

Since every cashier receipt contains a 215 Report, select this option and enter the receipt number for the 215 Report you wish to view. You may also select the type of report, accrued or detailed. A detailed report will show the debtor name along with charges applied (interest, court cost, admin. charge, marshal fee) for each bill.

Use this option when reconciling the Agent Cashier AR listings with each accounting document.

Select AR - Accounts Receivable Menu Option: print 215 Report

RECEIPT \#: check001 ONE,TEST 10-21-93 CHECK/MO PAYMENT

Select one of the following:

A ACCRUED

D DETAILED

ACCRUED OR DETAILED REPORT: ACCRUED// DETAILED

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

Pg. 1 OCT 22,1994@21:44:08

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 215 REPORT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

RECEIPT \#: CHECK001

---------------------------------------------------------------------------

Appropriation: 36X5014

1\) 000-K400081 19.01 DEBTOR: ARpatient,one

INT: 0.08 ADMIN: 0.91 MARS: 0.00 CC: 0.00

2\) 000-K401881 35.00 DEBTOR: TWO,TEST PATIENT

INT: 0.00 ADMIN: 0.00 MARS: 0.00 CC: 0.00

----------

54.51

INTEREST: (APP:36X1435) 0.08

ADMIN: (APP:36 3220) 0.91

MARSHALL: 0.00

COURT COSTS: 0.00

----------

0.99

PREPAYMENTS:

ERRORS:

TOTALS:

TOTAL AMOUNT POSTED: 55.00

TOTAL UNAPPLIED AMOUNT: 0.00

## PROFILE OF ACCOUNTS RECEIVABLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a report of all information and activities or events that have occurred against any account. You may view these accounts by entering the debtor name, bill number or PAT number. If the debtor is a patient, you may enter the social security number.

Use this option to obtain information for veteran or third party inquires. Also, it can be used to accumulate information for submitting delinquent debts to District Counsel.

OCT 22,1994 16:11 ACCOUNTS RECEIVABLE PROFILE

===========================================================================

NAME: ARpatient,one BILL \#: 000-K400144

SC(%): 10 SA: None

101 TEST ROAD SOC.SEC.NO.: 000-11-1111

ORLANDO, FL 43434 DATE OF BIRTH: 03-04-34

PHONE NO.: DATE POSTED: AUG 31,1992 17:45:58

CURRENT STATUS: COLLECTED/CLOSED CATEGORY: RX CO-PAYMENT/NSC VET

GL \#: DATE BILL PREPARED: AUG 31,1992

INTEREST EFFECTIVE RATE DATE: JUL 1,1991 ANNUAL INTEREST RATE: .085

ADMIN EFFECTIVE RATE DATE: JUL 1,1991 MONTHLY ADMIN RATE: .91

ORIGINAL AMOUNT: 0.00

FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

---------- ------------ -------------- ------

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

000-K400014 (PREP/REFU) 000-K400115 (RX C/COLL) 000-K400420 (PREP/CANC)

000-K400229 (PREP/REFU) 000-K400429 (PREP/REFU) 000-K400461 (VEND/PEND)

000-K400172 (CURR/BILL) 000-K401131 (RX C/COLL) 000-K401436 (EX-E/PEND)

000-K401828 (RX C/OPEN)

## STATUS LISTING FOR BILLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists all bills with a given status. This report will contain the bill's number, date, category, debtor, and balance. In addition, a summary will appear at the end of the report which will show the total number of bills with this status and the total balance of all bills with this status. To view this report, enter the status name at the system prompt. Common statuses searched for by Accounting Technicians are New Bill, and Refund Review; however, Accounting Technicians have the ability to get any status listing that would fulfill their needs.

The following table shows a list of all valid bill statuses.

| Bill Statuses |                        |
|-------------------|------------------------|
| ACTIVE            | OLD BILL               |
| ADD (AMEND)       | OPEN                   |
| AMEND             | PENDING APPROVAL       |
| AMENDED BILL      | PENDING ARCHIVE        |
| ARCHIVED          | RE-ESTABLISH           |
| BILL INCOMPLETE   | REFUND REVIEW      |
| CANCELLATION      | REFUNDED               |
| CANCELED BILL     | RETURNED FOR AMENDMENT |
| COLLECTED/CLOSED  | RETURNED FROM AR (NEW) |
| DELETE (AMEND)    | SUSPENDED              |
| IN-ACTIVE         | SUSPENSE               |
| INCOMPLETE        | WRITE-OFF              |
| NEW BILL      |                        |

Select AR - Accounts Receivable Menu Option: STATUS Listing For Bills

List for STATUS: OPEN

DEVICE: HOME//\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

Status: OPEN

Bill no. Date Prepared Category Debtor Balance

---------------------------------------------------------------------------

000-K400354 NOV 1,1992 RX CO-PAYMENT/N ONE,TEST 8.00

000-K400434 JUL 14,1994 PREPAYMENT TWO,TEST 7.00

000-K400356 OCT 1,1994 PREPAYMENT THREE,TEST 20.00

000-K401837 OCT 22,1994 RX CO-PAYMENT/S \*FOUR,TEST 10.00

000-K401838 OCT 22,1994 RX CO-PAYMENT/N ARpatient,one 2.00

TOTAL: 47.00

COUNT: 5.00

MEAN: 9.40 \* -indicates that patient is deceased

## TRANSACTION PROFILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view or print all information associated with a single transaction.

If a "?" or “??” is entered at the prompt to enter a bill or transaction number, a list of all transactions is generated. A nice feature about this listing is that it will display a summary of the bill number for the transaction, the transaction date, and the type of transaction. At the end of this list, enter the appropriate transaction number and all information for this transaction will be printed.

This option is often used in conjunction with the Profile of Accounts Receivable option. Transactions that appear on that profile can be viewed using the Transaction Profile option. To generate a profile, enter the bill number at the system prompt.

> **NOTE:** This option will not generate a listing for a "new" bill. New bills must be audited in order to see a profile.

Select Agent Cashier Option: TRANSACTION Profile

ENTER AR TRANSACTION NO. OR BILL NO.: 000-K300134 RX CO-PAYMENT/NSC VET

08-31-92 ARpatient,one COLLECTED/CLOSED \$0.00

1 62 000-K400134 08-31-92 INCREASE ADJUSTMENT

2 63 000-K400134 08-26-92 INCREASE ADJUSTMENT

3 79 000-K400134 08-31-92 PAYMENT (IN PART)

4 80 000-K400134 08-31-92 PAYMENT (IN PART)

5 86 000-K400134 09-03-92 PAYMENT (IN FULL)

CHOOSE 1-5: 1 62

Do you want to queue this output ? NO//\<ret\> (NO)

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

TRANSACTION PROFILE

============================================================================

ACCOUNT: ARpatient,one SSN: 000111111

TRANS. NO: 62 BILL NO: 000-K400134

TRANS. DATE: AUG 31,1992 TRANS. TYPE: INCREASE ADJUSTMENT

TRANS. AMOUNT: \$50.00 DATE POSTED: AUG 31,1992 17:45:58

ADJUSTMENT \#: 1

FISCAL YEAR PAT REFERENCE \# PRINCIPAL AMOUNT FY TRANS. AMOUNT

----------- ------------- ---------------- --------------

92 50.00 50.00

Brief Comment: Follow-up Date:

COMMENTS:

RECEIPT \#:

PROCESSED BY: TEST,ON