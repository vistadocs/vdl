---
title: ACKQ*3*12 Audiometric Exam Module Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Audiometric Exam Module
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3*12
group_key: "ACKQ:ACKQ:3"
file_numbers: []
security_keys: []
menu_options: 4
description: "The Audiometric Exam Module (ACKQ\3.0\3) was developed for Audiology and Speech Pathology Service (ASPS) to simplify and enhance the entry, display and use of information obtained during the Audiometric exam of a patient. This module is comprised of two distinct application functionalities: the Audi"
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - threshold
  - table
  - initial
  - contents
  - level
  - mask
  - final
  - thresh
  - ackqag
  - audiogram
page_count: 0
word_count: 6856
section_count: 30
table_count: 9
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

![](ackq-3-12-audiometric-exam-module-technical-manual/001.png)

Audiometric Exam Module

Technical Manual

Patch ACKQ\*3.0\*12

November 2005

V*ist*A Health Systems Design & Development

# # # Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # Preface](#preface)
  - [Purpose](#purpose)
  - [Scope of Manual](#scope-of-manual)
  - [Audience](#audience)
  - [Benefits](#benefits)
  - [Related Manuals](#related-manuals)
- [# # # # # # # Introduction](#introduction)
  - [Orientation](#orientation)
  - [Obtaining online technical information](#obtaining-online-technical-information)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Required Site-specific Data](#required-site-specific-data)
  - [Installation Process](#installation-process)
- [# # Overview of the Process Logic](#overview-of-the-process-logic)
  - [Enter Edit Audiogram Data](#enter-edit-audiogram-data)
  - [Transmission of Audiometric data](#transmission-of-audiometric-data)
    - [## Audiogram Display](#audiogram-display)
- [# # # # # Files](#files)
  - [Audiometric Exam Data : ^ACK(509850.9](#audiometric-exam-data-ack5098509)
  - [Files Referenced in ^ACK(509850.9](#files-referenced-in-ack5098509)
  - [Routines](#routines)
  - [Delphi Routines](#delphi-routines)
- [# # # Exported Options](#exported-options)
  - [ACKQROES3 - Audiogram Display](#ackqroes3-audiogram-display)
  - [ACKQROES3E - Audiogram Edit](#ackqroes3e-audiogram-edit)
- [# Archiving and Purging](#archiving-and-purging)
- [## ^ACK(509850.9,](#ack5098509)
- [# APIs](#apis)
  - [Called routines, entry points, and APIs](#called-routines-entry-points-and-apis)
    - [START^ACKQAG01](#startackqag01)
    - [TITLE^ACKQAG01(USER)](#titleackqag01user)
    - [GETDATA^ACKQAG02](#getdataackqag02)
    - [START^ACKQAG02](#startackqag02)
    - [START^ACKQAG03](#startackqag03)
    - [GETDATA^ACKQAG04](#getdataackqag04)
    - [START^ACKQAG04](#startackqag04)
    - [ACKEXIST^ACKQAG05](#ackexistackqag05)
    - [DFNIN^ACKQAG05](#dfninackqag05)
    - [NEWMSG^ACKQAG05](#newmsgackqag05)
    - [GETDATA^ACKQAG06(ACKQI, ACKI)](#getdataackqag06ackqi-acki)
    - [LOGIC^ACKQAG06(A1,A2,A3,A4,A5,A6,A7)](#logicackqag06a1a2a3a4a5a6a7)
  - [RPCs](#rpcs)
    - [ACKQROES](#ackqroes)
    - [ACKQAUD1](#ackqaud1)
    - [ACKQAUD2](#ackqaud2)
- [# # External Relations](#external-relations)
  - [Standalone Functionality](#standalone-functionality)
  - [Recommended Desktop Minimums](#recommended-desktop-minimums)
  - [Integration Agreements](#integration-agreements)
- [# Internal Relations](#internal-relations)
- [## M routines:](#m-routines)
  - [Delphi routines:](#delphi-routines-1)
  - [Module Variables](#module-variables)
  - [SAC exemptions and approval dates](#sac-exemptions-and-approval-dates)
- [# # Glossary](#glossary)
- [## Acronyms](#acronyms)
- [# # Appendices](#appendices)
  - [A: Determining Series Values To Place On Display](#a-determining-series-values-to-place-on-display)
  - [B: Calculation Of PB MAX And PI/PB](#b-calculation-of-pb-max-and-pipb)
  - [C: Sample Form 2364](#c-sample-form-2364)
  - [D: Message Box Errors](#d-message-box-errors)
- [# Index](#index)
- [ACKQAG01, 26, 33](#ackqag01-26-33)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiometric Exam Module (ACKQ\*3.0\*3) was developed for Audiology and Speech Pathology Service (ASPS) to simplify and enhance the entry, display and use of information obtained during the Audiometric exam of a patient. This module is comprised of two distinct application functionalities: the Audiogram Edit function and the Audiogram Display function. Both of these applications have been enhanced in patch ACKQ\*3.0\*12.

The Audiogram Edit function is a Windows based software application that allows clinicians to enter, edit or view a patient's audiogram exam information from the Computerized Patient Record System (CPRS) Tools menu or from the end user's desktop. Using this function, a new audiogram record can be entered, or an existing one can be edited.

Completed and signed records are stored in a local QUASAR global (“^ACK(509850.9,”). The records are also transmitted from this application to the Denver Distribution Center (DDC) through the V*ist*A MailMan system for inclusion with orders for hearing aids and repairs when ordered through the V*ist*A Remote Order Entry System (ROES) package.

The Audiogram Display function is a Windows based software application that allows clinicians to view a patient's audiogram(s) from the CPRS Tools menu or from the desktop. It can also be called from the Audiogram Edit application, if both applications exist in the same directory and folder. This function presents the clinical information in a standard format recognized within the hearing industry.

## Scope of Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides technical information associated with maintenance of the Audiometric Exam module of the QUASAR package. It describes the modular components that comprise the user interface and underlying technical structure of the application.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is intended to aid Information Resource Management (IRM) in the installation and maintenance of this software.

## Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiometric Exam Module was designed to provide Audiologists and staff with an easy way to enter, store and utilize exam data. Once the data is entered and saved, they can immediately view the audiometric display. They can also copy or print the display(s). They can select displays from their CPRS Tools menu or from their desktop for easy retrieval and comparison. Completed, signed data entries are also transmitted to the Denver Distribution Center (DDC) for storage and use in ordering hearing aids and repair. Patch ACKQ\*3.0\*12 has added the ability to go from one record to another without entering the user verify code for each record.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Audiometric Module ACKQ\*3.0\*12 Installation Guide

Audiometric Module ACKQ\*3.0\*3 Security Manual

Audiometric Module ACKQ\*3.0\*12 User Manual

Audiometric Module ACKQ\*3.0\*12 Release Notes

# # # # # # # # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The caret (^), sometimes referred to as the Up-Arrow, is used as the standard delimiter for data segments.

Users that are not set up to use multiple broker environments will default to using BROKERSERVER and port 9200 in the production account. If they have access to multiple accounts, they will still have to select which one to connect to when going from the edit to the display. For this application, login should be accomplished using local V*ist*A Access and Verify codes. (Many users of this application also have DDC Access and Verify codes for access to the DDC Remote Inquiry System. These DDC codes are not applicable to the Audiometric Exam module.) If the user is entering the application from the CPRS Tools menu, a patient will already be selected. If accessing the application from the desktop, a patient will need to be selected. If a new audiogram is being entered, the lookup is from the local PATIENT file (#2), otherwise the patient will be selected from the AUDIOMETRIC EXAM file entries. With patch 3.0\*12 the user will be able to go to additional records without having to re-enter the application each time.

## Obtaining online technical information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Websites:

V*ist*A RPC Broker Download site: <span class="mark">REDACTED</span>

V*ist*A document library: <http://www.va.gov/vdl/>

Use FileMan's DATA DICTIONARY UTILITIES option to print out the data dictionary for the file. After selecting this option, select the LIST FILE ATTRIBUTES option and the STANDARD, BRIEF or CONDENSED versions. The CONDENSED version is highly recommended as there are a large number of fields in the file.

> Use the KIDS BUILD FILE PRINT option if you would like a complete listing of package components exported with this software.

> KIDS Kernel Installation & Distribution

> Utilities ...

> Build File Print

Use the KIDS INSTALL FILE PRINT option if you'd like to print out the results of the installation process.

KIDS Kernel Installation & Distribution

Utilities ...

Install File Print

XUPRROU prints a list of any or all of the ACKQAG0\* routines.

Programmer Options ...

Routine Tools ...

List Routines

All Routines? No =\> No

Routine: ACKQAG0\*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Site-specific Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*ist*A system must have MailMan connectivity to the DDC (i.e., DDC.VA.GOV domain open) in order to transmit the audiometric data to the DDC.

The site's V*ist*A Server must be running the VA's RPC Broker listener.

The desktop system must be running a Windows operating system (WinNT, Win2K, WinXP).

The V*ist*A RPC Broker client must be installed and functional on the desktop system.

## Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software requires that the RPC Broker V1.1 be installed on any workstation on which the programs will be executed. If the workstation can already connect successfully via CPRS, BCMA, or PCMM, then the RPC Broker has already been installed. If the RPC Broker needs to be installed, please refer to the RPC Broker website for configuration information and to download the installation file: <span class="mark">REDACTED</span>

The CPRS application must be installed and functional on the V*ist*A server and desktop systems, to allow the audiogram applications to have access from the CPRS Tools menu. Optionally, the audiogram applications may be run directly from the desktop when linked to the executables in a server directory or on the local machine.

Install the KIDS build (ACKQ\*3.0\*12) into the local system.

The KIDS build will install:

- The M routines ACKQAG01, ACKQAG02, ACKQAG03, ACKQAG04, ACKQAG05, ACKQAG06 and ACKQAG08.
- The Remote Procedures ACKQAUD1, ACKQAUD2, ACKQROES, and ACKQROESD.

The options, ACKQROES3(view audiogram) and ACKQROES3E(edit audiogram), will be set up in file 19 and need to be assigned to a common menu option, or as a secondary menu option for the individual users. The programs will generate an error while context is being established, if not assigned.

The executables (ACKQROES3.exe and ACKQROES3E.exe) are contained in the zip file (Audiograms.zip). They can be installed in a network directory and a link placed on the desktop, or installed on the desktop system. Both of the generated executables need to be in the same directory, in order for the Enter Edit program to call the Display program directly.

For detailed installation instructions, refer to the *Audiometric Exam Module Installation Guide*

# # # Overview of the Process Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical staff with an overview of the processing functions in each module. In the next few pages, flow chart logic is accompanied by related routines and remote procedure calls supporting that logic.

Functions performed by these processes are:

- Entry of clinical audiogram data (creation of new audiogram record or modification of existing unsigned record)
- Transmission of audiogram record to the DDC
- Display of audiogram and associated functions

From CPRS, the patient DFN may be passed to the application as DFN=%DFN. If the DFN is provided, the program will default to that DFN instead of prompting for a patient lookup.

## Enter Edit Audiogram Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ackq-3-12-audiometric-exam-module-technical-manual/002.png)

## Transmission of Audiometric data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ackq-3-12-audiometric-exam-module-technical-manual/003.png)

### ## Audiogram Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ackq-3-12-audiometric-exam-module-technical-manual/004.png)

# # # # # # Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the specific data elements and their attributes in the Audiometric Exam Data file. A number of audiology-specific acronyms and abbreviations are used in the field names. Please reference the Glossary for full definitions.

## Audiometric Exam Data : ^ACK(509850.9 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A complete listing of fields and attributes can be obtained by using the FileMan 'List File Attributes' option, selecting the 'Standard' or 'Brief' format. The Condensed listing follows:

Field Field Name \[node;position\]

.01 DATE/TIME OF VISIT (RD), \[0;1\]

.02 PATIENT (P2'), \[0;2\]

.03 EXAMINING AUDIOLOGIST (P200'), \[0;3\]

.04 REFERRAL SOURCE (P44'), \[0;4\]

.05 AGE AT VISIT (N), \[0;5\]

.06 \*VA ELIGIBILITY STATUS (S), \[0;6\]

.07 TYPE OF VISIT (F), \[0;7\]

.08 TRANSDUCER TYPE (S), \[0;8\]

.09 DATE SIGNED (D), \[0;9\]

.1 TESTING STATION (P4'), \[0;10\]

.11 ICN (F), \[0;11\]

.12 DATE SENT TO DDC (D), \[0;12\]

.13 MESSAGE NUMBER (P3.9'), \[0;13\]

.14 CLAIM NUMBER (F), \[0,14\]

.15 RETRANSMISSION DATE (D),\[0;15\]

.16 RETRANSMISSION USER (P200),\[0;16\]

1.01 RIGHT FOUR FREQUENCY PTA (NJ3,0), \[1;1\]

1.02 LEFT FOUR FREQUENCY PTA (NJ3,0), \[1;2\]

1.03 RIGHT THREE FREQUENCY PTA (NJ3,0), \[1;3\]

1.04 LEFT THREE FREQUENCY PTA (NJ3,0), \[1;4\]

1.05 RIGHT TWO FREQUENCY PTA (NJ3,0), \[1;5\]

1.06 LEFT TWO FREQUENCY PTA (NJ6,2), \[1;6\]

1.07 RIGHT MCL (NJ3,0), \[1;7\]

1.08 RIGHT UCL (NJ3,0), \[1;8\]

1.09 LEFT MCL (NJ3,0), \[1;9\]

1.1 LEFT UCL (NJ3,0), \[1;10\]

1.11 R TYMPANOGRAM TYPE (S),\[1;11\]

1.12 L TYMPANOGRAM TYPE (S),\[1;12\]

10.01 INITIAL A/C THRESHOLD R 125 (NJ3,0), \[10;1\]

10.02 INITIAL A/C THRESHOLD R 250 (NJ3,0), \[10;2\]

10.03 INITIAL A/C THRESHOLD R 500 (NJ3,0), \[10;3\]

10.04 INITIAL A/C THRESHOLD R 750 (NJ3,0), \[10;4\]

10.05 INITIAL A/C THRESHOLD R 1000 (NJ3,0), \[10;5\]

10.06 INITIAL A/C THRESHOLD R 1500 (NJ3,0), \[10;6\]

10.07 INITIAL A/C THRESHOLD R 2000 (NJ3,0), \[10;7\]

10.08 INITIAL A/C THRESHOLD R 3000 (NJ3,0), \[10;8\]

10.09 INITIAL A/C THRESHOLD R 4000 (NJ3,0), \[10;9\]

10.1 INITIAL A/C THRESHOLD R 6000 (NJ3,0), \[10;10\]

10.11 INITIAL A/C THRESHOLD R 8000 (NJ3,0), \[10;11\]

10.12 INITIAL A/C THRESHOLD R 12000 (NJ3,0), \[10;12\]

11.01 \*INITIAL A/C THRESH TAG R 125 (S), \[11;1\]

11.02 \*INITIAL A/C THRESH TAG R 250 (S), \[11;2\]

11.03 \*INITIAL A/C THRESH TAG R 500 (S), \[11;3\]

11.04 \*INITIAL A/C THRESH TAG R 750 (S), \[11;4\]

11.05 \*INITIAL A/C THRESH TAG R 1000 (S), \[11;5\]

11.06 \*INITIAL A/C THRESH TAG R 1500 (S), \[11;6\]

11.07 \*INITIAL A/C THRESH TAG R 2000 (S), \[11;7\]

11.08 \*INITIAL A/C THRESH TAG R 3000 (S), \[11;8\]

11.09 \*INITIAL A/C THRESH TAG R 4000 (S), \[11;9\]

11.1 \*INITIAL A/C THRESH TAG R 6000 (S), \[11;10\]

11.11 \*INITIAL A/C THRESH TAG R 8000 (S), \[11;11\]

11.12 \*INITIAL A/C THRESH TAG R 12000 (S), \[11;12\]

15.01 RETEST A/C THRESHOLD R 125 (NJ3,0), \[10;1\]

15.02 RETEST A/C THRESHOLD R 250 (NJ3,0), \[10;2\]

15.03 RETEST A/C THRESHOLD R 500 (NJ3,0), \[10;3\]

15.04 RETEST A/C THRESHOLD R 750 (NJ3,0), \[10;4\]

15.05 RETEST A/C THRESHOLD R 1000 (NJ3,0), \[10;5\]

15.06 RETEST A/C THRESHOLD R 1500 (NJ3,0), \[10;6\]

15.07 RETEST A/C THRESHOLD R 2000 (NJ3,0), \[10;7\]

15.08 RETEST A/C THRESHOLD R 3000 (NJ3,0), \[10;8\]

15.09 RETEST A/C THRESHOLD R 4000 (NJ3,0), \[10;9\]

15.1 RETEST A/C THRESHOLD R 6000 (NJ3,0), \[10;10\]

15.11 RETEST A/C THRESHOLD R 8000 (NJ3,0), \[10;11\]

20.01 FINAL A/C THRESHOLD R 125 (NJ3,0), \[20;1\]

20.02 FINAL A/C THRESHOLD R 250 (NJ3,0), \[20;2\]

20.03 FINAL A/C THRESHOLD R 500 (NJ3,0), \[20;3\]

20.04 FINAL A/C THRESHOLD R 750 (NJ3,0), \[20;4\]

20.05 FINAL A/C THRESHOLD R 1000 (NJ3,0), \[20;5\]

20.06 FINAL A/C THRESHOLD R 1500 (NJ3,0), \[20;6\]

20.07 FINAL A/C THRESHOLD R 2000 (NJ3,0), \[20;7\]

20.08 FINAL A/C THRESHOLD R 3000 (NJ3,0), \[20;8\]

20.09 FINAL A/C THRESHOLD R 4000 (NJ3,0), \[20;9\]

20.1 FINAL A/C THRESHOLD R 6000 (NJ3,0), \[20;10\]

20.11 FINAL A/C THRESHOLD R 8000 (NJ3,0), \[20;11\]

20.12 FINAL A/C THRESHOLD R 12000 (NJ3,0), \[20;12\]

21.01 \*REPEAT A/C THRESH TAG R 125 (S), \[21;1\]

21.02 \*REPEAT A/C THRESH TAG R 250 (S), \[21;2\]

21.03 \*REPEAT A/C THRESH TAG R 500 (S), \[21;3\]

21.04 \*REPEAT A/C THRESH TAG R 750 (S), \[21;4\]

21.05 \*REPEAT A/C THRESH TAG R 1000 (S), \[21;5\]

21.06 \*REPEAT A/C THRESH TAG R 1500 (S), \[21;6\]

21.07 \*REPEAT A/C THRESH TAG R 2000 (S), \[21;7\]

21.08 \*REPEAT A/C THRESH TAG R 3000 (S), \[21;8\]

21.09 \*REPEAT A/C THRESH TAG R 4000 (S), \[21;9\]

21.1 \*REPEAT A/C THRESH TAG R 6000 (S), \[21;10\]

21.11 \*REPEAT A/C THRESH TAG R 8000 (S), \[21;11\]

21.12 \*REPEAT A/C THRESH TAG R 12000 (S), \[21;12\]

30.01 INITIAL A/C THRESHOLD L 125 (NJ3,0), \[30;1\]

30.02 INITIAL A/C THRESHOLD L 250 (NJ3,0), \[30;2\]

30.03 INITIAL A/C THRESHOLD L 500 (NJ3,0), \[30;3\]

30.04 INITIAL A/C THRESHOLD L 750 (NJ3,0), \[30;4\]

30.05 INITIAL A/C THRESHOLD L 1000 (NJ3,0), \[30;5\]

30.06 INITIAL A/C THRESHOLD L 1500 (NJ3,0), \[30;6\]

30.07 INITIAL A/C THRESHOLD L 2000 (NJ3,0), \[30;7\]

30.08 INITIAL A/C THRESHOLD L 3000 (NJ3,0), \[30;8\]

30.09 INITIAL A/C THRESHOLD L 4000 (NJ3,0), \[30;9\]

30.1 INITIAL A/C THRESHOLD L 6000 (NJ3,0), \[30;10\]

30.11 INITIAL A/C THRESHOLD L 8000 (NJ3,0), \[30;11\]

30.12 INITIAL A/C THRESHOLD L 12000 (NJ3,0), \[30;12\]

31.01 \*INITIAL A/C THRESH TAG L 125 (S), \[31;1\]

31.02 \*INITIAL A/C THRESH TAG L 250 (S), \[31;2\]

31.03 \*INITIAL A/C THRESH TAG L 500 (S), \[31;3\]

31.04 \*INITIAL A/C THRESH TAG L 750 (S), \[31;4\]

31.05 \*INITIAL A/C THRESH TAG L 1000 (S), \[31;5\]

31.06 \*INITIAL A/C THRESH TAG L 1500 (S), \[31;6\]

31.07 \*INITIAL A/C THRESH TAG L 2000 (S), \[31;7\]

31.08 \*INITIAL A/C THRESH TAG L 3000 (S), \[31;8\]

31.09 \*INITIAL A/C THRESH TAG L 4000 (S), \[31;9\]

31.1 \*INITIAL A/C THRESH TAG L 6000 (S), \[31;10\]

31.11 \*INITIAL A/C THRESH TAG L 8000 (S), \[31;11\]

31.12 \*INITIAL A/C THRESH TAG L 12000 (S), \[31;12\]

35.01 RETEST A/C THRESHOLD R 125 (NJ3,0), \[10;1\]

35.02 RETEST A/C THRESHOLD R 250 (NJ3,0), \[10;2\]

35.03 RETEST A/C THRESHOLD R 500 (NJ3,0), \[10;3\]

35.04 RETEST TEST A/C THRESHOLD R 750 (NJ3,0), \[10;4\]

35.05 RETEST A/C THRESHOLD R 1000 (NJ3,0), \[10;5\]

35.06 RETEST A/C THRESHOLD R 1500 (NJ3,0), \[10;6\]

35.07 RETEST A/C THRESHOLD R 2000 (NJ3,0), \[10;7\]

35.08 RETEST A/C THRESHOLD R 3000 (NJ3,0), \[10;8\]

35.09 RETEST A/C THRESHOLD R 4000 (NJ3,0), \[10;9\]

35.1 RETEST A/C THRESHOLD R 6000 (NJ3,0), \[10;10\]

35.11 RETEST A/C THRESHOLD R 8000 (NJ3,0), \[10;11\]

40.01 FINAL A/C THRESHOLD L 125 (NJ3,0), \[40;1\]

40.02 FINAL A/C THRESHOLD L 250 (NJ3,0), \[40;2\]

40.03 FINAL A/C THRESHOLD L 500 (NJ3,0), \[40;3\]

40.04 FINAL A/C THRESHOLD L 750 (NJ3,0), \[40;4\]

40.05 FINAL A/C THRESHOLD L 1000 (NJ3,0), \[40;5\]

40.06 FINAL A/C THRESHOLD L 1500 (NJ3,0), \[40;6\]

40.07 FINAL A/C THRESHOLD L 2000 (NJ3,0), \[40;7\]

40.08 FINAL A/C THRESHOLD L 3000 (NJ3,0), \[40;8\]

40.09 FINAL A/C THRESHOLD L 4000 (NJ3,0), \[40;9\]

40.1 FINAL A/C THRESHOLD L 6000 (NJ3,0), \[40;10\]

40.11 FINAL A/C THRESHOLD L 8000 (NJ3,0), \[40;11\]

40.12 FINAL A/C THRESHOLD L 12000 (NJ3,0), \[40;12\]

41.01 \* REPEAT A/C THRESH TAG L 125 (S), \[41;1\]

41.02 \* REPEAT A/C THRESH TAG L 250 (S), \[41;2\]

41.03 \* REPEAT A/C THRESH TAG 500 (S), \[41;3\]

41.04 \* REPEAT A/C THRESH TAG L 750 (S), \[41;4\]

41.05 \* REPEAT A/C THRESH TAG L 1000 (S), \[41;5\]

41.06 \* REPEAT A/C THRESHOLD TAG 1500 (S), \[41;6\]

41.07 \* REPEAT A/C THRESH TAG L 2000 (S), \[41;7\]

41.08 \* REPEAT A/C THRESH TAG L 3000 (S), \[41;8\]

41.09 \* REPEAT A/C THRESH TAG L 4000 (S), \[41;9\]

41.1 \* REPEAT A/C THRESH TAG L 6000 (S), \[41;10\]

41.11 \* REPEAT A/C THRESH TAG L 8000 (S), \[41;11\]

41.12 \* REPEAT A/C THRESH TAG L 12000 (S), \[41;12\]

50.01 \* INITIAL A/C MASK LEVEL R 125 (NJ3,0), \[50;1\]

50.02 \* INITIAL A/C MASK LEVEL R 250 (NJ3,0), \[50;2\]

50.03 \* INITIAL A/C MASK LEVEL R 500 (NJ3,0), \[50;3\]

50.04 \* INITIAL A/C MASK LEVEL R 750 (NJ3,0), \[50;4\]

50.05 \* INITIAL A/C MASK LEVEL R 1000 (NJ3,0), \[50;5\]

50.06 \* INITIAL A/C MASK LEVEL R 1500 (NJ3,0), \[50;6\]

50.07 \* INITIAL A/C MASK LEVEL R 2000 (NJ3,0), \[50;7\]

50.08 \* INITIAL A/C MASK LEVEL R 3000 (NJ3,0), \[50;8\]

50.09 \* INITIAL A/C MASK LEVEL R 4000 (NJ3,0), \[50;9\]

50.1 \* INITIAL A/C MASK LEVEL R 6000 (NJ3,0), \[50;10\]

50.11 \* INITIAL A/C MASK LEVEL R 8000 (NJ3,0), \[50;11\]

50.12 \* INITIAL A/C MASK LEVEL R 12000 (NJ3,0), \[50;12\]

51.01 FINAL A/C MASK LEVEL R 125 (NJ3,0), \[51;1\]

51.02 FINAL A/C MASK LEVEL R 250 (NJ3,0), \[51;2\]

51.03 FINAL A/C MASK LEVEL R 500 (NJ3,0), \[51;3\]

51.04 FINAL A/C MASK LEVEL R 750 (NJ3,0), \[51;4\]

51.05 FINAL A/C MASK LEVEL R 1000 (NJ3,0), \[51;5\]

51.06 FINAL A/C MASK LEVEL R 1500 (NJ3,0), \[51;6\]

51.07 FINAL A/C MASK LEVEL R 2000 (NJ3,0), \[51;7\]

51.08 FINAL A/C MASK LEVEL R 3000 (NJ3,0), \[51;8\]

51.09 FINAL A/C MASK LEVEL R 4000 (NJ3,0), \[51;9\]

51.1 FINAL A/C MASK LEVEL R 6000 (NJ3,0), \[51;10\]

51.11 FINAL A/C MASK LEVEL R 8000 (NJ3,0), \[51;11\]

51.12 FINAL A/C MASK LEVEL R 12000 (NJ3,0), \[51;12\]

60.01 \* INITIAL A/C MASK LEVEL L 125 (NJ3,0), \[60;1\]

60.02 \* INITIAL A/C MASK LEVEL L 250 (NJ3,0), \[60;2\]

60.03 \* INITIAL A/C MASK LEVEL L 500 (NJ3,0), \[60;3\]

60.04 \* INITIAL A/C MASK LEVEL L 750 (NJ3,0), \[60;4\]

60.05 \* INITIAL A/C MASK LEVEL L 1000 (NJ3,0), \[60;5\]

60.06 \* INITIAL A/C MASK LEVEL L 1500 (NJ3,0), \[60;6\]

60.07 \* INITIAL A/C MASK LEVEL L 2000 (NJ3,0), \[60;7\]

60.08 \* INITIAL A/C MASK LEVEL L 3000 (NJ3,0), \[60;8\]

60.09 \* INITIAL A/C MASK LEVEL L 4000 (NJ3,0), \[60;9\]

60.1 \* INITIAL A/C MASK LEVEL L 6000 (NJ3,0), \[60;10\]

60.11 \* INITIAL A/C MASK LEVEL L 8000 (NJ3,0), \[60;11\]

60.12 \* INITIAL A.C MASK LEVEL L 12000 (NJ3,0), \[60;12\]

61.01 FINAL A/C MASK LEVEL L 125 (NJ3,0), \[61;1\]

61.02 FINAL A/C MASK LEVEL L 250 (NJ3,0), \[61;2\]

61.03 FINAL A/C MASK LEVEL L 500 (NJ3,0), \[61;3\]

61.04 FINAL A/C MASK LEVEL L 750 (NJ3,0), \[61;4\]

61.05 FINAL A/C MASK LEVEL L 1000 (NJ3,0), \[61;5\]

61.06 FINAL A/C MASK LEVEL L 1500 (NJ3,0), \[61;6\]

61.07 FINAL A/C MASK LEVEL L 2000 (NJ3,0), \[61;7\]

61.08 FINAL A/C MASK LEVEL L 3000 (NJ3,0), \[61;8\]

61.09 FINAL A/C MASK LEVEL L 4000 (NJ3,0), \[61;9\]

61.1 FINAL A/C MASK LEVEL L 6000 (NJ3,0), \[61;10\]

61.11 FINAL A/C MASK LEVEL L 8000 (NJ3,0), \[61;11\]

61.12 FINAL A/C MASK LEVEL L 12000 (NJ3,0), \[61;12\]

70.01 INITIAL B/C THRESHOLD R 250 (NJ2,0), \[70;1\]

70.02 INITIAL B/C THRESHOLD R 500 (NJ2,0), \[70;2\]

70.03 INITIAL B/C THRESHOLD R 750 (NJ2,0), \[70;3\]

70.04 INITIAL B/C THRESHOLD R 1000 (NJ2,0), \[70;4\]

70.05 INITIAL B/C THRESHOLD R 1500 (NJ2,0), \[70;5\]

70.06 INITIAL B/C THRESHOLD R 2000 (NJ2,0), \[70;6\]

70.07 INITIAL B/C THRESHOLD R 3000 (NJ2,0), \[70;7\]

70.08 INITIAL B/C THRESHOLD R 4000 (NJ2,0), \[70;8\]

70.09 INITIAL B/C THRESHOLD R 6000 (NJ2,0), \[70;9\]

71.01 \* INITIAL B/C THRESH TAG R 250 (S), \[71;1\]

71.02 \* INITIAL B/C THRESH TAG R 500 (S), \[71;2\]

71.03 \* INITIAL B/C THRESH TAG R 750 (S), \[71;3\]

71.04 \* INITIAL B/C THRESH TAG R 1000 (S), \[71;4\]

71.05 \* INITIAL B/C THRESH TAG R 1500 (S), \[71;5\]

71.06 \* INITIAL B/C THRESH TAG R 2000 (S), \[71;6\]

71.07 \* INITIAL B/C THRESH TAG R 3000 (S), \[71;7\]

71.08 \* INITIAL B/C THRESH TAG R 4000 (S), \[71;8\]

71.09 \* INITIAL B/C THRESH TAG R 6000 (S), \[71;9\]

72.01 RETEST B/C THRESHOLD R 250 (NJ2,0), \[75;1\]

72.02 RETEST B/C THRESHOLD R 500 (NJ2,0), \[75;2\]

72.03 RETEST B/C THRESHOLD R 750 (NJ2,0), \[75;3\]

72.04 RETEST B/C THRESHOLD R 1000 (NJ2,0), \[75;4\]

72.05 RETEST B/C THRESHOLD R 1500 (NJ2,0), \[75;5\]

72.06 RETEST B/C THRESHOLD R 2000 (NJ2,0), \[75;6\]

72.07 RETEST B/C THRESHOLD R 3000 (NJ2,0), \[75;7\]

72.08 RETEST B/C THRESHOLD R 4000 (NJ2,0), \[75;8\]

72.09 RETEST B/C THRESHOLD R 6000 (NJ2,0), \[75;9\]

75.01 FINAL B/C THRESHOLD R 250 (NJ2,0), \[75;1\]

75.02 FINAL B/C THRESHOLD R 500 (NJ2,0), \[75;2\]

75.03 FINAL B/C THRESHOLD R 750 (NJ2,0), \[75;3\]

75.04 FINAL B/C THRESHOLD R 1000 (NJ2,0), \[75;4\]

75.05 FINAL B/C THRESHOLD R 1500 (NJ2,0), \[75;5\]

75.06 FINAL B/C THRESHOLD R 2000 (NJ2,0), \[75;6\]

75.07 FINAL B/C THRESHOLD R 3000 (NJ2,0), \[75;7\]

75.08 FINAL B/C THRESHOLD R 4000 (NJ2,0), \[75;8\]

75.09 FINAL B/C THRESHOLD R 6000 (NJ2,0), \[75;9\]

76.01 \*REPEAT B/C THRESH TAG R 250 (S), \[76;1\]

76.02 \*REPEAT B/C THRESH TAG R 500 (S), \[76;2\]

76.03 \*REPEAT B/C THRESH TAG R 750 (S), \[76;3\]

76.04 \*REPEAT B/C THRESH TAG R 1000 (S), \[76;4\]

76.05 \*REPEAT B/C THRESH TAG R 1500 (S), \[76;5\]

76.06 \*REPEAT B/C THRESH TAG R 2000 (S), \[76;6\]

76.07 \*REPEAT B/C THRESH TAG R 3000 (S), \[76;7\]

76.08 \* REPEAT B/C THRESH TAG R 4000 (S), \[76;8\]

76.09 \*REPEAT B/C THRESH TAG R 6000 (S), \[76;9\]

80.01 INITIAL B/C THRESHOLD L 250 (NJ2,0), \[80;1\]

80.02 INITIAL B/C THRESHOLD L 500 (NJ2,0), \[80;2\]

80.03 INITIAL B/C THRESHOLD L 750 (NJ2,0), \[80;3\]

80.04 INITIAL B/C THRESHOLD L 1000 (NJ2,0), \[80;4\]

80.05 INITIAL B/C THRESHOLD L 1500 (NJ2,0), \[80;5\]

80.06 INITIAL B/C THRESHOLD L 2000 (NJ2,0), \[80;6\]

80.07 INITIAL B/C THRESHOLD L 3000 (NJ2,0), \[80;7\]

80.08 INITIAL B/C THRESHOLD L 4000 (NJ2,0), \[80;8\]

80.09 INITIAL B/C THRESHOLD L 6000 (NJ2,0), \[80;9\]

81.01 \*INITIAL B/C THRESH TAG L 250 (S), \[81;1\]

81.02 \*INITIAL B/C THRESH TAG L 500 (S), \[81;2\]

81.03 \*INITIAL B/C THRESH TAG L 750 (S), \[81;3\]

81.04 \*INITIAL B/C THRESH TAG L 1000 (S), \[81;4\]

81.05 \* INITIAL B/C THRESH TAG L 1500 (S), \[81;5\]

81.06 \*INITIAL B/C THRESH TAG L 2000 (S), \[81;6\]

81.07 \*INITIAL B/C THRESH TAG L 3000 (S), \[81;7\]

81.08 \*INITIAL B/C THRESH TAG L 4000 (S), \[81;8\]

81.09 \*INITIAL B/C THRESH TAG L 6000 (S), \[81;9\]

85.01 FINAL B/C THRESHOLD L 250 (NJ2,0), \[85;1\]

85.02 FINAL B/C THRESHOLD L 500 (NJ2,0), \[85;2\]

85.03 FINAL B/C THRESHOLD L 750 (NJ2,0), \[85;3\]

85.04 FINAL B/C THRESHOLD L 1000 (NJ2,0), \[85;4\]

85.05 FINAL B/C THRESHOLD L 1500 (NJ2,0), \[85;5\]

85.06 FINAL B/C THRESHOLD L 2000 (NJ2,0), \[85;6\]

85.07 FINAL B/C THRESHOLD L 3000 (NJ2,0), \[85;7\]

85.08 FINAL B/C THRESHOLD L 4000 (NJ2,0), \[85;8\]

85.09 FINAL B/C THRESHOLD L 6000 (NJ2,0), \[85;9\]

86.01 \* REPEAT B/C THRESH TAG L 250 (S), \[86;1\]

86.02 \* REPEAT B/C THRESH TAG L 500 (S), \[86;2\]

86.03 \* REPEAT B/C THRESH TAG L 750 (S), \[86;3\]

86.04 \* REPEAT B/C THRESH TAG L 1000 (S), \[86;4\]

86.05 \* REPEAT B/C THRESH TAG L 1500 (S), \[86;5\]

86.06 \* REPEAT B/C THRESH TAG L 2000 (S), \[86;6\]

86.07 \* REPEAT B/C THRESH TAG L 3000 (S), \[86;7\]

86.08 \* REPEAT B/C THRESH TAG L 4000 (S), \[86;8\]

86.09 \* REPEAT B/C THRESH TAG L 6000 (S), \[86;9\]

90.01 \* INITIAL B/C MASK LEVEL R 250 (NJ3,0), \[90;1\]

90.02 \* INITIAL B/C MASK LEVEL R 500 (NJ3,0), \[90;2\]

90.03 \* INITIAL B/C MASK LEVEL R 750 (NJ3,0), \[90;3\]

90.04 \* INITIAL B/C MASK LEVEL R 1000 (NJ3,0), \[90;4\]

90.05 \* INITIAL B/C MASK LEVEL R 1500 (NJ3,0), \[90;5\]

90.06 \* INITIAL B/C MASK LEVEL R 2000 (NJ3,0), \[90;6\]

90.07 \* INITIAL B/C MASK LEVEL R 3000 (NJ3,0), \[90;7\]

90.08 \* INITIAL B/C MASK LEVEL R 4000 (NJ3,0), \[90;8\]

90.09 \* INITIAL B/C MASK LEVEL R 6000 (NJ3,0), \[90;9\]

91.01 FINAL B/C MASK LEVEL R 250 (NJ3,0), \[91;1\]

91.02 FINAL B/C MASK LEVEL R 500 (NJ3,0), \[91;2\]

91.03 FINAL B/C MASK LEVEL R 750 (NJ3,0), \[91;3\]

91.04 FINAL B/C MASK LEVEL R 1000 (NJ3,0), \[91;4\]

91.05 FINAL B/C MASK LEVEL R 1500 (NJ3,0), \[91;5\]

91.06 FINAL B/C MASK LEVEL R 2000 (NJ3,0), \[91;6\]

91.07 FINAL B/C MASK LEVEL R 3000 (NJ3,0), \[91;7\]

91.08 FINAL B/C MASK LEVEL R 4000 (NJ3,0), \[91;8\]

91.09 FINAL B/C MASK LEVEL R 6000 (NJ3,0), \[91;9\]

100.01 \* INITIAL B/C MASK LEVEL L 250 (NJ3,0), \[100;1\]

100.02 \* INITIAL B/C MASK LEVEL L 500 (NJ3,0), \[100;2\]

100.03 \* INITIAL B/C MASK LEVEL L 750 (NJ3,0), \[100;3\]

100.04 \* INITIAL B/C MASK LEVEL L 1000 (NJ3,0), \[100;4\]

100.05 \* INITIAL B/C MASK LEVEL L 1500 (NJ3,0), \[100;5\]

100.06 \* INITIAL B/C MASK LEVEL L 2000 (NJ3,0), \[100;6\]

100.07 \* INITIAL B/C MASK LEVEL L 3000 (NJ3,0), \[100;7\]

100.08 \* INITIAL B/C MASK LEVEL L 4000 (NJ3,0), \[100;8\]

100.09 \* INITIAL B/C MASK LEVEL L 6000 (NJ3,0), \[100;9\]

101.01 FINAL B/C MASK LEVEL L 250 (NJ3,0), \[101;1\]

101.02 FINAL B/C MASK LEVEL L 500 (NJ3,0), \[101;2\]

101.03 FINAL B/C MASK LEVEL L 750 (NJ3,0), \[101;3\]

101.04 FINAL B/C MASK LEVEL L 1000 (NJ3,0), \[101;4\]

101.05 FINAL B/C MASK LEVEL L 1500 (NJ3,0), \[101;5\]

101.06 FINAL B/C MASK LEVEL L 2000 (NJ3,0), \[101;6\]

101.07 FINAL B/C MASK LEVEL L 3000 (NJ3,0), \[101;7\]

101.08 FINAL B/C MASK LEVEL L 4000 (NJ3,0), \[101;8\]

101.09 FINAL B/C MASK LEVEL L 6000 (NJ3,0), \[101;9\]

110.03 MATERIAL-1 (S), \[110;3\]

110.04 PERCENT CORRECT R-1 (NJ3,0), \[110;4\]

110.05 PRESENTATION METHOD R-1 (S), \[110;5\]

110.06 PRESENTATION LEVEL R-1 (NJ3,0), \[110;6\]

110.07 MASKING LEVEL R-1 (NJ3,0), \[110;7\]

110.08 \* WORD LIST R-2 (S), \[110;8\]

110.09 PERCENT CORRECT R-2 (NJ3,0), \[110;9\]

110.1 \* PRESENTATION METHOD R-2 (S), \[110;10\]

110.11 PRESENTATION LEVEL R-2 (NJ3,0), \[110;11\]

110.12 MASKING LEVEL R-2 (NJ3,0), \[110;12\]

110.13 \* WORD LIST R-3 (S), \[110;13\]

110.14 PERCENT CORRECT R-3 (NJ3,0), \[110;14\]

110.15 \* PRESENTATION METHOD R-3 (S), \[110;15\]

110.16 PRESENTATION LEVEL R-3 (NJ3,0), \[110;16\]

110.17 MASKING LEVEL R-3 (NJ3,0), \[110;17\]

110.18 \* WORD LIST R-4 (S), \[110;18\]

110.19 PERCENT CORRECT R-4 (NJ3,0), \[110;19\]

110.2 \* PRESENTATION METHOD R-4 (S), \[110;20\]

110.21 PRESENTATION LEVEL R-4 (NJ3,0), \[110;21\]

110.22 MASKING LEVEL R-4 (NJ3,0), \[110;22\]

110.23 \* WORD LIST R-5 (S), \[110;23\]

110.24 PERCENT CORRECT R-5 (NJ3,0), \[110;24\]

110.25 \* PRESENTATION METHOD R-5 (S), \[110;25\]

110.26 PRESENTATION LEVEL R-5 (NJ3,0), \[110;26\]

110.27 MASKING LEVEL R-5 (NJ3,0), \[110;27\]

110.28 LIST R-1 (F),\[110;28\]

110.29 LIST R-2 (F),\[110;29\]

110.3 LIST R-3 (F),\[110;30\]

110.31 LIST R-4 (F),\[110;31\]

110.32 LIST R-5 (F),\[110;32\]

111.03 MATERIAL L-1 (S), \[111;3\]

111.04 PERCENT CORRECT L-1 (NJ3,0), \[111;4\]

111.05 PRESENTATION METHOD L-1 (S), \[111;5\]

111.06 PRESENTATION LEVEL L-1 (NJ3,0), \[111;6\]

111.07 MASKING LEVEL L-1 (NJ3,0), \[111;7\]

111.08 \* WORD LIST L-2 (S), \[111;8\]

111.09 PERCENT CORRECT L-2 (NJ3,0), \[111;9\]

111.1 \* PRESENTATION METHOD L-2 (S), \[111;10\]

111.11 PRESENTATION LEVEL L-2 (NJ3,0), \[111;11\]

111.12 MASKING LEVEL L-2 (NJ3,0), \[111;12\]

111.13 \* WORD LIST L-3 (S), \[111;13\]

111.14 PERCENT CORRECT L-3 (NJ3,0), \[111;14\]

111.15 \* PRESENTATION METHOD L-3 (S), \[111;15\]

111.16 PRESENTATION LEVEL L-3 (NJ3,0), \[111;16\]

111.17 MASKING LEVEL L-3 (NJ3,0), \[111;17\]

111.18 \* WORD LIST L-4 (S), \[111;18\]

111.19 PERCENT CORRECT L-4 (NJ3,0), \[111;19\]

111.2 \* PRESENTATION METHOD L-4 (S), \[111;20\]

111.21 PRESENTATION LEVEL L-4 (NJ3,0), \[111;21\]

111.22 MASKING LEVEL L-4 (NJ3,0), \[111;22\]

111.23 \* WORD LIST L-5 (S), \[111;23\]

111.24 PERCENT CORRECT L-5 (NJ3,0), \[111;24\]

111.25 \* PRESENTATION METHOD L-5 (S), \[111;25\]

111.26 PRESENTATION LEVEL L-5 (NJ3,0), \[111;26\]

111.27 MASKING LEVEL L-5 (NJ3,0), \[111;27\]

111.28 LIST L-1 (F),\[110;28\]

111.29 LIST L-2 (F),\[110;29\]

111.3 LIST L-3 (F),\[110;30\]

111.31 LIST L-4 (F),\[110;31\]

111.32 LIST L-5 (F),\[110;32\]

112.03 CI WORD LIST R-1 (S), \[112;3\]

112.04 CI PERCENT CORRECT R-1 (NJ6,2), \[112;4\]

112.08 CI WORD LIST R-2 (S), \[112;8\]

112.09 CI PERCENT CORRECT R-2 (NJ6,2), \[112;9\]

112.28 CI NOISE PERCENT RIGHT (NJ6,2), \[112;28\]

112.29 CI NOISE MATERIAL RIGHT (S), \[112;29\]

113.03 CI WORD LIST L-1 (S), \[113;3\]

113.04 CI PERCENT CORRECT L-1 (NJ6,2), \[113;4\]

113.08 CI WORD LIST L-2 (S), \[113;8\]

113.09 CI PERCENT CORRECT L-2 (NJ6,2), \[113;9\]

113.28 CI NOISE PERCENT LEFT (NJ6,2), \[113;28\]

113.29 CI NOISE MATERIAL LEFT (S), \[113;29\]

115.01 INITIAL SRT THRESH R (NJ3,0), \[115;1\]

115.02 REPEAT SRT THRESH R (NJ3,0), \[115;2\]

115.03 INITIAL SRT MASK LEVEL R (NJ3,0), \[115;3\]

115.04 FINAL SRT MASK LEVEL R (NJ3,0), \[115;4\]

115.05 INITIAL SRT THRESH L (NJ3,0), \[115;5\]

115.06 REPEAT SRT THRESH L (NJ3,0), \[115;6\]

115.07 INITIAL SRT MASK LEVEL L (NJ3,0), \[115;7\]

115.08 FINAL SRT MASK LEVEL L (NJ3,0), \[115;8\]

115.09 PBMAX R (NJ3,0), \[115;9\]

115.1 PBMIN R (NJ3,0), \[115;10\]

115.11 PI/PB R (NJ4,2), \[115;11\]

115.12 PBMAX L (NJ3,0), \[115;12\]

PBMIN L (NJ3,0), \[115;13\]

PI/PB L (NJ4,2), \[115;14\]

FINAL SRT TAG R (S),\[115;15\]

FINAL SRT TAG L (S),\[115;16\]

120.01 MIDDLE EAR PRESSURE R (NJ3,0), \[120;1\]

120.02 PK IMMITTANCE 226 R (NJ4,2), \[120;2\]

120.03 VEQ - EQUIV EAR CANAL VOL R (NJ4,2), \[120;3\]

120.04 IAR THRESHOLD R 500 (NJ3,0), \[120;4\]

120.05 IAR THRESHOLD R 1000 (NJ3,0), \[120;5\]

120.06 IAR THRESHOLD R 2000 (NJ3,0), \[120;6\]

120.07 IAR THRESHOLD R 4000 (NJ3,0), \[120;7\]

120.08 CAR THRESHOLD R 500 (NJ3,0), \[120;8\]

120.09 CAR THRESHOLD R 1000 (NJ3,0), \[120;9\]

120.1 CAR THRESHOLD R 2000 (NJ3,0), \[120;10\]

120.11 CAR THRESHOLD R 4000 (NJ3,0), \[120;11\]

120.12 ACOUSTIC REFLEX DECAY R 500 (S), \[120;12\]

120.13 ACOUSTIC REFLEX DECAY R 1000 (S), \[120;13\]

120.14 AR HALF LIFE 500 R (NJ2,0), \[120;14\]

120.15 AR HALF LIFE 1000 R (NJ2,0), \[120;15\]

120.16 INTER-TEST CONSISTENCY R (S), \[120;16\]

120.17 IAR BBN R (F),\[120;17\]

120.18 CAR BBN R (F), (F),\[120;18\]

120.19 PK IMMITTANCE 678 R(N),\[120;19\]

120.2 WEBER R(F),\[120;20\]

120.21 PT STENGER R(F),\[120;21\]

120.22 RINNE R(F),\[120;22\]

120.23 OTHER TEST R(F),\[120;23\]

121.01 PK IMMITTANCE 226 L (NJ3,0), \[121;1\]

121.02 STATIC COMPLIANCE L (NJ4,2), \[121;2\]

121.03 VEQ - EQUIV EAR CANAL VOL L (NJ4,2), \[121;3\]

121.04 IAR THRESHOLD L 500 (NJ3,0), \[121;4\]

121.05 IAR THRESHOLD L 1000 (NJ3,0), \[121;5\]

121.06 IAR THRESHOLD L 2000 (NJ3,0), \[121;6\]

121.07 IAR THRESHOLD L 4000 (NJ3,0), \[121;7\]

121.08 CAR THRESHOLD L 500 (NJ3,0), \[121;8\]

121.09 CAR THRESHOLD L 1000 (NJ3,0), \[121;9\]

121.1 CAR THRESHOLD L 2000 (NJ3,0), \[121;10\]

121.11 CAR THRESHOLD L 4000 (NJ3,0), \[121;11\]

121.12 ACOUSTIC REFLEX DECAY L 500 (S), \[121;12\]

121.13 ACOUSTIC REFLEX DECAY L 1000 (S), \[121;13\]

121.14 AR HALF LIFE 500 L (NJ2,0), \[121;14\]

121.15 AR HALF LIFE 1000 L (NJ2,0), \[121;15\]

121.16 INTER-TEST CONSISTENCY L (S), \[121;16\]

121.17 IAR BBN L (F),\[121;17\]

121.18 CAR BBN L (F), (F),\[121;18\]

121.19 PK IMMITTANCE 678 L (N),\[121;19\]

121.2 WEBER L (F) ,\[121;20\]

121.21 PT STENGER L (F) ,\[121;21\]

121.22 RINNE L (F),\[121;22\]

121.23 OTHER TEST L (F),\[121;23\]

122 COMMENTS (W), \[122;0\]

791000 node is created, but is only used at the DDC

## Files Referenced in ^ACK(509850.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^DPT( PATIENT

^VA(200 NEW PERSON

^SC( HOSPITAL LOCATION

^XMB(3.9, MESSAGE

^DIC(4, INSTITUTION

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical staff with a reference list of routines included in the Audiometric Exam module.

ACKQAG01

Called by RPC: ACKQAUD1 and routines: ACKQAG02 and ACKQAG04

Purpose: Retrieves the data for the Audiogram Display from ^ACK(509850.9)

ACKQAG02

Called by RPC: ACKQAUD2

Purpose: Retrieves the data for the Audiogram Edit from ^ACK(509850.9).

ACKQAG03

Called by RPC: ACKQROES

Purpose: Retrieves and prepares audiometric exam data for transmission to the Denver Distribution Center (DDC).

ACKQAG04

Called by routine: ACKQAG03

Purpose: Retrieves and prepares audiometric exam data for transmission to the Denver Distribution Center (DDC).

ACKQAG05

Called by routine: ACKQAG03 and RPC: ACKQROESD and ACKQAUD4

Purpose: Utilities for transmitting data to the DDC.

ACKQAG06

Called by routine: ACKQAG01

Purpose: Utilities for retrieving data for the Audiogram Display.

## Delphi Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Display Audiogram files .dpr, .pas and .dfm files:

> ACKQROES3.dpr project file

> uLayer.pas main driver program module & draw point connections

> uData.pas retrieval of data module

> uMask.pas determines & draws the masking symbols on the graph

> uTable.pas sets up and displays 2364 of data

> uAudKey.pas displays the symbol key

> uLayer.dfm Main form

> uTable.dfm 2364 form

> uAudKey.dfm Legend Key form

> Edit Audiogram .dpr, .pas and .dfm files:

> ACKQROES3E.dpr project file

> uEnterEdit.pas main driver program module

> uEditUtils.pas utilities for uEnterEdit

> uEditUtil2.pas additional utilities for uEnterEdit

> uInactivate.pas NotEdit utility to disable all controls

> uHelp1.pas Help1 module routine

> uHelp2.pas Help2 module routine

> uHelp3.pas Help3 module routine

> uHelp4.pas Help4 module routine

> uEnterEdit.dfm Main form

> uHelp1.dfm Help text form for main tab

> uHelp2.dfm Help text form for 2nd tab

> uHelp3.dfm Help text form for 3rd tab

> uHelp4.dfm Help text form for 4th tab

# # # # Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the two V*ist*A Broker options included in the Audiometric Exam module.

## ACKQROES3 - Audiogram Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: ACKQROES3

MENU TEXT: Audiogram Display

TYPE: Broker (Client/Server)

PACKAGE: QUASAR

DESCRIPTION: This is the Audiogram display taken from the AUDIOMETRIC EXAM DATA file 509850.9

RPC: ACKQAUD1

RPC: DDR FIND1

RPC: DDR FINDER

RPC: DDR GET DD HELP

RPC: DDR GETS ENTRY DATA

RPC: DDR LISTER

RPC: DDR VALIDATOR

RPC: XUS GET USER INFO

RPC: XUS SIGNON SETUP

RPC: XWB ARE RPCS AVAILABLE

RPC: XWB CREATE CONTEXT

RPC: XWB GET BROKER INFO

RPC: XWB GET VARIABLE VALUE

RPC: XWB IS RPC AVAILABLE

## ACKQROES3E - Audiogram Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: ACKQROES3E

MENU TEXT: Audiogram Enter Edit

TYPE: Broker (Client/Server)

PACKAGE: QUASAR

DESCRIPTION: This is the menu item to establish the connection for the AUDIOMETRIC EXAM DATA file Enter Edit program executable.

RPC: ACKQAUD2

RPC: ACKQAUD4

RPC: ACKQROES

RPC: ACKQROESD

RPC: DDR DELETE ENTRY

RPC: DDR FILER

RPC: DDR FIND1

RPC: DDR FINDER

RPC: DDR GETS ENTRY DATA

RPC: DDR GET DD HELP

RPC: DDR LISTER

RPC: DDR VALIDATOR

RPC: XUS GET USER INFO

RPC: XUS INTRO MSG

RPC: XUS SIGNON SETUP

RPC: XWB ARE RPCS AVAILABLE

RPC: XWB CREATE CONTEXT

RPC: XWB GET BROKER INFO

RPC: XWB GET VARIABLE VALUE

RPC: XWB IS RPC AVAILABLE

# # Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## ^ACK(509850.9,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the data stored by this module is part of the patient record, it should be retained as permanent data in accordance with V*ist*A patient data storage policy and regulations.

# # APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Called routines, entry points, and APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### START^ACKQAG01

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Called by RPC: ACKQAUD1.

> Input the reference array to accept data, DFN of patient and entry in file(opt).

> Returns, in the named array, the values for the graphical display and the 2364 - this is documented in routine.

> If a particular graph is wanted in the display, pass in the entry number as third parameter.

### TITLE^ACKQAG01(USER)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input DUZ

> Returns the printable title from the Title file ^DIC(3.1.

### GETDATA^ACKQAG02

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Provides the data for START^ACKQAG02.

### START^ACKQAG02

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Called from RPC: ACKQAUD2

> Input the array name by reference and DFN of patient.

> Gets the array of values for just the last audiogram for edit and transfer to the DDC.

### START^ACKQAG03

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Called by RPC: ACKQROES.

> Sets up and sends the message to the DDC with the audiometric data.

> The message number and date sent is placed back into the Audiometric Exam file for tracing purposes.

### GETDATA^ACKQAG04

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the entry number in file 509850.9

> Provides the transmission data for ACKQAG03

### START^ACKQAG04

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the array name to accept data and the DFN of the patient.

> Used by the RPC: ACKQAUD2 for the transmission of data to the DDC.

### ACKEXIST^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Checks for existence of file 509805.9 at the site.

### DFNIN^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the DFN of a patient.

> Returns the last entry number in file 509850.9 for a patient.

### NEWMSG^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Returns the message number as set up in ^XMB(3.9.

### GETDATA^ACKQAG06(ACKQI, ACKI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the entry in the Audiometric Exam file and the current line reading for START^ACKQAG01.

> Returns the threshold (dB) to be on the graph for a particular frequency (Hz) reading in a particular line of the array passed in START^ACKQAG01. (executes logic)

### LOGIC^ACKQAG06(A1,A2,A3,A4,A5,A6,A7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the various initial and final threshold and masking values and return the values that would be on the graph. See Appendix A.

## RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ACKQROES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TAG: START

> ROUTINE: ACKQAG03

> RETURN VALUE TYPE: SINGLE VALUE

> AVAILABILITY: PUBLIC

> WORD WRAP ON: FALSE

> VERSION: 3

> DESCRIPTION:

> This is the RPC used to setup and send to the DDC, the signed audiometric data file

> entry. It is triggered by the saving of a signed entry in 509850.9

> INPUT PARAMETER: DFN

> PARAMETER TYPE: LITERAL

> REQUIRED: YES

> SEQUENCE NUMBER: 1

> DESCRIPTION: This is the pointer to the patient file.

> INPUT PARAMETER: IEN

> PARAMETER TYPE: LITERAL

> REQUIRED: NO

> SEQUENCE NUMBER: 2

> DESCRIPTION: This is the entry in 509850.9 that the user is working on.

> INPUT PARAMETER: STANUM

> This is the Sta \# of the sending clinic

> INPUT PARAMETER: USRNAM

> PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 32

> REQUIRED: NO

> SEQUENCE NUMBER: 4

> DESCRIPTION: This is the name of the submitting user

> INPUT PARAMETER: USRSER

> PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 32

> REQUIRED: NO

> SEQUENCE NUMBER: 5

> DESCRIPTION: This is the name of the submitting user's service

RETURN PARAMETER DESCRIPTION:

> It returns a literal containing the local confirmation msg number,

> the msg number sent to the DDC, the error number, & the error msg.

### ACKQAUD1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TAG: START

> ROUTINE: ACKQAG01

> RETURN VALUE TYPE: ARRAY

> AVAILABILITY: PUBLIC

> WORD WRAP ON: FALSE

> DESCRIPTION:

> This RPC gets the audiogram data for entries in the Audiometric Exam Data file 509850.9 and returns it to the calling program in the array

> ACKQARR()

> INPUT PARAMETER: DFN

> PARAMETER TYPE: LITERAL

> REQUIRED: YES

> SEQUENCE NUMBER: 1

> DESCRIPTION: The internal number in the Patient file (2)

> INPUT PARAMETER: IEN

> PARAMETER TYPE: LITERAL

> REQUIRED: NO

> SEQUENCE NUMBER: 2

> DESCRIPTION: internal number in the Audiometric Exam Data file (509850.9)

> RETURN PARAMETER DESCRIPTION:

> ACKQARR(0) = these pieces:

> 1=# audiograms\[0-2\]

> 2=name of patient

> 3=first audiogram date seen

> 4=first tester name

> 5=age of patient at first test

> 6=title of tester for first audiogram

> 7=SSN of patient

> 8=second audiogram date(or error message if an error exists)

> 9=tester name for second audiogram

> 10=age of patient at second audiogram

> 11=title of tester for second audiogram

> ACKQARR(ctr) pieces for each all X values

> 1=X Value(Hz) being tested

> 2=ACKQI - internal record number in 509850.9

> 3=ear\[L,R\]

> 4=air Y(dB) val

> 5=airMask\[0-6\]

> 6=airMaskLevel

> 7=bone Y(dB) value

> 8=boneMask\[0-6\]

> 9=boneMaskLevel

> 10=IAR

> 11=CAR

> Will return to Delphi app as subscripted array

> RETURN() subscripted values

> 1-12(1st audiogram R ear)

> 13-24(1st audiogram L ear)

> 25 is speech recog 1st audiogram

> 26 is the 120/121 nodes for 1st audiogram

### ACKQAUD2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TAG: START

> ROUTINE: ACKQAG02

> RETURN VALUE TYPE: ARRAY

> AVAILABILITY: PUBLIC

> DESCRIPTION:

> Input the IEN of the 509850.9 file entry as the second parameter. Input the DFN as the third parameter, array by reference as first returns a subscripted array of data values for this audiogram. Used in the edit program

> INPUT PARAMETER: DFN

> PARAMETER TYPE: LITERAL

> REQUIRED: YES

> SEQUENCE NUMBER: 1

> DESCRIPTION: DFN of patient - entry in DPT(

> RETURN PARAMETER DESCRIPTION: Subscripted array of values for various Hz.

> This is not used for the Audiogram Display, just the edit program

> input: ref to array and DFN

> returns: array of values, RMPFERR if an error was found.

> Will return to the application as subscripted array,

> Subscripts: 1(general), 2-13(R ear), 14-25(L ear), 26(general)

> (1)=audiogram local ien^name of patient^last date seen^tester1^error msg

> (#)=pcs in rest of counter nodes.

> 1=Xvalue

> 2=ear\[L,R\]^

> 3=

> 4=iairY^

> 5=iairMask\[0-6\]^

> 6=iairMaskL^

> 7=iboneY^

> 8=iboneMask\[0-1\]^

> 9=iboneMaskL^

> 10=IAR^

> 11=CAR^

> 12=rairY^

> 13=rairMask\[0-6\]^

> 14=rairMaskL^

> 15=rboneY^

> 16=rboneMask\[0-1\]^

> 17=rboneMaskL^

> 18=AR DECAY^

> 19=HALF LF

# # # External Relations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Standalone Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Module can be run as a standalone product on a V*ist*A system with the included Audiometric Exam Data file (#209850.9). This file also refers to the PATIENT (#2) file, the NEW PERSON (#200) file, the INSTITUTION (#4) file, the HOSPITAL LOCATION (#44) file, and the title of the examining clinician from the TITLE (3.1) file. The facility is not required to have inpatient activity or use CPRS to use this module.

Through this application, audiometric exam records are delivered electronically to the DDC, allowing integration of this clinical data into orders placed through the Remote Order Entry System (ROES). By including audiometric data in ROES custom hearing aid orders, manufacturers of these hearing aids are provided with more complete information for the manufacture, modification, and repair of these highly customized devices.

## Recommended Desktop Minimums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| SPECIFICATION    | RECOMMENDED MINIMUM                                                                       |
| Processor        | 200 MHz                                                                                   |
| Memory           | 64 MB                                                                                     |
| Hard Drive       | 4GB                                                                                       |
| Video            | AGP 2x w/4MB                                                                              |
| CD-ROM           | 8x                                                                                        |
| Monitor          | 17" VGA, .28 pixel resolution                                                             |
| LAN Interface    | 10/100 Mbps Ethernet                                                                      |
| Keyboard         | 101 -key                                                                                  |
| Mouse            | Microsoft Compatible                                                                      |
| Operating System | Microsoft Windows 9x, 2000 or XP (MS Windows XP or Windows 2000 Pro strongly recommended) |
| Browser          | IE 5                                                                                      |

A system meeting the above specifications can be expected to provide the functionality necessary for this application. The VA Assistant Secretary for Information and Technology has established a set of minimum configurations for any new procurement of desktop systems across the enterprise (VA Directive 6401) For most of the specifications listed above, the VA minimum baseline exceeds the recommended minimum for this application, but the above specifications are provided to allow for use of equipment incurrent inventory, if necessary. In assessing procurement and/or other resource acquisition actions to meet this application's requirements, each facility is advised to give consideration to the specifications mandated by the above-mentioned Directive. Conformance with these established and/or emerging VA standards is encouraged. A dynamic update of the VA desktop standards is maintained at [http://vaww.vairm.vaco.va.gov/vadesktop](http://vaww.vairm.vaco.va.gov/vadesktop/)/.

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     |     |     |
|-----|-----|-----|
|     |     |     |
|     |     |     |
|     |     |     |

No integration agreements are used in the Audiometric Module.

# # Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## M routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

i ACKQAG01 Called by Option: ACKQAUD1

ii ACKQAG02 Called by Option: ACKQAUD2

iii ACKQAG03 Called by Option: ACKQROES

iv ACKQAG04 Called by routine: ACKQAG03

v ACKQAG05 Called by routine: ACKQAG03

vi ACKQAG06 Called by routine: ACKQAG01

## Delphi routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display Audiogram files: ACKQROES3.EXE

Display EnterEditAudiogram files: ACKQROES3E.EXE

## Module Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following QUASAR name spaced variables are used in the Audiometric Exam module.

|          |                                 |
|----------|---------------------------------|
| ACKI     | array subscript value           |
| ACKQ     | number of graphs                |
| ACKQ1IEN | first record internal number    |
| ACKQ2IEN | second record internal number   |
| ACKQA1   | air initial threshold           |
| ACKQA1L  | air initial masking level       |
| ACKQA1T  | air initial tag value           |
| ACKQA2   | air repeat threshold            |
| ACKQA2L  | air repeat masking level        |
| ACKQA2T  | air repeat tag value            |
| ACKQARR  | array name, passed by reference |
| ACKQB1   | bone initial threshold          |
| ACKQB1L  | bone initial masking level      |
| ACKQB1T  | bone initial tag value          |
| ACKQB2   | bone repeat threshold           |
| ACKQB2L  | bone repeat masking level       |
| ACKQB2T  | bone repeat tag value           |
| ACKQDAT  | FileMan date                    |
| ACKQER   | error message                   |
| ACKQER1  | error message                   |
| ACKQERR  | error message                   |
| ACKQFA   | file exist flag                 |
| ACKQFMD  | FileMan date loop holder        |
| ACKQHSSN | hold SSN value                  |
| ACKQIEN  | record internal number          |
| ACKQN    | subscript/counter               |
| ACKQSTNU | station number                  |
| ACKQT    | flag & dummy text holder        |
| ACKQUSNM | User name                       |
| ACKQUSSR | User service                    |

## SAC exemptions and approval dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application requires no exemptions from the V*ist*A Standards and Conventions for package development.

# # # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## Acronyms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AC Air Conduction

AR Acoustic Reflex

ARD Acoustic Reflex Decay

ASPS Audiology & Speech Pathology Service

BC Bone Conduction

C&P Compensation and Pension

CAR Contralateral Acoustic Reflex

CNC Consonant Nucleus Consonant

CNM Could Not Mask

DNT Could Not Test

dB Decibel

DDC Denver Distribution Center

DNT Did Not Test

EM Effective Masking

HL Hearing Level

Hz Hertz

IAR Ipsilateral Acoustic Reflex

MCL Most Comfortable Loudness

ML Masking Level

NR No Response

NU Northwestern University

pc Piece

PIPB Performance Intensity-Phonetically Balanced

Pr-L Probe Left

Pr-R Probe Right

PSAS Prosthetics & Sensory Aids Service

PTA Pure Tone Average

SAT Speech Awareness Threshold

SRT Speech Reception Threshold

UCL Uncomfortable Loudness

# # # Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some of the information in Appendices A, B, and C requires knowledge of clinical audiology terms and practices, but may also be of benefit to IRM technical staff.

## A: Determining Series Values To Place On Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Some of the key rules applied in preparing series values for display in the *Audiogram Display* application are as follows:

> The initial, repeat and final thresholds and the final masking level are obtained. The following rules are checked in order until a point is obtained:

> 1\. If the initial value is ‘CNT’ or ‘DNT’ there will be no point on the graph.

> Each of the following values will contain the masking level (if one exists).

> 2\. If the final reading has a value (including ‘+’) it will be used.

> 3\. If the retest value is “” then the initial value is used.

> 4\. If the initial value is “” then the retest value is used.

> 5\. If initial contains ‘+’ and retest does not, then retest is used.

> 6\. If the initial does not contain ‘+’ and the retest does, then initial is used.

> 7\. If initial is less than retest, then initial is used.

> 8\. Whatever is in retest is used.

> If the selected point indicates a 'No Response' (+), there will be a gap in the series.

## B: Calculation Of PB MAX And PI/PB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Calculation of PB MAX and PI/PB values in the *Audiometric Exam Enter/Edit* application is based on specific industry-standard formulae established for these measurements. Basic descriptions of some of these formulae are as follows:

PB MAX is the maximum percentage from the word recognition testing.

PB MIN is the minimum percentage from the word recognition testing.

PI/PB is an indices of possible retrocochlear pathology. It is calculated from the formula:

(PB MAX - PB MIN)/(PB MAX).

The PI/PB index will assess multiple scores and levels in one ear. The calculation will occur only when a second score obtained at a higher presentation level, is poorer than a prior score at a lower presentation level.

## C: Sample Form 2364

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ackq-3-12-audiometric-exam-module-technical-manual/005.png)

## D: Message Box Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="a-needed-rpc-xxxxxxxx-is-not-available.">A needed RPC XXXXXXXX is not available. </h3>
<p>Contact your IRM.</p>
<p>The 'XWB IS RPC AVAILABLE' remote procedure call returned FALSE for RPC XXXXXXXXX. IRM will need to install this RPC in order for the action to be workable.</p></td>
</tr>
<tr class="even">
<td><h3 id="a-problem-was-encountered-accessing-vista-rpc-xxxxx.">A problem was encountered accessing V<em>ist</em>A, RPC XXXXX. </h3>
<p>Contact your IRM Service.</p>
<p>The Broker call to remote procedure XXXXX failed.</p></td>
</tr>
<tr class="odd">
<td><h3 id="a-problem-was-encountered-communicating-with-the-server.">A problem was encountered communicating with the server.</h3>
<p>The RPCBroker call to the server was tried for a remote procedure, but it failed.</p></td>
</tr>
<tr class="even">
<td><h3 id="a-problem-with-the-rpc-call---no-data-to-graph.">A problem with the RPC call - no data to graph.</h3>
<p>The expected data for the selected entry was not returned by the remote procedure call.</p></td>
</tr>
<tr class="odd">
<td><h3 id="application-canceled.-or-unable-to-access-rpcbroker.">Application Canceled. Or unable to access RPCBroker.</h3>
<p>Broker.Connected returned False.</p></td>
</tr>
<tr class="even">
<td><h3 id="cannot-continue-without-patient.">Cannot continue without Patient.</h3>
<p>Patient identification number DFN is undefined or nil.</p></td>
</tr>
<tr class="odd">
<td><h3 id="broker-server-could-not-be-determined.">Broker Server could not be determined.</h3>
<p>The program did not pick up the name of either the broker server or the port.</p></td>
</tr>
<tr class="even">
<td><h3 id="connection-to-broker-server-could-not-be-established.">Connection to Broker Server could not be established.</h3>
<p>The Server and port selected could not be activated.</p></td>
</tr>
<tr class="odd">
<td><h3 id="no-charts-to-show-audiogram-terminating.">No Charts to Show! Audiogram Terminating.</h3>
<p>Called the View Audiogram option for a patient that didn't have any data in file 509850.9</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="no-patient-to-lookup">No Patient to lookup</h3>
<p>An attempt was made to continue without a patient selected. (DFN undefined or nil)</p></td>
</tr>
<tr class="even">
<td><h3 id="patient-not-selected">Patient not selected</h3>
<p>An attempt was made to continue without a patient selected.</p></td>
</tr>
<tr class="odd">
<td><h3 id="problem-encountered-in-setting-up-message---no-data-sent">Problem encountered in setting up message - no data sent!</h3>
<p>XMZ &lt; 1 was returned from the MailMan setup call.</p></td>
</tr>
<tr class="even">
<td><h3 id="problem-saving-entries-for-acoustic-immittance">Problem saving entries for Acoustic Immittance!</h3>
<p>A change on the Acoustic Immittance tab was not saved because the database would not accept it. Exiting and coming back to the page will cause the faulty entry to be missing.</p></td>
</tr>
<tr class="odd">
<td><h3 id="problem-saving-entries-for-left-ear">Problem saving entries for Left Ear!</h3>
<p>A change to the Left Ear was not saved because the database would not accept it. Exiting and coming back to the page will cause the faulty entry to be missing.</p></td>
</tr>
<tr class="even">
<td><h3 id="problem-saving-entries-for-right-ear">Problem saving entries for Right Ear!</h3>
<p>A change to the Right Ear was not saved because the database would not accept it.</p></td>
</tr>
<tr class="odd">
<td><h3 id="record-not-sent-to-ddc.">Record NOT sent to DDC.</h3>
<p>The setup of the transfer message failed after entering a DATE SIGNED. Another attempt could be made by having IRM remove the entry in the DATE SIGNED field in 509850.9. Then use the GUI to again sign the audiogram edit.</p></td>
</tr>
<tr class="even">
<td><h3 id="the-audiogram-option-is-not-approved-for-this-user.">The Audiogram Option is not approved for this user.</h3>
<p>Someone is attempting to access options ACKQROES3 or ACKQROES3E without it being on their menu tree.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="the-xxxxxxxx-programoption-name-could-not-be-accessed.">The XXXXXXXX program[option name] could not be accessed. </h3>
<p>Terminating application.</p>
<p>The CreateContext for the application failed- not in user's menu tree.</p></td>
</tr>
<tr class="even">
<td><h3 id="there-was-a-problem-deleting-the-record.">There was a problem deleting the record.</h3>
<p>The delete button was pressed, but the DIK call returned an error.</p></td>
</tr>
<tr class="odd">
<td><h3 id="user-identification-could-not-be-established.">User identification could not be established.</h3>
<p>The DUZ was not defined, or the XUS GET USER INFO rpc returned an error.</p></td>
</tr>
<tr class="even">
<td><h3 id="you-are-not-authorized-to-use-the-audiogram-enteredit">You are not authorized to use the Audiogram Enter/Edit</h3>
<blockquote>
<p><strong>program[ACKQROES3E]. Terminating application…</strong></p>
<p>Someone is attempting to access options ACKQROES3 or ACKQROES3E without it being on their menu tree.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><h3 id="users-station-not-added.-station-in-record-is-blank.">Users station not added. Station in record is blank.</h3>
<p>The program picked up an invalid pointer to the Institution file.</p></td>
</tr>
</tbody>
</table>

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ACKQAG01, 26, 33

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACKQAG02, 33

ACKQAG03, 26, 33

ACKQAG04, 34

ACKQAG05, 34

ACKQAG06, 34

ACKQAUD1, 26, 36

ACKQAUD2, 26, 38

ACKQROES, 26, 35

ACKQROES3, 27, 29

ACKQROES3E, 27, 30

Audiogram Display, i

Audiogram Edit, i

Broker, 3, 30

BROKER, 29

BUILD FILE PRINT, 1

CKQAG03, 26

connectivity, 3

CPRS, i, ii, 1, 3

DATA DICTIONARY UTILITIES, 1

Desktop Minimums, 42

display, i, 26

Display, 10, 27, 29, 45

domain, 3

edit, 3, 33

Edit, i, 26, 27, 30

Errors, 52

executables, 3

formula, 50

INSTALL FILE PRINT, 2

Integration Agreements, 43

KIDS, 1, 3

MailMan, 3

Minimum, 42

Monitor, 42

Operating System, 42

options, 3

PB MAX, 50

PB MIN, 50

PI/PB, 50

Process Logic, 5

project, 27

routines, 2, 45

Sample, 51

SERIES VALUES, 49

Tools, i, 3