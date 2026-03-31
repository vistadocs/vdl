---
title: Occurrence Screen Version 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
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
description: - [# Introduction](#introduction) - [# Implementation and Maintenance](#implementation-and-maintenance) - [Package-wide Variables](#package-wide-variables) - [# Routines](#routines) - [Routines to Map](#routines-to-map) - [Callable Routines](#callable-routines) - [Routine List](#routine-list) - [# F
audience: 
keywords: 
  - occurrence
  - table
  - contents
  - class
  - strong
  - options
  - package
  - routines
  - access
  - even
page_count: 0
word_count: 3347
section_count: 16
table_count: 123
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/9/09
revision_oldest: 3/9/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/octm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Occurrence_Screen/octm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=49"
---

![](occurrence-screen-version-3-technical-manual/001.png)

Occurrence Screen V. 3.0Technical ManualSeptember 1993

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
- [# Implementation and Maintenance](#implementation-and-maintenance)
- [Package-wide Variables](#package-wide-variables)
- [# Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Routine List](#routine-list)
- [# Files](#files)
  - [File List](#file-list)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
- [Exported Options](#exported-options)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Options](#exported-options-1)
- [Cross References](#cross-references)
- [Archiving and Purging](#archiving-and-purging)
- [External/Internal Relations](#externalinternal-relations)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
  - [XIndex](#xindex)
  - [Inquire to Options File](#inquire-to-options-file)
  - [Print Options File](#print-options-file)
  - [List File Attributes](#list-file-attributes)
- [Security](#security)
  - [General Security](#general-security)
  - [Security Keys](#security-keys)
  - [FileMan Access Codes](#fileman-access-codes)
- [Glossary](#glossary)
The Occurrence Screen package is a fully integrated system which is compatible with V. 7.0 of Kernel and V. 19 of VA FileMan.
The objectives of the package are to increase efficiency in the documenting of occurrences, permit better trend analysis, and provide a consistent format for stored data to be used for QM review at the regional and national levels.
There are two major components of this package: the automated capture of occurrences for screening and the automation of the review process. The software contains programs that do the following.
Auto Enrollment
Daily running of the auto enrollment routines populates the Occurrence Screen data base. Auto enrollment is performed by the Clinical Monitoring System. For further information, please see the Clinical Monitoring System Technical Manual.
Manual Enrollment
Provides for manual enrollment into the data base of occurrences not captured by the auto enrollment due to data not being available in the system at this time.
Worksheets
Produces copies of Clinical, Peer, Management, Committee, and worksheets to use in the review process.
Standard reports
Produces reports for trend analysis, including the mandated Semi-Annual report of occurrences.
Ad Hoc reports
Permits the creation of Ad Hoc reports by building sort and print templates on the fly.

# # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At implementation, the Package Setup Menu in the Occurrence Screen Manager Menu should be used to set up site-specific data. The Clinical Monitoring System Site Parameters Edit option should also be utilized and the fields populated. The easiest method of entering all the site parameters is to use the Combined Site Parameters Edit \[QAQ SITE PARAMETERS\] option in the QM Manager menu \[QAQ MANAGER\]. Instructions concerning the entry of this data is contained in the Occurrence Screen User Manual.

It is also necessary to queue the daily running of the auto enrollment routine.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No variables are used package wide.

# # Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines to map in the Occurrence Screen package.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Interim Management Support package has been given formal entry points into the Occurrence Screen package. The supported entry points are as follows.

PAD0^QAOSXTRN

Prints the Adverse Findings Report without practitioner names or codes

PSM0^QAOSXTRN

Prints the Summary of Occurrence Screening (Semi-Annual) Report

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain a listing of the routines contained in the Occurrence Screen package.

1\. Programmer Options Menu

2\. Routine Tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: QAOS\*

# # Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>File Number/Name</u> <u>Global</u> <u>Description</u>

741

QA OCCURRENCE SCREEN QA(741, Contains Occurrence Screen

data for each occurrence

screened at the .01 level.

\*741.1

QA OCCURRENCE SCREEN CRITERIA QA(741.1, Contains the list of screens

required by the Occurrence

Screen Circular, with

description.

\*741.2

QA OCCURRENCE REVIEW LEVEL QA(741.2, Contains the list of review

levels.

741.3++

QA OCCURRENCE CLINICAL QA(741.3, Contains the names of persons

REVIEWER authorized to be clinical

reviewers.

\*741.4

QA OCCURRENCE CLINICAL QA(741.4, Contains the list of reasons for

REFERRAL clinical referral for further

review as defined by the OS

Circular.

\*741.5

QA OCCURRENCE EXCEPTION QA(741.5, Contains the list of exceptions

for each screen as defined by

the OS Circular.

\*File comes with data

++ This file is not longer used. The functionality has been replaced by the QAOSCLIN security key.

<u>File Number/Name</u> <u>Global</u> <u>Description</u>

\*741.6

QA OCCURRENCE FINDINGS QA(741.6, Contains non-specific locations

in a hospital where an incident

may take place.

\*741.7

QA OCCURRENCE ACTION QA(741.7, Contains the list of standard-

ized actions to be taken as a

result of the review findings.

\*7421.8

QA OCCURRENCE SEVERITY QA(741.8, Contains the list of severity of

OF OUTCOME outcome levels as defined by

QM.

741.9

QA OCCURRENCE TREATING QA(741.9, Contains an entry for each

SPECIALTY treating specialty at the site.

741.93

QA OCCURRENCE MEDICAL TEAM QA(741.93, Contains the list of medical

teams at the site.

741.95

QA OCCURRENCE NUMBER QA(741.95, Contains the number of cases

CASES SCREENED screened.

741.97

QA OCCURRENCE COMMITTEE QA(741.97, Contains the list of standing

committees at the site.

741.99

QA OCCURRENCE AUTO QA(741.99, Contains historical list of dates

RUN DATES that auto enrollment was run.

The following are the steps you may take to obtain information concerning the files and templates contained in the Occurrence Screen package.

## File Flow (Relationships between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: Print Template

Sort Template

Input Template

List Template

4\. Sort by: Name

5\. Start with name: QAOS to QAOSZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information about menus and exported options concerning the Occurrence Screen package.

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Programmers Options

2\. Menu Management Menu

3\. Display Menus and Options Menu

4\. Diagram Menus

5\. Select User or Option Name: QAOS Main Menu

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: OPTION

4\. Sort by: Name

5\. Start with name: QAOS to QAOSZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

# Cross References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QA OCCURRENCE SCREEN file (#741)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>File, Field #</u></strong></td>
<td><strong><u>Field Name</u></strong></td>
<td><strong><u>X-Ref</u></strong></td>
<td><strong><u>Description</u></strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741,.01</td>
<td>QA PATIENT</td>
<td><p>B</p>
<p>AA1</p>
<p>AOCID</p></td>
<td><p>Required.</p>
<p>Screen, Date of Occurrence, Patient, and D0.</p>
<p>Trigger the OCCURRENCE IDENTIFIER field.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741,1</td>
<td>DATE</td>
<td><p>C</p>
<p>AA2</p>
<p>AOCID2</p>
<p>ATED</p>
<p>AED</p></td>
<td><p>Regular x-ref used for look-up.</p>
<p>Screen, Date of Occurrence, Patient, and D0.</p>
<p>Trigger the OCCURRENCE IDENTIFIER field.</p>
<p>Trigger the TOTAL ELAPSED DAYS field.</p>
<p>Trigger the reviewer ELAPSED DAYS field.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741,2</td>
<td>OCCURRENCE IDENTIFIER</td>
<td>E</td>
<td>Regular x-ref used for look-up.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741,3</td>
<td>SCREEN</td>
<td><p>D</p>
<p>AA3</p></td>
<td><p>Regular x-ref used for look-up.</p>
<p>Screen, Date of Occurrence, Patient, and D0.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.01,.01</td>
<td>REVIEW LEVEL</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.01,1</td>
<td>DATE REVIEW COMPLETED</td>
<td><p>ALAPSE</p>
<p>ADUES</p></td>
<td><p>Trigger the reviewer ELAPSED DAYS field.</p>
<p>Trigger the PEER &amp; MANAGEMENT DUE DATE fields.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.12,.01</td>
<td>REASON FOR EXCEPTION</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.15,.01</td>
<td>ACTION</td>
<td>B</td>
<td>Required</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.01,9</td>
<td>FINAL PEER REVIEW PER SERVICE</td>
<td>AONLY1</td>
<td><p>Regular x-ref.</p>
<p>Used to track only one YES per Peer per service.</p></td>
</tr>
</tbody>
</table>

|                           |                               |                  |                                                                                      |
|---------------------------|-------------------------------|------------------|--------------------------------------------------------------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u>         | <u>X-Ref</u> | <u>Description</u>                                                               |
| 741,11                    | STATUS                        | AD               | Regular x-ref used for sorting by status.                                            |
|                           |                               |                  |                                                                                      |
| 741,14                    | FINAL DISPOSITION DATE        | AC               | Trigger the TOTAL ELAPSED DAYS field.                                                |
|                           |                               |                  |                                                                                      |
| 741.017                   | COMMITTEE                     | B                | Required.                                                                            |
|                           |                               |                  |                                                                                      |
| 741,18                    | \*DATE VALIDATED / CONFIRMED  | AVAL             | Regular x-ref, no longer used (field marked for deletion).                           |
|                           |                               |                  |                                                                                      |
| 741.024,.01               | PEER ATTRIBUTION (INDIVIDUAL) | B                | Required.                                                                            |
|                           |                               |                  |                                                                                      |
| 741.025,.01               | PEER ATTRIBUTION (MED TEAM)   | B                | Required.                                                                            |
|                           |                               |                  |                                                                                      |
| 741.026,.01               | PEER ATTRIBUTION (HOSP LOC)   | B                | Required.                                                                            |
|                           |                               |                  |                                                                                      |
| 741,27                    | AUDIT                         | AUDIT            | Trigger to delete an audit trail record when an Occurrence Screen record is deleted. |
|                           |                               |                  |                                                                                      |
| 741,28                    | RECORD CREATION DATE          | ARCD             | Regular x-ref used by auto enroll for counting manually entered occurrences.         |

QA OCCURRENCE SCREEN CRITERIA file (#741.1)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>File, Field #</u></strong></td>
<td><strong><u>Field Name</u></strong></td>
<td><strong><u>X-Ref</u></strong></td>
<td><strong><u>Description</u></strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.1,.01</td>
<td>CODE</td>
<td><p>B</p>
<p>BA</p></td>
<td><p>Required.</p>
<p>MUMPS x-ref on only the integer portion of the code.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.1,2</td>
<td>EXPANDED SCREEN</td>
<td>C</td>
<td>Regular x-ref used for look-up.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.1,200</td>
<td>ASSOCIATED MONITOR</td>
<td>AM</td>
<td>Regular x-ref used by auto enroll to determine which screens are auto enroll screens.</td>
</tr>
</tbody>
</table>

QA OCCURRENCE REVIEW LEVEL file (#741.2)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.2,.01                 | LEVEL                 | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.2,1                   | REVIEW LEVEL NUMBER   | C                | Regular x-ref used for look-up. |

\*QA OCCURRENCE CLINICAL REVIEWER file (#741.3)

|                           |                       |                  |                        |
|---------------------------|-----------------------|------------------|------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u> |
|                           |                       |                  |                        |
| 741.3,.01                 | \*NAME                | B                | Required.              |

QA OCCURRENCE CLINICAL REFERRAL file (#741.4)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>File, Field #</u></strong></td>
<td><strong><u>Field Name</u></strong></td>
<td><strong><u>X-Ref</u></strong></td>
<td><strong><u>Description</u></strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.4,.01</td>
<td>REASON (SCREEN CODE)</td>
<td><p>B</p>
<p>AC1</p></td>
<td><p>Required.</p>
<p>Screen, hashed Reason (Screen Code) and D0.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.4,2</td>
<td>SCREEN</td>
<td>AC</td>
<td>Screen, hashed Reason (Screen Code) and D0.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.4,3</td>
<td>REASON - SHORT</td>
<td>C</td>
<td>Regular x-ref used for look-up.</td>
</tr>
</tbody>
</table>

QA OCCURRENCE EXCEPTIONS file (#741.5)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.5,.01                 | REASON                | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.5,.02                 | CODE                  | D                | Regular x-ref used for look-up. |
|                           |                       |                  |                                 |
| 741.5,1                   | SCREEN                | C                | Regular x-ref used for look-up. |

QA OCCURRENCE FINDINGS file (#741.6)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.6,.01                 | CODE                  | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.6,1                   | FINDINGS              | C                | Regular x-ref used for look-up. |

QA OCCURRENCE ACTION file (#741.7)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.7,.01                 | CODE                  | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.7,2                   | ACTION                | C                | Regular x-ref used for look-up. |

QA OCCURRENCE SEVERITY OF OUTCOME file (#741.8)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.8,.01                 | SEVERITY LEVEL        | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.8,1                   | SEVERITY              | C                | Regular x-ref used for look-up. |

QA OCCURRENCE TREATING SPECIALTY file (#741.9)

|                           |                       |                  |                        |
|---------------------------|-----------------------|------------------|------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u> |
|                           |                       |                  |                        |
| 741.9,.01                 | TREATING SPECIALTY    | B                | Required.              |

QA OCCURRENCE MEDICAL TEAM file (#741.93)

|                           |                       |                  |                        |
|---------------------------|-----------------------|------------------|------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u> |
|                           |                       |                  |                        |
| 741.93,.01                | DESIGNATION           | B                | Required.              |

QA OCCURRENCE NUMBER CASES SCREENED file (#741.95)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><u>File, Field #</u></strong></td>
<td><strong><u>Field Name</u></strong></td>
<td><strong><u>X-Ref</u></strong></td>
<td><strong><u>Description</u></strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.95,.01</td>
<td>*BEGINNING DATE</td>
<td><p>B</p>
<p>AA1</p></td>
<td><p>Required.</p>
<p>*Beginning Date, *Ending Date and D0.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>741.95,.02</td>
<td>*ENDING DATE</td>
<td>AA2</td>
<td>*Beginning Date, *Ending Date and D0.</td>
</tr>
</tbody>
</table>

QA OCCURRENCE COMMITTEE file (#741.97)

|                           |                       |                  |                                 |
|---------------------------|-----------------------|------------------|---------------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u>          |
|                           |                       |                  |                                 |
| 741.97,.01                | COMMITTEE             | B                | Required.                       |
|                           |                       |                  |                                 |
| 741.97,1                  | ABBREVIATION          | C                | Regular x-ref used for look-up. |

QA OCCURRENCE AUTO RUN DATES file (#741.99)

|                           |                       |                  |                        |
|---------------------------|-----------------------|------------------|------------------------|
| <u>File, Field \#</u> | <u>Field Name</u> | <u>X-Ref</u> | <u>Description</u> |
|                           |                       |                  |                        |
| 741.99,.01                | AUTO ENROLL RUN DATE  | B                | Required.              |

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Archiving

At the present time, there is no provision for archiving records, as no determination has yet been made by the Office of Quality Management on how long records are to be retained.

Purging

If the user wishes to delete a record in the QA Occurrence Screen file (#741), the option is available to them to mark the record as deleted, but still retain it in the file. The Purge Deleted Occurrence Screen Records option found in the Purge/Delete Menu of the Occurrence Screen Manager Menu may be used to remove these records from the file.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

External Relations

|             |                                   |                                                                                                                      |
|-------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|
| FILE \# | FILE NAME                     | USAGE                                                                                                            |
|             |                                   |                                                                                                                      |
| 2           | Patient                           | Used to extract patient data, such as name, SSN, admission date.                                                     |
|             |                                   |                                                                                                                      |
| 4.2         | Domain                            | Used by the Early Warning System options.                                                                            |
|             |                                   |                                                                                                                      |
| 40.7        | Clinic Stop                       | Used by the auto enroll routines.                                                                                    |
|             |                                   |                                                                                                                      |
| 41.1        | Scheduled Admission               | Used by the auto enroll routines.                                                                                    |
|             |                                   |                                                                                                                      |
| 42          | Ward Location                     | Used in the auto enroll routines and various reports.                                                                |
|             |                                   |                                                                                                                      |
| 44          | Hospital Location                 | Used to extract attribution location for inclusion in File 741.                                                      |
|             |                                   |                                                                                                                      |
| 45.7        | Facility Treating Specialty       | Used to extract Treating Specialties to populate File 741.                                                           |
|             |                                   |                                                                                                                      |
| 49          | Service/Section                   | Used to extract Service for inclusion in File 741.                                                                   |
|             |                                   |                                                                                                                      |
| 130         | Surgery                           | Used by the auto enroll routines.                                                                                    |
|             |                                   |                                                                                                                      |
| 200         | New Person                        | Used to extract user for inclusion in File 741.                                                                      |
|             |                                   |                                                                                                                      |
| 405         | Patient Movement                  | Used by the auto enroll routines, the reviewer worksheets, and the 101 to 101.1 conversion.                          |
|             |                                   |                                                                                                                      |
| 405.2       | MAS Movement Type                 | Used by the auto enroll routines.                                                                                    |
|             |                                   |                                                                                                                      |
| 409.5       | Scheduling Visits                 | Used by the auto enroll routines.                                                                                    |
|             |                                   |                                                                                                                      |
| 740         | Quality Assurance Site Parameters | Used to store site parameters.                                                                                       |
|             |                                   |                                                                                                                      |
| 740.1       | Ad Hoc Macro                      | Used by the Ad Hoc Reports option.                                                                                   |
|             |                                   |                                                                                                                      |
| 740.5       | QA Audit                          | Used to store name of user, date of action and type of action for each and every entry made by users via VA FileMan. |
|             |                                   |                                                                                                                      |
| 743         | QA Monitor                        | Used to perform the Occurrence Screen auto enroll.                                                                   |

Internal Relations

The package is designed to allow for tailoring of menus for particular users. This is to be determined by the QM Coordinator at each site, based on how the components of the QM task are assigned. The Occurrence Screen Manager Menu options are intended for use by the QM Coordinator. The Report menu can also stand alone if desired.

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure Occurrence Screen (OS) technical documentation. On-line technical documentation pertaining to the OS software, in addition to that which is located in the help prompts and on the help screens which are found throughout the OS package, may be generated through utilization of several KERNEL options. These include but are not limited to: XINDEX, Menu Management Inquire Option File, Print Option File, and FileMan List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the VistA Kernel Reference Manual.

## XIndex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the OS package, specify the following namespace at the "routine(s) ?\>" prompt: QAOS\*.

OS initialization routines which reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the OS namespace should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

## Inquire to Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu Manager option provides the following information about a specified option(s): option name, menu text, option description, type of option, and lock (if any). In addition, all items on the menu are listed for each menu option.

To secure information about OS options, the user must specify the name or namespace of the option(s) desired. QAOS is the namespace associated with the OS package.

## Print Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of OS options, the following option namespace should be specified: QAOS.

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security is maintained through menu distribution and assignment. The QM Coordinator will decide who is authorized to have the QM Manager Menu, which is used to maintain the files. Standard VA FileMan access has been applied to the files. VA FileMan access should be limited to those persons with NEED TO KNOW status. Data within the Occurrence Screen system is protected by the Privacy Act, and Title 38 U.S.C. 5705, as amended by Public Law 99-166 and the implementing HSRO (Health Services Review Organization) regulations in Title 38 Part 17. Exempt from this protection are aggregate statistical and trend reports that do not identify individual VA patients or employees.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The package uses a new security key, QAOSCLIN. The QAOSCLIN key is used to screen the reviewer NAME (#741.01,.02) field for Clinical reviewers. This key replaces the functionality of the QA OCCURRENCE CLINICAL REVIEWER file (#741.3).

## FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of recommended VA FileMan access codes associated with each file contained in the OS package. This list may be used to assist in assigning users appropriate VA FileMan access codes.

File File DD RD WR DEL LAYGO AUDIT

<u>Number</u> <u>Name</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>access</u>

741 QA OCCURRENCE SCREEN @ @

741.1 QA OCCURRENCE SCREEN

CRITERIA @ @

741.2 QA OCCURRENCE REVIEW

LEVEL @ @ @

741.3 \*QA OCCURRENCE

CLINICAL REVIEWER @ @

741.4 QA OCCURRENCE

CLINICAL REFERRAL @ @ @

741.5 QA OCCURRENCE

EXCEPTION @ @

FileMan Access Codes

File File DD RD WR DEL LAYGO AUDIT

<u>Number</u> <u>Name</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>access</u>

741.6 QA OCCURRENCE FINDINGS @ @ @

741.7 QA OCCURRENCE ACTION @ @ @

741.8 QA OCCURRENCE SEVERITY

OF OUTCOME @ @ @

741.9 QA OCCURRENCE

TREATING SPECIALTY @ @

741.93 QA OCCURRENCE

MEDICAL TEAM @ @

741.95 \*QA OCCURRENCE NUMBER

CASES SCREENED @

741.97 QA OCCURRENCE

COMMITTEE @ @

741.99 QA OCCURRENCE AUTO

RUN DATES @ @ @

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
