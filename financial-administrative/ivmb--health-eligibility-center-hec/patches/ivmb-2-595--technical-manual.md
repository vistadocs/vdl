---
title: IVMB*2*595 Military Sexual Trauma (MST) Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Military Sexual Trauma (MST)
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*595
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - ivmb
  - patch
  - routines
  - security
  - exported
  - files
  - external
  - archiving
page_count: 0
word_count: 1682
section_count: 21
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p595_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p595_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-595-military-sexual-trauma-mst-technical-manual/001.png)

veterans millennium health care and benefits act

military sexual trauma (MST)

Health eligibility center (HEC)

TECHNICAL Manual

Patch IVMB\*2\*595

February 2002

V*IST*A System Design & Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Related Manuals](#related-manuals)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
  - [Maintenance](#maintenance)
- [Files](#files)
  - [File List](#file-list)
  - [File Flow (Relationships Between Files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
- [Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Routine List](#routine-list)
- [Exported Options](#exported-options)
  - [Menu Diagram](#menu-diagram)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines/Entry Points/Application Programmer Interfaces (APIs)](#callable-routinesentry-pointsapplication-programmer-interfaces-apis)
- [External Interfaces](#external-interfaces)
- [External/ Internal Relations](#external-internal-relations)
  - [External Relations](#external-relations)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
  - [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
  - [SACC Exemptions/Non-standard Code](#sacc-exemptionsnon-standard-code)
- [Security](#security)
  - [Security Management](#security-management)
  - [Security Features](#security-features)
    - [Mail Groups and Alerts](#mail-groups-and-alerts)
    - [Remote Systems](#remote-systems)
    - [Archiving and Purging](#archiving-and-purging-1)
    - [Contingency Planning](#contingency-planning)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [References](#references)
    - [Official Policies](#official-policies)
- [Glossary](#glossary)
- [Index](#index)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of the Military Sexual Trauma (MST) portion of the Veterans Millennium Healthcare and Benefits Act, Public Law 106-117, Section 115 (a.k.a. Mill Bill) is to support the screening of veterans for MST, identify non-Veterans Administration workload associated with MST, and to enhance national MST reporting. This effort will impact Fee Basis, Women’s Health (WH), Health Eligibility Center (HEC/Enrollment), Clinician Desktop, Patient Information Management Systems (PIMS), the Corporate Databases, and V*IST*A software packages.

The enhancements will provide a means for identifying non-VA MST workload in the Fee Basis application, clinical reminders to clinicians, and specifications for the VA and non-VA workload reports to be generated at the Austin Automation Center (AAC). Also, PIMS and HEC will manage the MST status sharing between sites to minimize the instances in which a veteran is repeatedly asked about MST status. HEC will act as the authoritative database source.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this technical manual is to provide information to technical users who are responsible for implementing and maintaining the software.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Health Eligibility Center manuals will also be released with Patch IVMB\*2\*595

- Military Sexual Trauma (MST) User Manual

You can download the documentation as follows:

From the Anonymous Directory

1.  Go to the anonymous.software directory.
2.  Ftp the files listed in the following table. Remember to use binary format.

|                    |                             |
|--------------------|-----------------------------|
| File Name      | Documentation Component |
| IVMB_2_p595_um.pdf | User Manual                 |

From the TSPR Project Notebook Web Page

REDACTED

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Important Notice:*

Patch IVMB\*2\*595 should not be installed until

- *AFTER* Patch IVMB\*2\*573 has been installed

> *AND*

- ALL VA Medical Centers (VAMCs) have installed patches DG\*5.3\*379 and IVM\*2.0\*42.

As an added precaution, IVMB\*2\*595 will not be released until ALL VAMCs have installed the patches named above.

Patch IVMB\*2\*595 introduces changes to the Health Eligibility Center (HEC) Enrollment Module needed to support the Veterans Millennium Health Care and Benefits Act, Public Law 106-117 Section 115, and is one of several patches being released as part of the Military Sexual Trauma project. The following lists the necessary patches in the order in which they should be installed:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Install 1st (HEC)</strong></td>
<td><strong>Install 2nd (VAMC)</strong></td>
<td><strong>Install 3rd (HEC)</strong></td>
</tr>
<tr class="even">
<td>IVMB*2*573</td>
<td><p>DG*5.3*379</p>
<p>IVM*2.0*42</p></td>
<td>IVMB*2*595</td>
</tr>
</tbody>
</table>

For detailed installation instructions, please refer to the IVMB\*2\*595 patch description.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Populate the VHA CO MST mail group with staff members who should receive the MST National Report. Only the members of this mail group will receive the output generated by the AYCEMST NATIONAL REPORT menu option.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files are exported with Patch IVMB\*2\*595.

## File Flow (Relationships Between Files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan
2.  Data Dictionary Utilities Menu
3.  List File Attributes option
4.  Enter file number
5.  Select Standard listing format
6.  Select print device

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no templates exported with Patches IVMB\*2\*573 and IVMB\*2\*595.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines to map for Patch IVMB\*2\*595.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines exported with IVMB\*2\*595.

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of IVM routines with checksums included in Patch IVMB\*2\*595. The second line of each of these routine(s) will look like:

\<tab\>;;2.0;INCOME VERIFICATION;\*\*\[patch list\]\*\*;JULY 18,2000

|                  |                  |                 |                                     |
|------------------|------------------|-----------------|-------------------------------------|
| Routine Name | Before Patch | After Patch | Patch List                      |
| AYCBHL7          | 11688377         | 12193742        | 201,212,228,238,277,392,411,491,595 |
| AYCEMSTN         | N/A              | 14384037        | 595                                 |
| AYCEMSTR         | N/A              | 9100581         | 595                                 |
| AYCEZ07M         | 8108933          | 8108186         | 608,632,612,573,595                 |
| IVMB595I         | N/A              | 4238698         | 595                                 |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MST Reports (AYCEMST MST REPORTS)

\*\*LOCKED: IVMD MGT RPT\*\*

\|

\|

----1 MST Inquiry Report

\[AYCEMST INQUIRY REPORT\]

\*\*LOCKED: IVMD MGT RPT\*\*

----2 MST National Report

\[AYCEMST NATIONAL REPORT\]

\*\*LOCKED: IVMD MGT RPT\*\*

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving capabilities exported with Patch IVMB\*2\*595.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no purging capabilities exported with Patch IVMB\*2\*595.

# Callable Routines/Entry Points/Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines, entry points, or APIs associated with Patch IVMB\*2\*595.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no external interfaces associated with Patch IVMB\*2\*595.

# External/ Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*IST*A package versions or higher must be installed prior to installing Patches IVMB\*2\*573 and IVMB\*2\*595:

|                                 |                              |
|---------------------------------|------------------------------|
| Package Name                | Minimum Version Required |
| Income Verification Match (IVM) | 2.0                          |
| Kernel                          | 8.0                          |
| VA FileMan                      | 22.0                         |
| V*IST*A HL7             | 1.6                          |

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no DBIAs associated with Patch IVMB\*2\*595.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the MST options are designed to stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables exported with Patch IVMB\*2\*595.

## SACC Exemptions/Non-standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions exported with Patch IVMB\*2\*595.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements associated with Patch IVMB\*2\*595. In accordance with VHA Directive 10-93-142, the files and fields exported with Patch IVMB\*2\*595 should not be modified locally.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Populate the VHA CO MST mail group with staff members who should receive the MST National Report. Only the members of this mail group will receive the output generated by the AYCEMST NATIONAL REPORT menu option.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MST data will be shared between the HEC and VAMCs via Z07 Full Data Transmission HL7 messages.

### Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging capabilities exported with Patch IVMB\*2\*595.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using services should have a local contingency plan to be used in the event of application problems in a live environment. The plan should identify the procedure(s) for maintaining the functionality provided by the Error Processing Tool software in the event of system outage. Field Station Information Security Officers (ISOs) can get assistance from the regional ISO (RISO).

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized products embedded within or required by Patch IVMB\*2\*595.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IVMB\*2\*595 do not use electronic signatures.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the menu diagrams in the Exported Options section of this manual.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menu options are locked with the IVMD MGT RPT security key:

MST Reports \[AYCEMST MST REPORTS\]

1 MST Inquiry Report \[AYCEMST INQUIRY REPORT\]

2.  MST National Report \[AYCEMST NATIONAL REPORT\]

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files are exported with Patch IVMB\*2\*595.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Millennium Health Care and Benefits Act, Public Law 106-117, Section 115

### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In accordance with VHA Directive 10-93-142, the files and fields exported with Patch IVMB\*2\*595 should not be modified locally.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym         | Description                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| HEC             | Health Eligibility Center                                                                                     |
| HL7             | Health Level Seven                                                                                            |
| IVMB            | Package namespace used for HEC software development                                                           |
| VA              | Veterans Affairs                                                                                              |
| VAMC            | Veterans Affairs Medical Center                                                                               |
| VHA             | Veterans Health Administration                                                                                |
| V*IST*A | Veterans Health Information Systems and Technology Architecture                                               |
| MST             | Military Sexual Trauma                                                                                        |
| Mill Bill       | Veterans Millennium Health Care and Benefits Act, Public Law 106-117, Section 115                             |
| PIMS            | Patient Information Management System                                                                         |
| Z07             | HL7 full data transmission                                                                                    |
| Z11             | HL7 transmission from the HEC to VAMC site which contains a veteran’s eligibility and enrollment information. |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Archiving and Purging 5
C
Callable Routines 4
Callable Routines/Entry Points/Application Programmer Interfaces (APIs) 5
D
DBIA Agreements 6
E
Exported Options 5
External Interfaces 5
External Relations 6
External/ Internal Relations 6
F
File Flow (Relationships Between Files) 3
File List 3
Files 3
I
Implementation 2
Implementation and Maintenance 2
Internal Relations 6
Introduction 1
M
Maintenance 2
Menu Diagram 5
O
Overview 1
P
Package-wide Variables 7
Purpose 1
R
Related Manuals 1
Routine List 4
Routines 4
Routines to Map 4
S
SACC Exemptions/Non-standard Code 7
Security 8
T
Templates 3
