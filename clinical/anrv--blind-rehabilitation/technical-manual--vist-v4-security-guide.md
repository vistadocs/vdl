---
title: VIST Version 4 Technical Manual / Security Guide
doc_type: TM
doc_label: Technical Manual
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
  - table
  - contents
  - vist
  - anrv
  - security
  - patient
  - review
  - routines
  - options
  - software
page_count: 0
word_count: 2216
section_count: 22
table_count: 21
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: June 1998
revision_count: 1
revision_newest: 3/14/03
revision_oldest: 3/14/03
docx_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=106"
---

![](vist-version-4-technical-manual-security-guide/001.png)

VISUAL IMPAIRMENT SERVICE TEAM(VIST)Technical Manual/Security Guide

June 1998

Office of the Chief Information Officer

Revision History

|          |                                                        |                                                       |                                                                                             |
|----------|--------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Date | Revision                                           | Description                                       | Author                                                                                  |
| 6/1998   | Final Version 4.0                                      | VIST 4.0 Technical Manual                             | Office of Chief Information Officer                                                         |
| 3/14/03  | Final Version 4.0 +ANRV \*4 \*5 Patch Version 4.0.5.1. | Addition of Appendix A: ANRV \*4\*5 Patch User Manual | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

Table of Contents

Introduction [2](#introduction)

Icons [2](#icons)

Related Manuals [2](#related-manuals)

Implementation and Maintenance [3](#implementation-and-maintenance)

Resource Requirements [3](#resource-requirements)

Options to be Deleted during Install [3](#options-to-be-deleted-during-install)

Templates to be Deleted during Install [3](#templates-to-be-deleted-during-install)

Routines to Delete [5](#routines-to-delete)

Files [5](#files)

Routines [6](#routines)

Exported Options [6](#exported-options)

Menu Assignments [6](#menu-assignments)

Security Keys [6](#security-keys)

Package Security [6](#package-security)

Archiving and Purging [6](#archiving-and-purging)

Callable Routines [7](#callable-routines)

External Interfaces [7](#external-interfaces)

External Relations [7](#external-relations)

Data Base Integration Agreements (DBIAs) [7](#data-base-integration-agreements-dbias)

Internal Relations [7](#internal-relations)

Package-Wide Variables [7](#package-wide-variables)

Templates [8](#templates)

Security Management [9](#security-management)

Menu Assignments [9](#menu-assignments-1)

Security Keys [9](#security-keys-1)

Menus [9](#menus)

File Security [11](#file-security)

Appendix A: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1) [12](#appendix-a-blind-rehabilitation-vist-patient-review-anrv-4.0.5.1)

Introduction to VIST Patient Review Software [12](#introduction-to-vist-patient-review-software)

Implementation [12](#implementation)

Features [13](#features)

Software and Manual Retrieval [13](#software-and-manual-retrieval)

Files [14](#files-1)

Routines [14](#routines-1)

Data Dictionary Globals [14](#data-dictionary-globals)

Options [14](#options)

RPC Broker Calls [15](#rpc-broker-calls)

Glossary [16](#glossary)

Index [17](#index)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Icons](#icons)
  - [Related Manuals](#related-manuals)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Resource Requirements](#resource-requirements)
  - [Options to be Deleted during Install](#options-to-be-deleted-during-install)
  - [Templates to be Deleted during Install](#templates-to-be-deleted-during-install)
  - [Routines to Delete](#routines-to-delete)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [Menu Assignments](#menu-assignments)
  - [Security Keys](#security-keys)
  - [Package Security](#package-security)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Data Base Integration Agreements (DBIAs)](#data-base-integration-agreements-dbias)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Templates](#templates)
- [Security Management](#security-management)
  - [Menu Assignments](#menu-assignments-1)
  - [Security Keys](#security-keys-1)
  - [Menus](#menus)
  - [File Security](#file-security)
- [Appendix A: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1)](#appendix-a-blind-rehabilitation-vist-patient-review-anrv-4051)
  - [Introduction to VIST Patient Review Software](#introduction-to-vist-patient-review-software)
  - [Implementation](#implementation)
    - [Features](#features)
    - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [Files](#files-1)
  - [Routines](#routines-1)
  - [Data Dictionary Globals](#data-dictionary-globals)
  - [Options](#options)
  - [RPC Broker Calls](#rpc-broker-calls)
- [Glossary](#glossary)
- [Index](#index)
> The Visual Impairment Service Team (VIST) program is designed to enhance the efficiency of the Visual Impairment Service Team programs within the Department of Veterans Affairs (VA). With this program VIS Teams are able to easily manage and track activities and services provided to blinded veterans in their service area. This program integrates several fields of patient data to produce a variety of reports. The VIST patient record printout can be used in place of VA Form (10-1371) and is a more versatile document than the card. Semi- annual AMIS reports can be run and veterans can be added or deleted from the rolls quickly.
During the installation of VIST V. 4.0, all data entered using the class III Blind Rehabilitation software will be moved into the new files created for VIST V. 4.0. This conversion time will vary depending on the amount of patient information that was entered into the class III files.
> Information Resources Management (IRM) is the primary user of this manual.
> Users who are not familiar with Veterans Health Information systems and Technology Architecture (V*IST*A) software may also wish to refer to documentation for VA Kernel.

## Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Icons used to highlight key points in this manual are defined as follows:

- Indicates the user should take note of the information.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Visual Impairment Service Team V. 4.0 User Manual*

> *Visual Impairment Service Team V. 4.0 Installation Guide*

> *  
> *

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version (4.0) of VIST contains approximately 25 routines including all ANRV\* routines and compiled templates that take up approximately 69 K disk space.

## Options to be Deleted during Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                     |                             |
|---------------------|-----------------------------|
| Option Name     | Menu Text               |
| ANRV ASSESSMENT INQ | Individual Assessment - Old |

## Templates to be Deleted during Install 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                       |          |
|-----------------------|----------|
| Input             | File |
| ANRV EDIT CHECKLIST   | 623061   |
| ANRV EDIT LETTER      | 623033   |
| ANRV VIST PARM        | 623050   |
| ANRVACE               | 623036   |
| ANRVEID               | 623158   |
| ANRVRE                | 623158   |
| ANRVRRE               | 623160   |
|                       |          |
| Print             | File |
| ANRV ADDRESS LIST     | 623158   |
| ANRV ADDRESS LIST HDR | 623158   |
| ANRV AGE LIST         | 623158   |
| ANRV ASSESSMENT INQ   | 623158   |
| ANRV BIRTH LIST       | 623158   |
| ANRV CHECKLIST        | 623061   |
| ANRV CITY LIST        | 623158   |
| ANRV CLAIM REC INQ    | 623036   |
| ANRV COUNTY LIST      | 623158   |
| ANRV DECEASED LIST    | 623158   |
| ANRV ELIG AMIS LIST   | 623158   |
| ANRV EYE DIAG INQ     | 623158   |
| ANRV EYE DIAG LIST    | 623158   |
| ANRV EYE DIAG NAR     | 623158   |
| ANRV EYE DIAG PRINT   | 623158   |
| ANRV FEE PT           | 623158   |
| ANRV INC AMIS         | 623158   |
| Print (cont’d.)   | File |
| ANRV MAIL LABELS      | 623158   |
| ANRV ML BY CITY       | 623158   |
| ANRV ML BY COUNTY     | 623158   |
| ANRV POS LIST         | 623158   |
| ANRV PRINT LETTER     | 623158   |
| ANRV REFERRAL LIST    | 623158   |
| ANRV REVIEW INQ       | 623158   |
| ANRV ROSTER A/R       | 623158   |
| ANRV STATE LIST       | 623158   |
| ANRV ZIP CODE LIST    | 623158   |
| ANRVACP               | 623036   |
| ANRVAP                | 623158   |
| ANRVED                | 623158   |
| ANRVFVD               | 623158   |
| ANRVID                | 623158   |
| ANRVPR                | 623160   |
| ANRVREV               | 623158   |
| ANRVRP1               | 623158   |
| ANVRRL                | 623160   |
|                       |          |
| Sort              | File |
| ANRV ADDRESS LIST     | 623158   |
| ANRV AGE LIST         | 623158   |
| ANRV BIRTH LIST       | 623158   |
| ANRV CHECKLIST        | 623061   |
| ANRV CITY LIST        | 623158   |
| ANRV COUNTY LIST      | 623158   |
| ANRV DECEASED LIST    | 623158   |
| ANRV ELIG AMIS LIST   | 623158   |
| ANRV EYE DIAG LIST    | 623158   |
| ANRV EYE DIAG NAR     | 623158   |
| ANRV EYE DIAG PRINT   | 623158   |
| ANRV FEE PT           | 623158   |
| ANRV INC AMIS         | 623158   |
| ANRV MAIL LABELS      | 623158   |
| ANRV ML BY CITY       | 623158   |
| ANRV ML BY COUNTY     | 623158   |
| ANRV ML BY STATE      | 623158   |
| ANRV POS LIST         | 623158   |
| ANRV REFERRAL LIST    | 623158   |
| ANRV STATE LIST       | 623158   |
| ANRV ZIP CODE LIST    | 623158   |

|                   |          |
|-------------------|----------|
| Sort (cont’d) | File |
| ANRVACP           | 623036   |
| ANRVAD            | 623158   |
| ANRVAP            | 623158   |
| ANRVED            | 623158   |
| ANRVFVD           | 623158   |
| ANRVID            | 623158   |
| ANRVPR            | 623160   |
| ANRVREV1          | 623158   |
| ANRVRP1           | 623158   |
| ANRVRRL           | 623160   |

## Routines to Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ANRVPRE, ANRVPST, ANRVZ\*, and ANRV1\* routines will be deleted.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires the 10 files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

> The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use VA FileMan option *List File Attributes* \[DILIST\]*,* under *Data Dictionary Utilities* \[DI DDU\], to print the DDs. The following are the files for which you should print DDs:

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

-------------------------------------------------------------------------------

2040 VIST ROSTER YES NO NO

2041 VIST PARAMETERS YES NO NO

2041.5 VIST EYE DIAGNOSIS YES NO YES MERG NO NO

2041.6 VIST CHECKLIST OPTIONS YES NO YES MERG NO NO

2041.7 VIST BENEFITS AND SERVICES YES NO NO

CHECKLIST

2042 VIST REFERRAL FACILITY YES NO YES MERG NO NO

2042.5 VIST REFERRAL ROSTER YES NO NO

2043 VIST LETTER YES NO YES MERG NO NO

2043.5 VARO CLAIMS YES NO NO

2044 VIST LOCAL BENEFITS AND YES NO YES MERG NO NO

SERVICES

The namespace for the VIST package is ANRV.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of routines you will see for VIST when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (*First Line Routine Print*) to print a list of just the first line of each ANRV\* routine.

|          |         |         |         |          |
|----------|---------|---------|---------|----------|
| ANRVAM1  | ANRVAM2 | ANRVAP  | ANRVDEL | ANRVLET  |
| ANRVML   | ANRVML1 | ANRVML2 | ANRVML3 | ANRVML4  |
| ANRVPOST | ANRVPR  | ANRVPR1 | ANRVPR2 | ANRVRP   |
| ANRVRP2  | ANRVRP3 | ANRVRP4 | ANRVRP5 | ANRVRP6  |
| ANRVRP7  | ANRVRP8 | ANRVRP9 | ANRVRRL | ANRVSITE |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIST Coordinator may be assigned the VIST Menu option as the primary menu option.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are *no* security keys for the VIST software package.

## Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the “Software Product Security” section of this manual.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At present, the Visual Impairment Service Team software does not provide archiving and purging capabilities.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Entry points provided by the VIST package to other packages can be found in the External Relations section of this manual. No other routines are designated as callable from outside of this package.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no external interfaces.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following software is not included in this package and must be installed before this version of Visual Impairment Service Team is completely functional.

> <u>Package</u> <u>Minimum Version Needed</u>

> VA FileMan 21.0

> Kernel 8.0

> Patient Information

> Management System (PIMS) 5.3

> Fee Basis 3.5

## Data Base Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Visual Impairment Service Team (VIST) V. 4.0 has Data Base Integration Agreements (DBIAs) with the packages listed above. For complete information regarding the DBIA for VIST V. 4.0, please refer to the *DBA* \[DBA\] menu option on FORUM and then the *Integration AgreementMenu* \[DBA IA ISC\].

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the options in this package can be invoked independently.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no package-wide variables.

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                     |        |
|---------------------|--------|
| Sort                | File   |
| ANRV AGE LIST       | 2040   |
| ANRV BIRTH LIST     | 2040   |
| ANRV DECEASED LIST  | 2040   |
| ANRV ELIG AMIS LIST | 2040   |
| ANRV EYE DIAG NAR   | 2040   |
| ANRV EYE DIAG PRINT | 2040   |
| ANRV FEE PT         | 2040   |
| ANRV INC AMIS       | 2040   |
| ANRV REFERRAL LIST  | 2040   |
| ANRVAD              | 2040   |
| ANVRED              | 2040   |
| ANRVDFVD            | 2040   |
| ANRVID              | 2040   |
| ANRVREV1            | 2040   |
| ANRVRRL             | 2042.5 |
|                     |        |
| Input               | File   |
| ANRV EDIT CHECKLIST | 2041.7 |
| ANRV EDIT LETTER    | 2043   |
| ANRV PARAM EDIT     | 2041   |
| ANRV VIST PARM      | 2041   |
| ANRVACE             | 2043.5 |
| ANRVEID             | 2040   |
| ANRVRE              | 2040   |
| ANRVRRE             | 2042.5 |

|                     |        |
|---------------------|--------|
| Print               | File   |
| ANRV AGE LIST       | 2040   |
| ANRV BIRTH LIST     | 2040   |
| ANRV CHECKLIST      | 2041.7 |
| ANRV CLAIM REC INQ  | 2043.5 |
| ANRV DECEASED LIST  | 2040   |
| ANRV ELIG AMIS LIST | 2040   |
| ANRV EYE DIAG INQ   | 2040   |
| ANRV EYE DIAG NAR   | 2040   |
| ANRV EYE DIAG PRINT | 2040   |
| ANRV FEE PT         | 2040   |
| ANRV INC AMIS       | 2040   |
| ANRV REFERRAL LIST  | 2040   |
| ANRV REVIEW INQ     | 2040   |
| ANRV ROSTER A/R     | 2040   |
| ANRVAD              | 2040   |
| ANRVED              | 2040   |
| ANRVFVD             | 2040   |
| ANRVID              | 2040   |
| ANRVPR              | 2042.5 |
| ANRVREV             | 2040   |
| ANRVRRL             | 2042.5 |

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIST Coordinator may be assigned the VIST Menu option as the primary menu option.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are *no* security keys for the VIST software package.

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIST Menu

1 Edit VIST Options Menu ... \[ANRV EDIT VIST OPTIONS\]

> 1 Enter/Edit VIST Patient Record \[ANRV ENTER/EDIT VIST PATIENT\]

> 2 Enter/Edit VIST Referral Roster \[ANRV ENTER/EDIT REFERRAL\]

> 3 Enter/Edit Inactive VIST Roster\] \[ANRV ENTER/EDIT INACTIVE VIST\]

> 4 Enter/Edit VARO Claims Roster\] \[ANRV ENTER/EDIT VARO CLAIMS

> 5 Enter/Edit VIST Benefits Checklist \[ANRV ENTER/EDIT CHECKLIST

6.  Enter/Edit VIST Parameters \[ANRV ENTER/EDIT VIST PARAMETER\]
7.  Delete VIST Referral Roster \[ANRV DELETE REFERRAL\]
8.  Delete VIST Patient Record \[ANRV DELETE ROSTER\]

2 Print Individual Records... \[ANRV INDIVIDUAL RECORDS\]

> 1 Individual Patient Record \[ANRV PRINT PATIENT RECORD\]

> 2 Individual Referral Record \[ANRV PRINT IND. REFERRAL\]

> 3 Individual Eye History \[ANRV INDIVIDUAL EYE DIAG\]

> 4 Individual Claims Record \[ANRV CLAIM REC INQ\]

> 5 Individual Annual Review Record \[ANRV ANNUAL REVIEW INQ\]

> 6 Individual VIST Benefits Checklist \[ANRV CHECKLIST INQ\]

3 Print VIST Roster Menu... \[ANRV PRINT VIST OPTIONS\]

> 1 VIST Roster List \[ANRV VIST ROSTER PRINT\]

> 2 VIST Referral Roster List \[ANRV REFERRAL PRINT\]

> 3 VIST Roster List With Annual Review Date \[ANRV ROSTER A/R PRINT\]

> 4 VARO Claims List \[ANRV PRINT VARO CLAIMS\]

> 5 Inpatient List \[ANRV INPATIENT LIST\]

> 6 Outpatient Appointment List \[ANRV OUTPATIENT APPT. LIST\]

> 7 Deceased Patients List \[ANRV DECEASED PATIENTS\]

> 8 Inactive VIST Roster List \[ANRV PRINT INACTIVE VIST\]

> 9 Additions to VIST Roster \[ANRV ADD TO VIST ROSTER\]

> 10 Field Visit Dates List \[ANRV FIELD VISIT DATES\]

> 11 VIST Roster Sorts... \[ANRV ROSTER SORTS\]

> 1 State \[ANRV STATE LIST\]

> 2 City \[ANRV CITY LIST\]

> 3 Zip \[ANRV ZIP CODE LIST\]

> 4 County \[ANRV COUNTY LISTING\]

> 5 Address/Phone List \[ANRV ADDRESS LIST\]

> 6 Birthdate \[ANRV BIRTH LIST\]

> 7 Age \[ANRV AGE LIST\]

> 8 Eye Diagnosis \[ANRV EYE DIAG PRINT\]

> 9 Eye Diagnosis Narrative \[ANRV EYE DIAG NARRATIVE\]

> 10 Fee Basis List \[ANRV FEE PT\]

> 11 Period of Service \[ANRV POS LIST\]

> 12 Referral Source List \[ANRV REFERRAL SOURCE LIST\]

> 13 Annual Review Dates List \[ANRV ANNUAL REVIEW LIST\]

> 14 VIST Eligible (AMIS) List ANRV VIST ELIG LIST\]

> 12 AMIS Report \[ANRV AMIS REPORT\]

13. Incomplete AMIS Roster \[ANRV INCOMPLETE AMIS LISTING

4 VIST Letter Menu... \[ANRV LETTER MENU\]

> 1 Edit VIST Letter \[ANRV ENTER/EDIT VIST LETTER\]

> 2 Print VIST Letter \[ANRV PRINT LETTER\]

> 3 Test Label Alignment \[ANRV TEST LABEL\]

> 4 Print Mailing Labels by Patient \[ANRV MAIL LABELS\]

> 5 Print Mailing Labels by City \[ANRV LABELS BY CITY\]

> 6 Print Mailing Labels by County \[ANRV LABELS BY COUNTY\]

> 7 Print Mailing Labels by State \[ANRV LABELS BY STATE\]

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>File</strong></p>
<p><strong>Numbers</strong></p></td>
<td><strong>File Names</strong></td>
<td><strong>DD</strong></td>
<td><strong>RD</strong></td>
<td><strong>WR</strong></td>
<td><strong>DEL</strong></td>
<td><strong>LAYGO</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2040</td>
<td>VIST ROSTER</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2041</td>
<td>VIST PARAMETERS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2041.5</td>
<td>VIST EYE DIAGNOSIS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2041.6</td>
<td>VIST CHECKLIST OPTIONS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2041.7</td>
<td><p>VIST BENEFITS AND SERVICES</p>
<p>CHECKLIST</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2042</td>
<td>VIST REFERRAL FACILITY</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2042.5</td>
<td>VIST REFERRAL ROSTER</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2043</td>
<td>VIST LETTER</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2043.5</td>
<td>VARO CLAIMS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2044</td>
<td>VIST LOCAL BENEFITS AND SERVICES</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix A: Blind Rehabilitation VIST Patient Review (ANRV 4.0.5.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction to VIST Patient Review Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIST Patient Review software (VIST Patch ANRV, Version 4.0.5.1) collects Blind Rehabilitation data in two (2) interview formats in order to analyze Blind Rehabilitation services. By conducting interviews, the quality of care given to Blind Rehabilitation patients is greatly improved by improving the efficiency of the staff.

The VIST Patient Review application has been developed to improve the Blind Rehabilitation data collection process as well as to address VA Directive 2000-16 and VA Circular 96-057. In an effort to implement a user-friendly data collection environment, VIST Patient Review has been developed as a Graphical User Interface (GUI). Hence, this application is not integrated within VIST Version 4.0, (a roll-and-scroll application). However, it will be interfaced with Blind Rehabilitation Version 5.0, upon its release.

This patch provides an installation executable that is used in conjunction with the KIDS build to provide the user with a GUI environment that must be installed on the client's machine or as a shortcut on a server.

It is recommended that software is initially installed and tested in test accounts before installation in production accounts.

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Systems must have:

- RPC Broker, version 1.1.0.1. and above, Client Agent installed.
- Windows NT (Service Pack 2 & above) or 2000 installed.
- For text to speech interpretations, the system must have the Job Access With Speech (JAWS) software Version 4.0 default installation installed.

> This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 3 minutes.

### Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the VIST Patient Review ANRV patch utilizes a different environment than the VIST 4.0 application (VIST Patient Review is GUI and VIST 4.0 is Roll and Scroll), noting added features in this document is not appropriate. Instead, this section describes key GUI features made available by this application:

- Improved speed of entering and accessing patient data.
- Ability to navigate through application with a mouse or a keyboard.
- Allows text to voice interpretation for visually impaired users. This feature is available in conjunction with the install of the JAWS software package version 4.0, using the default installation configurations.
- Allows users flexibility in asking patients questions and reviewing answers.
- Introduces visually impaired patients to a Graphical User Interface (GUI) environment and JAWS text to voice software.
- Displays alerts for Restricted Access patient files, multiple matches to patient file searches and invalid electronic signature submissions.
- Tracks data entry authorization, by validating an electronic signature upon completion.

### Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following software and files, are exported as part of this patch:

> <u>File Name Contents Retrieval Format</u>

ANRV_4_0_5.KID KIDS Build ASCII

ANRV_4_0_5.ZIP File(s) indented below Binary

-SETUP.EXE VIST Patient Review Setup Executable

> (The SETUP.EXE is an installation program that is used to install the following files within the installation directory selected by executing the SETUP.EXE executable.)

\<INSTALLDIR\>

> \- ANRV.EXE Executable

\- ANRV.CNT Help CNT File

> \- ANRV.HLP Help File

> \<INSTALLDIR\>\DOCUMENTATION

> \- VIST_4_UM.DOC User Manual (Word Document)

> \- VIST_4_UM.PDF User Manual (Adobe Acrobat Document)

> \- VISTOUTCOMEREFGUIDE.DOC Quick Reference (Word Document)

> \- VISTOUTCOMEREFGUIDE.PDF Quick Reference (Adobe Acrobat

> Document)

> \- VISTOUTCOMERELEASENOTES.DOC Release Notes (Word

> Document)

> \- VISTOUTCOMERELEASENOTES.PDF Release Notes (Adobe Acrobat Document)

The files listed above may be obtained via FTP. The preferred method is to FTP the files from:

> [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

This transmits the files from the first available FTP server. Sites may also elect to retrieve software from a specific server as follows:

> <u>OIFO FTP Address Directory</u>

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of the files exported with this software.

- ANRV PATIENT REVIEW File (#2048)
- ANRV PATIENT REVIEW SECTIONS file (#2048.1)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are included with this software.

|        |                                     |
|--------|-------------------------------------|
| ANRVOA | User and Patient specifics          |
| ANRVOB | Patient Review specifics            |
| ANRVOP | Patient Review Parameter Definition |

## Data Dictionary Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following globals are used in this software.

|             |                           |
|-------------|---------------------------|
| ANRV 2048   | ANRV GUI Outcome          |
| ANRV 2048.1 | ANRV GUI Outcome Sections |

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ANRV Patient Review option is used by the GUI application to create context through the RPC Broker connection.

The ANRV Patient Review option is assigned to GUI Application Users.

## RPC Broker Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following RPC Broker calls are associated with the ANRV Patient Review option.

- ANRV CREATE OUTCOME
- ANRV GET OUTCOME TEXT
- ANRV GET PT OUTCOMES
- ANRV GET PTALL
- ANRV GET PTLAST5
- ANRV PTINFO CORE
- ANRV OUTCOME SECTION TEXT
- ANRV TANRVMESSAGE
- ANRV SET RECORD STATUS
- ANRV TANRVPATIENT
- ANRV GUI PARAMETER
- ANRV TANRVUSER
- ANRV FULLSSN

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

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Archiving and Purging · 6
C
Callable Routines · 6
D
DBIA Agreements · 7
E
External Interfaces · 7
External Relations · 7
F
File Security · 13
Files · 5
I
Internal Relations · 7
M
Menu Assignments · 6, 12
Menus · 12
O
Options to be Deleted during Install · 2
P
Package Security · 6
Package-Wide Variables · 7
R
Resource Requirements · 2
S
Security Keys · 6, 12
Security Management · 12
Software Product Security · 11
T
Templates · 8
V
VIST Menu · 12
