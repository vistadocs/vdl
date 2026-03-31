---
title: Occurrence Screen Version 3 ADPAC Guide
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: anchor
doc_subject: ADPAC Guide
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
description: For this portion of the manual, you should be at a terminal that can access Occurrence Screen V. 3.0 in a test account. This exercise demonstrates how to validate data and test the validity of documentation. It should also provide some insight as to the information that you should convey to the user
audience: 
keywords: 
  - occurrence
  - review
  - peer
  - auto
  - contents
  - table
  - clinical
  - service
  - report
  - enrollment
page_count: 0
word_count: 7407
section_count: 18
table_count: 57
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/9/09
revision_oldest: 3/9/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocadp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocadp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=49"
---

![](occurrence-screen-version-3-adpac-guide/001.png)

Occurrence Screen V. 3.0ADPAC GuideSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/9/09

|          |                                       |                     |                      |
|----------|---------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
| 3/9/09   | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [# Package Management](#package-management)
- [# Changes from V. 2.5 to V. 3.0](#changes-from-v-25-to-v-30)
  - [Auto Enroll Changes](#auto-enroll-changes)
  - [Report Changes](#report-changes)
  - [Edit Changes](#edit-changes)
  - [Miscellaneous Changes](#miscellaneous-changes)
- [# Implementation Check List](#implementation-check-list)
  - [Virgin Installations](#virgin-installations)
  - [Conversion Installations](#conversion-installations)
  - [# Menu Option Assignment](#menu-option-assignment)
- [Package Operation](#package-operation)
  - [Functional Flow](#functional-flow)
  - [Multi-Service Review](#multi-service-review)
  - [Automatic Enrollment](#automatic-enrollment)
    - [Changes from V. 2.5 to V. 3.0](#changes-from-v-25-to-v-30-1)
    - [Screens that are Auto Enrolled](#screens-that-are-auto-enrolled)
    - [Information Captured by Auto Enrollment](#information-captured-by-auto-enrollment)
    - [Worksheets](#worksheets)
    - [Auto Enrollment Supporting Options](#auto-enrollment-supporting-options)
    - [Trouble Shooting](#trouble-shooting)
  - [Manual Enrollment](#manual-enrollment)
  - [Reports](#reports)
  - [VAMC-Specific Screens](#vamc-specific-screens)
- [Exercises](#exercises)
  - [Overview](#overview)
  - [Instruction](#instruction)
  - [Example](#example)
  - [Summary](#summary)
- [Glossary](#glossary)
- [Appendix](#appendix)
This guide is designed as an educational and resource manual to support the Quality Management ADPAC in installation, testing, training, use, and maintenance of the Occurrence Screen software.
This software supports the Occurrence Screening process as described in the VHA (Veterans Health Administration) circular. It gathers and manipulates data for the following Occurrence Screens.
*Readmission within 10 days (Screen 101.1)*
Justified exceptions excluded by the software.
- Scheduled readmission
- Prior discharge AMA (against medical advice) or Irregular
- Readmission to NHCU, Intermediate Medicine, or Domiciliary
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
*Death (Screen 109)*
Justified exceptions excluded by the software.
- No justified exceptions can be excluded by the software
Justified exceptions that cannot be excluded by the software.
- DNR (do not resuscitate) order or local equivalent at time of admission or more than 7 days prior to death
- Admitted for palliative (terminal) care

# # Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occurrence Screening is considered a Risk Management activity; therefore, Occurrence Screening records and documents stored and produced by this Occurrence Screen software are considered confidential and privileged. Title 38 U.S.C. 5705, as amended by Public Law 99-166, and the implementing HSRO (Health Services Review Organization) regulations (Title 38 Part 17) provide that HSRO records and documents which refer to individual practitioners are confidential and privileged. Exempt from this protection are aggregate statistical data, such as Occurrence Screening trend reports that do not identify individual VA patients or employees.

# # Changes from V. 2.5 to V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Auto Enroll Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Beginning with this version, the Occurrence Screen auto enroll is performed by the Clinical Monitoring System.
- The auto enroll summary sheets now include *previous movement* which is defined as follows.

> <u>Screen</u> <u>Previous Movement</u>

> 101.1 Previous discharge date

> 102 Outpatient visit date that spawned the 102 occurrence

> 107 Date of the first O.R. visit

> 109 The death discharge's associated admission date

> 199 Previous discharge date

- The ASSOCIATED ADMISSION field (#741,.02) is now automatically stuffed by the auto enroll and manual entry options. (A post-init is also included to populate pre-existing Occurrence Screen records.)
- The auto enroll process automatically stuffs a severity level of 3 - death when an occurrence of 109 (death) is auto enrolled.
- The QA Site Parameters for Occurrence Screen now include a multiple field for scheduled admission clinics. The auto enroll will look for scheduled visits to these clinics to determine which admissions are scheduled.
- The auto enroll automatic printing of patient lists and worksheets now supports multi-divisional facilities. A new multiple field has been added to the site parameters to allow associating a printer with each division.
- The QA Site Parameters for Occurrence Screen now include a field that tells the auto enroll if the Surgery package is installed or not. If this field is answered YES, screen 107 can be auto enrolled.
- A new screen was added, 199 - Readmission to acute care within 48 hours of discharge to extended care. The screen is marked with a local status, but it is exported in the national number space. This screen is included to support the Quality Improvement Checklist (QUIC). The QA Occurrence Auto Run Dates file (#741.99) has been modified to track the statistics for this new screen.
- The manually entered occurrences are now counted by their record creation dates rather than their occurrence date. This leads to more accurate counts in the auto run dates tally report.

## Report Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A new report was added, Statistical Review Summary report. This is a report of the Clinical and Peer findings, the Management actions, and the Committee data.
- The Ad Hoc report generator was greatly enhanced.
- A new report option, Reliability Assessment Worksheets, was added to assist in the inter-reviewer reliability assessment process. This option prompts the user for a date range and the screens to be included. It then randomly selects a user-specified number of occurrences and prints clinical and peer worksheets (with and without data) for these occurrences.
- The Delinquent Reviews report now allows the user to select a date range for the report.
- Reviewer worksheets may now be printed totally blank of all data.
- The Occurrences by Service report now prompts the user for the services and screens to be included.
- The Patients Awaiting Clinical Review report now prompts the user for an occurrence date range.
- The Review Level Tracking report now prompts the user for an occurrence date range.
- Modifications to the Summary of Occurrence Screening (Semi-Annual) report.
- The user can request a report of those occurrences that are pending.
- The Number of Actions Taken column in part II is automatically filled in.
- The Service Specific occurrence table in part II is automatically filled in.

## Edit Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Multiple records may be selected by patient or date range for editing. There is also a site parameter to turn this feature on/off.
- A new cross reference has been added to File \#741 to allow look-ups of occurrences by the occurrence identifier field.
- The free text Comment fields in the Reviewer and Committee multiples have been changed to word processing fields. (A pre-init conversion moves the old field data into the new field.)
- A new option was added, Final Disposition. This option allows the final disposition date, final disposition reached by, and status fields to be quickly edited.
- Multi-service reviews are now possible. A Reviewing Service field was added to the review level multiple. Another field, Final Peer Review Per Service, was also added to allow for multiple Peer reviews per service. This field marks the final Peer review findings for a given service.
- The Validation/Confirmation option was removed from the menu. With the addition of multi-service reviews, validation is no longer necessary.
- The Clinical, Peer, Manager Review option asks if you are adding a new review level only if a duplicate review level already exists. If no duplicate is found, the new review level is automatically added.
- In the Enter New Occurrence option, if a duplicate occurrence is entered the warning/help message now includes instructions on how to enter another similar occurrence for the same patient, but with a unique date and time.
- The Purge Deleted Occurrence Screen Records option purges those records that have been marked as deleted. The user may choose a date range and which screens to delete.
- The Clinical Reviewers option has been modified to allow the user to allocate and deallocate the Clinical reviewer key (QAOSCLIN). See the Miscellaneous Changes portion of this section.

## Miscellaneous Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Severity level numbers are converted from 1-4 to 0-3 by a pre-init routine. The new numbering scheme now matches that used in the Incident Reporting package.
- The old version (V. 1.01) Occurrence Screen files/fields are deleted. Also deleted are the temporary OS/2.5 conversion fields in File \#740.
- The menus have been totally restructured. The Occurrence Screen User Menu is now located under the Occurrence Screen Manager Menu. Some of the menu text has also changed. See the Appendix.
- Summary of Occurrence Screen Bulletin option uploads the Summary of Occurrence Screen Report to the National QA Data Base (NQADB).
- The package makes use of security key QAOSCLIN. The QAOSCLIN key is used to screen the reviewer Name (#741.01,.02) field for Clinical reviewers. This key replaces the functionality of the QA Occurrence Clinical Reviewer file (#741.3). This file has been starred (\*) for deletion.

# # Implementation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Virgin Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this is a first time installation of Occurrence Screen at your site, you should review the following check list.

- 1\. Read the Functional Description section of the User Manual for an overview of the package contents. Review the Table of Contents in the User Manual to familiarize yourself with the information available to you.
- 2\. Review the contents of this ADPAC Guide. You will need to give it and the User Manual a closer examination once the software is installed.
- 3\. Discuss equipment requirements with IRM.

> a\. You need at least one dedicated (80 column) printer for your use, or one for each division if you are a multi-division site. Discuss placement of the printer(s) with IRM. The printer must be available at all times, even weekends since it will be used for the daily run of auto enrolled occurrences. If it is kept in a locked, unmanned room at night and over the weekend, decide who will be responsible for making sure the printer is turned on and has sufficient paper. If the printer runs out of paper, it will continue with the print as soon as paper is added.

> b\. The Statistical Review Summary report uses 132 columns. Refer to the User Manual for an example of the output. If this is a report you can use, check with IRM about available printers.

- 4\. Discuss the time frame for setting up a training account and going live with both the IRM staff and the QM staff.
- 5\. Review the Automatic Enrollment portion of the Package Operation section of this guide. It will explain how auto enrollment functions, and alert you to problems you may encounter. This will also help you setup the program. After reviewing this section, you should discuss the information with your MAS ADPAC. Specifically discuss 1) how scheduled admissions are handled and 2) whether or not MAS uses the Treating Specialty field for all patient movements.

Virgin Installations

- 6\. If at all possible, setup a test/training account under the direction of IRM. You can use this account to learn how the software works and to train the other users.
- 7\. Before setting up the software, you need to gather some information from the QM staff. Take time now to get what you need so setup will run smoothly.

> a\. Turn to the pages in the User Manual covering Site Parameters. Obtain sufficient information to respond to each field. If something isn't clear, discuss it with IRM or the QM staff. For convenience, you may want to write in your responses for future reference. Obviously, you can also access this option anytime to view its contents.

> b\. Obtain a list of those users who are Clinical Reviewers.

> c\. Discuss with the QM staff any types of occurrences they would like to track using this software that are not national screens. Review the chapters in the User Manual on VAMC-Specific Screens and Reasons for Clinical Referral or the VAMC-Specific Screens portion of the Package Operation section of this guide.

> d\. If medical teams are used at your site, does the QM staff wish to include medical teams in the Occurrence Screen software? If used, occurrences can be attributed to medical teams.

> e\. Committees are used in this software to review system and/or equipment problems. Obtain a list of committees that your site wants to use for referrals of these types of occurrences.

> f\. Compile a list of all the retired national screens that the QM staff wants to continue using (i.e., those marked as LOCAL).

Virgin Installations

- 8\. Before using the software, you must complete a, b, and c listed here or the software will not work. Using the Package Setup Menu:

> a\. Populate the Site Parameters option.

> b\. Populate the Clinical Reviewers option.

> c\. Assign a care type to all the treating specialties used at your site through the Treating Specialty Care Types option.

> d\. Populate the Committees option and the Medical Teams option if you intend to use them. Populate the VAMC-Specific Screens option and the Reasons for Clinical Referral option if you want to set up screens not exported with the software.

> e\. The installation of Occurrence Screen Version 3.0 will mark <u>all</u> retired national screens as INACTIVE. Consult list compiled under Step 7, letter f for those to be marked as LOCAL.

- 9\. Now is the time to learn how to use the software. Review this guide then run through the exercises provided. Use any options not covered in the exercises. Refer to the User Manual for additional help. Both of these manuals contain a great deal of information. Always check these references before asking for help.

> a\. Completely understand how multiple service review works.

> b\. Completely understand how the data for the Semi-Annual Report is generated.

> c\. Obtain a copy of the QM Integration Module User Manual and acquaint yourself with the sort and print modifiers available in Ad Hoc.

- 10\. Once you master the program, discuss menu option assignment with the QM Manager. Refer to the Menu Option Assignment section in this guide for suggestions. Provide a list of users and their menus to IRM.
- 11\. Now train the users. If you are using a training account, let them practice in that area. Show them how to check their input against the reports generated. Each user should understand how the software functions.

Virgin Installations

- 12\. Once everyone is trained, the software can be installed into a live account.

> a\. Repeat Step \#8. IRM must also populate the Clinical Monitoring System Site Parameters option. Auto enrollment of Occurrence Screens is managed by the Clinical Monitoring System.

> b\. Spend some time checking the auto enroll function. If there are problems, were they ones you expected? If not, refer back to the section on Automatic Enrollment. Determine what is happening and work to correct the problem. Remember, this software can only access data that is available.

> c\. Above all, check to see that data entered is appearing in the reports, specifically the Semi-Annual Report.

## Conversion Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will find that this version of Occurrence Screening is very similar to V. 2.5. The names of some of the options are different and the menus rearranged which may at first seem confusing. The changes were done to facilitate distribution of menus and selection of options. There were several options removed and several added. Refer to the Appendix for a listing of the menu and option name changes.

You will also see a number of enhancements that were included to speed up data entry and editing. Another important note is that with the installation of this software, the Clinical Monitoring System V. 1.0 is also installed. Occurrence Screening uses the Clinical Monitoring System to auto enroll the screens. With this information in mind, use the following check list for implementation of this version of the software.

- 1\. Study the software changes from V. 2.5 to V. 3.0 for anything that will affect setup of the software.
- 2\. Within the User Manual, review the Site Parameters option for any new information you will need, specifically:

> a\. Do you want to allow multiple patient selection when exercising some of the options? This is fully described in the Orientation Section of the User Manual.

> b\. Is the Surgery software installed and being used at your site? If it is, you will be able to auto enroll screen 107, Returns to OR.

> c\. Do you use one or more clinics to schedule admissions? You will want to enter the names of these clinics into the site parameters.

> d\. If you are a multi-divisional site, you can now enter each division into the site parameters along with a printer name for each division.

- 3\. The Statistical Review Summary report requires a 132 column print. See the example provided in the User Manual. If it is a report that you would like to use, discuss available printers with IRM.
- 4\. Following installation, IRM should populate the Clinical Monitoring System Site Parameters option using the instructional portion of the Clinical Monitoring System User Manual for direction.

Conversion Installations

- 5\. Following installation, populate the Occurrence Screen Site Parameters option. Use the instructional portion of the Occurrence Screen User Manual for direction. Then access each of the following options for any changes that must be made.

> a\. Using the Treating Specialty Care Types option, make certain that each treating specialty used at your site is assigned a specialty care type: Acute Care, Special Care, Intermediate Care, NHCU, or Psychiatry. You may not need to make any changes to this file, but now is the time to make sure what is there, is correct.

> b\. Using the Clinical Reviewers option, check to make certain every name with a key is correct. Now is the time to clean up any discrepancies.

> c\. Review the other options within the Package Setup Menu to see if there are any other changes you would like to make.

- 6\. Read through this manual again.

> a\. Completely understand how multiple service review works before assigning options to the users. You may want to install the package in a test account to work the software before training other users.

> b\. Completely understand how the data for the Semi-Annual Report is generated. Items c, d, e, f, and g are calculated differently than in the previous version. Teach these differences to the users.

> c\. Review multiple patient selection so you understand where it is used and how it works. Teach the users.

> d\. Obtain a copy of the QM Integration Module User Manual and acquaint yourself with the new sort and print modifiers available in Ad Hoc. Learn how to use these modifiers and train the users.

> e\. Review the list of changes between the previous version and this one. Using the software, see how the changes affect its function. Any useful information should be passed along to the users.

- 7\. Assign menus to users.
- 8\. Do not assume everything will work correctly. For the first couple weeks, do some data validation. Check with the users again to make sure they understand how the multiple service review works. Make sure their entries come out correctly on the Semi-Annual Report.

## # Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menus for Occurrence Screen were rearranged to facilitate the assignment of options to users. The entire menu is shown here.

Occurrence Screen Manager Menu

Occurrence Screen User Menu

Basic Occurrence Data

Clinical, Peer, Manager Review

Committee Review

Enter New Occurrence

Final Disposition

Inquire Occurrence Screen Record

Quick Exception Edit

Reports Menu

Ad Hoc Report

Adverse Findings

Delinquent Reviews

Occurrences by Service

Patients Awaiting Clinical Review

Review Level Tracking

Service Statistics

Statistical Review Summary

Summary of Occurrence Screening (Semi-Annual Rpt)

System/Equipment Problems

Worksheets

Open Closed/Deleted Occurrence Screen Record

Package Setup Menu

Clinical Reviewers

Committees

Medical Teams

Reasons for Clinical Referral

Site Parameters

Treating Specialty Care Types

VAMC-Specific Screens

Purge/Delete Menu

Auto Enrollment Run Dates Purge

Delete Occurrence Screen Record

Purge Deleted Occurrence Screen Records

Reports Menu

Audit File Inquiry

Display Treating Specialty Care Types

Enrollment Dates Tally

Practitioner Code List

Reliability Assessment Worksheets

Run Auto Enrollment Manually

Summary of Occurrence Screen Transmission

QA Ocurrence Screen file (#741) should never be edited via VA FileMan. Always edit through the options.

The Manager Menu should be assigned to an IRM support person, the QM ADPAC, and whoever manages the QM software in the ADPAC's absence.

The following are suggestions which may help you in menu distribution.

- Assign the User Menu to the Clinical Reviewers and their clerical staff.
- Assign the Clinical, Peer, Manager Review option and the Inquire Occurrence Screen Record option to Peer and Management reviewers or their designees.
- Assign the Committee Review option and the Inquire Occurrence Screen Record option to committee chairs or their designees.
- 

# Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flow of the Occurrence Screening process differs from site to site. The following flow shows you how the software may be used when there is no computer involvement by Peer, Manager, and Committee levels.

1\. If there are any cardiac/respiratory arrests from the day before, enter these occurrences manually through the Enter New Occurrence option. If your site is not using the Surgery package, any returns to the OR that are occurrences should be entered via this option.

2\. Print out the Clinical Worksheets for the manually enrolled screens using the Worksheets option.

3\. Pick up the worksheets for those screens that were auto enrolled from the previous day.

4\. Review the patient's records, completing the worksheets.

5\. Enter any exceptions to the criteria through the Quick Exception Edit option.

6\. Enter the data from the Clinical review through the Clinical, Peer, Manager Review option. Close out those records that do not need further review by entering the final disposition information.

7\. Using the Worksheets option, print out Clinical, Peer, Management, and for system/equipment problems, Committee Worksheets with data for those records that require further review. Send them on for second level review.

8\. When the worksheets are returned, enter any committee findings first via the Committee Review option. For those records requiring only committee review, use the Final Disposition option to close the record.

9\. Enter the data from the Peer and Manager reviews via the Clinical, Peer, Manager Review option and close out those records by entering the final disposition information. *Remember to enter a final Peer review for each reviewing service. This is essential for the Semi-Annual Report to reflect actual Peer reviews.*

## Multi-Service Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a good understanding of multi-service review, there are a few things to keep in mind.

- For the most accurate information, tell users to always complete the Reviewing Service field for <u>each</u> Peer review and <u>each</u> Manager review entered.
- <u>Each</u> Reviewing Service must have a <u>final</u> Peer review entered for an accurate accounting on the Semi-Annual Report.
- A <u>blank/null</u> Reviewing Service field is considered by the computer to be a service. It might be helpful to think of Null as the name of a single service.

Let's take a look at an example of a multi-service review.

The occurrence is a death that is referred for Peer review to Medicine and Surgery. Medicine sends it through two Peers for review and Surgery sends it to three Peers. One Service finds an outcome of Level 1 and the other finds an outcome of Level 2. Their reviews are entered into the program, but the user does not enter a Service for two of the Peer reviews from Surgery.

Reviewing Service

Field = : <u>Medicine</u> <u>Surgery</u> <u>\<NULL\></u>

Peer 1 Peer 3 (F) Peer 4

Peer 2 (F) Peer 5

(F)= Entered as Final Peer Review

On the Semi-Annual Report, the computer will count this as three (3) Occurrences Referred to Peer because it sees three different services, one (1) Level 1 Outcome of Peer Review, one (1) Level 2, and one (1) pending.

If a final Peer review is not entered for each Service that does a Peer review, that will be counted as a Pending Outcome of Peer Review. In the example above, the Reviewing Service field was Null for two reviews so it was counted as another service. Remember, if more than one Reviewing Service field is left Null, it is counted as a single service.

## Automatic Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Changes from V. 2.5 to V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several differences in auto enrollment to be noted with this version of Occurrence Screen. See the Changes from V. 2.5 to V. 3.0 section of this guide, Auto Enroll Changes.

### Screens that are Auto Enrolled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

101.1 Readmission within 10 days

102 Admission within 3 days following unscheduled Ambulatory Care visit

107 Return to OR in same admission (only if you answered YES in the Site Parameters that the

Surgery package is installed)

109 Death

The following screens were made inactive by V. 3.0 of Occurrence Screen, but if marked as Local under the VAMC-Specific Screens option, they will continue to be auto enrolled. We will only discuss the automatic enrollment of screens 101.1, 102, 107, and 109.

101 Readmission within 14 days

103 Admission within 3 days following Ambulatory Care surgery procedure

104 Admission or ASIH from VA Nursing home Care Unit:

> a\. Within 14 days of discharge from Acute Care

> b\. To Psychiatry Service

105 Transfer from Intermediate Medicine:

> a\. Within 14 days of transfer from Acute Care

> b\. To Psychiatry Service

106.1 Transfer to Special Care Unit within 72 hours of transfer from a Special Care Unit

*When setting up the software, you must use the Treating Specialty Care Types option and designate each of the Treating Specialties at your site as either Acute Care, Special Care, Intermediate Care, NHCU, or Psychiatry.* Any auto enrolled screen that is dependent upon the entry of Treating Specialty is dependent upon each specialty having been accurately entered into the Treating Specialty Care Types option.

*Auto enrollment in Occurrence Screen is also dependent upon information contained within the PIMS Scheduling package and the Surgery package for accurate capture of the screens.* If the packages are not being used as intended, there will be discrepancies with the auto enrollment feature. Surgery may be installed but not being used or not being fully used. Certain fields in MAS may not be used. Keep this in mind when you do any trouble shooting.

Automatic Enrollment

Auto enrollment runs once each day and captures those occurrences that happened on the day prior to the run. There is a manual run for the auto enrollment. We will describe this later in this section.

Screen 101.1, Readmission within 10 days, depends on the use of either the "Schedule an Admission" option or scheduled admission clinics. If your site only uses the "Schedule an Admission" option for scheduling admissions, patients are considered unscheduled admissions by the auto enrollment function if they are not entered as scheduled admissions in that option.

Some facilities use an admission clinic or clinics so they can schedule patients to come in at specific times during the day. Be sure that these clinics are entered into the Site Parameters options in the Scheduled Admission Clinic field. The auto enroll will look for scheduled visits to these clinics to determine which admissions are scheduled.

Also, the Treating Specialty field must be accurately entered. This screen looks for all readmissions for Acute Care, Special Care, Psychiatry, and Nursing Home. The only exception is if the Nursing Home readmission is the same day as discharge from Acute, Special or Psychiatry, it is not captured.

Screen 102, Admission within 3 days following unscheduled Ambulatory Care visit, auto enrolls any patient admitted to Acute or Special Care who has had any type of unscheduled Ambulatory Care visit. An Ambulatory Care visit could be a stop at outpatient pharmacy, a lab test or x-ray, or a clinic/ER visit. Every visit that is unscheduled, except same day admissions, will be picked up by this screen. MAS should be entering patients into either the "Registration" option for ER visits or the "Check-In/Unsched. Visit" option. *To reduce the number of auto enrolls of "walk-ins just before midnight/admitted after midnight", be sure to enter the minimum time between logout and admission within the option "Enter or Change Operational Parameters."* Screen 102 uses the minimum time between logout and admission from the site parameters file. If that field is left blank or "0" is entered, screen 102 will function as it did in V. 2.0.

Screen 107, Return to OR in same admission, depends on Surgery Version 3.0 being *fully implemented and the field, Surgery Package Installed in the Site Parameters, containing YES*. The screen picks up any patients who had major surgery and returned in the same admission for major surgery.

The patient must be an inpatient, and if the second surgery is scheduled prior to the first surgery being done, the program sees it as an exception and does not enroll the patient.

Screen 109, Death, depends on the Date of Death field in the Patient file.

Automatic Enrollment

### Information Captured by Auto Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is captured by the auto enrollment function because a screen is met, it also captures the following available information and stores it with the occurrence.

Patient name

Occurrence date

Ward or clinic where occurrence took place

Screen number and name

Treating specialty

Service

You will see other information printed on either the worksheets or auto enroll sheets (SS#, admitting diagnosis, previous D/C, current ward for example). This data is stored by the PIMS package, so the Occurrence Screen package does not have to house the information but picks it up when a printout is needed.

When the user finds auto enrolled data that is not correct, that information can be corrected by using the Basic Occurrence Data option or Clinical, Peer, Manager Review option. If auto enrollment picks up a patient that should not be captured, you can delete the entire record through the Delete Occurrence Screen Record option on the Purge/Delete Menu.

If a record is starred (\*) on the daily Auto Enrolled Occurrence Screen Patients, that means the patient was already in the data base when the run was done. This could only happen if the patient was either manually entered prior to the daily auto run <u>or</u> a manual run was done prior to the auto run, in which case, all the records will most likely be starred.

### Worksheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When installing the package, you need to consider whether or not you want the Clinical Worksheets printed whenever the auto enroll runs. If you answer YES to Auto-Print Clinical Worksheet in the Site Parameters option on installation or anytime thereafter, you automatically get Clinical Worksheets printed everyday for each occurrence captured. Just as this auto print of the worksheets can be turned on, it can be turned off at anytime through the Package Setup Menu.

Whenever there is a print of a Clinical Worksheet, manual or automatic, you always get Part 2 of the Clinical Worksheet. If you also want Part 1 printed each time, enter that choice through the Package Setup Menu option, Site Parameters.

Automatic Enrollment

As stated earlier, if the information is available when the worksheets print out during auto enrollment, the top portion of the worksheet provides the patient name and SS#, the occurrence date, the occurrence number and name, the current ward, Service, and the Treating Specialty.

### Auto Enrollment Supporting Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enrollment Dates Tally option is used to determine if it is necessary to run a manual enrollment because on one or more days auto enrollment missed running due to computer down time or printer malfunction. This is a simple tool used to backup the auto enroll function. The printout provides the number of patients captured for each screen for every date requested and tells the user what dates auto enroll did not run.

Run Auto Enrollment Manually option is used whenever you find auto enroll did not run on a particular date. It can also be used if you know that your site routinely delays entering particular data that is needed by the auto enrollment function, such as transfer information and deaths. It will star any occurrence that was previously entered and automatically enter all others into the package giving you a printout similar to the daily printout of auto enrolled patients.

When using this option, it is of particular importance to note that when running multiple reruns, you must choose start times separated by <u>at least</u> 30 minutes. The times must also be for today's date, in other words: "T@..." This run is CPU intensive, meaning that it uses a great deal of computer time. It is best to talk to your IRM support person to determine the best times to queue the printing of this output.

Auto Enrollment Run Dates Purge option eliminates old entries from the Auto Run Dates file. These entries are used by the Enrollment Dates Tally report to determine which days Auto Enrollment has or has not run. Before using this option, be sure auto enroll has run on every day you intend to purge. Keeping files "lean" helps a package run faster and is a necessary function of your job as QM ADPAC. The output Enrollment Dates Tally will show the message \*\*\* AUTO ENROLL DID NOT RUN ON THIS DATE \*\*\* for the purged dates.

Automatic Enrollment

### Trouble Shooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Trouble shooting can be the most labor intensive part of a package, particularly when software is first installed. It is best to be pro-active and check the auto enroll function at routine times throughout the use of the package. Also, consider checking the function whenever an Occurrence Screen patch is released that affects auto enroll or whenever a patch for the PIMS or Surgery packages is installed at your site.

A simple method of checking the data that is captured for screens 101.1, 106.1, and 109 is to use the daily MAS record (Gains and Loss) showing patient transfer and admission and discharge activity. Also, speak with your MAS ADPAC about obtaining access to certain PIMS options that will help you in your work.

For screen 102, inquire about the use of the Patient Profile option in the Outputs menu of the Scheduling module of the PIMS package and the Log of Disposition option found in the Disposition Outputs menu of the PIMS ADT Module.

For other auto enrolled screens, ask about the Detailed Inpatient Inquiry option which lists all admission dates for the selected patient and, within each admission, all transfer information and the discharge date.

For screen 107, make sure the Surgery package is fully implemented, not just installed.

You should also ask the MAS ADPAC if your site has designed other outputs that would give you the information you need.

When you find that the auto enroll function is not capturing records that should be captured or it is capturing more records than it should, begin with the information provided in this section and work through all the possibilities, including whether or not any necessary patches have been installed. From the information provided, you now know how the auto enroll function works; where it gets its data; what data it should be capturing; and what options support its function. If you still come up with a problem, discuss it with your IRM support person. Attempt to solve the problem before it is referred to your regional CIOFO support staff for QM software.

## Manual Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The manual enrollment of occurrences is accomplished through the Enter New Occurrence option. This must be done for any screens that cannot be auto enrolled (this includes all VAMC-specific screens).

If your site is not running the Surgery package, screen 107 (return to OR in the same admission) cannot be auto enrolled.

For all manually enrolled occurrences or VAMC-specific screens, the user will be asked to enter patient name, date of occurrence, screen, and ward/clinic (where occurrence took place). After entering this data, the user can either enter another record or start the review process.

> **NOTE:** To enter the same type occurrence for the same patient on the same day (e.g., two respiratory arrests on the same day), enter the times for each occurrence at the date prompt. With the time entered, the software recognizes them as two different occurrences.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should always validate the data in your printed reports. This discussion is provided so you will understand how the data is captured for each of the reports. Your users should understand that reports can only capture data that is available. If the data is not accurate, check first to see if the data was correctly entered.

Ad Hoc Report

A detailed description of this report appears in the QM Integration Module V. 1.7 User Manual.

Adverse Findings

The user will be asked to decide whether the output should include the names or codes or no names at all for the attending, resident, medical team, and those to whom the occurrence was attributed. The user will also need to enter a date range. The report only includes Final Peer Review adverse findings of level 2 or 3. Records can be either open or closed.

Delinquent Reviews

This report shows any reviews that are or were delinquent in completion on any open occurrence within a selected date range. At least a Clinical review must be entered with an action of "2 Refer to Peer Review" for a delinquent Peer review. The output looks for Peer review actions of "3 Refer to Management Review" and "6 Refer to Chief of Staff" for a delinquent Management review to appear. The review must have taken longer than the allowable number entered for either completion of Peer review or Management review (found under Site Parameters). If you skip entering parameters for timeliness of reviews, there will be no data for this report. The output lists by service the patient name, occurrence date and screen, when the due dates are for both Peer and Manager, and when they were actually completed.

Occurrences by Service

This report prints out all occurrences captured during a specified date range for selected services. The printout shows the patient name, date of occurrence, whether the record is open or closed, and the Treating Specialty. This report does not require any input beyond the service name for the occurrence to print out.

Patients Awaiting Clinical Review

This report provides a list of open occurrence records that have not had a Clinical review for a selected date range. The report includes the patient name, screen, date of occurrence, and current ward.

Review Level Tracking

This output prints out only open occurrences within the selected date range. There must be at least a Clinical level review entered for the occurrence to appear on the report. The information is provided by service and within service by name, with date and Occurrence Screen, and the findings from all reviews are listed.

ReportsService Statistics

This report comprises data by bed service. The service is determined by the Ward/Clinic field in Occurrence Screening instead of the Service field which can accept Nursing, Dietetics, Building Management, etc. as entries. If a record falls under "Non Count", that means your site has that particular ward in the Ward Location file listed as "Non Count" in its Service field. Any record falling under Unknown means that the Ward/Clinic field is \<Null\>. To print a list of those records with \<Null\> in the Ward/Clinic field, use Ad Hoc, sort by Ward/Clinic, and at the Beginning and Ending prompts, use the @ sign. For a record to appear on this report, it must fall within the date range selected.

Statistical Review Summary

This report is a summary of review activity presented in slightly different format than any of the above reports. To appear on this report, any record must fall within the date range selected.

Summary of Occurrence Screening

This report can print National, Local, and Inactive occurrences in any combination. The user may print out summaries for any given date range. The following information is extremely important in understanding how the data is captured for the report. Read it over carefully and make sure every user is familiar with the information.

System/Equipment Problems

This report depends on findings being entered into the Committee Review option. The user is asked to enter a date range. Both open and closed records with system and/or equipment problems will appear on the output.

*Definitions of column headers in Summary of Occurrence Screening*

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

Reportsa Criterion

This is a listing of the chosen screen numbers in order.

b Reviewed Clinically

See 1-5 above with the exception that it must have a Clinical review entered.

c Referred to Peer

See 1-5 above and must have Clinical Action = 2 <u>or</u> have any Peer review per service without a Clinical review entered. The number will also be incremented when multiple service Peer reviews are done. Refer to the Multi-Service Review section of this guide for more in-depth description of how these numbers are incremented.

d, e, f Outcome Of Peer Review, Number Final Ratings At (Levels 1, 2, 3)

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

## VAMC-Specific Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Designing Local Screens

The VAMC-Specific Screens option is found under the Package Setup Menu. It is used whenever you want to design a local screen other than those listed as nationally mandated Occurrence Screens.

Before using this option, decide on a number (any number 201 or greater) to identify with your screen. Give the screen a short name, and if you wish, a longer name that defines it further. Decide on any reasons for Exception. If there are no reasons for Exception, you should skip those fields by pressing the \<RET\> key.

Reasons for Clinical Referral

You may also want to assign reasons to refer these local screens on to Peer, Management, or Committee review. The Reasons for Clinical Referral option is used to do this. For each reason you enter, you will assign a code number and a short and long description of the reason. These reasons will print out on the Clinical Worksheet, Part 1.

Outputs

Data from VAMC-Specific Screens appears on all outputs. You may also access data concerning these local screens through the Ad Hoc Reports print option.

# Exercises

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For this portion of the manual, you should be at a terminal that can access Occurrence Screen V. 3.0 in a test account. This exercise demonstrates how to validate data and test the validity of documentation. It should also provide some insight as to the information that you should convey to the user in training.

## Instruction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The greatest help in deciding what information must be entered into the program is to understand what information is needed to produce the outputs. This exercise will take a look at the Summary of Occurrence Screening. Of all the reports, you and the users should become intimately familiar with how this report captures its data. Here is a reproduction used earlier in this manual of the definitions of column headers in the report.

*Definitions of column headers in Summary of Occurrence Screening*

\|CRITERION\|--# OF OCCURRENCES---\|--OUTCOME OF PEER REVIEW---\|-# OF OCCURRENCES-\|

\| SCREEN \| REVIEWED REFERRED \|LEVEL LEVEL LEVEL PENDING\| REFERRED FOR \|

\| \| CLINICALLY TO PEER \| 1 2 3 \| SYSTEM EQUIPMENT\|

\|=========\|=====================\|===========================\|==================\|

a b c d e f g h i

The following applies to all columns except that for Criterion Screen. Occurrence must:

6.  Be in date range chosen
7.  Be one of the screens chosen
8.  Must not be 'Deleted'
9.  Must have Clinical <u>and/or</u> Peer review(s)
10. Clinical Finding must not = 3 "Exception to Criteria".

a Criterion

This is a listing of the chosen screen numbers in order.

b Reviewed Clinically

See 1-5 above with the exception that it must have a Clinical review entered.

Instructionc Referred to Peer

See 1-5 above and must have Clinical Action = 2 <u>or</u> have any Peer review per service without a Clinical review entered. The number will also be incremented when multiple service Peer reviews are done. Refer to the Multi-Service Review section of this guide for more in-depth description of how these numbers are incremented.

d, e, f Outcome Of Peer Review, Number Final Ratings At (Levels 1, 2, 3)

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

Essentially, the definitions show that you can limit your input to Clinical and Peer reviews to obtain a Summary of Occurrence Screening.

Another main point that is not mentioned in the above directions is that to close out a record and take it out of your look up list of active records, you must enter a Final Disposition. The prompt "Do you wish to enter a FINAL DISPOSITION? NO//" only appears when certain actions and/or findings are entered. To always obtain the prompt when you have finished entering your data either in the Clinical or Peer review, enter an Action of 1 or 1.1. <u>Do not</u> skip the "Select ACTION:" prompt.

## Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now the best way to check to see if these directions are correct is to enter different types of reviews that will provide data for each column and print out a Summary of Occurrence Screens using the random date range that will cover the dates of the occurrences entered. Let's do that in a test account now entering all the occurrences for today's date.

Before entering reviews, we need occurrences in the program to work with. Even though the auto enroll mechanism can be tested while in the test account, the easiest method of getting occurrences into the program is by using the Enter New Occurrence option. Let's enter four occurrences, a 101.1, 102, 107, and 109, for today's date.

Now, using the definitions provided, enter:

- The 101.1 with only a Clinical review
- The 102 with a Clinical and Peer review with Level 2 finding
- The 107 with only a Peer review and a Level 1 finding
- The 109 with Clinical and Peer review, Level 1, and a System Issue.

To print a Summary of Occurrence Screening to capture the data you input, choose National screen criteria, a user selectable date range, and enter "T" for the beginning and ending dates. Your output should look like the following.

Example

> SUMMARY OF OCCURRENCE SCREENING - SEMI-ANNUAL REPORT - PART I

> -------------------------------------------------------------

> MEDICAL CENTER: HINES CIOFO

> PERSON PREPARING REPORT:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> TITLE & CORRESPONDENCE SYMBOL OF THE ABOVE:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> FTS TELEPHONE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ TELEFAX:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> REPORTING PERIOD: PERIOD FROM MAR 8,1998 TO MAR 8,1998

> \|CRITERION\|--# OF OCCURRENCES---\|--OUTCOME OF PEER REVIEW---\|-# OF OCCURRENCES-\|

> \| SCREEN \| REVIEWED REFERRED \|LEVEL LEVEL LEVEL PENDING\| REFERRED FOR \|

> \| \| CLINICALLY TO PEER \| 1 2 3 \| SYSTEM EQUIPMENT\|

> \|=========\|=====================\|===========================\|==================\|

> 1 (101.1) 1 0 0 0 0 0 0 0

> 2 (102) 1 1 0 1 0 0 0 0

> 3 (107) 0 1 1 0 0 0 0 0

> 4 (109) 1 1 1 0 0 0 1 0

> COMMENTS:

> PENDING OCCURRENCES MAR 08, 1998

> PAGE: 1

> Type 1 - Clinical action of 'Refer to Peer Review', but no Peer review was found

> Type 2 - Peer review(s) found for service(s), but none are marked as being final

> PATIENT SSN DATE OF OCCURRENCE TYPE

> -------------------------------------------------------------------------------

> No pending occurrences found.

Did your summary turn out the same way? If not, why not? Use the Inquire Occurrence Screen Record option and look at the data entered. To correct any record, use the Open Closed/Deleted Occurrence Screen Record option and enter the missing data.

Now test a multi-service review. Enter a new occurrence and give it three Peer reviews, one for Surgery, one for Medicine, and one leaving the Service field \<Null\>. How does this appear on the Semi-Annual Report?

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This instruction has shown you how data is validated and documentation is tested. The data entry for the exercise limited you to the use of only a small portion of the software, Clinical, Peer, Manager Review, Enter New Occurrence, and possibly the Quick Exception Edit and Open Closed/Deleted Occurrence Screen Record.

Now that you have tested the Summary of Occurrences, go back to the section on Reports and see what information is required by each report. Test the reports in the same manner that we tested the Summary of Occurrence Screens.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                     |                                                                                                                                                                                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC                  | Acute Care Unit                                                                                                                                                                                                                                                     |
|                     |                                                                                                                                                                                                                                                                     |
| Action              | Corrective or referral response taken as a result of an adverse finding on a review of an occurrence.                                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                     |
| Adverse findings    | Any findings above Level 1 care or any system and/or equipment problem.                                                                                                                                                                                             |
|                     |                                                                                                                                                                                                                                                                     |
| AMA                 | Against Medical Advice                                                                                                                                                                                                                                              |
|                     |                                                                                                                                                                                                                                                                     |
| ASIH                | Absent Sick In Hospital (nursing home patient).                                                                                                                                                                                                                     |
|                     |                                                                                                                                                                                                                                                                     |
| Attending physician | The staff physician responsible for the care of the patient involved in the occurrence.                                                                                                                                                                             |
|                     |                                                                                                                                                                                                                                                                     |
| Attribution         | Individuals, medical teams, or hospital locations involved in an occurrence. This is used for documentation and trend analysis, and is not necessarily used to assign blame.                                                                                        |
|                     |                                                                                                                                                                                                                                                                     |
| Auto enrollment     | The computer process that automatically extracts Occurrence Screens from daily admissions, transfers, and discharges.                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                     |
| Auto-print          | The computer process that produces printed documentation or reports without a specific request from the user. This is a part of auto enrollment.                                                                                                                    |
|                     |                                                                                                                                                                                                                                                                     |
| Closed occurrence   | An occurrence for which final disposition was made.                                                                                                                                                                                                                 |
|                     |                                                                                                                                                                                                                                                                     |
| Committee           | Any committee, such as Safety, that may be asked to review an occurrence involving a system and/or equipment problem.                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                     |
| Database            | (See File)                                                                                                                                                                                                                                                          |
|                     |                                                                                                                                                                                                                                                                     |
| Data dictionary     | A description of the file containing the categories of data that the user requires to produce the desired reports and printed documentation.                                                                                                                        |
|                     |                                                                                                                                                                                                                                                                     |
| Deleted occurrence  | An occurrence record that is considered not to be a valid item, such as an error in data entry, and is eliminated from the statistics. It is not actually deleted from the file, but marked to be ignored (this is a security precaution) in the gathering of data. |
|                   |                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
|                   |                                                                                                                                              |
| DNR               | Do Not Resuscitate                                                                                                                           |
|                   |                                                                                                                                              |
| Equipment problem | Having to do with the quality of the performance or design of equipment used, such as a respirator malfunction or broken wheelchair.         |
|                   |                                                                                                                                              |
| Exception         | A valid reason to eliminate an occurrence from being considered for further review, such as planned readmission within 10 days of discharge. |
|                   |                                                                                                                                              |
| Field             | One typed entry of data contained within a computer file. (Several fields make up a file.) Often called a prompt.                            |
|                   |                                                                                                                                              |
| File              | The computer's method of storing data required by the user. (See Field.) Sometimes also called a database.                                   |
|                   |                                                                                                                                              |
| Final disposition | The review of an occurrence was completed, corrective action (if any) was taken, and it is considered closed.                                |
|                   |                                                                                                                                              |
| Findings          | The categorized results of a review, such as optimal or Peer review needed.                                                                  |
|                   |                                                                                                                                              |
| Level 1 care      | A finding that "Most practitioners would handle case similarly."                                                                             |
|                   |                                                                                                                                              |
| Level 2 care      | A finding that "Most practitioners might handle case differently."                                                                           |
|                   |                                                                                                                                              |
| Level 3 care      | A finding that "Most practitioners would handle case differently."                                                                           |
|                   |                                                                                                                                              |
| Manager reviewer  | A Manager, such as a Service Chief or Chief of Staff, who is asked to review an occurrence for the purpose of taking action.                 |
|                   |                                                                                                                                              |
| Medical team      | A group of practitioners responsible for the care of the patient as a team.                                                                  |
|                   |                                                                                                                                              |
| Menu              | A computer display from which the User selects a process for the computer to perform, such as print a report, enter or change data, etc.     |
|                                      |                                                                                                                                                         |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      |                                                                                                                                                         |
| NHCU                                 | Nursing Home Care Unit                                                                                                                                  |
|                                      |                                                                                                                                                         |
| Occurrence Screen                    | A process whereby cases are identified which meet specified criteria.                                                                                   |
|                                      |                                                                                                                                                         |
| Open occurrence                      | A record of an occurrence still undergoing the review process.                                                                                          |
|                                      |                                                                                                                                                         |
| Option                               | A menu or one of the items in a menu.                                                                                                                   |
|                                      |                                                                                                                                                         |
| OR                                   | Operating Room                                                                                                                                          |
|                                      |                                                                                                                                                         |
| Parameter                            | A computer term referring to information supplied to the computer by the user in order to set up the programs to perform particular functions required. |
|                                      |                                                                                                                                                         |
| Peer reviewer                        | A Peer or committee of Peers that is asked by the Clinical reviewer to review an occurrence for a practitioner related issue.                           |
|                                      |                                                                                                                                                         |
| Practitioner                         | A licensed performer of medical services, such as a doctor.                                                                                             |
|                                      |                                                                                                                                                         |
| Primary Reason for Clinical Referral | The main purpose that a record is sent for further review, such as Peer, Manager or Committee.                                                          |
|                                      |                                                                                                                                                         |
| Provider                             | Any practitioner who is responsible for some portion of the care of the patient.                                                                        |
|                                      |                                                                                                                                                         |
| QM                                   | Quality Management                                                                                                                                      |
|                                      |                                                                                                                                                         |
| Queue                                | The process by which computer programs are scheduled to run at specific times.                                                                          |
|                                      |                                                                                                                                                         |
| Reopen                               | In the event that an occurrence is closed or deleted prematurely or in error, this function will reopen it for review.                                  |
|                                      |                                                                                                                                                         |
| Resident/provider                    | Any practitioner considered in "resident" status by the facility and is responsible for the care of the patient involved in an occurrence.              |
|                                      |                                                                                                                                                         |
| Review level                         | A level in the review process. The levels used in Occurrence Screening are Clinical, Peer, Manager and Committee.                                       |
|                     |                                                                                                                                                                                                                                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     |                                                                                                                                                                                                                                                                                                               |
| RM                  | Risk Management                                                                                                                                                                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                                                               |
| Run dates           | The dates on which Auto Enrollment ran.                                                                                                                                                                                                                                                                       |
|                     |                                                                                                                                                                                                                                                                                                               |
| Second level review | As used in this documentation, second level review refers to any Peer review for a practitioner related issue or any committee review for an equipment or system issue.                                                                                                                                       |
|                     |                                                                                                                                                                                                                                                                                                               |
| Severity of outcome | The actual or anticipated injury to the patient, ranging from no injury or disability to death.                                                                                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                                                               |
| Treating specialty  | The area of hospital treatment under which the occurrence happened.                                                                                                                                                                                                                                           |
|                     |                                                                                                                                                                                                                                                                                                               |
| Worksheet           | A computer-produced sheet containing an organized listing of data that a reviewer needs to enter into the computer. The reviewer can check off findings, actions, etc. It is intended both as a labor-saving device and a method of organizing data in the sequence in which the computer will request input. |

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Occurrence Screen menus have been restructured for V. 3.0. Below is a chart showing those menu/option names which have changed and their updated names.

Old Name New Name

Add or Change Data in Occurrence Screen Record Basic Occurrence Data

Delete Auto Enrollment Run Dates Auto Enrollment Run Dates Purge

Enter New Occurrence Manually Enter New Occurrence

Enter or Change Categories of Treating Specialties Treating Specialty Care Types

Enter or Change Clinical Reviewers Clinical Reviewers

Enter or Change Committees Committees

Enter or Change Medical Team Designations Medical Teams

Enter or Change Operational Parameters Site Parameters

Enter or Change Reasons for Clinical Referral Reasons for Clinical Referral

Enter or Change VAMC-Specific Screens VAMC-Specific Screens

Generate Early Warning System Bulletin Early Warning System Bulletin

Inquire/View Occurrence Screen Record Inquire Occurrence Screen Record

Occurrence Screening Occurrence Screen Manager Menu

Print/Report Menu Reports Menu

Reopen Closed/Deleted Occurrence Screen Record Open Closed/Deleted Occurrence Screen Record

Review: Clinical, Peer, Manager Clinical, Peer, Manager Review

Review: Committee Committee Review

Reviewer Worksheets Worksheets