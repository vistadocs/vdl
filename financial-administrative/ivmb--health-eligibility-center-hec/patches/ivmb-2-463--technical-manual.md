---
title: IVMB*2*463 Error Processing Phase 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Error Processing Phase 1
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*463
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - error
  - processing
  - aycbep
  - phase
  - software
  - routines
  - security
  - class
page_count: 0
word_count: 3043
section_count: 23
table_count: 11
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p463_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p463_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-463-error-processing-phase-1-technical-manual/001.png)

Error Processing Phase 1

Health eligibility center (HEC)

TECHNICAL Manual

Patch IVMB\*2\*463

May 2001

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
    - [User Groups](#user-groups)
    - [Purge Parameter](#purge-parameter)
- [Files](#files)
  - [File List](#file-list)
  - [File Flow (Relationships Between Files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
    - [List Templates](#list-templates)
- [Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Routine List](#routine-list)
- [Exported Options](#exported-options)
  - [Menu Diagram](#menu-diagram)
  - [Server Options](#server-options)
  - [Exported Protocols](#exported-protocols)
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

The Health Eligibility Center (HEC) system sends eligibility data, enrollment data, income data, and means test data to the local VA Medical Centers (VAMCs) using HL7 messaging. Eligibility, enrollment, and income data are sent via a Z11 HL7 transmission; means test data via a Z10 HL7 transmission. In the event that a local VAMC is unable to process the information received, it will notify the HEC of a problem. This notification is transmitted via an Application Error (AE) message.

The HEC performs its own error checking to prevent bad data from being sent to the VAMC where it will be rejected and sent back to the HEC as an application error message. This error checking process notifies the HEC of the problem via a Consistency Check (CC) message. Previously, both the AE and CC messages were transmitted via a bulletin to various users at the HEC. Some of these error messages can be corrected through a manual correction at the HEC; the patient record must then be re-queued to be transmitted to the VAMC.

The Error Processing Tool was created to easily correct the inaccurate data, send the updated data to the VAMC, and keep track of the progress of the error correction process. It allows users to review the errors, exchange messages with VAMC personnel regarding the resolution of the data discrepancy, queue a transmission to be sent to the VAMC, and make corrections at the HEC, if necessary.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of Patch IVMB\*2\*463 is to provide an error processing tool that allows users at the HEC to

- Easily correct inaccurate data at the HEC
- Send updated data to the VAMC
- Track the progress of the error correction process
- Review errors
- Exchange messages with VAMC personnel regarding the resolution of the data discrepancy
- Queue a transmission to be sent to the VAMC

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals will also be released with the Error Processing Phase 1 software.

- Error Processing Phase 1 Installation Guide
- Error Processing Phase 1 User Manual

You can download the Error Processing Phase 1 documentation as follows:

From the Anonymous Directory

1.  Go to the anonymous.software directory.
2.  Ftp the files listed in the following table. Remember to use binary format.

|                      |                             |
|----------------------|-----------------------------|
| File Name        | Documentation Component |
| IVMB_p463_hec_um.pdf | User Manual                 |
| IVMB_p463_hec_tm.pdf | Technical Manual            |
| IVMB_p463_hec_ig.pdf | Installation Guide          |

From the Project Notebook Web Page

REDACTED

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users must be defined in the new option, Error Processing User Group, in order to have access to the Error Processing Tool software.

Please see the Error Processing Phase 1 Installation Guide for information about installing and implementing the Error Processing Phase 1 software.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Processing User Group option allows error messages to be assigned to a class of users instead of being assigned to an individual user. This option allows supervisors to assign individual users to a user-defined group and to define the sort criteria for displaying the list of error messages displayed in the error processing tool.

It is very important to accurately maintain user group membership. A user must be defined in at least one user group to be able to access the Error Processing Tool software.

### Purge Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Error Message Purge Parameter option to define the number of days that errors with a status of CLOSED or DELETE remain in the Error Message Log File before being purged.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are exported with Patch IVMB\*2\*463.

|             |                            |                                                                                                                                                                                                                                                                                    |                |
|-------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| File \# | File Name              | Description                                                                                                                                                                                                                                                                    | Global     |
| 742080      | HEC ERROR PROCESSING LOG   | Tracks the progress of an error message in the HEC. The information captured by this log will be used for managerial reports. This file will be accessed on a daily basis, recording when errors are received at the HEC and their status updates until they are finally resolved. | ^IVMGA(742080, |
| 742081      | HEC ERROR PROCESSING GROUP | Stores the user group name and user name. After the initial definition, this file should require very little maintenance. It will be used to identify potential user groups that may be assigned responsibility for error processing.                                              | ^IVMGA(742081, |
| 742082      | HEC ERROR PROCESSING USER  | Stores user name and staff position (supervisor or contact representative), and sort order.                                                                                                                                                                                        | ^IVMGA(742082, |

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

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- AYCBEP ERROR PROCESSING; Menu ; This screen is used as the main entry point for the tool.
- AYCBEP2; Display ; This screen is used only to display a list of errors that exist in a single patient's file.
- AYCBEV VIEW ERROR DETAIL; Protocol ; Used to view the details of a single error, this screen also is used as the entry point for the Entry/Edit protocol.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines in the Error Processing Phase 1 software do not require mapping.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines in the Error Processing Phase 1 software.

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of IVM routines with checksums included in the Error Processing Phase 1 software. The second line of each of these routine(s) will look like:

\<tab\>;;2.0;INCOME VERIFICATION;\*\*\[patch list\]\*\*;JULY 18,2000

|                  |                  |                 |                |           |
|------------------|------------------|-----------------|----------------|-----------|
| Routine Name | Before Patch | After Patch | Patch List | Bytes |
| AYCBCMN          | 13446952         | 13460226        | 277, 463       | 8835      |
| AYCBEF           | N/A              | 335933          | 463            | 532       |
| AYCBEP           | N/A              | 22790628        | 463            | 4700      |
| AYCBEPD          | N/A              | 839471          | 463            | 1233      |
| AYCBEPG          | N/A              | 10157801        | 463            | 8613      |
| AYCBEPL1         | N/A              | 17344797        | 463            | 9730      |
| AYCBEPL2         | N/A              | 18481998        | 463            | 9484      |
| AYCBEPL3         | N/A              | 21031008        | 463            | 8500      |
| AYCBEPL5         | N/A              | 11198538        | 463            | 3562      |
| AYCBEPP          | N/A              | 1440007         | 463            | 1343      |
| AYCBEPR          | N/A              | 7524951         | 463            | 4943      |
| AYCBEPR1         | N/A              | 13535403        | 463            | 9972      |
| AYCBEPR2         | N/A              | 15465369        | 463            | 7882      |
| AYCBEPR3         | N/A              | 6347237         | 463            | 5305      |
| AYCBEPR4         | N/A              | 6929883         | 463            | 5262      |
| AYCBEPR5         | N/A              | 3137442         | 463            | 2733      |
| AYCBEPS1         | N/A              | 7840139         | 463            | 6104      |
| AYCBEP2          | N/A              | 4957248         | 463            | 4054      |
| AYCBEV           | N/A              | 5494529         | 463            | 3490      |
| IVMB463P         | N/A              | 2671015         | 463            | 2114      |

The following is a list of the VIVA routines with checksums included in the Error Processing Phase 1 software. The second line of each of these routines will look like:

\<tab\>;;1.0;VIVA;\*\*\[patch list\]\*\*;MAY 25, 1994

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Before Patch</strong></td>
<td><strong>After Patch</strong></td>
<td><strong>Patch List</strong></td>
<td><strong>Bytes</strong></td>
</tr>
<tr class="even">
<td>IVMBACK1</td>
<td>18384034</td>
<td>19882209</td>
<td><p>173, 196, 208, 233, 412,</p>
<p>463</p></td>
<td>9859</td>
</tr>
<tr class="odd">
<td>IVMEVI1</td>
<td>11759731</td>
<td>13164980</td>
<td>166, 30, 256, 292, 463</td>
<td>7419</td>
</tr>
<tr class="even">
<td>AYCBTBTO</td>
<td>7258902</td>
<td>7616983</td>
<td>277, 392, 397, 414, 463</td>
<td>9820</td>
</tr>
<tr class="odd">
<td>AYCBTBT1</td>
<td>7391115</td>
<td>7586253</td>
<td><p>277, 392, 397, 414, 412,</p>
<p>463</p></td>
<td>9992</td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Processing Tool (AYCB ERROR PROCESSING TOOL)

\|

\|

----1 Error Processing Menu

\[AYCB ERROR PROCESSING MENU\]

----2 Error Processing Reports

\[AYCB ERROR PROCESSING REPORTS\]

----3 Error Message Purge Parameters

\[AYCB ERROR MESSAGE PURGE PARAMETERS\]

----4 Error Processing User Group

\[AYCB ERROR PROCESSING USER GROUP\]

## Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AYCBEP ERROR LOG SERVER..........Error Processing Server

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are exported with the Error Processing Phase 1 software:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 22%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Protocol Name</th>
<th>Associated Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AYCBEP MENU</td>
<td>Menu</td>
<td><p>Set to Menu. Contains the following protocols:</p>
<ul>
<li><p>AYCBEP DATE RANGE</p></li>
<li><p>AYCBEP SORT</p></li>
<li><p>AYCBEP RETRANSMIT</p></li>
<li><p>AYCBEP FIND PATIENT</p></li>
<li><p>AYCBEP ASSIGN STAFF</p></li>
<li><p>AYCBEP MAIL</p></li>
<li><p>AYCBEP UPDATE STATUS</p></li>
<li><p>AYCBEP VIEW ERROR</p></li>
<li><p>AYCBEP ENTER/EDIT</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AYCBEP DATE RANGE</td>
<td>Change Date Range</td>
<td>Used to create a new list of errors within a user-supplied date range.</td>
</tr>
<tr class="odd">
<td>AYCBEP SORT</td>
<td>Sort List</td>
<td>Displays the existing list of errors in a different order according to a User selected sort order. The sort options are Assigned To, Date/Time, Patient Name, Error Text, Station Logging Error, and Error Status.</td>
</tr>
<tr class="even">
<td>AYCBEP RETRANSMIT</td>
<td>Retransmit Patient File</td>
<td>Flags the appropriate files which causes the chosen patient's file to be retransmitted to the site(s) that the patient has visited.</td>
</tr>
<tr class="odd">
<td>AYCBEP FIND PATIENT</td>
<td>Check Errors</td>
<td>Used to view a new list composed of all of the errors associated with a selected patient.</td>
</tr>
<tr class="even">
<td>AYCBEP ASSIGN STAFF</td>
<td>Assign Staff</td>
<td>Used to assign errors to individual users or a group of users for repair of faulty data.</td>
</tr>
<tr class="odd">
<td>AYCBEP MAIL</td>
<td>Mail Message</td>
<td>Invokes the VA MailMan messaging system.</td>
</tr>
<tr class="even">
<td>AYCBEP UPDATE STATUS</td>
<td>Update Error Status</td>
<td>Used to change the status of an error.</td>
</tr>
<tr class="odd">
<td>AYCBEP VIEW ERROR</td>
<td>View Error Detail</td>
<td><p>Displays a new list composed of the details associated with a single error. It will also have a Menu setting, and contain the following protocols:</p>
<ul>
<li><p>AYCBEP RETRANSMIT</p></li>
<li><p>AYCBEP FIND PATIENT</p></li>
<li><p>AYCBEP ASSIGN STAFF</p></li>
<li><p>AYCBEP MAIL</p></li>
<li><p>AYCBEP UPDATE STATUS</p></li>
<li><p>AYCBEP VIEW ERROR</p></li>
<li><p>AYCBEP ENTER/EDIT</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AYCBEP ENTER/EDIT</td>
<td>Enter/Edit VIVA Data</td>
<td>Entered only through the view error screen. Allows the user to modify VIVA data, then transmit the file to the appropriate site(s).</td>
</tr>
</tbody>
</table>

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving capabilities exported with the Error Processing Phase 1 software.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option \[AYCB EDIT PURGE DATE\] allows users to define the number of days that errors with a status of CLOSED or DELETE remain in the Error Message Log File before being purged.

# Callable Routines/Entry Points/Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines, entry points or APIs that can be called by other products. Any of the APIs called are existing routines.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 messaging has been altered slightly. Previously, when an AE was created, the system would put an entry of the error, along with several pieces of information, into the global ^XMB(3.9. The system would then send a mail message through MailMan to a pre-defined group at the HEC informing them that an error was received from V*IST*A associated with the ENROLLMENT File (#300.132). The same process occurs for the CCs, but through a series of Consistency Checkers. This functionality has be altered slightly. These are the following changes:

- When the error is received, whether an AE or CC, the entry into the ^XMB(3.9 global has been stopped. No entries will be filed.
- No new mail message will be sent to a group or a user when the Error is received.
- When an error message has been fixed (by the user the error was assigned to or by someone else), an HL7 message is sent to notify the user who fixed it that the error was closed or deleted.

# External/ Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*IST*A package versions or higher must be installed prior to installing the Error Processing Phase 1 software:

|                     |                              |
|---------------------|------------------------------|
| Package Name    | Minimum Version Required |
| IVM                 | 2.0                          |
| Kernel              | 8.0                          |
| VA FileMan          | 22.0                         |
| V*IST*A HL7 | 1.6                          |

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no DBIAs associated with the Error Processing Phase 1 software.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Error Processing Tool options have been designed to stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the Error Processing Phase 1 software.

## SACC Exemptions/Non-standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions associated with the Error Processing Phase 1 software.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements associated with the Error Processing Phase 1 software. In accordance with VHA Directive 10-93-142, the files and fields exported with the Error Processing Phase 1 software should not be modified locally.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new mail group, Error Processing Active/Exempt, has been created to receive any errors encountered during the installation of this software and the totals of records created, deleted, or purged.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Eligibility Center (HEC) system sends eligibility data, enrollment data, income data, and means test data to the local VA Medical Centers (VAMCs) using HL7 messaging. Eligibility, enrollment, and income data are sent via a Z11 HL7 transmission; means test data via a Z10 HL7 transmission. In the event that a local VAMC is unable to process the information received, it will notify the HEC of a problem. This notification is transmitted via an Application Error (AE) message.

The HEC performs its own error checking to prevent bad data from being sent to the VAMC where it will be rejected and sent back to the HEC as an application error message. This error checking process notifies the HEC of the problem via a Consistency Check (CC) message. Previously, both the AE and CC messages were transmitted via a bulletin to various users at the HEC. Some of these error messages can be corrected through a manual correction at the HEC; the patient record must then be re-queued to be transmitted to the VAMC.

The Error Processing Tool was created to easily correct the inaccurate data, send the updated data to the VAMC, and keep track of the progress of the error correction process. It allows users to review the errors, exchange messages with VAMC personnel regarding the resolution of the data discrepancy, queue a transmission to be sent to the VAMC, and make corrections at the HEC, if necessary.

### Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Archiving and Purging section of this manual.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using services should have a local contingency plan to be used in the event of application problems in a live environment. The plan should identify the procedure(s) for maintaining the functionality provided by Error Processing Phase 1 software in the event of system outage. Field Station Information Security Officers (ISOs) can get assistance from the regional ISO (RISO).

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized products embedded within or required by the Error Processing Phase 1 software.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Processing Phase 1 software does not use electronic signatures.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new or existing menu options that would warrant warnings about sensitive patient data being displayed when using any of the Error Processing Menu options.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contact Representatives are limited to the menu options that are available. These limitations will be accomplished by Security Keys. The security keys needed will be set up on the following menu options:

2 Error Processing Reports

3 Error Processing Purge Parameters

4 Error Processing User Group

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of recommended VA FileMan access codes for the files in the Error Processing Phase 1 software:

|             |                                 |     |     |     |     |       |       |
|-------------|---------------------------------|-----|-----|-----|-----|-------|-------|
| File Number | File Name                       | DD  | RD  | WR  | DEL | LAYGO | AUDIT |
| 742080      | HEC ERROR PROCESSING LOG FILE   | @   | @   | @   | @   | @     | @     |
| 742081      | HEC ERROR PROCESSING GROUP FILE | @   | @   | @   | @   | @     | @     |
| 742082      | HEC ERROR PROCESSING USER FILE  | @   | @   | @   | @   | @     | @     |

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In accordance with VHA Directive 10-93-142, the files and fields exported with the Error Processing Phase 1 software should not be modified locally.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym     | Description                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| AE              | Application Error                                                                                             |
| CC              | Consistency Check                                                                                             |
| HEC             | Health Eligibility Center                                                                                     |
| HL7             | Health Level Seven                                                                                            |
| IEN             | Internal Entry Number                                                                                         |
| SDD             | Software Design Description                                                                                   |
| SRS             | Software Requirements Specification                                                                           |
| SSN             | Social Security Number                                                                                        |
| VA              | Veterans Affairs                                                                                              |
| VAMC            | Veterans Affairs Medical Center                                                                               |
| VHA             | Veterans Health Administration                                                                                |
| V*IST*A | Veterans Health Information Systems and Technology Architecture                                               |
| VIVA            | Veterans Identification & Verification Access                                                                 |
| Z10             | HL7 transmission from the HEC to VAMC site which contains income test data.                                   |
| Z11             | HL7 transmission from the HEC to VAMC site which contains a veteran’s eligibility and enrollment information. |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Archiving and Purging 10
C
Callable Routines 6
Callable Routines/Entry Points/Application Programmer Interfaces (APIs) 11
D
DBIA Agreements 12
E
Exported Options 8
Exported Protocols 8
External Interfaces 11
External Relations 12
External/ Internal Relations 12
F
File Flow (Relationships Between Files) 4
File List 4
Files 4
I
Implementation 3
Implementation and Maintenance 3
Internal Relations 12
Introduction 1
L
List Templates 5
M
Maintenance 3
Menu Diagram 8
O
Overview 1
P
Package-wide Variables 13
Purge Parameter 3
Purpose 1
R
Related Manuals 2
Routine List 6
Routines 6
Routines to Map 6
S
SACC Exemptions/Non-standard Code 13
Security 14
T
Templates 5
U
User Groups 3
