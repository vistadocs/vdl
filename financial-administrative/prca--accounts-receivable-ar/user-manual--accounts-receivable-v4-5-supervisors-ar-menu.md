---
title: Accounts Receivable Version 4.5 User Manual - Supervisor's AR Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Supervisor's AR Menu
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
menu_options: 1
description: - [Supervisor’s AR Menu](#supervisors-ar-menu) - [Edit/Add “Bill Resulting From” List](#editadd-bill-resulting-from-list) - [Delete an Incomplete Transaction](#delete-an-incomplete-transaction) - [Administrative Cost Adjustment](#administrative-cost-adjustment) - [Form Letter Menu (Edit/Print)](#for
audience: 
keywords: 
  - table
  - contents
  - site
  - bill
  - edit
  - group
  - report
  - statements
  - form
  - parameters
page_count: 0
word_count: 3160
section_count: 12
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_6supvisr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_6supvisr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![](accounts-receivable-version-4-5-user-manual-supervisor-s-ar-menu/001.png)

# Supervisor’s AR Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Supervisor’s AR Menu](#supervisors-ar-menu)
  - [Edit/Add “Bill Resulting From” List](#editadd-bill-resulting-from-list)
  - [Delete an Incomplete Transaction](#delete-an-incomplete-transaction)
  - [Administrative Cost Adjustment](#administrative-cost-adjustment)
  - [Form Letter Menu (Edit/Print)](#form-letter-menu-editprint)
    - [Edit Form Letters](#edit-form-letters)
    - [Print Form Letters](#print-form-letters)
  - [Return Bill to Service](#return-bill-to-service)
  - [Agency location code (deposits)](#agency-location-code-deposits)
  - [ARCHIVE MENU](#archive-menu)
    - [detailed report of pending archive records](#detailed-report-of-pending-archive-records)
    - [Unmark records marked for archival](#unmark-records-marked-for-archival)
  - [Bad Debt Accrual OverRide](#bad-debt-accrual-override)
  - [nATIONAL ROLL-UP REPORT](#national-roll-up-report)
  - [Purge unprocessed fms document file](#purge-unprocessed-fms-document-file)
  - [site parameter edit](#site-parameter-edit)
    - [Deactivate Group](#deactivate-group)
    - [Group parameters](#group-parameters)
    - [interest/ADMIN/penalty rates](#interestadminpenalty-rates)
    - [IRS parameters](#irs-parameters)
    - [statement parameters](#statement-parameters)
    - [STOP/REACTIVATE NEW REFERRALS to TCSP](#stopreactivate-new-referrals-to-tcsp)

## Edit/Add “Bill Resulting From” List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option defines the list of reasons why a bill might be created. This user-defined list is used in other places throughout the package. This is used during the bill audit process by the Fiscal Auditor. Under the Clerk’s option, Audit An Electronic Bill, the system prompts for “Bill Resulting From”. Only entries from the Edit/Add “Bill Resulting From” List will be valid replies to this prompt.

Select Supervisor’s AR Menu Option: EDIT/Add “Bill Resulting From” List

Select AR DEBT LIST BRIEF NAME: DC

ARE YOU ADDING “DC” AS A NEW AR DEBT LIST (THE 35TH)? Y (YES)

AR DEBT LIST FULL NAME: DOCUMENTATION

BRIEF NAME: DC//\<ret\>

FULL NAME: DOCUMENTATION//\<ret\>

TYPE: ??

This is the type of the bill - Vendor, third party, patient, etc.

Enter “??” for a listing of available types.

CHOOSE FROM:

CP PATIENT

V VENDOR

NT THIRD PARTY/INSTITUTION

O PERSON

X ALL TYPE

NOPV VENDOR/PERSON/PATIENT/INSTITUTION

IO INSURANCE/PERSON

NV INSTITUTION/VENDOR

VO VENDOR/PERSON

VON VENDOR/PERSON/INSTITUTION

TYPE: VENDOR

## Delete an Incomplete Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option deletes erroneous transaction records for a given bill. During normal operations, the system will not allow an incomplete transaction to be entered. However, if there is a power failure, or if the system manager takes the system down without warning you, it is possible for incomplete transactions to become part of an account record. This option allows you to delete these records which clutter up an account.

## Administrative Cost Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option adjusts the interest or administration charges for an account. There are two ways you can use this option to adjust the interest or administration charges on an account. You can either reduce (or increase) the interest and administrative charges individually, or you can exempt the account from the charges which will reduce any existing outstanding balances to zero. These transactions will not show up in the Account Profile. You will know it took effect when you see that the total balance due on the account has been reduced to zero.

Select Supervisor’s AR Menu Option: ADMINISTRATIVE Cost Adjustment

Select ACCOUNTS RECEIVABLE BILL NO.: AA0008 000-AA0008 RX CO-PAYMENT/NSC

VET 08-18-92 ARpatient,one ACTIVE \$80.99

You may exempt the account from all the interest and administrative cost balances - making those balances zero (0), or adjust them.

Do you want to exempt the account from all the Int/Adm. costs? NO// YES

![](accounts-receivable-version-4-5-user-manual-supervisor-s-ar-menu/002.png)

## Form Letter Menu (Edit/Print)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options necessary to edit or print demand letters, including the various letters of indebtedness.

As the supervisor of Accounts Receivable, you have the authority to edit the body text of the canned letters that the system prints out for you. Before you do any editing, you should be familiar with the Text Editing features described in the User’s Guide to Computing (available from your IRM). Refer to the Clerk’s Follow-Up Letter Menu option for a discussion of the letters.

Warning : It is important to remember not to tamper with the formatting windows enclosed in vertical bars. These windows control the appearance of the letters when they are printed; you can cause yourself and your Site Manager endless amounts of grief if you make a small typographical error. If you have any doubts, contact your station’s support staff before you proceed. The reason for this option is that the obligatory text of these letters changes as regulations change.

### Edit Form Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays follow-up letter text for editing purposes. As the supervisor of Accounts Receivable, you have the authority to edit the body text of the canned letters that the system prints out for you. Before you do any editing, you should be familiar with the Text Editing features described in the User’s Guide to Computing (available from your IRM). This option should be used only when VACO or DC changes the wording of form letters.

Select Form Letter Menu (Edit/Print) Option: EDIT Form Letters

Select AR FORM LETTER NAME: ??

CHOOSE FROM:

CREDIT Notice of Credit Balance

FL 4-480 Ineligible Hospital (1FU)

FL 4-481 Humanitarian (1FU)

FL 4-482 Ineligible Hospital/Humanitarian (2FU)

FL 4-483 All Debts \$25.00-\$599.99(except Pharm/Means Test) (3FU)

FL 4-483a Current Employee/Ex-employee/Vendor (2FU)

FL 4-484 Ineligible Hospital/Humanitarian \$600.00-\$1199.00 (3FU)

FL 4-485

FL 4-513 Pharmacy and Means Test (1/2/3 FU)

FL 4-520a Current Employee (1FU)

FL 4-520b Ex-Employee (1FU)

FL 4-520c Current Employee - Prior 12/28/85 (1FU\*)

FL 4-520d Ex-employee - Prior 12/28/85 (1FU\*)

FL 4-521 Vendor (1FU)

FL 4-534 Ex-employee/Post Retirement (1FU\*)

IRS OFFSET IRS Offset Notice

Select AR FORM LETTER NAME: CREDIT Notice of Credit Balance

MAIN FORM BODY:. . .

18\>

20\> If there has been no charging activity on the account within the past

21\> year, the credit balance will be refunded if less than or equal

22\> to \$25.00. However, VA will not issue refunds for credit

23\> amounts of less than \$1.00.

EDIT Option:\<ret\>

### Print Form Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the appropriate form letter to see what a letter would look like for a given debtor. It is not recommended that this option be used to print and send a letter to a patient because it does not log this action or event within the patient’s account.

## Return Bill to Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option returns a given bill to the service that initially established it.

Once a bill has been approved and released by the billing service, it is no longer visible to the billing clerk or approving official. If you discover that the bill must be released back to the service during the audit portion of the billing cycle in Fiscal Service, or through correspondence with the debtor you have discovered a reason to send the bill back to the service, this option will let you return the bill. Returning the bill removes the Electronic Signature Codes; in order for the bill to become valid again, it must be routed through the service’s approving official.

Select Supervisor’s AR Menu Option: RETURN Bill to Service

Select ACCOUNTS RECEIVABLE BILL NO.: K00000 000-K00000 VENDOR 08-04-93 ONE,TEST VENDOR ACTIVE \$2044.66

Are you sure you want to return this bill to the Service ? NO// Y (YES)

DATE RETURNED TO SERVICE: AUG 4,1994//\<ret\>

FISCAL COMMENTS (RETURN): TEST// Re-Do

## Agency location code (deposits) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Supervisor to change the Agency Location Code. After conversion to AR 4.5 the ALC field is blank and must be assigned an ALC. See the Installation Guide for more information on this.

## ARCHIVE MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](accounts-receivable-version-4-5-user-manual-supervisor-s-ar-menu/003.png)

This menu contains options that allow a Supervisor to review bills prepared for archival. One of the options also allows a bill to be unmarked which excludes it from being archived.

### detailed report of pending archive records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a detailed listing of all bills that have been marked for archive; i.e., bills with a status of Pending Archive. The report contains the bill numbers and their respective debtor, category, old status, balance, and date of last activity.

Supervisors should use this report to determine those Veterans” bills that should not be archived and purged from the system. These include bills that may continue activity in the future. One example is Reimbursable Health Insurance bills which may be in litigation for long periods of time and could be recalled.

After determining particular bills that should not be archived (i.e., kept on the system) or there is not enough disk space, unmark appropriate bills to ensure they do not get archived or there is enough disk space to hold converted data. See the Unmark Records Marked For Archival option.

### Unmark records marked for archival

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option “de-selects” a particular bill that is pending archival. Valid bills to unmark include only bills that have already been marked for archival. See the Mark AR Records For Archival option.

After identifying bills to keep on your system, use this option to “unmark” them. This changes their status from Pending Archival to their previous status and ensures that they will not be archived then purged from the system.

## Bad Debt Accrual OverRide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu option will allow the user to over-ride the calculated write-off and contract adjustment totals from the 0160 appropriation (Ineligible Hospital and Emergency/Humanitarian), 2431 (Nursing Home Care NSC, Outpatient Care NSC, Hospital Care NSC, C Means test, Nursing Home Care per diem, and Hospital Care per diem), and the 5014 appropriation (Workers” Comp., No Fault Auto Accident, Crimes of Personal Violence, Reimbursable Health Insurance, and Rx Co-Pay).

Select OPTION NAME: BAD DEBT ACCR. EDIT BAD DEBT ACCRUAL OVER-RIDE

FUND: 0160

Previous Estimated Write-off Amount: 0

CURRENT EST. WRITE-OFF AMT.: 6036.02//

Previous Estimated Cont. Adj. Amount: 0

CURRENT EST. CONT. ADJ. AMT.: 0//

FUND: 2431

Previous Estimated Write-off Amount: 0

CURRENT EST. WRITE-OFF AMT.: 0//

Previous Estimated Cont. Adj. Amount: 0

CURRENT EST. CONT. ADJ. AMT.: 0//

FUND: 5014

Previous Estimated Write-off Amount: 0

CURRENT EST. WRITE-OFF AMT.: 300128.6//

Previous Estimated Cont. Adj. Amount: 0

CURRENT EST. CONT. ADJ. AMT.: 1986055.06//

## nATIONAL ROLL-UP REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report prints out information contained on the national roll-up. It allows selection of a range of dates for a set of criteria entered by the user. It also gives the option of printing a “detailed” report. A “detailed” report will list all bills and transactions for each criteria selected with the corresponding amounts.

> **NOTE:** The “Detailed” option should be used with caution as it will list each bill and each transaction for every sub-category of the chosen category, hence being very lengthy.

Select Supervisor’s AR Menu Option: NATional Roll-up Report

Starting ROLL-UP Date: 9-1 (SEP 01, 1994)

End ROLLUP Date: 9-30 (SEP 30, 1994)

This response must be a list or range, e.g., 1,3,5 or 2-4,8.

Enter Criteria Number(s): (1-20): ??

1\. NSC NURSING HOME COPAY

2\. NSC HOSPITAL COPAY

3\. NSC OUTPATIENT

4\. NSC INPATIENT INSURANCE

5\. NSC OUTPATIENT INSURANCE

6\. SC/NSC INPATIENT INSURANCE

7\. SC/NSC OUTPATIENT INSURANCE

8\. WORKERS COMP

9\. NO FAULT AUTO

10\. CRIMES OF PERSONAL VIOLENCE

11\. NSC PHARMACY COPAY

12\. SC PHARMACY COPAY

13\. PREPAYMENTS

14\. INELIGIBLE

15\. TORT FEASOR

16\. EMERGENCY/HUMANITARIAN

17\. SHARING AGREEMENT

18\. OTHER APPROPRIATIONS

19\. \$10/DIEM NSC HOSPITAL COPAYS

20\. \$5/DIEM NSC NURSING HOME COPAYS

Enter Criteria Number(s): (1-20): 3,4

Do you want a detailed report?

Enter Yes or No: NO// ?

A “Detailed” report will list the criteria and totals with each bill and

transaction for that criteria listed.

A “No” answer to this question will print out just the criteria and totals.

Answer “YES” or “NO”

Enter Yes or No: NO// \<ret\>

QUEUE TO PRINT ON

DEVICE: HOME// PC RUNNING SMARTERM 420 \[YOU CAN NOT SELECT A VIRTUAL TERMINAL\] *Must use a device other than HOME for this report!*

PREVIOUSLY, YOU HAVE SELECTED QUEUEING.

DO YOU STILL WANT YOUR OUTPUT QUEUED? YES// (YES)

DEVICE: HOME// ISC21 ROOM 730/16 PITCH/LASER III RIGHT MARGIN: 132//

## Purge unprocessed fms document file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to purge the AR/FMS document file (347). It will purge all entries older than the date entered by the user and should be used with care.

## site parameter edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options that define parameters relative to each site. This builds more flexibility into your software allowing it to be customized to fit your site’s needs.

### Deactivate Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Supervisor user to deactivate a currently active “group”.

Select Site Parameter Edit Option: deactivate Group

Select AR GROUP NAME: test2 ACCOUNS RECEIVABLE

Are you sure you want to Deactive Group “test2”? NO// y YES

\*\*\* Group Deactivated \*\*\*

### Group parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option adds or edits a billing agency’s demographic information including the name, address, city, state, zip, phone number, and hours of operation.

Use this to add a “group” like District Counsel, its address, and other necessary information. An AR GROUP has an associated type (AGENT CASHIER, RETURN PAYMENT, etc.) that has a name assigned by the site.

Select Site Parameter Edit Option: GROUP Parameters

Select AR GROUP NAME: ??

CHOOSE FROM:

ACCOUTS RECEIVABLE Type: ACCOUNT RECEIVABLE

HOSPITAL Type: SITE

VAMC Type: BILLING AGENCY

PATIENT STATEMENT ADDRESS Type: AGENT CASHIER

RETURN PAYMENT Type: RETURN PAYMENT

TEST Type: DISTRICT COUNSEL

This is the name assigned to the AR GROUP by the site. An AR GROUP

has an associated type (AGENT CASHIER, RETURN PAYMENT, etc.)

that has a name assigned by the site.

Select AR GROUP NAME: DOCUMENTATION

ARE YOU ADDING “DOCUMENTATION” AS A NEW AR GROUP (THE 9TH)? Y (YES)

AR GROUP TYPE: ??

CHOOSE FROM:

1 AGENT CASHIER

2 DISTRICT COUNSEL

3 DEPARTMENT OF JUSTICE

4 ACCOUNT RECEIVABLE

5 SITE

6 BILLING AGENCY

7 INACTIVE

8 RETURN PAYMENT

AR GROUP TYPE:

### interest/ADMIN/penalty rates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option modifies the interest, administration, and penalty rates for the effective date. Use this to increase/decrease the rates respectively when the current rates change. This menu option is locked with security key PRCAF LATE CHARGES.

Select Site Parameter Edit Option: INTEREST/Admin/Penalty Rates

Accounts Receivable Interest/Admin/Penalty Rate Report

OCT 22,1994 23:11 PAGE 1

RATE ANNUAL MONTHLY ANNUAL

EFFECTIVE INTEREST ADMIN PENALTY

DATE RATE CHARGE RATE

-------------------------------------------------------------------------

SITE: ALTOONA VAMC

JAN 1,1991 0.080 0.91

JUL 1,1991 0.085 0.91

JAN 1,1994 0.010 1.33 0.0800

Select RATE EFFECTIVE DATE: JAN 1,1994// Jan 1, 1994 JAN 1, 1994

ARE YOU ADDING “JAN 1, 1994” AS A NEW RATE EFFECTIVE DATE (THE 4TH FOR THIS AR SITE PARAMETER)? Y (YES)

ANNUAL INTEREST RATE: .095

MONTHLY ADMIN CHARGE: 1.00

ANNUAL PENALTY RATE: .05

### IRS parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option initializes the automation of the IRS referral functionality. The automation requires these parameters be set to function.

The parameters that need to be defined include the date for the IRS master code sheets to be sent to Austin; the date IRS offset letters are sent to respective patients, the current charge rate, and the responsible official.

Select Site Parameter Edit Option: IRS Parameters

RESPONSIBLE FOR IRS CODESHEETS: TWO,TEST

// ONE,TEST

DATE OF MASTER IRS OFFSET: NOV 26//\<ret\>

DATE OF IRS OFFSET LETTER: OCT 4//\<ret\>

IRS OFFSET AMOUNT: 9.35// 6.50

### statement parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option defines the characteristics for all of the patient statements. This includes defining the following parameters:

- Suppress Rights & Obligations
- Pharmacy Copay Statement Info (Brief or Expanded)
- Suppress Zero Balance
- Burster Machine Code
- Statement Comment
- UB Printer: (for UB-92 Forms)
- Report Printer
- Local CCPC Statements: (No Statements Sent or Send Statements To Local Mail Group)
- Local Statement Printer

Use this option to customize your site’s patient statements. “Suppress Rights & Obligations” means that the Notice of Rights which is the pharmacy and copay form letter will not print with the respective patient statements.

By defining brief or expanded, the level of detail for patient statements will print a brief or expanded version of each charge. An expanded version includes the following information: (1) the PRESCRIPTION NUMBER, (2) the DRUG NAME, (3) the number of DAYS the prescription will SUPPLY, (4) the prescribing PHYSICIAN, (5) the quantity of the prescription, and (6) the respective DATE each prescription was FILLED. A brief version includes the following: (1) the PRESCRIPTION NUMBERS and (2) the respective DATE each prescription was FILLED.

“Suppression Zero Balance” means that no statement will print if the statement has a balance due of \$0.00.

Code for the burster machine to recognize when to stuff the envelopes can be defined, for example: W ?90,“-------”.

> **NOTE:** IRM will need to edit this field to insert the MUMPS code necessary to write-out the burster machine code.

Two lines of text can be defined for all statements that are printed. This text can be anything from simple directions for making payments to holiday greetings for all of your customers.

Parameters to designate printers for UB Forms/Statements, Reports, and Local (Oversized) Statements are also included.

Finally, the LOCAL CCPC STATEMENTS parameter determines whether the RCCPC STATEMENTS mail group receives the CCPC Patient Statement transmission messages that go to the CCPC. Choices are NO STATEMENTS TO LOCAL MAIL GROUP and SEND STATEMENTS TO LOCAL MAIL GROUP. Suggest sending the statements in order to have a copy.

Select Site Parameter Edit \<TEST ACCOUNT\> Option: Statement Parameters

SUPPRESS RIGHTS & OBLIGATIONS: NO//

PHARMACY COPAY STATEMENT INFO: EXPANDED//

SUPPRESS ZERO BALANCE: YES//

BURSTER MACHINE CODE:

STATEMENT COMMENT: To pay your statement online, go to www.pay.gov or call 1-888-827-4817. Replace

UB PRINTER: \<enter the printer used for UB-92 Forms\>

REPORT PRINTER: \<enter the printer used for printing reports\>

LOCAL CCPC STATEMENTS: SEND STATEMENTS TO LOCAL MAIL GROUP

//

LOCAL STATEMENT PRINTER: \<enter the printer used for oversized statements\>

### STOP/REACTIVATE NEW REFERRALS to TCSP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to stop or reactivate new referrals to Cross-Servicing for an entire site in such events as a FEMA designated disaster location. Users need the PRCA CS STOP SITE key to be able to access this option. The system will display the current status of the Stop/Reactivate New Referrals to TCSP site parameter, along with the date the status was set, and the User who performed the stop or reactivate.

Stop example:

Select Site Parameter Edit \<TEST ACCOUNT\> Option: 2 Stop/Reactivate new referrals to TCSP

SITE IS REACTIVATED as of 05/13/2019 by LLLLL,KKKKKKK M

Are you sure you want to stop site? NO// y YES

\*\*\*\* SITE IS NOW STOPPED \*\*\*\*

Reactivate example:

Select Site Parameter Edit \<TEST ACCOUNT\> Option: 2 Stop/Reactivate new referrals to TCSP

CHOOSE 1-2: 2 Stop/Reactivate new referrals to TCSP

SITE IS STOPPED as of 05/23/2019 by BBBBB,JJJJJJ B

Are you sure you want to reactivate site? NO// yes YES

\*\*\*\* SITE IS NOW REACTIVATED \*\*\*\*