---
title: Occurrence Screen Version 3 Release Notes Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes
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
description: - [# Release Notes](#release-notes) - [Auto Enroll Changes](#auto-enroll-changes) - [Report Changes](#report-changes) - [Edit Changes](#edit-changes) - [Miscellaneous Changes](#miscellaneous-changes) - [Menu/Option Name Changes](#menuoption-name-changes) - [# Installation Guide](#installation-guide)
audience: 
keywords: 
  - filed
  - occurrence
  - referral
  - code
  - reason
  - review
  - clinical
  - qaos
  - reviewer
  - installation
page_count: 0
word_count: 4730
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/9/09
revision_oldest: 3/9/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocigrn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/ocigrn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=49"
---

![](occurrence-screen-version-3-release-notes-installation-guide/001.png)

Occurrence Screen V. 3.0Release Notes & Installation GuideSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/9/09

|          |                                       |                     |                      |
|----------|---------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
| 3/9/09   | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# # Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Release Notes](#release-notes)
  - [Auto Enroll Changes](#auto-enroll-changes)
  - [Report Changes](#report-changes)
  - [Edit Changes](#edit-changes)
  - [Miscellaneous Changes](#miscellaneous-changes)
  - [Menu/Option Name Changes](#menuoption-name-changes)
- [# Installation Guide](#installation-guide)
  - [Installation Check List](#installation-check-list)
  - [Installation Example](#installation-example)
  - [Resource Requirements](#resource-requirements)

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

## Menu/Option Name Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old NameNew Name

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

# # Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package was developed under and requires Kernel V. 7.0, FileMan V. 19.0, and MAS V. 5.0 or later. The global ^QA should be journaled and backed up. Journaling should be suspended during the installation.

Please ensure that all QA end users are off the system, other users may remain on. It is recommended that the initialization be done at a time of low activity.

> **NOTE:** Do not delete any of the QAQ\* routines prior to loading this package. A pre-init routine will take care of loading and/or deleting the appropriate QAQ routines.

## Installation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 1\. Load the QAO\*, QAM\*, QAQ\*, and QAI\* routines into the account where the ^QA global resides, or where you want it to reside. If ^QA does not exist, please place it by using the GLOMAN (DSM), %GCH (MSM), or GCREATE (ISM) utility.
- 2\. Initialize the package by running the Occurrence Screen installation routine.

> D ^QAOINST

> The install routine will update the QA Integration Module based upon the version you are running, if any. Clinical Monitoring System V1.0 then Occurrence Screen V3.0 will be initialized. See Installation Example.

- 3\. With the assistance of the QM Coordinator and using the Package Setup Menu option, populate the site-specific files as described in the Package Operation section of the Occurrence Screen User Manual. At a minimum, the Site Parameters and Treating Specialties options must be exercised for the auto-enrollment functionality to work properly. The Clinical Monitoring System Site Parameters Edit option should also be utilized and the fields populated. The easiest method of entering all the site parameters is to use the Combined Site Parameters Edit option \[QAQ SITE PARAMETERS\] in the QM Manager Menu \[QAQ MANAGER\].
- 4\. Using the Task Manager option "Schedule/Unschedule Options", please queue the automatic enrollment option "QAM TASKED AUTO ENROLL RUN" to run daily after midnight. Do not select a printer device within TaskMan. Define the device for output by using the Manager menu option "Site Parameters". "QAM TASKED AUTO ENROLL RUN" calls the Clinical Monitoring System to gather data from the previous day's activities.
- 5\. Ascertain that the QM users have their terminals and printers in place and functional.
- 6\. With the assistance of the QM Coordinator, assign the menus to users. The Occurrence Screen Manager menu is usually given to the QM ADPAC and at least one other person to cover time of leave and so that at least two people are trained in its use.
- 7\. The following routines are no longer being used and may be deleted: QAOI\*, QAOSA0\*, QAOSA1\*, QAOSAGIN, QAOSAPRT, QAOSAUT\*, QAOSCNV\*, QAOSPQC0, QAOT\*.
- 8\. The following options are no longer being used and may be deleted: QAOS TASKED AUTO ENROLL, QAOS VALIDATE.

## Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

D ^QAOINST

Beginning installation of Occurrence Screen Version 3.0.

You are running Version \#.# of the QA Integration Module. NOTE: Yourversion

I have to update the QA Integration Module to version 1.5 number mayvary.

This version (#1.5) of 'QAQINIT' was created on 15-JUN-1993

(at Hines ISC, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

740 QUALITY ASSURANCE SITE PARAMETERS

> **NOTE:** You already have the 'QUALITY ASSURANCE SITE PARAMETERS' File.

740.1 AD HOC MACRO

> **NOTE:** You already have the 'AD HOC MACRO' File.

740.5 QA AUDIT

> **NOTE:** You already have the 'QA AUDIT' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Install/Clean-up QM Integration Module routines.

Installation Example

Loading QAIADLAU Replacing QAQADLAU Deleting QAIADLAU

Loading QAIAHOC0 Replacing QAQAHOC0 Deleting QAIAHOC0

Loading QAIAHOC1 Replacing QAQAHOC1 Deleting QAIAHOC1

Loading QAIAHOC2 Replacing QAQAHOC2 Deleting QAIAHOC2

Loading QAIAHOC3 Replacing QAQAHOC3 Deleting QAIAHOC3

Loading QAIAHOC4 Replacing QAQAHOC4 Deleting QAIAHOC4

Loading QAIAHOCH Replacing QAQAHOCH Deleting QAIAHOCH

Loading QAIAHOCX Replacing QAQAHOCX Deleting QAIAHOCX

Loading QAIAHOCY Replacing QAQAHOCY Deleting QAIAHOCY

Loading QAIAHOCZ Replacing QAQAHOCZ Deleting QAIAHOCZ

Loading QAIAPGRP Replacing QAQAPGRP Deleting QAIAPGRP

Loading QAIAUDIT Replacing QAQAUDIT Deleting QAIAUDIT

Loading QAIAUTL Replacing QAQAUTL Deleting QAIAUTL

Loading QAIAXREF Replacing QAQAXREF Deleting QAIAXREF

Loading QAIDATE Replacing QAQDATE Deleting QAIDATE

Loading QAINTEG Replacing QAQNTEG Deleting QAINTEG

Loading QAIPKGVR Replacing QAQPKGVR Deleting QAIPKGVR

Loading QAISELCT Replacing QAQSELCT Deleting QAISELCT

Loading QAISITE Replacing QAQSITE Deleting QAISITE

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...............................

'QAQ MANAGER' Option Filed

'QAQ PACKAGES INQUIRE' Option Filed

'QAQ SITE PARAMETERS' Option Filed

'QAQ USER' Option Filed.......

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

Converting the Ad Hoc Macro file (#740.1)

-----------------------------------------

You are running Version 1.5V1 of the QA Integration Module.

Now installing Occurrence Screen Version 3.0.

This version (#1.0V1) of 'QAMINIT' was created on 15-JUN-1993

(at Hines ISC, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

743 QA MONITOR (including data)

I will OVERWRITE your data with mine.

743.1 FALL OUT

743.2 MONITOR HISTORY

743.3 CONDITION (including data)

I will OVERWRITE your data with mine.

743.4 DATA ELEMENT (including data)

I will OVERWRITE your data with mine.

743.5 GROUP

Installation Example

743.6 AUTO ENROLL RUN DATE

743.91 RATIONALE (including data)

I will OVERWRITE your data with mine.

743.92 TIME FRAME (including data)

I will OVERWRITE your data with mine.

> **NOTE:** This package also contains BULLETINS

> **NOTE:** This package also contains FUNCTIONS

> **NOTE:** This package also contains OPTIONS

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...SORRY, I'M WORKING AS FAST AS I CAN........................................

.........................................................................

'QAM MONITOR TOOL 1' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'QAM MONITOR TOOL 2' BULLETIN FILED -- Remember to add mail groups for new bulletins........................................

'QAM BUILD MONITOR EDIT' Option Filed

'QAM BUILD MONITOR MENU' Option Filed

'QAM BUILD PATIENT GROUP' Option Filed

'QAM COPY MONITOR EDIT' Option Filed

'QAM FALL OUT EDIT' Option Filed

'QAM GROUP FILE EDIT' Option Filed

'QAM INQ AUDIT FILE' Option Filed

'QAM INQ CONDITION FILE' Option Filed

'QAM INQ DATA ELEMENT FILE' Option Filed

'QAM INQ FALL OUT FILE' Option Filed

'QAM INQ GROUP FILE' Option Filed

'QAM MANAGER MENU' Option Filed

'QAM MANAGER REPORTS MENU' Option Filed

'QAM MANUAL AUTO ENROLL RUN' Option Filed

'QAM PGMR APP GROUP EDIT' Option Filed

'QAM PGMR CONDITIONS EDIT' Option Filed

'QAM PGMR DATA ELEMENTS EDIT' Option Filed

'QAM PGMR MENU' Option Filed

'QAM PGMR MONITOR EDIT' Option Filed

'QAM PGMR TIME FRAME EDIT' Option Filed

'QAM PURGE AUTO RUN DATES FILE' Option Filed

'QAM PURGE FALL OUT FILE' Option Filed

'QAM PURGE HISTORY FILE' Option Filed

'QAM PURGE MENU' Option Filed

'QAM QUICK MONITOR EDIT' Option Filed

'QAM RATIONALE FILE EDIT' Option Filed

'QAM RPT ADHOC' Option Filed

Installation Example

'QAM RPT AUTO/MAN MONITORS RUN' Option Filed

'QAM RPT BUILD MON WORKSHEET' Option Filed

'QAM RPT MONITOR ADHOC' Option Filed

'QAM RPT MONITOR DESCRIPTION' Option Filed

'QAM RPT MONITOR HISTORY' Option Filed

'QAM RPT MULTIPLE FALL OUTS' Option Filed

'QAM SAMPLE SIZE EDIT' Option Filed

'QAM SITE PARAMETERS EDIT' Option Filed

'QAM TASKED AUTO ENROLL RUN' Option Filed

'QAM USER MENU' Option Filed

'QAM USER REPORTS MENU' Option Filed.

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

Do you want to load the ICD Diagnosis/Procedure groups now? NO// (NO)

This version (#3.0) of 'QAOINIT' was created on 15-JUN-1993

(at Hines ISC, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

741 QA OCCURRENCE SCREEN

> **NOTE:** You already have the 'QA OCCURRENCE SCREEN' File.

741.1 QA OCCURRENCE SCREEN CRITERIA (including data)

> **NOTE:** You already have the 'QA OCCURRENCE SCREEN CRITERIA' File.

Want my data to overwrite yours? YES

741.2 QA OCCURRENCE REVIEW LEVEL (including data)

> **NOTE:** You already have the 'QA OCCURRENCE REVIEW LEVEL' File.

Want my data to overwrite yours? YES

741.3 \*QA OCCURRENCE CLINICAL REVIEWER

\*BUT YOU ALREADY HAVE 'QA OCCURRENCE CLINICAL REVIEWER' AS FILE \#741.3!

Shall I change the NAME of the file to \*QA OCCURRENCE CLINICAL REVIEWER? NO// YES

741.3 \*QA OCCURRENCE CLINICAL REVIEWER

> **NOTE:** You already have the '\*QA OCCURRENCE CLINICAL REVIEWER' File.

741.4 QA OCCURRENCE CLINICAL REFERRAL (including data)

> **NOTE:** You already have the 'QA OCCURRENCE CLINICAL REFERRAL' File.

Want my data to overwrite yours? NO// YES

741.5 QA OCCURRENCE EXCEPTION (including data)

> **NOTE:** You already have the 'QA OCCURRENCE EXCEPTION' File.

Want my data to overwrite yours? NO// YES

741.6 QA OCCURRENCE FINDINGS (including data)

> **NOTE:** You already have the 'QA OCCURRENCE FINDINGS' File.

Want my data to overwrite yours? NO// YES

Installation Example

741.7 QA OCCURRENCE ACTION (including data)

> **NOTE:** You already have the 'QA OCCURRENCE ACTION' File.

Want my data to overwrite yours? NO// YES

741.8 QA OCCURRENCE SEVERITY OF OUTCOME (including data)

> **NOTE:** You already have the 'QA OCCURRENCE SEVERITY OF OUTCOME' File.

Want my data to overwrite yours? NO// YES

741.9 QA OCCURRENCE TREATING SPECIALTY

> **NOTE:** You already have the 'QA OCCURRENCE TREATING SPECIALTY' File.

741.93 QA OCCURRENCE MEDICAL TEAM

> **NOTE:** You already have the 'QA OCCURRENCE MEDICAL TEAM' File.

741.95 \*QA OCCURRENCE NUMBER CASES SCREENED

> **NOTE:** You already have the '\*QA OCCURRENCE NUMBER CASES SCREENED' File.

741.97 QA OCCURRENCE COMMITTEE

> **NOTE:** You already have the 'QA OCCURRENCE COMMITTEE' File.

741.99 QA OCCURRENCE AUTO RUN DATES

> **NOTE:** You already have the 'QA OCCURRENCE AUTO RUN DATES' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Delete version 1.01 Occurrence Screen files/fields

--------------------------------------------------

The following files are about to be deleted:

513.73 \*ACTION

513.74 \*REVIEW LEVEL

513.75 \*OCCURRENCE SCREEN CRITERIA

513.76 \*QA MONITORS

513.77 \*QA SPECIAL/ACUTE BEDSECTION

513.78 \*CLINICAL REVIEWER

513.79 \*CLINICAL REVIEW FINDINGS

Installation Example

The following fields in the PATIENT QA EVENT file (#513.72)

are about to be deleted:

9 \*TREATING SPECIALTY

10 \*PRIMARY PHYSICIAN

12 \*PROVIDER

13 \*SCREEN

14 \*MONITOR

15.5 \*OCCURRENCE AND INCIDENT

30 \*CLINICAL REVIEWER

31 \*CLINICAL REVIEWER

32 \*CLINICAL REVIEW DATE

32.5 \*PRIMARY REASON CLIN REFERRAL

33 \*CLINICAL REVIEW FINDINGS

33.5 \*CAUSE OF EXCEPTION

34 \*CLINICAL REVIEW ACTION

35 \*PEER REVIEWER NAME (Mult)

42 \*SERVICE CHIEF REVIEW

43 \*SERVICE CHIEF REVIEWER

44 \*SERVICE CHIEF REVIEWER \#2

45 \*DATE SENT TO SRV CHIEF REVIEW

46 \*SERVICE CHIEF REVIEW DATE COM

48 \*SERVICE CHIEF REVIEW ACTION

49 \*SERVICE CHIEF REVIEW REMARKS

52 \*FINAL DISP. REACHED BY

53 \*CRITERION (Mult)

71 \*FNUMDAYS

73 \*TNUMDAYS

74 \*ATTRIBUTION (INDIVIDUALS) (Mult)

74.5 \*ATTRIBUTION (HOSP LOCATION) (Mult)

Are you sure you want to continue? NO// ?

Answer Y(es) to delete the items displayed,

and continue with the installation.

Answering N(o) will leave the files untouched

and abort the installation.

The following files are about to be deleted:

513.73 \*ACTION

513.74 \*REVIEW LEVEL

513.75 \*OCCURRENCE SCREEN CRITERIA

513.76 \*QA MONITORS

513.77 \*QA SPECIAL/ACUTE BEDSECTION

513.78 \*CLINICAL REVIEWER

513.79 \*CLINICAL REVIEW FINDINGS

Installation Example

The following fields in the PATIENT QA EVENT file (#513.72)

are about to be deleted:

9 \*TREATING SPECIALTY

10 \*PRIMARY PHYSICIAN

12 \*PROVIDER

13 \*SCREEN

14 \*MONITOR

15.5 \*OCCURRENCE AND INCIDENT

30 \*CLINICAL REVIEWER

31 \*CLINICAL REVIEWER

32 \*CLINICAL REVIEW DATE

32.5 \*PRIMARY REASON CLIN REFERRAL

33 \*CLINICAL REVIEW FINDINGS

33.5 \*CAUSE OF EXCEPTION

34 \*CLINICAL REVIEW ACTION

35 \*PEER REVIEWER NAME (Mult)

42 \*SERVICE CHIEF REVIEW

43 \*SERVICE CHIEF REVIEWER

44 \*SERVICE CHIEF REVIEWER \#2

45 \*DATE SENT TO SRV CHIEF REVIEW

46 \*SERVICE CHIEF REVIEW DATE COM

48 \*SERVICE CHIEF REVIEW ACTION

49 \*SERVICE CHIEF REVIEW REMARKS

52 \*FINAL DISP. REACHED BY

53 \*CRITERION (Mult)

71 \*FNUMDAYS

73 \*TNUMDAYS

74 \*ATTRIBUTION (INDIVIDUALS) (Mult)

74.5 \*ATTRIBUTION (HOSP LOCATION) (Mult)

Are you sure you want to continue? NO// Y (YES)

Deleting files:

513.73 \*ACTION

513.74 \*REVIEW LEVEL

513.75 \*OCCURRENCE SCREEN CRITERIA

513.76 \*QA MONITORS

513.77 \*QA SPECIAL/ACUTE BEDSECTION

513.78 \*CLINICAL REVIEWER

513.79 \*CLINICAL REVIEW FINDINGS

Installation Example

Deleting fields in the PATIENT QA EVENT file (#513.72):

9 \*TREATING SPECIALTY

10 \*PRIMARY PHYSICIAN

12 \*PROVIDER

13 \*SCREEN

14 \*MONITOR

15.5 \*OCCURRENCE AND INCIDENT

30 \*CLINICAL REVIEWER

31 \*CLINICAL REVIEWER

32 \*CLINICAL REVIEW DATE

32.5 \*PRIMARY REASON CLIN REFERRAL

33 \*CLINICAL REVIEW FINDINGS

33.5 \*CAUSE OF EXCEPTION

34 \*CLINICAL REVIEW ACTION

35 \*PEER REVIEWER NAME (Mult)

42 \*SERVICE CHIEF REVIEW

43 \*SERVICE CHIEF REVIEWER

44 \*SERVICE CHIEF REVIEWER \#2

45 \*DATE SENT TO SRV CHIEF REVIEW

46 \*SERVICE CHIEF REVIEW DATE COM

48 \*SERVICE CHIEF REVIEW ACTION

49 \*SERVICE CHIEF REVIEW REMARKS

52 \*FINAL DISP. REACHED BY

53 \*CRITERION (Mult)

71 \*FNUMDAYS

73 \*TNUMDAYS

74 \*ATTRIBUTION (INDIVIDUALS) (Mult)

74.5 \*ATTRIBUTION (HOSP LOCATION) (Mult)

Delete OS/2.5 temporary conversion fields from file \#740

--------------------------------------------------------

Field: 741.97 - \*SCREEN FILE CONVERSION DATE

Field: 741.98 - \*SEVERITY CONVERSION DATE

Kill the 'AC', 'AF' and 'AE' cross references in file \#741 NOTE: None

---------------------------------------------------------- of thesecross-

Xref: 'AC' killed references

Xref: 'AF' killed are used

Xref: 'AE' killed in OS 3.0.

Convert screen 107 to return to O.R. within 7 days

--------------------------------------------------

UNPLANNED RETURN TO OR IN SAME ADMISSION, OR WITHIN 7 DAYS OF OPERATION

Cleaning up OPTION and FIELD descriptions

-----------------------------------------

Working........

Installation Example

Converting severity level numbers from 1-4 to 0-3

-------------------------------------------------

1 =\> 0 - NO INJURY OR DISABILITY

2 =\> 1 - MINOR

3 =\> 2 - MAJOR

4 =\> 3 - DEATH

Converting text of findings

---------------------------

Changing finding number: 1

From: OPTIMAL CARE

To: UCR - USUAL CUSTOMARY & REASONABLE

Converting text of exceptions

-----------------------------

Screen: 107 Code: 2

From: TWO OPERATIONS SEPARATED BY MORE THAN 60 DAYS

To: TWO OPERATIONS SEPARATED BY MORE THAN 7 DAYS

Converting text of reasons for referral NOTE: Your

--------------------------------------- "Old text"may vary.

Screen: 101.1

Reason for referral code ==\> Old: 10 New: 99

Old text: OTHER

New text: OTHER

Screen: 101.1

Reason for referral code ==\> Old: ?? New: 10

Old text:

New text: PATIENT NON-COMPLIANCE

Screen: 101.1

Reason for referral code ==\> Old: 9 New: 9

Old text: DRUG TOXICITY

New text: DECUBITI DEHYDRATION OR DRUG TOXICITY

Screen: 101.1

Reason for referral code ==\> Old: 8 New: 8

Old text: FAILURE OF CONTINUING TREATMENT DURING OUTPATIENT PERIOD

New text: FAILURE OF CONTINUING TREATMENT DURING OUTPATIENT PERIOD

Screen: 101.1

Reason for referral code ==\> Old: 7 New: 7

Old text: UNEXPECTED RECURRENCE OF PRESUMABLY CURED DISEASE

New text: UNEXPECTED EXACERBATION OF ILLNESS

Installation Example

Screen: 101.1

Reason for referral code ==\> Old: 6 New: 6

Old text: PATIENT EDUCATION

New text: PATIENT EDUCATION

Screen: 101.1

Reason for referral code ==\> Old: 5 New: 5

Old text: DISCHARGE ORDERS

New text: DISCHARGE ORDERS

Screen: 101.1

Reason for referral code ==\> Old: 4 New: 4

Old text: PRE-EXISTENT UNDIAGNOSED CONDITION

New text: PRE-EXISTENT UNDIAGNOSED CONDITION

Screen: 101.1

Reason for referral code ==\> Old: 3 New: 3

Old text: TIMELINESS OF DISCHARGE

New text: TIMELINESS OF DISCHARGE

Screen: 101.1

Reason for referral code ==\> Old: 2 New: 2

Old text: DISCHARGE PLANS MADE DURING PREVIOUS HOSPITALIZATION

New text: DISCHARGE PLANS MADE DURING PREVIOUS HOSPITALIZATION

Screen: 101.1

Reason for referral code ==\> Old: 1 New: 1

Old text: COMPLICATION OF TREATMENT DURING PRIOR HOSPITALIZATION

New text: COMPLICATION OF TREATMENT DURING PRIOR HOSPITALIZATION

Screen: 102

Reason for referral code ==\> Old: 5 New: 99

Old text: OTHER

New text: OTHER

Screen: 102

Reason for referral code ==\> Old: 2 New: 2

Old text: OUTPATIENT DRUG THERAPY

New text: OUTPATIENT DRUG THERAPY

Installation Example

Screen: 102

Reason for referral code ==\> Old: 3 New: 3

Old text: FOLLOWED TWO OR MORE OUTPATIENT VISITS FOR SAME ACUTE CONDITION

New text: FOLLOWED TWO OR MORE OUTPATIENT VISITS FOR SAME ACUTE CONDITION

Screen: 102

Reason for referral code ==\> Old: 4 New: 4

Old text: ESCALATION OF CARE INAPPROPRIATELY DELAYED

New text: ESCALATION OF CARE INAPPROPRIATELY DELAYED

Screen: 102

Reason for referral code ==\> Old: ?? New: 1K

Old text:

New text: OUTPATIENT MANAGEMENT ISSUE: NON-COMPLIANCE AND FAILURE TO OBTAIN PRESCRIBED MEDICATIONS

Screen: 102

Reason for referral code ==\> Old: 1I New: 1J

Old text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF FINANCIAL OR SOCIAL SUPPORT SYSTEM PROBLEMS

New text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF FINANCIAL OR SOCIAL SUPPORT PROBLEMS

Screen: 102

Reason for referral code ==\> Old: 1H New: 1H

Old text: OUTPATIENT MANAGEMENT ISSUE: COMPLICATION OF OUTPATIENT PROCEDURE

New text: OUTPATIENT MANAGEMENT ISSUE: COMPLICATION OF OUTPATIENT PROCEDURE

Screen: 102

Reason for referral code ==\> Old: 1G New: 1G

Old text: OUTPATIENT MANAGEMENT ISSUE: RESPONSE TO CONSULTATION FINDINGS

New text: OUTPATIENT MANAGEMENT ISSUE: RESPONSE TO CONSULTATION FINDINGS

Screen: 102

Reason for referral code ==\> Old: 1F New: 1I

Old text: OUTPATIENT MANAGEMENT ISSUE: PATIENT EDUCATION

New text: OUTPATIENT MANAGEMENT ISSUE: PATIENT EDUCATION

Screen: 102

Reason for referral code ==\> Old: ?? New: 1F

Old text:

New text: OUTPATIENT MANAGEMENT ISSUE: USE OF CONSULTS

Installation Example

Screen: 102

Reason for referral code ==\> Old: 1E New: 1E

Old text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF ABNORMAL DIAGNOSTIC TEST RESULTS

New text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF ABNORMAL DIAGNOSTIC TEST RESULTS

Screen: 102

Reason for referral code ==\> Old: 1D New: 1D

Old text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF PATIENT'S SYMPTOMS/COMPLAINTS

New text: OUTPATIENT MANAGEMENT ISSUE: FOLLOW-UP OF PATIENT'S SYMPTOMS/COMPLAINTS

Screen: 102

Reason for referral code ==\> Old: 1C New: 1C

Old text: OUTPATIENT MANAGEMENT ISSUE: COMPLETENESS OF PHYSICAL EXAM

New text: OUTPATIENT MANAGEMENT ISSUE: COMPLETENESS OF PHYSICAL EXAM

Screen: 102

Reason for referral code ==\> Old: 1B New: 1B

Old text: OUTPATIENT MANAGEMENT ISSUE: ADDRESSING OF ABNORMAL VITAL SIGNS

New text: OUTPATIENT MANAGEMENT ISSUE: ADDRESSING OF ABNORMAL VITAL SIGNS

Screen: 102

Reason for referral code ==\> Old: 1A New: 1A

Old text: OUTPATIENT MANAGEMENT ISSUE: DENIAL OF CARE

New text: OUTPATIENT MANAGEMENT ISSUE: DENIAL OF CARE

Screen: 107

Reason for referral code ==\> Old: 5 New: 99

Old text: OTHER

New text: OTHER

Screen: 107

Reason for referral code ==\> Old: 4 New: 4

Old text: EQUIPMENT MALFUNCTION

New text: EQUIPMENT MALFUNCTION

Screen: 107

Reason for referral code ==\> Old: 3 New: 3

Old text: REMOVAL OF FOREIGN BODY

New text: REMOVAL OF FOREIGN BODY

Screen: 107

Reason for referral code ==\> Old: 2 New: 2

Old text: INITIAL PROCEDURE UNSUCCESSFUL

New text: INITIAL PROCEDURE UNSUCCESSFUL

Installation Example

Screen: 107

Reason for referral code ==\> Old: 1 New: 1

Old text: COMPLICATIONS FROM FIRST PROCEDURE

New text: COMPLICATIONS FROM FIRST PROCEDURE

Screen: 109

Reason for referral code ==\> Old: 15 New: 99

Old text: OTHER

New text: OTHER

Screen: 109

Reason for referral code ==\> Old: 14 New: 16

Old text: MAY HAVE BEEN PREVENTABLE

New text: MAY HAVE BEEN PREVENTABLE

Screen: 109

Reason for referral code ==\> Old: 13 New: 15

Old text: EQUIPMENT MALFUNCTION

New text: EQUIPMENT MALFUNCTION

Screen: 109

Reason for referral code ==\> Old: 12 New: 14

Old text: MEDICATION ERROR OR CHOICE OF MEDICATION

New text: MEDICATION ERROR OR CHOICE OF MEDICATION

Screen: 109

Reason for referral code ==\> Old: 11 New: 13

Old text: COMPLICATION OF ELECTIVE PROCEDURE

New text: COMPLICATION OF ELECTIVE PROCEDURE

Screen: 109

Reason for referral code ==\> Old: 10 New: 12

Old text: DURING OR WITHIN 72 HOURS OF ELECTIVE PROCEDURE

New text: DURING OR WITHIN 72 HOURS OF ELECTIVE PROCEDURE

Screen: 109

Reason for referral code ==\> Old: 9 New: 11

Old text: WITHIN 72 HOURS OF TRANSFER OUT OF SPECIAL CARE UNIT

New text: WITHIN 72 HOURS OF TRANSFER OUT OF SPECIAL CARE UNIT

Screen: 109

Reason for referral code ==\> Old: 8 New: 10

Old text: WITHIN 24 HOURS OF ADMISSION

New text: WITHIN 24 HOURS OF ADMISSION

Screen: 109

Reason for referral code ==\> Old: 7 New: 9

Old text: HOSPITAL INCURRED INCIDENT OR COMPLICATION OF TREATMENT

New text: HOSPITAL INCURRED INCIDENT OR COMPLICATION OF TREATMENT

Installation Example

Screen: 109

Reason for referral code ==\> Old: 6 New: 8

Old text: LACK OF DOCUMENTATION INDICATING PATIENT'S DEATH EXPECTED

New text: LACK OF DOCUMENTATION INDICATING PATIENT'S DEATH EXPECTED

Screen: 109

Reason for referral code ==\> Old: ?? New: 7

Old text:

New text: LACK OF DOCUMENTATION INDICATING EXPLANATION FOR DEATH

Screen: 109

Reason for referral code ==\> Old: 5 New: 6

Old text: FAILURE TO CARRY OUT ORDERS

New text: FAILURE TO CARRY OUT ORDERS

Screen: 109

Reason for referral code ==\> Old: 4 New: 5

Old text: SIGNS OF DETERIORATING CONDITION UNNOTED AND/OR UNREPORTED

New text: SIGNS OF DETERIORATING CONDITION UNNOTED AND/OR UNREPORTED

Screen: 109

Reason for referral code ==\> Old: 3 New: 4

Old text: LACK OF CONCORDANCE BETWEEN PREMORTEM AND POSTMORTEM DIAGNOSES

New text: LACK OF CONCORDANCE BETWEEN PREMORTEM AND POSTMORTEM DIAGNOSES

Screen: 109

Reason for referral code ==\> Old: ?? New: 3

Old text:

New text: AVOIDABLE CARDIAC OR PULMONARY ARREST

Screen: 109

Reason for referral code ==\> Old: 2 New: 2

Old text: CHANGE IN CONDITION WITH NO ACTION TAKEN

New text: CHANGE IN CONDITION WITH NO ACTION TAKEN

Screen: 109

Reason for referral code ==\> Old: 1 New: 1

Old text: LACK OF DOCUMENTATION OF PATIENT'S DETERIORATION

New text: LACK OF DOCUMENTATION OF PATIENT'S DETERIORATION

Installation Example

...SORRY, JUST A MOMENT PLEASE................................................

............................................................................................................

'QAOS AUDIT INQUIRY' Option Filed

'QAOS C/P/M REVIEW' Option Filed

'QAOS COMMITTEE REVIEW' Option Filed

'QAOS DELETE' Option Filed

'QAOS DELETE AUTO RUN DATES' Option Filed

'QAOS EDIT CLIN REVIEWER' Option Filed

'QAOS EDIT COMMITTEE' Option Filed

'QAOS EDIT MEDICAL TEAM' Option Filed

'QAOS EDIT OCCURRENCE' Option Filed

'QAOS EDIT REASONS CLIN REFER' Option Filed

'QAOS EDIT SCREEN' Option Filed

'QAOS ENTER OCCURRENCE' Option Filed

'QAOS FINAL DISPOSITION' Option Filed

'QAOS GENERATE EWS BULLETIN' Option Filed

'QAOS GENERATE SUMM OS BULLETIN' Option Filed

'QAOS MAIN MENU' Option Filed

'QAOS MANAGER MENU' Option Filed

'QAOS MANUAL AUTO ENROLL' Option Filed

'QAOS MGR EDIT MENU' Option Filed

'QAOS MGR REPORTS MENU' Option Filed

'QAOS PARAMETERS ENTER/EDIT' Option Filed

'QAOS PATIENT INQUIRY' Option Filed

'QAOS PURGE DEL MENU' Option Filed

'QAOS PURGE DELETED RECORDS' Option Filed

'QAOS QUICK EXCEPTION EDIT' Option Filed

'QAOS REOPEN' Option Filed

'QAOS REPORT MENU' Option Filed

'QAOS RPT AD HOC' Option Filed

'QAOS RPT ADVERSE FINDINGS' Option Filed

'QAOS RPT AWAITING CLIN REV' Option Filed

'QAOS RPT BY SERVICE' Option Filed

'QAOS RPT DELINQUENT REVIEWS' Option Filed

'QAOS RPT ENROLL DATES TALLY' Option Filed

'QAOS RPT PRACTITIONER NAME' Option Filed

'QAOS RPT RELIABILITY ASSMT' Option Filed

'QAOS RPT REVIEW LEVEL TRACKING' Option Filed

'QAOS RPT REVIEW SUMMARY' Option Filed

'QAOS RPT SEMI ANNUAL' Option Filed

'QAOS RPT SERVICE STATS' Option Filed

'QAOS RPT SYS/MGMT/EQUIP PROB' Option Filed

'QAOS RPT TXSP CARE TYPE' Option Filed

'QAOS RPT WORKSHEETS' Option Filed

'QAOS TASKED EWS' Option Filed

'QAOS TXSP' Option Filed

'QAOS USER MENU' Option Filed....

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

Installation Example

Load ASSOCIATED ADMISSION field,

convert COMMENTS to word processing

and, index the 'E' cross reference

-----------------------------------

The associated admission dates will now be calculated for all

Occurrence Screen records. The data is saved in the ASSOCIATED

ADMISSION field (741,.02). Depending on the number of

occurrences, this could take quite a while.

Also, the data in the COMMENTS fields in the REVIEWER and

COMMITTEE multiples (741.01,7 & 741.017,3) is copied to the

new word processing COMMENTS fields (741.01,10 & 741.017,10).

The old free text comments are deleted as they are converted.

The 'E' cross reference on the OCCURRENCE IDENTIFIER field

(#741,2) will also be created.

Working..............

Allocating the QAOSCLIN security key to the persons in the

QA OCCURRENCE SCREEN CLINICAL REVIEWER file (#741.3)

----------------------------------------------------------

Allocating key:

CLINICAL,REVIEWER ONE

CLINICAL,REVIEWER TWO

CLINICAL,REVIEWER THREE

Deallocating key:

\*\*\* None \*\*\*

Creating the QM User and Manager Menus...............

Installation of Occurrence Screen Version 3.0 complete!

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRTs

At least one CRT for the use of the QM Coordinator and more if required for the QM staff.

Printers

At least one dedicated for QM use. It is preferable to route the report of the daily Auto Enrollment running to this printer, if at all possible. The printer needs to be available at all times for producing reports and worksheets. It is preferable that the printer be a laser printer.

CPU Capacity

The daily interactive use of the package uses only a small amount of the total CPU capacity. The nightly run of the auto enroll routines is more intensive, but this process should be queued to run at a time of low CPU activity.

Disk Capacity:

(Number of records in File \#741 \* 6K) + 100K