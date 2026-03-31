---
title: PFOP Version 3 User Manual for Patient Funds Supervisor
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: for Patient Funds Supervisor
app_code: PRPF
app_name: Integrated Patient Funds
section: FIN
app_status: active
pkg_ns: PRPF
patch_ver: 3
patch_id: PRPF*3
group_key: "PRPF:PRPF:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The PFOP system is a computerized program that manages the private finances of Department of Veterans Affairs patients. The material to be stored in this system is the same information you have probably recorded on VA Form 10-1083, the Patient Account Card. Once installed, the PFOP system will accep
audience: 
keywords: 
  - patient
  - your
  - funds
  - account
  - ipfpatient
  - transaction
  - table
  - contents
  - prompt
  - balance
page_count: 0
word_count: 14228
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/pfop_sup.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/pfop_sup.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=46"
---

![](pfop-version-3-user-manual-for-patient-funds-supervisor/001.png)

Patient Funds (INTEGRATED) SystemUser Manual  
FORPATIENT FUNDS SUPERVISORVersion 3.0February 1989(Revised August 2018)

Preface

The Integrated Patient Funds software automates the mini-banking system that VA provides for patients to manage their personal funds while hospitalized in a VA medical facility.

This manual has concrete information and illustrations that will help you to perform your basic duties. Within the pages of this document, you will find descriptions of most of your patient fund activities, from enrolling new patients to posting Patient Fund transactions and generating reports that are used to reconcile Fiscal accounts. Your user manual is divided into two parts. Part I introduces the PFOP system and explains how you can transfer currently established Patient Fund accounts from your manual system to the computerized system. Part II reviews all of the PFOP system menu options and presents examples of the typical PFOP tasks you will be called on to perform at your computer terminal. If you are using one of the Decentralized Hospital Computer Program (DHCP) computer terminals for the first time, you may want to read the User’s Guide to Computing, a manual that introduces you to terms and tasks encountered in most DHCP applications and helps you get acquainted with your terminal and keyboard.

Table of Contents

Revision History

