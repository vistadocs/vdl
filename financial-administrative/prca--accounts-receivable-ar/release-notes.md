---
consolidated_title: "ar release notes"
app_code: PRCA
doc_type: RN
master_source: "PRCA*4.5*301 AR Release Notes"
master_pub_date: revision_count: 7
consolidated_from: 6 versions
prior_versions:
  - "PRCA*4.5*281 AR Release Notes"
  - "PRCA*4.5*310 AR Release Notes"
  - "PRCA*4.5*347 AR Release Notes"
  - "PRCA*4.5*373 AR Release Notes"
  - "PRCA*4.5*379 AR Release Notes"
---

> ![](prca-4-5-301-ar-release-notes/001.png)

Department of Veterans AffairsDebt Management CenterImplement Department of the Treasury’sCross-Servicing ProcessTAC-13-09842

Cross-Servicing

Accounts Receivable (AR)RELEASE NOTES /INSTALLATION GUIDEPRCA\*4.5\*301December 2016

*Version 1.1*

*(This page included for two-sided copying.)*Revision History

| Date       | Version | Description                                                                                                                                                                                                                              | Author    |
|------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 12/19/2016 | 1.1     | Slight modifications per HPS                                                                                                                                                                                                             | HPES Team |
| 11/02/2016 | 1.0     | Baseline Release                                                                                                                                                                                                                         | HPES Team |
| 10/17/2016 | .5      | Updated PRCA_45_P301_73.KID;1 information and installation instructions/information and patch description                                                                                                                                | HPES Team |
| 12/23/2015 | .4      | Addition of PRCA_45_P301_T62.KID;1 patch filename and v70 version# into Sec. 3 Patch Description                                                                                                                                         | HPES Team |
| 6/9/2015   | .3      | Added new blocked options on Cross-Serviced bills to Collections/Payments section                                                                                                                                                        | HPES Team |
| 4/22/2015  | .2      | Added Section 2.14 for Cross-Servicing Qualified / No Third Letter Sent; added Section 4.4 Post-Installation Instructions for Due Process Notification Routine; added Section 5 Backout / Rollback Procedures; updated Patch Description | HPES Team |
| 3/3/2015   | .1      | First draft document release                                                                                                                                                                                                             | HPES Team |

*(This page included for two-sided copying.)*Table of Contents

