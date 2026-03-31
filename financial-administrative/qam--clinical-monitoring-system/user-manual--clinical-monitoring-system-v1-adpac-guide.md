---
title: Clinical Monitoring System Version 1 ADPAC Guide
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: anchor
doc_subject: ADPAC Guide
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
description: - [# Introduction/Package Management](#introductionpackage-management) - [# Implementation Check List](#implementation-check-list) - [# Menu Option Assignment](#menu-option-assignment) - [Monitoring System Manager Menu](#monitoring-system-manager-menu) - [Monitoring System User Menu](#monitoring-sys
audience: 
keywords: 
  - condition
  - monitor
  - group
  - fall
  - date
  - class
  - auto
  - enroll
  - movement
  - time
page_count: 0
word_count: 20568
section_count: 22
table_count: 6
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 2
revision_newest: 2/23/09
revision_oldest: 11/15/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmadpac.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmadpac.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=32"
---

![](clinical-monitoring-system-version-1-adpac-guide/001.png)

Clinical Monitoring System V. 1.0ADPAC GuideSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 11/15/04

| Date     | Description (Patch \# if applic.)                                   | Project Manager | Technical Writer |
|----------|---------------------------------------------------------------------|-----------------|------------------|
| 11/15/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data |                 | REDACTED         |
| 2/23/09  | Reformatted Manual                                                  |                 | REDACTED         |

Table of Contents

# # Introduction/Package Management


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction/Package Management](#introductionpackage-management)
- [# Implementation Check List](#implementation-check-list)
- [# Menu Option Assignment](#menu-option-assignment)
  - [Monitoring System Manager Menu](#monitoring-system-manager-menu)
  - [Monitoring System User Menu](#monitoring-system-user-menu)
  - [Monitoring System Programmer Menu](#monitoring-system-programmer-menu)
- [# Package Operation](#package-operation)
  - [Functional Flow](#functional-flow)
    - [Condition File Inquire Option (Outputs Menu)](#condition-file-inquire-option-outputs-menu)
    - [Build a Monitor Worksheet Option (Outputs Menu)](#build-a-monitor-worksheet-option-outputs-menu)
    - [Group Edit Option](#group-edit-option)
    - [Enter/Edit a Monitor Option (Build Monitor Menu)](#enteredit-a-monitor-option-build-monitor-menu)
    - [Copy/Edit a Monitor Option (Build Monitor Menu)](#copyedit-a-monitor-option-build-monitor-menu)
    - [Patients With Multiple Fall Outs Option (Outputs Menu)](#patients-with-multiple-fall-outs-option-outputs-menu)
    - [Fall Out File Inquire Option (Outputs Menu)](#fall-out-file-inquire-option-outputs-menu)
    - [Fall Out Edit Option (Monitoring System User Menu)](#fall-out-edit-option-monitoring-system-user-menu)
    - [Sample Size Edit Option (Monitoring System User Menu)](#sample-size-edit-option-monitoring-system-user-menu)
    - [Auto/Manual Enroll Monitors Run Option (Outputs Menu)](#automanual-enroll-monitors-run-option-outputs-menu)
    - [Manually Run Auto Enroll Option](#manually-run-auto-enroll-option)
    - [Monitor History Report Option (Outputs Menu)](#monitor-history-report-option-outputs-menu)
  - [Auto Enroll Monitors](#auto-enroll-monitors)
    - [Building a Monitor that Automatically Enters/Enrolls Fall Outs](#building-a-monitor-that-automatically-entersenrolls-fall-outs)
  - [Manual Enroll Monitors](#manual-enroll-monitors)
    - [Building a Monitor that Accepts Manually Entered/Enrolled Fall Outs](#building-a-monitor-that-accepts-manually-enteredenrolled-fall-outs)
  - [Conditions, Groups, and Data Elements](#conditions-groups-and-data-elements)
  - [Purge Menu](#purge-menu)
  - [## ## Inquire Options](#inquire-options)
  - [Reports](#reports)
- [Exercises](#exercises)
  - [This section is intended to lead you through the options to build a monitor, enter data into manual monitors, do some trouble shooting, and track the findings from the monitors.](#this-section-is-intended-to-lead-you-through-the-options-to-build-a-monitor-enter-data-into-manual-monitors-do-some-trouble-shooting-and-track-the-findings-from-the-monitors)
  - [Exercise 1 - Condition File Inquire Option](#exercise-1-condition-file-inquire-option)
  - [Exercise 2 - Building an Auto Enrolled Monitor](#exercise-2-building-an-auto-enrolled-monitor)
  - [Exercise 3 - Building a Manual Enroll Monitor](#exercise-3-building-a-manual-enroll-monitor)
  - [Exercise 4 - Entering Data on Manually Enrolled Monitors](#exercise-4-entering-data-on-manually-enrolled-monitors)
- [Glossary](#glossary)
- [Appendix A – Additional Monitor Examples](#appendix-a-additional-monitor-examples)
  - [Lithium Blood Level Lab Test Monitor](#lithium-blood-level-lab-test-monitor)
  - [Transfers to ICU within 24 Hours of Admission](#transfers-to-icu-within-24-hours-of-admission)
  - [JCAHO Indicators of Care](#jcaho-indicators-of-care)
  - [JCAHO Anesthesia Indicators](#jcaho-anesthesia-indicators)
  - [JCAHO Trauma Indicators](#jcaho-trauma-indicators)
  - [JCAHO Cardiovascular Indicator](#jcaho-cardiovascular-indicator)
- [Appendix B - Condition Descriptions](#appendix-b-condition-descriptions)
- [Appendix C - Build a Monitor Worksheet](#appendix-c-build-a-monitor-worksheet)
- [Appendix D - Frequently Asked Questions](#appendix-d-frequently-asked-questions)
Introduction
This guide was designed as an educational and resource manual to support the Quality Management Automated Data Processing Application Coordinator (ADPAC) in installation, testing, training, use, and maintenance of the Monitoring System software.
The ADPAC Guide first gives you a checklist to follow to implement the Monitoring System. The menu options and their assignment to users are then discussed. A series of functional flow exercises illustrate step-by-step typical use of the package and provide examples of building several different monitors. Examples of JCAHO monitors at shown in Appendix A of this guide.
Package Management
Personal data within the package is covered by the Privacy Act. Data from any monitors considered a quality assurance activity is considered confidential and privileged. Title 38 U.S.C. 5705, as amended by Public Law 99-166, and the implementing HSRO (Health Services Review Organization) regulations (Title 38 Part 17) provide that HSRO records and documents which refer to individual practitioners are confidential and privileged. Exempt from this protection are aggregate statistical data, such as trend reports that do not identify individual patients or employees. Access to the software should be restricted to those personnel who meet the site's established access criteria to data for the above purposes.

# # Implementation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 1\. Read the Introduction, Orientation, and Package Management sections of the User Manual.
- 2\. Thoroughly cover the contents of this ADPAC Guide and glossaries in the documentation. Read the Package Operation section of the User Manual to learn about individual menu option functionality.
- 3\. The following software is used by the Clinical Monitoring System. To capture patients with the conditions MH Seclusion/Restraint or RXS 2+ Drugs in the Same Class, the Mental Health or Outpatient Pharmacy software must be running and routinely used. If a condition is chosen that looks at a non-existent file (say Mental Health), the user will be beeped. If the file is there but empty, meaning the site is not using the software or entering data into the file, no fall-outs will result.
- VA FileMan Version 19 or later
- MAS Version 5.2 or later (includes PTF and Scheduling)
- Kernel Version 7.0 or later
- Lab Version 5.1 or later
- Mental Health Version 4.18 or later
- Outpatient Pharmacy Version 5.5 or later
- 4\. Appendix A of this manual shows you how to set up JCAHO Anesthesia, Trauma, and Cardiovascular Indicators of Care. We recommend that if you want to build the JCAHO monitors, you ask IRM to enter YES at the prompt "Do you want to load the ICD Diagnosis/Procedure groups now?" during installation of the software. If the software has already been installed, the groups can be loaded at a later time by IRM. Directions are in the Installation Guide.
- 5\. Set up a test/training account under the direction of IRM. Remember, in order to see fall-out results, you may also have to enter data into VistA packages (admit patients, give them lab tests, etc.) in the test account.
- 6\. At this time IRM should populate (or help you populate) or edit the site parameters through the Site Parameters Edit option. Use the instructional portion of the User Manual for direction.
- 7\. Check with IRM to make sure they have queued the Tasked Run of Auto Enroll option so that it will run every night after midnight.
- 8\. Turn to the Exercises section of this ADPAC Guide and run through the exercises in your test database. Create a hard copy of the conditions, build a group, design a monitor, and enter and retrieve data. You might want to do this with your IRM support person present. Keep the hard copy of the conditions' descriptions as a reference that can be added to with future versions.
- 9\. Show the QM staff the information available to the software (conditions descriptions) and ask them for suggestions of appropriate monitors that you can set up in your test database for practice. If possible, enter patients into the test database that meet the conditions for your monitors and use the Auto/Manual Enroll Monitors Run option to see if they are picked up. Test as much of the software as you can. Become well acquainted with the Outputs Menu.
- 10\. Once you feel comfortable with the software, discuss its function with the QM staff. Determine who the users will be and what options they will be given. You will want to review the Menu Option Assignment section in this guide for suggestions. Give the list of users with the menu options they will need to your IRM support person so that the menu options can be assigned to each user. While it is assumed that this software could be used by any number of services interested in automating data collection for QM monitors, it is suggested that the number of users be kept to a minimum until you, IRM, and the QM staff are comfortable with its use and ready to support/train other users.
- 11\. Ask the users to define the mail group(s) that will receive bulletins from the active monitors. If these mail groups have not been developed, give the information to IRM. (The mail groups must be PUBLIC, not PRIVATE.)
- 12\. Discuss the time frame for setting up a training account, training staff, and going live with the software with both the IRM staff and the QM staff and any other services that might be involved in the use of the software.
- 13\. When you are satisfied that you have mastered the program, show the users how the package works and let them practice in the test account area.
- 14\. Once you and/or the users turn on any of the monitors in the live account, check the outputs frequently for two or three weeks to see if the auto enrollment feature is capturing the records that are expected. If not, you will want to review the conditions selected for those monitors with inaccurate outputs. IRM support may be helpful in fine-tuning the monitors.
- 15\. Set up a routine maintenance schedule to check the outputs. Remember to check after each new monitor is built.

# # Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is suggested that access to the options be provided according to the way the menu is presented. The manager/ADPAC would be given all of the menu options as seen below and the end users would be given just those seen in the User Menu. The User Menu could be further divided to differentiate between users that require edit access and those that just need reports access.

IRM may choose to retain control of the Site Parameter Edit option because it addresses fields that control the auto enroll function which can be very computer intensive.

## Monitoring System Manager Menu

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

> Patients With Multiple Fall Outs

Monitoring System User Menu

> Fall Out Edit

> Sample Size Edit

> Outputs Menu

> Ad Hoc Fall Out Report

> Fall Out File Inquire

> Monitor Description Report

> Monitor History Report

> Patients With Multiple Fall Outs

## Monitoring System User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will notice that the reports available within the Monitoring System User Menu are also found under the Manager's Outputs Menu. They were placed in both menus to make them easier for the manager to access and assign.

You will also notice that access to building monitors was not intended for the users, but for those few managers/ADPACs that have a good working knowledge of VistA, and who will give the time needed to design worthwhile monitors. The managers or ADPACs could be from any service, if there is a need and if the information they require can be/is accessed by the software.

## Monitoring System Programmer Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It should be mentioned here that there is a menu for programmers that is not shown. That menu allows a programmer to add conditions, data elements, time frames, and application groups to the software. They can also edit finished monitors. You must understand that some IRM departments will not be able to provide all of the programming services that this software allows. The Programmer Menu also includes the entire Manager Menu.

# # Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the general flow of the software and how it is best utilized. It takes you through designing a monitor and reviewing summaries of totals, percentages and thresholds. You will gain a better understanding of the flow if you follow up this discussion with the exercises shown in the Exercises Section of this manual.

### Condition File Inquire Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before designing a monitor with this package, you should become acquainted with the types of information the software can access through the exported conditions. The Condition File Inquire option provides descriptions of all the conditions, defines the information the condition requires, and lists data elements for each condition.

Conditions such as the following are used to define fall out records.

All men (SEX)

admitted (MAS MOVEMENT TYPE)

to Medicine Service (ON SERVICE)

age 65 or greater (AGE).

Data elements are patient information you will want to capture for each record that falls out. Note that the list of data elements differs with each condition. For each condition you choose, the data elements lists combine to produce one unique list.

Groups are defined when conditions call for them. As an example, when the MAS Movement Type condition is used, you are prompted "for a group that consists of specific movement types that fall under the transaction type selected." This group could consist of all discharge types. Each condition description tells you when a group is needed.

It is suggested that a manual of conditions be compiled and added to with each new version of the software (See Appendix B - Condition Descriptions). Determine whether or not the information you need for your monitor is found within the condition file (#743.3). If it is, then you can design an auto enrolled monitor.

### Build a Monitor Worksheet Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Print out a worksheet and fill in the information requested. If the conditions you choose do not call for groups, you may skip the Group Edit option. If they do call for groups, decide whether or not you want every item in the group. If you want every item, skip the Group Edit option. If you want a subset of the items, then you must build a group.

Functional Flow

### Group Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you determine which conditions to use, look through the descriptions of each to see if a group will need to be defined for the condition. If it does, then use the Group Edit option before designing your monitor.

### Enter/Edit a Monitor Option (Build Monitor Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you are set to begin the design of the monitor. Use the Build a Monitor Worksheet as your guide to the required information. You have the choice of designing an auto enroll monitor (one that uses your conditions to capture fall out records on a regular basis) or a manual enroll monitor (one that requires you to manually enter the records).

### Copy/Edit a Monitor Option (Build Monitor Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you create a monitor, you may find that you want to build a similar monitor. You may want the exact monitor for another service. You may want monitors that are similar; where one will provide daily fall outs while the other will look at the percentage of fall outs over given time frames.

### Patients With Multiple Fall Outs Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instead of daily printouts (of the fall out patients) which lists each monitor on a separate sheet, you may want to use the Patients with Multiple Fall Outs and Fall Out File Inquire options. The Patients With Multiple Fall Outs option can print sheet(s) of patients that fell out listed alphabetically.

### Fall Out File Inquire Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Fall Out File Inquire option and print each patient separately, along with their data elements. Each printout can be used as a worksheet.

### Fall Out Edit Option (Monitoring System User Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever a manual enroll monitor is created, it requires the user to input the records that meet the definitions of what the monitor intends to track. These records can only be entered via the Fall Out Edit option.

### Sample Size Edit Option (Monitoring System User Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you also intend to track percentages and thresholds on manually entered records, then the Sample Size Edit option must be used to enter changes in the sample reviewed.

Functional Flow

### Auto/Manual Enroll Monitors Run Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To troubleshoot and keep on top of dates when monitors have been run, you will need to use the Auto/Manual Enroll Monitors Run option. This report shows which monitors ran for each date.

> Automatic Report

> The following is a sample of the report that is automatically printed every night after the tasked auto enroll finishes processing. Note the dates on the report. July 20, 1998 was the day the Monitor was scanning. July 21, 1998 was the day the program ran and printed out the report.

AUTO/MANUAL ENROLL MONITORS RUN JUL 21, 1998

FOR JUL 20, 1998 PAGE: 1

AUTO ENROLL RUN DATE

MONITOR CODE (a/m=AUTO/MANUAL) MONITOR TITLE DATE RUN

--------------------------------------------------------------------------------------

JUL 20, 1998

AMA-1 (a) IRREG DISCHARGES JUL 21, 1998

AMA-2 (a) PSYCH IRREG DISCHARGES JUL 21, 1998

CH-1 (a) LITHIUM JUL 21, 1998

CH-2A (a) XFER FROM E/R TO CCU JUL 21, 1998

CH-2B (a) ACUTE MI DX JUL 21, 1998

LAB-1 (a) Elevated WBC's JUL 21, 1998

LITHIUM-1 (a) LITHIUM BLOOD LEVEL DONE JUL 21, 1998

MANUAL MONITOR (m) MANUAL JUL 21, 1998

PSY-3 (a) LOS ON SUBSTANCE ABUSE JUL 21, 1998

### Manually Run Auto Enroll Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Active monitors are normally run as a nightly task. IRM Service can schedule this task for you (see Technical Manual). The main purpose for the Manually Run Auto Enroll option is to use it only when one or more monitors has not run for a day. If a monitor has already been run for a given date in the past, the monitor will not rerun for that same day. Auto enroll looks at VistA transactions from the previous day (this includes updating Monitor History Statistics for records/fall outs manually entered). In other words, when auto enroll runs "tomorrow," it will only pick up fall outs with event dates of "today", not "yesterday", or any time before that.

For manually enrolled monitors, it is important to remember that it is the entry date, not the event date, that determines whether or not the data will be counted. A manually enrolled monitor requires total manual entry of fall out data. This option should be used whenever the auto enroll mechanism fails to run due to down time.

Functional Flow

### Monitor History Report Option (Outputs Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To follow-up and track changes in the monitors over time frames for reporting purposes, the Monitor History Report option provides a brief summary of percentages of fall out records to samples reviewed, and whether or not the threshold was met or surpassed. There will be one Monitor History summary per time frame for any given monitor.

## Auto Enroll Monitors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Building a Monitor that Automatically Enters/Enrolls Fall Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Building a monitor is defined as entering the conditions and how they relate to each other that will produce a needed record. A fall out record is one that meets the conditions as entered by the user. Records captured in this way are enrolled by the daily automatic enrollment feature of the software.

#### Enter/Edit a Monitor Option (Build Monitor Menu)

The following explains the major portions of the Enter/Edit a Monitor option. Refer to Appendix C, Build a Monitor Worksheet, if necessary.

*Standardizing Code Names*

Before utilizing this software, determine a method of standardizing the code names so monitors for each service can easily be identified. The list of monitors does not differentiate between users. If Surgical Service accesses the software, it will see all the monitors, not just theirs.

*Choosing Conditions*

Run off a hard copy of the definitions for each condition and its contents (data elements) to use as a reference. You may also refer to Appendix B, Condition Descriptions, at the end of this guide. Before building a monitor, review the hard copy to determine which conditions you plan to use.

Discuss your choice with the ADPAC for the package that will be accessed by the Monitoring System or with IRM to make sure the information you want will be found in the condition(s) you choose.

Sometimes you need to use the same condition twice in one monitor. To enter the condition a second time, use quotes (" ") around the condition. For the longer conditions, put quotes around a sufficient portion of the name to distinguish it from others like it, such as the following:

Condition \#1 Previous Discharge Treat Spec

Condition \#2 "Previous Discharge T"reat Spec

You can always see the conditions previously chosen by entering a "?" at the "Select CONDITION:" prompt.

Auto Enroll Monitors

*Defining Groups*

Depending on the condition selected, you may need to define a group before completing the monitor enter/edit. Read the condition description (available through the Condition File Inquire option) to find out if you need a group. Some conditions require a group. Some conditions ask questions that narrow down the scope of possible fall outs and do not require groups. The Age condition, for example, does not require a group because it asks for age ranges.

Other conditions ask a series of questions and give you the opportunity to select a group (which must be predefined through the Group Edit option). For these conditions, the series of questions may sufficiently narrow down the scope of possible fall outs for your purposes; in which case, you would press \<RET\> at the group prompt. If you determine that the scope needs to be further narrowed down, you must define a group. You will need to know what parent file (e.g., Hospital Location file, Facility Treating Specialty file, Movement Type file, etc.) has the information you will need. The condition descriptions tell you from which file you will select entries to be included in the group.

Let's walk through a difficult example using the Appointment condition. We want a list of all patients who were not seen in GU clinic and did not receive another appointment. Here is a copy of the description for the Appointment condition.

DESCRIPTION:

This condition produces a list of all appointments on the day that auto

enroll is scanning. The user may screen the appointments by entering a

clinic group, the appointment status, the purpose of the visit, and/or

an appointment type group.

This condition will request the following information:

CLINIC GROUP

A group of entries from the HOSPITAL LOCATION file (#44).

STATUS

The status of the appointment, i.e., No-show, Cancelled, etc.

PURPOSE OF VISIT

The purpose of the patient visit, i.e., C&P, 10/10, Unscheduled, etc.

APPOINTMENT TYPE GROUP

A group of entries from the APPOINTMENT TYPE file (#409.1).

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past for

an appointment.

Auto Enroll Monitors

The condition will ask for a clinic group. Leaving the Clinic Group blank would give me every clinic. Since I only want GU Clinic, I know I must define a group that contains just the GU clinic from the Hospital Location file.

The condition will ask for appointment status for this group I defined. From the status list I see I will need the following statuses but I will not need a group.

No Show

Cancelled by Clinic

Inpatient Appointment

Cancelled by Patient

The condition will ask if it needs to look at the purpose of the visit for the clinic group. We don't need to monitor any of the purposes, so I know I will be able to bypass the "Purpose of Visit" prompt.

I don't have to define the second group (appointment type) as the definition uses "and/or". However I need to check out the contents of the Appointment Type file just in case it would help. After reviewing it, I see that I could make a group for just Regular appointments. But, there is no need, so I will bypass this prompt by striking the \<RET\> key when I am building the monitor. It also means I can bypass the look back days.

Hospital Location file contents differ from site to site but the Status, Purpose of Visit, and Appointment Types are taken from the PIMS software and are the same for everyone.

*Determining Condition for Date of Event*

Enter the condition number that should be used to capture the event date.

You will be given a list of all the conditions you chose for your monitor. You must decide which one of the conditions will provide the Date of Event for the software. This date is important for setting the fall out record within your chosen time frame. Conditions that happen on specific days such as deaths, admissions, discharges, and transfers are typically the conditions you should choose from. However, there are exceptions when a condition that does not seem to be date-related can be chosen.

Auto Enroll Monitors

*Determining Fall Out Relationships*

This field specifically states the relationship between the conditions you entered. You may use the following to specify the relationship.

& and

! or

' not

() parentheses

How do your chosen conditions relate to each other to define the records you want to fall out? If necessary, consult with IRM about defining relationships. This is very important to the functioning of the auto enrollment feature.

Example: You want to see records for all patients age greater than 65 & (and) were discharged from either this ward ! (or) that ward &' (and did not) die.

Condition

Greater than 65 Age C1

Discharged Ward A MAS Movement Type C2

Discharged Ward B MAS Movement Type C3

Death Death C4

The Fall Out Relationship would be entered like this: C1&(C2!C3)&'C4

If this is confusing to you, the best way for you to begin is to select only one or two conditions for each monitor until you feel more adept at using the software.

*Defining Sample and Sample Relationship*

Some monitors do not require a sample because the data from the monitor will not be used for comparisons across time frames. Perhaps you are just looking for a list of patients to review or a list of fall outs to use for another monitor. If such is the case, bypass all questions relating to Sample by striking the \<RET\> key. Just before finishing the monitor, you will receive the messages "Warning: SAMPLE RELATIONSHIP not specified" and "No errors found". This is acceptable. A warning statement does not always need to be corrected. It depends entirely on what you intend the monitor to do for you. Error statements, on the other hand, must be corrected.

Auto Enroll Monitors

When you do want to track the number of fall outs (numerator) per the sample (denominator), you will need to define for the monitor which of the conditions make up the sample size or denominator. As you build your monitor, you will be asked to tell the software which of your chosen conditions helps to make up the sample. The sample becomes the denominator for determining what the percent of fall outs for the time frame is and is also used to determine when thresholds are met or exceeded.

- Contributes to Sample - This field determines whether or not this condition contributes to the sample size (denominator). This affects how information is collected to determine the size of the sample (denominator). Once you tell the software which conditions contribute to the sample, the software will display all those conditions for you so that you may define how those conditions relate to each other in determining the sample. You will respond YES or NO to this question for each condition entered.

Once you tell the software which conditions contribute to the sample, the software will display all those conditions for you so that you may define how those conditions relate to each other in determining the sample.

- Sample Size Relationship - Enter the relationship among the conditions. This field specifically states the relationship between the conditions that contribute to the sample size. You may use & (and), ! (or), ' (not) and parentheses () to specify the relationship. Does this look familiar? It is the same method used in defining Fall Out Relationship. Once again, if defining samples is not easy for you, discuss this with your IRM support person.

*What Does Time Frame Really Mean?*

Time frame tells the software when to start counting anew the number of fall outs and when to begin building the sample. Fall outs are NOT purged automatically at the end of a monitor's time frame. Time frame then tells the software when to quit counting and begin all over again. Time frames are used by the Monitor History file (#743.2) to show you stats for each chosen monitor so that one time frame can be compared to the next. At the end of a monitor's time frame, a new monitor history record is created for it and cumulative counting begins again.

Time frame does not tell the monitor when to quit auto enrolling records. That is done by the 'ON/OFF' switch, the 'START and END DATES', and the UNDER CONSTRUCTION or FINISHED 'MONITOR STATUS'. You must always enter a time frame even if a time frame does not seem essential to the output you wish to capture.

Auto Enroll Monitors

*Choosing a Threshold*

This discussion is not intended to explain how thresholds are derived. It is meant to discuss what happens when a threshold, either a number or percent, is entered.

For the threshold to be calculated the following fields must be completed: Conditions, Condition for Date of Event, Fall Out Relationship, Sample Relationship, Time Frame.

If a number threshold is entered, the software will calculate the threshold by counting each fall out from the beginning of the time frame until the threshold is met or exceeded. If a percent threshold is entered, you must also enter a number of records that will make up a minimum sample before the percent of fall outs to sample is calculated,

> THRESHOLD: 3%

> Minimum Sample

> For PERCENT thresholds this field defines the minimum sample size (denominator) that must be reached before threshold checking occurs.

> For NUMERIC thresholds this field may be used along with the BULLETIN WHEN MIN SAMPLE MET field (set to YES) as a pre-threshold notification.

and whether the percent calculated should be greater than or equal to, or less than or equal to the percent threshold.

Hi/Lo Percent

If the user chooses 'Hi', the threshold will be met when the percentage

is calculated to be \>= the threshold.

If the user chooses 'Lo', the threshold will be met when the percentage

is calculated to be \<= the threshold.

Hi/Lo Percent is only meaningful for percent thresholds.

CHOOSE FROM:

H HIGH

L LOW

*What is Meant by Duplicate Fall Outs?*

Duplicate fall outs does not mean enrolling the very same event (same day and same time) twice for a patient. It refers to two or more separate but like events for a patient within the time frame. Think about how you would handle the problem if you were looking at patient records. Do you want to know every instance of when a condition occurs to a patient within the same time frame, or will once be sufficient? Think about the definitions of your sample and your fall outs. Will 'duplicates' (every admission, every transfer, every CBC, every chest x-ray) muddy the findings or are they necessary to the findings?

Auto Enroll Monitors

*Determining Other Data to Capture*

Decide what information you want for every fall out record before you build your monitor. That will help you limit yourself to what is really needed. The condition description list will show which data items are available for each condition. Then when you choose from the available information listed, you can pick those things that match your list. Remember that not all information you might need can be found within VistA and may not be available to you through the conditions you choose.

*Bulletins*

Bulletins are simple mail messages that provide data on what is going on with the monitor. Bulletins can report when a threshold or alert level has been met and when the time frame is up.

*Activating/Deactivating a Monitor*

Activating and deactivating monitors depend on the following four fields.

> Start Date: This is the date the monitor should begin. The start date may fall in the middle of the time frame chosen for the monitor. In such cases, statistics for the first time frame will not reflect a full time frame set of data.

> End Date: If the end date is reached, the monitor will quit auto enrolling records. This field does not have to be completed for the monitor to run.

> On/Off Switch: This field controls whether or not a monitor is active. For an auto enroll monitor to capture data, the switch must be turned ON. For a manual entry monitor to be selectable, the switch must be turned ON. When you wish to stop using a monitor, this switch should be turned OFF.

> Monitor Status: Answer FINISHED to this field only when you are sure you are completely finished entering/editing this monitor; otherwise the monitor will be labeled as UNDER CONSTRUCTION. Once you answer FINISHED you will no longer be able to edit selected monitor fields, such as the conditions and their relationships.

## Manual Enroll Monitors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Building a Monitor that Accepts Manually Entered/Enrolled Fall Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be monitors that cannot be automatically enrolled due to the type of information or data that needs to be reviewed. An example would be those patient records that are reviewed for documentation. Say at discharge, the record is reviewed for a discharge note and the content of the note. The reviewer checks for the presence of the note, discussion of medications, the follow-up outpatient visit, any discharge precautions, etc. This information can only be found in the hard copy patient record, so it cannot be auto enrolled. However, a monitor can be designed that will accept the manual entry of a record of this type. You would manually enter all those records that fail review and enter the total count of records reviewed so the Monitoring System can track the percentage of fall out records for you.

After one or more records are manually entered via the Fall Out Edit option, they are counted by the nightly run of auto enroll based on their entry date. The count is then stored in the Monitor History file (#743.2).

#### Enter/Edit a Monitor Option

The same option is used to design the manually entered monitor as the auto enrolled monitor, but there are two major differences.

At the AUTO ENROLL MONITOR prompt, the user answers NO.

At the CONDITION prompt, the user answers MANUAL ENROLL CONDITION.

#### Sample Size Edit Option

The other main option that is needed for the manually enrolled monitor is Sample Size Edit. To keep a current count of fall outs versus sample, the user must routinely edit the sample size.

## Conditions, Groups, and Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Conditions*

A condition (or set of conditions) defines which records become fall out records. Conditions may be dependent upon defining a group. Be sure to read the description of each condition to see if a group will be needed.

*Data Elements*

These are the pieces of patient information that you want captured along with the fall out record. They vary in availability with the conditions that are chosen.

*Building Groups (Group Edit)*

Many of the conditions need to be further defined by building groups that will limit the condition to a specified range, such as a group of movement types, a group of wards, a group of similar medications, a group of diagnoses. Any condition that requires a defined group will refer to group in its description. The exercises in this manual will walk you through using the Conditions File Inquire option and defining a group.

## Purge Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Menu should be used by the IRM support person or the QM ADPAC to purge the following three files. Set standard time frames for purging the data to keep the database running smoothly.

*Auto Enroll Run Dates File Purge*

The Auto Enroll Run Date file (#743.6) contains each date that the auto enroll ran and the monitors that ran on that date. This is the information you will be purging. In other words, if you want to see what dates auto enroll ran and which monitors were in each run, this file can tell you. Saving these dates for any length of time is not necessary if auto enroll runs every day. You may decide to run this purge more frequently than the other purge options. One method may be to purge by the quarter. The run date(s) to be purged must fall within the selected date range for purging.

Purge Menu

*Fall Out File Purge*

The Fall Out file (#743.1) stores the patient name, monitor, event date, date the record was created, and any data elements associated with the record. Purging this information can be more critical. You may want to store this data for two or three years before purging it. If a monitor has turned out to be useless, in other words the data is useless, you can purge just the data for a single monitor. The fall out event date(s) to be purged must fall within the selected date range for purging.

*History File Purge*

The Monitor History file (#743.2) stores the monitor, start date, end date, number of fall outs, sample size, threshold met, date met, and bulletins sent. You may want to keep this data for awhile to compare data across time frames for many monitors. The time frame start date(s) to be purged must fall within the selected date range for purging.

## ## ## Inquire Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Condition File Inquire Option*

You will want to use this option to print a list of all the conditions available. It describes each condition, states whether or not it requires a group, and lists the data elements associated with it.

*Data Element File Inquire Option*

This option may be of more interest to the IRM staff. It shows the path (file and field) to the data element. However, as a user, you may wish to be aware of where the data comes from.

*Fall Out File Inquire Option*

This option lets you look at any patient and the fall outs for that patient. This is one method of checking patients with multiple fall outs. It shows all the data associated with each fall out. The Patients With Multiple Fall Outs option only lists the dates and monitor for each fall out.

*Group File Inquire Option*

Before defining a new group, you may want to check this option for a similar group that can be used. This option lists the group members and the parent file.

*Audit File Inquire Option*

This option allows you to pick a fall out record and view its audit file entry. The audit file data includes information on who modified the record, when it was modified, and what modification was performed.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Ad Hoc Fall Out Report*

Refer to the Exercises section of this manual for an example of using the ad hoc.

*Ad Hoc Monitor Report*

Refer to the Ad Hoc Report Generator documentation in the QM Integration User Manual for instructions on how to use the ad hoc.

*Monitor Description Report*

The Monitor Description Report provides a detailed description of the monitor. This is a nice summary of the rationale, standard of care, clinical indicator, how often data is compiled, threshold, etc. It does not show what conditions are used to build the monitor or what data elements are captured.

*Monitor History Report*

This file is updated nightly and will show the latest number of fall outs and sample size, percent of fall outs per sample, and whether the threshold has been met.

*Patients with Multiple Fall Outs*

This is a report for checking to see if a particular patient has been involved in more than one fall out record.

# Exercises

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This section is intended to lead you through the options to build a monitor, enter data into manual monitors, do some trouble shooting, and track the findings from the monitors.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Exercise 1 - Condition File Inquire Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Condition File Inquire option within the Monitoring System Manager's Outputs Menu lists all the accessible conditions in the software, gives a description of each, and lists all the other information (data elements) that can be captured if the condition is chosen. You will want to put together a manual of the conditions and add to it whenever any new conditions are added to the software. You can download to a PC to capture the data or you can send the output to a printer. The option will print one condition per page, or if downloaded to a PC and edited, you can print more than one to a page.

The following example would provide a print out of all conditions.

Select Outputs Menu Option: CONDITION File Inquire

Select CONDITION: ALL

By 'ALL' do you mean ALL NAMES? YES// \<RET\>

Another one: \<RET\>

DEVICE: QA Printer

============================================================================

CONDITION: AGE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who fall between an upper and a lower age limit entered by the user.

This condition will request the following information:

LOWER AGE LIMIT

The lower limit (inclusive) on patient age

UPPER AGE LIMIT

The upper limit (inclusive) on patient age.

Exercise 1 - Condition File Inquire Option

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

SPINAL CORD INJURY Any of these data elements can be requested for retrieval if

the *Age* condition is selected when building a monitor.

============================================================================

============================================================================

CONDITION: APPOINTMENT AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all appointments on the day that auto enroll is scanning. The user may screen the appointments by entering a clinic group, the appointment status, the purpose of the visit, and/or an appointment type group.

This condition will request the following information:

CLINIC GROUP

A group of entries from the HOSPITAL LOCATION file (#44).

STATUS

The status of the appointment, i.e., No-show, Cancelled, etc.

PURPOSE OF VISIT

The purpose of the patient visit, i.e., C&P, 10/10, Unscheduled, etc.

APPOINTMENT TYPE GROUP

A group of entries from the APPOINTMENT TYPE file (#409.1).

LOOK BACK TIME

The number of days (in addition to yesterday) to look into the past

for an appointment.

Exercise 1 - Condition File Inquire Option

DATA ELEMENTS:

AGE

APPOINTMENT DATE/TIME

APPOINTMENT STATUS

APPOINTMENT TYPE

APPT. CANCELLATION REASON

CLINIC

COVERED BY HEALTH INSURANCE?

DATE OF BIRTH

DATE OF DEATH

MARITAL STATUS

OCCUPATION

PURPOSE OF VISIT

RACE

RELIGIOUS PREFERENCE

SERVICE CONNECTED PERCENTAGE

SERVICE CONNECTED?

SEX

SOCIAL SECURITY NUMBER

SPINAL CORD INJURY Although not on this list, patient name is always one of

the data elements retrieved.

Conditions are used to define your fall out records and sample size.

Data elements are the bits of information you will want to capture for each record that falls out. Note that the list of data elements differs with each condition. Due to limitations in this version of Monitoring System, occasionally some of the data elements you request may not be retrieved.

## Exercise 2 - Building an Auto Enrolled Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that you have determined what information is available to you, let's develop a monitor. Define your monitor before beginning. Use the Build a Monitor Work-sheet to show you what information is required by the Enter/Edit a Monitor option.

*Determining the conditions to use*

You want to see the records of all females admitted to the hospital so the records can be reviewed for gynecological exams. For each record, you want the patient's name, social security number, admission date, last admission and discharge dates, and the admission ward. Can this monitor be auto enrolled? Can all the data you want be captured?

First let's review the Condition file (#743.3) to determine whether there are conditions that will meet our needs. The most obvious conditions that appear to meet our needs are Sex and MAS Movement Type. Let's review the descriptions and data elements for these two conditions.

=============================================================================

CONDITION: SEX AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of Male or Female patients.

This condition will request the following information:

SEX

The sex of the patients who should be captured.

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

Exercise 2 - Building an Auto Enrolled Monitor

============================================================================

CONDITION: MAS MOVEMENT TYPE AUTO ENROLL: YES

DESCRIPTION:

This condition allows the user to track selected MAS movement types.

First the user must select the transaction type of movement he wishes

to track, Admission, Transfer, Discharge, Check-in Lodger, Check-out

Lodger, or Treating Specialty. The user is then prompted for a group

that consists of specific movement types that fall under the

transaction type selected above.

This condition will request the following information:

MAS MOVEMENT TRANSACTION TYPE

The desired patient movement transaction type, i.e., admission,

transfer, discharge, etc.

MOVEMENT TYPE GROUP

A specific subset of patient movements that fall within the

transaction type chosen above. If admission was chosen as the

transaction type, the movement type group might include direct,

transfer in, etc. A group of entries from the MAS MOVEMENT TYPE file

(#405.2).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

These are the conditions that will be used. After seeing the data elements that are available for capture, we can also capture age for the fall out records. We will not be able to capture previous admission and discharge dates, but everything else seems okay. Now that we have determined that the Monitoring System can access the required information to find all women who are admitted to the hospital, we should now plan for all the other information that will be required to build this particular monitor.

Exercise 2 - Building an Auto Enrolled Monitor

One of the first things to be decided can be determined by referring back to the descriptions of the conditions. Always look to see if you will need to provide a group for a particular condition. In this case, the MAS Movement Type will need a group because we only want to look at direct admissions. What does this mean?

*Defining a Group*

A group is a list of members that will define the group you need. In this example, we will need to define one for Admission for the MAS Movement Type. The Group Edit option will help us limit our choices so we won't have to guess at what is required. Now is the time to do this before we begin building the monitor.

We will need to name this group. Give it a name that defines exactly what you are after within MAS Movement Type. You may want to use this same group for another monitor.

Select Monitoring System Manager Menu Option: Group Edit

Select GROUP: Direct Admissions

ARE YOU ADDING..... Y

GROUP PARENT FILE: ??

This field determines which file the group entries are to be found in.

CHOOSE FROM:

2 PATIENT

3 USER

6 PROVIDER

16 PERSON

37 DISPOSITION

42 WARD LOCATION

44 HOSPITAL LOCATION

45.7 FACILITY TREATING SPECIALTY

49 SERVICE/SECTION

200 NEW PERSON

405 PATIENT MOVEMENT

405.2 MAS MOVEMENT TYPE

405.3 MAS MOVEMENT TRANSACTION TYPE

409.1 APPOINTMENT TYPE

743 QA MONITOR

743.1 FALL OUT

Exercise 2 - Building an Auto Enrolled Monitor

Your list might look different than this one as each is defined by the site. If you need a file that is not in your list, speak with your IRM support person to see if it can be added (through the Application Group Edit option in the QM Programmer Menu).

GROUP PARENT FILE: 405.2 MAS MOVEMENT TYPE

NAME: Direct Admissions// \<RET\>

PARENT FILE: MAS MOVEMENT TYPE// \<RET\> (No Editing)

Now you must decide what you need within the MAS Movement Type. For this example, we need only direct admissions.

Select GROUP MEMBER: ??

You may enter '\[GROUP MEMBER' to select all entries that CONTAIN

the text 'GROUP MEMBER'. Enter '\[\*' to select ALL entries.

You may use a prefix of minus (-) to delete a range of group

members, for example '-\[GROUP MEMBER' or '-\[\*'.

> **WARNING:** Use of the contains operator (\[) is very computer intensive!

If you are having trouble adding another group member at the 'Select

GROUP MEMBER:' prompt try enclosing the new entry in quotes, e.g.,

"GROUP MEMBER".

> **NOTE:** Use of the '\[' may be disabled through the site parameters.

ANSWER WITH MAS MOVEMENT TYPE ENTRY NUMBER, OR NAME

DO YOU WANT THE ENTIRE 46-ENTRY MAS MOVEMENT TYPE LIST? Y (YES)

CHOOSE FROM:

1 AUTH ABSENCE 96 HOURS OR LESS

2 AUTHORIZED ABSENCE

3 UNAUTHORIZED ABSENCE

4 INTERWARD TRANSFER

5 CHECK-IN LODGER

6 CHECK-IN LODGER (OTHER FACILITY)

7 CHECK-OUT LODGER

8 AMBULATORY CARE (OPT-AC)

9 TRANSFER IN

10 TRANSFER OUT

11 NON-SERVICE CONNECTED (OPT-NSC)

12 DEATH

13 TO ASIH (VAH)

............

Select GROUP MEMBER: 15 DIRECT

GROUP MEMBER: DIRECT// \<RET\>

Select GROUP MEMBER: \<RET\>

Select GROUP: \<RET\>Exercise 2 - Building an Auto Enrolled Monitor

Do we need to prepare any other information before we build the monitor? Carefully look over the questions you will be asked and use the glossary for definitions of the terms. You might want to make out a list of your answers using the Build a Monitor Worksheet before accessing the option. You may also want to consider determining a method of naming/coding monitors, such as the code always beginning with the Service initials to which it belongs, etc. Refer to the Enter/Edit a Monitor option in the Clinical Monitoring System User Manual, if necessary.

Select Build Monitor Menu Option: Enter/Edit a Monitor

Select MONITOR: QA-1

CODE: QA-1// \<RET\>

TITLE: Female Admissions

SERVICE: QUALITY ASSURANCE

STANDARD OF CARE:

1\>All female patients should have...

2\>\<RET\>

EDIT Option: \<RET\>

CLINICAL INDICATOR:

1\> Yearly exams....

2\> \<RET\>

EDIT Option: \<RET\>

Select RATIONALE: Problem Prone

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// \<RET\>

Select CONDITION: SEX

CONDITION: SEX// \<RET\>

SEX: (M/F): F

CONTRIBUTES TO SAMPLE: YES

Select CONDITION: MAS MOVEMENT TYPE

CONDITION: MAS MOVEMENT TYPE// \<RET\>

MAS MOVEMENT TRANSACTION TYPE: ADMISSION

ADMISSION TYPE GROUP: DIRECT ADMISSIONS This is the group that we built earlier.

CONTRIBUTES TO SAMPLE: NOExercise 2 - Building an Auto Enrolled Monitor

Select CONDITION: \<RET\>

=============================================================================

CODE CONDITION

------ -----------

C1 SEX

C2 MAS MOVEMENT TYPE

FALL OUT RELATIONSHIP: C1&C2

> Before moving past this, make sure you understand why C1&C2 is entered. Speak with your IRM support staff if this is confusing.

=============================================================================

CODE CONDITION

------ -----------

C1 SEX

SAMPLE RELATIONSHIP: C1

> The software helps us with our choice.

=============================================================================

NUMBER CONDITION

-------- ----------

1 SEX

2 MAS MOVEMENT TYPE

CONDITION FOR DATE OF EVENT: 2

> For the Date of Event, we will be asked to choose between Sex and MAS Movement Type. The Date of Admission is when we need to pick up the fall outs which are found under MAS Movement Type.

=============================================================================

Exercise 2 - Building an Auto Enrolled Monitor

TIME FRAME: Annually

> What will we get if we enter a time frame here? We will get the number of patients that were females and were direct admissions to the hospital during the time frame chosen. This could be useful in checking numbers for sample size. Let's choose annually. You must always enter a time frame even if a time frame does not seem essential to the output you are after. At the end of a year, totals and statistics that have been accumulating in the Monitor History file (#743.2) record for this monitor will stop and a new record will be created for the next year.

THRESHOLD: \<RET\>

> We are not concerned with threshold for this monitor.

PRE-THRESHOLD ALERT LEVEL: \<RET\>

> Not needed with this monitor.

ALLOW 'DUPLICATE' FALL OUTS: YES

> If the same female patient is admitted twice within the yearly time frame, we want to see both admissions.

Select OTHER DATA TO CAPTURE: AGE

Select OTHER DATA TO CAPTURE: SOCIAL SECURITY NUMBER

Select OTHER DATA TO CAPTURE: WARD LOCATION

Select OTHER DATA TO CAPTURE: MOVEMENT DATE/TIME

Select OTHER DATA TO CAPTURE: \<RET\>Exercise 2 - Building an Auto Enrolled Monitor

PRINT DAILY FALL OUT LIST: NO// YES

> We need this printout to know which records to review.

PRINT DAILY WORKSHEETS: NO// \<RET\>

> This software offers the site the opportunity to develop worksheets and use this software to automate their daily print out with the patient data already on it.

BULLETIN WHEN THRESHOLD MET: NO// \<RET\>

BULLETIN AT END OF TIME FRAME: NO// \<RET\>

BULLETIN WHEN ALERT LEVEL MET: NO// \<RET\>

The following fields with the exception of END DATE must be completed for the monitor to be activated.

START DATE: TODAY

> Even though our time frame is annually, the monitor will begin capturing data immediately because we entered Today as the start date. You must remember to take this into account when you review the monitor history file (#743.2) for your monitor. The first set of figures will be based on a time frame that is defined by the start date.

END DATE: \<RET\>

> It is not necessary to fill this in unless there is a definite end date for the gathering of data for this monitor.

ON/OFF SWITCH: ON

> It must be turned on.

Exercise 2 - Building an Auto Enrolled Monitor

MONITOR STATUS: FINISHED

Once you are familiar with the Enter/Edit a Monitor option, you won't have to be so particular about how you go about the process, you can always go back to it for editing if you have not labeled it as "Finished". However, when you are first learning, it pays to be prepared. Fill in the Build a Monitor Worksheet and you will be fully prepared to use the Enter/Edit a Monitor option.

Now, admit several female patients for "today" into the test data base and tomorrow use the Run Auto Enroll Manually option to see if these patients fall out. The Event Date must be in the past for this option to work.

## Exercise 3 - Building a Manual Enroll Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that we have a monitor that provides us with a daily list of patient names and admission wards for all female patients, we also want a monitor that can tell us how well we are doing in meeting the requirements for gynecological exams of all female patients. Since our criteria to determine whether or not a patient has had the exams or been offered them cannot be auto enrolled, we will have to review the records and manually enroll the fall out records in the Monitoring System software. We will also have to manually tell the software how many records were reviewed so that it can determine percentages and report to us if we surpass thresholds. So a Manual Enroll Monitor is built when the conditions needed cannot be automatically enrolled by the software.

Since we have a good deal of information already in the original monitor that will remain the same for this monitor, let's use the Copy/Edit a Monitor option.

Select Build Monitor Menu Option: Copy/Edit a Monitor

Select MONITOR TO COPY: QA-1 FEMALE ADMISSIONS FINISHED

Are you sure you want to copy this monitor? NO// y (YES)

Copying monitor, please wait...

You may now edit the copy of the monitor, please change the CODE and TITLE.

CODE: Copy of QA-1// QA-2

TITLE: Copy of FEMALE ADMISSIONS Replace ... With Gyne exam compliance

Replace \<RET\>

Gyne exam compliance

SERVICE: QA// \<RET\>

STANDARD OF CARE:

1\>All female patients should have...

EDIT Option: \<RET\>

CLINICAL INDICATOR:

1\>Yearly exams.....

EDIT Option: \<RET\>

Select RATIONALE: Problem Prone// \<RET\>

RATIONALE: Problem Prone// \<RET\>

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES// N

Select CONDITION: MANUAL ENROLL CONDITION This is the <u>only</u> condition needed

when building a manual enroll

monitor.

CONDITION: MANUAL ENROLL CONDITION// \<RET\>Exercise 3 - Building a Manual Enroll Monitor

CONTRIBUTES TO SAMPLE: NO

> The records we will be manually enrolling are records that don't meet the standards for gynecological exams. Our sample (the total records reviewed) will be manually entered by us, so this prompt should be bypassed or you can enter NO here.

Select CONDITION: \<RET\>

=============================================================================

CODE CONDITION

------ -----------

C1 MANUAL ENROLL CONDITION

FALL OUT RELATIONSHIP: C1

> The *Manual Enroll* condition is always the fall out relationship for a manual enroll monitor.

=============================================================================

NUMBER CONDITION

-------- -----------

1 MANUAL ENROLL CONDITION

CONDITION FOR DATE OF EVENT: 1

> This field must be completed or you will receive an \*ERROR\* message. Enter 1 for *Manual Enroll* condition.

=============================================================================

TIME FRAME: Annually// \<RET\>

> Let's keep our time frames the same as the original auto enrolled monitor. We can compare our total number of records reviewed with the total provided us through the auto enrolled monitor QA-1.

Exercise 3 - Building a Manual Enroll Monitor

THRESHOLD: 3

> We can enter a threshold because we will be entering sample size information routinely so thresholds can be calculated.

PRE-THRESHOLD ALERT LEVEL: 2

> For this first time frame, we are just interested in obtaining a base line. But for the next one, we might want to know in advance so we can prevent the threshold from being crossed by taking some action. In that case, we would want to be warned in advance. We can edit the Pre-Threshold field at the time the next time frame begins or you can enter it at this time so it will be ready for the next go round.

ALLOW 'DUPLICATE' FALL OUTS: YES// \<RET\>

Select OTHER DATA TO CAPTURE: WARD LOCATION// ?

CHOOSE FROM:

AGE

SOCIAL SECURITY NUMBER

MOVEMENT DATE/TIME

WARD LOCATION

.....

Select OTHER DATA TO CAPTURE: WARD LOCATION// FACILITY TREATING SPECIALTY

PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: ATTENDING PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: PRIMARY CARE PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: \<RET\>

PRINT DAILY FALL OUT LIST: YES// NO

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// YESExercise 3 - Building a Manual Enroll Monitor

BULLETIN AT END OF TIME FRAME: YES// \<RET\>

BULLETIN WHEN ALERT LEVEL MET: NO// YES

BULLETIN MAIL GROUP: QA GROUP// \<RET\>

START DATE: NOV 6,1991// T

END DATE: \<RET\>

ON/OFF SWITCH: OFF// ON

MONITOR STATUS: UNDER CONSTRUCTION// FINISHED

With little effort, we have copied a monitor and changed only those fields that needed changing.

## Exercise 4 - Entering Data on Manually Enrolled Monitors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that we have two related monitors, one that provides us with the records for review and the other that lets us enter for tracking purposes the records that fail that review, let's enter some records into the manual monitor using the Fall Out Edit option from the Monitoring System User Menu.

Select User Menu Option: Fall Out Edit

Select MONITOR: QA-2 Gyne exam compliance FINISHED

Select PATIENT: CMSPATIENT,ONE

> If a patient has had other fall outs, they will be listed as in this example. If you use a patient that fell out for QA-1, then that fall out will appear with the name.

06-07-39 123456789 NSC VETERAN

\*\*\* FALL OUTS \*\*\*

XX-1 05-10-91

CAT-1 07-18-91

QA-1 10-20-91

EVENT DATE: TODAY

Searching FALL OUT file for this patient/monitor...

No fall outs found for this patient/monitor.

Are you adding:

CMSPATIENT,ONE 666-45-6789 OCT 29,1991

Gyne exam compliance QA-2 (m)

as a new Fall Out record? YES

For every manually enrolled record, there is an automatic creation date given to the record. The first three fields, Patient, Monitor, and Event Date are automatically filled. The defaults for these fields are based on the event date you entered above. The defaults will come from the admission date closest to the event date.

Exercise 4 - Entering Data on Manually Enrolled Monitors

PATIENT: CMSPATIENT,ONE// \<RET\>

MONITOR: QA-2// \<RET\>

EVENT DATE: OCT 29,1991// \<RET\>

SOCIAL SECURITY NUMBER: 666456789// \<RET\>

AGE: (1-130): 52// \<RET\>

MOVEMENT DATE/TIME: OCT 20, 1991@14:20// \<RET\>

WARD LOCATION: 3W// \<RET\>

FACILITY TREATING SPECIALTY:\<RET\> MEDICINE// \<RET\>

ATTENDING PHYSICIAN: CMSPROVIDER,ONE// \<RET\>

PRIMARY CARE PHYSICIAN: CMSPROVIDER,TWO// \<RET\>

Select PATIENT: \<RET\>

After entering a patient (or more if you wish), we should also update the sample size for this monitor. This only needs to be done for manual monitors. The auto enroll monitors can automatically track the sample size.

The sample size can be updated on a routine basis or it can be entered at the end of the time frame. If you want to be warned when the threshold is met, you should update it frequently.

Set a routine time (daily, every Friday, the last day of every month, etc.) to update the sample size for all your manually enrolled monitors where you want to track the percent fall out.

Select User Menu Option: SAmple Size Edit

Select MONITOR: QA-2 Gyne exam compliance FINISHED

Date for SAMPLE SIZE data: TODAY// \<RET\>

SAMPLE SIZE data was last edited: \*\*\* NEVER \*\*\*

Current FALL OUTS: 0

Current SAMPLE SIZE: 0

> Note that the number of fall outs is 0. Our entry today for CMSpatient,One will not appear until tomorrow when auto enroll picks up the number of entries for the MONITOR HISTORY file (#743.2).

Add/Subtract SAMPLE SIZE (-1000000 -\> 1000000): 10

New SAMPLE SIZE: 10

Date for SAMPLE SIZE data: TExercise 4 - Entering Data on Manually Enrolled Monitors

SAMPLE SIZE data was last edited: OCT 29,1991

Current FALL OUTS: 0

Current SAMPLE SIZE: 10

Add/Subtract SAMPLE SIZE (-1000000 -\> 1000000): \<RET\>

Date for SAMPLE SIZE data: \<RET\>

While you are updating your sample sizes, check to make sure the number of fall outs is accurate. There should be an automatic nightly run that picks up all new manually entered fall outs from the previous day. If this fails, your numbers could be inaccurate. Remember, if you are looking at data for today, those records you entered today will not appear until tomorrow.

If the numbers appear to be or are inaccurate, you will want to check the Auto/Manual Enroll Monitors Run to make sure the enrollment was done. We will learn how to fix this problem, but you should also have IRM check to see why the enrollment did not run.

Let's say you returned the next day and found the number of fall outs had not increased.

Select Outputs Menu Option: AUto/Manual Enroll Monitors Run

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: User Selectable

Beginning Date: 10/29/91

Ending Date: OCT 29,1991// \<RET\>

DEVICE: HOME// \<RET\>

> AUTO/MANUAL ENROLL MONITORS RUN OCT 30,1991

> OCT 29 1991 PAGE: 1

> AUTO ENROLL RUN DATE

> MONITOR CODE (a/m=AUTO/MANUAL) MONITOR TITLE DATE RUN

> --------------------------------------------------------------------------------

> OCT 29,1991 \*\*\* AUTO ENROLL DID NOT RUN FOR THIS DATE \*\*\*

To correct this problem, we can run a manual enroll found within the Manager Menu.

Select Monitoring System Manager Menu Option: MAnually Run Auto Enroll

Want to run auto enroll for specific monitors? NO// \<RET\>Exercise 4 - Entering Data on Manually Enrolled Monitors

Want to run auto enroll for specific services? NO// \<RET\>

Enter the date range you want auto enroll to scan

Monthly, Quarterly, Semi-Annually, Yearly, Fiscal Yearly, User Selectable

Select date range: USER SELECTABLE

Enter beginning and ending dates for the desired time period:

Beginning Date: 10/29/91 (OCT 28, 1991)

Ending Date: OCT 29,1991// \<RET\>

Range selected: OCT 29,1991

Queue auto enroll to run at: NOW The date/time you pick may be limited by the site

parameters.

Queueing auto enroll, please wait.

Want a report of the dates when auto enroll will run? YES// \<RET\>

DEVICE: HOME// \<RET\>

> MANUALLY QUEUED AUTO ENROLL RUN DATES OCT 30,1991

> OCT 29,1991 PAGE: 1

> START DATE END DATE QUEUED TO RUN TASK NUMBER

> --------------------------------------------------------------------------------

> OCT 29,1991 OCT 29,1991 OCT 30,1991@07:25:28 2226

You can now go back into the Sample Size Edit and check the fall out number. You can see that the number of fall outs is now 1.

Select User Menu Option: SAmple Size Edit

Select MONITOR: QA-2 Gyne exam compliance FINISHED

Date for SAMPLE SIZE data: TODAY// \<RET\>

SAMPLE SIZE data was last edited: OCT 29,1991

Current FALL OUTS: 1

Current SAMPLE SIZE: 10

Add/Subtract SAMPLE SIZE (-1000000 -\> 1000000):

Date for SAMPLE SIZE data: \<RET\>

Select MONITOR: \<RET\>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Alert Level</th>
<th>The level at which a bulletin is sent announcing that this level (pre-threshold) has been met. This is only meaningful for non-percentile thresholds. See Bulletin when Min Sample/Alert Level Met.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Allow Duplicate Fall Outs</td>
<td>Answering YES to this question allows an event to fall out multiple times for the same patient within a given time frame. Answering NO will allow the event to fall out only once per patient per time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Auto Enroll Monitor</td>
<td>This field determines whether or not this is an auto enroll monitor. You should answer YES to this field only if this monitor can be auto enrolled. Your answer will determine which conditions you will be allowed to select.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Auto Run Auto Enroll</td>
<td>This refers to the nightly automatic runs that scan VistA for patients who meet the criteria of the monitors which are set up in the QA MONITOR file (#743).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin at End of Time Frame</td>
<td>Enter YES if a bulletin should be sent at the end of each time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin Mail Group</td>
<td>This field contains the name of the mail group that the threshold, minimum sample, and end of time frame bulletins will be sent to.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin when Min Sample/Alert Level Met</td>
<td>Enter YES if a bulletin should be sent when the minimum sample is met or when the alert level is met for non-percentile thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin when Threshold Met</td>
<td>Enter YES if a bulletin should be sent when the threshold is met the first time within the time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Clinical Indicator</td>
<td>This word processing field defines the criteria necessary to meet the standard of care.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Code</td>
<td>This can either be free text or a predetermined list (of initial identifying letters or numbers) as defined by the site so that monitors can be grouped and easily retrieved by the service, section, etc.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Condition</td>
<td>A condition applies a True/False test on selected data elements in a patient's record. If the result of the test is true, that patient's record is captured for further processing.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Condition for Date of Event</td>
<td>Enter the condition number that should be used to capture the event date.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contributes to Sample</td>
<td>This field determines whether or not this condition contributes to the sample size (denominator). This affects how information is collected to determine the size of the sample (denominator).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>End Date</td>
<td>This field determines when the monitor should stop capturing data or when manual entry of data for this monitor is no longer allowed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Fall Out</td>
<td>A fall out is a patient who has been found to meet the criteria of a monitor. When a patient falls out a record is created in the FALL OUT file (#743.1) for that patient.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Fall Out Relationship</td>
<td>This field specifically states the relationship between the conditions entered by the user. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Group</td>
<td>A group is a list of similar items. An example would be a group of wards that are all psychiatry wards. Groups may have as many or as few group members as desired.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Hi/Lo Percent</td>
<td>If the user chooses "Hi", the threshold will be met when the percentage is calculated to be &gt;= to the threshold. If the user chooses "Lo", the threshold will be met when the percentage is calculated to be &lt;= the threshold. Hi/Lo is only meaningful for percent thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Manually Run Auto Enroll</td>
<td>Used to manually queue the auto enroll batch job. This option is used to run the auto enroll if one or more days in the past was missed due to down time.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Minimum Sample</td>
<td>This field defines the minimum sample size (denominator) that must be reached before threshold checking occurs. Minimum sample is meaningful only for percent thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Monitor</td>
<td>A monitor is made up of a set of conditions (criteria) and the relationships among those conditions. Monitors scan VistA on a nightly basis for patients who meet the monitor’s criteria.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Monitor Status</td>
<td><p>Answer FINISHED to this field only when you are sure you are completely finished entering/editing/</p>
<p>building this monitor. Once you answer FINISHED, you will no longer be able to edit selected monitor fields.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>On/Off Switch</td>
<td>This field controls whether or not a monitor is active. For an auto enroll monitor to capture data, this switch must be turned on. For a manual entry monitor to be selectable, the switch must be turned on. When you wish to stop using a monitor, this switch should be turned off.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Data to Capture</td>
<td>When a patient meets the conditions of the monitor and falls out, the other data to capture entries define which data elements in the patient's record should be collected.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td>Parameters further narrow down the definition of a condition. The format of a parameter is determined by the condition.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Print Daily Fall Out List</td>
<td>This field determines whether or not a generic list of all fall outs, sorted by monitor, is printed daily.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Print Daily Worksheets</td>
<td>This field determines whether worksheets are printed daily for all fall outs for this monitor. For this to work, the worksheet must first be created by a programmer and linked to the monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>QM</td>
<td>Quality Management</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>QM Coordinator</td>
<td>An individual tasked with the oversight of QM activities in the medical center.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Rationale</td>
<td>This field defines the rationale for the use of this monitor. You may select all that apply. (high volume, high risk, problem prone, other)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sample Relationship</td>
<td>Enter the relationships among the conditions. This field specifically states the relationship between the conditions that contribute to the sample size. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sample Size</td>
<td>The total number of patient records scanned by a monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Service</td>
<td>This field will allow the manager to track what monitors are currently being used by each service. The service entered has nothing to do with the conditions chosen or what data is auto enrolled.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Standard of Care</td>
<td>This word processing field defines the standard of care to be monitored.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Start Date</td>
<td>This field determines when the monitor should start to capture data or when manual entry of data for this monitor may begin.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Threshold</td>
<td>Threshold defines the number or percentage of fall outs after which some specific action will occur.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Time Frame</td>
<td>Time frame is the period of time over which the program begins capturing data and then sums up the data to start all over again with the beginning of the next similar time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Title</td>
<td>This is a short free text name determined by the user for this monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>

# Appendix A – Additional Monitor Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The examples in this section are designed to give you more ideas for setting up monitors at your site. They illustrate a few more complex monitors than shown in previous examples.

## Lithium Blood Level Lab Test Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose there is a need to identify patients (inpatient and outpatient) who have abnormal lithium blood levels. We want to see all the fall outs, but we also want to track total fall outs to total tests done on a monthly basis. The sample size will be all lithium tests. To limit the scope to inpatients, use the *On Ward* condition. To change that monitor to outpatients, use the not (') modifier in front of the *On Ward* condition when defining the Fall Out Relationship. You will see the not (') modifier used in the following Lithium monitor.

This example shows how to set up a monitor using the same condition twice - once with parameters to define fall out, and again with parameters to define Sample Size. When the same condition is selected twice for one monitor, you must remember in what order they were entered so that it will be possible to answer the Fall Out Relationship and Sample Size Relationship questions.

Certain types of lab tests (Chem, Hem, Tox, Ria, Ser) are accessible by the Clinical Monitoring System the day after the results are recorded in the VistA Lab Package. Accessibility of this data is dependent upon the fields being "numeric" and not "free text" or a "set of codes". (See the *Lab* condition in Appendix B for greater detail.)

A monitor can be built to capture all patients whose lithium test results are not within a normal therapeutic range. We'll use 0.5 - 2 as a normal therapeutic range. As with most monitors, it will be run nightly and will find patients whose test results went into VistA the day before.

Select Build Monitor Menu Option: ENTER/Edit a Monitor

Select MONITOR: LITH-1

ARE YOU ADDING 'LITH-1' AS A NEW QA MONITOR (THE 16TH)? Y (YES)

QA MONITOR TITLE: Abnormal Lithium Blood Level

CODE: LITH-1// \<RET\>

TITLE: Abnormal Lithium Blood Level Replace \<RET\>

SERVICE: PSY

1 PSYCHIATRY

2 PSYCHOLOGY 116B

CHOOSE 1-2: 1

STANDARD OF CARE:

1\>Patients will be maintained at a therapeutic level of lithium.2\>\<RET\>

EDIT Option:\<RET\>Lithium Blood Level Lab Test Monitor

CLINICAL INDICATOR:

1\>Patients with lithium blood level \<.05 or \> 2...2\>\<RET\>

EDIT Option: \<RET\>

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES

Select CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC

CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC// \<RET\>

LAB TEST: ?

Enter the name of an individual lab test whose result you want to monitor.

ANSWER WITH LABORATORY TEST NUMBER, OR NAME, OR LOCATION (DATA NAME)

DO YOU WANT THE ENTIRE LABORATORY TEST LIST? Y (YES)

CHOOSE FROM:

1 WBC

2 RBC

3 HGB

4 HCT

5 MCV

6 MCH

7 MCHC

11 NEUTROPHIL SEGS

12 BANDS

13 LYMPHS

14 MONOCYTES

15 EOSINOPHILS

16 BASOPHIL

17 METAMYELOCYTES

18 MYELOCYTES

19 PROMYELOCYTES

22 PLT SUFFICIENCY

25 ANISOCYTOSIS

26 POIKILOCYTOSIS

27 MICROCYTOSIS

28 MACROCYTOSIS

'^' TO STOP: ^

LAB TEST: LITHIUM

STARTING VALUE LITHIUM: 0.5 Enter the normal values.

ENDING VALUE LITHIUM: 2.0

CONTRIBUTES TO SAMPLE: NOLithium Blood Level Lab Test Monitor

Select CONDITION: "LAB"-CHEM,HEM,TOX,RIA,SER,ETC

> We need to enter the *Lab* condition again and specify sample size parameters that include ALL lithium tests. To enter the same condition twice, type in a sufficient number of characters to make it recognizable from other conditions and enclose it by double quotes as shown.

CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC// \<RET\>

LAB TEST: LITHIUM

STARTING VALUE LITHIUM: 0

ENDING VALUE LITHIUM: 999

> To catch all the tests done, we need to enter extreme low and high values.

CONTRIBUTES TO SAMPLE: YES

Select CONDITION: \<RET\>

> This is where it becomes necessary to remember the order in which you entered the two identical conditions.

=============================================================================

CODE CONDITION

------ -----------

C1 LAB-CHEM,HEM,TOX,RIA,SER,ETC

C2 LAB-CHEM,HEM,TOX,RIA,SER,ETC

FALL OUT RELATIONSHIP: 'C1&C2

> The first *Lab* condition (C1) contains the normal therapeutic range. We are interested in obtaining a list of patients outside this range. So we need the C2 condition that grabs all patients with a Lithium test and we eliminate those within the normal range by putting a (' ) modifier in front of it. This will produce a list of patients whose lab values do not fall within that range.

=============================================================================

CODE CONDITION

------ -----------

C2 LAB-CHEM,HEM,TOX,RIA,SER,ETC

SAMPLE RELATIONSHIP: C2Lithium Blood Level Lab Test Monitor

=============================================================================

NUMBER CONDITION

-------- -----------

1 LAB-CHEM,HEM,TOX,RIA,SER,ETC

2 LAB-CHEM,HEM,TOX,RIA,SER,ETC

CONDITION FOR DATE OF EVENT: 2

=============================================================================

TIME FRAME: Monthly

THRESHOLD: \<RET\>

PRE-THRESHOLD ALERT LEVEL: \<RET\>

ALLOW 'DUPLICATE' FALL OUTS: Y

> In this case each patient will be counted as often as the test is done during the time frame. You may choose to enter NO and have them only counted once during the time frame. It all depends on how you want to monitor Lithium use.

Select OTHER DATA TO CAPTURE: ??

When a patient meets the conditions of the monitor and falls out the

other data to capture entries define which data elements in the

patient's record should be collected.

CHOOSE FROM:

> At this time, the *Lab* condition does not allow additional data capture.

Select OTHER DATA TO CAPTURE: \<RET\>

PRINT DAILY FALL OUT LIST: NO// YES

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// YES

BULLETIN AT END OF TIME FRAME: NO// YES

BULLETIN WHEN ALERT LEVEL MET: NO// YES

BULLETIN MAIL GROUP: CHQAM

START DATE: T (JUL 22, 1992)

END DATE: T+365 (JUL 22, 1993)

ON/OFF SWITCH: OFF// ON

Checking monitor...

> **WARNING:** THRESHOLD not specified

No errors found.

MONITOR STATUS: UNDER CONSTRUCTION// FINISHED

## Transfers to ICU within 24 Hours of Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example shows how to build a monitor which will use fall out from another monitor. Capturing patients who are admitted and then transferred to ICU within 24 hours is a two-step process. First, a monitor must run each night to capture patients who were admitted. Then, a second monitor must run to find which of the Admission fall out patients were transferred to ICU within 24 hours. Both monitors will run every night. The Transfer Monitor cannot have fall outs until one night after fall outs are captured by the Admissions Monitor.

The Admissions Monitor will use the *MAS Movement Type* condition. It is not necessary to define an *MAS Movement Type* group for the Admissions Monitor because the MAS Movement Type condition asks for a transaction type. If the Admission transaction type is selected, there is no need to further restrict the type of admission. The ICU Transfer Monitor will require one group - ICU wards and two conditions - *Ward Transfer* and *Fall Out*. Fall Out will provide the Sample Size in the ICU Transfer Monitor.

The Admissions Monitor can be set up first.

Select Build Monitor Menu Option: ENTER/Edit a Monitor

Select MONITOR: ADM-ALL

ARE YOU ADDING 'ADM-ALL' AS A NEW QA MONITOR (THE 17TH)? Y (YES)

QA MONITOR TITLE: ALL ADMISSIONS

CODE: ADM-ALL// \<RET\>

TITLE: ALL ADMISSIONS// \<RET\>

SERVICE: DIRECTOR'S OFFICE 00

STANDARD OF CARE:

1\>\<RET\>

CLINICAL INDICATOR:

1\>\<RET\>

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES

Select CONDITION: MAS MOVEMENT TYPE

CONDITION: MAS MOVEMENT TYPE// \<RET\>

MAS MOVEMENT TRANSACTION TYPE: ?

ANSWER WITH MAS MOVEMENT TRANSACTION TYPE NUMBER, OR NAME

CHOOSE FROM:

1 ADMISSION

2 TRANSFER

3 DISCHARGE

4 CHECK-IN LODGER

5 CHECK-OUT LODGER

6 SPECIALTY TRANSFER

Enter the MAS transaction type of interest.

MAS MOVEMENT TRANSACTION TYPE: 1 ADMISSION

ADMISSION TYPE GROUP: \<RET\>

CONTRIBUTES TO SAMPLE: NO

Select CONDITION: \<RET\>Transfers to ICU within 24 Hours of Admission

=============================================================================

CODE CONDITION

------ -----------

C1 MAS MOVEMENT TYPE

FALL OUT RELATIONSHIP: C1

=============================================================================

NUMBER CONDITION

-------- -----------

1 MAS MOVEMENT TYPE

CONDITION FOR DATE OF EVENT: 1

=============================================================================

TIME FRAME: Monthly

THRESHOLD: \<RET\>

PRE-THRESHOLD ALERT LEVEL: \<RET\>

ALLOW 'DUPLICATE' FALL OUTS: YES

Select OTHER DATA TO CAPTURE: \<RET\>

PRINT DAILY FALL OUT LIST: NO// \<RET\>

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// \<RET\>

BULLETIN AT END OF TIME FRAME: NO// YES

BULLETIN WHEN ALERT LEVEL MET: NO// \<RET\>

BULLETIN MAIL GROUP: CHQAM

START DATE: T (JUL 22, 1992)

END DATE: \<RET\>

ON/OFF SWITCH: OFF// ON

Checking monitor...

> **WARNING:** SAMPLE RELATIONSHIP not specified

> **WARNING:** THRESHOLD not specified

No errors found.

MONITOR STATUS: UNDER CONSTRUCTION// FINISHED

Select MONITOR:

Next, the group of ICU wards must be defined for the ICU transfer monitor.

Select Monitoring System Manager Menu Option: GROUP Edit

Select GROUP: ICU WARDS WARD LOCATION

NAME: ICU WARDS// \<RET\>

PARENT FILE: WARD LOCATION// (No Editing)

Transfers to ICU within 24 Hours of Admission

Select GROUP MEMBER: 9EI// ?

You may enter \`\[GROUP MEMBER' to select all entries that CONTAIN

the text \`GROUP MEMBER'. Enter \`\[\*' to select ALL entries.

You may use a prefix of minus (-) to delete a range of group

members, for example \`-\[GROUP MEMBER' or \`-\[\*'.

> **WARNING:** Use of the contains operator (\[) is very computer intensive!

ANSWER WITH GROUP MEMBER

CHOOSE FROM:

10WC

13EI

15WR

9EI

> These wards have been defined as ICU wards in a group edit done previously.

YOU MAY ENTER A NEW GROUP MEMBER, IF YOU WISH

Answer must be 1-245 characters in length.

ANSWER WITH WARD LOCATION NUMBER, OR SYNONYM, OR SERVICE, OR NSERV

DO YOU WANT THE ENTIRE 64-ENTRY WARD LOCATION LIST? N (NO)

Select GROUP MEMBER: \<RET\>

Select Build Monitor Menu Option: ENTER/Edit a Monitor

Select MONITOR: ICU-XFER

ARE YOU ADDING 'ICU-XFER' AS A NEW QA MONITOR (THE 18TH)? Y (YES)

QA MONITOR TITLE: ICU XFER 24 HRS AFTER ADM

CODE: ICU-XFER// \<RET\>

TITLE: ICU XFER 24 HRS AFTER ADM Replace \<RET\>

SERVICE: DIRECTOR'S OFFICE 00

STANDARD OF CARE:

1\>Insure that patients who are admitted and have conditions...

2\>\<RET\>

EDIT Option: \<RET\>

CLINICAL INDICATOR:

1\>Using fall outs from the Admission monitor, identify patients

2\>who were transferred to ICU within 24 hours of admission.

3\>\<RET\>

EDIT Option: \<RET\>

Select RATIONALE: ?

ANSWER WITH RATIONALE

YOU MAY ENTER A NEW RATIONALE, IF YOU WISH

Enter the rationale for this monitor from the list displayed.

ANSWER WITH RATIONALE NAME

CHOOSE FROM:

High Risk

High Volume

Other

Problem Prone

Transfers to ICU within 24 Hours of Admission

Select RATIONALE: H

1 High Risk

2 High Volume

CHOOSE 1-2: 1

Select RATIONALE: \<RET\>

AUTO ENROLL MONITOR: YES

Select CONDITION: WARD TRANSFER

CONDITION: WARD TRANSFER// \<RET\>

WARD GROUP: ICU WARDS WARD LOCATION

> Here we use the group that defines ICU Wards.

CONTRIBUTES TO SAMPLE: ?

Enter Y(es) if this condition contributes to the sample size

(denominator).

CHOOSE FROM:

1 YES

0 NO

CONTRIBUTES TO SAMPLE: 0 NO

Select CONDITION: FALL OUT

> The *Fall Out* condition lets you select another monitor's fall outs for this monitor to look at.

CONDITION: FALL OUT// \<RET\>

FALL OUT MONITOR: ADM-ALL ALL ADMISSIONS FINISHED

LOOK BACK TIME: : (1-365): 1

> Since we want to capture all transfers to ICU within 24 hours of admission, look back time is one day.

ENTER THE TYPE OF DATE: (0/1): ?

0 AUTO ENROLL DATE

1 FALL OUT DATE

Enter the date you wish to be

associated with this condition.

Enter a 'RETURN' for the AUTO ENROLL DATE.

ENTER THE TYPE OF DATE: (0/1): \<RET\> AUTO ENROLL DATE

CONTRIBUTES TO SAMPLE: YES

Select CONDITION: \<RET\>

=============================================================================

CODE CONDITION

------ -----------

C1 WARD TRANSFER

C2 FALL OUT

Transfers to ICU within 24 Hours of Admission

FALL OUT RELATIONSHIP: C1&C2

=============================================================================

CODE CONDITION

------ -----------

C2 FALL OUT

SAMPLE RELATIONSHIP: C2

=============================================================================

NUMBER CONDITION

-------- -----------

1 WARD TRANSFER

2 FALL OUT

CONDITION FOR DATE OF EVENT: 1

=============================================================================

TIME FRAME: Monthly

THRESHOLD: 10

PRE-THRESHOLD ALERT LEVEL: 5

ALLOW 'DUPLICATE' FALL OUTS: YES

Select OTHER DATA TO CAPTURE: DIAGNOSIS \[SHORT\] PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: FACILITY TREATING SPECIALTY PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: PRIMARY CARE PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: ATTENDING PHYSICIAN PATIENT MOVEMENT

Select OTHER DATA TO CAPTURE: \<RET\>

PRINT DAILY FALL OUT LIST: NO// YES

PRINT DAILY WORKSHEETS: NO// \<RET\>

BULLETIN WHEN THRESHOLD MET: NO// YES

BULLETIN AT END OF TIME FRAME: NO// YES

BULLETIN WHEN ALERT LEVEL MET: NO// YES

BULLETIN MAIL GROUP: CHQAM

START DATE: T (JUL 22, 1992)

END DATE: \<RET\>

ON/OFF SWITCH: OFF// ON

Checking monitor...

No errors found.

MONITOR STATUS: UNDER CONSTRUCTION// FINISHED

Select MONITOR:

## JCAHO Indicators of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following suggested monitors are based on the JCAHO anesthesia, trauma, and cardiovascular indicators.

First, set up the following two monitors because some of the indicators use their fall out.

DEATH

Condition 1 DEATH

Fall Out Relationship C1

Condition for Date of Event 1 (date of death)

DEATH WITHAUTOPSY DISCHARGE

Condition 1 MAS MOVEMENT TYPE

MAS Movement Transaction Type: Discharge

Discharge Type Group: Use appropriate discharge type group

Fall Out Relationship C1

Condition for Date of Event 1 (date of death)

Previously built ICD groups for these monitors were exported with the software. Look for them labeled as AN-1, AN-2, etc. listed within the Group Edit option. If they are not there, ask IRM to run the routine that will lay them in. (See the Installation Guide.)

Any indicators not listed here either cannot be obtained because the data is not available through VistA or this version of the software does not access the package that has the data. Look for more indicators to be added in future versions.

Anesthesia Indicators were taken from <u>Anesthesia and Obstetrical Indicators Beta Phase Training Manual</u>, Joint Commission on Accreditation of Healthcare Organizations, 1990.

Trauma and Cardiovascular Indicators were taken from <u>Trauma, Oncology and Cardiovascular Indicators, Beta Phase Training Manual and Software User's Guide</u>, Joint Commission on Accreditation of Healthcare Organizations.

## JCAHO Anesthesia Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>AN-1 =&gt; 5</th>
<th><p>AN-1 Perioperative CNS Complication</p>
<p>AN-2 Perioperative Peripheral Neurologic Deficit</p>
<p>AN-3 Perioperative Acute Myocardial Infarction</p>
<p>AN-4 Perioperative Unplanned Cardiac Arrest</p>
<p>AN-5 Perioperative Unplanned Respiratory Arrest</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Select AN-1 =&gt; 5 DIAG GROUP depending on the monitor you are building.</p>
<p>ICD Procedure group: ANESTHESIA INDICATOR PROC LIST</p></td>
</tr>
<tr class="even">
<td>Fall Out Relationship</td>
<td>C1</td>
</tr>
<tr class="odd">
<td>Condition for Date of Event</td>
<td>1 (Procedure date)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>AN-6</strong></td>
<td>AN-6 Perioperative Death</td>
</tr>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Leave blank</p>
<p>ICD Procedure group: ANESTHESIA INDICATOR PROC LIST</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>FALL OUT</p>
<p>Fall Out Monitor: DEATH</p>
<p>Look Back Time: Number of days between discharge and PTF data entry at your site</p>
<p>Type of Date: Fall Out Date (Date of death)</p></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>C1&amp;C2</td>
</tr>
<tr class="even">
<td>Condition for Date of Event</td>
<td>2 (Date of death)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

## JCAHO Trauma Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>TR-8a,b</th>
<th>TR-8a,b Trauma patients undergoing laparotomy for wounds penetrating the abdominal wall, subcategorized by gunshot and/or stab wounds.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: TR-8A/B DIAG GROUP (GUNSHOT)/(KNIFE)</p>
<p>ICD Procedure group: Leave blank</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Leave blank</p>
<p>ICD Procedure group: TR-8 PROC GROUP</p></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>C1&amp;C2</td>
</tr>
<tr class="even">
<td>Sample Size Relationship</td>
<td>C1</td>
</tr>
<tr class="odd">
<td>Condition for Date of Event</td>
<td>2 (Date of procedure)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>TR-10</strong></td>
<td>TR-10 Adult trauma patients with femoral diaphyseal fractures treated by a non-fixation technique.</td>
</tr>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: TR-10 DIAG GROUP</p>
<p>ICD Procedure group: Leave blank</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Leave blank</p>
<p>ICD Procedure group: TR-10 PROC GROUP</p></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>C1&amp;'C2</td>
</tr>
<tr class="even">
<td>Sample Size Relationship</td>
<td>C1</td>
</tr>
<tr class="odd">
<td>Condition for Date of Event</td>
<td>1 (Admission date)</td>
</tr>
</tbody>
</table>

JCAHO Trauma Indicators

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>TR-11</th>
<th>TR-11 Intrahospital mortality of trauma patients with one or more of the following conditions who did not undergo a procedure for the condition: tension pneumothorax, hemoperitoneum, hemothoraces, ruptured aorta, pericardial tamponade, and epidural or subdural hemorrhage.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: TR-11 DIAG GROUP</p>
<p>ICD Procedure group: Leave blank</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Leave blank</p>
<p>ICD Procedure group: TR-11 PROC GROUP</p></td>
</tr>
<tr class="odd">
<td>Condition 3</td>
<td><p>FALL OUT</p>
<p>Fall Out Monitor: DEATH (See AN-6 for death monitor set-up.)</p>
<p>Look Back Time: Average number of days between discharge and PTF data entry at your site</p>
<p>Type of Date: Fall Out Date (Date of death)</p></td>
</tr>
<tr class="even">
<td>Fall Out Relationship</td>
<td>C3&amp;C1&amp;'C2</td>
</tr>
<tr class="odd">
<td>Sample Size Relationship</td>
<td>C3&amp;C1</td>
</tr>
<tr class="even">
<td>Condition for Date of Event</td>
<td>3 (Date of death)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

JCAHO Trauma Indicators

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>TR-12</th>
<th>TR-12 Trauma patients who expired within 48 hours of emergency department (ED) arrival for whom an autopsy was performed.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: TR-12 DIAG GROUP-BASIC TRAUMA</p>
<p>ICD Procedure group: Leave blank</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>FALL OUT</p>
<p>Fall Out Monitor: DEATH WITH AUTOPSY DISCHARGE</p>
<p>Look Back Time: Number of days between discharge and PTF data entry at your site</p>
<p>Type of Date: Fall Out Date (Date of death)</p></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>C1&amp;C2</td>
</tr>
<tr class="even">
<td>Condition for Date of Event</td>
<td>2 (Discharge/Death date)</td>
</tr>
</tbody>
</table>

## JCAHO Cardiovascular Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>CV-4</th>
<th>CV-4 Patients undergoing non-emergent percutaneous transluminal coronary angioplasty with subsequent occurrence of either an acute myocardial infarction or coronary artery bypass graft procedure within the same hospitalization.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Condition 1</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: Leave blank</p>
<p>ICD Procedure group: CV-4 PROC GROUP</p></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td><p>PTF DIAGNOSIS/OPERATION CODES</p>
<p>ICD Diagnosis group: CV-4 DIAG GROUP</p>
<p>ICD Procedure group: Leave blank</p></td>
</tr>
<tr class="odd">
<td>Fall Out Relationship</td>
<td>C1&amp;C2</td>
</tr>
<tr class="even">
<td>Sample Size Relationship</td>
<td>C1</td>
</tr>
<tr class="odd">
<td>Condition for Date of Event</td>
<td>1 (Date of procedure)</td>
</tr>
</tbody>
</table>

# Appendix B - Condition Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The condition listing on the following pages can be reproduced at your site through the Condition File Inquire option by entering ALL at the "CONDITION:" prompt. Familiarity with these conditions is necessary before attempting to build monitors.

Keep in mind the following general rules.

- Any question on the condition list that relates to a condition can be bypassed by entering \<RET\> at the prompt. The result of bypassing a question is that all possible criteria that it asks for will be considered valid. For example, if you select the *Appointment* condition and press \<RET\> at the "STATUS:" question, the appointments retrieved may have any status. The exception to this is that pressing \<RET\> at a "LOOK BACK DAYS:" prompt will cause the monitor to revert to its default behavior of looking only at what happened yesterday.
- Unless otherwise specified by entering a LOOK BACK DAYS, conditions are applied to transactions that occurred yesterday (T-1). If you enter a LOOK BACK DAYS, the monitor will apply the condition to T-1 as well as the additional number of days you enter. For example, if you enter 2 at the "LOOK BACK DAYS:" prompt, the monitor will look at T-1, T-2, and T-3.
- The "TYPE OF DATE:" question determines which date will be written to the EVENT DATE field of the fall out record.

As a reminder that defined groups may be needed for some conditions, we highlighted any notation to a group in the following listing of conditions. We also included file contents for those files that are exported with data and do not differ from site to site.

=============================================================================

CONDITION: AGE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who fall between an upper

and a lower age limit entered by the user.

This condition will request the following information:

LOWER AGE LIMIT

The lower limit (inclusive) on patient age

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

==================================================================

=============================================================================

CONDITION: APPOINTMENT AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all appointments on the day that

auto enroll is scanning. The user may screen the appointments by

entering a clinic group, the appointment status, the purpose of the

visit, and/or an appointment type group.

This condition will request the following information:

CLINIC GROUP

A group of entries from the HOSPITAL LOCATION file (#44).

STATUS

The status of the appointment, i.e., No-show, Cancelled, etc.

PURPOSE OF VISIT

The purpose of the patient visit, i.e., C&P, 10/10, Unscheduled,

etc.

APPOINTMENT TYPE GROUP

A group of entries from the APPOINTMENT TYPE file (#409.1).

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past

for an appointment.

DATA ELEMENTS:

AGE

APPOINTMENT DATE/TIME

APPOINTMENT STATUS

APPOINTMENT TYPE

APPT. CANCELLATION REASON

CLINIC

COVERED BY HEALTH INSURANCE?

DATE OF BIRTH

DATE OF DEATH

MARITAL STATUS

OCCUPATION

PURPOSE OF VISIT

RACE

RELIGIOUS PREFERENCE

SERVICE CONNECTED PERCENTAGE

SERVICE CONNECTED?

SEX

SOCIAL SECURITY NUMBER

SPINAL CORD INJURY

=============================================================================

Look back days

If you enter three (3) for the number of look back days, the program actually scans four (4) days. Example: If today = 5/28, the program scans 5/24, 25, 26, and 27.

Hospital Location file contents differ from site to site.

Status

NO-SHOW

CANCELLED BY CLINIC

NO-SHOW & AUTO RE-BOOK

CANCELLED BY CLINIC & AUTO RE-BOOK

INPATIENT APPOINTMENT

CANCELLED BY PATIENT

CANCELLED BY PATIENT & AUTO RE-BOOK

Purpose of Visit

C&P

10-10

SCHEDULED VISIT

UNSCHEDULED VISIT

Appointment Type file

COMPENSATION & PENSION

CLASS II DENTAL

ORGAN DONORS

EMPLOYEE

PRIMA FACIA

RESEARCH

COLLATERAL OF VET.

SHARING AGREEMENT

REGULAR

COMPUTER GENERATED

=============================================================================

CONDITION: DEATH AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all deaths.

This condition will not request any further information.

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

=============================================================================

=============================================================================

CONDITION: FALL OUT AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who previously fell out

for a specific monitor within a user selected number of days.

This condition will request the following information:

FALL OUT MONITOR

The monitor whose fall outs you wish to further monitor.

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past

for a fall out captured by a previous monitor.

TYPE OF DATE

The date that should be used as the event date for the fallout,

either the event date of the previous fall out or the auto enroll

date for the current fall out.

DATA ELEMENTS:

EVENT DATE (FALL OUT)

REC CREATION DATE (FALL OUT)

=============================================================================

Look back days

If you enter three (3) for the number of look back days, the program actually scans four (4) days. Example: If today = 5/28, the program scans 5/24, 525, 5/26, and 5/27.

When to use the *Fall Out* condition

CMS scans the data base once each day to pick up patients that meet specified conditions. Events (conditions) do not always happen on the same day for a patient. Perhaps a patient is seen in a clinic on one day (the first event) but we want to make sure his lab test (second event) is done within 5 days of being seen in clinic. We would build two monitors to obtain a list of fall out patients. The first monitor would scan for patients seen in a specific clinic. We will call the monitor Coumadin Clinic. This then becomes our *Fall Out* condition for our second monitor which will also scan for a selected lab test. The relationship between the conditions would be Fall Out (Coumadin Clinic) and not (&') Lab. This monitor would also use Look Back Days which would be entered as 4.

=============================================================================

CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who fall within a user

specified range of values for a user specified lab test.

This condition will request the following information:

LAB TEST

Any single Chem, Hem, Tox, Ria, or Ser type lab test.

STARTING VALUE

ENDING VALUE

The starting and ending (hi/lo) value range that you want to capture

for the selected lab test.

DATA ELEMENTS:

=============================================================================

> **NOTE:** This software will not ask Starting and Ending Values for 'free text' or 'set of codes' fields. If the *Lab* condition responds in the following manner

CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC// \<RET\>

LAB TEST: *LITHIUM*

STARTING VALUE LITHIUM:

ENDING VALUE LITHIUM:

then the field is numeric and you will be able to enter the values you want.

If the *Lab* condition responds in this manner

CONDITION: LAB-CHEM,HEM,TOX,RIA,SER,ETC// \<RET\>

LAB TEST: *LITHIUM*

"LAB TEST NAME":

then the field was set up at your site as either free text or a set of codes. If this monitor is an important part of your risk management activities, try negotiating with your Lab ADPAC to see if the field can be designated as numeric.

=============================================================================

CONDITION: LENGTH OF STAY IN SPECIALTY AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients who have been in the

same specialty group for a user selected number of days.

This condition will request the following information:

LENGTH OF STAY

The number of days a patient has stayed in a given treating

specialty. Enter 10 if you want to capture all patients with a

treating specialty LOS of ten days.

TREATING SPECIALTY GROUP

A group of entries from the FACILITY TREATING SPECIALTY file

(#45.7).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the Facility Treating Specialty file differ from site to site.

The number in LOS conditions

The patient will fall out when his stay equals the LOS entered in the condition. When or if the patient's LOS is greater than the LOS in the condition, the patient will not fall out.

=============================================================================

CONDITION: LENGTH OF STAY ON A WARD AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients who have been on a

given ward group for a user selected number of days.

This condition will request the following information:

LENGTH OF STAY

The number of days a patient has stayed on a given ward. Enter 10

if you want to capture all patients with a ward LOS of ten days.

WARD GROUP

A group of entries from the WARD LOCATION file (#42).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the Ward Location file differ from site to site.

The number in LOS conditions

The patient will fall out when his stay equals the LOS entered in the condition. When or if the patient's LOS is greater than the LOS in the condition, the patient will not fall out.

=============================================================================

CONDITION: LENGTH OF STAY SINCE ADMISSION AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients who have length of

stay since admission of X number of days.

This condition will request the following information:

LENGTH OF STAY

The number of days a patient has been an inpatient. Enter 10 if you

want to capture all patients with a LOS of ten days.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The number in LOS conditions

The patient will fall out when his stay equals the LOS entered in the condition. When or if the patient's LOS is greater than the LOS in the condition, the patient will not fall out.

=============================================================================

CONDITION: MANUAL ENROLL CONDITION AUTO ENROLL: NO

DESCRIPTION:

This is a generic manual enroll condition. It MUST be selected as

the condition for all monitors for which you plan to do manual data

entry.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

AGE

APPOINTMENT DATE/TIME

APPOINTMENT STATUS

APPOINTMENT TYPE

APPT. CANCELLATION REASON

ATTENDING PHYSICIAN

CLINIC

COVERED BY HEALTH INSURANCE?

DATE OF DEATH

DIAGNOSIS \[SHORT\]

DISPOSITION

EVENT DATE (FALL OUT)

FACILITY TREATING SPECIALTY

LOG IN DATE/TIME

LOG IN STATUS

LOG OUT DATE/TIME

MARITAL STATUS

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

OCCUPATION

PRIMARY CARE PHYSICIAN

PURPOSE OF VISIT

RACE

REASON FOR LATE DISPOSITION

REC CREATION DATE (FALL OUT)

RELIGIOUS PREFERENCE

ROOM-BED

SERVICE CONNECTED PERCENTAGE

SERVICE CONNECTED?

SEX

SOCIAL SECURITY NUMBER

SPINAL CORD INJURY

TRANSACTION TYPE

TYPE OF BENEFIT APPLIED FOR

TYPE OF CARE APPLIED FOR

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

=============================================================================

CONDITION: MAS MOVEMENT TYPE AUTO ENROLL: YES

DESCRIPTION:

This condition allows the user to track selected MAS movement types.

First the user must select the transaction type of movement he wishes

to track, Admission, Transfer, Discharge, Check-in Lodger, Check-out

Lodger, or Treating Specialty. The user is then prompted for a group

that consists of specific movement types that fall under the

transaction type selected above.

This condition will request the following information:

MAS MOVEMENT TRANSACTION TYPE

The desired patient movement transaction type, i.e., admission,

transfer, discharge, etc.

MOVEMENT TYPE GROUP

A specific subset of patient movements that fall within the

transaction type chosen above. If admission was chosen as the

transaction type, the movement type group might include direct,

transfer in, etc. A group of entries from the MAS MOVEMENT TYPE file

(#405.2).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

MAS Movement Transaction Type

> ADMISSION

> TRANSFER

> DISCHARGE

> CHECK-IN LODGER

> CHECK-OUT LODGER

> SPECIALTY TRANSFER

> NON-MOVEMENT

MAS Movement Type File

> AUTH ABSENCE 96 HOURS OR LESS

> AUTHORIZED ABSENCE

> UNAUTHORIZED ABSENCE

> INTERWARD TRANSFER

> CHECK-IN LODGER

> CHECK-IN LODGER (OTHER FACILITY)

> CHECK-OUT LODGER

> AMBULATORY CARE (OPT-AC)

> TRANSFER IN

> TRANSFER OUT

> NON-SERVICE CONNECTED (OPT-NSC)

> DEATH

> TO ASIH (VAH)

> FROM ASIH (VAH)

> DIRECT

> REGULAR

> IRREGULAR

> READMISSION TO NHCU/DOMICILIARY

> PROVIDER/SPECIALTY CHANGE

> OPT-SC

> FROM UNAUTHORIZED ABSENCE

> FROM AUTH. ABSENCE OF 96 HOURS OR LESS

> FROM AUTHORIZED ABSENCE

> FROM AUTHORIZED TO UNAUTHORIZED ABSENCE

> FROM UNAUTHORIZED TO AUTHORIZED ABSENCE

> NON-BED CARE

> NON-SERVICE CONNECTED (OPT-NSC)

> PRE-BED CARE (OPT-PBC)

> NON-VETERAN (OPT-NVE)

> TO NHCU FROM HOSP

> TO DOM FROM HOSP

> TO NHCU FROM DOM

> DISCHARGE TO CNH

> VA NHCU TO CNH

> WAITING LIST

> NON-VETERAN

> DEATH WITH AUTOPSY

> OPT-SC

> TO ASIH

> FROM ASIH

> WHILE ASIH

> TO ASIH (OTHER FACILITY)

> RESUME ASIH IN PARENT FACILITY

> CHANGE ASIH LOCATION (OTHER FACILITY)

> CONTINUED ASIH (OTHER FACILITY)

> DISCHARGE FROM NHCU/DOM WHILE ASIH

=============================================================================

CONDITION: MH SECLUSION/RESTRAINT AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients on a selected ward

group, with selected types and/or reasons for restraint. The maximum

number of hours allowed in restraint is also a parameter.

This condition will request the following information:

HOSPITAL LOCATION GROUP

A group of entries from the HOSPITAL LOCATION file (#44).

SECLUSION/RESTRAINT TYPE GROUP

A group of entries from the S/R CATEGORY file (#615.6).

REASON FOR S/R GROUP

A group of entries from the S/R REASONS file (#615.5).

MAXIMUM TIME IN S/R (HOURS)

The maximum number of hours a patient may be held in

seclusion/restraint before the patient will fall out for this

condition.

DATA ELEMENTS:

DATE TIME OF S/R ORDER

DATE/TIME S/R APPLIED

NAME OF NURSE PRESENT S/R

S/R ORDER TYPE

S/R ORDERED BY

S/R WARD

=============================================================================

The contents of the Hospital Location file differ from site to site.

S/R Category file

> LEATHER RESTRAINTS

> LOCKED SECLUSION

> SOFT RESTRAINTS

> UNLOCKED SECLUSION

S/R Reasons file

> HARM TO SELF

> HARM TO OTHERS

> DISRUPTING THERAPEUTIC MILIEU

=============================================================================

CONDITION: ON SERVICE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients on a user specified

service/section group. The service/section is determined from the

patient's current treating specialty.

This condition will request the following information:

SERVICE/SECTION GROUP

A group of entries from the SERVICE/SECTION file (#49).

COUNT SAMPLE SIZE BY

This field allows you to choose how the sample size will be

calculated. It can be counted by transfers, discharges, and the

number of patients in house at the end of the time frame.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the SERVICE/SECTION file differ from site to site.

=============================================================================

CONDITION: ON TREATING SPECIALTY AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients on a user specified

treating specialty group.

This condition will request the following information:

TREATING SPECIALTY GROUP

A group of entries from the FACILITY TREATING SPECIALTY file

(#45.7).

COUNT SAMPLE SIZE BY

This field allows you to choose how the sample size will be

calculated. It can be counted by transfers, discharges, and the

number of patients in house at the ending of the time frame.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the FACILITY TREATING SPECIALTY file differ from site to site.

=============================================================================

CONDITION: ON WARD AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients on a user specified

ward group.

This condition will request the following information:

WARD GROUP

A group of entries from the WARD LOCATION file (#42).

COUNT SAMPLE SIZE BY

This field allows you to choose how the sample size will be

calculated. It can be counted by admissions, transfers, discharges,

and the number of patients in house at the beginning or end of the

time frame.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the WARD LOCATION file differ from site to site.

Conditions: OS 101.1-199

============================================================================

CONDITION: OS-101.1 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 101.1,

'Readmission within 10 days.'

DATA ELEMENTS:

============================================================================

CONDITION: OS-102 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 102,

'Admission within 3 days of an unscheduled ambulatory care visit.'

DATA ELEMENTS:

============================================================================

CONDITION: OS-106.1 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 106.1,

'Unexpected transfer to a special care unit within 72 hours of

transfer from a special care unit.'

DATA ELEMENTS:

============================================================================

CONDITION: OS-107 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 107,

'Return to the O.R. in the same admission.'

DATA ELEMENTS:

============================================================================

CONDITION: OS-109 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 109, 'Death.'

DATA ELEMENTS:

============================================================================

CONDITION: OS-199 AUTO ENROLL: YES

DESCRIPTION:

This condition performs the auto enroll of Occurrence Screen 199,

'Readmission within 48 hours of D/C from extended care.'

DATA ELEMENTS:

============================================================================

=============================================================================

CONDITION: PATIENT GROUP AUTO ENROLL: YES

DESCRIPTION:

This condition is used to monitor a select group of patients.

This condition will request the following information:

PATIENT GROUP

A group of entries from the PATIENT file (#2).

DATA ELEMENTS:

=============================================================================

The contents of the PATIENT file differ from site to site.

=============================================================================

CONDITION: PREVIOUS DISCHARGE FROM WARD AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patient discharges within a user

selected 'look back time.' The discharges may be screened by wardgroup. The condition date is user selectable.

This condition will request the following information:

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past

for a discharge

WARD GROUP

A group of entries from the WARD LOCATION file (#42).

TYPE OF DATE

The date that should be used as the event date for the fallout,

either the date the fall out was auto enrolled or the discharge date.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the WARD LOCATION file differ from site to site.

Look back days

If you enter three (3) for the number of look back days, the program actually scans four (4) days. Example: If today = 5/28, the program scans 5/24, 525, 5/26, and 5/27.

=============================================================================

CONDITION: PREVIOUS DISCHARGE MVMENT TYPE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patient discharged within a user

selected 'look back time.' The discharges may be screened by MAS

movement type group. The condition date is user selectable.

This condition will request the following information:

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past

for a discharge.

MOVEMENT TYPE GROUP

A group of entries (discharge movements) from the MAS MOVEMENT TYPE

file (#405.2).

TYPE OF DATE

The date that should be used as the event date for the fall out,

either the date the fall out was auto enrolled or the discharge date.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

Look back days

If you enter three (3) for the number of look back days, the program actually scans four (4) days. Example: If today = 5/28, the program scans 5/24, 525, 5/26, and 5/27.

MAS Movement Type File

> AUTH ABSENCE 96 HOURS OR LESS

> AUTHORIZED ABSENCE

> UNAUTHORIZED ABSENCE

> INTERWARD TRANSFER

> CHECK-IN LODGER

> CHECK-IN LODGER (OTHER FACILITY)

> CHECK-OUT LODGER

> AMBULATORY CARE (OPT-AC)

> TRANSFER IN

> TRANSFER OUT

> NON-SERVICE CONNECTED (OPT-NSC)

> DEATH

> TO ASIH (VAH)

> FROM ASIH (VAH)

> DIRECT

> REGULAR

> IRREGULAR

> READMISSION TO NHCU/DOMICILIARY

> PROVIDER/SPECIALTY CHANGE

> OPT-SC

> FROM UNAUTHORIZED ABSENCE

> FROM AUTH. ABSENCE OF 96 HOURS OR LESS

> FROM AUTHORIZED ABSENCE

> FROM AUTHORIZED TO UNAUTHORIZED ABSENCE

> FROM UNAUTHORIZED TO AUTHORIZED ABSENCE

> NON-BED CARE

> NON-SERVICE CONNECTED (OPT-NSC)

> PRE-BED CARE (OPT-PBC)

> NON-VETERAN (OPT-NVE)

> TO NHCU FROM HOSP

> TO DOM FROM HOSP

> TO NHCU FROM DOM

> DISCHARGE TO CNH

> VA NHCU TO CNH

> WAITING LIST

> NON-VETERAN

> DEATH WITH AUTOPSY

> OPT-SC

> TO ASIH

> FROM ASIH

> WHILE ASIH

> TO ASIH (OTHER FACILITY)

> RESUME ASIH IN PARENT FACILITY

> CHANGE ASIH LOCATION (OTHER FACILITY)

> CONTINUED ASIH (OTHER FACILITY)

> DISCHARGE FROM NHCU/DOM WHILE ASIH

=============================================================================

CONDITION: PREVIOUS DISCHARGE TREAT SPEC AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patient discharges within a user

selected 'look back time.' The discharges may be screened by

treating specialty. The condition date is user selectable.

This condition will request the following information:

LOOK BACK DAYS

The number of days (in addition to yesterday) to look into the past

for a discharge.

TREATING SPECIALTY GROUP

A group of entries from the FACILITY TREATING SPECIALTY file

(#45.7).

TYPE OF DATE

The date that should be used as the event date for the fall out,

either the date the fall out was auto enrolled or the discharge date.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the FACILITY TREATING SPECIALTY file differ from site to site.

Look back days

If you enter three (3) for the number of look back days, the program actually scans four (4) days. Example: If today = 5/28, the program scans 5/24, 525, 5/26, and 5/27.

=============================================================================

CONDITION: PTF DIAGNOSES/OPERATION CODES AUTO ENROLL: YES

DESCRIPTION:

This condition will produce a list of closed out PTF records. An ICD

diagnosis group may be specified to screen out particular patients.

An ICD operation/procedure group may also be specified to screen out

particular patients. If both groups are entered the patient must

have both a diagnosis and an operation/procedure found in the groups

in order to fall out. If no groups are specified all closed out PTF

records with at least one diagnosis and one operation code will be

captured.

This condition will request the following information:

ICD DIAGNOSIS GROUP

A group of entries from the ICD DIAGNOSIS file (#80).

ICD PROCEDURE GROUP

A group of entries from the ICD OPERATION/PROCEDURE file (#80.1).

DATA ELEMENTS:

PTF ADMISSION DATE

PTF DISCHARGE DATE

PTF DISCHARGE SPECIALTY

PTF DRG

PTF DXLS

PTF ICD 10

PTF ICD 2

PTF ICD 3

PTF ICD 4

PTF ICD 5

PTF ICD 6

PTF ICD 7

PTF ICD 8

PTF ICD 9

PTF PROCEDURE 1

PTF PROCEDURE 2

PTF PROCEDURE 3

PTF PROCEDURE 4

PTF PROCEDURE 5

PTF TYPE OF DISPOSITION

PTF WARD AT DISCHARGE

=============================================================================

Contents of the ICD files are too large to list here.  
=============================================================================

CONDITION: READMISSION AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients readmitted to the

hospital within a user selected number of days.

This condition will request the following information:

DAYS BETWEEN DISCHARGE AND ADMISSION

This is the maximum number of days between a discharge and a

readmission. A fall out will occur if this number is greater than or

equal to the number of days between the discharge and the admission.

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

=============================================================================

CONDITION: REGISTRATION AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all registrations for the day that

auto enroll is running for. The user may screen the registrations by

entering the registration status, the type of benefit applied for,

the type of care applied for, and/or a disposition group.

This condition will request the following information:

STATUS

The status of a patient visit, i.e., 10/10, Unscheduled, etc.

TYPE OF BENEFIT APPLIED FOR

The type of benefit the patient is applying for, i.e., Hospital,

Outpatient, NHCU, etc.

TYPE OF CARE APPLIED FOR

The type of care the patient is applying for.

DISPOSITION GROUP

A group of entries from the DISPOSITION file (#37).

DATA ELEMENTS:

AGE

COVERED BY HEALTH INSURANCE?

DATE OF BIRTH

DATE OF DEATH

DISPOSITION

LOG IN DATE/TIME

LOG IN STATUS

LOG OUT DATE/TIME

MARITAL STATUS

OCCUPATION

RACE

REASON FOR LATE DISPOSITION

RELIGIOUS PREFERENCE

SERVICE CONNECTED PERCENTAGE

SERVICE CONNECTED?

SEX

SOCIAL SECURITY NUMBER

SPINAL CORD INJURY

TYPE OF BENEFIT APPLIED FOR

TYPE OF CARE APPLIED FOR

=============================================================================

Status

> 10-10 VISIT

> UNSCHEDULED

> APPLICATION WITHOUT EXAM

Type of Benefit Applied for

> HOSPITAL

> DOMICILIARY

> OUTPATIENT MEDICAL

> OUTPATIENT DENTAL

> NURSING HOME CARE

Type of Care Applied for

> DENTAL

> PLASTIC SURGERY

> STERILIZATION

> PREGNANCY

> ALL OTHER

Disposition File

ADMIT

CANCEL APPLICATION

CANCEL WITH EXAM

CANCEL WITHOUT EXAM

COMMUNITY RESOURCES

DEAD ON ARRIVAL

DOMICILIARY ADMISSION

DOMICILIARY WAITING LIST

FAILED TO COOPERATE/COMPLETED

FEE BASIS REFERAL, OTHER

HOSPITAL ADMISSION

HOSPITAL WAITING LIST

IN NEED OF DOMICILIARY

IN NEED OF NURSING HOME CARE

INELIGIBLE

INELIGIBLE-DISP COMMUNITY

INELIGIBLE-DISP OTHER

KEEP PREVIOUSLY SCHEDULED APPT

LOW PRIORITY-DISP COMMUNITY

LOW PRIORITY-DISP FEE BASIS

LOW PRIORITY-DISP OTHER

LOW PRIORITY-DISP OTHER VA

NO CARE OR TREATMENT REQUIRED

NURSING HOME ADMISSION

NURSING HOME WAITING LIST

PENDING DETERMINATION

PRE-BED CARE

REFERRED TO OTHER VA FACILITY

REFUSED TO PAY DEDUCTIBLE

RESOURCES NOT AVAILABLE

SCHEDULE FUTURE APPOINTMENT

SCHEDULED ADMISSION

TREATMENT MODALITY NOT AVAILABLE

TREATMENT PROVIDED NO RETURN

TRT MOD UNAVAIL-DISP COMMUNITY

TRT MOD UNAVAIL-DISP FEE BASIS

TRT MOD UNAVAIL-DISP OTHER

TRT MOD UNAVAIL-DISP OTHER VA

WAITING LIST

=============================================================================

CONDITION: RXS 2+ DRUGS IN THE SAME CLASS AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of patients who have two or more

active prescriptions for drugs in the same class. All new

prescriptions are scanned and the drug class is user selectable.

This condition will request the following information:

DRUG CLASS GROUP

A group of entries from the VA DRUG CLASS file (#50.605).

DATA ELEMENTS:

The VA Drug Class file is too large to list here.

=============================================================================

CONDITION: SEX AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of Male or Female patients.

This condition will request the following information:

SEX

The sex of the patients who should be captured.

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

=============================================================================

=============================================================================

CONDITION: SPECIALTY TRANSFER AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all specialty transfers on the day

that auto enroll is scanning. The user may choose a specific groupof specialties to monitor.

This condition will request the following information:

TREATING SPECIALTY GROUP

A group of entries from the FACILITY TREATING SPECIALTY file

(#45.7).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the FACILITY TREATING SPECIALTY file differ from site to site.

=============================================================================

CONDITION: SSN SAMPLE AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all patients whose SSN terminating

digit is in a range selected by the user.

This condition will request the following information:

LAST DIGITS OF SSN

This field allows the user to choose which patients should fall out

based on the last digit of their SSN. An entry of 1,3,5,7,9 will

only capture those patients whose SSN ends in an odd number.

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

=============================================================================

=============================================================================

CONDITION: WARD TRANSFER AUTO ENROLL: YES

DESCRIPTION:

This condition produces a list of all ward transfers on the day that

auto enroll is scanning. The user may choose a specific group ofwards to monitor. This condition looks for patients who were

transferred TO the ward(s) selected.

This condition will request the following information:

WARD GROUP

A group of entries from the WARD LOCATION file (#42).

DATA ELEMENTS:

ADMITTED FOR SC CONDITION?

ADMITTING REGULATION

ATTENDING PHYSICIAN

DIAGNOSIS \[SHORT\]

FACILITY TREATING SPECIALTY

MAS MOVEMENT TYPE

MOVEMENT DATE/TIME

PRIMARY CARE PHYSICIAN

ROOM-BED

TRANSACTION TYPE

TYPE OF MOVEMENT

WARD LOCATION

=============================================================================

The contents of the WARD LOCATION file differ from site to site.

# Appendix C - Build a Monitor Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

6\. Rationale(s):

\_\_\_ High Risk \_\_\_ Other

\_\_\_ High Volume \_\_\_ Problem Prone

Rationale Explanation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

Group Members: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Parent File: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Members: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Parent File: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Group Members: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

What other information is required by each condition?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Which conditions define the denominator (sample)?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Choose which conditions define the fall outs and what is their relationship to each other? Use & (and), ! (or), ' (not), and parentheses () to specify the relationship between two or more conditions. Example: (C1&C2)!(C3&C4)

10\. What is the relationship between the conditions that define the denominator (sample)? Use & (and), ! (or), ' (not), and parentheses () to specify the relationship between two or more conditions. Example: (C1&C2)!(C3!C4)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11\. What condition defines the date of the event:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12\. Time Frame: (Choose only one.)

\_\_\_ Annually \_\_\_ Monthly

\_\_\_ Daily \_\_\_ Quarterly

\_\_\_ Fiscal Semi-Annually \_\_\_ Semi-Annually

\_\_\_ Fiscal Yearly \_\_\_ Weekly

13\. Threshold: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If this is a percent threshold, should the threshold be met when the calculated percentage is (high) \>= or (low) \<= the threshold.

14\. For percent thresholds, the Minimum Sample Size:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

For numeric thresholds, the Pre-Threshold Alert Level:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

15\. Do you want to allow 'duplicate' fall outs during the time frame: Yes/No

16\. Other Data to Capture: Review the list of data elements for each condition you are using to select a list for capture with each fall out.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

17\. Do you want to print: 1) Daily fall out list: Yes / No

2\) Daily worksheets: Yes / No

18\. Do you want a bulletin: 1) When threshold met: Yes / No

2\) At end of time frame: Yes / No

3\) When alert level met: Yes / No

19\. What mail group will receive the bulletins:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

20\. Start Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

End Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

21\. Remember to turn it ON and mark it as FINISHED.

# Appendix D - Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Question:</th>
<th>What is the Clinical Monitoring System?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>The Clinical Monitoring System is a software program that nightly scans the VistA data base for selected conditions and provides a list of fall outs (patient names) that meet the conditions.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>All I want from the auto enroll monitor I'm developing is a list of patients. I'm not interested in numerator/denominator information, thresholds, time frames, etc. Can I ignore these fields?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td><p>You <strong>must answer</strong> the fields:</p>
<p>1. Auto Enroll Monitor as YES,</p>
<p>2. Fall Out Relationship,</p>
<p>3. Condition for Date of Event, and</p>
<p>4. Start Date.</p>
<p>And you <strong>must</strong> mark the monitor as <strong>Finished</strong> and turn it <strong>On</strong>.</p>
<p>You may bypass the fields:</p>
<p>1. Contributes to Sample,</p>
<p>2. Sample Relationship,</p>
<p>3. Time Frame,</p>
<p>4. Threshold,</p>
<p>5. Other Data to Capture, and</p>
<p>6. Bulletin Mail Group.</p>
<p>You also do not need to enter a:</p>
<p>1. Service,</p>
<p>2. Standard of Care,</p>
<p>3. Clinical Indicator, or</p>
<p>4. Rationale.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>I have built some monitors that I don't want to keep. How do I get rid of them?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>IRM was given a programming option, Monitor File Edit, that can be used to delete monitors.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Question:</th>
<th>What is a group?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>A group is made up of one or more or all of the entries from a file. The file might contain wards, patient names, services, treating specialties, etc.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>When should I build a group?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>First, review the description of each of the conditions you are going to use. If any of the descriptions mention a group, then you must decide if you want every entry in that file or only a subset of the file entries. If you want a subset, you must use the Group Edit option to build the group. If you want all the entries, respond by striking the &lt;RET&gt; key in the monitor edit (not group edit) to any of the group prompts.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>What if I don't know what members are in the group?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td><p>If you know what members you want but do not know if a group has already been built, use the Group File Inquire option.</p>
<p>If you do not know the contents of the file you need, check Appendix B of this Guide to see if a list of members is provided along with the condition. If not, then the list is most likely specific to the site. Either ask IRM for a print out of the members or query the file (enter ??) in the Group Edit option.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>I sometimes need to leave in the middle of building a monitor and when I return don't remember where I left off.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>At the "Select CONDITION:" prompt, enter one question mark. If you have already entered conditions, your list should appear numbered after the statement "ANSWER WITH CONDITION NUMBER:". You may choose each condition and view the responses already entered by moving down through the prompts by striking the &lt;RET&gt; key.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>How can I use the same condition twice in a monitor?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>Enter the condition in quotes (e.g., "LAB"). The entire name of the condition does not have to be entered, just enough to single it out.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
</tbody>
</table>

| Question: | I am designing the monitor and forget which of the conditions I planned on using and I don't want to exit the option to view the contents of the condition.                                                                                                                                                                                                                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Answer:   | At the "Select CONDITION:" prompt enter ?? to get a list of all the conditions. To get a description of a single condition, enter ?CONDITION NAME or enter ?\* to get a description for every condition. Refer to Appendix B in this Guide. We strongly suggest using the worksheet provided in the Build a Monitor Worksheet option to design your monitor before entering it into the software.                                                                            |
|           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Question: | How do I choose a Condition for Date of Event?                                                                                                                                                                                                                                                                                                                                                                                                                               |
|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Answer:   | Event generally means something has happened. Choose the condition with the most unique date associated with it. The conditions for Age, Patient Group, SSN Sample, and Sex would not be appropriate selections for Condition for Date of Event.                                                                                                                                                                                                                             |
|           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Question: | How do I determine what makes up the denominator?                                                                                                                                                                                                                                                                                                                                                                                                                            |
|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Answer:   | Before building a monitor for which you want to have denominator and numerator data, you should always define what members of the patient data base make up the denominator (sample) and numerator. That should help you in determining which conditions are needed for each. They depend entirely upon the type of information you intend to make comparisons by. For those conditions that do make up the denominator (sample size) answer YES to "Contributes to Sample". |
|           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Question: | Suppose I start a monitor in the middle of a quarterly time frame for a monitor. Does the quarter begin when the monitor starts? Or does the monitor start running at the beginning of the next full quarter?                                                                                                                                                                                                                                                                |
|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Answer:   | The monitor begins searching the data base the night following the Start Date (if it is turned on). Data is compiled for the MONITOR HISTORY file (#743.2) beginning the same day. This is important to remember when you compare one time frame to another. The results from the first time frame reflect the number of days the monitor was running.                                                                                                                       |
|           | \_\_\_\_\_\_\_\_\_\_\_\_\_\_                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Question:</th>
<th>What does "Allow 'Duplicate' Fall Outs" mean?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td><p>There are two types of duplicates:</p>
<p>1. The patient, monitor, and event date/time are identical. This type of duplicate will not be picked up by the Clinical Monitoring System.</p>
<p>2. The patient and monitor are identical and are within the same time frame. It may be the same date but different times. It may be different dates but within the same time frame. This type of duplicate will fall out when you answer YES to the prompt "Allow 'Duplicate' Fall Outs".</p></td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>How do I stop a monitor from running?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>Use the Quick Monitor Edit option and turn the monitor's ON/OFF switch Off.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>How do I know if CMS ran over a given date range?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>Use the Auto/Manual Enroll Monitors Run option.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
<tr class="even">
<td>Question:</td>
<td>If I choose a monthly time frame, does this mean auto enroll will scan for the entire time frame all at one time?</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Answer:</td>
<td>No. It runs every night but the statistics will be aggregated by the time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td>______________</td>
</tr>
</tbody>
</table>