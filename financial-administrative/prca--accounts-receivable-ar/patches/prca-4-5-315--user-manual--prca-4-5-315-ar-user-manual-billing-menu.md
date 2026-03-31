---
title: PRCA*4.5*315 AR User Manual - Billing Menu
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: AR  - Billing Menu
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*315
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 3
description: - [Billing Menu](#billing-menu) - [New Bill (Enter)](#new-bill-enter) - [veterans Beneficiary Travel](#veterans-beneficiary-travel) - [Display Pending Bill](#display-pending-bill) - [Approve/Print Pending Bill](#approveprint-pending-bill) - [Edit Bill](#edit-bill) - [Cancel Bill](#cancel-bill) - [Am
audience: 
keywords: 
  - bill
  - your
  - date
  - billing
  - table
  - contents
  - arpatient
  - status
  - amount
  - bills
page_count: 0
word_count: 3130
section_count: 11
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p315_4billing.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p315_4billing.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![](prca-4-5-315-ar-user-manual-billing-menu/001.png)

# Billing Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Billing Menu](#billing-menu)
  - [New Bill (Enter)](#new-bill-enter)
  - [veterans Beneficiary Travel](#veterans-beneficiary-travel)
  - [Display Pending Bill](#display-pending-bill)
  - [Approve/Print Pending Bill](#approveprint-pending-bill)
  - [Edit Bill](#edit-bill)
  - [Cancel Bill](#cancel-bill)
  - [Amend Bill Returned from AR](#amend-bill-returned-from-ar)
  - [BILL STATUS LISTING](#bill-status-listing)
  - [LIST ALL BILLS](#list-all-bills)
  - [VIEW A BILL](#view-a-bill)

## New Bill (Enter)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create all bills except patient, reimbursable health insurance bills and pharmacy bills. Reimbursable Health Insurance and Pharmacy bills are created by the Integrated Billing (IB) software.

The questions and prompts that the computer displays vary depending on what type of bill you are creating.

A summary of the types of forms and their associated categories is shown by this illustration.

| FORM | CATEGORY              |                                 |        |
|----------|---------------------------|---------------------------------|--------|
| 1080     | Military                  |                                 |        |
| 1081     | Federal Agencies - REFUND | Federal Agencies - REIMBURSABLE |        |
| 1114     | Ex-Employee               | Current Employee                | Vendor |

When a bill gets created using this option, the bill status changes from New Bill to Pending Approval. Next, the service who created the bill must audit and approve it; hence the status name, Pending Approval (See the Approve/Print Pending Bill option). Only when the bill has been approved by the service is it released to the Accounts Receivable section; specifically, the bill is sent to the AR Clerk for another audit. At this point, the bill status becomes Active and charges can now be applied to this bill.

Select Billing Option: NEW Bill (Enter)

SITE: ALTOONA VAMC//\<ret\> PENNSYLVANIA 000

FORM TYPE: ??

This response indicates the type of form for the bill.

(1080, 1081 or 1114).

CHOOSE FROM: 1 1081

2 1080

3 1114

FORM TYPE: 3 1114

CATEGORY: VENDOR

DATE BILL PREPARED: OCT 22,1994//\<ret\>

VOUCHER NUMBER: 123

BILLING AGENCY:\<ret\>

DEBTOR (PAYER): ARdebtor, One

ARE YOU ADDING 'ARDEBTOR, ONE' AS A NEW VENDOR (THE 35TH)? Y (YES)

VENDOR NUMBER: 35//\<ret\>

ARE YOU ADDING 'ARdebtor, One' AS A NEW AR DEBTOR? Y (YES)

Select DATE OF CHARGES: T OCT 22, 1994

DESCRIPTION OF CHARGES:

1\>This is for documentation!!

2\>\<ret\>

EDIT Option:\<ret\>

QUANTITY (UNITS): 1

UNIT COST: 5

UNIT: ea EACH

TOTAL AMOUNT: 5//\<ret\> (No Editing)

Select DATE OF CHARGES:\<ret\>

Select FISCAL YEAR: 94//\<ret\>

FY ORIGINAL AMOUNT: 5//\<ret\>

APPROPRIATION SYMBOL:\<ret\>

Select FISCAL YEAR:\<ret\>

(No Street Address) Edit Debtor Address:? YES//\<ret\> (YES)

IS THIS FOR VETERANS BENEFICIARY TRAVEL? NO//\<ret\>

Address Accounts Receivable will use:

ARDEBTOR, ONE

Phone:

BILLING ADDRESS1: 111

BILLING ADDRESS2: ONE WAY

BILLING ADDRESS3:\<ret\>

BILLING CITY: ONE

BILLING STATE: PENNSYLVANIA

BILLING ZIP CODE: 11111

BILLING PHONE NUMBER: (111)111-1111

Display/Print Bill:? YES//\<ret\> (YES)

DEVICE: HOME//\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

BILL \#: 000-K20189 DATE: 10/22/93 TYPE: 1114

DEBTOR: BILLING AGENCY:

ARdebtor, One

111 ,

ONE WAY

ONE, PA 11111

APPROVING OFFICIAL:

DATE DESCRIPTION QTY COST PER AMOUNT

-------------------------------------------------------------------------

10/22/93 1 5.0000 EA 5.00

This is for documentation!!

## veterans Beneficiary Travel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Bill pertains to Veterans beneficiary travel, then the question:

IS THIS FOR VETERANS BENEFICIARY TRAVEL? NO//\<ret\>

Should be answered yes. If so, a statement, including the Veterans’ appeal rights and responsibilities will be included in that bill as follows:

BILL \#: 442-K8008B2 DATE: 04/10/2018 TYPE: 1114

DEBTOR: BILLING AGENCY:

BOLAR PHARMACEUTICAL CO INC VA MEDICAL AND RO CENTER

33 RALPH AVE VA MEDICAL CENTER

PO BOX 30 2360 E PERSHING BLVD

COPIAGUE, NY 11726 CHEYENNE, WY 82001

CONTROL POINT : 321

APPROVING OFFICIAL:

FY: 18 APPR. SYMBOL: AMOUNT: 1000.00

DATE DESCRIPTION QUANTITY COST PER AMOUNT

--------------------------------------------------------------------------------

04/03/2018 TRAVEL 1 1000.0000 EA 1000.00

NOTICE OF RIGHTS AND RESPONSIBILITIES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COLLECTION: The U.S. Department of Veterans Affairs (VA) is required to

collect debts owed to the government. Action must be taken within sixty

\(60\) days from the initial billing statement to pay your debt in full or

establish a payment plan or your account may be referred for further

collection action. You have the right to inspect and copy the records

related to the debt. You also have the right to establish a payment plan.

You have the right to submit a compromise offer. You have the right to

request a waiver and a hearing on the waiver request. Collection action

includes referring your delinquent balance to the Department of

Treasury's Treasury Offset Program, which will include offset of any

federal and state payments to which you are entitled. This includes tax

refunds, social security benefits and salary or retirement benefits.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PAY YOUR BILL: Pay the debt in full by the balance due date on the

initial billing statement to avoid late charges and collection action:

In Person: At your local Veteran Affairs Medical Center's Agent

Cashier's Office

By Phone: (see below for local information)

By Mail: (see below for local information)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

LATE CHARGES: The VA is required to assess late charges on balances which

remain unpaid thirty (30) days after the statement date. These charges

consist of interest and administrative fees at rates established each

year. Interest will be charged from the date charges first appear on the

statement. You can avoid these charges by making timely payments by the

balance due date on the statement. A monthly administrative cost or

collection fee will be added to your debt if, within thirty (30) days of

the date of the statement on which charges first appear, full payment of

the debt is not received or a repayment plan agreement is not approved.

If an installment repayment plan is established and any installment is not

received by the due date, the monthly administrative cost or collection

fee will thereafter be charged until the debt is paid. Other collection

costs may be added to the debt if additional collection actions become

necessary.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

WAIVER: You have the right to request a waiver of part or all of your

debt. If the waiver is granted you will not be required to pay the amount

waived. To do so, submit an explanation and a completed Financial Status

Report (VA Form 5655) found at: www.va.gov/vaforms/va/pdf/VA5655.pdf.

Your explanation should include why you are not responsible for the debt

and any undue hardship the payment of the debt would cause you. You have

the right to request a hearing in connection with your request for a

waiver. To do so, submit a written request for hearing with your waiver

request. VA will notify you of the date, time and place where the hearing

will be held. Refer to the "Customer Service" and "Submitting Your

Request" sections below for more information.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMPROMISE OFFER: You have the right to request a compromise. A

compromise means you may propose a lesser amount as full settlement of the

debt. To request a compromise, submit your request in writing to VA,

specifying the dollar amount you are proposing VA should accept as payment

in full, and a completed Financial Status Report (VA Form 5655) found at:

www.va.gov/vaforms/va/pdf/VA5655.pdf. Refer to the "Customer Service"

and "Submitting Your Request" sections below for more information.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REPAYMENT PLAN: You have the right to establish a monthly repayment plan

at any time during your enrollment in VA health care if you cannot pay

your debt in full. To do so, submit a completed Agreement to Pay

Indebtedness (VA Form 1100) found at:

www.va.gov/vaforms/va/pdf/VA1100.pdf. Indicate your proposed monthly

payment amount in paragraph 1A. Refer to the "Customer Service" and

"Submitting Your Request" sections below for more information.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DISPUTE THE EXISTENCE OR AMOUNT OF THE DEBT: You have the right to

dispute the existence or amount of the debt. To do so, submit a letter

explaining why you question the validity or amount of the debt. To avoid

late charges, you must submit a dispute by the balance due date on the

statement. VA will not initiate collection if your dispute is received

within sixty (60) days from the initial billing statement. If VA receives

your notice later than sixty (60) days and collection has been initiated,

it will continue while the dispute is being reviewed. If the dispute is

resolved in your favor, all late charges will be removed from your

account, and any amounts withheld from your VA benefits, federal payments,

or wages will be refunded to you. Refer to the "Customer Service" and

"Submitting Your Request" sections below for more information.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CUSTOMER SERVICE: For additional information or assistance:

In Person: At your local Veteran Affairs Medical Center's

Agent Cashier's Office

By Phone: (see below for local information)

Online: Visit www.va.gov/vaforms to retrieve VA forms

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SUBMITTING YOUR REQUEST: Submit the required VA forms or documents to

apply for one of VA's Financial Hardship Programs:

In Person: At your local Veteran Affairs Medical Center's Agent

Cashier's Office

By Mail: Send completed forms and/or other required documentation

to the VA address at the top right of your statement to the

attention of the Fiscal Office/Bill of Collection Manager

For additional information, to request necessary forms or assistance in

accessing forms online, contact VA at REDACTED.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REPRESENTATION: An accredited representative of a Veteran Service

Organization or other service organization recognized by the Secretary of

Veterans Affairs may represent you without charge. You may employ an

attorney or VA accredited agent to assist you. The services of an

attorney or accredited agent representing you in adjudicative proceedings

before VA are subject to a fee limitation as set forth in 38 U.S.C. 5904.

If you desire representation and have not already designated a

representative, contact VA at REDACTED to request the necessary

forms. If an attorney or accredited agent represents you before VA, a

copy of any agreement between you and the attorney or accredited agent

about the payment of the attorney's or agent's fees must be filed at the

following address: Counsel to the Chairman (01C3), Board of Veterans

Appeals, 810 Vermont Avenue N.W., Washington D.C. 20420.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NOTICE TO CUSTOMERS MAKING PAYMENT BY CHECK: When you provide a check as

payment, you authorize VA to either use information from your check to

make a one-time electronic fund transfer from your account or to process

the payment as a check transaction. When VA uses information from your

check to make an electronic fund transfer, funds may be withdrawn from

your account as soon as the day we process your payment, and you will not

receive your check back from the financial institution. A Privacy Act

Statement required by 5 U.S.C. & 552a(e)(3) stating our authority for

soliciting and collecting the information from your check, and explaining

the purposes and routine uses which will be made of your check

information, VA Notice of Privacy Practices, IB 10-163 is available online

at www.va.gov/vhapublications or call toll free at 1-866-400-1238 to

obtain a copy by mail. Furnishing the check information is voluntary, but

a decision not to do so may require you to make payment by some other

method.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUESTIONS ABOUT PAYMENTS: Payments made in the past ten (10) days may not

have been applied to your account by the time your statement was prepared.

If so, this payment will be reflected in your account on the next

statement. For assistance in understanding your statement and assessed

charges contact VA at (see below for local information).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VA PRIVACY: The VA Notice of Privacy Practices, IB 10-163, which outlines

your privacy rights, is available online at www.va.gov/vhapublications,

or you may obtain a copy by writing the VHA Privacy Office (10P2C1) at 810

Vermont Avenue NW, Washington, DC 20420.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Local Agent Cashier Contact Information

Office Phone: (555)555-5555

Mailing Address: JANE DOE, AGENT CASHIER 04F

CHEYENNE, WY 82001

## Display Pending Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays a new bill with the status Pending Approval for purposes of review. The approving official of a new bill would use this option to review a bill before they approve it for release to the Accounts Receivable Section. If errors are found in the bill, use the Edit Bill option to correct them.

BILL \#: 000-K20061 DATE: 2/18/93 TYPE: 1114

DEBTOR: BILLING AGENCY:

ARpatient,one JAMES E VAN ZANDT VAMC

101 WALT ROAD 2907 TEST BLVD.

ORLANDO, FL 43434 ALTOONA, PA 16602-4377

CONTROL POINT:

APPROVING OFFICIAL:

DATE DESCRIPTION QTY COST PER AMOUNT

-------------------------------------------------------------------------

2/18/93 2 10.0000 EA 20.00

Testing Display Pending Bill Option

## Approve/Print Pending Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows an authorized individual to approve and print all new bills within their service and release them to the Accounts Receivable section; you will not be able to print 1114 bills. Once a new bill has been created using the New Bill (Enter) option, the bill will automatically be passed to the person within the service/section who is authorized to approve it and release it to Fiscal Service. This approving official will be reminded by the system when they logon to review the bill; if necessary, they may send the bill back to the billing clerk for further editing.

This option requires an Electronic Signature Code, which means only the holders of the PRCASVC security key will have access to this option. The computer uses the signature code to verify that you are authorized to approve bills and will show you only those bills that you are authorized to see. You will not be able to take action on any bill from any other service/section.

> **NOTE:** Once a bill has been released to the AR Section, you will no longer have any access to it. If you discover that further corrections are required, the Accounts Receivable Section must return the bill to you. This action removes your electronic signature (and your authorization) and allows you to either cancel or amend the bill.

Select Billing Option: APProve/Print Pending Bill

Enter Electronic Signature Code:\<electronic sig\> \<Signature verified\>

Select ACCOUNTS RECEIVABLE BILL NO.: K20005 000-K20005 VENDOR 02-14-93 ARpatient,one PENDING APPROVAL

Review Bill? YES//\<ret\> (YES)

BILL \#: 000-K20005 DATE: 2/14/93 TYPE: 1114

DEBTOR: BILLING AGENCY:

ARpatient,one

P.O. BOX 000 ,

ALTOONA, PA 16635

APPROVING OFFICIAL:

DATE DESCRIPTION QTY COST PER AMOUNT

-------------------------------------------------------------------------

2/14/93 10 2.0000 20.00

Approve this Bill? NO// YES (YES)

\*\*\* This bill has been released to the AR section \*\*\*

## Edit Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows information for a new or incomplete bill to be edited. This is the mechanism that allows correction of erroneous bills before they are released to Fiscal Service. If the bill has previously been approved and sent to Fiscal Service and returned, you cannot use this option to correct it; you must use the Amend Bill Returned from AR option. Entering the bill number invokes the system to display the current bill information and provides the opportunity to change it.

## Cancel Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the cancellation of a new or incomplete bill that has not been approved. This is often used when an erroneous bill has been discovered and it would be more efficient to start over with a new one. At that point, cancel the erroneous bill and create a new one to replace it. However, you will not be able to cancel a bill once it has been approved and released to Fiscal. If this situation should occur, you should contact the Accounts Receivable Section and request that the bill be returned to you for cancellation.

Select Billing Option: CANCEL Bill

Select ACCOUNTS RECEIVABLE BILL NO.: K20006 000-K20006 VENDOR 02-14-93 NO DEBTOR NAME ! BILL INCOMPLETE

Sure you want to cancel this Bill? NO// YES (YES)

## Amend Bill Returned from AR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is used to make changes to bills that have a Returned For Amendment status. It allows editing of bills that have been returned from Fiscal Service.

Once a bill is released to Fiscal Service, you will no longer have the ability to make changes to it unless it has been returned to you. Often times a bill is returned from Fiscal because it doesn't meet certain criteria. Use this option to correct the bill. You may not use the Edit Bill option on bills returned from AR because only the Amend Bill Returned From AR option leaves an audit trail.

BILL \#: 000-K20084 DATE: 3/1/93 TYPE: 1114

DEBTOR: BILLING AGENCY:

ARpatient,one

APPROVING OFFICIAL: /ES/ ARpatient,one DATE: 10/1/93

DATE DESCRIPTION QTY COST PER AMOUNT

-------------------------------------------------------------------------

3/1/93 0.45 100.00 45.00

COMPUTER AIDED GRAPHIC DESIGN MONITOR BROKE WHILE

USING FOR SPECIAL PROJECT FOR DEPARTMENT OF

VETERANS AFFAIRS.

3/5/93 4.5000 EA 0.00

Now amending bill...

AMENDED DATE: OCT 22,1994//\<ret\> (OCT 22, 1994)

AMENDED AMOUNT: 4.50

SERVICE COMMENTS (AMEND):\<ret\>

## BILL STATUS LISTING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists all bills with a given status. This report will contain the bill's number, date, category, debtor, and balance. In addition, a summary will appear at the end of the report which will show the total number of bills with this status and the total balance of all bills with this status. To view this report, enter the status name at the system prompt.

Common statuses searched for by Billers are Pending Approval, Returned For Amendment, and Canceled Bill; however, billers have the ability to get any status listing that would fulfill their needs. The following table shows a list of all valid bill statuses.

| Bill Statuses |                            |
|-------------------|----------------------------|
| ACTIVE            | OLD BILL                   |
| ADD (AMEND)       | OPEN                       |
| AMEND             | PENDING APPROVAL       |
| AMENDED BILL      | PENDING ARCHIVE            |
| ARCHIVED          | RE-ESTABLISH               |
| BILL INCOMPLETE   | REFUND REVIEW              |
| CANCELLATION      | REFUNDED                   |
| CANCELED BILL | RETURNED FOR AMENDMENT |
| COLLECTED/CLOSED  | RETURNED FROM AR (NEW)     |
| DELETE (AMEND)    | SUSPENDED                  |
| IN-ACTIVE         | SUSPENSE                   |
| INCOMPLETE        | WRITE-OFF                  |
| NEW BILL          |                            |

Status: NEW BILL

Bill no. Date Prepared Category Debtor Balance

-------------------------------------------------------------------------

000-K20005 FEB 14,1994 VENDOR ARpatient,one 20.00

000-K20158 SEP 1,1994 CURRENT EMP. ARpatient,two 150.00

000-K20172 SEP 10,1994 VENDOR ARpatient,three 200.00

TOTAL: 370.00

COUNT: 3.00

MEAN: 123.33 \* -indicates that patient is deceased

## LIST ALL BILLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists all bills within a given range. The report contains all pertinent information such as bill number, date, debtor, form type, status, original amount, and current balance.

This is often used to facilitate searching for an unknown bill number or debtor. It doesn't require you to go through every bill in your system, because all you need to know is a range where you think this unknown bill would appear.

BILL STATUS LIST FOR SERVICE OCT 22,1994 22:26 PAGE 1

Form Original Current

Bill \# Prepared Debtor Type Status Amount Balance

-------------------------------------------------------------------------

000-K00016 12/10/92 ARpatient,one 1081 ACTIVE 0 0.00

000-K00017 12/10/92 ARpatient,two 1080 CANCELLED 0 0.00

000-K00018 12/14/92 ARpatient,three 1081 ACTIVE 0 20.00

000-K00031 12/16/92 ARpatient,four 1114 ACTIVE 5000 5074.68

000-K00033 11/16/92 ARpatient,five 1080 WRITE-OFF 180 210.00

000-K00037 12/17/92 ARpatient,six 1114 ACTIVE 20 302.34

000-K00041 12/28/92 1114 CANCELLED 0 0.00

000-K00043 01/03/93 ARpatient,seven 1114 ACTIVE 200 208.21

000-K00044 01/03/93 ARpatient,eight 1114 CANCELLED 0.00

000-K10001 08/12/92 ARpatient,nine 1114 CANCELLATI 8 0.00

000-K10002 08/12/92 ARpatient,ten 1114 PENDING 10 3.00

000-K10003 08/13/92 ARpatient,one 1114 ACTIVE 40 40.00

000-K10004 08/13/92 ARpatient,two 1080 SUSPENSE 400 400.00

000-K10006 08/17/92 ARpatient,three 1081 PENDING 20 20.00

000-K10007 08/31/92 ARpatient,four 1114 PENDING 500 500.00

## VIEW A BILL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows viewing of any bill and any activity or event that has happened to it. It is very similar to the Profile of Accounts Receivable, except this option appends a description of the charges to the end of the report. A printout of the bill can also be obtained by selecting the appropriate device.

This will most often be used to acquire any information about a debtor's bill, which is generally helpful for debtor inquiries.

AUG 26,1994 09:53 ACCOUNTS RECEIVABLE PROFILE

==========================================================================

NAME: ARpatient,one BILL \#: 000-4K0005R

WASHINGTON, DC PHONE NO.:

CURRENT STATUS: PENDING APPROVAL CATEGORY: FEDERAL AGENCIES-REIMB.

FUND (APPROPRIATION): 0160A1

DATE BILL PREPARED: APR 29,1994

ORIGINAL AMOUNT: 1000.00

FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

----------- ------------ --------------- ------

94 1000.00

BALANCES PAID

LETTER1/ICD:

PRINCIPAL: 1000.00 0.00 LETTER2:

INTEREST: 0.00 0.00 LETTER3:

ADMINISTRATIVE: 0.00 0.00 IRS LETTER:

DC/DOJ REF.DATE:

CURRENT: 1000.00 0.00

TRANSACTIONS:

5 RETURNED FOR AMENDMENT 04/29/94 1000.00

BILL RESULTING FROM: OVERPAYMENT

Date Description Quantity Units Cost Total Cost

==========================================================================

04/29/94 0.00 0.0000 0.00