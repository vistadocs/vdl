---
title: VIST Version 4 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: ANRV
app_name: Visual Impairment Service Team (VIST)
section: CLI
app_status: active
pkg_ns: ANRV
patch_ver: 4
patch_id: ANRV*4
group_key: "ANRV:ANRV:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vist
  - table
  - contents
  - roster
  - review
  - patient
  - letter
  - edit
  - print
  - date
page_count: 0
word_count: 8237
section_count: 18
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: June 1998
revision_count: 2
revision_newest: 9/23/04
revision_oldest: 3/14/03
docx_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=106"
---

![](vist-version-4-user-manual/001.png)

VISUAL IMPAIRMENT SERVICE TEAM(VIST)User Manual

June 1998

Office of the Chief Information Officer

Revision History

|          |                                                        |                                                                                                                       |                                                                                             |
|----------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Date | Revision                                           | Description                                                                                                       | Author                                                                                  |
| 6/1998   | Final Version 4.0                                      | VIST 4.0 User Manual                                                                                                  | Office of Chief Information Officer                                                         |
| 3/14/03  | Final Version 4.0 +ANRV \*4 \*5 Patch Version 4.0.5.1. | Addition of Appendix B: ANRV \*4\*5 Patch User Manual                                                                 | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| 9/23/04  | Final Version 4.0                                      | Replaced SS#s on pages 9, 20, 22, 23, 25, 29-36, 42, 43, 51, 63 (Edited a screen shot on page 63 and removed the SS#) | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

Table of Contents

