---
title: SR*3*177 Surgery ICD-10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery ICD-10
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*177
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - code
  - surgery
  - report
  - codes
  - diagnosis
  - search
  - updated
  - assessment
page_count: 0
word_count: 2200
section_count: 14
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/icd-10_rn_sr_3_177.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/icd-10_rn_sr_3_177.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

---
title: ICD-10 Follow On Class 1 Software Remediation
---

Surgery

Software Version 3.0

Release Notes

SR\*3.0\*177

![](sr-3-177-surgery-icd-10-release-notes/001.png)

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
- [Surgery Interface File Download Option](#surgery-interface-file-download-option)
- [Alert Coder Regarding Coding Issues](#alert-coder-regarding-coding-issues)
- [MailMan Message Header](#mailman-message-header)
- [Surgery Risk Assessment](#surgery-risk-assessment)
  - [Non-Cardiac Surgery Risk Assessment](#non-cardiac-surgery-risk-assessment)
  - [Cardiac Surgery Risk Assessment](#cardiac-surgery-risk-assessment)
- [Modified Reports](#modified-reports)
  - [PCE Filing Status Report](#pce-filing-status-report)
  - [M&M Verification Report (Full Report)](#mm-verification-report-full-report)
  - [M&M Verification Report (Pre-Transmission Report)](#mm-verification-report-pre-transmission-report)
- [ICD-10 Searches](#icd-10-searches)
  - [ICD-10-CM Diagnosis Code Search](#icd-10-cm-diagnosis-code-search)
- [Technical Information](#technical-information)
  - [New Routines](#new-routines)
  - [New Input Template](#new-input-template)
  - [Addition to Data Dictionary](#addition-to-data-dictionary)
- [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Surgery package contained in patch SR\*3.0\*177.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 Activation Date.

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

Patch SR\*3\*177 makes the following changes to the Surgery application:

- Several reports and display screens have been updated to accommodate ICD-10 diagnosis codes.
- The only noticeable difference users see will occur when a specific ICD diagnosis code descriptor changes based on the date of operation for the case.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery manuals are posted on the VistA Documentation Library (VDL) page (<http://www.va.gov/vdl/application.asp?appid=103>).

The following Surgery user manuals are updated with changes for SR\*3\*177:

- Surgery V3.0 User Manual and Change Pages
- Surgery V3.0 Technical Manual/Security Guide and Change Pages

The following manual does not exist for the Surgery package:

- Installation Guide

> **NOTE:** Security information is contained within the *Surgery V. 3.0 Technical Manual/Security Guide*.

# Surgery Interface File Download Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option 2 of the *Surgery Interface File Download* Option has been updated from “ICD9” to “ICD.”

Example of Updated *Surgery Interface File Download* Option

Surgery Interface File Download Option

1\. CPT4

2\. ICD

3\. MEDICATION

4\. MONITOR

5\. PERSONNEL

6\. REPLACEMENT FLUID

7\. ANES SUPERVISE CODE

8\. LOCATION

# Alert Coder Regarding Coding Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Alert Coder has been updated to identify ICD-10 diagnosis codes.

Example of Updated Alert Coder

The following "final" codes have been entered for the case.

Postop Diagnosis Code (ICD-10): K71.51, Toxic liver disease with chronic active hepatitis with ascites

If you believe that the information coded is not correct and would like to alert the coders of the potential issue, enter a brief description of your concern below.

# MailMan Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan Message Header has been updated to accommodate ICD-10 codes. The header now lists “ICD” rather than “ICD9”.

Example of Updated MailMan Message Header

Subj: ICD OR CPT CODE DELETION \[#43805\] 10/15/13@09:00

1 line

From: SURGERY PACKAGE In 'IN' basket. Page 1

-------------------------------------------------------------------

Patient: SURPATIENT,TWELVE CASE \#: 12426

OPERATION DATE: 10/15/13 HERNIA REPAIR

# Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Non-Cardiac and Cardiac Surgery Risk Assessments have been updated to accommodate ICD-10 codes.

## Non-Cardiac Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example of Updated Non-Cardiac Surgery Risk Assessment

VA NON-CARDIAC RISK ASSESSMENT Assessment: 236 PAGE 3

FOR SURPATIENT,FORTY (COMPLETED)

=========================================================================

OUTCOME INFORMATION

Postoperative Diagnosis Code (ICD-10): K71.51, Toxic liver disease w/chron act hepatitis w/ascites

………………

\* T32.09 Rhinitus due to p 10/12/13

\* indicates Other (ICD10)

## Cardiac Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example of Updated Cardiac Surgery Risk Assessment

VA CONTINUOUS IMPROVEMENT IN CARDIAC SURGERY PROGRAM (CICSP/CICSP-X)

I. IDENTIFYING DATA

Patient: SURPATIENT,NINE Case \#: 238 Fac./Div. \#: 500

X. DETAILED DISCHARGE INFORMATION

Discharge ICD-10 Codes: K14.09 K15.90 T31.10

# Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports have been modified to accommodate ICD-10 codes:

- PCE Filing Status Report
- M&M Verification Report (Pre-Transmission Report)
- M&M Verification Report (Full Report)

## PCE Filing Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE Filing Status Report has been updated to include both ICD-9 and ICD-10 codes.

Example of Updated PCE Filing Status Report

JUN 10,2005@07:00 SURPATIENT,NINETYONE SURSURGEON,ONE GENERAL(OR WHEN Filed NOT DEFINED BELOW)

292 (53) SURSURGEON,ONE NOT ENTERED \<NONE\>

CPT Code: 44950 APPENDECTOMY ICD10 Diagnosis Code: E08.65 Short Description (TBD) ICD10 Diagnosis Code: R40.2124 ICD-10 Short Description (TBD)

Example of Updated PCE Filing Status Report: Filed/Not Filed Counts

CPT ICD

CASES CODES CODES

FILED: 2 2 2

NOT FILED: 2

----- ----- -----

TOTAL: 3 2 2

## M&M Verification Report (Full Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M&M Verification Report has been modified to include both ICD-9 and ICD-10 codes.

Example of Updated M&M Verification Report (Full Report)

CHEYENNE VAMC Page 1

M&M Verification Report

From: Sep 15,2013 To: Oct 15, 2013

REVIEWED BY:

Report Generated: DEC 28,2013

DATE REVIEWED:

OP DATE CASE \# SURGICAL SPECIALTY ASSESSMENT TYPE STATUS

DEATH RELATED

PRINCIPAL PROCEDURE

======================================================================

\>\>\> SURGPATIENT,ONE W

09/21/13 34216 GENERAL(OR WHEN NOT DEFINED BELOW)

NON-CARDIAC

TRANSMITTED

N/A

SIGMOID RESECTION

CPT Codes: 44140

Occurrences: OTHER OCCURRENCE \*\* POSTOP \*\* (09/21/13) CONT’D

CONT’D ICD9: 532.90 DUODENAL ULCER NOS \>\>\> Comments:

post op complications were ileus,anastomotic leak,

anemia, and leukocytosis.

10/08/13 34319 GENERAL(OR WHEN NOT DEFINED BELOW)

NON-CARDIAC

TRANSMITTED

N/A

LOOP COLOSTOMY

CPT Codes: 44140-78

Occurrences: BLEEDING/TRANSFUSIONS \*\* POSTOP \*\* (10/08/13)

ICD10: L21.9 SEBORRHEIC DERMATITIS, UNSPECIFIED

\>\>\> Comments:

please see Dr. Travers' note of 9/6/13. Also refer

to lab results 9/16 and 9/18.

OTHER OCCURRENCE \*\* POSTOP \*\* (10/08/13)

ICD10: G11.2 LATE-ONSET CEREBELLAR ATAXIA \>\>\> Comments:

Please refer to Dr. Travers' note on 9/8.

## M&M Verification Report (Pre-Transmission Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M&M Verification Report has been modified to include both ICD-9 and ICD-10 codes.

Example of Updated M&M Verification Report (Pre-Transmission Report)

M&M Verification Report Assessment Death

Op Date Specialty Procedure(s) Related Occurrence(s) - (Date) Type/Status

==================================================================================

\>\>\> SURPATIENT,TWENTY

09/16/13 GENERAL TOTAL LARYNGECTOMY NO NON-CARD/T

10/01/13 THORACIC CABG, VEIN, SIX+ NO CARDIAC/I

10/20/13 PERIPHERAL LT CAROTID ENDOARTERECTOMY NON-CARD/T

N/A OTHER OCCURRENCE (10/20/13) ICD10: Z03.818 ENCOUNTER FOR OBSERVATION FOR SUSPECTED EXPOSURE TO OTHER BIOLOGI

CAL AGENTS RULED OUT (10/19/13)

ICD10: Q26.4 ANOMALOUS PULMONARY VENOUS CONNECTION, UNSPECIFIED \*(10/05/13)

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery package provides the ability to search on ICD-10-CM diagnosis codes.

> **NOTE:** Existing ICD-9 functionality has not changed.

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and display its description. The Surgery application prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user. 

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes.

ICD-10-CM diagnosis code search highlights include:

- Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.
- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.
- The user is presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, the user is prompted to refine the search.
- The user can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.
- If the user performs a partial code search or text-based search, where more than one ICD-10 diagnoses which are Active for the “Date of Interest” are found to match, the search results (consisting of categories, subcategories or individual ICD-10 diagnosis codes) shall display in groups of no more than 4 per screen.

Example of Updated ICD Diagnosis Search

Prin Pre-op ICD Diagnosis Code (ICD10): S06

19 matches found

1\. S06.0X- Concussion (30)

2\. S06.1X- Traumatic cerebral edema (30)

3\. S06.2X- Diffuse traumatic brain injury (30)

4\. S06.30- Unspecified focal traumatic brain injury (30)

Press \<RETURN\> for more, "^" to exit, or Select 1-4:

5\. S06.31- Contusion and laceration of right cerebrum (30)

6\. S06.32- Contusion and laceration of left cerebrum (30)

7\. S06.33- Contusion and laceration of cerebrum,

unspecified (30)

8\. S06.34- Traumatic hemorrhage of right cerebrum (30)

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 7

30 matches found

1\. S06.330A Contusion and Laceration of Cerebrum,

unspecified, without Loss of Consciousness, Initial

Encounter

2\. S06.330D Contusion and Laceration of Cerebrum,

unspecified, without Loss of Consciousness, Subsequent

Encounter

3\. S06.330S Contusion and Laceration of Cerebrum,

unspecified, without Loss of Consciousness, Sequela

4\. S06.331A Contusion and Laceration of Cerebrum,

unspecified, with Loss of Consciousness of 30 Minutes or

less, Initial Encounter

Press \<RETURN\> for more, "^" to exit, or Select 1-4:

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some Surgery routines were added to replace direct global reads and old APIs with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible. The following new routines are added:

| Routine Name | Function                           |
|--------------|------------------------------------|
| SR3P177      | ICD-10 Diagnosis Code Installation |
| SROICDGT     | ICD-10 Diagnosis Search            |
| SROICDL      | ICD-10 Diagnosis Code Lookup       |

## New Input Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input template SRSRES2 (File \#130) has been added to the Surgery package.

## Addition to Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new ICD SEARCH API file (File \#130.4) has been added to the Data Dictionary.

This file is used as a repository of ICD search (lookup) functionality to support an application's need for different user interface calls across multiple versions of ICD Diagnosis and Procedure coding.

Each entry is associated with a specific version of ICD Diagnosis or Procedure coding, an application, and executable M code. The executable M code can be invoked from within the input transform of a field that points to the ICD DIAGNOSIS file (#80) or the ICD OPERATION/PROCEDURE file (#80.1) to achieve the correct search functionality specific to the ICD version.

# Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text (?) and extended help text (??, ???) are included for prompts related to ICD-10 codes.

When entering ?:

Enter code or “text” for more information.

When entering ??:

Enter a "free text" term or part of a term such as ”femur fracture”.

Or

Enter a ”classification code” (ICD/CPT etc) to find the single term associated with the code.

Or

Enter a ”partial code”. Include the decimal when a search criterion includes 3 characters or more for code searches.

When entering ???:

Number of Code Matches

----------------------

The ICD-10 Diagnosis Code search will show the user the number of matches found, indicate if additional characters in ICD code exist, and the number of codes within the category or subcategory that are available for selection.

19 matches found

M91. - Juvenile osteochondrosis of hip and pelvis (19)

This indicates that 19 unique matches or matching groups have been found and will be displayed.

M91. - the “-“ indicates that there are additional characters that specify unique ICD-10 codes available.

\(19\) Indicates that there are 19 additional ICD-10 codes in the M91 ”family” that are possible selections.

*(This page included for two-sided copying.)*