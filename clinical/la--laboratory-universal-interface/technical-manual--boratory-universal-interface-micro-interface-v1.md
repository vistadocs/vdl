---
title: "Laboratory: Universal Interface Micro Interface Version 1 Technical Manual"
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: 
  - 11
  - 61
  - 62
  - 8989
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - parameter
  - blockquote
  - class
  - sequence
  - release
  - interface
  - strong
  - micro
page_count: 0
word_count: 6685
section_count: 24
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 8
revision_newest: 04/12/2017
revision_oldest: 12/14/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

VistA Lab Enhancements – Microbiology

Release: Lab Micro Interface Release 1.0

(combined build for LA\*5.2\*90 and LR\*5.2\*474)

Technical Manual

AndSecurity Guide

![](laboratory-universal-interface-micro-interface-version-1-technical-manual/001.png)

April 2017

Document Version 1.7

Office of Information and Technology (OI&T)

Revision History

| Date       | Revision | Description                                                                                 | Author                             |
|------------|----------|---------------------------------------------------------------------------------------------|------------------------------------|
| 04/12/2017 | 1.7      | Updated software requirements.                                                              | <span class="mark">REDACTED</span> |
| 01/10/2017 | 1.6      | Addition of version number for Data Innovation’s Instrument Manager.                        | <span class="mark">REDACTED</span> |
| 01/06/2017 | 1.5      | Minor edits based on technical review provided by Enterprise Project Management Office.     | <span class="mark">REDACTED</span> |
| 01/04/2017 | 1.4      | Updated list of routines, section 4.0.                                                      | <span class="mark">REDACTED</span> |
| 12/17/2016 | 1.3      | Added clarifying information for section 1.4.2.                                             | <span class="mark">REDACTED</span> |
| 12/16/2016 | 1.2      | Minor edits to sections 5 and 6, and table 2.                                               | <span class="mark">REDACTED</span> |
| 12/15/2016 | 1.1      | Minor revisions. Sentence added to sections 3 and 15. Table 4 updated for point of contact. | <span class="mark">REDACTED</span> |
| 12/14/2016 | 1.0      | Document baselined.                                                                         | <span class="mark">REDACTED</span> |

<span id="_Ref251310381" class="anchor"></span>Table 1: Text Conventions

Artifact Rational

