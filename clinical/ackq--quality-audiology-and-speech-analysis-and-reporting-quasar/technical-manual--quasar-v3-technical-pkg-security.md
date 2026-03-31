---
title: QUASAR Version 3 Technical/Pkg Security (Updated ACKQ*3*13)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: Technical/Pkg Security (Updated ACKQ*3*13)
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3
group_key: "ACKQ:ACKQ:3"
file_numbers: []
security_keys: []
menu_options: 4
description: "QUASAR (Quality: Audiology and Speech Analysis and Reporting) is a VistA software package written for the Audiology and Speech Pathology Service (ASPS). QUASAR is used to enter, edit, and retrieve data for each audiometric exam of a patient and provides for the transmission of this data to various p"
audience: 
keywords: 
  - threshold
  - initial
  - table
  - level
  - contents
  - final
  - mask
  - thresh
  - audiogram
  - class
page_count: 0
word_count: 7715
section_count: 20
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0p13_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0p13_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

![](quasar-version-3-technical-pkg-security-updated-ackq-3-13/001.png)

QUASAR Audiogram Module  
Technical Manual and Package Security Guide

Version 3.0.12

November 2005

For Patch ACKQ\*3.0\*13

Health Systems Design & Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Related Documentation](#related-documentation)
  - [Audiogram Display through CPRS](#audiogram-display-through-cprs)
  - [Additional Information](#additional-information)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Required Site-specific Data](#required-site-specific-data)
  - [Installation Process](#installation-process)
    - [RPC Broker V1.1](#rpc-broker-v11)
    - [CPRS](#cprs)
    - [KIDS](#kids)
    - [QUASAR Audiogram Module (Audiogram Edit)](#quasar-audiogram-module-audiogram-edit)
    - [Remote Procedure](#remote-procedure)
    - [M Routine List](#m-routine-list)
    - [Delphi Executable](#delphi-executable)
    - [Vendor Installer](#vendor-installer)
    - [Troubleshooting QUASAR Audiogram Module](#troubleshooting-quasar-audiogram-module)
- [Process Logic](#process-logic)
  - [Transmission of Audiometric Data](#transmission-of-audiometric-data)
- [Files](#files)
  - [Audiometric Exam Data: ^ACK(509850.9](#audiometric-exam-data-ack5098509)
    - [Files Referenced in ^ACK(509850.9](#files-referenced-in-ack5098509)
- [Routines](#routines)
  - [M Routines](#m-routines)
  - [Delphi Routines](#delphi-routines)
- [Exported Options](#exported-options)
  - [ACKQROES3E - Audiogram Edit](#ackqroes3e-audiogram-edit)
- [Archiving and Purging](#archiving-and-purging)
  - [^ACK(509850.9,](#ack5098509)
- [APIs](#apis)
  - [START^ACKQAG03](#startackqag03)
  - [ACKEXIST^ACKQAG05](#ackexistackqag05)
  - [DFNIN^ACKQAG05](#dfninackqag05)
  - [NEWMSG^ACKQAG05](#newmsgackqag05)
- [RPC](#rpc)
    - [ACKQAUD1](#ackqaud1)
- [External Relationships](#external-relationships)
  - [CPRS Functionality](#cprs-functionality)
  - [Recommended Desktop Minimums](#recommended-desktop-minimums)
- [Integration Agreements](#integration-agreements)
- [Internal Relationships](#internal-relationships)
    - [M routines[^16]](#m-routines16)
    - [Delphi routines[^17]](#delphi-routines17)
    - [Module Variables](#module-variables)
    - [SAC Exemptions and Approval Dates](#sac-exemptions-and-approval-dates)
    - [Data Dictionary Changes](#data-dictionary-changes)
- [Global Variables](#global-variables)
- [Software Security[^19]](#software-security19)
  - [Security Management](#security-management)
  - [Security Features](#security-features)
- [Index](#index)
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 8%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Page</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>November 2003</td>
<td><p>ACKQ*3.0*3</p>
<p>Release of the GUI interface, Audiogram Module with two components: Audiogram Edit and Audiogram Display</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>November 2005</td>
<td><p>ACKQ*3.0*12</p>
<p>Updates to QUASAR Audiogram Module</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td rowspan="3"><p>July 2007</p>
<p>July 2007</p></td>
<td><p>Combine, format, and update the QUASAR and the Audiogram Module User Manuals.</p>
<p>Historical version: Quality: Audiology and Speech Analysis Reporting (QUASAR)</p>
<p>GUI version: QUASAR Audiogram Module</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>ACKQ*3.0*13</p>
<ul>
<li><p>Removed Sections IX, X, and XI from the historical version of the user manual.</p></li>
<li><p>Configure one of three audiometric instruments, GSI61 (Grason-Stadler), Madsen-Aurical (GN Otometrics), and AC40 (Interacoustics).</p></li>
<li><p>Check and monitor the status of the audiometer connection.</p></li>
<li><p>Import audiometric data from the audiometer to the Audiogram Module, point by point or batch mode.</p></li>
<li><p>Reset values in an audiometer capable of being reset and clear any buffers or memory used in the construction or passing of information.</p></li>
<li><p>Incorporate the graph (Audiogram Display component) as a tab in the Audiogram Edit window. The graphic display is updated in real time with data from the device.</p></li>
<li><p>The following items are added or modified to display within the surrounding area of the audiogram display (graph).</p></li>
</ul>
<ol type="a">
<li><p>Air Conduction averages</p></li>
<li><p>Audiogram symbol key, No Response, Rollover Index text boxes, and SRT, IAR, and CAR grids</p></li>
</ol>
<ul>
<li><p>Desktop access to the application is removed. The Audiogram Module can be configured and accessed only through the Computerized Patient Record System (CPRS) Tools menu.</p></li>
<li><p>The algorithm for <em>points to plot on the graph</em> uses the Retest value if there is no Final value.</p></li>
<li><p>The third row label on the Pure Tones tab changed from Final or Masked to Masked.</p></li>
<li><p>The Flip Tabs option is removed from the File menu.</p></li>
<li><p>A 1500 Hz column is added to the Pure Tones tab for Bone Conduction.</p></li>
<li><p>VA form 10-2364 is modified to conform to VA standards.</p></li>
</ul></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>ACKQAG03 is modified to suppress the MailMan notification sent to the user when an AUDIOMETRIC EXAM DATA file (#509850.9) record is transmitted to the Denver ALC.</p></li>
<li><p>ACKQAG05 is modified to replace DDC with DALC in the subject of the MailMan message that confirms the deletion of an AUDIOMETRIC EXAM DATA file (#509850.9) record from the local and DALC databases.</p></li>
<li><p>Remote procedure call ACKQAUD1 is added to the ACKQROES3E option to register the call to the Graph Display tab. The following remote procedure calls are removed from the ACKQROES3E option: XUS GET USER INFO, XUS INTRO MSG, XWB CREATE CONTEXT, XWB GET VARIABLE VALUE, and XWB GET BROKER INFO.</p></li>
</ul></td>
<td><p><a href="#m-routines">21</a></p>
<p><a href="#m-routines">21</a></p>
<p><a href="#ackqaud1">27</a></p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
*This page intentionally left blank for double-sided printing.*
Table of Contents
*This page intentionally left blank for double-sided printing.*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QUASAR (Quality: Audiology and Speech Analysis and Reporting) is a VistA software package written for the Audiology and Speech Pathology Service (ASPS). QUASAR is used to enter, edit, and retrieve data for each audiometric exam of a patient and provides for the transmission of this data to various programs.

Patch ACKQ\*3.0\*13 adds the ability to retrieve data directly from certain audiometric devices, and combines the Edit and Display components into one application. Recommended users (not doing data entry or capture), can use the Graph Display tab to view a graphic display of a record.

The QUASAR Audiogram Module is a Windows-based GUI interface, developed to simplify and enhance the entry, display, and use of information obtained during an audiometric exam of a patient.

The Audiogram Edit component (ACKQROES3E.exe) is a Windows-based software application that allows clinicians to enter, edit, and view a patient's audiometric exam record and a patient's audiogram graph. You access the component from the Computerized Patient Record System (CPRS) Tools menu.

The QUASAR Audiogram Module includes components that reside on two systems: the local facility VistA system and the Denver Acquisition & Logistics Center (Denver ALC) system. The local facility components include a VistA file, 'M' routines and options, remote procedure calls, and a Delphi executable. The Denver ALC ROES\*3.0 (Remote Order Entry System) order processing application incorporates patient-specific audiometric information that is taken from data transmitted to a national database from the QUASAR Audiogram Module. The information is used by vendors to produce customized hearing related items.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Related documentation is located in the VistA Document Library:

<http://www.va.gov/vdl/>

*QUASAR Audiogram Module Release Notes* for Patch ACKQ\* 3.0\*13

*QUASAR Audiogram Module Installation and Implementation Guide* for Patch ACKQ\* 3.0\*13

*QUASAR Package User Manual* for Patch ACKQ\* 3.0\*13

## Audiogram Display through CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any doctor with access to the local system can view the Audiogram Display within the application to aid in treatment and diagnosis decisions. They can continue to view the display as assigned in patch ACKQ\*3.0\*12. For information on Audiogram Display, refer to *Technical Manual - Audiometric Exam Module*, November 2005 in the VistA Document Library.

> <http://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12tm.pdf>

## Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Users set up to use multiple broker environments default to BROKERSERVER on port 9200 in the production account.
- You must login using local VistA Access and Verify codes. If prompted, use your VistA account, local Access and Verify codes.

> Local Access and Verify codes are not needed when single sign on is enabled in the selected environment, the end user has auto login, multiple sign on is used, and a session is active in another VistA application.

- Users may also have Denver ALC (Denver Acquisition & Logistics Center) Access and Verify codes for the Denver ALC Remote Inquiry System (RIS) or Remote Order Entry System (ROES). These Denver ALC codes are not needed for the Audiogram Module itself.
- Use FileMan's DATA DICTIONARY UTILITIES option to print out the data dictionary for a file.

> From the LIST FILE ATTRIBUTES option, select a version: STANDARD, BRIEF or CONDENSED. It is recommended that you use the CONDENSED version, because of the large number of fields in a file.

- Use the VistA KIDS Build File Print option \[XPD PRINT BUILD\] for a complete listing of package components exported with this software.

> KIDS - Kernel Installation & Distribution

> Utilities

> Build File Print

- Use the VistA KIDS Install File Print option \[XPD PRINT INSTALL FILE\] to print out the results of the installation process.

> KIDS - Kernel Installation & Distribution

> Utilities

> Install File Print

- In CPRS select a patient and enter the QUASAR Audiogram Module from the CPRS Tools menu. To change a patient, exit the QUASAR Audiogram Module and in CPRS select a new patient and enter the QUASAR Audiogram Module from the CPRS Tools menu.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Site-specific Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The VistA system must have MailMan connectivity to the Denver ALC (such as DDC.VA.GOV domain open), in order to transmit the audiometric data to the Denver ALC.
- The site's VistA Server must be running the VA's RPC Broker listener.
- The desktop system must be running a Windows operating system (WinNT, Win2K, WinXP).
- The VistA RPC Broker client must be installed and functional on the desktop system.

## Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RPC Broker V1.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- You are required to install RPC Broker V1.1 on every workstation on which the Audiogram Module is to be executed.
- The RPC Broker is already installed if the workstation connects successfully by way of CPRS, BCMA, or PCMM.
- To install the RPC Broker, refer to the RPC Broker website for configuration information and to download the installation file: <span class="mark">REDACTED</span>
- The RPC Broker patches must be up-to-date in all accounts running the QUASAR Audiogram Module.

### CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS application must be installed and functional on the VistA server and desktop systems, to access the audiogram application from the CPRS Tools menu.

### KIDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS[^1] build installs (ACKQ\*3.0\*13) the following options, remote procedure calls, and routines to the VistA system into the local system.

### QUASAR Audiogram Module (Audiogram Edit) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ACKQROES3E[^2] | Audiogram Edit allows access to the QUASAR Audiogram Module and is set up in the Option file \#19. |
|----------------|----------------------------------------------------------------------------------------------------|

- You must assign ACKQROES3E to a common menu option, or as a secondary menu option for the individual users.
- If not assigned, ACKQROES3E generates an error while context is established.

### Remote Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>ACKQAUD1</th>
<th>Used in the display part of the application.<br />
An RPC that gets the audiogram data the selected entry in the AUDIOMETRIC EXAM DATA file (#509850.9) and returns the data to the calling program.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### M Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ACKQAG03 | Sends audiometric data to Denver ALC. |
|----------|---------------------------------------|
| ACKQAG05 | Utility for transmitting data.        |

### Delphi Executable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>ACKQROES3E.exe</th>
<th><p>Application for the QUASAR Audiogram Module from CPRS.</p>
<p>The executable, ACKQROES3E.exe is contained in the ACKQ3_0P13_EDIT.ZIP file.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Vendor Installer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The vendor installer[^3] places DLLs in a specific folder on the PC used for hearing tests: C:\Program Files\VistA\QUASAR\Plugins\\

After downloading the vendor files (from <span class="mark">REDACTED</span> and installing the appropriate driver, as well as installing the current QUASAR executable, QUASAR can search for and communicate with compatible devices.

### Troubleshooting QUASAR Audiogram Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the QUASAR Audiogram Module[^4] does not display your device:

1.  Ensure that the driver for the correct device is installed and that all installation instructions (included in the installer) are followed.
1.  Check that the physical connection between the PC and the device is plugged in at both ends to available and functioning ports. If any port adapters are used (e.g. USB-COM, RS232-USB, etc.), ensure the driver for the adapter is installed before installing any additional vendor software.
2.  Make sure the device is plugged in and powered on. Also make sure that any device-specific changes were made. Changes may include setting communication characteristics through the device’s menu and pressing specific buttons to enable communication. In certain cases, physical hardware changes may be necessary, such as firmware chip replacement or dip-switch changes.
3.  For vendor-specific settings, consult the documentation for the equipment you are using, which is included with the vendor installer.

*This page intentionally left blank for double-sided printing.*

# Process Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Logic[^5] section provides technical staff with the processing functions in each application. The flow chart logic is accompanied by related routines and remote procedure calls supporting that logic.

Functions performed by these processes are:

- Entry of clinical audiogram data (creation of new audiogram record or modification of existing unsigned record).
- Transmission of the audiogram record to the Denver ALC.
- Display of the audiogram and associated functions.

> **NOTE:** From CPRS, the patient DFN is passed to the application as DFN=%DFN. If the DFN is provided, the program defaults to that DFN.  
% is used when you access Audiogram Edit from the server.

## Transmission of Audiometric Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This flow chart[^6] is a representation of the import of data from an audiometer to the module.

![](quasar-version-3-technical-pkg-security-updated-ackq-3-13/002.png)

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Files section lists the specific data elements and their attributes, in the Audiometric Exam Data file.

A number of audiology-specific acronyms and abbreviations are used in the field names. Refer to the [*Glossary*](#_Glossary) for full definitions.

## Audiometric Exam Data: ^ACK(509850.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a complete listing of fields and attributes use the FileMan: List File Attributes option, selecting the STANDARD or BRIEF format.

The CONDENSED listing[^7] follows:

Field Field Name \[node;position\]

.01 DATE/TIME OF VISIT (RD), \[0;1\]

.02 PATIENT (P2'), \[0;2\]

.03 EXAMINING AUDIOLOGIST (P200'), \[0;3\]

.04 REFERRAL SOURCE (P44'), \[0;4\]

.05 AGE AT VISIT (NJ3,0), \[0;5\]

.06 \* VA ELIGIBILITY STATUS (S), \[0;6\]

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

1.06 LEFT TWO FREQUENCY PTA (NJ3,0), \[1;6\]

1.07 RIGHT MCL (NJ3,0), \[1;7\]

1.08 RIGHT UCL (NJ3,0), \[1;8\]

1.09 LEFT MCL (NJ3,0), \[1;9\]

1.1 LEFT UCL (NJ3,0), \[1;10\]

Field Field Name \[node;position\]

1.11 R TYMPANOGRAM TYPE (S),\[1;11\]

1.12 L TYMPANOGRAM TYPE (S),\[1;12\]

10.01 INITIAL A/C THRESHOLD R 125 (F), \[10;1\]

10.02 INITIAL A/C THRESHOLD R 250 (F), \[10;2\]

10.03 INITIAL A/C THRESHOLD R 500 (F), \[10;3\]

10.04 INITIAL A/C THRESHOLD R 750 (F), \[10;4\]

10.05 INITIAL A/C THRESHOLD R 1000 (F), \[10;5\]

10.06 INITIAL A/C THRESHOLD R 1500 (F), \[10;6\]

10.07 INITIAL A/C THRESHOLD R 2000 (F), \[10;7\]

10.08 INITIAL A/C THRESHOLD R 3000 (F), \[10;8\]

10.09 INITIAL A/C THRESHOLD R 4000 (F), \[10;9\]

10.1 INITIAL A/C THRESHOLD R 6000 (F), \[10;10\]

10.11 INITIAL A/C THRESHOLD R 8000 (F), \[10;11\]

10.12 INITIAL A/C THRESHOLD R 12000 (F), \[10;12\]

11.01 \* INITIAL A/C THRESH TAG R 125 (S), \[11;1\]

11.02 \* INITIAL A/C THRESH TAG R 250 (S), \[11;2\]

11.03 \* INITIAL A/C THRESH TAG R 500 (S), \[11;3\]

11.04 \* INITIAL A/C THRESH TAG R 750 (S), \[11;4\]

11.05 \* INITIAL A/C THRESH TAG R 1000 (S), \[11;5\]

11.06 \* INITIAL A/C THRESH TAG R 1500 (S), \[11;6\]

11.07 \* INITIAL A/C THRESH TAG R 2000 (S), \[11;7\]

11.08 \* INITIAL A/C THRESH TAG R 3000 (S), \[11;8\]

11.09 \* INITIAL A/C THRESH TAG R 4000 (S), \[11;9\]

11.1 \* INITIAL A/C THRESH TAG R 6000 (S), \[11;10\]

11.11 \* INITIAL A/C THRESH TAG R 8000 (S), \[11;11\]

11.12 \* INITIAL A/C THRESH TAG R 12000 (S), \[11;12\]

15.01 RETEST A/C THRESHOLD R 125 (F), \[10;1\]

15.02 RETEST A/C THRESHOLD R 250 (F), \[10;2\]

15.03 RETEST A/C THRESHOLD R 500 (F), \[10;3\]

15.04 RETEST A/C THRESHOLD R 750 (F), \[10;4\]

15.05 RETEST A/C THRESHOLD R 1000 (F), \[10;5\]

15.06 RETEST A/C THRESHOLD R 1500 (F), \[10;6\] zxc

15.07 RETEST A/C THRESHOLD R 2000 (F), \[10;7\]

15.08 RETEST A/C THRESHOLD R 3000 (F), \[10;8\]

15.09 RETEST A/C THRESHOLD R 4000 (F), \[10;9\]

15.1 RETEST A/C THRESHOLD R 6000 (F), \[10;10\]

15.11 RETEST A/C THRESHOLD R 8000 (F), \[10;11\]

20.01 FINAL A/C THRESHOLD R 125 (F), \[20;1\]

20.02 FINAL A/C THRESHOLD R 250 (F), \[20;2\]

20.03 FINAL A/C THRESHOLD R 500 (F), \[20;3\]

20.04 FINAL A/C THRESHOLD R 750 (F), \[20;4\]

Field Field Name \[node;position\]

20.05 FINAL A/C THRESHOLD R 1000 (F), \[20;5\]

20.06 FINAL A/C THRESHOLD R 1500 (F), \[20;6\]

20.07 FINAL A/C THRESHOLD R 2000 (F), \[20;7\]

20.08 FINAL A/C THRESHOLD R 3000 (F), \[20;8\]

20.09 FINAL A/C THRESHOLD R 4000 (F), \[20;9\]

20.1 FINAL A/C THRESHOLD R 6000 (F), \[20;10\]

20.11 FINAL A/C THRESHOLD R 8000 (F), \[20;11\]

20.12 FINAL A/C THRESHOLD R 12000 (F), \[20;12\]

21.01 \* REPEAT A/C THRESH TAG R 125 (S), \[21;1\]

21.02 \* REPEAT A/C THRESH TAG R 250 (S), \[21;2\]

21.03 \* REPEAT A/C THRESH TAG R 500 (S), \[21;3\]

21.04 \* REPEAT A/C THRESH TAG R 750 (S), \[21;4\]

21.05 \* REPEAT A/C THRESH TAG R 1000 (S), \[21;5\]

21.06 \* REPEAT A/C THRESH TAG R 1500 (S), \[21;6\]

21.07 \* REPEAT A/C THRESH TAG R 2000 (S), \[21;7\]

21.08 \* REPEAT A/C THRESH TAG R 3000 (S), \[21;8\]

21.09 \* REPEAT A/C THRESH TAG R 4000 (S), \[21;9\]

21.1 \* REPEAT A/C THRESH TAG R 6000 (S), \[21;10\]

21.11 \* REPEAT A/C THRESH TAG R 8000 (S), \[21;11\]

21.12 \* REPEAT A/C THRESH TAG R 12000 (S), \[21;12\]

30.01 INITIAL A/C THRESHOLD L 125 (F), \[30;1\]

30.02 INITIAL A/C THRESHOLD L 250 (F), \[30;2\]

30.03 INITIAL A/C THRESHOLD L 500 (F), \[30;3\]

30.04 INITIAL A/C THRESHOLD L 750 (F), \[30;4\]

30.05 INITIAL A/C THRESHOLD L 1000 (F), \[30;5\]

30.06 INITIAL A/C THRESHOLD L 1500 (F), \[30;6\]

30.07 INITIAL A/C THRESHOLD L 2000 (F, \[30;7\]

30.08 INITIAL A/C THRESHOLD L 3000 (F), \[30;8\]

30.09 INITIAL A/C THRESHOLD L 4000 (F), \[30;9\]

30.1 INITIAL A/C THRESHOLD L 6000 (F), \[30;10\]

30.11 INITIAL A/C THRESHOLD L 8000 (F), \[30;11\]

30.12 INITIAL A/C THRESHOLD L 12000 (F), \[30;12\]

31.01 \* INITIAL A/C THRESH TAG L 125 (S), \[31;1\]

31.02 \* INITIAL A/C THRESH TAG L 250 (S), \[31;2\]

31.03 \* INITIAL A/C THRESH TAG L 500 (S), \[31;3\]

31.04 \* INITIAL A/C THRESH TAG L 750 (S), \[31;4\]

31.05 \* INITIAL A/C THRESH TAG L 1000 (S), \[31;5\]

31.06 \* INITIAL A/C THRESH TAG L 1500 (S), \[31;6\]

31.07 \* INITIAL A/C THRESH TAG L 2000 (S), \[31;7\]

31.08 \* INITIAL A/C THRESH TAG L 3000 (S), \[31;8\]

31.09 \* INITIAL A/C THRESH TAG L 4000 (S), \[31;9\]

Field Field Name \[node;position\]

31.1 \* INITIAL A/C THRESH TAG L 6000 (S), \[31;10\]

31.11 \* INITIAL A/C THRESH TAG L 8000 (S), \[31;11\]

31.12 \* INITIAL A/C THRESH TAG L 12000 (S), \[31;12\]

35.01 RETEST A/C THRESHOLD R 125 (F), \[10;1\]

35.02 RETEST A/C THRESHOLD R 250 (F), \[10;2\]

35.03 RETEST A/C THRESHOLD R 500 (F), \[10;3\]

35.04 RETEST TEST A/C THRESHOLD R 750 (F), \[10;4\]

35.05 RETEST A/C THRESHOLD R 1000 (F), \[10;5\]

35.06 RETEST A/C THRESHOLD R 1500 (F), \[10;6\]

35.07 RETEST A/C THRESHOLD R 2000 (F), \[10;7\]

35.08 RETEST A/C THRESHOLD R 3000 (F), \[10;8\]

35.09 RETEST A/C THRESHOLD R 4000 (F), \[10;9\]

35.1 RETEST A/C THRESHOLD R 6000 (F), \[10;10\]

35.11 RETEST A/C THRESHOLD R 8000 (F), \[10;11\]

40.01 FINAL A/C THRESHOLD L 125 (F), \[40;1\]

40.02 FINAL A/C THRESHOLD L 250 (F), \[40;2\]

40.03 FINAL A/C THRESHOLD L 500 (F), \[40;3\]

40.04 FINAL A/C THRESHOLD L 750 (F), \[40;4\]

40.05 FINAL A/C THRESHOLD L 1000 (F), \[40;5\]

40.06 FINAL A/C THRESHOLD L 1500 (F), \[40;6\]

40.07 FINAL A/C THRESHOLD L 2000 (F), \[40;7\]

40.08 FINAL A/C THRESHOLD L 3000 (F), \[40;8\]

40.09 FINAL A/C THRESHOLD L 4000 (F), \[40;9\]

40.1 FINAL A/C THRESHOLD L 6000 (F), \[40;10\]

40.11 FINAL A/C THRESHOLD L 8000 (F), \[40;11\]

40.12 FINAL A/C THRESHOLD L 12000 (F), \[40;12\]

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

Field Field Name \[node;position\]

50.04 \* INITIAL A/C MASK LEVEL R 750 (NJ3,0), \[50;4\]

50.05 \* INITIAL A/C MASK LEVEL R 1000 (NJ3,0), \[50;5\]

50.06 \* INITIAL A/C MASK LEVEL R 1500 (NJ3,0), \[50;6\]

50.07 \* INITIAL A/C MASK LEVEL R 2000 (NJ3,0), \[50;7\]

50.08 \* INITIAL A/C MASK LEVEL R 3000 (NJ3,0), \[50;8\]

50.09 \* INITIAL A/C MASK LEVEL R 4000 (NJ3,0), \[50;9\]

50.1 \* INITIAL A/C MASK LEVEL R 6000 (NJ3,0), \[50;10\]

50.11 \* INITIAL A/C MASK LEVEL R 8000 (NJ3,0), \[50;11\]

50.12 \* INITIAL A/C MASK LEVEL R 12000 (NJ3,0), \[50;12\]

51.01 FINAL A/C MASK LEVEL R 125 (F), \[51;1\]

51.02 FINAL A/C MASK LEVEL R 250 (F), \[51;2\]

51.03 FINAL A/C MASK LEVEL R 500 (F), \[51;3\]

51.04 FINAL A/C MASK LEVEL R 750 (F), \[51;4\]

51.05 FINAL A/C MASK LEVEL R 1000 (F), \[51;5\]

51.06 FINAL A/C MASK LEVEL R 1500 (F), \[51;6\]

51.07 FINAL A/C MASK LEVEL R 2000 (F), \[51;7\]

51.08 FINAL A/C MASK LEVEL R 3000 (F), \[51;8\]

51.09 FINAL A/C MASK LEVEL R 4000 (F), \[51;9\]

51.1 FINAL A/C MASK LEVEL R 6000 (F), \[51;10\]

51.11 FINAL A/C MASK LEVEL R 8000 (F), \[51;11\]

51.12 FINAL A/C MASK LEVEL R 12000 (F), \[51;12\]

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

60.12 \* INITIAL A/C MASK LEVEL L 12000 (NJ3,0), \[60;12\]

61.01 FINAL A/C MASK LEVEL L 125 (F), \[61;1\]

61.02 FINAL A/C MASK LEVEL L 250 (F), \[61;2\]

61.03 FINAL A/C MASK LEVEL L 500 (F), \[61;3\]

61.04 FINAL A/C MASK LEVEL L 750 (F), \[61;4\]

61.05 FINAL A/C MASK LEVEL L 1000 (F), \[61;5\]

61.06 FINAL A/C MASK LEVEL L 1500 (F), \[61;6\]

61.07 FINAL A/C MASK LEVEL L 2000 (F), \[61;7\]

61.08 FINAL A/C MASK LEVEL L 3000 (F), \[61;8\]

Field Field Name \[node;position\]

61.09 FINAL A/C MASK LEVEL L 4000 (F), \[61;9\]

61.1 FINAL A/C MASK LEVEL L 6000 (F), \[61;10\]

61.11 FINAL A/C MASK LEVEL L 8000 (F), \[61;11\]

61.12 FINAL A/C MASK LEVEL L 12000 (F), \[61;12\]

70.01 INITIAL B/C THRESHOLD R 250 (F), \[70;1\]

70.02 INITIAL B/C THRESHOLD R 500 (F), \[70;2\]

70.03 INITIAL B/C THRESHOLD R 750 (F), \[70;3\]

70.04 INITIAL B/C THRESHOLD R 1000 (F), \[70;4\]

70.05 INITIAL B/C THRESHOLD R 1500 (F), \[70;5\]

70.06 INITIAL B/C THRESHOLD R 2000 (F), \[70;6\]

70.07 INITIAL B/C THRESHOLD R 3000 (F), \[70;7\]

70.08 INITIAL B/C THRESHOLD R 4000 (F), \[70;8\]

70.09 INITIAL B/C THRESHOLD R 6000 (F), \[70;9\]

71.01 \* INITIAL B/C THRESH TAG R 250 (S), \[71;1\]

71.02 \* INITIAL B/C THRESH TAG R 500 (S), \[71;2\]

71.03 \* INITIAL B/C THRESH TAG R 750 (S), \[71;3\]

71.04 \* INITIAL B/C THRESH TAG R 1000 (S), \[71;4\]

71.05 \* INITIAL B/C THRESH TAG R 1500 (S), \[71;5\]

71.06 \* INITIAL B/C THRESH TAG R 2000 (S), \[71;6\]

71.07 \* INITIAL B/C THRESH TAG R 3000 (S), \[71;7\]

71.08 \* INITIAL B/C THRESH TAG R 4000 (S), \[71;8\]

71.09 \* INITIAL B/C THRESH TAG R 6000 (S), \[71;9\]

72.01 RETEST B/C THRESHOLD R 250 (F), \[75;1\]

72.02 RETEST B/C THRESHOLD R 500 (F), \[75;2\]

72.03 RETEST B/C THRESHOLD R 750 (F), \[75;3\]

72.04 RETEST B/C THRESHOLD R 1000 (F), \[75;4\]

72.05 RETEST B/C THRESHOLD R 1500 (F), \[75;5\]

72.06 RETEST B/C THRESHOLD R 2000 (F), \[75;6\]

72.07 RETEST B/C THRESHOLD R 3000 (F), \[75;7\]

72.08 RETEST B/C THRESHOLD R 4000 (F), \[75;8\]

72.09 RETEST B/C THRESHOLD R 6000 (F), \[75;9\]

75.01 FINAL B/C THRESHOLD R 250 (F), \[75;1\]

75.02 FINAL B/C THRESHOLD R 500 (F), \[75;2\]

75.03 FINAL B/C THRESHOLD R 750 (F), \[75;3\]

75.04 FINAL B/C THRESHOLD R 1000 (F), \[75;4\]

75.05 FINAL B/C THRESHOLD R 1500 (F), \[75;5\]

75.06 FINAL B/C THRESHOLD R 2000 (F), \[75;6\]

75.07 FINAL B/C THRESHOLD R 3000 (F), \[75;7\]

75.08 FINAL B/C THRESHOLD R 4000 (F), \[75;8\]

75.09 FINAL B/C THRESHOLD R 6000 (F), \[75;9\]

76.01 \* REPEAT B/C THRESH TAG R 250 (S), \[76;1\]

Field Field Name \[node;position\]

76.02 \* REPEAT B/C THRESH TAG R 500 (S), \[76;2\]

76.03 \* REPEAT B/C THRESH TAG R 750 (S), \[76;3\]

76.04 \* REPEAT B/C THRESH TAG R 1000 (S), \[76;4\]

76.05 \* REPEAT B/C THRESH TAG R 1500 (S), \[76;5\]

76.06 \* REPEAT B/C THRESH TAG R 2000 (S), \[76;6\]

76.07 \* REPEAT B/C THRESH TAG R 3000 (S), \[76;7\]

76.08 \* REPEAT B/C THRESH TAG R 4000 (S), \[76;8\]

76.09 \* REPEAT B/C THRESH TAG R 6000 (S), \[76;9\]

80.01 INITIAL B/C THRESHOLD L 250 (F), \[80;1\]

80.02 INITIAL B/C THRESHOLD L 500 (F), \[80;2\]

80.03 INITIAL B/C THRESHOLD L 750 (F), \[80;3\]

80.04 INITIAL B/C THRESHOLD L 1000 (F), \[80;4\]

80.05 INITIAL B/C THRESHOLD L 1500 (F), \[80;5\]

80.06 INITIAL B/C THRESHOLD L 2000 (F), \[80;6\]

80.07 INITIAL B/C THRESHOLD L 3000 (F), \[80;7\]

80.08 INITIAL B/C THRESHOLD L 4000 (F), \[80;8\]

80.09 INITIAL B/C THRESHOLD L 6000 (F), \[80;9\]

81.01 \* INITIAL B/C THRESH TAG L 250 (S), \[81;1\]

81.02 \* INITIAL B/C THRESH TAG L 500 (S), \[81;2\]

81.03 \* INITIAL B/C THRESH TAG L 750 (S), \[81;3\]

81.04 \* INITIAL B/C THRESH TAG L 1000 (S), \[81;4\]

81.05 \* INITIAL B/C THRESH TAG L 1500 (S), \[81;5\]

81.06 \* INITIAL B/C THRESH TAG L 2000 (S), \[81;6\]

81.07 \* INITIAL B/C THRESH TAG L 3000 (S), \[81;7\]

81.08 \* INITIAL B/C THRESH TAG L 4000 (S), \[81;8\]

81.09 \* INITIAL B/C THRESH TAG L 6000 (S), \[81;9\]

82.01 RETEST B/C THRESHOLD L 250 (F), \[82;1\]

82.02 RETEST B/C THRESHOLD L 500 (F), \[82;2\]

82.03 RETEST B/C THRESHOLD L 750 (F), \[82;3\]

82.04 RETEST B/C THRESHOLD L 1000 (F), \[82;4\]

82.05 RETEST B/C THRESHOLD L 1500 (F), \[82;5\]

82.06 RETEST B/C THRESHOLD L 2000 (F), \[82;6\]

82.07 RETEST B/C THRESHOLD L 3000 (F), \[82;7\]

82.08 RETEST B/C THRESHOLD L 4000 (F), \[82;8\]

82.09 RETEST B/C THRESHOLD L 6000 (F), \[82;9\]

85.01 FINAL B/C THRESHOLD L 250 (F), \[85;1\]

85.02 FINAL B/C THRESHOLD L 500 (F), \[85;2\]

85.03 FINAL B/C THRESHOLD L 750 (F), \[85;3\]

85.04 FINAL B/C THRESHOLD L 1000 (F), \[85;4\]

85.05 FINAL B/C THRESHOLD L 1500 (F), \[85;5\]

85.06 FINAL B/C THRESHOLD L 2000 (F), \[85;6\]

Field Field Name \[node;position\]

85.07 FINAL B/C THRESHOLD L 3000 (F), \[85;7\]

85.08 FINAL B/C THRESHOLD L 4000 (F), \[85;8\]

85.09 FINAL B/C THRESHOLD L 6000 (F), \[85;9\]

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

91.01 FINAL B/C MASK LEVEL R 250 (F), \[91;1\]

91.02 FINAL B/C MASK LEVEL R 500 (F), \[91;2\]

91.03 FINAL B/C MASK LEVEL R 750 (F), \[91;3\]

91.04 FINAL B/C MASK LEVEL R 1000 (F), \[91;4\]

91.05 FINAL B/C MASK LEVEL R 1500 (F), \[91;5\]

91.06 FINAL B/C MASK LEVEL R 2000 (F), \[91;6\]

91.07 FINAL B/C MASK LEVEL R 3000 (F), \[91;7\]

91.08 FINAL B/C MASK LEVEL R 4000 (F), \[91;8\]

91.09 FINAL B/C MASK LEVEL R 6000 (F), \[91;9\]

100.01 \* INITIAL B/C MASK LEVEL L 250 (NJ3,0), \[100;1\]

100.02 \* INITIAL B/C MASK LEVEL L 500 (NJ3,0), \[100;2\]

100.03 \* INITIAL B/C MASK LEVEL L 750 (NJ3,0), \[100;3\]

100.04 \* INITIAL B/C MASK LEVEL L 1000 (NJ3,0), \[100;4\]

100.05 \* INITIAL B/C MASK LEVEL L 1500 (NJ3,0), \[100;5\]

100.06 \* INITIAL B/C MASK LEVEL L 2000 (NJ3,0), \[100;6\]

100.07 \* INITIAL B/C MASK LEVEL L 3000 (NJ3,0), \[100;7\]

100.08 \* INITIAL B/C MASK LEVEL L 4000 (NJ3,0), \[100;8\]

100.09 \* INITIAL B/C MASK LEVEL L 6000 (NJ3,0), \[100;9\]

101.01 FINAL B/C MASK LEVEL L 250 (F), \[101;1\]

101.02 FINAL B/C MASK LEVEL L 500 (F), \[101;2\]

Field Field Name \[node;position

101.03 FINAL B/C MASK LEVEL L 750 (F), \[101;3\]

101.04 FINAL B/C MASK LEVEL L 1000 (F), \[101;4\]

101.05 FINAL B/C MASK LEVEL L 1500 (F), \[101;5\]

101.06 FINAL B/C MASK LEVEL L 2000 (F), \[101;6\]

101.07 FINAL B/C MASK LEVEL L 3000 (F), \[101;7\]

101.08 FINAL B/C MASK LEVEL L 4000 (F), \[101;8\]

101.09 FINAL B/C MASK LEVEL L 6000 (F), \[101;9\]

110.03 MATERIAL-1 (S), \[110;3\]

110.04 PERCENT CORRECT R-1 (F), \[110;4\]

110.05 PRESENTATION METHOD R-1 (S), \[110;5\]

110.06 PRESENTATION LEVEL R-1 (NJ3,0), \[110;6\]

110.07 MASKING LEVEL R-1 (F), \[110;7\]

110.08 \* WORD LIST R-2 (S), \[110;8\]

110.09 PERCENT CORRECT R-2 (F), \[110;9\]

110.1 \* PRESENTATION METHOD R-2 (S), \[110;10\]

110.11 PRESENTATION LEVEL R-2 (NJ3,0), \[110;11\]

110.12 MASKING LEVEL R-2 (F), \[110;12\]

110.13 \* WORD LIST R-3 (S), \[110;13\]

110.14 PERCENT CORRECT R-3 (F), \[110;14\]

110.15 \* PRESENTATION METHOD R-3 (S), \[110;15\]

110.16 PRESENTATION LEVEL R-3 (NJ3,0), \[110;16\]

110.17 MASKING LEVEL R-3 (F), \[110;17\]

110.18 \* WORD LIST R-4 (S), \[110;18\]

110.19 PERCENT CORRECT R-4 (F), \[110;19\]

110.2 \* PRESENTATION METHOD R-4 (S), \[110;20\]

110.21 PRESENTATION LEVEL R-4 (NJ3,0), \[110;21\]

110.22 MASKING LEVEL R-4 (F), \[110;22\]

110.23 \* WORD LIST R-5 (S), \[110;23\]

110.24 PERCENT CORRECT R-5 (F), \[110;24\]

110.25 \* PRESENTATION METHOD R-5 (S), \[110;25\]

110.26 PRESENTATION LEVEL R-5 (NJ3,0), \[110;26\]

110.27 MASKING LEVEL R-5 (NJ3,0), \[F\]

110.28 LIST R-1 (F),\[110;28\]

110.29 LIST R-2 (F),\[110;29\]

110.3 LIST R-3 (F),\[110;30\]

110.31 LIST R-4 (F),\[110;31\]

110.32 LIST R-5 (F),\[110;32\]

111.03 MATERIAL L-1 (S), \[111;3\]

111.04 PERCENT CORRECT L-1 (F), \[111;4\]

111.05 PRESENTATION METHOD L-1 (S), \[111;5\]

111.06 PRESENTATION LEVEL L-1 (NJ3,0), \[111;6\]

Field Field Name \[node;position\]

111.07 MASKING LEVEL L-1 (F), \[111;7\]

111.08 \* WORD LIST L-2 (S), \[111;8\]

111.09 PERCENT CORRECT L-2 (F), \[111;9\]

111.1 \* PRESENTATION METHOD L-2 (S), \[111;10\]

111.11 PRESENTATION LEVEL L-2 (NJ3,0), \[111;11\]

111.12 MASKING LEVEL L-2 (F), \[111;12\]

111.13 \* WORD LIST L-3 (S), \[111;13\]

111.14 PERCENT CORRECT L-3 (F), \[111;14\]

111.15 \* PRESENTATION METHOD L-3 (S), \[111;15\]

111.16 PRESENTATION LEVEL L-3 (NJ3,0), \[111;16\]

111.17 MASKING LEVEL L-3 (F), \[111;17\]

111.18 \* WORD LIST L-4 (S), \[111;18\]

111.19 PERCENT CORRECT L-4 (F), \[111;19\]

111.2 \* PRESENTATION METHOD L-4 (S), \[111;20\]

111.21 PRESENTATION LEVEL L-4 (NJ3,0), \[111;21\]

111.22 MASKING LEVEL L-4 (F), \[111;22\]

111.23 \* WORD LIST L-5 (S), \[111;23\]

111.24 PERCENT CORRECT L-5 (F), \[111;24\]

111.25 \* PRESENTATION METHOD L-5 (S), \[111;25\]

111.26 PRESENTATION LEVEL L-5 (NJ3,0), \[111;26\]

111.27 MASKING LEVEL L-5 (F), \[111;27\]

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

115.01 INITIAL SRT THRESH R (F), \[115;1\]

115.02 REPEAT SRT THRESH R (F), \[115;2\]

115.03 INITIAL SRT MASK LEVEL R (F), \[115;3\]

Field Field Name \[node;position\]

115.04 FINAL SRT MASK LEVEL R (F), \[115;4\]

115.05 INITIAL SRT THRESH L (F), \[115;5\]

115.06 REPEAT SRT THRESH L (F), \[115;6\]

115.07 INITIAL SRT MASK LEVEL L (F), \[115;7\]

115.08 FINAL SRT MASK LEVEL L (F), \[115;8\]

115.09 PBMAX R (NJ3,0), \[115;9\]

115.1 PBMIN R (NJ3,0), \[115;10\]

115.11 PI/PB R (NJ4,2), \[115;11\]

115.12 PBMAX L (NJ3,0), \[115;12\]

115.13 PBMIN L (NJ3,0), \[115;13\]

115.14 PI/PB L (NJ4,2), \[115;14\]

115.15 \*FINAL SRT TAG R (S), \[115;15\]

115.16 \*FINAL SRT TAG L (S), \[115;16\]

115.17 \*INITIAL SRT TAG R (S), \[115;17\]

115.18 \*INITIAL SRT TAG L (S), \[115;18\]

115.19 APPLIED MAX R (NJ1,0), \[115;19\]

115.2 APPLIED MAX L (NJ1,0), \[115;20\]

120.01 MIDDLE EAR PRESSURE R (F), \[120;1\]

120.02 PK IMMITTANCE 226 R (NJ5,2), \[120;2\]

120.03 VEQ - EQUIV EAR CANAL VOL R (NJ5,2), \[120;3\]

120.04 IAR THRESHOLD R 500 (F), \[120;4\]

120.05 IAR THRESHOLD R 1000 (F), \[120;5\]

120.06 IAR THRESHOLD R 2000 (F), \[120;6\]

120.07 IAR THRESHOLD R 4000 (F), \[120;7\]

120.08 CAR THRESHOLD R 500 (F), \[120;8\]

120.09 CAR THRESHOLD R 1000 (F), \[120;9\]

120.1 CAR THRESHOLD R 2000 (F), \[120;10\]

120.11 CAR THRESHOLD R 4000 (F), \[120;11\]

120.12 ACOUSTIC REFLEX DECAY R 500 (S), \[120;12\]

120.13 ACOUSTIC REFLEX DECAY R 1000 (S), \[120;13\]

120.14 AR HALF LIFE 500 R (F), \[120;14\]

120.15 AR HALF LIFE 1000 R (F), \[120;15\]

120.16 INTER-TEST CONSISTENCY R (S), \[120;16\]

120.17 IAR BBN R (F),\[120;17\]

120.18 CAR BBN R (F), (F),\[120;18\]

120.19 PK IMMITTANCE 678 R(NJ5,2),\[120;19\]

120.2 WEBER R(F),\[120;20\]

120.21 PT STENGER R(F),\[120;21\]

120.22 RINNE R(F),\[120;22\]

120.23 OTHER TEST R(F),\[120;23\]

121.01 MIDDLE EAR PRESSURE L (F), \[121;1\]

Field Field Name \[node;position\]

121.02 PK IMMITTANCE 226 L (NJ5,2), \[121;2\]

121.03 VEQ - EQUIV EAR CANAL VOL L (NJ5,2), \[121;3\]

121.04 IAR THRESHOLD L 500 (F), \[121;4\]

121.05 IAR THRESHOLD L 1000 (F), \[121;5\]

121.06 IAR THRESHOLD L 2000 (F), \[121;6\]

121.07 IAR THRESHOLD L 4000 (F), \[121;7\]

121.08 CAR THRESHOLD L 500 (F), \[121;8\]

121.09 CAR THRESHOLD L 1000 (F), \[121;9\]

121.1 CAR THRESHOLD L 2000 (F), \[121;10\]

121.11 CAR THRESHOLD L 4000 (F), \[121;11\]

121.12 ACOUSTIC REFLEX DECAY L 500 (S), \[121;12\]

121.13 ACOUSTIC REFLEX DECAY L 1000 (S), \[121;13\]

121.14 AR HALF LIFE 500 L (F), \[121;14\]

121.15 AR HALF LIFE 1000 L (F), \[121;15\]

121.16 INTER-TEST CONSISTENCY L (S), \[121;16\]

121.17 IAR BBN L (F),\[121;17\]

121.18 CAR BBN L (F),\[121;18\]

121.19 PK IMMITTANCE 678 L (NJ5,2),\[121;19\]

121.2 WEBER L (F) ,\[121;20\]

121.21 PT STENGER L (F) ,\[121;21\]

121.22 RINNE L (F),\[121;22\]

121.23 OTHER TEST L (F),\[121;23\]

122 COMMENTS (W), \[122;0\]

> **NOTE:** 791000 node is created, but is only used at the Denver ALC.

### Files Referenced in ^ACK(509850.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ^DPT( PATIENT
- ^VA(200 NEW PERSON
- ^SC( HOSPITAL LOCATION
- ^XMB(3.9, MESSAGE
- ^DIC(4, INSTITUTION

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## M Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M routines[^8] section provides technical staff with a reference list of routines included in the ACKQ\*3.0\*13 Audiogram Module.

- ACKQAG03  
  *Called by RPC:* ACKQROES  
  *Purpose:* Retrieves and prepares audiometric exam data for transmission to the Denver ALC.
- .ACKQAG05  
  *Called by routine:* ACKQAG03 *and RPC:* ACKQROESD and ACKQAUD4  
  *Purpose:* Utilities for transmitting data to the Denver ALC.

## Delphi Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delphi routines[^9] of the Audiogram Edit are file types: .dpr, .pas, and .dfm.

| File              | Description                                |
|-----------------------|------------------------------------------------|
| ACKQROES3E.dpr        | Project file                                   |
| uEnterEdit.pas        | Main driver program module                     |
| uDevice.pas       | Select and configure audiometric device to use |
| uAgmLKUP.pas      | Look up prior audiograms                       |
| uEditUtils.pas        | Utilities for uEnterEdit                       |
| uEditUtil2.pas        | Additional utilities for uEnterEdit            |
| uEditUtil3.pas    |                                                |
| uInactivate.pas       | NotEdit utility to disable all controls        |
| uHelp1.pas            | Help for Audiogram Entry page                  |
| uHelp2.pas            | Help for Pure Tones page                       |
| uHelp3.pas            | Help for Speech Audiometry page                |
| uHelp4.pas            | Help for Acoustic Immittance page              |
| uHelp5.pas        | Help for Graph Display page                    |
| uTable.pas        | Display VA form 10-2364                        |
| uGraphUtil.pas    | Utility for graphic display page               |
| uGraphUtil2.pas   | Utility for graphic display page               |
| uMask.pas         | Utility for graphic display page               |
| uInitRead.pas     |                                                |
| frmVistAAbout.pas | VistA About form code                          |
| Splvista.pas      | VistA splash screen code                       |
| uEnterEdit.dfm        | Main form                                      |
| uAgmLKUP.dfm      | Form to list available audiograms - Find       |
| uDevice.dfm       | Form to list available audiometric devices     |
| uHelp1.dfm            | Help Form for the entry page                   |
| uHelp2.dfm            | Help Form for Pure Tones page                  |
| uHelp3.dfm            | Help Form for Speech Audiometry page           |
| uHelp4.dfm            | Help Form for Acoustic Immittance page         |
| uHelp5.dfm            | Help Form for graphic display page             |
| frmVistAAbout.dfm | VistA About form                               |
| Splvista.dfm      | VistA splash screen                            |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Exported Options[^10] section describes the VistA Broker option included in the Audiogram Module.

## ACKQROES3E - Audiogram Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: ACKQROES3E[^11]

MENU TEXT: Audiogram Enter Edit

TYPE: Broker (Client/Server)

PACKAGE: QUASAR

DESCRIPTION: This is the menu item to establish the connection for the AUDIOMETRIC EXAM DATA file Audiogram Edit executable.

RPC: ACKQAUD1

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ^ACK(509850.9,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the data stored in this file is part of the patient record, it should be retained as permanent data in accordance with the VistA patient data storage policy and regulations.

*This page intentionally left blank for double-sided printing.*

# APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains the called routines, entry points, and API's[^12] of ACKQROES3E.

## START^ACKQAG03

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Called by RPC: ACKQROES.

> Sets up and sends the message to the Denver ALC with the audiometric data.

> The message number and date sent is placed back into the Audiometric Exam DATA file for tracing purposes.

## ACKEXIST^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Checks for existence of file 509805.9 at the site.

## DFNIN^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input the DFN of a patient.

> Returns the last entry number in file 509850.9 for a patient.

## NEWMSG^ACKQAG05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Returns the message number as set up in ^XMB(3.9.

*This page intentionally left blank for double-sided printing.*

# RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following remote procedure call[^13] is in ACKQROES3E.

### ACKQAUD1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TAG: START

> ROUTINE: ACKQAG01

> RETURN VALUE TYPE: ARRAY

> AVAILABILITY: PUBLIC

> WORD WRAP ON: FALSE

> DESCRIPTION: This RPC gets the audiogram data for entries in the Audiometric Exam Data file 509850.9 and returns it to the calling program in the array.

*This page intentionally left blank for double-sided printing.*

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CPRS Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Module cannot be run as a standalone product on a VistA system.

- Facilities are required to use CPRS functionality[^14] for the Audiogram Module.
- Other files are referenced: the PATIENT (#2) file, the NEW PERSON (#200) file, the INSTITUTION (#4) file, the HOSPITAL LOCATION (#44) file, and the title of the examining clinician from the TITLE (3.1) file.
- The Audiogram Module delivers audiometric exam records electronically to the Denver ALC.
- Audiometric data is integrated into custom hearing aid orders placed through the Remote Order Entry System (ROES).
- ROES provides hearing aid manufacturers more complete information for the manufacture, modification, and repair of hearing aids.
- Any doctor with access to the local system can view the Audiogram Display within the application to aid in treatment and diagnosis decisions. They may also continue to view the display as assigned in patch ACKQ\*3.0\*12. For information on Audiogram Display, refer to *Audiometric Exam Module Installation Guide*, November 2005 in the VistA Document Library.

> [www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal\_(QUASAR)/ackq3_0_p12ig.pdf](http://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12ig.pdf)

## Recommended Desktop Minimums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A system with the following specifications can provide the functionality necessary for this application.

|                   |                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------|
| Specification | Recommended Minimum                                                                   |
| Processor         | 200 MHz                                                                                   |
| Memory            | 64 MB                                                                                     |
| Hard Drive        | 4GB                                                                                       |
| Video             | AGP 2x w/4MB                                                                              |
| CD-ROM            | 8x                                                                                        |
| Monitor           | 17" VGA, .28 pixel resolution                                                             |
| LAN Interface     | 10/100 Mbps Ethernet                                                                      |
| Keyboard          | 101-key                                                                                   |
| Mouse             | Microsoft Compatible                                                                      |
| Operating System  | Microsoft Windows 9x, 2000 or XP (MS Windows XP or Windows 2000 Pro strongly recommended) |
| Browser           | IE 5                                                                                      |

- The VA Assistant Secretary for Information and Technology established a set of minimum configurations for new procurement of desktop systems across the enterprise (VA Directive 6401).
- The VA minimum baseline exceeds the recommended minimum for this application and applies to most of the specifications listed above. The specifications are provided for use with existing equipment, if necessary.
- Each facility is advised to consider the specifications mandated by Directive 6401 when assessing procurement and/or other resource acquisitions to meet the requirements of the QUASAR Audiogram Module.

Conforming to these established and/or emerging VA standards is recommended.

A dynamic update of the VA Desktop Standards is maintained at <span class="mark">REDACTED</span>  
<span id="_Toc168906789" class="anchor"></span>Vendor Installation Wizard

The Vendor Installation Wizard[^15] places DLLs in a specific folder on the PC used for hearing tests: C:\Program Files\VistA\QUASAR\Plugins\\

> **NOTE:** GSI 61 may require a firmware chip update. Follow your site’s procurement process for contacting the vendor: Viasys Grason-Stadler.

Obtain the current driver installer for your device from the QUASAR website.

<span class="mark">REDACTED</span>

To create a download account:

1.  From the VistA menu on the left, click Downloads.
4.  Follow the directions for creating an account.
5.  Download the appropriate installer.
6.  Follow the instructions for installing the driver for your device.

> **NOTE:** The driver installation process varies from installer to installer. Self-guided instructions are within the installer executable.

# Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No unsupported integration agreements are used in the Audiogram Module.

*This page intentionally left blank for double-sided printing.*

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### M routines[^16]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ACKQAG03 Called by Option: ACKQROES
7.  ACKQAG05 Called by routine: ACKQAG03

### Delphi routines[^17]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display Audiogram Edit files: ACKQROES3E.EXE

### Module Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following QUASAR name space variables are used in the Audiogram Module.

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
| ACKQUSNM | user name                       |
| ACKQUSSR | user service                    |

### SAC Exemptions and Approval Dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Module requires no exemptions from VistA Standards and Conventions for package development.

### Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phonetically-Balanced Maximum (PB Max) fields are used to implement the following new functionality and required data dictionary changes[^18]:

The QUASAR Audiogram Module allows the clinician to specify which Word Recognition test (1, 2, 3, 4, or 5) for the left and right ears should be used for displaying the PB Max value. If the test is not specified by the user, the Audiogram Module utilizes current logic for displaying the PB Max value as the default behavior. This is necessary because some Word Recognition tests may include half-list values that cannot be reported as PB Max for some exam types.

The following data dictionary changes were approved by the DBA.

The following two fields were added to the AUDIOMETRIC EXAM DATA file (#509850.9) as follows:

DATA ELEMENT NAME TITLE GLOBAL LOCATION DATA TYPE

-----------------------------------------------------------------------------------------------------------------

509850.9,115.19 APPLIED MAX R 115;19 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>5)!(X\<0)!(X?.E1"."1N.N) X

LAST EDITED: NOV 30, 2006

HELP-PROMPT: Type a Number between 0 and 5, 0 Decimal Digits

DESCRIPTION: This field contains the test to use for PB Max.  
It is manually selected from the GUI if it is anything other than the default.

509850.9,115.2 APPLIED MAX L 115;20 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>5)!(X\<0)!(X?.E1"."1N.N) X

LAST EDITED: NOV 30, 2006

HELP-PROMPT: Type a Number between 0 and 5, 0 Decimal Digits

DESCRIPTION: This field contains the test to use for PB Max.  
It is manually selected from the GUI if it is anything other than the default.

The following fields of the AUDIOMETRIC EXAM DATA file (#509850.9) were expanded from the previous length of 1-2 characters to accept 1-4 characters.

DATA ELEMENT NAME TITLE GLOBAL LOCATION DATA TYPE

-----------------------------------------------------------------------------------------------------------------

509850.9,110.28 List R-1 110;28 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 1 of the Right ear.

509850.9,110.29 LIST R-2 110;29 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 2 of the Right ear.

DATA ELEMENT NAME TITLE GLOBAL LOCATION DATA TYPE

-----------------------------------------------------------------------------------------------------------------

509850.9,110.3 LIST R-3 110;30 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 3 of the Right ear.

509850.9,110.31 LIST R-4 110;31 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 4 of the Right ear.

509850.9,110.32 LIST R-5 110;32 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 5 of the Right ear.

509850.9,111.28 LIST L-1 111;28 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 1 of the Left ear.

509850.9,111.29 LIST L-2 111;29 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 2 of the Left ear.

509850.9,111.3 LIST L-3 111;30 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 3 of the Left ear.

DATA ELEMENT NAME TITLE GLOBAL LOCATION DATA TYPE

-----------------------------------------------------------------------------------------------------------------

509850.9,111.31 LIST L-4 111;31 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 4 of the Left ear.

509850.9,111.32 LIST L-5 111;32 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>4!(\$L(X)\<1) X

HELP-PROMPT: Answer must be 1-4 characters in length.

DESCRIPTION: Word list used for Test 5 of the Left ear.

# Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Module requires no global variables.

*This page intentionally left blank for double-sided printing.*

# Software Security[^19]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional security measures are to be applied. The Audiogram Module uses the standard RPC broker log-in procedure to validate the user and allow access to the system.

No additional licenses are necessary to run the software.

Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mail Groups and Bulletins  
    There is a mail group or bulletin associated with this software when the record is sent to the Denver ALC, as well as when the record is deleted.
8.  Remote Systems  
    Application data is transmitted to the Denver ALC.
9.  Contingency Planning  
    It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.
10. Interfacing  
    Specialized (non VA) interfaces (DLLs) are used and required by this application.
11. Electronic Signatures  
    Electronic signatures are used by this application.
12. Menus  
    There are no options of special note for the Information Security Officers (ISO's) to view.
13. Restricted Patient Records  
    A patient record marked sensitive is handled by CPRS.

*This page intentionally left blank for double-sided printing.*

<span id="_Glossary" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Word/Acronym</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>API</td>
<td>Application Programmer Interface</td>
</tr>
<tr class="even">
<td>AC</td>
<td>Air Conduction</td>
</tr>
<tr class="odd">
<td>AR</td>
<td>Acoustic Reflex</td>
</tr>
<tr class="even">
<td>ARD</td>
<td>Acoustic Reflex Decay</td>
</tr>
<tr class="odd">
<td>ASPS/A&amp;PS</td>
<td>Audiology and Speech Pathology Service</td>
</tr>
<tr class="even">
<td>BC</td>
<td>Bone Conduction</td>
</tr>
<tr class="odd">
<td>C&amp;P</td>
<td>Compensation and Pension</td>
</tr>
<tr class="even">
<td>CAR</td>
<td>Contralateral Acoustic Reflex</td>
</tr>
<tr class="odd">
<td>CNC</td>
<td>Consonant Nucleus Consonant</td>
</tr>
<tr class="even">
<td>CNM</td>
<td>Could Not Mask</td>
</tr>
<tr class="odd">
<td>CNT</td>
<td>Could Not Test</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>dB</td>
<td>Decibel</td>
</tr>
<tr class="even">
<td>Denver ALC</td>
<td>Denver Acquisition &amp; Logistics Center<br />
A part of the Department of Veteran's Affairs, Office of Acquisition and Logistics, and located in Denver, Colorado.</td>
</tr>
<tr class="odd">
<td>DNT</td>
<td>Did Not Test</td>
</tr>
<tr class="even">
<td>DSS</td>
<td>Decision Support System</td>
</tr>
<tr class="odd">
<td>EM</td>
<td>Effective Masking</td>
</tr>
<tr class="even">
<td>HL</td>
<td>Hearing Level</td>
</tr>
<tr class="odd">
<td>Hz</td>
<td>Hertz</td>
</tr>
<tr class="even">
<td>IAR</td>
<td>Ipsilateral Acoustic Reflex</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td>MCL</td>
<td>Most Comfortable Loudness</td>
</tr>
<tr class="odd">
<td>ML</td>
<td>Masking Level</td>
</tr>
<tr class="even">
<td>NR</td>
<td>No Response</td>
</tr>
<tr class="odd">
<td>PB</td>
<td>Phonetically Balanced</td>
</tr>
<tr class="even">
<td>pc</td>
<td>Piece</td>
</tr>
<tr class="odd">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="even">
<td>PI/PB</td>
<td>Performance Intensity-Phonetically Balanced</td>
</tr>
<tr class="odd">
<td>Pr-L</td>
<td>Probe Left</td>
</tr>
<tr class="even">
<td>Pr-R</td>
<td>Probe Right</td>
</tr>
<tr class="odd">
<td>PSAS</td>
<td>Prosthetics and Sensory Aids Service</td>
</tr>
<tr class="even">
<td>PTA</td>
<td>Pure Tone Average</td>
</tr>
<tr class="odd">
<td>QUASAR</td>
<td>Quality: Audiology and Speech Analysis and Reporting</td>
</tr>
<tr class="even">
<td>Routine</td>
<td>Groups of program lines that are saved, loaded, and called as a single unit by way of a specific name.</td>
</tr>
<tr class="odd">
<td>SAT</td>
<td>Speech Awareness Threshold</td>
</tr>
<tr class="even">
<td>Sensitive Patient</td>
<td>Patient is marked sensitive when the patient requests the patient data be restricted.</td>
</tr>
<tr class="odd">
<td>SRT</td>
<td>Speech Reception Threshold</td>
</tr>
<tr class="even">
<td>UCL</td>
<td>Uncomfortable Loudness</td>
</tr>
<tr class="odd">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="even">
<td>VARO</td>
<td>Veterans Affairs Regional Office</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Access code 2
ACKQ\*3.0\*12 2
ACKQAG03 25
ACKQAG05 25
ACKQAUD1 27
ACKQROES3E 1, 22, 23
APIs 25
Archiving 23
Audiogram display 2
Audiogram edit 1, 4, 23
Audiogram module
Delphi executable 4
Delphi routines 22
M routine list 4
M routines 21
Remote procedure 4
Audiometric Exam Data file 9
C
CPRS 1
CPRS functionality 29
CPRS Tools 3
D
Data dictionary
PB Max 34
Word recognition 34
Data dictionary changes 34
Data dictionary utilities 2
Delphi routines 33
Desktop minimums 30
DFN reference 7
E
Entry points 25
Exported options 23
External relationships 29
F
File 509850.9 23
Files referenced in 509850.9 20
G
Global variables 37
I
Install process 3
Installer, Vendor 31
Integration agreements 31
Internal relationships 33
K
KIDS build 3
KIDS Build File Print 2
KIDS Install File Print 2
M
M routines 33
MailMan 3
Module variables 33
P
Process logic 7
Transmission of audiometric data 8
Purging 23
Q
QUASAR 1
QUASAR audiogram module 1, 4
Troubleshooting 5
R
Related documentation 1
ROES 1
Routines
Called 25
RPC Broker 3
RPCs 27
S
Security features 39
Security management 39
Site-specific data 3
Software security 39
V
Vendor installation wizard 31
Vendor installer 4, 31
Verify code 2
VistA document library 1
[^1]: Two M routines and a remote procedure are added in the Patch 13 KIDS build.
[^2]: Section added about the Audiogram Edit component.
[^3]: Section added about the vendor DLL installer.
[^4]: Section added for troubleshooting the Audiogram Module.
[^5]: Removed the Enter Edit Audiogram Data flow chart and removed the Audiogram Display flow chart.
[^6]: Modified the Transmission of Audiometric Data flow chart.
[^7]: Updated the condensed listing of fields and attributes.
[^8]: Added two new M routines.
[^9]: Removed the Display Audiogram Delphi routines.
[^10]: Removed the exported option: ACKQROES3 – Audiogram Display.
[^11]: Added one remote procedure call.
[^12]: Modified the called routines, entry points, and APIs.
[^13]: Modified the remote procedure calls list.
[^14]: Modified external relationships by replacing Standalone Functionality with CPRS Functionality.
[^15]: Section is added for the vendor installation wizard.
[^16]: Modified internal relationships by adding two routines.
[^17]: Modified internal relationships by removing Display Audiogram files: ACKQROES3.EXE .
[^18]: Added a section on data dictionary changes.
[^19]: Chapter added for software security.
