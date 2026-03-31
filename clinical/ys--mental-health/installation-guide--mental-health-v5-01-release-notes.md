---
title: Mental Health Version 5.01 Installation Guide  Release Notes
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 1
description: - [# Preface](#preface) - [# # # # ## Pre-INIT, INIT, and Post-INIT Actions](#pre-init-init-and-post-init-actions) - [Installation of Mental Health V. 5.01 is accomplished through the actions of the package’s pre-INIT, INIT, and post-INIT routines. The main actions of these groups of routines are li
audience: 
keywords: 
  - filed
  - routine
  - mental
  - health
  - conversion
  - compiling
  - yssr
  - print
  - progress
  - reference
page_count: 0
word_count: 13374
section_count: 9
table_count: 13
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/mh5_01.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/mh5_01.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

Decentralized Hospital Computer Program

MENTAL HEALTH

INSTALLATION GUIDE

AND RELEASE NOTES

December 1994

Information Systems Center

Dallas, Texas

# # Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Preface](#preface)
- [# # # # ## Pre-INIT, INIT, and Post-INIT Actions](#pre-init-init-and-post-init-actions)
- [Installation of Mental Health V. 5.01 is accomplished through the actions of the package’s pre-INIT, INIT, and post-INIT routines. The main actions of these groups of routines are listed below.](#installation-of-mental-health-v-501-is-accomplished-through-the-actions-of-the-packages-pre-init-init-and-post-init-routines-the-main-actions-of-these-groups-of-routines-are-listed-below)
    - [Pre-INIT Actions](#pre-init-actions)
    - [INIT Actions](#init-actions)
  - [### Post-INIT Actions](#post-init-actions)
- [#### Mental Health - Deletion of the Out of Order Message](#mental-health-deletion-of-the-out-of-order-message)
  - [Installation Procedures](#installation-procedures)
    - [First Time Installation for Mental Health V. 5.01](#first-time-installation-for-mental-health-v-501)
    - [Installation over Mental Health V. 4.18](#installation-over-mental-health-v-418)
    - [Installation over Mental Health V. 5.0](#installation-over-mental-health-v-50)
  - [Post-Installation Checks and Actions](#post-installation-checks-and-actions)
    - [YS PSYCHTEST Bulletin and Mail Group](#ys-psychtest-bulletin-and-mail-group)
    - [DSM Conversion Data Deletion](#dsm-conversion-data-deletion)
    - [DSM Conversion Routine Deletion](#dsm-conversion-routine-deletion)
- [RELEASE NOTES](#release-notes)
- [Release Notes](#release-notes-1)
  - [DSM Diagnostic Codes Background](#dsm-diagnostic-codes-background)
  - [Mental Health V. 5.0 Changes](#mental-health-v-50-changes)
    - [Visible Changes](#visible-changes)
    - [Technical and/or Transparent Changes](#technical-andor-transparent-changes)
  - [Mental Health V. 5.01 Changes](#mental-health-v-501-changes)
    - [### Visible Changes](#visible-changes-1)
    - [Technical and/or Transparent Changes](#technical-andor-transparent-changes-1)
  - [Package Distribution](#package-distribution)
- [# Appendix](#appendix)
  - [Menu Maps](#menu-maps)
    - [YSUSER Menu Map](#ysuser-menu-map)
    - [YSMANAGER Menu Map](#ysmanager-menu-map)
The Mental Health Version 5.01 Maintenance Release Installation Guide and Release Notes are designed to provide the Department of Veterans Affairs Medical Center (VAMC) Information Resources Management (IRM) Service Chief, Automated Information Systems (AIS) Site Manager, and Clinical Coordinator with the necessary technical information required to install Mental Health V. 5.01. This version repoints the existing patient DSM-III and DSM-III-R data to the new DSM IV diagnostic codes in the DSM file (#627.7) created during installation. The Mental Health V. 5.0 Technical Manual provides the instructions for setting package parameters, making site specific changes, and other Post-Installation setup tasks.

# # # # # ## Pre-INIT, INIT, and Post-INIT Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installation of Mental Health V. 5.01 is accomplished through the actions of the package’s pre-INIT, INIT, and post-INIT routines. The main actions of these groups of routines are listed below.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-INIT Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Mental Health - Menu Options “Out of Order” Message

The following table contains menu options to be placed “Out of Order” by the pre-INIT process.

#### <table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>External Menu Option Text</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Internal Menu Option Name</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Profile of Patient</p>
</blockquote></td>
<td><blockquote>
<p>YSPATPROF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSM-III-R Diagnosis (Problem list)</p>
</blockquote></td>
<td><blockquote>
<p>YSPLDX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Enter Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>YSDIAGE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print Diagnoses</p>
</blockquote></td>
<td><blockquote>
<p>YSDIAGP-DX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print DXLS History</p>
</blockquote></td>
<td><blockquote>
<p>YSDIAGP-DXLS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Enter/Edit Current Inpatient Data</p>
</blockquote></td>
<td><blockquote>
<p>YSCENED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Group Data Entry/Edit</p>
</blockquote></td>
<td><blockquote>
<p>YSCENGED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Active Diagnoses</p>
</blockquote></td>
<td><blockquote>
<p>YSCENDIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Outpatient Medications</p>
</blockquote></td>
<td><blockquote>
<p>YSCENMEDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Profile Data</p>
</blockquote></td>
<td><blockquote>
<p>YSCENPP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Work List</p>
</blockquote></td>
<td><blockquote>
<p>YSCENWL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ward/Team History - LOS, DRG and DXLS</p>
</blockquote></td>
<td><blockquote>
<p>YSCENTMHX</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Mental Health - Progress Notes Clean Up

The following two pre-INIT actions will only be performed if the Mental Health Progress Notes conversion to Generic Progress Notes has been completed.

#### #### Mental Health Progress Notes Option Deletions

The following table contains a list of obsolete Mental Health Progress Notes menu options deleted by the pre-INIT process.

|                                       |                               |
|---------------------------------------|-------------------------------|
| External Menu Option Text         | Internal Menu Option Name |
| Author.........Print                  | YSPN PRINT AUTHOR             |
| Copy Progress Note                    | YSPN COPY                     |
| Correction to a Progress Note         | YSPN CORRECTION               |
| Cosign a Progress Note                | YSPN COSIGNER                 |
| Date...........Print                  | YSPN PRINT DATE               |
| Edit/Add Signature to a Progress Note | YSPN SIGNATURE                |
| Entry of Progress Note                | YSPN ENTRY                    |
| Location.......Print                  | YSPN PRINT LOCATION           |
| Patient Name...Print                  | YSPN PRINT PT                 |
| Print Progress Note (s)               | YSPN PRINT MENU               |
| Progress Note                         | YSPN MENU                     |
| Type of Note...Print                  | YSPN PRINT TYPE               |
| View Progress Note                    | YSPN INQUIRY                  |

#### Progress Notes File Deletions

The pre-INIT process deletes the following obsolete Mental Health Progress Notes files:

1\. PROGRESS NOTES file (#606)

2\. PROGRESS NOTES TYPE file (#606.5)

#### Package Name Update

The Mental Health entry in the PACKAGE file (#9.4 ) was previously called “Mental Health System.” This package entry is renamed to “Mental Health” by the pre-INIT process.

### INIT Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INIT will install all software structures (not created by the pre-INITs and post-INITs) required to run Mental Health V. 5.01. These structures include such components as files, templates, options, security keys, and bulletins. See the Technical Guide for a complete list of software structures installed by the Mental Health V 5.01 INITs.

## ### Post-INIT Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Mental Health - Menu Options “Out of Order” Message

The following table contains menu options to be placed “Out of Order” by the post-INIT process as the first action after completion of the package install.

|                                       |                               |
|---------------------------------------|-------------------------------|
| External Menu Option Text         | Internal Menu Option Name |
| Profile of Patient                    | YSPATPROF                     |
| DSM-III-R Diagnosis (Problem list)    | YSPLDX                        |
| Enter Diagnosis                       | YSDIAGE                       |
| Print Diagnoses                       | YSDIAGP-DX                    |
| Print DXLS History                    | YSDIAGP-DXLS                  |
| Enter/Edit Current Inpatient Data     | YSCENED                       |
| Group Data Entry/Edit                 | YSCENGED                      |
| Active Diagnoses                      | YSCENDIA                      |
| Outpatient Medications                | YSCENMEDS                     |
| Patient Profile Data                  | YSCENPP                       |
| Work List                             | YSCENWL                       |
| Ward/Team History - LOS, DRG and DXLS | YSCENTMHX                     |

#### Patient Movement Tracking

The MAS package DGMP MOVEMENT EVENTS protocol is activated whenever patients are admitted, transferred, or discharged. This protocol activates the Mental Health YS PATIENT MOVEMENTS protocol which updates the MENTAL HEALTH INPT file (#618.4). This protocol is created by the post-INIT process, if the protocol does not already existent.

#### Option Deletions

The following table contains a list of obsolete menu options deleted by the pre-INIT process.

#### |                                           |                               |
|-------------------------------------------|-------------------------------|
| External Menu Option Text             | Internal Menu Option Name |
| Inpatient History                         | YSCENHX                       |
| Patient List                              | YSCENPATL                     |
| Short Problem List                        | YSCENPROB                     |
| Treatment Plan Tracker                    | YSCENTPT                      |
| Update Mental Health Census               | YSCENUP                       |
| Print Diagnoses                           | YSDIAGP                       |
| DELETE.......Delete OLD YS Security Locks | YS SITE-FILE 19               |
| Key Allocation                            | YSKEY                         |

#### Mental Health Progress Note Print Template Deletions

The following table contains a list of obsolete Mental Health Progress Note print templates deleted by the post-INIT process.

|                                           |
|-------------------------------------------|
| Mental Health Progress Note Templates |
| YSPN PT FOOTER                            |
| YSPN PT HEADER                            |
| YSPN PT PRINT                             |

#### Mental Health Site Parameters Field

Current Version Number field (#10) in the MENTAL HEALTH SITE PARAMETERS file (#602) is updated to “5.01”.

#### DSM Conversion Overview

The conversion process is the repointing of patient DSM data from the original DSM3 file (#627) and DSM-III-R file (#627.5) to the new DSM file (#627.7). Before each entry is repointed, the original value of the pointer field is stored in the DSM CONVERSION file (#627.99). The entries in the DSM CONVERSION file (#627.99) serve as the basis for the restart and restore capabilities of the DSM repointing software. (See the “DSM Conversion” section for additional information.)

> **NOTE:** • The following files contain patient DSM data that will be repointed the new DSM file (#627.7).

<u>File pointing to the DSM3 file (#627)</u>:

• MEDICAL RECORD file (#90)

<u>Files pointing to the DSM-III-R file (#627.5)</u>:

• GENERIC PROGRESS NOTES file (#121)

• DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8)

• The DSM CONVERSION file (#627.99) can be deleted by IRMS once a successful conversion of the patient DSM data has been completed. The DSM CONVERSION file (#627.99) will be deleted by the next Mental Health version.

# #### Mental Health - Deletion of the Out of Order Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The last action of the post-INIT is to delete the “Out of Order” message from the following table of menu options.

|                                       |                               |
|---------------------------------------|-------------------------------|
| External Menu Option Text         | Internal Menu Option Name |
| Profile of Patient                    | YSPATPROF                     |
| DSM-III-R Diagnosis (Problem list)    | YSPLDX                        |
| Enter Diagnosis                       | YSDIAGE                       |
| Print Diagnoses                       | YSDIAGP-DX                    |
| Print DXLS History                    | YSDIAGP-DXLS                  |
| Enter/Edit Current Inpatient Data     | YSCENED                       |
| Group Data Entry/Edit                 | YSCENGED                      |
| Active Diagnoses                      | YSCENDIA                      |
| Outpatient Medications                | YSCENMEDS                     |
| Patient Profile Data                  | YSCENPP                       |
| Work List                             | YSCENWL                       |
| Ward/Team History - LOS, DRG and DXLS | YSCENTMHX                     |

#### .c4DSM Conversion Information

#### DSM Files in Mental Health V. 5.0

DSM diagnosis entered on patients, using the various versions of the Mental Health package prior to V. 5.01, have been placed in three different files. These files are the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and the DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8). The DSM diagnostic codes recorded in the MEDICAL RECORD file (#90) point to the obsolete DSM3 file (#627). Diagnostic codes recorded in the GENERIC PROGRESS NOTES (#121) and DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8) point to the obsolete DSM-III-R file (#627.5).

#### New DSM Files in Mental Health V. 5.01

A new DSM file (#627.7) has been created to hold the new DSM-IV diagnostic codes. The DSM file (#627.7) contains the DSM-III and DSM-III-R diagnostic codes originally placed in the DSM3 file (#627) and DSM-III-R file (#627.5).

> **NOTE:** After a successful installation of Mental Health V. 5.01, the DSM3 file (#627) and DSM-III-R file (#627.5) files will no longer be used and become obsolete. These files will be deleted by the next version of Mental Health.

#### DSM Data Conversion

The entries in the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and the DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8), pointing to the obsolete DSM3 file (#627) and DSM-III-R file (#627.5), will be repointed to the new DSM file (#627.7). The repointing of patient DSM data from the obsolete files, to the new DSM file (#627.7), is performed as the last action of the Mental Health V. 5.01 post-INIT.

> **NOTE:** The repointing of patient DSM data is also referred to as the conversion of patient DSM data.

The following table lists the files and fields holding patient DSM data:

> **NOTE:** Asterisks preceding field names in this table are part of the field name, not references to additional information.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 28%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File</strong></td>
<td><strong>Field Information</strong></td>
<td><strong>Field Comments</strong></td>
</tr>
<tr class="even">
<td>MEDICAL RECORD (#90)</td>
<td><p>*DSM-III DIAGNOSIS</p>
<p>(#.01)</p></td>
<td><p><u>Structure</u>:</p>
<p>.01 field of the *DSM-III Diagnosis (#90.04) subfile multiple.</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM3 file (#627).</p></td>
</tr>
<tr class="odd">
<td>MEDICAL RECORD (#90)</td>
<td><p>*PRINCIPAL DSM-III DIAGNOSIS</p>
<p>(#102)</p></td>
<td><p><u>Structure</u>:</p>
<p>Second piece of the DX1 node.</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM3 file (#627).</p></td>
</tr>
<tr class="even">
<td>MEDICAL RECORD (#90)</td>
<td><p>*X DSM-III DIAGNOSIS</p>
<p>(#102.6)</p></td>
<td><p><u>Structure</u>:</p>
<p>Fourth piece of the DX1 node.</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM3 file (#627).</p></td>
</tr>
<tr class="odd">
<td>MEDICAL RECORD (#90)</td>
<td><p>*PAST PRINCIPAL DX</p>
<p>(#.01)</p></td>
<td><p><u>Structure</u>:</p>
<p>.01 field of the *PAST PRINCIPAL DX (#90.06) subfile multiple.</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM3 file (#627).</p></td>
</tr>
<tr class="even">
<td>MEDICAL RECORD (#90)</td>
<td><p>*PAST X DIAGNOSIS</p>
<p>(#.01)</p></td>
<td><p><u>Structure</u>:</p>
<p>.01 field of the *PAST X DIAGNOSIS (#90.07) subfile multiple.</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM3 file (#627).</p></td>
</tr>
<tr class="odd">
<td>GENERIC PROGRESS NOTES (#121)</td>
<td><p>DXLS</p>
<p>(#30)</p></td>
<td><p><u>Structure</u>:</p>
<p>Variable pointer to the ICD9 (#80) and DSM-III-R file (#627.5).</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM-III-R file (#627.5).</p></td>
</tr>
</tbody>
</table>

Chart continues on the next page...

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 28%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File</strong></td>
<td><strong>Field Information</strong></td>
<td><strong>Field Comments</strong></td>
</tr>
<tr class="even">
<td>DIAGNOSTIC RESULTS - MENTAL HEALTH (#627.8)</td>
<td><p>DIAGNOSIS</p>
<p>(#1)</p></td>
<td><p><u>Structure</u>:</p>
<p>Variable pointer to the ICD9 (#80) and DSM-III-R file (#627.5).</p>
<p><u>Target</u>:</p>
<p>Pointer to the DSM-III-R file (#627.5).</p></td>
</tr>
</tbody>
</table>

#### Conversion Process

The following section describes the events which occur during the conversion process of the patient DSM data. In describing these events, the phrases “Original Value” and “New Conversion Value” are used frequently.

\* <u>Original Value</u>:

The MEDICAL RECORD file (#90) contains five DSM related fields. These fields point to the DSM3 file (#627). The original values of entries in these five MEDICAL RECORD file (#90) fields are the internal entry numbers from the DSM3 file (#627). The GENERIC PROGRESS NOTES file (#121) and DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8) have one variable pointer field in each file. The variable pointer fields in both files are identical, pointing to the ICD9 file (#80) and DSM-III-R file (#627.5). (Entries pointing to the ICD9 file (#80) are not converted.) The original values of entries in these two fields are the variable pointer references to the DSM-III-R file (#627.5).

\*\* <u>New Conversion Value</u>:

The entries in the DSM3 file (#627) and DSM-III-R file (#627.5) have been copied into the new DSM file (#627.7). When these entries were copied into the DSM file (#627.7), the internal entry number of the new entry was recorded in the new DSM IEN field in the parent (DSM3 or DSM-III-R) file. The DSM IEN field is used when determining the correct, new internal entry number or variable pointer reference to be recorded in the patient data fields being converted. The new conversion value is either the internal entry number stored in the DSM IEN field and pointing to the DSM file (#627.7) for pointer fields, or the variable pointer reference using the internal entry number stored in the DSM IEN field and pointing to the DSM (#627.7) file for variable pointer fields.

1\. All unconverted entries are evaluated in the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8). All entries in these three files pointing to the DSM3 file (#627) and DSM-III-R file (#627.5) will have events (A through F) performed:

NOTES:

• As the conversion process proceeds through the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8), the “tracking nodes” are set in the DSM CONVERSION file (#627.99). These “tracking nodes” are used to record such values as the number of records converted, last record converted, and a file-by-file status of the conversion process as it is completed. (All “tracking nodes” created by the conversion process are descendant from the ^YSD(627.99,"AS") node.

• In addition to the ^YSD(627.99,"AS") node, “tracking nodes” are used to record the date and time of the conversion process as it is completed in the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and the DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8). Three fields in the MENTAL HEALTH SITE PARAMETERS file (#602) are also used to permanently record the date and time of the conversion process when completed. These three fields are:

• DSM-Medical Record Conversion Completion field (#11)

• DSM-Generic Progress Notes Conversion Completion field (#12)

• DSM-Diagnostic Results - Mental Health Conversion Completion field (#13)

> **CAUTION:** Diagnosis related fields must be converted only once! The DSM CONVERSION file (#627.99) protects against multiple conversions of these diagnosis related fields. It is mandatory that the DSM CONVERSION file (#627.99) be left intact, and unmodified in any way, until the conversion of the patient DSM data has been successfully completed!

> a\. An entry is made in the DSM CONVERSION file (#627.99).

> The DSM CONVERSION file (#627.99) entry, at this point, holds only the internal entry number from the parent file.

> b\. The STATUS field of the DSM CONVERSION file (#627.99) entry is set to “S”.

> The “S” status indicates that the recording of the original value\* of the DSM-III or DSM-III-R diagnosis in the DSM CONVERSION file (#627.99) is \<S\>tarting.

> c\. The original value\* of the DSM-III or DSM-III-R diagnosis is recorded in the DSM CONVERSION file (#627.99) entry created by Step A.

> If more than one diagnosis related field exists in a MEDICAL RECORD file (#90) entry, the original values\* of all fields are recorded under one DSM CONVERSION file (#627.99) entry.

> d\. The STATUS field of the DSM CONVERSION file (#627.99) entry is set to “R”.

> The “R” status indicates that the original value\* of the DSM-III or DSM-III-R diagnosis has been \<R\>ecorded in the DSM CONVERSION file (#627.99).

> e\. The original value\* of the DSM-III or DSM-III-R diagnosis is reset to the new conversion value.\*\*

> f\. The STATUS field of the DSM CONVERSION file (#627.99) entry is set to “C”.

> The “C” status indicates that the original value\* of the DSM-III or DSM-III-R diagnosis has been recorded in the DSM CONVERSION file (#627.99), and that the DSM related field in the parent file has been successfully \<C\>onverted to its new conversion value.\*\*NOTE: If the conversion of a file entry or entries is not possible for any reason, the status of the entry is set to “E”, for \<E\>rror, and the entry is displayed in the error report.

2\. After all DSM related fields in the MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8) have been converted, the following events occur:

> a\. The date and time of conversion completion is recorded in a tracking node in the DSM CONVERSION file (#627.99).

> b\. Conversion statistics and errors are compiled and displayed to the user.

> **NOTE:** • Conversion statistics and the error report can be reprinted at any time. See the “Reprinting Conversion Statistics and the Error Report” section of this Installation Guide.

• See the section entitled “DSM Conversion Information” for additional details.

#### Restart of DSM Conversion

If the conversion of DSM data aborts abnormally, the conversion process can be restarted by calling CONVERT^YSD4DSM. When the DSM conversion is restarted, previously converted records will be skipped. The conversion will resume at the point where previous conversion activity ceased. The terminal dialogue seen during the restarting of conversion is shown below.

> **NOTE:** The conversion of DSM data can be restarted an unlimited number of times.

\>D CONVERT^YSD4DSM

Placing Options Out of Order

OK to restart conversion now? Y (YES)

Repointing Medical Record file data from the DSM3 file to the DSM file...

..............................................................................

..............................................................................

.

Repointing Generic Progress Notes data from the DSM-III-R to the DSM file...

Repointing Diagnostic Results data from the DSM-III-R file to the DSM file...

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

...................

Installation of DSM-IV Diagnostic Codes and patient data conversion completed!!

DSM Conversion Error Totals Dallas

==============================================================================

Error Summary: Medical Record (#90) file errors: 1991

Generic Progress Notes (#121) file errors: 0

Diagnostic Results (#627.8) file errors: 0

-----------------------------------------------------

Total number of errors: 1991

Print Errors? Y// N (NO)

Returning Options to Service

#### DSM Data Restoration

Repointed patient DSM data can be restored to the preconversion state at any time during the conversion, after an abnormal abortion of the conversion process, or after the conversion process is completed. To start the restoration of the patient DSM data to the original values\*, call ALL^YSD40060. The terminal dialogue seen during the restoration of DSM data is shown below.

> **NOTE:** The process of returning patient DSM data to the original state, undoing the conversion, is also referred to as data or baseline “restoration.”

\>D ALL^YSD40060

The use of this option will restore the entries in the Medical Record,

Diagnostic Results, and Generic Progress Notes files to their original

condition. When this occurs, the Conversion file entry used during the

restoration process will be deleted...

> **NOTE:** Only those entries which have completed the initial conversion will be

restored. (These entries have a status of \<C\>onverted.)

OK to start restoration process? No// Y (YES)

Starting restoration....................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

........................................................................

Restoration complete...

\# Progress Notes Restored: 20016

\# Diagnostic Results Restored: 18806

\# Medical Records Restored: 12147

#### Printing Conversion Statistics and the Error Report

After the conversion of DSM data has completed, conversion statistics and errors are displayed on screen. Both the conversion statistics and error information can be redisplayed and/or printed at any time (prior to the deletion of the data in the DSM CONVERSION file (#627.99). This can be done using the following calls:

CallResulting Action

REPORT^YSD4DSM Redisplays conversion statistics

ERRORS^YSD4DSM Prints error data

The terminal dialogue seen during the use of these two call points is shown below.

#### Printing Conversion Statistics REPORT^YSD4DSM

\>D REPORT^YSD4DSM

DSM Conversion Summary Report Dallas

Dec 20, 1994@16:24:37

==============================================================================

Medical Record \# of records: 67671

Medical Record \# of records converted: 12147

Generic Progress Notes \# of records: 20018

Generic Progress Notes \# of records converted: 20016

Diagnostic Results \# of records: 23864

Diagnostic Results \# of records converted: 18806

------------------------------------------------------------------------------

Total number of records: 111553

Total number of records converted: 50969

Print Errors? Y// N (NO)

Returning Options to Service

#### Printing Error Information ERRORS ^YSD4DSM

\>D ERRORS^YSD4DSM

DSM Conversion Error Totals Dallas

==============================================================================

Error Summary: Medical Record (#90) file errors: 2145

Generic Progress Notes (#121) file errors: 0

Diagnostic Results (#627.8) file errors: 0

-----------------------------------------------------

Total number of errors: 2145

Print Errors? Y// \<RET\> (YES)

DEVICE: HOME// \<RET\> RIGHT MARGIN: 80// \<RET\>

DSM Conversion Error Report Dallas

Dec 20, 1994@16:26:09 Page: 1

==============================================================================

File# Entry# Node Mult# Error Text Code#

==============================================================================

90 1003 XDX 1 Invalid data structure 295.7

90 1017 XDX 1 Invalid data structure 296.3

90 1019 XDX 1 Invalid data structure 298.9

90 1025 XDX 1 Invalid data structure 295.92

90 1031 XDX 1 Invalid data structure 303.91

90 1033 XDX 1 Invalid data structure 301.83

90 1034 XDX 1 Invalid data structure 295.34

90 1035 XDX 1 Invalid data structure 296.82

90 1039 XDX 1 Invalid data structure 295.34

90 1048 XDX 1 Invalid data structure 295.95

90 1051 XDX 1 Invalid data structure 295.34

90 1053 XDX 1 Invalid data structure 303.91

90 1078 XDX 1 Invalid data structure 304.01

90 1079 XDX 1 Invalid data structure 309.81

90 1110 XDX 1 Invalid data structure 309.81

Hit RETURN to continue, or '^' to continue... ^

DSM Conversion Error Totals Dallas

Dec 20, 1994@16:26:09 Page: 2

==============================================================================

Error Summary: Medical Record (#90) file errors: 2145

Generic Progress Notes (#121) file errors: 0

Diagnostic Results (#627.8) file errors: 0

-----------------------------------------------------

Total number of errors: 2145

> **NOTE:** If the conversion of the patient DSM data abnormally aborts, the conversion statistics and error data generated up to the time of conversion abortion can be displayed on screen by calling REPORT^YSD4DSM.

## Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.01 may be installed on a clean account (with no version of Mental Health present). It may also be installed on an account with Mental Health V. 4.18 or V. 5.0. The following installation instructions apply to all three account environments.

> **NOTE:** Please refer to the section entitled “Version Installation Orders and Dependencies” for additional information regarding version number and environment requirements.

1\. If not already done, convert all Mental Health Progress Notes to the new Progress Notes format as outlined in the Progress Notes V. 2.5 package Installation Guide. (This is required in order to install Mental Health V. 5.01.)

NOTES:

• The conversion of Mental Health Progress Notes to the Generic Progress Notes format can be done any time prior to the actual installation of Mental Health

V. 5.01.

• If you have already installed Mental Health V. 5.0, the conversion of Progress Notes data has already been done. (Mental Health V. 5.0 and V. 5.01 cannot be installed until Progress Notes V. 2.5 is installed, and all Mental Health Progress Notes data is converted to the new format.)

• Step 1 does not have to be performed at the same time as steps 2 through 19. This step in the installation process can be done weeks or months prior to the remainder of the installation process!

2\. Archive the PROGRESS NOTES (#606) and PROGRESS NOTES TYPE (#606.5) files, if they exist on your system.

> **NOTE:** These files are made obsolete by the Progress Notes conversion, and if they exist, will be deleted by the Mental Health V. 5.01 pre-INIT.

3\. Patient DSM data in the MEDICAL RECORD (#90), GENERIC PROGRESS NOTES (#121), and DIAGNOSTIC RESULTS - MENTAL HEALTH (#627.8) files, will be repointed by the post-INIT process. The global data in these files should be backed up. Copy all globals shown in the following files and global list to disk and/or tape.

|             |                                    |                 |
|-------------|------------------------------------|-----------------|
| File \# | File Name                      | Global Name |
| 90          | MEDICAL RECORD                     | ^MR             |
| 121         | GENERIC PROGRESS NOTES             | ^GMR(121,       |
| 627.8       | DIAGNOSTIC RESULTS - MENTAL HEALTH | ^YSD(627.8,     |

> **NOTE:** Even though all converted data can be returned to its original state using the restoration features built into the conversion software, it is highly recommended that the listed globals be copied to disk or tape before proceeding with installation of Mental Health V. 5.01.

4\. Inform all Mental Health users of the unavailability of the package.

5\. Disable mapped routines. (This applies to VAX and Alpha systems only.)

6\. Disable journaling. (This applies to VAX and Alpha systems only.)

7\. Delete all the YI\*, YS\*, and YT\* routines.

> **CAUTION:** Do not delete any locally created YIZ\*, YSZ\*, or YTZ\* routines!

8\. The MH5_01.GBL file contains the testing and interview global data ^YTT(601). Kill ^YTT(601) prior to installing the contents of MH5_01.GBL. Then install MH5_01.GBL.

> **NOTE:** On VAX or Alpha systems, use the %GTI utility to load the global data contained in the MH5_01.GBL file. To load global data, 486 sites should use the %GR utility.

9\. Load the routines contained in the MH5_01.RTN file.

> **NOTE:** 486 Sites only!

The routines should be loaded and the INITs should be run on the print server where TaskMan resides.

10\. Access your system and proceed to the programmer access level. Use a terminal that can provide a hard copy of the process.

11\. Install Mental Health V. 5.01 by calling D ^YSINIT. Please see Examples of installation in the next sections.

Refer to Examples on First Time Installation for Mental Health V. 5.01

12\. Delete the YSI\* INIT routines when installation of Mental Health V. 5.01 is complete. (This is optional.)

13\. On 486 sites, the YI\*, YS\*, and YT\* routines should be moved to the compute and print servers. (This step should be skipped by VAX and Alpha systems.)

> **NOTE:** 486 Sites only!

YSXR namespaced routines are created by the compilation of cross references during the installation of Mental Health V. 5.01, and YSCP namespaced routines are created by compilation of print templates during the installation of Mental Health V. 5.01. These routines should also be moved to the compute and print servers.

14\. Enable mapped routines (if applicable).

15\. Enable journaling (if applicable).

16\. If not already done prior to the installation of Mental Health V. 5.01, create the YS PSYCHTEST mail group, populate the group with members, and link the mail group with the YS PSYCHTEST bulletin. If the mail group has already been created and populated and linked, review the members in the YS PSYCHTEST mail group.

> **NOTE:** See the section entitled “YS PSYCHTEST Bulletin and Mail Group” for complete instructions.

17\. Inform all Mental Health users of the availability of the package.

### First Time Installation for Mental Health V. 5.01

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows the terminal dialogue seen during installation of Mental Health V. 5.01 on a clean account (with no installed version of Mental Health.)

Example: INIT Completed at the Dallas ISC

\>D ^YSINIT

This version (#5.01) of 'YSINIT' was created on 20-DEC-1994

(at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

90 MEDICAL RECORD

99 PT. TEXT

> **NOTE:** You already have the 'PT. TEXT' File.

600.7 CRISIS NOTE DISPLAY

601 MH INSTRUMENT

601.2 PSYCH INSTRUMENT PATIENT

601.3 COPYRIGHT HOLDER (including data)

I will OVERWRITE your data with mine.

601.4 INCOMPLETE PSYCH TEST PATIENT

602 MENTAL HEALTH SITE PARAMETERS

605 MH TEXT (including data)

I will OVERWRITE your data with mine.

615 MH CLINICAL FILE

615.2 SECLUSION/RESTRAINT

615.5 S/R REASONS (including data)

I will MERGE your data with mine.

615.6 S/R CATEGORY (including data)

I will MERGE your data with mine.

615.7 S/R RELEASE CRITERIA (including data)

I will MERGE your data with mine.

615.8 S/R ALTERNATIVES (including data)

I will MERGE your data with mine.

615.9 S/R OBSERVATION CHECKLIST (including data)

I will MERGE your data with mine.

617 MH WAIT LIST

618 MENTAL HEALTH CENSUS

618.2 MENTAL HEALTH TEAM

618.4 MENTAL HEALTH INPT

620 PROBLEM (including data)

I will OVERWRITE your data with mine.

624 JOB BANK

625 INDICATOR (including data)

I will OVERWRITE your data with mine.

627 DSM3 (including data)

I will OVERWRITE your data with mine.

627.5 DSM-III-R (including data)

I will OVERWRITE your data with mine.

627.7 DSM (including data)

I will OVERWRITE your data with mine.

627.8 DIAGNOSTIC RESULTS - MENTAL HEALTH

627.9 DSM MODIFIERS (including data)

I will OVERWRITE your data with mine.

627.99 DSM CONVERSION

628 YSEXPERT

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Starting the Mental Health 5.01 pre-init now...

If your package file contains an entry named 'Mental Health System'

it will be renamed 'Mental Health' ...

Placing Options Out of Order

> **NOTE:** You are not required to have the ICD Diagnosis file \#80 installed

but the Final Discharge Note within Progress Notes points to this file.

If you wish to use this type of note, please install this file.

...SORRY, LET ME THINK ABOUT THAT A MOMENT....................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

................................

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

YSXRAA1 routine filed

YSXRAA2 routine filed

YSXRAA3 routine filed

YSXRAA4 routine filed

YSXRAA routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAB1 routine filed

YSXRAB2 routine filed

YSXRAB3 routine filed

YSXRAB4 routine filed

YSXRAB routine filed

Compiling Cross-Reference routine.............

...HMMM, THIS MAY TAKE A FEW MOMENTS...

YSXRAC1 routine filed

YSXRAC2 routine filed

YSXRAC3 routine filed

YSXRAC4 routine filed

YSXRAC5 routine filed

YSXRAC6 routine filed

YSXRAC7 routine filed

YSXRAC8 routine filed

YSXRAC routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

YSXRAD1 routine filed

YSXRAD2 routine filed

YSXRAD routine filed.

Compiling Cross-Reference routine.............

...SORRY, HOLD ON...

YSXRAE1 routine filed

YSXRAE2 routine filed

YSXRAE3 routine filed

YSXRAE4 routine filed

YSXRAE routine filed

Compiling Cross-Reference routine.............

...SORRY, HOLD ON...

YSXRAF1 routine filed

YSXRAF2 routine filed

YSXRAF3 routine filed

YSXRAF4 routine filed

YSXRAF5 routine filed

YSXRAF6 routine filed

YSXRAF routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAG1 routine filed

YSXRAG2 routine filed

YSXRAG routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAJ1 routine filed

YSXRAJ2 routine filed

YSXRAJ3 routine filed

YSXRAJ4 routine filed

YSXRAJ routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAK1 routine filed

YSXRAK2 routine filed

YSXRAK3 routine filed

YSXRAK4 routine filed

YSXRAK5 routine filed

YSXRAK6 routine filed

YSXRAK7 routine filed

YSXRAK8 routine filed

YSXRAK9 routine filed

YSXRAK10 routine filed

YSXRAK11 routine filed

YSXRAK12 routine filed

YSXRAK routine filed

Compiling Cross-Reference routine.............

...SORRY, HOLD ON...

YSXRAL1 routine filed

YSXRAL2 routine filed

YSXRAL routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAM1 routine filed

YSXRAM2 routine filed

YSXRAM routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAN1 routine filed

YSXRAN2 routine filed

YSXRAN routine filed.

Compiling Cross-Reference routine.............

...SORRY, HOLD ON...

YSXRAO1 routine filed

YSXRAO2 routine filed

YSXRAO routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, HOLD ON...

YSXRAP1 routine filed

YSXRAP2 routine filed

YSXRAP routine filed.

Compiling Cross-Reference routine.............

...SORRY, JUST A MOMENT PLEASE...

YSXRAQ1 routine filed

YSXRAQ2 routine filed

YSXRAQ3 routine filed

YSXRAQ4 routine filed

YSXRAQ routine filed

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAR1 routine filed

YSXRAR2 routine filed

YSXRAR routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAS1 routine filed

YSXRAS2 routine filed

YSXRAS routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAT1 routine filed

YSXRAT2 routine filed

YSXRAT3 routine filed

YSXRAT4 routine filed

YSXRAT5 routine filed

YSXRAT6 routine filed

YSXRAT routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, HOLD ON...

YSXRAU1 routine filed

YSXRAU2 routine filed

YSXRAU routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAV1 routine filed

YSXRAV2 routine filed

YSXRAV routine filed.

Compiling Cross-Reference routine.............

...HMMM, THIS MAY TAKE A FEW MOMENTS...

YSXRAW1 routine filed

YSXRAW2 routine filed

YSXRAW routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

YSXRAX1 routine filed

YSXRAX2 routine filed

YSXRAX3 routine filed

YSXRAX4 routine filed

YSXRAX routine filed............

Compiling Cross-Reference routine.............

...HMMM, THIS MAY TAKE A FEW MOMENTS...

YSXRAY1 routine filed

YSXRAY2 routine filed

YSXRAY3 routine filed

YSXRAY4 routine filed

YSXRAY routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAZ1 routine filed

YSXRAZ2 routine filed

YSXRAZ3 routine filed

YSXRAZ4 routine filed

YSXRAZ5 routine filed

YSXRAZ6 routine filed

YSXRAZ routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...

YSXRBA1 routine filed

YSXRBA2 routine filed

YSXRBA3 routine filed

YSXRBA4 routine filed

YSXRBA5 routine filed

YSXRBA6 routine filed

YSXRBA routine filed........

'YS-AXIS 4' Help Frame filed.

'YS-GAF SCALE' Help Frame filed.

'YS-GEN MODIFIER' Help Frame filed.

'YS-LIST-OF-TESTS' Help Frame filed.

'YS-PHY-EXAM-NORM' Help Frame filed.

'YS-PSYCHOSOCIAL STRESSORS' Help Frame filed.

'YSCENP' Help Frame filed.

'YSDIAG' Help Frame filed..

'YS PSYCHTEST' BULLETIN FILED -- Remember to add mail groups for new bulletins..

..............................................................................

.........................................

'YS SITE PARAMETERS' Option Filed

'YS SITE-FILE 16' Option Filed

'YS SITE-FILE 602 TEST LIM' Option Filed

'YS SITE-FILE 602 WWU' Option Filed

'YS SITE-FILE 615.5' Option Filed

'YS SITE-FILE 615.6' Option Filed

'YS SITE-FILE 615.7' Option Filed

'YS SITE-FILE 615.8' Option Filed

'YS SITE-FILE 615.9' Option Filed

'YSADMTEST' Option Filed

'YSAPROB' Option Filed

'YSCENCAD' Option Filed

'YSCENCL' Option Filed

'YSCENCRISIS' Option Filed

'YSCENDAYHX' Option Filed

'YSCENDCDOC' Option Filed

'YSCENDIA' Option Filed

'YSCENED' Option Filed

'YSCENEDM' Option Filed

'YSCENFS' Option Filed

'YSCENGED' Option Filed

'YSCENIL' Option Filed

'YSCENLOS' Option Filed

'YSCENMAIN' Option Filed

'YSCENMEDS' Option Filed

'YSCENMGR' Option Filed

'YSCENNAM' Option Filed

'YSCENNEW' Option Filed

'YSCENPAHX' Option Filed

'YSCENPASS' Option Filed

'YSCENPL' Option Filed

'YSCENPP' Option Filed

'YSCENREM' Option Filed

'YSCENROT' Option Filed

'YSCENSL' Option Filed

'YSCENSUBUP' Option Filed

'YSCENTAH' Option Filed

'YSCENTCEN' Option Filed

'YSCENTESTING' Option Filed

'YSCENTMHX' Option Filed

'YSCENTPTE' Option Filed

'YSCENTPTP' Option Filed

'YSCENUNITUP' Option Filed

'YSCENUNT' Option Filed

'YSCENWDM' Option Filed

'YSCENWL' Option Filed

'YSCLERK' Option Filed

'YSCLINRECORD' Option Filed

'YSCOMMENT' Option Filed

'YSCRISNOT' Option Filed

'YSDECTREES-R' Option Filed

'YSDIAG' Option Filed

'YSDIAGE' Option Filed

'YSDIAGP-DX' Option Filed

'YSDIAGP-DXLS' Option Filed

'YSDIRTEST' Option Filed

'YSEPROB' Option Filed

'YSEXTESTS' Option Filed

'YSFPROB' Option Filed

'YSHX1' Option Filed

'YSHXPAST' Option Filed

'YSHXPASTR' Option Filed

'YSINST RESTART LIMIT' Option Filed

'YSIPROB' Option Filed

'YSJOBINQ' Option Filed

'YSJOBKILL' Option Filed

'YSJOBLIST' Option Filed

'YSJOBUPDATE' Option Filed

'YSKILLINC' Option Filed

'YSMANAGEMENT' Option Filed

'YSMANAGER' Option Filed

'YSMCHK' Option Filed

'YSMKIL' Option Filed

'YSMLST' Option Filed

'YSMOVP' Option Filed

'YSMUSE' Option Filed

'YSPATMSG' Option Filed

'YSPATPROF' Option Filed

'YSPERSHX' Option Filed

'YSPERSHXR' Option Filed

'YSPHYEXAM' Option Filed

'YSPIT' Option Filed

'YSPLDX' Option Filed

'YSPLPDX' Option Filed

'YSPPROB' Option Filed

'YSPRINT' Option Filed

'YSPROBLIST' Option Filed

'YSPTINSTRU' Option Filed

'YSRAPROB' Option Filed

'YSREVSYS' Option Filed

'YSREVSYSR' Option Filed

'YSRFPROB' Option Filed

'YSRSPROB' Option Filed

'YSSR 10-2683' Option Filed

'YSSR 15-CHECK' Option Filed

'YSSR DELETE' Option Filed

'YSSR EDIT' Option Filed

'YSSR ENTRY' Option Filed

'YSSR MGT UTILITY' Option Filed

'YSSR MGTRD' Option Filed

'YSSR MGTRI' Option Filed

'YSSR MGTRN' Option Filed

'YSSR MGTRW' Option Filed

'YSSR RELEASE' Option Filed

'YSSR REPORTS' Option Filed

'YSSR REVIEW' Option Filed

'YSSR REVIEW RPT' Option Filed

'YSSR SEC/RES' Option Filed

'YSSR W-ORDER' Option Filed

'YSTESTBAT' Option Filed

'YSTSTAUD' Option Filed

'YSUSER' Option Filed

'YSUTIL' Option Filed

'YSVOCATIONAL' Option Filed

'YSWAITCR' Option Filed

'YSWAITE' Option Filed

'YSWAITEDI' Option Filed

'YSWAITLST' Option Filed

'YSWAITP' Option Filed

'YSWAITREM' Option Filed

'YSWAITSHUF' Option Filed...........................

Compiling YSJOB print template of File 624..................

'YSCPAA' ROUTINE FILED..

Compiling YSSR 10-2683 FOOTER print template of File 615.2....

'YSCPAE' ROUTINE FILED.

Compiling YSSR 10-2683 HEADER print template of File 615.2.............

'YSCPAF' ROUTINE FILED...........

Compiling YSSR 10-2683 PRINT print template of File 615.2.....................

'YSCPAG' ROUTINE FILED..........

Compiling YSSR DATE MGT HEADER print template of File 615.2..........

'YSCPAH' ROUTINE FILED.......

Compiling YSSR DATE MGT PRINT print template of File 615.2....................

.

'YSCPAI' ROUTINE FILED.........

Compiling YSSR NURSE MGT HEADER print template of File 615.2.........

'YSCPAJ' ROUTINE FILED.......

Compiling YSSR NURSE MGT PRINT print template of File 615.2.............

'YSCPAK' ROUTINE FILED...........

Compiling YSSR PT INQ HEADER print template of File 615.2...............

.

'YSCPAL' ROUTINE FILED.............

Compiling YSSR PT INQ PRINT print template of File 615.2................

'YSCPAM' ROUTINE FILED...

Compiling YSSR REVIEW ACTION HEADER print template of File 615.2........

.....

'YSCPAN' ROUTINE FILED........

Compiling YSSR REVIEW ACTION PRINT print template of File 615.2.........

.

'YSCPAO' ROUTINE FILED........

Compiling YSSR WARD MGT HEADER print template of File 615.2.........

'YSCPAP' ROUTINE FILED.......

Compiling YSSR WARD MGT PRINT print template of File 615.2............

'YSCPAQ' ROUTINE FILED...........

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Starting Post-init process...

Placing Options Out of Order

Adding the YS PATIENT MOVEMENT to the DGPM MOVEMENT EVENTS protocol...

This version of 'YSONIT' was created on 18-JUN-1993

(at DALLAS ISC - FS ACCOUNT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please.....

'YS PATIENT MOVEMENT' Protocol Filed

OK, Protocol Installation is Complete.

Deleting obsolete options...

Deleting obsolete YSPN\* print templates ....

Setting MH Parameters data...

All post-init tasks have now been completed, except the conversion of DSM3

and DSM-III-R data to the new DSM file. This will be done now...

Performing DSM environment checks...

The DSM conversion is about to begin. During this conversion...

\* All entries in the Medical Record file, pointing to the DSM3 file, will

be repointed to the DSM file.

\* All entries in the Generic Progress Notes file, pointing to the DSM-III-R

file, will be repointed to the DSM file.

\* All entries in the Diagnostic Results - Mental Health file, pointing to

the DSM-III-R file, will be repointed to the DSM file.

Please read the Mental Health V. 5.01 Installation guide for full

documentation of the process!!

Repointing Medical Record file data from the DSM3 file to the DSM file...

Repointing Generic Progress Notes data from the DSM-III-R to the DSM file...

Repointing Diagnostic Results data from the DSM-III-R file to the DSM file...

Installation of DSM-IV Diagnostic Codes and patient data conversion completed!!

No DSM conversion errors to report....

Returning Options to Service

\>

### Installation over Mental Health V. 4.18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows the terminal dialogue seen during installation of Mental Health V. 5.01 on a Mental Health V. 4.18 account.

Example: INIT Completed at the Dallas ISC

\>D ^YSINIT

This version (#5.01) of 'YSINIT' was created on 20-DEC-1994

(at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

90 MEDICAL RECORD

> **NOTE:** You already have the 'MEDICAL RECORD' File.

99 PT. TEXT

> **NOTE:** You already have the 'PT. TEXT' File.

600.7 CRISIS NOTE DISPLAY

> **NOTE:** You already have the 'CRISIS NOTE DISPLAY' File.

601 MH INSTRUMENT

> **NOTE:** You already have the 'MH INSTRUMENT' File.

601.2 PSYCH INSTRUMENT PATIENT

> **NOTE:** You already have the 'PSYCH INSTRUMENT PATIENT' File.

601.3 COPYRIGHT HOLDER (including data)

> **NOTE:** You already have the 'COPYRIGHT HOLDER' File.

I will OVERWRITE your data with mine.

601.4 INCOMPLETE PSYCH TEST PATIENT

> **NOTE:** You already have the 'INCOMPLETE PSYCH TEST PATIENT' File.

602 MENTAL HEALTH SITE PARAMETERS

> **NOTE:** You already have the 'MENTAL HEALTH SITE PARAMETERS' File.

605 MH TEXT (including data)

> **NOTE:** You already have the 'MH TEXT' File.

I will OVERWRITE your data with mine.

615 MH CLINICAL FILE

> **NOTE:** You already have the 'MH CLINICAL FILE' File.

615.2 SECLUSION/RESTRAINT

> **NOTE:** You already have the 'SECLUSION/RESTRAINT' File.

615.5 S/R REASONS (including data)

> **NOTE:** You already have the 'S/R REASONS' File.

I will MERGE your data with mine.

615.6 S/R CATEGORY (including data)

> **NOTE:** You already have the 'S/R CATEGORY' File.

I will MERGE your data with mine.

615.7 S/R RELEASE CRITERIA (including data)

> **NOTE:** You already have the 'S/R RELEASE CRITERIA' File.

I will MERGE your data with mine.

615.8 S/R ALTERNATIVES (including data)

> **NOTE:** You already have the 'S/R ALTERNATIVES' File.

I will MERGE your data with mine.

615.9 S/R OBSERVATION CHECKLIST (including data)

> **NOTE:** You already have the 'S/R OBSERVATION CHECKLIST' File.

I will MERGE your data with mine.

617 MH WAIT LIST

> **NOTE:** You already have the 'MH WAIT LIST' File.

618 MENTAL HEALTH CENSUS

> **NOTE:** You already have the 'MENTAL HEALTH CENSUS' File.

618.2 MENTAL HEALTH TEAM

> **NOTE:** You already have the 'MENTAL HEALTH TEAM' File.

618.4 MENTAL HEALTH INPT

> **NOTE:** You already have the 'MENTAL HEALTH INPT' File.

620 PROBLEM (including data)

> **NOTE:** You already have the 'PROBLEM' File.

I will OVERWRITE your data with mine.

624 JOB BANK

> **NOTE:** You already have the 'JOB BANK' File.

625 INDICATOR (including data)

> **NOTE:** You already have the 'INDICATOR' File.

I will OVERWRITE your data with mine.

627 DSM3 (including data)

> **NOTE:** You already have the 'DSM3' File.

I will OVERWRITE your data with mine.

627.5 DSM-III-R (including data)

> **NOTE:** You already have the 'DSM-III-R' File.

I will OVERWRITE your data with mine.

627.7 DSM (including data)

I will OVERWRITE your data with mine.

627.8 DIAGNOSTIC RESULTS - MENTAL HEALTH

> **NOTE:** You already have the 'DIAGNOSTIC RESULTS - MENTAL HEALTH' File.

627.9 DSM MODIFIERS (including data)

\*BUT YOU ALREADY HAVE 'DSM-III-R MODIFIERS' AS FILE \#627.9!

Shall I change the NAME of the file to DSM MODIFIERS? NO// Y (YES)

627.9 DSM MODIFIERS (including data)

> **NOTE:** You already have the 'DSM MODIFIERS' File.

I will OVERWRITE your data with mine. Mark- this is fine

627.99 DSM CONVERSION

628 YSEXPERT

> **NOTE:** You already have the 'YSEXPERT' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES//\<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES//\<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES//\<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES//\<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Starting the Mental Health 5.01 pre-init now...

\*\*\* MENTAL HEALTH - PROGRESS NOTE CLEAN-UP \*\*\*

As part of the Pre-Init process the old Mental Health

Progress Note functionality will be removed. The following

will be purged at this time:

1\. Data and Data Dictionaries for File \#606

2\. Data and Data Dictionaries for File \#606.5

3\. All YSPN\* options in the OPTION file \#19

Please reference the Progress Notes Package 'Installation

Guide' for instructions as to how to remove the Mental Health

Progress Note routines. Make sure you have followed the

Clean-Up instructions and have a backup of your Mental

Health package before continuing this INIT process!!

Are you ready to continue the Pre-Init ?

If your package file contains an entry named 'Mental Health System'

it will be renamed 'Mental Health' ...

Placing Options Out of Order

Renaming the 'Mental Health System' package file entry... done...

Deleting the Progress Note file, \#606 ....

Deleting the Progress Note Type file, \#606.5 ....

Deleting YSPN\* options ....

\*\*\* Pre-Init Clean-Up is complete, remember to delete YSPN\* routines \*\*\*

...HMMM, I'M WORKING AS FAST AS I CAN.......................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

...........................

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAA1 routine filed

YSXRAA2 routine filed

YSXRAA3 routine filed

YSXRAA4 routine filed

YSXRAA routine filed

Compiling Cross-Reference routine.............

...HMMM, I'M WORKING AS FAST AS I CAN...

YSXRAB1 routine filed

YSXRAB2 routine filed

YSXRAB3 routine filed

YSXRAB4 routine filed

YSXRAB routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAC1 routine filed

YSXRAC2 routine filed

YSXRAC3 routine filed

YSXRAC4 routine filed

YSXRAC5 routine filed

YSXRAC6 routine filed

YSXRAC7 routine filed

YSXRAC8 routine filed

YSXRAC routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAD1 routine filed

YSXRAD2 routine filed

YSXRAD routine filed.

Compiling Cross-Reference routine.............

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAE1 routine filed

YSXRAE2 routine filed

YSXRAE3 routine filed

YSXRAE4 routine filed

YSXRAE routine filed

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAF1 routine filed

YSXRAF2 routine filed

YSXRAF3 routine filed

YSXRAF4 routine filed

YSXRAF5 routine filed

YSXRAF6 routine filed

YSXRAF routine filed

Compiling Cross-Reference routine.............

...SORRY, THIS MAY TAKE A FEW MOMENTS...

YSXRAG1 routine filed

YSXRAG2 routine filed

YSXRAG routine filed.

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

YSXRAJ1 routine filed

YSXRAJ2 routine filed

YSXRAJ3 routine filed

YSXRAJ4 routine filed

YSXRAJ routine filed

Compiling Cross-Reference routine.............

...HMMM, THIS MAY TAKE A FEW MOMENTS...

YSXRAK1 routine filed

YSXRAK2 routine filed

YSXRAK3 routine filed

YSXRAK4 routine filed

YSXRAK5 routine filed

YSXRAK6 routine filed

YSXRAK7 routine filed

YSXRAK8 routine filed

YSXRAK9 routine filed

YSXRAK10 routine filed

YSXRAK11 routine filed

YSXRAK12 routine filed

YSXRAK routine filed

Compiling Cross-Reference routine.............

...SORRY, JUST A MOMENT PLEASE...

YSXRAL1 routine filed

YSXRAL2 routine filed

YSXRAL routine filed.

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAM1 routine filed

YSXRAM2 routine filed

YSXRAM routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAN1 routine filed

YSXRAN2 routine filed

YSXRAN routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAO1 routine filed

YSXRAO2 routine filed

YSXRAO routine filed.

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAP1 routine filed

YSXRAP2 routine filed

YSXRAP routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...

YSXRAQ1 routine filed

YSXRAQ2 routine filed

YSXRAQ3 routine filed

YSXRAQ4 routine filed

YSXRAQ routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

YSXRAR1 routine filed

YSXRAR2 routine filed

YSXRAR routine filed

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

YSXRAS1 routine filed

YSXRAS2 routine filed

YSXRAS routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

YSXRAT1 routine filed

YSXRAT2 routine filed

YSXRAT3 routine filed

YSXRAT4 routine filed

YSXRAT5 routine filed

YSXRAT6 routine filed

YSXRAT routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAU1 routine filed

YSXRAU2 routine filed

YSXRAU routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAV1 routine filed

YSXRAV2 routine filed

YSXRAV routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAW1 routine filed

YSXRAW2 routine filed

YSXRAW routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAX1 routine filed

YSXRAX2 routine filed

YSXRAX3 routine filed

YSXRAX4 routine filed

YSXRAX routine filed............

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAY1 routine filed

YSXRAY2 routine filed

YSXRAY3 routine filed

YSXRAY4 routine filed

YSXRAY routine filed

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

YSXRAZ1 routine filed

YSXRAZ2 routine filed

YSXRAZ3 routine filed

YSXRAZ4 routine filed

YSXRAZ5 routine filed

YSXRAZ6 routine filed

YSXRAZ routine filed.

Compiling Cross-Reference routine.............

...HMMM, HOLD ON...

YSXRBA1 routine filed

YSXRBA2 routine filed

YSXRBA3 routine filed

YSXRBA4 routine filed

YSXRBA5 routine filed

YSXRBA6 routine filed

YSXRBA routine filed........

'YS-AXIS 4' Help Frame filed.

'YS-GAF SCALE' Help Frame filed.

'YS-GEN MODIFIER' Help Frame filed.

'YS-LIST-OF-TESTS' Help Frame filed.

'YS-PHY-EXAM-NORM' Help Frame filed.

'YS-PSYCHOSOCIAL STRESSORS' Help Frame filed.

'YSCENP' Help Frame filed.

'YSDIAG' Help Frame filed..

'YS PSYCHTEST' BULLETIN FILED -- Remember to add mail groups for new bulletins..

..............................................................................

.........................................

'YS SITE PARAMETERS' Option Filed

'YS SITE-FILE 16' Option Filed

'YS SITE-FILE 602 TEST LIM' Option Filed

'YS SITE-FILE 602 WWU' Option Filed

'YS SITE-FILE 615.5' Option Filed

'YS SITE-FILE 615.6' Option Filed

'YS SITE-FILE 615.7' Option Filed

'YS SITE-FILE 615.8' Option Filed

'YS SITE-FILE 615.9' Option Filed

'YSADMTEST' Option Filed

'YSAPROB' Option Filed

'YSCENCAD' Option Filed

'YSCENCL' Option Filed

'YSCENCRISIS' Option Filed

'YSCENDAYHX' Option Filed

'YSCENDCDOC' Option Filed

'YSCENDIA' Option Filed

'YSCENED' Option Filed

'YSCENEDM' Option Filed

'YSCENFS' Option Filed

'YSCENGED' Option Filed

'YSCENIL' Option Filed

'YSCENLOS' Option Filed

'YSCENMAIN' Option Filed

'YSCENMEDS' Option Filed

'YSCENMGR' Option Filed

'YSCENNAM' Option Filed

'YSCENNEW' Option Filed

'YSCENPAHX' Option Filed

'YSCENPASS' Option Filed

'YSCENPL' Option Filed

'YSCENPP' Option Filed

'YSCENREM' Option Filed

'YSCENROT' Option Filed

'YSCENSL' Option Filed

'YSCENSUBUP' Option Filed

'YSCENTAH' Option Filed

'YSCENTCEN' Option Filed

'YSCENTESTING' Option Filed

'YSCENTMHX' Option Filed

'YSCENTPTE' Option Filed

'YSCENTPTP' Option Filed

'YSCENUNITUP' Option Filed

'YSCENUNT' Option Filed

'YSCENWDM' Option Filed

'YSCENWL' Option Filed

'YSCLERK' Option Filed

'YSCLINRECORD' Option Filed

'YSCOMMENT' Option Filed

'YSCRISNOT' Option Filed

'YSDECTREES-R' Option Filed

'YSDIAG' Option Filed

'YSDIAGE' Option Filed

'YSDIAGP-DX' Option Filed

'YSDIAGP-DXLS' Option Filed

'YSDIRTEST' Option Filed

'YSEPROB' Option Filed

'YSEXTESTS' Option Filed

'YSFPROB' Option Filed

'YSHX1' Option Filed

'YSHXPAST' Option Filed

'YSHXPASTR' Option Filed

'YSINST RESTART LIMIT' Option Filed

'YSIPROB' Option Filed

'YSJOBINQ' Option Filed

'YSJOBKILL' Option Filed

'YSJOBLIST' Option Filed

'YSJOBUPDATE' Option Filed

'YSKILLINC' Option Filed

'YSMANAGEMENT' Option Filed

'YSMANAGER' Option Filed

'YSMCHK' Option Filed

'YSMKIL' Option Filed

'YSMLST' Option Filed

'YSMOVP' Option Filed

'YSMUSE' Option Filed

'YSPATMSG' Option Filed

'YSPATPROF' Option Filed

'YSPERSHX' Option Filed

'YSPERSHXR' Option Filed

'YSPHYEXAM' Option Filed

'YSPIT' Option Filed

'YSPLDX' Option Filed

'YSPLPDX' Option Filed

'YSPPROB' Option Filed

'YSPRINT' Option Filed

'YSPROBLIST' Option Filed

'YSPTINSTRU' Option Filed

'YSRAPROB' Option Filed

'YSREVSYS' Option Filed

'YSREVSYSR' Option Filed

'YSRFPROB' Option Filed

'YSRSPROB' Option Filed

'YSSR 10-2683' Option Filed

'YSSR 15-CHECK' Option Filed

'YSSR DELETE' Option Filed

'YSSR EDIT' Option Filed

'YSSR ENTRY' Option Filed

'YSSR MGT UTILITY' Option Filed

'YSSR MGTRD' Option Filed

'YSSR MGTRI' Option Filed

'YSSR MGTRN' Option Filed

'YSSR MGTRW' Option Filed

'YSSR RELEASE' Option Filed

'YSSR REPORTS' Option Filed

'YSSR REVIEW' Option Filed

'YSSR REVIEW RPT' Option Filed

'YSSR SEC/RES' Option Filed

'YSSR W-ORDER' Option Filed

'YSTESTBAT' Option Filed

'YSTSTAUD' Option Filed

'YSUSER' Option Filed

'YSUTIL' Option Filed

'YSVOCATIONAL' Option Filed

'YSWAITCR' Option Filed

'YSWAITE' Option Filed

'YSWAITEDI' Option Filed

'YSWAITLST' Option Filed

'YSWAITP' Option Filed

'YSWAITREM' Option Filed

'YSWAITSHUF' Option Filed...........................

Compiling YSJOB print template of File 624..................

'YSCPAA' ROUTINE FILED..

Compiling YSSR 10-2683 FOOTER print template of File 615.2....

'YSCPAE' ROUTINE FILED.

Compiling YSSR 10-2683 HEADER print template of File 615.2.............

'YSCPAF' ROUTINE FILED...........

Compiling YSSR 10-2683 PRINT print template of File 615.2....................

'YSCPAG' ROUTINE FILED..........

Compiling YSSR DATE MGT HEADER print template of File 615.2..........

'YSCPAH' ROUTINE FILED.......

Compiling YSSR DATE MGT PRINT print template of File 615.2....................

.

'YSCPAI' ROUTINE FILED.........

Compiling YSSR NURSE MGT HEADER print template of File 615.2.........

'YSCPAJ' ROUTINE FILED.......

Compiling YSSR NURSE MGT PRINT print template of File 615.2...................

'YSCPAK' ROUTINE FILED...........

Compiling YSSR PT INQ HEADER print template of File 615.2....................

'YSCPAL' ROUTINE FILED.............

Compiling YSSR PT INQ PRINT print template of File 615.2................

'YSCPAM' ROUTINE FILED...

Compiling YSSR REVIEW ACTION HEADER print template of File 615.2..............

'YSCPAN' ROUTINE FILED........

Compiling YSSR REVIEW ACTION PRINT print template of File 615.2...............

'YSCPAO' ROUTINE FILED........

Compiling YSSR WARD MGT HEADER print template of File 615.2.........

'YSCPAP' ROUTINE FILED.......

Compiling YSSR WARD MGT PRINT print template of File 615.2....................

'YSCPAQ' ROUTINE FILED...........

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Starting Post-init process...

Placing Options Out of Order

Adding the YS PATIENT MOVEMENT to the DGPM MOVEMENT EVENTS protocol...

This version of 'YSONIT' was created on 18-JUN-1993

(at DALLAS ISC - FS ACCOUNT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please.....

'YS PATIENT MOVEMENT' Protocol Filed

YS PATIENT MOVEMENT added as item to DGPM MOVEMENT EVENTS.

OK, Protocol Installation is Complete.

Deleting obsolete options...

Deleting obsolete YSPN\* print templates ....

Setting MH Parameters data...

All post-init tasks have now been completed, except the conversion of DSM3

and DSM-III-R data to the new DSM file. This will be done now...

Performing DSM environment checks...

The DSM conversion is about to begin. During this conversion...

\* All entries in the Medical Record file, pointing to the DSM3 file, will

be repointed to the DSM file.

\* All entries in the Generic Progress Notes file, pointing to the DSM-III-R

file, will be repointed to the DSM file.

\* All entries in the Diagnostic Results - Mental Health file, pointing to

the DSM-III-R file, will be repointed to the DSM file.

Please read the Mental Health V. 5.01 Installation guide for full

documentation of the process!!

Repointing Medical Record file data from the DSM3 file to the DSM file...

..........................................................................................................................................................................................................................................

Repointing Generic Progress Notes data from the DSM-III-R to the DSM file...

.............................................................................

Repointing Diagnostic Results data from the DSM-III-R file to the DSM file...

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

Installation of DSM-IV Diagnostic Codes and patient data conversion completed!!

DSM Conversion Error Totals Dallas

==============================================================================

Error Summary: Medical Record (#90) file errors: 2145

Generic Progress Notes (#121) file errors: 0

Diagnostic Results (#627.8) file errors: 0

-----------------------------------------------------

Total number of errors: 2145

Print Errors? Y// N (NO)

Returning Options to Service

### Installation over Mental Health V. 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows the terminal dialogue seen during installation of Mental Health V. 5.01 on a Mental Health V. 5.0 account.

Example: INIT Completed at the Dallas ISC

\>D ^YSINIT

This version (#5.01) of 'YSINIT' was created on 20-DEC-1994

(at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.20.0)

AM GOING TO SET UP THE FOLLOWING FILES:

90 MEDICAL RECORD

> **NOTE:** You already have the 'MEDICAL RECORD' File.

99 PT. TEXT

> **NOTE:** You already have the 'PT. TEXT' File.

600.7 CRISIS NOTE DISPLAY

> **NOTE:** You already have the 'CRISIS NOTE DISPLAY' File.

601 MH INSTRUMENT

> **NOTE:** You already have the 'MH INSTRUMENT' File.

601.2 PSYCH INSTRUMENT PATIENT

> **NOTE:** You already have the 'PSYCH INSTRUMENT PATIENT' File.

601.3 COPYRIGHT HOLDER (including data)

> **NOTE:** You already have the 'COPYRIGHT HOLDER' File.

I will OVERWRITE your data with mine.

601.4 INCOMPLETE PSYCH TEST PATIENT

> **NOTE:** You already have the 'INCOMPLETE PSYCH TEST PATIENT' File.

602 MENTAL HEALTH SITE PARAMETERS

> **NOTE:** You already have the 'MENTAL HEALTH SITE PARAMETERS' File.

605 MH TEXT (including data)

> **NOTE:** You already have the 'MH TEXT' File.

I will OVERWRITE your data with mine.

615 MH CLINICAL FILE

> **NOTE:** You already have the 'MH CLINICAL FILE' File.

615.2 SECLUSION/RESTRAINT

> **NOTE:** You already have the 'SECLUSION/RESTRAINT' File.

615.5 S/R REASONS (including data)

> **NOTE:** You already have the 'S/R REASONS' File.

I will MERGE your data with mine.

615.6 S/R CATEGORY (including data)

> **NOTE:** You already have the 'S/R CATEGORY' File.

I will MERGE your data with mine.

615.7 S/R RELEASE CRITERIA (including data)

> **NOTE:** You already have the 'S/R RELEASE CRITERIA' File.

I will MERGE your data with mine.

615.8 S/R ALTERNATIVES (including data)

> **NOTE:** You already have the 'S/R ALTERNATIVES' File.

I will MERGE your data with mine.

615.9 S/R OBSERVATION CHECKLIST (including data)

> **NOTE:** You already have the 'S/R OBSERVATION CHECKLIST' File.

I will MERGE your data with mine.

617 MH WAIT LIST

> **NOTE:** You already have the 'MH WAIT LIST' File.

618 MENTAL HEALTH CENSUS

> **NOTE:** You already have the 'MENTAL HEALTH CENSUS' File.

618.2 MENTAL HEALTH TEAM

> **NOTE:** You already have the 'MENTAL HEALTH TEAM' File.

618.4 MENTAL HEALTH INPT

> **NOTE:** You already have the 'MENTAL HEALTH INPT' File.

620 PROBLEM (including data)

> **NOTE:** You already have the 'PROBLEM' File.

I will OVERWRITE your data with mine.

624 JOB BANK

> **NOTE:** You already have the 'JOB BANK' File.

625 INDICATOR (including data)

> **NOTE:** You already have the 'INDICATOR' File.

I will OVERWRITE your data with mine.

627 DSM3 (including data)

> **NOTE:** You already have the 'DSM3' File.

I will OVERWRITE your data with mine.

627.5 DSM-III-R (including data)

> **NOTE:** You already have the 'DSM-III-R' File.

I will OVERWRITE your data with mine.

627.7 DSM (including data)

I will OVERWRITE your data with mine.

627.8 DIAGNOSTIC RESULTS - MENTAL HEALTH

> **NOTE:** You already have the 'DIAGNOSTIC RESULTS - MENTAL HEALTH' File.

627.9 DSM MODIFIERS (including data)

\*BUT YOU ALREADY HAVE 'DSM-III-R MODIFIERS' AS FILE \#627.9!

Shall I change the NAME of the file to DSM MODIFIERS? NO// Y (YES)

627.9 DSM MODIFIERS (including data)

> **NOTE:** You already have the 'DSM MODIFIERS' File.

I will OVERWRITE your data with mine.

627.99 DSM CONVERSION

628 YSEXPERT

> **NOTE:** You already have the 'YSEXPERT' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Starting the Mental Health 5.01 pre-init now...

If your package file contains an entry named 'Mental Health System'

it will be renamed 'Mental Health' ...

Placing Options Out of Order

> **NOTE:** You are not required to have the ICD Diagnosis file \#80 installed

but the Final Discharge Note within Progress Notes points to this file.

If you wish to use this type of note, please install this file.

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS

.....................................................................................................................................................................................................................................................................................................................................................................................................................................

Compiling Cross-Reference routine.............

...SORRY, JUST A MOMENT PLEASE...

YSXRAA1 routine filed

YSXRAA2 routine filed

YSXRAA3 routine filed

YSXRAA4 routine filed

YSXRAA routine filed

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAB1 routine filed

YSXRAB2 routine filed

YSXRAB3 routine filed

YSXRAB4 routine filed

YSXRAB routine filed

Compiling Cross-Reference routine.............

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

YSXRAC1 routine filed

YSXRAC2 routine filed

YSXRAC3 routine filed

YSXRAC4 routine filed

YSXRAC5 routine filed

YSXRAC6 routine filed

YSXRAC7 routine filed

YSXRAC8 routine filed

YSXRAC routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

YSXRAD1 routine filed

YSXRAD2 routine filed

YSXRAD routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAE1 routine filed

YSXRAE2 routine filed

YSXRAE3 routine filed

YSXRAE4 routine filed

YSXRAE routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAF1 routine filed

YSXRAF2 routine filed

YSXRAF3 routine filed

YSXRAF4 routine filed

YSXRAF5 routine filed

YSXRAF6 routine filed

YSXRAF routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

YSXRAG1 routine filed

YSXRAG2 routine filed

YSXRAG routine filed.

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

YSXRAJ1 routine filed

YSXRAJ2 routine filed

YSXRAJ3 routine filed

YSXRAJ4 routine filed

YSXRAJ routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

YSXRAK1 routine filed

YSXRAK2 routine filed

YSXRAK3 routine filed

YSXRAK4 routine filed

YSXRAK5 routine filed

YSXRAK6 routine filed

YSXRAK7 routine filed

YSXRAK8 routine filed

YSXRAK9 routine filed

YSXRAK10 routine filed

YSXRAK11 routine filed

YSXRAK12 routine filed

YSXRAK routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAL1 routine filed

YSXRAL2 routine filed

YSXRAL routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

YSXRAM1 routine filed

YSXRAM2 routine filed

YSXRAM routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAN1 routine filed

YSXRAN2 routine filed

YSXRAN routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAO1 routine filed

YSXRAO2 routine filed

YSXRAO routine filed.

Compiling Cross-Reference routine.............

...SORRY, JUST A MOMENT PLEASE...

YSXRAP1 routine filed

YSXRAP2 routine filed

YSXRAP routine filed.

Compiling Cross-Reference routine.............

..SORRY, JUST A MOMENT PLEASE...

YSXRAQ1 routine filed

YSXRAQ2 routine filed

YSXRAQ3 routine filed

YSXRAQ4 routine filed

YSXRAQ routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAR1 routine filed

YSXRAR2 routine filed

YSXRAR routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

YSXRAS1 routine filed

YSXRAS2 routine filed

YSXRAS routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAT1 routine filed

YSXRAT2 routine filed

YSXRAT3 routine filed

YSXRAT4 routine filed

YSXRAT5 routine filed

YSXRAT6 routine filed

YSXRAT routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

YSXRAU1 routine filed

YSXRAU2 routine filed

YSXRAU routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRAV1 routine filed

YSXRAV2 routine filed

YSXRAV routine filed.

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAW1 routine filed

YSXRAW2 routine filed

YSXRAW routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAX1 routine filed

YSXRAX2 routine filed

YSXRAX3 routine filed

YSXRAX4 routine filed

YSXRAX routine filed............

Compiling Cross-Reference routine.............

...SORRY, HOLD ON...

YSXRAY1 routine filed

YSXRAY2 routine filed

YSXRAY3 routine filed

YSXRAY4 routine filed

YSXRAY routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

YSXRAZ1 routine filed

YSXRAZ2 routine filed

YSXRAZ3 routine filed

YSXRAZ4 routine filed

YSXRAZ5 routine filed

YSXRAZ6 routine filed

YSXRAZ routine filed.

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

YSXRBA1 routine filed

YSXRBA2 routine filed

YSXRBA3 routine filed

YSXRBA4 routine filed

YSXRBA5 routine filed

YSXRBA6 routine filed

YSXRBA routine filed........

'YS-AXIS 4' Help Frame filed.

'YS-GAF SCALE' Help Frame filed.

'YS-GEN MODIFIER' Help Frame filed.

'YS-LIST-OF-TESTS' Help Frame filed.

'YS-PHY-EXAM-NORM' Help Frame filed.

'YS-PSYCHOSOCIAL STRESSORS' Help Frame filed.

'YSCENP' Help Frame filed.

'YSDIAG' Help Frame filed..

'YS PSYCHTEST' BULLETIN FILED -- Remember to add mail groups for new bulletins..

......................................................................................................................

'YS SITE PARAMETERS' Option Filed

'YS SITE-FILE 16' Option Filed

'YS SITE-FILE 602 TEST LIM' Option Filed

'YS SITE-FILE 602 WWU' Option Filed

'YS SITE-FILE 615.5' Option Filed

'YS SITE-FILE 615.6' Option Filed

'YS SITE-FILE 615.7' Option Filed

'YS SITE-FILE 615.8' Option Filed

'YS SITE-FILE 615.9' Option Filed

'YSADMTEST' Option Filed

'YSAPROB' Option Filed

'YSCENCAD' Option Filed

'YSCENCL' Option Filed

'YSCENCRISIS' Option Filed

'YSCENDAYHX' Option Filed

'YSCENDCDOC' Option Filed

'YSCENDIA' Option Filed

'YSCENED' Option Filed

'YSCENEDM' Option Filed

'YSCENFS' Option Filed

'YSCENGED' Option Filed

'YSCENIL' Option Filed

'YSCENLOS' Option Filed

'YSCENMAIN' Option Filed

'YSCENMEDS' Option Filed

'YSCENMGR' Option Filed

'YSCENNAM' Option Filed

'YSCENNEW' Option Filed

'YSCENPAHX' Option Filed

'YSCENPASS' Option Filed

'YSCENPL' Option Filed

'YSCENPP' Option Filed

'YSCENREM' Option Filed

'YSCENROT' Option Filed

'YSCENSL' Option Filed

'YSCENSUBUP' Option Filed

'YSCENTAH' Option Filed

'YSCENTCEN' Option Filed

'YSCENTESTING' Option Filed

'YSCENTMHX' Option Filed

'YSCENTPTE' Option Filed

'YSCENTPTP' Option Filed

'YSCENUNITUP' Option Filed

'YSCENUNT' Option Filed

'YSCENWDM' Option Filed

'YSCENWL' Option Filed

'YSCLERK' Option Filed

'YSCLINRECORD' Option Filed

'YSCOMMENT' Option Filed

'YSCRISNOT' Option Filed

'YSDECTREES-R' Option Filed

'YSDIAG' Option Filed

'YSDIAGE' Option Filed

'YSDIAGP-DX' Option Filed

'YSDIAGP-DXLS' Option Filed

'YSDIRTEST' Option Filed

'YSEPROB' Option Filed

'YSEXTESTS' Option Filed

'YSFPROB' Option Filed

'YSHX1' Option Filed

'YSHXPAST' Option Filed

'YSHXPASTR' Option Filed

'YSINST RESTART LIMIT' Option Filed

'YSIPROB' Option Filed

'YSJOBINQ' Option Filed

'YSJOBKILL' Option Filed

'YSJOBLIST' Option Filed

'YSJOBUPDATE' Option Filed

'YSKILLINC' Option Filed

'YSMANAGEMENT' Option Filed

'YSMANAGER' Option Filed

'YSMCHK' Option Filed

'YSMKIL' Option Filed

'YSMLST' Option Filed

'YSMOVP' Option Filed

'YSMUSE' Option Filed

'YSPATMSG' Option Filed

'YSPATPROF' Option Filed

'YSPERSHX' Option Filed

'YSPERSHXR' Option Filed

'YSPHYEXAM' Option Filed

'YSPIT' Option Filed

'YSPLDX' Option Filed

'YSPLPDX' Option Filed

'YSPPROB' Option Filed

'YSPRINT' Option Filed

'YSPROBLIST' Option Filed

'YSPTINSTRU' Option Filed

'YSRAPROB' Option Filed

'YSREVSYS' Option Filed

'YSREVSYSR' Option Filed

'YSRFPROB' Option Filed

'YSRSPROB' Option Filed

'YSSR 10-2683' Option Filed

'YSSR 15-CHECK' Option Filed

'YSSR DELETE' Option Filed

'YSSR EDIT' Option Filed

'YSSR ENTRY' Option Filed

'YSSR MGT UTILITY' Option Filed

'YSSR MGTRD' Option Filed

'YSSR MGTRI' Option Filed

'YSSR MGTRN' Option Filed

'YSSR MGTRW' Option Filed

'YSSR RELEASE' Option Filed

'YSSR REPORTS' Option Filed

'YSSR REVIEW' Option Filed

'YSSR REVIEW RPT' Option Filed

'YSSR SEC/RES' Option Filed

'YSSR W-ORDER' Option Filed

'YSTESTBAT' Option Filed

'YSTSTAUD' Option Filed

'YSUSER' Option Filed

'YSUTIL' Option Filed

'YSVOCATIONAL' Option Filed

'YSWAITCR' Option Filed

'YSWAITE' Option Filed

'YSWAITEDI' Option Filed

'YSWAITLST' Option Filed

'YSWAITP' Option Filed

'YSWAITREM' Option Filed

'YSWAITSHUF' Option Filed...........................

Compiling YSJOB print template of File 624..................

'YSCPAA' ROUTINE FILED..

Compiling YSSR 10-2683 FOOTER print template of File 615.2....

'YSCPAE' ROUTINE FILED.

Compiling YSSR 10-2683 HEADER print template of File 615.2.............

'YSCPAF' ROUTINE FILED...........

Compiling YSSR 10-2683 PRINT print template of File 615.2...................

'YSCPAG' ROUTINE FILED..........

Compiling YSSR DATE MGT HEADER print template of File 615.2..........

'YSCPAH' ROUTINE FILED.......

Compiling YSSR DATE MGT PRINT print template of File 615.2....................

'YSCPAI' ROUTINE FILED.........

Compiling YSSR NURSE MGT HEADER print template of File 615.2.........

'YSCPAJ' ROUTINE FILED.......

Compiling YSSR NURSE MGT PRINT print template of File 615.2...................

'YSCPAK' ROUTINE FILED...........

Compiling YSSR PT INQ HEADER print template of File 615.2.....................

'YSCPAL' ROUTINE FILED.............

Compiling YSSR PT INQ PRINT print template of File 615.2................

'YSCPAM' ROUTINE FILED...

Compiling YSSR REVIEW ACTION HEADER print template of File 615.2..............

'YSCPAN' ROUTINE FILED........

Compiling YSSR REVIEW ACTION PRINT print template of File 615.2...............

'YSCPAO' ROUTINE FILED........

Compiling YSSR WARD MGT HEADER print template of File 615.2.........

'YSCPAP' ROUTINE FILED.......

Compiling YSSR WARD MGT PRINT print template of File 615.2....................

'YSCPAQ' ROUTINE FILED...........

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Starting Post-init process...

Placing Options Out of Order

Adding the YS PATIENT MOVEMENT to the DGPM MOVEMENT EVENTS protocol...

This version of 'YSONIT' was created on 18-JUN-1993

(at DALLAS ISC - FS ACCOUNT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please.....

'YS PATIENT MOVEMENT' Protocol Filed

OK, Protocol Installation is Complete.

Deleting obsolete options...

Deleting obsolete YSPN\* print templates ....

Setting MH Parameters data...

All post-init tasks have now been completed, except the conversion of DSM3

and DSM-III-R data to the new DSM file. This will be done now...

Performing DSM environment checks...

The DSM conversion is about to begin. During this conversion...

\* All entries in the Medical Record file, pointing to the DSM3 file, will

be repointed to the DSM file.

\* All entries in the Generic Progress Notes file, pointing to the DSM-III-R

file, will be repointed to the DSM file.

\* All entries in the Diagnostic Results - Mental Health file, pointing to

the DSM-III-R file, will be repointed to the DSM file.

Please read the Mental Health V. 5.01 Installation guide for full

documentation of the process!!

Repointing Medical Record file data from the DSM3 file to the DSM file...

..............................................................................

..............................................................................

Repointing Generic Progress Notes data from the DSM-III-R to the DSM file...

Repointing Diagnostic Results data from the DSM-III-R file to the DSM file...

..............................................................................

..............................................................................

............................................................................................................................................................

..............................................................................

..............................................................................

.................

Installation of DSM-IV Diagnostic Codes and patient data conversion completed!!

DSM Conversion Error Totals Dallas

==============================================================================

Error Summary: Medical Record (#90) file errors: 2145

Generic Progress Notes (#121) file errors: 0

Diagnostic Results (#627.8) file errors: 0

-----------------------------------------------------

Total number of errors: 2145

Print Errors? Y// N (NO)

Returning Options to Service

## Post-Installation Checks and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the installation of Mental Health V. 5.01 and the conversion of all DSM-III and DSM-III-R diagnosis code pointers by the post-INIT routines, the following steps should be taken.

### YS PSYCHTEST Bulletin and Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.01 installs the YS PSYCHTEST bulletin. This bulletin, linked with the YS PSYCHTEST mail group, is used to notify clinicians when tests and interviews are administered to patients at the request of someone other than the person administering the test. (This condition is met when the person administering the test is different than the person entered as the “Professional requesting instrument.”) Even though the YS PSYCHTEST bulletin is automatically installed by the package, clinician notification will not occur until the following steps have been followed:

1\. Using the Mail Group Edit \[XMEDITMG\] menu option, perform the following action:

If not already existent, create a mail group named YS PSYCHTEST.

2\. Link the YS PSYCHTEST mail group to the YS PSYCHTEST bulletin using the Bulletin Edit \[XMEDITBUL\] menu option. Do this by entering “YS PSYCHTEST” into the MAIL GROUP field of the YS PSYCHTEST bulletin.

#### Terminal Dialog

The terminal dialogue seen during the creation and population of the YS PSYCHTEST mail group, and the linking of the YS PSYCHTEST bulletin and mail group is shown below.

#### Mail Group Creation

Select MAIL GROUP NAME: YS PSYCHTEST

NAME: YS PSYCHTEST// \<RET\>

Select MEMBER: WALTER,REED// @

SURE YOU WANT TO DELETE? Y (YES)

Select MEMBER: \<RET\>

DESCRIPTION:

1\>The YS PSYCHTEST mail group is linked with the YS PSYCHTEST bulletin.

2\>

EDIT Option: \<RET\>

TYPE: private// \<RET\>

ORGANIZER: ^

#### Bulletin/Mail Group Link

Select BULLETIN NAME: YS PSYCHTEST

NAME: YS PSYCHTEST// \<RET\>

SUBJECT: Surrogate Entry of Tests and Interviews Replace \<RET\>

Select MAIL GROUP: YS PSYCHTEST// \<RET\>

DESCRIPTION:

1\>Notifies mental health professionals when someone requests

2\>tests or interviews in their names.

EDIT Option: \<RET\>

MESSAGE:

1\>Tests and/or interviews were undertaken by \|1\|.

2\>They were initiated by \|2\| on \|3\|,

3\>with \|4\| listed as requesting the tests.

4\>

5\>Test(s) and/or Interview(s): \|5\|

6\> \|6\| \|7\| \|8\| \|9\| \|10\| \|11\| \|12\| \|13\| \|14\| \|15\|

EDIT Option: \<RET\>

Select PARAMETER: 14// \<RET\>

DESCRIPTION:

1\>Test/interview name

EDIT Option: \<RET\>

Select PARAMETER: \<RET\>

### DSM Conversion Data Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DSM CONVERSION file (#627.99) is used during the post-INIT conversion of patient DSM data, to hold the original DSM data values prior to conversion. The DSM Conversion file also holds other conversion tracking and controlling nodes.

After successful conversion of DSM data, the data in the DSM CONVERSION file can be backed up, and then deleted. (The pre-INIT for the next Mental Health version will delete the DSM CONVERSION file.)

NOTES:

• The DSM CONVERSION file should not be deleted, only the data associated with the file!

• The deletion of DSM CONVERSION file data should not be done until Mental Health V. 5.01 has been used by clinicians entering, editing, and viewing DSM data for a sufficient length of time to detect any conversion problems.

• When backing up the DSM CONVERSION file’s global data, MSM sites should use the %GS utility. Alpha sites should use the %GTO utility. The global to save to disk, using either the %GS or %GTO utility, is ^YSD(627.99,.

This is the terminal dialogue seen during the deletion of DSM CONVERSION file data.

\>D DELDATA^YSD4UT01

The DSM Conversion file (#627.99) holds data generated during the Mental

Health V. 5.01 post init repointing of DSM patient data. This file will be

deleted when the next version of Mental Health is installed. However, you

may wish to delete the data in this file now. (This should not be done

until Mental Health V. 5.01 has been used by clinicians entering, editing,

and viewing DSM data for a sufficient length of time to detect

any conversion problems.)

NOTE !!! Please back up all data contained the DSM Conversion file's

'^YSD(627.99,' global before deleting any data.

You are about to delete the data contained in the DSM Conversion file!!

OK to continue? No// YES

The data in the DSM Conversion file will now be deleted!!!

Press RETURN to begin deletion, or '^' to exit...\<RET\>

... All data deleted ...

### DSM Conversion Routine Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-INIT and post-INIT routines, and all other routines associated with the pre-INIT and post-INIT process, are YSD4 namespaced. After the installation of Mental Health V. 5.01, the conversion of DSM data, and the deletion of the conversion data contained in the DSM CONVERSION file (#627.99), the YSD4 namespaced routines are no longer needed and can be deleted.

NOTES:

• If no data exists in the DSM CONVERSION file after the installation of Mental Health V. 5.01, or if the site does not plan to delete the data in the DSM Conversion file, all YSD4 namespaced routines can be deleted immediately after the installation of Mental Health V. 5.01.

• If data exists in the DSM CONVERSION file, and the site plans to delete the data, the deletion of the YSD4 namespaced routines should be postponed until after the DSM CONVERSION file data has been deleted. (See the previous section entitled “DSM Conversion Data Deletion” for additional information.)

# RELEASE NOTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Version 5.01 is a maintenance release. Only the Installation Guide and Release Notes are released with Version 5.01. The Technical Manual, Users Guide and Security Manual released with Mental Health V. 5.0 remain the same.

Mental Health Version 5.01 was created to provide the new DSM-IV diagnostic codes released in April 1994, to the users of the Mental Health package. Diseases and conditions are classified in the Mental Health package by using either the Diagnostic and Statistical Manual of Mental Disorders (DSM) diagnostic codes. DSM codes are owned and published by the American Psychiatric Association (APA), or the International Classification of Diseases (ICD) diagnostic codes, which are owned and published by the World Health Organization (WHO). The ICD diagnostic codes current version is referred to as ICD9 diagnostic codes. The following information summarizes the DSM Diagnostic Codes background and the changes contained in Mental Health V. 5.0 and V. 5.01.

## DSM Diagnostic Codes Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first version of DSM diagnostic codes provided in the Mental Health package was the DSM-III diagnostic codes. The DSM-III diagnostic codes entries were placed in the DSM3 file (#627). Patient DSM related data making use of (pointing to) the DSM3 file (#627) was stored in the MEDICAL RECORD file (#90). Subsequently, the revised version of the DSM-III diagnostic codes, referred to as DSM-III-R diagnostic codes, were to be made available to users of the Mental Health package. At that point the following modifications to the Mental Health package were made:

> • A new file was created to hold the DSM-III-R diagnostic codes. This file was the DSM-III-R file (#627.5).

> • The new DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8) was created to hold the patient DSM data using (pointing to) the DSM-III-R file.

> **NOTE:** When the DSM-III-R file (#627.5) and the DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8) were created, the DSM3 file (#627) and the DSM-specific fields in the MEDICAL RECORD file (#90) became obsolete. At that point, data entry into the MEDICAL RECORD file (#90) permanently ceased.

## Mental Health V. 5.0 Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The changes in the following lists were originally made by Mental Health V. 5.0, and are also included in Mental Health V. 5.01. These lists of changes are included in the Release Notes for sites who have not installed Mental Health V. 5.0, and are installing V. 5.01 on top of an account holding Mental Health V. 4.18.

### Visible Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Automatic Update of Inpatient/Features data from MAS updates, using Protocol Actions associated with the DGPM MOVEMENT EVENTS protocol. All Additions, Changes or Deletions of Patient ADMISSIONS, TRANSFERS or DISCHARGES will automatically generate a TaskMan job which will update the Mental Health Census data used by the Inpatient/Features option of the Mental Health package.

2\. The following list of tests and interviews have been added for the first time, or were present in the Mental Health package at some previous time and are being restored.

> MISS Mississippi Scale (Combat Stress)

> ERS Employment Readiness Scale

> BAI Beck Anxiety Index

> BDI Beck Depression Scale

> BHS Beck Hopelessness Scale

> BSI Beck Scale for Suicidal Ideation

3\. Corrections were made to misspellings and wording of questions on the following tests and interviews.

> PROB Problem List

> MROS Medical Review of Systems

> PSOC Patient Reported Psychosocial History

> AOR Analysis of Relationships

> CRS Carroll Rating Scale for Depression

> STAI STAI - State-Trait Anxiety Scale

4\. Improvements were made to some of the “Help” text of the instruments.

5\. Copyright information was updated and added to output reports.

6\. Security key checking was added to testing batteries and displays.

### Technical and/or Transparent Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Mental Health V. 5.0 contains Mental Health V. 4.18 verified patches.

2\. Documentation was added at all line tags that are called as either an entry point from another routine or as ENTRY or EXIT actions in options. The documentation indicates the “Called From” source.

3\. All direct KILLs of the %ZTSK global have been changed to calls to KILL^%ZTLOAD.

4\. All references to X ^DD("DD") have been changed to D DD^%DT.

5\. All references to X ^%ZIS("C") have been changed to D ^%ZISC.

6\. The majority of the End of Screen prompts have been changed to use the reader routine DIR, taking advantage of the End-Of-Page entry point.

7\. Most FOR loops now use the argumentless FOR structure (1991 ANSI Standard).

8\. All occurrences of the \$NEXT command (in 339 lines) were changed to \$ORDER to comply with standards.

9\. All existing locks have been changed to take advantage of incremental locks. All calls to DIE now lock the data element being edited by the use of incremental locks.

10\. Required referencing of the NEW PERSON file (#200) was implemented.

11\. Print templates are now compiled into routines that start with the YSCP namespace (YS Compiled Print).

12\. All cross references are now compiled into routines that start with the YSXR namespace.

## Mental Health V. 5.01 Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes were made in Mental Health V. 5.01.

### ### Visible Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. The following tests and interviews have been modified:

The Strong-Campbell Interest Inventory (SCII) is changed to the Strong Interest Inventory (SII)

If you select the “BECK” instrument, the “BDI” instrument will be administered in its place.

2\. Enter, Edit, and View Software Modifications

Software modifications were made to correctly display patient DSM data entered. These modifications will allow the user to enter, edit, and view patient DSM data entered after V. 5.01 installation. These changes are explained below.

• Generic Input Prompts

Previously, when entering or selecting diagnosis the user was prompted for a “DSM-III-R” diagnosis. Users are now asked to enter a “DSM” diagnosis.

|                       |                             |
|-----------------------|-----------------------------|
| New Prompt        | Old Prompt              |
| Enter DSM DIAGNOSIS:  | Enter DSM-III-R DIAGNOSIS:  |
| Select DSM DIAGNOSIS: | Select DSM-III-R DIAGNOSIS: |

> **NOTE:** At this time, new documentation showing screen output that includes DSM related input prompts, headers, and labels will not be released for Mental Health V. 5.01.

### Technical and/or Transparent Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Mental Health V. 5.01 contains Mental Health V. 5.0 verified patches.

2\. DSM file (#627.7)

The DSM file (#627.7) was created to store the DSM-III, DSM-III-R, and DSM-IV diagnostic codes. This file will also store any future versions of the DSM diagnostic codes. Each DSM diagnostic code entry is unique to a DSM version (even if entries are identical) and is identified by the DSM Version field.

3\. Patient DSM Data Conversion

During the Mental Health V. 5.01 post-INIT, all patient DSM data pointing to the DSM3 file (#627) and the DSM-III-R file (#627.5) will be repointed to the new DSM file (#627.7).

> **NOTE:** The following files contain patient data and will be repointed to the new DSM file (#627.7).

• <u>File pointing to the DSM3 file (#627)</u>:

\* MEDICAL RECORD file (#90)

• <u>Files pointing to the DSM-III-R file (#627.5)</u>:

\* GENERIC PROGRESS NOTES file (#121)

\* DIAGNOSTIC RESULTS - MENTAL HEALTH file (#627.8)

Two new Psychological Instrument Restart Parameters were added to the Mental Health V. 5.01 package. Both parameters are site changeable. One parameter is a site default for all instruments the second parameter is associated with individual instruments. They are used to determine the number of days allowed between the discontinuation and subsequent restarting of a test or interview.

4\. DSM Conversion File

The DSM CONVERSION file (#627.99) is used during the process of repointing MEDICAL RECORD file (#90), GENERIC PROGRESS NOTES file (#121), and DIAGNOSTIC RESULTS -MENTAL HEALTH file (#627.8), DSM data from the DSM3 (#627) or DSM-III-R (#627.5) files to the new DSM file (#627.7). The DSM CONVERSION file holds the DSM patient data in these files prior to conversion, making possible graceful restoration of patient data to baseline in the case of catastrophe. In addition to the fields contained in the DSM CONVERSION file, additional global nodes are created by the conversion software and stored in the

^YSD(627.99,"AS" global space. (These nodes are not restorable by reindexing the file!). The "AS" nodes are used to track the progress of conversion and enable the conversion process to be restarted an unlimited number of times. The ^YSD(627.99,"AS","TE" global space are used to track conversion data that does not meet the data stored on the "TE" conversion criteria checks. If errors exist, the "TE" nodes will be used to create the error report.

5\. DSM Conversion Restarts and Restores

The following safety provisions have been incorporated into the process of repointing the patient DSM data. These enhancements includes the ability to restart the repointing process multiple times and to restore all patient data to their original values.

• DSM Conversion Restart

The repointing of the patient DSM data is initially started by the Mental Health

V. 5.01 post-INIT. If the post-INIT abnormally aborts during the conversion of the patient DSM data, the conversion process can be restarted by using the call point supplied in the “Restart of DSM Conversion” section of the Installation Guide.

• DSM Data Restoration

The restoration of data can be done at any time, midway through the patient DSM data conversion process, or after the conversion process is completed. All patient DSM data entries can be restored to their pre conversion values by using the call point supplied in the “DSM Data Restoration” section of the Installation Guide.

6\. Mental Health Inpatient Movement Tracking

The Mental Health Inpatient Movement Tracking had numerous problems in the past. To correct these problems and have maintainable code, a total rewrite of the routines was in order.

The Mental Health package tracks inpatients on Mental Health wards in the MENTAL HEALTH INPT file (#618.4). Entries in this file are updated in the following manner:

• Patient admitted, transferred, or discharged by MAS.

• MAS protocol “DGPM Movement Events” activated.

• MAS protocol activates the Mental Health “YS MOVEMENT EVENTS” protocol.

• MH protocol calls routine YSCUP.

• Routine YSCUP performs necessary actions. (Actions include “no action,” or adding, updating, or deleting entries in the MENTAL HEALTH INPT file (#618.4).

The actions performed by the YSCUP routine are as follows:

• BEGIN^YSCUP calls CTRL^YSCUP000 to perform all necessary actions.

> \_ Checks for DFN.

> \_ Call to GETMH^YSCUP003 finds all MENTAL HEALTH INPT file entries for patient, and uses them to create the YSMH( array.

> \_ Call to GETMOVES^YSCUP003 finds all movements for the patients current or last inpatient stay. These movements are used to create the YSPM( array.

> \_ Call the STATUS builds piece 1 and 2 of the YST variable. (i.e., STATUS.)

> \_ Call the MATCH^YSCUP003 compares YSMH( to YSPM( and adds piece 4-6 to YST.

> \_ Call to XTMP^YSCUP004 creates ^XTMP audit entry.

> \_ Call to ACTION performs all entry creation, updating, or deletion as seen in the next subsection.

> \- Subroutine NOMH1: Deletes record if no MH wards in current stay.

> \- Subroutine NOMH2: Exits with no actions if no MH wards or moves.

> \- Subroutine MHMOV: Creates and updates new entry if no MH entry exists.

> \- Subroutine UPDATE: Updates last MH entry using last move.

> \_ Call to UPDST^YSCUP004 stores the value of YST in ^XTMP. (Piece 7 of YST is Updated by the subroutine calls under ACTION.)

> \_ Call to CLEAN^YSCUP004 kills the redundant YSPM("A" array data out of the ^XTMP entry.

> \_ QUITs if any Mental Health actions have taken place, returning to BEGIN^YSCUP.

> \_ Call to NOMH^YSCUP004 kills most of the ^XTMP data, leaving the header plus a small amount of additional data. (This only occurs if no Mental Health actions have occurred.)

> \_ QUIT returns control to BEGIN^YSCUP.

• BEGIN^YSCUP calls END to kill all YSCUP generated variables.

• Execution exits.

> **NOTE:** ^XTMP data is assigned a vaporization date of “Today + 1.”

## Package Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health V. 5.01 package is distributed as two separate files. The table shown below includes the file names and a description of the contents of each file:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 20%" />
<col style="width: 73%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>#</strong></td>
<td><strong>File Name</strong></td>
<td><strong>Description of File Contents</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>MH5_01.RTN</td>
<td>YI*, YS*, YT*, GMRPNP3, and GMRPNP4 routines.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>MH5_01.GBL</td>
<td><p>^YTT(601 global.</p>
<p>Comment: The ^YTT(601 global contains all data</p>
<p>associated with psychological tests and interviews.</p>
<p>Due to the size of this global, it is distributed as a</p>
<p>separate file.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

The files MH5_01.RTN and MH5_01.GBL are distributed to other Information Systems Centers in two ways:

1\. placed in the Dallas Information Systems Center’s anonymous directory

2\. placed on disk and/or tape and mailed.

> **NOTE:** The media chosen for distribution, tape or disk, depends on the site configuration; Alpha, or 486.

Appendix

# # Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Maps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health V. 5.01 package exports two menu systems: YSUSER, containing the options needed for user level clinicians, and YSMANAGER, holding the options needed for Mental Health managers. All other Mental Health options are available under these two menu systems. The following two menu maps display the menu options.

> **NOTE:** On the menu maps below, the menu options containing any DSM related modifications either in queries or outputs are noted in bold print.

### YSUSER Menu Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health \[YSUSER\]

==============================================================================

Clinical Record \[YSCLINRECORD\]

\| Profile of patient \[YSPATPROF\]

\| Problem list \[YSPROBLIST\]

\| \| Formulate new problem list \[YSFPROB\]

\| \| Add a new problem \[YSAPROB\]

\| \| Edit a problem \[YSEPROB\]

\| \| Print the problem list \[YSPPROB\]

\| \| Inactivate an active problem \[YSIPROB\]

\| \| Reactivate an inactive problem \[YSRAPROB\]

\| \| Resolve a problem \[YSRSPROB\]

\| \| Reformulate a problem \[YSRFPROB\]

\| \| DSM Diagnosis (Problem list) \[YSPLDX\]

\| \| ICD9 Diagnosis (Problem list) \[YSPLPDX\]

\| Diagnosis \[YSDIAG\]

\| \| Enter Diagnosis \[YSDIAGE\]

\| \| Print Diagnoses \[YSDIAGP-DX\]

\| \| Print DXLS History \[YSDIAGP-DXLS\]

\| History - present illness \[YSHX1\]

\| Past medical history (results of pt. report) \[YSHXPASTR\]

\| Psychosocial history (results of pt. report) \[YSPERSHXR\]

\| Review of systems (results of pt. report) \[YSREVSYSR\]

\| Physical exam \[YSPHYEXAM\]

\| Crisis note \[YSCRISNOT\]

\| Progress Notes User Menu \[GMRPN\]

\| \| Entry of Progress Note \[GMRPN ENTRY\]

\| \| Entry of Progress Note -- Copy Existing Note \[GMRPN COPY\]

\| \| Amend a Progress Note \[GMRPN ADDENDUM\]

\| \| Complete Unsigned Note(s) \[GMRPN SIGNATURE\]

\| \| Co-Sign Progress Note(s) \[GMRPN COSIGNER\]

\| \| Review Progress Note(s) \[GMRPN INQUIRY\]

\| \| Print Progress Notes Menu \[GMRPN PRINT\]

\| \| \| Patient Name \[GMRPN PRINT PT\]

\| \| \| Patient Location \[GMRPN PRINT LOCATION\]

\| \| \| Date of Progress Note \[GMRPN PRINT DATE\]

\| \| \| Author of Progress Note \[GMRPN PRINT AUTHOR\]

\| \| \| Title of Progress Note \[GMRPN PRINT TITLE\]

\| \| \| Type of Progress Note \[GMRPN PRINT TYPE\]

\| \| Patient Warning (CWAD) Display \[GMRPNCW\]

\| \| Edit Electronic Signature code \[XUSESIG\]

\| Patient message \[YSPATMSG\]

\| Tests and interviews (results) \[YSPRINT\]

\| Seclusion/Restraint \[YSSR SEC/RES\]

\| \| Entry of Patient to Seclusion/Restraint \[YSSR ENTRY\]

\| \| Release of Patient from Seclusion/Restraint \[YSSR RELEASE\]

\| \| Fifteen-Minute Check \[YSSR 15-CHECK\]

\| \| Seclusion/Restraint Report Utilities \[YSSR REPORTS\]

\| \| \| MONTHLY..Monthly Report (VA Form 10-2683) \[YSSR 10-2683\]

\| \| \| PATIENT..S/R Mgmt Report by Patient Episode \[YSSR MGTRI\]

\| \| \| DATE.....S/R Mgmt Report by Date \[YSSR MGTRD\]

\| \| \| NURSING..S/R Mgmt Report by Nursing Shift \[YSSR MGTRN\]

\| \| \| REVIEW...S/R Mgmt Report of Review Actions \[YSSR REVIEW RPT\]

\| \| \| WARD.....S/R Mgmt Ward Report \[YSSR MGTRW\]

Patient-administered Instruments \[YSPTINSTRU\]

\| Past medical history \[YSHXPAST\]

\| Psychosocial history \[YSPERSHX\]

\| Review of systems \[YSREVSYS\]

\| Psychological tests/interviews (administer) \[YSADMTEST\]

Vocational Rehabilitation \[YSVOCATIONAL\]

\| Update job bank \[YSJOBUPDATE\]

\| Search job bank \[YSJOBLIST\]

\| Inquire to job bank \[YSJOBINQ\]

\| Purge job bank \[YSJOBKILL\]

General Management \[YSMANAGEMENT\]

\| Wait lists \[YSWAITLST\]

\| \| Print wait list \[YSWAITP\]

\| \| Add patient to wait list \[YSWAITE\]

\| \| Edit patient list data \[YSWAITEDI\]

\| \| Move patient on list \[YSWAITSHUF\]

\| \| Remove patient from list \[YSWAITREM\]

\| \| Create/edit wait lists \[YSWAITCR\]

\| List Tests & Interviews \[YSMLST\]

\| Clerk-entered tests \[YSCLERK\]

\| Staff entry of tests/interviews \[YSDIRTEST\]

\| Append comments to tests and interviews \[YSCOMMENT\]

Inpatient Features \[YSCENMAIN\]

\| Census \[YSCENFS\]

\| Enter/Edit MH Inpatient Data \[YSCENEDM\]

\| \| Discharge Comments Entry \[YSCENDCDOC\]

\| \| Enter/Edit Current Inpatient Data \[YSCENED\]

\| \| Group Data Entry/Edit \[YSCENGED\]

\| \| Treatment Plan Tracking data entry \[YSCENTPTE\]

\| Individual Data Look Up \[YSCENPAHX\]

\| Group Data Lookup \[YSCENUNT\]

\| \| Crisis notes and Messages \[YSCENCRISIS\]

\| \| Active Diagnoses \[YSCENDIA\]

\| \| Outpatient Medications \[YSCENMEDS\]

\| \| Psychological Tests and Interviews \[YSCENTESTING\]

\| \| Patient Profile Data \[YSCENPP\]

\| Name Search \[YSCENNAM\]

\| Patient Lists \[YSCENPL\]

\| \| Custom List \[YSCENCL\]

\| \| Individual Patient List \[YSCENIL\]

\| \| Pass/Last Transfer List \[YSCENPASS\]

\| \| Short Patient List \[YSCENSL\]

\| \| Work List \[YSCENWL\]

\| Statistics \[YSCENWDM\]

\| \| Current Inpatient Days \[YSCENLOS\]

\| \| Previous Admissions by Date \[YSCENDAYHX\]

\| \| Recent Admissions \[YSCENNEW\]

\| \| Graph of Patients Remaining \[YSCENREM\]

\| \| Team Admissions Record \[YSCENTAH\]

\| \| Team Census \[YSCENTCEN\]

\| \| Treatment Plan Tracking Report \[YSCENTPTP\]

\| \| Ward/Team History - LOS, DRG and DXLS \[YSCENTMHX\]

### YSMANAGER Menu Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHS Manager \[YSMANAGER\]

==============================================================================

Inpatient Features management functions \[YSCENMGR\]

\| Cancel a MH Census Discharge \[YSCENCAD\]

\| Rotation of Teams \[YSCENROT\]

\| Team Definition \[YSCENSUBUP\]

\| Ward Definition \[YSCENUNITUP\]

Mental Health System site parameters \[YS SITE PARAMETERS\]

\| REASONS......Edit S/R Reasons File \[YS SITE-FILE 615.5\]

\| CATEGORY.....Edit S/R Category File \[YS SITE-FILE 615.6\]

\| RELEASE......Edit S/R Release Criteria File \[YS SITE-FILE 615.7\]

\| ALTERNATIVES.Edit S/R Alternatives File \[YS SITE-FILE 615.8\]

\| CHECKLIST....Edit S/R Checklist File \[YS SITE-FILE 615.9\]

\| WWU..........Edit Weighted Work Unit (WWU) \[YS SITE-FILE 602 WWU\]

\| SIGNATURE....Edit Signature Block Title \[YS SITE-FILE 16\]

\| INSTRUMENT...Edit Instrument Restart Day Limit \[YS SITE-FILE 602 TEST LIM\]

Psych test utilities \[YSUTIL\]

\| Usage Statistics \[YSMUSE\]

\| Audit test/interview data \[YSTSTAUD\]

\| Check Psych Data Base \[YSMCHK\]

\| Test battery utility \[YSTESTBAT\]

\| Exempt psychological tests \[YSEXTESTS\]

\| Delete Patient Data \[YSMKIL\]

\| Print test/interview items \[YSPIT\]

\| Delete incomplete tests/interviews \[YSKILLINC\]

\| Edit Instrument Restart Limit \[YSINST RESTART LIMIT\]

Move crisis notes and messages \[YSMOVP\]

Seclusion/Restraint Management Utilities \[YSSR MGT UTILITY\]

\| Review of Seclusion/Restraint Action \[YSSR REVIEW\]

\| Written Order Edit \[YSSR W-ORDER\]

\| Edit Seclusion/Restraint Entry \[YSSR EDIT\]

\| Delete Seclusion/Restraint Entry \[YSSR DELETE\]

Decision Tree Shell \[YSDECTREES-R\]

Progress Notes Mgmt Menu \[GMRPNMGR\]

\| Progress Notes User Menu \[GMRPN\]

\| \| Entry of Progress Note \[GMRPN ENTRY\]

\| \| Entry of Progress Note -- Copy Existing Note \[GMRPN COPY\]

\| \| Amend a Progress Note \[GMRPN ADDENDUM\]

\| \| Complete Unsigned Note(s) \[GMRPN SIGNATURE\]

\| \| Co-Sign Progress Note(s) \[GMRPN COSIGNER\]

\| \| Review Progress Note(s) \[GMRPN INQUIRY\]

\| \| Print Progress Notes Menu \[GMRPN PRINT\]

\| \| \| Patient Name \[GMRPN PRINT PT\]

\| \| \| Patient Location \[GMRPN PRINT LOCATION\]

\| \| \| Date of Progress Note \[GMRPN PRINT DATE\]

\| \| \| Author of Progress Note \[GMRPN PRINT AUTHOR\]

\| \| \| Title of Progress Note \[GMRPN PRINT TITLE\]

\| \| \| Type of Progress Note \[GMRPN PRINT TYPE\]

\| \| Patient Warning (CWAD) Display \[GMRPNCW\]

\| \| Edit Electronic Signature code \[XUSESIG\]

\| Complete Unsigned Note(s) for Author \[GMRPN MGR SIGN\]

\| List Unsigned Progress Notes \[GMRPN UNSIGNED\]

\| Purge Progress Notes \[GMRPX PURGE MENU\]

\| \| Purge Unsigned Progress Note(s) \[GMRPX PURGE UNSIGNED\]

\| \| Delete a Signed Progress Note \[GMRPX PURGE SIGNED\]

\| \| Purge Archived Progress Notes \[GMRPX PURGE\]

\| Remove Note from Patient Warnings (CWAD) \[GMRPN CRISIS MOVE\]

\| Add/Inquire to Progress Note Title(s) \[GMRPN TITLE EDIT\]

\| Edit Progress Note Security Key Holders \[GMRPN KEY\]

\| Parameter Edit for Progress Notes \[GMRPN PARAMETER\]