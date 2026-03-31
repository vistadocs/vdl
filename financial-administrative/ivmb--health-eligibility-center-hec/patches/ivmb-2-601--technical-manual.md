---
title: IVMB*2*601 Error Processing Phase 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Error Processing Phase 2
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*601
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
  - tool
  - blockquote
  - aycbep
  - software
  - routines
  - security
page_count: 0
word_count: 2827
section_count: 22
table_count: 20
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p601_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p601_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-601-error-processing-phase-2-technical-manual/001.png)

Error Processing Tool

Health eligibility center (HEC)

draft TECHNICAL Manual

Patch IVMB\*2\*601

November 2001

V*IST*A System Design & Development

Table of Contents

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Overview](#overview)
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
|                   |                                                     |            |
|-------------------|-----------------------------------------------------|------------|
| Revision Date | Description                                     | Author |
| 5/18/2001         | Initial Version                                     | REDACTED   |
| 1/22/2002         | Updated to include Patch IVMB\*2\*601 functionality | REDACTED   |
| 1/28/2002         | Updated title page, footers, introduction           | REDACTED   |
| 3/19/02           | Updated Introduction section                        | REDACTED   |
|                   |                                                     |            |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 1 of the Error Processing Tool project created a file in which both Application Error (AE) and Consistency Check (CC) error messages were filed. Software was developed to allow processing of the CC errors: to easily correct the inaccurate data, send the updated data to the VA Medical Centers (VAMCs), and track the progress of the error correction process.

Phase 2 of the Error Processing Tool project adds the processing of Review File cases to the tool created in Phase 1. This is possible because the procedures to correct the Review File cases are similar to those processes used to correct the CC errors, and this software more closely meets the needs of the users than the current Review File software.

Entries are filed into the Review File when the solicited or unsolicited Z11 HL7 messages from the Austin Automation Center (AAC) are received at the Health Eligibility Center (HEC), and the data in the message is found to have some type of inconsistency with the data on file at the HEC. This data must be evaluated to determine if it should be uploaded into the HEC system.

Patch IVMB\*2\*601 merges the Consistency Check errors and Application Errors from the HEC ERROR PROCESSING LOG File \#742080 (old) into the HEC ERROR PROCESSING PROJECT File \#742085 (new), and applies the needed modifications to the tool to incorporate the Review File errors.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals will also be released with Patch IVMB\*2\*601:

- Error Processing Tool Release Notes
- Error Processing Tool User Manual

You can download the Error Processing Tool documentation as follows:

From the Anonymous Directory

1.  Go to the anonymous.software directory.
2.  Ftp the files listed in the following table. Remember to use binary format.

|                      |                             |
|----------------------|-----------------------------|
| File Name        | Documentation Component |
| IVMB_p601_hec_um.pdf | User Manual                 |
| IVMB_p601_hec_rn.pdf | Release Notes               |

From the Project Notebook Web Page

REDACTED

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users must be defined in a user group in order to access the Error Processing Tool software. Supervisors must assign members to user groups using the Error Processing User Group menu option.

For detailed installation instructions, refer to the IVMB\*2\*601 patch description in the Patch Module.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Processing User Group option allows error messages to be assigned to a class of users instead of being assigned to an individual user. It also allows supervisors to assign individual users to a user-defined group and to define the sort criteria for displaying the list of error messages displayed in the error processing tool.

It is very important to accurately maintain user group membership. A user must be defined in at least one user group to be able to access the Error Processing Tool software.

### Purge Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Error Message Purge Parameter option to define the number of days that errors with a status of CLOSED or DELETE remain in the HEC ERROR PROCESSING LOG File (#742085) before being purged.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are associated with the Error Processing Tool:

|             |                              |                                                                                                                                                                                                                                                                                    |                |
|-------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| File \# | File Name                | Description                                                                                                                                                                                                                                                                    | Global     |
| 742080      | HEC ERROR PROCESSING LOG     | Tracks the progress of an error message in the HEC. The information captured by this log will be used for managerial reports. This file will be accessed on a daily basis, recording when errors are received at the HEC and their status updates until they are finally resolved. | ^IVMGA(742080, |
| 742081      | HEC ERROR PROCESSING GROUP   | Stores the user group name and user name. After the initial definition, this file should require very little maintenance. It will be used to identify potential user groups that may be assigned responsibility for error processing.                                              | ^IVMGA(742081, |
| 742082      | HEC ERROR PROCESSING USER    | Stores user name and staff position (supervisor or contact representative), and sort order.                                                                                                                                                                                        | ^IVMGA(742082, |
| 742085      | HEC ERROR PROCESSING PROJECT | Stores error data                                                                                                                                                                                                                                                                  | ^IVMGA(742085, |

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

|                          |              |                                                                                                                      |
|--------------------------|--------------|----------------------------------------------------------------------------------------------------------------------|
| Routine Name         | Function | Description                                                                                                      |
| AYCBEP ERROR PROCESSING  | Menu         | This screen is used as the main entry point for the tool.                                                            |
| AYCBEP                   | Display      | This screen is used only to display a list of errors that exist in a single patient's file.                          |
| AYCBEV VIEW ERROR DETAIL | Protocol     | Used to view the details of a single error, this screen also is used as the entry point for the Entry/Edit protocol. |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines in the Error Processing Tool software do not require mapping.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines in the Error Processing Tool software.

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the IVM routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;2.0;INCOME VERIFICATION;\*\*\[patch list\]\*\*;May 25, 1994

|                  |                  |                 |                                                                      |           |
|------------------|------------------|-----------------|----------------------------------------------------------------------|-----------|
| Routine Name | Before Patch | After Patch | Patch List                                                       | Bytes |
| AYCBAAC          | 6714728          | 7234340         | 125,146,174,182,184,191,217,190,291,332,356,414,561,601              | 7411      |
| AYCBCMN          | 13903817         | 13903817        | 277,510,455,463,601                                                  | 9271      |
| AYCBDVER         | 4267167          | 2799699         | 125,149,190,280,299,561,601                                          | 3533      |
| AYCBEF           | 335992           | 336001          | 463,601                                                              | 536       |
| AYCBENAV         | 5130603          | 3996759         | 188,195,201,221,190,257,287,295,330,359,392,455,532,601              | 6960      |
| AYCBENR          | 6019986          | 7560158         | 125,142,146,138,149,182,191,201,224,190,308,332,347,356,414, 561,601 | 9385      |
| AYCBEP           | 21433008         | 39389312        | 463,601                                                              | 9164      |
| AYCBEP1          | N/A NEW          | 2305048         | 601                                                                  | 2319      |
| AYCBEP2          | 6778011          | 7788051         | 463,601                                                              | 6725      |
| AYCBEPG          | 10886676         | 11048387        | 463,601                                                              | 9230      |
| AYCBEPL1         | 16186122         | 14028330        | 463,601                                                              | 8943      |
| AYCBEPL2         | 17874376         | 19646739        | 463,601                                                              | 10000     |
| AYCBEPL3         | 18907582         | 18603483        | 463,601                                                              | 9893      |
| AYCBEPL4         | N/A NEW          | 15004252        | 601                                                                  | 9587      |
| AYCBEPL5         | 20460714         | 28630197        | 463,601                                                              | 9768      |
| AYCBEPL6         | N/A NEW          | 4955364         | 601                                                                  | 3018      |
| AYCBEPP          | 1660266          | 1024790         | 463,601                                                              | 1357      |
| AYCBEPR          | 14915725         | 16062006        | 463,601                                                              | 9662      |
| AYCBEPR1         | 13072577         | 12197965        | 463,601                                                              | 8864      |
| AYCBEPR2         | 14646945         | 15689965        | 463,601                                                              | 7801      |
| AYCBEPR3         | 8909791          | 11065896        | 463,601                                                              | 8364      |
| AYCBEPR4         | 7076837          | 12867721        | 463,574,601                                                          | 9433      |
| AYCBEPR5         | 3463967          | 14072031        | 463,601                                                              | 8017      |
| AYCBEPR6         | N/A NEW          | 12016515        | 601                                                                  | 8764      |
| AYCBEPR7         | N/A NEW          | 15811027        | 601                                                                  | 8213      |
| AYCBEPR8         | N/A NEW          | 8861427         | 601                                                                  | 6585      |
| AYCBEPS4         | N/A NEW          | 13834696        | 601                                                                  | 9178      |
| AYCBEPS5         | N/A NEW          | 8003909         | 601                                                                  | 9003      |
| AYCBEPS6         | N/A NEW          | 2751531         | 601                                                                  | 3198      |
| AYCBEV           | 7789071          | 14812705        | 463,601                                                              | 9892      |
| AYCBFLAG         | 6900596          | 8268172         | 125,210,328,561,601                                                  | 6461      |
| AYCBNAME         | 2854969          | 2596147         | 125,165,176,219,255,190,299,601                                      | 3456      |
| AYCBSCAW         | 399864           | 938119          | 146,181,468,601                                                      | 1581      |
| AYCBTAAC         | 7840191          | 10083264        | 125,224,313,332,401,455,561,601                                      | 7443      |
| AYCBTBT1         | 7626309          | 7626494         | 277,392,397,414,412,463,601                                          | 9895      |
| AYCBTBTO         | 7668388          | 7668573         | 277,392,397,414,463,601                                              | 9856      |
| AYCBUTL2         | 5652416          | 5663532         | 248,332,455,601                                                      | 6997      |
| AYCBXREF         | N/A NEW          | 4088247         | 601                                                                  | 3669      |
| AYCBZRD          | 2110368          | 2305223         | 125,146,180,601                                                      | 1328      |
| AYCEPHPT         | 5339525          | 8474295         | 491,535,601                                                          | 6576      |
| IVMB601P         | N/A NEW          | 3930563         | 601                                                                  | 2646      |
| IVMBACK1         | 19658719         | 19723381        | 173,196,208,233,412,463,601                                          | 9891      |

The following is a list of the VIVA routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;1.0;VIVA;\*\*\[patch list\]\*\*;May 28, 1996

|                  |                  |                 |                                              |           |
|------------------|------------------|-----------------|----------------------------------------------|-----------|
| Routine Name | Before Patch | After Patch | Patch List                               | Bytes |
| IVMEVI1          | 13048910         | 12987947        | 9,50,15,16,24,166,30,256,292,455,463,565,601 | 7808      |
| IVMEVI2          | 11224568         | 11399431        | 5,9,11,50,15,16,565,292,455,463,582,601      | 7184      |
| IVMEVI3          | 11799174         | 11920864        | 20,22,24,166,292,455,463,565,601             | 7375      |

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

----3 Error Processing Purge Parameters

\[AYCB EDIT PURGE DATE\]

----4 Error Processing User Group

\[AYCB ERROR PROCESSING GROUP\]

----5 Error Processing Inquiry *New in Phase 2!*

\[AYCB SINGLE RECORD LOOKUP\]

## Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AYCBEP ERROR LOG SERVER..........Error Processing Server

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are exported with the Error Processing Tool:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 22%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Protocol Name</strong></th>
<th><strong>Associated Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AYCBEP MENU</td>
<td>Menu</td>
<td><p>Set to Menu. Contains the following protocols:</p>
<ul>
<li><blockquote>
<p>AYCBEP DATE RANGE</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP SORT</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP RETRANSMIT</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP FIND PATIENT</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP ASSIGN STAFF</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP MAIL</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP UPDATE STATUS</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP VIEW ERROR</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP ENTER/EDIT</p>
</blockquote></li>
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
<li><blockquote>
<p>AYCBEP RETRANSMIT</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP FIND PATIENT</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP ASSIGN STAFF</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP MAIL</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP UPDATE STATUS</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP VIEW ERROR</p>
</blockquote></li>
<li><blockquote>
<p>AYCBEP ENTER/EDIT</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>AYCBEP ENTER/EDIT</td>
<td>Enter/Edit VIVA Data</td>
<td>Entered only through the view error screen. Allows the user to modify VIVA data, then transmit the file to the appropriate site(s).</td>
</tr>
<tr class="odd">
<td>AYCBEP ADD COMMENT</td>
<td>Enter/Edit/View</td>
<td>Used to enter, edit, and view 240 characters of free text about a case. This option shall be available for processing consistency check and review file errors.</td>
</tr>
<tr class="even">
<td>AYCBEP VIEW AAC HL7 DATA</td>
<td>View AAC HL7 Data</td>
<td>Used as a view only screen which will list 22 fields transmitted by the HL7 message from the AAC.</td>
</tr>
<tr class="odd">
<td>AYCBEV SPACER</td>
<td>View Error Detail</td>
<td>Used to format the protocol list shown in the View Error Detail option.</td>
</tr>
</tbody>
</table>

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving capabilities exported with the Error Processing Tool software.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option AYCB EDIT PURGE DATE allows users to define the number of days that errors with a status of CLOSED or DELETE remain in the Error Message Log File before being purged.

# Callable Routines/Entry Points/Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines, entry points or APIs that can be called by other products. Any of the APIs called are existing routines.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 2 of the Error Processing Tool project (Patch IVMB\*2\*601) adds the processing of Review File cases to the Error Processing Tool created in Phase 1. Entries are filed into the Review File when the solicited or unsolicited (ORF/ORU) Z11 HL7 messages from the AAC are received at the HEC, and the data in the message is found to have some type of inconsistency with the data on file at the HEC. This data must be evaluated to determine if it should be uploaded into the HEC system.

# External/ Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*IST*A package versions or higher must be installed prior to installing the Error Processing Tool software:

|                     |                              |
|---------------------|------------------------------|
| Package Name    | Minimum Version Required |
| IVM                 | 2.0                          |
| Kernel              | 8.0                          |
| VA FileMan          | 22.0                         |
| V*IST*A HL7 | 1.6                          |

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no DBIAs associated with the Error Processing Tool software.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Error Processing Tool options have been designed to stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the Error Processing Tool software.

## SACC Exemptions/Non-standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions associated with the Error Processing Tool software.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements associated with the Error Processing Tool software. In accordance with VHA Directive 10-93-142, the files and fields exported with the Error Processing Tool software should not be modified locally.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following mail groups are associated with the Error Processing Tool:

|                                |                                                                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Mail Group Name            | Description                                                                                                                |
| Error Processing Active/Exempt | Receives any errors encountered during the installation of this software and the totals of records created, deleted, or purged |
| Error Processing Active/Exempt | Includes several people at the HEC.                                                                                            |

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

Using services should have a local contingency plan to be used in the event of application problems in a live environment. The plan should identify the procedure(s) for maintaining the functionality provided by Error Processing Tool software in the event of system outage. Field Station Information Security Officers (ISOs) can get assistance from the regional ISO (RISO).

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized products embedded within or required by the Error Processing Tool software.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Processing Tool software does not use electronic signatures.

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

The following is a list of recommended VA FileMan access codes for the files in the Error Processing Tool software:

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

In accordance with VHA Directive 10-93-142, the files and fields exported with the Error Processing Tool software should not be modified locally.

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
Exported Protocols 9
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
P
Package-wide Variables 13
Purge Parameter 3
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