A Technical Manual is a required end-user document for all OI&T software releases. The intended audience for this document is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
  - [Text Conventions](#text-conventions)
    - [Disclaimers](#disclaimers)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
- [Files](#files)
  - [Kernel Patches](#kernel-patches)
  - [Global Growth](#global-growth)
- [Routines](#routines)
- [Templates](#templates)
- [Parameters](#parameters)
- [Data Dictionary (DD)](#data-dictionary-dd)
- [Exported Options](#exported-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-wide Variables](#software-wide-variables)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [HL7 ERR Segment](#hl7-err-segment)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [RACI Chart](#raci-chart)
- [Glossary](#glossary)
The Veterans Health Information Systems Technology Architecture (VistA) Laboratory Enhancement for Microbiology shall provide enhancements which will support the electronic bidirectional communication of automated identification and susceptibility testing instruments with the VistA Laboratory Universal Interface (UI) through middleware or a generic instrument manager. The enhancements will provide standardization across the VA resulting in improved efficiency and enhanced security of patients’ information. The Lab Micro Interface Release 1.0 Kernel Installation and Distribution System (KIDS) combined build that contains the patches LA\*5.2\*90 and LR\*5.2\*474 support the initiative.
The transfer of electronic order and result lab data is achieved via the Health Level Seven International (HL7) standard. This standard focuses on the application layer, or the seventh layer of the Open Systems Interconnection model (OSI model). Additional information regarding HL7 is included in section 10.4, HL7 messaging.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the guide is to familiarize users with the important features and navigational elements of the Lab Micro Interface Release 1.0 build.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*474 will provide new functionality to the Enter/Verify Data option of the Lab UI package. Three new release actions will now be available to the Technologist with the authority to release results. Results will be available to the applicable authorized clinicians and providers. In addition, the patch will allow a VA Medical Center the option of setting release defaults at the Package or User level.

Patch LA\*5.2\*90 will provide the constructs necessary to allow Microbiology or MI subscripted tests to be added to an Auto Instrument entry. An enhancement is also included for antibiotic susceptibility result processing which will now allow laboratories the ability to report susceptibilities to antimicrobial agents by utilizing SNOMED CT codes such as Positive and Negative. The handling of variations is also included in the build, such as the reporting of extended-spectrum beta-lactamases or ESBL enzymes that are resistant to most beta-lactam antibiotics. Locally mapped codes using an “L” for code set ID will now be processed for antibiotic susceptibilities.

All of the following SNOMED CT codes shall be supported with the release of patch LA\*5.2\*90:

- 131196009 Susceptible
- 260357007 Moderately susceptible
- 264841006 Intermediately susceptible
- 30714006 Resistant
- 10828004 Positive
- 260385009 Negative

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for the Technical Manual and Security Guide are the following:

- Laboratory Information Managers (LIMs)
- Microbiology Technologists
- Automated Data Processing Application Coordinators (ADPACs)
- Information Resources Management (IRM) staff

Installation and auto-instrumentation setup for the Lab Micro Interface Release 1.0 build requires interactive participation between IRM staff and LIM or ADPAC personnel.

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:

| Font              | Use                              | Example                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the link: <http://www.va.gov/vdl>                                                      |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
|                       | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
|                       | VistA filenames                      | XYZ file \#798.1                                                                                                          |
|                       | VistA field names                    | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.” |
| Courier New, bold     | User responses to screen prompts     | NO                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                          |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | “There are no changes in the performance of the system once the installation process is complete.”                        |
| Times New Roman Bold  | Emphasis                             | Note: You can also type the access code, followed by a semicolon, followed by the verify code.                        |

<span id="_Toc469572843" class="anchor"></span>Table 2: List of Routines

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation is also available on the VistA Document Library (VDL) The online versions will be updated as needed. Please look for the latest version on the VDL: <http://www.va.gov/vdl/>
The following documents were used in preparation of this guide:
- Laboratory Universal Interface (UI) Version 1.6 Health Level 7 (HL7) Version 2.5.1 Interface Specifications Document for Lab Micro Interface Release 1.0. November 2016, version 2.0.
- Deployment, Installation, Back-out, Rollback Guide for release Lab Micro Interface Release 1.0. September 2016, version 1.7.
- LA\*5.2\*90 Patch Description. November 2016. Note: this document is available via Forum only.
- LR\*5.2\*474 Patch Description. November 2016. Note: this document is available via Forum only.
- Systems Design Document for the VistA Laboratory Enhancement Microbiology, initiative, May 2016, version .9. Note: this document is not available.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram depicts the data flows between the VistA Lab package, the Data Innovation (DI) Instrument Manager (IM), and the analyzers. Examples of analyzers utilized at sites include: BD Bactec<sup>TM</sup>, Dade MicroScan <sup>TM</sup>, and bioMérieux Vitek<sup>TM</sup> systems.

<span id="_Toc469572848" class="anchor"></span>Figure 1: High-level Process Flowchart

![](laboratory-universal-interface-micro-interface-version-1-technical-manual/002.png)

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA software is a Kernel Installation and Distribution System (KIDS) software release. The table below describes the software and documentation available for download.

Table 2: Software Files to Download

<table>
<caption><p><span id="_Toc469572844" class="anchor"></span>Table 3: List of Templates</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 77%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>Host File</th>
<th>File Name</th>
<th>FTP Protocol</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KIDS Distribution</td>
<td><p>The Lab_Micro_Interface_Release 1_0.KID file contains 2 patches:</p>
<ul>
<li><blockquote>
<p>LR*5.2*474</p>
</blockquote></li>
<li><blockquote>
<p>LA*5.2*90</p>
</blockquote></li>
</ul></td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>ZIP</td>
<td><p>The Lab_Micro_Interface_Release 1_0.DOCS.ZIP contains both PDF and DOC formatted files of the following documents:</p>
<p>VLE Micro_Lab_Micro_Interface_Release_1.0_Technical_Manual</p>
<p>VLE Micro_Lab_Micro_Interface_Release_1.0_User_Guide</p>
<p>VLE Micro_Deployment_Installation_Roll Back_Back Out_Guide</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

<span id="_Toc469572844" class="anchor"></span>Table 3: List of Templates

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 build will operate on the current VA computer hardware systems.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 build will operate on the current VA computer systems, which includes Kernel 8.0 and FileMan 22.

Lab Micro Interface Release 1.0 will work in conjunction with the functionality in the Auto Release 1.0 (LR\*5.2\*458 and LA\*5.2\*88) software build and Data Innovation’s enhanced IM driver software. Thus, the prerequisites for the utilization of the full functionality in the Lab Micro Interface Release 1.0 build includes the following:

- Auto Release 1.0 (LR\*5.2\*458 and LA\*5.2\*88).
- Data Innovations IM version 8.13.03 or greater.

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan 22 is the only database requirement for the Lab Micro Interface Release 1.0 build.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and auto-instrumentation setup for the Lab Micro Interface Release 1.0 build requires interactive participation between IRM staff and LIM or ADPAC personnel.

The Lab Micro Interface Release 1.0 build may be loaded with users on the system if the Lab Interface related activities have been halted. Halting of activities include, but are not limited to, the following:

- Editing of an Auto Instrument file entry.
- Turn off the Auto Downloading process to prevent the building and downloading of a Load/Worklist to the Instrument Manager.
- Shut down all LA7UI logical links and any other HL7 process (HLZTCP or HLLP processes) to prevent the processing of result messages from the IM.

In addition, you may wish to install the patches during non-peak hours.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers Kernel patches and Global Growth considerations.

## Kernel Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patches must be current on the target system to avoid problems loading and/or installing the patches.

## Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no significant change to global growth.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of routines applies to the Lab Micro Interface Release 1.0 build:

| Routine | Release  | Brief Description                                                                                                      |
|-------------|--------------|----------------------------------------------------------------------------------------------------------------------------|
| LRMIEDZ2    | LR\*5.2\*474 | Microbiology edited routine.                                                                                               |
| LRVR0       | LR\*5.2\*474 | Pertains to LEDI MI/AP Auto-instrument verification                                                                        |
| LRVRMI2     | LR\*5.2\*474 | Continuation of LRVRMI4 and is used for extracting results from the LAH global and storing it into LAB DATA FILE (#63).    |
| LRVRMI2A    | LR\*5.2\*474 | Continuation of LRVRMI4 and is used for extracting results from the LAH global and storing it into LAB DATA FILE (#63).    |
| LRVRMI3     | LR\*5.2\*474 | Continuation of LRVRMI4 and is used for extracting results from the LAH global and storing it into LAB DATA FILE (#63).    |
| LRVRMI4     | LR\*5.2\*474 | Extracts the information in the ^TMP ("LRMI", \$J) global and stores it into the Lab Data micro sub-file.                  |
| LRVRMI4A    | LR\*5.2\*474 | Extracts the information in the ^TMP ("LRMI", \$J) global and stores it into the Lab Data micro sub-file.                  |
| LA7VHLU6    | LA\*5.2\*90  | HL7 Code Sets utility.                                                                                                     |
| LA7VIN7A    | LA\*5.2\*90  | Process ORU's OBX for Micro (BACTERIA).                                                                                    |
| LA7VIN7B    | LA\*5.2\*90  | Process ORU's OBX for Micro (FUNGAL and MYCOBACTERIA).                                                                     |
| LA7VIN7     | LA\*5.2\*90  | Process OBX segment data for Micro ORU messages.                                                                           |
| LA7VIN2A    | LA\*5.2\*90  | Continuation of LA7VIN2 and supports the performing lab functionality by processing incoming Universal Interface messages. |
| LA90A       | LA\*5.2\*90  | Environment check routine.                                                                                                 |

<span id="_Toc469572846" class="anchor"></span>Table 5: Tier Support Contact Information for COTS Software

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new templates are associated with patch LR\*5.2\*474 that is a part of the Lab Micro Interface Release 1.0 build:

<table>
<caption><p><span id="_Toc469572847" class="anchor"></span>Table 6: RACI Chart</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Template Name</strong></th>
<th><strong>File Name and Number</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LR USER</td>
<td><p>PARAMETER TEMPLATE</p>
<p>FILE #8989.52</p></td>
</tr>
<tr class="even">
<td>LR PKG</td>
<td><p>PARAMETER TEMPLATE</p>
<p>FILE #8989.52</p></td>
</tr>
</tbody>
</table>

<span id="_Toc469572847" class="anchor"></span>Table 6: RACI Chart

The two parameter templates are shown in the figures below. If desired, perform a FileMan inquiry of the PARAMETER TEMPLATE file (#8989.52).

<span id="_Toc468272149" class="anchor"></span>Figure 2: LR USER

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NAME: <strong>LR USER</strong> DISPLAY TEXT: Lab User Level Parameters</p>
<p>USE ENTITY FROM: NEW PERSON</p>
<p>SEQUENCE: 100 PARAMETER: LR VER DISPLAY PREV COMMENT</p>
<p>SEQUENCE: 200 PARAMETER: LA7UTILA PARSE</p>
<p>SEQUENCE: 210 PARAMETER: LA7UTILA USE BROWSER</p>
<p>SEQUENCE: 50 PARAMETER: LR LABEL PRINTER DEFAULT</p>
<p>SEQUENCE: 220 PARAMETER: LA7UTILA SHOIDS</p>
<p>SEQUENCE: 125 PARAMETER: LRAPRES1 AP ALERT</p>
<p>SEQUENCE: 120 PARAMETER: LR AP REPORT SELECTION</p>
<p>SEQUENCE: 300 PARAMETER: LR CH GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 305 PARAMETER: LR MI GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 310 PARAMETER: LR AP GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 110 PARAMETER: LR MI VERIFY DISPLAY PROVIDER</p>
<p>SEQUENCE: 130.1 PARAMETER: LR ACCESSION DEFAULT SPECIMEN</p>
<p>SEQUENCE: 130.2 PARAMETER: LR ACCESSION DEFAULT COL SAMP</p>
<p>SEQUENCE: 130.3 PARAMETER: LR ACCESSION DEFAULT LAB TEST</p>
<p>SEQUENCE: 150.1 PARAMETER: LR MANIFEST EXC PREV TEST</p>
<p>SEQUENCE: 102 PARAMETER: LR VER DEFAULT PERFORMING LAB</p>
<p>SEQUENCE: 112.6 PARAMETER: LR MI VERIFY CPRS ALERT</p>
<p>SEQUENCE: 112.3 PARAMETER: LR CH VERIFY CPRS ALERT</p>
<p>SEQUENCE: 150.2 PARAMETER: LR MANIFEST DEFLT ACCESSION</p>
<p>SEQUENCE: 900 PARAMETER: LR MAPPING DEFAULT DIRECTORY</p>
<p>SEQUENCE: 900.1 PARAMETER: LR MAPPING DEFAULT FILESPEC</p>
<p>SEQUENCE: 104 PARAMETER: LR ASK PERFORMING LAB AP</p>
<p>SEQUENCE: 105 PARAMETER: LR ASK PERFORMING LAB MICRO</p>
<p><strong>SEQUENCE: 113 PARAMETER: LR MI UI RELEASE DEFAULT</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc469572850" class="anchor"></span>Figure 3: LR PKG

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NAME: <strong>LR PKG</strong></p>
<p>DISPLAY TEXT: Lab Package Level Parameters</p>
<p>USE ENTITY FROM: PACKAGE</p>
<p>SEQUENCE: 1 PARAMETER: LR COLLECT MONDAY</p>
<p>SEQUENCE: 2 PARAMETER: LR COLLECT TUESDAY</p>
<p>SEQUENCE: 3 PARAMETER: LR COLLECT WEDNESDAY</p>
<p>SEQUENCE: 4 PARAMETER: LR COLLECT THURSDAY</p>
<p>SEQUENCE: 5 PARAMETER: LR COLLECT FRIDAY</p>
<p>SEQUENCE: 6 PARAMETER: LR COLLECT SATURDAY</p>
<p>SEQUENCE: 7 PARAMETER: LR COLLECT SUNDAY</p>
<p>SEQUENCE: 8 PARAMETER: LR IGNORE HOLIDAYS</p>
<p>SEQUENCE: 11 PARAMETER: LR EGFR METHOD</p>
<p>SEQUENCE: 12 PARAMETER: LR EGFR AGE CUTOFF</p>
<p>SEQUENCE: 13 PARAMETER: LR EGFR RESULT SUPPRESS</p>
<p>SEQUENCE: 9.2 PARAMETER: LR VER EA VERIFY BY UID</p>
<p>SEQUENCE: 9.1 PARAMETER: LR VER EM VERIFY BY UID</p>
<p>SEQUENCE: 20 PARAMETER: LRAPRES1 AP ALERT</p>
<p>SEQUENCE: 21 PARAMETER: LR AP REPORT SELECTION</p>
<p>SEQUENCE: 24 PARAMETER: LR AP SNOMED SYSTEM PRINT</p>
<p>SEQUENCE: 50 PARAMETER: LR CH GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 52 PARAMETER: LR MI GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 54 PARAMETER: LR AP GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 9.3 PARAMETER: LR MI VERIFY DISPLAY PROVIDER</p>
<p>SEQUENCE: 130.1 PARAMETER: LR ACCESSION DEFAULT SPECIMEN</p>
<p>SEQUENCE: 130.2 PARAMETER: LR ACCESSION DEFAULT COL SAMP</p>
<p>SEQUENCE: 130.3 PARAMETER: LR ACCESSION DEFAULT LAB TEST</p>
<p>SEQUENCE: 25 PARAMETER: LR AP SURGERY REFERENCE</p>
<p>SEQUENCE: 9.35 PARAMETER: LR MI VERIFY CPRS ALERT</p>
<p>SEQUENCE: 9.36 PARAMETER: LR CH VERIFY CPRS ALERT</p>
<p>SEQUENCE: 8.1 PARAMETER: LR LAB COLLECT FUTURE</p>
<p>SEQUENCE: 8.11 PARAMETER: LR MAX DAYS CONTINUOUS</p>
<p>SEQUENCE: 200 PARAMETER: LR REPORTS FACILITY PRINT</p>
<p>SEQUENCE: 900 PARAMETER: LR MAPPING DEFAULT DIRECTORY</p>
<p>SEQUENCE: 900.1 PARAMETER: LR MAPPING DEFAULT FILESPEC</p>
<p>SEQUENCE: 22 PARAMETER: LR ASK PERFORMING LAB AP</p>
<p>SEQUENCE: 23 PARAMETER: LR ASK PERFORMING LAB MICRO</p>
<p>SEQUENCE: 150.1 PARAMETER: LR MANIFEST EXC PREV TEST</p>
<p>SEQUENCE: 150.2 PARAMETER: LR MANIFEST DEFLT ACCESSION</p>
<p>SEQUENCE: 120</p>
<p>PARAMETER: LR AP DEFAULT ACCESSION NUMBER</p>
<p>SEQUENCE: 210 PARAMETER: LR WORKLIST DATA CLEANUP</p>
<p><strong>SEQUENCE: 9.305 PARAMETER: LR MI UI RELEASE DEFAULT</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new parameter LR MI UI RELEASE DEFAULT will be included which will provide the Veterans Affairs Medical Center (VAMC) site the ability to set the release default at the package and/or user levels.

A display of the parameter is shown in the figure below. If desired, perform a FileMan inquiry of the PARAMETER DEFINITION file (#8989.51).

<span id="_Toc468272150" class="anchor"></span>Figure 4: LR MI UI RELEASE DEFAULT Parameter

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NAME: LR MI UI RELEASE DEFAULT</p>
<p>DISPLAY TEXT: Default Micro Instrument Release Action</p>
<p>MULTIPLE VALUED: Yes INSTANCE TERM: Load/Work List</p>
<p>VALUE TERM: Default load/work list verify method</p>
<p>PROHIBIT EDITING: No VALUE DATA TYPE: set of codes</p>
<p>VALUE DOMAIN: 0:Quit;1:Release;2:Comments/Release;3:Edit (full)</p>
<p>VALUE HELP: Specify the default result release action presented to user.</p>
<p>KEYWORD: MICRO UI</p>
<p>INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 68.2</p>
<p>DESCRIPTION:</p>
<p>Used to designate the default release action presented to the user when</p>
<p>verifying automated microbiology results in the "MI" subscript via options</p>
<p>that use a load/work list. Parameter is associated with the load/worklist</p>
<p>selected by the user.</p>
<p>Parameter can be set at the package or user level.</p>
<p>User level takes precedence over package level.</p>
<p>PRECEDENCE: 1 ENTITY FILE: USER</p>
<p>PRECEDENCE: 2 ENTITY FILE: PACKAGE</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Data Dictionary (DD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DD \#62.41, LABORATORY TESTS sub-file is modified with the installation of patch LA\*5.2\*90 that is a part of the Lab Micro Interface Release 1.0 build.

The trigger for the ROUTINE STORAGE field has been rewritten as a “NEW STYLE” cross reference and will only be set when for Chemistry (CH) subscripted tests.

LABORATORY TESTS (#30) was changed from CHEM TESTS and the screen modified to allow for MI subscripted tests to be selected.

<span id="_Toc468272147" class="anchor"></span>Figure 5: DD \#62.41

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>STANDARD DATA DICTIONARY #62.41 -- LABORATORY TESTS SUB-FILE</p>
<p>JUN 8,2016@12:37:17 PAGE 1</p>
<p>STORED IN ^LAB(62.4,D0,3, SITE: TEST.CHEYENNE.MED.VA.GOV UCI:</p>
<p>VISTA,ROU</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>--------------------------------------------------------------------------</p>
<p>62.41,.01 TEST 0;1 POINTER TO LABORATORY TEST FILE (#60) (Required) (Multiply asked)</p>
<p>INPUT TRANSFORM: S DIC("S")="I $D(^LAB(60,Y,.2))!(""MI""[$P</p>
<p>(^LAB(60,Y,0),U,4))" D ^DIC K DIC S DIC=DI</p>
<p>E,X=+Y K:Y&lt;0 X</p>
<p>LAST EDITED: JUN 07, 2016</p>
<p>HELP-PROMPT: Enter the name of a test for which the instrument will send data.</p>
<p>DESCRIPTION: This contains the test names for this instrument.</p>
<p>SCREEN: S DIC("S")="I $D(^LAB(60,Y,.2))!(""MI""[$P</p>
<p>(^LAB(60,Y,0),U,4))"</p>
<p>EXPLANATION: Allow CH atomic test or Microbiology subscript test</p>
<p>FIELD INDEX: AD (#867) MUMPS IR ACTION</p>
<p>Short Descr: Set "ROUTINE STORAGE" field with CH subscripted test data name number</p>
<p>Description: This trigger cross reference will only populate the "ROUTINE STORAGE" field with</p>
<p>63.04 data location file number for CH (Chemistry) atomic subscripted test having</p>
<p>data name field populated. See example below. MI (Microbiology) subscripted test</p>
<p>have no data name, therefore the "AUTO INSTRUMENT" file # 62.4, "TEST" field #30,</p>
<p>(#62.41), subfile #62.41, "ROUTINE STORAGE" file #11 will NOT be set.</p>
<p>EXAMPLE: CH subscripted test having DATA NAME will populate the ROUTINE</p>
<p>STORAGE field with: TV(#,1) MI subscripted test will NOT set the ROUTINE STORAGE</p>
<p>field.</p>
<p>Set Logic: S $P(^LAB(62.4,DA(1),3,DA,1),U)="TV("_X2(3</p>
<p>)_",1)"</p>
<p>Set Cond: S X=(X2(2)="CH")&amp;(X2(3)'="")</p>
<p>Kill Logic: S $P(^LAB(62.4,DA(1),3,DA,1),U)=""</p>
<p>X(1): TEST (62.41,.01) (Subscr 1) (Len 10)</p>
<p>(forwards)</p>
<p>Transform (Display):</p>
<p>X(2): Computed Code: S X=$P($G(^LAB(60,X(1),0)),</p>
<p>U,4)</p>
<p>(Subscr 2)</p>
<p>X(3): Computed Code: S X=$P($G(^LAB(60,X(1),.2))</p>
<p>,U)</p>
<p>(Subscr 3)</p>
<p>FILES POINTED TO FIELDS</p>
<p>LABORATORY TEST (#60) TEST (#.01)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 build does not contain any associated exported options or protocols.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail groups, alerts, and bulletins are not created, required, or used by the software.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated documentation will be available on the VistA Document Library (VDL). The online versions will be updated as needed. Please look for the latest version on the VDL if more information is required:

- Laboratory Universal Interface (UI) Version 1.6 Health Level 7 (HL7) Version 2.5.1 Interface Specifications Document for Lab Micro Interface Release 1.0 available via <http://www.va.gov/vdl>
- LDSI/LEDI IV Update HL7 Interface Specification document available via <http://www.va.gov/vdl>

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integration Control Registrations (ICRs) were not created and/or used.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

API’s are not applicable.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC’s are not applicable.

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Universal Interface (UI) implements an interface to the HL7 Standard for use by the VistA Laboratory application in communicating with non-VistA systems to exchange healthcare information. The interface strictly adheres to the HL7 Standard and avoids using “Z” type extensions to the Standard.

The following HL7 message types are used to support the exchange of Laboratory information:

- ACK General Acknowledgment
- ORM Order
- ORR General Order Response Message response to any ORM
- ORU Observational Results Unsolicited

The following HL7 segments are used to support the exchange of Laboratory information:

- ERR Error
- MSA Message Acknowledgment
- MSH Message Header
- NTE Notes and Comment
- OBR Observation Request
- OBX Observation
- ORC Common Order
- PID Patient Identification
- PV1 Patient Visit

For additional information, please refer to the Laboratory Universal Interface (UI) Version 1.6 Health Level 7 (HL7) Version 2.5.1 Interface Specifications Document for the Lab Micro Interface Release 1.0 build is available at: <http://www.va.gov/vdl>.

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Web services were not created and/or used.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAC exemptions for this software were not required.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All related routines are listed in Section 4, Routines.

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAC exemptions for this software were not required.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Privacy represents information that must be protected and covers the collection, use, and disclosure of personal information. Security represents how information must be protected and encompasses the methods for accessing and protecting the information. A Security Guide aids in controlling the release of sensitive information related to nationally released software. The Lab Micro Interface Release 1.0 build does not contain any highly sensitive information. Information may be obtained through the Freedom of Information Act (FOIA) requests. There are no unique/atypical features or other information that would be of interest to security personnel or other support groups.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security menus and options are not distributed with the build.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software security keys are not required for the build.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any additional file security for the software is not required.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures are not applicable.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software does not provide any secure data transmission capabilities.

The following websites address encryption of data exchanged over any facility connection:

- Federal Information Security Management Act (FISMA): <http://csrc.nist.gov/groups/SMA/fisma/index.html>

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software does not provide any data archiving capabilities.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-standard or special cross-references are not applicable.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides examples of interface application errors, back up procedures, and contact information.

## HL7 ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERR segment is used to add error comments to acknowledgment messages when receiving ORU Result Messages. The fields supported are listed below and can be utilized in troubleshooting issues.

> ERR-3 HL7 Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-3 will contain value 0 from HL7 Table 0357.
- If MSA-1 Acknowledgment Code is AE then ERR-3 will contain an error code/message from HL7 Table 0357.

> ERR-4 Severity

- If MSA-1 Acknowledgment Code is AA then ERR-4 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from HL7 Table 0357

ERR-5 Application Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-5 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-5 will contain an error code/message from VistA Laboratory LA7 MESSAGE LOG BULLETINS FILE (#62.485)

ERR-8 User Message

- If MSA-1 Acknowledgment Code is AA then ERR-8 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-8 will contain text message from ERR-5.

ERR-9 Inform Person Indicator

- If MSA-1 Acknowledgment Code is AA then ERR-9 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-9 will contain ”USR”.

An example of an AE application error is shown below.

<span id="_Toc461622853" class="anchor"></span>Figure 6: Example Message with an AE application error.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>DATE/TIME ENTERED: NOV 19, 2016@07:37:36</p>
<p>  TRANSMISSION TYPE: OUTGOING</p>
<p>  RELATED EVENT PROTOCOL: LA7UI1 ORU-R01 EVENT</p>
<p>MESSAGE TEXT:  </p>
<p> MSA|AE|AITC001|Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.</p>
<p> </p>
<p> ERR|||207^Application internal error^HL70357|E|49^Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.^99VA62.485||</p>
<p>|Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3</p>
<p>716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.|USR</p>
<p> </p>
<blockquote>
<p>  NO. OF CHARACTERS IN MESSAGE: 530   NO. OF EVENTS IN MESSAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was run as directed, ‘Backup a Transport Global’, then routines have the ability to be restored from the “backup” MailMan message that was generated. However, the KIDS installation process does not perform a restore of other VistA components, such as data dictionary, cross-reference, and template changes, etc.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

Table 3 lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information.

<span id="_Ref390770787" class="anchor"></span>Table 4: Tier Support Contact Information

| Name                                  | Role                   | Org | Contact Info                    |
|-------------------------------------------|----------------------------|---------|-------------------------------------|
| Clinical Application Coordinator          | Tier 0 Support             | VHA     | Local to each facility.             |
| OI&T National Service Desk                | Tier 1 Support             | OI&T    | <span class="mark">REDACTED</span>  |
| OI&T Local Support                        | Tier 2 Support             | OI&T    | OI&T Local Helpdesk                 |
| Health Product Support                    | Tier 2 Support             | VHA     | <span class="mark">REDACTED</span>  |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T    | <span class="mark">REDACTED</span>  |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T    | <span class="mark">REDACTED</span>  |
| Enterprise Operations                     | Tier 3 & 4 Support         | OI&T    | OI&T Enterprise Operations Helpdesk |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Role</strong></th>
<th><strong>Organization</strong></th>
<th><strong>Contact Information</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LIM</td>
<td>Tier 0 Support</td>
<td>VHA</td>
<td>Local to each facility</td>
</tr>
<tr class="even">
<td>Commercial of-the-shelf (COTS) Vendor</td>
<td>Tier 2 Support</td>
<td>Vendor</td>
<td><p>Data Innovations</p>
<p><a href="http://www.datainnovations.com/">http://www.datainnovations.com/</a></p></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# RACI Chart 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Responsible (R): The persons or groups who execute the task are responsible for the correct execution of the process and activities.
- Accountable (A): For each activity, only one role (person or group) should be answerable for owning the end result and process quality.
- Consulted (C): A person or group that provides additional knowledge and information.
- Informed (I): A person or group that only receives process execution and quality information (per activity or in summary form).

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Functional Roles</strong></th>
<th><blockquote>
<p><strong>Requirements</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Design</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Development</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Test</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Documentation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Training</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Deployment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Program Manager</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Project Manager</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>R, I, C</td>
<td>R</td>
<td>R</td>
<td>R</td>
</tr>
<tr class="odd">
<td>Project Planner</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
</tr>
<tr class="even">
<td>Technical Architect</td>
<td>I, C</td>
<td>A, R</td>
<td>A, R</td>
<td>R, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
</tr>
<tr class="odd">
<td>Functional Analyst</td>
<td>R, I, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, I, C</td>
<td>R, I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Requirements Manager</td>
<td>A, R</td>
<td>R, I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
<td>R, I, C</td>
<td>I, C</td>
</tr>
<tr class="odd">
<td>Configuration Manager</td>
<td>I</td>
<td>I</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I</td>
<td>A, R</td>
</tr>
<tr class="even">
<td>Test Manager</td>
<td>I</td>
<td>I</td>
<td>I, C</td>
<td>A, R</td>
<td>R, I, C</td>
<td>I</td>
<td>I, C</td>
</tr>
<tr class="odd">
<td>Test Analyst</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>R, C</td>
<td>I, C</td>
<td>I</td>
<td>I</td>
</tr>
<tr class="even">
<td>Lead Developer</td>
<td>I, C</td>
<td>I, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, I, C</td>
<td>I, C</td>
<td>R, I, C</td>
</tr>
<tr class="odd">
<td>Developer</td>
<td>I, C</td>
<td>I, C</td>
<td>R, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Training Manager</td>
<td>I</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
<td>A, R</td>
<td>I</td>
</tr>
<tr class="odd">
<td>Technical Writer</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>A, R</td>
<td>I</td>
<td>I</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Glossary of Terms</strong></th>
<th><strong>Definitions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access Code</td>
<td><blockquote>
<p>A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td><blockquote>
<p>Automated Data Processing Coordinator.</p>
</blockquote>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM). Also, the designated individual responsible for user-level management and maintenance of an application package (<em>e.g.</em>, Laboratory).</td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>Auto Instruments</td>
<td><blockquote>
<p>Automated instruments used in the Lab that identify and measure tissue or other specimens.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Bactec<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for analyzing blood cultures within the Microbiology module.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>COTS</td>
<td><blockquote>
<p>Commercial off-the-shelf. Software or hardware that can be purchased as a packaged solution.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Driver</td>
<td><blockquote>
<p>Computer program which transports electronic information such as data or commands going between two computers or devices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td><blockquote>
<p>FileMan is a set of M utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FORUM</td>
<td><blockquote>
<p>FORUM is the VA’s national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The National Patch Module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (e.g., a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>File Transfer Protocol (FTP)</td>
<td><blockquote>
<p>A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in Internet Standard 9, Request for Comments 959.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Generic Instrument Manager (GIM)</td>
<td><blockquote>
<p>Vendor system communicating with VistA is called a Generic Interface Manager (GIM).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Globals</td>
<td><blockquote>
<p>M uses globals: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
</blockquote>
<p>SET ^A(“first_name”)=”Craig”</p>
<blockquote>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common M programs is a database management system. FileMan is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Kernel Installation and Distribution System (KIDS)</td>
<td><blockquote>
<p>KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LIM</td>
<td><blockquote>
<p>Laboratory Information Manager.</p>
<p>The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other Computerized Patient Record System (CPRS) functions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>M</td>
<td><blockquote>
<p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. M data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Mass Spec<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for organism identification within the Microbiology module.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MUMPS</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Namespace</td>
<td><blockquote>
<p>A logical partition on a physical device that contains all the artifacts for a complete M system, including globals, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MRSA-PT.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td><blockquote>
<p>A specific type of MailMan message used to distribute KIDS builds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SNOMED CT</td>
<td><blockquote>
<p>Systematized Nomenclature of Medicine Clinical Terms was developed to standardize the coding of information regarding specific diseases.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td><blockquote>
<p>Department of Veterans Affairs Medical Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Vitek<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for measuring antibiotic susceptibility within the Microbiology module.</p>
</blockquote></td>
</tr>
</tbody>
</table>