List of Figures

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Accounts Receivable 4.5 Enhancements](#accounts-receivable-45-enhancements)
  - [Cross-Servicing Menu](#cross-servicing-menu)
  - [Accounts Receivable Screens: Cross-Servicing Display](#accounts-receivable-screens-cross-servicing-display)
  - [Treasury Offset Program (TOP) Modifications](#treasury-offset-program-top-modifications)
  - [Cross-Servicing Referrals](#cross-servicing-referrals)
  - [Cross-Servicing Update File](#cross-servicing-update-file)
  - [Recall Debt or Debtor from Cross-Servicing](#recall-debt-or-debtor-from-cross-servicing)
  - [Cross-Servicing Collections / Payments](#cross-servicing-collections-payments)
  - [Cross-Servicing Unprocessable File](#cross-servicing-unprocessable-file)
  - [Reconciliation File](#reconciliation-file)
  - [Reports](#reports)
  - [Transaction Profile Screen Modifications](#transaction-profile-screen-modifications)
  - [Monthly Patient Statements](#monthly-patient-statements)
  - [Updated Due Process Notification Letter](#updated-due-process-notification-letter)
  - [Cross-Serviced Qualified / No Third Letter Sent](#cross-serviced-qualified-no-third-letter-sent)
- [Patch Description](#patch-description)
- [Installation Instructions](#installation-instructions)
  - [Obtain Patch](#obtain-patch)
  - [Run Optional Installation Options for Multi-Build](#run-optional-installation-options-for-multi-build)
  - [Install Build](#install-build)
  - [Post-Installation Instructions](#post-installation-instructions)
- [Backout / Rollback Procedures](#backout-rollback-procedures)
  - [Pre-Implementation Steps Required](#pre-implementation-steps-required)
  - [Software Rollback Procedures](#software-rollback-procedures)
  - [Database Rollback Procedures](#database-rollback-procedures)
The U.S. Department of Treasury (Treasury) Cross-Servicing project is the next phase in the implementation of the Debt Collection Improvement Act (DCIA) of 1996 by the Department of Veterans Affairs (VA). Previously, VA had implemented the Treasury Offset Program (TOP), which provided the Consolidated Patient Account Centers (CPAC) Accounts Receivable (AR) staff with an automated method of referring eligible, delinquent debts to Treasury. In May 2014, the Digital Accountability and Transparency Act of 2014 (DATA Act) was signed into law, requiring VA to notify Treasury of any legally enforceable non-tax debt owed to VA that is over 120 days delinquent so that Treasury can offset the debt administratively. The Cross-Servicing project will enable CPACs to transfer a debt that has been delinquent 120 days or more to Treasury for collection.
The modifications to the Accounts Receivable (AR) 4.5 application for Cross-Servicing are being released under Patch \# PRCA\*4.5\*301, which is being released in the host file: PRCA_45_P301.KID.
The following figure illustrates the high-level process flow for Cross-Servicing.
<span id="_Toc469998154" class="anchor"></span>Figure 1: Cross-Servicing Scope of Integration and Process Flow
![](prca-4-5-301-ar-release-notes/002.png)

# Accounts Receivable 4.5 Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a brief description of the new features and functionality of the Cross- Servicing patch (PRCA\*4.5\*301). More detailed information on the Cross-Servicing functionality can be found in the application user and technical manuals found on the AR Virtual Documentation Library (VDL) at the following link:

<http://www.va.gov/vdl/application.asp?appid=29>

## Cross-Servicing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the installation of this patch, a new Cross-Servicing Menu was created. From this menu, a user can select from the following options:

- Cross-Servicing Bill Report (for Cross-Servicing Reports, refer to Section 2.10)
- Cross-Servicing Recall Report
- Debt Referral Reject Report
- List IAI Error Codes
- Print Reconciliation Report
- Print Cross-Servicing Report
- Recall/Reactivate TCSP Referral for a Bill (refer to Section 2.6)
- Recall/Reactivate TCSP Referral for a Debtor (refer to Section 2.6)
- Stop/Reactivate a TCSP Referral for a Bill (refer to Section 2.4)

Additional details are provided for the above menu items in the following sub-sections (as noted above).

## Accounts Receivable Screens: Cross-Servicing Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For debtors that have one or more bills referred to Cross-Servicing, the following AR Screens will now display Cross-Servicing referral, recall, and reject information:

- Full Account Profile
- Brief Account Profile
- Profile of Accounts Receivable
- Bill Profile
- Account Profile from the Agent Cashiers Menu

## Treasury Offset Program (TOP) Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following TOP modifications are also released under this patch:

- The 180-day, TOP-referral batch process was modified to exclude all new, First Party bills.
- New, First Party bills will no longer be referred to TOP. (Note that all First Party bills currently referred to TOP will remain in TOP.)
- First Party bills will now age in VistA until they are 120 days or older in delinquency and then will be referred to Cross-Servicing.
- The weekly batch referral to Cross-Servicing excludes accounts that are flagged referred to TOP.

## Cross-Servicing Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Cross-Servicing Referral enhancements are released under this patch:

- Batch task created in VistA to generate a file of delinquent, First Party bills.
- Batch process to create the referral file runs once per week for the new referrals, and is transmitted to the Austin Information Technology Center (AITC) once per week.
- A new field, *Debt Referred to Cross-Servicing,* now displays on the bill to flag a bill referred to Cross-Servicing.
- A new field, *CS Referred Date*, displays on the bill to identify the date the bill was referred to Cross-Servicing.
- When the bill is rejected for any reason, VistA removes the *Debt Referred to Cross-Servicing* and *CS Referred Date* flags.
- For all bills that have been referred to Cross-Servicing, VistA stops the accrual of interest and fees.
- VistA automatically creates a Referral File of delinquent First Party bills in Integrated Agency Interface (IAI) format, containing record types: H, 1, 2, 2A, 2C, and Z. Note that not all record types will be included in each referral.
- When the Referral Batch Job is completed, a bulletin (MailMan message) is generated confirming that the Referral File was transmitted.
- A bill can be prevented from being referred to Cross Servicing by running the “Stop/Reactivate a TCSP Referral for a Bill” VistA option. Users can toggle between Stopping and Reactivating a bill for referral using this option.

## Cross-Servicing Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also included in this patch is a Cross-Servicing Update File. The specifications of the Update File are provided below:

- Batch task created to generate an Update File in IAI format containing the updated information for previously referred bills.
- Batch process created to transmit the Update File, consisting of updates to a debt and debtor’s contact information to AITC once per week.
- No interest, fees, or bill amount increases are included in the Update File.
- Changes to a debtor’s name, Tax Identification Number (TIN), and address will be included in the Update File.
- Bill amount decreases for offsets originating from DMC will also be included in the Update File.
- VistA automatically creates an Update File in Integrated Agency Interface (IAI) format, containing an additional record type, 5B. 5A record types are not used. Note that not all record types will be included in each update.
- When the Update Batch Job is completed, a bulletin (MailMan message) is generated confirming that the Update File was transmitted.

## Recall Debt or Debtor from Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the new recall items on the Cross-Servicing Menu for recalling a debt or debtor, the following recall enhancements are released under this patch:

- Batch process runs once per week to automatically recall bills from Cross-Servicing that are less than \$25 and have had no payment activity in over 365 days.
- The Recall File, containing all recalled debts or debtors is sent to AITC in IAI format.
- When processing a manual recall on a debt or debtor, the user is prompted to enter a recall reason, which displays under the new field name, *CS Recall Reason*.
- The Debt Recall Reasons include: “01 Debt Referred in Error”, “07 Agency is Forgiving Debt”, and “08 Agency Can Collect through Internal Offset”. The Debtor Recall Reasons include: “03 Bankruptcy with Automatic Stay”, “05 Debtor is Disabled with the Inability to Pay”, and “06 Debtor is Deceased”.
- Once the Recall Batch Job is completed, a new field, *CS Recalled Date*, displays on the bill to identify the date the bill was recalled from Cross-Servicing.
- When the Recall Batch Job is completed, a bulletin (MailMan message) is generated confirming that the Recall File was transmitted.
- Note that once debt is recalled from Cross-Servicing, it cannot be re-referred to Cross- Servicing. However if a Debtor is recalled, additional new debts (bills) are allowed to be cross-serviced under that Debtor.

## Cross-Servicing Collections / Payments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following enhancements are released under this patch related to collections / payments on bills referred to Cross-Servicing:

- With the implementation of Cross-Servicing, VistA <u>prevents</u> the manual posting of payments when the bill is flagged as referred to Cross-Servicing.
- For active, First Party Bills referred to Cross-Servicing, VistA allows the automated application of payments from Treasury and DMC through the AITC Lockbox process.
- When a Treasury payment is applied at the bill level (via Lockbox), VistA updates the Total Cross-Servicing (CS) Debt amount.
- VistA keeps the bill active and continues to collect on a bill if payments made create a bill balance less than \$25.00 and a current payment plan exists for the First Party bill.
- For all bills referred to Cross-Servicing, the following option is now <u>blocked</u>:
  - Set Up Repayment Plan \[PRCAC SET REPAYMENT\]. A repayment plan must be set up by Treasury and not implemented by VHA in VistA.
- Before a user can perform the following options on a Cross-Serviced bill, the bill must first be recalled.
  - Fiscal Offer Terminated \[PRCAC TR TERM-FISCAL\]
  - Compromise Termination \[PRCAC TR TERM-COMPROMISE\]
  - Suspend an AR Bill \[PRCAC TR SUSPENDED\]
  - Partial Waiver \[PRCAC WAIVED PART\]
  - Full Waiver \[PRCAC WAIVED FULL\]
  - Administrative Cost Adjustment \[PRCAF ADJ ADMIN\]
- VistA generates a Collections bulletin (MailMan message) for Cross-Servicing.

## Cross-Servicing Unprocessable File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For those bills referred to Cross-Servicing and were rejected by AITC, DMC or Treasury, VistA receives and processes “reject” messages from all three groups in the form of an Unprocessable File in IAI format. The following additional enhancements are released under this patch for the Cross-Servicing Unprocessable File:

- VistA generates a MailMan message for Cross-Servicing rejects.
- VistA captures the first nine error codes from the IAI Unprocessable File for each rejected bill, and displays the reject source, reject code, the reject reason, and the reject date on the bill sub-screen on the Full Account Profile, Brief Account Profile, Account Profile from the Agent Cashiers Menu, and Profile of Accounts Receivable, as well as the Bill Profile screens.
- VistA prevents the re-referral of any rejected bills in future batch processing until the rejected bill is corrected and the ‘Stop’ flag is removed.

## Reconciliation File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Reconciliation File enhancements are released under this patch:

- VistA receives the Reconciliation File from Treasury via AITC on the first day of every month through VA MailMan.
- VistA generates a bulletin for Cross-Servicing indicating those returned debts / debtors that Treasury has sent in the Reconciliation File.
- When a debt is returned by Treasury, the Cross-Servicing referral information will be deleted from the returned debt. VistA populates the Effective Date for stopping the Cross-Servicing referral with the Returned Date in the R1 record and the Stop Referral Reason with ‘Other’ with a comment of ‘By Reconciliation’.
- When a debtor is returned by Treasury, the Cross-Servicing referral information on all debts for that debtor will be deleted. VistA populates the Effective Date for stopping the Cross-Servicing referral with the Returned Date in the R2 record and a Stop Referral Reason of ‘Other’.
- VistA generates a bulletin indicating those returned debts or debtors that Treasury sent in the Reconciliation File.
- VistA generates a bulletin indicating the compromise offers that Treasury has sent in the Reconciliation File.
- When a Reconciliation File is received with a Compromise Indicator = ‘Y’ on the R2 record (Field \# 19), VistA places a stop on the Cross-Servicing referral (which deletes the referral on all Cross-Serviced debts for that debtor). ‘Other’ is populated for the Stop Reason and an Effective Date for the stop is populated using the Closed Date from the R2 record (Field \# 21).

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Cross-Servicing Reports are released under this patch:

- Print Cross-Servicing Report: Lists bills referred to Cross-Servicing as of the date the report is run. The report includes the Bill Number, Debtor’s Name, SSN, Original Amount of Debt initially referred to Cross-Servicing, date sent for Cross-Servicing (CS Referred Date) and the Current Amount Owed on the bill / balance owed. User can sort by Bill Number, Debtor Name, or Cross-Servicing Referred Date.
- Cross-Servicing Bill Report: Lists bills referred to Cross-Servicing for a single Debtor. The report includes the Debtor’s Name, SSN, CS Referred Date, Current Amount Owed balance owed, Bill Number, Bill Status, the Original Amount of Debt initially referred to Cross-Servicing, Principal, Interest, Administrative Fees, and Court Fees.
- Cross-Servicing Recall Report: Lists recalled bills by Bill Number from the Recall Files. The report includes the Bill Number, Debtor’s Name, SSN, Amount Recalled, Recall Reason, and CS Recall Date.
- Debt Referral Reject Report: Lists rejected bills by Debtor Name from the Unprocessable Files. The report includes the Debtor’s Name, SSN, Bill \#, Record Type, Action Code, Error Code, Code Translation, and Reject Date. Only AR Supervisors and AR Clerks have access to this report. This report also has the feature of being able to export to MS-Excel by adding delimiters to the data displayed on the users screen.
- List IAI Error Codes: Listing of the IAI Error Codes in error code order. The display contains a) Error Code, b) Field Name, c) associated Record Types, and d) Description.
- Print Reconciliation Report: Lists bills that have been received in the Reconciliation IAI file from Treasury. The report includes the Debtor’s Name, Bill Number, Returned Date, and Closed Date. The report also includes the Return Reason description and any required supporting information.

## Transaction Profile Screen Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications are released under this patch to the Transaction Profile screen:

- New field added to capture the FUND data element. This field is populated with the extracted value from FUND (field 203) in the ACCOUNTS RECEIVABLE (#430) file.
- New field added to capture the Revenue Source Code (RSC) data element. This field is populated with the extracted value from RSC (field 255.1) in the ACCOUNTS RECEIVABLE (#430) file.

## Monthly Patient Statements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications to the monthly patient statements are released under this patch:

- The value of the bills referred to Cross-Servicing is excluded from the “Previous Balance” and “Balance” block on the monthly patient statement.
- When a bill is no longer referred to Cross-Servicing, the value of bills is included in the “Previous Balance” and “Balance” block on the monthly patient statement.

## Updated Due Process Notification Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC currently sends letters to debtors notifying them of potential referral to Treasury at the debtor level. With the implementation of Cross-Servicing, VistA will now supply AITC with debtor information at the bill level. The following Cross-Servicing Due Process Notification enhancements are released under this patch:

- Upon implementation of Cross-Servicing, a one-time-only process will generate a historical Initial Due Process Notification (DPN) file that identifies bills that comply with all of the Cross-Servicing rules, but are less than \$25.
- On a weekly basis, the Initial DPN File will be checked by VistA for any bills that had been identified previously as less than \$25 and have increased (due to fees and charges) to \$25 or more.
- VistA transmits the DPN File to AITC in an IAI-modified format containing the delinquent bill number, debtor’s name, address, and dollar amount of debt.
- After a 60 day waiting period the bill will be Cross-Serviced
- Note that this DPN File will only be required for approximately 12 months and will address debts that were established 12 months prior to the nationwide implementation of Cross-Servicing.
- The feature is configurable. DPN processing can be disabled, extended, and modified via the AR SITE PARAMETER (342,100) file

## Cross-Serviced Qualified / No Third Letter Sent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A bulletin is generated by VistA when there is eligible debt for Cross-Servicing and a third collection letter has not been sent.
- The bulletin contains the debtor’s name and bill number(s).

# Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the patch description that will be released through Forum following the national rollout of the Cross-Servicing patch (PRCA\*4.5\*301).

<span id="_Toc469998155" class="anchor"></span>Figure 2: PRCA\*4.5\*301 Patch Description

VistA Patch Display Page: 1

=============================================================================

Run Date: DEC 19, 2016 Designation: PRCA\*4.5\*301 v95

Package : ACCOUNTS RECEIVABLE Priority : MANDATORY

Version : 4.5 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)PRCA\*4.5\*229\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*249\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*263\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*265\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*270\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*296\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*298\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*303\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*304\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

(v)PRCA\*4.5\*309\<\<= must be installed BEFORE \`PRCA\*4.5\*301'

Subject: TREASURY CROSS-SERVICING PROGRAM

Category: ROUTINE

ENHANCEMENT

Description:

===========

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This patch supports changes to the Veterans Health Information

System and Technology Architecture (VistA) for the Treasury

Cross-Servicing Program (TCSP). PRCA\*4.5\*301 (Accounts Receivable-AR)

is being released in host file: PRCA_45_P301.KID.

It is imperative that these patches be installed no later than the

compliance date. Your understanding and support is appreciated.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The Chief Business Office (CBO) requested modifications to the VistA

Accounts Receivable Package to support the next phase in the implementation

of the Debt Collection Improvement Act (DCIA) of 1996 by the Department of

Veterans Affairs (VA).

This patch modifies the Account Receivable (AR) v4.5 application as

described below:

1\. TOP Modifications

\- Exclude first party bills from the TOP process unless the date the bill

became active is prior to the Activation Date. Do not exclude bills

from the TOP process that are identified as referred to TOP.

2\. DMC Referral Flag

\- The VistA system shall not modify the 90-day DMC debt referral process.

3\. Referral File

\- The VistA system shall automatically create a file of delinquent first

party bills.

\- The VistA system shall create the file in IAI format, containing record

types H, 1, 2, 2A, 2C, 3, Z.

\- The VistA system shall schedule the batch process to create the referral

file once per week for new referrals.

\- The VistA system shall have the ability to stop a bill from being

referred to Cross-Servicing.

4\. Update File

\- The VistA shall create a batch task to generate a file of updated

information for previously referred bills.

\- The VistA system shall create the file in IAI format, containing record

types H, 1, 2, 2A, Z.

\- The VistA system shall schedule the batch process to create the update

file once per week for new referrals.

\- The VistA system shall have the ability to stop a bill from being

updated to Cross-Servicing.

5\. Recall File

\- The VistA shall create a batch task to generate a file to recall

previously referred bills by debt, debtor, or case.

\- The VistA system shall create the file in IAI format, containing record

types H, 1, 2, 3, Z.

\- The VistA system shall schedule the batch process to create the recall

file once per week for new referrals.

\- The VistA system shall have the ability to stop a bill from being

recalled to Cross-Servicing.

6\. Reconciliation File

\- The VistA shall create a batch task to generate a file of updated

information for Reconciliation bills.

7\. Monthly Patient Statements - Bills Referred to Cross-Servicing

\- The VistA system shall exclude the value of bills that have been

referred to Cross-Servicing from the 'Previous Balance' and 'Balance'

block on the monthly patient statement.

8\. Monthly Patient Statements - Bills Not Referred to Cross-Servicing

\- The VistA system shall include the value of bills in the 'Previous

Balance' and 'Balance' block on the monthly patient statement when a

bill is no longer referred to Cross-Servicing.

9\. Unprocessable File - Bills that are sent for referral to Cross-

Servicing but are deemed not valid are rejected and returned to

VistA with the source of the error and the error code. The rejected

debts and error codes are stored historically and reported in debts

profile reports and reject reports.

10\. Due Process Notification (DPN) - A letter notification system for

debts expected to be sent to Cross-Servicing. From Cross-Servicing

initialization, debts under \$25.00 will be tracked for one year. As

the debts become qualified to Cross-Servicing referral, AITC will be

notified to send due process letters. After a sixty day waiting,

if the debts become qualified, the debts will be referred to Cross-

Servicing in the usual fashion.

11\. Cross-Servicing Qualified / No Third Letter Sent - A bulletin will

be generated by VistA when there is eligible debt for Cross-

Servicing and a third collection letter has not been sent. The

bulletin will contain the debtor's name and bill number(s).

12\. Activation Date - The VistA system shall not refer bills to

Cross-Servicing if they were not active prior to the Activation

Date. For Little Rock \#598, Beckley \#517, and Upstate NY \#528

the Activation Date has been set to February 1, 2015. For all

other sites, the Activation Date has been set to August 1, 2015.

Patch Components:

=================

Files & Fields Associated:

--------------------------

The following is a list of files included in this patch:

File Name (Number) Field Name (Number) New/Mod/Del

------------------ ------------------- -----------

AR DEBTOR (#340) TCSP RECALL FLAG field (#7.02) NEW

TCSP RECALL DATE field (#7.03) NEW

TCSP RECALL REASON field (#7.04) NEW

DATE DEBTOR REFERRED TO TCSP field(#7.05 NEW

AR DEBTOR (#342) CROSS-SERVICING START DATE field (#100) NEW

AR BATCH PAYMENT (#344)

RECEIPT PAY TYPE field (#.19) NEW

AR BATCH PAYMENT (#344) Subfile TRANSACTION (#344.01)

PATIENT NAME OR BILL NUMBER (#.09) MOD

LOCKBOX TRANSACTION CODE (#.15) NEW

TCS IAI ERROR CODES (#348.5)

ERROR CODE ID (#.01) NEW

FIELD NAME/ACTION (#1) NEW

RECORD TYPE (#2) NEW

ERROR MESSAGE (#3) NEW

TCS IAI ACTION CODES (#348.6)

ACTION CODE (#.01) NEW

ACTION DESCRIPTION (#1) NEW

RECORD TYPE (#2) NEW

TCS IAI RECORD TYPES (#348.7)

RECORD TYPE ID (#.01) NEW

RECORD TYPE DESCRIPTION (#1) NEW

DATA TYPE (#2) NEW

ACCOUNTS RECEIVABLE (#430)

DATE BILL REFERRED TO TCSP field (#151) NEW

TCSP RECALL FLAG field (#152) NEW

TCSP RECALL EFF. DATE field (#153) NEW

TCSP RECALL REASON field (#154) NEW

RECALL AMOUNT field (#155) NEW

STOP TCSP REFERRAL FLAG field (#157) NEW

STOP TCSP REFERRAL EFF. DATE field (#158) NEW

STOP TCSP REFERRAL REASON field (#159) NEW

STOP TCSP REFERRAL COMMENT field (#159.1) NEW

TCSP CASE RECALL FLAG field (#159.2) NEW

TCSP CASE RECALL EFF DATE (#159.3) NEW

TCSP CASE RECALL REASON (#159.4) NEW

TCSP GENDER (#159.5) NEW

ORIGINAL TCSP TIN field (#161) NEW

ORIGINAL TCSP DEBTOR NAME field (#162) NEW

TCSP DELINQUENCY DATE field (#163) NEW

TCSP DEBTOR ADDRESS, LINE 1 field (#164) NEW

TCSP DEBTOR ADDRESS, LINE 2 field (#165) NEW

TCSP DEBTOR ADDRESS, CITY field (#166) NEW

TCSP DEBTOR ADDRESS, STATE field (#167) NEW

TCSP DEBTOR ZIP CODE field (#168) NEW

ORIGINAL TCSP AMOUNT field (#169) NEW

CURRENT TCSP AMOUNT field (#169.1) NEW

TCSP DEBTOR PHONE (#169.2) NEW

TCSP COUNTRY CODE (#169.3) NEW

TCSP DOB (#169.4) NEW

DUE PROCESS NOTIFICATION FLAG (#173) NEW

DUE PROCESS REQUEST DATE (#174) NEW

DUE PROCESS LETTER PRINT DATE (#175) NEW

DUE PROCESS REFERRAL DATE (#176) NEW

DUE PROCESS ERROR DATE (#177) NEW

DUE PROCESS ERROR CODES (#178) NEW

SEND TCSP RECORD 1 field (#191) NEW

SEND TCSP RECORD 2 field (#192) NEW

SEND TCSP RECORD 2A field (#193) NEW

SEND TCSP RECORD 2C field (#194) NEW

STOP INTEREST ADMIN CALC (#199.2) NEW

RETURNED DATE (#301) NEW

RETURN REASON CODE (#302) NEW

COMPROMISED INDICATOR (#303) NEW

COMPROMISE AMOUNT (#304) NEW

CLOSED DATE (#305) NEW

BANKRUPTCY DATE (#306) NEW

DATE OF DEATH (#307) NEW

DATE OF DISSOLUTION (#308) NEW

ACCOUNTS RECEIVABLE (#430) Subfile CS DECREASE ADJ TRANS NUMBER

(#430.0171)

CS DECREASE ADJ TRANS NUMBER (#.01) NEW

SEND TCSP RECORD 5B NEW

ACCOUNTS RECEIVABLE (#430) Subfile REJECT DATE (#430.0172)

REJECT DATE (#.01) NEW

REJECT SOURCE (#1) NEW

REJECT REASON1 (#2) NEW

REJECT REASON2 (#3) NEW

REJECT REASON3 (#4) NEW

REJECT REASON4 (#5) NEW

REJECT REASON5 (#6) NEW

REJECT REASON6 (#7) NEW

REJECT REASON7 (#8) NEW

REJECT REASON8 (#9) NEW

REJECT REASON9 (#10) NEW

RECORD TYPE (#11) NEW

RECORD ACTION CODE (#12) NEW

REJECT BATCH ID (#13) NEW

REJECT MM MSG NO. (#14) NEW

AR RETURN REASON CODE (#430.5)

CODE (#.01) NEW

DESCRIPTION (#1) NEW

CATEGORY (#2) NEW

Forms Associated:

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

TCSP NEW

TPC NEW

TPL NEW

Options Associated:

Option Name Type New/Modified/Deleted

----------- ----------- ------------------------

PRCAF SUPERVISOR MENU MENU MODIFIED

RCTCSP BILL REPORT RUN ROUTINE NEW

RCTCSP IAI ERROR CODES LIST RUN ROUTINE NEW

RCTCSP MENU MENU NEW

RCTCSP RECALL REPORT RUN ROUTINE NEW

RCTCSP RECALLB RUN ROUTINE NEW

RCTCSP RECALLD RUN ROUTINE NEW

RCTCSP RECONCIL REPORT RUN ROUTINE NEW

RCTCSP REJ SERVER SERVER NEW

RCTCSP REJECT REPORT RUN ROUTINE NEW

RCTCSP REPORT RUN ROUTINE NEW

RCTCSP STOP RUN ROUTINE NEW

RCTCSPD SERVER SERVER NEW

RCTCSPR SERVER SERVER NEW

Protocols Associated:

---------------------

N/A

Security Keys Associated:

-------------------------

Security Key Name

-----------------

N/A

Templates Associated:

Template Name Type File Name (Number) New/Mod/Del

------------- ---- ------------------ -----------

PRCA MEANS PROFILE PRINT ACCOUNTS RECEIVABLE MOD

(#430)

PRCA OTHER PROFILE PRINT ACCOUNTS RECEIVABLE MOD

(#430)

PRCA PROFILE PRINT ACCOUNTS RECEIVABLE MOD

(#430)

PRCA TCSP RECALLB PRINT ACCOUNTS RECEIVABLE NEW

(#430)

PRCA TCSP RECALLD PRINT ACCOUNTS RECEIVABLE NEW

(#430)

TCS IAI ERROR CODES LIST PRINT TCS IAI ERROR CODES NEW

(#348.5)

Remote Procedure New/Mod/Del

---------------- -----------

N/A

Additional Information:

N/A

New Service Request (NSRs):

---------------------------

N/A

Patient Safety Issues (PSIs):

-----------------------------

N/A

Remedy Ticket(s) & Overview:

----------------------------

N/A

Test Sites:

-----------

VISN 16, Region 2, Central Arkansas Veterans Healthcare System, John L.

McClellan Memorial Veterans Hospital, Station \#598, Little Rock,

Arkansas

VISN 2, Region 4, VA Health Care Upstate New York, Station \#528.

VISN 6, Region 3, VA Mid-Atlantic Health Care Network, Beckley VA Medical

Center, Station \#517, Beckley, West Virginia.

VISN 6, Region 3, VA Mid-Atlantic Health Care Network, W. G. (Bill)

Hefner VA Medical Center, Station \#659, Salisbury, North Carolina.

VISN 23, Region 2, Nebraska-Western Iowa Health Care System, Omaha VA

Medical Center, Station \#636, Omaha, Nebraska.

Documentation Retrieval Instructions:

=====================================

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to retrieve files from REDACTED

This transmits the files from the first available server. Sites may

also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure

File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the

following OI Field Offices:

Albany: REDACTED

Hines: REDACTED

Salt Lake City: REDACTED

The documentation will be in the form of Adobe Acrobat files.

The following files should be downloaded in the binary SFTP mode.

Filename Description

-------- -----------

prca_4_5_p301_um.pdf Cross-Servicing User Manual

prca_4_5_p301_rn.pdf Cross-Servicing Release Notes / Installation Guide

prca_4_5_p301_tm.pdf Accounts Receivable Technical Manual

/ Security Guide

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

Patch Installation:

===================

Installation Instructions:

--------------------------

This patch may be run with users on the system, however because the

TOP options need to be placed out of order, we suggest it be

installed after business hours (5PM), but not when the Accounts

Receivable Background job is running (1AM). For large/integrated

sites the weekend is the most favorable time for installation.

This patch may take up to 8 hours to install.

The following options should be disabled during installation:

TOP Menu \[RCTOP MENU\]

1\. OBTAIN PATCHES

==============

Obtain the host file PRCA_45_P301.KID, which contains the following

one patch install:

PRCA\*4.5\*301

Sites can retrieve VistA software from the following SFTP addresses.

The preferred method is to SFTP the files from:

REDACTED

This will transmit the files from the first available SFTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The PRCA_45_P301.KID host file is located in the anonymous.software

directory. Use ASCII Mode when downloading the file.

2\. From the Installation menu, select the LOAD A DISTRIBUTION option.

When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file PRCA_45_P301.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]PRCA_45_P301.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

PRCA\*4.5\*301

Use INSTALL NAME: PRCA\*4.5\*301 to install this distribution.

3\. RUN OPTIONAL INSTALLATION OPTIONS FOR BUILD:

==================================================

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

PRCA\*4.5\*301):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. INSTALL BUILD:

====================

This is the step to start the installation of this KIDS build. This

will need to be run for PRCA\*4.5\*301 build.

a\. Choose the Install Package(s) option to start the install.

b\. When prompted for the "Select INSTALL NAME:", enter PRCA\*4.5\*301.

c\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion

of Install?" YES// enter YES.

d\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? NO//" enter NO.

e\. When prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? YES//" enter YES.

f\. When prompted "Enter options you wish to mark as 'Out Of

Order':" enter the following options:

TOP Menu \[RCTOP MENU\]

g\. When prompted "Enter protocols you wish to mark as 'Out Of

Order':" enter \<return\>.

h\. When prompted "Delay Install (Minutes): (0-60): 0//" enter an

appropriate number of minutes to delay the installation in

order to give users enough time to exit the disabled options

before the installation starts.

i\. When prompted "Device: Home//" respond with the correct device.

=================== POST-INSTALLATION INSTRUCTIONS ====================

The post-install routine for patch PRCA\*4.5\*301 will flag debts

currently under \$25 for the Due Process Notification functionality. In

addition, the Cross-Servicing installation date is filed into the

AR Site Parameter file \#342.

The user will see the following messages displayed in the installation

log:

\>\>\>Cross-Servicing Start Date set to (current date).

\>\>\>Begin the Due Process Initialization.

\>\>\>The Initialization may take up to 8 hours.

\>\>\>Due Process Initialization is complete.

The post install routine PRCA45301P may be deleted from the system if the

post-install process has completed.

========================================================================

Routine Information:

====================

The second line of each of these routines now looks like:

;;4.5;Accounts Receivable;\*\*\[Patch List\]\*\*;Mar 20, 1995;Build 144

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PRCAAPR1

Before: B43791904 After: B45827636 \*\*34,45,108,143,141,206,192,

218,276,275,284,303,301\*\*

Routine Name: PRCAATR

Before: B19181234 After: B22771269 \*\*36,104,172,138,233,276,303,301\*\*

Routine Name: PRCABJ

Before: B36508118 After: B39614762 \*\*11,34,101,114,155,153,141,

165,167,173,201,237,304,301\*\*

Routine Name: PRCADR

Before: B15191429 After: B17506368 \*\*21,45,108,141,241,301\*\*

Routine Name: PRCADR2

Before: B15662355 After: B16711783 \*\*45,104,108,149,141,172,241,

233,263,301\*\*

Routine Name: PRCAEXM

Before: B12096933 After: B13617982 \*\*67,103,196,301\*\*

Routine Name: PRCAGDR

Before: B10035785 After: B14896021 \*\*78,198,219,301\*\*

Routine Name: PRCAGS

Before: B16858191 After: B22454707 \*\*34,78,301\*\*

Routine Name: PRCAGST1

Before: B9197569 After: B9484383 \*\*2,48,104,176,249,301\*\*

Routine Name: PRCAGT

Before: B19865936 After: B22272453 \*\*100,162,165,169,219,301\*\*

Routine Name: PRCAGU

Before: B11613288 After: B12887006 \*\*181,219,301\*\*

Routine Name: PRCAPRO

Before: B14369527 After: B14760379 \*\*2,21,125,147,198,301\*\*

Routine Name: PRCAREP

Before: B12812144 After: B13936976 \*\*301\*\*

Routine Name: PRCASER1

Before: B15957526 After: B16741481 \*\*48,104,165,233,301\*\*

Routine Name: RC45301P

Before: n/a After: B1337108 \*\*301\*\*

Routine Name: RCBEADJ

Before: B66159160 After: B77125147 \*\*169,172,204,173,208,233,298,301\*\*

Routine Name: RCBECHGS

Before: B12081486 After: B14080962 \*\*153,237,301\*\*

Routine Name: RCBEIB

Before: B39033616 After: B41614858 \*\*157,270,301\*\*

Routine Name: RCBEPAY

Before: B27398421 After: B26246409 \*\*153,304,301\*\*

Routine Name: RCBEPAYF

Before: B25701767 After: B49084627 \*\*153,301\*\*

Routine Name: RCBEUTR1

Before: B35457473 After: B36268452 \*\*153,169,192,226,270,276,301\*\*

Routine Name: RCCPCPS

Before: B71404162 After: B80898915 \*\*34,70,80,48,104,116,149,170,

181,190,223,237,219,265,301\*\*

Routine Name: RCDPAPLI

Before: B43587980 After: B46722534 \*\*114,141,241,303,301\*\*

Routine Name: RCDPBPLI

Before: B47751255 After: B57251656 \*\*114,153,301\*\*

Routine Name: RCDPBPLM

Before: B57667335 After: B61916200 \*\*114,153,159,241,276,303,301\*\*

Routine Name: RCDPLPL3

Before: B52913516 After: B54165729 \*\*153,304,301\*\*

Routine Name: RCDPLPL4

Before:B236411644 After:B238259256 \*\*304,301\*\*

Routine Name: RCDPRPL3

Before: B81211213 After: B81971704 \*\*114,148,153,173,301\*\*

Routine Name: RCDPURED

Before: B41284430 After: B50615527 \*\*114,169,174,196,202,244,268,

271,304,301\*\*

Routine Name: RCDPURET

Before: B61262925 After: B75859214 \*\*114,141,169,173,196,221,304,301\*\*

Routine Name: RCDPXPAP

Before: B49106296 After: B54412655 \*\*114,150,206,296,301\*\*

Routine Name: RCDPXPAY

Before: B62956528 After: B65069620 \*\*114,148,150,301\*\*

Routine Name: RCTCSJR

Before: n/a After:B113325699 \*\*301\*\*

Routine Name: RCTCSJS

Before: n/a After:B200131768 \*\*301\*\*

Routine Name: RCTCSJS1

Before: n/a After: B57381357 \*\*301\*\*

Routine Name: RCTCSP1

Before: n/a After:B168147966 \*\*301\*\*

Routine Name: RCTCSP2

Before: n/a After: B87861761 \*\*301\*\*

Routine Name: RCTCSP3

Before: n/a After: B79802534 \*\*301\*\*

Routine Name: RCTCSP3S

Before: n/a After: B30705650 \*\*301\*\*

Routine Name: RCTCSPD

Before: n/a After:B168545559 \*\*301\*\*

Routine Name: RCTCSPRS

Before: n/a After: B53928265 \*\*301\*\*

Routine Name: RCTCSPU

Before: n/a After: B55616924 \*\*301\*\*

Routine Name: RCTOPD

Before: B63586774 After: B70123756 \*\*141,187,224,236,229,301\*\*

Routine Name: RCWROFF

Before: B34901459 After: B38468960 \*\*168,204,309,301\*\*

Routine Name: RCWROFF1

Before: B33354440 After: B35416905 \*\*168,204,233,301\*\*

Routine list of preceding patches: 229, 249, 263, 265, 296, 298, 303, 304

309

=============================================================================

User Information:

Entered By : BRICKER,DENNIS Date Entered : JAN 13,2014

Completed By: Date Completed:

Released By : Date Released :

=============================================================================

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be run with users on the system; however, because the Treasury Offset Program (TOP) options need to be placed out of order, it is suggested that this patch be installed after business hours, but NOT when the Accounts Receivable (AR) Background Job is running. For large/integrated sites the weekend is the most favorable time for installation.

This patch may take up to eight (8) hours to install.

The following option should be disabled before installation:

- TOP Menu \[RCTOP MENU\].

The following sub-sections outlines the steps for installing PRCA\*4.5\*301.

## Obtain Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps outline how to retrieve the host file:

1.  Obtain the host file PRCA_45_P301.KID, which contains the following one patch install: PRCA\*4.5\*301.
2.  Sites can retrieve VistA software from the following SFTP addresses. The preferred method is to SFTP the files from: REDACTED. This will transmit the files from the first available SFTP server.
3.  Sites may also elect to retrieve software directly from a specific server as follows:

> Albany REDACTED

> Hines REDACTED

> Salt Lake City REDACTED

4.  The PRCA_45_P301.KID host file is located in the anonymous.software directory. Use ASCII Mode when downloading the file.
5.  From the Installation menu, select the LOAD A DISTRIBUTION option.
6.  When prompted for “Enter a Host File:”, enter the full directory path where you saved the host file PRCA_45_P301.KID (e.g., SYS\$SYSDEVICE:\[ANONYMOUS\] PRCA_45_P301.KID).
7.  When prompted for “OK to continue with Load? NO//”, enter YES.
8.  The following will display: Loading Distribution...PRCA\*4.5\*301
9.  Use INSTALL NAME: PRCA\*4.5\*301 to install this distribution.

## Run Optional Installation Options for Multi-Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Installation menu, you may select to use the following options (when prompted for the INSTALL NAME, enter PRCA\*4.5\*301):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD’s or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (e.g., routines, DD’s, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

## Install Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below steps are to start the installation of the KIDS build. This will need to be run to install PRCA\*4.5\*301. Note that although it is a KIDS build, it does not entail installing more than one application.

1.  Choose the Install Package(s) option to start the install.
2.  When prompted for the “Select INSTALL NAME:”, enter PRCA\*4.5\*301.
3.  When prompted, “Want KIDS to INHIBIT LOGONs during the install? NO//”, enter NO.
4.  When prompted, “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//”, enter YES.
5.  When prompted, “Enter options you wish to mark as 'Out Of Order':”, enter the following option: TOP Menu \[RCTOP MENU\].
6.  When prompted, “Enter protocols you wish to mark as 'Out Of Order':”, enter \<return\>.
7.  When prompted, “Delay Install (Minutes): (0-60): 0//" enter an appropriate number of minutes to delay the installation in order to give users enough time to exit the disabled options before the installation starts.
8.  When prompted, “Device: Home//”, respond with the correct device.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install routine for Patch \# PRCA\*4.5\*301 will flag debts currently under \$25 for the Due Process Notification (DPN) functionality. In addition, the Cross-Servicing installation date is filed into the AR Site Parameter file \#342.

The user will see the following messages displayed in the installation log:

> \>\>\>Cross-Servicing Start Date set to (current date).

> \>\>\>Begin the Due Process Initialization.

> \>\>\>The Initialization may take up to 8 hours.

> \>\>\>Due Process Initialization is complete.

The post-install routine, “RC45301P” may be deleted from the system if the post-install process has completed.

# Backout / Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides step-by-step instructions for the back-out during / right after a failed installation of the patch, as well as how to roll back to a previous state after the release has been running in production for a period of time and has failed.

## Pre-Implementation Steps Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the backup steps in Section 4.2 were completed. These steps create a copy of the current patch (PRCA\*4.5\*301) in VistA MailMan. Verify that the information is sent to the following mail groups after every patch install: TSCP, TPC, and TPL. Backup the routines before the installation of the new patch.

> **NOTE:** Log a national ticket through CA SDM to restore the backed up routines in order to allow HPS assessment prior to following the rollback procedure.

## Software Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps document the procedures for rolling back to a previous patch version.

1.  Go to your Vista MailMan inbox and open the most recent version of the backup message. The Subject of the message will read “Backup of PRCA\*4.5\*30”.

<span id="_Toc469998156" class="anchor"></span>Figure 3: Sample MailMan Backup Message

![](prca-4-5-301-ar-release-notes/003.png)

2.  After you have opened the message, at the Enter message action (in IN basket): prompt, enter Xtract PackMan.
3.  At the Select PackMan function: prompt, enter 6 for INSTALL/CHECK MESSAGE.
4.  The following warning message will display:

> Warning: Installing this message will cause a permanent update of globals and routines.

> Do you really want to do this? NO//

5.  Enter Yes.
6.  The following message will display:

> Routines are the only parts that are backed up.  NO other parts

> are backed up, not even globals.  You may use the 'Summarize Message'

> option of PackMan to see what parts the message contains.

> Those parts that are not routines should be backed up separately

> if they need to be preserved.

> Shall I preserve the routines on disk in a separate back-up message? YES//

7.  Enter Yes.
8.  The following is an example display once the roll back is complete. Compare the functionality between the two builds to verify that the roll back was successful.

<span id="_Toc469998157" class="anchor"></span>Figure 4: PackMan Backup Message

![](prca-4-5-301-ar-release-notes/004.png)

## Database Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all database restores, local site staff will need to restore the data using the last nightly back up of the database. Please log a CA SDM ticket for assistance.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PRCA*4.5*347 AR Release Notes

## Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch provides four new DMC reports and an update to the PRCA RCDMC REFERRAL MENU.

### PRCA RCDMC REFERRAL MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRCA RCDMC REFERRAL MENU has four new report options:

1.  Option RCDMCR4 0-40 PERC SC CHNG RPT (0 to 40 Percent SC Change Reconciliation Report) added.
2.  Option RCDMCR5 1ST PARTY IB CANC RPT (First Party Charge IB Cancellation Recon Report) added.
3.  Option RCDMCR7 10-40% COPAY RPT (10-40% SC Med Care Copay Exempt Chrg Recon Report) added.
4.  Option \[RCDMCR6 50-100SC,PENSION,A&A\] (50-100% SC, A&A, Pension Exempt Chrg Recon Report) added.

### to 40 Percent SC Change Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will assist users in reviewing the legitimacy of first party bills for Veterans who received a new or updated change to a 0-40% Service Connected (SC) eligibility factor and received the change in VistA during the report time frame requested. This report prints information on bills/charges without an IB Status of “Cancelled” and with an A/R Status of Active, Suspended, Open, Write-Off, Collected/Closed, Cancellation, or with an IB Bill Status of On Hold, for episodes of care within a user selected time frame.

The report does not include bills for:

- debtors whose Service Connection is 50% or more
- debtors who are receiving a VA pension (regardless of their SC%)
- debtors receiving Aid and Attendance

The User is prompted to enter a beginning and ending date related to the rated disabilities/eligibility change, a beginning and ending date for a VistA last status update date range, and a beginning and ending date for an episodes of care date range. Veterans who meet the above criteria and whose rated disability eligibility has changed during the selected timeframe will be included in the report.

The report allows you to choose whether to print the report in a detailed format, a summary format, or in an Excel format.

It is recommended that you queue this report to a device that is 132 characters wide.

1.  The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.
2.  If there is no Rated Disability Original Effective Date, then “NODATE” will be displayed/printed for the RD Orig Date.
3.  Only one row will display/print for a particular rated disability if there is no RD ORIG DATE.

The report output includes Veteran’s name, SSN, combined service connected percentage, the VistA last status change date, the rated disability name, the extremity associated with the rated disability (if applicable), the original rated disability date, bill number, charge amount for the bill, medical care date, medication fill date, the prescription number, the prescription name, and the bill status.

### First Party Charge IB Cancellation Recon Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will assist users in reviewing first party charges receiving Integrated Billing (IB) cancellation for potential refund activities or charge cancellation accuracy, and to identify and monitor cancellation activity productivity so Veteran customers can receive refunds due to them for retroactive eligibility exemptions. The report provides data for first party charges receiving IB cancellation for a user defined bill cancellation date range.

The report provides the option to print only bills with payments or print all bills within the user specified bill cancellation date range. If only bills with payments are printed, the report will include bills with an IB Status of “Cancelled” that have charges AND a payment. If all bills are printed, the report will include bills with an IB Status of “Cancelled” regardless of presence of payments.

The report allows you the option to print the report in an Excel format.

It is recommended that you queue this report to a device that is 132 characters wide.

4.  This report does not include bills with third-party AR Category Types of “Reimbursable” or “Pre-payments”.

The report output includes Veteran name, SSN, bill number, charge amount, medical care date, medication fill date, prescription number, prescription name, IB cancellation date, IB cancellation reason, and cancelled by.

### 10-40% SC Med Care Copay Exempt Chrg Recon Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 10-40% SC Med Care Copay Exempt Chrg Recon Report is provided to assist users in reviewing all medical care copayment bills containing charges with a distinct date of service on or after the copayment exemption effective date for Veterans with SC Percent equal to 10 to 40% and does not show prescription copayment bills.

The report captures any medical care copayment charge without an IB status of cancelled, and with an AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, Cancellation, or an IB Status of On-Hold, with a date of service on or after the exemption effective date.

The User can select to run the report for a bill status of Active, Open, Suspended, Collected/Closed, On-Hold, Write-Off, or ALL. The ALL option includes the six noted statuses plus the AR status of Cancellation.

The report allows users to choose whether to print the report in a non-Excel Delimited format or an Excel Delimited format.

It is recommended that users queue this report to a device that is 132 characters wide.

5.  The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.
6.  If a Veteran has more than one bill, the report prints a row for every bill number (K#) they have that meets the report parameters.
7.  If a bill has a Status of “On-Hold”, the Bill number field will be blank.
8.  If the Veteran record tied to the bill does not have a Co-Payment Exemption Date, the report prints/displays “NODATE” in the EXMPTDT field.

The report output includes Veteran name, SSN, Service Connected percentage, bill number, co-pay exemption date, medical care date, and bill status.

### 50-100% SC Exempt Charge Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 50-100% SC Exempt Charge Reconciliation Report is provided to assist users in reviewing all bills containing charges with a distinct date of service on or after the co-payment exemption effective date for Veterans with Primary or Secondary Eligibility equal to 50 to 100% Service Connected.

The report captures any charges without an IB status of cancelled, and with an AR Status of Active, Open, Suspended, Write-Off, Collected/Closed, Cancellation, or an IB Status of On-Hold, with a date of service on or after the exemption effective date.

The User can select to run the report for a bill status of Active, Open, Suspended, Collected/Closed, On-Hold, Write-Off, or ALL. The ALL option includes the six noted statuses plus an AR status of Cancellation.

The report allows users to choose whether to print the report in a non-Excel Delimited format or an Excel Delimited format.

It is recommended that users queue this report to a device that is 132 characters wide.

9.  The Med Care Date column will contain either an Outpatient Visit Date OR an Inpatient Discharge Date. The same K \# (Bill \#) could show on the report with the same date for the event where there was an outpatient date and an inpatient discharge date for the same Veteran.
10. The Med Care Date will be blank if the charge is for a medication.
11. The RxFillDt will be blank if there is a Med Care Date.
12. The RX# and RX Name will be blank if the charge is for medical care.
13. If a Veteran has more than one bill, the report prints a row for every bill number (K#) they have that meets the report parameters.
14. If a bill has a Status of “On-Hold”, the Bill number field will be blank.
15. If the Veteran record tied to the bill does not have a Co-Payment Exemption Date, the report prints/displays “NODATE” in the EXMPTDT field and only prints one row of information if the Debtor has at least one bill matching the selected “Status” (e.g. Active, Open, Suspended, Collected/Closed, Write-Off, On-Hold).

The report output includes Veteran name, SSN, Service Connected percentage, bill number, co-pay exemption date, medical care date, Rx fill date, Rx number, Rx name, and bill status.

## Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No upgrade information applies.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None at this time.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents (located from the [VA Software Document Library](https://www.va.gov/vdl/)) apply to this release:

- Accounts Receivable 4.5 Technical Manual
- Debt Management Center (DMC) User Guide
- Deployment, Installation, Back-Out, and Rollback Guide (PRCA\*4.5\*347)

### From: PRCA*4.5*281 AR Release Notes

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Accounts Receivable (AR) package contained in patch PRCA\*4.5\*281.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after October 1, 2013 (current implementation date).

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM Diagnosis Codes                 | ICD-10-CM Diagnosis Codes                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Chapter 1 is alpha; character 2 is numeric;                                   |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS Procedure Codes                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3,800 codes (approximately)      | 87,000 codes (approximately)                                                                                                           |
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch PRCA\*4.5\*281 makes the following changes to the AR application:

- To support future maintenance, an Application Program Interface (API) replaces direct global reads.
- Updates to the IB/AR Data Extract to include retrieval of ICD-10 diagnosis and procedure codes.

> **NOTE:** The AR package does not have a Graphical User Interface (GUI) and therefore does not require Section 508 compliance.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR manuals are posted on the VistA Documentation Library (VDL) [AR](http://www.va.gov/vdl/application.asp?appid=29) page.

The following AR manuals are updated with changes for PRCA\*4.5\*281:

- AR Technical Manual/Security Guide
- AR User Manual – Title Page
- AR User Manual - Glossary

The following AR manuals do not contain changes relating to PRCA\*4.5\*281:

- Installation Guide
- AR User Manual - Accounts Receivable
- AR User Manual - Agent Cashier
- AR User Manual - Archive AR Records Menu
- AR User Manual - Billing Menu
- AR User Manual - Clerk's AR Menu
- AR User Manual - Clerk's AR Menu - Part 2
- AR User Manual - Introduction
- AR User Manual - Supervisor's AR Menu

The following manual does not exist for this package:

- Security Guide

> **NOTE:** Security information is contained within the *AR Technical Manual*.

## Data Extract Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*281 updates functionality for the VHA Chief Business Office (CBO) Data Extract, which is sent via a flat file to the Allocation Resource Center (ARC) in Boston to include retrieval of ICD-10 diagnosis and procedures. For more information, refer to the VistA IB/AR Data Extract Release Notes on the VDL [AR](http://www.va.gov/vdl/application.asp?appid=29) page.

## Third Party Joint Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR package uses the Integrated Billing (IB) option, *Third Party Joint Inquiry (TPJI)*, which is impacted by ICD-10. For specific information, please refer to the ICD-10 Software Remediation Project Release Notes for Integrated Billing, patch IB\*2\*461.

The following integration agreements exist between AR and IB:

- 4121
- 4045

## Regional Counsel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA AR package provides a Regional Counsel (RC) referral process, whereby billing data is electronically transmitted for review by legal counsel (Regional Counsel or Department of Justice).

Note 1: The RC/DOJ Action Menu is used for this purpose. The Refer to RC/DOJ and Review/Refer TP Bills to RC options are used to trigger the transmissions to the RC database.

Note 2: Additional details regarding these transmissions are documented in the ICD-10 AR SDD.

Note 3: The RC referral process currently includes the decimal in the ICD diagnosis and procedure codes, and supports a maximum length of 10 characters for the codes. The ICD-10 diagnosis and ICD-10 procedure short descriptions have been expanded in the ICD-10 code set to the maximum length of 60 characters. The Regional Counsel database is able to accommodate the 60 character ICD-10 short description without making any modifications to their database. Due to differences in code set versions for ICD-9 and ICD-10 the Regional Counsel (RC) referral process is being tested for ICD-10 impact to insure that the process works with the addition of code set version ICD-10.

The VistA AR Regional Counsel referral process shall support ICD-10 diagnoses and ICD-10 procedures for bills that have ICD-10 data associated with them.

- ICD-10 diagnosis codes (up to 8 characters, including the decimal after the 3rd character)
- ICD-10 diagnosis short descriptions (up to 60 characters)
- ICD-10 procedure codes (consisting of 7 characters, with no decimal)
- ICD-10 procedure short descriptions (up to 60 characters)

The VistA AR Regional Counsel referral process shall continue to support ICD-9 diagnoses and ICD-9 procedures for bills that have ICD-9 data associated with them.

- ICD-9 diagnosis codes (up to 5 characters, including the decimal after the 3rd character)
- ICD-9 diagnosis short descriptions (up to 24 characters)
- ICD-9 procedure codes (up to 5 characters, including the decimal after the 3rd character)
- ICD-9 procedure short descriptions (up to 24 characters

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following AR routine was modified to replace direct global reads and old APIs with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible.

| Routine Name | Function                         |
|--------------|----------------------------------|
| RCXVDC4      | AR Data Extraction Data Creation |

## Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing extract has been modified to accommodate for the ICD-10 Code Set.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Extract</th>
<th>Fields/Data Elements Being Extracted</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CBO Data Extract</td>
<td><p>Record 399.0304:</p>
<ul>
<li><p>PROCEDURE</p></li>
<li><p>ICD PROCEDURE CODE QUALIFIER</p></li>
<li><p>ASSOCIATED DIAGNOSIS (1) PRIMARY DIAGNOSIS</p></li>
<li><p>ICD ASSOCIATED DIAGNOSIS (1) CODE QUALIFIER</p></li>
</ul></td>
</tr>
</tbody>
</table>

### From: PRCA*4.5*379 AR Release Notes

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the Accounts Receivable (RC) application and applies to the changes made between this release and any previous release of this software.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRCA\*4.5\*379 patch implements the new CPAC High Risk Veteran Reconciliation Report \[PRCA HRFS RECONCILIATION RPT\] that allows VHA's CPAC users to view first party charges for patients with the High Risk for Suicide flag in order to improve efficiency and accountability in revenue operations.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications made by PRCA\*4.5\*379:

This patch implements the report that allows VHA's CPAC users to view first party charges for patients with the High Risk for Suicide flag in order to improve efficiency and accountability in revenue operations.

Additionally, this patch makes changes to the First Party VCR. When using the option PRCA FP VETERAN CHRG RPT to display the VCR, after selecting the other filter prompts, the prompt that asked to display LETTERS has been changed. The prompt now reads:

Do you want to see:

1.  Letter Dates
2.  Total Payments Received on Bill Number
3.  Neither

Enter Selection (1,2, or 3) 3//

The default selection is 3 for "Neither". If option 3 is selected, the report will not print the four (4) Letter Dates columns, Total Payments Received on Bill Number, nor any value they contain.

Also, the information used to populate the Medical Date of Service column has been updated. If the Veteran has an entry in the INTEGRATED BILLING ACTION File (#350) the value for the Medical Date of Service column will show the DATE BILLED FROM Field (#.14).

If the BILL/CLAIMS File (#399) is used, the Medical Date of Service column will display the STATEMENT COVERS FROM Field (#151).
