---
title: DVB Version 4 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: HINQ
app_name: Hospital Inquiry
section: FIN
app_status: active
pkg_ns: HINQ
patch_ver: 4
patch_id: HINQ*4
group_key: "HINQ:HINQ:4"
file_numbers: []
security_keys: []
menu_options: 1
description: - [# Revision History](#revision-history) - [# Introduction](#introduction) - [HINQ Replacement Diagram](#hinq-replacement-diagram) - [HINQ User Interface](#hinq-user-interface) - [HINQ Processing](#hinq-processing) - [Pending](#pending) - [New Mail](#new-mail) - [Error](#error) - [IDCU Error](#idcu
audience: 
keywords: 
  - mark
  - class
  - blank
  - hinq
  - even
  - table
  - contents
  - span
  - suspense
  - code
page_count: 0
word_count: 14725
section_count: 48
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 1992
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_62_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_62_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=41"
---

![](dvb-version-4-technical-manual/001.png)

HOSPITAL INQUIRY (HINQ)

TECHNICAL MANUAL

March 1992

Health Systems Design & Development (HSD&D)

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# Introduction](#introduction)
    - [HINQ Replacement Diagram](#hinq-replacement-diagram)
  - [HINQ User Interface](#hinq-user-interface)
  - [HINQ Processing](#hinq-processing)
  - [Pending](#pending)
  - [New Mail](#new-mail)
  - [Error](#error)
  - [IDCU Error](#idcu-error)
  - [HINQUP Features](#hinqup-features)
  - [Enter a Request in the HINQ Suspense File](#enter-a-request-in-the-hinq-suspense-file)
  - [Generate HINQ Requests](#generate-hinq-requests)
  - [Individual HINQ Request](#individual-hinq-request)
  - [Print Suspense File Messages](#print-suspense-file-messages)
  - [Process the HINQ Suspense File](#process-the-hinq-suspense-file)
  - [Status of HINQ By Patient](#status-of-hinq-by-patient)
  - [Utilities for Suspense File](#utilities-for-suspense-file)
  - [View the HINQ Suspense File](#view-the-hinq-suspense-file)
- [# Orientation](#orientation)
- [# Implementation and Maintenance](#implementation-and-maintenance)
  - [HL7 Z11 Crossmapping](#hl7-z11-crossmapping)
  - [HINQ Z11 Transaction](#hinq-z11-transaction)
- [# Routines](#routines)
    - [HEC to MVR Eligibility Query Diagram](#hec-to-mvr-eligibility-query-diagram)
  - [HEC Z07 & Z11 Processing](#hec-z07-z11-processing)
  - [HEC Processing HINQ Z11ORU](#hec-processing-hinq-z11oru)
  - [e\Gate Server transaction Handling](#egate-server-transaction-handling)
  - [HINQ Transactions with Simultaneous Z11 Update for HEC](#hinq-transactions-with-simultaneous-z11-update-for-hec)
  - [HEC Queries to MVR](#hec-queries-to-mvr)
  - [VBA Push Updates to HEC](#vba-push-updates-to-hec)
- [Files](#files)
  - [Globals and Files](#globals-and-files)
  - [File List](#file-list)
  - [Menu Diagram](#menu-diagram)
  - [Bulletins](#bulletins)
  - [Compiled Templates](#compiled-templates)
- [<span class="mark">HINQ Response from AITC</span>](#span-classmarkhinq-response-from-aitcspan)
  - [<span class="mark">HINQ Response Segments</span>](#span-classmarkhinq-response-segmentsspan)
  - [<span class="mark">Transfer to the Suspense (#395.5) file</span>](#span-classmarktransfer-to-the-suspense-3955-filespan)
  - [<span class="mark">Parsing the Suspense (#395.5) File</span>](#span-classmarkparsing-the-suspense-3955-filespan)
- [# Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [# External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
  - [Stand-alone files](#stand-alone-files)
  - [Stand-alone options](#stand-alone-options)
- [Package-Wide Variables](#package-wide-variables)
  - [Key Variables](#key-variables)
- [Security](#security)
  - [General Security](#general-security)
  - [Security Keys](#security-keys)
  - [VBA/VBA Security](#vbavba-security)
  - [Legal Requirements](#legal-requirements)
- [Performance Requirements](#performance-requirements)
  - [Latency](#latency)
  - [Packet Sizing](#packet-sizing)
  - [VA FileMan Access Codes](#va-fileman-access-codes)
- [# How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
  - [XINDEX](#xindex)
  - [Diagram Menus](#diagram-menus)
  - [Inquire to Option File](#inquire-to-option-file)
  - [Print Options File](#print-options-file)
  - [List File Attributes](#list-file-attributes)
- [Glossary](#glossary)
- [<span class="mark">APPENDIX A – AITC HINQ RESPONSE</span>](#span-classmarkappendix-a-aitc-hinq-responsespan)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 54%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>03/1992</td>
<td>Initial Release</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>Revised the HINQ technical manual according to the team feedback</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>Removed the How to use this manual section</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>Updated format styles</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>Updated Exported Options</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>UPdated Internal Relations</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>Updated Key Variables</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>Updated VA Fileman Access</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>Updated How to Generate On-line Document</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>Updated Introduction section of (V 4.0)</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>Updated Pending Status found in the Suspense File</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/17/05</td>
<td>Deleted Abbreviated section</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/18/05</td>
<td>Based upon feed/back from the team</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/18/05</td>
<td>Added DVBHQD2 code in Routine List</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/18/05</td>
<td>Deleted DVBNTEG code in Routine List</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/18/05</td>
<td>Deleted Entitlement Code in File List</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/18/05</td>
<td>Deleted Diary Definitions in File List</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/23/05</td>
<td>Based upon feed/back from the team</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/23/05</td>
<td>Removed the Menu Diagram from the Export Option</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/23/05</td>
<td>Removed the Routine List codes</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/23/05</td>
<td>Removed the File List</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/23/05</td>
<td>Removed the File Flow</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/20/05</td>
<td>Updated HL7 Z11 Crossmapping Table</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/20/05</td>
<td>Added Diagnostic Extremity Code to Crossmapping Table</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/20/05</td>
<td>Added Diag-Orig Effective Date of SC Rating to Crossmapping Table</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/20/05</td>
<td>Added Rating Date of SC per Disability</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/20/05</td>
<td>Effective Date of Combined Evaluation</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td>Added HINQ Replacement Diagram</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/04/05</td>
<td>Added HINQ User Interface</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td>Added ORU/ORF Z11 Segment to existing chart</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/05/05</td>
<td>Added Performance Requirements</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/05/05</td>
<td>Added Latency</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/05/05</td>
<td>Added Packet Sizing</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/24/12</td>
<td><p>Patch DVB*4.0*62/DG*5.3*797 –</p>
<p>Updated for Remedy Ticket HD 484945.</p></td>
<td>REDACTED/ REDACTED/REDACTED</td>
</tr>
<tr class="odd">
<td>3/12/12</td>
<td>Added Note under the File List on pg. 13 that the ENTITLEMENT CODES (#395.1) file and the DIARY DEFINITIONS (#395.4) file are no longer used.</td>
<td>REDACTED/REDACTED</td>
</tr>
<tr class="even">
<td>3/27/12</td>
<td><p>Patch DVB*4.0*62/DG*5.3*797 –</p>
<p>Updated footer date from April to March.</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main features of the HINQ package include the following.

- Requests may be sent individually, when necessary, or numerous requests may be forwarded in batch mode
- Status of Suspense file entries is automatically updated by the system to indicate the current status of the request
- Expanded informational response is obtained
- Provides the capability to update returned HINQ data directly into the PATIENT file

A HINQ is a request from a VA Medical Center for information pertaining to a veteran. HINQ requests are sent from a V*IST*A computer over TCP/IP to an interface at the AAC (Austin Automation Center) and then to the VBA (Veterans Benefits Administration) computer where veteran information is stored. Requests are processed by the VBA computer and returned via the AAC to the V*IST*A computer.

### HINQ Replacement Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-version-4-technical-manual/002.png)

## HINQ User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are minor changes made to the HINQ user interface that effect the following fields:

- VBA’s new HINQ service will request for the following items:
  - Veteran’s Claim Number
  - Social Security Number
  - Veteran’s Service Number
- The “User name”prompt has been removed.

## HINQ Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HINQ requests can only be directly sent to the VBA computer by users who are holders of the HINQ security key, DVBHINQ, and who have received a HINQ password. Other users may make HINQ requests but these are placed into a file (called the HINQ Suspense file) to be sent by a user with the required security to the VBA computer at a later time.

The HINQ Suspense file serves two major functions. As its name suggests, HINQ requests can be placed in this file for later processing. These requests are entered into the file with a status of PENDING. Selected options allow holders of the HINQ security key to release these requests for transmission to the VBA computer. The file also serves as a log in that HINQ responses from the VBA computer are also entered here in a NEW or ERROR status. This provides the medical center with a log of HINQ activity.

The status of Suspense file entries is updated automatically by the system to indicate the current status of the request. Following are the four available statuses for entries in the Suspense file: PENDING, NEW MAIL, ERROR, or IDCU ERROR.

## Pending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a request is placed into the Suspense file for later transmission, the entry is given the status of PENDING. The Suspense file should be used to store requests for batch transmission or when it is not possible to send the request directly to the VBA computer as in the following cases.

- The user does not have the required security - HINQ key and password.
- The network communication system is not functioning.

When these conditions are detected by the HINQ software, requests are automatically directed to the Suspense file.

## New Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Suspense file with the status of PENDING are updated to the NEW MAIL status when a request has been processed without error by the VBA computer and a response has been returned to the HINQ mail group.

## Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Suspense file with the status of PENDING are updated to the ERROR status when an error has occurred in the processing of this HINQ inquiry at the VBA computer. For example, the HINQ password was missing or invalid.

## IDCU Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Suspense file with the status of PENDING are updated to the IDCU ERROR status when an error has occurred in the return transmission of the HINQ string.

The HINQ package interfaces with the PIMS package allowing users to make HINQ Suspense file entries through select PIMS options. However, the MAS parameter, "Ask HINQ at Registration", and the MCCR parameter, "Ask HINQ in MCCR", must be set to YES in order to accomplish this.

The HINQ Package includes the following options/menus.

## HINQUP Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options contained in this menu encompass all the updating features. These options are only available to holders of the DVBHINQ and DG ELIGIBILITY security keys.

## Enter a Request in the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter requests for inquiries into the HINQ Suspense file.

## Generate HINQ Requests 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ. When requests for HINQ inquiries are entered through this option, PENDING entries in the Suspense file are transmitted to the VBA computer.

## Individual HINQ Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ, and is used to immediately transmit requests for HINQ inquiries to the VBA computer. This option does not create Suspense file entries.

## Print Suspense File Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a listing of those patients currently in the Suspense file with a HINQ response message. You may choose to print by patient, requestor or date/time.

## Process the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ. It is used to release PENDING requests in the Suspense file to the VBA computer.

## Status of HINQ By Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gives information about entries in the Suspense file including the HINQ response message if one has been received. Depending on how your site has this option set up, the option may only be available to holders of the HINQ security key, DVBHINQ.

## Utilities for Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options contained in this menu are used to perform HINQ utility functions such as purge entries in the HINQ Suspense file, delete an entry from the HINQ Suspense file, edit HINQ parameters and recompile HINQ templates. Depending on how your site has this menu set up, it may only be available to holders of the HINQ security key, DVBHINQ.

## View the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the entries in the Suspense file on the screen.

# # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HINQ Technical Manual has been divided into major sections for general clarity and simplification of the information being presented. This manual is intended to be a reference document. While the user is free to review the document from "cover to cover", it is best used by reviewing specific sections which contain the information required for a particular need. The Files Section shows the pointer relationships between the HINQ files and files external to the HINQ package. This section also has a listing of each HINQ Input and Print template. The Implementation and Maintenance Section provides information on any aspect of the package that is site configurable. The Exported Options Section provides a menu diagram of the HINQ package. The Routines Section contains information about the HINQ routines, including a description of each, routines to map, and callable routines. The Security Section contains legal requirements and recommended VA FileMan access codes. Lastly, there are brief sections on archiving and purging, how to generate on-line documentation, and package-wide variables for the HINQ package.

# # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several parameters associated with the HINQ package that are site configurable. These include IDCU ADDRESS, IDCU USERNAME-PASSWORD, HINQ DEVICE NAME, BATCH DEVICE NAME, and RDPC (Regional Data Processing Center) TIME DIFFERENCE. They can be accessed through the Edit HINQ Suspense File Parameters option through the Utilities for Suspense File Menu. If you have never installed HINQ and/or do not have the old HINQ parameters, you must use the Edit HINQ Suspense File Parameters option to set the parameters (refer to the HINQ Menu Section of the HINQ User Manual for specific instructions).

Once the parameters are set, the system will update the parameters automatically. For example, the LAST NET-WORKDAY parameter contains the date of the previous NETWORK DAY and is set and updated by the system. If necessary, this parameter can be set to an earlier date to view the HINQ Suspense file for a time previous to the last network day.

There are two site configurable outputs. USE HIGH INTENSITY is used to turn on/off the appearance of boldface type and the blinking character on the HINQ screens. The blinking character (arrow, etc.) is used to bring attention to a discrepancy or error between data in the PATIENT file and the HINQ response. HINQ MAIL MESSAGES, if set to YES, will generate mail response messages for batch HINQ requests (i.e., when the Generate HINQ Requests and Process the HINQ Suspense file options are utilized). If set to NO, only the summary bulletin will be generated.

## HL7 Z11 Crossmapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously all crossmapping was processed through the HEC and MVR interface components by using two non-standard HL7 transactions. With the implementation of the HINQ Interim Solution Phase 1 enhancements, the new VBA data set is crossmapped by the AAC interface engine to the existing HINQ response, and the existing HL7 Z11 formats.

| VBA Data Element Name                             | HINQ Layout Service Version 1.4 Line No. | ORU~/ORF~Z11 Segment | Sequence Name                              | Sequence Number |
|-------------------------------------------------------|----------------------------------------------|--------------------------|------------------------------------------------|---------------------|
| Veteran Name (Last, First, Middle & Suffix)           | 16,17,18,19                                  | PID                      | Patient Name                                   | 5                   |
| Date of Birth                                         | 28                                           | PID                      | Date/Time Of Birth                             | 7                   |
| Sex Indicator                                         | 30                                           | PID                      | Sex                                            | 8                   |
| Social Security Number                                | 26                                           | PID                      | SSN Number - Patient                           | 19                  |
| Sensitivity (Security) Level                          | 32                                           | OBX                      | Observation Value                              | 5                   |
| Type of Benefit                                       | 37                                           | ZEL                      | ELIGIBILITY CODE (C&P Ent Code)                | 2                   |
| Veteran Name (Last, First, Middle & Suffix)           | 16,17,18,19                                  | ZEL                      | LONG ID (CPO Stub)                             | 3                   |
| Claim Number                                          | 34                                           | ZEL                      | CLAIM FOLDER NUMBER                            | 6                   |
| Active Folder Location                                | 35                                           | ZEL                      | CLAIM FOLDER LOCATION                          | 7                   |
| Computed                                              | 0                                            | ZEL                      | ELIGIBLITY STATUS (BIRLS-DIAG-Verified)        | 10                  |
| Aid and Attendance Payee ("AANAGE"=yes)               | 90                                           | ZEL                      | RECEIVING A&A BENEFITS?                        | 14                  |
| Net Award Amount                                      | 44                                           | ZEL                      | C&P Net Awd Amt                                | 18                  |
| Competency Indicator                                  | 39                                           | ZPD                      | RATED INCOMPETENT                              | 8                   |
| Date Of Death                                         | 29                                           | ZPD                      | DATE OF DEATH                                  | 9                   |
| POW Capture & Release Dates                           | 131 & 132                                    | ZPD                      | POW STATUS INDICATED?                          | 17                  |
| Diagnostic Code (up to 30 occurrences, SC only)       | 77                                           | ZRD                      | DISABILITY CONDITION                           | 2                   |
| Diagnostic Percentage (up to 30 occurrences, SC only) | 78                                           | ZRD                      | DISABILITY %                                   | 3                   |
| Diagnostic Extremity                                  | 79                                           | ZRD                      | Diagnostic Extremity                           | TBD                 |
| Diag-Org Effective Date of Service Connected Rating   | 80                                           | ZRD                      | Original Effective Date SC Rating              | TBD                 |
| Rating Date of SC per Disability                      | 81                                           | ZRD                      | Current Effective Date SC Rating               | TBD                 |
| Combined % of Disability (SC only)                    | 83                                           | ZSP                      | Service Connected Percentage (CPO_COMB_Degree) | 3                   |
| Permanent And Total Indicator                         | 85                                           | ZSP                      | P&T\*                                          | 6                   |
| Employable Indicator                                  | 88                                           | ZSP                      | Unemployable                                   | 7                   |
| P&T Effective Date                                    | 86                                           | ZSP                      | P&T Effective Date                             | 10                  |
| Effective Date of Combined Evaluation                 | 84                                           | ZSP                      | Combined % Effective Date                      | TBD                 |

Changes to the existing Z11 messages to accommodate the new VBA data set will be:

- Sequence 5, Patient Name, in the PID Segment will be built from the Veteran Name fields (Last, First, Middle and Suffix) in the VBA response.
- Sequence 2, C&P Ent Code, of the ZEL Segment will be calculated based on the Type of Benefit Claim Code provided in the new VBA dataset, as follows: code C (compensation) will be converted to entitlement code 01, codes OLP, 306P and IP will be converted to entitlement code 0L. All other Type of Benefit Claim Codes applies to dependents’ claims and will not be sent to the HEC during the Interim Solution.
- Sequence 3, CPO Stub, in the ZEL Segment will be built from the Veteran Name fields (Last, First, Middle and Suffix) in the VBA response.
- Sequence 9 in the ZEL Segment (BIRBLS_DIAG_VERIFIED) is left blank.
- Sequence 10 in the ZEL Segment (BIRLS_DIAG_VERIFIED) will be left blank;
- Sequence 14, Receiving A&A Benefits?, in the ZEL Segment will be set to code 2 when the VBA dataset includes Aid and Attendance Payee = AANAGE.
- Sequence 17, POW Status Indicated?, in the ZPD Segment will be set to “Yes” when the VBA dataset includes a POW Capture and/or a POW Release Date.
- Sequence 12,13,14 is added to the ZRD Segment. They will occur for each disability code that is present in the VBA response. The new data elements are Diagnostic Extremity (Bilateral factor). Rated Disability original effective date, and Rated Disability current effective date.
- Sequence 6, P&T Indicator, and a new sequence 10 for the P&T Effective Date, in the ZSP Segment will become a part of the Z11~ORU routinely sent to the HEC by MVR. If VBA P&T Indicator = PTNSC, then Sequence 6 will be set to 1 (Yes). If VBA P&T Indicator is anything else, then Sequence 6 will be set to 0 (No). Sequence 10, P&T Effective Date will have a date only when Sequence 6, P&T Indicator, is set to “Yes.”
- Sequence 11 for the Combined SC% Effective Date is added to the ZSP Segment.
- Data Dictionary modifications made to the Veterans ID & Verification Access (#300.11) file (New Fields)=P&T Effective Date, Combined SC Percent Effective Date, Rated Disabilities,

> DX Extremity Bilateral Factor, Disability Original Effective Date, Disability Current Effective Date.

- HEC Error Processing Project (#743085) (New Fields)=P&T Effective Date 2;5 Node piece, field \# 8.1.,Combined SC Percent Effective Date 2;6 Node piece, field \#8.2.,Rated Disabilities 2;5 Node piece, field \#9.,DX Extremity Bilateral factor -0;5 Node piece, field \#4.

Disability Original Effective Date -0, 6 Node piece, field \#5.,Disability Current Effective Date -0;7 Node piece, field \# 6.

- Template Modifications:

The IVME enter VIVA input template was modified to include the following Rated Disabilities (#300.119) subjfields from the Veterans ID and Verification Access (#300.11) file.=DX Extremity Bilateral Factor field \#4.,Disability Original Effective Date field \#5.,Disability Current Effective Date field \#6.

## HINQ Z11 Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*ist*A HINQ queries that are received by the e\*Gate server are automatically reformatted to suit the new VBA query process standards. These HINQ transactions are updated with simultaneous Z11 messaging that is processed for HEC

Listed below are the following bullets that describe the process

- The e\*Gate server reformats the VBA response to fit the requirements of an existing V*ist*A HINQ response before returning it to the requested site
- V*ist*A HINQ response is automatically released by the e\*Gate server, where a simultaneous HL7 unsolicited update is generated
- It is passed to the HEC through the MVR

Based upon the current HINQ volume, it is estimated that an average of 65,000 additional HL7 unsolicited updates are processed per week.

# # Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to obtain a list of routines found in the HINQ DVB\*4.0\*49 software package listed below in the menu diagram.

DEV,VOO\>D P^DI

VA FileMan 22.0

Select OPTION: PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: ROUTINE//

SORT BY: NAME//

START WITH NAME: FIRST// DVBHCZ

GO TO NAME: LAST// DVBHZ

WITHIN NAME, SORT BY:

FIRST PRINT FIELD: NAME

THEN PRINT FIELD:

Heading (S/C): ROUTINE LIST//

START AT PAGE: 1//

DEVICE: UCX/TELNET Right Margin: 80//

### HEC to MVR Eligibility Query Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-version-4-technical-manual/003.png)

## HEC Z07 & Z11 Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps apply strictly to processing VistA Z07 and Z11 messages. The Z11 receiver process will automatically recognize the following new data fields:

- Combined % Effective Date, and for each disability code.
- The Diagnostic Extremity code.
- Original Effective Date of SC Rating.
- Current Effective Date of SC Rating

These new data fields are received from the HEC and are stored in the Patient file.

Currently there are no changes made to the outgoing Z07’s to HEC to include the P&T Effective date and four new additional fields.

1.  The Service Connected Calculator, and the SC percent over-ride calculator, which adds an additional 10% to the Combined Percentage in selected pension cases; however both will be disabled. VBA will provide the correct Combined Percentage (ZSP, Seq 3).
2.  Processing to verify eligibility is updated to use the following rules:
- If Entitlement Code = 0L and total check amount \>\$0 then YES to Receiving VA Pension and NO to Receiving VA Disability even if SC rated conditions are present. Enter SC = YES if SC rated conditions are present.
- If Entitlement Code = 01 or Null and SC rated conditions are present and total check amount \>\$0 then YES to SC and YES to Receiving VA Disability.
- If Entitlement Code = 01 or Null and SC rated conditions are present and total check amount =\$0 or Null then YES to SC and NO to Receiving VA Disability.
- If Entitlement Code = Null and no SC rated conditions are present and total check amount =\$0 or Null, then use data in site records to try to build a verified eligibility record.

## HEC Processing HINQ Z11~ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The consistency check, “Potential Missing Rated Disabilities,” is not included in the processing for the Z11~ORU.
2.  The consistency check, “Potential SC% reduction,” is removed from the Z11~ORU upload process.

> The VBA Push is triggered by a VBA award action which includes updates that are initiated in the Corporate database for all disabilities of record.

## e\*Gate Server transaction Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HINQ Transactions with Simultaneous Z11 Update for HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*ist*A HINQ queries that are received by the e\*Gate server are automatically converted to accommodate the new VBA query convention. The following guideline defines the process.

- The e\*Gate server reformats the VBA response to fit the requirements of the existing V*ist*A HINQ response before returning it to the requested site.
- HINQ response is automatically released by the e\*Gate server.
- A simultaneous HL7 unsolicited update is generated to the HEC (the HINQ Z11-ORU).
- HINQ Z11-ORU transactions are sent to the HEC every 30 minutes.

Currently it is estimated that an average of 65,000 additional HL7 unsolicited updates is processed each week.

## HEC Queries to MVR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The e\*Gate server will automatically receive HEC eligibility queries from MVR. They are converted to conform with the new VBA query process requirements. The following outline illustrates each step:

- e\*Gate server reformats the VBA response to conform to the requirements of the existing HL7 solicited update response (Z11~ORF) message.
- This function is returned to the HEC through the MVR server.
- A secure FTP is used to send all HEC queries to VBA nightly.

## VBA Push Updates to HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The e\*Gate server receives unsolicited updates from VBA. The following outline describes the process.

- The query is reformatted to conform to the requirements of an existing HL7 unsolicited update (Z11~ORU).
- The Z11 update is then forwarded to the HEC by the MVR server.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main global used in the HINQ package is ^DVB. The main file is the HINQ Suspense file (#395.5) located in global ^DVB(395.5,.

It is recommended, but not required, that global ^DVB be journaled.

Field 14.9 of the NEW PERSON file must contain a unique HINQ employee number for each user with the HINQ password.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to obtain a file list found in the HINQ DVB\*4.0\*49 software package listed below in the menu diagram. Note: the ENTITLEMENT CODES (#395.1) file and the DIARY DEFINITIONS (#395.4) file are no longer used.

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION: PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: FILE//

SORT BY: NAME// NUMBER

START WITH NUMBER: FIRST// 395

GO TO NUMBER: LAST// 395.99

WITHIN NUMBER, SORT BY:

FIRST PRINT ATTRIBUTE: NAME

THEN PRINT ATTRIBUTE:

Heading (S/C): FILE LIST//

START AT PAGE: 1//

DEVICE: UCX/TELNET Right Margin: 80//

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HINQ contains a bulletin, DVB HINQ RESPONSE, which will be sent when the processing of the HINQ Suspense file has returned with information. It will contain the number of successful responses, abbreviated responses and error responses. The patient names will be provided with the error responses.

## Compiled Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Template Routine Type

DVBHINQ UPDATE DVBHCE\* Input

DVBHINQ PAT-HINQ COMP DVBHCG\* Print

These templates can be compiled/recompiled through the recompile option in the utilities option of HINQ.

# <span class="mark">HINQ Response from AITC</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">HINQ Requests are generated either from Pending Requests out of the Suspense (#395.5) file or by direct individual HINQ requests. AITC responds to each HINQ request with a single large variable length string of approximately 1500 characters referred to as the HINQ Response. Within the variable length response string are fixed length data elements. Not all segments may appear, giving the string a variable length.</span>

## <span class="mark">HINQ Response Segments</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">A detailed description of the HINQ Response data elements appear in Appendix A. The HINQ Response segments are as follow:</span>

<span class="mark">Header Section - A 6 field string containing the veteran DFN identifier, response string length and response codes.</span>

<span class="mark">Basic Segment – A 101 field data segment containing details of the veteran’s claim including claim number, award amounts, and details related to the claim. The most recently added fields to this segment are the pension fields. If the award is a pension, this segment will contain the pension award effective date, termination dates, and reason codes.</span>

<span class="mark">Statistical Segment – A string containing general marital history, competency determination and disability information. The most recently added fields to this segment are the Permanent and Total Effective date and the DD214 Dental Indicator.</span>

<span class="mark">Diagnostic Segment – A data segment containing the detailed service connected diagnostic data for up to 150 codes including percent service connected disability and effective date.</span>

<span class="mark">Child/Birth Segment – If there are any children, for each child, this segment contains fixed length sections including the date of birth and status of each child.</span>

<span class="mark">Address Segment – A fixed length segment of 145 characters containing the veteran’s current address.</span>

<span class="mark">Reference Number Segment – A short segment containing the social security number.</span>

<span class="mark">Income Segment – A data segment containing details of current and past year income including adjustments.</span>

<span class="mark">Monthly Retirement Segment – A data segment containing the verified retirement amount.</span>

<span class="mark">BIRLS Segment – A 24 field data segment containing the Beneficiary Identification Records Locator Subsystem (BIRLS) data. BIRLS contains basic identifying information on a VA claimant including service information.</span>

<span class="mark">HINQ end of string delimiter – A hard coded ‘NNNN’ to indicate the end of the HINQ Response string.</span>

## <span class="mark">Transfer to the Suspense (#395.5) file</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The Suspense (#395.5) file is subscripted with the patient’s DFN. The HINQ Response string for a patient is deposited into the patient’s Suspense (#395.5) file entry on the “RS” node as a multiple field in 245 character consecutive chunks. As a typical example, a test data set is shown below. In this test data the patient’s DFN, ‘523388976’, of the HINQ Response Header Section (see Appendix A) begins at the 8<sup>th</sup> character position of the first “RS” string.</span>

<span class="mark">^DVB(395.5,523388976,"RS",1,0)="HINQ2 523388976 918499995153 100 AJDOCX</span>

<span class="mark">ZN 01 24300 24300 015 0 01 1</span>

<span class="mark">H 0 1</span>

<span class="mark">"</span>

<span class="mark">^DVB(395.5,523388976,"RS",2,0)=" M 0326195111221957 02081933</span>

<span class="mark">N MAXZARET 0</span>

<span class="mark"></span>

<span class="mark">"</span>

<span class="mark">^DVB(395.5,523388976,"RS",3,0)="</span>

<span class="mark"></span>

<span class="mark"></span>

<span class="mark">"</span>

<span class="mark">^DVB(395.5,523388976,"RS",4,0)=" 145 101775 TJOXZ DAX</span>

<span class="mark">ZEL OCXZNELLK5 ADXZS DRIVE+STXZ MA</span>

<span class="mark">666243428</span>

<span class="mark">.00 "</span>

<span class="mark">^DVB(395.5,523388976,"RS",5,0)="</span>

<span class="mark"></span>

<span class="mark">66624342811223565 JOXZ DAXZEL</span>

<span class="mark">OCXZNELL "</span>

<span class="mark">^DVB(395.5,523388976,"RS",6,0)="</span>

<span class="mark"></span>

<span class="mark">ARMY 03261951 11221957</span>

<span class="mark">HON 0 1 M Y 2 "</span>

<span class="mark">^DVB(395.5,523388976,"RS",7,0)=" 20 08182008610010 0818200808182008626010 08</span>

<span class="mark">18200808182008 "</span>

## <span class="mark">Parsing the Suspense (#395.5) File</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The Suspense file is parsed following the HINQ Response data layout in Appendix A. The individual fields are placed in subscripted local variables and passed to the requesting operation either for display or for selective updating of the patient’s file.</span>

# # Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HINQ product exports 2 menu structures. These are HINQ Menu and HINQ User Menu (excludes all Utilities for Suspense File options).

HINQ Transaction Test - This option is used to determine if the communication link between the hospital and the VBA is functioning properly. It will function exactly like the individual HINQ request but there is no user intervention. As this option executes, it will display the steps it is taking on the screen. The transaction test will always return an error indicating that the password is invalid if the link is up and running

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the HINQ package does not have an actual archiving feature at this time, the Purge Suspense File option allows old entries in the HINQ Suspense file to be deleted. This serves the same purpose as an archiving feature because it frees up space for current entries in the HINQ Suspense file. Deletion of the old entries through the Purge Suspense File option is permanent, whereas deletion through an archiving feature would not be.

The recommended procedure is to queue the AUTO HINQ PURGE option through TaskMan to run on a monthly basis. This will maintain the size of the HINQ Suspense file.

# # External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FileMan Version 18

Kernel Version 6.5

All HINQ responses when using the "Individual" option are transferred to MailMan messages with a call to XMD using standard MailMan conventions. HINQ requests entered into the Suspense file are stored there for future use. A Bulletin will be sent to the DVBHINQ mail group to notify members of returned HINQ responses after processing of the Suspense file has taken place.

When utilizing the Update HINQs to the Patient file option, the MAS consistency checker will be run if a patient's data is updated with HINQ information. This is done to correct any inconsistencies in the patient's record. It is a direct call to the ^DGRPC MAS routine.

Information concerning the functionality of the consistency checker may be found in the PIMS User Manual.

HINQ will now utilize the NEW PERSON file instead of the USER file. The HINQ EMPLOYEE NUMBER (field 14.9) was write protected in the NEW PERSON file. HINQ has obtained permission to take the write protection off Field 14.9 of the NEW PERSON file and place it on Field 14.9 of the USER file. This way the sites can update the HINQ EMPLOYEE NUMBER using FileMan.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Stand-alone files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

395.2 Anatomical-Loss Codes

395.3 Monthly Compensation

## Stand-alone options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Request in the HINQ Suspense File

View the HINQ Suspense File

Edit HINQ Suspense File Parameters

Delete Entry from HINQ Suspense File

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the HINQ package.

## Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below are a few of the many important variables associated with the HINQ package.

DVBDEV IDCU device

DVBERR VBA error message

DVBIP TCP/IP address

DVBLOG RDPC IDCU code

DVBLEN Length of HINQ response string from VBA

DVBNUM Employee number

DVBSTN Station number

DVBZ HINQ request string

X(N) Receives HINQ response from RDPC

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the storage of the returning HINQ information, a check sum has been developed to insure the integrity of the stored data. If the HINQ information in the Suspense file has been adjusted since the last HINQ, a warning message will appear (see below) and the HINQ data will not be accessible.

"HINQ data does NOT seem right

Re-HINQ and/or Notify system manager.

HINQ check sum failure for {patient name}"

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DVBHINQ Access to options requiring HINQ password

DG ELIGIBILITY Access to Update HINQs to the Patient File option

## VBA/VBA Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VBA has set up a new Common Security Services table in their database to control access to VBA data from VHA and other entities. In order to obtain the VBA employee number and password, VA Form 20-8824e, Common Security Services (CSS) User Access Request form must be completed and forwarded to the facility's supporting VBA Regional Office. The form is normally completed by the facility's ISO, but the responsibility may have been delegated to others, such as a HINQ coordinator or to IRM. The application access to request is "Web HINQ." Once the VBA ISO has updated the Common Security file with information about the employee, the Employee Identification Number (EIN) and password will be returned to the facility. The EIN is the HINQ Employee Number and must be loaded in the NEW PERSON file as explained in External Relations above.

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known legal requirements associated with this package.

# Performance Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Latency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Latency controls the actual amount of time a transaction can travel through the network.

Response times are affected through this process primarily because of the following elements:

- Whenever a HINQ query requires a response from three different databases.
- A build-up of traffic on the network, which can cause some of the segments to process slower than others.

In order to avoid prolong delays that are caused by the demands of the processor’s resources HINQ has developed a delay mechanism that will automatically trigger whenever a response is not received in a adequate amount of time.

## Packet Sizing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data is broadcast through this network communication process. The VistA processor will automatically transmit a packet of data to the target processor that opens the communication channel. The target processor then returns an acknowledgment to the sender. During the initial testing it was discovered that a change in the packet size had caused HINQ processing to fail with certain platforms. This discovery has caused VBA to re-evaluate restoring the size of their packets to 256 bytes.

## VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FileMan Access Codes are not sent out with any of the HINQ files. Below is a list of the suggested FileMan Access Codes associated with each file that belongs to the HINQ package.

FILE FILE DD RD WR DEL LAYGO

<u>NUMBER</u> <u>NAME</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

395 DVB PARAMETER \# D d d d

395.2 ANATOMICAL LOSS CODES @ D @ @ @

395.3 MONTHLY COMPENSATION @ D @ @ @

395.5 HINQ SUSPENSE \# D d d d

395.7 HINQ AUDIT \# D d d d

# # How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure HINQ technical documentation. On-line technical documentation pertaining to the HINQ software, in addition to that which is located in the help prompts and on the help screens found throughout the HINQ package, may be generated through utilization of several KERNEL options. These include, but are not limited to: XINDEX, Diagram Menus, MenuMan Inquire to OPTION File and Print OPTIONS file, and VA FileMan List File Attributes.

Entering question marks at the "Select...Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the KERNEL REFERENCE MANUAL.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to Programming Standards. The XINDEX output may include the following components: Compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Globals, Label References, and External References. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the HINQ package, specify the following at the "routine(s) ?\>" prompt: DVBH\* (-) DVBHC\*.

HINQ initialization routines and compiled template routines which reside in the UCI in which XINDEX is being run, as well as local routines found within the HINQ namespace, should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-). Use an apostrophe (') to accomplish this.

## Diagram Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print the complete HINQ Menu, enter DVB HMENU-HINQ at the first prompt.

To print the HINQ User Menu, enter DVB HMENU-USER at the first prompt.

## Inquire to Option File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This MenuMan option provides the following information about a specified option(s): option name, menu text, option description, type of option, and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about HINQ options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the HINQ package is DVB.

## Print Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file, or may elect to specify a single option or range of options. To obtain a list of HINQ options, the following option namespace should be specified: DVB.

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, and description, help prompt, cross-reference(s), input transform, date last edited and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates and sort templates.

If you are running Kernel 7/FileMan 19, List File Attributes will be found under the Data Dictionary Utilities.

For a comprehensive listing of HINQ files, please refer to the FILE Section of this manual.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BIRLS Beneficiary Information and Records Locator
Subsystem
C&P Compensation and Pension
DVBHINQ A security key in the HINQ package.
HINQ employee number A number entered into the NEW PERSON file for each
user who has a HINQ password. It is distributed by
VBA and uniquely identifies each user to VBA.
HINQ Response Response from VBA computer to a HINQ request.
HINQ Suspense File File which serves 2 major functions - stores HINQ
requests for later processing and serves as a log in
that HINQ responses are entered here.
HINQ Suspense Pending request awaiting transmission
File statuses New Mail successful response received
Error error occurred in the processing of
this inquiry at the VBA computer
IDCU error error occurred in the return
transmission of the HINQ string
IDCU Integrated Data Communications Utility
VBA Veterans Benefits Administration

# <span class="mark">APPENDIX A – AITC HINQ RESPONSE</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><mark>Field name</mark></strong></th>
<th><strong><mark>HINQLayout data element</mark></strong></th>
<th><strong><mark>Type</mark></strong></th>
<th><strong><mark>Length</mark></strong></th>
<th><strong><mark>Description</mark></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><mark>C&amp;P Record</mark></strong></td>
<td><strong><mark>Set Description from Corporate</mark></strong></td>
<td><strong><mark> </mark></strong></td>
<td><strong><mark> </mark></strong></td>
<td><strong><mark> </mark></strong></td>
</tr>
<tr class="even">
<td><mark>HEADER SECTION</mark></td>
<td><mark> </mark></td>
<td><strong><mark> </mark></strong></td>
<td><strong><mark> </mark></strong></td>
<td><mark> </mark></td>
</tr>
<tr class="odd">
<td><mark>command</mark></td>
<td><mark>HINQ</mark></td>
<td><mark>alpha</mark></td>
<td><mark>4</mark></td>
<td><mark>value = "HINQ" - indicates that this is a Hospital Inquiry</mark></td>
</tr>
<tr class="even">
<td><mark>BIRLS Response code</mark></td>
<td><mark>2, 6, 9, B, C, D</mark></td>
<td><mark>alpha or numeric</mark></td>
<td><mark>1</mark></td>
<td><mark>2 = record is returned. C = retry, D = Sensitivity level restriction, 9 = Invalid Psw, 6 = Invalid UserID/Your Userid has been locked/You do not have the authority to run the requested application, B = Problem on Database/retry</mark></td>
</tr>
<tr class="odd">
<td><mark>C&amp;P Response code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>DFN</mark></td>
<td><mark>blanks</mark></td>
<td><mark>blank</mark></td>
<td><mark>14</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>message length</mark></td>
<td><mark>Calculated</mark></td>
<td><mark>numeric</mark></td>
<td><mark>4</mark></td>
<td><mark>length of the response message string</mark></td>
</tr>
<tr class="odd">
<td><mark>BASIC SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark>Claim Number</mark></td>
<td><mark>Claim Number</mark></td>
<td><mark>alpha</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Benefit Indicator</mark></td>
<td><mark>enter 1</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>always has a value of one</mark></td>
</tr>
<tr class="even">
<td><mark>Payee Number</mark></td>
<td><mark>enter 00</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>indicates veteran</mark></td>
</tr>
<tr class="odd">
<td><mark>Last disk update</mark></td>
<td><mark>blanks</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Record Type</mark></td>
<td><mark>enter A</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>always has a value of A</mark></td>
</tr>
<tr class="odd">
<td><mark>Veteran name</mark></td>
<td><mark>parse from:</mark></td>
<td></td>
<td></td>
<td><mark>name format if the name is longer than the 20 characters allowed for address line 1.1. drop the suffix 2. if still too long drop all but the middle name initial 3. if still too long drop all but the first name initial 4. if still too long truncate the last name.</mark></td>
</tr>
<tr class="even">
<td><mark>First Initial</mark></td>
<td><mark>Veteran First Name</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Middle initial</mark></td>
<td><mark>Veteran Middle Name</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Surname</mark></td>
<td><mark>Veteran Last Name</mark></td>
<td><mark>alpha</mark></td>
<td><mark>5</mark></td>
<td><mark>first 5 characters of last name</mark></td>
</tr>
<tr class="odd">
<td><mark>Activity</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Date last activity</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Station</mark></td>
<td><mark>last 2 char from Active Folder Location</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>station number code: return last 2 digits</mark></td>
</tr>
<tr class="even">
<td><mark>Recoupment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>PFOP/FDIB</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Consolidated payment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Deduction/balance</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Burial Award</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Clothing allowance</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Headstone</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Mail code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Net award amt</mark></td>
<td><mark>Net Award Amount</mark></td>
<td><mark>numeric</mark></td>
<td><mark>6</mark></td>
<td><mark>(pertains only to veteran) will be formatted to nnnn.nn/ code removed decimal return nnnnnn</mark></td>
</tr>
<tr class="odd">
<td><mark>Net award date</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>8</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Check amt</mark></td>
<td><mark>Check Amount</mark></td>
<td><mark>numeric</mark></td>
<td><mark>6</mark></td>
<td><mark>will be formatted to nnnn.nn/ code removed decimal return nnnnnn</mark></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Entitlement code</mark></td>
<td><mark>Type of benefit</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>306P, IP, OLP = 0L; C = 01; 306DP, IDP, OLDP, 1312A, DIC, DICP, DICR, DC, BD, SB, CA, EORP, ME, MOH, NSCAI, NSCBB, NSTC, PA, SCBB, SCT, SPA, TA = " " (i.e. blank blank). VBA will return up to 20 codes. The first code in the list is used by HINQ to populate Entitlement code.</mark></td>
</tr>
<tr class="odd">
<td><mark>Address lines</mark></td>
<td><mark>5</mark></td>
<td><mark>numeric</mark></td>
<td><mark>1</mark></td>
<td><mark>number of address lines in record - always 5</mark></td>
</tr>
<tr class="even">
<td><mark>Insurance change segment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Tax indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Chief attorney</mark></td>
<td><mark>Chief Attorney, Fiduciary</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Change reason</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>CHAMP/VA indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>CARS segment indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Dependency</mark></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><mark>Total Number of Children</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>total dependents this award</mark></td>
</tr>
<tr class="even">
<td></td>
<td><mark>Children Count for a max of 20</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>total dependents this record</mark></td>
</tr>
<tr class="odd">
<td><mark>Children in school</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Helpless children</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Service organization</mark></td>
<td><mark>Power of Atty/Svc Org or Priv Atty</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td><mark>Power of Attorney/Service Org Only using 2nd &amp; 3rd char from VBA</mark></td>
</tr>
<tr class="even">
<td><mark>EVR Control code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>EVR type</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Income code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Special law code</mark></td>
<td><mark>Medal of Honor</mark></td>
<td><mark>alpha</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Net worth</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Net worth custodian/spouse</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>A&amp;A</mark></td>
<td><mark>Aid And Attendance payee</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>Aid &amp; Attendance/Housebound - payee AANAGE =A; HBVESMPIF=H; else Blank</mark></td>
</tr>
<tr class="odd">
<td><mark>Purge Indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Active folder locator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Veteran SSN verified</mark></td>
<td><mark>Verified SSN Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>0=Not verified, 1=verified(code makes no checks)</mark></td>
</tr>
<tr class="even">
<td><mark>BSSI indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Payee/spouse SSN verified</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Check stuffer</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Med. Benefits code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Benefit change indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Auto allowance paid</mark></td>
<td><mark>Auto Allowance Paid</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Auto adapt. Equip. paid</mark></td>
<td><mark>Auto Adapt Equipment Paid</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>EAEO=E, EAAE=A, NEAAE=N, or Null</mark></td>
</tr>
<tr class="odd">
<td><mark>Special adapt. housing paid</mark></td>
<td><mark>Special Adaptive Housing paid</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Nursing home indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Character of Discharge</mark></td>
<td><mark>Character of Service (from MOST recent period)</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>H=Honorable, D=Dishonorable, U=Uncharacterized, O=Other(code makes no checks)</mark></td>
</tr>
<tr class="even">
<td><mark>Original award effective date</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>8</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Mailing list indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Security level</mark></td>
<td><mark>Sensitive Check Level</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Incarceration</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>POW indicator</mark></td>
<td><mark>calculate this: 0=none, 1&lt;30, or 2=&gt;30; no POW dates is a blank (" ")</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Statistical segment type</mark></td>
<td><mark>enter 1</mark></td>
<td><mark>numeric</mark></td>
<td><mark>1</mark></td>
<td><mark>0=none, 1=A, 2=B, 3=C(we always return '1')</mark></td>
</tr>
<tr class="even">
<td><mark>Birth segment code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Withholding/apportionment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Non-recurring payment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Accrue payment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Irregular payment</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Pay change segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>DD/EFT segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Reference segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Proceeds segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Military pay status code</mark></td>
<td><mark>No Payment Status Code</mark></td>
<td><mark>numeric</mark></td>
<td><mark>1</mark></td>
<td><mark>0=none, 1=present(code makes no checks)</mark></td>
</tr>
<tr class="even">
<td><mark>Manila payment code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Suspense Segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>No payment status code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Futures error</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Diagnostics error</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Statistical error</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Basic error</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Future segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Prior segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Income segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Monthly retirement segment ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Rate not supported</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Over age 72</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>VRE Account record</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>REPS indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Active reservist</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Reservist # days waived</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Audit related A/R indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Pension Award Effective Date</mark></td>
<td><mark>Pension Award Effective Date</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>Pension Award Reason Code</mark></td>
<td><mark>Pension Award Reason Code</mark></td>
<td><mark>alpha</mark></td>
<td><mark>12</mark></td>
<td><mark>If Pension Award Effective Date is not NULL, Pension Award Reason Code = the first non-NULL Pension Award Reason Text value</mark></td>
</tr>
<tr class="odd">
<td><mark>Pension Award Termination Date</mark></td>
<td><mark>Pension Award Termination Date</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>Pension Termination Code 1</mark></td>
<td><mark>Pension Award Reason One Text</mark></td>
<td><mark>alpha</mark></td>
<td><mark>12</mark></td>
<td><mark>If Pension Award Termination Date is not NULL, Pension Termination Code 1 = Pension Award Reason One Text</mark></td>
</tr>
<tr class="odd">
<td><mark>Pension Termination Code 2</mark></td>
<td><mark>Pension Award Reason Two Text</mark></td>
<td><mark>alpha</mark></td>
<td><mark>12</mark></td>
<td><mark>If Pension Award Termination Date is not NULL, Pension Termination Code 2 = Pension Award Reason Two Text</mark></td>
</tr>
<tr class="even">
<td><mark>Pension Termination Code 3</mark></td>
<td><mark>Pension Award Reason Three Text</mark></td>
<td><mark>alpha</mark></td>
<td><mark>12</mark></td>
<td><mark>If Pension Award Termination Date is not NULL, Pension Termination Code 3 = Pension Award Reason Three Text</mark></td>
</tr>
<tr class="odd">
<td><mark>Pension Termination Code 4</mark></td>
<td><mark>Pension Award Reason Four Text</mark></td>
<td><mark>alpha</mark></td>
<td><mark>12</mark></td>
<td><mark>If Pension Award Termination Date is not NULL, Pension Termination Code 4 = Pension Award Reason Four Text</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark>STATISTICAL SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark>Type A</mark></td>
<td><mark> </mark></td>
<td><mark>for record type A</mark></td>
</tr>
<tr class="odd">
<td><mark>Blind indicator</mark></td>
<td><mark>Blind Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>"B=Blind"</mark></td>
</tr>
<tr class="even">
<td><mark>Sex</mark></td>
<td><mark>Sex Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>M/F</mark></td>
</tr>
<tr class="odd">
<td><mark>Branch of service</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>EOD</mark></td>
<td><mark>EOD Date (from most recent period)</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="odd">
<td><mark>RAD</mark></td>
<td><mark>RAD Date (from most recent period)</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>Additional Service</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>DOB - vet</mark></td>
<td><mark>Date of Birth</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>misc code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Combat_Disabled_Iindicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Employable</mark></td>
<td><mark>Employable Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>N employable, Y =unemployable</mark></td>
</tr>
<tr class="even">
<td><mark>Competency</mark></td>
<td><mark>Competency Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>Possible codes are: C, CC, IR, ICC, LDC, PIC, DEFC; C, CC, PIC &amp; DEFC = C competence, ICC, IR &amp; LDC = I incompetent</mark></td>
</tr>
<tr class="odd">
<td><mark>Spouse A&amp;A/HB</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Competency payment status</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Special provision code</mark></td>
<td><mark>Permanent and Total Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>set to 3 if the VBA response is PT35 and to 2 if the VBA response is NPT35</mark></td>
</tr>
<tr class="even">
<td><mark>Special monthly comp. code</mark></td>
<td><mark>blank</mark></td>
<td><mark>alpha</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Loss of use code</mark></td>
<td><mark>Loss of use Code</mark></td>
<td><mark>alpha</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Anatomical loss code</mark></td>
<td><mark>Anatomical Loss Code</mark></td>
<td><mark>alpha</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Other loss code</mark></td>
<td><mark>Other Loss Code</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Vet married to vet code</mark></td>
<td><mark>Veteran Married to Veteran</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>Y(straight copy)</mark></td>
</tr>
<tr class="odd">
<td><mark>DOB - Spouse</mark></td>
<td><mark>Spouse Birth Date</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>Spouse first name</mark></td>
<td><mark>Spouse First Name</mark></td>
<td><mark>alpha</mark></td>
<td><mark>10</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Hospital SMC code</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>DOB - father</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>8</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>DOB - mother</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>8</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>4</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Permanent and Total Effective Date</mark></td>
<td><mark>Permanent and Total Effective Date</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>DD214 Dental Indicator</mark></td>
<td><mark>DD214 Dental Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>If VBA value = 'Y', set to 'N'<br />
If VBA value = 'N', set to 'Y'</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><mark>DIAGNOSTIC SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="odd">
<td><mark># SC diagnostic codes</mark></td>
<td><mark>Diagnostic Count for a maximum of 150</mark></td>
<td><mark>numeric</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Combined disability %</mark></td>
<td><mark>Combined % Of Disability</mark></td>
<td><mark>alpha</mark></td>
<td><mark>3</mark></td>
<td><mark>If the Combined % Of Disability is not present in the Corporate database as RATING_AWARD_DETAIL Sc_Combnd_Pct_Nbr, then it will be calculated from the current SC disabilities and returned as Comb-Deg (3) from BDN.</mark></td>
</tr>
<tr class="odd">
<td><mark>Effective Date of Combined Evaluation</mark></td>
<td><mark>Effective Date of Combined Evaluation</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>code/percent/extremity/effective date/rating date</mark></td>
<td></td>
<td></td>
<td></td>
<td><mark>(up to 150 occurrences - if empty use blanks)</mark></td>
</tr>
<tr class="odd">
<td><mark>Code</mark></td>
<td><mark>Diagnostic Code</mark></td>
<td><mark>alpha</mark></td>
<td><mark>4</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>% disability</mark></td>
<td><mark>Diagnostic Percentage (%)</mark></td>
<td><mark>numeric</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Diagnostic Extremity</mark></td>
<td><mark>Diagnostic Extremity</mark></td>
<td><mark>alpha</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Original Effective Date Of Service Connected Rating</mark></td>
<td><mark>Original Effective Date Of Service Connected Rating</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="odd">
<td><mark>Rating Date of SC Per Disability</mark></td>
<td><mark>Rating Date of SC Per Disability</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>CHILD/BIRTH SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark>Total # children</mark></td>
<td><mark>Total Number Of Children</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark># child segments</mark></td>
<td><mark>Children Count for a max of 20</mark></td>
<td><mark>numeric</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>child data</mark></td>
<td></td>
<td></td>
<td></td>
<td><mark>(up to 20 occurrences - blanks if not used)</mark></td>
</tr>
<tr class="odd">
<td><mark>DOB</mark></td>
<td><mark>Child Birth Date</mark></td>
<td><mark>numeric</mark></td>
<td><mark>8</mark></td>
<td><mark>ddmmyyyy</mark></td>
</tr>
<tr class="even">
<td><mark>Status</mark></td>
<td><mark>Child Status</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>A=AASP, H=HC, M=MC, N=NAWDDEP, P=PAR, S=SCHCHD</mark></td>
</tr>
<tr class="odd">
<td><mark>First name</mark></td>
<td><mark>Child First Name</mark></td>
<td><mark>alpha</mark></td>
<td><mark>10</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Withholding/APP Segment</mark></td>
<td><mark>Blanks for 20</mark></td>
<td><mark>blank</mark></td>
<td><mark>20</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>ADDRESS SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Length of segment</mark></td>
<td><mark>total of 145 in length</mark></td>
<td><mark>numeric</mark></td>
<td><mark>3</mark></td>
<td><mark>always 145</mark></td>
</tr>
<tr class="even">
<td><mark>Sequence control</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Name line indicator</mark></td>
<td><mark>1</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>which of the address lines holds the name - always 1</mark></td>
</tr>
<tr class="even">
<td><mark>Zip code</mark></td>
<td><mark>Zip Code Prefix; Zip Code First Suffix</mark></td>
<td><mark>alpha</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Line length code</mark></td>
<td><mark>this and the following line</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td><mark>these two fields repeated up to 6 times (see HINQ Ref for codes)</mark></td>
</tr>
<tr class="even">
<td><mark>Address line</mark></td>
<td><mark>are 145 in length</mark></td>
<td><mark>alpha</mark></td>
<td><mark>var</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>var</mark></td>
<td><mark>use to expand to 145 characters for the address segment</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>REF NUMBER SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark>Ref # for Type A Ref segment</mark></td>
<td><mark>Social Security Number</mark></td>
<td><mark>alpha</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Ref # for Type C Ref segment</mark></td>
<td><mark>blanks</mark></td>
<td><mark>blank</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Ref # for Type X Ref segment</mark></td>
<td><mark>blanks</mark></td>
<td><mark>blank</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><mark>INCOME SEGMENT</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="odd">
<td><mark>Income segment type</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Payment reduced indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>No Adj necessary indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Acct not automatically adj ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Payment increased indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Retro decrease made indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Increase protected by spec law</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Retro increase made indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Indiv underestimated income ind</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Source of payee income</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Source of spouse income</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Previously reported income</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Income reported this year</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Last calendar year reported</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>4</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Income for VA purposes</mark></td>
<td><mark>Income For VA purposes</mark></td>
<td><mark>numeric</mark></td>
<td><mark>5</mark></td>
<td><mark>will be formatted to nnn.nn/ code removed decimal return nnnnn</mark></td>
</tr>
<tr class="even">
<td><mark>Type medical or last expense</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Amt of medical or last expense</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Transaction 13Q processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Transaction 45 processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Transaction 47 processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Transaction 47I processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Transaction 48 processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Transaction 48G processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Transaction 49 processed</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Ver SS adjusted by COLA</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Hardship expense</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>5</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>MONTHLY RETIREMENT SEG</mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
<td><mark> </mark></td>
</tr>
<tr class="even">
<td><mark># retirement segments</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>2</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>expansion</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>(retirement data)</mark></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Type retirement income</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Verified monthly amount</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>6</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Reported monthly amount</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>6</mark></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong><mark>field name</mark></strong></td>
<td><strong><mark>HINQLayout6 data element</mark></strong></td>
<td><strong><mark>type</mark></strong></td>
<td><strong><mark>length</mark></strong></td>
<td><strong><mark>description</mark></strong></td>
</tr>
<tr class="even">
<td><strong><mark>BIRLS</mark></strong></td>
<td><strong><mark>Set Description from Corporate</mark></strong></td>
<td><strong><mark> </mark></strong></td>
<td><strong><mark> </mark></strong></td>
<td><strong><mark>(this part is added to the C&amp;P message)</mark></strong></td>
</tr>
<tr class="odd">
<td><mark>SSN</mark></td>
<td><mark>Social Security Number</mark></td>
<td><mark>alpha</mark></td>
<td><mark>9</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Service number</mark></td>
<td><mark>Military Service Number</mark></td>
<td><mark>alpha</mark></td>
<td><mark>9</mark></td>
<td><mark>(occurs three times)</mark></td>
</tr>
<tr class="odd">
<td><mark>Alternate name</mark></td>
<td><mark>Prior First Name, Middle, Last, Suffix</mark></td>
<td><mark>alpha</mark></td>
<td><mark>63</mark></td>
<td><mark>(occurs three times)</mark></td>
</tr>
<tr class="even">
<td><mark>DOD</mark></td>
<td><mark>Date Of Death</mark></td>
<td><mark>alpha</mark></td>
<td><mark>8</mark></td>
<td><mark>MMDDYYYY</mark></td>
</tr>
<tr class="odd">
<td><mark>Service data</mark></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Branch</mark></td>
<td><mark>Branch Of Service</mark></td>
<td><mark>alpha</mark></td>
<td><mark>4</mark></td>
<td><mark>(occurs three times, use blanks if empty)<br />
(Air_Force "AF") (Air_Force_Academy "AFA") (Air_Force_Reserve "AFR") (Air_National_Guard "AFNG") (Army "ARMY") (Army_Air_Corps_or_Army_Air_Force "AAC") (Army_National_Guard "ARNG") (Army_Reserves "AR") (Coast_Guard "CG") (Coast_Guard_Academy "CGA") (Coast_Guard_Reserves "CGR") (Marine_Corps "MC") (Marine_Corps_Reserves "MCR") (Merchant_Marine "MM") (Naval_Academy "NA") (Navy "NAVY") (Navy_Reserves "NR") (Public_Health_Service "PHS")</mark></td>
</tr>
<tr class="odd">
<td><mark>EOD</mark></td>
<td><mark>EOD Date</mark></td>
<td><mark>alpha</mark></td>
<td><mark>8</mark></td>
<td><mark>MMDDYYYY (occurs three time - use blanks if empty)</mark></td>
</tr>
<tr class="even">
<td><mark>RAD</mark></td>
<td><mark>RAD Date</mark></td>
<td><mark>alpha</mark></td>
<td><mark>8</mark></td>
<td><mark>MMDDYYYY (occurs three time - use blanks if empty)</mark></td>
</tr>
<tr class="odd">
<td><mark>Character of service</mark></td>
<td><mark>Character Of Service</mark></td>
<td><mark>alpha</mark></td>
<td><mark>3</mark></td>
<td><mark>(occurs three times, use blanks if empty)<br />
(BAD_CONDUCT "BAD") (DISHONORABLE "DIS") (DISHONORABLE_FOR_VA_PURPOSES "DVA") (GENERAL "GEN") (HONORABLE "HON") (HONORABLE_FOR_VA_PURPOSES "HVA") (OTHER_THAN_HONORABLE "OTH") (UNCHARACTERIZED "UNC") (UNCHARACTERIZED_ENTRY_LEVEL "UEL") (UNDER_HONORABLE_CONDITIONS "UHC") (UNDESIRABLE "UND") (UNKNOWN "UNK") (UNSUITABLE "UNS") (UNVERIFIED "UNV")</mark></td>
</tr>
<tr class="even">
<td><mark>POW - number of days</mark></td>
<td><mark>calculate POW Capture Date - POW Release Date</mark></td>
<td><mark>alpha</mark></td>
<td><mark>4</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Total active service</mark></td>
<td><mark>Total Active Service</mark></td>
<td><mark>alpha</mark></td>
<td><mark>6</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Current folder location</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>3</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Verified SS indicator</mark></td>
<td><mark>Verified SSN Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>VA employee ID</mark></td>
<td><mark>VA Employee</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Vietnam service indicator</mark></td>
<td><mark>Vietnam Service Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Disability indicator</mark></td>
<td><mark>Disability Decision</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Medal of honor indicator</mark></td>
<td><mark>Medal Of Honor</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Active duty training indicator</mark></td>
<td><mark>Active Duty Training Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Sex</mark></td>
<td><mark>Sex Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Guardianship case indicator</mark></td>
<td><mark>Guardianship</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Incompetent indicator</mark></td>
<td><mark>Competency Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>C&amp;P record indicator</mark></td>
<td><mark>blank</mark></td>
<td><mark>blank</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>Service data verified indicator</mark></td>
<td><mark>Verified Svc. Data</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="even">
<td><mark>Homeless veteran indicator</mark></td>
<td><mark>Homeless Veteran Indicator</mark></td>
<td><mark>alpha</mark></td>
<td><mark>1</mark></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>HINQ end of string delimiter</mark></td>
<td><mark>NNNN</mark></td>
<td><mark>alpha</mark></td>
<td><mark>4</mark></td>
<td><mark>hard code NNNN for end of string</mark></td>
</tr>
</tbody>
</table>