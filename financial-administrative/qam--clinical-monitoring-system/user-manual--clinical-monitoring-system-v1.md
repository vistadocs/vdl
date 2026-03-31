---
title: Clinical Monitoring System Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: QAM
app_name: Clinical Monitoring System
section: FIN
app_status: active
pkg_ns: QAM
patch_ver: 1
patch_id: QAM*1
group_key: "QAM:QAM:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Introduction](#introduction) - [# Orientation](#orientation) - [# Package Management](#package-management) - [Monitoring System Manager Menu](#monitoring-system-manager-menu) - [Group Edit](#group-edit) - [Patient Group](#patient-group) - [Manually Run Auto Enroll](#manually-run-auto-enroll) -
audience: 
keywords: 
  - monitor
  - date
  - fall
  - group
  - condition
  - auto
  - enroll
  - patient
  - class
  - table
page_count: 0
word_count: 11201
section_count: 10
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 2
revision_newest: 2/23/09
revision_oldest: 11/15/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=32"
---

![](clinical-monitoring-system-version-1-user-manual/001.png)

Clinical Monitoring System V. 1.0User ManualSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 11/15/04

|          |                                                                     |                     |                      |
|----------|---------------------------------------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.)                               | Project Manager | Technical Writer |
| 11/15/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data |                     | REDACTED             |
| 2/23/09  | Reformatted Manual                                                  |                     | REDACTED             |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [# Orientation](#orientation)
- [# Package Management](#package-management)
- [Monitoring System Manager Menu](#monitoring-system-manager-menu)
  - [Group Edit](#group-edit)
  - [Patient Group](#patient-group)
  - [Manually Run Auto Enroll](#manually-run-auto-enroll)
  - [Rationale Edit](#rationale-edit)
  - [Site Parameters Edit](#site-parameters-edit)
  - [Build Monitor Menu](#build-monitor-menu)
    - [Enter/Edit a Monitor](#enteredit-a-monitor)
    - [Copy/Edit a Monitor](#copyedit-a-monitor)
    - [Quick Monitor Edit](#quick-monitor-edit)
  - [Purge Menu](#purge-menu)
    - [Auto Enroll Run Dates File Purge](#auto-enroll-run-dates-file-purge)
    - [Fall Out File Purge](#fall-out-file-purge)
    - [History File Purge](#history-file-purge)
  - [Outputs Menu](#outputs-menu)
    - [Ad Hoc Fall Out Report](#ad-hoc-fall-out-report)
    - [Ad Hoc Monitor Report](#ad-hoc-monitor-report)
    - [Audit File Inquire](#audit-file-inquire)
    - [Auto/Manual Enroll Monitors Run](#automanual-enroll-monitors-run)
    - [Build a Monitor Worksheet](#build-a-monitor-worksheet)
    - [Condition File Inquire](#condition-file-inquire)
    - [Data Element File Inquire](#data-element-file-inquire)
    - [Fall Out File Inquire](#fall-out-file-inquire)
    - [Group File Inquire](#group-file-inquire)
    - [Monitor Description Report](#monitor-description-report)
    - [Monitor History Report](#monitor-history-report)
    - [Patients With Multiple Fall Outs](#patients-with-multiple-fall-outs)
  - [Monitoring System User Menu](#monitoring-system-user-menu)
    - [Fall Out Edit](#fall-out-edit)
    - [Sample Size Edit](#sample-size-edit)
    - [Outputs Menu](#outputs-menu-1)
- [Glossary](#glossary)
- [Option Index](#option-index)
The Clinical Monitoring System package is a fully integrated system compatible with Version 7.0 or later of Kernel and Version 19 or later of VA FileMan. The NEW PERSON file (#200) is required.
The heart of the Clinical Monitoring System package is in building monitors using conditions and groups for patient auto enrollment.
The main function of this software is to capture data for patients meeting specified conditions. All monitors within the framework of this software are ultimately based upon patient related data. In order to capture data, you create monitors that run nightly. These nightly runs "auto enroll" (or capture) the patients defined by the monitors.
This system looks at what happened yesterday in VistA. It can capture such items as ward, treating specialty, SSN, age, etc. For a more extensive list of items, use the Data Element File Inquire option within the Outputs Menu of the Monitoring System Manager Menu. Data elements available for capture vary depending on the conditions you select when building monitors.
Conditions are provided with the Clinical Monitoring System package. Examples of conditions include ON WARD, READMISSION, MAS MOVEMENT TYPE, PREVIOUS DISCHARGE, etc. You may use the Condition File Inquire option to obtain information on selected/all conditions. The information provided will describe the condition; tell you what questions will be asked when using a condition; tell you when you must define a group for the condition, and list the other data that is available for capture.
Each condition chosen for a monitor brings up a set of questions pertaining to it. For example, if you choose the AGE condition, you will be asked age ranges. Some conditions require a group be defined such as a group of wards, drug classes, MAS movement types, etc. Patients captured by the monitors are called "fall outs". With each condition used, there is a list of other data that can be captured when a patient becomes a “fall out” that might include items such as ward, admission date, attending, etc.
The monitors can be queued to run nightly, or manually run, one or more at a time. Each monitor has an "ON/OFF" switch, an "UNDER CONSTRUCTION" or "FINISHED" status, and START and STOP dates so that running it can be tightly controlled.
Software Features
- Provides the user with the ability to design a monitor that will auto enroll cases that meet the user's defined criteria/conditions from VistA.
- Allows the user to set time frames for computing percentages and tracking findings between time frames.
- Has the ability to alert users when important thresholds or dates are met.
- Provides a mechanism to add site-developed conditions and data elements and routines such as site-designed worksheets to the software. MUMPS programming is a required part of site-specific enhancement.
- Provides mechanisms for controlling the disk space and CPU time resources used by the Clinical Monitoring System.
- Allows the user to manually enter cases.

# # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The format of this manual is summarized in the Table of Contents. The Glossary defines general terms relevant to the Clinical Monitoring System and computer use.

The software package uses basic VA FileMan. Refer to Users Guide to Computing for more in-depth help. The following summarizes some of the VA FileMan functions and conventions that are used within the Clinical Monitoring System package.

Exiting

Depending on where you are within the program, entering an "up-arrow" (compressing the shift key while striking the 6) will allow you to jump to the beginning of a new record or to the menu options. Then pressing the \<RET\> key until you pass through the different levels of the menus will exit you from the program or back to the menu option you wish to use.

Help (?, ??, or ???)

Whenever you are unclear on the definition of a menu option or on how to respond to a prompt, one, two, or three question marks may be entered to obtain an explanation.

Deleting

Deleting default answers that appear before a "//" or a "Replace" is done by entering @ (compressing the shift key while striking the 2). Refer to the Users Guide to Computing for instruction on deleting within word processing fields.

Device

Striking the \<RET\> (return) key following the "DEVICE:" prompt will print the requested output on the computer screen. If a "Right Margin" prompt shows, you will need to strike the \<RET\> key once again. Enter the name of the printer/device following the "DEVICE:" prompt to print a hard copy of the output.

Patient Look-ups

When prompted to enter a patient name, use at least the first two letters of the last name to identify the patient. You may also enter the first initial of the last name and the last four digits of the social security number to obtain a record on a specific patient.

Bold Print

Bold print is used throughout the documentation for all user input in the instructional portion of the manual.

\<RET\>

The \<RET\> symbol is used throughout the manual to designate the use of the return or enter key.

# # Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Personal data within the package is covered by the Privacy Act. Data from any monitors considered a quality assurance activity is considered confidential and privileged. Title 38 U.S.C. 5705, as amended by Public Law 99-166, and the implementing HSRO (Health Services Review Organization) regulations (Title 38 Part 17) provide that HSRO records and documents which refer to individual practitioners are confidential and privileged. Exempt from this protection are aggregate statistical data, such as trend reports that do not identify individual patients or employees. Access to the software should be restricted to those personnel who meet the site's established access criteria to data for the above purposes.

# Monitoring System Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Group Edit

Patient Group

Manually Run Auto Enroll

Rationale Edit

Site Parameters Edit

Build Monitor Menu

> Enter/Edit a Monitor

> Copy/Edit a Monitor

> Quick Monitor Edit

Purge Menu

> Auto Enroll Run Dates File Purge

> Fall Out File Purge

> History File Purge

Outputs Menu

> Ad Hoc Fall Out Report

> Ad Hoc Monitor Report

> Audit File Inquire

> Auto/Manual Enroll Monitors Run

> Build a Monitor Worksheet

> Condition File Inquire

> Data Element File Inquire

> Fall Out File Inquire

> Group File Inquire

> Monitor Description Report

> Monitor History Report

Patients With Multiple Fall Outs

Monitoring System User Menu

> Fall Out Edit

> Sample Size Edit

> Outputs Menu

> Ad Hoc Fall Out Report

> Fall Out File Inquire

> Monitor Description Report

> Monitor History Report

> Patients With Multiple Fall Outs

## Group Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Group Edit option allows you to create groups of similar data from any VistA file that is in the QAM application group. First determine the conditions you want to use to build your monitor, and then see if within the definition of that condition you will need to define a group. This option is used only when the condition chosen to define a monitor calls for a group. For example, the Ward Location file contains all the wards at the site. You can select specific wards from this file to create a group. MAS Movement Type file contains movement types such as regular, irregular, discharge to CNH, death, etc. You could make a group of admissions to acute care by selecting the "Transfer In", "Direct", and "To ASIH" entries from the MAS Movement Type file.

Descriptions of the conditions are available through the Condition File Inquire option and can also be found in Appendix B of the ADPAC Guide. Use the condition descriptions to determine whether or not you need to define groups.

The Clinical Monitoring System software provides short-cuts so you do not always have to define groups. If, for example, you would like all MAS MOVEMENT TYPES that are “admission” transactions, you do not need to create a group containing all of the individual admission transaction MAS MOVEMENT TYPE entries. Instead, choose the MAS MOVEMENT TYPE condition when building your monitor. When asked which category of movement you are interested in, select "ADMISSIONS", then press \<RET\> at the group prompt.

Example

Select GROUP: SUBSTANCE ABUSE

Are you adding 'SUBSTANCE ABUSE' as a new GROUP (the 2ND)? No// Y (YES)

GROUP PARENT FILE: FACILITY TREATING SPECIALTY

NAME: SUBSTANCE ABUSE// \<RET\>

PARENT FILE: FACILITY TREATING SPECIALTY// (No Editing)

Select GROUP MEMBER: PSYCHIATRY

GROUP MEMBER: PSYCHIATRY// \<RET\>

Select GROUP MEMBER: \<RET\>

## Patient Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows the user to build a group of patients to monitor using the VA FileMan search option. Once the search and sort parameters have been input, the QAMDFM function must be used at one of the “print field” prompts. This function should be used on a field that is a pointer, free text pointer, or free text Patient Name field.

Usage: QAMFDN(Patient_name_Field) or QAMDFN(#Patient_name_Field_number)

This option can also be used to update an existing patient group. The file search would occur the same way as when creating a new patient group; however, you will be asked if the newly found entries should be merged with the existing entries or if the old entries should be deleted prior to the search.

If no group entries were created, the group will be deleted.

Example

We want to build a list of Dr. Brach's patients that had occurrences. Any file we search must have a Patient field that points to the PATIENT file. Dr. Brach is the attending so the Attending Physician field is searched for any entries containing BRACH.

Select GROUP: CMSPROVIDER,ONE’S PATIENTS

Are you adding 'CMSPROVIDER,ONE'S PATIENTS' as a new GROUP? No// Y (YES)

Select FILE TO SEARCH: 741 QA OCCURRENCE SCREEN

Searching the QA OCCURRENCE SCREEN file(#741)

-A- SEARCH FOR QA OCCURRENCE SCREEN FIELD: ATTENDING PHYSICIAN

-A- CONDITION: CONTAINS

-A- CONTAINS: CMSPROVIDER

-B- SEARCH FOR QA OCCURRENCE SCREEN FIELD: \<RET\>

IF:A// \<RET\> ATTENDING PHYSICIAN CONTAINS "CMSPROVIDER"

STORE RESULTS OF SEARCH IN TEMPLATE: \<RET\>

SORT BY: NUMBER// \<RET\>

START WITH NUMBER: FIRST// \<RET\>

FIRST PRINT FIELD: QAMDFN(QA PATIENT)

THEN PRINT FIELD: \<RET\>Patient GroupExample\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Heading (S/C): QA OCCURRENCE SCREEN SEARCH Replace \<RET\>

STORE PRINT LOGIC IN TEMPLATE: \<RET\>

DEVICE: \<RET\> HOME RIGHT MARGIN: 80// \<RET\>

QA OCCURRENCE SCREEN SEARCH JAN 19,1998 11:09 PAGE 1

QAMDFN(QA PATIENT)

-----------------------------------------------------------------------------

NUMBER: 7

CMSPATIENT,ONE

NUMBER: 8

CMSPATIENT,TWO

NUMBER: 10

CMSPATIENT,THREE

NUMBER: 14

CMSPATIENT,FOUR

NUMBER: 18

CMSPATIENT,FIVE

5 MATCHES FOUND.

Building the CMSPROVIDER ONE’S PATIENTS group...

## Manually Run Auto Enroll

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

Active monitors are normally run as a nightly task as scheduled by IRM Service. This option allows the user to run selected monitors or selected services when, for some reason, one or more monitors has not run for a day. If a monitor has already been run for a given date in the past, the monitor will not rerun for that same day.

Auto enroll looks at VistA transactions from the previous day to capture fall outs. When auto enroll runs "tomorrow," it will only pick up fall outs with event dates of "today" not "yesterday" or any time before that. For example, fall outs with event dates of 1/4/98 will be picked up when auto enroll runs on 1/5/98.

For manually enrolled monitors, it is important to remember that it is the entry date, not the event date, that will determine whether or not the data will be auto enrolled. Therefore, a record entered manually today will be picked up by auto enroll tomorrow. (A manually enrolled monitor requires total manual entry of fall out data. See the Clinical Monitoring System ADPAC Guide for more details.)

Certain site parameters must contain entries before you may utilize this option. Depending on how the *Manual Auto Run Allowed Times* site parameter is set up, the manual run may only be performed at certain times during the day.

Example

Want to run auto enroll for specific monitors? No// \<RET\> (No)

Want to run auto enroll for specific services? No// \<RET\> (No)

Enter the date range you want auto enroll to scan

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: USER SELECTABLE

Enter beginning and ending dates for the desired time period:

Beginning Date: 2 16 98 (FEB 16, 1998)

Ending Date: FEB 16,1998// \<RET\>98 (FEB 16, 1998)

Range selected: FEB 16,1998 to FEB 16,1998

Queue auto enroll to run at: N (FEB 17,1998@09:30)

Manually Run Auto EnrollExample

Queueing auto enroll, please wait.

Want a report of the dates when auto enroll will run? YES// \<RET\> (Yes)

DEVICE: \<RET\> RIGHT MARGIN: 80// \<RET\>

MANUALLY QUEUED AUTO ENROLL RUN DATES FEB 17,1998

PERIOD FROM FEB 16,1998 TO FEB 16,1998 PAGE: 1

START DATE END DATE QUEUED TO RUN TASK NUMBER

-----------------------------------------------------------------------------

FEB 16,1998 FEB 16,1998 FEB 17,1998@09:30:31 1449

## Rationale Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

Rationales are reasons for the use of the monitors. This option allows you to enter new rationales other than those exported with the software (High Volume, Problem Prone, High Risk, Other).

For each rationale, it allows editing of the *Requires Explanation* field. Entering YES at this field means a word processing field will be provided at the time this rationale is selected within the Clinical Monitoring software, so that a more complete explanation can be entered for the rationale.

Example

Select RATIONALE: ??

Choose from:

1 High Volume

2 High Risk

3 Problem Prone

4 Other

This field contains the rationales for the use of a monitor.

Select RATIONALE: 1 High Volume

NAME: High Volume// \<RET\>

REQUIRES EXPLANATION: N NO

## Site Parameters Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The IRM support staff should configure the program to the site through this option. The following parameters may be entered/edited.

*Day Weekly Time Frame Begins*

This is the day of the week that should begin each weekly time frame. Generally, this would be Sunday but could be Monday since that is considered a regular work day.

*Monitoring System Device*

The device on which auto enroll reports will print.

*Max Days Per Manual Auto Run*

This field contains the maximum number of auto enroll runs that may be run consecutively. A date range of more than three days is allowed; however, the Clinical Monitoring System will break the job up into several tasks, each spanning three days. Note that if this field is set to too small a number and the user runs auto enroll over a large number of days, a large number of tasks will be created.

*Time Between Manual Auto Runs*

This field contains the number of minutes between queued runs of auto enroll. This, together with the MAX DAYS limit above, is used to tightly control the use of computer resources that auto enroll processing uses.

*Manual Auto Run Allowed Times*

This field contains the range of time during which auto enroll may be manually queued to run. The format is HHMM-HHMM (where hh = hours and mm = minutes). The second time must be greater than the first.

*Allow Use of ‘\[‘ in Group Edit*

Allows use of the "contains" operator ( \[ ) in the group edit. If this field is set to YES, the user may enter “\[GROUP MEMBER” during group edit to select all entries that contain the text “GROUP MEMBER” as part of their name. Building groups using the “contains” operator is computer intensive.

Site Parameters EditExample

Select QUALITY ASSURANCE SITE PARAMETERS NAME: CHICAGO

DAY WEEKLY TIME FRAME BEGINS: Monday

MONITORING SYSTEM DEVICE: DEV-LASER(10)-PORT-80

MAX DAYS PER MANUAL AUTO RUN: 3

TIME BETWEEN MANUAL AUTO RUNS: 30

MANUAL AUTO RUN ALLOWED TIMES: 0000-2359

ALLOW USE OF \`\[' IN GROUP EDIT: YES// \<RET\>

## Build Monitor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter/Edit a Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Enter/Edit a Monitor option is used to build an auto enroll monitor (automatically enrolls fall out cases) or a manual enroll monitor (accepts manual entry of patient names).

Associating a service with the monitor at the *Service* prompt will allow you to print out a list of all monitors for the service through the Manually Run Auto Enroll option.

The entry at the *Treating Specialty Group* prompt should have been defined through the Group Edit option on the Manager Menu before utilizing this option, if necessary.

You may enter '?CONDITION' (e.g., ?AGE) at the *Select CONDITION* prompt to see a description of a condition or range of conditions. Enter '?\*' to see the descriptions for all conditions. You may only select conditions that match the monitor type (auto enroll or manual enroll).

Before you begin to build a monitor, you may want to consider the following tips.

- Read through this manual to determine required information.
- Define your monitor using that information and the Build a Monitor Worksheet which may be obtained through the Build a Monitor Worksheet option on the Outputs Menu.
- Determine the conditions needed. Use the Condition File Inquire option to check if those conditions are available.
- Determine if any of the conditions require a group be defined. If so, use the Group Edit option to build the group.

  
Build Monitor Menu*Enter/Edit a Monitor*Introduction

Manually entered monitors require more work than auto enrolled monitors.

- Once they are built, you should use the Fall Out Edit option on the Monitoring System User Menu to enter names of patients who meet the fall out conditions you have determined. You will then be prompted with default information for the data elements that have been built into the monitor.
- Since this is a monitor that you are reviewing manually, there will be cases that are not considered fall outs. If you want to keep track of the total number of cases you reviewed, use the Sample Size Edit option on the Monitoring System User Menu to update the sample size.
- Manually entered fall outs will be automatically counted by the nightly run of auto enroll if the entry date of the fall out is the day just previous to the auto enroll. Auto enroll runs pick up those fall outs whose entry dates are T-1 and updates the statistics which can be accessed through the Monitor History Report option.

*Error/Warning Designations*

The Clinical Monitoring System checks the validity of your monitor and displays errors and warnings to help you correct it. Fields with an \*ERROR\* designation must be completed for the program to auto enroll patients. \*WARNING\* designations are to let the user know that certain portions of the monitor may not run if the field is not completed. For many monitors, those fields may not be necessary. However, the ON/OFF SWITCH field (which receives a \*WARNING\* when it is turned OFF), must be ON for the monitor to run.

Please note that up-arrow jumping between prompts is not allowed in this option. This is due to the internal processing that the Clinical Monitoring System must accomplish. The Quick Monitor Edit option, described later in this manual, allows certain fields to be edited without reediting the entire monitor.

  
Build Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

Select MONITOR: ??

This can either be free text or a predetermined list (of initial

identifying letters or numbers) as defined by the site so that monitors

can be grouped and easily retrieved by the service, section, or whatever.

Select MONITOR: PSY-3

Are you adding 'PSY-3' as a new QA MONITOR (the 12TH)? No// Y (YES)

QA MONITOR TITLE: LOS ON SUBSTANCE ABUSE

CODE: PSY-3// \<RET\>

TITLE: LOS ON SUBSTANCE ABUSE Replace \<RET\>

SERVICE: PSYCHIATRY 136

STANDARD OF CARE:

No existing text

Edit? NO// \<RET\>

CLINICAL INDICATOR:

No existing text

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]======\< CLINICAL INDICATOR \>========\[ \<PF1\>H=Help \]====

For this monitor the indicator is a stay of 28 days in aSubstance Abuse treating specialty.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>===T

Select RATIONALE: Other

Explain Rationale

No existing text

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]======\< EXPLAIN RATIONALE \>========\[ \<PF1\>H=Help \]====

This monitor is an aid to determining the adequacy of discharge planningfor those patients whose stays exceed the designated LOS.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>===T

Build Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// YES

Select CONDITION: ?

You may enter '?CONDITION' (e.g., ?AGE) at the 'Select CONDITION:'

prompt to see a description of a condition or range of conditions.

Enter '?\*' to see the descriptions for all conditions.

Answer with CONDITION , or NUMBER

You may enter a new CONDITION, if you wish

Enter a condition that will make up the monitor.

You may only select conditions that match the monitor type,

auto/manual enroll.

Answer with CONDITION NAME

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// YES

Select CONDITION: ?

You may enter '?CONDITION' (e.g., ?AGE) at the 'Select CONDITION:'

prompt to see a description of a condition or range of conditions.

Enter '?\*' to see the descriptions for all conditions.

Answer with CONDITION , or NUMBER

You may enter a new CONDITION, if you wish

Enter a condition that will make up the monitor.

You may only select conditions that match the monitor type,

auto/manual enroll.

Answer with CONDITION NAME

Do you want the entire CONDITION list? Y (YES)

CHOOSE FROM:

AGE

APPOINTMENT

DEATH

FALL OUT

LAB-CHEM,HEM,TOX,RIA,SER,ETC

LENGTH OF STAY IN SPECIALTY

LENGTH OF STAY ON A WARD

LENGTH OF STAY SINCE ADMISSION

MAS MOVEMENT TYPE

MH SECLUSION/RESTRAINT

ON SERVICE

ON TREATING SPECIALTY

ON WARD

OS-101.1

OS-102

OS-106.1

OS-107

OS-109

OS-199

PATIENT GROUP

PREVIOUS DISCHARGE FROM WARD

PREVIOUS DISCHARGE MVMENT TYPE

PREVIOUS DISCHARGE TREAT SPEC

Build Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

PTF DIAGNOSES/OPERATION CODES

READMISSION

REGISTRATION

RXS 2+ DRUGS IN THE SAME CLASS

SEX

SPECIALTY TRANSFER

SSN SAMPLE

WARD TRANSFER

Select CONDITION: LENGTH OF STAY IN SPECIALTY

CONDITION: LENGTH OF STAY IN SPECIALTY// \<RET\>

LENGTH OF STAY: (1-365): 28

TREATING SPECIALTY GROUP: 26 SUBSTANCE ABUSE FACILITY TREATING SPECIALTY

CONTRIBUTES TO SAMPLE: ??

This field determines whether or not this condition contributes to the

sample size (denominator). This affects how information is collected

to determine the size of the sample (denominator). Answer 'YES' to

this question if the patients meeting this condition should be counted

in the sample size. Answer 'NO' if these patients should not be counted.

CHOOSE FROM:

1 YES

0 NO

CONTRIBUTES TO SAMPLE: YES

Select CONDITION: \<RET\>

============================================================================

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

FALL OUT RELATIONSHIP: ??

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

This field specifically states the relationship between the conditions

entered by the user. The user may use & (and), ! (or), ' (not), and

parentheses () to specify the relationship.

Build Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

FALL OUT RELATIONSHIP: C1

============================================================================

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

SAMPLE RELATIONSHIP: ??

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

Enter the relationship among the conditions. This field specifically

states the relationship between the conditions that contribute to the

sample size. The user may use & (and), ! (or), ' (not) and

parentheses () to specify the relationship.

SAMPLE RELATIONSHIP: C1

============================================================================

NUMBER CONDITION

-------- -----------

1 LENGTH OF STAY IN SPECIALTY

CONDITION FOR DATE OF EVENT: ??

NUMBER CONDITION

-------- -----------

1 LENGTH OF STAY IN SPECIALTY

This field controls which of the conditions will provide the date that

will be used as the event date for the fall out. You will usually

want to pick the condition whose date most uniquely defines the event

you are monitoring. For example, if you were monitoring all female

(Condition \#1: SEX) admissions (Condition \#2: MAS MOVEMENT TYPE)

you would pick condition number two as the condition to supply the

event date.

CONDITION FOR DATE OF EVENT: 1  
Build Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

=============================================================================

TIME FRAME: ??

Time frame is the period of time over which the program begins capturing

data and then sums up the data to start all over again with the beginning

of the next similar time frame.

CHOOSE FROM:

Annually

Daily

Fiscal Semi-Annually

Fiscal Yearly

Monthly

Quarterly

Semi-Annually

Weekly

TIME FRAME: QUARTERLY Quarterly

THRESHOLD: ??

Threshold defines the number or percentage of fall outs after which

some specific action will occur. The threshold may be entered as a

pure numeric response (e.g., 38), or as a percentage (e.g., 38%).

THRESHOLD: 10

PRE-THRESHOLD ALERT LEVEL: ??

For PERCENT thresholds:

This field defines the minimum sample size (denominator)

that must be reached before threshold checking occurs.

For NUMERIC thresholds:

This field may be used along with the BULLETIN WHEN MIN SAMPLE

MET field (set to YES) as a pre-threshold notification.

PRE-THRESHOLD ALERT LEVEL: 4

ALLOW 'DUPLICATE' FALL OUTS: ??

Answering Y(es) to this question allows an event to fall out multiple

times for the same patient within a given time frame. Answering N(o)

will allow the event to fall out only once per time frame.

For example, a monitor is set up to capture all admissions over a

monthly time frame. Assume a patient is admitted twice in the same

month. Answering 'NO' to this question will capture only the

patient's first admission. Answering 'YES' will capture both.

CHOOSE FROM:

1 YES

0 NO

ALLOW 'DUPLICATE' FALL OUTS: YESBuild Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

Select OTHER DATA TO CAPTURE: ??

When a patient meets the conditions of the monitor and falls out the

other data to capture entries define which data elements in the patient's

record should be collected.

CHOOSE FROM:

ADMITTED FOR SC CONDITION? PATIENT MOVEMENT

ADMITTING REGULATION PATIENT MOVEMENT

ATTENDING PHYSICIAN PATIENT MOVEMENT

DIAGNOSIS \[SHORT\] PATIENT MOVEMENT

FACILITY TREATING SPECIALTY PATIENT MOVEMENT

MAS MOVEMENT TYPE PATIENT MOVEMENT

MOVEMENT DATE/TIME PATIENT MOVEMENT

PRIMARY CARE PHYSICIAN PATIENT MOVEMENT

ROOM-BED PATIENT MOVEMENT

TRANSACTION TYPE PATIENT MOVEMENT

TYPE OF MOVEMENT PATIENT MOVEMENT

WARD LOCATION PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: WARD LOCATION PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: PRIMARY CARE PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: ATTENDING PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: \<RET\>

PRINT DAILY FALL OUT LIST: NO// ??

This field determines whether or not a generic list of all fall outs,

sorted by monitor, is printed daily.

CHOOSE FROM:

1 YES

0 NO

PRINT DAILY FALL OUT LIST: NO// YES

PRINT DAILY WORKSHEETS: NO// ??

This field determines whether worksheets are printed daily for all fall

outs for this monitor. For this to work, the worksheet must first be

created by a programmer and linked to the monitor.

CHOOSE FROM:

1 YES

0 NO

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// ??

If this field is answered YES, then a bulletin will be sent to a

specified mail group when the threshold is met. This bulletin is sent

only once per time frame.

CHOOSE FROM:

1 YES

0 NO

BULLETIN WHEN THRESHOLD MET: NO// YESBuild Monitor Menu*Enter/Edit a Monitor*Example 1 - Auto Enroll Monitor

BULLETIN AT END OF TIME FRAME: NO// ??

If this field is answered YES, then a bulletin will be sent to a

specified mail group when the end of the time frame is reached. This

bulletin is sent only once per time frame.

CHOOSE FROM:

1 YES

0 NO

BULLETIN AT END OF TIME FRAME: NO// YES

BULLETIN WHEN ALERT LEVEL MET: NO// ??

If this field is answered YES, than a bulletin will be sent to a

specified mail group when the minimum sample size is met or exceeded.

This bulletin is sent only once per time frame.

CHOOSE FROM:

1 YES

0 NO

BULLETIN WHEN ALERT LEVEL MET: NO// YES

BULLETIN MAIL GROUP: ?

Enter the mail group bulletins should be sent to.

Only ‘public’ mail groups are selectable.

Answer with MAIL GROUP NAME

Do you want the entire MAIL GROUP List? NO

BULLETIN MAIL GROUP: QAM-NOTIFICATION

START DATE: T (JUL 17, 1992)

END DATE: T+365 (JUL 17, 1993)

ON/OFF SWITCH: OFF// ??

This field controls whether or not a monitor is active. For an auto

enroll monitor to capture data the switch must be turned on. For a

manual entry monitor to be selectable, the switch must be turned on.

When you wish to stop using a monitor, this switch should be turned off.

CHOOSE FROM:

1 ON

0 OFF

ON/OFF SWITCH: OFF// ON

Checking monitor...

No errors found.

MONITOR STATUS: UNDER CONSTRUCTION// ??

Answer FINISHED to this field only when you are sure you are completely

finished entering/editing this monitor. Once you answer FINISHED

you will no longer be able to edit selected monitor fields.

CHOOSE FROM:

1 FINISHED

0 UNDER CONSTRUCTION

MONITOR STATUS: UNDER CONSTRUCTION// FINISHED

  
Build Monitor Menu*Enter/Edit a Monitor*Example 2 - Manual Enroll Monitor

Select MONITOR: CAT-1

Are you adding 'CAT-1' as a new QA MONITOR (the 5TH)? No// Y (YES)

QA MONITOR TITLE: XXX TEST MANUAL ENTRY

CODE: CAT-1// \<RET\>

TITLE: XXX TEST MANUAL ENTRY Replace \<RET\>

SERVICE: QUALITY MANAGEMENT

STANDARD OF CARE:

No existing text

Edit? NO// \<RET\>

CLINICAL INDICATOR:

No existing text

Edit? NO// \<RET\>

Select RATIONALE: Problem Prone

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// NO

Select CONDITION: MANUAL ENROLL CONDITION

CONDITION: MANUAL ENROLL CONDITION// \<RET\>

CONTRIBUTES TO SAMPLE: \<RET\>

Select CONDITION: \<RET\>

=============================================================================

CODE CONDITION

------ -----------

C1 MANUAL ENROLL CONDITION

FALL OUT RELATIONSHIP: C1

=============================================================================

=============================================================================

NUMBER CONDITION

-------- -----------

1 MANUAL ENROLL CONDITION

CONDITION FOR DATE OF EVENT: 1

=============================================================================

TIME FRAME: Quarterly

THRESHOLD: 20

PRE-THRESHOLD ALERT LEVEL: \<RET\>

ALLOW 'DUPLICATE' FALL OUTS: \<RET\>

Select OTHER DATA TO CAPTURE: AGE PATIENT

Select OTHER DATA TO CAPTURE: DIAGNOSIS \[SHORT\] PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: FACILITY TREATING SPECIALTY PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: PRIMARY CARE PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: SOCIAL SECURITY NUMBER PATIENT

Select OTHER DATA TO CAPTURE: WARD LOCATION PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: \<RET\>  
Build Monitor Menu*Enter/Edit a Monitor*Example 2 - Manual Enroll Monitor

PRINT DAILY FALL OUT LIST: NO// \<RET\>

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// YES

BULLETIN AT END OF TIME FRAME: NO// YES

BULLETIN WHEN ALERT LEVEL MET: NO// \<RET\>

BULLETIN MAIL GROUP: QA-1

START DATE: T-5

END DATE: \<RET\>

ON/OFF SWITCH: OFF// ON

Checking monitor...

> **WARNING:** SAMPLE RELATIONSHIP not specified

No errors found.

MONITOR STATUS: UNDER CONSTRUCTION// FINISHEDBuild Monitor Menu

### Copy/Edit a Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option takes an existing monitor and copies it to a new monitor. It could be utilized if you wish to design a new monitor similar to an existing one.

The option automatically adds the words "Copy of" to the Code and Title fields of the selected monitor. These fields allow up to 30 characters, so the code and name may be truncated if they are too long. It is recommended that you change the code and title of the new monitor at the time the copy is made.

Example

Select MONITOR TO COPY: PSY-1 LOS ON SUBSTANCE ABUSE FINISHED

Are you sure you want to copy this monitor? NO// Y (YES)

Copying monitor, please wait...

You may now edit the copy of the monitor, please change the CODE and TITLE.

CODE: Copy of PSY-1// PSY-12

TITLE: Copy of LOS ON SUBSTANCE ABUSE Replace ... With LOS ON ALCOHOL REHAB

Replace

LOS ON ALCOOHOL REHAB

SERVICE: PSYCHIATRY// \<RET\>

STANDARD OF CARE:

No existing text

Edit? NO// \<RET\>

CLINICAL INDICATOR:

No existing text

Edit? NO// \<RET\>

Select RATIONALE: Other// PROBLEM PRONE

EXPLAIN RATIONALE:

No existing text

Edit? NO// \<RET\>

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// \<RET\>

Select CONDITION: LENGTH OF STAY IN SPECIALTY// \<RET\>

...OK? YES// \<RET\> (YES)

CONDITION: LENGTH OF STAY IN SPECIALTY// \<RET\>

LENGTH OF STAY (1-365): 28// 30

TREATING SPECIALTY GROUP: SUBSTANCE ABUSE// ALCOHOL REHAB

CONTRIBUTES TO SAMPLE: YES// \<RET\>

Select CONDITION: \<RET\>Build Monitor Menu*Copy/Edit a Monitor*Example

===========================================================================

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

FALL OUT RELATIONSHIP: C1// \<RET\>

=============================================================================

CODE CONDITION

------ -----------

C1 LENGTH OF STAY IN SPECIALTY

SAMPLE RELATIONSHIP: C1// \<RET\>

=============================================================================

NUMBER CONDITION

------ -----------

1 LENGTH OF STAY IN SPECIALTY

CONDITION FOR DATE OF EVENT: 1// \<RET\>

=============================================================================

TIME FRAME: Quarterly// \<RET\>

THRESHOLD: 5// \<RET\>

PRE-THRESHOLD ALERT LEVEL: 4// \<RET\>

ALLOW 'DUPLICATE' FALL OUTS: YES// \<RET\>

Select OTHER DATA TO CAPTURE: WARD LOCATION// \<RET\>

PRINT DAILY FALL OUT LIST: YES// \<RET\>

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: YES// \<RET\>

BULLETIN AT END OF TIME FRAME: YES// \<RET\>

BULLETIN WHEN ALERT LEVEL MET: YES// \<RET\>

BULLETIN MAIL GROUP: QA-1// \<RET\>

START DATE: JUL 17,1991// \<RET\>

END DATE: \<RET\>

ON/OFF SWITCH: OFF// \<RET\>

MONITOR STATUS: UNDER CONSTRUCTION// \<RET\>  
Build Monitor Menu

### Quick Monitor Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows for editing of the following monitor fields; on/off switch, start and end dates, bulletin switches, and bulletin mail groups.

It is recommended that this option be used to edit active monitors.

Example

Select MONITOR: PSY-1 LOS ON SUBSTANCE ABUSE FINISHED

PRINT DAILY FALL OUT LIST: YES// \<RET\>

PRINT DAILY WORKSHEETS: NO// YES

BULLETIN WHEN THRESHOLD MET: YES// \<RET\>

BULLETIN AT END OF TIME FRAME: YES// \<RET\>

BULLETIN WHEN ALERT LEVEL MET: YES// \<RET\>

BULLETIN MAIL GROUP: QA-1// \<RET\>

START DATE: JUL 17,1991// \<RET\>

END DATE: \<RET\>

ON/OFF SWITCH: ON// OFF

Checking monitor...

> **WARNING:** ON/OFF SWITCH is turned off

No errors found.

MONITOR STATUS: FINISHED// \<RET\>

## Purge Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Enroll Run Dates File Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option purges data generated from the Auto Enroll Run Date file (#743.92) for selected monitors for a selected date range. Note that once the data has been deleted, it cannot be recovered.

The Auto Enroll Run Date file contains one entry for each date. Within that entry is a list of all the monitors that ran on that date. When this file is purged, the monitor names that are stored with each date in the selected purge date range are deleted; however, the date entry is not deleted.

Example

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* This option DELETES selected data from the Auto Enroll Run Dates file \*

\* Once the data has been deleted it CANNOT BE RECOVERED \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure you want to continue? NO// YES

Select the monitors to delete.

Select MONITOR: PSY-1

Another one: \<RET\>

Select the date range to delete.

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: 7/15/98

Ending Date: JUL 15,1998// \<RET\>

Range selected: JUL 15,1998 to JUL 15,1998

Ready to DELETE, are you sure? NO// YES

Deletion request queued.

Purge Menu

### Fall Out File Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option purges data from the FALL OUT file (#743.1) for selected monitors for a selected date range. Note that once the data has been deleted, it cannot be recovered.

Example

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* This option DELETES selected data from the Fall Out file \*

\* Once the data has been deleted it CANNOT BE RECOVERED \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure you want to continue? NO// YES

Select the monitors to delete.

Select MONITOR: PSY-1

Another one: \<RET\>

Select the date range to delete.

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: T-2

Ending Date: JUL 15,1998// \<RET\>

Range selected: JUL 15,1998 to JUL 15,1998

Ready to DELETE, are you sure? NO// YES

Deletion request queued.

Purge Menu

### History File Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option purges data from the Monitor History file (#743.2) for selected monitors for a selected date range. The Monitor History file contains the numbers for sample size and fall outs. Note that once the data has been deleted, it cannot be recovered.

Example

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* This option DELETES selected data from the Monitor History file \*

\* Once the data has been deleted it CANNOT BE RECOVERED \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure you want to continue? NO// YES

Select the monitors to delete.

Select MONITOR: PSY-1

Another one: \<RET\>

Select the date range to delete.

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: T-2

Ending Date: JUL 15,1998// \<RET\>

Range selected: JUL 15,1998 to JUL 15,1998

Ready to DELETE, are you sure? NO// YES

Deletion request queued.

## Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ad Hoc Fall Out Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to design your own reports from data in the Fall Out file (#743.1). The data elements present in the FALL OUT file are determined by the data elements selected when the monitor was built. An attempt to sort/print a data element that was not entered into the monitor's *Other Data to Capture* will produce no data for that element.

It is suggested that you limit your sorts by making Event Date one of the sorts and enter a range. Event Date is the date of the transaction that caused the record to fall out. If the monitor has a look-back of 30 days, the Event Date could be as much as 30 days prior to the Creation Date. Creation Date is the date the monitor was looking at when it ran (i.e., yesterday).

If you built an admission monitor to use only as a fall out condition for other monitors, you will get a list of all admissions.

Example

Enter the fields you wish to sort on.

Maximum two sort fields allowed.

1 Patient Name 3 Event Date

2 Monitor 4 Data Element

Sort selection \#1: 2

Enter the beginning and ending values for MONITOR CODE.

Start with: First// PSY-1

End with: Last// PSY-1

Select next field to sort on.

Maximum two sort fields allowed.

\* indicates already selected.

1 Patient Name 3 Event Date

2 \*Monitor 4 Data Element

Sort selection \#2: \<RET\>  
Outputs Menu*Ad Hoc Fall Out Report*Example

Enter the fields you wish to print.

Maximum four print fields allowed.

1 Patient Name 3 Event Date

2 Monitor 4 Data Element

Print selection \# 1: 1

Select next field to print on.

Maximum four print fields allowed.

\* indicates already selected.

1 \*Patient Name 3 Event Date

2 Monitor 4 Data Element

Print selection \# 2: 3

Select next field to print on.

Maximum four print fields allowed.

\* indicates already selected.

1 \*Patient Name 3 \*Event Date

2 Monitor 4 Data Element

Print selection \# 3: 4

Select Data Element: A

By 'A' do you mean ALL 69 DATA ELEMENTS? YES// \<RET\>

Another one: \<RET\>

Select next field to print on.

Maximum four print fields allowed.

\* indicates already selected.

1 \*Patient Name 3 \*Event Date

2 Monitor 4 \*Data Element

Print selection \# 4: \<RET\>

Enter the special report header, if desired (maximum 55 characters): TEST

DEVICE: HOME// HALLWAY PRINTER RIGHT MARGIN: 80// \<RET\>Outputs Menu*Ad Hoc Fall Out Report*Example

TEST JUL 18,1998

SORTED BY MONITOR PAGE: 1

\*\* This information is confidential in accordance with Title 38 U.S.C. 5705 \*\*

--------------------------------------------------------------------------------

---MONITOR: PSY-1

PATIENT NAME: CMSPATIENT,ONE

EVENT DATE: JUL 18,1998 CREATION DATE: JUL 18,1998

ADMITTING REGULATION ACTIVE PSYCHOSIS

AGE 52

APPOINTMENT DATE/TIME

DIAGNOSIS \[SHORT\] PARANOIA

FACILITY TREATING SPECIALTY PSYCHIATRY

PRIMARY CARE PHYSICIAN CMSPROVIDER,ONE

PURPOSE OF VISIT

SOCIAL SECURITY NUMBER 666456789

WARD LOCATION 3W

PATIENT NAME: CMSPATIENT,TWO

EVENT DATE: JUL 18,1998 CREATION DATE: JUL 18,1998

ADMITTING REGULATION

AGE 46

APPOINTMENT DATE/TIME

DIAGNOSIS \[SHORT\] DIABETES

FACILITY TREATING SPECIALTY MEDICINE

PRIMARY CARE PHYSICIAN CMSPROVIDER,TWO

PURPOSE OF VISIT

SOCIAL SECURITY NUMBER 000456789

WARD LOCATION 5E

  
Outputs Menu

### Ad Hoc Monitor Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to design reports from data in the QA Monitor file (#743). A maximum of four sort fields and seven prints fields are allowed. For more complete instructions on how to use the Ad Hoc Report Generator, refer to the Ad Hoc Report Generator chapter in the QM Integration User Manual.

Example

============= Monitoring System Ad Hoc Report Generator ==============

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

Standard of Care 17 End Date

Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch Mail Group Description

11 Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 Other Data To Capture

Sort selection \# 1 : 11 Condition

Sort from: BEGINNING// \<RET\>

========= Clinical Monitoring System Ad Hoc Report Generator =========

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

Standard of Care 17 End Date

Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch Mail Group Description

11 \* Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 Other Data To Capture

Sort selection \# 2 : 26 Other Data To Capture

Sort from: BEGINNING// \<RET\>  
Outputs Menu*Ad Hoc Monitor Report*Example

========= Clinical Monitoring System Ad Hoc Report Generator =========

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

Standard of Care 17 End Date

Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch Mail Group Description

11 \* Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 \* Other Data To Capture

Sort selection \# 3 : \<RET\>

========= Clinical Monitoring System Ad Hoc Report Generator =========

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

4 Standard of Care 17 End Date

5 Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

7 Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch 23 Mail Group Description

11 Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 Other Data To Capture

Print selection \# 1 : 11 Condition

  
Outputs Menu*Ad Hoc Monitor Report*Example

========= Clinical Monitoring System Ad Hoc Report Generator =========

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

4 Standard of Care 17 End Date

5 Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

7 Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch 23 Mail Group Description

11 \* Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 Other Data To Capture

Print selection \# 2 : 26 Other Data To Capture

========= Clinical Monitoring System Ad Hoc Report Generator =========

1 Monitor Code 14 Threshold

2 Monitor Title 15 Hi/Lo Percent

3 Service 16 Start Date

4 Standard of Care 17 End Date

5 Clinical Indicator 18 Print Daily Fall Out List

6 Rationale 19 Bulletin When Threshold Met

7 Explain Rationale 20 Bulletin At End Of Time Frame

8 Auto Enroll Monitor 21 Bulletin When Min Sample Met

9 Monitor Status 22 Bulletin Mail Group

10 On/Off Switch 23 Mail Group Description

11 \* Condition 24 Mail Group Member

12 Time Frame 25 Allow 'Duplicate' Fall Outs

13 Min Sample/Alert Level 26 \* Other Data To Capture

Print selection \# 3 : \<RET\>

Enter special report header, if desired (maximum of 60 characters).

\<RET\>

DEVICE: \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

QA MONITOR LIST MAR 2,1999 09:29 PAGE 1

Condition Other Data To Capture

---------------------------------------------------------------------------

LENGTH OF STAY IN SPECIALTY ATTENDING PHYSICIAN

LENGTH OF STAY IN SPECIALTY PRIMARY CARE PHYSICIAN

LENGTH OF STAY IN SPECIALTY WARD LOCATION

Outputs Menu

### Audit File Inquire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Audit File Inquire option allows you to pick a fall out record and view its audit file entry. The audit file data includes information on who modified the record, when it was modified, and what modification was performed.

The date/time tells you when the monitor ran or when manual edit captured the fall out record or edited it.

The only prompts are for patient name and device.

Example

--------------------------------------------------------------------------------------

MONITORING SYSTEM AUDIT TRAIL DEC 9,1998 10:34 PAGE 1

PATIENT

DATE/TIME ACTION USER

COMMENT

--------------------------------------------------------------------------------------

18 CMSPATIENT,ONE

OCT 29,1998 08:22 OPEN CMSUSER,ONE

MANUAL ENROLLED FALL OUT

OCT 29,1998 08:22 EDIT CMSUSER,TWO

MANUAL EDIT OF FALL OUT DATA

  
Outputs Menu

### Auto/Manual Enroll Monitors Run

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Auto/Manual Enroll Monitors Run option produces a report that shows whether or not auto enroll ran and, if it did, which monitors were run.

Example

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: 7 16 98 (JUL 16, 1998)

Ending Date: JUL 16,1998// \<RET\> (JUL 16, 1998)

Range selected: JUL 16,1998 to JUL 16,1998

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

AUTO/MANUAL ENROLL MONITORS RUN JUL 19,1998

PERIOD FROM JUL 16,1998 TO JUL 16,1998 PAGE: 1

AUTO ENROLL RUN DATE

MONITOR CODE (a/m=AUTO/MANUAL) MONITOR TITLE DATE RUN

--------------------------------------------------------------------------------

JUL 16,1998

Copy of XX-1 (a) Copy of DEATH JUL 17,1998

FALL-1 (m) FALL MONITOR JUL 17,1998

LOS-1 (a) LOS ON WARD JUL 17,1998

MEM-1 (m) MANUAL ENROLL MONITOR JUL 17,1998

NEW-9 (a) BRAND NEW MONITOR JUL 17,1998

XX-1 (a) DEATH JUL 17,1998

XX-2 (a) DEATH 2 JUL 17,1998

XXS-1 (a) DEATH ON SERVICE JUL 17,1998

  
Outputs Menu

### Build a Monitor Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is used to print a blank worksheet that can be used to collect the information you need to build a monitor. The only prompts are for number of worksheets to print and device.

Example

Build a Monitor Worksheet

1\. Shortened code name or number: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Title: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. Service: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4\. Standard of Care: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5\. Clinical Indicator: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Outputs Menu*Build a Monitor Worksheet*Example

6\. Rationale(s):

\_\_\_ High Risk \_\_\_ Other

\_\_\_ High Volume \_\_\_ Problem Prone

Rationale Explanation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7\. Auto Enroll Monitor: Yes / No

8\. Conditions that apply: (Number each to aid you in answering questions

related to conditions.)

\_\_\_ AGE \_\_\_ OS-106.1

\_\_\_ APPOINTMENT \_\_\_ OS-107

\_\_\_ DEATH \_\_\_ OS-109

\_\_\_ FALL OUT \_\_\_ OS-199

\_\_\_ LAB-CHEM,HEM,TOX,RIA,SER,ETC \_\_\_ PATIENT GROUP

\_\_\_ LENGTH OF STAY IN SPECIALTY \_\_\_ PREVIOUS DISCHARGE FROM WARD

\_\_\_ LENGTH OF STAY ON A WARD \_\_\_ PREVIOUS DISCHARGE MVMENT TYPE

\_\_\_ LENGTH OF STAY SINCE ADMISSION \_\_\_ PREVIOUS DISCHARGE TREAT SPEC

\_\_\_ MANUAL ENROLL CONDITION \_\_\_ PTF DIAGNOSES/OPERATION CODES

\_\_\_ MAS MOVEMENT TYPE \_\_\_ READMISSION

\_\_\_ MH SECLUSION/RESTRAINT \_\_\_ REGISTRATION

\_\_\_ ON SERVICE \_\_\_ RXS 2+ DRUGS IN THE SAME CLASS

\_\_\_ ON TREATING SPECIALTY \_\_\_ SEX

\_\_\_ ON WARD \_\_\_ SPECIALTY TRANSFER

\_\_\_ OS-101.1 \_\_\_ SSN SAMPLE

\_\_\_ OS-102 \_\_\_ WARD TRANSFER

Do any of the conditions require the development of a group? If so, use the

Group Edit option to build the needed group(s). See the condition description for what groups are needed and their parent files.

Group Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Parent File: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Members:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Outputs Menu*Build a Monitor Worksheet*Example

Group Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Parent File:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Members:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Parent File:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Members:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

What other information is required by each condition?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Which conditions define the denominator (sample)?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Choose which conditions define the fall outs and what is their relationship to each other? Use & (and), ! (or), ' (not), and parentheses () to specify the relationship between two or more conditions. Example: (C1&C2)!(C3&C4)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10\. What is the relationship between the conditions that define the denominator (sample)? Use & (and), ! (or), ' (not), and parentheses () to specify the relationship between two or more conditions. Example: (C1&C2)!(C3!C4)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11\. What condition defines the date of the event:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12\. Time Frame: (Choose only one.)

\_\_\_ Annually \_\_\_ Monthly

\_\_\_ Daily \_\_\_ Quarterly

\_\_\_ Fiscal Semi-Annually \_\_\_ Semi-Annually

\_\_\_ Fiscal Yearly \_\_\_ Weekly

Outputs Menu*Build a Monitor Worksheet*Example

13\. Threshold:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If this is a percent threshold, should the threshold be met when the calculated percentage is (high) \>= or (low) \<= the threshold.

14\. For percent thresholds, the Minimum Sample Size:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

For numeric thresholds, the Pre-Threshold Alert Level:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

15\. Do you want to allow 'duplicate' fall outs during the time frame: Yes/No

16\. Other Data to Capture: Review the list of data elements for each condition you are using to select a list for capture with each fall out.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

17\. Do you want to print: 1) Daily fall out list: Yes / No

2\) Daily worksheets: Yes / No

18\. Do you want a bulletin: 1) When threshold met: Yes / No

2\) At end of time frame: Yes / No

3\) When alert level met: Yes / No

19\. What mail group will receive the bulletins:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

20\. Start Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

End Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

21\. Remember to turn it ON and mark it as FINISHED.

  
Outputs Menu

### Condition File Inquire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option produces a report showing the name of the condition, whether or not it is auto enrolled, a description of the condition, and which data elements are associated with the condition. Please note any condition descriptions that call for a group. A group must be defined when that condition is chosen.

Example

Select CONDITION: AGE

Another one: \<RET\>

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

================================================================================

CONDITION: AGE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who fall between an upper

and a lower age limit entered by the user.

This condition will request the following information:

LOWER AGE LIMIT

The lower limit (inclusive) on patient age.

UPPER AGE LIMIT

The upper limit (inclusive) on patient age.

DATA ELEMENTS:

AGE

COVERED BY HEALTH INSURANCE?

DATE OF BIRTH

DATE OF DEATH

MARITAL STATUS

OCCUPATION

RACE

RELIGIOUS PREFERENCE

SERVICE CONNECTED PERCENTAGE

SERVICE CONNECTED?

SEX

SOCIAL SECURITY NUMBER

SPINAL CORD INJURY

================================================================================

  
Outputs Menu

### Data Element File Inquire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option shows you the path (file and field) to the data element. Information provided includes Element Name, File Name, Data Dictionary (DD) Level, Field \#, and DD Number.

Example

Select DATA ELEMENT: SEX PATIENT

Another one: \<RET\>

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

================================================================================

ELEMENT: SEX FILE: PATIENT

DD LEVEL FIELD \# DD NUMBER

1 .02 2

================================================================================

  
Outputs Menu

### Fall Out File Inquire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to see any patient in the Fall Out file (#743.1) and all the data associated with that fall out.

Example

Select PATIENT: CMSPATIENT,ONE XX-1 05-07-91@110000 03-06-23 666456789 EMPLOYEE

Another one: \<RET\>

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

\*\* This information is confidential in accordance with Title 38 U.S.C. 5705 \*\*

================================================================================

NAME: CMSPATIENT,ONE MONITOR: XX-1 (a)

EVENT DATE: MAY 7,1998@11:00 CREATION DATE: MAY 7,1998

AGE 68

DATE OF BIRTH MAR 6,1923

DATE OF DEATH MAY 7,1998@11:00

MARITAL STATUS MARRIED

SERVICE CONNECTED? NO

SOCIAL SECURITY NUMBER 666456789

================================================================================

  
Outputs Menu

### Group File Inquire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option provides you with the name of the group, what file the group is from, and the group members.

Example

Select GROUP: SUBSTANCE ABUSE FACILITY TREATING SPECIALTY

Another one: \<RET\>

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

================================================================================

GROUP: SUBSTANCE ABUSE FILE: FACILITY TREATING SPECIALTY

MEMBERS:

SUBSTANCE ABUSE

================================================================================

  
Outputs Menu

### Monitor Description Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Monitor Description Report option produces an output which shows all the fields which make up the selected monitor(s). Some of these fields may include title, code, start and end dates, clinical indicator, and standard of care.

The report can be sorted by either service or monitor.

Example

Sort report by Service or Monitor: Service// MONITOR

Select MONITOR: PSY-1 LOS ON SUBSTANCE ABUSE FINISHED

Another one: PSY-2

Another one: \<RET\>

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>  
Outputs Menu*Monitor Description Report*Example

MONITOR DESCRIPTION REPORT JUL 17,1998

PAGE: 1

================================================================================

CODE: PSY-1 (a) TITLE: LOS ON SUBSTANCE ABUSE

SERVICE: PSYCHIATRY

STATUS: Finished SWITCH: On START: JUL 17,1998 END:

TIME FRAME: Quarterly THRESHOLD: 5 ALERT LEVEL: 4

HI/LO %: n/a DUPLICATES: Yes

STANDARD OF CARE

------------------

CLINICAL INDICATOR

--------------------

RATIONALE EXPLANATION

----------- --------------

Problem Prone

Other This monitor is looking at the adequacy of

discharge planning for those patients whose

stays exceed the designated 28 days.

MONITOR DESCRIPTION REPORT JUL 17,1998

PAGE: 1

================================================================================

CODE: PSY-2 (a) TITLE: LOS SUBST ABUSE % \>28 DAYS

SERVICE: PSYCHIATRY

STATUS: Under Construction SWITCH: Off START: JUL 17,1998 END:

TIME FRAME: Quarterly THRESHOLD: 1% MIN SAMPLE: 20

HI/LO %: High DUPLICATES: Yes

STANDARD OF CARE

------------------

CLINICAL INDICATOR

--------------------

RATIONALE EXPLANATION

----------- --------------

Problem Prone

Other This monitor will be used to compare

quarterly figures/percent of patients whose

stays exceed 28 days to number of

admissions.

  
Outputs Menu

### Monitor History Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Monitor History Report option shows the statistics for the selected monitor(s) broken up by time frames.

The END date on this report has a different meaning than the END DATE field you see when editing a monitor. The Monitor History END date is the end of a time frame. The monitor END DATE is the date the monitor will stop running. For example, the PSY-1 monitor below has a quarterly time frame, so its first history record covers the month between Oct 1, 1998 and Dec 31, 1998. After Dec 31, 1998, a second history record will be created for PSY-2 with a start date of Jan 1, 1999 and an end date of Mar 31, 1999.

Example

Select MONITOR: PSY-1 LOS ON SUBSTANCE ABUSE UNDER CONSTRUCTION

Another one: \<RET\>

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: 10/1/98 (OCT 01, 1998)

Ending Date: OCT 1,1998// \<RET\> (OCT 01, 1998)

Range selected: OCT 1,1998 to OCT 1,1998

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

MONITOR HISTORY DEC 19,1998

PAGE: 1

--------------------------------------------------------------------------------

CODE: PSY-1 (a) TITLE: LOS ON SUBSTANCE ABUSE

THRESHOLD: 10% MINSAMPLE: 25 TIM FR: QUARTERLY

START: OCT 1,1998 FALL OUT: 1 PERCENT: 5.000%

END: DEC 31,1998 SAMPLE SIZE: 20 THRESHOLD MET: NO

  
Outputs Menu

### Patients With Multiple Fall Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Patients With Multiple Fall Outs option allows you to choose a group of monitors, range of dates, and minimum number of fall outs to appear on the report. The fall outs (patients) must have one fall out within the selected monitor(s).

Example

Select MONITOR: A

By 'A' do you mean all '3' QA MONITOR CODES? YES// \<RET\> (Yes)

Another one: \<RET\>

Minimum number of fall outs per patient:(1-99): 2

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Enter beginning and ending dates for the desired time period:

Beginning Date: 1/1/98 (JAN 01, 1998)

Ending Date: JAN 1,1998// 6/1/98 (JUN 01, 1998)

Range selected: JAN 1,1998 to JUN 1,1998

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

PATIENTS WITH MULTIPLE FALL OUTS (MIN=2) JUL 17,1998

PERIOD FROM JAN 1,1998 TO JUN 1,1998 PAGE: 1

\*\* This information is confidential in accordance with Title 38 U.S.C. 5705 \*\*

PATIENT SOCIAL SECURITY NUMBER

EVENT DATE MONITOR TITLE MONITOR CODE

--------------------------------------------------------------------------------

CMSpatient,ONE 666-45-6789

MAY 21,1998 DEATH XX-1 (a)

MAY 21,1998 LOS ON WARD LOS-1 (a)

## Monitoring System User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Fall Out Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Fall Out Edit option allows you to add a new fall out or edit an existing one. The selected monitor status must be *Finished* in order to utilize this option.

This option must be used to enter data for any monitors whose condition is Manual Enroll.

Example

Select MONITOR: CAT-1 XXX TEST MANUAL ENTRY FINISHED

Select PATIENT: CMSPATIENT,ONE 03-03-33 666456789 EMPLOYEE

EVENT DATE: T-4

Searching FALL OUT file for this patient/monitor...

No fall outs found for this patient/monitor.

Are you adding

CMSPATIENT,ONE 666-45-6789 JUL 14,1998

XXX TEST MANUAL ENTRY CAT-1 (m)

as a new Fall Out record? Y (Yes)

PATIENT: CMSPATIENT,ONE// \<RET\>

MONITOR: CAT-1// \<RET\>

EVENT DATE: JUL 14,1998// \<RET\>

AGE: (1-130): 58// \<RET\>

DIAGNOSIS \[SHORT\]: NASAL POLPYS Replace \<RET\>

FACILITY TREATING SPECIALTY: OTOLARYNGOLOGY// \<RET\>

PRIMARY CARE PHYSICIAN: CMSPROVIDER,TEN// \<RET\>

SOCIAL SECURITY NUMBER: 666456789// \<RET\>

WARD LOCATION: 3W// \<RET\>

Select PATIENT: \<RET\>

Select MONITOR: \<RET\>  
Monitoring System User Menu

### Sample Size Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows the user to edit the sample size for a selected date and selected monitor.

Example

Select MONITOR: CAT-1 XXX TEST MANUAL ENTRY FINISHED

Date for SAMPLE SIZE data: TODAY// \<RET\> (JUL 21, 1998)

SAMPLE SIZE data was last edited: JUL 14,1998

Current FALL OUTS: 2

Current SAMPLE SIZE: 8

Add/Subtract SAMPLE SIZE (-1000000 -\> 1000000): 2

New SAMPLE SIZE: 10

Date for SAMPLE SIZE data: T (JUL 21, 1998)

SAMPLE SIZE data was last edited: JUL 21,1998

Current FALL OUTS: 2

Current SAMPLE SIZE: 10

Add/Subtract SAMPLE SIZE (-1000000 -\> 1000000): \<RET\>

Date for SAMPLE SIZE data: \<RET\>

Select MONITOR: \<RET\>  
Monitoring System User Menu

### Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ad Hoc Fall Out Report

Fall Out File Inquire

Monitor Description Report

Monitor History Report

Patients With Multiple Fall Outs

The options contained on this menu are the same as those found on the Outputs Menu of the Monitoring System Manager Menu. Please refer to the option documentation for these options in the Monitoring System Manager Menu, if necessary.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Alert Level</td>
<td>The level at which a bulletin is sent announcing that this level (pre-threshold) has been met. This is only meaningful for non-percentile thresholds. See Bulletin when Min Sample/Alert Level Met.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Allow Duplicate Fall Outs</td>
<td>Answering YES to this question allows an event to fall out multiple times for the same patient within a given time frame. Answering NO will allow the event to fall out only once per patient per time frame.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Auto Enroll Monitor</td>
<td>This field determines whether or not this is an auto enroll monitor. You should answer YES to this field only if this monitor can be auto enrolled. Your answer will determine which conditions you will be allowed to select.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Auto Run Auto Enroll</td>
<td>This refers to the nightly automatic runs that scan VistA for patients who meet the criteria of the monitors which are set up in the QA MONITOR file (#743).</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bulletin at End of Time Frame</td>
<td>Enter YES if a bulletin should be sent at the end of each time frame.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bulletin Mail Group</td>
<td>This field contains the name of the mail group that the threshold, minimum sample, and end of time frame bulletins will be sent to.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bulletin when Min Sample/Alert Level Met</td>
<td>Enter YES if a bulletin should be sent when the minimum sample is met or when the alert level is met for non-percentile thresholds.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bulletin when Threshold Met</td>
<td>Enter YES if a bulletin should be sent when the threshold is met the first time within the time frame.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Clinical Indicator</td>
<td>This word processing field defines the criteria necessary to meet the standard of care.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Code</td>
<td>This can either be free text or a predetermined list (of initial identifying letters or numbers) as defined by the site so that monitors can be grouped and easily retrieved by the service, section, etc.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Condition</td>
<td>A condition applies a True/False test on selected data elements in a patient's record. If the result of the test is true, that patient's record is captured for further processing.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Condition for Date of Event</td>
<td>Enter the condition number that should be used to capture the event date.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contributes to Sample</td>
<td>This field determines whether or not this condition contributes to the sample size (denominator). This affects how information is collected to determine the size of the sample (denominator).</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>End Date</td>
<td>This field determines when the monitor should stop capturing data or when manual entry of data for this monitor is no longer allowed.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Fall Out</td>
<td>A fall out is a patient who has been found to meet the criteria of a monitor. When a patient falls out a record is created in the FALL OUT file (#743.1) for that patient.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>This field specifically states the relationship between the conditions entered by the user. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Group</td>
<td>A group is a list of similar items. An example would be a group of wards that are all psychiatry wards. Groups may have as many or as few group members as desired.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Hi/Lo Percent</td>
<td>If the user chooses "Hi", the threshold will be met when the percentage is calculated to be &gt;= to the threshold. If the user chooses "Lo", the threshold will be met when the percentage is calculated to be &lt;= the threshold. Hi/Lo is only meaningful for percent thresholds.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Manually Run Auto Enroll</td>
<td>Used to manually queue the auto enroll batch job. This option is used to run the auto enroll if one or more days in the past was missed due to down time.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Minimum Sample</td>
<td>This field defines the minimum sample size (denominator) that must be reached before threshold checking occurs. Minimum sample is meaningful only for percent thresholds.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Monitor</td>
<td>A monitor is made up of a set of conditions (criteria) and the relationships among those conditions. Monitors scan VistA on a nightly basis for patients who meet the monitor’s criteria.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Monitor Status</td>
<td><p>Answer FINISHED to this field only when you are sure you are completely finished entering/editing/</p>
<p>building this monitor. Once you answer FINISHED, you will no longer be able to edit selected monitor fields.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>On/Off Switch</td>
<td>This field controls whether or not a monitor is active. For an auto enroll monitor to capture data, this switch must be turned on. For a manual entry monitor to be selectable, the switch must be turned on. When you wish to stop using a monitor, this switch should be turned off.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Other Data to Capture</td>
<td>When a patient meets the conditions of the monitor and falls out, the other data to capture entries define which data elements in the patient's record should be collected.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Parameter</td>
<td>Parameters further narrow down the definition of a condition. The format of a parameter is determined by the condition.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Print Daily Fall Out List</td>
<td>This field determines whether or not a generic list of all fall outs, sorted by monitor, is printed daily.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Print Daily Worksheets</td>
<td>This field determines whether worksheets are printed daily for all fall outs for this monitor. For this to work, the worksheet must first be created by a programmer and linked to the monitor.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>QM</td>
<td>Quality Management</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>QM Coordinator</td>
<td>An individual tasked with the oversight of QM activities in the medical center.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Rationale</td>
<td>This field defines the rationale for the use of this monitor. You may select all that apply. (high volume, high risk, problem prone, other)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sample Relationship</td>
<td>Enter the relationships among the conditions. This field specifically states the relationship between the conditions that contribute to the sample size. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sample Size</td>
<td>The total number of patient records scanned by a monitor.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Service</td>
<td>This field will allow the manager to track what monitors are currently being used by each service. The service entered has nothing to do with the conditions chosen or what data is auto enrolled.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Standard of Care</td>
<td>This word processing field defines the standard of care to be monitored.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Start Date</td>
<td>This field determines when the monitor should start to capture data or when manual entry of data for this monitor may begin.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Threshold</td>
<td>Threshold defines the number or percentage of fall outs after which some specific action will occur.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Time Frame</td>
<td>Time frame is the period of time over which the program begins capturing data and then sums up the data to start all over again with the beginning of the next similar time frame.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Title</td>
<td>This is a short free text name determined by the user for this monitor.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>

# Option Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ad Hoc Fall Out Report

Ad Hoc Monitor Report

Audit File Inquire

Auto Enroll Run Dates File Purge

Auto/Manual Enroll Monitors Run

Build a Monitor Worksheet

Condition File Inquire

Copy/Edit a Monitor

Data Element File Inquire

Enter/Edit a Monitor

Fall Out Edit

Fall Out File Inquire

Fall Out File Purge

Group Edit

Group File Inquire

History File Purge

Manually Run Auto Enroll

Monitor Description Report

Monitor History Report

Patient Group

Patients With Multiple Fall Outs

Quick Monitor Edit

Rationale Edit

Sample Size Edit

Site Parameters Edit