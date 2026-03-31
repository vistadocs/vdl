---
title: Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.2
patch_id: EDIS*2.1.2
group_key: "EDIS:EDIS:2.1.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - edis
  - contents
  - report
  - software
  - emergency
  - codes
  - modifications
  - worksheet
  - patient
page_count: 0
word_count: 2837
section_count: 15
table_count: 5
figure_count: 9
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

ICD-10 Follow On Class 1 Software Remediation Project

Emergency Department Integration Software (EDIS)

Release Notes

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/001.png)

VistA EDP\*2.0\*2

GUI EDIS Version 2.1.2

November 2014

Office of Information and Technology (OI&T)

Product Development

Revision History

| Date          | Version | Description                          | Author                                                               |
|---------------|---------|--------------------------------------|----------------------------------------------------------------------|
| November 2014 | 1.0     | Tech Writer edit; baseline document. | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| March 2014    | 0.1     | Draft document.                      | HP                                                                   |

Table 1: ICD-9-CM and ICD-10-CM Comparison

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [New Features and Functions](#new-features-and-functions)
  - [ICD Codes Change](#icd-codes-change)
  - [Text on Screens](#text-on-screens)
    - [Modifications to the Disposition Pane in Edit Closed View](#modifications-to-the-disposition-pane-in-edit-closed-view)
    - [Modifications to the Disposition Pane in the Visit Worksheet View](#modifications-to-the-disposition-pane-in-the-visit-worksheet-view)
    - [Modifications to the Delay Report](#modifications-to-the-delay-report)
    - [Modifications to the ED Mental Health Patients Report](#modifications-to-the-ed-mental-health-patients-report)
    - [Modifications to the Exposure Report](#modifications-to-the-exposure-report)
    - [Modifications to the VA Admissions Report](#modifications-to-the-va-admissions-report)
    - [Modifications to the Activity Report](#modifications-to-the-activity-report)
    - [Modifications to the Active Problems Pane in Assess Worksheet View](#modifications-to-the-active-problems-pane-in-assess-worksheet-view)
- [ICD-10 Searches](#icd-10-searches)
  - [ICD-10-CM Diagnosis Code Search](#icd-10-cm-diagnosis-code-search)
- [Additional Software Fixes](#additional-software-fixes)
  - [Remove Patient without Provider for Certain Dispositions](#remove-patient-without-provider-for-certain-dispositions)
  - [Correct Nurse and Resident Roles in Edit Closed](#correct-nurse-and-resident-roles-in-edit-closed)
  - [Fix Bed Selection in Visit Worksheet](#fix-bed-selection-in-visit-worksheet)
  - [Remove Provider Report](#remove-provider-report)
  - [Fix Visit Worksheet When Switching from Edit Closed](#fix-visit-worksheet-when-switching-from-edit-closed)
- [Technical Information](#technical-information)
  - [Routines](#routines)
  - [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Emergency Department Integration Software (EDIS) software contained in patch EDP\*2.0\*2 and EDIS 2.1.2.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after October 1, 2015 (current implementation date).

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

Table 2: ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

Table 3: ANONYMOUS Software Directories

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

EDIS is used by healthcare professionals to track and manage the flow of patient care in the Emergency Department. EDIS utilizes Web-based views that provide users with the following capabilities:

- Add emergency department patients to the Display Board
- View information about patients on the Display Board
- Edit patient information on the Display Board
- Remove patients from the Display Board
- Generate administrative reports
- Input discharge diagnosis

EDIS integrates with VistA Scheduling (Appointment Management) through the creation of scheduled or unscheduled appointments; these appointments will display in the Computerized Patient Record System (CPRS).

EDIS is a Java-based package with a Graphical User Interface (GUI).

Patch EDP\*2\*2/EDIS v2.1.2 makes the following changes to the EDIS application:

- ICD-10-CM replaces ICD-9-CM as the diagnostic coding system for outpatient encounters with an encounter date on or after the ICD-10 activation date.
- Online forms display “ICD-10” instead of “ICD-9” where appropriate.
- Search features for codes are standardized and enhanced.
- On the EDIS Configuration window, if you do not select Diagnosis must be coded as ICD, the application accepts only free-text diagnoses (the default setting), and does not utilize ICD codes. Free-text diagnoses have no ICD impact.

In addition, EDP\*2\*2/EDIS v.2.1.2 fixes the following Remedy tickets:

1.  CQ EDIS00001187 (Remedy INC000000897239): EDIS will now allow a user to remove a patient without selecting a Provider for the following special classes of Disposition:
    1.  Left without being treated
    2.  Patient name entered in error
    3.  Sent to primary care
2.  CQ EDIS00001188 (Remedy INC000000897799): Nurses and Resident roles now correctly open the Edit Closed worksheet.
3.  CQ EDIS00001189 (Remedy INC000000898138): Selecting the first bed in the list of the Visit worksheet no longer brings up a 'Missing Bed' popup when clicking on the "Save" button.
4.  CQ EDIS00001190: The Provider report has been removed from EDIS.
5.  CQ EDIS00001192: After a user switches from viewing an Edit Closed worksheet to editing and saving a Visit worksheet, the Visit worksheet no longer blanks out.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents and files are available on the Anonymous software directories identified in the table below:

- EDIS v.2.1.2 Server and Client Installation Guide
- EDIS v.2.1.2 Big Board Installation Guide
- EDIS v.2.1.2 Release Notes
- EDIS v.2.1.2 Technical Manual
- EDIS v.2.1.2 User Guide
- EDIS Glossary
- EDIS Installation Package Zip File (contains Launch_EDIS.bat and edisautologon.reg)

The documents (except the zip file) are also available on the VistA Documentation Library (VDL), which is located at <http://www.va.gov/vdl/application.asp?appid=179>.

| OIFO                | FTP Address                                                          | Directory                                                            |
|---------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Albany              | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| Hines               | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| Salt Lake City      | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| VistA Download Site | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |

Table 4: Document Files

The documents appear on the Anonymous software directories under the file names listed in the table below.

<table style="width:100%;">
<caption><p>Table 5: Updated Routines</p></caption>
<colgroup>
<col style="width: 65%" />
<col style="width: 25%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Title</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDIS_2_1_2_IG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Server and Client Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_BigBrd_IG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Big Board Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDIS_2_1_2_RN.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Release Notes</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_TM.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Technical Manual</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDIS_2_1_2_UG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 User Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_Glossary.PDF</td>
<td>Emergency Department Integration Software Glossary</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>EDP2_1_1.zip</p>
<p><strong>NOTE:</strong> The zip file and its contents have NOT been updated for the EDIS v.2.1.2/EDP*2.0*2 release. The file is included with the latest release documentation for ease of reference but is still named for the release in which it was last modified (EDIS v.2.1.1/EDP*2.0*6).</p></td>
<td>Emergency Department Integration Software Installation Package Zip File</td>
<td>Binary</td>
</tr>
</tbody>
</table>

Table 5: Updated Routines

# New Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

## ICD Codes Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generally, on or after October 1, 2015, the available diagnosis codes will change from ICD-9 to ICD-10. This change is keyed on the dates of patient service, which is the Time In for the Emergency Department visit.

For example, if the patient’s emergency department visit Time In is before the ICD-10 activation date, then ICD-9 codes are used. If the patient’s emergency department visit Time In is on or after the ICD-10 activation date, then ICD-10 codes will be used.

## Text on Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several reports have information added to differentiate between ICD-9 and ICD-10 entries.

### Modifications to the Disposition Pane in Edit Closed View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See callouts below.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/002.png)

Figure 1: Disposition Pane in Edit Closed View

### Modifications to the Disposition Pane in the Visit Worksheet View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See callouts below.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/003.png)

Figure 2: Disposition Pane in Visit Worksheet View

### Modifications to the Delay Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“ICD” and “ICD Type” columns have been added right after the Diagnoses column.

If the report start date is *prior to* the ICD-10 activation date, and stop date is *on or after* the ICD-10 activation date (which means that patient visits with ICD-9 diagnoses <u>and</u> patient visits with ICD-10 diagnoses associated may appear on the report), the new “ICD” column displays the appropriate code and the new “ICD Type” column indicates ICD-9-CM or ICD-10-CM as applicable.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/004.png)

Figure 3: Delay Report

### Modifications to the ED Mental Health Patients Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICD-10 update differentiates between ICD-9-CM selection criteria and ICD-10-CM selection criteria to determine which records will be included in the ED Mental Health Patients Report View/Export/Print to include Records with ICD-10-CM Diagnosis Codes in Categories F10 through F99 Inclusive (as shown below) on or after the ICD-10 activation date.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/005.png)

Figure 4: ICD-10-CM List of Diseases, Chapter 5, Mental and Behavioral Disorders (F01-F99)

ED Mental Health Patients Report View

“ICD” and “ICD Type” columns have been added right after the Diagnoses column.

If the report start date is *prior to* the ICD-10 activation date, and stop date is *on or after* the ICD-10 activation date (which means that patient visits with ICD-9 diagnoses <u>and</u> patient visits with ICD-10 diagnoses associated may appear on the report), the new “ICD” column displays the appropriate code and the new “ICD Type” column indicates ICD-9-CM or ICD-10-CM as applicable.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/006.png)

Figure 5: ED Mental Health Patients Report

### Modifications to the Exposure Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“ICD” and “ICD Type” columns have been added right after the Diagnoses column.

The “Time In” for the visit determines whether the new “ICD” column displays the ICD-9 or ICD-10 code and the new “ICD Type” column indicates ICD-9-CM or ICD-10-CM as applicable.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/007.png)

Figure 6: Exposure Report

### Modifications to the VA Admissions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“ICD” and “ICD Type” columns have been added right after the Diagnoses column.

If the report start date is *prior to* the ICD-10 activation date, and stop date is *on or after* the ICD-10 activation date (which means that patient visits with ICD-9 diagnoses <u>and</u> patient visits with ICD-10 diagnoses associated may appear on the report), the new “ICD” column displays the appropriate code and the new “ICD Type” column indicates ICD-9-CM or ICD-10-CM as applicable.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/008.png)

Figure 7: VA Admissions Report

### Modifications to the Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“ICD” and “ICD Type” columns have been added right after the Diagnoses column.

If the report start date is *prior to* the ICD-10 activation date, and stop date is *on or after* the ICD-10 activation date (which means that patient visits with ICD-9 diagnoses <u>and</u> patient visits with ICD-10 diagnoses associated may appear on the report), the new “ICD” column displays the appropriate code and the new “ICD Type” column indicates ICD-9-CM or ICD-10-CM as applicable.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/009.png)

Figure 8: Activity Report

### Modifications to the Active Problems Pane in Assess Worksheet View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the patient has Active problems in their Problem List which have ICD-9 diagnosis codes associated, the ICD-9 diagnosis code displays in the ICD column, as per existing functionality. If the patient has Active problems in their Problem List which have ICD-10 diagnosis codes associated, the ICD-10 diagnosis code displays in the ICD column.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/010.png)

Figure 9: Active Problems Pane in Assess Worksheet View

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS package provides the ability to search on ICD-10-CM diagnosis codes.

> **NOTE:** Existing ICD-9 functionality has not changed. If the Time In for the visit (encounter) is prior to the ICD-10 activation date and the end user enters a diagnosis and selects Search, the Diagnosis Search List displays ICD-9–CM diagnoses.

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and display its description. The user interface prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user. 

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes.

ICD-10-CM diagnosis code search highlights include:

- Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.
- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined is the process of selecting the correct valid ICD-10 diagnosis code.
- The user is presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, the user is prompted to refine the search.
- The user can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

# Additional Software Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to introducing ICD-10 functionality, EDP\*2\*2/EDIS v.2.1.2 fixes the Remedy tickets described below.

## Remove Patient without Provider for Certain Dispositions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CQ EDIS00001187 (Remedy INC000000897239): EDIS will now allow a user to remove a patient without selecting a Provider for the following special classes of Disposition:

- Left without being treated
- Patient name entered in error
- Sent to primary care

## Correct Nurse and Resident Roles in Edit Closed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CQ EDIS00001188 (Remedy INC000000897799): Nurses and Resident roles now correctly open the Edit Closed worksheet.

## Fix Bed Selection in Visit Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CQ EDIS00001189 (Remedy INC000000898138): Selecting the first bed in the list of the Visit worksheet no longer brings up a 'Missing Bed' popup when clicking on the "Save" button.

## Remove Provider Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CQ EDIS00001190: The Provider report has been removed from EDIS.

## Fix Visit Worksheet When Switching from Edit Closed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CQ EDIS00001192: After a user switches from viewing an Edit Closed worksheet to editing and saving a Visit worksheet, the Visit worksheet no longer blanks out.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some EDIS routines were modified to replace direct global reads and old Application Programming Interfaces (APIs) with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible.

The routines listed in the table below were updated in patch EDIS v2.1.2/EDP\*2.0\*2. The checksums listed in the “After Checksum” column are new checksums and can be checked with CHECK1^XTSUMBLD.

| Routine Name | Before Checksum | After Checksum |
|--------------|-----------------|----------------|
| EDP22PST     | N/A             | 737172         |
| EDPCONV      | 69787121        | 70928886       |
| EDPFAA       | 36904209        | 37763699       |
| EDPFLEX      | 1745474         | 10693270       |
| EDPLEX       | N/A             | 11049187       |
| EDPLOG       | 58048189        | 64279489       |
| EDPLPCE      | 32808524        | 39952113       |
| EDPQLE       | 43232281        | 55054483       |
| EDPQPCE      | 3317665         | 6816999        |
| EDPRPT1      | 50357723        | 51586751       |
| EDPRPT10     | 30220543        | 32122849       |
| EDPRPT2      | 24332800        | 26475007       |
| EDPRPT7      | 20666458        | 23000869       |
| EDPRPT7C     | 22153636        | 24197469       |
| EDPRPTBV     | 28273730        | 30889629       |
| EDPX         | 12709600        | 16354064       |

## Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emergency Department Integration Software (EDIS) help file is updated to differentiate when ICD‑9‑CM and ICD‑10‑CM diagnosis codes are used according to the ICD-10 activation date requirements.

Click the help file icon ![](emergency-dept-integration-software-gui-edis-version-2-1-2-release-notes/011.png) at the top right of the application to view the help file.