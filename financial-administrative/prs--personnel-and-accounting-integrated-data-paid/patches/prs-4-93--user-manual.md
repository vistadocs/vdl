---
title: PRS*4*93 User Manual - Part-Time Physicians
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Part-Time Physicians
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4*93
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 2
description: - [Human Resources Personnel](#human-resources-personnel) - [New Options](#new-options) - [PT Physician Menu](#pt-physician-menu) - [Employee Menu](#employee-menu) - [Changed Options](#changed-options) - [New Options](#new-options-1) - [PT Physician with Memorandum Menu](#pt-physician-with-memorandu
audience: 
keywords: 
  - time
  - part
  - physician
  - memorandum
  - physicians
  - period
  - manual
  - leave
  - table
  - contents
page_count: 0
word_count: 7903
section_count: 12
table_count: 16
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p93_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p93_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

![](prs-4-93-user-manual-part-time-physicians/001.png)

Part-time Physicians

[Personnel and Accounting](http://www.va.gov/vdl/Financial_Admin.asp?appID=51)

[Integrated Data (PAID)](http://www.va.gov/vdl/Financial_Admin.asp?appID=51)

USER GUIDEPRS\*4.0\*93February 2007

Health Systems Design and Development

Table of Contents

# Human Resources Personnel


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Human Resources Personnel](#human-resources-personnel)
  - [New Options](#new-options)
    - [PT Physician Menu](#pt-physician-menu)
- [Employee Menu](#employee-menu)
  - [Changed Options](#changed-options)
  - [New Options](#new-options-1)
    - [PT Physician with Memorandum Menu](#pt-physician-with-memorandum-menu)
- [Timekeepers Main Menu](#timekeepers-main-menu)
  - [Changed Options](#changed-options-1)
  - [## ## New Options](#new-options-2)
    - [PT Physician Menu](#pt-physician-menu-1)
- [Payroll Main Menu](#payroll-main-menu)
  - [New Options](#new-options-3)
    - [PT Physician Menu](#pt-physician-menu-2)
- [Payroll Supervisor Menu](#payroll-supervisor-menu)
  - [Changed Option](#changed-option)
- [# # T&A Supervisor Menu](#ta-supervisor-menu)
  - [Changed Options](#changed-options-2)
  - [New Options](#new-options-4)
    - [PT Physician Menu](#pt-physician-menu-3)
- [Data Supplement](#data-supplement)
  - [PTP ESR DATA FILE DESCRIPTIONS](#ptp-esr-data-file-descriptions)
  - [WORK SUMMARY SCREEN DESCRIPTIONS](#work-summary-screen-descriptions)

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PT Physician Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new menu contains all of the options required for Human Resources personnel to process part-time physicians with a Memorandum of Service Level Expectations.

#### Enter Memoranda

This option allows Human Resources personnel to enter a Memorandum of Service Level Expectations for part-time physicians.

Once you enter the employee’s name, information such as the employee’s SSN, and pay information are displayed. You are then prompted to enter the start date of the pay period (the end date is calculated automatically), the agreed hours, and any initial comments. An electronic signature code is required to complete the memorandum.

The software will automatically assign the PRSP EMP security key to the part-time physician when a new memorandum is entered. This key provides access to the PT Physician With Memorandum Menu \[PRSP PTP MENU\].

![](prs-4-93-user-manual-part-time-physicians/002.png)

#### Terminate Memoranda

This option allows you to terminate a Memorandum of Service Level Expectations for part-time physicians in cases where the part-time physician is unable to fulfill their obligation or their employment with the VA is terminated.

Once the employee name is entered, the memorandum is displayed.

![](prs-4-93-user-manual-part-time-physicians/003.png)

You are then asked if you want to terminate this memorandum. If you answer yes, you are prompted for the termination date which must be the last day of a pay period.

> WARNING: It is very important that the memorandum is terminated in a timely manner and recorded through the Terminate Memoranda option. The termination process should occur during the pay period in which the memorandum will end. Once the timecard for this pay period has been transmitted to Austin and the status is updated to TRANSMITTED, the software will not allow you to select the last day of this pay period as the termination date.

You can also enter any comments in reference to the termination. An electronic signature code is required to complete the termination.

![](prs-4-93-user-manual-part-time-physicians/004.png)

#### Delete Future Memoranda

This option allows Human Resources personnel to delete a part-time physician's Memorandum of Service Level Expectations that has yet to begin. This option is used in cases where the part-time physician has decided not to enter into a memorandum with the VA.

Since memoranda cannot overlap and there is a 6-month limit on entering future memoranda, there should only be one future memorandum at any one time.

Future memoranda that start in a pay period that has not been opened, can be deleted without any other checks being made.

If the memorandum being deleted starts in a pay period that has already been opened, the following rules apply.

- If the payroll has already been processed for the first pay period of the part-time physician’s memorandum, the memorandum will have to be terminated and reconciled.
- If the timecard has already been transmitted but the cut off window for transmitting timecards is still open, the Payroll Supervisor will have to determine if there is enough time to return the timecard, delete the memorandum, have the timekeeper post all of the tours with the correct time, re-certify the timecard and re-transmit the timecard before the window closes. If there is, they can return the timecard and delete the memorandum. If there isn’t enough time, the memorandum will have to be terminated and reconciled.
- For timecards with a status of Payroll, the Payroll Supervisor will have to return it to the Timekeeper before they can delete the memorandum.

Once the memorandum is deleted, the software checks each daily ESR. For any daily ESRs with a status of APPROVED, the timecard posting for that day is deleted.

Once all of the necessary timecards entries have been deleted, the entire ESR record for the pay period will be deleted.

![](prs-4-93-user-manual-part-time-physicians/005.png)

#### Begin Reconciliation Process

This option allows Human Resources personnel to review a part-time physician's Memorandum of Service Level Expectations and to determine what reconciliation actions will need to occur, based on the final hours worked by the part-time physician.

After the physician’s name is entered, the summary of their memorandum and hours worked per pay period are displayed.

One or more of the following reconciliation choices appear for selection.

1.  No reconciliation needed
2.  Pay VA for negative balance
3.  Pay Phy for positive balance

The next screen allows you to choose whether to print a paper copy of the reconciliation information and deliver it to the part-time physician, or to forward an electronic version of it to the physician.

A signature code is required to complete the process. The status of the memorandum is then updated from ACTIVE to RECONCILIATION STARTED.

![](prs-4-93-user-manual-part-time-physicians/006.png)

![](prs-4-93-user-manual-part-time-physicians/007.png)

![](prs-4-93-user-manual-part-time-physicians/008.png)

#### Reconcile Memoranda

This option allows Human Resources personnel to review a part-time physician's Memorandum of Service Level Expectations and to complete the memorandum reconciliation, once the part-time physician has completed and signed the Begin Reconciliation Process form

This option allows you to add the part-time physician’s comments if the reconciliation was handled on paper, and to add any additional comments.

After you electronically sign the reconciliation, it will lock the memorandum so that no further changes can be made.

![](prs-4-93-user-manual-part-time-physicians/009.png)

![](prs-4-93-user-manual-part-time-physicians/010.png)

![](prs-4-93-user-manual-part-time-physicians/011.png)

#### Memoranda Report

This option allows you to review a memorandum for a selected employee and pay period.

After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

VA TIME & ATTENDANCE SYSTEM

DISPLAY PT PHYSICIAN MEMORANDA

Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

Select PAY PERIOD: 04-21

Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

The software displays all of the information related to the part-time physician's Memorandum of Service Level Expectations.

The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

![](prs-4-93-user-manual-part-time-physicians/012.png)

Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they are listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it is listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination, etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments are also listed.

WARNING! If there are incomplete ESRs, DO NOT proceed with the reconciliation.

![](prs-4-93-user-manual-part-time-physicians/013.png)

#### Memoranda Expiring Within Date Range

This option allows Human Resources personnel to identify a part-time physician’s Memorandum of Service Level Expectations that will expire within the specified date range, so that the appropriate paperwork to begin the memorandum renewal can be initiated.

You have the option of entering an “Off By” percentage between 1 and 100. When entered, only memorandums that are off by more than the percentage you specify will be included. For example, if you enter 5, only memorandums within the date range you’ve selected and that are off by more than 5% will be included.

![](prs-4-93-user-manual-part-time-physicians/014.png)

![](prs-4-93-user-manual-part-time-physicians/015.png)

![](prs-4-93-user-manual-part-time-physicians/016.png)

#### Display Pay Period ESR

This option allows Human Resources personnel to review a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

![](prs-4-93-user-manual-part-time-physicians/017.png)

![](prs-4-93-user-manual-part-time-physicians/018.png)

![](prs-4-93-user-manual-part-time-physicians/019.png)

# Employee Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to this patch, all part-time physicians tracked their time and attendance on paper form VA Form 4-5631a, known as a Subsidiary Record. After this patch, the part-time physicians who elect to enter into a Memorandum of Service Level Expectations with the VA will track their time and attendance via an automated Electronic Subsidiary Record which will be stored within the VistA PAID/ETA software files.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Cancel Leave Request

Approved leave is automatically posted to the ESR. This option was modified to remove such leave from the ESR when the employee cancels it.

#### Edit Leave Request

Approved leave is automatically posted to the ESR. This option was modified to remove such leave from the ESR when the leave is edited since editing revokes the supervisor’s approval of the leave.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PT Physician with Memorandum Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PT Physician With Memorandum Menu has been added to the existing Employee Menu, and contains the options used by part-time physicians with a Memorandum of Service Level Expectations to perform the necessary actions related to tracking of their Time and Attendance.

This menu is only accessible to employees that hold the PRSP EMP key. This key is automatically assigned when Human Resources enters a memorandum for the employee.

#### Electronic Subsidiary Record-Daily Enter/Edit

This option displays the action pick list and two new screens that will allow the part-time physician to monitor the status of their Electronic Subsidiary Record (ESR) for a selected pay period, and to enter their time and attendance. The first screen is called the Work Summary Screen (WSS) and the second is called the ESR Data Entry Screen.

#### Action Pick List

When the Electronic Subsidiary Record-Daily Enter/Edit option is first invoked, the software reviews the part-time physician’s memorandum and generates a pick list of items requiring their attention. The pick list contains the following types of actions in this order:

1.  Any prior memoranda that need to be reconciled.
2.  Any prior pay periods that have incomplete daily ESRs.
3.  The current pay period.
4.  The next pay period if it has been opened and if the part-time physician has an active memorandum covering this pay period.

The following is an example of the action pick list that you might see upon entering this option.

Select PT Physician With Memorandum Menu Option: 1 Electronic Subsidiary Record-Daily Enter/Edit

1\. Reconcile Prior Memorandum from OCT 05, 2003 TO OCT 02, 2004

2\. Edit ESR for prior pay period 04-18 \[Sun 5-Sep-04 - Sat 18-Sep-04\]

3\. Edit ESR for prior pay period 04-20 \[Sun 3-Oct-04 - Sat 16-Oct-04\]

4\. Edit ESR for prior pay period 04-21 \[Sun 17-Oct-04 - Sat 30-Oct-04\]

Select an Item : (1-4): 1//

Items selected from group 1 are covered later in this document.

If the part-time physician selects any item from group 2, 3 or 4, the Work Summary Screen (WSS) screen is displayed.

#### The Work Summary Screen

Once an item is selected from group 2, 3, or 4, the Work Summary Screen for that item is displayed. Information such as the employee name, SSN, Station Number, Normal Hours, Duty Base, T&L, Pay Plan, and the last Pay Period processed are displayed, as well as memorandum and annual leave information, as of that pay period. (Please see the supplement at the end of this document for a description of all pertinent fields.)

The days of the pay period are grouped by week, and are listed in order of the day number (not the date) for selection. Each day shows the ESR Daily Status and a listing of the various types of time recorded for this day, if any.

When the pay period is opened, the system initially populates each ESR day with a status of either DAY OFF (if the employee does not have a scheduled tour for that day) or NOT STARTED (if the employee does have a scheduled tour for that day).

Once you complete and sign the ESR for a particular day, the status is updated to one of the following.

*PENDING* - the ESR day was modified and saved, but not signed.

*SIGNED* - the ESR day was completed and signed.

All days on the ESR with a scheduled tour, must be electronically signed by the physician. There may be circumstances when no work is performed and no leave is taken on a scheduled day. In this case, the physician electronically signs the day by selecting the day, and without entering any time on the ESR, saves the ESR day. When an ESR day is saved with no work or leave entered, you are prompted to sign the day.

> **NOTE:** The supervisor reviews ESR days that have been signed by a part-time physician. The supervisor can change the status of the day to either APPROVED or RESUBMIT. The APPROVED status indicates that no further action needs to be taken by the part-time physician. The RESUBMIT status indicates that the part-time physician should modify the data on the ESR and then re-sign it.

Sample Work Summary Screen

![](prs-4-93-user-manual-part-time-physicians/020.png)

#### The Daily Electronic Subsidiary Record (ESR)

Once you select a day, the Electronic Subsidiary Record (ESR) for that day is displayed. Up to seven separate entries may be made for each day. The part-time physician should enter the appropriate number of entries to accurately reflect the actual work performed during the course of the day.

The time segments should be posted in chronological order whenever possible but the software will accept the postings in any order. For example, if an additional time segment needs to be added at a later date, it can be added to the end of the existing list of postings.

The ESR Data Entry Screen includes employee information such as name, SSN, Station Number, Time and Leave Unit, the Tour Beginning Date, and if a tour has been assigned to the day, a summary of the tour’s start/stop times and meal time, if any. (Please see the supplement at the end of this document for a complete list of pertinent field descriptions.)

Following is a list of the data entry fields with a brief description

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>START</th>
<th>The time that an individual work or leave segment began.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STOP</td>
<td>The time that an individual work or leave segment ended.</td>
</tr>
<tr class="even">
<td>TYPE OF TIME</td>
<td><p>The type of time worked or leave taken.</p>
<p>AA Authorized Absence</p>
<p>AD Adopt</p>
<p>AL Annual Leave</p>
<p>CB Family Care</p>
<p>CP Continuation of Pay (COP)</p>
<p>DL Donor Leave</p>
<p>HX Holiday Excused</p>
<p>ML Military Leave</p>
<p>NL Non-pay Annual Leave</p>
<p>RG Regular Time</p>
<p>RL Restored Annual Leave</p>
<p>SL Sick Leave</p>
<p>TR Training</p>
<p>TV Travel</p>
<p>WP Leave Without Pay</p></td>
</tr>
<tr class="odd">
<td>REMARKS CODE</td>
<td>A code which further describes the TYPE OF TIME entered. Only the appropriate REMARKS CODES that correspond to the TYPE OF TIME entered will be allowed. Enter a ? for a list of the appropriate choices. (This field is optional.)</td>
</tr>
<tr class="even">
<td>MEAL</td>
<td>Enter the best approximation of time for the meal during this work segment, in increments of 15 minutes. Meals may not be longer than 60 minutes, so appropriate meal times are 15, 30, 45, and 60. Enter a 0 or leave the field blank to indicate that no meal was taken. When meals are taken, they must be entered, even when they are not scheduled for that tour. Meals may be entered for periods of both regular hours and leave. Entering the meal time will automatically deduct the meal from the total creditable hours in the work segment.</td>
</tr>
<tr class="odd">
<td>HRS</td>
<td>This is a calculated field. The system will automatically enter the number of hours entered for each segment based on the START, STOP, and MEAL times.</td>
</tr>
<tr class="even">
<td>REMARKS</td>
<td>Any further comments you would like to enter. Any remarks entered here are seen by the supervisor when they review the daily ESR. (This field is optional unless Authorized Absence is entered.)</td>
</tr>
</tbody>
</table>

As you make each entry, you can move to the next field on the form by entering a Tab or by pressing the Enter key. A question mark (?) may be entered at most fields for a list of possible entries and/or formats. For further information on using this type of edit screen, please refer to Chapter 1 of the [Personnel and Accounting Integrated Data (PAID)](http://www.va.gov/vdl/Financial_Admin.asp?appID=51) User Manual, which can be accessed from the VistA Documentation Library (VDL) web page at www.va.gov/vdl/.

Up-arrow REMARKS (^REMARKS) allows you to jump to the REMARKS field. This field is free text and will allow up to 70 characters. These remarks are optional, but they may be helpful to the Supervisor as they review your daily ESRs. It is recommended that REMARKS be entered when the part-time physician deviates from their normally scheduled tour of duty or if they work on a day where they were not scheduled to work.

The software allows you to skip to the COMMAND prompt by entering an up-arrow (^) in any field. You can automatically save the changes and skip directly to the electronic signature prompt by entering Num Lock and then E in any field.

Once you have completed your daily ESR entries and navigated to the COMMAND prompt, enter SAVE or EXIT. If you enter EXIT without saving first, you will be asked if you wish to save your entries. Once you enter SAVE, you will be asked for an Electronic Signature. If you do not enter a signature, the ESR is given a status of PENDING, and you will see the following message:

PENDING: changes were saved without signature.

Sample ESR

Some of the fields will allow abbreviated entries. For example, you may enter 7A or 3P for a time. You may enter a question mark (?) at most fields for a description of acceptable formats and/or entries.

![](prs-4-93-user-manual-part-time-physicians/021.png)

![](prs-4-93-user-manual-part-time-physicians/022.png)

#### Extended Absence

This menu contains options used to enter or maintain extended absence records. An extended absence is a future period of time when the part-time physician will not be performing work for the VA during a normally scheduled tour of duty and they are not planning on using an approved type of leave to cover their absence.

An electronic signature code is required to use these options. An electronic signature code can be entered/edited through the Electronic Signature Code Edit option.

#### Enter Extended Absence

This option allows a part-time physician to specify a future period of time when they will not be performing work for the VA (extended absence). The software automatically changes the status to “Signed” for ESR days with a scheduled tour of duty, if those days are covered by the period of extended absence. Therefore, the physician does not need to manually update their ESR during their absence.

You are prompted to enter a beginning and ending date for a new period of extended absence, as well as any remarks. An electronic signature code is required to complete the entry.

Please see the sample screen provided under Edit Extended Absence.

#### Edit Extended Absence

This option allows the part-time physician to edit a previously entered extended absence. The software will automatically update the current and future days on the ESR as necessary. However, any ESR days that are prior to the current day will not be automatically modified when an extended absence is edited. An extended absence cannot be edited if its “To Date” is prior to the current day. A signature code is required to complete the edit.

*Sample Screens for Enter/Edit Extended Absence options.*

![](prs-4-93-user-manual-part-time-physicians/023.png)

*Edited Screen*

![](prs-4-93-user-manual-part-time-physicians/024.png)

#### Cancel Extended Absence

This option allows the part-time physician to cancel a previously entered extended absence. The software will automatically update the current and future days on the ESR, as necessary. However, any ESR days that are prior to the current day will not be automatically modified when an extended absence is cancelled. An extended absence cannot be cancelled if its “To Date” is prior to the current day.

![](prs-4-93-user-manual-part-time-physicians/025.png)

#### Display Extended Absence

This option allows you to display a list of extended absence records that end on or after a specified date. The timeframe of the absence, as well as any remarks, the status, and the dates entered and/or updated are displayed.

![](prs-4-93-user-manual-part-time-physicians/026.png)

#### Display Pay Period ESR

This option displays a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

![](prs-4-93-user-manual-part-time-physicians/027.png)

![](prs-4-93-user-manual-part-time-physicians/028.png)

![](prs-4-93-user-manual-part-time-physicians/029.png)

#### Display Memoranda

This option displays information related to the part-time physician's Memorandum of Service Level Expectations. It includes fields that help to identify the part-time physician (name, SSN, T&L etc.) and a memorandum summary (Start/End dates, Agreed Hours, completion percentages etc.). This will be followed by a list of pay periods covered by the memorandum and the hours credited during each of these pay periods. If any Non-Pay or Leave Without Pay occurred during the memorandum, a list of the hours and the pay period in which they occurred will be displayed.

If the memorandum has ended and the part-time physician has selected their reconciliation choice via the electronic form, their reconciliation choice and any reconciliation comments will be displayed.

![](prs-4-93-user-manual-part-time-physicians/030.png)

#### Select Reconciliation Choice

This option allows you to review a recently ended memorandum, and to select a reconciliation option. One or more of the following reconciliation choices might appear for selection.

1.  No reconciliation needed
2.  Pay VA for negative balance
3.  Pay Phy for positive balance

The review screen is shown here. The next screen shows more information related to the memorandum and the reconciliation options.

![](prs-4-93-user-manual-part-time-physicians/031.png)

![](prs-4-93-user-manual-part-time-physicians/032.png)

![](prs-4-93-user-manual-part-time-physicians/033.png)

# Timekeepers Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Post Employee Time

This option has been modified to prevent selection of a part-time physician with an active memorandum. The new option, Post PT Physician Time, must be used to post time for such employees.

#### Enter/Edit Employee Tour of Duty

This option has been modified to perform additional steps when a tour is changed for a part-time physician with an active memorandum. In addition to the normal step of removing any timecard postings on the changed day, the software will also reset the status of any daily ESR the part-time physician has already posted to RESUBMIT, so they will have to review and repost the information if necessary.

## ## ## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PT Physician Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains all of the options that Timekeepers will need to monitor and post timecards for part-time physicians with a Memorandum of Service Level Expectations.

#### Post PT Physician Time

This option allows the timekeeper to post time card data for part-time physicians with a Memorandum of Service Level Expectations. Regular employee’s timecards can not be selected using this option. This action should only be done at the direction of the T&L supervisor when the physician's Electronic Subsidiary Record (ESR) cannot be completed before time card certification for the pay period. Unscheduled regular time (RG) will only be tracked via the ESR and cannot be posted to the time card.

Non Pay, AWOL, and On Suspension can not be posted on the ESR. When appropriate, these must be posted directly on the timecard by the timekeeper. Furthermore, for a current pay period, the timekeeper will have to post these to the timecard after the ESR day has been approved. This is because approval of an ESR day for a timecard with timekeeper status (i.e., not yet certified) will repost the timecard and overwrite any previous postings for that day.

If you are responsible for more than one T&L Unit, you are first prompted to select a T&L Unit. You are then prompted for a date, and whether or not to post the employees time cards in alphabetical order.

![](prs-4-93-user-manual-part-time-physicians/034.png)

![](prs-4-93-user-manual-part-time-physicians/035.png)

#### Display Pay Period ESR

This option displays a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

![](prs-4-93-user-manual-part-time-physicians/036.png)

![](prs-4-93-user-manual-part-time-physicians/037.png)

![](prs-4-93-user-manual-part-time-physicians/038.png)

#### Display PP ESR Exceptions

This option allows Supervisors to review daily ESR exceptions for part-time physicians with a Memorandum of Service Level Expectations. It can be used to verify that part-time physicians have completed each day within the pay period with a scheduled Tour of Duty and to monitor other work performed on scheduled days off.

![](prs-4-93-user-manual-part-time-physicians/039.png)

#### Memoranda Report

This option allows you to review a memorandum for a selected employee and pay period.

After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

VA TIME & ATTENDANCE SYSTEM

DISPLAY PT PHYSICIAN MEMORANDA

Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

Select PAY PERIOD: 04-21

Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

The software displays all of the information related to the part-time physician's Memorandum of Service Level Expectations.

The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

![](prs-4-93-user-manual-part-time-physicians/040.png)

Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination, etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

![](prs-4-93-user-manual-part-time-physicians/041.png)

# Payroll Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PT Physician Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new menu has been added to the existing Payroll Supervisor Menu. The PT Physician Menu contains all of the necessary options to allow the Payroll Supervisor to monitor the status of a part-time physician’s Memorandum of Service Level Expectations.

#### Memoranda Report

This option allows you to review a memorandum for a selected employee and pay period.

After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

VA TIME & ATTENDANCE SYSTEM

DISPLAY PT PHYSICIAN MEMORANDA

Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

Select PAY PERIOD: 04-21

Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

The software displays all of the information related to the part-time physician's Memorandum of Service Level Expectations.

The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

![](prs-4-93-user-manual-part-time-physicians/042.png)

Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination, etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

![](prs-4-93-user-manual-part-time-physicians/043.png)

#### Display Pay Period ESR

This option allows you to review a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

![](prs-4-93-user-manual-part-time-physicians/044.png)

![](prs-4-93-user-manual-part-time-physicians/045.png)

![](prs-4-93-user-manual-part-time-physicians/046.png)

#### ESR Exceptions For Entire Memoranda

This option generates a report that lists any part-time physician who has not yet completed an ESR for any pay period within their memorandum, allowing supervisors to identify and monitor incomplete daily ESRs.

You can choose whether or not to include the current pay period in the report, and you may include all part-time physicians in the T&L, or enter individual part-time physicians.

![](prs-4-93-user-manual-part-time-physicians/047.png)

![](prs-4-93-user-manual-part-time-physicians/048.png)

# Payroll Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Changed Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Open Next Pay Period

This option was modified to initialize the ESR daily status and auto post holidays, leave, and extended absences to the ESR for the new pay period. It will also update the status of the memorandum from NOT STARTED to ACTIVE, if the pay period being opened is the first pay period covered by the memorandum.

# # # T&A Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Supervisory Approvals

This option was modified to automatically post an approved leave request to the ESR in an open pay period if the employee taking leave is a part-time physician with an active memorandum.

If any portion of the leave request covers a future pay period that has not been opened yet, the appropriate ESR records will be automatically posted when the pay period is opened.

If the leave request does not pass all of the necessary checks, it will not be posted to the ESR record.

#### Pay Period Certification

This option was modified to review the part-time physician's ESR and to update the various categories of hours worked in the PT PHYSICIAN MEMORANDUM (#458.7) file when the associated timecard is certified.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PT Physician Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new menu has been added to the existing T&A Supervisor Menu. The PT Physician Menu contains all of the necessary options to allow the T&A and T&A OT Supervisor to monitor and maintain the part-time physician’s Memorandum of Service Level Expectations.

#### Approve Signed ESRs

The T&A supervisor is required to review each signed day of the part-time physician's ESR, and take one of the following actions.

Approve - if the ESR day appears to be correct.

Resubmit - if the physician needs to correct the ESR day.

Bypass - to skip the day now and take action on it at a later time.

The (A)pprove, (B)ypass or (R)esubmit actions may be applied to an individual day or to all the days listed.

To take action on an individual day, select the day by entering its item number from the list and then enter the action you wish to apply to this day. If the Resubmit action is selected, you will also be prompted to enter a short text description like your phone number etc.

Individual days that have been marked with an action will not be altered when you apply another action type to the remaining days in the list.

Once you have completed your entries, an electronic signature code is required to complete the process.

When the T&A Supervisor approves a signed day, this option attempts to update the part-time physician's timecard for that day. Updates to the timecard will be screened based on the status of the timecard and the affect of any potential update. If the timecard associated with the ESR day being approved has a status of TIMEKEEPER, then the approval action will always update the timecard.

An individual ESR approval may be rejected if the following conditions are met.

1.  The timecard associated with the ESR day being approved has a status of Transmitted to Austin or Payroll.
2.  There is a discrepancy between the timecard and ESR. That is, if for any type of time, such as sick leave, annual leave, military leave, etc., the total number of hours posted to the timecard is not equal to the total number of hours posted to the ESR.
3.  The type of time discrepancy must also involve a type of time that is reported to the AAC. So, in general, the type of time—RG—Regular Hours, is not considered, since it is only posted to the ESR.

If the first condition is met, then the software checks to determine if an ESR approval would result in an incorrect report to the AAC due to a discrepancy between the timecard and the ESR. To do this, total hours are calculated for all types of time that are recorded on the timecard and all the types of time that are on the ESR for a particular day. Next, the totals for each type of time are compared. If any of the total hours for a type of time, like sick leave, annual leave, holiday excused, military leave, etc., don't match; then the ESR cannot be approved, and a message is displayed to the supervisor, showing the type of time that does not match, and the total hours for that type of time.

Following is an example of the type of message that could be displayed. It shows the discrepancies between the timecard hours and the ESR hours, followed by the ESR and timecard postings.

> ESR approval REJECTED for PAIDPTP,ONE on day 4 in PP 04-18.

> Time Discrepancies must be resolved.    Timecard Status: TRANSMITTED TO AUSTIN

> Payroll must initiate corrected timecard or physician must resubmit ESR.

> ESR approval REJECTED for PAIDPTP,ONE on day 4 in PP 04-18.

>                TIME DISCREPANCIES BETWEEN TIMECARD AND ESR

>       Error          Type of Time      Timecard Hrs      ESR Hrs

>   --------------------------------------------------------------

>   LEAVE mismatch          TR                0               1.5

>                                 ESR POSTING

> Item    Date     Scheduled Tour     Work/Leave Posted        Hours Meal  Status

> ----------------------------------------------------------------------

>    Wed  8-Sep-04 03:30P-MID Shift 2

>                                  04:00P-06:00P   TRAINING    01:30  30

>                                  08:00A-09:00A   REG TIME    01:00      Approved

>                               TIMECARD POSTING

>        Date          Scheduled Tour           Tour Exceptions

>   ------------------------------------------------------------

>    Wed  8-Sep-04     03:30P-MID             

>                        Shift 2

There are three special cases:

1.  Since RG should not be posted on the timecard and only on the ESR, RG is generally ignored.
2.  Since WP with remarks On Suspension or AWOL can only be posted to the timecard, WP with these remarks is also ignored.
3.  Since on any day that NP is posted to the timecard there can be no work performed, a check is performed to make sure that there is no RG or any leave posted to the ESR when NP is on the timecard.

The comparison does not consider start and stop times, specifically.  E.g. A timekeeper may need to post around a lunch for leave during the middle of the day on the physician’s timecard.  The timekeeper posts, 10a-noon Sick Leave then 12:30pm-2pm sick leave.  The part-time physician then updates their ESR with 10a-2:00pm Sick Leave and puts 30 minutes in the meal field.  This would be o.k. since the total sick leave would be 3.5 hours in each case.

![](prs-4-93-user-manual-part-time-physicians/049.png)

If all of the days in the list need to have the same action or if you have previously selected and marked all of the days that need to have a different action, you can then enter the necessary action to apply to the remaining days.

![](prs-4-93-user-manual-part-time-physicians/050.png)

After each individual or group action has been entered, the software will update the Status field.

![](prs-4-93-user-manual-part-time-physicians/051.png)

You then see the Supervisory Action Summary, and are prompted for your electronic signature code to complete the approval process.

![](prs-4-93-user-manual-part-time-physicians/052.png)

#### Memoranda Report

This option generates a report which allows the supervisor to review a memorandum for a selected employee and pay period that can be used to monitor the status of the hours worked and leave taken since the memorandum began.

After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

VA TIME & ATTENDANCE SYSTEM

DISPLAY PT PHYSICIAN MEMORANDA

Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

Select PAY PERIOD: 04-21

Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

The software displays all of the information related to the part-time physician's Memorandum of Service Level Expectations.

The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

![](prs-4-93-user-manual-part-time-physicians/053.png)

Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination, etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

![](prs-4-93-user-manual-part-time-physicians/054.png)

#### Display PP ESR Exceptions

This option allows Supervisors to review daily ESR exceptions for part-time physicians with a Memorandum of Service Level Expectations. It can be used to verify that part-time physicians have completed each day within the pay period with a scheduled Tour of Duty and to monitor other work performed on scheduled days off.

![](prs-4-93-user-manual-part-time-physicians/055.png)

#### ESR Exceptions For Entire Memoranda

This option generates a report that lists any part-time physician who has not yet completed an ESR for any pay period within their memorandum, allowing supervisors to identify and monitor incomplete daily ESRs.

You can choose whether or not to include the current pay period in the report, and you may include all part-time physicians in the T&L, or enter individual part-time physicians.

![](prs-4-93-user-manual-part-time-physicians/056.png)

![](prs-4-93-user-manual-part-time-physicians/057.png)

#### Display Pay Period ESR

This option allows the supervisor to review a part-time physician's ESR record. Any pay period from a current or past memorandum may be selected. If the next pay period has already been opened, it may also be selected.

The T&A Supervisor selects a T&L Unit, a part-time physician and the date they need to unlock.

VA TIME & ATTENDANCE SYSTEM

UNLOCK DAILY ESR

Select T&L Unit: 028

Select EMPLOYEE: PAIDPTP,ONE PAIDPTP,ONE 000-28-0001

Posting Date: 3/7/2005 (MAR 07, 2005)

Once the posting date has been selected, the entire ESR for that pay period is displayed for the Supervisor to review and verify that they have selected the correct ESR day to unlock.

![](prs-4-93-user-manual-part-time-physicians/058.png)

![](prs-4-93-user-manual-part-time-physicians/059.png)

![](prs-4-93-user-manual-part-time-physicians/060.png)

#### Unlock Daily ESR

This option allows Supervisors to select and unlock individual days in prior Pay Period ESRs, so the part-time physician can change or complete any incomplete daily ESRs.

![](prs-4-93-user-manual-part-time-physicians/061.png)

![](prs-4-93-user-manual-part-time-physicians/062.png)

If you answer YES at the “Confirm Unlock” prompt, a remarks prompt is displayed. The Supervisor may enter a short comment or phone number.

After the remarks are entered, the day is given a status of RESUBMIT.

![](prs-4-93-user-manual-part-time-physicians/063.png)

# Data Supplement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PTP ESR DATA FILE DESCRIPTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME</strong></th>
<th><strong>BRIEF DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ESR START TIME</td>
<td><p>The time the part-time physician actually began work/leave.</p>
<p>Time may be entered in any of the following formats: 8A or 8a, 8:00A, 8:15A, 8:15AM or military time: 0800, 1300; or MID or 12M for midnight; NOON or 12N for noon. Time must be in quarter hours; e.g., 8A or 8:15A or 8:30A or 8:45A.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ESR STOP TIME</td>
<td><p>The time the part-time physician actually stopped work/leave.</p>
<p>Time may be entered in any of the following formats: 8A or 8a, 8:00A, 8:15A, 8:15AM or military time: 0800, 1300; or MID or 12M for midnight; NOON or 12N for noon. Time must be in quarter hours; e.g., 8A or 8:15A or 8:30A or 8:45A.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ESR TYPE OF TIME</td>
<td><p>The type of time worked/leave taken. Following are the choices displayed if you enter a ?.</p>
<p>AA Authorized Absence</p>
<p>AD Adopt</p>
<p>AL Annual Leave</p>
<p>CB Family Care</p>
<p>HX Holiday Excused</p>
<p>DL Donor Leave</p>
<p>ML Military Leave</p>
<p>NL Non-pay Annual Leave</p>
<p>RG Regular Time</p>
<p>RL Restored Annual Leave</p>
<p>SL Sick Leave</p>
<p>WP Leave Without Pay</p></td>
</tr>
</tbody>
</table>

PTP ESR DATA FILE DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME</strong></th>
<th><strong>BRIEF DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESR SPECIAL CODE</td>
<td>A code which further describes the TYPE OF TIME entered. Only the appropriate choices that correspond to the TYPE OF TIME entered will be allowed. Enter a ? for a list of the appropriate choices.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESR MEAL TIME</td>
<td>The amount of time, if any, you took for a meal time.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DAILY ESR REMARKS</td>
<td>Any further comments you would like to enter.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESR DAILY STATUS</td>
<td><p>The status of the part-time physician's daily Electronic Subsidiary Record (ESR). The possible values are:</p>
<p>NOT STARTED</p>
<p>PENDING</p>
<p>SIGNED</p>
<p>RESUBMIT</p>
<p>APPROVED</p>
<p>DAY OFF.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PT PHYSICIAN DATE/TIME STAMP</td>
<td>The Date and Time the part-time physician electronically signed their daily ESR record.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESR SUPERVISOR REMARKS</td>
<td>Comments entered by the Supervisor after they have marked a daily ESR as RESUBMIT. This can be text up to 17 characters.</td>
</tr>
</tbody>
</table>

PTP ESR DATA FILE DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME</strong></th>
<th><strong>BRIEF DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ESR DAY LAST SIGN METHOD</td>
<td><p>This field indicates how the current ESR record was signed. If the employee signs the ESR day, then the status will be MANUAL POST. However, it is also possible for the software to sign the ESR day on behalf of the employee based on some other action such as supervisor approval of an electronic leave request, or auto-posting of an extended absence, or auto-posting of holiday excused The possible values are:</p>
<p>MANUAL POST</p>
<p>EXTENDED ABSENCE</p>
<p>LEAVE REQUEST</p>
<p>HOLIDAY</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

## WORK SUMMARY SCREEN DESCRIPTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD NAME</strong></th>
<th><strong>BRIEF DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>EMPLOYEE NAME</td>
<td><p>The employee’s name in the following format: LAST NAME followed by a comma; FIRST NAME or INITIAL; followed by a blank space; MIDDLE NAME or INITIAL; if applicable a blank space, JR, SR or INITIAL.</p>
<p>Example: <strong>LASTNAME,FIRSTNAME MI JR</strong></p>
<p>No periods are placed after either initials or titles.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>STATION NUMBER</td>
<td>The number assigned to a Department of Veterans Affairs (VA) Installation for identification and control purposes.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>T &amp; L UNIT</td>
<td>Time and Leave Unit. A number that identifies a specific group of employees for time and leave tracking purposes.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SSN</td>
<td>The number used for identification and control purposes to refer to an employee.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NORMAL HOURS</td>
<td>This field contains the number of normal hours an employee is scheduled to work in a pay period</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DUTY BASIS</td>
<td>Code identifies the time basis that an employee is scheduled to work. An employee may have a full-time (1), part-time (2), intermittent (3) basis work schedule.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PAY PLAN</td>
<td>Code identifies the pay system under which the employee's Compensation is determined.</td>
</tr>
</tbody>
</table>

WORK SUMMARY SCREEN DESCRIPTIONS, cont.

| FIELD NAME               | BRIEF DESCRIPTION                                                                                                                                                                                                                  |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              |                                                                                                                                                                                                                                        |
| COMPRESSED/FLEXITIME CODE    | Indicates an employee is working a tour that is approved as a compressed or flextime schedule. The field can be blank or coded with a "C" for Compressed or "F" for flextime.                                                          |
|                              |                                                                                                                                                                                                                                        |
| FLSA                         | Code identifies whether an employee is covered under the Fair Labor Standards Act (FLSA) minimum wage and overtime provisions.                                                                                                         |
|                              |                                                                                                                                                                                                                                        |
| ANNUAL LEAVE CURRENT BALANCE | The annual leave balance this leave year to date.                                                                                                                                                                                      |
|                              |                                                                                                                                                                                                                                        |
| PAY PERIOD                   | This field contains the year-pay period in the form of YY-PP where YY represents the year and PP represents the pay period. This field reflects the pay period that was selected by the part-time physician from the action pick list. |
|                              |                                                                                                                                                                                                                                        |
| START DATE                   | The Start Date of the part-time physician’s 364 day Memorandum of Service Level Expectations. The Start Date will always be the first day of a pay period. The memorandum will cover exactly 26 full pay periods.                      |
|                              |                                                                                                                                                                                                                                        |
| END DATE                     | The End Date of the part-time physician's 364 day Memorandum of Service Level Expectations. The End Date will always be the last day of a Pay Period.                                                                                  |

WORK SUMMARY SCREEN DESCRIPTIONS, cont.

| FIELD NAME             | BRIEF DESCRIPTION                                                                                                                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                            |                                                                                                                                                                                                                                                    |
| AGREED \# OF HOURS         | The number of hours that the part-time physician agreed to work during their 364 day memorandum. This number must be equally divisible by 26.                                                                                                      |
|                            |                                                                                                                                                                                                                                                    |
| TOTAL HOURS WORKED         | The total hours worked by the part-time physician since the beginning of their memorandum. This includes both scheduled tour hours and extra hours worked.                                                                                         |
|                            |                                                                                                                                                                                                                                                    |
| AVE HRS/PP TO COMPLETE MEM | The average number of hours that the part-time physician will have to work to meet the Agreed Hours in their Memorandum of Service Level Expectations.                                                                                             |
|                            |                                                                                                                                                                                                                                                    |
| AGREED \# OF HOURS         | The number of hours that the part-time physician agreed to work during their 364 day memorandum. This number must be equally divisible by 26 (the number of pay periods in a calendar year).                                                       |
|                            |                                                                                                                                                                                                                                                    |
| % OF HOURS COMPLETED       | The percentage of scheduled hours completed since the beginning of the memorandum. This percentage reflects any AWOL (Absent Without Leave) hours that might have occurred during the memorandum. This field would also include any Non Pay hours. |

WORK SUMMARY SCREEN DESCRIPTIONS, cont.

| FIELD NAME | BRIEF DESCRIPTION                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                |                                                                                                                                                                                                                      |
| % OFF TARGET   | The percentage that the part-time physician is either ahead or behind on meeting their Agreed Hours. This percentage is based on the part-time physician's total Hours Worked and their Normal Hours per Pay Period. |
|                |                                                                                                                                                                                                                      |