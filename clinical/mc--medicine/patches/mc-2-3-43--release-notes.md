---
title: MC*2.3*43/44 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: MC
app_name: Medicine
section: CLI
app_status: active
pkg_ns: MC
patch_ver: 2.3
patch_id: MC*2.3*43
group_key: "MC:MC:2.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - diagnosis
  - table
  - contents
  - print
  - codes
  - medical
  - procedure
  - date
  - medicine
page_count: 0
word_count: 1571
section_count: 9
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/icd-10_rn_mc_2_3_43_44.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/icd-10_rn_mc_2_3_43_44.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=77"
---

ICD-10 Follow On Class 1 Software Remediation Project

VistA Medicine

Release Notes

MC\*2.3\*43 & MC\*2.3\*44

![](mc-2-3-43-44-release-notes/001.png)

July 2014

Office of Information and Technology

Product Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
    - [Dependencies](#dependencies)
    - [Patches](#patches)
  - [Documentation](#documentation)
- [Medical Diagnosis/ICD Codes File (#697.5)](#medical-diagnosisicd-codes-file-6975)
- [Rheumatology Modifications](#rheumatology-modifications)
  - [Menu Options](#menu-options)
  - [Diagnosis Edit Option](#diagnosis-edit-option)
  - [Print Menu Option](#print-menu-option)
- [ICD-10 Searches](#icd-10-searches)
- [Technical Information](#technical-information)
  - [Routines](#routines)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Medicine package contained in patches MC\*2.3\*43 and MC\*2.3\*44.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alphanumeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision-making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                             |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character |
| Decimal after first 2 characters | Does not contain decimals                                                                                                             |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patches MC\*2.3\*43 and MC\*2.3\*44 make the following changes to the Medicine application:

- Updates the MEDICAL DIAGNOSIS/ICD CODES File \#697.5 with ICD-10 codes.
- Modifies the Diagnosis Edit \[MCRHDIAGF\] option to populate an ICD code relevant to the procedure date when selecting a medical diagnosis.
- Modifies the Diagnosis Print \[MCRHDIAGP\] and Print All Report \[MCRHALLP\] options to change the column header to “ICD” instead of “ICD9”.
- Changes field descriptions in several Medicine files by replacing the text “ICD9” with “ICD”.

NOTE 1: Many of the fields are not currently used and are flagged for future use. The *Line Enter/Edit Menu* ... \[MCRHMENULIN\] option, which is no longer used, is placed “out of order”.

NOTE 2: The Rheumatology Menu is the only part of the Medicine application that needed to be remediated for ICD-10.

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parent package of Medicine, Clinical Procedures (CP), is added as a subscriber to Interface Control Registration (ICR) \#5747.

### Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following associated patches must be installed prior to installing Patch MC\*2.3\*43:

- LEX\*2\*80
- ICD\*18\*57
- MC\*2.3\*44

The following associated patches must be installed prior to installing Patch MC\*2.3\*44:

- MC\*2.3\*42
- LEX\*2\*80
- ICD\*18\*57

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medicine manuals are posted on the VistA Documentation Library (VDL) <http://www.va.gov/vdl/application.asp?appid=77> page.

The following Medicine manuals are updated with changes for MC\*2.3\*43 and MC\*2.3\*44:

- User Manual
- Technical Manual

The following manual does not exist for this package:

- Security Guide

# Medical Diagnosis/ICD Codes File (#697.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MEDICAL DIAGNOSIS/ICD CODES File (#697.5) now includes ICD-10 codes. A Medical Diagnosis may be associated with both ICD-9 and ICD-10 codes, based on the current code set active at the time of the procedure date. If the procedure date is on or after the ICD-10 activation date, then the ICD-10 code mapped to the medical diagnosis will be populated.

# Rheumatology Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Medicine package is an M/Roll and Scroll/Character-based package for Medicine Specialties. The *RheumatologyMenu* option of the Medicine package is now updated for ICD-10.

> Medicine Menu Options

> Select Medicine Menu Option:?

> 1 Cardiology Menu ...

> 2 GI Menu ...

> 3 Pulmonary Menu ...

> 4 Hematology Menu ...

> 5 Pacemaker Menu ...

> 6 Rheumatology Menu ...

> 7 Generalized Procedure Menu ...

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> 10 Workload Reporting Management ...

The following options on the *Rheumatology Menu* are updated for the ICD-10 enhancement.

> Rheumatology Menu Options

1.  Diagnosis Edit
2.  Add NEW visit/display Patient Background Info.
3.  History Narrative Edit
4.  Print Serial Laboratory Info
5.  Display/Print Drug Treatment Program
6.  Health Assessment (HAQ) Edit
7.  Health/Physical History Edit
8.  Physical Examination Edit
9.  Death Admin Edit
10. Print Menu
11. Line Enter/Edit Menu  
    \*\*\> Out of order: OUT OF ORDER
12. Problem Oriented Consult Menu
13. Image Capture
14. Summary of Patient Procedures
15. Rheumatology Management Menu

## *Diagnosis Edit* Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Diagnosis Edit* \[MCRHDIAG\] option modifications allow you to enter the diagnosis text, which then displays the selection of medical diagnoses based on the current active ICD code set for that procedure date. If the procedure date is on or after the ICD-10 activation date, then the medical diagnoses mapping to the ICD-10 code is selectable.

*Diagnosis Edit* Option: Entering an ICD-10 Medical Diagnosis Code

Rheumatology patient diagnosis 03/20/12

1 DATE/TIME(R):OCT 1,2013

2 RHEUMATOLOGY PATIENT(R):AGENT,ORANGE  
3 DIAGNOSIS(M):GOUT  
4 PROCEDURE SUMMARY:This is a test of procedures.  
5 SUMMARY:NORMAL  
6 PRIMARY PROVIDER:MEDPROVIDER,ONE  
  
  
ANSWER WITH MEDICAL DIAGNOSIS/ICD CODES  
DO YOU WANT THE ENTIRE MEDICAL DIAGNOSIS/ICD CODES LIST? y (YES)  
CHOOSE FROM:  
COCCYDYNIA  
DRUG RELATED LUPUS ERYTHEMATOS  
Press \<RETURN\> to Continue, '^' to Quit:

## *Print Menu* Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options on the *Print Menu* are updated for ICD-10.

Rheumatology Print Menu

Select Rheumatology Menu Option: 10 Print Menu

Select Print Menu Option: ?

1 Diagnosis Print

2 Background Information Print

3 History Narrative Print

4 Serial Laboratory Info. Print

5 Health Assessment (HAQ) Print

6 Health/Physical History Print

7 Physical Examination Print

8 Death Admin Print

9 Print All Report

10 Brief Rheumatology Report

The *Print Menu* \[MCRHMENUPRT\] option column header now displays “ICD” instead of “ICD9”.

*Print Menu* Option

Select Rheumatology Menu Option: 10 Print Menu

Select Print Menu Option: DiagnosisPrint

Enter patient name or the date & time: 10-30-2013 PATIENTTWO, RHEU 000223333

DEVICE: HOME// UCX/TELNET Right Margin: 80//

Pg.1 10/30/13 11:23

CONFIDENTIAL RHEUMATOLOGY REPORT

PATIENTTWO,RHEU 000-22-3333 NOT INPATIENT DOB: APR 29,1959

PROCEDURE DATE/TIME: 10/30/13 07:03

\- - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - -

PROVIDER:

PROBLEM LIST

OCTOBER 30, 2013 17:03

PATIENT DATE DIAGNOSIS ICD CODE

------- ---- --------- ---------PATIENTTWO,RHEU 09/05/13 CONGENITAL HEART DISEASE - OTHER 747.21

10/16/13 CONGENITAL HEART DISEASE - OTHER Q25.4

On the diagnoses section of the “Print All Reports”, “ICD” now replaces “ICD9”.

Print All Report

Select Print Menu Option: 9 Print All Report

Enter patient name or the date & time: 10-1-2013AGENT,ORANGE 666112233

DEVICE: HOME// ;;100 UCX/TELNET Right Margin: 80//

Pg. 1 03/20/12 18:58

CONFIDENTIAL RHEUMATOLOGY REPORT

AGENT,ORANGE 666-11-2233 NOT INPATIENT DOB: JAN 12,1942

PROCEDURE DATE/TIME: 10/01/13

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

PROVIDER: MEDPROVIDER,ONE

PROBLEM LIST

OCT 1,2013

PATIENT DATE DIAGNOSIS ICD CODE

------- ---- --------- ---------

AGENT,ORANGE 10/01/13 COCCYDYNIA V70.0XXA

BACK GROUND INFORMATION

Address: 440 LANE BLVD

NEW YORK 12208

Home phone: 800-555-1212

Work phone:

Sex: MALE

Race:

Maritus status: NEVER MARRIED

Employment status:

Occupation:

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

The VistA Medicine package does not contain a direct search for ICD-9 diagnosis codes so this application does not utilize the standard Lexicon search utility for ICD-10-CM diagnoses.

> **NOTE:** The “Date of Interest” within the VistA Medicine package is equivalent to the procedure date for the VistA Medicine package.

If the procedure date is *on or after* the ICD-10 activation date, the VistA Medicine package shall provide the ability to search the generic text MEDICAL DIAGNOSIS/ICD CODES File (#697.5) entries and store the matching ICD-10 diagnosis code pointer to the ICD-10 DIAGNOSIS File (#80).

Use the FileMan Inquiry to check entries randomly in file (#697.5) to ensure the ICD-10 codes were added.

MEDICAL DIAGNOSIS/ICD CODES File (#697.5) Showing ICD-10 Codes

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: ICD DIAGNOSIS// 697.5 MEDICAL DIAGNOSIS/ICD CODES

(907 entries)

Select MEDICAL DIAGNOSIS/ICD CODES: \`1 MYOCARDIAL INFARCTION - ACUTE

ANOTHER ONE: \`7 MYOCARDITIS

ANOTHER ONE: \`100 DIFFUSE DUODENITIS NOTED

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computed Fields

DIAGNOSIS: MYOCARDIAL INFARCTION - ACUTE

PROCEDURE: CATH

ICD CODE: 410.9

ICD CODE: 410.0

ICD CODE: 410.1

ICD CODE: 410.4

ICD CODE: 410.2

ICD CODE: 410.3

ICD CODE: 410.5

ICD CODE: 410.8

ICD CODE: 410.6

ICD CODE: I21.3

ICD CODE: I22.9

ICD CODE: I21.09

ICD CODE: I22.0

ICD CODE: I21.01

ICD CODE: I21.02

ICD CODE: I21.19

ICD CODE: I22.1

ICD CODE: I21.11

ICD CODE: I21.29

Enter RETURN to continue or '^' to exit:

ICD CODE: I22.8

ICD CODE: I21.21

SPECIAL DIAGNOSIS TYPE: CARDIOLOGY DIAGNOSIS

PROCEDURE NAME: CATH

DIAGNOSIS: MYOCARDITIS

PROCEDURE: CATH

ICD CODE: 422.91

ICD CODE: 422.99

ICD CODE: 422.90

ICD CODE: 032.82

ICD CODE: 074.23

ICD CODE: 036.43

ICD CODE: 398.0

ICD CODE: 422.92

ICD CODE: 093.82

ICD CODE: 422.93

ICD CODE: I40.0

ICD CODE: I40.1

ICD CODE: I40.8

Enter RETURN to continue or '^' to exit:

ICD CODE: I40.9

ICD CODE: A36.81

ICD CODE: B33.22

ICD CODE: A39.52

ICD CODE: I09.0

ICD CODE: A52.06

SPECIAL DIAGNOSIS TYPE: CARDIOLOGY DIAGNOSIS

PROCEDURE NAME: CATH

DIAGNOSIS: DIFFUSE DUODENITIS NOTED

PROCEDURE: EGD

ICD CODE: 535.6

ICD CODE: K29.80

ICD CODE: K29.81

SPECIAL DIAGNOSIS TYPE: GI DIAGNOSIS

PROCEDURE NAME: EGD

Select MEDICAL DIAGNOSIS/ICD CODES:

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medicine package is dependent on the following Application Program Interfaces (APIs) for the implementation of the ICD-10 project. These APIs are currently under development. Any delay in the release of these APIs will directly affect this project.

| Name/Signature of the Component | Provider Application | Consumer Application | ICR | ICD Related? |
|-------------------------------------|--------------------------|--------------------------|---------|------------------|
| \$\$CSI^ICDEX                       | DRG Grouper              | Medicine                 | Yes     | No               |
| \$\$ICDDX^ICDEX                     | DRG Grouper              | Medicine                 | Yes     | No               |
| \$\$IMP^ICDEX                       | DRG Grouper              | Medicine                 | Yes     | No               |
| \$\$SINFO^ICDEX                     | DRG Grouper              | Medicine                 | Yes     | No               |