Initiated on 12/22/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Description (Patch # if applic.)</td>
<td>Project Manager</td>
<td>Technical Writer</td>
</tr>
<tr class="even">
<td>08/20/18</td>
<td><p>Patch: XU*8*679</p>
<p>Added note to page <a href="#XU_80_679"><u>57</u></a> regarding Electronic Signature Block restrictions.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/06/06</td>
<td><p>Added note on Database Diagnostic Report. Corrected footer to say that this is a manual for ‘Supervisors.’</p>
<p>Patch: PRPF*3*22</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/22/04</td>
<td>Pdf file checked for accessibility to readers with disabilities.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/22/04</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# Functional Description


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Functional Description](#functional-description)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Using The System Menu](#using-the-system-menu)
  - [Enrolling A Patient In The System](#enrolling-a-patient-in-the-system)
    - [Step 1 - The Signature Code Edit option](#step-1-the-signature-code-edit-option)
    - [Step 2 - The Long Form Registration Option](#step-2-the-long-form-registration-option)
    - [Step 3 - The Post Balance Carried Forward from Manual System Option](#step-3-the-post-balance-carried-forward-from-manual-system-option)
  - [Posting A Patient Funds Transaction](#posting-a-patient-funds-transaction)
- [Menu Option Information](#menu-option-information)
  - [Using The Add/Edit Patient Account Option](#using-the-addedit-patient-account-option)
    - [Long Form Registration](#long-form-registration)
    - [Short Form Registration](#short-form-registration)
    - [Post Balance Carried Forward from Manual System](#post-balance-carried-forward-from-manual-system)
    - [Edit Selected Patient Data](#edit-selected-patient-data)
    - [Change Account Status (ACTIVE/INACTIVE)](#change-account-status-activeinactive)
    - [Address Edit](#address-edit)
    - [Guardian Edit](#guardian-edit)
  - [Using The Balance Check Option](#using-the-balance-check-option)
  - [Using The Post Patient Funds Transaction Option](#using-the-post-patient-funds-transaction-option)
  - [Using The Multiple Transaction Posting Option](#using-the-multiple-transaction-posting-option)
  - [Using The Tickler (Suspense) File Menu](#using-the-tickler-suspense-file-menu)
    - [Add/Edit Suspense Item](#addedit-suspense-item)
    - [Delete Individual Suspense Item](#delete-individual-suspense-item)
    - [Kill Complete Suspense Date for an Individual Patient](#kill-complete-suspense-date-for-an-individual-patient)
    - [Review Suspense items for Individual Patient](#review-suspense-items-for-individual-patient)
    - [Print Suspense Report](#print-suspense-report)
  - [Using The Card Display/Print Menu](#using-the-card-displayprint-menu)
    - [Selected Card(s) - Print](#selected-cards-print)
    - [All Cards - Print](#all-cards-print)
    - [Transaction Display](#transaction-display)
    - [Information Display](#information-display)
    - [Master Transaction Review](#master-transaction-review)
  - [Using The Output (Reports) Menu](#using-the-output-reports-menu)
    - [Activity (AUDIT) Listing](#activity-audit-listing)
    - [Dormant Account Listing](#dormant-account-listing)
    - [Indigent Patient Listing](#indigent-patient-listing)
    - [Overdue Restriction Search](#overdue-restriction-search)
    - [Patient Summary Report](#patient-summary-report)
    - [Search for Min/Max Restrictions](#search-for-minmax-restrictions)
    - [Out of Balance Report](#out-of-balance-report)
    - [Listing of Patients](#listing-of-patients)
    - [Balance In Accounts](#balance-in-accounts)
    - [Transaction Listing](#transaction-listing)
    - [Fiscal Reports](#fiscal-reports)
    - [Unassigned Station-ID List](#unassigned-station-id-list)
  - [Using The Signature Code Edit Option](#using-the-signature-code-edit-option)
  - [Using The Supervisor Menu](#using-the-supervisor-menu)
    - [Add/Edit Patient Funds Forms](#addedit-patient-funds-forms)
    - [Enter/Edit Remarks Codes](#enteredit-remarks-codes)
    - [Clear Account Lock](#clear-account-lock)
    - [Deferral Date Edit](#deferral-date-edit)
    - [Productivity Report](#productivity-report)
    - [Update Patient Status for ALL Accounts](#update-patient-status-for-all-accounts)
    - [Verify and Correct Balance](#verify-and-correct-balance)
    - [Negative Balance Report](#negative-balance-report)
    - [Database Diagnostic Report](#database-diagnostic-report)
- [Glossary](#glossary)
The PFOP system electronically manages money held for patients hospitalized at VA facilities. The system’s foundation is the Patient Funds account. Essentially, the Patient Funds account operates much like a checking account; however, the money in a Patient Funds account does not accrue interest and, in some cases, restrictions limit the amount of cash patients may withdraw in a given time period. While using the PFOP system, you will perform tasks that closely resemble the banking activities required to maintain checking accounts. In short, you will be called upon to perform the three basic PFOP system functions that follow.
Establish Patient Funds Account
A Patient Funds account can be opened for any individual listed in both the Patient file (# 2) and the Patient Funds file (# 470). Your facility’s Patient file stores the patient name, social security number, pertinent addresses used by the PFOP system, and any additional medical information about a patient. Your facility’s Patient Funds file stores data associated with the PFOP system (e.g., account balance, restrictions, etc.).
Post Transactions
You may electronically post deposits to Patient Funds accounts and post withdrawals from Patient Funds accounts. You will also have on-line access to the current balances of Patient Funds accounts and to transactions involving those accounts.
Reconcile Accounts and Reports
Several reports are provided that can be used to help reconcile accounts with Fiscal Service. When generating these reports, you are able to select any one of several formats designed to meet the needs of a variety of users.
Because Patient Funds accounts are maintained electronically, PFOP data security and proper data maintenance are serious concerns. To protect PFOP data, you must enter an electronic signature code when completing each transaction. The electronic signature is equivalent to a written signature and holds the same legal responsibilities. Like all other PFOP users, you are responsible for entering and changing your own electronic signature code and you have a menu option designed specifically for this purpose (please refer to the Using the Signature Code Edit Option section for more information).

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFOP system is a computerized program that manages the private finances of Department of Veterans Affairs patients. The material to be stored in this system is the same information you have probably recorded on VA Form 10-1083, the Patient Account Card. Once installed, the PFOP system will accept information that you enter into your computer terminal, eliminating the need to record information on the form.

Using a computerized system to manage Patient Funds offers several advantages. First, the program improves efficiency and productivity by reducing unnecessary effort. You no longer have to record the same categories of information over and over again with each new transaction for the same patient. Your program also provides rigorous fiscal and accountability controls that protect Patient Funds (these controls satisfy guidelines described in MP-4, Part I; and in M-1, Part I, Chapter 8).

On the pages that follow, you will find descriptions of options used to enroll patients in the system, process system transactions, and print reports that show system transactions. PFOP operates on the same system that manages your medical center’s Patient file, it also shares information stored in that file. Only after a patient is admitted to your hospital and is entered into the Patient file will you be able to enroll the individual in the PFOP system.

Since it’s part of the Decentralized Hospital Computer Program (DHCP), the PFOP System not only operates on the same computers that manage your medical center’s Patient file, it also shares information stored in that file. Only after a patient is registered -- in other words, admitted to your hospital and entered into the Patient file -- will you be able to enroll the individual in the PFOP System. Now, let’s take a look at all of your system options and discover the ways in which they help simplify Patient Funds management.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While your manual system is still operating, you should enter ALL of your patient accounts into the computer. To do this, enter each patient’s demographic information and current balance from your manual system. After you have entered the balance for each account, you have moved from a manual system to a computerized system and you are ready to process ALL future patient fund transactions electronically.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/002.png)

Roadmap to the PFOP Implementation Process  
Once you have completed the previous four tasks and you begin using the PFOP system, you may encounter two on-screen messages. If a power failure or line drop occurs while you are working on an account, your terminal screen may display the message “This file is being edited by (YOUR LAST NAME, YOUR FIRST NAME). When you see your name in such a message, get out of your current option. Using a special menu option, your supervisor will clear the account so that you can RESUME WORK on the account. You may also encounter the message “Patient is deceased.” Should this message appear on your display, please continue working on the account. If the Patient Funds procedure is deemed appropriate, the system will accept the information that you enter about the deceased patient.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*SPECIAL NOTE TO FACILITIES RUNNING AN EARLIER VERSION OF THE PFOP SYSTEM

This installation of the PFOP system requires a major conversion of the way in which information is stored in the computer. Version 3.0 CANNOT store patient transactions that already exist on your system. It CAN, however, retain patient demographic information that already exists on your system AND the current balance for each patient account. Before installing your new version, you should:

- Print Out ALL PATIENT ACCOUNT CARDS currently on your system (these printouts may come in handy later, should you need information about any of the transactions that your new version was unable to store).
- Talk to your system Manager about ways to prevent the loss of data during the installation process.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Using The System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFOP options represent basic tasks you will need to perform. Some of the options clearly identity your task-they will ask you to add an account, for example, or edit an account. Other options identify a subject matter area and then lead you towards a series of basic tasks that must be performed. In any case, you should view your options in the same manner you regard a list of items on a restaurant menu. Your options are selections that form a menu, and you are called upon to select any of the menu options that correspond to your duties as a Patient Funds Supervisor. Take a look at the PFOP system menu options that follow.

1 Add/Edit Patient Account  
2 Balance Check  
3 Post Patient Funds Transaction  
4 Multiple Transaction Posting  
5 Tickler (SUSPENSE) File Menu  
6 Card Display/Print Menu

7 Output (Reports) Menu

8 Signature Code Edit

9 Supervisor Menu

You will notice, the Add/Edit Patient Account option tells you exactly what task to perform and the Multiple Transaction Posting option identifies the type of material or subject matter area you will be handling; and the Supervisor Menu option states your job title. Once selected, your menu options lead you step-by-step through a series of tasks. As you proceed, the computer will ask you a series of questions or present a series of prompts, using clear, direct language. If you cannot understand a question or cannot figure out how to respond to a prompt, simply enter a question mark (?). Whenever you respond to a question or to a prompt by entering a question mark, the computer will present an explanation that you may need to prepare a response or will present a list of ALL possible responses. Now, let’s turn to the next section and examine the options you will use when setting up a new Patient Funds account on your computerized system and when processing Patient Funds transactions.

## Enrolling A Patient In The System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1 - The Signature Code Edit option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it eliminates the use of paper forms to process patient accounts, the PFOP system retains much of the information formerly recorded on the forms, including the initials of the individual who processes an account transaction. Under the old system, you had to record your initials on a VA form. Now you have a computer counterpart-an electronic signature code that you will enter when you post a transaction. This electronic code is your legal signature. It’s just as binding and just as effective as your handwritten signature on a piece of paper. Because it’s “encrypted” or scrambled, no one-not even a computer programmer-can duplicate your signature code. It’s yours alone. Furthermore, you alone are responsible for entering your new signature code into the computer or changing your code. Unless you tell someone your electronic signature code, this basic type of protection makes it impossible for someone to process a transaction in your name.

To begin, select the Electronic Signature Code Edit option under the User’s Toolbox (XUSERTOOLS) menu. At the INITIALS: prompt, enter the two to five characters that will represent your name. Then enter your name, your job title, and your office area code and telephone number at the three prompts that follow. Finally, at the ENTER NEW SIGNATURE CODE: and at the RE-ENTER SIGNATURE CODE FOR VERIFICATION: prompts, enter the 6 to 20 characters (no control or lowercase characters) that will serve as your PFOP system electronic signature.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/003.png)

Remember, your electronic signature is your legal signature. Entering your code on the computer is equivalent to signing your name on a VA Form.

### Step 2 - The Long Form Registration Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have established your electronic signature, it’s time to enter the demographic material for your new Patient Funds account. To begin, select the Add/Edit Patient Account menu option and study the following information that appears on your screen:

> 1 Long Form Registration  
> 2 Short Form Registration  
> 3 Post Balance Carried Forward from Manual System  
> 4 Edit Selected Patient Data  
> 5 Change Account Status (ACTIVE//NACTIVE)  
> 6 Address Edit  
> 7 Guardian Edit

What you see now are options for the Add/Edit Patient Account submenu. You will use these submenu options to perform a variety of enrollment tasks, most of which are explained later in this manual. All you want to do now, however, is use ONE of the options to begin the patient enrollment process. Select the Long Form Registration option, and your computer terminal will display the prompt Select PATIENT FUNDS NAME. On this prompt line, you will enter the name of the patient you wish to enroll in the PFOP System. If the program refuses to accept your entry, the patient MAY NOT be enrolled in your center’s Hospital Patient File OR you may have incorrectly entered the characters that make up the patient’s name. To find out if the patient is actually enrolled in the Hospital Patient file, enter a ? at the PATIENT FUNDS NAME prompt. Entering a question mark in this field allows you to see a list of the patients who are currently enrolled in the Personal Funds of Patients System AS WELL AS a list of the patients who are enrolled in your center’s Hospital Patient File.

After accepting your response to the PATIENT FUNDS NAME prompt, your terminal screen will display the prompt

STATION NAME: ANYCITY//

Enter a ?? for a list of station name entries. After making this entry, you will see the prompt

PATIENT TYPE: UNRESTRICTED//

At the PATIENT TYPE: prompt you may enter any one of four responses. To see a list of the four responses, enter a ? at the prompt. If you are processing an “unrestricted” account, simply accept the default answer at the PATIENT TYPE: prompt. If you enter R for “restricted” at the PATIENT TYPE: prompt, you must also enter the name of the patient’s physician as well as the month, day, and year the restriction took effect. Since a “restricted” account has fiduciaries -in other words, money held in trust - you will also have to enter the weekly and monthly dollar amounts the patient is allowed to withdraw from the account. After the PATIENT TYPE prompt: appears the

PATIENT STATUS: UNKNOWN//

prompt, the field in which you identify the patient’s competency level. Select the default answer if it’s the appropriate response. Or enter a ? in the PATIENT STATUS field and your screen will display a list of all the appropriate responses. Next, you will respond to the following prompt:

INDIGENT: NO //

Press the RETURN key to accept the default answer or enter Y for YES. (The criteria used to determine a patient’s indigent status are described in the Patient Assistance Program.) Here’s what your screen will display if you enter question marks at the PATIENT TYPE and PATIENT STATUS prompts.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/004.png)

After responding to the INDIGENT status prompt, you will arrive at a series of fields that require information about a patient’s personal funds. Information that you provide in this series helps the VA maintain accounts for patients rated “incompetent.” Here, you will identify the amounts and sources of gratuitous funds awarded to patients who, in the opinion of the VA or a civil court, are incapable of managing their own affairs because of mental or physical inadequacy. You will also identify the frequency of the payment awards. Using information that you enter, the PFOP system will compute the patient’s daily balance of funds.

In the first part of the series, you will see prompts with the titles APPORTIONEE \$; GUARDIAN \$ INSTITUTIONAL AWARD; REGIONAL OFFICE; and OTHER ASSETS. At the APPORTIONEE \$, GUARDIAN \$, INSTITUTIONAL AWARD, and OTHER ASSETS prompts, you will record the dollar amount for each funding type by entering numbers between 0 and 99999. If you type ? in response to the REGIONAL OFFICE: prompt, you are asked to enter either the appropriate institution (station) number or name. You will also be asked if you wish to see a list containing the names and numbers of 194 institutions.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/005.png)

Once you have completed your responses to the first part of the series about personal funds, you will come to the part that requires information about balance amounts AND about income sources income amounts, and frequency of income payments. You will need to respond to the MINIMUM and MAXIMUM balance prompts ONLY if you are processing (1) a “restricted” account; (2) the account of a patient who is eligible for the Patient Assistance Program; or (3) the account of a patient who is deemed “incompetent” and who has neither spouse nor children. If you query the INCOME SOURCE prompt, your screen will display the lines:

ANSWER WITH INCOME SOURCE

YOU MAY ENTER A NEW SOURCE, IF YOU WISH

Enter a person/type of income for this patient.

Do not exceed 25 characters.

Entering an income source will yield the PAYEE:, AMOUNT:, and FREQUENCY prompts. If you enter a ? in response to PAYEE:, you are asked to enter the name of the individual to whom the funds are distributed. In response to ? at the FREQUENCY: prompt, your program will present a list containing words such as “daily” and “monthly” and will ask you to enter the appropriate response.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/006.png)

After you complete your responses to the series of prompts about the patient’s personal funds, you will see the GENERAL INFORMATION/REMARKS prompt. If the VA form you are consulting has any basic comments about the patient, the patient’s guardians, and so on, please enter those remarks here. If you hold the PRPF CLERK security key, your screen will display the SPECIAL REMARKS prompt. In this field, please enter any confidential information contained in the VA form. And remember, the system will display special remarks only to PRPF CLERK security key holders.

Once you finish responding to the SPECIAL REMARKS field, you will have successfully enrolled a patient in the PFOP system. NOW you are ready for the third and final step in the enrollment process: entering your patient’s current balance into the system.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/007.png)

### Step 3 - The Post Balance Carried Forward from Manual System Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To complete the final step in the PFOP system enrollment procedure, you will need to select Post Balance Carried Forward from Manual System, an option under the Add/Edit Patient Account menu. But you should select this option only when you are converting from a manual to a computerized system. During the enrollment process, you are busy transferring information from a manual to a computerized system. Already, you have transferred the demographic data required to enroll the patient. Using the Post Balance option, you can now transfer the patient’s current balance.

To begin, find the manual system’s current balance for the patient you have just enrolled. Then, enter the manual system balance into the computer. At the next prompt, enter your electronic signature, a code that validates the transaction. Remember: you are the only one who knows your code and you are the only one who SHOULD know your code. It’s your legal signature and carries the same importance on computer documents as your written signature on checks and other papers and forms. Once you have entered the current balance and your signature code into the PFOP system, the enrollment procedure ends. You have completed the task of setting up a Patient Funds account. From this point on, you will use the computer to process all transactions involving the Patient Funds account you have just established. (Save your manual records for historical purposes only.)

![](pfop-version-3-user-manual-for-patient-funds-supervisor/008.png)

## Posting A Patient Funds Transaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have converted from a manual to a computerized program, the system menu option that you will use most often is Post Patient Funds Transaction. When you select this option, you are able to process a single deposit or a single withdrawal drawn on a patient’s account. Before you process the transaction, however, you will see the patient’s current balance. And, if you are handling a transaction for a patient classified as “restricted” or “limited unrestricted”, you will see the monthly or weekly amounts authorized for withdrawal from the patient’s account.

When using the Post Patient Funds Transaction option, you will identify the transaction type, entering a D for deposit or W for withdrawal. After selecting “withdrawal” and responding to the AMOUNT prompt, you may encounter the statement.

> Because of a deferred item in this account, the available balance

> is insufficient to fund this withdrawal. (OPTION TERMINATED)

Unless you hold a SECURITY KEY, you cannot process a withdrawal that exceeds the amount available in the account. If you are “kicked out”, enter the same Patient Funds name again and look at the amounts under TOTAL BALANCE, DEFERRED, and AVAILABLE FOR WITHDRAWAL. No doubt, the AVAILABLE FOR WITHDRAWAL amount is lower than the TOTAL BALANCE amount. Here’s why. Let’s say, for example, you deposited a \$50 check. Then, at the DEFERRAL DATE: prompt, you entered the ACTUAL day, month, and year on which the deferral period would end in the future (or you may have entered T+15 for “today” and the total number of days in the deferral period). After recording the transaction as a “deferred item”, your PFOP system added \$50 to the TOTAL BALANCE. But the AVAILABLE FOR WITHDRAWAL amount is \$50 LESS than the TOTAL BALANCE amount. What has happened is this: your system is now holding the \$50 in reserve for 15 days. Within that 15-day deferral period, the check for \$50 will probably “clear”. Once the deferral period ends, your system will no longer refer to this transaction as a “deferred item” and will add the \$50 to the AVAILABLE FOR WITHDRAWAL amount.

If you are a security key holder, your system eliminates the phrase (OPTION TERMINATED), replacing it with a statement that stresses the following: (1) you have the authority to post a transaction that exceeds the amount available for withdrawal; and (2) after you have posted the transaction, you are held accountable should the deferred item fail to clear.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/009.png)

When responding to the REFERENCE: prompt, you can enter numbers or alphanumeric codes based on the following categories and combinations:

> field service receipt numbers

> schedule numbers with form number prefixes

> control numbers with form number prefixes

> ACP and number

> voucher schedule with VS as prefix

> purchase order number with PO as prefix

> reference number used to record document

After you have entered the date of the transaction, you will then be asked to identify the form of the currency - is it a check, for example, or cash? If you are processing a check, you will encounter two additional prompts either immediately or later in the sequence. With a deposit, you will see:

DEFERRAL DATE:

Again, here you will enter the ACTUAL day, month, and year on which the deferral period will end in the future (or you will enter “T” for “today”, a plus sign, and the total number of days in the deferral period). If you are processing a withdrawal from a “restricted” account or “limited unrestricted” account, you will see the statement:

COUNT IN RESTRICTION BALANCE: YES//

Accept the default response and the system will subtract the transaction amount from the account’s monthly or weekly restriction amount.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/010.png)

![](pfop-version-3-user-manual-for-patient-funds-supervisor/011.png)

If you need help in responding to the FORM: prompt, enter a ? and you will get a list of all the appropriate responses. When you reach the REMARKS: field, you may enter a code OR comments OR both. In this field’s help prompt, you will see the following codes and code-ASSOCIATED terms:

|                                  |                      |
|----------------------------------|----------------------|
| ADJ adjustment to previous entry | SD specific donation |
| CC cancellation                  | NBC non bed care     |
| CA cash withdrawal, general use  | VAP VA pension       |
| CB coupon books                  | VAC VA compensation  |
| CL clothing                      | SS Social Security   |
| I incidentals                    | GE general use       |
| SE special expenditures          |                      |

To enter text as well as a code, type the ENTIRE character-combination, a comma, and then your comment. You can enter a maximum of 50 characters. But when you enter both code and text, the system counts the characters in the code-ASSOCIATED term and THEN counts the characters in your comment. If, for example, you type:

CL,Needed robe,slippers,shorts,T-shirt,pants

your REMARKS field entry will amount to 50 characters, even though you have typed only 44. What happens is this: instead of counting your CL code as two characters, the system counts each letter in “clothing” - the code-ASSOCIATED term. And since the word clothing has eight characters and the comma that follows represents a ninth, you have already used 9 of the allowable 50 characters. Now, stop for a minute and count each letter and space of the comment below.

Needed robe,slippers,shorts,T-shirt,pants

After adding the characters, commas, and the sole space in the above entry, you should have reached a total of 41. Now, add the 9 characters in your code-ASSOCIATED term plus comma to the 41 characters in your comment and you have reached the maximum of 50 characters. If your entry totals more than 50 characters, the system will display the message “Total Number of Characters may not exceed 50.” and you will have to revise and reenter your text. Here’s what your code, comma, and comment should look like on your display.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/012.png)

After you have responded to the REMARKS: field, you will encounter the prompts “Is it OK to Post this data to the Permanent Files? YES// and “Enter Electronic Signature Code.” Once the system accepts your code, the screen will display the updated patient account and you can check the accuracy of the material you entered.

# Menu Option Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using The Add/Edit Patient Account Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit Patient Account submenu has seven options. You used two of them in Section 4 of this manual, while completing the patient enrollment process. In this section, you will briefly review the two options you encountered earlier and learn about the remaining submenu options. Let’s begin by taking another look at your Add/Edit submenu.

1 Long Form Registration

2 Short Form Registration

3 Post Balance Carried Forward from Manual System

4 Edit Selected Patient Data

5 Change Account Status (ACTIVE/INACTIVE)

6 Address Edit

7 Guardian Edit

Of the seven submenu options, two allow you to set up a new patient account while the rest help you to change an existing account’s demographic information. In short, your Add/Edit options help you establish and revise records for patient accounts.

### Long Form Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When registering a patient in the system, you will generally use the Long Form Registration option. After selecting this option, you are able to enter information about a patient’s assets, income sources from guardians and institutions, amount and frequency of payments, and other categories. For a step-by-step review of the tasks you will perform when using this option, see the “Enrolling a Patient in the System” section of this manual.

### Short Form Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have very little information about a patient, you can enroll the individual on a temporary basis. To do this, select Short Form Registration and then simply enter the patient’s name and category “type”, account status classification, and any remarks that exist on your forms. If you enter U for “unrestricted” or X for “unknown”, your screen will display the prompt GENERAL INFORMATION/REMARKS. Then the temporary enrollment procedure will come to an end. If you are setting up a new account for a VA patient who is classified as “limited unrestricted” or “restricted”, you will encounter several additional prompts before you reach the field for REMARKS. First, you will see:

DATE OF CURRENT

RESTRICTION:

Entering a question mark at this prompt yields format guidelines for the date.

Let’s say, for example, the patient’s restriction was established on March 20, 1987. If that is the case, your terminal will accept any one of the following valid formats for the date that you enter:

MAR 20 1987 3/20/87  
20 MAR 87 032087

In addition, your terminal will accept T for TODAY; T+1 or T+2, etc., for TOMORROW and THE DAY AFTER TOMORROW; T-1 for YESTERDAY, etc.; and T-3W for 3 WEEKS AGO, and so on. You will also be asked to enter the name of the physician who authorized the restriction and the dollar amounts restricted weekly and monthly.

Finally, the screen will display the “Remarks” prompts. If you have no comments to enter, simply press the RETURN key twice and you will complete the temporary enrollment process for the patient. But one final note: Soon after setting up a temporary account, you should transfer it to permanent status, using the Long Form Registration option.

Select PATIENT FUNDS NAME: IPFPATIENT, ONE ANYCITY, FL 6-16-40 000456789 NO NON-VETERAN (OTHER)

NO ENROLLMENT APPLICATION ON FILE

STATION NAME: ANYCITY, FL//

ACCOUNT STATUS: ACTIVE//

PATIENT TYPE: ?

Choose from:

L LIMITED UNRESTRICTED

R RESTRICTED

U UNRESTRICTED

X UNKNOWN

PATIENT TYPE:

GENERAL INFORMATION/REMARKS:

1\>

SPECIAL REMARKS:

1\>

### Post Balance Carried Forward from Manual System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you transfer demographic information from your Patient Account Cards to your computer terminal, you have to use the Add/Edit Patient Account option. When it’s time to transfer the patient account current balance, you will use the Post Balance Carried Forward from Manual System option. For a description of the steps involved in transferring an account balance from a Patient Account card to your new computerized system, see Step 3 of the “Enrolling a Patient in the System” section of this manual.

### Edit Selected Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because your information base is electronically preserved, updating patient information is a fairly simple task. Whenever you need to revise the default entries for such categories as PATIENT TYPE, INDIGENT, OTHER ASSETS, GENERAL INFORMATION, or SPECIAL REMARKS, use your Edit Selected Patient Data option. If, on the other hand, the default response is accurate, simply press the RETURN key.

### Change Account Status (ACTIVE/INACTIVE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to change a patient’s account status from active to inactive or inactive to active. However, an account’s balance of funds must be equal to zero before you can change the account status to inactive. You can also edit a patient’s station through this option.

Select Add/Edit Patient Account Option: Change Account Status (ACTIVE/INACTIVE)

Select PATIENT FUNDS NAME: IPFPATIENT, ONE ANYSITE, DE 6-16-40 000456789 NO NON-VETERAN (OTHER)

NO ENROLLMENT APPLICATION ON FILE

ACCOUNT STATUS: ACTIVE//

STATION NAME: ANYSITE, DE// ANYCITY, FL 999

Select PATIENT FUNDS NAME:

### Address Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you receive updated information about a patient’s place of residence or other related material, use the Address Edit option to enter the changes. Your computer will accept changes in three residential address fields and in fields for the name of the city in which the patient resides, the zip code and state, and the telephone numbers for residence and work site. After you enter a change, you will proceed to the next field. Continue pressing “Enter” until you reach the field(s) you wish to edit, and continue adding updated information in each appropriate field. When all fields have been displayed for editing, you are returned to the Select PATIENT FUNDS NAME: prompt.

If you wish to review the edited information, enter the name of the same patient once again and check the new defaults. If you do not wish to review the updated material, simply enter the name of another patient whose address you wish to edit, or press RETURN or an UP-ARROW (^) and RETURN to exit the option.

### Guardian Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your medical center’s Hospital Patient File stores all of the information about the guardians for a Patient Funds account. Should any of this information need to be revised, you will select Guardian Edit, an option that has access to the Hospital Patient File. After selecting this option, you will provide updated information about “civil” or VA guardians, entering the current addresses and phone numbers of established guardians as well as the names, addresses, and phone numbers of newly designated guardians.

## Using The Balance Check Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to review an account’s total balance, the amount available for withdrawal, total amount for deferred items, and other financial information. Also included is data entered under GENERAL REMARKS and, if you hold the PRPF CLERK security key, any SPECIAL REMARKS. Information may not be edited through this option.

Select Patient Funds (INTEGRATED) System Option: 2 Balance Check

Select PATIENT FUNDS NAME: IPFPATIENT, ONE ANYCITY, FL 6-16-40 000456789 NO NON-VETERAN (OTHER)

NO ENROLLMENT APPLICATION ON FILE

IPFPATIENT, ONE SSN: 000-45-6789 CLAIM \#: 00000000

\* \* \* ACCOUNT TYPE IS RESTRICTED \* \* \*

WARD:

STATION NAME: ANYCITY, FL

AUTH WD/MONTH: \$20.00 AUTH WD/WEEK: \$5.00

ACTUAL: \$0.00 ACTUAL: \$0.00

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

TOTAL BALANCE: (\$20.00) PRIVATE SOURCE: \$0.00

DEFERRED: \$0.00 GRATUITOUS: (\$20.00)

AVAILABLE FOR WITHDRAWAL: (\$20.00)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

GENERAL REMARKS/INFORMATION:

SPECIAL REMARKS:

The information contained in this report is protected by the Privacy Act of 1974

## Using The Post Patient Funds Transaction Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to post a single deposit or a single withdrawal to a Patient Funds account. (The Multiple Transaction Posting option is used to enter multiple transactions). Please see the Posting a Patient Funds Transaction section of this manual for more detailed information about the procedures used to enter a single Patient Funds transaction.

Select Patient Funds (INTEGRATED) System Option: 3 Post Patient Funds Transaction

Select PATIENT FUNDS NAME: IPFPATIENT, TWO ANYCITY, IL 3-22-50 000456789 YES SC VETERAN

NO ENROLLMENT APPLICATION ON FILE Claim \#: 000000000

IPFPATIENT, TWO SSN: 000-45-6789 CLAIM \#: 000000000

\* \* \* ACCOUNT TYPE IS RESTRICTED \* \* \*

WARD:

STATION NAME: ANYCITY, IL

AUTH WD/MONTH: \$40.00 AUTH WD/WEEK: \$10.00

ACTUAL: \$0.00 ACTUAL: \$0.00

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

TOTAL BALANCE: \$180.00 PRIVATE SOURCE: \$0.00

DEFERRED: \$0.00 GRATUITOUS: \$180.00

AVAILABLE FOR WITHDRAWAL: \$180.00

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

GENERAL REMARKS/INFORMATION:

SPECIAL REMARKS:

The information contained in this report is protected by the Privacy Act of 1974

Do you wish to continue with this transaction? YES// (YES)

DEPOSIT/WITHDRAWAL: w WITHDRAWAL

AMOUNT: 10 \$ 10.00

REFERENCE: wkly allot

TRANSACTION DATE: TODAY// (JUN 14, 2002)

CASH/CHECK/OTHER: CASH// CASH

FORM: 10-1126// WITHDRAWAL OF PERSONAL FUNDS

SOURCE: GRATUITOUS// GRATUITOUS

REMARKS:

COUNT IN RESTRICTION BALANCE: YES// YES

Is it OK to Post this data to the Permanent Files? YES// (YES)

You have no signature code on file. Please contact your IRM staff for assistanc

e\.

## Using The Multiple Transaction Posting Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are processing single transactions for different accounts, you will often find yourself repeatedly entering the same preliminary information. To save time and avoid duplicated effort, your PFOP System allows you to process a series of transactions at one sitting, using the Multiple Transaction Posting option. Before you can use this option, however, you have to make sure all of the grouped transactions share certain basic attributes.

First of all, you must work with either a GROUP OF DEPOSITS or a GROUP OF WITHDRAWALS. In addition, each transaction in your group must allow you to make the same responses to a series of preliminary prompts that precede the prompt for the deposit or withdrawal AMOUNT. These preliminary prompts require such information as transaction date, form, and source; type of transaction (D for deposit and W for withdrawal); and type of currency (cash, check, or “other”). If you select the word “withdrawal” during this preliminary stage, your screen will later display the COUNT IN RESTRICTION BALANCE: NO// prompt. It you enter the word “check” during this preliminary stage, your screen will later display the DEFERRAL DATE: prompt. After responding to the REMARKS prompt, you are ready to review the information you entered at the preliminary prompts.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/013.png)

Since your responses to the series of preliminary prompts will represent all of your patient transactions until you exit from the option, the system gives you a chance to review all of your entries. Immediately after you have responded to the REMARKS: prompt, your screen will display all of the information you entered during the series of preliminary prompts. Only after you have seen your responses to the preliminary prompts does the system ask:

> OK to continue? YES//

Once you elect to continue, the second stage begins. Basically, the second stage prompts require two responses for each transaction in the group: the account name and the amount. All of the transactions in your series can be posted to a single account or to several accounts. If you have a series of deposits or withdrawals to be posted to ONE account, simply enter the name of the same individual at each Select PATIENT FUNDS NAME prompt. If, on the other hand, you have a series of deposits or withdrawals to be posted to SEVERAL accounts, you will enter the name of a new individual at each Select PATIENT FUNDS NAME prompt.

When you are entering withdrawals, your screen will display important financial information about an account before presenting the AMOUNT prompt. You will see, among other details, the account’s TOTAL BALANCE, any DEFERRED amount, and the amount AVAILABLE for withdrawal. Should you enter a withdrawal amount that exceeds the weekly amount available for withdrawal in a RESTRICTED account, you will see the message:

> WARNING, Posting this amount will exceed the WEEKLY withdrawal limitaion.

> Is it OK to exceed the WEEKLY limitation? NO//

A similar message appears when you enter an amount that exceeds the monthly restriction amount. Yet another message appears IF you enter an amount that is greater then the total balance available in ANY TYPE OF ACCOUNT and IF you hold the appropriate security key: under these circumstances you will encounter the message:

> The balance of \$845.00 is not sufficient to complete this transaction. Processing of this transaction will cause this patient’s account to be overdrawn. You will be assuming PERSONAL responsibility for this action.

> DO YOU WISH TO OVERDRAW THIS ACCOUNT? NO//

After a second statement inquires if you are SURE you wish to overdraw the account, you will see the prompt COUNT IN RESTRICTION BALANCE: NO// and, finally, the prompt “Is it OK to post this data to the permanent files? YES//”.

## Using The Tickler (Suspense) File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you receive Patient Funds account information about issues that must be deferred for action or review, you will place them in what is commonly called a “tickler” or suspense file. There, you will collect such items as a reminder to make sure a patient’s monthly check has cleared the bank before allowing the patient to withdraw the check’s cash amount; a reminder to pay a patient’s monthly rent and utilities; and any other patient account issues to be resolved at some point in the future. To begin, select the Tickler (Suspense) File Menu option.

> 1 Add/Edit Suspense Item

> 2 Delete Individual Suspense Item

> 3 Kill Complete Suspense Date for Individual Patient

> 4 Review Suspense Items for Individual Patient

> 5 Print Suspense Report

The Tickler menu options will allow you to perform several tasks. Using these options, you can enter and revise suspense items for one Patient Funds account or several. You can cancel a single SUSPENSE ITEM. Or you can cancel a SUSPENSE DATE, eliminating all items entered on the same day in the same account. You can read or print all of the items for a single account. And you can read or print a list of the items for all Tickler file accounts.

### Add/Edit Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are ready to enter an item into a patient account, select the Add/Edit Suspense Item option. The prompts that appear on your screen will ask for the name of the Patient Funds account, the date of the suspense item, a few words that can serve as an identifier for the item, and a description of the item. When responding to the Select ITEM ID: prompt, please enter a short description that identifies the suspense item, using no more than 40 characters. When responding to the FULL DESCRIPTION prompt, fully explain the situation that requires your attention or action. Should you require help in entering information in this word processing field, review the word processing section of the Users Guide to Computing.

In the screens that follow, you will see responses to all of the basic prompts that appear when you enter a new suspense item in a Patient Funds account and you will see what your entries will look like when you return to review or edit the same suspense item.

### Delete Individual Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever you need to delete a suspense item from a patient account, simply select the Delete Individual Suspense Item option. Using this menu option, you can remove ONE suspense item listed under a suspense date. But remember: your suspense date may have MORE THAN ONE suspense item. If you want to make sure that you are selecting the correct suspense date AND the correct suspense item listed under that date, enter a ? at the Select PATIENT FUNDS NAME prompt and at the Select ID: prompt.

When you have deleted your single suspense item from a patient account, your screen will again display the Select PATIENT FUNDS NAME prompt, allowing you to enter a new name.

### Kill Complete Suspense Date for an Individual Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes, you will find several suspense items listed under one suspense date. If you need to delete all of the suspense items listed under one suspense date, you can do so by simply deleting the suspense date, as opposed to deleting each individual item. When such a need arises, select the option entitled Kill Complete Suspense Date for an Individual Patient.

Once you have deleted a suspense date for a patient account, your screen will again display the Select PATIENT FUNDS NAME prompt, allowing you to enter a new name.

### Review Suspense items for Individual Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To see all of the suspense items in a single patient account or a selected group of items within an account, select the option entitled Review Suspense items for Individual Patient. If you want to see a PORTION of the list, simply respond to prompts requiring a range of dates. But let’s say that you want to view ALL of the suspense items in an account. To see or to print everything, accept the default response when the prompt START WITH SUSPENSE DATE: FIRST// appears. When the DEVICE: prompt appears next, you will have two choices. If VIEWING the suspense items on the screen is your objective, press the RETURN key at the DEVICE: prompt and again at the RIGHT MARGIN: 80// prompt. If PRINTING is your objective, enter your printer name or number at the DEVICE: prompt and then press the RETURN key at the RIGHT MARGIN: 98// prompt.

If you want to see or print a PORTION of all the items in the account, enter a date at the FIRST prompt and a date at the LAST prompt.

To see the items on your screen, enter a return at the DEVICE: prompt and at the RIGHT MARGIN: 80// prompt.

### Print Suspense Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you want to produce a document that lists ALL of the suspense items for ALL your patient accounts, use the Print Suspense Report option. To print everything in your file, press the RETURN key at the START WITH SUSPENSE DATE: FIRST// prompt. To print items for a certain period, simply enter a beginning date at the START WITH SUSPENSE DATE: FIRST// prompt and an ending date at the GO TO SUSPENSE DATE: LAST// prompt. Next, enter the name or number of your printer at the DEVICE: prompt and then press RETURN at the RIGHT MARGIN: 98// prompt.

The Print option also allows you to VIEW your report on the screen. If you simply want to take a look at the patient account suspense items, press the RETURN key at the DEVICE: prompt and again at the RIGHT MARGIN: 80// prompt.

## Using The Card Display/Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within your Card Display/Print Menu, you will find options that allow you to perform many display and print functions. Using the menu sub options, you can print or display Patient Account Cards and transactions; you can display demographic information; and you can display master transaction material.

> 1 Selected Card(s) - Print  
> 2 All Cards - Print  
> 3 Transaction Display  
> 4 Information Display  
> 5 Master Transaction Review

### Selected Card(s) - Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use your Selected Card(s) - Print option to produce Patient Funds Cards. To print a card for ONE account, enter the patient’s name at the Select PATIENT NAME: prompt and press RETURN at the Select Next PATIENT NAME: prompt. To print cards for SEVERAL accounts, enter a different name at each successive name prompt until you reach the end of your list. Should you elect to DISPLAY instead of PRINT your list, the computer retains the information and -when you select the option again later - will ask if you wish to delete the earlier list. Finally, before printing, make sure you enter the name or number of a device that has a line length of at least 132 characters and a page length of at least 62 lines. Your Application Coordinator or Site Manager should have a list of the printers that meet these specifications.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/014.png)

Once you have printed out the Patient Account Card or cards, you will have a report that lists the amount of each deposit or withdrawal attributed to an account; the date on which each transaction took place; income sources; and the account’s ending balance. Your report will also include the patient’s demographic profile, ward location, type of patient account, patient status, and remarks, if any (the system allows up to 50 characters in the remarks column but prints only the first 34 - along with an asterisk; if you need to display the entire comment, return to your Post Patient Funds Transaction option).

### All Cards - Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select the option All Cards-Print, you are allowed to print a Patient Funds Card for ALL patient accounts. However, your program recognizes two distinct groups within the ALL category. What you will encounter, in fact, after selecting this option is the message:

> This option will print a card for each ACTIVE patient

> in the file or for ALL patients regardless of status.

After asking if you wish to run the ALL Cards - Print option, you are asked:

> Do you wish to print only the ACTIVE cards? YES//

If you select ALL cards, you will see the statement “I will now print a card for ALL cards”. If you select ALL ACTIVE cards, you will see the statement “I will now print a card for ALL ACTIVE cards”. When you are ready to print, accept the default response at the OK TO CONTINUE? YES// prompt and then enter the name or number of a device that has a line length of at least 132 characters and a page length of at least 62 lines. Be sure to contact your Application Coordinator or Site Manager if you need a list of the printers that meet these specifications.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/015.png)

### Transaction Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can display or print all of the transactions processed within a specific range of dates for an individual patient account or for several accounts when you select the Transaction Display option. If you elect to print the transactions and you need a list of printers, simply enter a ? at the DEVICE: prompt.

### Information Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Demographic information about any patient enrolled in the system is stored in both the Patient Funds file (# 470) and the Hospital Patient file (# 2). To gain access to such material as the patient’s address, birthdate, date of admission to the VA, name of nearest relative, and other demographic information and to gain access to information about the financial status of the patient’s account, simply select the Information Display option and then enter the patient name. If you want to print the account information, enter the name or number of your printer at the DEVICE: prompt. If you want to view the account information, press the RETURN key at the DEVICE: prompt and press RETURN at the RIGHT MARGIN: prompt. In your first screen, you will see demographic and financial information.

In the second screen that appears after you select the Information Display option, you will see information under the categories “Name”, “Social Security Number”, “Nearest Relative, Civil Guardian”, “VA Guardian”, “Sources of income”, and “General Information/Remarks”.

### Master Transaction Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each transaction that you record in the system receives an alphanumeric code such as 9M or 42M. The “M” represents the word “master”, while the Arabic number represents the order in which the transaction took place - for example, transaction 9M occurred earlier than transaction 42M.

If you wish to see or print all of the transactions in your file, select the option entitled Master Transaction Review. At that point, your screen will display the prompt:

Select MASTER TRANSACTION ID:

![](pfop-version-3-user-manual-for-patient-funds-supervisor/016.png)

Enter a ? at the MASTER TRANSACTION ID: prompt and your screen will ask you to enter a Patient Funds master transaction number and will also ask if you need to review the complete list of all the Patient Funds master transaction numbers in the system. Once you enter the Patient Funds master transaction ID, you are ready either to print the master list or review the information on your screen.

## Using The Output (Reports) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generating reports is another important task that you are called upon to perform. With the increased use of your system comes the increased need to produce printouts that support the basic fiscal and accountability controls designed to protect monies held in trust. Whenever you use the menu options

Activity (AUDIT) Listing  
Dormant Account Listing  
Indigent Patient Listing  
Overdue Restriction Search  
Patient Summary Report  
Search for Min./Max Restrictions  
Out of Balance Report  
Listing of Patients  
Balance in Accounts  
Transaction Listing  
Fiscal Reports

Unassigned Station-ID List

you are working within the Output (Reports) Menu and the reports that you print with these menu options will help the VA monitor all of the transactions involving Patient Funds

accounts.

### Activity (AUDIT) Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides a printout of all Patient Funds transactions for a selected date range. The information is sorted in the following order: (1) transaction date; (2) type of transaction - deposit or withdrawal; (3) type of currency - cash, check, or “other”; and the (4) type of VA form. Subtotals are calculated for each transaction type, type of currency, and VA form.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

Select Output (Reports) Menu Option: Activity (AUDIT) Listing

Single Station List or All Station List: ALL// s SINGLE

Select INSTITUTION NAME: CITYNAME, NY 514

Enter Beginning Date: t-20 (MAY 25, 2002)

Enter Ending Date: t (JUN 14, 2002)

...Hmmm, This may take a few moments...

DEVICE: UCX/TELNET Right Margin: 80// 132

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 1

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

DATE TRANSACTION ENTERED: MAY 29,2002

DEPOSIT/WITHDRAWAL: DEPOSIT

CASH/CHECK/OTHER: CASH

FORM: 4-1028

CITYNAME, NY IPFPATIENT, ONE MAY 29,2002 GIFT 50.00 FROM SISTER

-----------

SUBTOTAL 50.00

-----------

SUBTOTAL 50.00

-----------

SUBTOTAL 50.00

-----------

SUBTOTAL 50.00

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 2

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

DATE TRANSACTION ENTERED: MAY 30,2002

DEPOSIT/WITHDRAWAL: DEPOSIT

CASH/CHECK/OTHER: CASH

FORM: 4-1028

CITYNAME, NY IPFPATIENT, ONE MAY 29,2002 WKLY ALLO 50.00

CITYNAME, NY IPFPATIENT, TWO MAY 29,2002 GIFT 20.00

CITYNAME, NY IPFPATIENT, TWO MAY 29,2002 WKLY ALLO 20.00

CITYNAME, NY IPFPATIENT, THREE MAY 29,2002 WKLY ALLO 100.00

CITYNAME, NY IPFPATIENT, THREE MAY 29,2002 GIFT 100.00

CITYNAME, NY IPFPATIENT, FOUR MAY 29,2002 WKLY ALLO 10.00

-----------

SUBTOTAL 300.00

-----------

SUBTOTAL 300.00

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 3

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

CASH/CHECK/OTHER: CHECK

FORM: 4-1028

CITYNAME, NY IPFPATIENT, ONE MAY 29,2002 WKLY ALLO 40.00

CITYNAME, NY IPFPATIENT, ONE MAY 29,2002 WKLY ALLO 50.00

CITYNAME, NY IPFPATIENT, TWO MAY 29,2002 GIFT 20.00

-----------

SUBTOTAL 110.00

-----------

SUBTOTAL 110.00

CASH/CHECK/OTHER: OTHER

FORM: 4-1028

CITYNAME, NY IPFPATIENT, THREE MAY 29,2002 GIFT 30.00 FROM DAUGHTER

CITYNAME, NY IPFPATIENT, FOUR MAY 29,2002 WKLY ALLO 50.00

-----------

SUBTOTAL 80.00

-----------

SUBTOTAL 80.00

-----------

SUBTOTAL 490.00

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 4

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

DEPOSIT/WITHDRAWAL: WITHDRAWAL

CASH/CHECK/OTHER: CASH

FORM: 10-1126

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA -20.00 TEST DATA

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA -20.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA -20.00

CITYNAME, NY IPFPATIENT, FOUR MAY 30,2002 TEST DATA -20.00

CITYNAME, NY IPFPATIENT, FOUR MAY 30,2002 TEST DATA -20.00

CITYNAME, NY IPFPATIENT, FOUR MAY 30,2002 TEST DATA -25.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA -50.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA -50.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA -50.00

-----------

SUBTOTAL -275.00

-----------

SUBTOTAL -275.00

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 5

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

CASH/CHECK/OTHER: CHECK

FORM: 10-1126

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA -10.00

-----------

SUBTOTAL -10.00

-----------

SUBTOTAL -10.00

CASH/CHECK/OTHER: OTHER

FORM: 10-1126

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 WKLY WDL -5.00

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 WKLY WDL -20.00

-----------

SUBTOTAL -25.00

-----------

SUBTOTAL -25.00

-----------

SUBTOTAL -310.00

-----------

SUBTOTAL 180.00

-----------

PATIENT FUNDS DAILY ACTIVITY (AUDIT) LISTING JUN 14,2002 13:49 PAGE 6

TRANSACTION

STATION PATIENT NAME DATE REFERENCE AMOUNT REMARKS

---------------------------------------------------------------------------------------------------------------

TOTAL 230.00

The information contained in this report is protected by the Privacy Act of 1974

### Dormant Account Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option searches the accounts and prints a list of all accounts which have had no activity for the period of time you specify at the first prompt.

Enter number of days since last transaction for account to be included

on this report. 180//

At this point, accept the default response or enter a higher or lower number. This new number represents the maximum time period that must pass without any account activity before the account is considered dormant. While viewing the list on your screen, you MAY spot accounts that have zero balances. At printing time, you will have a chance to exclude such accounts when you respond to the prompt “Do you wish to include accounts with zero (0) balances? NO//”.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? to see the list of institutions. Only an institution with a station number assigned to it may be selected.

### Indigent Patient Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option list all patients marked “Indigent”. (This is done by entering YES in the INDIGENT field in the Long Form Registration option.)

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? to see the list of institutions. Only an institution with a station number assigned to it may be selected.

PATIENT FUNDS INDIGENT LIST JUN 13,2002 16:12 PAGE 1

STATION NAME SSN WARD INDGNT BALANCE

--------------------------------------------------------------------------------

CITYNAME, NY IPFPATIENT, ONE 000456789 YES 60.00

CITYNAME, NY IPFPATIENT, TWO 000456789 YES 85.00

The information contained in this report is protected by the Privacy Act of 1974

### Overdue Restriction Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generating a list of all Patient Funds accounts that are identified as “restricted” and that have dates of restriction older than 180 days can be accomplished by selecting the menu option entitled Overdue Restriction Search. In the displayed or printed report of all accounts that have overdue restrictions, you will see each patient’s name, social security number, and current restriction date.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? to see the list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS LISTING OF OUT OF DATE RESTRICTIONS JUN 13,2002 10:21 PAGE 1

DATE OF

CURRENT PROVIDER AUTHORIZING

STATION NAME NAME SSN WARD RESTRICTION RESTRICTION

-------------------------------------------------------------------------------------------------

IPFPATIENT, ONE 000456789 SEP 28,2001 IPFPROVIDER, ONE

ANYCITY, FL IPFPATIENT, TWO 000456789 OCT 22,2001 IPFPROVIDER, ONE

ANYCITY, IL IPFPATIENT, THREE 000456789 NOV 1,2001 IPFPROVIDER, ONE

ANYSITE, DE IPFPATIENT, FOUR 000456789 NOV 11,2001 IPFPROVIDER, ONE

The information contained in this report is protected by the Privacy Act of 1974

### Patient Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the close of EACH BUSINESS DAY, you should use the Patient Summary Report menu option to produce a list of all your ACTIVE Patient Funds accounts. In the printed list, you will find information that will help the PFOP program to disburse Patient Funds manually should a computer failure occur.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be printed at 132 columns.

### Search for Min/Max Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a report of all accounts on which the balance is outside of the range(s) specified in the minimum and maximum balance fields in the Long Form Registration option.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

PATIENT FUNDS MIN/MAX \#1 REPORT JUN 12,2002 15:38 PAGE 1

MINIMUM MAXIMUM

STATION BALANCE BALANCE

NAME NAME SSN WARD BALANCE \#1 \#1

-------------------------------------------------------------------------------

IPFPATIENT, ONE 000456789 10 400

IPFPATIENT, TWO 000456789 -5.00 3 120

CITYNAME, NY IPFPATIENT, THREE 000456789 -5.00 55 410

ANYCITY, IPFPATIENT, FOUR 000456789 5.00 15 260

ANYCITY, IPFPATIENT, FIVE 000456789 -5.00 25 300

LONG BEACH IPFPATIENT, SIX 000456789 -20.00 8 220

PATIENT FUNDS MIN/MAX \#2 REPORT JUN 12,2002 15:39 PAGE 1

MINIMUM MAXIMUM

STATION BALANCE BALANCE

NAME NAME SSN WARD BALANCE \#2 \#2

-------------------------------------------------------------------------------

IPFPATIENT, ONE 000456789 20 300

IPFPATIENT, TWO 000456789 -5.00 15 200

CITYNAME, NY IPFPATIENT, THREE 000456789 -5.00 23 333

ANYCITY, IPFPATIENT, FOUR 000456789 5.00 17 310

ANYCITY, IPFPATIENT, FIVE 000456789 -5.00 15 200

LONG BEACH IPFPATIENT, SIX 000456789 -20.00 80 450

The information contained in this report is protected by the Privacy Act of 1974

### Out of Balance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option reviews each account and compares the computed balance (the figure that is calculated at the time you select this menu option) for each transaction with the stored balance (the figure that is derived after you have completed a Patient Funds account transaction) for the account. If a discrepancy is found, the patient is listed on the report for later evaluation.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS OUT OF BALANCE REPORT JUN 6,2002 16:16 PAGE 1

STORED COMPUTED

STORED PRIVATE STORED COMPUTED PRIVATE COMPUTED

STATION NAME SSN BALANCE SOURCE GRATUITOUS BALANCE SOURCE GRATUITOUS

---------------------------------------------------------------------------------------------------------------

CITYNAME, NY IPFPATIENT, TWO 000456789 1.00 0.00 85.00 85.00 0.00 85.00

ANYCITY, FL IPFPATIENT, ONE 000456789 1.00 0.00 5.00 5.00 0.00 5.00

ANYCITY, FL IPFPATIENT, THREE 000456789 1.00 0.00 -5.00 -5.00 0.00 -5.00

LONG BEACH, CA IPFPATIENT, FOUR 000456789 1.00 0.00 -20.00 -20.00 0.00 -20.00

LONG BEACH, CA IPFPATIENT, FIVE 000456789 1.00 0.00 5.00 5.00 0.00 5.00

ANYCITY, IL IPFPATIENT, SIX 000456789 1.00 0.00 180.00 180.00 0.00 180.00

OMAHA, NE IPFPATIENT, SEVEN 000456789 1.00 0.00 3.00 3.00 0.00 3.00

The information contained in this report is protected by the Privacy Act of 1974

### Listing of Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a list of all Patient Funds patients. Information includes the station, patient’s name, Social Security Number, claim number, ward, account status, patient type (restricted or unrestricted), date of current restriction (if any), date of birth, date of last transaction, and the stored balance for the account.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS LIST JUN 13,2002 13:04 PAGE 1

DATE OF DATE OF

CLAIM ACCOUNT PATIENT CURRENT LAST STORED

STATION NAME SSN NUMBER WARD STATUS TYPE RESTRICTION DOB TRANSACTION BALANCE

--------------------------------------------------------------------------------------------------------------------

IPFPAT, ONE 000456789 ACTIVE RESTRICTE SEP 28,2001 MAR 5,1945

IPFPAT, TWO 000456789 ACTIVE RESTRICTE MAY 30,2002 JUL 9,1961 MAY 30,2002 -5.00

CITYNAME, NY IPFPAT, THREE 000456789 ACTIVE UNRESTRIC APR 4,1954 MAY 30,2002 60.00

CITYNAME, NY IPFPAT, FOUR 000456789 ACTIVE RESTRICTE MAY 24,2002 FEB 2,1909 MAY 30,2002 90.00

CITYNAME, NY IPFPAT, FIVE 000456789 ACTIVE UNRESTRIC MAR 3,1933 MAY 30,2002 85.00

The information contained in this report is protected by the Privacy Act of 1974

### Balance In Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a report that shows the grand total of the balances in the Patient Funds system. This report is used by Fiscal to reconcile the general ledger.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

Select Output (Reports) Menu Option: Balance in Accounts

Single Station List or All Station List: ALL// s SINGLE

Select INSTITUTION NAME: CITYNAME, NY 514

...Excuse me, I'm working as fast as I can...

DEVICE: UCX/TELNET Right Margin: 80//

PATIENT FUNDS BALANCE IN ALL ACCOUNTS JUN 13,2002 13:26 PAGE 1

STORED

STATION NAME NAME BALANCE

--------------------------------------------------------------------------------

CITYNAME, NY IPFPATIENT, THREE 60.00

CITYNAME, NY IPFPATIENT, ONE 90.00

CITYNAME, NY IPFPATIENT,TWO 85.00

CITYNAME, NY IPFPATIENT,FOUR -5.00

-----------

SUBTOTAL 230.00

-----------

TOTAL 230.00

The information contained in this report is protected by the Privacy Act of 1974

### Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report of all the Patient Funds transactions entered into your system for a selected date range. Transactions are grouped by the date the transaction was entered. The report includes the station name, transaction ID, patient name, the reference code, transaction date and dollar amount, the type of transaction (deposit or withdrawal), and the initials of the Patient Funds clerk who processed the transaction.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS DAILY TRANSACTION LISTING JUN 13,2002 13:53 PAGE 1

TRANSACTION TRANSACTION CLERK

STATION ID PATIENT NAME REFERENCE DATE AMOUNT DEP/WITH INITIALS

---------------------------------------------------------------------------------------------------------------

DATE TRANSACTION ENTERED: MAY 29,2002

CITYNAME, NY 1M IPFPATIENT, ONE WKLY ALLOT MAY 29,2002 50.00 DEPOSIT

DATE TRANSACTION ENTERED: MAY 30,2002

CITYNAME, NY 2M IPFPATIENT, TWO WKLY ALLOT MAY 29,2002 40.00 DEPOSIT

CITYNAME, NY 3M IPFPATIENT, THREE WKLY ALLOT MAY 29,2002 30.00 DEPOSIT

CITYNAME, NY 4M IPFPATIENT, FOUR GIFT MAY 30,2002 -20.00 WITHDRAWAL

The information contained in this report is protected by the Privacy Act of 1974

### Fiscal Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fiscal Reports menu includes the Audit Report, the Transaction Summary Report, and the Date Variance Report. At the end of each month, Fiscal Service will attempt to reconcile the transaction amounts in the general ledger control accounts and the transaction amounts in your fiscal report accounts.

Audit Report

In the Audit Report, information is sorted by transaction date; transaction type; and form type. If, for example, you processed seven deposits on May 30, 2002 using the BALCARFWD form for two of the transactions and FORM 4-1028 for the remaining, your report will list the patient account names for all seven transactions under May 30, 2002. Within that broad category, all seven transactions will appear under DEPOSIT (instead of WITHDRAWAL). Finally, under DEPOSIT, you will find the subheading FORM with all the associated detailed records for that form.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS END OF MONTH REPORT FOR FISCAL SERVICE JUN 14,2002 14:57 PAGE 1

DATE

TRANSACTION

STATION PATIENT NAME ENTERED REFERENCE CASH/CHECK/OTHER AMOUNT REMARKS

------------------------------------------------------------------------------------------------------

TRANSACTION DATE: MAY 29,2002

DEPOSIT/WITHDRAWAL: DEPOSIT

FORM: 4-1028

CITYNAME, NY IPFPATIENT, TWO MAY 29,2002 TEST DATA CASH 50.00

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA CHECK 40.00

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA OTHER 30.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA CASH 50.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA CHECK 50.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA OTHER 50.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CASH 20.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CHECK 20.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CASH 20.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH 100.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH 100.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH 10.00

-----------

SUBTOTAL 540.00

PATIENT FUNDS END OF MONTH REPORT FOR FISCAL SERVICE JUN 14,2002 14:57 PAGE 2

DATE

TRANSACTION

STATION PATIENT NAME ENTERED REFERENCE CASH/CHECK/OTHER AMOUNT REMARKS

------------------------------------------------------------------------------------------------------

TRANSACTION DATE: MAY 30,2002

DEPOSIT/WITHDRAWAL: WITHDRAWAL

FORM: 10-1126

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA CASH -20.00

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA CHECK -10.00

CITYNAME, NY IPFPATIENT, TWO MAY 30,2002 TEST DATA OTHER -5.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA CASH -20.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA CASH -20.00

CITYNAME, NY IPFPATIENT, THREE MAY 30,2002 TEST DATA OTHER -20.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CASH -20.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CASH -20.00

CITYNAME, NY IPFPATIENT, FIVE MAY 30,2002 TEST DATA CASH -25.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH -50.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH -50.00

CITYNAME, NY IPFPATIENT, ONE MAY 30,2002 TEST DATA CASH -50.00

-----------

SUBTOTAL -310.00

-----------

TOTAL 230.00

The information contained in this report is protected by the Privacy Act of 1974

Transaction Summary Report

The Transaction Summary Report report lists all of the transactions entered into the system for a date or range of dates specified by the user. It differs from the transaction summary used by the Patient Fund Clerks in that it sorts by the DATE OF THE TRANSACTION rather than the DATE THE TRANSACTION WAS ENTERED. This allows for predating entries for the previous month on the first day of the following month.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

This report should be run at 132 columns.

PATIENT FUNDS - FISCAL TRANSACTION SUMMARY JUN 14,2002 15:07 PAGE 1

DATE

TRANSACTION TRANSACTION CLERK

STATION ID PATIENT NAME REFERENCE ENTERED AMOUNT DEP/WITH INITIALS

-----------------------------------------------------------------------------------------------------

TRANSACTION DATE: MAY 29,2002

CITYNAME, NY 1M IPFPATIENT, TWO TEST DATA MAY 29,2002 50.00 DEPOSIT

CITYNAME, NY 2M IPFPATIENT, TWO TEST DATA MAY 30,2002 40.00 DEPOSIT

CITYNAME, NY 3M IPFPATIENT, TWO TEST DATA MAY 30,2002 30.00 DEPOSIT

CITYNAME, NY 31M IPFPATIENT, THREE TEST DATA MAY 30,2002 50.00 DEPOSIT

CITYNAME, NY 32M IPFPATIENT, THREE TEST DATA MAY 30,2002 50.00 DEPOSIT

CITYNAME, NY 33M IPFPATIENT, THREE TEST DATA MAY 30,2002 50.00 DEPOSIT

CITYNAME, NY 43M IPFPATIENT, FOUR TEST DATA MAY 30,2002 20.00 DEPOSIT

CITYNAME, NY 44M IPFPATIENT, FOUR TEST DATA MAY 30,2002 20.00 DEPOSIT

CITYNAME, NY 45M IPFPATIENT, FOUR TEST DATA MAY 30,2002 20.00 DEPOSIT

CITYNAME, NY 103M IPFPATIENT, ONE TEST DATA MAY 30,2002 100.00 DEPOSIT

CITYNAME, NY 104M IPFPATIENT, ONE TEST DATA MAY 30,2002 100.00 DEPOSIT

CITYNAME, NY 105M IPFPATIENT, ONE TEST DATA MAY 30,2002 10.00 DEPOSIT

PATIENT FUNDS - FISCAL TRANSACTION SUMMARY JUN 14,2002 15:07 PAGE 2

DATE

TRANSACTION TRANSACTION CLERK

STATION ID PATIENT NAME REFERENCE ENTERED AMOUNT DEP/WITH INITIALS

------------------------------------------------------------------------------------------------------

TRANSACTION DATE: MAY 30,2002

CITYNAME, NY 4M IPFPATIENT, TWO TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 5M IPFPATIENT, TWO TEST DATA MAY 30,2002 -10.00 WITHDRAWAL

CITYNAME, NY 6M IPFPATIENT, TWO TEST DATA MAY 30,2002 -5.00 WITHDRAWAL

CITYNAME, NY 34M IPFPATIENT, THREE TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 35M IPFPATIENT, THREE TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 36M IPFPATIENT, THREE TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 46M IPFPATIENT, FOUR TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 47M IPFPATIENT, FOUR TEST DATA MAY 30,2002 -20.00 WITHDRAWAL

CITYNAME, NY 48M IPFPATIENT, FOUR TEST DATA MAY 30,2002 -25.00 WITHDRAWAL

CITYNAME, NY 106M IPFPATIENT, ONE TEST DATA MAY 30,2002 -50.00 WITHDRAWAL

CITYNAME, NY 107M IPFPATIENT, ONE TEST DATA MAY 30,2002 -50.00 WITHDRAWAL

CITYNAME, NY 108M IPFPATIENT, ONE TEST DATA MAY 30,2002 -50.00 WITHDRAWAL

The information contained in this report is protected by the Privacy Act of 1974

Date Variance Report

This options allows you to print a report of transactions, for a selected date range, on which the Transaction Date and Date Transaction entered of different.

Select Fiscal Reports Option: Date Variance Report

\* Previous selection: DATE TRANSACTION ENTERED not null

START WITH DATE TRANSACTION ENTERED: FIRST//

DEVICE: UCX/TELNET Right Margin: 80// 132

PATIENT FUNDS MASTER TRANSACTION LIST OF DATE VARIANCES JUL 2,2002 09:20 PAGE 1

DATE DAYS

TRANSACTION TRANSACTION TRANSACTION BETWEEN

ID PATIENT NAME AMOUNT DATE ENTERED DATES

------------------------------------------------------------------------------------------------------

2M IPFPATIENT, TWO 40.00 MAY 29,2002 MAY 30,2002 1

3M IPFPATIENT, TWO 30.00 MAY 29,2002 MAY 30,2002 1

7M IPFPATIENT, ONE 50.00 MAY 29,2002 MAY 30,2002 1

8M IPFPATIENT, ONE 40.00 MAY 29,2002 MAY 30,2002 1

9M IPFPATIENT, ONE 30.00 MAY 29,2002 MAY 30,2002 1

13M IPFPATIENT, FOUR 50.00 MAY 29,2002 MAY 30,2002 1

14M IPFPATIENT, FOUR 50.00 MAY 29,2002 MAY 30,2002 1

15M IPFPATIENT, FOUR -10.00 MAY 29,2002 MAY 30,2002 1

19M IPFPATIENT, FIVE 20.00 MAY 29,2002 MAY 30,2002 1

20M IPFPATIENT, FIVE 10.00 MAY 29,2002 MAY 30,2002 1

21M IPFPATIENT, FIVE 10.00 MAY 29,2002 MAY 30,2002 1

25M IPFPATIENT, SIX 30.00 MAY 29,2002 MAY 30,2002 1

26M IPFPATIENT, SIX 10.00 MAY 29,2002 MAY 30,2002 1

27M IPFPATIENT, SIX 10.00 MAY 29,2002 MAY 30,2002 1

31M IPFPATIENT, THREE 50.00 MAY 29,2002 MAY 30,2002 1

32M IPFPATIENT, THREE 50.00 MAY 29,2002 MAY 30,2002 1

33M IPFPATIENT, THREE 50.00 MAY 29,2002 MAY 30,2002 1

### Unassigned Station-ID List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows users to determine which Patient Funds accounts do not have a Station Identifier. The report includes the patient name, SSN, and ward number, and is sorted by the patient name. You are given the option of including INACTIVE patients on the report, if you wish.

Enter a RETURN at the DEVICE: prompt to print this report to your screen, or enter the appropriate printer name/number.

Select Output (Reports) Menu Option: Unassigned Station-ID List

Would you like to include INACTIVE patients in this report? NO//

...Sorry, Let me put you on 'HOLD' for a second...

DEVICE: UCX/TELNET Right Margin: 80//

UNASSIGNED STATION NAME LISTING JUN 17,2002 11:36 PAGE 1

PATIENT NAME SSN WARD

-------------------------------------------------------------------------------

IPFPATIENT, ONE 000456789 5D MED

IPFPATIENT, TWO 000456789 5A SURG

The information contained in this report is protected by the Privacy Act of 1974

## Using The Signature Code Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you need to enter or change your electronic signature code, select the Electronic Signature Code Edit option under the User’s Toolbox (XUSERTOOLS) menu. The electronic signature or computer code is your legal signature; it is just as binding and just as effective as your handwritten signature on a piece of paper. Because it’s “encrypted” or scrambled, no one-not even a computer programmer-can duplicate your signature code. It’s yours alone. Furthermore, you alone are responsible for entering your new signature code into the computer or changing your code.

This menu option also allows you to change your initials, your signature block printed name, your signature block title, and your office phone number. Now, to begin, simply enter two to five new characters at the INITIALS: prompt or accept the default response, if any. Follow the same procedure - entering your new or revised information OR accepting the default response - at the SIGNATURE BLOCK PRINTED NAME: prompt, the SIGNATURE BLOCK TITLE: prompt, and the OFFICE PHONE: prompt. In the final field, you are asked to enter the 6 to 20 characters (no control or lowercase characters) that serve as your electronic signature. If you are a new user, the screen will display the “Enter New Signature Code:” prompt. If you are a regular user, the screen will first display the “Enter current Signature Code:” prompt and will then display the “Enter New Signature Code:” prompt.

> <span id="XU_80_679" class="anchor"></span>Note: If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/017.png)

Remember, your electronic signature is your legal signature. Entering your code on the computer is equivalent to signing your name on a VA Form.

## Using The Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only those individuals who manage the work and assignments of Patient Funds clerks and other system users will have access to the Supervisor Menu. These options are used to modify forms and information and to review work progress reports. They allow you to update account forms and information, and determine if your unit is operating effectively.

1 Add/Edit Patient Funds Forms  
2 Enter/Edit Remarks Codes  
3 Clear Account Lock  
4 Deferral Date Edit  
5 Productivity Report  
6 Update Patient Status for ALL Accounts  
7 Verify and Correct Balance

8 Archive Patient Funds Transactions

   9 Summarize & Purge Patient Funds Transactions

10 Date Variance Report

11 Negative Balance Report

12 Database Diagnostic Report

 

### Add/Edit Patient Funds Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select the Add/Edit Patient Funds Forms menu option, you have the tools necessary to design a new system form or modify an existing one. Among the fields that you can add or change are the form number, the form title, the abbreviation used to identify the form, and the type of action (deposit, withdrawal, or both). If you need to see a list of the form names and their corresponding numbers, enter ? at the Select PATIENT FUNDS FORMS NAME: prompt. After you have entered the form name or number, your screen will display a series of prompts that give you a chance to modify or delete an existing field in the form you have selected.

### Enter/Edit Remarks Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Enter/Edit Remarks Codes option allows you to change the fields in any one of the twelve remarks codes you encountered while using the Post Patient Funds Transaction option. To see a list of the remarks code numbers and the terms they represent, simply enter a ? at the Select PATIENT FUNDS REMARKS CODE NAME: prompt. After you select the desired code number, your screen will display the code and then the full remark, allowing you to edit one or both. If, for example, you select remarks code number 8, your screen will display the default response SD//. And your next prompt will be SPECIFIC DONATION//.

![](pfop-version-3-user-manual-for-patient-funds-supervisor/018.png)

Using your Add/Edit Patient Funds Forms Option

![](pfop-version-3-user-manual-for-patient-funds-supervisor/019.png)

Using your Enter/Edit Remarks Codes Option

### Clear Account Lock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To prevent another user from selecting the SAME Patient Funds account that you are currently editing, your system automatically LOCKS the account. Once you finish working on the account, the system then CLEARS or unlocks the account. On rare occasions, the task that you are performing might end abruptly because of a power failure or line drop. In such an event, the automatic clear or unlock procedure may not occur and your screen will display the message “This file is being edited by (YOUR LAST NAME, YOUR FIRST NAME). Please try later”. When you see such a message, get out of your current option. Then select the Clear Account Lock menu option and unlock the account you were editing before the interruption occurred. You will use this same option to unlock accounts for Patient Funds Clerks who encounter the same difficulties and contact you for help.

### Deferral Date Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes, you will find it necessary to change the deferral date for a transaction. When this need arises, use the Deferral Date Edit option. Deferral dates are changed for two basic reasons: the date originally entered was incorrect or the Facility Director decides another date is more appropriate. When using this option, you will have to reply to both the Select DEFERRED CREDIT REF \#: prompt and the DEFERRED DATE: prompt. The deferred credit reference number prompt refers to the computer-generated number assigned to each deferral transaction.

### Productivity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Productivity Report that you generate by selecting the menu option of the same name, you will see information outlining the number of transactions that each system user posted for a range of dates. At the end of the report appears the total number of transactions posted. To print a copy of the report, enter your printer name or number at the DEVICE: prompt and then either accept the default response at the RIGHT MARGIN: prompt or enter your own margin specification. To display the report, press the RETURN key twice - once at the DEVICE: prompt and once at the RIGHT MARGIN: prompt.

### Update Patient Status for ALL Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Included within your file of Patient Funds accounts are the names of inactive as well as active accounts. To print or display a report that lists each accounts status, simply select the menu option entitled Update Patient Status for ALL Accounts.

### Verify and Correct Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system maintains two sets of balances: the computed balance and the stored balance. When generating the computed balance, the system reviews each one of the transactions in a Patient Funds account and then calculates the total balance amount. Such a procedure can take a long time, especially if an account has a large number of transactions. When computing the account’s stored balance, on the other hand, the system is much faster. It looks only at the stored balance (the amount calculated after the most recent account transaction). When a new transaction takes place against an account, your system adds or subtracts the value of the transaction against the stored balance and then derives the NEW stored balance.

Should you need to review or correct the balance in a Patient Funds account, select the menu option entitled Verify and Correct Balance; however, before using this menu option, make sure that the account has been audited. Once you have selected the Verify and Correct Balance menu option, you will see amounts listed under the columns “Balance in Account” and “Corrected Balance” and you will see the prompt:

Are you ready to post the corrected balances to the account? NO //

### Negative Balance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a list of all accounts with a negative balance in the stored balance, monthly restriction balance, or weekly restriction balance.

You will see the prompt, “Single Station List or All Station List: ALL//”. Accept the default of ALL to include all stations. If you enter SINGLE, you are prompted to enter an institution name. You may enter a ?? for a list of institutions. Only an institution with a station number assigned to it may be selected.

PATIENT FUNDS NEGATIVE BALANCE LIST JUN 13,2002 15:05 PAGE 1

MONTHLY WEEKLY

STORED RESTRICTION RESTRICTION

STATION NAME SSN BALANCE BALANCE BALANCE

-------------------------------------------------------------------------------

OMAHA, NE IPFpatient, ONE 000456789 -20.00 0.00 0.00

OMAHA, NE IPFpatient, TWO 000456789 -10.00 0.00 0.00

ANYSITE, IPFpatient, THREE 000456789 -10.00 0.00 0.00

ANYSITE, IPFpatient, FOUR 000456789 -30.00 0.00 0.00

ANYSITE, IPFpatient, FIVE 000456789 -20.00 0.00 0.00

The information contained in this report is protected by the Privacy Act of 1974

### Database Diagnostic Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to help with database diagnostic analysis. This database analysis will be restricted to files relating to the Patient Funds package. The new diagnostic report displays a summary of invalid or missing data elements. Additionally, the diagnostic report summary has an available detail report that provides specific break out information regarding all invalid or missing data elements that are displayed in the summary. The new menu option for the Database Diagnostic Report \[PRPF DATA DIAGNOSTIC REPORT\] is listed on the Patient Funds Supervisor menu \[PRPF SUPERVISOR\] and will require the PRPF SUPERVISOR key.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fiduciary A legal entity or individual who is appointed by a court of competent jurisdiction or by the administrator and who receives VA benefits reserved for the eligible person’s use and advantage.
Gratuitous Funds With the exception of insurance, all funds that are derived from VA benefits and that are deposited in the account of a VA patient rated as Incompetent. Although the VA cannot purchase U.S. savings bonds with gratuitous funds, the patient or the patient’s representative can. When these bonds are redeemed, the proceeds (principal) are considered gratuitous funds.
Guardian A person or corporation who, following the decree of a court of competent jurisdiction, protects the person or property, or both, of a minor or mentally incompetent VA beneficiary.
Incompetent VA or court decreed classification assigned to patients who, because of mental or physical incapacity, are unable to manage their own affairs.
Institutional Award An award of disability compensation, pension, or emergency officers’ retirement pay to the Director of a VA health care facility, or to another Federal, State, or private contract facility, on behalf of a veteran rated incompetent by the VA, or adjudged incompetent by court decree, or rated incompetent by both.
Nongratuitous Funds All funds in patients’ accounts except those described as gratuitous. Interest on U.S. savings bonds purchased from gratuitous funds is also considered nongratutious.
Patients Individuals receiving hospitalization, nursing home care, and domiciliary care under VA auspices. Also individuals whose funds are managed by the VA following their release from authorized medical care.
PFOP Funds that patients or their representatives deposit in non-interest bearing accounts for safekeeping at VA health care facilities.
Restricted Accounts Patient accounts managed by the facility Director or the appointed designee.who serves as trustee. Deposited in this type of account are personal funds that belong to the following types of patients:
> 1\. All patients adjudged incompetent by a court.
> 2\. All patients whom the VA rates as Incompetent or whom the Director considers incapable of administering their funds.
> 3\. For purposes of administration, psychiatric patients whose funds should be controlled because of their ward assignment or because an incompetency rating is pending.
> For temporary periods, Directors may designate certain “restricted” accounts as “unrestricted” and may authorize the patient concerned to use the account, within prudent limits, as an unrestricted account if such use will aid the patient’s therapeutic progress or will help to determine whether the patient has the ability to handle the funds.
Review Panel Three-member board that determines patient’s competency and reviews appeals about patient competency. Panel includes (1) the Director (except where the Director appoints a team to determine the patient’s competency) or Assistant Director; (2) the Chief of Staff; and (3) a mental health professional. Members of the treatment team for the patient being evaluated are prohibited from serving on the review panel.
Unrestricted Accounts Accounts of patients capable of handling personal funds that are deposited for safekeeping. Such accounts are not subject to the trusteeship of the Director, and are available for return to the patients on demand.