Introduction [6](#introduction)

Icons [6](#icons)

Related Documentation [6](#related-documentation)

Visual Impairment Service Team (VIST) V. 4.0 Menu [7](#visual-impairment-service-team-vist-v.-4.0-menu)

Entering and Editing VIST Options [9](#entering-and-editing-vist-options)

*Edit VIST Options Menu* [9](#edit-vist-options-menu)

Enter/Edit VIST Patient Record [9](#enteredit-vist-patient-record)

Enter/Edit VIST Referral Roster [13](#enteredit-vist-referral-roster)

Enter/Edit Inactive VIST Roster [14](#enteredit-inactive-vist-roster)

Enter/Edit VARO Claims Roster [15](#enteredit-varo-claims-roster)

Enter/Edit VIST Benefits Checklist [16](#enteredit-vist-benefits-checklist)

Enter/Edit VIST Parameters [18](#enteredit-vist-parameters)

Delete VIST Referral Roster [19](#delete-vist-referral-roster)

Delete VIST Patient Record [19](#delete-vist-patient-record)

Printing Individual Records [20](#printing-individual-records)

*Print Individual Records* [20](#print-individual-records)

Individual Patient Record [20](#individual-patient-record)

Individual Referral Record [22](#individual-referral-record)

Individual Eye History [23](#individual-eye-history)

Individual Claims Record [24](#individual-claims-record)

Individual Annual Review Record [25](#individual-annual-review-record)

Individual VIST Benefits Checklist [26](#individual-vist-benefits-checklist)

Printing the VIST Roster [28](#printing-the-vist-roster)

*Print VIST Roster Menu* [28](#print-vist-roster-menu)

VIST Roster List [28](#vist-roster-list)

VIST Referral List [29](#vist-referral-list)

VIST Roster List with Annual Review Date [30](#vist-roster-list-with-annual-review-date)

VARO Claims List [31](#varo-claims-list)

Inpatient List [32](#inpatient-list)

Outpatient Appointment List [33](#outpatient-appointment-list)

Deceased Patients List [34](#deceased-patients-list)

Inactive VIST Roster List [34](#inactive-vist-roster-list)

Additions to VIST Roster [35](#additions-to-vist-roster)

Field Visit Date(s) List [36](#field-visit-dates-list)

VIST Roster Sorts… [37](#vist-roster-sorts)

State [37](#state)

City [37](#city)

ZIP [37](#zip)

County [37](#county)

Address/Phone List [37](#addressphone-list)

Birthdate [38](#birthdate)

Age [38](#age)

Eye Diagnosis [38](#eye-diagnosis)

Eye Diagnosis Narrative [38](#eye-diagnosis-narrative)

Fee Basis List [38](#fee-basis-list)

Period of Service [39](#period-of-service)

Referral Source List [39](#referral-source-list)

Annual Review Dates List [39](#annual-review-dates-list)

VIST Eligible (AMIS) List [39](#vist-eligible-amis-list)

AMIS Report [40](#amis-report)

Incomplete AMIS Roster [43](#incomplete-amis-roster)

Using the VIST Letter Menu [44](#using-the-vist-letter-menu)

*VIST Letter Menu* [44](#vist-letter-menu)

Edit VIST Letter [44](#edit-vist-letter)

Print VIST Letter [46](#print-vist-letter)

Test Label Alignment [46](#test-label-alignment)

Print Mailing Labels by Patient [46](#print-mailing-labels-by-patient)

Print Mailing Labels by City [46](#print-mailing-labels-by-city)

Print Mailing Labels by County [46](#print-mailing-labels-by-county)

Print Mailing Labels by State [47](#print-mailing-labels-by-state)

Glossary [48](#glossary)

Appendix A: VIST Letters [49](#appendix-a-vist-letters)

Example of a BRC Application Letter [49](#example-of-a-brc-application-letter)

Example of a BRC Follow-up Letter [50](#example-of-a-brc-follow-up-letter)

Example of a Claim Letter [50](#example-of-a-claim-letter)

Example of Invitation for VIST Review [52](#example-of-invitation-for-vist-review)

Example of an IRS Exemption Letter [53](#example-of-an-irs-exemption-letter)

Appendix B: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1) [54](#appendix-b-blind-rehabilitation-vist-patient-review-anrv-4.0.5.1)

Introduction to VIST Patient Review Software [54](#introduction-to-vist-patient-review-software)

Orientation of VIST Patient Review Controls [54](#orientation-of-vist-patient-review-controls)

Next\> Button [55](#next-button)

OK Button [55](#ok-button)

\<Back Button [56](#back-button)

Cancel Button [56](#cancel-button)

Exit Button [57](#exit-button)

Radio Buttons [58](#radio-buttons)

Drop Down Lists [58](#drop-down-lists)

Electronic Signatures [59](#electronic-signatures)

Review [59](#review)

Getting Started [61](#getting-started)

Logging into VIST [61](#logging-into-vist)

VIST Signon [61](#vist-signon)

Patient Selection [62](#patient-selection)

Selecting a Patient [62](#selecting-a-patient)

Confirming Patient Selection [63](#confirming-patient-selection)

Unrestricted Access Patient File [63](#unrestricted-access-patient-file)

Restricted Access Patient File [65](#restricted-access-patient-file)

Multiple Matches [67](#multiple-matches)

Actions [68](#actions)

Create a New Patient Review [69](#create-a-new-patient-review)

Rehabilitation Interview: [69](#rehabilitation-interview)

Annual Review: [69](#annual-review)

Review a Completed Patient Review [70](#review-a-completed-patient-review)

Selecting a Patient Review [71](#selecting-a-patient-review)

Selecting a Patient Review Section [72](#selecting-a-patient-review-section)

Patient Review Interviews [73](#patient-review-interviews)

Section Summaries [73](#section-summaries)

Answering Questions [73](#answering-questions)

Mouse: [74](#mouse)

Keyboard: [74](#keyboard)

Completing Sections / Interviews [76](#completing-sections-interviews)

Messages [77](#messages)

Index [81](#index)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Icons](#icons)
  - [Related Documentation](#related-documentation)
- [Visual Impairment Service Team (VIST) V. 4.0 Menu](#visual-impairment-service-team-vist-v-40-menu)
- [Entering and Editing VIST Options](#entering-and-editing-vist-options)
  - [Edit VIST Options Menu](#edit-vist-options-menu)
    - [Enter/Edit VIST Patient Record](#enteredit-vist-patient-record)
    - [Enter/Edit VIST Referral Roster](#enteredit-vist-referral-roster)
    - [Enter/Edit Inactive VIST Roster](#enteredit-inactive-vist-roster)
    - [Enter/Edit VARO Claims Roster](#enteredit-varo-claims-roster)
    - [Enter/Edit VIST Benefits Checklist](#enteredit-vist-benefits-checklist)
    - [Enter/Edit VIST Parameters](#enteredit-vist-parameters)
    - [Delete VIST Referral Roster](#delete-vist-referral-roster)
    - [Delete VIST Patient Record](#delete-vist-patient-record)
- [# Printing Individual Records](#printing-individual-records)
  - [Print Individual Records](#print-individual-records)
    - [Individual Patient Record](#individual-patient-record)
    - [Individual Referral Record](#individual-referral-record)
    - [Individual Eye History](#individual-eye-history)
    - [Individual Claims Record](#individual-claims-record)
    - [Individual Annual Review Record](#individual-annual-review-record)
    - [Individual VIST Benefits Checklist](#individual-vist-benefits-checklist)
- [# Printing the VIST Roster](#printing-the-vist-roster)
  - [Print VIST Roster Menu](#print-vist-roster-menu)
    - [VIST Roster List](#vist-roster-list)
    - [### VIST Referral List](#vist-referral-list)
    - [VIST Roster List with Annual Review Date](#vist-roster-list-with-annual-review-date)
    - [VARO Claims List](#varo-claims-list)
    - [Inpatient List](#inpatient-list)
    - [Outpatient Appointment List](#outpatient-appointment-list)
    - [Deceased Patients List](#deceased-patients-list)
    - [Inactive VIST Roster List](#inactive-vist-roster-list)
    - [Additions to VIST Roster](#additions-to-vist-roster)
    - [Field Visit Date(s) List](#field-visit-dates-list)
    - [VIST Roster Sorts…](#vist-roster-sorts)
    - [AMIS Report](#amis-report)
    - [Incomplete AMIS Roster](#incomplete-amis-roster)
- [# Using the VIST Letter Menu](#using-the-vist-letter-menu)
  - [VIST Letter Menu](#vist-letter-menu)
    - [Edit VIST Letter](#edit-vist-letter)
    - [Print VIST Letter](#print-vist-letter)
    - [Test Label Alignment](#test-label-alignment)
    - [Print Mailing Labels by Patient](#print-mailing-labels-by-patient)
    - [Print Mailing Labels by City](#print-mailing-labels-by-city)
    - [Print Mailing Labels by County](#print-mailing-labels-by-county)
    - [Print Mailing Labels by State](#print-mailing-labels-by-state)
- [Glossary](#glossary)
- [Appendix A: VIST Letters](#appendix-a-vist-letters)
  - [Example of a BRC Application Letter](#example-of-a-brc-application-letter)
  - [Example of a BRC Follow-up Letter](#example-of-a-brc-follow-up-letter)
  - [Example of a Claim Letter](#example-of-a-claim-letter)
  - [Example of Invitation for VIST Review](#example-of-invitation-for-vist-review)
  - [Example of an IRS Exemption Letter](#example-of-an-irs-exemption-letter)
- [Appendix B: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1)](#appendix-b-blind-rehabilitation-vist-patient-review-anrv-4051)
  - [Introduction to VIST Patient Review Software](#introduction-to-vist-patient-review-software)
  - [Orientation of VIST Patient Review Controls](#orientation-of-vist-patient-review-controls)
    - [Next\> Button](#next-button)
    - [OK Button](#ok-button)
    - [\<Back Button](#back-button)
    - [Cancel Button](#cancel-button)
    - [Exit Button](#exit-button)
    - [Radio Buttons](#radio-buttons)
    - [Drop Down Lists](#drop-down-lists)
    - [Electronic Signatures](#electronic-signatures)
    - [Review](#review)
  - [Getting Started](#getting-started)
    - [Logging into VIST](#logging-into-vist)
    - [VIST Signon](#vist-signon)
  - [Patient Selection](#patient-selection)
    - [Selecting a Patient](#selecting-a-patient)
    - [Confirming Patient Selection](#confirming-patient-selection)
  - [Actions](#actions)
    - [Create a New Patient Review](#create-a-new-patient-review)
    - [Review a Completed Patient Review](#review-a-completed-patient-review)
    - [Selecting a Patient Review](#selecting-a-patient-review)
    - [### Selecting a Patient Review Section](#selecting-a-patient-review-section)
  - [Patient Review Interviews](#patient-review-interviews)
    - [Section Summaries](#section-summaries)
    - [### Answering Questions](#answering-questions)
    - [Mouse:](#mouse)
    - [Keyboard:](#keyboard)
    - [Completing Sections / Interviews](#completing-sections-interviews)
    - [Messages](#messages)
    - [# Index](#index)
> The Visual Impairment Service Team (VIST) program is designed to enhance the efficiency of the Visual Impairment Service Team programs within the Department of Veterans Affairs (VA). With this program, Visual Impairment Service Teams are able to easily manage and track activities and services provided to blinded veterans in their service area. This program integrates several fields of patient data to produce a variety of reports. The VIST patient record printout can be used in place of VA Form (10-1371) and is a more versatile document than the card. Semi- annual Automated Management Information System (AMIS) reports can be run and veterans can be added or deleted from the rolls quickly.
During the installation of VIST V. 4.0, all data entered using the class III Blind Rehabilitation software will be moved into the new files created for VIST V. 4.0. This conversion time will vary depending on the amount of patient information that was entered into the class III files.
> The VIST Coordinator is the primary user of this program.

## Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Icons used to select key points in this manual are defined as follows:

![](vist-version-4-user-manual/002.png) Required security keys

- Indicates the user should take note of the information.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Visual Impairment Service Team V. 4.0 Technical Manual/Security Guide*

> *Visual Impairment Service Team V. 4.0 Installation Guide*

> *Visual Impairment Service Team V. 4.0 ANRV \* 4 \* 5 Blind Rehabilitation Outcomes Patch Release Notes*

# Visual Impairment Service Team (VIST) V. 4.0 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIST Menu

1 Edit VIST Options Menu...

> 1 Enter/Edit VIST Patient Record

> 2 Enter/Edit VIST Referral Roster

> 3 Enter/Edit Inactive VIST Roster

> 4 Enter/Edit VARO Claims Roster

> 5 Enter/Edit VIST Benefits Checklist

6.  Enter/Edit VIST Parameters
7.  Delete VIST Referral Roster
8.  Delete VIST Patient Record

2 Print Individual Records...

> 1 Individual Patient Record

> 2 Individual Referral Record

> 3 Individual Eye History

> 4 Individual Claims Record

> 5 Individual Annual Review Record

> 6 Individual VIST Benefits Checklist

3 Print VIST Roster Menu...

> 1 VIST Roster List

> 2 VIST Referral Roster List

> 3 VIST Roster List with Annual Review Date

> 4 VARO Claims List

> 5 Inpatient List

> 6 Outpatient Appointment List

> 7 Deceased Patients List

> 8 Inactive VIST Roster List

> 9 Additions to VIST Roster

> 10 Field Visit Dates List

> 11 VIST Roster Sorts...

> 1 State

> 2 City

> 3 ZIP

> 4 County

> 5 Address/Phone List

> 6 Birthdate

> 7 Age

> 8 Eye Diagnosis

> 9 Eye Diagnosis Narrative

> 10 Fee Basis List  
> 11 Period of Service

> 12 Referral Source List

> 13 Annual Review Dates List

> 14 VIST Eligible (AMIS) List

> 12 AMIS Report

> 13 Incomplete AMIS Roster

4 VIST Letter Menu...

> 1 Edit VIST Letter

> 2 Print VIST Letter

> 3 Test Label Alignment

> 4 Print Mailing Labels by Patient

> 5 Print Mailing Labels by City

> 6 Print Mailing Labels by County

> 7 Print Mailing Labels by State

# Entering and Editing VIST Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## *Edit VIST Options Menu*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ANRV EDIT VIST OPTIONS\] \[Synonym:1\]

> This menu allows you to access the options to edit various fields within the VIST database.

If this is the first time your site is using this software, you need to use the *Enter/Edit the VIST Parameters* option to enter site parameters first for the program to work properly.

### Enter/Edit VIST Patient Record 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT VIST PATIENT\] \[Synonym:1\]

> With this option you are able to enter/edit the social data for the VIST veterans.

Example: Enter/Edit VIST Patient Record

Select VIST Menu Option: <u>?</u>

1 Edit VIST Options Menu ...

2 Print Individual Records ...

3 Print VIST Roster Menu ...

4 VIST Letter Menu ...

Select VIST Menu Option: <u>1</u> Edit VIST Options Menu

Select Edit VIST Options Menu Option: <u>?</u>

1 Enter/Edit VIST Patient Record

2 Enter/Edit VIST Referral Roster

3 Enter/Edit Inactive VIST Roster

4 Enter/Edit VARO Claims Roster

5 Enter/Edit VIST Benefits Checklist

6 Enter/Edit VIST Parameters

Select Edit VIST Options Menu Option: <u>1</u> Enter/Edit VIST Patient Record

Select VIST ROSTER NAME: <u>OAT,W</u>ILLIE 09-01-50 123456789

Are you adding 'OAT,WILLIE' as a new VIST ROSTER (the 17TH)? No// <u>Y</u> (Yes)

ENROLLMENT DATE: <u>0327</u> (MAR 27, 1998)

REFERRAL SOURCE: <u>?</u>

Enter source of referral.

Choose from:

1 VA EYE CLINIC

2 NON-VA EYE CLINIC

3 STATE AGENCY

4 COMMUNITY AGENCY

5 VA STAFF

6 VETERANS SERVICE ORGANIZATION

7 FAMILY/FRIEND

8 SELF

9 OTHER

REFERRAL SOURCE: <u>1</u> VA EYE CLINIC

LIVING ARRANGEMENT: <u>?</u>

Enter the veteran's living arrangements.

Choose from:

1 ALONE

2 FAMILY

3 NURSING HOME

4 STATE VETERANS CENTER

5 UNKNOWN

6 LIVES WITH FRIEND

7 BOARD AND CARE

8 OTHER

LIVING ARRANGEMENT: <u>2</u> FAMILY

NUMBER OF DEPENDENTS: <u>2</u>

SPOUSE'S NAME: <u>CATHY</u>

Select NAME OF DEPENDENT & INFO: <u>MARLENE</u>

Are you adding 'MARLENE' as a new NAME OF DEPENDENT & INFO (the 1ST for this VIST ROSTER)? No// <u>Y</u> (Yes)

Select NAME OF DEPENDENT & INFO: <u>\<ENTER\></u>

VA ELIGIBILITY: <u>SC 30%, A&A, VIETNAM</u>

VA ENTITLEMENT (AMIS): <u>?</u>

Enter VA entitlement.

Choose from:

022 0% ONLY (022)

023 10% SC THRU SMC (023)

024 SC FOR BLINDNESS (024)

025 NSC PENSION A&A/HB (025)

NSC NSC PENSION ONLY

OTH NSC OTHER ELIGIBILITY

VA ENTITLEMENT (AMIS): <u>024</u> SC FOR BLINDNESS (024)

Select EYE DIAGNOSIS: <u>?</u>

Answer with EYE DIAGNOSIS

You may enter a new EYE DIAGNOSIS, if you wish

Enter Eye Diagnosis.

Answer with VIST EYE DIAGNOSIS

Do you want the entire 14-Entry VIST EYE DIAGNOSIS List? <u>Y</u> (Yes)

Choose from:

APHAKIA

CATARACT

CHORIOID/RETINAL

CORNEAL DISEASE

DIABETIC RETINOPATHY

GLAUCOMA

HISTOPLASMOSIS

MACULAR DISEASE

OPTIC ATROPHY

OPTIC NERVE

OTHER

RETINAL DETACHMENT

RETINITIS PIGMENTOSA

TRAUMA

You may enter a new VIST EYE DIAGNOSIS, if you wish

Answer must be 3-30 characters in length.

Select EYE DIAGNOSIS: <u>TRAUMA</u>

Are you adding 'TRAUMA' as a new EYE DIAGNOSIS (the 1ST for this VIST ROSTER)? No// <u>Y</u> (Yes)

Select EYE DIAGNOSIS:

Select EYE EXAM DATE: <u>0327</u> MAR 27, 1998

Are you adding 'MAR 27, 1998' as a new EYE EXAM DATE (the 1ST for this VIST ROSTER)? No// <u>Y</u> (Yes)

EYE DIAGNOSIS NARRATIVE: GLAUCOMA

VISUAL ACUITY RIGHT EYE: <u>20/100</u>

VISUAL ACUITY LEFT EYE: <u>20/70</u>

VISUAL FIELD RIGHT EYE: <u>10-15</u>

VISUAL FIELD LEFT EYE: <u>5</u>

VISUAL ACTIVITY (AMIS): <u>?</u>

Enter Visual Acuities or fields per AMIS guidelines.

Choose from:

004 NO SIGHT (004)

005 LP UP TO & INCLUDING 5/200 (005)

006 LP OF 6/200 TO 20/200 (006)

007 FIELD RESTRICTION (007)

008 NOT KNOWN (008)

VISUAL ACTIVITY (AMIS): <u>007</u> FIELD RESTRICTION (007)

GENERAL HEALTH:

1\><u>\<ENTER\></u>

Select VIS TEAM REVIEW DATE: <u>0327</u> MAR 27, 1998

Are you adding 'MAR 27, 1998' as

a new VIS TEAM REVIEW DATE (the 1ST for this VIST ROSTER)? No// <u>Y</u> (Yes)

AMIS-STATUS OF REVIEW: <u>?</u>

Enter the AMIS status at the time of review.

Choose from:

035 COMPLETE (035)

036 DECLINED (036)

037 NO SHOW (037)

AMIS-STATUS OF REVIEW: <u>035</u> COMPLETE (035)

TYPE OF REVIEW: <u>?</u>

Enter the type of review.

Choose from:

1 FORMAL

2 COMPONENT

TYPE OF REVIEW: <u>1</u> FORMAL

Select VIS TEAM REVIEW DATE: <u>0424</u> APR 24, 1998

Are you adding 'APR 24, 1998' as

a new VIS TEAM REVIEW DATE (the 2ND for this VIST ROSTER)? No// Y (Yes)

Select VIS TEAM REVIEW DATE: <u>\<ENTER\></u>

Select VIST FIELD VISIT DATE (AMIS): <u>\<ENTER\></u>

VIST ELIGIBLE (AMIS): <u>?</u>

Enter veteran's eligibility for VIST services.

Choose from:

001 YES (001)

002 NO - REVIEWED FOR BRC ATTENDANCE (002)

003 NO - OTHER (003)

NO NO - NOT LEGALLY BLIND

I INACTIVE

VIST ELIGIBLE (AMIS): <u>Y</u> YES (001)

MAJOR ACTIVITY (AMIS): <u>?</u>

Enter the code corresponding to the veteran's major activity.

Choose from:

009 EMP FOR PAY (009)

010 ENG IN TRN/SCHOOL (010)

011 VOL WORK 10HRS/WK (011)

012 RETIRED W/APPROP. ACT. (012)

013 TOO ILL OR TOO DISABLED (013)

014 NO WELL DEFINED ACT. (014)

015 NOT KNOWN (015)

MAJOR ACTIVITY (AMIS): <u>013</u> TOO ILL OR TOO DISABLED (013)

FINANCIAL AND BENEFITS INFO:

1\><u>\<ENTER\></u>

PATIENT HISTORY:

1\><u>\<ENTER\></u>

ACTIVITIES:

1\><u>\<ENTER\></u>

ADJUSTMENT TO BLINDNESS:

1\><u>\<ENTER\></u>

IMPRESSIONS:

1\><u>\<ENTER\></u>

PLAN:

1\><u>\<ENTER\></u>

Select VIST ROSTER NAME:<u>\<ENTER\></u>

Select Edit VIST Options Menu Option: <u>\<ENTER\></u>

### Enter/Edit VIST Referral Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT INACTIVE VIST\] \[Synonym:2\]

> This option allows you to keep track of referrals for VA, state, and local blind rehabilitation programs.

> The veteran should be listed on the VIST Roster for you to be able to add him/her to the Referral Roster.

Example: Enter/Edit VIST Referral Roster

Select Edit VIST Options Menu Option: <u>2</u> Enter/Edit VIST Referral Roster

Select VIST REFERRAL ROSTER NAME: <u>OAT,W</u>ILLIE

Are you adding 'OAT,WILLIE' as a new VIST REFERRAL ROSTER (the 4TH)? No// <u>Y</u>

(Yes)

Select REFERRAL DATE: <u>010798</u> (JAN 07, 1998)

Are you adding 'JAN 07, 1998' as a new REFERRAL DATE (the 1ST for this VIST REFERRAL ROSTER)? No// <u>Y</u> (Yes)

PLACE OF REFERRAL: <u>BIRM</u>INGHAM (CENTER)

TYPE OF REFERRAL (AMIS): <u>?</u>

Enter the type of referral.

Choose from:

039 CTR 1ST EXP (039)

040 CTR ADDL TRN (040)

041 CLINIC 1ST EXP (041)

042 CLINIC ADDL TRN (042)

043 NON VA 1ST EXP (043)

044 NON VA ADDL TRN (044)

TYPE OF REFERRAL (AMIS): 039 CTR 1ST EXP (039)

STATUS OF APPLICATION: <u>?</u>

Enter the status of the application.

Choose from:

051 ACCEPTED

045 REJECTED (CENTER)

046 REJECTED (CLINIC)

052 WITHDREW

053 PENDING

STATUS OF APPLICATION: 051 ACCEPTED

DATE OF NOTIFICATION: <u>\<ENTER\></u>

BLIND REHAB ADMISSION DATE: <u>0330</u> MAR 30, 1998

BLIND REHAB DISCHARGE DATE: <u>0430</u> (APR 30, 1998)

TYPE OF DISCHARGE: <u>?</u>

Enter the type of discharge.

Choose from:

047 BLIND CENTER (047)

048 BLIND CLINIC (048)

049 OTHER NON VA (049)

TYPE OF DISCHARGE: <u>047</u> BLIND CENTER (047)

Select REFERRAL DATE: <u>\<ENTER\></u>

Select VIST REFERRAL ROSTER NAME: <u>\<ENTER\></u>

Select Edit VIST Options Menu Option:<u>\<ENTER\></u>

### Enter/Edit Inactive VIST Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT INACTIVE LIST\] \[Synonym:3\]

> You can keep track of veterans removed from the VIST Roster due to death, relocation, or change in legal blindness status with this option. It is recommended that veterans not be deleted from the VIST Roster until after they have been considered inactive for a period of time. The period of time is up to the VIST Coordinator’s discretion. This will ensure accurate AMIS reporting.

Don’t inactivate a veteran until after the AMIS period is completed, otherwise statistical records regarding the veteran will not be counted on your semiannual AMIS report.

Make sure you change the veteran’s VIST Eligible status to INACTIVE in the *Enter/Edit VIST Patient Record* option. Otherwise, the veteran will be counted on the AMIS report.

Example: Enter/Edit Inactive VIST Roster

Select Edit VIST Options Menu Option: <u>3</u> Enter/Edit Inactive VIST Roster

Select VIST ROSTER NAME: <u>OAT,W</u>ILLIE

Select INACTIVATION DATE: <u>0501</u> MAY 01, 1998

REASON: <u>?</u>

Enter the reason that this veteran was inactivated.

Choose from:

1 DECEASED

2 RELOCATED

3 NOT LEGALLY BLIND

REASON: <u>2</u> RELOCATED

Select VIST ROSTER NAME: <u>\<ENTER\></u>

Select Edit VIST Options Menu Option: <u>\<ENTER\></u>

### Enter/Edit VARO Claims Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT VARO CLAIMS\] \[Synonym:4\]

> This option allows you to keep track of Veterans Affairs Regional Office (VARO) claims filed to the regional office.

The veteran should be listed on the VIST Roster for you to be able to add him to the VARO Claims Roster.

Example: Enter/Edit VARO Claims Roster

Select Edit VIST Options Menu Option: <u>4</u> Enter/Edit VARO Claims Roster

Select VARO CLAIMS NAME: <u>OAT,W</u>ILLIE

Are you adding 'OAT,WILLIE' as a new VARO CLAIMS (the 8TH)? No// <u>Y</u> (Yes)

NAME: OAT,WILLIE// <u>\<ENTER\></u>

Select DATE OF CLAIM: <u>0327</u> MAR 27, 1998

Are you adding 'MAR 27, 1998' as a new DATE OF CLAIM (the 1ST for this VARO CLAIMS)? No// <u>Y</u> (Yes)

CLAIM: <u>?</u>

Enter the type of claim being filed.

Choose from:

01 A&A/HB (IMPROVED PENSION)

02 INCREASE SC RATING

03 INITIAL SC RATING

04 SWITCH TO IMPROVED PENSION

05 OTHER

CLAIM: <u>01</u> A&A/HB (IMPROVED PENSION)

REGIONAL OFFICE: ATLANTA, GA// <u>\<ENTER\></u>

VARO DECISION: <u>?</u>

Enter the VARO decision, accepted ,denied, or pending, regarding this

claim.

Choose from:

A ACCEPTED

D DENIED

P PENDING

VARO DECISION: <u>A</u> ACCEPTED

Select DATE OF CLAIM: <u>\<ENTER\></u>

Select VARO CLAIMS NAME: <u>\<ENTER\></u>

Select Edit VIST Options Menu Option: <u>\<ENTER\></u>

### Enter/Edit VIST Benefits Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT CHECKLIST\] \[Synonym:5\]

> You are able to keep track of each VIST veteran’s eligibility for and use of various benefits and services for the blind with this option.

The veteran should be listed on the VIST Roster for you to be able to add him to the VARO Claims Roster.

Example: Enter/Edit VIST Benefits Checklist

Select Edit VIST Options Menu Option: <u>5</u> Enter/Edit VIST Benefits Checklist

Select VIST BENEFITS AND SERVICES CHECKLIST NAME: <u>OAT,W</u>ILLIE

Are you adding 'OAT,WILLIE' as

a new VIST BENEFITS AND SERVICES CHECKLIST (the 2ND)? No// <u>Y</u> (Yes)

NAME: OAT,WILLIE// <u>\<ENTER\></u>

AUTO GRANT: <u>?</u>

Enter whether or not the veteran has used or is eligible for the Auto

Grant.

Answer with VIST CHECKLIST OPTIONS CHECKLIST NAME

Choose from:

DECLINED

NOT AVAILABLE

NOT ELIGIBLE

PENDING

YES

AUTO GRANT: <u>Y</u>ES

BLIND REHAB. TRAINING: <u>Y</u>ES

CHAMPUS: <u>NOT E</u>LIGIBLE

CHAMPVA: <u>NOT E</u>LIGIBLE

CLOTHING ALLOWANCE: <u>NOT E</u>LIGIBLE

EDUCATION - VA: <u>NOT E</u>LIGIBLE

FEE BASIS: <u>P</u>ENDING

HISA: <u>P</u>ENDING

INSURANCE - SDVI: <u>NOT A</u>VAILABLE

INSURANCE - WAIVE PREMIUM: <u>NOT E</u>LIGIBLE

PROSTHETICS: <u>P</u>ENDING

SAH - 801(a): <u>NOT E</u>LIGIBLE

SAH - 801(b): <u>NOT E</u>LIGIBLE

VA VOCATIONAL REHABILITATION: <u>D</u>ECLINED

VIST ANNUAL REVIEW: <u>Y</u>ES

IDENTIFICATION CARD: <u>Y</u>ES

BLINDED VETERANS ASSOCIATION: <u>Y</u>ES

COMMISSARY AND EXCHANGE: <u>Y</u>ES

NATIONAL CONSUMER GROUPS: <u>Y</u>ES

FREE POSTAGE: NOT ELIGIBLE

PHONE DIRECTORY ASSISTANCE: <u>Y</u>ES

DOG GUIDE TRAINING: PENDING

HADLEY SCHOOL FOR THE BLIND: <u>NOT A</u>VAILABLE

HANDICAP PARKING PLACARD: <u>Y</u>ES

INCOME TAX DEDUCTION: <u>Y</u>ES

NAT'L PARKS ADMISSION PERMIT: <u>Y</u>ES

RADIO READING SERVICE: <u>Y</u>ES

RECORDING FOR THE BLIND: <u>Y</u>ES

SOCIAL SECURITY: <u>Y</u>ES

TALKING BOOKS: <u>Y</u>ES

VOTING RIGHTS: <u>Y</u>ES

Select LOCAL BENEFITS AND SERVICES: <u>?</u>

Answer with LOCAL BENEFITS AND SERVICES

You may enter a new LOCAL BENEFITS AND SERVICES, if you wish

Indicate veteran's awareness of these programs.

Answer with VIST LOCAL BENEFITS AND SERVICES NAME

Choose from:

HUNTING/FISHING LICENSE

LOCAL AGENCY FOR THE BLIND

PROPERTY TAX EXEMPTION

STATE SERVICES FOR THE BLIND

TRANSIT PASS

Select LOCAL BENEFITS AND SERVICES: <u>LOC</u>AL AGENCY FOR THE BLIND

Are you adding 'LOCAL AGENCY FOR THE BLIND' as

a new LOCAL BENEFITS AND SERVICES (the 1ST for this VIST BENEFITS AND SERVICES CHECKLIST)? No// <u>Y</u> (Yes)

STATUS: <u>P</u>ENDING

Select LOCAL BENEFITS AND SERVICES: <u>STA</u>TE SERVICES FOR THE BLIND

Are you adding 'STATE SERVICES FOR THE BLIND' as

a new LOCAL BENEFITS AND SERVICES (the 2ND for this VIST BENEFITS AND SERVICES CHECKLIST)? No// <u>Y</u> (Yes)

STATUS:

Select LOCAL BENEFITS AND SERVICES: <u>\<ENTER\></u>

Select VIST BENEFITS AND SERVICES CHECKLIST NAME: <u>\<ENTER\></u>

Select Edit VIST Options Menu Option: <u>\<ENTER\></u>

### Enter/Edit VIST Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT VIST PARAMETER\] \[Synonym:6\]

> You can customize the VIST program using this option. The VIST Coordinator’s name should be entered as you want it to look on the VIST Patient Record. It should include any title or other information you wish to see as a part of the name. The telephone extension and/or routing symbol, whichever you prefer, will be printed on the VIST Veteran Record directly under the name of the VIST Coordinator. When you enter VARO claims, you will be asked which regional office the claim was submitted to. Enter the name of the regional office you use most often at the “DEFAULT REGIONAL OFFICE” prompt and it will appear as the default whenever you enter VARO claims.

> First time users should use the *Enter/Edit VIST Parameters* option before using other options. The fields shown in the example below will be blank and must be answered for the program to work properly. Once set, this option can be ignored until there is a change in VIST Coordinators.

Example: Enter/Edit VIST Parameters

Select Edit VIST Options Menu Option: <u>6</u> Enter/Edit VIST Parameters

The site name, BIRMINGHAM, AL., is already defined in the VIST PARAMETERS

file.

Do you want to edit the SITE NAME in the VIST PARAMETER file? No// <u>Y</u> YES

SITE NAME: BIRMINGHAM, AL.// <u>\<ENTER\></u>

VIST COORDINATOR: Fred Smith// <u>JOHN GROVENER</u>

ROUTING SYMBOL OR PHONE: 111// <u>\<ENTER\></u>

DEFAULT REGIONAL OFFICE: ATLANTA, GA// <u>\<ENTER\></u>

Select Edit VIST Options Menu Option: <u>\<ENTER\></u>

### Delete VIST Referral Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV DELETE REFERRAL\] \[Synonym:7\]

> This option allows the VIST Coordinator to delete a veteran from the VIST REFERRAL ROSTER file (#2042.5).

### Delete VIST Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV DELETE ROSTER\] \[Synonym:8\]

> This option allows the VIST Coordinator to delete a veteran from the VIST ROSTER file (#2040). It also deletes the corresponding entries for the veteran in the VIST BENEFITS AND SERVICES CHECKLIST (#2041.7), VIST REFERRAL ROSTER (#2042.5), and VARO CLAIMS (#2043.5) files.

# # Printing Individual Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## *Print Individual Records*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ANRV INDIVIDUAL RECORDS\] \[Synonym:2\]

This menu contains options that allow the VIST Coordinator to print information for one VIST veteran.

### Individual Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV PRINT PATIENT RECORD\] \[Synonym:1\]

> This is the electronic version of the VIST Record, VA FORM 10-1371. This option provides you with a printout of a combination of information from the VIST patient record file and the main hospital database file.

Example: Individual Referral Record

Select VIST Menu Option: <u>2</u> Print Individual Records

Select Print Individual Records Option: <u>1</u> Individual Patient Record

Select VIST PATIENT: <u>OAT,W</u>ILLIE 09-01-50 123456789

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VISUAL IMPAIRMENT SERVICE TEAM (VIST)

PATIENT RECORD

BIRMINGHAM, AL. (521)

APR 01, 1998

Name: OAT,WILLIE

Address: GOLDEN TEMPLE AVENUE

City,State,Zip: FYFE, AL 22222

County: JACKSON

Phone: 123-456-7890

Social Security Number: 123-45-6789

VA Claim Number:

Location of Claim File:

Service Dates:

Branch of Service (Last):

Date of Birth: SEP 1,1950

Place of Birth: AUSTIN, TX

Age: 47

Employment Status: SELF EMPLOYED

Marital Status: NEVER MARRIED

Living Arrangement: FAMILY

Number of Dependents: 1

Name of Spouse: CATHY

Dependent(s) Name(s):

MARLENE

VIST Eligibility: SC 30%, A&A, VIETNAM

Rated Disability:

Eye Diagnosis: TRAUMA

Eye Exam Date (Last): MAR 27, 1998

Visual Acuity Right Eye: 20/100

Visual Acuity Left Eye: 20/70

Visual Field Right Eye: 10-15

Visual Field Left Eye: 5

VIST Review Date (Last): APR 24, 1998

Status of Review:

Type of Review:

Eligibility on Review Date: SC 30%, A&A, VIETNAM

Field Visit Date (Last):

OAT,WILLIE 449-34-5555 Page 1

VISUAL IMPAIRMENT SERVICE TEAM (VIST)

PATIENT RECORD

BIRMINGHAM, AL. (521)

APR 22, 1998

VIS TEAM ASSESSMENT

General Health:

Financial/Benefits:

Patient History:

Activities:

Adjustment to Blindness:

Impressions:

*\[This report has been abbreviated to save space.\]*

### Individual Referral Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV PRINT IND. REFERRAL\] \[Synonym:2\]

> This option provides you with a printout of a patient’s referral history. The record is sorted by the date of referral and includes the place of referral, AMIS information, and admit/discharge dates.

Example: Individual Referral Record

Select VIST Menu Option: <u>2</u> Print Individual Records

Select Print Individual Records Option: <u>2</u> Individual Referral Record

Select VIST REFERRAL ROSTER NAME: <u>OAT,W</u>ILLIE

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIS TEAM PATIENT REFERRAL RECORD APR 1,1998 12:31 PAGE 1

REFERRAL APPLICATION NOTIF. ADM. DSCH.

DATE PLACE OF REFERRAL TYPE STATUS DATE DATE DATE TYPE OF DISCHARGE

-------------------------------------------------------------------------------------------------------------------

Name: OAT,WILLIE

Social Security No.: 123-45-6789

03/30/98 BIRMINGHAM (CENTER) CTR 1ST EXP (039) ACCEPTED 11/07/97 03/31/98 BLIND CENTER (047)

### Individual Eye History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV INDIVIDUAL EYE DIAG\] \[Synonym:3\]

> This option provides you with a printout of a patient’s VIST eye history. The record is sorted by the date of the VIST eye examination and includes the diagnosis, visual acuities, and fields.

> Example: Individual Eye History

> Select Print Individual Records Option: <u>3</u> Individual Eye History

> Select VIST ROSTER NAME: <u>OAT,W</u>ILLIE

> DEVICE: *\[Select Print Device\]*

> Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

> INDIVIDUAL VIST EYE HISTORY

> Veteran's Name: OAT,WILLIE

> Social Security: 123-45-6789

> Eye Diagnosis: TRAUMA

> EXAM ACUITY ACUITY FIELD FIELD

> DATE RIGHT EYE LEFT EYE RIGHT EYE LEFT EYE

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> MAR 27,1998 20/100 20/70 10-15 5

### Individual Claims Record 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV CLAIM REC INQ\] \[Synonym:4\]

> With this option, you get a printout of VARO claims filed by VIST on behalf of an individual. This record is sorted by the date of the claim and includes the type of claim, regional office, and the VARO decision.

> Example: Individual Claims Record

> Select Print Individual Records Option: <u>4</u> Individual Claims Record

> Select VARO CLAIMS NAME: <u>JONES,M</u>ICK 12-12-87 222334444 NO

> DEVICE: *\[Select Print Device\]*

> Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

> INDIVIDUAL VIST CLAIM RECORD

> Veteran's Name: JONES,MICK

> Soc. Sec. No.: 222-33-4444

> Claim No.: c-22233444

> Date of Claim Type of Claim Regional Office VARO Decision

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> JAN 31,1998 INCREASE SC RATING ATLANTA, GA DENIED

> FEB 10,1998 SWITCH TO IMPROVED PENSION ATLANTA, GA ACCEPTED

### Individual Annual Review Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ANNUAL REVIEW INQ\] \[Synonym:5\]

> Using this option, you can obtain a printout of past VIST Reviews for a particular blinded veteran. The printout includes the Review date, veteran’s name, social security number, status of review, type of review, and eligibility on review date.

> Example: Individual Annual Review Record

> Select Print Individual Records Option: <u>5</u> Individual Annual Review Record

> Select VIST ROSTER NAME: <u>OAT,W</u>ILLIE

> DEVICE: *\[Select Print Device\]*

> Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

> ANNUAL REVIEW INQUIRY APR 1,1998 12:36 PAGE 1

> NAME SSN

> VIS TEAM AMIS-STATUS OF TYPE OF

> REVIEW DATE REVIEW REVIEW ELIGIBILITY ON REVIEW DATE

> --------------------------------------------------------------------------------

> OAT,WILLIE 123456789

> MAR 27,1998 COMPLETE (035) FORMAL SC 30%, A&A, VIETNAM

> APR 24,1998 SC 30%, A&A, VIETNAM

### Individual VIST Benefits Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV CHECKLIST INQ\] \[Synonym:6\]

> This option provides you with a printout of an individual’s eligibility of use of various VA and non-VA benefits and services for blinded veterans.

Example: Individual VIST Benefits Checklist

Select Print Individual Records Option: <u>6</u> Individual VIST Benefits Checklist

Select VIST BENEFITS AND SERVICES CHECKLIST NAME: <u>OAT,W</u>ILLIE

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST BENEFITS & SERVICES CHECKLIST

Veteran's Name: OAT,WILLIE

VIST Review Date: APR 24,1998

Soc. Sec. No.: 449-34-5555

VA BENEFITS AND SERVICES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Auto Grant YES

Blind Rehabilitation Training YES

CHAMPUS NOT ELIGIBLE

CHAMPVA NOT ELIGIBLE

Clothing Allowance NOT ELIGIBLE

Education NOT ELIGIBLE

Fee Basis PENDING

HISA PENDING

Insurance - Service Disabled Veterans Insurance NOT AVAILABLE

Insurance - Waive Premium NOT ELIGIBLE

Prosthetics PENDING

Specially Adapted Housing - 801(a) NOT ELIGIBLE

Special Housing Adaptations - 801(b) NOT ELIGIBLE

VA Vocational Rehabilitation DECLINED

VIST Annual Review YES

NON-VA BENEFITS AND SERVICES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Identification Card YES

Blinded Veterans Association YES

Commissary and Exchange YES

National Consumer Groups YES

Free Postage NOT ELIGIBLE

Free Telephone Directory Assistance YES

Dog Guide Training PENDING

Hadley School for the Blind NOT AVAILABLE

Handicap Parking Placard YES

Income Tax Deduction YES

National Parks Lifetime Admission Permit YES

Radio Reading Service YES

Recording for the Blind YES

Social Security YES

Talking Books YES

Voting Rights YES

LOCAL BENEFITS AND SERVICES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Local Agency For The Blind PENDING

State Services For The Blind

# # Printing the VIST Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## *Print VIST Roster Menu*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ANRV PRINT VIST OPTIONS\] \[Synonym:3\]

> This menu contains options that enable the VIST Coordinator to print the records of veterans referred for VA, state, and local blind rehabilitation services.

### VIST Roster List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV VIST ROSTER PRINT\] \[Synonym:1\]

> This printout is an alphabetic printout of every veteran being served by your VIST program. It includes each veteran’s name, social security number, VIST eligibility, period of service, and VA eligibility.

> If you choose to print this list by All patients, patients with a date of death entry in Medical Administration Service (MAS) will not appear on the VIST Roster List. If you choose to print this list by individual patient and that patient has a date of death entry in MAS, a message will be displayed with the date of death.

Example: VIST Roster List

Select Print VIST Roster Menu Option: <u>1</u> VIST Roster List

VIST ROSTER PRINTOUT

Do you want the report to list:

(A)ll patients, or

(S)elect patients

Choose A or S: <u>A</u>LL

The right margin for this report is 132.

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST ROSTER PRINTOUT Printed APR 1,1998@12:41 Page 1

NAME SSN VIST ELIGIBLE PERIOD OF VIST ELIGIBILITY

SERVICE

-----------------------------------------------------------------------------------------------------------

ALLEN,PATRICK 123-45-6789

BASS,EARNEST T. 123-45-6789 NO - OTHER (003) VIETNAM ERA SC LESS THAN 50%

CASH,JOHNNY 123-45-6789 NO - OTHER (003) POST-VIETNAM

CLAMPETT,ELLIE MAE 123-45-6789 YES (001) OTHER

CLEAVER,THEODORE 123-45-6789 NO - OTHER (003) POST-KOREAN SC LESS THAN 50%

DAVIS,PAULETTE 123-45-6789 POST-VIETNAM HOUSEBOUND

DAWSON,EB 123-45-6789 NO - REVIEWED FOR BRC AID & ATTENDANCE

DIDDLEY,BO 123-45-6789 YES (001) OTHER

JADESTONE,MICK 123-45-6789 YES (001)

JONES,MICK 123-45-6789 YES (001) WORLD WAR II SC LESS THAN 50%

OAT,WILLIE 123-45-6789 YES (001) SC 30%, A&A, VIETNAM

REYNOLDS,NANCY 123-45-6789 YES (001) SC LESS THAN 50%

ZOOM,BILLY 123-45-6789 YES (001) OTHER FEDERAL AGENCY

### ### VIST Referral List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV REFERRAL PRINT\] \[Synonym:2\]

> This option provides you with a printout of referrals for blind rehabilitation based on the date of referral. You have the choice of how far back in time (i.e., one day, one month, one year, two years, etc.) the roster will be printed out. This printout is helpful for double checking the semi-annual AMIS report.

Example: VIST Referral List

Select Print VIST Roster Menu Option: <u>2</u> VIST Referral Roster List

\* Previous selection: REFERRAL DATE not null

START WITH REFERRAL DATE: FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST REFERRAL ROSTER LIST APR 1,1998 12:46 PAGE 1

REFERRAL DATE NAME PLACE OF REFERRAL STATUS NOTIF. DATE ADM. DATE DSCH. DATE

-------------------------------------------------------------------------------------------------

JAN 26,1998 CLAMPETT,ELLIE BIRMINGHAM (CENTER) ACCEPTED JAN 26,1998 JAN 26,1998 FEB 6,1998

FEB 12,1998 JONES,MICK BIRMINGHAM (CENTER) ACCEPTED FEB 12,1998 FEB 12,1998 FEB 12,1998

### VIST Roster List with Annual Review Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ROSTER A/R PRINT\] \[Synonym:3\]

> This option is identical to the *VIST Roster List* option, except that it includes information on each veteran’s last annual review. The printout includes the veteran’s name, social security number, VIST eligibility, last annual review date, and status of review.

Example: VIST Roster List with Annual Review Date

Select Print VIST Roster Menu Option: <u>3</u> VIST Roster List With Annual Review Date

START WITH NAME: FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST ROSTER PRINTOUT - ANNUAL REVIEW APR 20,1998 10:48 PAGE 1

LAST

ANNUAL

NAME SSN VIST ELIGIBLE VIST ELIGIBILITY REVIEW STATUS

-------------------------------------------------------------------------------------------------

BASS,EARNEST T. 123-45-6789 NO - OTHER (003) SC LESS THAN 50% 09/09/97 COMPLETE (035)

BODEAN,JETHRO 123-45-6789 INACTIVE HOUSEBOUND 08/07/97 DECLINED (036)

CASH,JOHNNY 123-45-6789 NO - OTHER (003) 03/18/98 COMPLETE (035)

CLAMPETT,ELLIE MAE 123-45-6789 YES (001) 01/22/98 COMPLETE (035)

CLEAVER,THEODORE 123-45-6789 NO - OTHER (003) SC LESS THAN 50% 01/00/97 COMPLETE (035)

DIDDLEY,BO 123-45-6789 YES (001)

JONES,MICK 123-45-6789 YES (001) SC LESS THAN 50% 10/27/97 COMPLETE (035)

OAT,WILLIE 123-45-6789 YES (001) SC 30%, A&A, VIETNAM 04/24/98 COMPLETE (035)

REYNOLDS,NANCY 123-45-6789 YES (001) SC LESS THAN 50% 02/04/98 NO SHOW (037)

ZOOM,BILLY 123-45-6789 YES (001) OTHER FEDERAL AGENCY 03/27/98 COMPLETE (035)

### VARO Claims List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV PRINT VARO CLAIMS\] \[Synonym:4\]

> This option provides you with a printout that is sorted by date of VARO claims filed by VIST on behalf of blinded veterans. The printout includes the date of claim, veteran’s name, social security number, VA claim number, type of claim, regional office, and the VARO decision.

Example: VARO Claims List

Select Print VIST Roster Menu Option: <u>4</u> VARO Claims List

VIST VARO CLAIMS LIST

Do you want the report to list:

(A)ll patients or

(S)elect patients

Choose A or S: <u>A</u>LL

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST VARO CLAIMS LIST Printed APR 1,1998@12:54 Page: 1

NAME SSN VA CLAIM \# DATE OF CLAIM REGIONAL OFFICE VARO DECISION

CLAIM

-------------------------------------------------------------------------------------------------------------------

BASS,EARNEST T. 123-45-6789 123455119 MAR 27,1998 A&A/HB (IMPROVED PENSION) ATLANTA, GA ACCEPTED

BELL,MARY 123-45-6789 MAR 2,1987 INCREASE SC RATING ASHEVILLE, NC DENIED

DIDDLEY,BO 123-45-6789 SEP 9,1988 OTHER BIG SPRING, TX DENIED

OCT 6,1989 SWITCH TO IMPROVED PENSION BIG SPRING, TX ACCEPTED

JADESTONE,MICK 123-45-6789 DEC 25,1986 INITIAL SC RATING BAY PINES, FL ACCEPTED

JONES,MICK 123-45-6789 22233444 JAN 31,1998 INCREASE SC RATING ATLANTA, GA DENIED

FEB 10,1998 SWITCH TO IMPROVED PENSION ATLANTA, GA ACCEPTED

REYNOLDS,NANCY 123-45-6789 488599776 AUG 9,1997 INITIAL SC RATING ATLANTA, GA ACCEPTED

### Inpatient List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV INPATIENT LIST\] \[Synonym:5\]

> You can obtain a printout of VIST patients currently admitted to your VA Medical Center using this option. The printout is sorted by ward and includes the veteran’s name, social security number, room number, and date of admission.

Example: Inpatient List

Select Print VIST Roster Menu Option: <u>5</u> Inpatient List

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST INPATIENT ROSTER LIST APR 20,1998 13:26 PAGE 1

NAME SSN WARD ROOM-BED

--------------------------------------------------------------------------------

BODEAN,JETHRO 123-45-6789 1 SOUTH

DAVIS,PAULETTE 123-45-6789 1 WEST (

ZOOM,BILLY 123-45-6789 1 WEST (

ALLEN,PATRICK 123-45-6789 1 WEST ( 101-A

BELL,MARY 123-45-6789 1 WEST ( 102-2

DAWSON,EB 123-45-6789 2 EAST

CLAMPETT,ELLIE MAE 123-45-6789 2 EAST 250-A

DIDDLEY,BO 123-45-6789 2 EAST 250-B

JADESTONE,MICK 123-45-6789 2 EAST 250-D

CASH,JOHNNY 123-45-6789 2 SOUTH 230-A

DASTARDLY,DICK 123-45-6789 2 SOUTH 230-D

### Outpatient Appointment List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV OUTPATIENT APPT. LIST\] \[Synonym:6\]

> This option provides you with a printout of past or future outpatient appointments for VIST patients. You enter a date range and the printout lists all appointments by date and time. The printout includes the date of appointment, veteran’s name, social security number, time of appointment, and clinic.

Example: Outpatient Appointment List

Select Print VIST Roster Menu Option: <u>6</u> Outpatient Appointment List

OUTPATIENT APPOINTMENT LIST

The right margin for this report is 132.

Do you want to sort by (P)atient or (D)ate/time of appointment?

Choose P or D: <u>P</u>ATIENT

BEGINNING date for report: <u>T-45</u> (MAR 06, 1998)

ENDING date for report: <u>T</u> (APR 20, 1998)

Do you want to list outpatient appointments for:

(A)ll patients, or

(S)elect patients.

Choose A or S: <u>A</u> ALL

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST ROSTER OUTPATIENT APPOINTMENTS FROM MAR 6,1998 TO APR 20,1998 Page 1

NAME SSN LAST ANNUAL REVIEW STATUS APPT. DATE/TIME CLINIC

-----------------------------------------------------------------------------------------------------

BASS,EARNEST T. 123-45-6789 SEP 9,1997 COMPLETE (035) MAR 26,1998@11:00 CARDIOLOGY

DIDDLEY,BO 123-45-6789 MAR 25,1998@10:30 PULMONARY

### Deceased Patients List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV DECEASED PATIENTS\] \[Synonym:7\]

> Using a date range you can print out a list of VIST eligible veterans that have been listed as deceased in the main Veterans Health Information Systems and Technology Architecture (V*IST*A) files with this option.

Example: Deceased Patients List

Select Print VIST Roster Menu Option: <u>7</u> Deceased Patients List

\* Previous selection: NAME:DATE OF DEATH not null

START WITH NAME:DATE OF DEATH: FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

DECEASED LISTING OF VIST PATIENTS APR 20,1998 13:30 PAGE 1

NAME SSN DATE OF DEATH

--------------------------------------------------------------------------------

CLEAVER,THEODORE 123-45-6789 JUN 22,1995

### Inactive VIST Roster List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV PRINT INACTIVE VIST\] \[Synonym:8\]

> This option provides you with a printout of VIST eligible veterans listed on the Inactive VIST Roster.

Example: Inactive VIST Roster List

Select Print VIST Roster Menu Option: <u>8</u> Inactive VIST Roster List

\* Previous selection: INACTIVATION DATE not null

START WITH INACTIVATION DATE: FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

VIST ROSTER INACTIVATION LIST \*\*BE SURE VIST ELIGIBLE READS INACTIVE\*\*

APR 20,1998 13:31 PAGE 1

INACTIVATION

DATE NAME SSN REASON VIST ELILGIBLE

---------------------------------------------------------------------------------------------

JAN 26,1998 JONES,MICK 123-45-6789 RELOCATED

YES (001)

FEB 27,1998 REYNOLDS,NANCY 123-45-6789 NOT LEGALLY BLIND

YES (001)

MAY 1,1998 OAT,WILLIE 123-45-6789 RELOCATED

YES (001)

------------------------

COUNT 3

### Additions to VIST Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ADD TO VIST ROSTER\] \[Synonym:9\]

> Using a date range you can print a list of veterans added to the VIST Roster with this option.

Example: Additions to VIST Roster

Select Print VIST Roster Menu Option: <u>9</u> Additions to VIST Roster

\* Previous selection: ENROLLMENT DATE not null

START WITH ENROLLMENT DATE: FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

ADDITIONS TO VIST ROSTER APR 20,1998 13:32 PAGE 1

ENROLLMENT

DATE NAME SSN VIST ELIGIBLE REFERRAL SOURCE

-------------------------------------------------------------------------------------

MAY 5,1994 DASTARDLY,DICK 123-45-6789 YES (001) FAMILY/FRIEND

JUN 6,1996 BODEAN,JETHRO 123-45-6789 INACTIVE OTHER

MAR 26,1997 JONES,MICK 123-45-6789 YES (001) FAMILY/FRIEND

JUN 7,1997 BASS,EARNEST T. 123-45-6789 NO - OTHER (0 SELF

JAN 22,1998 CLAMPETT,ELLIE MAE 123-45-6789 YES (001) VA EYE CLINIC

JAN 30,1998 REYNOLDS,NANCY 123-45-6789 YES (001) SELF

FEB 3,1998 DAWSON,EB 123-45-6789 NO - REVIEWED VA STAFF

FEB 3,1998 DIDDLEY,BO 123-45-6789 YES (001) SELF

FEB 18,1998 JONES,MICK 123-45-6789 YES (001) VA EYE CLINIC

MAR 18,1998 CASH,JOHNNY 123-45-6789 NO - OTHER (0 VA EYE CLINIC

MAR 27,1998 BELL,MARY 123-45-6789 NO - REVIEWED VA EYE CLINIC

MAR 27,1998 CLEAVER,THEODORE 123-45-6789 NO - OTHER (0 VA EYE CLINIC

MAR 27,1998 OAT,WILLIE 123-45-6789 YES (001) VA EYE CLINIC

------------------------------

COUNT 13

### Field Visit Date(s) List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV FIELD VISIT DATES\] \[Synonym:10\]

> With this option you can obtain a printout of field visit date(s) counted by the AMIS report. This option allows you to enter a date range for this printout.

Example: Field Visit Date(s) List

Select Print VIST Roster Menu Option: <u>10</u> Field Visit Dates List

\* Previous selection: VIST FIELD VISIT DATE (AMIS) not null

START WITH VIST FIELD VISIT DATE (AMIS): FIRST// <u>\<ENTER\></u>

DEVICE: *\[Select Print Device\]*

Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

FIELD VISIT(S) DATE LIST APR 20,1998 13:34 PAGE 1

FIELD VIST

DATE NAME SSN VIST ELIGIBLE

-----------------------------------------------------------------------------------

AUG 9,1995 DASTARDLY,DICK 123-45-6789 YES (001)

JAN 1997 CLEAVER,THEODORE 123-45-6789 NO - OTHER (003)

SEP 8,1997 BODEAN,JETHRO 123-45-6789 INACTIVE

SEP 9,1997 BASS,EARNEST T. 123-45-6789 NO - OTHER (003)

JAN 30,1998 CLAMPETT,ELLIE MAE 123-45-6789 YES (001)

MAR 19,1998 JONES,MICK 123-45-6789 YES (001)

APR 18,1998 ZOOM,BILLY 123-45-6789 YES (001)

### VIST Roster Sorts…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ROSTER SORTS\] \[Synonym:11\]

> This menu includes various options for sorting the VIST Roster.

#### State

> \[ANRV STATE LIST\] \[Synonym:1\]

> This option provides an alphabetic printout of the entire VIST Roster by state of residence. You can sort by a particular state, or the report will print alphabetically by state.

#### City

> \[ANRV CITY LIST\] \[Synonym:2\]

> This option provides an alphabetic printout of the entire VIST Roster by city of residence. You can sort by a particular city, or the report will print alphabetically by city.

#### ZIP

> \[ANRV ZIP CODE LIST\] \[Synonym:3\]

> This option provides an alphabetic printout of the entire VIST Roster by ZIP code of residence. You can sort by a ZIP code, or the report will print numerically by ZIP code (smallest number listed first, i.e., 94304 would be listed before 94305).

#### County

> \[ANRV COUNTY LIST\] \[Synonym:4\]

> This option provides an alphabetic printout of the entire VIST Roster by county of residence. You can sort by a particular county, or the report will print alphabetically by county.

#### Address/Phone List

> \[ANRV ADDRESS LIST\] \[Synonym:5\]

> This option provides an alphabetic printout of the entire VIST Roster listing each veteran’s name, address, and phone number.

#### Birthdate

> \[ANRV BIRTH LIST\] \[Synonym:6\]

> This option provides an alphabetic printout of the entire VIST Roster by birthdate. You can sort by a particular month, or the report will print alphabetically by month (i.e., August would be listed before February).

#### Age

> \[ANRV AGE LIST\] \[Synonym:7\]

> This option provides an alphabetic printout of the entire VIST Roster by age. You can sort by a particular age, or the report will print numerically by age (i.e., youngest would be listed first).

#### Eye Diagnosis

> \[ANRV EYE DIAG PRINT\] \[Synonym:8\]

> This option provides an alphabetic printout of the entire VIST Roster by eye diagnosis. You can sort by a particular eye diagnosis, or the report will print alphabetically by diagnosis (i.e., Cataract would be listed before Retinitis Pigmentosa).

#### Eye Diagnosis Narrative

> \[ANRV EYE DIAG NARRATIVE\] \[Synonym:9\]

> This option provides an alphabetic printout of the entire VIST Roster by eye diagnosis narrative. This option uses the old eye diagnosis field (which was an open narrative) to help users complete an updated listing of the new eye diagnosis field. You can sort by a particular eye diagnosis, or the report will print alphabetically by diagnosis (i.e., Cataract would be listed before Retinitis Pigmentosa).

#### Fee Basis List

> \[ANRV FEE PT\] \[Synonym:10\]

> This option provides an alphabetic printout of VIST eligible veterans with Fee Bases eligibility.

#### Period of Service

> \[ANRV POS LIST\] \[Synonym:11\]

> This option provides an alphabetic printout of the entire VIST Roster by period of service. You can sort by a particular period of service, or the report will print alphabetically by period of service (i.e., Korean Era would be listed before Vietnam War).

#### Referral Source List

> \[ANRV REFERRAL SOURCE LIST\] \[Synonym:12\]

> This option provides an alphabetic printout of the entire VIST Roster by referral source (who referred veteran to VIST). A date range can be entered for this printout. You can sort by a particular referral source, or the report will print alphabetically by referral source.

#### Annual Review Dates List

> \[ANRV ANNUAL REVIEW LIST\] \[Synonym:13\]

> This option provides a printout of past VIST Reviews sorted by date. The printout includes the Review date, veteran’s name, last four social security numbers, and the status of the review and the type of review. A date range can be entered for this printout.

#### VIST Eligible (AMIS) List

> \[ANRV VIST ELIG LIST\] \[Synonym:14\]

> This option provides an alphabetic printout of the entire VIST Roster sorted by VIST eligible (AMIS) category (001,002,003, NO-NOT LEGALLY BLIND). The report includes the veteran’s name, social security number, and VIST Eligible (AMIS) category.

### AMIS Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV AMIS REPORT\] \[Synonym:12\]

> This option provides a printout of the calculated totals for every category from 001 through 049 of the semi-annual AMIS report. If the VIST Roster contains incomplete AMIS (mandatory category) information, this option will print a list of those records by patient name and social security number at the end of the AMIS report.

> This option may also be used to transmit the AMIS report to the program office.

> Double check all figures to ensure the accuracy of the results.

> Example: Transmission of AMIS Report

> Select Print VIST Roster Menu Option: <u>12</u> AMIS Report

> I WILL PRINT THE AMIS REPORT FOR PERIOD SPECIFIED.

> BEGINNING AMIS DATE: <u>T-10</u> (APR 10, 1998)

> ENDING AMIS DATE: <u>T</u> (APR 20, 1998)

> Do you want to email the AMIS report to the program office?(Y/N)? <u>Y</u> (Yes)

> Enter Average Man Hours Expensed by

> VIST Coordinator Per Week or ^ to exit: <u>?</u>

> Field 050 - Average Man Hours must be entered

> Must be a number between 1 and 9999.99

> Up to 2 decimal precision is allowed.

> Enter Average Man Hours Expensed by

> VIST Coordinator Per Week or ^ to exit: <u>1</u>

> Example: AMIS Report Printout

> Select Print VIST Roster Menu Option: <u>12</u> AMIS Report

> I WILL PRINT THE AMIS REPORT FOR PERIOD SPECIFIED.

> BEGINNING AMIS DATE: <u>T-10</u> (APR 10, 1998)

> ENDING AMIS DATE: <u>T</u> (APR 20, 1998)

> Do you want to email the AMIS report to the program office?(Y/N)? <u>N</u> (No)

> DEVICE: *\[Select Print Device\]*

> Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

> VISUAL IMPAIRMENT SERVICE TEAM (VIST)

> AMIS CODE SHEET

> FACILITY: BIRMINGHAM ISC (#14) Page 1

> Period Beginning: APR 10,1998

> Period Ending: APR 20,1998

> FIELD

> CODE TOTAL

> TOTAL VIST ELIGIBLE VETERANS 001 9

> NON VIST ELIGIBLE VETERANS

> Reviewed for BRC Attendance 002 2

> Other 003 3

> \_\_\_\_\_\_

> 14

> VISUAL ACTIVITY

> No Sight 004 1

> LP up to and including 5/200 005 0

> LP of 6/200 to 20/200 006 1

> Legally Blind by field restriction 007 2

> Not known 008 5

> \_\_\_\_\_\_

> 9

> MAJOR ACTIVITY

> Employed for pay 009 2

> Engaged in training or school 010 1

> Volunteer work (10 hrs/wk) 011 0

> Retired w/approp. activities 012 0

> Too ill or too disabled 013 2

> No well defined activity 014 1

> Not known 015 3

> \_\_\_\_\_

> 9

> PERIOD OF SERVICE

> WWI, Spanish American War 016 0

> WWII 017 1

> Korean 018 0

> Vietnam Era 019 0

> Peacetime 020 4

> Not known 021 4

> \_\_\_\_\_\_

> 9

> ENTITLEMENT

> Service Connected

> 0% only 022 1

> Comp. SC, 10% - SMC 023 0

> SC for blindness 024 5

> NSC Pension A&A/HB 025 0

> \_\_\_\_\_\_

> 6

> AGE CATEGORY

> Under 25 026 1

> 25-34 027 1

> 35-44 028 2

> 45-54 029 2

> 55-64 030 1

> 65-74 031 0

> 75-84 032 1

> 85 and over 033 1

> Not known 034 0

> \_\_\_\_\_\_

> 9

> TOTAL NUMBER OF VIST ANNUAL REVIEWS 035 0

> DECLINED VIST ANNUAL REVIEW 036 0

> 'NO SHOW' FOR VIST ANNUAL REVIEW 037 0

> VIST COORDINATOR AND COORDINATOR 038 1

> INITIATED FIELD VISITS

> VIST REFERRALS

> Blind Rehabilitation Center

> First Experience 039 0

> Additional Training 040 0

> Blind Rehabilitation Clinic

> First Experience 041 0

> Additional Training 042 0

> Other Non-VA Agencies

> First Experience 043 0

> Additional Training 044 0

> VETERANS NOT ACCEPTED FOR BLIND

> REHABILITATION

> Blind Rehabilitation Center 045 0

> Blind Rehabilitation Clinic 046 0

> VETERANS DISCHARGED DURING

> REPORT PERIOD

> Blind Rehabilitation Center 047 0

> Blind Rehabilitation Clinic 048 0

> Other Non-VA 049 0

> AVERAGE MAN HOURS EXPENSED BY 050 \_\_\_\_\_\_ hours

> VIST COORDINATOR PER WEEK

> PATIENTS WITH MISSING AMIS DATA

> ================================================================================

> DAVIS,PAULETTE 123456789

> ALLEN,PATRICK 123456789

### Incomplete AMIS Roster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV INCOMPLETE AMIS LISTING\] \[Synonym:13\]

> This option provides you with a printout of VIST Roster entries that have incomplete AMIS documentation in the ENTER/EDIT VIST Patient Record database. This option should be run prior to printing the AMIS report.

> Select Print VIST Roster Menu Option: <u>13</u> Incomplete AMIS Roster

> DEVICE: *\[Select Print Device\]*

> Do you want your output QUEUED? NO// <u>\<ENTER\></u> (NO)

report follows

> INCOMPLETE AMIS ROSTER APR 20,1998 13:46 PAGE 1

> NAME SSN

> --------------------------------------------------------------------------------

> ALLEN,PATRICK 123456789

> DAVIS,PAULETTE 123456789

# # Using the VIST Letter Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## *VIST Letter Menu*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ANRV LETTER MENU\] \[Synonym:4\]

The *VIST Letter Menu* allows you to edit and print letters and mailing labels for various functions related to VIST. This feature has been added as a convenience for VIST Coordinators. There are 5 different letter options:

- BRC Application Letter This is a cover letter for a Blind Rehabilitation Center (BRC) Application packet. This letter requires editing and is meant to be printed for a particular veteran.
- BRC Follow-up Letter This is a questionnaire sent to the veteran following blind rehabilitation training. It is used to assist the center or clinic in following-up on the veteran.
- Claim Letter This is a cover letter to a VARO when filing a claim on behalf of a VIST veteran. This letter is meant to be printed for a particular veteran.
- Invitation for VIST Review This is an invitation for blinded veterans to notify VIST that they would like to participate in an annual review. This letter satisfies the requirements of M-2, Part XXIII and is meant to be printed as a mass mailing.
- IRS Exemption Letter This letter is to be used for any other purpose needed by VIST.

### Edit VIST Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV ENTER/EDIT VIST LETTER\] \[Synonym:1\]

With this option, you can edit one or all of the VIST letters. The VIST letter choices include BRC Application Letter, BRC Follow-up Letter, Claim Letter, Invitation for VIST Review, and Miscellaneous.

Edit the letter as you would an e-mail or FORUM message. It is recommended that you switch to a full-screen editor to fully utilize the edit letter option.

> \*\*\*IMPORTANT\*\*\*

> Do *not* edit any of the special header features or fields that appear when editing a VIST letter. These areas of text are bracketed by the vertical line symbol (\|). Some of these fields are used to pull out identifying information on each veteran that will receive a letter or are also used to center a header. When data is bracketed with “\< \>”, you must edit this information by entering data that pertains to a particular veteran and your facility. You *must* remove the “\< \>” symbols while editing so that they do not appear in the letter.

> Example of Edit VIST Letter

Select VIST Menu Option: <u>4</u> VIST Letter Menu

Select VIST Letter Menu Option: <u>1</u> Edit VIST Letter

Select VIST LETTER NAME: <u>?</u>

Answer with VIST LETTER NAME

Choose from:

BRC APPLICATION LETTER

BRC FOLLOW-UP LETTER

CLAIM LETTER

INVITATION FOR VIST REVIEW

IRS EXEMPTION

You may enter a new VIST LETTER, if you wish

Answer must be 3-30 characters in length.

Select VIST LETTER NAME: <u>CLAIM</u> LETTER

REQUIRES PATIENT NAME: YES// <u>\<ENTER\></u>

TEXT OF LETTER:. . .

. . .

32\>3. If you have any questions or concerns regarding this request please

33\>don't hesitate to contact me at FTS: \<Enter Your Facility's Phone Number\>.

34\>Please send me a copy of your rating decision.

35\>

36\>

37\>

38\>

39\>

40\>\<Enter VIST Coordinator's Name\>, VIST Coordinator

EDIT Option: <u>33</u>

33\>don't hesitate to contact me at FTS: \<Enter Your Facility's Phone Number\>.

Replace <u>\<Enter Your Facility's Phone Number\></u> With <u>(111)222-3333</u>

Replace <u>\<ENTER\></u>

don't hesitate to contact me at FTS: (111)222-3333.

Edit line: <u>\<ENTER\></u>

EDIT Option: <u>\<ENTER\></u>

Select VIST LETTER NAME: <u>\<ENTER\></u>

### Print VIST Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV PRINT LETTER\] \[Synonym:2\]

> This option allows you to print one or more of the VIST letters.

> Select VIST Letter Menu Option: <u>2</u> Print VIST Letter

> Select Form Letter to Print: <u>CLAIM</u> LETTER

> If you wish to print a letter for a single patient

> Select Patient: <u>OAT,W</u>ILLIE 09-01-50 449345555

> DEVICE: *\[Select Print Device\]*

### Test Label Alignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV TEST LABEL\] \[Synonym:3\]

> This option allows the VIST Coordinator to print a test mailing label to check the alignment of the labels in the printer before printing other mailing labels.

### Print Mailing Labels by Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV MAIL LABELS\] \[Synonym:4\]

> With this option you can generate a set of mailing labels for mass mailings. You can print labels for all patients, or select patients. This option is designed to work with 3½” by 15/16”, fanfold strip (1 wide) size labels.

### Print Mailing Labels by City

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV LABELS BY CITY\] \[Synonym:5\]

> With this option you can generate a set of mailing labels for mass mailing by city. You can print labels for all patients, or select patients. This option is designed to work with 3½” by 15/16”, fanfold strip (1 wide) size labels.

### Print Mailing Labels by County

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV LABELS BY COUNTY\] \[Synonym:6\]

> With this option you can generate a set of mailing labels for mass mailing by county. You can print labels for all patients, or select patients. This option is designed to work with 3½” by 15/16”, fanfold strip (1 wide) size labels.

### Print Mailing Labels by State

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ANRV LABELS BY STATE\] \[Synonym:7\]

> With this option you can generate a set of mailing labels for mass mailing by state. You can print labels for all patients, or select patients. This option is designed to work with 3½” by 15/16”, fanfold strip (1 wide) size labels.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMIS Automated Management Information System
BRC Application Letter This is a cover letter for a Blind Rehabilitation Center (BRC) Application packet. This letter requires editing and is meant to be printed for a particular veteran.
BRC Follow-up Letter This is a questionnaire sent to the veteran following blind rehabilitation training. It is used to assist the center or clinic in following-up on the veteran.
Claim Letter This is a cover letter to a VARO when filing a claim on behalf of a VIST veteran. This letter is meant to be printed for a particular veteran.
Invitation for VIST Review This is an invitation for blinded veterans to notify VIST that they would like to participate in an annual review. This letter satisfies the requirements of M-2, Part XXIII and is meant to be printed as a mass mailing.
IRS Exemption Letter This letter is to be used for any other purpose needed by VIST.
Non-VIST Eligible Veterans Veterans that are legally blind, but not VIST eligible according to regulation. Veterans who meet this criteria should either be designated 002-NO-BRC or 003 NO-Other under the VIST ELIGIBLE (AMIS) field in the *Enter/Edit VIST Patient Record* option.
VARO Veterans Affairs Regional Office
VIST Visual Impairment Service Team

# Appendix A: VIST Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Example of a BRC Application Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

APR 20,1998

\<Enter Name of Chief (Routing Symbol)\>

Chief

Central Blind Rehabilitation Center

\<Enter Your VA Medical Center\>

\<Enter Street Address\>

\<Enter City, State ZIP\>

SUBJ: Application for Admission to a VA Blind Rehabilitation Program

1\. VETERAN: OAT,WILLIE 449345555

2\. VIST BRC PROGRAM RECOMMENDATION: CENTER

3\. PREVIOUS VA BLIND REHABILITATION: \<Enter Year and Place\>

4\. Enclosed with this cover letter is the following BRC application

information:

\* VAF 10-10 (signed)

\* VIS Team Assessment

\* Eye Examination

\* History and Physical Examination

\* Relevant Lab, EKG and X-ray Reports

\* Audiology Examination

\* Required VA Forms

5\. If you have any questions or concerns regarding this application,

please don't hesitate to contact me at FTS: \<Enter Your Facility’s Phone Number\>.

\<VIST Coordinator’s Name\>, VIST Coordinator

## Example of a BRC Follow-up Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Enter Your VA Medical Center\>

\<Enter Street Address\>

\<Enter City, State ZIP\>

APR 20,1998

Willie Oat

2700 Guadalupe St.

Austin, TX 76893

Dear Mr. Oat:

We hope you enjoyed your recent blind rehabilitation training and were

able to take some new found knowledge home with you that will make living

with your visual loss easier. For the benefit of the VIST Coordinator as

well as the Blind Rehabilitation Center or Clinic, we would appreciate your

assistance with answering the following questions as they relate to your

return from Blind Rehabilitation:

l\. Has there been a change in your vision or medical condition?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Has there been a change in your financial situation?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. How are you using the skills learned at the Blind Rehabilitation Center

or Clinic?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4\. What did your spouse or family member think of the family program at

the Blind Center or Clinic?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5\. Are you using the low vision aids issued to you? If so how?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6\. Are you continuing to have major problems coping with your vision loss?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7\. What are your goals and future plans?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Thank you for your assistance. Please return this completed letter in the

enclosed envelope.

Sincerely Yours,

\<VIST Coordinator’s Name\>, VIST COORDINATOR

## Example of a Claim Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs

> \<Enter Your VA Medical Center\>

> \<Enter Street Address\>

> \<Enter City, State ZIP\>

> APR 20,1998

> SUBJ: Re-evaluation of SC Condition

> 1\. Identifying Information: Veteran: OAT,WILLIE

> Claim \#: c-

> SS \#: 123456789

> 2\. Willie Oat was seen by the VIS Team on \<Enter Date Veteran was seen by VIS Team\>. He reports having decreased vision in both eyes and is requesting a re-evaluation of his current VA rating for vision loss. The veteran is currently rated \<Enter SC Percentage\> SC for vision loss. Our eye clinic found the veteran’s best corrected central acuity to be \<Enter Best Corrected Central Acuity\> in both eyes. Enclosed with this letter is a copy of the VIST eye exam.

> 3\. If you have any questions or concerns regarding this request please don't

> hesitate to contact me at FTS: \<Enter Your Facility’s Phone Number\>. Please send me a copy of your rating decision.

> \<VIST Coordinator’s Name\>, VIST Coordinator

## Example of Invitation for VIST Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Enter Your VA Medical Center\>

\<Enter Street Address

\<Enter City, State ZIP

APR 20,1998

Willie Oat

2700 Guadalupe St.

Austin, TX 76893

Dear Mr. Oat:

The Visual Impairment Service Team (VIS Team), \<Enter Your VAMC\> is

pleased to offer your annual appointment to evaluate your overall health

status and to make certain you are receiving the specialized benefits

available through the Department of Veterans Affairs. This appointment

includes the following: (1) A complete physical examination; (2) An eye

examination; (3) A hearing evaluation; (4) A review of your prosthetic

needs as they relate to your blindness; and (5) An interview with the VIST

Coordinator who may be able to assist you with specific problems as they

relate to your sight loss.

This annual review is entirely VOLUNTARY ON YOUR PART. IT DOES NOT IN ANY

WAY affect your status with the VA if you choose not to participate.

However, we sincerely encourage you to take advantage of this opportunity.

Please complete the form at the bottom of this letter and return it in the

enclosed prepaid envelope. Even if you choose not to request an

appointment, it would be appreciated if you would complete and return the

form.

I personally look forward to an opportunity to meet with you if I have not

already done so.

Sincerely,

\<VIST Coordinator’s Name\>, VIST Coordinator

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

IF YOU HAVE QUESTIONS, PLEASE CALL \<Enter VIST Coordinator’s Name\>, VIST COORDINATOR:

TELEPHONE \<Enter Your Facility Phone Number\>

NAME:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ADDRESS:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

HOME OR CONTACT TELEPHONE \#:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ BIRTHDATE:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SCHEDULE ME FOR 1998 : YES:\_\_\_ NO:\_\_\_ I PREFER THE MONTH OF:\_\_\_\_\_\_\_\_\_\_\_\_\_\_

I AM NOT INTERESTED IN A VIST REVIEW BECAUSE:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SIGNATURE:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ DATE:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Example of an IRS Exemption Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Enter Your VA Medical Center\>

\<Enter Street Address\>

\<Enter City, State ZIP\>

APR 20,1998

Willie Oat

2700 Guadalupe St.

Austin, TX 76893

To Whom It May Concern:

This is to advise that the veteran mentioned above is legally blind

according to records of this Medical Center. If there are any questions

with regard to the veteran's visual acuities or visual fields, you may

contact (Release of Information) at this Medical Center \<Enter Your Facility’s Phone Number\>. The veteran's legal blindness is permanent and irreversible.

\<Enter VIST Coordinator’s Name\>, VIST Coordinator

# Appendix B: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction to VIST Patient Review Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIST Patient Review software (VIST Patch ANRV, Version 4.0.5.1) collects Blind Rehabilitation data in two (2) interview formats in order to analyze Blind Rehabilitation services. By conducting interviews, the quality of care given to Blind Rehabilitation patients is greatly improved by improving the efficiency of the staff.

The VIST Patient Review application has been developed to improve the Blind Rehabilitation data collection process as well as to address VA Directive 2000-16 and VA Circular 96-057. In an effort to implement a user-friendly data collection environment, VIST Patient Review has been developed as a Graphical User Interface (GUI). Hence, this application is not integrated within VIST Version 4.0, (a roll-and-scroll application). However, it will be interfaced with Blind Rehabilitation Version 5.0, upon its release. The Blind Rehabilitation Version 5.0 upgrade is in the planning stage at the time of this document publication.

> **NOTE:** *For Text to Speech Software Users*: JAWS (Job Access with Speech) version 4.0 is the text to speech software package supported for integration with the VIST Patient Review 4.0.5.1. package. Default installation settings should be used (refer to the JAWS installation manual). If default settings are NOT used, choosing instead non-standard options, explanatory screen text within VIST Patient Review may not be automatically read. In the event that JAWS is not installed using default settings, entire screens of text may be read by using the \<Insert\> + B keys or the JAWS Review Cursor. Specific areas such as combo box contents or individual lines of text, can be read by using the \<Insert\> + Tab keys.

## Orientation of VIST Patient Review Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter key is illustrated as \<ENTER\> and is included when the \<ENTER\> keystroke is needed.

> The Tab key is illustrated as \<TAB\> and is included when the \<TAB\> keystroke is needed.

> The Delete key is illustrated as \<DELETE\> and is included when the \<DELETE\> keystroke is needed.

> The Up and Down arrow keys are illustrated as \< ↑ \> and \< ↓ \> and are included when the up and down arrow keystrokes are needed.

> The Page Up key is illustrated as \<Page Up\> and is included when the \<Page Up\> keystroke is needed.

> The Alt key is illustrated as \<ALT\> and is used in conjunction with other designated keys to quickly activate control keys (i.e. Next, Cancel, Review, Back) minimizing necessary keystrokes.

> Next = \<ALT\>+N  
> Back = \<ALT\>+B  
> Cancel = \<ALT\>+C  
> Review = \<ALT\>+R  
> Help = \<ALT\>+H

> The Escape key is illustrated as \<Esc\> and is included when the \<Esc\> keystroke is needed.

### Next\> Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/003.png)

> The Next\> Button moves the cursor to the next sequential page, maintaining provided settings.

> Using a mouse:

> 1\. Proceed to next screen by clicking the 'Next\>' button using a mouse.

> Using a keyboard:

> Use keyboard shortcut: \<ALT\>+N

> OR

> 1\. Select the 'Next\>' Button by pressing \<TAB\> until the 'Next\>' Button is selected.

> 2\. Proceed by pressing \<ENTER\>.

### OK Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/004.png)

> The OK Button applies entered values into an active dialog box, then closes the current window.

> Using a mouse:

> 1\. Apply entered information or choices by clicking the 'OK' button using a mouse.

> Using a keyboard:

> 1\. Select the 'OK' Button by pressing \<TAB\> until the 'OK' Button is selected.

> 2\. Proceed by pressing \<ENTER\>.

### \<Back Button 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/005.png)

> The \<Back Button is used to return to the previous screen.

> Using a mouse:

> 1\. Return to previous screen by clicking the '\<Back' button using a mouse.

> Using a keyboard:

> Use keyboard shortcut: \<ALT\>+B

> OR

> 1\. Select the '\<Back' Button by pressing \<TAB\> until the '\<Back' Button is selected.

> 2\. Proceed by pressing \<ENTER\>.

### Cancel Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/006.png)

> The Cancel Button is used to discard selected settings, terminating the current process, and returning the user to the first screen of the active area.

> Using a mouse:

> 1\. Clear current actions and return to section starting screen by clicking the 'Cancel' button using a mouse.

> Using a keyboard:

> Use keyboard shortcut: \<ALT\>+C

> OR

> 1\. Select the 'Cancel' Button by pressing \<TAB\> until the 'Cancel' Button is selected.

> 2\. Proceed by pressing \<ENTER\>.

### Exit Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/007.png)

> The Exit Button stops any further processing and closes the entire application.

> Using a mouse:

> 1\. Close the application completely by clicking the 'Exit' button using a mouse.

> Using a keyboard:

> 1\. Select the 'Exit' Button by pressing \<TAB\> until the 'Exit' Button is selected.

> 2\. Proceed by pressing \<ENTER\>.

### Radio Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vist-version-4-user-manual/008.png)

> A Radio Button, also referred to as an Option Button, represents the ability to select one option within a set of choices.

> Using a mouse:

> 1\. Choose an option by clicking within the circle to the left of the chosen option.

> Using a keyboard:

> 1\. Move to the area containing the radio buttons by pressing \<TAB\> until the area is selected.

> 2\. Choose an option by pressing the \< ↑ \> and \< ↓ \> (up/down arrow) keys.

> 3\. Proceed by pressing \<ENTER\>.

### Drop Down Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/009.png)

> Drop Down List Boxes allow selection of a single item from a list, while conserving space until the list is needed.

> Using a Mouse:

> 1\. Type the first few characters of the requested information in the empty text box. This will display a list of available options.

> 2\. Browse available options by sliding the scroll bar up or down the list.

> 3\. Make a choice by clicking on one of the options in the list, then pressing \<ENTER\>.

> Using a Keyboard:

> 1\. Type the first few characters of the requested information in the empty text box.

> 2\. Browse available options by pressing the \< ↑ \> and \< ↓ \> (up/down arrow) keys.

> 3\. Make a choice by highlighting the selected choice, then pressing \<ENTER\>.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vist-version-4-user-manual/010.png)

> An Electronic Signature is a unique code assigned to each System User by the System Administrator, allowing the submission & saving of Patient Review Interviews and/or sections of Patient Review Interviews.

> Using a Mouse:

> 1\. Type the Electronic Signature in the text box.

> 2\. Submit the section or Patient Review by pressing \<ENTER\>.

> Using a Keyboard:

> 1\. Type the Electronic Signature in the text box.

> 2\. Submit the active section or Patient Review by pressing \<ENTER\>.

### Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/011.png)

> The Review button allows the review of entered interview answers prior to saving them into a database. Reviewing must be done prior to entering an electronic signature.

> Using a Mouse:

> 1\. Click the Review button.

> 2\. Review answers, clicking on answer drop down boxes to change answers.

> 3\. Click the ‘Next\>’ button to proceed to the next page.

> 4\. Upon acceptance of all answers, enter the electronic signature in the appropriate text box to save the answers.

> Using a Keyboard:

> Use keyboard shortcut: \<ALT\>+R

> OR

1.  Press \<TAB\> until the ‘Review’ button is selected, then press \<ENTER\>.
2.  Review answers, using the \<TAB\> key to move between questions, and using the \< ↑ \> and \< ↓ \> (up and down arrow keys) to move through answer options.
3.  Select other answers by highlighting them, then moving to the next question pressing the \<TAB\> key.
4.  Proceed to the next page by pressing \<TAB\> until the Next\> button is selected, then pressing \<ENTER\>.
5.  Upon acceptance of all answers, enter the electronic signature in the appropriate text box to save the answers.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Logging into VIST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Choose the VIST Patient Review icon or .exe file from your desktop.

> 2\. Browse the names of the servers by clicking the drop down list arrow using a mouse or by pressing the up and down arrow keys.

> 3a. Select a server by clicking it with a mouse or selecting it using the up and down arrow keys (Refer to the System Administrator), then pressing \<ENTER\>.

> OR

> 3b. Cancel Login by clicking the 'Cancel' button with a mouse or by pressing \<ALT\> +C (Cancel button shortcut keys).

> NOTE: If you are not sure of the proper server to log into, please refer to the Network or System Administrator.

### VIST Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After initial login, the VIST Sign On screen displays. It provides important messages pertinent to VIST system users as well as confirming Access and Verify codes.

> 1\. Review the displayed message(s) in the dialog box.

> 2\. Type your assigned Access Code in the 'Access Code' text box then press Tab to go to the Verify Code text box.

> 3\. Type a valid Verify Code (Passcode) in the 'Verify Code' text box.

> 4a. Process entered data by clicking the 'OK' button using a mouse or by pressing \<ENTER\>.

> OR

> 4b. Cancel Signon by clicking the 'Cancel' button with a mouse or by pressing \<ALT\> +C (Cancel button shortcut keys).

> NOTE: If you are not sure of your Access Code or Verify Code please refer to your System Administrator or department administrative staff.

## Patient Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vist-version-4-user-manual/012.png)

> 1\. Type the first characters of the patient’s last name, or the patients last 4 of their SSN, or the patients full SSN, or the patient last name initial plus the last 4 of their SSN (Last 5) in the 'Select a Patient' text box. A list of matching and/or similar patient names will display.

> 2\. Choose a patient file by selecting a name in the alphabetic list. Do this by clicking on it using a mouse or by scrolling through the names using the up/down arrow keys.

> 3\. Activate choice by pressing \<ENTER\>.

> NOTE: The patient will only be chosen upon pressing the \<ENTER\> key.

> NOTE: To search for an entirely different name than the originally entered criteria, the current criteria must be deleted from the text box by selecting the entry then pressing the \<DELETE\> key or by backspacing several times until the contents are cleared.

> These actions will display a ‘Confirm Patient Selection’ screen, allowing confirmation or cancellation of the chosen patient.

### Confirming Patient Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ‘Confirm Patient Selection’ dialog box displays patient information of the chosen patient. It is used to verify that the displayed patient is the one to be activated; hence, the one data is collected from or about. The following data is displayed on the ‘Confirm Patient Selection’ screen:

> Name: Lists the chosen patient's name in Last Name, First Name format.

> Sex: Lists the sex of the chosen patient.

> Date of Birth: Lists the date of birth of the chosen patient in mm/dd/yyyy format as well as their calculated age

> Social Security Number: Lists the entire social security number of the chosen patient.

> Service Connected: Indicates if the patient is service connected using Yes or No answers.

> Type: Indicates the type of service the patient is or was affiliated with.

> Veteran: Indicates if patient is a veteran of the United States military using Yes or No answers.

> The Confirm Patient Selection screens display differently for Unrestricted access patient files, Restricted access patient files, and criteria searches that return multiple matches.

#### Unrestricted Access Patient File

> The Unrestricted Access Confirm Patient Selection screen displays patient information of the chosen unrestricted patient. It is used to verify that the displayed patient file is the one to be activated, hence, the one that data is collected from or about.

> ![](vist-version-4-user-manual/013.png)

> 1\. Verify displayed patient information.

> 2a. Continue activating the chosen patient by clicking the 'Next\>' button with a mouse or pressing \<TAB\> until the 'Next\>' button is selected then pressing \<ENTER\>.

> OR

> 2b. Return to the 'Patient Select' list to choose another patient by clicking the 'Cancel' button with a mouse or by pressing \<TAB\> until the 'Cancel' button is selected, then pressing \<ENTER\>.

#### Restricted Access Patient File

> This Restricted Access patient file dialog box displays patient information of a chosen Restricted Access patient file. It is used to verify that the displayed patient file is the desired one to be activated, and to inform the user of security issues involved.

> ![](vist-version-4-user-manual/014.png)

> 1\. Verify the non-sensitive patient information that is displayed (sensitive data is blocked at this point).

> 2a. Return to the 'Patient Select' list to choose another patient by clicking the 'Cancel' button with a mouse or by pressing \<TAB\> until the 'Cancel' button is selected, then pressing \<ENTER\>.

> OR

> 2b. Continue activating the chosen patient by clicking the 'I understand the security issues' button with a mouse or pressing \<TAB\> until the 'I understand the security issues' button is selected, then pressing \<ENTER\>. Pressing the 'I understand the security issues' button displays the 'Sensitive Record Access' warning screen which displays all of the sensitive data previously blocked, as well as notifying the assigned Station Security Officer that you are accessing this file.

> These actions will display the full screen of restricted patient information.

> ![](vist-version-4-user-manual/015.png)

> 3\. Review the full screen of information to verify that this is the desired patient file.

> 4\. Take note of the 'Restricted Record' warning.

> 5a. Return to the 'Patient Select' list to choose another patient by clicking the 'Cancel' button using a mouse or by pressing \<TAB\> until the 'Cancel' button is selected, then pressing \<ENTER\>.

> OR

> 5b. Continue activating the chosen patient by clicking the 'Next\>' button with a mouse or pressing \<TAB\> until the 'Next\>' button is selected, then pressing \<ENTER\>.

#### Multiple Matches

> If more than one patient file matches the search criteria, the Multiple Match Confirm Patient Selection dialog box is displayed. This dialog box lists detailed data for the most closely matching patient as well as a brief listing of other matching patients. All displayed data is used to choose the correct patient.

![](vist-version-4-user-manual/016.png)

> 1\. Verify the detailed patient information (this is information belonging to the most closely matching patient), as well as the other matching patient information, noting the patient which best matches the criteria.

> 2a. CONFIRM CHOICE OF DISPLAYED PATIENT (detailed data displayed at the top of dialog box) by clicking on the 'Next\>' button using a mouse or by pressing \<ALT\> +N (Next button shortcut keys).

> OR

> 2b. SELECT A DIFFERENT PATIENT by clicking the 'Cancel' button using a mouse or by pressing \<ALT\> +C (Cancel button shortcut keys).

## Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If more than one (1) action option is available for the contents of a patient file, the ‘Choose an Action to Perform’ screen displays. This screen allows users to indicate if they want to Create A New Patient Review or if they want to Complete Or Review An Existing Patient Review.

> ![](vist-version-4-user-manual/017.png)

> 1\. Make sure the desired action radio button is chosen – either ‘Create a new Patient Review’ or ‘Complete or Review a completed Patient Review’. Do this by clicking in the circle to the left of the action title with a mouse or by pressing \<TAB\> until the action title area is selected. Once highlighting the action title area, use the \< ↑ \> and \< ↓ \> (up/down arrow) keys to select the desired action title.

> 2\. Proceed by either pressing \<ENTER\> or clicking the 'Next' button with a mouse.

### Create a New Patient Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a New Patient Review: Creating a New Patient Review requires the user to choose the type of interview they want to conduct: a Rehabilitation or Annual Interview. The interview type determines the question layout while the assigned file security (i.e. Restricted or Unrestricted file) will determine the Confirmation screen that is displayed.

> ![](vist-version-4-user-manual/018.png)

#### #### Rehabilitation Interview: 

> Rehabilitation Patient Review Interviews consist of questions that address a patient’s physical abilities at a given point in time. These questions compare a patient’s abilities prior to and then after rehabilitation services. This interview is designed to be started and finished during one conversation between the patient and a Blind Rehabilitation staff member.

#### Annual Review: 

> Annual Review Interviews consist of extensive, categorized questions asked of each Blind Rehabilitation patient annually. The interview addresses all areas of a patient’s status, and allows the system user to stop the interview at any point, saving answers thus far selected. Incomplete interviews can be re-accessed at any time to complete unfinished sections or to review previously selected answers. Annual interviews can be re-accessed at any time to complete unfinished sections or to review previously selected answers.

> 1\. Proceed through each Patient Review by selecting answers from drop down boxes adjacent to each question, then by clicking the Next\> button with a mouse or by pressing \<ALT\>+N (Next button shortcut keys).  

> These actions will display the next page of questions. Repeat these steps for all pages.

> These actions will eventually display the ‘Completion’ screens.

### Review a Completed Patient Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When reviewing a completed Patient Review, it should be noted that originating date and time, status of interview, and the interview type are all used as criteria to choose a Patient Review. Refer to the ‘Select a Patient Review’ and the ‘Select a Patient Review section’ screens. After indicating the Patient Review and the Patient Review Section that you wish to access the ‘Review completed responses’ screen will display the submitted and saved questions & answers.

> ![](vist-version-4-user-manual/019.png)

1.  Review the displayed questions and answers.  
      
    Page layout displays the Section title (i.e. Living Skills), the ‘TASK’ which is a summary of the actual question (i.e. TASK: Communicated in writing), and the responses that were chosen and saved (i.e. 0-No Response).  
      
    NOTE: Rehabilitation Reviews (Pre/Post) contain Pre-Rehab and Post Rehab answers to each question, where as Annual Reviews only contain one (1) response to each question.

> 2a. Choose another existing Patient Review Interview for the active patient by selecting the ‘\<Back’ button using a mouse or by pressing the \<ALT\>+B keys (the Back button shortcut keys).

> OR

2.  2b. Select a different patient by selecting the ‘Cancel’ button using a mouse or by pressing the \<ALT\>+C keys (the Cancel button shortcut keys).

### Selecting a Patient Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Select a Review screen is used to select a Patient Review to be completed or reviewed.

> ![](vist-version-4-user-manual/020.png)

> 1\. Select a Patient Review by highlighting a row of data. Do this by clicking on a row of data using a mouse or by pressing \<TAB\> until the data list area is activated then press the \< \>or \< \> (up/down arrow) keys to select the chosen Patient Review.  

> NOTE: The JAWS Version 4.0 text to speech software will verbally indicate when a text to speech user tabs into the data list area.

> 2\. Proceed by clicking the ‘Next\>’ button with a mouse or pressing \<ALT\>+N (Next\> button shortcut keys).

> NOTE: ‘Incomplete’ Patient Reviews require that a section within the interview be indicated. ‘Complete’ Patient Reviews display one scrolling screen containing all submitted/saved answers.

### ### Selecting a Patient Review Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Choose A Section screen lists the sections within a chosen Patient Review that are available for completion or review. This screen also indicates the status of each section (i.e., Complete or Incomplete). Question sections depend upon type of interview (i.e. Annual or Rehabilitation).

> ![](vist-version-4-user-manual/021.png)

> 1\. Make sure the radio button for the desired section is chosen. Do this by clicking in the circle to the left of the section title using a mouse or by pressing \<TAB\> until the section title area is selected. Once highlighting the section title area, use the \< ↑ \> and \< ↓ \> (up/down arrow) keys to select the chosen section.

> 2\. Proceed by either clicking the ‘Next\>’ button with a mouse or pressing \<ALT\>+N (Next button shortcut keys).

> These actions will display the first page of the chosen section of the Incomplete Patient Review. If the section status is ‘Complete’ the ‘Review Completed Responses’ screen will be displayed.

## Patient Review Interviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Section Summaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are sections of questions found within Patient Reviews:

> OTHER HEALTH PROBLEMS:

> This section contains questions that confirm major medical conditions, self-administration of injectable and oral meds, and the ability of the patient to monitor his/her own blood sugar.

> LIVING SKILLS:

> This section contains questions that address the ability to communicate by writing, typing, or word processing, ability to pay own bills, maintain own bank account, measure using common measuring devices, use the internet or use e-mail.

> ORIENTATION AND MOBILITY:

> This section contains questions that address the need to avoid obstacles while walking and crossing streets.

> VISUAL SKILLS:

> This section contains questions that address the ability to watch TV comfortably, read magazines, newspapers, books, or mail.

> MANUAL SKILLS:

> This section contains questions that address the ability to assemble things, measure things, organize things, or perform home maintenance.

> BLIND REHAB EXPERIENCES:

> This section contains questions that address prior Blind Rehab experiences.

### ### Answering Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All Patient Reviews contain questions that display a drop down box listing available answer options.

> ![](vist-version-4-user-manual/022.png)

1.  Read each question thoroughly.
2.  Review answer options and choose answer using:

### Mouse:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click on the answer text box arrow at the right side of the answer text box. This action expands the answer option list.

> ![](vist-version-4-user-manual/023.png)

> *Expanded answer option list.*

> OR

### Keyboard:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Press \<TAB\> until the answer text box is selected.

> ![](vist-version-4-user-manual/024.png)

> *Selected answer text box using \<TAB\>.*

> Press the \< \>or \< \> (up/down arrow) keys to view answer options individually in the text box. Choose an answer by leaving that answer selected in the text box, tabbing to the next question.

> ![](vist-version-4-user-manual/025.png)

> *Answer options display in the text box*

> 3\. Repeat step 2 for each question.

> 4a. Proceed to next page of questions after all the answers are chosen. Click the ‘Next\>’ button using a mouse or press \<ALT\> + N (Next button shortcut keys).

> OR

> 4b. Choose a different patient review to work in by clicking the ‘\<Back’ button using a mouse or pressing \<ALT\>+B (Back button shortcut keys).

> OR

> 4c. Select an entirely new patient by clicking the ‘Cancel’ button using a mouse or pressing \<ALT\>+C (Cancel button shortcut keys).

### Completing Sections / Interviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are two (2) screens which display after answering all interview questions: 1.) the Completion Action screen and 2.) the Electronic Signature screen. These screens display upon completing questions in each section, at the end of Annual reviews, and at the end of Rehabilitation reviews.

> 1\. The Completion Action screen:  

> ![](vist-version-4-user-manual/026.png)  

> This screen allows the user to:

- Review questions and answers prior to answers being saved into the VistA database by selecting the ‘Choose to go back and review the interview from the beginning’ option.  
    
  OR
- Save the finished interview into the VistA database immediately by choosing ‘choose to go forward to the electronic signature page to save the review onto VistA’.
  1.  The Electronic Signature Screen:

> ![](vist-version-4-user-manual/027.png)

> The Electronic Signature screen is displayed after selecting the ‘Choose to go forward to the electronic signature page…’ option on the ‘Completion Action’ screen. This screen allows the user to:

- Send the interview answers into the VistA database by typing a valid electronic signature in the Electronic Signature text box then pressing \<ENTER\>. This will add a new record into the ANRV Patient Review file on the VistA database.

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The 'Signon cancelled by user' message will display when you cancel signin at the 'VIST Login' screen.

![](vist-version-4-user-manual/028.png)

> 1\. Click on 'OK' button using a mouse or press \<ENTER\>.

> These actions will close the login screen, closing the application completely.

> The 'Not a valid ACCESS CODE / VERIFY CODE pair' message will display when you enter invalid login information.

![](vist-version-4-user-manual/029.png)

> 1\. Click on the 'OK' button using a mouse or press \<ENTER\>.

> These actions will clear the invalid Access Code (Login Name) and Verify Code (Password) from the text boxes, allowing re-entry of codes.

> The 'Electronic Signature is Incorrect' or an 'Electronic Signature was not found' messages display when you attempt to proceed from the 'Completion' screen without entering a valid electronic signature.

![](vist-version-4-user-manual/030.png)

> 1\. Click on the 'OK' button using a mouse or by press \<ENTER\>.

> 2\. Re-enter a valid electronic signature in the Electronic Signature text box by clicking in the text box using a mouse, then typing a signature, or, if using the keyboard, press \<TAB\> until the text box is activated, then type a valid electronic signature in the text box.

> 'The Patient Review has been updated to complete' message will display after a Patient Review is completed and saved locally.

![](vist-version-4-user-manual/031.png)

*Dialog box displayed after completing a Patient Review*

> 1\. Click on the 'OK' button by using a mouse or by press \<ENTER\>.

> The 'Would you like to continue to the next section?' dialog box will display after completing each section of an Annual Patient Review. Proceed by answering the prompts.

![](vist-version-4-user-manual/032.png)

*Dialog box displayed after completing a section within an incomplete Patient Review.*

> 1\. Select the appropriate answer by clicking 'Yes' or 'No' using a mouse or press \<TAB\> to highlight the appropriate answer, then press \<ENTER\>.

> The 'Please complete all questions before continuing' message will display when you attempt to proceed to the next page of Patient Review questions without answering all questions on the page.

![](vist-version-4-user-manual/033.png)

> 1\. Click the 'OK' button using a mouse or by press \<ENTER\>.

> 2\. Select an answer from each of the question drop down boxes.

> 3\. Select the 'Next\>' button using a mouse or if using a keyboard press \<ALT\> +N (Next\> button shortcut keys).

> A standard dialog box is used to display numerous error messages at various intervals throughout the VIST Patient Review application. They include:

> 'An error occurred during lookup', 'An error occurred while receiving patient information', 'An error occurred while getting the list of outcomes', 'An error occurred while getting the Outcome text', 'An error occurred while retrieving the text', 'An error occurred while setting the record status', 'An error occurred while sending data', 'An error occurred while creating the Outcome', 'An error occurred while saving the Outcome', 'An error occurred during the update', 'Error Encountered', 'The Section was not saved properly', 'An error has occurred during transmission'.

![](vist-version-4-user-manual/034.png)

Required actions will depend upon the severity of the error. These errors may close the program completely, requiring a user to re-login. If the error does not shut down the program, some general guidelines are:

1\. Click on the 'OK' button using a mouse or press \<ENTER\>.

2a. Validate the data you are entering, then re-enter it into the provided area(s), then follow prompts.

OR

2b. Contact your System Administrator for further assistance.

### # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Additions to VIST Roster · 33

Address/Phone List · 35

Age · 36

AMIS Report Printout · 38

Annual Review Dates List · 37

B

Birthdate · 36

BRC Application Letter · 51

BRC Follow-up Letter · 52

C

City · 35

Claim Letter · 53

County · 35

D

Deceased Patients List · 32

Delete VIST Patient Record · 15

Delete VIST Referral Roster · 15

E

Edit VIST Letter · 44

Edit VIST Options Menu · 5

Enter/Edit Inactive VIST Roster · 10

Enter/Edit VARO Claims Roster · 11

Enter/Edit VIST Benefits Checklist · 12

Enter/Edit VIST Parameters · 14

Enter/Edit VIST Patient Record · 5

Enter/Edit VIST Referral Roster · 9

Entering and Editing VIST Options · 5

Example of a BRC Application Letter · 51

Example of a BRC Follow-up Letter · 52

Example of a Claim Letter · 53

Example of an IRS Exemption Letter · 55

Example of Invitation for VIST Review · 54

Eye Diagnosis · 36

Eye Diagnosis Narrative · 36

F

Fee Basis List · 36

Field Visit Date(s) List · 34

I

Icons · 1

Inactive VIST Roster List · 32

Incomplete AMIS Roster · 41

Individual Annual Review Record · 22

Individual Claims Record · 21

Individual Eye History · 20

Individual Patient Record · 17

Individual Referral Record · 19

Individual VIST Benefits Checklist · 23

Inpatient List · 30

Invitation for VIST Review · 54

IRS Exemption Letter · 55

O

Outpatient Appointment List · 31

P

Period of Service · 37

Print Individual Records · 17

Print Mailing Labels by City · 46

Print Mailing Labels by County · 46

Print Mailing Labels by Patients · 46

Print Mailing Labels by State · 47

Print VIST Letter · 46

Print VIST Roster Menu · 25

Printing Individual Records · 17

Printing the VIST Roster · 25

R

Referral Source List · 37

Related Manuals · 1

S

State · 35

T

Test Label Alignment · 46

U

Using the VIST Letter Menu · 43

V

VARO Claims List · 29

VIST Eligible (AMIS) List · 37

VIST Letter Menu · 43

VIST Referral List · 27

VIST Roster List · 25

VIST Roster List with Annual Review Date · 28

VIST Roster Sort · 35

Visual Impairment Services Teams (VIST) V. 4.0 Menu · 2

Z

ZIP · 35