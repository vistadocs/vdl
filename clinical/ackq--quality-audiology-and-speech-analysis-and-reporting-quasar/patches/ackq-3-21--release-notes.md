---
title: ACKQ*3*21 ICD-10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3*21
group_key: "ACKQ:ACKQ:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - code
  - visit
  - count
  - codes
  - diagnosis
  - entry
  - diagnostic
  - reports
page_count: 0
word_count: 1425
section_count: 11
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/icd-10_rn_ackq_3_21.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/icd-10_rn_ackq_3_21.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

ICD-10 Follow On Class 1 Software Remediation Project

Quality Audiology and Speech Analysis and Reporting (QUASAR)

Application Version 3.21

Release Notes

ACKQ\*3\*21

![](ackq-3-21-icd-10-release-notes/001.png)

August 2014

Office of Information and Technology

Product Development

Table of Contents

*(This page intentionally left blank)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [ICD Code Searches](#icd-code-searches)
- [Modified Screens](#modified-screens)
  - [New Visit Entry Screen and Edit Visit Entry Screens](#new-visit-entry-screen-and-edit-visit-entry-screens)
  - [Patient Inquiry Screen](#patient-inquiry-screen)
- [Modified Reports](#modified-reports)
  - [Visits by Diagnosis](#visits-by-diagnosis)
  - [A&SP Clinic Visit Report](#asp-clinic-visit-report)
- [Technical Information](#technical-information)
  - [Routines](#routines)
  - [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Quality Audiology and Speech Analysis and Reporting (QUASAR) package contained in patch ACKQ\*3\*21.

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

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                             |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character |
| Decimal after first 2 characters | Does not contain decimals                                                                                                             |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch ACKQ\*3\*21 makes the following changes to the QUASAR application:

- Provides the ICD-10-CM Diagnosis short description on the screens and in reports.
- Help text has been modified to accommodate ICD-10 implementation. The Help prompts the user to enter an ICD code rather than an ICD-9 code.

The reports impacted are:

- Visits by Diagnosis – via the *A&SP Reports* menu option
- Tailor-Made A&SP Reports – via the *A&SP Reports* menu option
- Print A&SP Capitation Report – via the *Management Reports A&SP* menu option
- Print A&SP File Entries (A&SP DIAGNOSTIC CONDITION file (#509850.1)

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QUASAR manuals are posted on the VistA Documentation Library (VDL) (<http://www.va.gov/vdl/application.asp?appid=97>).

The following QUASAR user manuals are updated with changes for ACKQ\*3\*21:

- Technical Manual
- User Manual

The following manual does not exist for this package:

- Security Guide

> **NOTE:** Security Information is contained within the *Technical/Pkg Security Manual*.

The following manuals exist on the VDL but are not updated for this package:

- Install/Implement Guide for ACKQ\*3.0\*13
- Technical Manual – Audiometric Exam Module

# ICD Code Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QUASAR continues to utilize the Diagnosis Dictionary for search functionality, but now users can search for both ICD-9 and ICD-10 codes. Short descriptions of codes are displayed with the search results.

> **NOTE:** Existing ICD-9 functionality has not changed.

# Modified Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens have been modified to accommodate ICD-10 codes:

- New/Edit Visit Entry Screens
- Patient Inquiry Screen

## New Visit Entry Screen and Edit Visit Entry Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The New Visit Entry screen and the Edit Visit Entry screen have been updated to reflect either ICD-9 and/or ICD-10 codes.

Example of New Visit Entry Screen or Edit Visit Entry Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>QUASAR V 3. NEW VISIT ENTRY OR EDIT VISIT ENTRY</p>
<p>Patient Diagnostic History</p>
<p>Ms. QUASARPATIENT has been seen for the following:</p>
<p>DIAGNOSIS DATE ENTERED</p>
<p>------------------------------------------------------------------------------</p>
<p>ICD-9-CM</p>
<p>389.18   SENSONRL HEAR LOSS, BILAT 03/16/06</p>
<p>388.31   SUBJECTIVE TINNITUS 03/16/06</p>
<p>ICD-10-CM</p>
<p>H90.3     SENSONRL HEAR LOSS, BILAT 10/15/15</p>
<p>H93.1     TINNITUS, BILAT 10/15/15</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Patient Inquiry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Inquiry screen has been updated to reflect either ICD-9 and/or ICD-10 codes.

Example of Patient Inquiry Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patient Inquiry</p>
<p>Patient Diagnostic History</p>
<p>Ms. QUASARPATIENT has been seen for the following:</p>
<p>DIAGNOSIS DATE ENTERED</p>
<p>------------------------------------------------------------------------------</p>
<p>ICD-9-CM</p>
<p>389.18   SENSONRL HEAR LOSS, BILAT 03/16/06</p>
<p>388.31   SUBJECTIVE TINNITUS 03/16/06</p>
<p>ICD-10-CM</p>
<p>H90.3     SENSONRL HEAR LOSS, BILAT 10/15/15</p>
<p>H93.1     TINNITUS, BILAT 10/15/15</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports have been modified to accommodate ICD-10 codes:

- Visits by Diagnosis
- Tailor-Made A&SP Reports
- Print A&SP Capitation Report
- Print A&SP File Entries

## Visits by Diagnosis 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Visits by Diagnosis report has been updated to reflect both ICD-9 and ICD-10 codes.

> **NOTE:** If the date range does not include ICD-10 data, the report does not indicate ICD-9 code designation.

Example of Visits by Diagnosis Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Audiology &amp; Speech Pathology</p>
<p>Diagnostic Code Statistics</p>
<p>for</p>
<p>XXXXXXXX</p>
<p>Covering Visits from 01/01/09 to 10/15/15</p>
<p>For Division: NASHVILLE</p>
<p>-----------------------------------------------------------------------------</p>
<p>STOP CODE: SPEECH PATHOLOGY</p>
<p>CLINIC: SPEECH PATH - CHRISTY</p>
<p>CLINICIAN: XXXXXXXX</p>
<p>ICD-9 DIAGNOSIS</p>
<p>141.9 MALIG NEO TONGUE NOS COUNT: 3</p>
<p>386.54 HYPOACT LABYRINTH BILAT COUNT: 1</p>
<p>387.9 OTOSCLEROSIS NOS COUNT: 1</p>
<p>V41.2 PROBLEMS WITH HEARING COUNT: 1</p>
<p>V53.2 ADJUSTMENT HEARING AID COUNT: 2</p>
<p>V57.3 SPEECH-LANGUAGE THERAPY COUNT: 1</p>
<p>V70.5 HEALTH EXAM-GROUP SURVEY COUNT: 1</p>
<p>ICD-10 DIAGNOSIS</p>
<p>F07.0 PERSONALITY CHANGE DUE TO KNOWN COUNT 1</p>
<p>PHYSIOLOGICAL CONDITION:</p>
<p>G31.84 MILD COGNITIVE IMPAIRMENT, SO STATED COUNT: 1</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>Printed: 10/15/15 at 09:42 Page: 2</p>
<p>Audiology &amp; Speech Pathology</p>
<p>Diagnostic Code Statistics</p>
<p>For Division: NASHVILLE</p>
<p>Summary</p>
<p>-----------------------------------------------------------------------------</p>
<p>STOP CODE: SPEECH PATHOLOGY</p>
<p>141.9 MALIG NEO TONGUE NOS COUNT: 3</p>
<p>386.54 HYPOACT LABYRINTH BILAT COUNT: 1</p>
<p>387.9 OTOSCLEROSIS NOS COUNT: 1</p>
<p>F07.0 PERSONALITY CHANGE DUE TO KNOWN COUNT 1</p>
<p>PHYSIOLOGICAL CONDITION:</p>
<p>G31.84 MILD COGNITIVE IMPAIRMENT, SO STATED COUNT: 1</p>
<p>V41.2 PROBLEMS WITH HEARING COUNT: 1</p>
<p>V53.2 ADJUSTMENT HEARING AID COUNT: 2</p>
<p>V57.3 SPEECH-LANGUAGE THERAPY COUNT: 1</p>
<p>V70.5 HEALTH EXAM-GROUP SURVEY COUNT: 1</p>
<p>Total For SPEECH PATHOLOGY 12</p>
<p>Total For Division: NASHVILLE 12</p>
<p>Enter RETURN to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## A&SP Clinic Visit Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A&SP Clinic Visit report has been updated to reflect both ICD-9 and ICD-10 codes.

Example of Clinic Visit Report

A&SP CLINIC VISIT LIST NOV 22, 2013 13:22 PAGE 1

TIME

SPENT DIAGNOSTIC

PATIENT NAME DATE PRIMARY PROVIDER (minutes) CODE

------------------------------------------------------------------------------

QUASARPATIENT1,TWO AUG 16, 1999 QUASARPROVIDER, SIX 30 388.12

QUASARPATIENT1,ONE AUG 16, 1999 QUASARPROVIDER, SIX 25 388.1

QUASARPATIENT1,FOUR OCT 15, 2015 QUASARPROVIDER, SIX 30 H93.19

> **NOTE:** CDR and audiometric fields in QUASAR are obsolete. CDR is no longer used and the audiometric functionality was replaced by GUI QUASAR (audiometric module).

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following QUASAR routines were added to accommodate the ICD-10 code set:

| Routine Name | Function                                                         |
|--------------|------------------------------------------------------------------|
| ACKQ3P21     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P22     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P23     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P24     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P25     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P26     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P27     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P28     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P29     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P30     | Stores ICD-10 Diagnosis data                                     |
| ACKQ3P31     | Stores ICD-10 Diagnosis data                                     |
| ACKQAICD     | Utility to determine whether or not to use ICD-9 or ICD-10 codes |

## Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text has been updated for ICD-10 Diagnosis codes.

Changes to Online Help Text

Select DIAGNOSTIC CODE: 141.9// ?

Answer with DIAGNOSTIC CODE

Choose from:

141.9

V53.2

V53.2

V57.3

V70.5

You may enter a new DIAGNOSTIC CODE, if you wish

Enter an ICD code for this clinic visit.

The diagnostic code must be active and consistent with the stop code.

Answer with A&SP DIAGNOSTIC CONDITION CODE

Do you want the entire A&SP DIAGNOSTIC CONDITION List?

*(This page intentionally left blank)*