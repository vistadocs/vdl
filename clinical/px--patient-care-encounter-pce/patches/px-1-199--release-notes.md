---
title: PX*1*199 ICD-10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10
app_code: PX
app_name: Patient Care Encounter (PCE)
section: CLI
app_status: active
pkg_ns: PX
patch_ver: 1
patch_id: PX*1*199
group_key: "PX:PX:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - diagnosis
  - table
  - code
  - encounter
  - contents
  - fracture
  - codes
  - date
  - report
  - bone
page_count: 0
word_count: 2439
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/icd-10_rn_px_1_199.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/icd-10_rn_px_1_199.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=82"
---

ICD-10 Follow On Class 1 Software Remediation

Patient Care Encounter (PCE)

Release Notes

PX\*1.0\*199

![](px-1-199-icd-10-release-notes/001.png)

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
- [# New Features and Functions](#new-features-and-functions)
  - [Differentiating ICD-9 and ICD-10 Diagnosis Codes](#differentiating-icd-9-and-icd-10-diagnosis-codes)
  - [Diagnosis Code Search Function](#diagnosis-code-search-function)
- [Changes to Existing Software](#changes-to-existing-software)
  - [Historical Encounters](#historical-encounters)
  - [Reports](#reports)
    - [CIDC Missing Data Report](#cidc-missing-data-report)
    - [Diagnosis Ranked by Frequency Report](#diagnosis-ranked-by-frequency-report)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Release Notes describe new features and functions, as well as changes to existing software, resulting from the International Classification of Diseases, Tenth Revision (ICD-10) software remediation effort for Veterans Health Information Systems and Technology Architecture (VistA) Patient Care Encounter (PCE), patch number PX\*1.0\*199.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with ICD-10 Clinical Modification (ICD-10-CM) and ICD-10 Procedure Coding System (ICD-10-PCS) dates of service, or dates of discharge for inpatients, that occur on or after the  
ICD-10 Activation Date (initially October 1, 2013).

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                                                           | ICD-10-CM                                                                     |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 3-5 characters                                                                     | 3-7 characters (not including the decimal)                                    |
| 1st character is numeric (chapters 1-17) or alpha (E or V) (supplemental chapters) | Character 1 is alpha; character 2 is numeric                                  |
| 2nd, 3rd, 4th and 5th characters are numeric                                       | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters                                                   | Decimal is used after third character                                         |

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

With implementation of ICD-10 codes, patch PX\*1\*199 provides differentiation between ICD-9 and ICD-10 diagnosis codes.

Throughout the PCE package, references to ICD-9 are frequently changed to a generic reference such as ICD or Diagnosis. The ICD-9 label is retained in a few places where only ICD-9 codes will be displayed. All reports have been reformatted to accommodate the longer ICD-10 codes and the longer descriptions. Essentially, though, users should experience very little change. In addition, other VistA packages that use PCE services through Application Program Interface (API) calls should experience no change in functionality. The API parameters for both Input and Output remain the same.

An example of the updated text changes where ICD-9 is now generic to represent ICD-9 or ICD-10 is shown below:

Old

Associated Primary Diagnosis ICD9 Code not in File 80

New

Associated Primary Diagnosis ICD Code not in File 80

Examples of the updated text changes where ICD-9 or ICD-10 will be individually specified based on the transaction date or report date range are shown below:

Select ICD-9 Diagnosis: 100.81

*or*

ICD-10 Diagnosis Code: F17.209

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

HELP SCREEN ALL DIAGNOSES (ICD-9 CODES)

ITEM CODE DESCRIPTION

1 001.1 CHOLERA DUE TO VIBRIO CHOLERAE EL TOR

2 001.9 CHOLERA, UNSPECIFIED

3 002.0 TYPHOID FEVER

*or*

HELP SCREEN ALL DIAGNOSES (ICD-10 CODES)

ITEM CODE DESCRIPTION

1 A00.0 CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR CHOLERAE

2 A00.1 CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR ELTOR

3 A00.9 CHOLERA, UNSPECIFIED

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

3 Most Frequent ICD9 Diagnoses:

Code Description Frequency

-------- ------------------------------------------ ---------

1\. 280.8 IRON DEFIC ANEMIA NEC 4

2\. 305.79 OTHER SYMPATHOMIMETIC, NEC 3

3\. 812.09 FX UPPER HUMERUS NEC-CL 2

*or*

3 Most Frequent ICD10 Diagnoses:

Code Description Freq.

-------- ------------------------------------------ ---------

A00.0 Cholera due to Vibrio cholerae 01, biovar cholerae 4

E08.649 Diabetes due to underlying condition w hypoglycemia w/o coma 3

H21.253 Iridoschisis, bilateral 2

The changes documented in the following sections pertain to the Options/Actions within the PCE Coordinator Menu listed below:

PCE COORDINATOR MENU OPTIONS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SUP PCE Encounter Data Entry - Supervisor</p>
<p>PCE PCE Encounter Data Entry</p>
<p>DEL PCE Encounter Data Entry and Delete</p>
<p>NOD PCE Encounter Data Entry without Delete</p>
<p>VIEW PCE Encounter Viewer</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

PCE provides the ability to add, edit, store and search on ICD-10-CM diagnosis codes. PCE displays ICD-10-CM diagnosis codes and short descriptions/definitions.

> **NOTE:** If the encounter or appointment date is prior to the ICD-10 Activation Date, PCE retains the current search functionality for ICD-9 diagnosis codes and descriptions/definitions.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals are updated with changes for PX\*1\*199:

- PCE User Manual
- PCE User Manual Appendices
- PCE Technical Manual

The following manuals do not contain changes relating to PX\*1\*199:

- PCE Installation Guide

The following manual does not exist for this package/application:

- Security Guide

# # New Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following enhancements allow for entry, display, lookup (search), print, storage, and internal and/or external transmissions of the ICD-10-CM code sets:

ICD-10-CM replaces ICD-9-CM as the diagnostic coding system for outpatient encounters with an encounter date on or after the ICD-10 Activation Date. 

There will be a period of time when dual code sets (ICD-9-CM and ICD-10-CM) are used to accommodate outpatient encounter dates of service prior to and following the ICD-10 Activation Date, as well as for reporting and research purposes.

## Differentiating ICD-9 and ICD-10 Diagnosis Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the encounter or appointment date is prior to the ICD-10 Activation Date, the PCE package adds an ICD-9 label following diagnosis prompts within PCE: DX, ED, CP, IM, ST, IN.

If the encounter or appointment date is on or after the ICD-10 Activation Date, the PCE package adds an ICD-10 label to the following diagnosis prompts within PCE: DX, ED, CP, IM, ST, IN.

PCE ENCOUNTER ACTIONS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>UE Update Encounter</p>
<p>AD Add Standalone Enc.</p>
<p>HI Make Historical Encounter</p>
<p>IN Checkout Interview</p>
<p>ED Edit an Item</p>
<p>IM Immunization</p>
<p>ST Skin Test</p>
<p>DD Display Detail</p>
<p>DX Diagnosis (ICD)</p>
<p>EP Expand Appointment</p>
<p>CP CPT (Procedure)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Diagnosis Code Search Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE ICD-10 diagnosis code search functionality allows you to select a single, valid ICD-10 diagnosis code and display its description. The user interface prompts you for input, invokes the Lexicon utility to get data, and then presents that data. 

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes. A dash after a number indicates that it contains a sub-category.

ICD-10-CM diagnosis code search highlights include:

- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined is the process of selecting the correct valid ICD-10 diagnosis code.
- You are presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, you are prompted to refine the search.
- You can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

The PCE package provides the ability to search on ICD-10-CM diagnosis codes at the following prompts:

- ICD-10 Diagnosis Code:
- Primary ICD-10 Diagnosis:
- 1st Secondary ICD-10 Diagnosis:
- ICD-10 Diagnosis:
- ICD-10 Diagnosis 2:
- Enter ICD-10 Diagnosis :
- Enter NEXT ICD-10 Diagnosis:
- What is ICD-10 DIAGNOSIS 1 for this procedure:

Example of ICD-10 Diagnosis Code Search

Select Action: Quit// DX Diagnosis (ICD)

Patient's Service Connection and Rated Disabilities:

Service Connected: No

Rated Disabilities: None Stated

ICD-10 Diagnosis Code: S62

7 matches found

1\. S62.0- Fracture of navicular \[scaphoid\] bone of wrist

\(147\)

2\. S62.1- Fracture of other and unspecified carpal bone(s)

\(357\)

3\. S62.2- Fracture of first metacarpal bone (231)

4\. S62.3- Fracture of other and unspecified metacarpal

bone (560)

5\. S62.5- Fracture of thumb (105)

6\. S62.6- Fracture of other and unspecified finger(s)

\(490\)

7\. S62.9- Unspecified fracture of wrist and hand (21)

Select 1-7: 1

4 matches found

1\. S62.00- Unspecified fracture of navicular \[scaphoid\]

bone of wrist (21)

2\. S62.01- Fracture of distal pole of navicular \[scaphoid\]

bone of wrist (42)

3\. S62.02- Fracture of middle third of navicular \[scaphoid\]

bone of wrist (42)

4\. S62.03- Fracture of proximal third of navicular

\[scaphoid\] bone of wrist (42)

Select 1-4: 4

42 matches found

1\. S62.031A Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

for closed Fracture

2\. S62.031B Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

for open Fracture

3\. S62.031D Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Routine Healing

4\. S62.031G Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Delayed Healing

5\. S62.031K Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Nonunion

6\. S62.031P Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Malunion

7\. S62.031S Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Sequela

8\. S62.032A Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of left Wrist, Initial Encounter

for closed Fracture

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 1

# Changes to Existing Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Existing software was enhanced to accommodate Historical Encounters. Reports were updated to display ICD-10 information.

## Historical Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCE is able to accommodate Historical Encounters in the ICD-9 environment with the use of the HI menu option, as shown below:

Current ICD-9 Functionality for Historical Encounters

UE Update Encounter CD Change Date Range VC View by Clinic

LI List by Appointment CC Change Clinic DD Display Detail

AD Add Standalone Enc. IN Check Out Interview GF GAF Score

HI Make Historical Enc. PC PC Assign or Unassign

TI Display Team Info QU Quit

SP Select New Patient

Select Action: Quit//HI {RETURN}

Select Action: Quit// HI Make Historical Enc.

This will create a historical encounter for documenting a clinical encounter

only and will not be used by Scheduling, Billing or Workload credit.

Enter RETURN to continue or '^' to exit: '

All other types of VISIT records use the Visit Date to determine whether the diagnoses associated with the record will come from the ICD-9 code set or the ICD-10 code set. The historical encounter records, also known as historic event records, must allow entry of ICD-10 codes when Data Entry Date is on or after the ICD-10 Activation Date.

Therefore, when the system’s date is on or after the ICD-10 Activation Date, PCE provides the ability to assign an ICD-10 code to a historic patient encounter and then add, edit, store, display, and search for the ICD-10 code on a historic patient encounter.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reports documented below pertain to the following Options within the PCE Coordinator and PCE Clinical Reports menus:

MENU OPTIONS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PCE Coordinator Menu:</p>
<p>MDR CIDC Missing Data Report</p>
<p>PCE Clinical Reports Menu:</p>
<p>CP Caseload Profile by Clinic</p>
<p>DX Diagnosis Ranked by Frequency</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### CIDC Missing Data Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missing Data Report sort selection now lists DIAGNOSIS as selection 3 rather than ICD9.

CIDC Missing Data Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PCE Missing Data Report</p>
<p>Would you like to include ALL Data Sources? YES// <strong>Y</strong></p>
<p> Date Range Selection </p>
<p>Beginning date: <strong>9/29/2013</strong> (SEPTEMBER 29, 2013)</p>
<p>Ending date: <strong>10/2/2013</strong> (OCTOBER 2, 2013)</p>
<p>* Report Sort Selection *</p>
<p>(1) DATA SOURCE</p>
<p>(2) CPT</p>
<p>(3) DIAGNOSIS</p>
<p>(4) PATIENT</p>
<p>(5) ELIGIBILITY</p>
<p>Enter number between 1 and 5: <strong>3</strong></p>
<p>Select one of the following:</p>
<p>D DETAILED REPORT</p>
<p>S STATISTICS ONLY</p>
<p>Select report type: DETAILED REPORT// <strong>D DETAILED REPORT</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PCE MISSING DATA REPORT</p>
<p>OCT 2,2013@07:25:32</p>
<p>By Clinic, Provider, and Date</p>
<p>SEP 29, 2013 through OCT 2,2013</p>
<p>Page 1</p>
<p>=================================================================================</p>
<p>BARKER DENTAL</p>
<p>Unknown</p>
<p>SORT VALUE: DIAGNOSIS</p>
<p>ICD9 = 130.5</p>
<p>SEP 29, 2013:</p>
<p>Patient SSN Date/Time Enc. ID Created by User Defect</p>
<p>Test, PT 000-00-0000 SEP 29, 2013@9:00 00XXX-YYY PROVIDER,ONE Procedure: 11308 missing assoc. DXs</p>
<p>TOTAL DEFECTS FOR 00XXX-YYY: 1</p>
<p>TOTAL DEFECTS FOR SEP 29, 2013: 1</p>
<p>TOTAL ENCOUNTERS FOR SEP 29, 2013: 1</p>
<p>TOTAL DEFECTS FOR SORT VALUE - 130.5: 1</p>
<p>TOTAL ENCOUNTERS FOR SORT VALUE - 130.5: 1</p>
<p>=================================================================================</p>
<p>ICD10 = I13.1</p>
<p>OCT 1, 2013:</p>
<p>Test, PT 000-00-0000 OCT 1, 2013@9:00 00XXX-YYY</p>
<p>TOTAL DEFECTS FOR 58PQG-CHY: 1</p>
<p>TOTAL DEFECTS FOR OCT 1, 2013: 1</p>
<p>TOTAL ENCOUNTERS FOR OCT 1, 2013: 1</p>
<p>TOTAL DEFECTS FOR SORT VALUE – I13.1: 1</p>
<p>TOTAL ENCOUNTERS FOR SORT VALUE – I13.1: 1</p>
<p>=================================================================================</p></td>
</tr>
</tbody>
</table>

### Diagnosis Ranked by Frequency Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The date of the report determines whether ICD-9 or ICD-10 codes and descriptions are printed.

CPE Diagnosis Ranked by Frequency Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

8 Most Frequent ICD10 Diagnoses:

Code Description Freq.

-------- ------------------------------------------------------------ -------

A00.0 Cholera due to Vibrio cholerae 01, biovar cholerae 3

E08.649 Diabetes due to underlying condition w hypoglycemia w/o coma 2

W54.0XXA Bitten by dog, initial encounter 1

I11.0 Hypertensive heart disease with heart failure 1

I10. Essential (primary) hypertension 1

H21.253 Iridoschisis, bilateral 1

E11.319 Type 2 diabetes w unsp diabetic rtnop w/o macular edema 1

A01.00 Typhoid fever, unspecified 1

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\(This page included for two-sided copying.)*