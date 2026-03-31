---
title: Incomplete Records Tracking (IRT) Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: DGJ
app_name: Incomplete Records Tracking (IRT)
section: CLI
app_status: active
pkg_ns: DGJ
patch_ver: 1
patch_id: DGJ*1
group_key: "DGJ:DGJ:1"
file_numbers: []
security_keys: []
menu_options: 1
description: - [Introduction 1](#introduction-1) - [Orientation 3](#orientation-3) - [Incomplete Records Tracking Menu 5](#incomplete-records-tracking-menu-5) - [Glossary 19](#glossary-19) - [The Incomplete Records Tracking (IRT) software is formerly a component of PIMS V. 5.3. With PIMS V. 5.3, it includes many
audience: 
keywords: 
  - report
  - reports
  - physician
  - date
  - incomplete
  - record
  - deficiency
  - days
  - deficiencies
  - number
page_count: 0
word_count: 4388
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=124"
---

![](incomplete-records-tracking-irt-version-1-user-manual/001.png)

Incomplete Records Tracking (IRT)User Manual

April 2002

V*IST*A Software Design & Development

Table of Contents

## Introduction 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On-Line Help 3

## Incomplete Records Tracking Menu 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add a New/Edit Deficiency 5

> Delete an IRT 6

> Edit a Complete IRT 7

> Enter/Edit an IRT 8

> IRT Update Std. Deficiencies 9

> Print Menu 10

> Incomplete Reports Print 10

> Physician Deficiency Report 11

> Transcription Productivity Report 12

> Undictated Reports Print 14

> Set up IRT Parameters 15

> View an IRT Record 17

## Glossary 19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

# The Incomplete Records Tracking (IRT) software is formerly a component of PIMS V. 5.3. With PIMS V. 5.3, it includes many enhancements that should allow the users greater flexibility and efficiency when tracking incomplete records.


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Introduction 1](#introduction-1)
  - [Orientation 3](#orientation-3)
  - [Incomplete Records Tracking Menu 5](#incomplete-records-tracking-menu-5)
  - [Glossary 19](#glossary-19)
- [The Incomplete Records Tracking (IRT) software is formerly a component of PIMS V. 5.3. With PIMS V. 5.3, it includes many enhancements that should allow the users greater flexibility and efficiency when tracking incomplete records.](#the-incomplete-records-tracking-irt-software-is-formerly-a-component-of-pims-v-53-with-pims-v-53-it-includes-many-enhancements-that-should-allow-the-users-greater-flexibility-and-efficiency-when-tracking-incomplete-records)
- [On-Line Help](#on-line-help)
- [Add a New/Edit Deficiency](#add-a-newedit-deficiency)
- [DEFAULT MEDICAL RECORD TYPE](#default-medical-record-type)
- [ASIH Absent sick in hospital](#asih-absent-sick-in-hospital)
The package now tracks all types of deficiencies, in addition to those already being tracked (Discharge and Interim Summaries and OP Reports). The sites will have the ability to add the deficiencies they wish to track to make this package more site specific.
The Physician for Deficiency will be tracked throughout the IRT process. The users will know who is responsible for the deficiency at various stages of tracking, from entry through completion.
The following is a brief description of each IRT option.
ADD A NEW/EDIT DEFICIENCY
This option allows the site to add a new deficiency or edit an existing deficiency
Delete aN IRT
The Delete an IRT option is used to delete an incomplete operation report, interim summary, or discharge summary.
EDIT A COMPLETE IRT
This option allows editing of an IRT record that has already been completed.
ENTER/EDIT AN IRT
The Enter/Edit an IRT option is used to enter new IRT records and edit incomplete IRT records in the tracking system.
IRT UPDATE STD. DEFICIENCIES
This option will create IRT entries for the site's standard deficiencies for selected date range admissions.
PRINT MENU
> Incomplete Reports Print
> The Incomplete Reports Print option is used to produce a listing of operation reports, interim summaries, and discharge summaries that are incomplete or deficient for one or more of the following reasons: undictated, not transcribed, not signed, or not reviewed.
PHYSICIAN DEFICIENCY REPORT
> This option is used to produce a listing of all uncompleted deficiencies for a physician, patient, or service/specialty.
> TRANSCRIPTION PRODUCTIVITY REPORT
This option allows the user to print reports which track the number of days from the event date to the record being coded.
Undictated Reports Print
The Undictated Reports Print option is used to produce a listing of operation reports, interim summaries, and discharge summaries that have not been dictated within the required timeframe established through the site parameters at your site.
Set up IRT Parameters
The Set up IRT Parameters option is used to establish site specific parameters for the IRT module. It is also used to activate/inactivate the IRT module.
VIEW AN IRT RECORD
This option is used to display a patient’s list of deficiencies that are currently, or were previously, incomplete.
Orientation

# *On-Line Help*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements which provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". The HELP message will appear under the prompt, then the prompt will be repeated. For example, perhaps you see the prompt

> FACILITY TREATING SPECIALTY:

and you need assistance answering. You enter ? and the HELP message would appear.

Enter the TREATING SPECIALTY assigned to this patient with this movement.

> This must be an active treating specialty.

> Answer with FACILITY TREATING SPECIALTY NAME

> FACILITY TREATING SPECIALTY:

For some prompts, the system will list the possible answers from which you may choose. Any time choices appear with numbers, the system will usually accept the number or the name.

A HELP message may not be available for every prompt. If you enter a "?" or "??" at a prompt that does not have a HELP message, the system will repeat the prompt.

Incomplete Records Tracking (IRT) Menu

# Add a New/Edit Deficiency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add a New/Edit Deficiency option allows the site to add a new deficiency or edit an existing deficiency. This option should be utilized before using the IRT software as it establishes the deficiencies the site will track.

A list of deficiencies is sent out with the software. The deficiency name and category will be highlighted on the screen display and will not be editable. Deficiencies that are subsequently added by the site will not be highlighted on the screen display and can be edited. Neither can be deleted.

The Deficiency Parameter List screen will be displayed upon entering the option. You may only select from the deficiencies displayed on the screen. To move to a deficiency not displayed, enter “JC” at the “Select Action:” prompt.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

When entering an IRT, only those deficiencies that have been turned on by answering YES to the TRACK DEFICIENCY field will be choices for the user.

You may specify a deficiency as STANDARD through this option. When the IRT background job is run, an IRT entry will be created for each of the standard deficiencies for the previous day's admissions.

You must hold the DGJ SUPER security key to access this option.

Delete an IRT

The Delete an IRT option is used to delete an IRT entry. You must hold the DGJ CLERK SUPER security key to access this option.

At multidivisional facilities, you will be prompted for a division. Your selection should be the division where the entry you wish to delete was initiated. This is a required response if you wish to continue in the option; however, entry of an up-arrow \<^\> will exit the option and return you to the menu.

If the TRACK OUTPATIENT OP REPORTS site parameter is set to YES, you will be prompted for whether you wish to display inpatient or outpatient deficiencies. If the selected patient has more than one admission or outpatient operation date, they will be listed for selection.

The deficiencies for the selected date will be displayed. If there is more than one, you will be prompted to choose. If there are none, you will be so notified.

At the "Select Action:" prompt you may enter EP (Expand Deficiency) to view additional data or DL (Delete an IRT) to delete. The deficiency chosen for deletion will now be displayed. You will need to enter "QUIT" at the "Select Action:" prompt to get to the delete prompt. If you choose to delete, the first screen will then be redisplayed with the deficiency deleted.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Edit a Complete IRT

The Edit a Complete IRT option allows the editing of a completed IRT record. The criteria that determines if a record is complete is site specific. If the ARE REPORTS REVIEWED? IRT site parameter is set to YES, the record must be reviewed before it is considered complete. If the parameter is set to NO, the record is complete after it has been signed.

You must hold the DGJ CLERK SUPER security key to access this option.

At multidivisional facilities, you will be prompted for a division. Only those records meeting the criteria (for complete status) set for the specified division may be selected through this option.

If the TRACK OUTPATIENT OP REPORTS site parameter is set to YES, you will be prompted for whether you wish to display inpatient or outpatient deficiencies. If the selected patient has more than one admission or outpatient operation date, they will be listed for selection.

The deficiencies for the selected date will be displayed. If there is more than one, you will be prompted to choose. If the patient does not have a completed IRT record on file, you will be so notified.

At the "Select Action:" prompt you may enter EP (Expand Deficiency) to view additional data or CE (Complete IRT Edit) to edit. The deficiency chosen for editing will now be displayed. You may then select the data group(s) you wish to edit. You may not edit those fields marked by an asterisk (\*). After editing, the record will be redisplayed with the newly entered values.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

For the discharge summary type of report, only holders of the DGJ TS UPDATE security key will be able to edit the specialty, primary physician, and attending physician fields. The attending physician field will only appear if the ARE REPORTS REVIEWED? IRT site parameter is set to YES.

Enter/Edit an IRT

The Enter/Edit an IRT option is used to enter a new or edit an existing incomplete record in the IRT tracking system. The information entered/edited through this option is controlled by the IRT parameters for the selected division.

When a patient is transferred with an ASIH (absent-sick-in-hospital) movement, the pseudo discharge date of thirty days from the ASIH movement date is stored as the event date of the original IRT record and a new IRT record is created for the ASIH admission. If the patient returns before the 30 days is up, both of the IRT records (the original admission and the ASIH admission) are updated. The event date for the ASIH IRT record will be the date the patient returns to the original facility while the event date for the original admission IRT record will be the admission date. If the patient gets discharged while ASIH less than thirty days, both records will be updated with the same discharge date.

If a patient's admission is deleted, all corresponding IRT records are deleted. If a patient is discharged and no IRT record is on file, one is created for that admission.

If the TRACK OUTPATIENT OP REPORTS IRT site parameter is set to NO, the system will not track outpatient operation reports and you will not be able to enter them through this option.

For the discharge summary type of report, only holders of the DGJ TS UPDATE security key will be able to edit the specialty, primary physician, and attending physician fields. The attending physician field will only appear if the ARE REPORTS REVIEWED? IRT site parameter is set to YES.

The Record Tracking fields BORROWER, PHONE/ROOM, and DATE/TIME CHARGED have been added to the record display so that users can access the patient record more easily and update deficiencies in a timely manner.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

The screen displays the deficiencies by category; listing the category name and the deficiencies in that category below it. Only those deficiencies that have been activated through the Add a New/Edit Deficiency option can be selected when adding a new deficiency.

Several actions may be taken against the list of deficiencies: entering a new deficiency, editing an existing incomplete deficiency, displaying all the IRT data for a selected deficiency, updating the treating specialty, jumping from one category to another, and updating the status of a deficiency to COMPLETE (except for discharge summary, interim summary, and operation report). Users holding the DGJ SUPER security key will have the ability to delete an IRT entry and edit a completed IRT entry. If the key is not held, these functions will appear in parentheses and will not be selectable. You must hold the DGJ TS UPDATE security key to make changes to treating specialty data for discharge summaries.

IRT Update Std. Deficiencies

The IRT Update Std. Deficiencies option will create IRT entries for the site's standard deficiencies for those admissions that occurred within the selected date range. This option should be utilized only if the IRT Update Std. Def. Background Job option fails.

A bulletin will be sent to a specified mail group listing those patients within the chosen date range that have short form discharges (discharged within 48 hours of admission).

You must hold the DGJ SUPER security key to access this option.

  
Print MenuIncomplete Reports Print

The Incomplete Reports Print option is used to produce a listing of operation reports, interim summaries, and discharge summaries that are incomplete or deficient for one or more of the following reasons: undictated, not transcribed, not signed, or not reviewed. This option maybe used by transcriptionists to determine which reports or summaries are incomplete and need to be completed.

At multidivisional facilities, this report will print in alphabetical order by selected division name. You will have the ability to sort this report by patient name, event date, physician name, or service/treating specialty. Within divisions, all reports will print in alphabetical order except when sorting by event date. This report will print in chronological order.

You may generate this report for inpatients, outpatients, or both. You may choose to report one/many/all deficiencies and one/many/all incomplete record statuses. The report is printed for a selected date range by event date.

The following information will be displayed on the output, as appropriate, depending on how you choose to sort the report: division, patient name and ID number, event date, discharge type, location (if an inpatient, this will be the ward, if an outpatient, this will be the requesting clinic), report/summary type and status, current borrower of the record, physician (if the IRT parameters are set to review reports and the report needs to be reviewed, the physician shown will be the attending physician; if not, the physician listed will be the one responsible for completing the delinquent IRT record), service, specialty, and the total number of days since the event date.

If you sort by physician, the report will also contain a count of incomplete reports for each physician. If you sort by service/specialty, the report will contain the number of reports for each specialty and a subtotal count of reports for each service.

The "Total Days" column is calculated from the event date to the current date for all summaries listed with a status of INCOMPLETE. For summaries with a status other than INCOMPLETE, the total days will be computed as the number of days since the last event. For example, if the status is currently signed, the total days will be computed as the number of days since the summary was signed.

Also, a message may be displayed at the bottom of each page if the INCOMPLETE SUMMARIES MESSAGE IRT parameter contains an entry. This is a free text field entered through the Set up IRT Parameters option.

A division totals page is included at the end of each report. This page will show the division and the total number of delinquent reports for that division.

This report should be printed at 132 columns and queued to a printer.

Print MenuPhysician Deficiency Report

The Physician Deficiency Report option is used to produce a listing of all uncompleted deficiencies for a physician, patient, or service/specialty.

You will have the ability to sort this report by patient, physician name, or service/treating specialty. You may choose to report for one/many/all divisions and one/many/all deficiencies. You may generate this report for inpatients, outpatients, or both. The report is printed for a selected date range by event date.

You may choose to list/not list Summary category deficiencies on the output for those patients who have not yet been discharged.

The following information will be displayed on the output, as appropriate, depending on how you choose to sort the report: division, patient name and ID number, event date, status, physician, service/specialty, deficiency, admission date, borrower, phone and room number, and date record charged out. The last three elements are related to the Record Tracking package and specify where the patient's medical records are located.

The physician listed for the deficiency will be the physician responsible for the next action taken against this deficiency.

This report should be printed at 132 columns and queued to a printer.

Print MenuTranscription Productivity Report

The Transcription Productivity Report option allows the user to print reports which track the number of days from the event date to the record being coded. Its major sort is by physician (one/many/all) or service/treating specialty (one/many/all) and, at multidivisional facilities, divisions (one/many/all). The user may generate the report for inpatients, outpatients, or both. You may choose to print a report which includes patient lists only, a totals page only, or both patient lists and a totals page. You may choose to report one/many/all summary types. The report is printed for a selected date range by event date.

The following information will be displayed on the output, as appropriate, depending on how you choose to sort the report.

division

patient name

patient ID number

event date

physician

service

specialty

dictation date

location for inpatients, the ward; for outpatients, the requesting clinic

type of report discharge summary, op report, interim report

status undictated, dictated, transcribed, signed

DIC DATE date the record was dictated

D/C-DIC number of days from discharge to dictation

DIC-TRN number of days from dictation to transcription

TRN-COD number of days from transcription to coding

TOT DAYS total number of days from the event date to coding

DAYS DELQ number of days the record is delinquent

DELQ\>30 number of days over 30 that the record is delinquent

TOT REC total number of records

REC DELQ number of delinquent records

%DELQ\>30 percentage of incomplete records that are delinquent over

30 days

Any record not completed in 30 days or less is considered delinquent.

If you choose to sort by service/treating specialty and print the totals page, only the service names (not the specialty names) will be listed on the report.

Print MenuTranscription Productivity Report

While the actual number of days are provided on the patient lists, the average days for the following categories are shown on the totals page.

D/C-DIC DIC-TRAN

TRAN-COD DAYS DELQ

DELQ\>30

Reports generated through this option should be printed at 132 columns and queued to a printer.

Print MenuUndictated Reports Print

The Undictated Reports Print option is used to produce a listing of operation reports, interim summaries, and discharge summaries that have not been dictated within the required time frame established through the IRT site parameters at your site. This option could be used by transcriptionists to determine which reports or summaries are incomplete and to alert physicians which reports or summaries need to be dictated.

At multidivisional facilities, this report will print in alphabetical order by selected division name. You will have the ability to sort this report by patient name, event date, physician name, or service/treating specialty. Within divisions, all reports will print in alphabetical order except when sorting by event date. This report will print in chronological order.

You may generate this report for inpatients, outpatients, or both and you may choose to report one/many/all summary types. The report is printed for a selected date range by event date.

The following information will be displayed on the output, as appropriate, depending on how you choose to sort the report: division, patient name and ID number, event date, discharge type, location (if an inpatient, this will be the ward, if an outpatient, this will be the requesting clinic), current borrower of the record, report or summary type, physician (physician responsible for dictating the report), service, specialty, and the total number of days since the event date.

If you sort by physician, the report will also contain a count of undictated reports for each physician. If you sort by service/treating specialty, the report will contain the number of reports for each specialty and a subtotal count of reports for each service.

A message may be displayed at the bottom of each page if the INCOMPLETE SUMMARIES MESSAGE IRT parameter contains an entry. This is a free text field entered through the Set up IRT Parameters option.

A division totals page is included at the end of each report. This page will show the division and the total number of undictated reports for that division.

This report should be printed at 132 columns and queued to a printer.

Set up IRT Parameters

The Set up IRT Parameters option is used to establish site specific parameters for the IRT module and also to activate/inactivate the IRT module. You must hold the DGJ SUPER security key to access this option.

These site parameters determine the default physician responsible for dictating and signing the summary/report, whether review by another physician is required, the default physician (if any) responsible for reviewing the summary/report, whether outpatient operation reports are tracked, the number of days a physician has to dictate, sign, and review a summary/report before it is considered incomplete, any message you wish to have appear on the bottom of each page of the Incomplete Reports List or Undictated Reports List, and if short forms (admission and discharge within 48 hours) should have standard deficiencies created for them.

Listed below is a brief explanation of each site parameter.

MEDICAL CENTER DIVISION NAME

The name or number of the division for which you wish to set the IRT parameters. The division entered at this prompt must be in the MEDICAL CENTER DIVISION file.

TRACK INCOMPLETE SUMMARIES?

Enter YES to track incomplete summaries/reports. If NO is entered, the IRT module will be inactivated and no incomplete reports or summaries will be tracked. The system will maintain the default values of all other site parameters while the module is inactivated. When the IRT module is reactivated, those defaults will become effective.

DEFAULT PRIMARY PHYSICIAN

Select PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report entry is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default physician.

ARE REPORTS REVIEWED?

Enter YES if this division requires a second physician to review the summary/report. Enter NO if review by a second physician is not necessary.

DEFAULT REVIEWING PHYSICIAN

This prompt will only appear if YES was entered at the previous prompt. Enter PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report entry is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default physician.

Set up IRT ParametersDEFAULT PHYS. FOR SIGNATURE

Select PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report entry is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default physician.

TRACK OUTPATIENT OP REPORTS?

Enter YES if you want to track outpatient operation reports at this division. Enter NO to not track outpatient reports.

DAYS FOR DICTATION

The number of days (0-99) the physician has to dictate a summary/report before it is considered incomplete.

DAYS FOR SIGNATURE

The number of days (0-99) from the date of transcription the physician has to sign the summary/report before it is considered incomplete.

DAYS FOR REVIEW

The number of days (0-99) the reviewing physician has to review the report, once it has been signed, before it is considered incomplete. This prompt will only appear if the "ARE REPORTS REVIEWED" prompt is answered YES.

INCOMPLETE SUMMARIES MESSAGE

A free text message, 1-99 characters in length, which will appear on the reports generated by the Incomplete Reports Print and Undictated Reports Print options.

STD. DEFIC. FOR SHORT FORMS

Enter YES if you wish the IRT background job to create standard deficiencies for short form discharges (discharged less than 48 hours after admission).

# DEFAULT MEDICAL RECORD TYPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Record Type name used for Medical Records. If the entry is left blank, the default value will be MEDICAL RECORDS. This parameter is useful at sites which may have a different name for their Medical Records department.

View an IRT Record

The View an IRT Record option is used to display a patient’s list of deficiencies that are currently, or were previously, incomplete. This option would be used to determine what deficiencies exist in a particular report or summary or to determine what reports or summaries for a specific patient are still incomplete.

At multidivisional facilities, you will be prompted for a division. Your selection should be the division where the report you wish to view was initiated. This is a required entry if you wish to continue in this option; however, entry of an up-arrow \<^\> will exit the option and return you to the menu.

You will next be prompted for the patient record and whether you would like to view inpatient or outpatient reports. If you choose inpatient, you will be prompted for the admission for which you want to view the reports.

All reports meeting the criteria you have entered will be displayed in List Manager format. You may then select to expand on one or more of the reports listed by selecting "EP Expand Deficiency". The expanded entry will show some of the following information: patient name, type of report, event date, admission date, division, location, service, physician responsible, specialty, primary physician, and attending physician. For summaries, you can also view information about when and by whom the record was dictated, transcribed, signed, and reviewed.

You may view multiple IRT records during the same session.

Glossary

# ASIH Absent sick in hospital

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRT Incomplete Records Tracking

VISTA Veterans Health Information Systems and Technology Architecture