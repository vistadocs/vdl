---
title: SD 5.3 586 ICD-10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 586 ICD-10
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3
group_key: "SD:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - diagnosis
  - clinic
  - date
  - code
  - codes
  - test
  - changes
  - sdamodo
page_count: 0
word_count: 1640
section_count: 14
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/icd-10_rn_sd_5_3_586.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/icd-10_rn_sd_5_3_586.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

ICD-10 Follow On Class 1 Software Remediation Project

VistA Scheduling

Release Notes

SD\*5.3\*586

![](sd-5-3-586-icd-10-release-notes/001.png)

July 2014

Office of Information and Technology

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [Routines](#routines)
  - [Print Clinic Installation Checklist](#print-clinic-installation-checklist)
  - [Setup Clinic Modified Routine (SDB)](#setup-clinic-modified-routine-sdb)
  - [Provider/Diagnosis Report (SDAMODO, SDAMODO2, SDAMODO3)](#providerdiagnosis-report-sdamodo-sdamodo2-sdamodo3)
  - [Routing Slips (SDROUT2)](#routing-slips-sdrout2)
- [Technical Information](#technical-information)
  - [Data Dictionary APIs (SDAMICD)](#data-dictionary-apis-sdamicd)
  - [Hospital Location (File \#44)](#hospital-location-file-44)
  - [Disability Condition (File \#31)](#disability-condition-file-31)
  - [SDSC Service Connected Changes (File \#409.48)](#sdsc-service-connected-changes-file-40948)
  - [Remote Procedure Calls](#remote-procedure-calls)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Veterans Health Information Systems and Technology Architecture (VistA) Scheduling package contained in patch SD\*5.3\*586.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch SD\*5.3\*586 makes the following changes to the VistA Scheduling application:

- Added modifications for the following reports:
  - Provider/Diagnosis Report \[SDAM PROVIDER/DIAGNOSIS REPORT\]
  - Routing Slips \[SDROUT\]
- ICD-10-CM replaces ICD-9-CM as the diagnostic coding system for outpatient encounters with an encounter date on or after the ICD-10 activation date and inpatient treatment episodes with a discharge date on or after the ICD-10 activation date.
- For a period of time, the VHA requires the use of dual code sets (ICD-9-CM, ICD-10-CM) to accommodate outpatient dates of service and inpatient discharge dates prior to and following the ICD-10 activation date as well as for reporting and research purposes.

The Scheduling Data Dictionary was modified for the following:  

- The input transform and screen in the Hospital Location File (#44), sub-file Diagnosis (#44.11) was changed to allow multiple versions of ICD codes and a default ICD code for each version.
- Field names and descriptions were updated in the Disability Condition File (#31), sub-file Related ICD Codes (#31.01) to replace the text “ICD9” with “ ICD”. 
- The file description was updated for  the SDSC Service Connected Changes File (#409.48) to replace the text “ICD9” with “ ICD”.

The following Remote Procedures were modified replacing the text “ICD9” with “ ICD”:

- SDOE GET PRIMARY DIAGNOSIS
- SDOE FIND DIAGNOSIS

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Scheduling manuals are posted on the VistA Documentation Library (VDL) [VistA Scheduling](http://www.va.gov/vdl/application.asp?appid=100) page.

The following VistA Scheduling user manuals are updated with changes for SD\*5.3\*586:

- PIMS Technical Manual
- User Manual – Supervisor Menu
- User Manual – Menus, Intro & Orientation

The following manuals do not require changes for this patch:

- PIMS User Manual – Outputs Menu
- Recall Reminder Technical & Security Guide
- Recall Reminder User Guide
- User Manual – Ambulatory Care Reporting
- User Manual – Appointment Menu
- PIMS Installation Guide

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses changes to VistA Scheduling routines.

## Print Clinic Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new routine allows users to print the Clinic Installation Checklist to assist them with entering corresponding ICD-10 codes for existing ICD-9 codes.

Print Clinic Installation Checklist

Clinic Installation Checklist April 12, 2012

Clinic ICD9 Code(s) Short Description Default

(ICD9)

-------------------- ------------ -------------------------

TESTCLINIC 800.00 CLOSED SKULL VAULT FX Y

ZTEST 330.0 LEUKODYSTROPHY N

Test Hospice 487.8 FLU W MANIFESTATION NEC Y

Test Hospice 487.1 FLU W RESP MANIFEST NEC N

Test Hospice V04.8 VACCIN FOR INFLUENZA N

Test Hospice V03.81 PROPHY VACCINE HIB N

Test Hospice V06.6 PROPHY VACC STREP PNEU&FL N

Test Hospice 482.2 H.INFLUENZAE PNEUMONIA N

Test Hospice 038.41 H. INFLUENAE SEPTICEMIA N

Test Hospice 041.5 H. INFLUENZAE INFECT NOS N

ZZAT TEST2 100.81 LEPTOSPIRAL MENINGITIS N

ZZAT TEST2 275.5 HUNGRY BONE SYNDROME Y

ZZAT TEST2 300.6 DEPERSONALIZATION DISORD N

SPEECH PATH – TEST V40.1 PROB WITH COMMUNICATION N

## Setup Clinic Modified Routine (SDB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no changes to the Setup Clinic functionality. The program accepts active ICD codes as enforced by the Data Dictionary screening and input transforms. One default ICD code is allowed for each ICD version.

The VistA Scheduling package adds the following new fields to the *Setup Clinic* option:

- Select DIAGNOSIS:
- DIAGNOSIS:
- DEFAULT DIAGNOSIS:

Set-Up Clinic

| Select OPTION NAME: SDBUILD Set up a Clinic               |
|-----------------------------------------------------------|
| Set up a Clinic                                           |
|                                                           |
| Select CLINIC NAME: CHY ENT TEST SCHEDPROV, ONE P         |
| NAME: CHY ENT TEST//                                      |
| ABBREVIATION: TEST//                                      |
| CLINIC MEETS AT THIS FACILITY?: YES//                     |
| SERVICE: MEDICINE//                                       |
| NON-COUNT CLINIC? (Y OR N): NO//                          |
| DIVISION: CHEYENNE VAMROC//                               |
| STOP CODE NUMBER: ENT//                                   |
| DEFAULT APPOINTMENT TYPE: REGULAR//                       |
| ADMINISTER INPATIENT MEDS?:                               |
| TELEPHONE: 7234//                                         |
| REQUIRE X-RAY FILMS?: YES//                           |
| REQUIRE ACTION PROFILES?: NO//                        |
| NO SHOW LETTER: CHEYENNE FAILED TO REPORT//           |
| PRE-APPOINTMENT LETTER: CHEYENNE APPT//               |
| CLINIC CANCELLATION LETTER: CHEYENNE CLINIC CANCELLED |
| //                                                        |
| APPT. CANCELLATION LETTER: CHEYENNE CANCELLED APPOINTMENT |
| //                                                        |
| ASK FOR CHECK IN/OUT TIME: NO//                       |
| Select PROVIDER: SchedProv,One//                      |
| PROVIDER: SchedProv,One//                                 |
| DEFAULT PROVIDER: YES//                               |
| Select PROVIDER:                                          |
| DEFAULT TO PC PRACTITIONER?: NO//                     |
| Select DIAGNOSIS: 428.0//                             |
| DIAGNOSIS: 428.0//                                    |
| DEFAULT DIAGNOSIS: Y//                                |
| Select DIAGNOSIS: E01.1//                             |
| DIAGNOSIS: E01.1//                                    |
| DEFAULT DIAGNOSIS: Y//                                |
| WORKLOAD VALIDATION AT CHK OUT: Y//                   |
| ALLOWABLE CONSECUTIVE NO-SHOWS: 2//                   |
| MAX \# DAYS FOR FUTURE BOOKING: 120//                 |
| START TIME FOR AUTO REBOOK: 9//                       |
| MAX \# DAYS FOR AUTO-REBOOK: 1//                      |
| SCHEDULE ON HOLIDAYS?:                                    |
| CREDIT STOP CODE:                                         |
| PROHIBIT ACCESS TO CLINIC?:                               |
| PHYSICAL LOCATION: A149A//                            |
| PRINCIPAL CLINIC:                                         |
| OVERBOOKS/DAY MAXIMUM: 30//                           |
| Select SPECIAL INSTRUCTIONS:                              |
| LENGTH OF APP'T: 30//                                 |
| VARIABLE APP'NTMENT LENGTH: YES, VARIABLE LENGTH      |
| //                                                        |
| AVAILABILITY DATE: 10/1/2014                          |

## Provider/Diagnosis Report (SDAMODO, SDAMODO2, SDAMODO3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the appointment occurs on or after the ICD-10 activation date, the ICD-10 code and the long description displays.

The Provider/Diagnosis Report routines SDAMODO, SDAMODO2, SDAMODO3 are modified to distinguish between ICD-9 and ICD-10 codes by properly displaying them in prompts and report headings, depending on the date for which the report is run.

Provider/Diagnosis Report Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PAT/APPT/CLINIC: PATIENT, TST Oct 2, 2014@16:31 CHY EMERGENCY ROOM</p>
<p>ICD CODE: ...There are 2 ICD CODES associated with this encounter.</p>
<p>- - E N C O U N T E R D I A G N O S I S (ICD10 CODES) - -</p>
<p>No. ICD10 DESCRIPTION PROBLEM LIST</p>
<p>1 E08.00 Diabetes mellitus due to underlying condition PRIMARY ORDERING</p>
<p>with hyperosmolarity without nonketotic</p>
<p>hyperglycemic-hyperosmolar coma (NKHHC)</p>
<p>MST:N</p>
<p>2 E08.01 Diabetes mellitus due to underlying condition RESULTING</p>
<p>with hyperosmolarity with coma</p>
<p>MST:N</p>
<p>3 E08.10 Diabetes mellitus due to underlying condition</p>
<p>with ketoacidosis without coma</p>
<p>MST:N</p>
<p>4 E08.11 Diabetes mellitus due to underlying condition</p>
<p>with ketoacidosis with coma</p>
<p>MST:N</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Routing Slips (SDROUT2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the appointment date is on or after the ICD-10 activation date, the VistA Scheduling package displays the ICD-10 label to the Routing Slip Report.

Select Outputs Option: Routing Slips

DO YOU WANT ROUTING SHEET FOR A SINGLE PATIENT? No// Y (Yes)

Select PATIENT NAME: SCHEDPATIENT, ONE 1-1-70 666229876 YES SC VETERAN

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

DEVICE: HOME// UCX/TELNET Right Margin: 80//

\*\*\* FACILITY: 1ALBANY

PAGE 1 OUTPATIENT ROUTING SLIP \*\*\* SERVICE CONNECTED 50% to 100% \*\*\*

SCHEDPATIENT, ONE APPOINTMENT DATE

666-22-9876

123 MAIN ST

ANYTOWN, STATE 11111

UNITED STATES

PSA: UNKNOWN

SC Percent: 60%

Disabilities: NONE STATED

Health Insurance: NO

Insurance COB Subscriber ID Group Holder Effective Expires

===========================================================================

No Insurance Information

\*\*CURRENT APPOINTMENTS\*\*

TIME CLINIC LOCATION

List diagnosis (ICD10) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

List any procedures performed during this clinic visit \_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Was treatment for SC Condition? \_\_Yes \_\_No

\*\*FUTURE APPOINTMENTS\*\*

DATE TIME CLINIC LOCATION

\*\*\* FACILITY: 1ALBANY

PAGE 2 OUTPATIENT ROUTING SLIP \*\*\* SERVICE CONNECTED 50% to 100% \*\*\*

SCHEDPATIENT, ONE APPOINTMENT DATE

666-22-9876

123 MAIN ST

ANYTOWN, STATE 11111

UNITED STATES

PSA: UNKNOWN

SC Percent: 60%

Disabilities: NONE STATED

Health Insurance: NO

Insurance COB Subscriber ID Group Holder Effective Expires

===========================================================================

No Insurance Information

10/03/2014 1:00 PM ZZAT TEST2

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Dictionary APIs (SDAMICD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDAMICD is a new routine containing the Application Program Interfaces (APIs) used in the Data Dictionary for HOSPITAL LOCATION:DIAGNOSIS fields.

F44SCRN1 - Screening Logic for File \#44, Multiple \#44.11, Field \#.01

F44SCRN2 - Screening Logic for File \#44, Multiple \#44.11, Field \#.02

DEFLTICD - Get Default ICD Code for Clinic

ICDVER - Get ICD Version

## Hospital Location (File \#44)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hospital location (File \#44) allows multiple versions of ICD codes, and a default ICD code for each version. A new field \[ICD Version (File \#44 Multiple \#44.11, Field \#.03)\] specifies the ICD version of a code.

STANDARD DATA DICTIONARY \#44.11 -- DIAGNOSIS SUB-FILE FEB 3,2012@17:55:15 PAGE 1

STORED IN ^SC(D0,"DX", SITE: TECHNICAL INTEGRATION SERVICE UCI: DEVESS,DEVESS

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

These are the diagnoses associated with this clinic. These diagnoses will be

displayed when updating the diagnosis through Appointment Management or Check

Out to assist the user in entering the correct diagnosis.

(NOTE: Kernel's File Access Security has been installed in this UCI.)

CROSS

REFERENCED BY: DEFAULT DIAGNOSIS(ADDX), DIAGNOSIS(B)

INDEXED BY: ICD VERSION & DIAGNOSIS (C)

## Disability Condition (File \#31)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Field names and descriptions are ICD version non-specific.

## SDSC Service Connected Changes (File \#409.48)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file description is ICD version non-specific.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The description is ICD version non-specific for the following files:

SDOE GET PRIMARY DIAGNOSIS

SDOE FIND DIAGNOSIS

*(This page included for two-sided copying.)*