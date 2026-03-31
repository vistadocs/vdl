---
title: Functional Independence Measurement (FIM) Version 1 Technical and Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Technical and
app_code: FIM
app_name: Functional Independence Measurement
section: CLI
app_status: active
pkg_ns: FIM
patch_ver: 1
patch_id: FIM*1
group_key: "FIM:FIM:1"
file_numbers: []
security_keys: []
menu_options: 4
description: The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC). The FIM is an 18-item 7-level functional assessment
audience: 
keywords: 
  - class
  - table
  - colspan
  - contents
  - even
  - code
  - date
  - message
  - segment
  - patient
page_count: 0
word_count: 10040
section_count: 29
table_count: 34
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2003
revision_count: 5
revision_newest: 5/02/2003
revision_oldest: 2/26/2003
docx_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=134"
---

---
title: |
  ![](functional-independence-measurement-fim-version-1-technical-and-security-guide/001.png)

  Functional Independence Measurement (FIM) Technical Manual and Security Guide

  ![](functional-independence-measurement-fim-version-1-technical-and-security-guide/002.png)

  Version 1.0

  May 2003

  Department of Veterans Affairs

  VistA System Design and Development
---

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Related Manual](#related-manual)
  - [Online Help](#online-help)
- [Orientation](#orientation)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [VistA Intranet](#vista-intranet)
  - [Assumptions about the Reader](#assumptions-about-the-reader)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Log In](#system-log-in)
  - [Configuration File Management](#configuration-file-management)
- [File Diagram](#file-diagram)
- [Protocols](#protocols)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [XINDEX](#xindex)
  - [Callable Routines/Entry Points/APIs](#callable-routinesentry-pointsapis)
- [Broker Context Menu Option Assignment](#broker-context-menu-option-assignment)
- [External Interfaces](#external-interfaces)
  - [Exported Remote Procedure Calls (RPC)](#exported-remote-procedure-calls-rpc)
- [External Relations](#external-relations)
  - [Data Base Agreements (DBIAs)](#data-base-agreements-dbias)
- [Software Security](#software-security)
  - [Mail Groups](#mail-groups)
  - [Remote Systems](#remote-systems)
  - [Archiving and Purging](#archiving-and-purging)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing Software](#interfacing-software)
  - [Security Keys](#security-keys)
  - [Equipment](#equipment)
- [Appendix A - Databases](#appendix-a-databases)
- [Appendix B – Health Level Seven (HL7) Specifications](#appendix-b-health-level-seven-hl7-specifications)
- [Introduction](#introduction-1)
- [General Specifications](#general-specifications)
  - [Communication Protocol](#communication-protocol)
  - [Application Processing Rules](#application-processing-rules)
  - [HL7 Concepts and Definitions](#hl7-concepts-and-definitions)
    - [Messages](#messages)
    - [Segments](#segments)
    - [Fields](#fields)
    - [Position (sequence within the segment)](#position-sequence-within-the-segment)
    - [Maximum length](#maximum-length)
    - [Data type](#data-type)
    - [Optionality](#optionality)
    - [Repetition](#repetition)
    - [Message Delimiters](#message-delimiters)
    - [Data Types](#data-types)
    - [Use of Escape Sequences in Text Fields](#use-of-escape-sequences-in-text-fields)
  - [Specification Conventions](#specification-conventions)
    - [Segment Tables Definitions](#segment-tables-definitions)
- [HL7 Messages](#hl7-messages)
  - [HL7 Message Definition](#hl7-message-definition)
    - [ORU – Unsolicited transmission of an observation (Event type R01)](#oru-unsolicited-transmission-of-an-observation-event-type-r01)
  - [HL7 Segment Definitions and Specifics](#hl7-segment-definitions-and-specifics)
    - [MSH Attributes](#msh-attributes)
    - [MSH field definitions](#msh-field-definitions)
    - [PID Attributes](#pid-attributes)
    - [PID field definitions](#pid-field-definitions)
    - [PV1 Attributes](#pv1-attributes)
  - [PV1 Field Definitions](#pv1-field-definitions)
    - [PV1 – Admission Type](#pv1-admission-type)
  - [NTE – Notes and Comments Segment – Attributes](#nte-notes-and-comments-segment-attributes)
    - [NTE field definitions](#nte-field-definitions)
    - [OBR Attributes](#obr-attributes)
    - [OBR Field Definitions](#obr-field-definitions)
    - [OBX Attributes](#obx-attributes)
    - [OBX field definitions](#obx-field-definitions)
|           |                                                 |
|-----------|-------------------------------------------------|
| Date      | Description                                     |
| 2/26/2003 | Updates from <span class="mark">REDACTED</span> |
| 3/31/2003 | Updates from <span class="mark">REDACTED</span> |
| 4/14/2003 | Updates from <span class="mark">REDACTED</span> |
| 4/22/2003 | Updates from <span class="mark">REDACTED</span> |
| 5/02/2003 | Updates from <span class="mark">REDACTED</span> |
TABLE OF CONTENTS

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC). The FIM is an 18-item 7-level functional assessment designed to evaluate the amount of assistance required by a person with a disability to perform basic life activities safely and effectively. There are five types of FIM assessments: admission, goals, interim, discharge, and follow-up. The FIM assessments are used clinically to monitor the outcomes of rehabilitative care, as required by the Joint Commission on the Accreditation of Health Care Organizations (JCAHO) and the Commission on the Accreditation of Rehabilitative Facilities (CARF). According to VHA Directive 2000-16, medical centers are mandated to measure and track rehabilitation outcomes on all new stroke, lower-extremity amputees, and traumatic brain injury (TBI) patients using the FIM. Finally, the Performance Measurement Workgroup of the Department of Veterans Affairs Central Office (VACO) approved a Network Director Performance Measure for rehabilitation for FY03 that requires the collection of FIM data. FIM Version 1.0 should greatly ease the burden placed on rehabilitation professionals in the field who are working to comply with the new performance measure.

Functional Independence provides a Graphic User Interface (GUI) front end programmed in Delphi to allow multiple clinicians to input FIM data for a given patient. This documentation will then be available in CPRS as a progress note with addendums and/or a completed consults. The GUI front end will also gather demographic data, as well as other required data by FSOD from VistA, eliminating the need for the clinician search of VistA for the information and re-enter for FIM. The FIM data will be placed in a VistA FileMan file for Health Level Seven (HL7) transmission to the FSOD at ACC.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information in this manual is technical in nature and is developed for the following individuals who are responsible for the installing, supporting, maintaining, and testing this software:

> Information Resource Management (IRM)

> Clinical Coordinators

> National VistA Support (NVS)

## Related Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Functional Independence Measurement (FIM) Installation Guide, V.1.0Functional Independence Measurement (FIM) User Manual, V.1.0*

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions, procedures, and other information are available from the FIM online help file. You may access the help file by clicking on Help\|Contents from the menu bar or by pressing the F1 key while you have any FIM screen dialog open.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user’s response in this manual is in bold type, but does not appear on the screen as bold. The bold part of the entry is the letter or letters that you must type so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, you will see the symbol \<RET\>. This symbol is not shown but is implied if there is bold input.

Within the roll and scroll part of the system, help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. You can find this information enclosed in brackets, for example, \[type ward name here\], and will not appear on the screen.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|        |                                                                                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------|
| Symbol | Description                                                                                                       |
|        | Used to inform the reader of general information including references to additional reading material. See example |
|        | Used to caution the reader to take special notice of critical information.                                        |

Table 1: Documentation Symbol Descriptions

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA FIM software files and Installation and Implementation Guide (i.e., RMIM1_0IG.PDF) are available on the following Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directories.

|                |                                    |                                    |
|----------------|------------------------------------|------------------------------------|
| OIFO           | FTP Address                        | Directory                          |
|  Albany        | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Hines          | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Salt Lake City | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

VistA FIM software and documentation are distributed as the following set of files:

<table style="width:100%;">
<colgroup>
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 24%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File Name</td>
<td>Contents</td>
<td>Retrieval Format</td>
<td>File Size</td>
</tr>
<tr class="even">
<td>RMIM1_0.KID</td>
<td>KIDS build</td>
<td>ASCII</td>
<td>219,648 bytes</td>
</tr>
<tr class="odd">
<td>RMIM1_0.ZIP</td>
<td>FIM Executable</td>
<td>BINARY</td>
<td>1,121,792 bytes</td>
</tr>
<tr class="even">
<td>RMIM1_0IG.pdf<br />
RMIM1_0IG.doc</td>
<td>Installation Guide</td>
<td>BINARY</td>
<td><p>1,350 bytes</p>
<p>28,570 bytes</p></td>
</tr>
<tr class="odd">
<td>RMIM1_0TM.pdf<br />
RMIM1_0TM.doc</td>
<td>Technical Manual and Security Guide</td>
<td>BINARY</td>
<td><p>2,460 bytes</p>
<p>17,530 bytes</p></td>
</tr>
<tr class="even">
<td>RMIM1_0UM.pdf<br />
RMIM1_0UM.doc</td>
<td>Users Manual</td>
<td>BINARY</td>
<td>19,350 bytes<br />
29,130 bytes</td>
</tr>
</tbody>
</table>

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online Documentation for this product is available on the intranet at the following address: [www.va.gov/vdl](http://www.va.gov/vdl). This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the Clinical Case Registries link and it will take you to the FIM documentation.

## Assumptions about the Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- (e.g., Kernel Installation and distribution System \[KIDS\])
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the Functional Independence Measures (FIM) Installation Guide for additional information about installing and implementing this software.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><p>There are three ways to run the FIM.exe:</p>
<ol type="1">
<li><p>If site chooses to pass parameters within the Tools menu of CPRS, Patient Selection will be controlled by CPRS only.*</p></li>
<li><p>If site chooses to hang the software within the Tools menu of CPRS without passing parameters, Patient Selection will be controlled by FIM. FIM will run as a stand-alone.</p></li>
<li><p>If site chooses to initiate FIM through other means (i.e. desktop shortcut), Patient Selection will be controlled by FIM. FIM will run as a stand-alone.</p></li>
</ol>
<p>*If site chooses to launch FIM from the CPRS Tools menu using parameter passing (s=%SRV p=%PORT d=%DFN):</p>
<ol type="1">
<li><p>Patient Selection will be controlled by CPRS.</p></li>
<li><p>No Patient Selection will be allowed in FIM</p></li>
<li><p>If FIM has an active patient record open, and CPRS changes patient, users will be informed that all current input data will be ignored.</p></li>
<li><p>FIM will shut down.</p></li>
</ol></td>
</tr>
</tbody>
</table>

## System Log In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will display the same Broker Server list that you see in CPRS if your site has server lists installed. If you wish to make changes to the list, use the ServerList program that was distributed with the RPCBroker.

## Configuration File Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RMIM FIM SITE PARAMETERS file (#783.9) stores the system parameter data.

The settings in this file are critical to the proper operation of the Functional Independence Measurement. Incorrect or missing setting will cause unpredictable results.

The following fields are provided in this file:

.01 FACILITY NAME

.02 HIGHEST CASE NUMBER

.03 MAIL GROUP

.04 FSOD NOTE TITLE

.05 NON FSOD NOTE TITLE

.06 CONSULT TITLE

10 FACILITY CODE (multiple)

The following is an explanation of the individual entries:

FACILITY NAME Name of your site

HIGHEST CASE NUMBER Internal use

MAIL GROUP Receives messages when a record that goes to FSOD gets

created or edited

FSOD NOTE TITLE Used for progress notes when data is sent to FSOD

NON FSOD NOTE TITLE Used for progress note when data is not sent to FSOD

CONSULT TITLE Used for consults when data is sent to FSOD

FACILITY CODE (multiple) Code(s) assigned to your site by FSOD

# File Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td>FILE (#)<br />
POINTER FIELD</td>
<td>POINTER<br />
TYPE</td>
<td>(#) FILE<br />
POINTER FIELD</td>
<td>FILE POINTED TO</td>
</tr>
<tr class="even">
<td>L=Laygo<br />
*=Truncated</td>
<td>S=File not in set<br />
m=Multiple</td>
<td>N=Normal Ref.<br />
v=Variable Pointer</td>
<td>C=Xref.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>783 FUNCTIONAL *</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>PATIENT</td>
<td>- &gt; PATIENT</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>PROG NOTE IEN</td>
<td>- &gt; TIU DOCUMENT</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>EMAIL ID</td>
<td>- &gt; MESSAGE</td>
</tr>
</tbody>
</table>

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM DRIVER FIM – FSOD EVENT DRIVER

RMIM SUBSCRIBER RMIM FIM – FSOD SUBSCRIBER

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM.exe file is associated with the Functional Independence Measurement and must be placed on an End-User Workstation or a Consolidated Network Location. The following files are installed on the VistA server:

|                                                    |                                                                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File                                               | Description                                                                                                                                                |
| Functional Independence Measurement Record file    | This file holds all the information that is transmitted to Austin. This file is populated by the Functional Independence Measurement (FIM) Delphi template |
| Functional Independence Measurement Parameter file | Site Parameter for FIM.                                                                                                                                    |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the listing below to learn the routines installed on your site's VistA Server during the installation of RMIM V. 1.0. The first line of each routine briefly describes its general information.

|     |                                                                                                                   |
|-----|-------------------------------------------------------------------------------------------------------------------|
|     | You can use the Kernel First line Routine Print option to print a list containing the first line of each routine. |

The following list contains the routines included in RMIM Version 1.0

|         |                 |
|---------|-----------------|
| Routine | Checksum Values |
| RMIMHL  | 5598302         |
| RMIMRP  | 7242673         |
| RMIMU   | 3354346         |
| RMIMU1  | 2235473         |
| RMIMV   | 8374421         |

# Exported Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                           | Option Name                               | Descriptions                                                                                                                                                                                                              |
|---------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RMIM EDIT SITE PARAMETER  | FIM Site Parameter Edit                   | Option to edit the RMIM FIM SITE PARAMETER file (#783.9).                                                                                                                                                                 |
| RMIM MAIL SERVER          | RMIM Mail Server                          | Server option used to populate information in file \#783 (RMIM FIM FSOD RECORD), fields AUSTIN STATUS (ACK or ERR) and ERROR DESCRIPTION (if one exists). This server option processes the AAC mail message back to site. |
| RMIM MAIL SERVER REPORT   | Austin Error Report for FSOD Transmission | Report for coordinators to observe if Austin had an error processing an entry.                                                                                                                                            |
| RMIM NIGHTLY TRANSMISSION | FIM to FSOD Transmission Task             | This task should be scheduled nightly to send all edited cases to FSOD Austin.                                                                                                                                            |
| RMIM REPORTS              | FIM Repots                                | Menu to hold FIM coordinator reports.                                                                                                                                                                                     |
| RMIMCOORD MENU            | FIM Coordinators Menu                     | Menu consisting of an option to edit the FIM Site parameter and Reports.                                                                                                                                                  |
| RMIMFIM                   | RMIM FIM Context version 1.0              | CONTEXT needed to run the FIM template (Delphi form).                                                                                                                                                                     |
| RMIMIT                    | FIM Retransmit all records to Austin      | An option not on any menu. This option is for Information Management staff to use if all cases need to be re-transmitted to Austin FSOD.                                                                                  |
| RMIMXMIT                  | FIM to FSOD by Patient                    | Report sorted by patient to view all cases sent to FSOD and the status of that transmission.                                                                                                                              |
| RMIMXMIT DATE             | FIM to FSOD by Transmission Date          | Report sorted by transmission date for all cases transmitted to Austin.                                                                                                                                                   |

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XINDEX is a routine that produces a report called the VA Cross-Reference. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a listing of internal and external routine calls.

XINDEX is invoked from programmer mode: D ^XINDEX.

When selecting routines, select RMIM\*.

## Callable Routines/Entry Points/APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines in this package. Files and databases should be included in your network saves.

# Broker Context Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have the @ sign, you will not need these Broker Menus to see these menus. We created options for each type of user to avoid us having to remove the @ sign from ourselves.

For Employees who can run FIM, assign the Broker Context Menu \[RMIM FSOD\] to these employees secondary menu.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a unidirectional interface from the FIM to the AAC based upon HL7 V2.3.1 messaging standards.

The function of the message is to pass information relating to local FIM patient data to a centralized database.

A two-phased process is required for message transactions. VistA will send a batch HL7 message and receive a commit acknowledgment from the AAC over the same link. This tells VistA the message was received correctly. After the message has been processed, the AAC will connect back to the sending VistA site (using the standard listener on the port 5000) and send an application acknowledgment. See Appendix B for HL7 information

## Exported Remote Procedure Calls (RPC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM distributes the following RPCs:

| RPC Name               | Line Tag | Routine |
|------------------------|----------|---------|
| RMIM AUTHOR LOOKUP     | AL       | RMIMR   |
| RMIM CHECK DUPLICATE   | DUP      | RMIMV   |
| RMIM CONSULT LIST      | CON      | RMIMV   |
| RMIM CONVERT DATE      | DTFMT    | RMIMRP  |
| RMIM FIM PARAMETER     | PRM      | RMIMRP  |
| RMIM GET CASES         | LC       | RMIMRP  |
| RMIM GET DFN           | DFN      | RMIMRP  |
| RMIM GET FORM          | FRM      | RMIMRP  |
| RMIM GET PATIENT DME   | DME      | RMIMRP  |
| RMIM GET SELECTED CASE | GC       | RMIMRP  |
| RMIM GET USER INFO     | DUZ      | RMIMRP  |
| RMIM LOCATION LOOKUP   | LL       | RMIMRP  |
| RMIM LOCK PATIENT      | PT L     | RMIMRP  |
| RMIM PATIENT INFO      | PI       | RMIMRP  |
| RMIM PATIENT LOOKUP    | PL       | RMIMRP  |
| RMIM RESTRICTED RECORD | RRN      | RMIMRP  |
| RMIM SAVE FSOD         | SAV      | RMIMRP  |
| RMIM SEND EMAIL        | XM       | RMIMRP  |
| RMIM VERSION           | RPC      | RMIMVP  |

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing FIM, make sure that your system includes the following VistA software applications and versions (those listed or higher).

| Application Name | Minimum Version |
|------------------|-----------------|
| Kernel           | V. 8            |
| Kernel Toolkit   | V. 7.3          |
| VA FileMan       | V. 22           |
| RPC Broker       | V. 1.1          |
| TIU              | V.1.0           |
| OERR             | V.3.0           |
| HL7              | V.1.6           |
| MailMan          | V.8             |

## Data Base Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of DBIAs requested for FIM:

| Name                       | DBIA Number |
|----------------------------|-------------|
| ORQQCN LIST                | 1671        |
| ORWD DT                    | 1824        |
| ORWU DT                    | 3363        |
| TIU SIGN RECORD            | 1790        |
| TIU UPDATE RECORD          | 1799        |
| TIU REQUIRES COSIGNATURE   | 1800        |
| TIU CREATE ADDENDUM RECORD | 1805        |

# Software Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measures transmits data to the national database through the VA network; this network has security protection in place. Local coordinators will have their profile within Computerized Patient Record System (CPRS) amended by a local IRM to allow them to have access to the local FIM functionality. No other users will be able to access the local FIM unless they are set up in this method. All patients Social Security Numbers (SSN) and names are encrypted before transmission to an agreed upon standard. The fields sent to the AAC become readable upon receipt of the data, however only high-level users have access to the unencrypted fields when viewing the national database.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM Coordinators Mail Group RMIM FSOD is used for communication between users of the FIM template and the Coordinators. When a record that goes to FSOD gets created or edited, the FIM template will send a message to this group.

The RMIM FSOD TRANSMISSION Mail Group is used for the transmission of FIM data to the FSOD database in Austin. No members need to be in this group. The mail group should have REMOTE MEMBER: XXX@Q-FIM.MED.VA.GOV, which was created by the FIM install.

The RMIM MAIL SERVER mail group may be used in the future for better communication between Facility System and the Austin Automation Center in regards to ACK or ERR status. No members need to be in this group.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a Broker aware product written in Delphi 5, FIM connects to the M server from a client workstation. This connection is subject to authentication, as any normal logon requires. If the user is present in the new person file, successfully logs on to the VistA Server, and has the RMIMFIM option, they will have the ability to run the application. The Functional Independence Measurement can be anywhere on the VA’s TCP/IP network.

Encryption is used when a user’s access, verify, and electronic signature codes are sent from the client to the server.

See RPC Broker V. 1.1 Technical Manual page 31-32 for further information on RPC Broker’s security features.

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging functions necessary with FIM.

## Contingency Planning 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites utilizing the Functional Independence Measurement software should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

## Interfacing Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interface software is HL7. This will transmit FIM data to the AAC.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two keys associated with this software.

1.  RMIM COORD

This key is given to a user(s) who coordinate the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC). The key allows the FSOD coordinator to edit any part of the FIM record within the template prior to sending to Austin.

4.  RMIM FSOD

This key is given to user(s) who are allowed to send updates via the FIM Template to the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC).

## Equipment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Default PC Printer:

Reports require that the personal computer have a valid default printer specified. See Microsoft operating system documentation for details on setting up default printers.

# Appendix A - Databases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 28%" />
<col style="width: 12%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><strong>RMIM FIM FSOD RECORD</strong><br />
LOCAL FIM DATABASE</th>
<th></th>
<th><strong>FSOD</strong><br />
FSOD DATABASE</th>
</tr>
<tr class="odd">
<th colspan="2">NUMBER</th>
<th></th>
<th>LABEL</th>
<th></th>
<th>LABEL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>0.01</td>
<td colspan="2"></td>
<td>ENTRY NUMBER</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>0.02</td>
<td colspan="2"></td>
<td>SITE CASE NUMBER</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="even">
<td>0.03</td>
<td colspan="2"></td>
<td>PATIENT</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>0.04</td>
<td colspan="2"></td>
<td>PT ID</td>
<td></td>
<td>PATIENT_CODE/PATIENT_ID</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td>n/a</td>
<td></td>
<td>FIRST_NAME</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td>n/a</td>
<td></td>
<td>LAST_NAME</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td>n/a</td>
<td></td>
<td>MIDDLE_INITIAL</td>
</tr>
<tr class="odd">
<td>0.05</td>
<td colspan="2"></td>
<td>PT DOB</td>
<td></td>
<td>BIRTH_DATE</td>
</tr>
<tr class="even">
<td>0.06</td>
<td colspan="2"></td>
<td>FACILITY CODE</td>
<td></td>
<td>FACILITY_ID</td>
</tr>
<tr class="odd">
<td>0.07</td>
<td colspan="2"></td>
<td>TYPE OF CARE</td>
<td></td>
<td>CARE_CLASS_CODE</td>
</tr>
<tr class="even">
<td>0.08</td>
<td colspan="2"></td>
<td>IMPAIRMENT GROUP</td>
<td></td>
<td>IMPAIRMENT_CODE</td>
</tr>
<tr class="odd">
<td>0.09</td>
<td colspan="2"></td>
<td>ONSET DATE</td>
<td></td>
<td>ONSET_DATE</td>
</tr>
<tr class="even">
<td>0.1</td>
<td colspan="2"></td>
<td>ADMIT DATE</td>
<td></td>
<td>ADMIT_DATE</td>
</tr>
<tr class="odd">
<td>0.11</td>
<td colspan="2"></td>
<td>DSCHG DATE</td>
<td></td>
<td>DISCHARGE_DATE</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td>n/a</td>
<td></td>
<td>THERAPY_START_DATE</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td>n/a</td>
<td></td>
<td>THERAPY_END_DATE</td>
</tr>
<tr class="even">
<td>0.12</td>
<td colspan="2"></td>
<td>EDIT DATE</td>
<td></td>
<td>ASSESSMENT_DATE</td>
</tr>
<tr class="odd">
<td>0.13</td>
<td colspan="2"></td>
<td>XMIT DATE</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="even">
<td>0.14</td>
<td colspan="2"></td>
<td>OP CODE</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>0.15</td>
<td colspan="2"></td>
<td>READY FOR XMIT</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="even">
<td>0.16</td>
<td colspan="2"></td>
<td>PROG NOTE IEN</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>0.17</td>
<td colspan="2"></td>
<td>EMAIL ID</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="even">
<td>0.2</td>
<td colspan="2"></td>
<td>AUSTIN STATUS</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>0.21</td>
<td colspan="2"></td>
<td>ERROR DISCRIPTION</td>
<td></td>
<td>n/a</td>
</tr>
<tr class="even">
<td>1.01</td>
<td colspan="2"></td>
<td>STREET</td>
<td></td>
<td>STREET</td>
</tr>
<tr class="odd">
<td>1.02</td>
<td colspan="2"></td>
<td>CITY</td>
<td></td>
<td>CITY</td>
</tr>
<tr class="even">
<td>1.03</td>
<td colspan="2"></td>
<td>STATE</td>
<td></td>
<td>STATE</td>
</tr>
<tr class="odd">
<td>1.04</td>
<td colspan="2"></td>
<td>POSTAL CODE</td>
<td></td>
<td>POSTAL_CODE</td>
</tr>
<tr class="even">
<td>1.05</td>
<td colspan="2"></td>
<td>TELEPHONE</td>
<td></td>
<td>TELEPHONE</td>
</tr>
<tr class="odd">
<td>1.06</td>
<td colspan="2"></td>
<td>GENDER CODE</td>
<td></td>
<td>GENDER_CODE</td>
</tr>
<tr class="even">
<td>1.07</td>
<td colspan="2"></td>
<td>ETHNIC CODE</td>
<td></td>
<td>ETHNICITY_CODE</td>
</tr>
<tr class="odd">
<td>1.08</td>
<td colspan="2"></td>
<td>MARITAL CODE</td>
<td></td>
<td>MARITAL_CODE</td>
</tr>
<tr class="even">
<td>1.09</td>
<td colspan="2"></td>
<td>ACTIVE MIL IND</td>
<td></td>
<td>ACTIVE_MIL_IND</td>
</tr>
<tr class="odd">
<td>2.01</td>
<td colspan="2"></td>
<td>ADMIT CLASS</td>
<td></td>
<td>ADMIT_CLASS_CODE</td>
</tr>
<tr class="even">
<td>2.03</td>
<td colspan="2"></td>
<td>INTERRUPTION CODE</td>
<td></td>
<td>INTERRUPTION_CODE</td>
</tr>
<tr class="odd">
<td>2.04</td>
<td colspan="2"></td>
<td>TRANSFER 1 DATE</td>
<td></td>
<td>TRANSFER1_DATE</td>
</tr>
<tr class="even">
<td>2.05</td>
<td colspan="2"></td>
<td>RETURN 1 DATE</td>
<td></td>
<td>RETURN1_DATE</td>
</tr>
<tr class="odd">
<td>2.06</td>
<td colspan="2"></td>
<td>TRANSFER 2 DATE</td>
<td></td>
<td>TRANSFER2_DATE</td>
</tr>
<tr class="even">
<td>2.07</td>
<td colspan="2"></td>
<td>RETURN 2 DATE</td>
<td></td>
<td>RETURN2_DATE</td>
</tr>
<tr class="odd">
<td>2.08</td>
<td colspan="2"></td>
<td>TRANSFER 3 DATE</td>
<td></td>
<td>TRANSFER3_DATE</td>
</tr>
<tr class="even">
<td>2.09</td>
<td colspan="2"></td>
<td>RETURN 3 DATE</td>
<td></td>
<td>RETURN3_DATE</td>
</tr>
<tr class="odd">
<td>2.1</td>
<td colspan="2"></td>
<td>ETIOLOGIC CODE</td>
<td></td>
<td>ETIOLOGIC_CODE</td>
</tr>
<tr class="even">
<td>2.11</td>
<td colspan="2"></td>
<td>ASIA CODE</td>
<td></td>
<td>ASIA_CODE</td>
</tr>
<tr class="odd">
<td>3.01</td>
<td colspan="2"></td>
<td>DIAGNOSIS1</td>
<td></td>
<td>DIAGNOSIS1_CODE</td>
</tr>
<tr class="even">
<td>3.02</td>
<td colspan="2"></td>
<td>DIAGNOSIS2</td>
<td></td>
<td>DIAGNOSIS2_CODE</td>
</tr>
<tr class="odd">
<td>3.03</td>
<td colspan="2"></td>
<td>DIAGNOSIS3</td>
<td></td>
<td>DIAGNOSIS3_CODE</td>
</tr>
<tr class="even">
<td>3.04</td>
<td colspan="2"></td>
<td>DIAGNOSIS4</td>
<td></td>
<td>DIAGNOSIS4_CODE</td>
</tr>
<tr class="odd">
<td>3.05</td>
<td colspan="2"></td>
<td>DIAGNOSIS5</td>
<td></td>
<td>DIAGNOSIS5_CODE</td>
</tr>
<tr class="even">
<td>3.06</td>
<td colspan="2"></td>
<td>DIAGNOSIS6</td>
<td></td>
<td>DIAGNOSIS6_CODE</td>
</tr>
<tr class="odd">
<td>3.07</td>
<td colspan="2"></td>
<td>DIAGNOSIS7</td>
<td></td>
<td>DIAGNOSIS7_CODE</td>
</tr>
<tr class="even">
<td>4.01</td>
<td colspan="2"></td>
<td>A EAT</td>
<td></td>
<td>EAT_FIM</td>
</tr>
<tr class="odd">
<td>4.02</td>
<td colspan="2"></td>
<td>A GROOM</td>
<td></td>
<td>GROOM_FIM</td>
</tr>
<tr class="even">
<td>4.03</td>
<td colspan="2"></td>
<td>A BATH</td>
<td></td>
<td>BATH_FIM</td>
</tr>
<tr class="odd">
<td>4.04</td>
<td colspan="2"></td>
<td>A DRESS UP</td>
<td></td>
<td>DRESS_UP_FIM</td>
</tr>
<tr class="even">
<td>4.05</td>
<td colspan="2"></td>
<td>A DRESS LO</td>
<td></td>
<td>DRESS_LO_FIM</td>
</tr>
<tr class="odd">
<td>4.06</td>
<td colspan="2"></td>
<td>A TOILET</td>
<td></td>
<td>TOILET_FIM</td>
</tr>
<tr class="even">
<td>4.07</td>
<td colspan="2"></td>
<td>A BLADDER</td>
<td></td>
<td>BLADDER_FIM</td>
</tr>
<tr class="odd">
<td>4.08</td>
<td colspan="2"></td>
<td>A BOWEL</td>
<td></td>
<td>BOWEL_FIM</td>
</tr>
<tr class="even">
<td>4.09</td>
<td colspan="2"></td>
<td>A TRANS CHAIR</td>
<td></td>
<td>TRANS_CHAIR_FIM</td>
</tr>
<tr class="odd">
<td>4.1</td>
<td colspan="2"></td>
<td>A TRANS TOILET</td>
<td></td>
<td>TRANS_TOILET_FIM</td>
</tr>
<tr class="even">
<td>4.11</td>
<td colspan="2"></td>
<td>A TRANS TUB</td>
<td></td>
<td>TRANS_TUB_FIM</td>
</tr>
<tr class="odd">
<td>4.12</td>
<td colspan="2"></td>
<td>A LOCOM WALK</td>
<td></td>
<td>LOCOM_WALK_FIM</td>
</tr>
<tr class="even">
<td>4.13</td>
<td colspan="2"></td>
<td>A LOCOM STAIR</td>
<td></td>
<td>LOCOM_STAIR_FIM</td>
</tr>
<tr class="odd">
<td>4.14</td>
<td colspan="2"></td>
<td>A COMPREHEND</td>
<td></td>
<td>COMPREHEND_FIM</td>
</tr>
<tr class="even">
<td>4.15</td>
<td colspan="2"></td>
<td>A EXPRESS</td>
<td></td>
<td>EXPRESS_FIM</td>
</tr>
<tr class="odd">
<td>4.16</td>
<td colspan="2"></td>
<td>A INTERACT</td>
<td></td>
<td>INTERACT_FIM</td>
</tr>
<tr class="even">
<td>4.17</td>
<td colspan="2"></td>
<td>A PROBLEM</td>
<td></td>
<td>PROBLEM_FIM</td>
</tr>
<tr class="odd">
<td>4.18</td>
<td colspan="2"></td>
<td>A MEMORY</td>
<td></td>
<td>MEMORY_FIM</td>
</tr>
<tr class="even">
<td>4.19</td>
<td colspan="2"></td>
<td>A WALK MODE</td>
<td></td>
<td>WALK_MODE</td>
</tr>
<tr class="odd">
<td>4.2</td>
<td colspan="2"></td>
<td>A COMPREHEND MODE</td>
<td></td>
<td>COMPREHEND_MODE</td>
</tr>
<tr class="even">
<td>4.21</td>
<td colspan="2"></td>
<td>A EXPRESS MODE</td>
<td></td>
<td>EXPRESS_MODE</td>
</tr>
<tr class="odd">
<td>5.01</td>
<td colspan="2"></td>
<td>D EAT</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.02</td>
<td colspan="2"></td>
<td>D GROOM</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.03</td>
<td colspan="2"></td>
<td>D BATH</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.04</td>
<td colspan="2"></td>
<td>D DRESS UP</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.05</td>
<td colspan="2"></td>
<td>D DRESS LO</td>
<td></td>
<td>The FIM fields repeat for each type of assessment</td>
</tr>
<tr class="even">
<td>5.06</td>
<td colspan="2"></td>
<td>D TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.07</td>
<td colspan="2"></td>
<td>D BLADDER</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.08</td>
<td colspan="2"></td>
<td>D BOWEL</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.09</td>
<td colspan="2"></td>
<td>D TRANS CHAIR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.1</td>
<td colspan="2"></td>
<td>D TRANS TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.11</td>
<td colspan="2"></td>
<td>D TRANS TUB</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.12</td>
<td colspan="2"></td>
<td>D LOCOM WALK</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.13</td>
<td colspan="2"></td>
<td>D LOCOM STAIR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.14</td>
<td colspan="2"></td>
<td>D COMPREHEND</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.15</td>
<td colspan="2"></td>
<td>D EXPRESS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.16</td>
<td colspan="2"></td>
<td>D INTERACT</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.17</td>
<td colspan="2"></td>
<td>D PROBLEM</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.18</td>
<td colspan="2"></td>
<td>D MEMORY</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.19</td>
<td colspan="2"></td>
<td>D WALK MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5.2</td>
<td colspan="2"></td>
<td>D COMPREHEND MODE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5.21</td>
<td colspan="2"></td>
<td>D EXPRESS MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.01</td>
<td colspan="2"></td>
<td>I EAT</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.02</td>
<td colspan="2"></td>
<td>I GROOM</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.03</td>
<td colspan="2"></td>
<td>I BATH</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.04</td>
<td colspan="2"></td>
<td>I DRESS UP</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.05</td>
<td colspan="2"></td>
<td>I DRESS LO</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.06</td>
<td colspan="2"></td>
<td>I TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.07</td>
<td colspan="2"></td>
<td>I BLADDER</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.08</td>
<td colspan="2"></td>
<td>I BOWEL</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.09</td>
<td colspan="2"></td>
<td>I TRANS CHAIR</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.1</td>
<td colspan="2"></td>
<td>I TRANS TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.11</td>
<td colspan="2"></td>
<td>I TRANS TUB</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.12</td>
<td colspan="2"></td>
<td>I LOCOM WALK</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.13</td>
<td colspan="2"></td>
<td>I LOCOM STAIR</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.14</td>
<td colspan="2"></td>
<td>I COMPREHEND</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.15</td>
<td colspan="2"></td>
<td>I EXPRESS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.16</td>
<td colspan="2"></td>
<td>I INTERACT</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.17</td>
<td colspan="2"></td>
<td>I PROBLEM</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.18</td>
<td colspan="2"></td>
<td>I MEMORY</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.19</td>
<td colspan="2"></td>
<td>I WALK MODE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6.2</td>
<td colspan="2"></td>
<td>I COMPREHEND MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6.21</td>
<td colspan="2"></td>
<td>I EXPRESS MODE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.01</td>
<td colspan="2"></td>
<td>F EAT</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.02</td>
<td colspan="2"></td>
<td>F GROOM</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.03</td>
<td colspan="2"></td>
<td>F BATH</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.04</td>
<td colspan="2"></td>
<td>F DRESS UP</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.05</td>
<td colspan="2"></td>
<td>F DRESS LO</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.06</td>
<td colspan="2"></td>
<td>F TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.07</td>
<td colspan="2"></td>
<td>F BLADDER</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.08</td>
<td colspan="2"></td>
<td>F BOWEL</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.09</td>
<td colspan="2"></td>
<td>F TRANS CHAIR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.1</td>
<td colspan="2"></td>
<td>F TRANS TOILET</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.11</td>
<td colspan="2"></td>
<td>F TRANS TUB</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.12</td>
<td colspan="2"></td>
<td>F LOCOM WALK</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.13</td>
<td colspan="2"></td>
<td>F LOCOM STAIR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.14</td>
<td colspan="2"></td>
<td>F COMPREHEND</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.15</td>
<td colspan="2"></td>
<td>F EXPRESS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.16</td>
<td colspan="2"></td>
<td>F INTERACT</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.17</td>
<td colspan="2"></td>
<td>F PROBLEM</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.18</td>
<td colspan="2"></td>
<td>F MEMORY</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.19</td>
<td colspan="2"></td>
<td>F WALK MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7.2</td>
<td colspan="2"></td>
<td>F COMPREHEND MODE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.21</td>
<td colspan="2"></td>
<td>F EXPRESS MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>8.01</td>
<td colspan="2"></td>
<td>G EAT</td>
<td></td>
<td>EAT_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.02</td>
<td colspan="2"></td>
<td>G GROOM</td>
<td></td>
<td>GROOM_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.03</td>
<td colspan="2"></td>
<td>G BATH</td>
<td></td>
<td>BATH_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.04</td>
<td colspan="2"></td>
<td>G DRESS UP</td>
<td></td>
<td>DRESS_UP_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.05</td>
<td colspan="2"></td>
<td>G DRESS LO</td>
<td></td>
<td>DRESS_LO_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.06</td>
<td colspan="2"></td>
<td>G TOILET</td>
<td></td>
<td>TOILET_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.07</td>
<td colspan="2"></td>
<td>G BLADDER</td>
<td></td>
<td>BLADDER_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.08</td>
<td colspan="2"></td>
<td>G BOWEL</td>
<td></td>
<td>BOWEL_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.09</td>
<td colspan="2"></td>
<td>G TRANS CHAIR</td>
<td></td>
<td>TRANS_CHAIR_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.1</td>
<td colspan="2"></td>
<td>G TRANS TOILET</td>
<td></td>
<td>TRANS_TOILET_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.11</td>
<td colspan="2"></td>
<td>G TRANS TUB</td>
<td></td>
<td>TRANS_TUB_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.12</td>
<td colspan="2"></td>
<td>G LOCOM WALK</td>
<td></td>
<td>LOCOM_WALK_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.13</td>
<td colspan="2"></td>
<td>G LOCOM STAIR</td>
<td></td>
<td>LOCOM_STAIR_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.14</td>
<td colspan="2"></td>
<td>G COMPREHEND</td>
<td></td>
<td>COMPREHEND_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.15</td>
<td colspan="2"></td>
<td>G EXPRESS</td>
<td></td>
<td>EXPRESS_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.16</td>
<td colspan="2"></td>
<td>G INTERACT</td>
<td></td>
<td>INTERACT_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.17</td>
<td colspan="2"></td>
<td>G PROBLEM</td>
<td></td>
<td>PROBLEM_FIM_GOAL</td>
</tr>
<tr class="odd">
<td>8.18</td>
<td colspan="2"></td>
<td>G MEMORY</td>
<td></td>
<td>MEMORY_FIM_GOAL</td>
</tr>
<tr class="even">
<td>8.19</td>
<td colspan="2"></td>
<td>G WALK MODE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>8.2</td>
<td colspan="2"></td>
<td>G COMPREHEND MODE</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>8.21</td>
<td colspan="2"></td>
<td>G EXPRESS MODE</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix B – Health Level Seven (HL7) Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes a unidirectional interface from the VistA FIM database to the FSOD database based upon HL7 V2.3.1 messaging standards.

# General Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) Model. This is the application level. Levels one through six involve primarily communication protocols.

The TCP/IP network standard will be used to support the Transport layer and Network layer of the interface. The Minimal Lower Layer Protocol (MLLP) will be used to support the Presentation layer protocol for the interface and will encapsulate the HL7 V2.3.1 messages with start and end markers.

One link only will be required for message transactions. VistA will send a batch HL7 message and receive acknowledgments over the same link.

## Application Processing Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol will not be repeated here.

## HL7 Concepts and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. A three-character code contained within each message identifies its type.

The real-world event that initiates an exchange of messages is called a trigger event. These codes represent values such as a patient is admitted or an order event occurred. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.

### Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat.

Each segment is given a name. Each segment is identified by a unique three-character code known as the Segment ID.

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. HL7 does not care how systems actually store data within an application. When fields are transmitted, they are sent as character strings.

Except where noted, HL7 data fields may take on the null value. Sending the null value, which is transmitted as two double quote marks (“”), is different from omitting an optional data field. The difference appears when the contents of a message will be used to update a record in a database rather than create a new one. If no value is sent, (i.e., it is omitted) the old value should remain unchanged. If the null value is sent, the old value should be changed to null. Please note that at this time there will be no null values sent.

### Position (sequence within the segment)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defines the ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table. In the segment attribute tables, this information is in a column labeled SEQ.

### Maximum length

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defines the maximum number of characters that one occurrence of the data field may occupy. It is calculated to include the component and sub component separators. Because the maximum length is that of a single occurrence, the repetition separator is not included in calculating the maximum length. In the segment attribute tables, this information is in a column labeled LEN.

### Data type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defines the restrictions on the contents of the data field. There are a number of data types defined by HL7. The data types used in this specification are described in the next section titled Data Types. This information is in a column labeled DT in the segment attribute tables.

### Optionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defines whether the field is required, optional, or conditional in a segment. The designations are:

|       |                                                                                                                                                                                              |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value | Description                                                                                                                                                                                  |
| B     | Left in for backward compatibility with previous versions of HL7. The field definitions following the segment attribute table should denote the optionality of the field for prior versions. |
| C     | Conditional on the trigger event, or some other field.                                                                                                                                       |
| O     | Optional                                                                                                                                                                                     |
| R     | Required                                                                                                                                                                                     |
| X     | Not used with this trigger event                                                                                                                                                             |

In the segment attribute tables, this information is in a column labeled OPT.

### Repetition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defines whether the field may repeat. The designations are:

|           |                                                                       |
|-----------|-----------------------------------------------------------------------|
| Value     | Description                                                           |
| N         | No repetition permitted                                               |
| Y         | The field may repeat an indefinite or site-determined number of times |
| Y/Integer | The field may repeat up to the number specified by the integer        |

Each occurrence may contain the number of characters specified by the field’s maximum length. In the segment attribute tables, this information is in a column labeled RP/#.

### Message Delimiters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In constructing a message certain special characters are used. They are the segment terminator, the field separator, the component separator, subcomponent separator, repetition separator, and escape character.

The segment terminator is always a carriage return (in ASCII, a hex 0D).

The other delimiters are defined in the MSH segment, with the field delimiter in the 4th character position, and the other delimiters occurring as in the field called Encoding Characters, which is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the entire message.

The Clinical Registries interface uses the HL7 standard values, found in the table below:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th>Delimiter</th>
<th>Suggested Value</th>
<th>Encoding Character Position</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Segment Terminator</td>
<td><p>&lt;cr&gt;</p>
<p>hex 0D</p></td>
<td></td>
<td>Terminates a segment record. Implementers cannot change this value.</td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>I</td>
<td></td>
<td>Separates 2 adjacent data fields within a segment. It also separates the segment ID from the 1<sup>st</sup> data field in each segment</td>
</tr>
<tr class="odd">
<td>Component Separator</td>
<td>^</td>
<td>1</td>
<td>Separates 2 adjacent components of data fields, where allowed</td>
</tr>
<tr class="even">
<td>Subcomponent Separator</td>
<td>&amp;</td>
<td>2</td>
<td>Separates adjacent subcomponents of data fields, where allowed. If there are no subcomponents, it may be omitted</td>
</tr>
<tr class="odd">
<td>Repetition Separator</td>
<td>~</td>
<td>3</td>
<td>Separates multiple occurrences of a field, where allowed</td>
</tr>
<tr class="even">
<td>Escape Character</td>
<td>\</td>
<td>4</td>
<td>Escape Character for use with any field represented by an ST, TX or FT data type, or for use with the data component of the ED data type.</td>
</tr>
</tbody>
</table>

### Data Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Type Category/ Data type</th>
<th>Data Type Name</th>
<th>Notes/Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Alphanumeric</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ST</td>
<td>String</td>
<td></td>
</tr>
<tr class="odd">
<td>TX</td>
<td>Text data</td>
<td></td>
</tr>
<tr class="even">
<td>FT</td>
<td>Formatted text</td>
<td></td>
</tr>
<tr class="odd">
<td>Numerical</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CQ</td>
<td>Composite quantity with units</td>
<td>&lt;quantity (NM)&gt; ^ &lt;units (CE)&gt;</td>
</tr>
<tr class="odd">
<td>NM</td>
<td>Numeric</td>
<td></td>
</tr>
<tr class="even">
<td>SI</td>
<td>Sequence ID</td>
<td></td>
</tr>
<tr class="odd">
<td>Identifier</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ID</td>
<td>Coded values for HL7 tables</td>
<td></td>
</tr>
<tr class="odd">
<td>IS</td>
<td>Coded value for user-defined tables</td>
<td></td>
</tr>
<tr class="even">
<td>HD</td>
<td>Hierarchic designator</td>
<td><p>&lt;namespace ID (IS)&gt; ^ &lt;universal ID (ST)&gt; ^ &lt;universal ID type (ID)&gt;</p>
<p>Used only as part of EI and other data types.</p></td>
</tr>
<tr class="odd">
<td>EI</td>
<td>Entity identifier</td>
<td>&lt;entity identifier (ST)&gt; ^ &lt;namespace ID (IS)&gt; ^ &lt;universal ID (ST)&gt; ^ &lt;universal ID type (ID)&gt;</td>
</tr>
<tr class="even">
<td>PL</td>
<td>Person location</td>
<td>&lt;point of care (IS)&gt; ^ &lt;room (IS)&gt; ^ &lt;bed (IS)&gt; ^ &lt;facility (HD)&gt; ^ &lt; location status (IS )&gt; ^ &lt;person location type (IS)&gt; ^ &lt;building (IS)&gt; ^ &lt;floor (IS)&gt; ^ &lt;location description (ST)&gt;</td>
</tr>
<tr class="odd">
<td>PT</td>
<td>Processing type</td>
<td>&lt;processing ID (ID)&gt; ^ &lt;processing mode (ID)&gt;</td>
</tr>
<tr class="even">
<td>Date/Time</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DT</td>
<td>Date</td>
<td>YYYY[MM[DD]]</td>
</tr>
<tr class="even">
<td>TM</td>
<td>Time</td>
<td>HH[MM[SS[.S[S[S[S]]]]]][+/-ZZZZ]</td>
</tr>
<tr class="odd">
<td>TS</td>
<td>Time stamp</td>
<td>YYYY[MM[DD[HHMM[SS[.S[S[S[S]]]]]]]][+/-ZZZZ] ^ &lt;degree of precision&gt;</td>
</tr>
<tr class="even">
<td>Code Values</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CE</td>
<td>Coded element</td>
<td>&lt;identifier (ST)&gt; ^ &lt;text (ST)&gt; ^ &lt;name of coding system (ST)&gt; ^ &lt;alternate identifier (ST)&gt; ^ &lt;alternate text (ST)&gt; ^ &lt;name of alternate coding system (ST)&gt;</td>
</tr>
<tr class="even">
<td>CX</td>
<td>Extended composite ID with check digit</td>
<td>&lt;ID (ST)&gt; ^ &lt;check digit (ST)&gt; ^ &lt;code identifying the check digit scheme employed (ID)&gt; ^ &lt; assigning authority (HD)&gt; ^ &lt;identifier type code (IS)&gt; ^ &lt; assigning facility (HD)</td>
</tr>
<tr class="odd">
<td>XCN</td>
<td>Extended composite ID number and name</td>
<td>In Version 2.3, use instead of the CN data type. &lt;ID number (ST)&gt; ^ &lt;family name (ST)&gt; &amp; &lt;last_name_prefix (ST) ^ &lt;given name (ST)&gt; ^ &lt;middle initial or name (ST)&gt; ^ &lt;suffix (e.g., JR or III) (ST)&gt; ^ &lt;prefix (e.g., DR) (ST)&gt; ^ &lt;degree (e.g., MD) (ST)&gt; ^ &lt;source table (IS)&gt; ^ &lt;assigning authority (HD)&gt; ^ &lt;name type code (ID)&gt; ^ &lt;identifier check digit (ST)&gt; ^ &lt;code identifying the check digit scheme employed (ID)&gt; ^ &lt;identifier type code (IS)&gt; ^ &lt;assigning facility (HD)&gt; ^ &lt;name representation code (ID)&gt;</td>
</tr>
<tr class="even">
<td>Generic</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CM</td>
<td>Composite</td>
<td>No new CM’s are allowed after HL7 Version 2.2. Hence there are no new CM’s in Version 2.3.</td>
</tr>
<tr class="even">
<td>Demographics</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>XAD</td>
<td>Extended address</td>
<td>In Version 2.3, replaces the AD data type. &lt;street address (ST)&gt; ^ &lt;other designation (ST)&gt; ^ &lt;city (ST)&gt; ^ &lt;state or province (ST)&gt; ^ &lt;zip or postal code (ST)&gt; ^ &lt;country (ID)&gt; ^ &lt; address type (ID)&gt; ^ &lt;other geographic designation (ST)&gt; ^ &lt;county/parish code (IS)&gt; ^ &lt;census tract (IS)&gt; ^ &lt;address representation code (ID)&gt;</td>
</tr>
<tr class="even">
<td>XPN</td>
<td>Extended person name</td>
<td>In Version 2.3, replaces the PN data type. &lt;family name (ST)&gt; ^ &lt;given name (ST)&gt; &amp; &lt;last_name_prefix (ST)&gt; ^ &lt;middle initial or name (ST)&gt; ^ &lt;suffix (e.g., JR or III) (ST)&gt; ^ &lt;prefix (e.g., DR) (ST)&gt; ^ &lt;degree (e.g., MD) (IS)&gt; ^ &lt;name type code (ID) &gt; ^ &lt;name representation code (ID)&gt;</td>
</tr>
<tr class="odd">
<td>XON</td>
<td>Extended composite name and ID number for organizations</td>
<td>&lt;organization name (ST)&gt; ^ &lt;organization name type code (IS)&gt; ^ &lt;ID number (NM)&gt; ^ &lt;check digit (NM)&gt; ^ &lt;code identifying the check digit scheme employed (ID)&gt; ^ &lt;assigning authority (HD)&gt; ^ &lt;identifier type code (IS)&gt; ^ &lt;assigning facility ID (HD)&gt; ^ &lt;name representation code (ID)&gt;</td>
</tr>
<tr class="even">
<td>XTN</td>
<td>Extended telecommunications number</td>
<td>In Version 2.3, replaces the TN data type. [NNN] [(999)]999-9999 [X99999] [B99999] [C any text] ^ &lt;telecommunication use code (ID)&gt; ^ &lt;telecommunication equipment type (ID)&gt; ^ &lt;email address (ST)&gt; ^ &lt;country code (NM)&gt; ^ &lt;area/city code (NM)&gt; ^ &lt;phone number (NM)&gt; ^ &lt;extension (NM)&gt; ^ &lt;any text (ST)&gt;</td>
</tr>
<tr class="odd">
<td>Time Series:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>TQ</td>
<td>Timing/quantity</td>
<td>For timing/quantity specifications for orders, see Chapter 4, Section 4.4. &lt;quantity (CQ)&gt; ^ &lt;interval (*)&gt; ^ &lt;duration (*)&gt; ^ &lt;start date/time (TS)&gt; ^ &lt;end date/time (TS)&gt; ^ &lt;priority (ST)&gt; ^ &lt;condition (ST)&gt; ^ &lt;text (TX)&gt; ^ &lt;conjunction (ID)&gt; ^ &lt;order sequencing (*)&gt; ^ &lt;performance duration (CE)&gt; ^ &lt;total occurrences (NM)&gt;</td>
</tr>
</tbody>
</table>

### Use of Escape Sequences in Text Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a field of type TX, FT, or CF is being encoded, the escape character may be used to signal certain special characteristics of portions of the text field. The escape character is whatever display ASCII character is specified in the Escape Character component of *MSH-2-encoding character*s.

The character \\ must be used to represent the character so designated in a message. An escape sequence consists of the escape character followed by an escape code ID of one character, and another occurrence of the escape character. The following escape sequences are used by the Hepatitis C HL7 interface:

|       |                        |
|-------|------------------------|
| Value | Description            |
| \S\\  | Component separator    |
| \T\\  | Subcomponent separator |
| \R\\  | Repetition separator   |
| \E\\  | Escape character       |

## Specification Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Segment Tables Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|              |                                                            |
|--------------|------------------------------------------------------------|
| Column       | Description                                                |
| SEQ          | Ordinal position of the data field within the segment      |
| LEN          | Maximum length of a field                                  |
| DT           | HL7 data type                                              |
| OPT          | Required, Optional, Conditional, or Backward compatible    |
| RP/#         | Repeating field (Y/N/#)                                    |
| ELEMENT NAME | Field description                                          |
| COMMENTS     | Set to ‘See Notes’, if the field is used in this interface |

# HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HL7 Message Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message is sent as a batch message. Each patient will be transmitted as an individual record.

ORU Observational Results (Unsolicited)

MSH Message Header

PID Patient Identification

\[PV1\] Patient Visit

{NTE} Notes and Comments

{

OBR Observations Report ID

{

\[OBX\] Observation/Result  
}

### ORU – Unsolicited transmission of an observation (Event type R01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The function of this message is to initiate the transmission of information about a report. With the observation segment (OBX), and the OBR, one can construct almost any clinical report as a three‑level hierarchy, with the PID segment at the upper level, an order segment (OBR) at the next level and one or more observation segments (OBX) at the bottom. One result segment (OBX) is transmitted for each component of a diagnostic report, such as a series of Diagnosis codes or an Admission’s scores.

| Segment | Order Message          | HL7 Chapter |
|---------|------------------------|-------------|
| MSH     | Message header         | 2           |
| PID     | Patient identification | 3           |
| OBR     | Order detail           | 4           |
| OBX     | Observation/Result     | 7           |

## HL7 Segment Definitions and Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | ELEMENT NAME                    | COMMENTS  |
|-----|-----|-----|-----|------|---------------------------------|-----------|
| 1   | 1   | ST  | R   |      | Field Separator                 | See Notes |
| 2   | 4   | ST  | R   |      | Encoding Characters             | See Notes |
| 3   | 180 | HD  | O   |      | Sending Application             | See Notes |
| 4   | 180 | HD  | O   |      | Sending Facility                | See Notes |
| 5   | 180 | HD  | O   |      | Receiving Application           | See Notes |
| 6   | 180 | HD  | O   |      | Receiving Facility              | See Notes |
| 7   | 26  | TS  | O   |      | Date/Time Of Message            | See Notes |
| 8   | 40  | ST  | O   |      | Security                        | NV        |
| 9   | 7   | CM  | R   |      | Message Type                    | See Notes |
| 10  | 20  | ST  | R   |      | Message Control ID              | See Notes |
| 11  | 3   | PT  | R   |      | Processing ID                   | See Notes |
| 12  | 8   | ID  | R   |      | Version ID                      | See Notes |
| 13  | 15  | NM  | O   |      | Sequence Number                 | NV        |
| 14  | 180 | ST  | O   |      | Continuation Pointer            | NV        |
| 15  | 2   | ID  | O   |      | Accept Acknowledgment Type      | NV        |
| 16  | 2   | ID  | O   |      | Application Acknowledgment Type | NV        |
| 17  | 2   | ID  | O   |      | Country Code                    | See Notes |
| 18  | 6   | ID  | O   | Y/3  | Character Set                   | NV        |
| 19  | 60  | CE  | O   |      | Principal Language Of Message   | NV        |

### MSH field definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSH – Field Separator \<1\>/\<1\>/\<ST\>

Definition: This field contains the separator between the segment ID and the first real field, *MSH-2-encoding characters*. As such, it serves as the separator and defines the character to be used as a separator for the rest of the message. Recommended value is \|, (ASCII 124).

#### MSH – Encoding Characters \<2\>/\<4\>/\<ST\>

Definition: This field contains the four characters in the following order: the component separator, repetition separator, escape character, and subcomponent separator. Recommended values are ^~\\, (ASCII 94, 126, 92, and 38, respectively).

#### MSH – Sending Application \<3\>/\<180\>/\<HD\>

Definition: This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site defined.

#### MSH – Sending Facility \<4\>/\<180\>/\<HD\>

Definition: This field contains the address of one of several occurrences of the same application within the sending system. Entirely user‑defined.

#### MSH – Receiving Application \<5\>/\<180\>/\<HD\>

Definition: This field uniquely identifies the receiving application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site‑defined.

#### MSH – Receiving Facility \<6\>/\<180\>/\<HD\>

Definition: This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations. See comments: *MSH-4-sending facility*. Entirely site‑defined.

#### MSH – Date/Time Of Message \<7\>/\<26\>/\<TS\>

Definition: This field contains the date/time that the sending system created the message. If the time zone is specified, it will be used throughout the message as the default time zone.

Format: YYYYMMDDHHMMSS

MSH – Message Type \<9\>/\<7\>/\<CM\>

Components: \<message type (ID)\> ^ \<trigger event (ID)\>

Definition: This field contains the message type and trigger event for the message.

VistA sends an ORM message type with the trigger event O01 for orders from Radiology/Nuclear Medicine and TIU. An ORU message type with the trigger event R01 for unsolicited observation results is sent to VistA.

#### MSH – Message Control ID \<10\>/\<20\>/\<ST\>

Definition: This field contains a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message acknowledgment segment (MSA).

#### MSH – Processing ID \<11\>/\<3\>/\<PT\>

Components: \<processing ID (ID)\> ^ \<processing mode (ID)\>

Definition: This field identifies the status of the interface. The processing mode component is not used.

| Value | Description |
|-------|-------------|
| P     | Production  |
| D     | Debugging   |
| T     | Training    |

#### MSH – Version ID \<12\>/\<8\>/\<ID\>

Definition: This field is matched by the receiving system to its own version to be sure the message will be interpreted correctly.

The VistA TIU Connection interface currently uses version 2.3 of the HL7 standard. However, future versions will be implemented as needed.

#### MSH – Country Code \<17\>/\<2\>/\<ID\>

Definition: This field contains the country of origin for the message.

Example:

MSH\|^~\\\|RMIM SITE\|FIM\|RMIM AAC\|FSOD\|20021009123935-0500\|\|ORU^R01^ORU_R01\|54823249\|T\|2.4\|\|\|NE\|AL\|US

### PID Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | ELEMENT NAME                      | COMMENTS  |
|-----|-----|-----|-----|------|-----------------------------------|-----------|
| 1   | 4   | SI  | O   |      | Set ID - Patient ID               | NV        |
| 2   | 20  | CX  | O   |      | Patient ID (External ID)          | See Notes |
| 3   | 20  | CX  | R   | Y    | Patient ID (Internal ID)          | See Notes |
| 4   | 20  | CX  | O   | Y    | Alternate Patient ID - PID        | See Notes |
| 5   | 48  | XPN | R   | Y    | Patient Name                      | See Notes |
| 6   | 48  | XPN | O   |      | Mother’s Maiden Name              | NV        |
| 7   | 26  | TS  | O   |      | Date/Time of Birth                | See Notes |
| 8   | 1   | IS  | O   |      | Sex                               | See Notes |
| 9   | 48  | XPN | O   | Y    | Patient Alias                     | NV        |
| 10  | 1   | IS  | O   |      | Race                              | See Notes |
| 11  | 106 | XAD | O   | Y    | Patient Address                   | See Notes |
| 12  | 4   | IS  | B   |      | County Code                       | NV        |
| 13  | 40  | XTN | O   | Y    | Phone Number - Home               | See Notes |
| 14  | 40  | XTN | O   | Y    | Phone Number - Business           | NV        |
| 15  | 60  | CE  | O   |      | Primary Language                  | NV        |
| 16  | 1   | IS  | O   |      | Marital Status                    | See Notes |
| 17  | 3   | IS  | O   |      | Religion                          | NV        |
| 18  | 20  | CX  | O   |      | Patient Account Number            | NV        |
| 19  | 16  | ST  | O   |      | SSN - Patient                     | See Notes |
| 20  | 25  | DLN | O   |      | Driver's License Number - Patient | NV        |
| 21  | 20  | CX  | O   | Y    | Mother's Identifier               | NV        |
| 22  | 3   | IS  | O   |      | Ethnic Group                      | NV        |
| 23  | 60  | ST  | O   |      | Birth Place                       | NV        |
| 24  | 2   | ID  | O   |      | Multiple Birth Indicator          | NV        |
| 25  | 2   | NM  | O   |      | Birth Order                       | NV        |
| 26  | 4   | IS  | O   | Y    | Citizenship                       | NV        |
| 27  | 60  | CE  | O   |      | Veterans Military Status          | See Notes |
| 28  | 80  | CE  | O   |      | Nationality                       | NV        |
| 29  | 26  | TS  | O   |      | Patient Death Date and Time       | NV        |
| 30  | 1   | ID  | O   |      | Patient Death Indicator           | NV        |

### PID field definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID – Patient ID (external ID) \<2\>/\<20\>/\<CX\>

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>

Definition: When the patient is from another institution, outside office, etc., the identifier used by that institution can be shown in this field. This contains the patient SSN.

#### PID – Patient ID (internal ID) \<3\>/\<20\>/\<CX\> 

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>

Definition: This field contains the primary identifier, or other identifiers used by the facility to identify a patient uniquely. This will be VistA DFN.

#### PID – Alternate patient ID \<4\>/\<20\>/\<CX\>

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<assigning authority (HD)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\>

Definition: This field contains the IEN and local Case number.

#### PID – Patient Name \<5\>/\<48\>/\<XPN\> 

Components: \<family name (ST)\> ^ \<given name (ST)\> ^ \<middle initial or name (ST)\>

Definition: This field contains the legal name of the patient.

#### PID – Date/Time of Birth \<7\>/\<26\>/\<TS\> 

Definition: This field contains the patient’s date of birth.

Format: YYYYMMDD

#### PID – Sex \<8\>/\<1\>/\<IS\> 

Definition: This field contains the patient’s sex.

| Value | Description |
|-------|-------------|
| 2     | Female      |
| 1     | Male        |

#### PID – Race \<10\>/\<1\>/\<IS\>

Definition: This field refers to the patient’s ethnic code.

1-White

2-Black

3-Asian

4-Native American

5-Other

6-Hispanic

#### PID – Patient Address \<11\>/\<106\>/\<XAD\>

Components: \<street address (ST)\> ^ \<other designation (ST)\> ^ \<city (ST)\> ^ \<state or province (ST)\> ^ \<zip or postal code(ST)\> ^ \<country (ID)\> ^ \< address type (ID)\> ^ \<other geographic designation (ST)\> ^ \<county/parish code (IS)\> ^ \<census tract (IS)\>

Definition: This field contains the mailing address of the patient.

#### PID – Telephone \<13\>/\<40\>/\<XTN\>

Definition: This field contains the patient’s Telephone Number.

#### PID – Marital Code \<16\>/\<1\>/\<IS\>

Definition: This field contains the patient’s Marital Code.

1-Never Married

2-Married

3-Widowed

4-Separated

5-Divorced

#### PID – SSN – Patient \<19\>/\<16\>/\<ST\>

Definition: This field contains the patient’s social security number.

Format: \[555555555\] or \[555555555P\]

> **NOTE:** PID does not include the “-“ in this field.

#### PID – Veterans Military Status \<27\>/\<16\>/\<ST\>

Definition: This field contains the patient’s Active Military Indicator.

A-Active Military

N-Not Active Military

#### Example PID segment

PID\|\|000001640\|2604\|8^25\|TEST^SAM^ONE\|\|19400516\|1\|\|\|NONE^^LONGLY^^12345^USA\|\|(561)123-1234\|\|\|\|\|\|000001640\|\|\|\|\|\|\|\|N

### PV1 Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | ELEMENT NAME              | COMMENTS  |
|-----|-----|-----|-----|------|---------------------------|-----------|
| 1   | 4   | SI  | O   |      | Set ID - PV1              | NV        |
| 2   | 1   | IS  | R   |      | Patient Class             | See Notes |
| 3   | 80  | PL  | O   |      | Assigned Patient Location | NV        |
| 4   | 2   | IS  | O   |      | Admission Type            | See Notes |
| 5   | 20  | CX  | O   |      | Preadmit Number           | NV        |
| 6   | 80  | PL  | O   |      | Prior Patient Location    | NV        |
| 7   | 60  | XCN | O   | Y    | Attending Doctor          | NV        |
| 8   | 60  | XCN | O   | Y    | Referring Doctor          | NV        |
| 9   | 60  | XCN | O   | Y    | Consulting Doctor         | NV        |
| 10  | 3   | IS  | O   |      | Hospital Service          | NV        |
| 11  | 80  | PL  | O   |      | Temporary Location        | NV        |
| 12  | 2   | IS  | O   |      | Preadmit Test Indicator   | NV        |
| 13  | 2   | IS  | O   |      | Readmission Indicator     | NV        |
| 14  | 3   | IS  | O   |      | Admit Source              | NV        |
| 15  | 2   | IS  | O   | Y    | Ambulatory Status         | NV        |
| 16  | 2   | IS  | O   |      | VIP Indicator             | NV        |
| 17  | 60  | XCN | O   | Y    | Admitting Doctor          | NV        |
| 18  | 2   | IS  | O   |      | Patient Type              | NV        |
| 19  | 20  | CX  | O   |      | Visit Number              | NV        |
| 20  | 50  | FC  | O   | Y    | Financial Class           | NV        |
| 21  | 2   | IS  | O   |      | Charge Price Indicator    | NV        |
| 22  | 2   | IS  | O   |      | Courtesy Code             | NV        |
| 23  | 2   | IS  | O   |      | Credit Rating             | NV        |
| 24  | 2   | IS  | O   | Y    | Contract Code             | NV        |
| 25  | 8   | DT  | O   | Y    | Contract Effective Date   | NV        |
| 26  | 12  | NM  | O   | Y    | Contract Amount           | NV        |
| 27  | 3   | NM  | O   | Y    | Contract Period           | NV        |
| 28  | 2   | IS  | O   |      | Interest Code             | NV        |
| 29  | 1   | IS  | O   |      | Transfer to Bad Debt Code | NV        |
| 30  | 8   | DT  | O   |      | Transfer to Bad Debt Date | NV        |
| 31  | 10  | IS  | O   |      | Bad Debt Agency Code      | NV        |
| 32  | 12  | NM  | O   |      | Bad Debt Transfer Amount  | NV        |
| 33  | 12  | NM  | O   |      | Bad Debt Recovery Amount  | NV        |
| 34  | 1   | IS  | O   |      | Delete Account Indicator  | NV        |
| 35  | 8   | DT  | O   |      | Delete Account Date       | NV        |
| 36  | 3   | IS  | O   |      | Discharge Disposition     | NV        |
| 37  | 25  | CM  | O   |      | Discharged to Location    | NV        |
| 38  | 2   | IS  | O   |      | Diet Type                 | NV        |
| 39  | 2   | IS  | O   |      | Servicing Facility        | NV        |
| 40  | 1   | IS  | B   |      | Bed Status                | NV        |
| 41  | 2   | IS  | O   |      | Account Status            | NV        |
| 42  | 80  | PL  | O   |      | Pending Location          | NV        |
| 43  | 80  | PL  | O   |      | Prior Temporary Location  | NV        |
| 44  | 26  | TS  | O   |      | Admit Date/Time           | See Notes |
| 45  | 26  | TS  | O   |      | Discharge Date/Time       | See Notes |
| 46  | 12  | NM  | O   |      | Current Patient Balance   | NV        |
| 47  | 12  | NM  | O   |      | Total Charges             | NV        |
| 48  | 12  | NM  | O   |      | Total Adjustments         | NV        |
| 49  | 12  | NM  | O   |      | Total Payments            | NV        |
| 50  | 20  | CX  | O   |      | Alternate Visit ID        | NV        |
| 51  | 1   | IS  | O   |      | Visit Indicator           | NV        |
| 52  | 60  | XCN | O   | Y    | Other Healthcare Provider | NV        |

## PV1 Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PV1 – Admission Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PV1 – Patient Class \<2\>/\<1\>/\<IS\>

Care Class Code

1= Acute Rehab Inpatient

2= Sub Acute Rehab Inpatient

3= Continuum of Care

#### PV1 – Admission Type \<4\>/\<2\>/\<IS\>

Admit Class Code

1= Initial Rehab

2= Short Stay

3= Readmission

#### PV1 – Admit Date/Time \<44\>/\<26\>/\<TS\>

Definition: This field contains the admit date/time. It is to be used if the event date/time is different than the admit date and time, i.e., a retroactive update. This field is also used to reflect the date/time of an outpatient/emergency patient registration.

> **NOTE:** Date could be a Therapy Start Date depending on the admit class code.

#### PV1 – Discharge Date/Time \<45\>/\<26\>/\<TS\>

Definition: This field contains the discharge date/time. It is to be used if the event date/time is different than the discharge date and time, that is, a retroactive update. This field is also used to reflect the date/time of an outpatient/emergency patient discharge.

> **NOTE:** Date could be a Therapy Start Date depending on the admit class code.

#### Example PV1 segment

PV1\| \|CLASS\| \|ADMIT\| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \| \|20020801\|20020801

## NTE – Notes and Comments Segment – Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     |     |     |     |      |                   |           |
|-----|-----|-----|-----|------|-------------------|-----------|
| SEQ | LEN | DT  | OPT | RP/# | ELEMENT NAME      | COMMENTS  |
| 1   | 4   | SI  | O   |      | Set ID – NTE      | NV        |
| 2   | 8   | ID  | O   |      | Source of Comment | NV        |
| 3   | 245 | FT  | O   | Y    | Comment           | See Notes |
| 4   | 60  | CE  | O   |      | Comment Type      |           |

### NTE field definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NTE-3 Comment

Definition: This field contains the transfer/return dates.

Transfer 1 date – Return 1 date – Transfer 2 date – Return 2 date – Transfer 3 date – Return 3 date

Example: CCCCMMDD

#### Example NTE segment

NTE\|1\|L\|20020923^20020923^20020923^20020923^20020923^20020923\|

### OBR Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | ELEMENT NAME                               | COMMENTS  |
|-----|-----|-----|-----|------|--------------------------------------------|-----------|
| 1   | 4   | SI  | C   |      | Set ID ‑ OBR                               | NV        |
| 2   | 75  | EI  | C   |      | Placer Order Number                        | NV        |
| 3   | 75  | EI  | C   |      | Filler Order Number +                      | NV        |
| 4   | 200 | CE  | R   |      | Universal Service ID                       | See Notes |
| 5   | 2   | ID  | B   |      | Priority                                   | NV        |
| 6   | 26  | TS  | B   |      | Requested Date/time                        | NV        |
| 7   | 26  | TS  | C   |      | Observation Date/Time \#                   | See Notes |
| 8   | 26  | TS  | O   |      | Observation End Date/Time \#               | NV        |
| 9   | 20  | CQ  | O   |      | Collection Volume \*                       | NV        |
| 10  | 60  | XCN | O   | Y    | Collector Identifier \*                    | NV        |
| 11  | 1   | ID  | O   |      | Specimen Action Code \*                    | NV        |
| 12  | 60  | CE  | O   |      | Danger Code                                | NV        |
| 13  | 300 | ST  | O   |      | Relevant Clinical Info.                    | See Notes |
| 14  | 26  | TS  | C   |      | Specimen Received Date/Time \*             | NV        |
| 15  | 300 | CM  | O   |      | Specimen Source \*                         | NV        |
| 16  | 80  | XCN | O   | Y    | Ordering Provider                          | NV        |
| 17  | 40  | XTN | O   | Y/2  | Order Callback Phone Number                | NV        |
| 18  | 60  | ST  | O   |      | Placer field 1                             | NV        |
| 19  | 60  | ST  | O   |      | Placer field 2                             | NV        |
| 20  | 60  | ST  | O   |      | Filler Field 1 +                           | NV        |
| 21  | 60  | ST  | O   |      | Filler Field 2 +                           | NV        |
| 22  | 26  | TS  | C   |      | Results Rpt/Status Chng - Date/Time +      | NV        |
| 23  | 40  | CM  | O   |      | Charge to Practice +                       | NV        |
| 24  | 10  | ID  | O   |      | Diagnostic Serv Sect ID                    | NV        |
| 25  | 1   | ID  | C   |      | Result Status +                            | NV        |
| 26  | 400 | CM  | O   |      | Parent Result +                            | NV        |
| 27  | 200 | TQ  | O   | Y    | Quantity/Timing                            | NV        |
| 28  | 150 | XCN | O   | Y/5  | Result Copies To                           | NV        |
| 29  | 150 | CM  | O   |      | Parent                                     | NV        |
| 30  | 20  | ID  | O   |      | Transportation Mode                        | NV        |
| 31  | 300 | CE  | O   | Y    | Reason for Study                           | NV        |
| 32  | 200 | CM  | O   |      | Principal Result Interpreter +             | NV        |
| 33  | 200 | CM  | O   | Y    | Assistant Result Interpreter +             | NV        |
| 34  | 200 | CM  | O   | Y    | Technician +                               | NV        |
| 35  | 200 | CM  | O   | Y    | Transcriptionist +                         | NV        |
| 36  | 26  | TS  | O   |      | Scheduled Date/Time +                      | NV        |
| 37  | 4   | NM  | O   |      | Number of Sample Containers \*             | NV        |
| 38  | 60  | CE  | O   | Y    | Transport Logistics of Collected Sample \* | NV        |
| 39  | 200 | CE  | O   | Y    | Collector’s Comment \*                     | NV        |
| 40  | 60  | CE  | O   |      | Transport Arrangement Responsibility       | NV        |
| 41  | 30  | ID  | O   |      | Transport Arranged                         | NV        |
| 42  | 1   | ID  | O   |      | Escort Required                            | NV        |
| 43  | 200 | CE  | O   | Y    | Planned Patient Transport Comment          | NV        |

### OBR Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBR – Universal Service ID \<4\>/\<200\>/\<CE\>

This will be the fields required separated by ^SSN^DOB^Care Class^ Onset Date^Impairment Group^ Admit Date^Facility Code

#### OBR – Observation Date/time \# \<7\>/\<26\>/\<TS\>

Assessment Date (length/size 10)

#### OBR – Relevant Clinical Info. \<13\>/\<300\>/\<ST\>

Etiologic Code (length/size 10)

#### Example OBR segment

OBR\|\|\|\|000001640^19400516^1^20020826^17.51^20020828^1433\|\|\|20020916\|\|\|\|\|\|250.0

### OBX Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/#  | ELEMENT NAME                 | COMMENTS  |
|-----|-----|-----|-----|-------|------------------------------|-----------|
| 1   | 10  | SI  | O   |       | Set ID - OBX                 | See Notes |
| 2   | 2   | ID  | C   |       | Value Type                   | See Notes |
| 3   | 590 | CE  | R   |       | Observation Identifier       | See Notes |
| 4   | 20  | ST  | C   |       | Observation Sub-ID           | NV        |
| 5   | 245 | \*  | C   | Y[^1] | Observation Value            | See Notes |
| 6   | 60  | CE  | O   |       | Units                        | NV        |
| 7   | 10  | ST  | O   |       | References Range             | NV        |
| 8   | 5   | ID  | O   | Y/5   | Abnormal Flags               | NV        |
| 9   | 5   | NM  | O   |       | Probability                  | NV        |
| 10  | 2   | ID  | O   | Y     | Nature of Abnormal Test      | NV        |
| 11  | 1   | ID  | R   |       | Observ Result Status         | See Notes |
| 12  | 26  | TS  | O   |       | Date Last Obs Normal Values  | NV        |
| 13  | 20  | ST  | O   |       | User Defined Access Checks   | NV        |
| 14  | 26  | TS  | O   |       | Date/Time of the Observation | NV        |
| 15  | 60  | CE  | O   |       | Producer's ID                | NV        |
| 16  | 80  | XCN | O   |       | Responsible Observer         | NV        |
| 17  | 60  | CE  | O   | Y     | Observation Method           | NV        |

### OBX field definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX – Set ID – OBX \<1\>/\<10\>/\<SI\>

Defined as array number.

#### OBX – Value Type \<2\>/\<2\>/\<ID\>

Defined as NM = Assessment Type Data

CE = Diagnoses Data

FT= Case Notes

TX= DME Items

#### OBX – Observation Identifier \<3\>/\<590\>/\>CE\>

A= Admission, D= Discharge, I= Interim, F= Follow-up and G= Goals

Diagnoses

Case Notes

DME Items

#### OBX – Observation Value \<5\>/\<65536\>/\<\>

ASIA Impairment Scale

A-Complete

B-Sensory Preserved

C-Motor Nonfunctional

D-Motor Functional

E-Normal

The value of the Results 0-9 on scores for different assessment types or the ASIA code followed by the 7 Diagnoses codes. Will be based on Observation Identifier

#### OBX – Observ Result Status \<11\>/\<1\>/\<ID\> 

Always an F – used by HL7

#### Example OBX segment

OBX\|1\|NM\|ADMISSION\| \|1^^1^^^^2^^^^^1^^^^4^^^^3\| \| \| \| \| \|F

OBX\|2\|CE\|DIAGNOSES CODE\| \|A^610.1^^410.0^^^^750.1\| \| \| \| \| \|F

OBX\|nn\|FT\|CASE NOTES\| \|test of the note\| \| \| \| \| \|F

OBX\|nn\|TX\|DME ITEMS\| \|item^cost\| \| \| \| \| \|F

[^1]: May repeat for multipart, single answer results with appropriate data types, e.g., CE, TX, and FT data types.