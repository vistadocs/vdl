---
title: HBH*1*25 ICD - 10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD - 10
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: HBH
patch_ver: 1
patch_id: HBH*1*25
group_key: "HBPC:HBH:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - date
  - report
  - discharge
  - diagnosis
  - table
  - contents
  - admission
  - patient
  - codes
page_count: 0
word_count: 4055
section_count: 17
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/icd-10_rn_hbh_1_25.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/icd-10_rn_hbh_1_25.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

ICD-10 Follow On Class 1 Software Remediation

VistA Home Based Primary Care (HBPC)

Release Notes

HBH\*1.0\*25

![](hbh-1-25-icd-10-release-notes/001.png)

August 2014

Office of Information and Technology

Product Development

Table of Contents

*  
(This page intentionally left blank)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Dependencies](#dependencies)
  - [Documentation](#documentation)
- [Discharge Data Entry](#discharge-data-entry)
  - [Evaluation/Admission Data Report by Patient (80)](#evaluationadmission-data-report-by-patient-80)
  - [Discharge Data Report by Patient (80)](#discharge-data-report-by-patient-80)
  - [Admissions/Discharges by Date Range Report (132)](#admissionsdischarges-by-date-range-report-132)
  - [Patient Visit Data Report (80)](#patient-visit-data-report-80)
  - [Visit Data by Date Range Report (80)](#visit-data-by-date-range-report-80)
  - [ICD Code/Dx Text by Date Range Report (80)](#icd-codedx-text-by-date-range-report-80)
  - [Active Census with ICD Code/Text Report (132)](#active-census-with-icd-codetext-report-132)
  - [Form Errors Report (80)](#form-errors-report-80)
  - [Ability to Print HBPC Reports](#ability-to-print-hbpc-reports)
- [ICD-10 Searches](#icd-10-searches)
  - [Searches and Look-Ups](#searches-and-look-ups)
- [Known Issue](#known-issue)
- [Technical Information](#technical-information)
  - [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Home Based Primary Care (HBPC) package contained in patch HBH\*1\*25.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ICD-9-CM</p>
</blockquote></th>
<th><blockquote>
<p>ICD-10-CM</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3-5 characters</td>
<td>3-7 characters (not including the decimal)</td>
</tr>
<tr class="even">
<td>1st character is numeric (chapters 1-17) or alpha (E or V) (supplemental chapters)</td>
<td>Character 1 is alpha; character 2 is numeric;</td>
</tr>
<tr class="odd">
<td>2nd, 3rd, 4th and 5th characters are numeric</td>
<td>Characters 3–7 are alpha or numeric (alpha characters are not case sensitive)</td>
</tr>
<tr class="even">
<td>Decimal after first 3 characters</td>
<td>Decimal is used after third character</td>
</tr>
</tbody>
</table>

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

Patch HBH\*1\*25 makes the following changes to the HBPC application:

- Displays ICD-10-CM diagnosis codes and full descriptions / definitions.
- ICD-10 diagnosis code up to 8 characters (including the decimal point that follows the third character).
- Full descriptions/definitions.
- ICD-10 label.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following associated patches must be installed prior to installing Patch HBH\*1\*25.

- ICD\*18.0\*57
- LEX\*2.0\*80
- HBH\*1.0\*16
- HBH\*1.0\*22
- HBH\*1.0\*24

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HBPC manuals are posted on the VistA Documentation Library (VDL) page:

<http://www.va.gov/vdl/application.asp?appid=68>

The following HBPC user manuals are updated with changes for HBH\*1\*25:

- Home Based Primary Care Technical Manual
- Home Based Primary Care User Manual

The following manuals are not updated for ICD-10:

- Home Based Primary Care Installation Guide
- Home Based Primary Care Package Security Guide

# Discharge Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Date Of Interest is the Discharge Date.

The Discharge Data Entry option allows for entering, editing, and storing Discharge data for a patient including the diagnosis code (ICD-10 Code). The following screen shows all of the information including the Diagnosis for Discharge Data Entry.

Discharge Data Entry Data Display

Select HBPC Information System Menu Option: Discharge Data Entry

Select HBHC PATIENT NAME: HBPCPATIENT, FIVE 03-01-12 1-1-60 666878787

NO SC VETERAN

DISCHARGE DATE: APR 30,2012//

ELIGIBILITY @ DISCHARGE: Other Non-Service Connected (05)

//

MARITAL STATUS @ DISCHARGE: Married (1)//

LIVING ARRANGEMENTS @ D/C: With Spouse (2)//

DISCHARGE STATUS: Transferred to Other Provider (1)

//

TRANSFER DESTINATION: VA Provided Care (1)//

TYPE OF DESTINATION AGENCY: Not Determined (9)//

PRIMARY DIAGNOSIS @ DISCHARGE: HIV

14 matches found

1\. B20. Human Immunodeficiency Virus \[HIV\] Disease

2\. B97.35 Human Immunodeficiency Virus, Type 2 \[HIV 2\] as

the Cause of Diseases classified elsewhere

3\. O98.711 Human Immunodeficiency Virus \[HIV\] Disease

Complicating Pregnancy, first Trimester

4\. O98.712 Human Immunodeficiency Virus \[HIV\] Disease

Complicating Pregnancy, second Trimester

5\. O98.713 Human Immunodeficiency Virus \[HIV\] Disease

Complicating Pregnancy, third Trimester

6\. O98.719 Human Immunodeficiency Virus \[HIV\] Disease

Complicating Pregnancy, unspecified Trimester

7\. O98.72 Human Immunodeficiency Virus \[HIV\] Disease

Complicating Childbirth

8\. O98.73 Human Immunodeficiency Virus \[HIV\] Disease

Complicating the Puerperium

Press \<RETURN\> for more, "^" to exit, or Select 1-8:

9\. R75. Inconclusive Laboratory Evidence of Human

Immunodeficiency Virus \[HIV\]

10\. Z11.4 Encounter for Screening for Human

Immunodeficiency Virus \[HIV\]

11\. Z20.6 Contact with and (Suspected) Exposure to Human

Immunodeficiency Virus \[HIV\]

12\. Z21. Asymptomatic Human Immunodeficiency Virus \[HIV\]

Infection Status

13\. Z71.7 Human Immunodeficiency Virus \[HIV\] Counseling

14\. Z83.0 Family History of Human Immunodeficiency Virus

\[HIV\] Disease

Select 1-14:

## Evaluation/Admission Data Report by Patient (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Primary Diagnosis @ Adm field value allows you to display, add, or edit code based on the current active code set on the given Admission date.

Evaluation/Admission Data Entry Data Display

Select HBHC PATIENT NAME: HBPCPATIENT, FIVE 1-1-40 000000005 YES SC VETERAN

Enrollment Priority: GROUP 2 Category: IN PROCESS End Date:

Are you adding 'HBPCPATIENT,FIVE' as a new HBHC PATIENT (the 9TH)? No// Y

(Yes)

HBHC PATIENT DATE: T (On or after the ICD-10 Activation Date)

DATE: FEB 29,2000// \<RET\>

STATE CODE: ANYSTATE // \<RET\>

COUNTY CODE: ANYCOUNTY (031)// \<RET\>

ZIP CODE: 66611// \<RET\>

ELIGIBILITY @ EVALUATION: Service Connected Less Than 50% (03)// \<RET\>

BIRTH YEAR: 1940

\*\*\* Contact MAS if value is incorrect. \*\*\*

PERIOD OF SERVICE: Vietnam (07)// \<RET\>

SEX: Male (1)

\*\*\* Contact MAS if value is incorrect. \*\*\*

RACE: White (1)

\*\*\* Contact MAS if value is incorrect. \*\*\*

MARITAL STATUS @ EVALUATION: Married (1)// \<RET\>

LIVING ARRANGEMENTS @ EVAL: 1 Alone (1)

LAST AGENCY PROVIDING CARE: 1 VA Provided Care (1)

TYPE OF LAST CARE AGENCY: 5 Hospice (5)

ADMIT/REJECT ACTION: 1 Admit to HBHC (1)

PRIMARY DIAGNOSIS @ ADMISSION: E57.123 MAL NEO PANCREAS BODY COMPLICATION/COMORBIDITYSECONDARY DIAGNOSES @ ADM: F00.1 DementiaD20.24 Neurological DisorderB01.1 Infectious Disease

VISION @ ADMISSION: 2 Moderate Loss (2)

HEARING @ ADMISSION: 2 Moderate Loss (2)

EXPRESSIVE COMMUNICATION @ ADM: 1 Speaks and is Usually Understood (1)

RECEPTIVE COMMUNICATION @ ADM: 1 Usually Understands Oral Communication (1)

BATHING @ ADMISSION: 2 Receives Help (2)

DRESSING @ ADMISSION: 2 Receives Help (2)

TOILET USAGE @ ADMISSION: 2 Receives Help (2)

TRANSFERRING @ ADMISSION: 2 Receives Help (2)

EATING @ ADMISSION: 2 Receives Help (2)

WALKING @ ADMISSION: 3 Not Done or Done Without Patient Participation (3)

BOWEL CONTINENCE @ ADMISSION: 2 Incontinent Occasionally (2)

BLADDER CONTINENCE @ ADMISSION: 3 Incontinent or Ostomy/Catheter Not Self Care

\(3\)

MOBILITY @ ADMISSION: 3 Confined Indoors, Not Bed Disabled (3)

ADAPTIVE TASKS @ ADMISSION: 2 Requires Help (2)

BEHAVIOR PROBLEMS @ ADMISSION: 1 Does Not Exhibit This Characteristic (1)

DISORIENTATION @ ADMISSION: 1 Does Not Exhibit This Characteristic (1)

MOOD DISTURBANCE @ ADMISSION: 2 Exhibits This Characteristic (2)

CAREGIVER LIMITATIONS @ ADM: 1 Minimal or None (1)

PERSON COMPLETING EVL/ADM FORM: 100 HBPCPROVIDER,TWO HINES ISC

...OK? Yes// \<RET\> (Yes)

DATE EVAL/ADM FORM COMPLETED: T (FEB 29, 2014)

CASE MANAGER: 100 HBPCPROVIDER,TWO HINES ISC

## Discharge Data Report by Patient (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Diagnosis @ D/C field value allows you to display, add, store and edit code based on the current active code set on the Discharge date.

Select HBHC PATIENT NAME: HBPCPATIENT,SEVEN 5-20-66 000000007

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

01-03-14

DISCHARGE DATE: T (On or after the ICD-10 Activation Date)

ELIGIBILITY @ DISCHARGE: Service Connected 50% or More (01)

// \<RET\> Service Connected 50% or More (01)

MARITAL STATUS @ DISCHARGE: 1 Married (1)

LIVING ARRANGEMENTS @ D/C: 2 With Spouse (2)

DISCHARGE STATUS: 2 Anticipated Institutionalization (2)

TRANSFER DESTINATION: 2 Non VA Care (2)

TYPE OF DESTINATION AGENCY: 3 Nursing Home (3)

PRIMARY DIAGNOSIS @ DISCHARGE: E57.123 MAL NEO PANCREAS BODYSECONDARY DIAGNOSES @ D/C: F00.1 DementiaD20.24 Neurological DisorderB01.1 Infectious DiseaseE02.23 EARLY SKIN YAWS NEC

VISION @ DISCHARGE: 3 Severe Loss (3)

HEARING @ DISCHARGE: 3 Severe Loss (3)

EXPRESSIVE COMMUNICATION @ D/C: 4 Uses Only Gestures, Grunts, or Primitive Symbols (4)

RECEPTIVE COMMUNICATION @ D/C: 5 Does Not Understand (5)

BATHING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

DRESSING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

TOILET USAGE @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

TRANSFERRING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

EATING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

WALKING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

BOWEL CONTINENCE @ DISCHARGE: 3 Incontinent or Ostomy/Catheter Not Self Care (3)

BLADDER CONTINENCE @ DISCHARGE: 3 Incontinent or Ostomy/Catheter Not Self Care (3)

MOBILITY @ DISCHARGE: 3 Confined Indoors, Not Bed Disabled (3)

ADAPTIVE TASKS @ DISCHARGE: 2 Requires Help (2)

BEHAVIOR PROBLEMS @ DISCHARGE: 1 Does Not Exhibit This Characteristic (1)

DISORIENTATION @ DISCHARGE: 2 Exhibits This Characteristic (2)

MOOD DISTURBANCE @ DISCHARGE: 2 Exhibits This Characteristic (2)

CAREGIVER LIMITATIONS @ D/C: 3 Moderately Severe (3)

PERSON COMPLETING D/C FORM: 100 HBPCPROVIDER,TWO HINES ISC

...OK? Yes// \<RET\> (Yes)

## Admissions/Discharges by Date Range Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The column header showing the code set for the Date Range report displays based on the following:

> **NOTE:** The column header in various ICD Code reports is customized to match the type of ICD code that appears in the report. If the report only covers ICD-9 era dates, the column header is ICD9; if the report covers only ICD-10 era dates, the column header is ICD10; and if the report covers both ICD-9 and ICD-10 era dates, the column header is ICD.

Select Admissions or Discharges: (A/D): Admissions

Beginning Report Date: 3/21/2014 (MAR 21, 2014)

Ending Report Date: T (MAR 28, 2014)

DEVICE: HOME// (Enter a device capable of printing 132 columns)

\>\>\> HBPC Admissions by Date Range Report \<\<\< Page: 1

Run Date: MAR 28, 2000 Date Range: MAR 21, 2014 to MAR 28, 2014

Admission Date Patient Name SSN ICD10 Code Diagnosis Text

11-03-14 HBPCPATIENT,EIGHT 000-00-0008 571.49 CHRONIC HEPATITIS NEC

---------------------------------------------------------------------

12-02-14 HBPCPATIENT1,ONE 000-00-0011 230.2 CA IN SITU STOMACH

---------------------------------------------------------------------

12-03-14 HBPCPATIENT,NINE 000-00-0009 231.0 CA IN SITU LARYNX

---------------------------------------------------------------------

01-03-14 HBPCPATIENT,TWO 000-00-0002 147.8 MAL NEO NASOPHARYNX NEC

---------------------------------------------------------------------

02-29-14 HBPCPATIENT,FIVE 000-00-0005 157.1 MAL NEO PANCREAS BODY

---------------------------------------------------------------------

03-09-14 HBPCPATIENT1,TWO 000-00-0012 157.3 MAL NEO PANCREATIC DUCT

---------------------------------------------------------------------

=====================================================================

Total Admissions: 6

=====================================================================

==== End of Report ====

## Patient Visit Data Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on the current active code set, the report shows either ICD-9 or ICD-10 code with description in the visit data.

Beginning Report Date: 2/1/14 (FEB 01, 2014)

Ending Report Date: T (FEB 29, 2014)

DEVICE: HOME// (Enter a device)

\>\>\> HBPC Patient: HBPCPATIENT,SEVEN 000-00-0007 Visit Data Report \<\<\< Page: 1

Run Date: FEB 29, 2014 Date Range: FEB 01, 2014 to FEB 29, 2014

Admission Primary Diagnosis: E57.123 MAL NEO PANCREAS BODY

====================================================================

Visit Date: 02-10-2014 Prov No.: 102 Prov Name: HBPCPROVIDER,TWO

Diagnosis: I61.311 MAL NEO CARTILAGE LARYNX

CPT Code: 92502 EAR AND THROAT EXAMINATION

Modifier: - 26 PROFESSIONAL COMPONENT

--------------------------------------------------------------------

==== End of Report ====

## Visit Data by Date Range Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on the current active code set, the report shows either ICD-9 or ICD-10 code with description in the visit data.

Beginning Report Date: 5/29 (MAY 29, 2014)

Ending Report Date: 6/2 (JUN 02, 2014)

\>\>\> HBPC Visit Data by Date Range Report \<\<\< Page: 1

Provider: HBPCPROVIDER,TWO (152)

Run Date: JUN 02, 2000 Date Range: MAY 29, 2014 to JUN 02, 2014

Admission Primary Diagnosis: E57.123 MAL NEO PANCREAS BODY

============================================================================

Visit Date: 06-02-2014 Patient Name: HBPCPATIENT,EIGHT Last 4: 0008

Diagnosis: I61.311 MAL NEO CARTILAGE LARYNX

CPT Code: 92502 EAR AND THROAT EXAMINATION

Modifier: - 26 PROFESSIONAL COMPONENT

Modifier: - 77 REPEAT PROCEDURE BY ANOTHER PHYSICIAN

============================================================================

Provider: HBPCPROVIDER,TWO (152) Visits Total: 1

## ICD Code/Dx Text by Date Range Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the date range you enter is after the ICD-10 activation date, then the column header states "ICD10 Code/Diagnosis Text". If date range includes the ICD-10 activation date, then the column header states "ICD Code/Diagnosis Text".

If you do not wish to include all the ICD Diagnosis codes, then the"Select ICD Diagnosis:" prompt asks for ICD-10 codes if the date range is after the ICD-10 activation date. If date range includes the ICD-10 activation date, then the prompt inputs both ICD-9 and ICD-10 codes.

> **NOTE:** This report has been renamed to “icd Code/Dx Text by Date Range Report”.

Select Reports Menu Option: icd Code/Dx Text by Date Range Report (80)

Beginning Report Date: 1/1/14 (JAN 01, 2014)

Ending Report Date: t (APR 05, 2014)

Do you wish to include ALL ICD Diagnosis Codes on the report? No// (No)

Select ICD DIAGNOSIS: diet

12 matches found

1\. E60. Dietary zinc deficiency (10/01/2013) (Pending)

2\. E58. Dietary calcium deficiency (10/01/2013) (Pending)

3\. E59. Dietary selenium deficiency (10/01/2013) (Pending)

4\. D52.0 Dietary folate deficiency anemia (10/01/2013)

(Pending)

5\. Z71.3 Dietary counseling and surveillance (10/01/2013)

(Pending)

Press \<RETURN\> for more, '^' to exit, or Select 1-5:

6\. Z72.4 Inappropriate diet and eating habits (10/01/2013)

(Pending)

7\. D51.3 Other dietary vitamin B12 deficiency anemia

(10/01/2013) (Pending)

8\. Z91.11 Patient's noncompliance with dietary regimen

(10/01/2013) (Pending)

9\. K52.2 Allergic and dietetic gastroenteritis and colitis

(10/01/2013) (Pending)

10\. O24.430 Gestational diabetes in the puerperium, diet

controlled (10/01/2013) (Pending)

Press \<RETURN\> for more, '^' to exit, or Select 1-10:

11\. O24.410 Gestational diabetes mellitus in pregnancy, diet

controlled (10/01/2013) (Pending)

12\. O24.420 Gestational diabetes mellitus in childbirth, diet

controlled (10/01/2013) (Pending)

Select 1-12: 12

Do you wish to include ALL codes within category O24? Yes// (Yes)

Select ICD DIAGNOSIS:

## Active Census with ICD Code/Text Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the date range is after the ICD-10 activation date, then the column header states "ICD10 Code". If the date range includes the ICD-10 activation date, then the column header states "ICD Code".

Select OPTION NAME: HBHCRP18 Active Census with ICD Code/Text Report (132)

Active Census with ICD Code/Text Report (132)

Beginning Report Date: 1/1/13 (JAN 01, 2013)

Ending Report Date: T (APR 05, 2015)

\>\>\> HBPC Active Census with ICD Code/Text Report \<\<\< Page: 1

Run Date: APR 05, 2015

Date Range: JAN 01, 2013 to APR 05, 2015

Patient Name Last Four Date

ICD10 Code

Diagnosis Text

===============================================================================

HBPCPATIENT, ONE 0001 JAN 05, 2014

436\.

CVA

-------------------------------------------------------------------------------

HBPCPATIENT, TWO 0002 JAN 06, 2014

428.0

CONGEST HEART FAIL UNSPECIFIED

-------------------------------------------------------------------------------

HBPCPATIENT, THREE 0003 JAN 27, 2014

564.1

IRRITABLE BOWEL SYNDROME

--------------------------------------------------------------------------------

HBPCPATIENT, FOUR 0004 JAN 04, 2014

250.40

DMII RENL NT ST UNCNTRLD

--------------------------------------------------------------------------------

HBPCPATIENT, FIVE 0005 JAN 05, 2014

185\.

MALIGN NEOPL PROSTATE

--------------------------------------------------------------------------------

HBPCPATIENT, SIX 0006 JAN 25, 2014

429.1

MYOCARDIAL DEGENERATION

---------------------------------------------------------------------------------

=================================================================================

Active Census Total: 6

=================================================================================

==== End of Report ====

## Form Errors Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on the current active code set, the report shows either ICD-9 or ICD-10 code with description in the visit data.

Select OPTION NAME: HBHCRP1

1 HBHCRP1 Form Errors Report (80)

2 HBHCRP10 Program Census Report (80)

3 HBHCRP11 Team Census Report (80)

4 HBHCRP12 Episode of Care/Length of Stay Report (80)

5 HBHCRP16 Rejections from HBPC Program Report (132)

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 HBHCRP1 Form Errors Report (80)

Form Errors Report (80)

DEVICE: HOME// UCX/TELNET

\>\>\> HBPC Form Errors Report \<\<\< Page: 1

Run Date: APR 05, 2012

Patient Last

File IEN Patient Name Four Visit Clinic Name Date Form

=============================================================================

\`7171882 HBPCTEST,TWO 0201 HBPC Test Clinic APR 04, 2012@14:15 Visit

Error: Provider Missing

ICD: 244.0 POSTSURGICAL HYPOTHYROID

ICD: 215.7 BENIGN NEO TRUNK NOS

CPT: 85025 COMPLETE CBC W/AUTO DIFF WBC QTY: 1 CPT Code Prov \#:

-----------------------------------------------------------------------------

\`7171881 HBPCTEST,ONE 0101 HBPC Test Clinic APR 04, 2012@15:00 Visit

Error: HBHC Provider Number Missing

Provider: HBPCPROVIDER, ONE Encounter Prov \#: 1946

ICD: \* 428.0 CONGEST HEART FAIL UNSPECIFIED \* Primary Dx

ICD: 496. CHR AIRWAY OBSTRUCT NEC

CPT: 85025 COMPLETE CBC W/AUTO DIFF WBC QTY: 1 CPT Code Prov \#: 1946

-----------------------------------------------------------------------------

> **NOTE:** Please use Appointment Management to Correct Visit Errors. Run

Edit Form Errors Data option when corrections are complete.

==== End of Report ====

## Ability to Print HBPC Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA HBPC package prints the ICD-10 diagnosis code up to 8 characters (including the decimal point that follows the third character) for all known Secondary Diagnosis @ Adm. for the Patient on the various Data Report by Patient Reports.

> **NOTE:** This report is now titled “HBPC Active Census with ICD Code/Text Report”.

HBPC Active Census with ICD10 Code/Text Report

Beginning Report Date: 1/1/2013 (JAN 01, 2013)

Ending Report Date: 12/31/2013 (DEC 31, 2013)

DEVICE: HOME// (Enter a device that prints 132 columns)

\>\>\> HBPC Active Census with ICD10 Code/Text Report \<\<\< Page: 1

Run Date: MAR 29, 2014 Date Range: JAN 01, 2013 to DEC 31, 2013

Patient Name SSN Date ICD Code Diagnosis Text

=====================================================================

HBPCPATIENT,EIGHT 000-00-0008 NOV 03, 2013 E16.844 CHR PULMON HEART DIS NEC

---------------------------------------------------------------------

HBPCPATIENT1,SIX 000-00-0016 DEC 02, 2013 E16.844 CHR PULMON HEART DIS NEC

---------------------------------------------------------------------

---------------------------------------------------------------------

Active Census Total: 64

==== End of Report ====

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HBPC package provides the ability to search on ICD-10-CM diagnosis codes and ICD-10-PCS procedure codes.

> **NOTE:** Existing ICD-9 functionality has not changed.

## Searches and Look-Ups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Date Of Interest is the Admission Date.

The software utilizes new Application Program Interfaces (APIs) to perform the Look-ups and searches. The searches may return more matches than can be displayed on a single screen.

1.  To perform a search or look-up, you can enter any of the following:
- A valid ICD-10 code.
- A partial ICD-10 code.
- A partial description of a valid ICD-10 code.
2.  If you select a valid ICD-10 code, the software will continue to the next function.
3.  If you select one partial ICD-10 code (i.e., a branch node denoted by a trailing "-" ), all of the immediate descendants of that branch node display.
4.  Step 3 repeats until you select a valid ICD-10 code.

The example below shows the new ICD-10 search API drilling down two levels to select a valid ICD-10 code.

Step \#1: You enter the first three characters (F14) of a valid ICD-10 code.

Result: The software displays the total number of entries that match the three character input (20), a numbered list of matching codes, their descriptions, and designates leaf nodes matches.

ICD-10 Diagnosis code: F14 \<enter\>

20 matches found

1\. F14.10 Cocaine Abuse, Uncomplicated

2\. F14.12- Cocaine abuse with intoxication

3\. F14.14 Cocaine Abuse with Cocaine-Induced Mood Disorder

4\. F14.15- Cocaine abuse with cocaine-induced psychotic disorder

5\. F14.18- Cocaine abuse with other cocaine-induced disorder

6\. F14.19 Cocaine Abuse with unspecified Cocaine-Induced Disorder

7\. F14.20 Cocaine Dependence, Uncomplicated

8\. F14.21 Cocaine Dependence, in Remission

Step \#2: You review the list and select entry \#4 (F14.15-), which is a branch node.

Result: The software displays the total number of entries that match the partial ICD-10 code F14.15, a numbered list of matching code(s), their descriptions, and whether the entry is a branch (-) or a leaf node. In this example, there are three matches and all three of them are valid ICD-10 codes (no “-“ at the end of the code).

3 matches found

1\. F14.150 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder with Delusions (ICD-10-CM F14.150)

2\. F14.151 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder with Hallucinations (ICD-10-CM F14.151)

3\. F14.159 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder, unspecified (ICD-10-CM F14.159)

Select 1-3: 2 \<enter\>

Step \#3: Review the list and select entry \#2 (F14.151), which is a valid ICD-10 code.

Result: The software displays the valid ICD-10 code as well as the code's full description on the next line.

ICD-10 Diagnosis code: F14.151

ICD-10 Diagnosis description: Cocaine Abuse with Cocaine-Induced Psychotic Disorder with Hallucinations (ICD-10-CM F14.151)

If the Admission date is updated, and that the new active coding system is different from the previously entered Primary Diagnosis @ Admission's coding system, then the Primary Diagnosis is deleted.

# Known Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICD-10 Class I Remediation project will update VistA to include the ICD-10 Diagnosis and Procedure codes. The first patches to be delivered by this project will be the STS patches ICD\*18.0\*57 and LEX\*2.0\*80 which will include both the ICD-10 Diagnosis and Procedure codes along with new or updated APIs that will be used by the other VistA applications to select, retrieve and display these new codes.

Several VistA applications do not currently utilize code set versioning. Those applications are Prosthetics, Home Based Primary Care, and Laboratory: Anatomic Pathology. As a result, these applications currently allow inactive ICD-9 codes to be displayed and selected for ICD-9 dates of service.

During the interim, after the installation of the STS ICD-10 Class I Remediation patches and prior to the ICD-10 Implementation date (10/01/2014), these applications will also allow the display and selection of inactive ICD-10 codes including statuses of (Inactive) or (Pending). The users of these applications should use CAUTION to select ICD-9 or ICD-10 codes that are appropriate and active.

The following examples show how the software appears in these applications:

EXAMPLE 1: Inactive ICD-9 codes

The warning (Inactive) appears at the end of the short description.

Select ICD DIAGNOSIS: 100.0// 488.1

4 matches found

1\. 488.1 FLU DT IDEN H1N1 VIRUS (Inactive)

2\. 488.11 FLU DT 2009 H1N1 W PNEU (Major CC)

3\. 488.12 FLU-2009 H1N1 W OTH RESP

4\. 488.19 FLU-2009 H1N1 W OTH MAN (Inactive)

Select 1-4:

Select ICD DIAGNOSIS:

EXAMPLE 2: Inactive ICD-10 codes

The warning (Pending) appears at the end of the short description.

Select ICD DIAGNOSIS: 100.0// A27.

4 matches found

1\. A27.0 Leptospirosis icterohemorrhagica (10/01/2014) (Pending)

2\. A27.81 Aseptic meningitis in leptospirosis (10/01/2014) (Pending)

3\. A27.89 Other forms of leptospirosis (10/01/2014) (Pending)

4\. A27.9 Leptospirosis, unspecified (10/01/2014) (Pending)

When creating or editing records dated after the ICD-10 Activation Date, the software will correctly screen out both the inactive ICD-9 and inactive ICD-10 codes.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text (?) and extended help text (??, ???) is included for prompts related to ICD-10 codes. Below are screen displays of the new HBPC help text feature in Evaluation/Admission Data Entry and Discharge Data Entry.

HBPC Help Text Display for Evaluation/Admission Data Entry

          Evaluation/Admission Data Entry

          Discharge Data Entry

          Reports Menu ...

          Transmission Menu ...

          Manager Menu ...

          Medical Foster Home (MFH) Menu ...

Select HBPC Information System Menu Option: evaluation/Admission Data Entry

Select HBHC PATIENT NAME: HBPCTEST, ONE       7-4-28    000331029     YES     SC VETERAN      DC

Enrollment Priority: GROUP 1    Category: ENROLLED      End Date:

         ...OK? Yes//   (Yes)

     1   HBPCTEST, ONE       01-20-09

     2   HBPCTEST, ONE      01-25-13

CHOOSE 1-2: 2  HBPCTEST, ONE     01-25-13

\*\*\*  Record contains Discharge data indicating a Complete Episode of Care  \*\*\*

DATE: JAN 25,2013//

STATE CODE: WYOMING//

COUNTY CODE: LARAMIE  (021)//

ZIP CODE: 82009//

ELIGIBILITY @ EVALUATION: Service Connected 50% or More  (01)

         //

BIRTH YEAR:  1928

                  \*\*\*  Contact MAS if value is incorrect.  \*\*\*

PERIOD OF SERVICE: Vietnam  (07)//

SEX:  Male  (1)

                  \*\*\*  Contact MAS if value is incorrect.  \*\*\*

RACE:  Obsolete Field  Jan 2003

MARITAL STATUS @ EVALUATION: Married  (1)//

LIVING ARRANGEMENTS @ EVAL: With Spouse  (2)//

LAST AGENCY PROVIDING CARE: VA Provided Care  (1)

         //

TYPE OF LAST CARE AGENCY: Community-Based Services  (6)

         //

ADMIT/REJECT ACTION: Admit to HBHC  (1)//

PRIMARY DIAGNOSIS @ ADMISSION: f

Please enter at least the first two characters of the ICD-10 code or code

description to start the search.

PRIMARY DIAGNOSIS @ ADMISSION: ?

Enter code or "text" for more information.

PRIMARY DIAGNOSIS @ ADMISSION: ??

Enter a "free text" term or part of a term such as "femur fracture".

or

Enter a "classification code" (ICD/CPT etc) to find the single term

associated with the code.

or

Enter a "partial code". Include the decimal when a search criterion

includes 3 characters or more for code searches.

PRIMARY DIAGNOSIS @ ADMISSION: ???

Number of Code Matches

----------------------

The ICD-10 Diagnosis Code search will show the user the number of matches

found, indicate if additional characters in ICD code exist, and the number

of codes within the category or subcategory that are available for selection.

For example:

14 matches found

M91. - Juvenile osteochondrosis of hip and pelvis (19)

This indicates that 14 unique matches or matching groups have been found

and will be displayed.

M91. - the "-" indicates that there are additional characters that specify

unique ICD-10 codes available.

\(19\) Indicates that there are 19 additional ICD-10 codes in the M91 "family"

that are possible selections.

PRIMARY DIAGNOSIS @ ADMISSION:

HBPC Help Text Display for Discharge Data Entry

Evaluation/Admission Data Entry

          Discharge Data Entry

          Reports Menu ...

          Transmission Menu ...

          Manager Menu ...

          Medical Foster Home (MFH) Menu ...

Select HBPC Information System Menu Option: discharge Data Entry

Select HBHC PATIENT NAME: HBPCTEST, TWO         3-8-18    000448404

    YES     SC VETERAN      DC

Enrollment Priority: GROUP 1    Category: NOT ENROLLED  End Date: 10/10/2010

     1   HBPCTEST, TWO       04-29-09

     2   HBPCTEST, TWO        08-05-10

CHOOSE 1-2: 2  HBPCTEST, TWO        08-05-10

DISCHARGE DATE: JAN 25,2013//

ELIGIBILITY @ DISCHARGE: Service Connected 50% or More  (01)

         //

MARITAL STATUS @ DISCHARGE: Married  (1)//

LIVING ARRANGEMENTS @ D/C: Not Determined  (9)//

DISCHARGE STATUS: Anticipated Institutionalization  (2)

         //

TRANSFER DESTINATION: VA Provided Care  (1)//

TYPE OF DESTINATION AGENCY: Hospice  (5)//

PRIMARY DIAGNOSIS @ DISCHARGE: f

Please enter at least the first two characters of the ICD-10 code or code

description to start the search.

PRIMARY DIAGNOSIS @ DISCHARGE: ?

Enter code or "text" for more information.

PRIMARY DIAGNOSIS @ DISCHARGE: ??

Enter a "free text" term or part of a term such as "femur fracture".

or

Enter a "classification code" (ICD/CPT etc) to find the single term

associated with the code.

or

Enter a "partial code". Include the decimal when a search criterion

includes 3 characters or more for code searches.

PRIMARY DIAGNOSIS @ DISCHARGE: ???

Number of Code Matches

----------------------

The ICD-10 Diagnosis Code search will show the user the number of matches

found, indicate if additional characters in ICD code exist, and the number

of codes within the category or subcategory that are available for selection.

For example:

14 matches found

M91. - Juvenile osteochondrosis of hip and pelvis (19)

This indicates that 14 unique matches or matching groups have been found

and will be displayed.

M91. - the "-" indicates that there are additional characters that specify

unique ICD-10 codes available.

\(19\) Indicates that there are 19 additional ICD-10 codes in the M91 "family"

that are possible selections.

PRIMARY DIAGNOSIS @ DISCHARGE:

*(This page intentionally left blank)*