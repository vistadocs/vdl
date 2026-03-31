---
title: Occurrence Screen Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: QAO
app_name: Occurrence Screen
section: FIN
app_status: active
pkg_ns: QAO
patch_ver: 3
patch_id: QAO*3
group_key: "QAO:QAO:3"
file_numbers: []
security_keys: []
menu_options: 0
description: This software supports the Occurrence Screening process as described in the VHA (Veterans Health Administration) circular. It gathers and manipulates data for the following Occurrence Screens.
audience: 
keywords: 
  - occurrence
  - peer
  - table
  - review
  - contents
  - date
  - service
  - clinical
  - report
  - reviewer
page_count: 0
word_count: 7609
section_count: 13
table_count: 51
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2016
revision_count: 1
revision_newest: 3/9/09
revision_oldest: 3/9/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=49"
---

![](occurrence-screen-version-3-user-manual/001.png)

Occurrence Screen V. 3.0User ManualSeptember 1993

Revised for Patch QAO\*3\*10 June 2016

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/9/09

|          |                                                                                                                                                   |                     |                      |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.)                                                                                                             | Project Manager | Technical Writer |
| 6/2016   | Per patch QAO\*3\*10, on page 1, in section “Return to OR in same admission (Screen 107)” removed the line “Surgeries not classified as MAJOR.”   | REDACTED            | REDACTED             |
| 3/2015   | Added justified exception. P [1](#introduction). (QAO\*3\*9). Added revision date to title page. Added revision date and patch number to footers. | REDACTED            | REDACTED             |
| 3/9/09   | Reformatted Manual                                                                                                                                |                     | REDACTED             |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Overview](#overview)
  - [Functional Description](#functional-description)
- [# Orientation](#orientation)
  - [Date Range Selection](#date-range-selection)
  - [Multiple Patient Selection](#multiple-patient-selection)
- [# Package Management](#package-management)
- [# Package Operation](#package-operation)
  - [Menu Description](#menu-description)
  - [Occurrence Screen User Menu](#occurrence-screen-user-menu)
    - [Basic Occurrence Data](#basic-occurrence-data)
    - [Clinical, Peer, Manager Review](#clinical-peer-manager-review)
    - [Committee Review](#committee-review)
    - [Enter New Occurrence](#enter-new-occurrence)
    - [Final Disposition](#final-disposition)
    - [Inquire Occurrence Screen Record](#inquire-occurrence-screen-record)
    - [Quick Exception Edit](#quick-exception-edit)
    - [Reports Menu](#reports-menu)
    - [Worksheets](#worksheets)
  - [Open Closed/Deleted Occurrence Screen Record](#open-closeddeleted-occurrence-screen-record)
  - [Package Setup Menu](#package-setup-menu)
    - [Clinical Reviewers](#clinical-reviewers)
    - [Committees](#committees)
    - [Medical Teams](#medical-teams)
    - [Reasons for Clinical Referral](#reasons-for-clinical-referral)
    - [Site Parameters](#site-parameters)
    - [Treating Specialty Care Types](#treating-specialty-care-types)
    - [VAMC-Specific Screens](#vamc-specific-screens)
  - [Purge/Delete Menu](#purgedelete-menu)
    - [Auto Enrollment Run Dates Purge](#auto-enrollment-run-dates-purge)
    - [Delete Occurrence Screen Record](#delete-occurrence-screen-record)
    - [Purge Deleted Occurrence Screen Records](#purge-deleted-occurrence-screen-records)
  - [Reports Menu](#reports-menu-1)
    - [Audit File Inquiry](#audit-file-inquiry)
    - [Display Treating Specialty Care Types](#display-treating-specialty-care-types)
    - [Enrollment Dates Tally](#enrollment-dates-tally)
    - [Practitioner Code List](#practitioner-code-list)
    - [Reliability Assessment Worksheets](#reliability-assessment-worksheets)
  - [Run Auto Enrollment Manually](#run-auto-enrollment-manually)
  - [Summary of Occurrence Screen Transmission](#summary-of-occurrence-screen-transmission)
- [Glossary](#glossary)
- [Option Index](#option-index)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software supports the Occurrence Screening process as described in the VHA (Veterans Health Administration) circular. It gathers and manipulates data for the following Occurrence Screens.

*Readmission within 10 days (Screen 101.1)*

Justified exceptions excluded by the software.

- Scheduled readmission
- Prior discharge AMA (against medical advice) or Irregular
- Readmission to NHCU (Nursing Home Care Unit), Intermediate Medicine, or Domiciliary

Justified exceptions that cannot be excluded by the software.

- Readmission for alcohol or drug abuse, chemotherapy, or radiation therapy
- Condition precipitating readmission didn't exist at time of prior admission

*Admission within 3 days following unscheduled Ambulatory Care visit (Screen 102)*

Justified exceptions excluded by the software.

- Scheduled admission
- Admission same day as visit
- Admission to Psychiatry Service, NHCU, Intermediate Medicine, or Domiciliary

*Return to OR in same admission (Screen 107)*

Justified exceptions excluded by the software.

- Two operations separated by more than 7 days
- Second procedure unrelated to first
- Planned multiple stage procedure documented prior to first surgery (when the case is scheduled prior to the first surgery being done)

Justified exceptions that cannot be excluded by the software.

- Planned multiple stage procedure documented prior to first surgery (when the case is not scheduled prior to the first surgery being done)
- Second operation in response to findings from first procedure

Overview

*Death (Screen 109)*

Justified exceptions excluded by the software.

- No justified exceptions can be excluded by the software

Justified exceptions that cannot be excluded by the software.

- DNR (do not resuscitate) order or local equivalent at time of admission or more than 7 days prior to death
- Admitted for palliative (terminal) care

> **NOTE:** If any of the above justified exceptions that are excluded by the software are not being excluded at your site, please review your package setup.

Provisions are made within the package for the addition of other hospital-specific screens. National screens that were discontinued through policy changes are listed in the package as "Inactive" but may be made "Local" to reactivate them. They are as follows.

1. Readmission within 14 days. (Screen 101)
2. Admission within 3 days following Ambulatory Care surgery procedure. (Screen 103)
3. Admission or ASIH from VA Nursing Home Care Unit.

a\. Within 14 days of discharge from Acute Care. (Screen 104.1)

b\. To Psychiatry Service. (Screen 104.2)

4. Transfer from Intermediate Medicine.

a\. Within 14 days of transfer from Acute Care. (Screen 105.1)

b\. To Psychiatry Service. (Screen 105.2)

5. Transfer to a Special Care unit within 72 hours of a surgical procedure. (Screen 106.2)
6. Transfer to a Special Care Unit within 72 hours of transfer from a Special Care Unit. (Screen 106.1)
7. Cardiac or respiratory arrest. (Screen 108)

## Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Occurrence Screen package is a component of the Quality/Risk Management sub-system within the VistA (Veterans Health Information Systems and Technology Architecture) system. It is designed to be used as a tool to accomplish the following.

- Automate the gathering of Occurrence Screen data. This is accomplished by a daily running of the automatic enrollment routine, which captures screens 101.1, 102, 107 (when site is using the VistA Surgery package) and 109. Refer to the Overview section above for a listing of types of justified exceptions that are excluded by the software. There is provision for the manual entry of screens if they cannot be or were not auto enrolled from data currently available in the VistA system.
- Provide for the inclusion of hospital-specific screens within the program. These screens must be entered manually. It also allows continued tracking of the screens that are no longer required.
- Automate the creation of clinical, peer, management, and committee worksheets. The findings and/or actions of the previous review levels can be printed.
- Facilitate the tracking of occurrences by means of various tracking reports. An ad hoc report feature is included for use in trend analysis.
- Produce the Semi-Annual Summary of Occurrence Screening.

# # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The format of this manual is summarized in the Table of Contents. The Glossary defines general terms relevant to Occurrence Screening and computer use. The following summarizes some of the VA FileMan functions that are used within the Occurrence Screen package.

Exiting

Depending on where you are within the program, entering an "up-arrow" (compressing the shift key while striking the 6) will allow you to jump to the beginning of a new record or to the menu options. Then pressing the enter key until you pass through the different levels of the menus will exit you from the program or back to the menu option you wish to use.

Help (?, ??, or ???)

Whenever you are unclear on the definition of a menu option or on how to respond to a prompt, one, two, or three question marks (three are always used for explanations of menu options) may be entered to obtain an explanation.

Deleting

Deleting default answers that appear before a "//" or a "Replace" is done by entering @ (compressing the shift key while striking the 2). Deleting word processing is done by using the delete key while on the same line of text. Text on a different line can only be deleted through "EDIT option". While in word processing, you may enter ? after "EDIT option:" to obtain a list of possible edits to the text.

Device

Striking the \<RET\> or \<CR\> key following the "DEVICE:" prompt will print the requested output on the computer screen. If a "Right Margin" prompt shows, you will need to strike the \<RET\>/\<CR\> key once again. Enter the name of the printer/device following the "DEVICE:" prompt to print a hard copy of the output.

Patient Look-ups

When prompted to enter a patient name, use at least two letters of the last name to identify the patient. Entering only a single letter in the Occurrence Screen package will bring up the text description for each screen beginning with that letter or the program will give you a "??" following the letter.

On-Line Documentation

On-line documentation is provided in the form of Help throughout the program. At any time you become unsure of how to respond to a prompt, simply enter ?, ??, or ??? to obtain more information. Generally this package provides all on-line documentation for individual prompts by entering ? or ??. To obtain brief descriptions of each option within a menu, enter ??? following the "Select...Menu Option:". Description of the menu options can also be found under the Package Operation and throughout the instructional portion of this manual.

## Date Range Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the features of the Occurrence Screen package is the flexibility provided in the matter of dates to be used for inquiry and printouts. The date range prompts in Occurrence Screen follow a specific pattern throughout the package. Common date prompts are given in all instances where a range is desired, whether it be a month, quarter, year, semi-annual period or other. This feature is described below.

The basic prompt that will appear for date range selection is:

Monthly, Quarterly, Semi-Annual, Yearly, Fiscal Yearly, User Selectable

Select date range:

Next, you are prompted for a specific date range for the type of range you have chosen. If data is entered that cannot be interpreted as appropriate for the range selected, error messages are displayed and you are returned to the basic date prompt.

<u>Range</u> <u>Prompt</u> <u>Error Message(s)</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 45%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Monthly</td>
<td>Enter Month and Year:</td>
<td>Enter a month and year only</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Quarterly</td>
<td>Enter Quarter and Year:</td>
<td>Enter quarter period in this format: 1-92, 2/92, or 3 92</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Semi-Annual</td>
<td><p>Enter quarter Period and FY you wish Semi-Annual range to end with</p>
<p>Enter Quarter and Year:</p></td>
<td>Enter quarter period in this format: 2-92, 2/92, or 2 92</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Yearly</td>
<td>Enter YEAR:</td>
<td>Enter 2 or 4 digit year: 92 or 1992</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Fiscal Yearly</td>
<td>Enter FISCAL YEAR:</td>
<td>Enter 2 or 4 digit fiscal year</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>User Selectable</td>
<td><p>Enter beginning and ending dates for the desired time period:</p>
<p>Beginning Date:</p>
<p>Ending Date:</p></td>
<td>Standard error messages for date entries</td>
</tr>
</tbody>
</table>

When a date range is selected, it is displayed on the screen in this format for reference and you are prompted for printer device and/or other specific information necessary to perform the option.

RANGE SELECTED: JAN 1, 1992 TO JAN 31, 1992

## Multiple Patient Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this version of Occurrence Screen, we are giving you a choice of how you want to select patients for editing, closing, deleting, etc., for the following options:

Basic Occurrence Data

Clinical, Peer, Manager Review

Committee Review

Final Disposition

Quick Exception Edit

Worksheets

Open Closed/Deleted Occurrence Screen Record

In previous versions, you selected one patient and edited, closed, deleted, etc. the record. In this version, you can either continue using that method or you can use the method described here.

Selecting patients by Single/Multiple Records

Select one of the following:

1 Single/Multiple Records

2 Records by Date Range

Patient selection method: Single/Multiple Records// 1 Single/Multiple Records

Select PATIENT: OSPATIENT,ONE 11-09-92 102 OPEN 04-05-56 000456789 NSC VETERAN

Another one: OSPATIENT,TWO 11-09-92 101.1 OPEN 02-03-45 666456789 NSC VETERAN

Another one: \<RET\>

*The program then brings up each name as the prior patient edit is completed.*

Selecting patients by date range

Select one of the following:

1 Single/Multiple Records

2 Records by Date Range

Patient selection method: Single/Multiple Records// 2 Records by Date Range

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: USER SELECTABLE

Enter beginning and ending dates for the desired time period:

Multiple Patient Selection

Beginning Date: T-1 (NOV 09, 1992)

Ending Date: NOV 9,1992// \<RET\> (NOV 09, 1992)

Range selected: NOV 9,1992 to NOV 9,1992

When you select a date range, you get all the patients that had occurrences in that range.

If you decide you want this functionality, you need to "turn it on" using the Site Parameters option. Throughout the Package Operation section of this manual, we have the function "turned on" so you can see how it works with those options that use it.

# # Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occurrence screening is considered a Risk Management activity; therefore, Occurrence Screening records and documents stored and produced by this Occurrence Screen software are considered confidential and privileged. Title 38 U.S.C. 5705, as amended by Public Law 99-166, and the implementing HSRO (Health Services Review Organization) regulations (Title 38 Part 17) provide that HSRO records and documents which refer to individual practitioners are confidential and privileged. Exempt from this protection are aggregate statistical data, such as Occurrence Screening trend reports that do not identify individual VA patients or employees.

# # Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occurrence Screen Manager Menu - It is suggested that this menu which contains all the Occurrence Screen options be used by IRM and be given to the QM ADPAC.

Occurrence Screen User Menu - It is suggested that this menu be given to the QM Coordinators and or other staff responsible for entering occurrence data into VistA.

> Basic Occurrence Data - Used to enter or change the basic occurrence data in an Occurrence Screen record that is relevant to all review levels.

> Clinical, Peer, Manager Review - Used to enter and edit Clinical, Peer and Management reviews of occurrences.

> Committee Review - Used to enter and edit Committee reviews of occurrences that have equipment or system issues.

> Enter New Occurrence - Used to manually enter an occurrence into the system.

> Final Disposition - Used for a quick disposition of the record.

> Inquire Occurrence Screen Record - Allows the user to view any patient occurrence record.

> Quick Exception Edit - Used to quickly mark records as exceptions.

> Reports Menu - Main report menu for the Occurrence Screen package.

> Ad Hoc Reports - Allows the users to design their own reports from the data in the Occurrence Screen package.

> Adverse Findings - Produces a report of occurrences with care level findings of two or three.

> Delinquent Reviews - Produces a report showing peer and management reviews that have not been closed and are now past the due dates for review.

> Occurrences by Service - Produces a report of occurrences sorted by service with one service per page.

> Patients Awaiting Clinical Review - Produces a report showing which patients are still awaiting a clinical review.

> Review Level Tracking - Produces a report showing the findings or actions taken for all completed reviews.

Menu Description

> Service Statistics - Provides total numbers of occurrences for each service.

> Statistical Review Summary - Produces a compiled report of occurrences, findings, etc.

> Summary of Occurrence Screening (Semi-Annual Rpt.) - Produces the Summary of Occurrence Screening (Semi-Annual Report).

> System/Equipment Problems - Produces a report of occurrences found to be caused by system or equipment problems.

> Worksheets - Allows the user to print worksheets for all levels of review with or without any previously entered review data. You will get blank worksheets if you choose an occurrence that has no data entered or you may request blank worksheets.

Open Closed/Deleted Occurrence Screen Record - Allows the user to reopen a record for editing after it has been closed or deleted.

Package Setup Menu - The options within this menu should be populated when setting up the package. The options Site Parameters, Treating Specialty Care Types, and Clinical Reviewers must be completed prior to use of the auto enroll or the option Clinical, Peer, Manager Review.

> Clinical Reviewers - Used to enter or change the names of the people who are to be used as clinical reviewers.

> Committees - Used to enter/delete the names of the committees that will be conducting Occurrence Screen reviews.

> Medical Teams - Used to enter or change the names of medical teams within the facility.

> Reasons for Clinical Referral - Used to develop or change the list of reasons to refer a patient to second level review for all active Local screens.

> Site Parameters - Used to enter/edit the site parameters for the Occurrence Screen package.

> Treating Specialty Care Types - Used to enter or change the care type designations (Special, Acute, Intermediate, NHCU, and Psychiatry) for all active treating specialties. Note: For accurate auto enrollment of screens 101.1 and 102, the treating specialties must be entered by MAS at the time of a patient movement.

> VAMC-Specific Screens - Allows the user to enter site specific screens in the range of 201-999.99. Exceptions to these screens may also be entered. Screens can be marked as "Inactive" or "Local".

Menu Description

Purge/Delete Menu - Use this menu to delete records and to clean up your database, but use it with discretion. It is recommended that IRM and the QM ADPAC have this menu assigned to them.

> Auto Enrollment Run Dates Purge - Used to delete data for a range of dates from the Auto Enroll Run Dates file. This file contains the dates on which auto enroll was run and the number of patients auto enrolled for that date.

> Delete Occurrence Screen Record - Used to treat an Occurrence Screen record as deleted. A deleted record remains in the file, but it is invisible to the user. A record may be "undeleted" by using the Reopen Closed/Deleted Occurrence Screen Record option.

> Purge Deleted Occurrence Screen Records - Allow the site the ability to remove "deleted" records from the database.

Reports Menu: It is recommended that this Reports Menu be given to IRM and the QM ADPAC.

> Audit File Inquiry - Allows the user to pick an Occurrence Screen record and view the audit file entry for this occurrence. The audit file data includes information on who modified the record, when it was modified, and what modification was performed.

> Display Treating Specialty Care Types - Shows the treating specialties and the care types assigned to them.

> Enrollment Dates Tally - Produces a report showing the dates on which auto enroll ran or failed to run. For the dates auto enroll ran, the number of patients auto enrolled and manually entered is displayed.

> Practitioner Code List - Used to update and print a practitioner code listing.

> Reliability Assessment Worksheets - Provides worksheets for accomplishing the reliability assessment and computes the percentage of records reviewed for the assessment.

Run Auto Enrollment Manually - Runs auto enrollment for any given date in the past.

Summary of Occurrence Screen Transmission - Generates a bulletin that contains the statistical information found in the Summary of Occurrence Screening (Semi-Annual) report.

## Occurrence Screen User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Basic Occurrence Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the basic data in a patient's Occurrence Screen record. It contains fields for Ward/Clinic, Date, Screen, Severity of Outcome, Service, Treating Specialty, Medical Team, Attending, and Resident/Provider. Its use is not intended to add occurrence records to the file, but rather to augment data not captured at the time of auto or manual enrollment.

Changes to other portions of the patient's record must be made through the Clinical, Peer, Manager Review option, the Committee Review option, or the Final Disposition option.

Occurrence Screen User Menu

### Clinical, Peer, Manager Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the results of the review process. Data entered here is used for review tracking and for documenting the final disposition of each occurrence. The new functionality includes the following:

- ability to select a list of records for editing at the beginning of the option
- ability to bypass the basic occurrence data when entering more than one review level at a time
- ability to enter more than one service peer and management review.

You must show the final outcome of Peer review from each Service to which the occurrence is referred by answering YES to the "Final Peer Review:" prompt. If there is more than one Peer review for a single service, enter YES when the final Peer review findings are entered for that service. This affects data in the semi-annual report and the way the package manages peer attribution. (Management review here is the same as Service Chief review level.)

The basic occurrence data will appear only once, at the beginning of the review. Note that the Severity of Outcome now appears as part of the basic occurrence data.

The reasons for referral to second level review are different for each type of occurrence. These reasons may be edited using the Reasons for Clinical Referral option.

Be sure to enter the reviewing service. It affects the semi-annual report and protects the peer attribution by keeping the entries visible only to the corresponding service. Peer Attribution refers to those individuals, teams, or locations that probably contributed to the occurrence. These attribution fields relate to the service entered for the peer. Be sure to always enter a service for each peer reviewer. When more than one peer is reviewing the record, enter Peer again at the Review Level. This peer will be from a different service.

Occurrence Screen User Menu

### Committee Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Committee Review option is used to enter findings for system and/or equipment problems. A record cannot be closed through this option. A record can only be closed via the Clinical, Peer, Manager Review option or via the Final Disposition option.

Occurrence Screen User Menu

### Enter New Occurrence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to manually enter an occurrence into the system. Its main use would be to enter screens 107 and 108, the non-auto enrolled screens. Use this option to enter the occurrences into the software for any locally built screens or any national screens that cannot be auto enrolled.

Keep in mind when editing the Ward/Clinic field that this field determines the service for the Service Statistics report. The Service Statistics report is comprised of only the bed services.

Occurrence Screen User Menu

### Final Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to enter the final disposition for an occurrence. You are prompted for final disposition date and the review level at which the final disposition was reached.

Occurrence Screen User Menu

### Inquire Occurrence Screen Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a quick view of data in a patient's Occurrence Screen record in standard VA FileMan Inquiry format. All fields that contain data are shown including the coded Occurrence Identifier.

Occurrence Screen User Menu

### Quick Exception Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to enter exceptions more quickly than through the Clinical, Peer, Manager Review option. The user is prompted for a clinical reviewer, a patient, and the specific exception(s). The occurrence is then automatically marked as an exception and closed out.

Occurrence Screen User Menu

### Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ad Hoc Reports

Use this Ad Hoc option to design reports. Included for greater flexibility in your design are the following sort and print modifiers. For a more complete description on how to use the modifiers available in Ad Hoc Reports, see the QM Integration Module Version 1.5, User Manual.

*Sort Modifiers*

Macro functions: \[L Load sort macro \[S Save sort macro

\[O Output macro \[I Inquire sort macro \[D Delete sort macro

Sort prefixes: (e.g. enter +1 to turn on totaling for field 1)

\+ Totaled fields - Reverse sort order ! Sequence/ranking number

\# New page on sort @ Suppress sub-header ' Range without sorting

Sort suffixes: (e.g. enter 1;C5 to print the field 1 sub-header at column 5)

;Cn - Start the sub-header ;Ln - Use the first n characters of

caption at column n a field value for sorting

;Sn - Skip n lines every time the ;"xxx" - Use xxx as the sub-header

sort field value changes caption, for no caption ;""

*Print Modifiers*

Macro functions: \[L Load print macro \[S Save print macro

\[O Output macro \[I Inquire print macro \[D Delete print macro

Print prefixes: (e.g. enter !1 to turn on counting for field 1)

& Total ! Count + Total, Count & Mean

\# Total, Count, Mean, Maximum, Minimum, and Standard Deviation

Print suffixes: (e.g. enter 1;C5 to print the field 1 value at column 5)

;Cn - Start output at column n ;Yn - Start output at line n

Use ;C-n to start output n Use ;Y-n to start output n

columns from the right margin lines from the bottom margin

;Ln - Left justify data in an ;Rn - Right justify data in an

output field of n characters output field of n characters

Will truncate the output Will not truncate the output

;Wn - Wrap output in a field of n ;X - Omit spaces between print

characters, breaks at word fields and suppress the

divisions, default wrap ;W column header

;Sn - Skip n lines before printing ;Dn - Output numeric value with n

Use ;S to skip one line decimal places (rounds off)

;N - Do not print duplicated data ;T - Use field Title as header

;"" - Suppress column header ;"xxx" - Use xxx as column header

columns from the right margin lines from the bottom margin

  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

The following description shows you how to obtain a report of occurrences by ward/clinic. Then using VA File Manager modifiers, we show you how to change the appearance of the report. Sort and print choices are starred (\*). Note: You must accept every Clinic Service when using the sort field "Clinic Service". For all other sort fields, you are allowed to limit within the selection.

============= Occurrence Screen Ad Hoc Report Generator =============

1 Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Sort selection \# 1: 4 Date of Occurrence

Sort from: BEGINNING// \<RET\>  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

============= Occurrence Screen Ad Hoc Report Generator =============

1 Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 \* Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Sort selection \# 2 : 9 Ward/Clinic

Sort from: BEGINNING// \<RET\>  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

============= Occurrence Screen Ad Hoc Report Generator =============

1 Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 \* Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 \* Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Sort selection \# 3: 1 Occurrence Screen

Sort from: BEGINNING// \<RET\>  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

============= Occurrence Screen Ad Hoc Report Generator =============

1 \* Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 \* Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 \* Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Sort selection \# 4: \<RET\>  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

============= Occurrence Screen Ad Hoc Report Generator =============

1 Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier 26 Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team 34 Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Print selection \# 1: 1 Occurrence Screen

  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

============= Occurrence Screen Ad Hoc Report Generator =============

1 \* Occurrence Screen 21 Review Level (Clin,Peer,Mgmt)

2 Patient Name 22 Reviewer Name

3 Social Security Number 23 Reviewer Service

4 Date of Occurrence 24 Reviewer Findings

5 Screen Status 25 Reviewer Actions

6 Occurrence Identifier 26 Reviewer Comments

7 Associated Admission 27 Date Review Completed

8 Severity of Outcome 28 Reviewer Elapsed Days

9 Ward/Clinic 29 Primary Reason Clin Referral

10 Service/Section 30 Reason for Exception

11 Bed Service 31 Final Peer Review Per Service

12 Clinic Service 32 Committee

13 Treating Specialty 33 Committee Confirmed Issue

14 Medical Team 34 Committee Comments

15 Attending Physician 35 Peer Attrib (Individual)

16 Resident/Provider 36 Serv Peer Attrib (Individual)

17 Status (Open,Closed,Deleted) 37 Peer Attrib (Med Team)

18 Final Disposition Date 38 Serv Peer Attrib (Med Team)

19 Final Disposition Authority 39 Peer Attrib (Hosp Loc)

20 Total Elapsed Days 40 Serv Peer Attrib (Hosp Loc)

Print selection \# 2: \<RET\>

Do you want the report to include 'deleted' records? NO// \<RET\> (NO)

Do you want the report to include 'exception to criteria' records? NO//

\<RET\> (NO)

Enter special report header, if desired (maximum of 60 characters).

Occurrences by Ward/Clinic

DEVICE: \<RET\> RIGHT MARGIN: 80// \<RET\>  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

Take a close look at the information in this report. Each date that had an occurrence is shown with the ward/clinic and occurrence listed. This information can be presented in a clearer format. Take a look at the next page.

Occurrences by Ward/Clinic FEB 16,1999 11:49 PAGE 1

Screen

-----------------------------------------------------------------------------

Occurrence Date: DEC 6,1998

Ward/Clinic: 1 WEST

101.1

Occurrence Date: DEC 21,1998

Ward/Clinic: 1 WEST

102

Occurrence Date: FEB 2,1999 12:42

Ward/Clinic: 1 WEST

107

Occurrence Date: FEB 3,1999

Ward/Clinic: 1 EAST

102

102

201

201

Ward/Clinic: 1 NORTH

108

Ward/Clinic: 1 SOUTH

106.1

Ward/Clinic: 1 WEST

102

109

  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

Now let's modify the printout. Enter the following sort and print fields along with their modifiers.

The ' sort modifier will select this range but sort by the other chosen sort fields. This modifier is often used with a date field.

Sort by:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

'4 Date of Occurrence

The + sort modifier prints subtotals for the field. It must be present when the ! print modifier is used. The C5 and C25 will space each sort field respectively at the fifth column and the 25th column. The S1 used with ward/clinic will space one line whenever a new ward/clinic prints.

+9;C5;S1 Ward/Clinic

+1;C25 Occurrence Screen

At the "Sort selection \#1 :" prompt, enter each sort separated by a comma as shown here. This will save you steps.

Sort selection \#1 : '4,+9;C5;S1,+1;C25

The ! print modifier prints counts for the field. The count will begin in column 40 and the column will be titled "TOTALS".

Print by:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

!10;C40;"TOTALS" Ward/Clinic

  
Occurrence Screen User Menu*Reports Menu*Ad Hoc Reports

Here's what we printed. The count is for the date range we selected without sorting by each date. We added the date range to the header. Now our main sort is the ward/clinic field and within that Occurrence Screen. Note how much easier it is to see that 1 West had a total of 5 occurrences, one of which was a death. We also see that there were a total of 11 occurrences, 2 of which were locally defined types (201).

Number Occurrences by Ward/Clinic 10/98-2/99 FEB 16,1999 11:53 PAGE 1

TOTALS

-----------------------------------------------------------------------------

WARD/CLINIC: 1 EAST

Screen: 102

SUBCOUNT 2

Screen: 201

SUBCOUNT 2

SUBCOUNT 4

WARD/CLINIC: 1 NORTH

Screen: 108

SUBCOUNT 1

SUBCOUNT 1

WARD/CLINIC: 1 SOUTH

Screen: 106.1

SUBCOUNT 1

SUBCOUNT 1

WARD/CLINIC: 1 WEST

Screen: 101.1

SUBCOUNT 1

Screen: 102

SUBCOUNT 2

Screen: 107

SUBCOUNT 1

Screen: 109

SUBCOUNT 1

SUBCOUNT 5

COUNT 11

Occurrence Screen User Menu*Reports Menu*

#### Adverse Findings

This option produces a report (by service) of occurrences with care level findings of two or three for a selected date range. You may choose to include on the report the names of the following items, the codes of those items, or none of those items.

> attending physician resident/provider

> medical team

> attributions

Occurrence Screen User Menu*Reports Menu*

#### Delinquent Reviews

This option produces a report of open occurrences of peer and manager reviews whose completion dates are greater than the due date. Peer and management due and completed dates are shown. The report only looks for the first peer and management reviews for an occurrence. Delays cannot be determined for multiple reviews per level.

Delays can only be determined if the fields for Peer Review Days and Management Review Days are filled in through the Site Parameters option.

The “---“ line on the report indicates that the due date was not met.

Occurrence Screen User Menu*Reports Menu*

#### Occurrences by Service

This option produces a report of occurrences sorted by service. Information provided includes the patient name and ssn, date of occurrence, status of occurrence, and treating specialty.

Each service prints on a separate page.

Occurrence Screen User Menu*Reports Menu*

#### Patients Awaiting Clinical Review

This option produces a report for a selected date range listing those patients with open records who are awaiting a clinical review. You may choose to sort by the patient’s current ward/clinic or the ward/clinic where the occurrence took place.

Patients appear on the report in alphabetical order by screen.

Occurrence Screen User Menu*Reports Menu*

#### Review Level Tracking

This option produces a report by showing the findings or actions taken for all open occurrences with a clinical review already entered. All reviews in process as of the date the report is printed are listed.

Patients appear on the report in alphabetical order by screen.

Occurrence Screen User Menu*Reports Menu*

#### Service Statistics

This option produces a report showing the total number of occurrences per service over a user-selected date range. You may sort the report by criteria (Occurrence Screen) or by service.

Occurrence Screen User Menu*Reports Menu*

#### Statistical Review Summary

This option produces a statistical report showing the clinical review findings, the peer review findings by service, the management review actions by service, and the committee confirmed issue statistics.

Occurrence Screen User Menu*Reports Menu*

#### Summary of Occurrence Screening (Semi-Annual Rpt)

This option produces the Summary of Occurrence Screening (Semi-Annual) report. It is the same report as the one in the Occurrence Screen circular.

You may choose to print Part II of the report, Information on Program Operation. This includes sections on Improvement Actions, Results of the Reliability Assessments, Service-Specific Occurrences, and Facility Workload Data. You may also choose to print the pending occurrences.

Below are the definitions of the column headers in the Summary of Occurrence Screening (Semi-Annual Rpt).

\|CRITERION\|--# OF OCCURRENCES---\|--OUTCOME OF PEER REVIEW---\|-# OF OCCURRENCES-\|

\| SCREEN \| REVIEWED REFERRED \|LEVEL LEVEL LEVEL PENDING\| REFERRED FOR \|

\| \| CLINICALLY TO PEER \| 1 2 3 \| SYSTEM EQUIPMENT\|

\|=========\|=====================\|===========================\|==================\|

a b c d e f g h i

The following applies to all columns except that for Criterion Screen. Occurrence must:

1.  Be in date range chosen
2.  Be one of the screens chosen
3.  Must not be 'Deleted'
4.  Must have Clinical <u>and/or</u> Peer review(s)
5.  Clinical Finding must not = 3 "Exception to Criteria".

a Criterion

This is a listing of the chosen screen numbers in order.

b Reviewed Clinically

See 1-5 above with the exception that it must have a Clinical review entered.

c Referred to Peer

See 1-5 above and must have Clinical Action = 2 <u>or</u> have any Peer review per service without a Clinical review entered. The number will also be incremented when multiple service Peer reviews are done. Refer to the Multi-Service Review section of this guide for more in-depth description of how these numbers are incremented.

Occurrence Screen User Menu*Reports Menu*Summary of Occurrence Screening (Semi-Annual Rpt)d, e, f Outcome Of Peer Review, Number Final Ratings At (Levels 1, 2, 3)

The number is derived from the Peer Findings when Level 1, 2, or 3 is entered and Final Peer Review Per Service = Yes.

g Outcome Of Peer Review, Pending

Number derived from having a Clinical Action of Refer to Peer and No Peer Review, or Peer Review but no Service marked as Final.

h Number Of Occurrences, Referred System

When Clinical Findings are one of the following:

> 5 System Issue

> 7 Peer Review needed and System Issue

> 8 Peer Review Needed and Equipment and System Issues

> 9 Equipment and System Issues

i Number of Occurrences, Referred Equipment

When Clinical Findings are one of the following:

> 4 Equipment Issue

> 6 Peer Review Needed and Equipment Issue

> 8 Peer Review Needed and Equipment and System Issues

> 9 Equipment and System Issues

Occurrence Screen User Menu*Reports Menu*

#### System/Equipment Problems

This option produces a report of occurrences caused by system and/or equipment problems. Information provided includes patient name, SSN, date, status, and confirmed issue.

Occurrence Screen User Menu

### Worksheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows printing of worksheets for all levels of review with or without any previously entered review data. You may print the Clinical Review Worksheet (Part 1 and 2), the Peer Review Worksheet, the Management Review Worksheet, or the Committee Review Worksheet.

Two of the Occurrence Screen site parameters affect the printing of worksheets. The *Clinical Worksheet Part 1* parameter must be set to YES for Part 1 of the Clinical Worksheet to print through this option. If the Auto-Print Clinical Worksheet parameter is set to YES, Clinical Worksheets will be automatically printed as part of the auto enrollment process.

## Open Closed/Deleted Occurrence Screen Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to reopen a record for editing after it has been closed or deleted. Reopening a record will delete all final disposition data. You will be given this warning upon selection of this option.

## Package Setup Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Clinical Reviewers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/delete the names of the individuals who will be performing clinical reviews. The software checks for the current holders of the Clinical Reviewer key upon selection.

Package Setup Menu

### Committees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/delete the names of the committees that will be conducting Occurrence Screen reviews. You may enter an abbreviation for the committee.

Package Setup Menu

### Medical Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the names of the medical teams who may be associated with occurrences. Medical teams are used in assigning attribution.

You may wish to not utilize this option if you do not use medical teams or have no need to assign attribution to them.

Package Setup Menu

### Reasons for Clinical Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows adding, editing, deleting of the reasons for clinical referral associated with each screen. These reasons appear in the clinical reviewer edit and on Part I of the Clinical Reviewer Worksheet.

The option also allows the manager to design a "reason for referral" list for every VAMC-specific screen.

Package Setup Menu

### Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the site parameters for the Occurrence Screen software. The following is an explanation of each parameter.

If you choose to not make an entry at the two r*eview days* prompts, you will not be able to print the Delinquent Reviews report.

*Peer Review Days*

This is the allowable number of days between the completion of the clinical review and the completion of the peer review.

*Management Review Days*

This is the allowable number of days between the completion of the clinical review and the completion of the management review.

*Min Time Between Logout & Adm*

Enter the minimum time, in hours, between a disposition log out and an admission. This time is used when auto enrolling admissions within 3 days following unscheduled ambulatory care visits. If the time between the log out and the admission is less than this time, the event will not be captured. If the time is greater than or equal to this time, it will be captured.

*Clinical Worksheet Part 1*

Part 1 of the Clinical Worksheet contains a list of Primary Reasons for Clinical Referral for the screen involved. When you print the worksheet, do you want Part 1 printed?

*Auto-Print Clinical Worksheet*

Do you want worksheets printed automatically when a patient is auto enrolled in Occurrence Screen?

*Allow Mult Patient Selection*

Entering YES here will allow selection of several patients at once for editing when utilizing several of the Occurrence Screen options. Entering NO will allow for selection of only one patient at a time.

Package Setup Menu*Site ParametersSurgery Package Installed*

The Surgery package must be running at your site. Entering YES will allow auto enroll to scan the Surgery package for Screen 7, Return to the O.R. in the Same Admission.

*Select Scheduled Admission Clinic*

This field contains the clinic(s) that are used to schedule patient admissions. The data entered in this field is used by the auto enroll to determine which admissions are scheduled.

*Default OS Device*

This field contains the default printer device for Occurrence Screen. Auto-printed Clinical Worksheets will be routed to this device.

*Mutely-Divisional OS Facility*

Enter YES if your site is multi-divisional. A YES entered here will allow you to select a different auto enroll output device for each division.

*Select OS Hospital Division*

This prompt will only appear if you answered YES at the multi-divisional facility prompt. Enter the name of each hospital division followed by the auto enroll device for that division.

Package Setup Menu

### Treating Specialty Care Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the care type designations for user-selected treating specialties. When a question mark (?) is entered at the Select Treating Specialty prompt, the specialties already defined are listed first. Then the entire Facility Treating Specialty list follows if requested.

It is important to note that accurate auto enrollment of Screens 101.1, 102 and 106.1 is dependent upon the treating specialties being entered by MAS at the time of admission or transfer. All treating specialties in use at your site should be assigned a care type through this option; otherwise, auto enroll may fail to capture some occurrences.

Package Setup Menu

### VAMC-Specific Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter site specific screens in the range 201-999.99. Medical centers may enter their own screens (201 through 999.99), but may not change existing national screens (101.1,102,107,109). Screens may not have any trailing zeros or decimal points.

The option allows the user to set the screen status to either local or inactive. Exceptions to screens may also be entered.

Refer to the Reasons for Clinical Referral option if you want to develop a list of reasons to refer a record to second level review for each VAMC-specific screen.

## Purge/Delete Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Enrollment Run Dates Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this option is to eliminate old entries from the QA Occurrence Auto Run Dates file. This file contains the dates on which auto enroll was run and the number of patients auto enrolled for that date.

Before using this option, be sure auto enroll ran on every day you wish to delete.

  
Purge/Delete Menu

### Delete Occurrence Screen Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option permits you to mark an Occurrence Screen record as “deleted” and should be used when inadvertent entries are made. Note that the record is not actually deleted from the file, but the status is changed to "deleted" so that it does not appear as either open or closed when inquiry is made to the file during normal processing. If necessary, the record’s deleted status may be changed by using the Reopen Closed/Deleted Occurrence Screen Record option.

To remove deleted cases from the file, use the Purge Deleted Occurrence Screen Records option.

Purge/Delete Menu

### Purge Deleted Occurrence Screen Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Deleted Occurrence Screen Records option is used to delete the Occurrence Screen records that have been marked as deleted.

This option purges those Occurrence Screen records flagged as deleted once these records have been purged they cannot be recovered. You will be given this warning upon this option selection.

## Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Audit File Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to pick an Occurrence Screen record and view the audit file entry for this occurrence. The audit file data includes information on who modified the record, when it was modified, and what modification was performed.

Reports Menu

### Display Treating Specialty Care Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a listing of all the treating specialties in use at your facility and their associated care type (acute, special, intermediate care, NHCU, or psychiatry). Any specialty without a designated care type will show as

\*\*\*NOT SPECIFIED\*\*\*.

The report may be sorted by care type or by specialty.

Reports Menu

### Enrollment Dates Tally

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report showing the dates on which auto enroll ran or failed to run. For the dates auto enroll ran, the number of patients auto enrolled and manually entered is displayed.

If you answer YES to *Include retired national screens?* prompt, all inactive screens will appear and question marks will show up where the tallies should be.

Reports Menu

### Practitioner Code List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report showing the names and code numbers (DUZ) of the resident/providers and attending physicians that have been entered into the Occurrence Screen software package. Only practitioners who have been linked with occurrences will be found on this list.

If sorted by code, the DUZ numbers will be in ascending numerical order.

Reports Menu

### Reliability Assessment Worksheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option randomly selects occurrences, within user specified parameters, and prints worksheets for the assessment of inter-reviewer reliability. The user may select a data range, the type of screens to include (national, local, inactive) and the number of occurrences to capture. Since this option is used to print a large number of worksheets, it must be queued.

This option automatically computes the percentage of occurrences reviewed for reliability by taking the number of occurrences captured for the reliability assessment and dividing first by total clinical reviews and then by total peer reviews. It prints worksheets for each occurrence that contain data from the original reviews. If you wish, you may also request blank worksheets for each occurrence.

## Run Auto Enrollment Manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to set up special runs or reruns of auto enrollment. The Enrollment Dates Tally report can be printed to tell you which dates auto enrollment did not run.

If you run auto enrollment manually for a day on which it previously ran, (such as a rerun) a message appears on the output stating that the records are already in the file and duplicate entries will not be made into Occurrence Screening. A report of occurrences enrolled will be produced.

Running this option may not pick up all patients for Screen 106.1. Any 106.1 that has been discharged after the date selected to run auto enrollment manually will not be captured.

## Summary of Occurrence Screen Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a MailMan message that contains the statistical information found in parts one and two of the Summary of Occurrence Screening (Semi-Annual) report. The user will be prompted for those data elements that are not saved in the Occurrence Screen database - reviewer reliability assessment and workload data.

The message is automatically sent to the National Quality Assurance Data Base (NQADB) at the Hines CIOFO. Once the data has been loaded into the NQADB, it may be viewed and used by the facility, region, and VACO as appropriate.

Semi-annual date range is automatically selected as the date range.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                      |                                                                                                                                                                                                                                                                                                               |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC                                   | Acute Care Unit                                                                                                                                                                                                                                                                                               |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Action                               | Corrective or referral response taken as a result of an adverse finding on a review of an occurrence.                                                                                                                                                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Adverse findings                     | Any findings above Level 1 care or any system and/or equipment problem.                                                                                                                                                                                                                                       |
|                                      |                                                                                                                                                                                                                                                                                                               |
| AMA                                  | Against Medical Advice                                                                                                                                                                                                                                                                                        |
|                                      |                                                                                                                                                                                                                                                                                                               |
| ASIH                                 | Absent Sick In Hospital (nursing home patient).                                                                                                                                                                                                                                                               |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Attending physician                  | The staff physician responsible for the care of the patient involved in the occurrence.                                                                                                                                                                                                                       |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Attribution                          | Individuals, medical teams, or hospital locations involved in an occurrence. This is used for documentation and trend analysis, and is not necessarily used to assign blame.                                                                                                                                  |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Auto enrollment                      | The computer process that automatically extracts Occurrence Screens from daily admissions, transfers, and discharges.                                                                                                                                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Auto-print                           | The computer process that produces printed documentation or reports without a specific request from the user. This is a part of auto enrollment.                                                                                                                                                              |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Closed occurrence                    | An occurrence for which final disposition was made.                                                                                                                                                                                                                                                           |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Committee                            | Any committee, such as Safety, that may be asked to review an occurrence involving a system and/or equipment problem.                                                                                                                                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Database                             | (See File)                                                                                                                                                                                                                                                                                                    |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Data dictionary                      | A description of the file containing the categories of data that the user requires to produce the desired reports and printed documentation.                                                                                                                                                                  |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Deleted occurrence                   | An occurrence record that is considered not to be a valid item, such as an error in data entry, and is eliminated from the statistics. It is not actually deleted from the file, but marked to be ignored (this is a security precaution) in the gathering of data.                                           |
|                                      |                                                                                                                                                                                                                                                                                                               |
| DNR                                  | Do Not Resuscitate                                                                                                                                                                                                                                                                                            |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Equipment problem                    | Having to do with the quality of the performance or design of equipment used, such as a respirator malfunction or broken wheelchair.                                                                                                                                                                          |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Exception                            | A valid reason to eliminate an occurrence from being considered for further review, such as planned readmission within 10 days of discharge.                                                                                                                                                                  |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Field                                | One typed entry of data contained within a computer file. (Several fields make up a file.) Often called a prompt.                                                                                                                                                                                             |
|                                      |                                                                                                                                                                                                                                                                                                               |
| File                                 | The computer's method of storing data required by the user. (See Field.) Sometimes also called a database.                                                                                                                                                                                                    |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Final disposition                    | The review of an occurrence was completed, corrective action (if any) was taken, and it is considered closed.                                                                                                                                                                                                 |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Findings                             | The categorized results of a review, such as optimal or Peer review needed.                                                                                                                                                                                                                                   |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Level 1 care                         | A finding that "Most practitioners would handle case similarly."                                                                                                                                                                                                                                              |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Level 2 care                         | A finding that "Most practitioners might handle case differently."                                                                                                                                                                                                                                            |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Level 3 care                         | A finding that "Most practitioners would handle case differently."                                                                                                                                                                                                                                            |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Manager reviewer                     | A Manager, such as a Service Chief or Chief of Staff, who is asked to review an occurrence for the purpose of taking action.                                                                                                                                                                                  |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Medical team                         | A group of practitioners responsible for the care of the patient as a team.                                                                                                                                                                                                                                   |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Menu                                 | A computer display from which the User selects a process for the computer to perform, such as print a report, enter or change data, etc.                                                                                                                                                                      |
|                                      |                                                                                                                                                                                                                                                                                                               |
| NHCU                                 | Nursing Home Care Unit                                                                                                                                                                                                                                                                                        |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Occurrence Screen                    | A process whereby cases are identified which meet specified criteria.                                                                                                                                                                                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Open occurrence                      | A record of an occurrence still undergoing the review process.                                                                                                                                                                                                                                                |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Option                               | A menu or one of the items in a menu.                                                                                                                                                                                                                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                               |
| OR                                   | Operating Room                                                                                                                                                                                                                                                                                                |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Parameter                            | A computer term referring to information supplied to the computer by the user in order to set up the programs to perform particular functions required.                                                                                                                                                       |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Peer reviewer                        | A Peer or committee of Peers that is asked by the Clinical reviewer to review an occurrence for a practitioner related issue.                                                                                                                                                                                 |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Practitioner                         | A licensed performer of medical services, such as a doctor.                                                                                                                                                                                                                                                   |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Primary Reason for Clinical Referral | The main purpose that a record is sent for further review, such as Peer, Manager or Committee.                                                                                                                                                                                                                |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Provider                             | Any practitioner who is responsible for some portion of the care of the patient.                                                                                                                                                                                                                              |
|                                      |                                                                                                                                                                                                                                                                                                               |
| QM                                   | Quality Management                                                                                                                                                                                                                                                                                            |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Queue                                | The process by which computer programs are scheduled to run at specific times.                                                                                                                                                                                                                                |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Reopen                               | In the event that an occurrence is closed or deleted prematurely or in error, this function will reopen it for review.                                                                                                                                                                                        |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Resident/provider                    | Any practitioner considered in "resident" status by the facility and is responsible for the care of the patient involved in an occurrence.                                                                                                                                                                    |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Review level                         | A level in the review process. The levels used in Occurrence Screening are Clinical, Peer, Manager and Committee.                                                                                                                                                                                             |
|                                      |                                                                                                                                                                                                                                                                                                               |
| RM                                   | Risk Management                                                                                                                                                                                                                                                                                               |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Run dates                            | The dates on which Auto Enrollment ran.                                                                                                                                                                                                                                                                       |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Second level review                  | As used in this documentation, second level review refers to any Peer review for a practitioner related issue or any committee review for an equipment or system issue.                                                                                                                                       |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Severity of outcome                  | The actual or anticipated injury to the patient, ranging from no injury or disability to death.                                                                                                                                                                                                               |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Treating specialty                   | The area of hospital treatment under which the occurrence happened.                                                                                                                                                                                                                                           |
|                                      |                                                                                                                                                                                                                                                                                                               |
| Worksheet                            | A computer-produced sheet containing an organized listing of data that a reviewer needs to enter into the computer. The reviewer can check off findings, actions, etc. It is intended both as a labor-saving device and a method of organizing data in the sequence in which the computer will request input. |

# Option Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ad Hoc Reports

Adverse Findings

Audit File Inquiry

Auto Enrollment Run Dates Purge

Basic Occurrence Data

Clinical, Peer, Manager Review

Clinical Reviewers

Committee Review

Committees

Delete Occurrence Screen Record

Delinquent Reviews

Display Treating Specialty Care Types

Enrollment Dates Tally

Enter New Occurrence

Final Disposition

Inquire Occurrence Screen Record

Medical Teams

Occurrences by Service

Open Closed/Deleted Occurrence Screen Record

Patients Awaiting Clinical Review

Practitioner Code List

Purge Deleted Occurrence Screen Records

Quick Exception Edit

Reasons for Clinical Referral

Reliability Assessment Worksheets

Review Level Tracking

Run Auto Enrollment Manually

Service Statistics

Site Parameters

Statistical Review Summary

Summary of Occurrence Screen Transmission

Summary of Occurrence Screening (Semi-Annual Rpt)

System/Equipment Problems

Treating Specialty Care Types

VAMC-Specific Screens

Worksheets