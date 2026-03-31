---
title: Beneficiary Travel Version 1 User Manual (Updated with DGBT*1*41)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (Updated with DGBT*1*41)
app_code: DGBT
app_name: Beneficiary Travel
section: CLI
app_status: active
pkg_ns: DGBT
patch_ver: 1
patch_id: DGBT*1
group_key: "DGBT:DGBT:1"
file_numbers: []
security_keys: []
menu_options: 7
description: 
audience: 
keywords: 
  - report
  - date
  - travel
  - dgbtpatient
  - table
  - contents
  - testing
  - beneficiary
  - claim
  - dellinger
page_count: 0
word_count: 8428
section_count: 10
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt_1_41_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt_1_41_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=123"
---

Beneficiary Travel (BT)

User Manual

![](beneficiary-travel-version-1-user-manual-updated-with-dgbt-1-41/001.png)

Revised for Patch DGBT\*1\*41

February 2024

Office of Information and Technology (OIT)

Product Development

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 55%" />
<col style="width: 14%" />
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
<td>2/2024</td>
<td>DGBT*1*0*41</td>
<td><p>Decomission of options</p>
<p>Removed sections:</p>
<p><strong>4.1 Bene Travel Account file Enter/Edit</strong></p>
<p><strong>4.2 Claim Enter/Edit – Special Mode Claims</strong></p>
<p><strong>4.4 Reprint Denial of Benefits Letters</strong></p></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>12/2023</td>
<td>DGBT*1*0*40</td>
<td><p>Partial decommission of package and decommission of BT Dashboard – removing Mileage claims functionality – leaving Special Mode Claims</p>
<p>Removed mentions of decommissioned functions:</p>
<p>BT Alternate Income Enter/Edit [DGBT ALTERNATE INCOME]   </p>
<p>Income Certification Eligibility [DGBT BENE TRAVEL CERTIFICATION]                                           </p>
<p>Edit the BT Dashboard configuration [DGBT BENE TRAVEL CONFIG EDIT]                                             </p>
<p>Parameter Rates Enter/Edit [DGBT BENE TRAVEL RATES]      </p>
<p>Reprint of 70-3542d form [DGBT BENE TRAVEL REPRINT]       </p>
<p>Manual Deductible Waiver [DGBT MANUAL DEDUCTIBLE WAIVER]</p></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>11/23/2015</td>
<td>2.6</td>
<td>Updated Section 3.4 per PS review</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>10/29/2015</td>
<td>2.5</td>
<td>BT Bulleting added Section 3.4</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>9/2015</td>
<td>DGBT*1*25</td>
<td>Corrected misspelling of “processing”, p 20.</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>3/5/2014</td>
<td>2.3</td>
<td>Modified the following sections to add VFA changes: Introduction, 4.2 “Waiver Expiration”, “Income and Status Display from Means and Co-pay tests”, and “Previous Income Information Retrieval”, and glossary</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>12/2013</td>
<td>2.2</td>
<td>Updated for patch 21. Removed summary of Distance Enter/Edit menu option and section for Distance Enter/Edit menu option which was removed from the application; pages 6, 34. Revised mileage prompt; page 20.</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>2/25/2013</td>
<td>2.1</td>
<td>Updated Table on Content</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>2/22/2013</td>
<td>2.0</td>
<td>Removed Report of Claim Amounts from Sub Menu and add it to Main Menu. Corrected font on section 4.1. Corrected formatting of paragraphs.</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>01/15/2013</td>
<td>2.0</td>
<td>Final – added additional HPS comments</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>01/08/2013</td>
<td>2.0</td>
<td>Final – accepted PS changes</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>01/01/2013</td>
<td>2.0</td>
<td>Draft 15 – added index</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>12/17/2012</td>
<td>2.0</td>
<td>Draft 14 – updated based on PS comments</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>11/27/2012</td>
<td>2.0</td>
<td>Draft 13 – updated based on changes during Alpha testing Section 4.1, section 4.2</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>9/4/12</td>
<td>2.0</td>
<td>Draft 12</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>9/3/12</td>
<td>2.0</td>
<td>Draft 11</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>8/30/2012</td>
<td>2.0</td>
<td>Updated draft 7 based on AM comments</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>8/30/2012</td>
<td>2.0</td>
<td>Updated draft 8 based on AM comments</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>8/29/2012</td>
<td>2.0</td>
<td>Updated draft based on CH comments</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>8/24/2012</td>
<td>2.0</td>
<td>Updated User Manual based on 2012 enhancements</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>2/2008</td>
<td>1.0</td>
<td><p>Patch 14, 15 (ability to change rates</p>
<p>removed)</p></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>4/2002</td>
<td></td>
<td>Originally released</td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
  - [Is this Chapter for You?](#is-this-chapter-for-you)
  - [How Does VistA Work?](#how-does-vista-work)
    - [Exiting an Option](#exiting-an-option)
    - [Entering Data](#entering-data)
    - [Obtaining Help](#obtaining-help)
    - [Responding to Prompts](#responding-to-prompts)
    - [Select Prompt](#select-prompt)
    - [Yes/No Prompt](#yesno-prompt)
    - [Default Prompt](#default-prompt)
    - [Invalid Response](#invalid-response)
    - [LAYGO](#laygo)
    - [Entering Dates and Times](#entering-dates-and-times)
    - [Making Corrections](#making-corrections)
    - [Spacebar Recall Feature](#spacebar-recall-feature)
- [Beneficiary Travel Menu](#beneficiary-travel-menu)
  - [Beneficiary Travel Reports Submenu](#beneficiary-travel-reports-submenu)
  - [Summary of Main Menu items](#summary-of-main-menu-items)
  - [Summary of Reports Sub-Menu Options](#summary-of-reports-sub-menu-options)
  - [Beneficiary Travel Bulletin](#beneficiary-travel-bulletin)
- [User Instructions](#user-instructions)
  - [View of Claim](#view-of-claim)
  - [Beneficiary Travel Reports](#beneficiary-travel-reports)
    - [Summary Report](#summary-report)
  - [> The Summary Report provides statistical totals for analysis of facility BT funds expended, claims processed, claim denials, alternate transportation usage, and Veteran eligibility demographics during a specified timeframe.](#the-summary-report-provides-statistical-totals-for-analysis-of-facility-bt-funds-expended-claims-processed-claim-denials-alternate-transportation-usage-and-veteran-eligibility-demographics-during-a-specified-timeframe)
    - [Audit Report](#audit-report)
    - [Clerk Report](#clerk-report)
    - [Travel Pattern Report](#travel-pattern-report)
    - [Special Mode Report](#special-mode-report)
    - [Fiscal Report](#fiscal-report)
    - [Report of Claim Amounts](#report-of-claim-amounts)
- [Glossary](#glossary)
- [Troubleshooting](#troubleshooting)
- [Index](#index)
The Beneficiary Travel application allows Special Mode claims to be created quickly and easily. Options on the Beneficiary Travel menu provide access to functions to determine and issue beneficiary travel pay. Travel reimbursement is given to specific categories of eligible Veterans, some of whom are subject to monthly deductibles. The deduction requirement may be waived for any Veteran who meets specific criteria, subject to the approval of the local medical center director or designee. Some of the categories eligible for this waiver have income limitations in which case an income certification form is completed and signed yearly by the Veteran, and noted in the system.
Non-employee attendants identified as Caregiver or enrolled as Collaterals for the Transplant program will be issued travel reimbursement under the Caregiver or Collateral’s name. All other non-employee attendants who are eligible for travel reimbursement will be issued payment under the Veteran’s name in the computer.
The Beneficiary Travel Enhancement project in 2012 added features for easy creation of Special Mode claims, , income information retrieval, as well as automatic determination of eligibility for Veterans to receive Beneficiary Travel reimbursement payments. The enhancement project added a series of reports with standard metrics to be run at the local level. These reports can be displayed on the monitor, printed out locally, or exported as a delimited text file to be imported into spreadsheet software (e.g. Excel). After being exported from the BT system, these reports can be sent from the local facilities to the Chief Business Office (CBO) to be aggregated into national reports for metrics and planning purposes.
> **NOTE:** Veterans Financial Assessment (VFA) – Means Tests less than 1 year old from the VFA Start Date and forward will be considered valid (current) and will not expire.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Is this Chapter for You?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are just learning to use Veterans Health Information Systems and Technology Architecture (VistA) software, this chapter will introduce you to a small but important part of the VistA world—signing on, entering data, and getting out. You do not have to be a computer expert or know a lot of technical terms to use VistA software. You do have to follow instructions. And, in general, you need to be curious, flexible, and patient. This chapter will help you to get started. If you are an experienced VistA user, this chapter can serve as a reminder.

## How Does VistA Work?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA software packages use the computer in an interactive fashion. An interactive system involves a conversation with the computer. The computer asks you to supply information and immediately processes it. You will be interacting with the software by responding to prompts (the questions) in the program. Your responses are recognized by the computer when you complete the interaction by pressing the Return or Enter key.

This software is "menu driven.” A menu is a screen display which lists all of the choices (options) available. You will see only the menus, options, and functions, which you have security clearance to use. Once you have made a selection, the software can display another menu (submenu) or you might be asked to answer questions which allow the computer to perform tasks.

### Exiting an Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In most cases, when you begin an option you will continue through it to a normal ending. At times however, you might want to exit the option to do something else. To stop what you are doing, enter a caret ^, which can also be referred to as an up-arrow or circumflex (Shift-6 on most keyboards). You can use the caret at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering the caret to completely exit the system.

### Entering Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each response that you type must be followed by pressing the Return key (or Enter key) to indicate you have completed that entry. In many cases, you need only enter the first few letters (called shortcut synonyms) of an option or field, and the computer fills in the rest. Shortcut synonyms help increase speed and accuracy.

If a prompt has no "default response" and you want to bypass the question, press the Return or Enter key and the computer will go on to the next question. You will be allowed to bypass a question only if the information is not required to continue with the option. If the prompt has a default response, entering Return or Enter is the same as entering the default response.

Some typists use the lower case L for the number 1 and the letter O for zero. Please keep in mind that with this software the number 1 and the letter l are not interchangeable. Also, the number 0 and the letter O are not interchangeable.

### Obtaining Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need assistance while interacting with the software, enter a question mark or two to receive on-line help.

? Entering a single question mark at a prompt will provide a brief help message.

?? Using two question marks will provide a more detailed help message, but may also start displaying a long list of responses to choose from.

### Responding to Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the computer prompts you with a question, typically a colon : will follow. Several types of prompts may be used including yes/no, select, and default. Prompts usually ask for information that is later stored as a field in a file, like the basic prompt shown below.

DATE OF BIRTH: Enter a value, like March 3, 1960, then press the Return or Enter key.

### Select Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the answer to the prompt is a choice of several alternatives, the question can appear prefixed with the word Select, as below.

Select PATIENT NAME:

### Yes/No Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the question requires either a Yes or No response (in which case simply Y or N, upper or lower case, is acceptable), the question will usually be followed by a question mark rather than a colon.

ARE YOU SURE?

Sometimes, the text of the question will include, within parentheses, the different allowable responses that you can make to that question.

ARE YOU SURE (Y/N)?

### Default Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes the question that the computer is asking has a standard expected answer. This is known as the default response. In order to save you the trouble of typing the most probable answer, the computer provides the answer followed with a double slash //. Either you enter nothing (also known as a null response) by pressing the Return key to accept the default response as your answer, or you can type a different response.

IS IT OKAY TO DELETE? NO//

### Invalid Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer software checks each answer immediately after it is entered. Whenever the computer determines that an answer is invalid for any reason, it usually beeps, displays two questions marks, and repeats the question on a new line.

### LAYGO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA software checks your answers against an internally stored table of valid answers. If your answer is not stored in this table but the Learn-As-You-GO (LAYGO) mode is allowed, the computer adds your response as one of those valid answers.

### Entering Dates and Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the acceptable answer to a question is a date, use the following answer formats. Note that the response is not case sensitive; upper or lower case input is acceptable.

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

The year portion of the date can be left off; normally the system will assume current year. Occasionally, the software will allow you to enter a time-of-day in connection with a date, for example, 4:00 <span class="smallcaps">p.m.</span> on July 20, 1994. To do this, type the date in one of the above forms followed by an at sign @, followed by the time. For example, you might enter:

20 JUL 94@4PM

In this mode, you can enter time either as military (four digit) time, hour AM/PM, or hour:minute:second AM/PM, or simply NOW (or Now or now) for the current date/time.

The colon : can be omitted. AM/PM can also be omitted if the time being entered is between 6 <span class="smallcaps">a.m.</span> and 6 <span class="smallcaps">p.m.</span> Thus, today at 3:30 <span class="smallcaps">p.m.</span> can be entered as:

T@330

Use MID as a response to mean 12:00 <span class="smallcaps">a.m.</span> (midnight) and NOON as a response to mean 12:00 <span class="smallcaps">p.m.</span> for time associated with dates.

T+3W@MID

### Making Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you want to delete an answer previously entered without substituting any other answer, enter an at sign @ as a response to that prompt. This leaves the answer blank.

DATE OF BIRTH: May 21, 1946//@

In this example, the date on file has been erased and now there is no answer to the "DATE OF BIRTH" prompt; it is null.

The system will ask you to confirm that you really intend to delete the information.

> **NOTE:** You may not be able to delete a response if the information is required.

ARE YOU SURE?

This question is a safety feature, giving you a chance to change your mind now, without re-editing later.

### Spacebar Recall Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using this software, you might want to answer a prompt with a code meaning *the same as before*. For prompts that ask you to select one of several existing entries, the computer is capable of remembering what your last response was the last time you answered the same prompt. This feature is called spacebar recall and employs the spacebar and Return keys. Different hardware and software configurations support this feature to different degrees.

You generally can repeat information you entered the last time you responded to this prompt by entering a space and pressing the Return or Enter key. For example, you might wish to do a series of procedures for one patient. Each time (after the first), you are asked for the patient’s name, you can enter a space and press the Return key and the computer will enter the same patient. The example below assumes that the user entered 5EAST at the last Select WARD: prompt.

Select WARD: \<space\>\<return\> 5EAST

# Beneficiary Travel Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is an overview of the BT menu and option structure as it appears to users, followed by a summary of each option.

-------------------------------------------------------------------------------------------------

 

          Report of Claim Amounts

          View of Claim

   RPTS   Beneficiary Travel Reports ...

----------------------------------------------------------------------------------

 

## Beneficiary Travel Reports Submenu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-------------------------------------------------------------------------------------------------

SUM     Summary Report

AUD     Audit Report

CL         Clerk Report

PAT       Travel Pattern Report

SP          Special Mode Report

FISC      Fiscal Report

-------------------------------------------------------------------------------------------------

## Summary of Main Menu items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REPORT OF CLAIM AMOUNTS

> The Report of Claim Amounts option allows the user to print a variety of statistical reports for a specified date range.

> VIEW OF CLAIM

> This option allows the user to review a previously entered travel claim for a patient.

> BENEFICIARY TRAVEL REPORTS…

> The Beneficiary Travel Reports option allows the user to access a sub-menu of report options. These reports can be displayed, printed, or exported as text files.

## Summary of Reports Sub-Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SUMMARY REPORT

> The Summary Report option allows the user to print a total report for either Special Mode or Mileage claims to be used for reporting metrics and planning purposes. This report can also be exported as a text file for import into other software.

> AUDIT REPORT

> The Audit Report option allows the user to print a full report of Mileage claims to be used by the CBO for aggregation for National reporting metrics. This report can also be exported as a text file for import into other software.

> CLERK REPORT

> The Clerk Report option allows the user to print either a full or total report for either Special Mode or Mileage claims based on entry clerk. This report can also be exported as a text file for import into other software.

> TRAVEL PATTERN REPORT

> The Travel Pattern Report option allows the user to print a full report of Mileage claims to be used to analyze mileage travel patterns. This report can also be exported as a text file for import into other software.

> SPECIAL MODE REPORT

> The Special Mode Report option allows the user to print either a full or total report of Special Mode claims for a specified date range. This report can also be exported as a text file for import into other software.

> FISCAL REPORT

> The Fiscal Report option allows the user to print a sub-set of the fields on the 70-3542d Voucher form for a specified date range. This report can also be exported as a text file for import into other software.

## Beneficiary Travel Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of EAS\*1\*113 and Informational Patch DGBT\*1\*29, the ES HL7 ORU-Z06 message sends the BT Financial Indicator (BTFI) to VistA in the ZMT-31 segment-sequence. The BTFI is stored to the BT FINANCIAL INDICATOR (#4) field of the ANNUAL MEANS TEST (#408.31) file. The new BT Financial Indicator (BTFI) is displayed on the Means Test and Copay Test overview screens. The BTFI will be sent from the Enrollment System and shared with all sites of record when the Income Verification Matching (IVM) application has performed a conversion and/or reversal on an income test where the Veteran had a BT award prior to the IVM action. A BT CLAIMS PROCESSING mail group is automatically created in VistA to receive the BT Bulletin named EAS BT CLAIMS PROCESSING when an IVM income test is uploaded resulting in a change to the BT Financial Indicator. Users who validate BT eligibility based on income or process BT claims should be added to the mail group.

When an IVM converted/reversal income test is received from ES, a check will be done to see if the BT Financial Indicator is different than the BT Financial Indicator on file, (e.g. the new Financial Indicator is 1 (YES) and the BT Financial Indicator on File is 0 (No),or the new status is 0 (NO) and the BT Financial Indicator on File is 1 (Yes) or a null). If the BT Financial Indicator has changed, a bulletin will be sent to the BT CLAIMS PROCESSING Mail group.

The bulletin will contain the following information:

Mail Message From: Health Eligibility Center Date: MM/DD/YYYY HH:MM

Subject: IVM-Beneficiary Travel Financial Indicator upload FOR\<DFN\>

An Income Verification Match verified Beneficiary Travel information

has been uploaded for the following patient.

Patient Name: BTPATIENT,ONE

LAST 4 OF SSN: XXXX

ICN: XXXXXXXXXXVXXXXXX

DFN: XXXXXX

STATION NUMBER: 988

Prev Category: EXEMPT

New Category: NON-EXEMPT

Date of Test: 05/14/2014

Income Year of Conversion: 2013

The BT Financial Indicator may be viewed on the Means Test or RX Copay Test summary screen using the View a Past Means Test \[DG MEANS TEST VIEW TEST\] or View a Past Copay Test \[DG CO-PAY TEST VIEW TEST\] options respectively.

Select DATE OF TEST: 5-9-2015// MEANS TEST MT COPAY REQUIRED IVM PRIMARY

Patient: REGPATIENT,ONE Date of Test: MAY 09, 2015

Total Dependents: 0 Type Of Test: MEANS TEST

Status: MT COPAY REQUIRED Date/Time Completed: JAN 06, 2015

Primary Test For Year: YES Source Of Test: IVM

Income: Completed By:

Net Worth: Date/Time Category Changed: JAN 26, 2015@08

Deductible Expenses: Category Changed By:

Agreed to Pay Deduct.: YES Adjudicated Date/Time:

Declines Income Info: No Longer Required Date:

MT Threshold: \$30978

GMT Threshold: BT Financial Indicator: YES

Date Vet Signed Test:

Means Test Signed?:

Refused to Sign:

Date IVM MT Completed: FEB 06, 2015

COMMENT(S):

Z06 MT via Edb

\*\* DETAILED MEANS TEST INCOME INFORMATION IS NOT AVAILABLE \*\*

# User Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## View of Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The View of Claim option is used to review a previously entered travel claim for a patient. Once the patient name has been entered, all the travel claim dates/times for that patient will be automatically listed for selection.

> The Beneficiary Travel Claim Information Display screen will be shown for the selected claim. Some of the data items displayed may include: patient's name, social security number, date of birth, eligibility; "depart from" and "to" addresses; whether claim is for one-way or round-trip mileage; cost of meals, ferry, bridges, lodging; account type, and amount payable.

> This option is used for viewing only. Claims may not be entered or edited here.

Example 1: VIEWING A CLAIM

> **NOTE:** In this example, the patient has a denied claim on July 15. This is indicated by the (D) next to the claim date.

Select Beneficiary Travel Menu Option: view of Claim

Select PATIENT NAME: DGBTPATIENT,TESTING A

DGBTPATIENT,TESTING A 5-4-50 0450P \*\*Pseudo SSN\*\*

YES SC VETERAN

Enrollment Priority: GROUP 3 Category: IN PROCESS End Date: 10/31/2011

Select Claim DATE/TIME:

1\. JUL 29,2012@22:04

2\. JUL 29,2012@19:54

3\. JUL 15,2012@11:45 (D)

4\. JUL 13,2012@17:04

5\. JUL 13,2012@15:26

Type '^' to Stop, or

Choose 1-5: 1 JUL 29,2012@22:04

Beneficiary Travel Claim Information \<Display\>

Claim Date: JUL 29,2012@22:04 Division: DBA

Name: DGBTPATIENT,TESTING A PT ID: 0450P DOB: MAY 4,1950

Depart From: 2821 ANYWHERE STREET To: 1ALBANY

LATHAM, NY 12110 33384 88TH ST

ALBANY, NY 12112

Eligibility: SC LESS THAN 50% SC%: 0

Account: 826 SPECIAL MODE - NON-EMERGENT

Mode/Trans: WHEELCHAIR VAN One Way/Round Trip: ONE WAY

Carrier: VENDOR \#1 Total Miles Traveled: 24.00

Invoice: 232 Base Rate Fee: \$1.00

Date Received: JUL 29, 2012 Mileage Fee: \$1.00

Pre-Authorized: YES No-Show/No Load Fee: \$0.00

Payment: APPROVED Wait Time Fee: \$0.00

Auth. Person: BRODNY,PAVEL B Extra Crew Fee: \$0.00

Equipment Fee: \$0.00

Total Invoice Amount: \$2.00

Remarks:

## Beneficiary Travel Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Submenu: RPTS Beneficiary Travel Reports

> Reporting capabilities provided by the BT system allow users to do the following:

- Run any report manually on demand
- Specify the timeframe for the data to be included in the report
- Export results from any report into Microsoft Excel
- Print or queue any report to a facility printer

The report selection criteria will be Start and End Dates based on Claim entry date. Start and End names will be based on the Veteran’s last name with a default of AAA and ZZZ. Depending on the type of report they can be run as Mileage or Special Mode reports. Another criteria will be the detail level of Full or Total.

RPTS     Beneficiary Travel Reports ...

---------------------------------------------------------------------------------------------------------------

SUM     Summary Report

AUD     Audit Report

CL         Clerk Report

PAT       Travel Pattern Report

SP          Special Mode Report

FISC      Fiscal Report

------------------------------------------------------------------------------------------------------------------------

### Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > The Summary Report provides statistical totals for analysis of facility BT funds expended, claims processed, claim denials, alternate transportation usage, and Veteran eligibility demographics during a specified timeframe.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Summary Report option allows the user to print a total report for either Special Mode or Mileage claims to be used for reporting metrics and planning purposes. This report can also be exported as a text file for import into other software.

Input Data:

Start Date

End Date

Type of Report:

Excel document:

Expected Output:

Display version for monitor or printer, or text file to import into Excel

Example 1: SUMMARY MILEAGE REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: SUM Summary Report

START DATE: T-55 (JUN 05, 2012)

END DATE: T (JUL 30, 2012)

Select one of the following:

M MILEAGE

S SPECIAL MODE

Which claim type do you want to run?: MILEAGE

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

BT SUMMARY REPORT PRINT DATE: JUL 30, 2012@01:16:57 PAGE 1

Jun 05, 2012 TO Jul 30, 2012

CLAIM TYPE: MILEAGE

DIVISION: DBA

==========================================================================================================================

DIVISION ENTERED ACCT CLAIMS MILEAGE CC FEE MOST ECON M&L F&B

DED PAYABLE

==========================================================================================================================

DBA Jun 07, 2012 829 1 22 \$0.00 \$11.00 \$21.00 \$32.00

\$6.00 \$26.00

DBA Jun 11, 2012 829 2 12 \$333.00 \$10.00 \$20.00 \$30.00

\$0.42 \$30.00

DBA Jun 20, 2012 829 4 700 \$0.00 \$0.00 \$0.00 \$0.00

\$24.00 \$266.50

DBA Jun 22, 2012 829 1 45 \$0.00 \$0.00 \$0.00 \$0.00

\$3.00 \$15.68

DBA Jul 01, 2012 829 1 200 \$0.00 \$0.00 \$0.00 \$0.00

\$3.00 \$77.00

DBA Jul 02, 2012 829 1 400 \$0.00 \$0.00 \$0.00 \$0.00

\$6.00 \$160.00

DBA Jul 05, 2012 829 2 100 \$0.00 \$0.00 \$0.00 \$0.00

\$6.00 \$35.50

DBA Jul 10, 2012 829 1 10 \$0.00 \$0.00 \$10.00 \$0.00

\$3.00 \$11.15

Please press return to continue or '^' to stop

BT SUMMARY REPORT PRINT DATE: JUL 30, 2012@01:16:57 PAGE 2

Jun 05, 2012 TO Jul 30, 2012

CLAIM TYPE: MILEAGE

DIVISION: DBA

==========================================================================================================================

DIVISION ENTERED ACCT CLAIMS MILEAGE CC FEE MOST ECON M&L F&B

DED PAYABLE

==========================================================================================================================

DBA Jul 11, 2012 829 1 6 \$0.00 \$0.00 \$0.00 \$0.00

\$2.49 \$0.00

DBA Jul 13, 2012 829 3 141 \$0.00 \$0.00 \$0.00 \$0.00

\$12.42 \$46.10

DBA Jul 15, 2012 829 1 200 \$50.00 \$26.00 \$0.00 \$0.00

\$0.00 \$26.00

DBA Jul 24, 2012 829 2 60 \$57.85 \$72.50 \$58.00 \$54.00

\$0.00 \$98.65

DBA Jul 25, 2012 829 3 66 \$20.00 \$0.00 \$0.00 \$0.00

\$7.66 \$19.73

DBA Jul 29, 2012 829 1 11 \$0.00 \$12.00 \$0.00 \$4.00

\$0.00 \$8.57

BT SUMMARY REPORT PRINT DATE: JUL 30, 2012@01:16:57 PAGE 3

Jun 05, 2012 TO Jul 30, 2012

CLAIM TYPE: MILEAGE

DIVISION: DBA

==========================================================================================================================

DIVISION ENTERED ACCT CLAIMS MILEAGE CC FEE MOST ECON M&L F&B

DED PAYABLE

==========================================================================================================================

==========================================================================================================================

CLAIMS MILEAGE CC FEE MOST ECON M&L F&B

DED PAYABLE

24 1973 \$460.85 \$131.50 \$109.00 \$120.00

\$73.99 \$820.88

==========================================================================================================================

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP...

  
Example 2: SUMMARY MILEAGE REPORT FOR EXPORT TO EXCEL

Select Beneficiary Travel Reports Option: Select Beneficiary Travel Reports Option: SUM Summary Report

START DATE: T-55 (JUN 05, 2012)

END DATE: T (JUL 30, 2012)

Select one of the following:

M MILEAGE

S SPECIAL MODE

Which claim type do you want to run?: MILEAGE

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// 0;512;999 VIRTUAL TELNET

DATE ENTERED^DIVISION^ACCT^# CLAIMS^MILEAGE^CC FEE^MOST ECONOMIC^M & L^FERRIES AND BRIDGES^DEDUCTIBLE^AMOUNT PAYABLE

Jun 07, 2012^DBA^829^1^22^0.00^11.00^21.00^32.00^6.00^26.00

Jun 11, 2012^DBA^829^2^12^333.00^10.00^20.00^30.00^0.42^30.00

Jun 20, 2012^DBA^829^4^700^0.00^0.00^0.00^0.00^24.00^266.50

Jun 22, 2012^DBA^829^1^45^0.00^0.00^0.00^0.00^3.00^15.68

Jul 01, 2012^DBA^829^1^200^0.00^0.00^0.00^0.00^3.00^77.00

Jul 02, 2012^DBA^829^1^400^0.00^0.00^0.00^0.00^6.00^160.00

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Audit Report provides information to audit claims for accuracy. The Audit Report option allows the user to print a full report of Mileage claims to be used by the CBO for aggregation for National reporting metrics. This report can also be exported as a text file for import into other software. These reports are wider than normal reports and the right margin will need to be increased to 255 characters.

Input Data:

Start Date

End Date

Start Name

End Name

Excel document:

Expected Output:

> Display version for monitor or printer, or text file to import into Excel

Example 1: AUDIT REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: AUD Audit Report

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Audit Report \*\*\*\*\*\*\*\*\*\*\*\*\*

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME : AAA//

END NAME : ZZZ//

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 255 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 255

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Audit Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 1

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DATE ENT CLAIM DATE PATIENT NAME SSN ELIG SC % ACCT R/O MILEAGE CC MODE CC FEE ECON DED PAYABLE DEP ADDRESS DEP CITY DEP STATE DEP ZIP DIV REMARKS

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

07/01/12 06/29/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 200 \$0.00 \$0.00 \$3.00 \$77.00 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/02/12 07/02/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 400 \$0.00 \$0.00 \$6.00 \$160.00 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/05/12 05/03/12 DGBTPATIENT,THREE 702-03-2470P SC LESS THAN 50% 35 829 R 50 \$0.00 \$0.00 \$6.00 \$14.75 832 NOWHERE ST LATHAM NEW YORK 12110 DBA

07/05/12 07/05/12 DGBTPATIENT,THREE 702-03-2470P SC LESS THAN 50% 35 829 R 50 \$0.00 \$0.00 \$0.00 \$20.75 832 NOWHERE ST LATHAM NEW YORK 12110 DBA

07/10/12 07/10/12 DGBTTEST,EIGHTEEN 202-09-1687P NSC 829 O 10 \$0.00 \$0.00 \$3.00 \$11.15 762 SUSETTA LAKELAND FLORIDA 33801 DBA

07/11/12 07/11/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 6 \$0.00 \$0.00 \$2.49 \$0.00 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/13/12 07/12/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 40 \$0.00 \$0.00 \$6.00 \$10.60 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

PRESS RETURN TO CONTINUE OR '^' TO STOP

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Audit Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 2

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DATE ENT CLAIM DATE PATIENT NAME SSN ELIG SC % ACCT R/O MILEAGE CC MODE CC FEE ECON DED PAYABLE DEP ADDRESS DEP CITY DEP STATE DEP ZIP DIV REMARKS

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

07/13/12 07/13/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 100 \$0.00 \$0.00 \$6.00 \$35.50 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/13/12 07/13/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 O 1 \$0.00 \$0.00 \$0.42 \$0.00 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/15/12 07/15/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 R 200 TAXI \$50.00 \$26.00 \$0.00 \$26.00 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA

07/24/12 05/10/12 DGBTTEST,EIGHT 202-09-2787P HOUSEBOUND 829 R 10 AIRPLANE \$22.00 \$55.00 \$0.00 \$81.15 48 CENTRAL AVE DOVER NEW HAMPSHIRE 03820 DBA

07/24/12 07/15/12 DGBTPATIENT,POW 602-01-0160P SC LESS THAN 50% 829 R 50 TAXI \$35.85 \$17.50 \$0.00 \$17.50 123 OAK ST LATHAM NEW YORK 12110 DBA

07/25/12 07/11/12 DGBTTEST,GOOFY 000-00-2650P SC LESS THAN 50% 829 R 60 \$0.00 \$0.00 \$6.00 \$18.90 DBA

07/25/12 07/18/12 DGBTTEST,GOOFY 000-00-2650P SC LESS THAN 50% 829 R 4 \$0.00 \$0.00 \$1.66 \$0.00 DBA

PRESS RETURN TO CONTINUE OR '^' TO STOP

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Audit Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 3

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DATE ENT CLAIM DATE PATIENT NAME SSN ELIG SC % ACCT R/O MILEAGE CC MODE CC FEE ECON DED PAYABLE DEP ADDRESS DEP CITY DEP STATE DEP ZIP DIV REMARKS

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

07/25/12 07/19/12 DGBTTEST,GOOFY 000-00-2650P SC LESS THAN 50% 829 O 2 TAXI \$20.00 \$0.00 \$0.00 \$0.83 DBA

07/29/12 07/29/12 DGBTPATIENT,TESTING A 000-00-0450P SC LESS THAN 50% 10 829 O 11 \$0.00 \$12.00 \$0.00 \$8.57 2821 ANYWHERE STREE LATHAM NEW YORK 12110 DBA This is a test for Mileage typ

e Patient

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP....

> Example 2: AUDIT REPORT FOR EXPORT TO EXCEL

Select Beneficiary Travel Reports Option: AUD Audit Report

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Audit Report \*\*\*\*\*\*\*\*\*\*\*\*\*

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME : AAA//

END NAME : ZZZ//

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 255

DATE ENTERED^CLAIM DATE^PATIENT NAME^SSN^ELIGIBILITY^SC PERCENTAGE^ACCOUNT^R/O^MILES^CC MODE^CC FEE^MOST ECONOMICAL^DEDUCTIBLE AMOUNT^AMOUNT PAYABLE^PLACE OF DEPARTURE^CITY OF DEPARTURE^STATE OF DEPARTURE^ZIP CODE OF DEPARTURE^DIVISION^REMARKS

07/01/12^06/29/12^DGBTPATIENT,TESTING A^000-00-0450P^SC LESS THAN 50%^10^829^R^200^^0.00^0.00^3.00^77.00^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^DBA^

07/05/12^07/05/12^DGBTPATIENT,THREE^702-03-2470P^SC LESS THAN 50%^35^829^R^50^^0.00^0.00^0.00^20.75^832 NOWHERE ST^LATHAM^NEW YORK^12110^DBA^

07/10/12^07/10/12^DGBTTEST,EIGHTEEN^202-09-1687P^NSC^^829^O^10^^0.00^0.00^3.00^11.15^762 SUSETTA^LAKELAND^FLORIDA^33801^DBA^

07/11/12^07/11/12^DGBTPATIENT,TESTING A^000-00-0450P^SC LESS THAN 50%^10^829^R^6^^0.00^0.00^2.49^0.00^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^DBA^

07/24/12^05/10/12^DGBTTEST,EIGHT^202-09-2787P^HOUSEBOUND^^829^R^10^AIRPLANE^22.00^55.00^0.00^81.15^48 CENTRAL AVE^DOVER^NEW HAMPSHIRE^03820^DBA^

07/24/12^07/15/12^DGBTPATIENT,POW^602-01-0160P^SC LESS THAN 50%^^829^R^50^TAXI^35.85^17.50^0.00^17.50^123 OAK ST^LATHAM^NEW YORK^12110^DBA^

07/25/12^07/11/12^DGBTTEST,GOOFY^000-00-2650P^SC LESS THAN 50%^^829^R^60^^0.00^0.00^6.00^18.90^^^^^DBA^

07/25/12^07/18/12^DGBTTEST,GOOFY^000-00-2650P^SC LESS THAN 50%^^829^R^4^^0.00^0.00^1.66^0.00^^^^^DBA^

07/25/12^07/19/12^DGBTTEST,GOOFY^000-00-2650P^SC LESS THAN 50%^^829^O^2^TAXI^20.00^0.00^0.00^0.83^^^^^DBA^

07/29/12^07/29/12^DGBTPATIENT,TESTING A^000-00-0450P^SC LESS THAN 50%^10^829^O^11^^0.00^12.00^0.00^8.57^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^DBA^This is a test for Mileage type Patient

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Clerk Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clerk Report retrieves information about claims entered by a specific BT clerk. The Clerk Report option allows the user to print either a full or total report for either Special Mode or Mileage claims based on entry clerk. This report can also be exported as a text file for import into other software.

Input Data:

Start Date

End Date

Type of Report:

All clerks:

Full/Total

Excel document:

Expected Output:

> Display version for monitor or printer, or text file to import into Excel

Example 1: CLERK REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: CL Clerk Report

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

Select one of the following:

M MILEAGE

S SPECIAL MODE

Which claim type do you want to run?: MILEAGE

Do you wish to run this report for all clerks? YES//

Select one of the following:

F FULL

T TOTAL

Which claim type do you want to run?: FULL

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 255

=================================================================================================================================

PATIENT NAME SSN CLERK CL DT ENT DT ACCT

DIVISION R/O MILEAGE CC MODE CC FEE ECON M&L

F&B DED PAYABLE REMARKS

=================================================================================================================================

DGBTPATIENT,TESTING A 000000450P DELLINGER,BARRY Jun 29, 2012 Jul 01, 2012 829

DBA R 200 \$0.00 \$0.00 \$0.00

\$0.00 \$3.00 \$77.00

DGBTPATIENT,TESTING A 000000450P DELLINGER,BARRY Jul 02, 2012 Jul 02, 2012 829

DBA R 400 \$0.00 \$0.00 \$0.00

\$0.00 \$6.00 \$160.00

DGBTPATIENT,THREE 702032470P DELLINGER,BARRY May 03, 2012 Jul 05, 2012 829

DBA R 50 \$0.00 \$0.00 \$0.00

\$0.00 \$6.00 \$14.75

DGBTPATIENT,THREE 702032470P DELLINGER,BARRY Jul 05, 2012 Jul 05, 2012 829

DBA R 50 \$0.00 \$0.00 \$0.00

\$0.00 \$0.00 \$20.75

BT CLERK REPORT PRINT DATE: JUL 30, 2012@01:57:43 PAGE 2

Jun 30, 2012 TO Jul 30, 2012

VERSION: FULL

TYPE: MILEAGE

DIVISION: DBA

CLERK: ALL

=================================================================================================================================

PATIENT NAME SSN CLERK CL DT ENT DT ACCT

DIVISION R/O MILEAGE CC MODE CC FEE ECON M&L

F&B DED PAYABLE REMARKS

=================================================================================================================================

DGBTTEST,EIGHTEEN 202091687P ENGLEBACH,ROB Jul 10, 2012 Jul 10, 2012 829

DBA O 10 \$0.00 \$0.00 \$10.00

\$0.00 \$3.00 \$11.15

DGBTPATIENT,TESTING A 502050450P BRODNY,PAVEL B Jul 11, 2012 Jul 11, 2012 829

DBA R 6 \$0.00 \$0.00 \$0.00

\$0.00 \$2.49 \$0.00

DGBTPATIENT,TESTING A 502050450P DELLINGER,BARRY Jul 12, 2012 Jul 13, 2012 829

DBA R 40 \$0.00 \$0.00 \$0.00

\$0.00 \$6.00 \$10.60

DGBTPATIENT,TESTING A 502050450P DELLINGER,BARRY Jul 13, 2012 Jul 13, 2012 829

DBA R 100 \$0.00 \$0.00 \$0.00

\$0.00 \$6.00 \$35.50

BT CLERK REPORT PRINT DATE: JUL 30, 2012@01:57:43 PAGE 3

Jun 30, 2012 TO Jul 30, 2012

VERSION: FULL

TYPE: MILEAGE

DIVISION: DBA

CLERK: ALL

=================================================================================================================================

PATIENT NAME SSN CLERK CL DT ENT DT ACCT

DIVISION R/O MILEAGE CC MODE CC FEE ECON M&L

F&B DED PAYABLE REMARKS

=================================================================================================================================

DGBTPATIENT,TESTING A 502050450P BRODNY,PAVEL B Jul 13, 2012 Jul 13, 2012 829

DBA O 1 \$0.00 \$0.00 \$0.00

\$0.00 \$0.42 \$0.00

DGBTPATIENT,TESTING A 502050450P DELLINGER,BARRY Jul 15, 2012 Jul 15, 2012 829

DBA R 200 TAXI \$50.00 \$26.00 \$0.00

\$0.00 \$0.00 \$26.00

DGBTTEST,EIGHT 202092787P DELLINGER,BARRY May 10, 2012 Jul 24, 2012 829

DBA R 10 AIRPLANE \$22.00 \$55.00 \$33.00

\$44.00 \$0.00 \$81.15

DGBTPATIENT,POW 602010160P DELLINGER,BARRY Jul 15, 2012 Jul 24, 2012 829

DBA R 50 TAXI \$35.85 \$17.50 \$25.00

\$10.00 \$0.00 \$17.50

BT CLERK REPORT PRINT DATE: JUL 30, 2012@01:57:43 PAGE 4

Jun 30, 2012 TO Jul 30, 2012

VERSION: FULL

TYPE: MILEAGE

DIVISION: DBA

CLERK: ALL

=================================================================================================================================

PATIENT NAME SSN CLERK CL DT ENT DT ACCT

DIVISION R/O MILEAGE CC MODE CC FEE ECON M&L

F&B DED PAYABLE REMARKS

=================================================================================================================================

DGBTTEST,GOOFY 302022650P DELLINGER,BARRY Jul 11, 2012 Jul 25, 2012 829

DBA R 60 \$0.00 \$0.00 \$0.00

\$0.00 \$6.00 \$18.90

DGBTTEST,GOOFY 302022650P DELLINGER,BARRY Jul 18, 2012 Jul 25, 2012 829

DBA R 4 \$0.00 \$0.00 \$0.00

\$0.00 \$1.66 \$0.00

DGBTTEST,GOOFY 302022650P DELLINGER,BARRY Jul 19, 2012 Jul 25, 2012 829

DBA O 2 TAXI \$20.00 \$0.00 \$0.00

\$0.00 \$0.00 \$0.83

DGBTPATIENT,TESTING A 502050450P BRODNY,PAVEL B Jul 29, 2012 Jul 29, 2012 829

DBA O 11 \$0.00 \$12.00 \$0.00

\$4.00 \$0.00 \$8.57 This is a test for Mileage type Patient

BT CLERK REPORT PRINT DATE: JUL 30, 2012@01:57:43 PAGE 5

Jun 30, 2012 TO Jul 30, 2012

VERSION: FULL

TYPE: MILEAGE

DIVISION: DBA

CLERK: ALL

===============================================================================================================================

GRAND TOTALS: CLAIMS MILEAGE CC FEE ECON M&L

F&B DED PAYABLE

16 1194 \$127.85 \$110.50 \$68.00

\$58.00 \$40.57 \$482.70

===============================================================================================================================

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP....

Example 2: CLERK REPORT FOR EXPORT TO EXCEL

Select Beneficiary Travel Reports Option: CL Clerk Report

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

Select one of the following:

M MILEAGE

S SPECIAL MODE

Which claim type do you want to run?: MILEAGE

Do you wish to run this report for all clerks? YES//

Select one of the following:

F FULL

T TOTAL

Which claim type do you want to run?: FULL

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 0;512;999 Right Margin:

80// ^

DEVICE: HOME// 0;512;9999 VIRTUAL TELNET

DATE ENTERED^PATIENT^PATIENT ID^CLERK^CLAIM DATE^DIVISION^ACCT^R/O^MILEAGE^CC MODE^CC FEE^MOST ECONOMIC^M & L^FERRIES & BRIDGES^DEDUCTIBLE^AMOUNT PAYABLE^REMARK

Jul 01, 2012^DGBTPATIENT,TESTING A^502050450P^DELLINGER,BARRY^Jun 29, 2012^DBA^829^R^200^^0.00^0.00^0.00^0.00^3.00^77.00^

Jul 02, 2012^DGBTPATIENT,TESTING A^502050450P^DELLINGER,BARRY^Jul 02, 2012^DBA^829^R^400^^0.00^0.00^0.00^0.00^6.00^160.00^

Jul 05, 2012^DGBTPATIENT,THREE^702032470P^DELLINGER,BARRY^May 03, 2012^DBA^829^R^50^^0.00^0.00^0.00^0.00^6.00^14.75^

Jul 05, 2012^DGBTPATIENT,THREE^702032470P^DELLINGER,BARRY^Jul 05, 2012^DBA^829^R^50^^0.00^0.00^0.00^0.00^0.00^20.75^

Jul 10, 2012^DGBTTEST,EIGHTEEN^202091687P^ENGLEBACH,ROB^Jul 10, 2012^DBA^829^O^10^^0.00^0.00^10.00^0.00^3.00^11.15^

Jul 11, 2012^DGBTPATIENT,TESTING A^502050450P^BRODNY,PAVEL B^Jul 11, 2012^DBA^829^R^6^^0.00^0.00^0.00^0.00^2.49^0.00^

Jul 13, 2012^DGBTPATIENT,TESTING A^502050450P^DELLINGER,BARRY^Jul 12, 2012^DBA^829^R^40^^0.00^0.00^0.00^0.00^6.00^10.60^

Jul 13, 2012^DGBTPATIENT,TESTING A^502050450P^DELLINGER,BARRY^Jul 13, 2012^DBA^829^R^100^^0.00^0.00^0.00^0.00^6.00^35.50^

Jul 13, 2012^DGBTPATIENT,TESTING A^502050450P^BRODNY,PAVEL B^Jul 13, 2012^DBA^829^O^1^^0.00^0.00^0.00^0.00^0.42^0.00^

Jul 15, 2012^DGBTPATIENT,TESTING A^502050450P^DELLINGER,BARRY^Jul 15, 2012^DBA^829^R^200^TAXI^50.00^26.00^0.00^0.00^0.00^26.00^

Jul 24, 2012^DGBTTEST,EIGHT^202092787P^DELLINGER,BARRY^May 10, 2012^DBA^829^R^10^AIRPLANE^22.00^55.00^33.00^44.00^0.00^81.15^

Jul 24, 2012^DGBTPATIENT,POW^602010160P^DELLINGER,BARRY^Jul 15, 2012^DBA^829^R^50^TAXI^35.85^17.50^25.00^10.00^0.00^17.50^

Jul 25, 2012^DGBTTEST,GOOFY^302022650P^DELLINGER,BARRY^Jul 11, 2012^DBA^829^R^60^^0.00^0.00^0.00^0.00^6.00^18.90^

Jul 25, 2012^DGBTTEST,GOOFY^302022650P^DELLINGER,BARRY^Jul 18, 2012^DBA^829^R^4^^0.00^0.00^0.00^0.00^1.66^0.00^

Jul 25, 2012^DGBTTEST,GOOFY^302022650P^DELLINGER,BARRY^Jul 19, 2012^DBA^829^O^2^TAXI^20.00^0.00^0.00^0.00^0.00^0.83^

Jul 29, 2012^DGBTPATIENT,TESTING A^502050450P^BRODNY,PAVEL B^Jul 29, 2012^DBA^829^O^11^^0.00^12.00^0.00^4.00^0.00^8.57^This is a test for Mileage type Patient

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Travel Pattern Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Travel Pattern Report will be used to analyze distance/location to Veteran claims for unique travel patterns. The Travel Pattern Report option allows the user to print a full report of Mileage claims to be utilized for the analysis of mileage travel patterns. This report can also be exported as a text file for import into other software.

Input Data:

Start Date

End Date

Start Name

End Name

Excel document:

Expected Output:

> Display version for monitor or printer/Text file to import into Excel

Example 1: TRAVEL PATTERN REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: PAT Travel Pattern Report

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Travel Pattern Report \*\*\*\*\*\*\*\*\*\*\*\*\*

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME : AAA//

END NAME : ZZZ//

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 255 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 255

> \*\*\*\*\*\*\*\*\*\*\*\*\* BT Travel Pattern Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 1

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CLAIM DATE PATIENT NAME SSN ACCT DEP ADDRESS DEP CITY DEP STATE DEP ZIP R/O MILEAGE PAYABLE CLERK REMARKS

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------06/29/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 200 \$77.00 DELLINGER,BARRY

07/02/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 400 \$160.00 DELLINGER,BARRY

05/03/12 DGBTPATIENT,THREE 702-03-2470P 829 832 NOWHERE ST LATHAM NEW YORK 12110 R 50 \$14.75 DELLINGER,BARRY

07/05/12 DGBTPATIENT,THREE 702-03-2470P 829 832 NOWHERE ST LATHAM NEW YORK 12110 R 50 \$20.75 DELLINGER,BARRY

07/10/12 DGBTTEST,EIGHTEEN 202-09-1687P 829 762 SUSETTA LAKELAND FLORIDA 33801 O 10 \$11.15 ENGLEBACH,ROB

07/11/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 6 \$0.00 BRODNY,PAVEL B

07/12/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 40 \$10.60 DELLINGER,BARRY

PRESS RETURN TO CONTINUE OR '^' TO STOP

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Travel Pattern Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 2

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CLAIM DATE PATIENT NAME SSN ACCT DEP ADDRESS DEP CITY DEP STATE DEP ZIP R/O MILEAGE PAYABLE CLERK REMARKS

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

07/13/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 100 \$35.50 DELLINGER,BARRY

07/13/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 O 1 \$0.00 BRODNY,PAVEL B

07/15/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 R 200 \$26.00 DELLINGER,BARRY

05/10/12 DGBTTEST,EIGHT 202-09-2787P 829 48 CENTRAL AVE DOVER NEW HAMPSHIRE 03820 R 10 \$81.15 DELLINGER,BARRY

07/15/12 DGBTPATIENT,POW 602-01-0160P 829 123 OAK ST LATHAM NEW YORK 12110 R 50 \$17.50 DELLINGER,BARRY

07/11/12 DGBTTEST,GOOFY 000-00-2650P 829 R 60 \$18.90 DELLINGER,BARRY

07/18/12 DGBTTEST,GOOFY 000-00-2650P 829 R 4 \$0.00 DELLINGER,BARRY

PRESS RETURN TO CONTINUE OR '^' TO STOP

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Travel Pattern Report 06/30/12-07/30/12 \*\*\*\*\*\*\*\*\*\*\*\*\* Page: 3

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CLAIM DATE PATIENT NAME SSN ACCT DEP ADDRESS DEP CITY DEP STATE DEP ZIP R/O MILEAGE PAYABLE CLERK REMARKS

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

07/19/12 DGBTTEST,GOOFY 000-00-2650P 829 O 2 \$0.83 DELLINGER,BARRY

07/29/12 DGBTPATIENT,TESTING A 000-00-0450P 829 2821 ANYWHERE STREE LATHAM NEW YORK 12110 O 11 \$8.57 BRODNY,PAVEL B This is a test for Mileage type Patient

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP....

Example 2: TRAVEL PATTERN REPORT FOR EXPORT TO EXCEL

> **NOTE:** In this example, the Device options 0;512;999 will be selected for exporting to an Excel file. 512 is the margin width and 999 is the page length.

Select Beneficiary Travel Reports Option: PAT Travel Pattern Report

\*\*\*\*\*\*\*\*\*\*\*\*\* BT Travel Pattern Report \*\*\*\*\*\*\*\*\*\*\*\*\*

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME : AAA//

END NAME : ZZZ//

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// 0;512;999

CLAIM DATE^PATIENT NAME^SSN^ACCOUNT^PLACE OF DEPARTURE^CITY OF DEPARTURE^STATE OF DEPARTURE^ZIP CODE OF DEPARTURE^R/O^MILES^AMOUNT PAYABLE^WHO ENTERED INTO FILE^REMARKS

06/29/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^200^77.00^DELLINGER,BARRY^

07/02/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^400^160.00^DELLINGER,BARRY^

05/03/12^DGBTPATIENT,THREE^702-03-2470P^829^832 NOWHERE ST^LATHAM^NEW YORK^12110^R^50^14.75^DELLINGER,BARRY^

07/05/12^DGBTPATIENT,THREE^702-03-2470P^829^832 NOWHERE ST^LATHAM^NEW YORK^12110^R^50^20.75^DELLINGER,BARRY^

07/10/12^DGBTTEST,EIGHTEEN^202-09-1687P^829^762 SUSETTA^LAKELAND^FLORIDA^33801^O^10^11.15^ENGLEBACH,ROB^

07/11/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^6^0.00^BRODNY,PAVEL B^

07/12/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^40^10.60^DELLINGER,BARRY^

07/13/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^100^35.50^DELLINGER,BARRY^

07/13/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^O^1^0.00^BRODNY,PAVEL B^

07/15/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^R^200^26.00^DELLINGER,BARRY^

05/10/12^DGBTTEST,EIGHT^202-09-2787P^829^48 CENTRAL AVE^DOVER^NEW HAMPSHIRE^03820^R^10^81.15^DELLINGER,BARRY^

07/15/12^DGBTPATIENT,POW^602-01-0160P^829^123 OAK ST^LATHAM^NEW YORK^12110^R^50^17.50^DELLINGER,BARRY^

07/11/12^DGBTTEST,GOOFY^000-00-2650P^829^^^^^R^60^18.90^DELLINGER,BARRY^

07/18/12^DGBTTEST,GOOFY^000-00-2650P^829^^^^^R^4^0.00^DELLINGER,BARRY^

07/19/12^DGBTTEST,GOOFY^000-00-2650P^829^^^^^O^2^0.83^DELLINGER,BARRY^

07/29/12^DGBTPATIENT,TESTING A^000-00-0450P^829^2821 ANYWHERE STREET^LATHAM^NEW YORK^12110^O^11^8.57^BRODNY,PAVEL B^This is a test for Mileage type Patient

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Special Mode Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Special Mode Report will be used to analyze information on Special Mode claims. The Special Mode Report option allows the user to print either a full or total report of Special Mode claims for a specified date range. This report can also be exported as a text file for import into other software.

Input Data:

Start Date

End Date

Start Name

End Name

Type of Report:

Excel document:

Expected Output:

> Display Version for monitor or printer/Text file to import into excel

Example 1: SPECIAL MODE REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: SP Special Mode Report

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME: AAA//

END NAME: ZZZ//

Select one of the following:

F FULL

T TOTAL

Which claim type do you want to run?: FULL

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

BT SPECIAL MODE FULL REPORT PRINT DATE: JUL 30, 2012@02:17:23 PAGE 1

Jun 30, 2012 TO Jul 30, 2012

FIRST VETERAN NAME: AAA

LAST VETERAN NAME: ZZZ

DIVISION: DBA

================================================================================================================================

PATIENT NAME CLAIM DATE MODE INV \# INVOICE DATE

R/O MILES BASE RATE MILEAGE NSNL WAIT FEE EXT CREW SPEC EQ INV AMT ENTRY DATE

DIVISION VENDOR STATUS

================================================================================================================================

DGBTPATIENT,TESTING A Jul 03, 2012 ALS AMBULANCE 8484 Jul 03, 2012

R 25 \$200.00 \$50.00 \$0.00 \$0.00 \$0.00 \$0.00 \$250.00 Jul 03, 2012

DBA VENDOR \#1

DGBTPATIENT,THREE Jul 05, 2012 ALS AMBULANCE 8833 Jul 05, 2012

R 25 \$200.00 \$50.00 \$0.00 \$0.00 \$0.00 \$0.00 \$250.00 Jul 05, 2012

DBA VENDOR \#1

DGBTPATIENT,TESTING A Jul 11, 2012 BLS AMBULANCE 123 Jul 11, 2012

O 20 \$1.00 \$1.00 \$0.00 \$0.00 \$0.00 \$0.00 \$2.00 Jul 11, 2012

DBA VENDOR \#1

DGBTPATIENT,TESTING A Jul 29, 2012 WHEELCHAIR VAN 232 Jul 29, 2012

R 24 \$1.00 \$1.00 \$0.00 \$0.00 \$0.00 \$0.00 \$2.00 Jul 29, 2012

DBA VENDOR \#1

BT SPECIAL MODE FULL REPORT PRINT DATE: JUL 30, 2012@02:17:23 PAGE 2

Jun 30, 2012 TO Jul 30, 2012

FIRST VETERAN NAME: AAA

LAST VETERAN NAME: ZZZ

DIVISION: DBA

================================================================================================================================

GRAND TOTALS: MILES BASE RATE MILEAGE NSNL WAIT FEE EXT CREW SPEC EQ INV AMT CLAIMS

94 \$402.00 \$102.00 \$0.00 \$0.00 \$0.00 \$0.00 \$504.00 4

================================================================================================================================

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP....

Example 2: SPECIAL MODE REPORT FOR EXPORT TO EXCEL

Select Beneficiary Travel Reports Option: SP Special Mode Report

START DATE: T-30 (JUN 30, 2012)

END DATE: T (JUL 30, 2012)

START NAME: AAA//

END NAME: ZZZ//

Select one of the following:

F FULL

T TOTAL

Which claim type do you want to run?: FULL

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// 0;512;999 VIRTUAL TELNET

ENTRY DATE^PATIENT^CLAIM DATE^CC MODE^INV \#^INV DT^R/O^MILES^BASE RATE^MILE FEE^NO SHOW NO LOAD^WAIT TIME^EXTRA CREW^SPECIAL EQUIPMENT^INV AMT^DIVISION^VENDOR^STATUS

Jul 03, 2012^DGBTPATIENT,TESTING A^Jul 03, 2012^ALS AMBULANCE^8484^Jul 03, 2012^R^25^200.00^50.00^0.00^0.00^0.00^0.00^250.00^DBA^VENDOR \#1^

Jul 05, 2012^DGBTPATIENT,THREE^Jul 05, 2012^ALS AMBULANCE^8833^Jul 05, 2012^R^25^200.00^50.00^0.00^0.00^0.00^0.00^250.00^DBA^VENDOR \#1^

Jul 11, 2012^DGBTPATIENT,TESTING A^Jul 11, 2012^BLS AMBULANCE^123^Jul 11, 2012^O^20^1.00^1.00^0.00^0.00^0.00^0.00^2.00^DBA^VENDOR \#1^

Jul 29, 2012^DGBTPATIENT,TESTING A^Jul 29, 2012^WHEELCHAIR VAN^232^Jul 29, 2012^R^24^1.00^1.00^0.00^0.00^0.00^0.00^2.00^DBA^VENDOR \#1^

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Fiscal Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Fiscal Report has been added under the Beneficiary Travel Reports (RPTS) section named Fiscal Report (FISC) of the Beneficiary Travel Menu which allows a user to generate a report of voucher information for a selected facility and a specified date range.

Input Data:

Start Date

End Date

Excel document:

Expected Output:

Display Version for monitor or printer/Text file to import into excel

Example 1: FISCAL REPORT DISPLAYED

Select Beneficiary Travel Menu Option: RPTS Beneficiary Travel Reports

Select Beneficiary Travel Reports Option: FISC Fiscal Report

START DATE: T-10 (JUL 20, 2012)

END DATE: T (JUL 30, 2012)

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

BT ELECTRONIC VOUCHER REPORT PRINT DATE: JUL 30, 2012@02:33:24 PAGE 1

Jul 20, 2012 TO Jul 30, 2012

DIVISION: DBA

===============================================================================================================================

NAME SSN CLAIM DATE ENTRY DATE CLERK ACCT

ADDRESS

CITY ST ZIP FACILITY

FACILITY ADDRESS

DEPARTURE

DEPARTURE

DESTINATION

DESTINATION

MILES RATE ALLOW M&L F&B TOTAL ECON TOTAL PAYABLE 1W RT DED CC FEE

REMARKS FISCAL SYMBOLS

===============================================================================================================================

DGBTTEST,EIGHT 202092787P May 10, 2012@16:09 JUL 24, 2012 DELLINGER,BARRY 829

48 CENTRAL AVE APT 4G

DOVER NH 03820 1ALBANY 33384 88TH ST

ALBANY NY 12112

48 CENTRAL AVE APT 4G

DOVER NH 03820

DBA 33384 88TH ST

ALBANY NY 12112

10 .415 \$4.15 \$33.00 \$44.00 \$81.15 \$55.00 \$88.00 \$81.15 0 0 \$0.00 \$22.00

PRESS RETURN TO CONTINUE OR '^' TO STOP....

===============================================================================================================================

GRAND TOTALS

MILES CLMS ALLOW M&L F&B TOTAL ECON TOTAL PAYABLE 1W RT DED CC FEE

137 6 \$56.86 \$58.00 \$58.00 \$172.86 \$84.50 \$142.50 \$126.95 0 8 \$34.15 \$77.85

===============================================================================================================================

REPORT HAS FINISHED, PRESS RETURN TO CONTINUE OR '^' TO STOP....

EXAMPLE 2: FISCAL REPORT FOR EXPORT TO EXCEL

Select Beneficiary Travel Reports Option: FISC Fiscal Report

START DATE: T-10 (JUL 20, 2012)

END DATE: T (JUL 30, 2012)

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data. On some terminals, this can be done by

clicking on the 'Tools' menu above, then click on 'Capture

Incoming Data' to save to Desktop. This report may take a

while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the

file, please enter '0;512;999' at the 'DEVICE:' prompt.

DEVICE: HOME// 0;512;999 VIRTUAL TELNET

NAME^ADD1^ADD2^CITY^STATE^ZIP^ID^FAC^DEP^DEST^MILES^M & L^TOTAL - 11^TOTAL - 13^CL DT^CERT^VOUCH DT^ACCOUNT^DED^CC FEE^PAYABLE

DGBTTEST,EIGHT^48 CENTRAL AVE^APT 4G^DOVER^NH^03820^202092787P^1ALBANY^03820^12112^10^33.00^81.15^88.00^May 10, 2012^DELLINGER,BARRY^JUL 24, 2012^829^0.00^22.00^81.15

DGBTTEST,GOOFY^^^^^^302022650P^1ALBANY^^12112^60^0.00^24.90^0.00^Jul 11, 2012^DELLINGER,BARRY^JUL 25, 2012^829^6.00^0.00^18.90

DGBTPATIENT,POW^123 OAK ST^APT 3G^LATHAM^NY^12110^602010160P^1ALBANY^12110^12112^50^25.00^55.75^42.50^Jul 15, 2012^DELLINGER,BARRY^JUL 24, 2012^829^0.00^35.85^17.50

DGBTTEST,GOOFY^^^^^^302022650P^1ALBANY^^12112^4^0.00^1.66^0.00^Jul 18, 2012^DELLINGER,BARRY^JUL 25, 2012^829^1.66^0.00^0.00

DGBTTEST,GOOFY^^^^^^302022650P^1ALBANY^^12112^2^0.00^0.83^0.00^Jul 19, 2012^DELLINGER,BARRY^JUL 25, 2012^829^0.00^20.00^0.83

DGBTPATIENT,TESTING A^2821 ANYWHERE STREET^^LATHAM^NY^12110^502050450P^1ALBANY^12110^12112^11^0.00^8.57^12.00^Jul 29, 2012^BRODNY,PAVEL B^JUL 29, 2012^829^0.00^0.00^8.57

REPORT HAS FINISHED, TURN OFF CAPTURE, THEN PRESS RETURN TO CONTINUE OR '^' TO STOP....

### Report of Claim Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Report of Claim Amounts option can be used to print a variety of statistical reports for beneficiary travel for a specified claim date range. You may choose between the Standard Claims report or the Payable Claims Statistics report.

> The Payable Claims Statistics report prints the travel claim statistics for the ALL OTHER and C&P payment categories for a selected date range. The report is sorted by account and patient and includes the following data: name, patient ID, claim date/time, total mileage amount, deductible amount, amount payable, and remarks.

> The Standard Claims report is broken down by division and can be sorted by account, patient, account type, or carrier. One, many, or all divisions/accounts/patients/account types/carriers may be selected.

> The ACCOUNT is equivalent to the Fund Control Point while the ACCOUNT TYPE is a grouping of like accounts. For example, as of 10-1-90, "828 ALL OTHER" was changed to "829

> ALL OTHER". A new entry (829) was added to the BENEFICIARY TRAVEL ACCOUNT file (#392.3) and the old entry (828) was inactivated. There now exists more than one account with the same "type".

> If there are no patients who meet the criteria selected, the report will read "NO PATIENTS FOUND".

> You may choose to print a full report or a report showing totals only. Each report will supply individual totals as well as division and grand totals. The data displayed in the Totals Only report includes the sort-by category (account, patient name, account type, carrier), deductible amount, amount payable, and the total amount for the date range selected. Choosing to display the Full Report will provide additional information such as patient name, patient ID#, date of claim, carrier, and the deductible and payable amounts for each individual claim. The total

> number of patients will be displayed for the account type and carrier reports whether Totals Only or Full Report is selected.

Example 1: REPORT OF CLAIMS AMOUNTS: PAYABLE CLAIMS STATISTICS, NO DATA

Select Beneficiary Travel Reports Option: AMT Report of Claim Amounts

BENEFICIARY TRAVEL REPORT OUTPUTS

1.....Payable Claims Statistics

2.....Standard Claims Output

Enter Option: (1-2): 1

Enter Beginning Search Date: : AUG 03, 2012// (AUG 03, 2012)

Enter Ending Search Date: : AUG 03, 2012// (AUG 03, 2012)

This report requires 132 columns to print

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

Enter RETURN to continue or '^' to exit:

Payable Claims Report Report Date: AUG 03, 2012 Page: 1

Inclusion Dates: Aug 03, 2012 to Aug 03, 2012

For ACCOUNT TYPE: ALL OTHER

Mileage Amount Amount

Patient Name Patient ID Claim DATE/TME Amount Deduct Payable Remarks

---------------- ------------ ------------------ ------ ------ ------- -----------

No data found for accounts 'ALL OTHER' or 'C&P'

Example 2: REPORT OF CLAIMS AMOUNTS: PAYABLE CLAIMS STATISTICS

BENEFICIARY TRAVEL REPORT OUTPUTS

1.....Payable Claims Statistics

2.....Standard Claims Output

Enter Option: (1-2): 1

Enter Beginning Search Date: : AUG 03, 2012// T-30 (JUL 04, 2012)

Enter Ending Search Date: : AUG 03, 2012// (AUG 03, 2012)

This report requires 132 columns to print

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

...HMMM, HOLD ON...

Enter RETURN to continue or '^' to exit:

Payable Claims Report Report Date: AUG 03, 2012 Page: 1

Inclusion Dates: Jul 04, 2012 to Aug 03, 2012

For ACCOUNT TYPE: ALL OTHER

Mileage Amount Amount

Patient Name Patient ID Claim DATE/TME Amount Deduct Payable Remarks

---------------- ------------ ------------------ ------ ------ ------- -----------

Division: DBA

=========

DGBTPATIENT,TESTING A 000-00-0450P JUL 04, 2012@14:10 10.38 3.00 7.38

DGBTPATIENT,TESTING A 000-00-0450P JUL 04, 2012@14:17 10.38 3.00 7.38

DGBTPATIENT,TESTING A 000-00-0450P JUL 05, 2012@17:49 83.00 6.00 77.00

DGBTPATIENT,TESTING A 000-00-0450P JUL 11, 2012@18:47 2.49 2.49 0.00

DGBTPATIENT,TESTING A 000-00-0450P JUL 12, 2012@12:00 16.60 6.00 10.60

DGBTPATIENT,TESTING A 000-00-0450P JUL 13, 2012@15:26 41.50 6.00 35.50

DGBTPATIENT,TESTING A 000-00-0450P JUL 13, 2012@17:04 0.42 0.42 0.00

DGBTPATIENT,TESTING A 000-00-0450P JUL 15, 2012@11:45 83.00 0.00 26.00

DGBTPATIENT,TESTING A 000-00-0450P JUL 29, 2012@19:54 4.57 0.00 8.57 This is a test for Mileage type Patient

DGBTPATIENT,TESTING A 000-00-0450P JUL 29, 2012@23:57 2.49 0.00 2.49

Enter RETURN to continue or '^' to exit:

Payable Claims Report Report Date: AUG 03, 2012 Page: 2

Inclusion Dates: Jul 04, 2012 to Aug 03, 2012

For ACCOUNT TYPE: ALL OTHER

Mileage Amount Amount

Patient Name Patient ID Claim DATE/TME Amount Deduct Payable Remarks

---------------- ------------ ------------------ ------ ------ ------- -----------

DGBTPATIENT,TESTING A 000-00-0450P JUL 30, 2012@03:08 9.96 0.00 9.96 THIS IS TEST OF COMMON CARRIER

DGBTPATIENT,POW 602-01-0160P JUL 15, 2012@12:13 20.75 0.00 17.50

DGBTPATIENT,THREE 702-03-2470P JUL 05, 2012@20:48 20.75 0.00 20.75

DGBTTEST,EIGHTEEN 202-09-1687P JUL 10, 2012@19:42 4.15 3.00 11.15

DGBTTEST,GOOFY 000-00-2650P JUL 11, 2012@13:00 24.90 6.00 18.90

DGBTTEST,GOOFY 000-00-2650P JUL 18, 2012@12:00 1.66 1.66 0.00

DGBTTEST,GOOFY 000-00-2650P JUL 19, 2012@13:15 0.83 0.00 0.83

DGBTTEST,GOOFY 000-00-2650P JUL 31, 2012@09:34 16.60 3.00 13.60

------ ------ -------

Subtotals 354.43 40.57 267.61

Subtotal Count of Claims: 18

------ ------ -------

TOTALS 354.43 40.57 267.61

TOTAL CLAIMS: 18

Example 3: REPORT OF CLAIM AMOUNTS: STANDARD CLAIMS OUTPUT

BENEFICIARY TRAVEL REPORT OUTPUTS

1.....Payable Claims Statistics

2.....Standard Claims Output

Enter Option: (1-2): 2

Enter beginning date: T-30 (JUL 04, 2012)

Enter ending date: T (AUG 03, 2012)

Sort output by: PATIENT//

Select patient: ALL//

Display Report (F)ULL or (T)OTALS ONLY: FULL//

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80// 132

DIVISION: DBA AUG 3,2012@01:18 PAGE 1

BENEFICIARY TRAVEL OUTPUT BY PATIENT

FROM JUL 4,2012 TO AUG 3,2012

DATE ACCOUNT \$DEDUC \$PAYABLE CARRIER

================================================================================

DGBTPATIENT,TESTING A:000-00-0450P

JUL 4,2012 ALL OTHER 3.00 7.38

JUL 4,2012 ALL OTHER 3.00 7.38

JUL 5,2012 ALL OTHER 6.00 77.00

JUL 11,2012 ALL OTHER 2.49 0.00

JUL 11,2012 SPECIAL MODE - 0.00 0.00

Enter \<RET\> to continue or ^ to QUIT :

DIVISION: DBA AUG 3,2012@01:18 PAGE 2

BENEFICIARY TRAVEL OUTPUT BY PATIENT

FROM JUL 4,2012 TO AUG 3,2012

DATE ACCOUNT \$DEDUC \$PAYABLE CARRIER

================================================================================

DGBTPATIENT,TESTING A:000-00-0450P

JUL 29,2012 ALL OTHER 0.00 2.49

JUL 30,2012 ALL OTHER 0.00 9.96

JUL 30,2012 SPECIAL MODE - 0.00 0.00

TOTAL \$26.91 \$184.88

DGBTPATIENT,POW:000-00-0160P

JUL 15,2012 ALL OTHER 0.00 17.50

TOTAL \$0.00 \$17.50

Enter \<RET\> to continue or ^ to QUIT :

DIVISION: DBA AUG 3,2012@01:18 PAGE 3

BENEFICIARY TRAVEL OUTPUT BY PATIENT

FROM JUL 4,2012 TO AUG 3,2012

DATE ACCOUNT \$DEDUC \$PAYABLE CARRIER

================================================================================

DGBTTEST,EIGHTEEN:000-00-1687P

JUL 10,2012 ALL OTHER 3.00 11.15

TOTAL \$3.00 \$11.15

DGBTTEST,GOOFY:000-00-2650P

JUL 11,2012 ALL OTHER 6.00 18.90

JUL 18,2012 ALL OTHER 1.66 0.00

JUL 19,2012 ALL OTHER 0.00 0.83

JUL 31,2012 ALL OTHER 3.00 13.60

TOTAL \$10.66 \$33.33

Enter \<RET\> to continue or ^ to QUIT :

DIVISION: DBA AUG 3,2012@01:18 PAGE 4

BENEFICIARY TRAVEL OUTPUT BY PATIENT

FROM JUL 4,2012 TO AUG 3,2012

DATE ACCOUNT \$DEDUC \$PAYABLE CARRIER

================================================================================

DIVISION TOTAL \$40.57 \$267.61

Enter \<RET\> to continue or ^ to QUIT :

AUG 3,2012@01:18 PAGE 1

BENEFICIARY TRAVEL OUTPUT BY PATIENT

DIVISION TOTALS

FROM JUL 4,2012 TO AUG 3,2012

DIVISION NAME \$DEDUC \$PAYABLE \$TOTAL

================================================================================

DBA \$40.57 \$267.61 \$308.18

GRAND TOTAL \$40.57 \$267.61 \$308.18

BENEFICIARY TRAVEL REPORT OUTPUTS

1.....Payable Claims Statistics

2.....Standard Claims Output

Enter Option: (1-2):

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term         | Definition                                                                                                                                                                                                                                                                     |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A&A          | Aid and Attendance                                                                                                                                                                                                                                                             |
| ALS          | Advanced Life Support                                                                                                                                                                                                                                                          |
| Beneficiary  | The party to whom the mileage reimbursement is owed. In most cases, the Beneficiary is the same as the patient. There are some exceptions for instance when the patient is under anesthesia and the caretaker presents the appointment documentation to the Travel Office.     |
| BLS          | Basic Life Support                                                                                                                                                                                                                                                             |
| BT           | Beneficiary Travel                                                                                                                                                                                                                                                             |
| BTD          | Beneficiary Travel Dashboard                                                                                                                                                                                                                                                   |
| CBO          | Chief Business Office                                                                                                                                                                                                                                                          |
| HB           | House Bound                                                                                                                                                                                                                                                                    |
| InterSystems | The 3rd party vendor that provides a product known as InterSystems Cache                                                                                                                                                                                                       |
| MT           | Means Test                                                                                                                                                                                                                                                                     |
| OIG          | Office of Inspector General                                                                                                                                                                                                                                                    |
| Rx           | Prescription                                                                                                                                                                                                                                                                   |
| SC%          | Service Connected disability % determines the amount of VA benefits for which a Veteran qualifies based on a service-connected injury(ies) or illness(es).                                                                                                                     |
| Section 508  | A Public Law that agencies must provide employees and members of the public who have disabilities access to electronic and information technology that is comparable to the access available to employees and members of the public who are not individuals with disabilities. |
| SSN          | Social Security Number                                                                                                                                                                                                                                                         |
| VA           | Veterans Affairs                                                                                                                                                                                                                                                               |
| VACO         | Veterans Affairs Central Office                                                                                                                                                                                                                                                |
| VAF          | VA Form                                                                                                                                                                                                                                                                        |
| VFA          | Veterans Financial Assessment                                                                                                                                                                                                                                                  |
| VHA          | Veterans Health Administration                                                                                                                                                                                                                                                 |
| VistA        | Veterans Health Information Systems Technology Architecture                                                                                                                                                                                                                    |
| VMS          | Virtual Memory System                                                                                                                                                                                                                                                          |

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Why does the C&P question not trigger the C&P account to be automatically entered? 

The question was added for eligibility purposes only to trigger a denial of benefits if “NO” was entered. A feature to automatically trigger a change in account  type based on the eligibility question was not included in the specifications for the current version.

When a Veteran is not eligible for payment or eligible for payment only when the care is SC, the system asks whether this is a claim for an SC appointment or a claim for a Comp and Pension appointment. How do I deny a claim and get to the denial letters when the reason is related to the 30 day rule or something else? 

Answering “NO” at the prompts will mark the Veteran as not eligible for payment and you will be prompted to continue the claim providing a reason or to deny the claim and print the letter. The reason for the denial is not tied to the question so you will be able to select any of the available choices.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

30 Day Application Requirement 16
AUDIT REPORT DISPLAYED 40
Audit Report example 40
AUDIT REPORT FOR EXPORT TO EXCEL 42
Automatic Deductible Zero 12
Automatic Eligibility Determination 12
Bene Travel Account file Enter/Edit 9
Beneficiary Travel Menu 6
Beneficiary Travel Reports Submenu 6
BT Deductible Tracking 14
BT Report menu 36
Caregiver eligibility 13
Claim Enter/Edit 10
Claim Enter/Edit Examples 19
CLAIMS AMOUNTS
PAYABLE CLAIMS STATISTICS, NO DATA 44
CLERK REPORT DISPLAYED 43
Clerk Report example 43
CLERK REPORT FOR EXPORT TO EXCEL 45
Common Carrier Mode of Transportation 16
Delete default answer at prompt 4
Denial of Benefits 16
DENIAL OF BENEFITS DURING MILEAGE TRAVEL CLAIM ENTRY 23
DENIAL OF BENEFITS DURING SPECIAL MODE TRAVEL CLAIM ENTRY 29
Display Last Address Change Date 15
Edit Denial Letters Template ...................................................................................................................... 39
9
ENTERING A SPECIAL MODE TRAVEL CLAIM 26
ENTERING ALTERNATE INCOME 43
FISCAL REPORT DISPLAYED 52
Fiscal Report examples 52
FISCAL REPORT FOR EXPORT TO EXCEL 53
Glossary 59
Help 3
Income and Status Display from Means tests 15
Introduction 1
Logging in to VistA 2
Medical Review (Special Mode claims) 17
Message on Service Connected Appointment Only 15
Net Income display 12
Non-Qualified Appointment 17
Non-Veteran 17
NSC High Income 17
On-line Help 3
Other eligibility 13
Previous Income Information Retrieval 15
Prompts
correcting a default answer 4
entering dates and times 4
types of 3
using Spacebar Recall 5
REPORT OF CLAIM AMOUNTS
STANDARD CLAIMS OUTPUT 57
Report of Claim Amounts examples 54
REPORT OF CLAIMS AMOUNTS
PAYABLE CLAIMS STATISTICS 56
Reprint Denial of Benefits Letters 35
REPRINTING DENIAL OF BENEFITS LETTER 35
SAMPLE CLAIM VOUCHER 32
SC\<30% Non-SC Appointment 17
Spacebar Recall 5
SPECIAL MODE REPORT DISPLAYED 49
Special Mode Report example 49
SPECIAL MODE REPORT FOR EXPORT TO EXCEL 51
Special Mode Trip Tracking 10
SUMMARY MILEAGE REPORT DISPLAYED 37
SUMMARY MILEAGE REPORT FOR EXPORT TO EXCEL 39
Summary of Main Menu items 6
Summary of Reports Sub-Menu Options 7
Summary Report example 37
Table of Contents iv
Transplant eligibility 13
TRAVEL PATTERN REPORT DISPLAYED 46
Travel Pattern Report example 46
TRAVEL PATTERN REPORT FOR EXPORT TO EXCEL 48
Troubleshooting 60
User Instructions 9
View of Claim 41
VIEWING A CLAIM 41
VistA
getting started with 2
Waiver Expiration 14
