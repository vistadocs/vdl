---
title: LA*5.2*68 Laboratory HL7 Specification
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: Laboratory HL7 Specification
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*68
group_key: "LR:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 16%\\" /> <col style=\\"width: 9%\\" /> <col style=\\"width: 36%\\" /> <col style=\\"width: 22%\\" /> <col style=\\"width: 15%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Revision</th> <th>Description</th> <th>Section</th> <th>Author</th> </tr> </thead> <tbody"
audience: 
keywords: 
  - span
  - mark
  - class
  - xxxxxx
  - table
  - message
  - vista
  - code
  - identifier
  - contents
page_count: 0
word_count: 18559
section_count: 20
table_count: 35
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/la_5_2hl7spec_68.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/la_5_2hl7spec_68.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

![](la-5-2-68-laboratory-hl7-specification/001.png)

Lab-VA HDR and COTS  
HL7 Interface Specification  
for Patch LA\*5.2\*68

July 2010

VistA Health Systems Design & Development

Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 36%" />
<col style="width: 22%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Section</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8/13/04</td>
<td>1.0</td>
<td>Initial Draft.</td>
<td>All</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/19/05</td>
<td>1.1</td>
<td>Incorporated microbiology comments in HL7 table 0356 per HDR-IMS request</td>
<td>NTE message segment</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/17/05</td>
<td>1.2</td>
<td>Incorporated new examples CH, MI and SP subscript sample messages</td>
<td>Message examples</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/18/05</td>
<td>1.21</td>
<td><p>Removed reference to ‘control’ in specimen source section.</p>
<p>Corrected OBR sequence in sample messages.</p>
<p>Added tables listing default NLT and LOINC mapping for sections of VistA Laboratory that are not NLT/LOINC mapped.</p></td>
<td><p>OBR message section</p>
<p>Message examples</p>
<p>Specific Message Consideration</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/31/05</td>
<td>1.22</td>
<td><p>Updated MSH message type</p>
<p>Updated OBX-3 regarding LOINC and VUID as coding systems</p></td>
<td><p>MSH section</p>
<p>OBX message section</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/09/05</td>
<td>1.23</td>
<td>Updated OBX-6 regarding units with L coding system when from VistA and not standardized units.</td>
<td>OBX message section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/27/05</td>
<td>1.24</td>
<td>Fixed formatting of messages examples</td>
<td>OBX message section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/02/05</td>
<td>1.25</td>
<td>Updated ORC-2/3 and OBR-2/3 with namespace and universal id.</td>
<td>OBR and OBX message section and message examples</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/09/05</td>
<td>1.26</td>
<td><p>Added ORC-21/22 to ORC segment.</p>
<p>Added additional codes to HL7 table 0356.</p>
<p>Updated NTE-4 field in NTE segment.</p>
<p>Specified SNOMED as the alternate code system for OBR-15.1 Specimen Source</p></td>
<td>OBR, OBX and NTE message section and message examples</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/06/05</td>
<td>1.27</td>
<td>Updated OBR-12</td>
<td>OBR section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/22/05</td>
<td>1.28</td>
<td>Updated OBX-3 to CNE data type to indicate code system version id.</td>
<td>OBX section and message examples</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/29/05</td>
<td>1.28</td>
<td><p>Added ORD-17</p>
<p>Updated OBX table, OBX-7 R/O/C changed to RE</p></td>
<td>ORC section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/19/05</td>
<td>1.29</td>
<td>Added OBR-19</td>
<td>OBR section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/23/05</td>
<td>1.30</td>
<td><p>Updated ORC-12 to repeating, ORC-22</p>
<p>Updated OBR-15</p></td>
<td><p>ORC section</p>
<p>OBR section</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/14/06</td>
<td>1.30</td>
<td><p>Added ORC-13</p>
<p>Added OBX-4</p></td>
<td><p>ORC section</p>
<p>OBX section</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/30/06</td>
<td>1.31</td>
<td><p>Updated MSH</p>
<p>Updated MSA</p>
<p>Updated OBR-2/3 and OBR-2/3</p></td>
<td><p>MSH section</p>
<p>MSA section</p>
<p>ORC/OBR section</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/17/07</td>
<td>1.32</td>
<td><p>Updated/corrected Lab protocols</p>
<p>Updated message flow diagram</p>
<p>Updated statement of intent</p>
<p>Updated communications protocol</p>
<p>Updated Message acknowledgment Table 0008</p>
<p>Updated Message Header</p>
<p>Updated specimen source</p>
<p>Updated Observation Identifier and added OBX-23/OBX-24</p>
<p>Updated PID/PV1 Segment</p></td>
<td><p>Event and Subscriber Protocols section</p>
<p>Communications Requirements for HL7 Interfaces section</p>
<p>Overview section</p>
<p>General specification section</p>
<p>Segments section</p>
<p>MSH section</p>
<p>Observation Request section</p>
<p>Observation section</p>
<p>PID and PV1 sections</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>6/20/2007</td>
<td>1.33</td>
<td><p>Updated ORC-12/OBR-16 sections with NPI/VPID info</p>
<p>Updated MSA/NTE/ORC/OBR/OBX tables with VA optionality</p>
<p>Updated OBR-32, OBR-33, OBR-34 and OBR-35</p>
<p>Added usage columns to tables 0078, 0085</p>
<p>Add OBX-19</p>
<p>Add OBR-21</p></td>
<td><p>ORC and OBR sections</p>
<p>MSA/NTE/ORC/OBR/OBX sections</p>
<p>OBR section</p>
<p>OBX section</p>
<p>OBX section</p>
<p>OBR section</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/10/2007</td>
<td>1.33</td>
<td>Added OBR-25</td>
<td>OBR section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/03/2008</td>
<td>1.34</td>
<td><p>Added OBR-44</p>
<p>Added OBX-25</p></td>
<td><p>OBR section</p>
<p>OBX section</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/26/2008</td>
<td>1.35</td>
<td><p>Updated microbiology table</p>
<p>Updated OBR-10,11,14, 26, 29</p>
<p>Updated ORC-13, 21, 22</p>
<p>Updated OBX-18, 24</p></td>
<td><p>Specific Message Consideration section</p>
<p>OBR section</p>
<p>ORC section</p>
<p>OBX section</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2009</td>
<td>1.36</td>
<td><p>Reformat and update to OED Documentation Standards</p>
<p>Updated the result messages examples</p></td>
<td>Entire document</td>
<td><p>CBeynon</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>December 2009</td>
<td>1.36</td>
<td>Changed dates to December 2009</td>
<td></td>
<td>CBeynon</td>
</tr>
<tr class="even">
<td>January 2010</td>
<td></td>
<td>Changed dates to Month 2010</td>
<td></td>
<td>CBeynon</td>
</tr>
<tr class="odd">
<td>March 2010</td>
<td></td>
<td>Changed dates to May 2010 and fixed numbering</td>
<td></td>
<td>CBeynon</td>
</tr>
<tr class="even">
<td>April 2010</td>
<td></td>
<td><p>Added updates provided by HDR</p>
<p>Added updates from <mark>REDACTED</mark></p></td>
<td></td>
<td>CBeynon</td>
</tr>
<tr class="odd">
<td>June 2010</td>
<td></td>
<td><p>Changed dates from May 2010 to July 2010 for release</p>
<p>Added updates from HDR</p></td>
<td></td>
<td>CBeynon</td>
</tr>
</tbody>
</table>

Table of Contents

# # Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Statement of Intent](#statement-of-intent)
  - [Scope](#scope)
  - [Overview of HL7 Terminology](#overview-of-hl7-terminology)
    - [Communication Protocol](#communication-protocol)
    - [Application Processing Rules](#application-processing-rules)
    - [Messages](#messages)
    - [Segments](#segments)
    - [Fields](#fields)
    - [Data Type](#data-type)
  - [References](#references)
- [HL7 Segments in ACK and ORU Messages](#hl7-segments-in-ack-and-oru-messages)
  - [MSA Segment – Message Acknowledgment](#msa-segment-message-acknowledgment)
    - [MSA Field Definitions](#msa-field-definitions)
  - [MSH Segment – Message Header](#msh-segment-message-header)
    - [MSH Field Definitions](#msh-field-definitions)
  - [NTE Segment – Laboratory Notes and Comments](#nte-segment-laboratory-notes-and-comments)
    - [NTE Field Definitions](#nte-field-definitions)
  - [OBR Segment – Observation Request](#obr-segment-observation-request)
    - [OBR Field Definitions](#obr-field-definitions)
  - [OBX Segment - Observation](#obx-segment-observation)
    - [OBX Field Definitions](#obx-field-definitions)
  - [ORC Segment – Common Order](#orc-segment-common-order)
    - [ORC Field Definitions](#orc-field-definitions)
  - [PID Segment – Patient Identification](#pid-segment-patient-identification)
  - [PV1 Segment – Patient Visit](#pv1-segment-patient-visit)
- [Transaction Specifications](#transaction-specifications)
  - [General](#general)
  - [Event and Subscriber Protocols](#event-and-subscriber-protocols)
  - [Activate Message Generation and Transmission](#activate-message-generation-and-transmission)
  - [Inactivate Message Generation and Transmission](#inactivate-message-generation-and-transmission)
  - [Specific Message Consideration](#specific-message-consideration)
    - [Anatomic Pathology Results](#anatomic-pathology-results)
    - [Microbiology Results](#microbiology-results)
    - [Bacteriology Results](#bacteriology-results)
    - [Surgical Pathology Results](#surgical-pathology-results)
    - [Cytopathology Results](#cytopathology-results)
    - [Electron Microscopy Results](#electron-microscopy-results)
  - [Specific Transactions](#specific-transactions)
    - [Result Message](#result-message)
    - [Message Acknowledgment](#message-acknowledgment)
- [Communication Requirements for HL7 Interfaces](#communication-requirements-for-hl7-interfaces)
  - [Using TCP/IP and HL7 Minimal Lower Level Protocol](#using-tcpip-and-hl7-minimal-lower-level-protocol)
    - [Requirements](#requirements)
    - [TCP/IP Connections](#tcpip-connections)
    - [Flow Control](#flow-control)
    - [VistA Client/Server Process Parameters](#vista-clientserver-process-parameters)
    - [Automated Recovery Procedure](#automated-recovery-procedure)
    - [Message Transmission Retry Attempts](#message-transmission-retry-attempts)
    - [Error Management](#error-management)
This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard. This interface forms the basis for the exchange of healthcare information between the VistA Laboratory software application and the VA Health Data Repository (HDR) and Commercial Off the Shelf (COTS) subscribers to VistA Laboratory HL7 result (ORU) messages. The interface is a *broadcast* type interface in which VistA Laboratory automatically notifies subscribers (receiving applications) of available Laboratory test results. The following result types are supported:
| VistA Laboratory Subscript | Traditional Functional Sections                                |
|----------------------------|----------------------------------------------------------------|
| CH                         | Chemistry, Hematology, Coagulation, Serology, Urinalysis, etc. |
| MI                         | Microbiology, Virology, Mycology, Parasitology                 |
| SP                         | Surgical Pathology                                             |
| CY                         | Cytopathology                                                  |
| EM                         | Electron Microscopy                                            |

## Statement of Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of Information developed and implemented a generic interface to the HL7 Standard for use by the VistA Laboratory application in communicating with non-VistA systems to exchange healthcare information. The interface strictly adheres to the HL7 Standard and avoids using “Z” type extensions to the Standard. This interface specification is subject to modification and revision to incorporate changes, improvements, and enhancements. Later versions may support additional functionality of the current HL7 V 2.4 Standard and new functionality released in future versions of the HL7 Standard. In some cases, data types are pre-adopted from other versions of the HL7 standard when they are more appropriate to convey required information.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the HL7 messages (ORU and ACK) transmitted from the VistA Laboratory application system. The purpose of these messages is to exchange information concerning laboratory test results, specifically for test order and reports.

## Overview of HL7 Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sections 1.1.1 through 1.1.6 define the terms and concepts used throughout this Interface Specification.

### Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard defines only the seventh level of the Open System Inter-connect (OSI) protocol. This is the application level. Levels 1-6 involve primarily communication protocols. The HL7 Standard provides some guidance in this area. The communication Standard used for interfacing with the VistA Laboratory package is based on the HL7 Minimal Lower Level (MLLP) Standard as described in the HL7 Interface Standard document.

### Application Processing Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard describes the basic rules for application processing by the exchange of sending and receiving messages between systems. Information contained in the Standard is not repeated here. Interfacing with the VistA Laboratory package requires familiarization with the HL7 Standard V. 2.4.

HL7 distinguishes between two methods of update:

1.  snapshot mode
2.  action code/unique identifier mode

Both modes apply to repeating segments and repeating segment groups. For repeating fields, only snapshot processing applies. For the purpose of this specification, only snapshot processing is supported for segments, segment groups, and fields.

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message is the unit of data transferred between systems. It comprises a group of segments in a defined sequence. Each message has a message type that defines its purpose. A three-character code contained within each message identifies its type. The event that initiates an exchange of messages is called a trigger event. VistA Laboratory uses two HL7 messages.

| ACK | General Acknowledgment            |
|-----|-----------------------------------|
| ORU | Observational Results Unsolicited |

### Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or may be allowed to repeat. Each segment has a name and is identified by a unique three-character code known as the Segment ID.

Example

The ORU message contains segments: Message Header (MSH), Patient ID (PID), Observation Request (OBR), and Observation Segment (OBX).

The following HL7 segments support the transmission of Laboratory information. For details and examples of all segments used to interface with the VistA Laboratory software application, refer to Section 3 Transaction Specifications.

| MSA | Message Acknowledgment |
|-----|------------------------|
| MSH | Message Header         |
| NTE | Notes and Comment      |
| OBR | Observation Request    |
| OBX | Observation            |
| ORC | Common Order           |
| PID | Patient Identification |
| PV1 | Patient Visit          |

Segment tables define the fields and properties of each HL7 segment throughout this document. The following terms are used in the headings of the segment tables.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>Sequence Number is the ordinal position of the data field within the segment. This number refers to the data field in the comments text that follows the segment definition table.</td>
</tr>
<tr class="even">
<td>LEN</td>
<td>Length is the maximum number of characters that one occurrence of the data field may occupy.</td>
</tr>
<tr class="odd">
<td>DT</td>
<td>Data Type identifies the restrictions on the contents of the data field as defined by the HL7 Standard.</td>
</tr>
<tr class="even">
<td>R/O/C</td>
<td><p>R/O/C indicates whether the data field is required, optional, or conditional in a segment.</p>
<p><strong>R</strong>–required<br />
<strong>O</strong> (null)–optional<br />
<strong>X</strong>–not used with the trigger event<br />
<strong>C</strong>–conditional on the trigger event</p></td>
</tr>
<tr class="odd">
<td>VA R/O/C</td>
<td><p>VA (R/O/C) indicates whether the data field is required, optional, or conditional in a segment used by the Department of Veterans Affairs (VA).</p>
<p><strong>R</strong>–required</p>
<p><strong>RE</strong>–required or empty<br />
<strong>O</strong> (null)–optional<br />
<strong>X</strong>–not used with the trigger event<br />
<strong>C</strong>–conditional on the trigger event</p></td>
</tr>
<tr class="even">
<td>RP/#</td>
<td><p>Repetition indicates the number of times you can repeat a field.</p>
<p><strong>N (null)</strong>–no repetition allowed</p>
<p><strong>Y</strong>–the field may repeat an indefinite or site determined number of times</p>
<p><strong>(integer)</strong>–you can repeat the field the number of times specified by the integer</p></td>
</tr>
<tr class="odd">
<td>TBL#</td>
<td>Table attribute of the data field defined by the HL7 standard (for a set of coded values) or negotiated between the VistA Laboratory application and the vendor system. Local tables used by the VA begin with the prefix <strong>99VA</strong>.</td>
</tr>
<tr class="even">
<td>Element Name</td>
<td>Globally unique, descriptive name for the field</td>
</tr>
</tbody>
</table>

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. The HL7 Messaging Standard does not specify how systems must store data within an application. Fields are transmitted as character strings.

### Data Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data type identifies the restrictions on the contents of a data field. HL7 defines a number of data types. This information is in a column labeled DT in the segment attribute tables from the HL7 Messaging Standards.

| Data Type                    | Data Type Name                                                                       |
|------------------------------|--------------------------------------------------------------------------------------|
| AD                           | Address                                                                              |
| CD                           | Channel definition                                                                   |
| CE                           | Coded element                                                                        |
| CF                           | Coded element with formatted values                                                  |
| CK                           | Composite ID with check digit                                                        |
| CM                           | Composite                                                                            |
| CN                           | Composite ID number and name                                                         |
| CNE                          | Coded with no exceptions                                                             |
| CP                           | Composite price                                                                      |
| CQ                           | Composite quantity with units                                                        |
| CWE                          | Coded with exceptions                                                                |
| CX                           | Extended composite ID with check digit                                               |
| DLN                          | Driver's license number                                                              |
| DR                           | Date/time range                                                                      |
| DT                           | Date                                                                                 |
| ED                           | Encapsulated data                                                                    |
| EI                           | Entity identifier                                                                    |
| FC                           | Financial class                                                                      |
| FN                           | Family name                                                                          |
| FT                           | Formatted text                                                                       |
| HD                           | Hierarchic designator                                                                |
| ID                           | Coded values for HL7 tables                                                          |
| IS                           | Coded value for user-defined tables                                                  |
| JCC                          | Job code/class                                                                       |
| MA                           | Multiplexed array                                                                    |
| MO                           | Money                                                                                |
| NA                           | Numeric array                                                                        |
| NM                           | Numeric                                                                              |
| PL                           | Person location                                                                      |
| PN                           | Person name                                                                          |
| PPN                          | Performing person time stamp                                                         |
| PT                           | Processing type                                                                      |
| QIP                          | Query input parameter list                                                           |
| QSC                          | Query selection criteria                                                             |
| RCD                          | Row column definition                                                                |
| RI                           | Repeat interval                                                                      |
| RP                           | Reference pointer                                                                    |
| SAD                          | Street Address                                                                       |
| SCV                          | Scheduling class value pair                                                          |
| SI                           | Sequence ID                                                                          |
| SN                           | Structured numeric                                                                   |
| SRT                          | Sort order                                                                           |
| ST                           | String                                                                               |
| TM                           | Time                                                                                 |
| TN                           | Telephone number                                                                     |
| TQ                           | Timing/quantity                                                                      |
| TS                           | Time stamp                                                                           |
| <span class="mark">XX</span> | Text data                                                                            |
| VH                           | Visiting hours                                                                       |
| VID                          | Version identifier                                                                   |
| XAD                          | Extended address                                                                     |
| XCN                          | Extended composite ID number and name                                                |
| XON                          | Extended composite name and ID number for organizations                              |
| XPN                          | Extended person name                                                                 |
| XTN                          | Extended telecommunications number                                                   |
| A                            | Active                                                                               |
| I                            | Inactive                                                                             |
| L                            | Inactive - Lost to follow-up (cancel contract)                                       |
| M                            | Inactive - Moved or gone elsewhere (cancel contract)                                 |
| O                            | Other                                                                                |
| P                            | Inactive - Permanently inactive (Do not reactivate or add new entries to the record) |

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Messaging Standard version 2.4, American National Standards Institute, 2000  
  [HL7 Messaging Standard](https://www.hl7.org/library/bookstore/)
- VistA HL7 Technical Documentation  
  <http://vista.med.va.gov/messaging/msgadmin/HL7documentation.asp>
- Messaging & Interface Services (M&IS)  
  <http://vista.med.va.gov/messaging/plannerfaqs.asp>
- VHA Software Document Library (VDL), Laboratory Electronic Data Interchange (LEDI), Clinical Section Version 5.2  
  <http://www.va.gov/vdl/application.asp?appid=75>
- HL7 Documents and Presentations <http://www.hl7.org/lib_admin/docs.cfm?dir=library/committees/conf&comm=conf>

# HL7 Segments in ACK and ORU Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 segment fields support the transmission of laboratory test results in ACK and ORU messages.

## MSA Segment – Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSA segment contains information sent in response to receiving a message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL \# | Element Name        |
|-----|-----|-----|-------|----------|-----|--------|---------------------|
| 1   | 2   | ID  | R     | R        |     | 8      | Acknowledgment Code |
| 2   | 20  | ST  | R     | R        |     |        | Message Control ID  |
| 3   | 80  | ST  |       | C        |     |        | Text Message        |

### MSA Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Acknowledgment Code (ID) 

Acknowledgment Code can have the following values:

HL7 Table 0008 Acknowledgment Code

| Value | Description                                         | VA Usage |
|-------|-----------------------------------------------------|----------|
| AA    | Application Accept                                  | Not used |
| AE    | Application Error                                   | Not used |
| AR    | Application Reject                                  | Not used |
| CA    | Enhanced mode: Accept acknowledgment: Commit Accept | Used     |
| CE    | Enhanced mode: Accept acknowledgment: Commit Error  | Used     |
| CR    | Enhanced mode: Accept acknowledgment: Commit Reject | Used     |

#### Message Control ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the appropriate message.

#### Text Message (ST)

This optional text field describes an error condition. The text can be printed in error logs or presented to end-users.

## MSH Segment – Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL \# | Element Name                    |
|-----|-----|-----|-------|----------|-----|--------|---------------------------------|
| 1   | 1   | ST  | R     | R        |     |        | Field Separator                 |
| 2   | 4   | ST  | R     | R        |     |        | Encoding Characters             |
| 3   | 15  | HD  | O     | R        |     |        | Sending Application             |
| 4   | 20  | HD  | O     | R        |     |        | Sending Facility                |
| 5   | 30  | HD  | O     | R        |     |        | Receiving Application           |
| 6   | 30  | HD  | O     | R        |     |        | Receiving Facility              |
| 7   | 26  | TS  | R     | R        |     |        | Date/Time Of Message            |
| 8   | 40  | ST  | O     | X        |     |        | Security                        |
| 9   | 7   | CM  | R     | R        |     | 76     | Message Type                    |
| 10  | 20  | ST  | R     | R        |     |        | Message Control ID              |
| 11  | 1   | PT  | R     | R        |     | 103    | Processing ID                   |
| 12  | 8   | VID | R     | R        |     | 104    | Version ID                      |
| 15  | 2   | ID  | O     | R        |     | 155    | Accept Acknowledgment Type      |
| 16  | 2   | ID  | O     | X        |     | 155    | Application Acknowledgment Type |

### MSH Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The segment terminator is always a carriage return (in ASCII, a hex 0D).

The other delimiters are defined in the MSH segment, with the field delimiter in the fourth character position, and the other delimiters occurring as in the field called Encoding Characters, which is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the entire message.

#### Field Separator (ST)

This field is the separator between the segment ID and the first real field, MSH-2-encoding characters. It serves as the separator and defines the character to be used as a separator for the rest of the message.

VistA Laboratory does not have pre-defined field separators. Applications are advised to use the value of this field to determine the field separator used throughout the message.

#### Encoding Characters (ST)

This field is four characters in the following order: component separator, repetition separator, escape character, and subcomponent separator.

VistA Laboratory does not have pre-defined encoding characters. Applications are advised to use the value of this field to determine the encoding characters used throughout the message.

#### Sending Application (HD)

This field interfaces with lower level protocols.

LA7LAB identifies VistA Laboratory.

#### Sending Facility (HD)

This field addresses one of several occurrences of the same application within the sending system. This field is the three-digit number identifying the medical center division, as found in the VistA INSTITUTION file (#4), Station Number field (#99). The actual facility name is entered into this field by the VistA HL package when addressing the message to each subscriber. It is in the form of a DNS type value and reflects the domain name associated with the VA facility.

#### Receiving Application (HD) 

Refer to sending application. The actual subscriber’s application name is entered into this field by the VistA HL package when addressing the message to each subscriber. For messages addressed to the VA Health Data Repository (HDR) the value is LA7HDR.

#### Receiving Facility (HD)

Refer to sending facility. The actual subscriber’s facility name is entered into this field by the VistA HL package when addressing the message to each subscriber.

#### Date/Time of Message (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

#### Security (ST)

In some applications of HL7, this field implements security features. Its use is not yet specified.

#### Message Type (CM)

Message Type is a composite element made up of the following:

\<message type\> \<trigger event\> \<message structure\>

- The first component is the message type, found in Table 76 - Message Type.
- The second component is the trigger event code found in Table 3 - Event Type Code.
- The third component is the abstract message structure code defined by HL7 Table 0354 - Message Structure.

The receiving system uses this field to know the data segments to recognize, and possibly the application to which to route this message.

#### Message Control ID (ST)

This field is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA) of the accept (commit) acknowledgment message (ACK).

#### Processing ID (ID)

This field determines whether to process the message as defined in the HL7 application processing rules.

HL7 Table 0103 Processing ID

| Value | Description |
|-------|-------------|
| D     | Debugging   |
| P     | Production  |
| T     | Training    |

#### Version ID (ID)

This field is matched by the receiving system to its own version to be sure the message is interpreted correctly.

HL7 Table 0104 Version ID

| Value | Description                |
|-------|----------------------------|
| 2.1   | Released 2.1 March 1990    |
| 2.2   | Released 2.2 December 1994 |
| 2.3   | Released 2.3 May 1997      |
| 2.3.1 | Released 2.3.1 May 1999    |
| 2.4   | Released 2.4 November 2000 |

> **NOTE:** Lab HDR requires V. 2.4

#### Accept Acknowledgment Type (ID)

This field defines the conditions under which accept acknowledgments must be returned in response to this message.

HL7 Table 0155 Accept/Application Acknowledgment Conditions

| Value | Description                  |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

> **NOTE:** VistA Laboratory specifies a value of AL for this field.

#### Application Acknowledgment Type (ID)

This field defines the conditions under which application acknowledgments are required in response to this message.

HL7 Table 155 Accept/Application Acknowledgment Conditions

| Value | Description                  |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

> **NOTE:** VistA Laboratory specifies a value of NE for this field.

## NTE Segment – Laboratory Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NTE segment reports the Laboratory notes or comments.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL \# | Element Name                |
|-----|-----|-----|-------|----------|-----|--------|-----------------------------|
| 1   | 4   | SI  | O     | R        |     |        | Set ID - Notes And Comments |
| 2   | 8   | ID  | O     | R        |     | 0105   | Source Of Comment           |
| 3   | 64k | FT  | O     | R        | Y   |        | Comment                     |
| 4   | 250 | CE  | O     | R        |     | 0364   | Comment Type                |

### NTE Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Set ID - Notes and Comments (SI)

This field is used where multiple NTE segments are included in a message.

#### Source of Comment (ID)

VistA Laboratory encodes this field with L for Lab Result (ORU) messages.

#### Comment (FT)

This field contains the comment associated with the specimen and/or a specific test.

#### Comment Type (CE)

This field contains the comment type.

- VA user-defined entries (VA-LR\*) indicate the type of comments and their source within a VistA Laboratory report.
- Entries (VA-LRMI\*) indicate Microbiology (MI-subscript) report comments.
- This field is valued when a microbiology report (MI subscript) contains comments that follow an OBR segment and describe the nature of the microbiology comment.

User-defined Table 0364 - Comment type

| Value      | Description                          | Comment                               |
|------------|--------------------------------------|---------------------------------------|
| PI         | Patient Instructions                 |                                       |
| AI         | Ancillary Instructions               |                                       |
| GI         | General Instructions                 |                                       |
| 1R         | Primary Reason                       |                                       |
| 2R         | Secondary Reason                     |                                       |
| GR         | General Reason                       |                                       |
| RE         | Remark                               |                                       |
| DR         | Duplicate/Interaction Reason         |                                       |
| VA-LR001   | Order Comment                        | Laboratory order comment              |
| VA-LR002   | Result Comment                       | Laboratory result comment             |
| VA-LR003   | Result Interpretation                | Laboratory test result interpretation |
| VA-LRMI001 | Comment on Specimen (#. 99)          | Lab microbiology comment              |
| VA-LRMI010 | Bact Rpt Remark (#13)                | Lab microbiology comment              |
| VA-LRMI011 | Preliminary Bact Comment (#1)        | Lab microbiology comment              |
| VA-LRMI012 | Bacteriology Test(s) (#1.5)          | Lab microbiology comment              |
| VA-LRMI013 | Bacteriology Smear/Prep (#11.7)      | Lab microbiology comment              |
| VA-LRMI020 | Parasite Rpt Remark (#17)            | Lab microbiology comment              |
| VA-LRMI021 | Preliminary Parasite Comment (#16.5) | Lab microbiology comment              |
| VA-LRMI022 | Parasite Test(s) (16.4)              | Lab microbiology comment              |
| VA-LRMI023 | Parasitology Smear/Prep (#15.51)     | Lab microbiology comment              |
| VA-LRMI030 | Mycology RPT Remark (#21)            | Lab microbiology comment              |
| VA-LRMI031 | Preliminary Mycology Comment (#20.5) | Lab microbiology comment              |
| VA-LRMI032 | Mycology Test(s) (#20.4)             | Lab microbiology comment              |
| VA-LRMI033 | Mycology Smear/Prep (#19.6)          | Lab microbiology comment              |
| VA-LRMI040 | TB Rpt Remark (#27)                  | Lab microbiology comment              |
| VA-LRMI041 | Preliminary TB Comment (#26.5)       | Lab microbiology comment              |
| VA-LRMI042 | TB Test(s) (#26.4)                   | Lab microbiology comment              |
| VA-LRMI050 | Virology Rpt Remark (#37)            | Lab microbiology comment              |
| VA-LRMI051 | Preliminary Virology Comment (#36.5) | Lab microbiology comment              |
| VA-LRMI052 | Virology Test (#36.4)                | Lab microbiology comment              |

## OBR Segment – Observation Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the reporting of clinical data, the OBR serves as the report header. The OBR segment identifies the observation set represented by the following observations.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL \# | Element Name                  |
|-----|-----|-----|-------|----------|-----|--------|-------------------------------|
| 1   | 4   | SI  | C     | R        |     |        | Set ID - Observation Request  |
| 2   | 22  | EI  | C     | C        |     |        | Placer Order Number           |
| 3   | 22  | EI  | C     | R        |     |        | Filler Order Number           |
| 4   | 250 | CE  | R     | R        |     |        | Universal Service ID          |
| 7   | 26  | TS  | C     | R        |     |        | Observation Date/Time         |
| 11  | 1   | ID  | O     | C        |     |        | Specimen Action Code          |
| 12  | 60  | CE  | O     | C        |     |        | Danger Code                   |
| 14  | 26  | TS  | C     | R        |     |        | Specimen Received Date/Time   |
| 15  | 300 | CM  | O     | R        |     | 0070   | Specimen Source               |
| 16  | 60  | XCN | O     | R        | Y   |        | Ordering Provider             |
| 19  | 60  | ST  | O     | R        |     |        | Placer Field \#2              |
| 20  | 60  | ST  | O     | R        |     |        | Filler Field \#1              |
| 21  | 60  | ST  | O     | R        |     |        | Filler Field \#2              |
| 22  | 26  | TS  | O     | R        |     |        | Results Rpt/Status Chng - D/T |
| 24  | 10  | ID  | O     | R        |     | 0074   | Diagnostic Serv Sect ID       |
| 25  | 1   | ID  | C     | RE       |     | 0123   | Result Status                 |
| 26  | 200 | CM  | O     | RE       |     |        | Parent Result                 |
| 29  | 200 | CM  | O     | RE       |     |        | Parent                        |
| 32  | 200 | CM  | 0     | C        |     |        | Principle Result Interpreter  |
| 33  | 200 | CM  | O     | C        | Y   |        | Assistant Result Interpreter  |
| 34  | 200 | CM  | O     | C        | Y   |        | Technician                    |
| 35  | 200 | CM  | O     | C        | Y   |        | Transcriptionist              |
| 44  | 250 | CE  | O     | RE       |     | 0088   | Procedure Code                |

### OBR Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Set ID - Observation Request (SI)

This field is a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

#### Placer Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier\> \<namespace ID\>\<universal ID\>\<Universal ID Type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the placer. Currently the first component is valued with the VistA Lab Unique Identifier (UID) or the human readable accession. This identifier is returned with the results. The VistA Lab UID is a ten-character alpha/numeric identifier. The accession is constructed from the associated accession area abbreviation, concatenated with the abbreviated accession date, concatenated with the accession number.

For entity identifier

- For CH subscript tests, the UID field (#.31) within the Chem, Hem, Tox, Ria, Ser, etc. subfile (#4) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the ACCESSION field (#.06) within the Chem, Hem, Tox, Ria, Ser, etc. subfile (#4) of the VistA LAB DATA file (#63) is transmitted.

- For MI subscript tests, the UID field (#.31) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the MICROBIOLOGY ACCESSION field (#.06) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63) is transmitted.

- For SP subscript tests, the SURGICAL PATH ACC \# field (#.06) within the Surgical Pathology subfile (#8) of the VistA LAB DATA file (#63)
- For CY subscript tests, the CYTOPATH ACC \# field (#.06) within the Cytopathology subfile (#63.09) of the VistA LAB DATA (#63)
- For EM subscript test, the EM ACC \# field (#.06) within the Electron Microscopy subfile (#62.02) of the VistA LAB DATA file (#63)
- For Point of Care (POC) testing when the POC system transmitted an order number

For namespace ID

- LR – for VistA Laboratory related tests
- LRPOC – for VistA Laboratory Point of Care related tests

For universal ID

The institution related to the order in the form of a VistA HL7 standard DNS reference.

For universal ID type

DNS

Example

\|1073100001~LR~TEST.DEVELOPEMNT.MED.VA.GOV~DNS\|

#### Filler Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier\> \<namespace ID\> \<universal ID\>\<Universal ID Type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the filler. Currently the first component is valued with the VistA Lab Unique Identifier (UID) or accession. This identifier is returned with the results. The VistA Lab UID is a ten-character alpha/numeric identifier. The accession is constructed from the associated accession area abbreviation, concatenated with the abbreviated accession date, concatenated with the accession number

For entity identifier

- For CH subscript tests, the UID field (#.31) within the Chem, Hem, Tox, Ria, Ser, etc. subfile (#4) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the ACCESSION field (#.06) within the Chem, Hem, Tox, Ria, Ser, etc. subfile (#4) of the VistA LAB DATA file (#63) is transmitted.

- For MI subscript tests, the UID field (#.31) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the MICROBIOLOGY ACCESSION field (#.06) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63) is transmitted.

- For SP subscript tests, the SURGICAL PATH ACC \# field (#.06) within the Surgical Pathology subfile (#8) of the VistA LAB DATA file (#63)
- For CY subscript tests , the CYTOPATH ACC \# field (#.06) within the Cytopathology subfile (#63.09) of the VistA LAB DATA (#63)
- For EM subscript test, the EM ACC \# field (#.06) within the Electron Microscopy subfile (#62.02) of the VistA LAB DATA (#63)

For namespace ID

LR – for VistA Laboratory related tests

For universal ID

The institution related to the order in the form of a VistA HL package standard DNS reference.

For universal ID type

DNS

#### Universal Service ID (CE)

This field is a coded element made up of the following:

\<identifier\> \<text\> \<name of coding system\> \<alternate identifier\> \<alternate text\> \<name of alternate coding system\>

This field is an identifier code for the observation or ordered test. This can be based on local and/or universal codes.

The WKLD CODE file (#64) is used to identify the observed test and will be the value of the universal service id. It contains the VA National Laboratory Test code. Future versions may utilize LOINC codes as an additional coding system. The alternate code is the local test name from LABORATORY TEST file (#60).

\<NLT code File \#64 Field \#1\>^\<text\>^\<99VA64\>^\<File \#60 internal entry number\>^\<File \#60, NAME field (#.01)\>^\<99VA60\>

#### Observation Date/Time (TS)

This field is the clinically relevant date/time of the observation. This is the date and time of the specimen collection. Value for this field is derived from Date/Time Specimen Taken field (#.01) within VistA LAB DATA file (#63).

| Subscript | Subfile | Field                           |
|-----------|---------|---------------------------------|
| CH        | 63.04   | Date/Time Specimen Taken (#.01) |
| CY        | 63.09   | Date/Time Specimen Taken (#.01) |
| EM        | 63.02   | Date/Time Specimen Taken (#.01) |
| MI        | 63.05   | Date/Time Specimen Taken (#.01) |
| SP        | 63.08   | Date/Time Specimen Taken (#.01) |

#### OBR-11 Specimen Action Code (ID)

This field identifies the action to take with respect to the specimens that accompany or precede this order. The purpose of this field is to further qualify (when appropriate) the general action indicated by the order control code contained in the accompanying ORC segment.

Example

When a new order (ORC - “NW”) is sent to the lab, this field tells the lab whether or not to collect the specimen (“L” or “O”). Refer to HL7 Table 0065 - Specimen action code for valid values.

HL7 Table 0065 - Specimen action code

| Value | Description                                    |
|-------|------------------------------------------------|
| A     | Add ordered tests to the existing specimen     |
| G     | Generated order; reflex order                  |
| L     | Lab to obtain specimen from patient            |
| O     | Specimen obtained by service other than Lab    |
| P     | Pending specimen; Order sent prior to delivery |
| R     | Revised order                                  |
| S     | Schedule the tests specified below             |

Currently VistA Laboratory does not value this field. A subsequent VistA Laboratory patch will record this information with laboratory results at which time this field will be valued when available.

#### Danger Code (CE)

This field contains the code and/or text indicating any known or suspected patient or specimen hazards, e.g., patient with active tuberculosis or blood from a hepatitis patient. Either code and/or text may be absent. However, the code is always placed in the first component position and any free text in the second component position. Free text without a code must be preceded by a component delimiter.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The Danger Code contains the information located within the LAB DATA file (#63) Pat. Info. field (#.091). VistA does not code this information. It is transmitted as text and occurs in the second component of this field.

#### Specimen Received Date/Time (TS)

This field is the actual time of arrival of a specimen at the diagnostic service. Depending on the nature of the test, the value for this field is derived from the following fields within VistA LAB DATA file (#63).

| Subscript | Subfile | Field                             |
|-----------|---------|-----------------------------------|
| CH        | 63.04   | Date/Time Specimen Taken (#.01)   |
| CY        | 63.09   | Date/Time Specimen Received (#.1) |
| EM        | 63.02   | Date/Time Specimen Received (#.1) |
| MI        | 63.05   | Date/Time Received (#.1)          |
| SP        | 63.08   | Date/Time Specimen Received (#.1) |

For Chemistry/Hematology (CH), VistA Lab attempts to retrieve this value from the LAB ARRIVAL TIME (#12) within the Accession Number subfile (#68.02), within the Date subfile (#68.01) of the VistA Accession file (#68). If no value is found, the Date/Time Specimen Taken field (#.01), within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#62.04) is reported to maintain compliance with HL7 standard.

#### Specimen Source (CM)

This field contains the information on the specimen source.

Components

\<specimen source name or code\>^\<additives\>^\<freetext\>^\<body site\>^\<site modifier\>^\<collection method modifier code\>

The specimen source component is encoded as a CWE data type and contains nine subcomponents.

> **NOTE:** Use of CWE data type is pre-adopted from HL7 v2.6 to facilitate expression of coding system version and local terms.

\<code from HL7 Table 0070\>&\<text\>&\<HL70070\>^\<SNOMED code\>&\<text\>&\<SNM\>&\<coding system version id&\<alternate coding system version id\>&\<local specimen name\>

> **NOTE:** In a future VistA Laboratory patch, the SNOMED code system will be replaced with the SNOMED CT code system.

The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061) and are placed in the first three subcomponents.

- The first is the VistA TOPOGRAPHY file (#61), which is mapped to the corresponding entry in file \#64.061.
- The second subcomponent text contains the Table 0070 description.
- The third subcomponent contains the HL7 table identifier.
- The fourth through sixth subcomponents contain the corresponding SNOMED code with the text of the topography from VistA TOPOGRAPHY file (#61).
- The eighth component contains the version of the SNOMED code.
- The ninth component contains the name (text) of the related local topography as specified in the table.

| Subscript | Subfile | Field                      |
|-----------|---------|----------------------------|
| CH        | 63.04   | Specimen Type (#.05)       |
| CY        | 63.09   | Specimen Topography (#.06) |
| EM        | 63.02   | Specimen Topography (#.06) |
| MI        | 63.05   | Site/Specimen (#.05)       |
| SP        | 63.08   | Specimen Topography (#.06) |

The body site component (fourth) contains the related collection sample encoded as a CWE data type when the specimen relates to a microbiology (MI subscript) report.

- When the collection sample is mapped to SNOMED CT the first three subcomponents contain the applicable SNOMED CT code with the seventh subcomponent indicating the SNOMED CT version.
- The fourth through sixth components contain the local code based on the VistA Laboratory COLLECTION SAMPLE file (#62).
- The ninth component contains the local name (text) of the related collection sample

Example

257261003&Swab (specimen)&SCT&50&SWAB&99VA62&20060101&&SWAB

#### Ordering Provider (XCN)

This field contains the identity of the person who is responsible for creating the request (i.e., ordering physician).

This field identifies the provider who ordered the test. The ID code and the name may be present. This field is repeated in ORC-12 and contains the same value per the HL7 standards.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & universal ID type (ID)

Subcomponents of assigning facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

ID can be valued with one of three identifiers.

When the provider is assigned a National Provider ID (NPI) the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS. The check digit is transmitted in the identifier check digit (eleventh component). NPI.is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

Example

HL7 delimiters \|^~\\

\|0000000003^LRPROVIDER^ONE^D^^^MD^^USDHHS^^3^NPI^NPI\|

- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA and identifier type code (thirteenth component) contains PN.
- If there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with -VA and the VA station number.

#### Placer Field (#2) (ST)

This field (#2) contains vital information for linking the incoming result with the original order. The data must be passed in the following format:

\<\>^\<\>^\<Accession Area\>^\<Accession Date\>^\<Accession Number\>^\<Accession\>^

\<Universal ID\>^\<Sequence Number\>

All components are optional except the Universal ID, which must match with the Placer Order Number.

> **NOTE:** Data in this field can be encoded using HL7 escape sequences.

#### Filler Field (#1) (ST)

This field (#1) contains information relating to the filler of the results and the reference to the data storage location of the results in VistA LAB DATA file (#63).

The data is structured using the following format:

\<LRDFN (VistA LAB DATA file (#63) internal entry number)\>^\<File \#63 subscript (“CH”, “CY”,“MI”,”SP”,”EM”)\>^\<specimen date/time internal entry number in VistA LAB DATA file (#63\>

> **NOTE:** This field can be HL7 escape encoded when the data conflicts with the HL7 delimiters used to encode the HL7 message.

#### Filler Field (#2) (ST)

This field (#2) contains information relating to the filler of the results and the reference to the accession related to the results in VistA LAB DATA file (#63).

The data is structured using the following format:

LRACC^LRAA^LRAD^LRAN^Accession Area^Area Abbreviation^NLT

Where:

| LRACC             | Human readable accession                                                  |
|-----------------------|---------------------------------------------------------------------------|
| LRAA              | Internal entry number of accession area in ACCESSION file (#68)           |
| LRAD              | FileMan accession date                                                    |
| LRAN              | Accession number                                                          |
| Accession Area    | Accession area name from ACCESSION file (#68) based on LRAA value         |
| Area Abbreviation | Accession area abbreviation from ACCESSION file (#68) based on LRAA value |
| NLT               | Order NLT code of ordered test                                            |

> **NOTE:** This field can be HL7 escape encoded when the data conflicts with the HL7 delimiters used to encode the HL7 message.

#### Results Report/Status Change – Date/Time (TS)

This field contains the date and time the report is released. It is derived from the following fields in VistA LAB DATA file (#63):

| Subscript | Subfile | Field                           |
|-----------|---------|---------------------------------|
| CH        | 63.04   | Date Report Completed (#.03)    |
| CY        | 63.09   | Report Release Date/Time (#.11) |
| EM        | 63.02   | Report Release Date/Time (#.11) |
| MI        | 63.05   | Date Report Completed (#.03)    |
| SP        | 63.08   | Report Release Date/Time (#.11) |

#### Diagnostic Serv Sect ID (ID)

This field contains a reference to the data storage location of the results in VistA LAB DATA file (#63).

The various subscripts are mapped as follows.

HL7 Table 0074 – Diagnostic Serv Sect ID Mapping

| VistA Subscript       | HL7 Table 0074 – Diagnostic Serv Sect ID |
|-----------------------|----------------------------------------------|
| CH                    | CH                                           |
| MI-Micro bacteriology | MB                                           |
| MI-Parasitology       | PAR                                          |
| MI-Mycology           | MYC                                          |
| MI-Mycobacteriology   | MCB                                          |
| MI-Virology           | VR                                           |
| CY                    | CY                                           |
| SP                    | SP                                           |
| EM                    | PAT                                          |
| AU                    | PAT                                          |
| BB                    | BLB                                          |

#### Result Status (ID)

This field is the status of results for this order. This conditional field is required whenever the

OBR is contained in a report message. It is not required as part of an initial order.

This field is the response to an order status query where the level of detail requested does not include the OBX segments. When the individual status of each result is necessary, OBX-11 – Observ Result Status may be used.

For chemistry/hematology, etc. (CH) subscript tests this field is not valued. For status of the individual results, refer to OBX-11 – Observ Result Status.

For microbiology (MI) subscript and anatomic pathology (SP, CY, and EM) subscripts, this field contains the status of the whole report.

HL7 Table 0123 – Result Status

| Value | Description                                                                             | VA Usage |
|-------|-----------------------------------------------------------------------------------------|----------|
| O     | Order received; specimen not yet received                                               | Used     |
| I     | No results available; specimen received, procedure incomplete                           | Used     |
| S     | No results available; procedure scheduled, but not done                                 | Not Used |
| A     | Some, but not all, results available                                                    | Used     |
| P     | Preliminary: A verified early result is available, final results not yet obtained       | Used     |
| C     | Correction to results                                                                   | Used     |
| R     | Results stored; not yet verified                                                        | Not used |
| F     | Final results; results stored and verified. Can only be changed with a corrected result | Used     |
| X     | No results available; Order canceled                                                    | Used     |
| Y     | No order on record for this test (Used only on queries)                                 | Not used |
| Z     | No record of this patient (Used only on queries)                                        | Not used |

#### Parent Result (CM)

This field uniquely identifies the parent result’s OBX segment related to this order.

\<OBX-3-observation identifier of parent result\>^\<OBX-4-sub-ID of parent result\>

If the current battery is an antimicrobial susceptibility, the parent results identified OBX contains a result, which identifies the organism on which the susceptibility was run.

VistA currently only uses this field for microbiology (MI) subscript results when reporting antibiotic susceptibility.

#### Parent (CM)

This field relates a child to its parent when a parent-child relationship exists. Parent is a two-component field. The components of the placer order number and the filler order number are transmitted in subcomponents of this two-component field.

\<parent’s placer order number\>^\<parent’s filler order number\>

Antimicrobial susceptibilities spawned by cultures, need to record the parent (culture) filler order number here.

#### Principle Result Interpreter (CM)

This field identifies the physician or other clinician who interpreted the observation and is responsible for the report content. This information is derived from Pathologist field (# .02) for Surgical Pathology (SP), Cytopathology (CY) and Electron Microscopy (EM) subscripts in LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

> **NOTE:** XCN Replaces CN data type as of v 2.3. XCN data type pre-adopted to convey additional information regarding the type of identifier.

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID and the assigning authority (ninth component) contains USDHHS, the check digit is transmitted in identifier check digit (eleventh component).. NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).
- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (ninth component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (-VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### Assistant Result Interpreter (CM)

This field identifies the clinical observer who assisted in the interpretation of study. This information is derived from RESIDENT PATHOLOGIST field (# .021) for Surgical Pathology (SP); CYTOTECH (# .021) for Cytopathology (CY); and RESIDENT OR EMTECH (# .06) field for Electron Microscopy (EM) subscripts in LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

> **NOTE:** XCN Replaces CN data type as of v 2.3. XCN data type pre-adopted to convey additional information regarding the type of identifier.

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID and the assigning authority (ninth component) contains USDHHS, the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).
- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (9th component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (-VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### Technician (CTM)

This field identifies the performing technician. This information is derived from CYTOTECH field (# .021) for Cytopathology (CY) and RESIDENT OR EMTECH field (# .021) for Electron Microscopy (EM) subscripts in file LAB DATA (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

> **NOTE:** XCN Replaces CN data type as of v 2.3. XCN data type pre-adopted to convey additional information regarding the type of identifier.

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the technician is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (ninth component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### Typist (CM)

This field identifies the report transcriber. This information is derived from TYPIST field (# .09) for Surgical Pathology (SP); CYTOTECH (# .021) for Cytopathology (CY); and RESIDENT OR EMTECH (# .06) for Electron Microscopy (EM) subscripts in file LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

> **NOTE:** XCN Replaces CN data type as of v 2.3. XCN data type pre-adopted to convey additional information regarding the type of identifier.

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the typist is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (ninth component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (-VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### Procedure Code (CE)

This field contains a unique identifier assigned to the procedure, if any, associated with the charge. Refer to User-defined table 0088 - Procedure code for suggested values. This field is a CE data type for compatibility with clinical and ancillary systems

Components

\<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\>

- When the ordered laboratory test has an associated order NLT code, the order NLT and CPT code is reported. The CPT code is reported as the primary code and the NLT code as the alternate.
- When the NLT code is not linked to an associated CPT code, the NLT code is reported as the primary code.

\<CPT code File \#81 Field \#1\>^\<text\>^\<C4 or HCPCS\>^\<NLT code File \#64 Field \#1\>^\<text\>^\<99VA64

or

\<NLT code File \#64 Field \#1\>^\<text\>^\<99VA64

Example

\|84100~ASSAY OF PHOSPHORUS~C4~84100.0000~Phosphate Inorganic~99VA64\|

## OBX Segment - Observation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBX segment transmits a single observation or observation fragment.

| Seq | Len   | DT  | Usage | VA R/O/C | RP/# | TBL# | Element Name                             |
|-----|-------|-----|-------|----------|------|------|------------------------------------------|
| 1   | 4     | SI  | O     | R        |      |      | Set Id – OBX                             |
| 2   | 3     | ID  | C     | C        |      | 0125 | Value Type                               |
| 3   | 250   | CWE | R     | R        |      |      | Observation Identifier                   |
| 4   | 20    | ST  | C     | C        |      |      | Observation Sub-ID                       |
| 5   | 65536 |     | O     | C        |      |      | Observation Value                        |
| 6   | 250   | CE  | O     | C        |      |      | Units                                    |
| 7   | 60    | ST  | O     | R        |      |      | Reference Ranges                         |
| 8   | 5     | IS  | O     | C        |      | 0078 | Abnormal Flags                           |
| 11  | 1     | ID  | R     | R        |      | 0085 | Observ Result Status                     |
| 13  | 20    | ST  | 0     | C        |      |      | User Defined Access Checks               |
| 14  | 26    | TS  | O     | R        |      |      | Date/Time Of The Observation             |
| 15  | 250   | CE  | O     | R        |      |      | Producer’s ID                            |
| 16  | 250   | XCN | O     | R        |      |      | Responsible Observer                     |
| 17  | 250   | CE  | O     | C        |      |      | Observation Method                       |
| 18  | 22    | EI  | O     | C        |      |      | Equipment Instant Identifier             |
| 19  | 26    | TS  | O     | C        |      |      | Date/Time Of Analysis                    |
| 23  | 567   | XON | O     | C        |      |      | Performing Organization Name             |
| 24  | 631   | XAD | O     | C        |      |      | Performing Organization Address          |
| 25  | 3002  | XCN | O     | C        |      |      | Performing Organization Medical Director |

> **NOTE:** OBX-23/OBX-24/OBX-25 were pre-adopted from HL7 v2.5.1 in preparation for conformance with HITSP.

### OBX Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Set ID - Observation Simple (SI)

This field is a sequence number used to identify the segment repetitions.

#### Value Type (ID)

This field is the format of the observation value in OBX.

> HL7 Table 0125 – Value Type

| Value                        | Description              |
|------------------------------|--------------------------|
| CE                           | Coded Entry              |
| CNE                          | Coded with no exceptions |
| CWE                          | Coded with exceptions    |
| FT                           | Formatted Text           |
| NM                           | Numeric                  |
| SN                           | Structured Numeric       |
| ST                           | String Data              |
| <span class="mark">XX</span> | Text                     |

Although there are other entries in the HL7 table, only the above values are transmitted by VistA. It is valued unless OBX-11 is not valued per the HL7 Standard: *It must be valued if OBX-11-Observ result status is not valued with an ‘X’*. If OBX-11 contains “X” and OBX-5 is not valued, OBX-2 is not valued.

#### Observation Identifier (CWE)

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\> ^ \<coding system version ID (ST)\> ^ alternate coding system version ID (ST)\> ^ \<original text (ST)\>

Observation Identifier is a coded element

- When a result is LOINC (Logical Observation Identifiers Names and Codes) encoded, LOINC is the coding system and VUID the alternate coding system. The text for the VUID (Veterans Health Administration (VHA) Unique ID) code is the VA assigned national test display name.
- When no VA display name is associated with the VUID, the field is blank. The local test name is the VistA LABORATORY TEST file (#60), Name field (#.01), when expressing laboratory test results associated with the VistA CH subscript.

\<LOINC CODE\> \<text\> \<LN\> \<VUID CODE\> \<text\> \<99VA95.3\> \<LOINC version \#\> \< VUID version \#\> \<local test name\>

VUID is a unique meaningless integer assigned to reference terms VHA wide.

When a local code is used as either the primary or alternate for chemistry/hematology (“CH”) subscript results, it is encoded as: \<”CH” data name number\<\>data name label\<\>99VA63\>.

This field is a unique identifier for the observation test results.

HL7 delimiters \|^~\\Example

LOINC as primary, VUID as alternate

\|2345-7^GLUCOSE:MCNC:PT:SER/PLAS:QN^LN^4665460^ ^99VA95.3^2.14^2.14^Serum Glucose\|

Example

LOINC code as primary, local code as alternate (no VUID available)

\|2951-2^SODIUM:SCNC:PT:SER/PLAS:QN^LN^CH5^SODIUM^99VA63^2.13^5.2^SODIUM\|

Example

Local code as primary, (no LOINC/VUID available) HL7 delimiters: \|^~\\

\|CH5^SODIUM^99VA63^^^^^5.2^SODIUM\|

For microbiology (MI subscript) and anatomic pathology (SP, CY and EM subscripts) the coding of this field is as specified in section 3.4 of this specification.

#### Observation Sub-ID (ST)

This field distinguishes between multiple OBX segments with the same observation ID organized under one OBR.

VistA for chemistry/hematology type results (CH subscript) values this field with “CH” concatenated with the field number of the field used to store the instance of this result within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63).

VistA uses this field for microbiology results, which contain multiple organisms and antibiotic susceptibilities, anatomic pathology results to distinguish multiple sections of the report, and for general chemistry/hematology/serology, etc. type results to distinguish results using the same observation ID.

#### Observation Value (ST)

This field is the value observed by the observation producer. The length of this field is variable, depending upon the value type.

#### Units (CE)

This field is a coded element.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The default coding system for Units consists of the ISO abbreviations as defined in Section 7.1.4 of the *HL7 Standard V. 2.4*. Currently VistA uses units derived from a local file. These are encoded with coding system L. The text component contains the value of the identifier component.

#### Reference Range (ST)

The field contains the identified range for this specific result.

#### Abnormal Flag (ID)

This field contains the entries identified by table 0078.

HL7 Table 0078 – Value Type

| Value | Description                                                                                   | VA Usage |
|-------|-----------------------------------------------------------------------------------------------|----------|
| L     | Below low normal                                                                              | Used     |
| H     | Above high normal                                                                             | Used     |
| LL    | Below lower panic limits                                                                      | Used     |
| HH    | Above upper panic limits                                                                      | Used     |
| \<    | Below absolute low-off instrument scale                                                       | Not Used |
| \>    | Above absolute high-off instrument scale                                                      | Not Used |
| N     | Normal (applies to non-numeric results)                                                       | Not Used |
| A     | Abnormal (applies to non-numeric results)                                                     | Not Used |
| AA    | Very abnormal (applies to non-numeric results, analogous to panic limits for numeric results) | Not Used |
| Null  | No range defined, or normal ranges don’t apply                                                | Used     |
| U     | Significant change up                                                                         | Not Used |
| D     | Significant change down                                                                       | Not Used |
| B     | Better—use when direction not relevant                                                        | Not Used |
| W     | Worse—use when direction not relevant                                                         | Not Used |
|       | For microbiology susceptibilities only                                                    |          |
| S     | Susceptible                                                                                   | Used     |
| R     | Resistant                                                                                     | Used     |
| I     | Intermediate                                                                                  | Used     |
| MS    | Moderately susceptible                                                                        | Used     |
| VS    | Very susceptible                                                                              | Used     |

#### Observ Result Status (ID)

This field reflects the current completion status of the results for one Observation Identifier.

HL7 Table 0085 – Observation Result Status Codes Interpretation

| Value | Description                                                                                  | VA Usage |
|-------|----------------------------------------------------------------------------------------------|----------|
| C     | Record coming over is a correction and thus replaces a final result                          | Used     |
| D     | Deletes the OBX record                                                                       | Not Used |
| F     | Final results; can only be changed with a corrected result                                   | Used     |
| I     | Specimen in lab; results pending                                                             | Used     |
| N     | Not asked                                                                                    | Not Used |
| O     | Order detail description only (no result)                                                    | Not Used |
| P     | Preliminary results                                                                          | Used     |
| R     | Results entered – not verified                                                               | Not Used |
| S     | Partial results                                                                              | Used     |
| X     | Results cannot be obtained for this observation                                              | Used     |
| U     | Results status change to final without retransmitting results already sent as ‘preliminary’. | Not used |
| W     | Post original as wrong                                                                       | Not Used |

#### User Defined Access Checks

This field permits the producer to record results-dependent codes for classifying the observation at the receiving system.

The VistA system values this field when an antimicrobial susceptibility result is reported and access checks are specified by the reporting facility.

| Value            | VUID    | Description                                                                                                  |
|------------------|---------|--------------------------------------------------------------------------------------------------------------|
| Always Display   | 4500665 | Always display the result                                                                                    |
| Never Display    | 4500805 | Never display the result, unless the user has the LRLAB key that indicates user is laboratory personnel      |
| Restrict Display | 4500877 | Display the result only when the interpretation of all antibiotics, which are always displayed, is resistant |

#### Date/Time of the Observation (TS)

The observation date/time is the physiologically relevant date/time or the closest approximation to that date/time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

#### Producer’s ID (CE)

This field contains the unique identifier of the responsible producing service and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories.

If this field is null, the receiving system assumes the observations are produced by the sending organization. This information supports CLIA regulations in the US. The code for producer ID is recorded as a CE data type. In the US, the Medicare number of the producing service is usually used as the identifier.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The ID number is the station number found in the VistA INSTITUTION file (#4), Station Number field (#99). The text is the value of the Official VA Name field (#100). If this value is null, the value of the Name field (#.01) is used.

The Laboratory CLIA number, when available, is transmitted as the alternate identifier with the name of the coding system, 99VACLIA.

#### Responsible Observer (XCN)

When required, this field contains the identifier of the individual directly responsible for the observation (such as, the person who performed or verified the observation).

- In a nursing service, the observer is usually the professional who performed the observation (such as, took the blood pressure).
- In a laboratory, the observer is the technician who performed or verified the analysis.

The code for the observer is recorded as a CE data type. If the code is sent as a local code, it must be unique and unambiguous when combined with OBX-15-producer ID. When available, the code is transmitted with results.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility ID

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS, and the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

- When the responsible observer is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA, and the identifier type code (thirteenth component) contains PN.
- If there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted, concatenated with -VA and the VA station number.

The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### Observation Method (CE) 00936

Use this optional field to transmit the method or procedure by which an observation is obtained when the sending system needs to distinguish a measurement obtained by different methods where the distinction is not implicit in the test ID.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

VistA values this field, when available, with the related methodology associated with the result from WKLD SUFFIX CODES file (#64.2).

\<WKLD SUFFIX CODE\> \<text\> \<99VA64_2 \> \<alternate identifier\> \<alternate text\> \<name of alternate coding system

#### Equipment Instant Identifier (EI)

This field identifies the Equipment Instance (such as, Analyzer, Analyzer module, group of Analyzers) responsible for the production of the observation.

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

VistA Laboratory values this field with the information and in the form originally transmitted by the automated instrument that produced the result.

#### Date/Time of the Analysis (TS)

This field transfers the time stamp associated with the generation of the analytical result by the instrument specified in Equipment Instance Identifier.

VistA values this field with the date/time at which the associated results are verified and released.

#### Performing Organization Name (XON)

This field contains the name of the organization/service responsible for performing the service. When this field is null, the receiving system assumes the observations are produced by the sending organization. The information for producer ID is recorded as an XON data type.

For laboratories, this field specifies the laboratory that produced the test result described in this OBX segment and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories. This information supports CLIA regulations in the US. For producing laboratories, which are CLIA certified, the CLIA identifier is used as the organization identifier (component 10).

Components

\<Organization Name (ST)\> ^ \<Organization Name Type Code (IS)\> ^ ID Number (NM)\> ^ \<Check Digit (NM)\> ^ \<Check Digit Scheme (ID)\> ^ \<Assigning Authority (HD)\> ^ \<Identifier Type Code (ID)\> ^ \<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^ \<Organization Identifier (ST)\>

> **NOTE:** Pre-adopted from HL7 v2.5.1

- Organization Name (first component) contains the name of the VA facility or other organization.
- Organization Name Type (second component) contains:
1.  D to display the name when Facility is found in the VistA INSTITUTION file (#4)
2.  L to display the legal name when the official VA Name field (#100) is found in the VistA INSTITUTION file (#4)
3.  A to display the alias name when the Facility name is known
- ID Number (third component) contains the VA station number when it is numeric
- Assigning authority (sixth component) contains:
1.  USVHA when there is a facility ID
2.  CLIA when there is a CLIA identifier
- Identifier Type Code (seventh component) contains:
1.  FI when there is a facility identifier.
4.  LN when there is a CLIA identifier
- Name Representation Code (ninth component) is A when it is a facility identifier
- Organization Identifier (tenth component) contains:
1.  VA station number when it is a VA facility identifier
5.  DoD DMIS ID when there is a DoD facility identifier
6.  3-letter local ID when there is a non-VA, non-DoD facility identifier
7.  Laboratory CLIA number when there is a CLIA identifier.

#### Performing Organization Address (XAD)

This field contains the address of the organization/service responsible for performing the service. For laboratories, this field specifies the address of the laboratory that produced the test result described in this OBX segment and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories. This information supports CLIA regulations in the US.

Components

\<Street Address (SAD)\> ^ \<Other Designation (ST)\> ^ \<CITY (ST)\> ^ \<State or Province (ST)\> ^ \<Zip or Postal Code (ST)\> ^ \<Country (ID)\> ^ \<Address Type (ID)\> ^ \<Other Geographic Designation (ST)\> ^ \<County/Parish Code (IS)\> ^ \<Census Tract (IS)\> ^ \<Address Representation Code (ID)\> ^ \<DEPRECATED-Address Validity Range (DR)\> ^ \<Effective Date (TS)\> ^ \<Expiration Date (TS)\>

> **NOTE:** Pre-adopted from HL7 v2.5.1

Currently only components 1-6 are valued by VistA. Organization address is derived from the VistA INSTITUTION file (#4) using VistA HL supported API \$\$HLADDR^HLFNC.

Example

1234 Anyplace Avenue^Building 456^VistA City^<span class="mark">XX</span>^99999^USA

#### Performing Organization Medical Director (XCN)

This field contains the medical director of the organization/service responsible for performing the service. For laboratories, this field specifies the medical director of the laboratory that produced the test result described in this OBX segment and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories.

This field is different from OBX-16. OBX-16 identifies the individual who performed the lab test (made the observation), whereas this field identifies the individual who is the medical director of the organization responsible for the result. This information supports CLIA regulations in the US.

Components

\<ID Number (ST)\> ^ \<Family Name (FN)\> ^ \<Given Name (ST)\> ^ \<Second and Further Given Names or Initials Thereof (ST)\> ^ \<Suffix (e.g., JR or III) (ST)\> ^ \<Prefix (e.g., DR) (ST)\> ^ \<DEPRECATED-Degree (e.g., MD) (IS)\> ^ \<Source Table (IS)\> ^ \<Assigning Authority (HD)\> ^ \<Name Type Code (ID)\> ^ \<Identifier Check Digit (ST)\> ^ \<Check Digit Scheme (ID)\> ^ \<Identifier Type Code (ID)\> ^ \<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^ \<Name Context (CE)\> ^ \<DEPRECATED-Name Validity Range (DR)\> ^ \<Name Assembly Order (ID)\> ^ \<Effective Date (TS)\> ^ \<Expiration Date (TS)\> ^ \<Professional Suffix (ST)\> ^ \<Assigning Jurisdiction (CWE)\> ^ \<Assigning Agency or Department (CWE)\>

Subcomponents for Family Name (FN)

\<Surname (ST)\> & \<Own Surname Prefix (ST)\> & \<Own Surname (ST)\> & \<Surname Prefix From Partner/Spouse (ST)\> & \<Surname From Partner/Spouse (ST)\>

Subcomponents for Assigning Authority (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\> & \<Universal ID Type (ID)\>

Subcomponents for Assigning Facility (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\> & \<Universal ID Type (ID)\>

Subcomponents for Name Context (CE)

\<Identifier (ST)\> & \<Text (ST)\> & \<Name of Coding System (ID)\> & \<Alternate Identifier (ST)\> & \<Alternate Text (ST)\> & \<Name of Alternate Coding System (ID)\>

Subcomponents for DEPRECATED-Name Validity Range (DR)

\<Range Start Date/Time (TS)\> & \<Range End Date/Time (TS)\>

> **NOTE:** Subcomponent contains sub-subcomponents

Subcomponents for Effective Date (TS)

\<Time (DTM)\> & \<DEPRECATED-Degree of Precision (ID)\>

Subcomponents for Expiration Date (TS)

\<Time (DTM)\> & \<DEPRECATED-Degree of Precision (ID)\>

Subcomponents for Assigning Jurisdiction (CWE)

\<Identifier (ST)\> & \<Text (ST)\> & \<Name of Coding System (ID)\> & \<Alternate Identifier (ST)\> & \<Alternate Text (ST)\> & \<Name of Alternate Coding System (ID)\> & \<Coding System Version ID (ST)\> & \<Alternate Coding System Version ID (ST)\> & \<Original Text (ST)\>

Subcomponents for Assigning Agency or Department (CWE)

\<Identifier (ST)\> & \<Text (ST)\> & \<Name of Coding System (ID)\> & \<Alternate Identifier (ST)\> & \<Alternate Text (ST)\> & \<Name of Alternate Coding System (ID)\> & \<Coding System Version ID (ST)\> & \<Alternate Coding System Version ID (ST)\> & \<Original Text (ST)\>

> **NOTE:** Pre-adopted from HL7 v2.5.1

Currently VistA does not support this field. Support will be added in a future version of this interface specification as part of the VA implementation of the HITSP Use Case for Laboratory Result Reporting.

## ORC Segment – Common Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All applications use the ORC segment as the primary means of communicating specific laboratory order information. This segment contains data items that are common to all orders.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL \# | Element Name              |
|-----|-----|-----|-------|----------|-----|--------|---------------------------|
| 1   | 2   | ID  | R     | R        |     | 0119   | Order Control             |
| 2   | 22  | EI  | C     | R        |     |        | Placer Order Number       |
| 3   | 22  | EI  | C     | R        |     |        | Filler Order Number       |
| 12  | 250 | XCN | O     | R        |     |        | Ordering Provider         |
| 13  | 80  | PL  | O     | C        |     |        | Enterer’s Location        |
| 17  | 60  | CE  | O     | O        |     |        | Entering Organization     |
| 21  | 250 | XON | O     | R        | N   |        | Ordering Facility Name    |
| 22  | 250 | XAD | O     | R        | N   |        | Ordering Facility Address |

### ORC Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Order Control (SI)

This field is the value that determines the function of the order segment. The contents are hard-coded with RE for result messages originating from VistA. All ORU messages contain RE.

#### Placer Order Number (EI)

This field is an entity identifier made up of the following:

\<entity identifier\> \<namespace ID\>\<universal ID\>

It is a permanent identifier for an order and its associated observations on the placer’s system. Currently the first component is valued with the VistA Lab Unique Identifier (UID) or human readable accession. This identifier is returned with the results. The VistA Lab UID is a ten-character alpha/numeric identifier. The accession is constructed from the associated accession area abbreviation, concatenated with the abbreviated accession date, concatenated with the accession number

For entity identifier

- For CH subscript tests, the UID field (#.31) within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the ACCESSION field (#.06) within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63) is transmitted.

- For MI subscript tests, the UID field (#.31) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the MICROBIOLOGY ACCESSION field (#.06) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63) is transmitted.

- For SP subscript tests, the SURGICAL PATH ACC \# field (#.06) within the Surgical Pathology subfile (#8) of the VistA LAB DATA file (#63)
- For CY subscript tests, the CYTOPATH ACC \# field (#.06) within the Cytopathology subfile (#63.09) of the VistA LAB DATA file (#63)
- For EM subscript test, the EM ACC \# field (#.06) within the Electron Microscopy subfile (#62.02) of the VistA LAB DATA file (#63)
- For Point of Care (POC) testing after the POC system transmits an order number

For namespace ID

- LR – for VistA Laboratory related tests
- LRPOC – for VistA Laboratory Point of Care related tests

For universal ID

> The institution related to the order in the form of a VistA HL package standard DNS reference.

For universal ID type

> DNS

#### Filler Order Number (EI)

This field is an entity identifier made up of the following:

\<entity identifier\> \<namespace ID\>\<universal ID\>

It is a permanent identifier for an order and its associated observations on the placer’s system. Currently the first component is valued with the VistA Lab Unique Identifier (UID) or human readable accession. This identifier is returned with the results. The VistA Lab UID is a ten-character alpha/numeric identifier. The accession is constructed from the associated accession area abbreviation, concatenated with the abbreviated accession date, concatenated with the accession number

For entity identifier

- For CH subscript tests, the UID field (#.31) within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the ACCESSION field (#.06) within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63) is transmitted.

- For MI subscript tests, the UID field (#.31) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63)

> **NOTE:** When the instance of the order pre-dates the generation of the UID or is not available, the MICROBIOLOGY ACCESSION field (#.06) within the Microbiology, etc. subfile (#5) of the VistA LAB DATA file (#63) is transmitted.

- For SP subscript tests, the SURGICAL PATH ACC \# field (#.06) within the Surgical Pathology subfile (#8) of the VistA LAB DATA file (#63)
- For CY subscript tests , the CYTOPATH ACC \# field (#.06) within the Cytopathology subfile (#63.09) of the VistA LAB DATA file (#63)
- For EM subscript test, the EM ACC \# field (#.06) within the Electron Microscopy subfile (#62.02) of the VistA LAB DATA file (#63)

For namespace ID

> LR – for VistA Laboratory related tests

For universal ID

> The institution related to the order in the form of a VistA HL package standard DNS reference.

For universal ID type

> DNS

#### Ordering Provider (XCN)

This field contains the person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field repeats in OBR-16.

Components

> In Version 2.3 and later, instead of the CN data type, use

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

ID can be valued with one of three identifiers.

1.  When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS, and the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).
3.  When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA , and the identifier type code (13th component) contains PN.
4.  If there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with -VA and the VA station number.

The value for this field is derived from fields in the LAB DATA file (#63).

| Subscript | Subfile | Field                    |
|-----------|---------|--------------------------|
| CH        | 63.04   | Requesting Person (#.1)  |
| CY        | 63.09   | Physician (#.07)         |
| EM        | 63.02   | Physician (#.07)         |
| MI        | 63.05   | Physician (#.07)         |
| SP        | 63.08   | Surgeon/Physician (#.07) |

#### Enterer’s Location (PL)

This field specifies the location (such as, nurse station, ancillary service location, clinic, and floor) where the person who entered the request was physically located when the order was entered.

> **NOTE:** This refers to the current transaction as reflected in ORC-1 Order Control Code.

Only those subcomponents relevant to the enterer’s location should be valued (commonly nursing unit; facility; building; floor). The person who entered the request is defined in ORC-10 Entered By.

Components

\<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<person location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> ^ \<location description (ST)\> Subcomponents of facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

VistA values this field as follows:

For point of care

> The hospital location as named in HOSPITAL LOCATION file (#44)

For facility

> The facility as found in the INSTITUTION file (#4)

For personal location type

> If the type of location is Point of Care – C, N, D

Example

1 TEST (NORTH)^^^170K&REGION 7 ISC,<span class="mark">XX</span> (KRN)&L^^N

#### Entering Organization (CE)

This field is a coded element.

\<identifier\>\<text\>\<99VA4\>

The identifier number is the station number found in the VistA INSTITUTION file (#4), field Station Number (#99). The text is the value of field Official VA Name (#100). If this value is null, the value of field Name (#.01) is used.

#### Ordering Facility Name (XON)

This field contains the name of the facility placing the order.

Components

\<Organization Name (ST)\> ^ \<Organization Name Type Code (IS)\> ^\<DEPRECATED-ID Number (NM)\> ^ \<Check Digit (NM)\> ^ \<Check Digit Scheme (ID)\> ^ \<Assigning Authority (HD)\> ^ \<Identifier Type Code (ID)\> ^\<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^

\<Organization Identifier (ST)\>

Subcomponents for Assigning Authority (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

Subcomponents for Assigning Facility (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

- Organization Name (first component) contains the name of the VA facility or other organization.
- Organization Name Type (second component) contains:
1.  D to display the name when Facility is found in the VistA INSTITUTION file (#4)
8.  L to display the legal name when the official VA Name field (#100) is found in the VistA INSTITUTION file (#4)
9.  A to display the alias name when the Facility name is known
- ID Number (third component) contains the VA station number when it is numeric
- Assigning authority (sixth component) contains:
1.  USVHA when there is a facility ID
10. CLIA when there is a CLIA identifier
- Identifier Type Code (seventh component) contains:
1.  FI when there is a facility identifier.
11. LN when there is a CLIA identifier
- Name Representation Code (ninth component) is A when it is a facility identifier
- Organization Identifier (tenth component) contains:
1.  VA station number when it is a VA facility identifier
12. DoD DMIS ID when there is a DoD facility identifier
13. 3-letter local ID when there is a non-VA, non-DoD facility identifier
14. Laboratory CLIA number when there is a CLIA identifier.

#### Ordering Facility Address (XAD)

This field contains the address of the facility placing the order. It is the physical address of the facility as stored in the VA INSTITUTION file (#4) using VistA HL supported API \$\$HLADDR^HLFNC.

Components

\<Street Address (SAD)\> ^ \<Other Designation (ST)\> ^ \<City (ST)\> ^ \<State or Province (ST)\> ^ \<Zip or Postal Code (ST)\> ^ \<Country (ID)\> ^ \<Address Type (ID)\> ^ \<Other Geographic Designation (ST)\> ^ \<County/Parish Code (IS)\> ^ \<Census Tract (IS)\> ^ \<Address Representation Code (ID)\> ^\<DEPRECATED-Address Validity Range (DR)\> ^ \<Effective Date (TS)\> ^\<Expiration Date (TS)\>

Subcomponents for Street Address (SAD)

\<Street or Mailing Address (ST)\> & \<Street Name (ST)\> & \<Dwelling Number (ST)\>

Subcomponents for DEPRECATED-Address Validity Range (DR)

\<Range Start Date/Time (TS)\> & \<Range and Date/Time (TS)\>

Subcomponents for Effective Date (TS)

\<Time (DTM)\> & \<DEPRECATED-Degree of Precision (ID)\>

Subcomponents for Expiration Date (TS)

\<Time (DTM)\> & \<DEPRECATED-Degree of Precision(ID)\>

Example

1234 Anyplace Avenue^Building 456^VistA City^<span class="mark">XX</span>^99999^USA

## PID Segment – Patient Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that is not likely to change frequently.

VistA Laboratory uses an application Programming interface (API) to the Patient Information Management System (PMIS), which constructs the PID segment. This is by way of API BLDPID^VAFCQRY. Documentation for the PID segment produced by this API is contained in the MPI/PD HL7 Interface Specification located in the VistA Software Document Library at <http://www.va.gov/vdl/application.asp?appid=16>

## PV1 Segment – Patient Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV1 segment is used to communicate information on a visit specific basis.

VistA Laboratory uses an API to the Patient Information Management System (PMIS), which constructs the PV1 segment. This is through APIs:

- \$\$IN^VAFHLPV1 to build PV1 segments on inpatients
- \$\$OUT^VAFHLPV1 to build PV1 segments on outpatients

Documentation for the PV1 segment produced by these APIs is contained in the MPI/PD HL7 Interface Specification located on the VistA Software Document Library at <http://www.va.gov/vdl/application.asp?appid=16>

# Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA initiates ORU result messages, which are acknowledged with an ACK accept acknowledgment.

## Event and Subscriber Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA initiates ORU result messages, which are acknowledged with an ACK accept acknowledgment.

NAME: LA7 LAB RESULTS ACTION

ITEM TEXT: Lab process results for HL7 messaging

TYPE: action

PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Action protocol to setup sending lab results to HL7 message subscribers via protocol LA7 LAB RESULTS AVAILABLE (EVN) - Lab Results Available Event. This protocol should be attached to protocol LAB RESULTS =\> EXTERNAL PACKAGE \[LR7O ALL EVSEND RESULTS\] which is an extended action protocol triggered by the lab result verification process.

ENTRY ACTION: D QUEUE^LA7HDR TIMESTAMP: 59056,40855

NAME: LA7 LAB RESULTS AVAILABLE (EVN) ITEM TEXT: Lab Results Available Event

TYPE: event driver

DESCRIPTION:

A VistA Laboratory package HL7 ORU result message is created and sent by the HL package for transmission to any subscribers of event protocol LA7 LAB RESULTS AVAILABLE (EVN).

It provides the capability for the generation of a Laboratory HL7 ORU message containing patient laboratory results to subscribers of the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN) as these results are made available within the Laboratory package.

The following subscripts are supported by the event: CH, MI, SP, CY, EM.

TIMESTAMP: 59725,36770 SENDING APPLICATION: LA7LAB

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

MESSAGE STRUCTURE: ORU_R01 ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: NE VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D ACK^LA7VHL

SUBSCRIBERS: LA7 LAB RESULTS TO HDR (SUB)

NAME: LA7 LAB RESULTS TO HDR (SUB) ITEM TEXT: Send Lab Results to HDR  
TYPE: subscriber CREATOR: LRUSER,ONE

DESCRIPTION: This protocol should be attached to the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN). See this protocol for further information.

This subscriber protocol is used by the Laboratory package to indicate to the HL package to send laboratory results to the VA Health Data Repository (HDR).

It utilizes the "Router" Subscriber Protocol supported by the VistA HL package. The routing logic uses the value of the parameter passed into the router to determine which Laboratory package subscript should be sent to the HDR.

The following subscripts are supported by the event:

"CH", "MI", "SP", "CY", "EM".

Examples:

ROUTING LOGIC: D RTR^LA7HDR("CH;") will only send to HDR results associated with Laboratory "CH" subscript.

ROUTING LOGIC: D RTR^LA7HDR("MI;") will only send to HDR results associated with Laboratory "MI" subscript.

ROUTING LOGIC: D RTR^LA7HDR("CH;MI;") will only send to HDR results associated with Laboratory "CH", and "MI" subscripts.

ROUTING LOGIC: D RTR^LA7HDR("CH;MI;SP;") will only send to HDR results associated with Laboratory "CH", "MI", and "SP" subscripts.

ROUTING LOGIC: D RTR^LA7HDR("CH;MI;SP;CY;EM;") will send to HDR results associated with all Laboratory subscripts currently supported.

> **NOTE:** The order of the subscripts listed in the input parameter is not significant. Separating the subscripts using the ";" character is significant.

TIMESTAMP: 61205,41189 RECEIVING APPLICATION: LA  
EVENT TYPE: R01

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

ROUTING LOGIC: ;D RTR^LA7HDR("CH;")

## Activate Message Generation and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps only when activating the transmission of laboratory data to the VA HDR and/or interfacing to a Commercial Off the Shelf System (COTS) or other VistA subscriber.

No further action is required, if there is no requirement to activate this interface.

- To activate messaging to the VA HDR perform steps 1, 2, and 3.
- To activate messaging to COTS and other VistA subscribers perform steps 1 and 4.
1.  Generate and transmit HL7 Lab ORU result messages
1.  Enable the configuration LA7HDR in LA7 MESSAGE PARAMETER file (#62.48), and use VA File Manager to set the field Status (#2) to Active.
15. When this field is set to Inactive, the generation of the Lab HL7 ORU message is turned off.

Select VA FileMan Option: Enter or Edit File Entries

INPUT TO WHAT FILE: LA7 MESSAGE PARAMETER// 62.48 LA7 MESSAGE PARAMETER

EDIT WHICH FIELD: ALL// STATUS

THEN EDIT FIELD:

Select LA7 MESSAGE PARAMETER CONFIGURATION: LA7HDR

STATUS: INACTIVE// ACTIVE ACTIVE

5.  Set up the VDEFVIE4 link for Laboratory data transmission
1.  Use the HL7 Main Menu: select Filer and Link Management Options option to edit logical link VDEFVIE4.
16. Enable Auto Startup and add the IP address and port number.  
    IP address: 10.224.67.234  
    Port number: 5021
17. Use the HL7 Main Menu, Start/Stop Links option to start the VDEFVIE4 link.
18. Use the HL7 Main Menu, Site Parameters Edit option to select VDEF view and add VDEFVIE4 to the view.
6.  Activate the interface to the VA HDR
1.  On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\], use the Protocol Edit \[HL EDIT INTERFACE\] menu option to edit the protocol LA7 LAB RESULTS TO HDR (SUB).
19. On the second ScreenMan screen, remove the leading (;) character from the Routing Logic field.
20. Enter the Save command to retain the changes to the protocol.

Example: Editing the Routing Logic field

HL7 SUBSCRIBER PAGE 2 OF 2

LA7 LAB RESULTS TO HDR (SUB)

---------------------------------------------------------------------------

RECEIVING APPLICATION: LA7HDR

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?:

LOGICAL LINK: VDEFVIE4

PROCESSING RTN:

ROUTING LOGIC: D RTR^LA7HDR("CH;") \<-- remove leading ";" character

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

After the change, the field displays as:

ROUTING LOGIC: D RTR^LA7HDR("CH;")

7.  Transmit Lab HL7 ORU result messages to another system, such as a Commercial Off the Shelf System (COTS)
1.  Create an HL7 subscriber protocol, as documented in the *HL7 Site Manager & Developer Manual* version 1.6\*56.
21. Attach the HL7 subscriber protocol as a subscriber to HL7 event protocol, LA7 LAB RESULTS AVAILABLE (EVN).
8.  On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\] menu option, use the Protocol Edit \[HL EDIT INTERFACE\] option to add the HL7 subscriber.

## Inactivate Message Generation and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>![](la-5-2-68-laboratory-hl7-specification/002.png)</th>
<th><strong>Notify the HDR Project Office<br />
in the event that this interface is deactivated and the interface to the HDR was previously activated</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To control Lab HL7 ORU message generation and transmission after the interface is activated or to inactivate message generation and/or transmission, perform the following steps.

Use step 1 to inactivate all message generation to all subscribers.

Use step 2 to inactivate message generation/transmission to a specific subscriber.

1.  Inactivate Lab HL7 ORU message generation and transmission to all subscribers of event protocol, LA7 LAB RESULTS AVAILABLE (EVN)
1.  Disable the configuration LA7HDR in the LA7 MESSAGE PARAMETER file (#62.48), and set the field Status (#2) to Inactive using VA File Manager Enter or Edit File Entries \[DIEDIT\].
22. When this field is set to Inactive, the generation of the Lab HL7 ORU message is turned off.
9.  Inactivate message transmission to a specific subscriber
1.  On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\] menu option, use the Protocol Edit \[HL EDIT INTERFACE\] option to remove the related subscriber protocol from the event protocol LA7 LAB RESULTS AVAILABLE (EVN).
23. For the VA HDR, remove subscriber protocol LA7 LAB RESULTS TO HDR (SUB).

## Specific Message Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Anatomic Pathology Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Anatomic Pathology is not CPRS-aware and is unable to notify CPRS about the release of anatomic pathology results. HDR is notified of the availability of anatomic pathology results by three new-style cross-references in the LAB DATA file (#63). These indexes also trigger generation of the Lab HL7 ORU message, if this capability was enabled.

1.  Subfile \#63.02

> New-Style Indexes:

> AC (#98) FIELD MUMPS ACTION

> Short Descr: Notify HDR and others that this report is available.

> Description: This MUMPS cross-reference triggers the sending of this report to the Health Data Repository (HDR) and other subscribers when Electron Microscopy results are released.

> Set Logic: D APQ^LA7HDR(DA(1),"EM",DA)

> Kill Logic: Q

> X(1): REPORT RELEASE DATE (63.02,.11) (Subscr 1) (forwards)

10. Subfile \#63.08

> New-Style Indexes:

> AD (#95) FIELD MUMPS ACTION

> Short Descr: Notify HDR and others that this report is available. Description: This MUMPS cross-reference triggers the sending of this report to the Health Data Repository (HDR) and other subscribers when Surgical Pathology results are released.

> Set Logic: D APQ^LA7HDR(DA(1),"SP",DA)

> Kill Logic: Q

> X(1): REPORT RELEASE DATE/TIME (63.08,.11) (Subscr 1) (forwards)

11. Subfile \#63.09

> New-Style Indexes:

> AD (#96) FIELD MUMPS ACTION

> Short Descr: Notify HDR and others that this report is available.

> Description: This MUMPS cross-reference triggers the sending of this report to the Health Data Repository (HDR) and other subscribers when Cytopathology results are released.

> Set Logic: D APQ^LA7HDR(DA(1),"CY",DA)

> Kill Logic: Q

> X(1): REPORT RELEASE DATE/TIME (63.09,.11) (Subscr 1) (forwards)

### Microbiology Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of microbiology results. A default encoding is enabled to LOINC encode standard microbiology tests and antibiotics.

There is default mapping of NLT/LOINC codes to standard fields within the Microbiology subfile (#5) multiple of LAB DATA file (#63).

| Test                           | Order NLT  | Result NLT | LOINC Code |
|--------------------------------|------------|------------|------------|
| Bacteriology report (#11)      | 87993.0000 |            |            |
| Gram stain (#11.6)             | 87993.0000 | 87754.0000 | 664-3      |
| Urine Screen (#11.57)          | 87993.0000 | 93949.0000 | 630-4      |
| Sputum Screen (#11.58)         | 87993.0000 | 93948.0000 | 6460-0     |
| Bacteria colony count (#12,1)  |            | 87719.0000 | 564-5      |
| Parasite report (#14)          | 87505.0000 |            |            |
| Parasite organism (#16)        | 87505.0000 | 87576.0000 | 17784-0    |
| Mycology report (#18)          | 87994.0000 |            |            |
| Fungal organism (#20)          | 87994.0000 | 87578.0000 | 580-1      |
| Fungal colony count (#20,1)    | 87994.0000 | 87723.0000 | 19101-5    |
| Mycobacterium report (#22)     | 87995.0000 |            |            |
| Acid Fast stain (#24)          | 87995.0000 | 87756.0000 | 11545-1    |
| Acid Fast stain quantity (#25) | 87995.0000 | 87583.0000 | 11545-1    |
| Mycobacterium organism (#26)   | 87995.0000 | 87589.0000 | 543-9      |
| Virology report (#33)          | 87996.0000 |            |            |
| Viral agent (#36)              | 87996.0000 | 87590.0000 | 6584-7     |

### Bacteriology Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The susceptibilities of a bacteriology or mycobacterium (TB) organism are based on the local site's mapping of the National VA Lab Code field (#64) in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and the related default LOINC code associated with the VA NLT code.

### Surgical Pathology Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Surgical Pathology results.

There is default mapping of NLT/LOINC codes to standard fields within the SURGICAL PATHOLOGY file (#8) multiple of the LAB DATA file (#63).

| Test                            | Order NLT  | Result NLT | LOINC Code |
|---------------------------------|------------|------------|------------|
| Specimen (#.012)                | 88515.0000 | 88539.0000 | 22633-2    |
| Brief clinical history (#.013)  | 88515.0000 | 88542.0000 | 22636-5    |
| Preoperative diagnosis (#.014)  | 88515.0000 | 88544.0000 | 10219-4    |
| Operative findings (#.015)      | 88515.0000 | 88546.0000 | 10215-2    |
| Postoperative diagnosis (#.016) | 88515.0000 | 88547.0000 | 10218-6    |
| Gross description (#1)          | 88515.0000 | 88549.0000 | 22634-0    |
| Microscopic description (#1.1)  | 88515.0000 | 88563.0000 | 22635-7    |
| Frozen section (#1.3)           | 88515.0000 | 88569.0000 | 22635-7    |
| Surgical path diagnosis (#1.4)  | 88515.0000 | 88571.0000 | 22637-3    |
| Supplementary report (#1.2)     | 88515.0000 | 88589.0000 | 22639-9    |
| Specimen weight (#2)            | 88515.0000 | 81233.0000 | 3154-2     |

### Cytopathology Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Cytopathology results.

There is default mapping of NLT/LOINC codes to standard fields within the Cytopathology (#9) multiple of LAB DATA file (#63).

| Test                            | Order NLT  | Result NLT | LOINC Code |
|---------------------------------|------------|------------|------------|
| Specimens (#.012)               | 88593.0000 | 88539.0000 | 22633-2    |
| Brief clinical history (#.013)  | 88593.0000 | 88542.0000 | 22636-5    |
| Preoperative diagnosis (#.014)  | 88593.0000 | 88544.0000 | 10219-4    |
| Operative findings (#.015)      | 88593.0000 | 88542.0000 | 10215-2    |
| Postoperative diagnosis (#.016) | 88593.0000 | 88547.0000 | 10218-6    |
| Gross description (#1)          | 88593.0000 | 88549.0000 | 22634-0    |
| Microscopic examination (#1.1)  | 88593.0000 | 88563.0000 | 22635-7    |
| Supplementary report (#1.2)     | 88593.0000 | 88589.0000 | 22639-9    |
| Cytopathology diagnosis (#1.4)  | 88593.0000 | 88571.0000 | 22637-3    |

### Electron Microscopy Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Electron Microscopy.

There is default mapping of NLT/LOINC codes to standard fields within the Electron Microscopy (#2) multiple of LAB DATA file (#63).

| Test                            | Order NLT  | Result NLT | LOINC Code |
|---------------------------------|------------|------------|------------|
| Specimens (#.012)               | 88597.0000 | 88057.0000 | 22633-2    |
| Brief clinical history (#.013)  | 88597.0000 | 88542.0000 | 22636-5    |
| Preoperative diagnosis (#.014)  | 88597.0000 | 88544.0000 | 10219-4    |
| Operative findings (#.015)      | 88597.0000 | 88542.0000 | 10215-2    |
| Postoperative diagnosis (#.016) | 88597.0000 | 88547.0000 | 10218-6    |
| Gross description (#1)          | 88597.0000 | 88549.0000 | 22634-0    |
| Microscopic examination (#1.1)  | 88597.0000 | 88563.0000 | 22635-7    |
| Supplementary report (#1.2)     | 88597.0000 | 88589.0000 | 22639-9    |
| EM diagnosis (#1.4)             | 88597.0000 | 88571.0000 | 22637-3    |

## Specific Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Result Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORU Observational Results Unsolicited Message

| MSH       | Message Header         |
|-----------|----------------------------|
| {\[PID\]  | Patient Identification     |
| \[PV1\]   | Patient Visit              |
| {\[ORC\]  | Order Common               |
| OBR       | Observations Report ID     |
| {\[NTE\]} | Laboratory Note or Comment |
| {\[OBX\]  | Observation Segment        |
| {\[NTE\]} | Laboratory Note or Comment |
| }         |                            |
| }         |                            |
| }         |                            |

Example: Chemistry/hematology/serology message

MSH\|^~\\\|LA7LAB\|522^MHCVSS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|LA7HDR\|200HD^HDR.MED.VA.GOV^DNS\|20090303164215-0500\|\|ORU^R01^ORU_R01\|52245904\|T\|2.4\|\|\|AL\|NE\|

PID\|1\|\|000001111^^^USSSA&&0363^SS^VA FACILITY ID&522&L~375^^^USVHA&&0363^PI^VA FACILITY ID&522&L\|\|LRPATIENT^ONE^^JR^^^L\|LRMOTHER^MAIDEN^^^^^M\|19200212\|M\|\|2054-5-SLF^^0005^2054-5^^CDC\|^^^^^^P^^~^^<span class="mark">XXXXXXXXXX</span>^<span class="mark">XX</span>^^^N\|\|\|\|\|M\|25\|\|000001111\|\|\|\|<span class="mark">XXXXXXXXXX</span> DC\|N\|\|\|\|\|\|\|

PV1\|1\|I\|\|\|\|^^\|115^LRPROVIDER^ONE^^JR^DR^MD\|\|\|1\|\|\|\|\|\|\|\|NSC VETERAN\|\|\|15\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|522\|\|\|\|\|20060106105459-0500\|

ORC\|RE\|0381580001^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|0381580001^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|\|\|\|^^^^^R\|\|\|\|\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|1 TEST (NORTH)^^^170K&REGION 7 ISC,<span class="mark">XX</span> (KRN)&L^^N\|\|\|\|170K^REGION 7 ISC,<span class="mark">XX</span> (KRN)^99VA4\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^522^^^USVHA^FI^^A^522\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|1\|0381580001^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|0381580001^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|81122.0000^Auto Chem \>18 test^99VA64^268^CHEM 20^99VA60\|\|\|20080606131851-0500\|\|\|\|L\|\|\|20080606131923-0500\|67922002&Serum (substance)&SCT&SER&Serum&HL70070&20060101&&SERUM\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\0381580001\|356\S\CH\S\6919392.868149\|SMAC 0606 1\S\1\S\3080606\S\1\S\CHEM-20\S\SMAC\S\81122.0000\|20080703231815-0500\|\|CH\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|81122.0000^Auto Chem \>18 test^99VA64

NTE\|1\|L\|For Test: CHEM 20~Testing Lab HDR interface\|VA-LR001^Order Comment^HL70364

NTE\|2\|L\|Specimen slightly hemolyzed~Recommend repeating in one week~CREATININE reported incorrectly as 7.2 by \[235-VA522\].~Changed to 13.3 on Jul 03, 2008@23:18 by \[6521-VA522\].~CREATININE normalcy reported incorrectly as H by \[235-VA522\].~Changed to H\* on Jul 03, 2008@23:18 by \[6521-VA522\].\|VA-LR002^Result Comment^HL70364

OBX\|1\|NM\|14749-6^Glucose:SCnc:Pt:Ser/Plas:Qn^LN^4656317^^99VA95.3^2.19^2.19^GLUCOSE\|CH2\|765\|mg/dL^mg/dL^L\|60-123\|HH\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~81352.0000^Glucose Fasting^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\| 70-99 mg/dL NORMAL~ 100-125 mg/dL Impaired Fasting Glucose~ \>/= 126 mg/dL Provisional Diagnosis of Diabetes~ ~ \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*\|VA-LR003^Result Interpretation^HL70364

OBX\|2\|NM\|3094-0^Urea nitrogen:MCnc:Pt:Ser/Plas:Qn^LN^4673484^^99VA95.3^2.19^2.19^UREA NITROGEN\|CH3\|3\|mg/dL^mg/dL^L\|11-24\|L\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~83940.0000^BUN^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|NM\|2160-0^Creatinine:MCnc:Pt:Ser/Plas:Qn^LN^4663483^^99VA95.3^2.19^2.19^CREATININE\|CH4\|13.3\|mg/dL^mg/dL^L\|.8-1.3\|HH\|\|\|C\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|00000000000000000001^LRUSER^LAB^^^^^^USVHA^^^^PN\|.3035^DU PONT ACA^99VA64.2~82565.0000^Creatinine^99VA64\|\|20080703231813-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|NM\|2947-0^Sodium:SCnc:Pt:Bld:Qn^LN^4671867^^99VA95.3^2.19^2.19^SODIUM\|CH5\|110\|meq/L^meq/L^L\|135-145\|LL\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~84295.0000^Sodium^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|5\|NM\|2823-3^Potassium:SCnc:Pt:Ser/Plas:Qn^LN^4670505^^99VA95.3^2.19^2.19^POTASSIUM\|CH6\|6.7\|meq/L^meq/L^L\|3.8-5.3\|HH\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~84140.0000^Potassium^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|6\|NM\|2075-0^Chloride:SCnc:Pt:Ser/Plas:Qn^LN^4662584^^99VA95.3^2.19^2.19^CHLORIDE\|CH7\|123\|meq/L^meq/L^L\|100-108\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82435.0000^Chloride^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|7\|NM\|1963-8^Bicarbonate:SCnc:Pt:Ser:Qn^LN^4661390^^99VA95.3^2.19^2.19^CO2\|CH8\|55\|meq/L^meq/L^L\|23-31\|HH\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~83646.0000^HCO3^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|Any interpretive test related information will appear in this section of the report.\|VA-LR003^Result Interpretation^HL70364

OBX\|8\|NM\|2000-8^Calcium:SCnc:Pt:Ser/Plas:Qn^LN^4661785^^99VA95.3^2.19^2.19^CALCIUM\|CH9\|15.2\|mg/dL^mg/dL^L\|9-11\|HH\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82310.0000^Calcium^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|9\|NM\|2777-1^Phosphate:MCnc:Pt:Ser/Plas:Qn^LN^4670018^^99VA95.3^2.19^2.19^PO4\|CH10\|1.2\|mg/dL^mg/dL^L\|2.2-3.9\|L\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~83141.0000^Phosphorus^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|10\|NM\|CH11^URIC ACID^99VA63^^^^5.2^^URIC ACID\|CH11\|2.3\|mg/dL^mg/dL^L\|4.2-8.5\|L\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~84550.0000^Uric Acid^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|11\|NM\|2093-3^Cholesterol:MCnc:Pt:Ser/Plas:Qn^LN^4662777^^99VA95.3^2.19^2.19^CHOLESTEROL\|CH12\|99\|mg/dL^mg/dL^L\|135-288\|L\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~83679.0000^Cholesterol^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|12\|NM\|CH13^PROTEIN,TOTAL^99VA63^^^^5.2^^PROTEIN,TOTAL\|CH13\|9.8\|g/dL^g/dL^L\|6.2-7.7\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~84155.0000^Protein Total^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|13\|NM\|1751-7^Albumin:MCnc:Pt:Ser/Plas:Qn^LN^4659241^^99VA95.3^2.19^2.19^ALBUMIN\|CH14\|4.9\|g/dL^g/dL^L\|3.8-5\|\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82040.0000^Albumin^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|14\|NM\|1975-2^Bilirubin:MCnc:Pt:Ser/Plas:Qn^LN^4661507^^99VA95.3^2.19^2.19^TOT. BILIRUBIN\|CH15\|15.1\|mg/dL^mg/dL^L\|.3-1.7\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82250.0000^Bilirubin Total^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building456^^<span class="mark">XX</span>^^USA

OBX\|15\|NM\|1968-7^Bilirubin.glucuronidated+Bilirubin.albumin bound:MCnc:Pt:Ser/Plas:Qn^LN^4661437^^99VA95.3^2.19^2.19^DIR. BILIRUBIN\|CH16\|1.4\|mg/dL^mg/dL^L\|0-.3\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82249.0000^Bilirubin Direct^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|16\|NM\|CH17^ALKALINE PHOSPHATASE^99VA63^^^^5.2^^ALKALINE PHOSPHATASE\|CH17\|427\|U/L^U/L^L\|48-136\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~82110.0000^Phosphatase Alkaline Placental^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|17\|NM\|2532-0^Lactate dehydrogenase:CCnc:Pt:Ser/Plas:Qn^LN^4667425^^99VA95.3^2.19^2.19^LDH\|CH18\|962\|U/L^U/L^L\|128-227\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~83802.0000^LDH^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|18\|NM\|CH19^SGOT^99VA63^^^^5.2^^SGOT\|CH19\|555\|U/L^U/L^L\|11-32\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~81122.0000^Auto Chem \>18 test^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|19\|NM\|CH20^SGPT^99VA63^^^^5.2^^SGPT\|CH20\|432\|U/L^U/L^L\|12-66\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~81122.0000^Auto Chem \>18 test^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|20\|NM\|2324-2^Gamma glutamyl transferase:CCnc:Pt:Ser/Plas:Qn^LN^4665239^^99VA95.3^2.19^2.19^GAMMA-GTP\|CH21\|123\|U/L^U/L^L\|0-65\|H\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~81234.0000^GGTP^99VA64\|\|20080606132123-0500\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|21\|NM\|CH791^CALCULATED OSMOLALITY^99VA63^^^^5.2^^CALCULATED OSMOLALITY\|CH791\|248\|mOsm/L^mOsm/L^L\|275-300\|\|\|\|F\|\|\|20080606131851-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|.3035^DU PONT ACA^99VA64.2~81122.0000^Auto Chem \>18 test^99VA64\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

  
Example: Microbiology message

MSH\|^~\\\|LA7LAB\|522^MHCVSS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|LA7HDR\|200HD^HDR.MED.VA.GOV^DNS\|20090303170542-0500\|\|ORU^R01^ORU_R01\|52245905\|T\|2.4\|\|\|AL\|NE\|

PID\|1\|\|000001111^^^USSSA&&0363^SS^VA FACILITY ID&522&L~375^^^USVHA&&0363^PI^VA FACILITY ID&522&L\|\|LRPATIENT^ONE^^JR^^^L\|LRMOTHER^MAIDEN^^^^^M\|19200212\|M\|\|2054-5-SLF^^0005^2054-5^^CDC\|^^^^^^P^^~^^<span class="mark">XXXXXXXXXX</span>^<span class="mark">XX</span>^^^N\|\|\|\|\|M\|25\|\|000001111\|\|\|\|<span class="mark">XXXXXXXXXX</span> <span class="mark">XX</span>\|N\|\|\|\|\|\|\|

PV1\|1\|I\|\|\|\|^^\|115^LRPROVIDER^ONE^^JR^DR^MD\|\|\|1\|\|\|\|\|\|\|\|NSC VETERAN\|\|\|15\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|522\|\|\|\|\|20060106105459-0500\|

ORC\|RE\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|\|\|\|\|\|\|\|\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|1 TEST (NORTH)^^^170K&REGION 7 ISC,<span class="mark">XX</span> (KRN)&L^^N\|\|\|\|170K^REGION 7 ISC,<span class="mark">XX</span> (KRN)^99VA4\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^522^^^USVHA^FI^^A^522\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|1\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|87993.0000^Micro Bacteriology Culture^99VA64\|\|\|20080501111313-0500\|\|\|\|\|\|\|20080501111313-0500\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\1408000004\|356\S\MI\S\6919497.888687\|MICRO 08 4\S\12\S\3080000\S\4\S\MICROBIOLOGY\S\MICRO\S\87993.0000\|20081110\|\|MB\|P\|\|\|\|\|\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|\|\|\|\|\|\|\|\|\|\|87040^BLOOD CULTURE FOR BACTERIA^C4^87993.0000^Micro Bacteriology Culture^99VA64

NTE\|1\|L\|\|VA-LRMI001^Comment on Specimen (#.99)^HL70364

NTE\|2\|L\|Several organisms found upon culture\|VA-LRMI010^Bact Rpt Remark (#13)^HL70364

NTE\|3\|L\|General comment on the culture/report\|VA-LRMI010^Bact Rpt Remark (#13)^HL70364

OBX\|1\|CWE\|630-4^Bacteria identified:Prid:Pt:Urine:Nom:Culture^LN^4684556^^99VA95.3^2.19^2.19^URINE SCREEN\|\|10828004^Positive^SCT^^^^20060101\|\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|2\|ST\|664-3^Microscopic observation:Prid:Pt:XXX:Nom:Gram stain^LN^4684916^^99VA95.3^2.19^2.19^GRAM STAIN\|\|GRAM POSITIVE COCCI, IN CHAINS\|\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|ST\|664-3^Microscopic observation:Prid:Pt:XXX:Nom:Gram stain^LN^4684916^^99VA95.3^2.19^2.19^GRAM STAIN\|\|GRAM POSITIVE RODS\|\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|ST\|664-3^Microscopic observation:Prid:Pt:XXX:Nom:Gram stain^LN^4684916^^99VA95.3^2.19^2.19^GRAM STAIN\|\|GRAM POSITIVE COCCI, IN CLUSTERS WITH SPORES\|\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|5\|CWE\|11475-1^Microorganism identified:Prid:Pt:XXX:Nom:Culture^LN^4652804^^99VA95.3^2.19^2.19^ORGANISM\|99VA4:522:3-1\|112283007^Escherichia coli (organism)^SCT^1^ESCHERICHIA COLI^99VA61.2^20060101^5.2^ESCHERICHIA COLI\|\|\|A\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|organism comment shows here\|RE^Remark^HL70364

OBX\|6\|ST\|564-5^Colony count:Num:Pt:XXX:Qn:VC^LN^4683874^^99VA95.3^2.19^2.19^QUANTITY\|99VA4:522:3-1\|\>10,000 - \<25,000\|CFU/ml^CFU/ml^L\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|7\|CWE\|11475-1^Microorganism identified:Prid:Pt:XXX:Nom:Culture^LN^4652804^^99VA95.3^2.19^2.19^ORGANISM\|99VA4:522:3-2\|52499004^Pseudomonas aeruginosa (organism)^SCT^4836^PSEUDOMONAS AERUGINOSA^99VA61.2^20060101^5.2^PSEUDOMONAS AERUGINOSA\|\|\|A\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|Comment \#1 on the organism\|RE^Remark^HL70364

NTE\|2\|L\|Comment \#2 on the organsim\|RE^Remark^HL70364

OBX\|8\|ST\|564-5^Colony count:Num:Pt:XXX:Qn:VC^LN^4683874^^99VA95.3^2.19^2.19^QUANTITY\|99VA4:522:3-2\|\>50,000 - \<75,000\|CFU/ml^CFU/ml^L\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|9\|CWE\|11475-1^Microorganism identified:Prid:Pt:XXX:Nom:Culture^LN^4652804^^99VA95.3^2.19^2.19^ORGANISM\|99VA4:522:3-3\|73457008^Proteus mirabilis (organism)^SCT^4833^PROTEUS MIRABILIS^99VA61.2^20060101^5.2^PROTEUS MIRABILIS\|\|\|A\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|Comment on the proteus isolate\|RE^Remark^HL70364

OBX\|10\|ST\|564-5^Colony count:Num:Pt:XXX:Qn:VC^LN^4683874^^99VA95.3^2.19^2.19^QUANTITY\|99VA4:522:3-3\|\>25,000 - \<50,000\|CFU/ml^CFU/ml^L\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|2\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|87565.0000^Bacteriology Susc^99VA64\|\|\|20080501111313-0500\|\|\|\|\|\|\|20080501111313-0500\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\1408000004\|356\S\MI\S\6919497.888687\|MICRO 08 4\S\12\S\3080000\S\4\S\MICROBIOLOGY\S\MICRO\S\87565.0000\|20081110\|\|MB\|P\|11475-1&Microorganism identified:Prid:Pt:XXX:Nom:Culture&LN&4652804&&99VA95.3&2.19&2.19&ORGANISM^99VA4:522:3-1^Escherichia coli (organism)\|\|\|1408000004^1408000004\|\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|\|\|\|\|\|\|\|\|\|\|87565.0000^Bacteriology Susc^99VA64

OBX\|1\|CWE\|18928-2^Gentamicin:Susc:Pt:Isolate:OrdQn^LN^4660716^^99VA95.3^2.19^2.19^GENTMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|2\|CWE\|18903-5^Chloramphenicol:Susc:Pt:Isolate:OrdQn^LN^4660690^^99VA95.3^2.19^2.19^CHLORAM\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|CWE\|18993-6^Tetracycline:Susc:Pt:Isolate:OrdQn^LN^4660787^^99VA95.3^2.19^2.19^TETRCLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|CWE\|18864-9^Ampicillin:Susc:Pt:Isolate:OrdQn^LN^4660646^^99VA95.3^2.19^2.19^AMPICLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|DISPLAY COMMENT\|RE^Remark^HL70364

OBX\|5\|CWE\|18873-0^Carbenicillin:Susc:Pt:Isolate:OrdQn^LN^4660656^^99VA95.3^2.19^2.19^CARBCLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|6\|CWE\|18996-9^Tobramycin:Susc:Pt:Isolate:OrdQn^LN^4660790^^99VA95.3^2.19^2.19^TOBRMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|7\|CWE\|18912-6^Colistin:Susc:Pt:Isolate:OrdQn^LN^4660700^^99VA95.3^2.19^2.19^COLISTIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|3\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|87565.0000^Bacteriology Susc^99VA64\|\|\|20080501111313-0500\|\|\|\|\|\|\|20080501111313-0500\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\1408000004\|356\S\MI\S\6919497.888687\|MICRO 08 4\S\12\S\3080000\S\4\S\MICROBIOLOGY\S\MICRO\S\87565.0000\|20081110\|\|MB\|P\|11475-1&Microorganism identified:Prid:Pt:XXX:Nom:Culture&LN&4652804&&99VA95.3&2.19&2.19&ORGANISM^99VA4:522:3-2^Pseudomonas aeruginosa (organism)\|\|\|1408000004^1408000004\|\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|\|\|\|\|\|\|\|\|\|\|87565.0000^Bacteriology Susc^99VA64

OBX\|1\|CWE\|18928-2^Gentamicin:Susc:Pt:Isolate:OrdQn^LN^4660716^^99VA95.3^2.19^2.19^GENTMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|2\|CWE\|18996-9^Tobramycin:Susc:Pt:Isolate:OrdQn^LN^4660790^^99VA95.3^2.19^2.19^TOBRMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|CWE\|18860-7^Amikacin:Susc:Pt:Isolate:OrdQn^LN^4660642^^99VA95.3^2.19^2.19^AMIKACN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|CWE\|18969-6^Piperacillin:Susc:Pt:Isolate:OrdQn^LN^4660760^^99VA95.3^2.19^2.19^PIPERACILLIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|5\|CWE\|18886-2^Cefotaxime:Susc:Pt:Isolate:OrdQn^LN^4660670^^99VA95.3^2.19^2.19^CEFOTAXIME\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|6\|CWE\|18947-2^Mezlocillin:Susc:Pt:Isolate:OrdQn^LN^4660736^^99VA95.3^2.19^2.19^MEZLOCILLIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|4\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|87565.0000^Bacteriology Susc^99VA64\|\|\|20080501111313-0500\|\|\|\|\|\|\|20080501111313-0500\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\1408000004\|356\S\MI\S\6919497.888687\|MICRO 08 4\S\12\S\3080000\S\4\S\MICROBIOLOGY\S\MICRO\S\87565.0000\|20081110\|\|MB\|P\|11475-1&Microorganism identified:Prid:Pt:XXX:Nom:Culture&LN&4652804&&99VA95.3&2.19&2.19&ORGANISM^99VA4:522:3-3^Proteus mirabilis (organism)\|\|\|1408000004^1408000004\|\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|\|\|\|\|\|\|\|\|\|\|87565.0000^Bacteriology Susc^99VA64

OBX\|1\|CWE\|18928-2^Gentamicin:Susc:Pt:Isolate:OrdQn^LN^4660716^^99VA95.3^2.19^2.19^GENTMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|2\|CWE\|18903-5^Chloramphenicol:Susc:Pt:Isolate:OrdQn^LN^4660690^^99VA95.3^2.19^2.19^CHLORAM\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|CWE\|18878-9^Cefazolin:Susc:Pt:Isolate:OrdQn^LN^4660661^^99VA95.3^2.19^2.19^CEFAZOLIN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|CWE\|18993-6^Tetracycline:Susc:Pt:Isolate:OrdQn^LN^4660787^^99VA95.3^2.19^2.19^TETRCLN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|5\|CWE\|18864-9^Ampicillin:Susc:Pt:Isolate:OrdQn^LN^4660646^^99VA95.3^2.19^2.19^AMPICLN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|DISPLAY COMMENT\|RE^Remark^HL70364

OBX\|6\|CWE\|18998-5^Trimethoprim+Sulfamethoxazole:Susc:Pt:Isolate:OrdQn^LN^4660792^^99VA95.3^2.19^2.19^TRMSULF\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|7\|CWE\|18860-7^Amikacin:Susc:Pt:Isolate:OrdQn^LN^4660642^^99VA95.3^2.19^2.19^AMIKACN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|8\|CWE\|18888-8^Cefoxitin:Susc:Pt:Isolate:OrdQn^LN^4660672^^99VA95.3^2.19^2.19^CEFOXITIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|9\|CWE\|18969-6^Piperacillin:Susc:Pt:Isolate:OrdQn^LN^4660760^^99VA95.3^2.19^2.19^PIPERACILLIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|10\|CWE\|18886-2^Cefotaxime:Susc:Pt:Isolate:OrdQn^LN^4660670^^99VA95.3^2.19^2.19^CEFOTAXIME\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|11\|CWE\|18947-2^Mezlocillin:Susc:Pt:Isolate:OrdQn^LN^4660736^^99VA95.3^2.19^2.19^MEZLOCILLIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|12\|CWE\|18986-0^Sulfisoxazole:Susc:Pt:Isolate:OrdQn^LN^4660779^^99VA95.3^2.19^2.19^SULFISOXAZOLE\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|P\|\|4500665\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

NTE\|1\|L\|Administer as last resort due toxicity\|RE^Remark^HL70364

OBX\|13\|NM\|21070-8^Antibiotic XXX:Susc:Pt:Isolate:OrdQn:MIC^LN^4662927^^99VA95.3^2.19^2.19^GENTAMICIN\|\|33.4\|UG/ML\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|14\|NM\|23658-8^Antibiotic XXX:Susc:Pt:Isolate:OrdQn^LN^4665685^^99VA95.3^2.19^2.19^GENTAMICIN\|\|66.8\|UG/ML\|\|\|\|\|P\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBR\|5\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|1408000004^LR^FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|93978.0000^Antibiotic Level^99VA64^547^ANTIBIOTIC LEVEL^99VA60\|\|\|20080501111313-0500\|\|\|\|A\|\|\|20080501111313-0500\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\1408000004\|356\S\MI\S\6919497.888687\|MICRO 08 4\S\12\S\3080000\S\4\S\MICROBIOLOGY\S\MICRO\S\93978.0000\|20080501111313-0500\|\|MB\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|93978.0000^AntibioticLevel^99VA64

OBX\|15\|SN\|44433-1^Antibiotic XXX\R\peak:MCnc:Pt:Ser/Plas:Qn^LN^4703118^^99VA95.3^2.19^2.19^SUPER GENTAMCIN\|\|12-14\|\|\|\|\|\|\|\|\|20080501111313-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

Example: Surgical Pathology message

MSH\|^~\\\|LA7LAB\|522^MHCVSS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>^DNS\|LA7HDR\|200HD^HDR.MED.VA.GOV^DNS\|20090304174009-0500\|\|ORU^R01^ORU_R01\|52245928\|T\|2.4\|\|\|AL\|NE\|

PID\|1\|\|000001111^^^USSSA&&0363^SS^VA FACILITY ID&522&L~375^^^USVHA&&0363^PI^VA FACILITY ID&522&L\|\|LRPATIENT^ONE^^JR^^^L\|LRMOTHER^MAIDEN^^^^^M\|19200212\|M\|\|2054-5-SLF^^0005^2054-5^^CDC\|^^^^^^P^^~^^<span class="mark">XXXXXXXXXX</span>^<span class="mark">XX</span>^^^N\|\|\|\|\|M\|25\|\|000001111\|\|\|\|<span class="mark">XXXXXXXXXX</span> <span class="mark">XX</span>\|N\|\|\|\|\|\|\|

PV1\|1\|I\|\|\|\|^^\|115^LRPROVIDER^ONE^^JR^DR^MD\|\|\|1\|\|\|\|\|\|\|\|NSC VETERAN\|\|\|15\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|522\|\|\|\|\|20060106105459-0500\|

ORC\|RE\|2209000007^LR\|2209000007^LR\|\|\|\|\|\|\|\|\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\|\|522^ZZ <span class="mark">XXXXXX</span>^99VA4

OBR\|1\|2209000007^LR\|2209000007^LR\|88515.0000^Surgical Pathology Procedures NOS^99VA64\|\|\|20090304\|\|\|\|\|\|\|200903041341-0500\|20677005&Iliac crest bone marrow (body structure)&SCT&776&BONE MARROW, ILIAC CREST&99VA61&20060101&5.2&BONE MARROW, ILIAC CREST\|1111111112^LRPROVIDER^ONE^^JR^DR^MD^^USDHHS^^2^NPI^NPI\|\|\|\S\\S\\S\\S\\S\\S\2209000007\|356\S\SP\S\6909694.8659\|NSP 09 7\S\15\S\3090000\S\7\S\SURGICAL PATHOLOGY\S\NSP\S\88515.0000\|20090304174007-0500\|\|SP\|F\|\|\|\|\|\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|1111111112&LRPROVIDER&ONE&&JR&DR&MD&&USDHHS^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|^^^^^^522&FS.FO-<span class="mark">XXXXXX.XXX.XX.XXX</span>&DNS\|\|\|\|\|\|\|\|\|88399^SURGICAL PATHOLOGY PROCEDURE^C4^88515.0000^Surgical Pathology Procedures NOS^99VA64

OBX\|1\|CWE\|22633-2^Path report.site of origin:Anat:Pt:Specimen:Nar^LN^4664583^^99VA95.3^2.19^2.19\|SPEC-1\|20677005^Iliac crest bone marrow (body structure)^SCT^776^BONE MARROW, ILIAC CREST^99VA61^20060101^5.2^Bone Marrow, core \#1\|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|2\|CWE\|22633-2^Path report.site of origin:Anat:Pt:Specimen:Nar^LN^4664583^^99VA95.3^2.19^2.19\|SPEC-2\|20677005^Iliac crest bone marrow (body structure)^SCT^776^BONE MARROW, ILIAC CREST^99VA61^20060101^5.2^Bone Marrow, core \#2\|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|3\|FT\|22636-5^Path report.relevant Hx:Find:Pt:Specimen:Nar^LN^4664586^^99VA95.3^2.19^2.19\|\|Unexplained decrease in platelet count over 12 month period. \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|4\|FT\|10219-4^Operative note preoperative Dx:Imp:Pt:\R\Patient:Nar^LN^4651469^^99VA95.3^2.19^2.19\|\|The field contains the patient's pre-operative diagnosis which is usually provided by the surgeon. \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|5\|FT\|10215-2^Operative note findings:Find:Pt:\R\Patient:Nar^LN^4651465^^99VA95.3^2.19^2.19\|\|This is the surgeon's operative finding after the operation has been completed. \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|6\|FT\|10218-6^Operative note postoperative Dx:Imp:Pt:\R\Patient:Nar^LN^4651468^^99VA95.3^2.19^2.19\|\|Post-operative Diagnosis: Thrombocytopenia \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|7\|FT\|22634-0^Path report.gross observation:Find:Pt:Specimen:Nar^LN^4664584^^99VA95.3^2.19^2.19\|\|Very floppy ear received in basket. Domestic dispute? Seriously doubt that specimen is actually a bone marrow from a human. Submitted by Dr. Mickey J Mouse MD \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|8\|FT\|22635-7^Path report.microscopic observation:Prid:Pt:Specimen:Nar:XXX stain^LN^4664585^^99VA95.3^2.19^2.19\|\|A lot of little short hairs. Looks like they caught the little fella by the proverbial "short Hairs". What a way to go on a Sunday. \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

OBX\|9\|FT\|22637-3^Path report.final diagnosis:Imp:Pt:Specimen:Nar^LN^4664587^^99VA95.3^2.19^2.19\|\|In the case of a surgical case, we could choose to type the original post-operative findings of the case directly at this prompt \\br\\ \\br\OR We could choose to upload a previously typed operative findings for this case at this prompt. \\br\\.br\OR We could choose to type in only the diagnosis with some additional information indicating that the case was read at XYZ Hospital as follows: \\br\\ \\br\DIAGNOSIS: Ear, right, punch biopsy - fatal \\br\\.br\Submitted by Dr. Lab Provider, One. \|\|\|\|\|\|F\|\|\|200903041341-0500\|522^ZZ <span class="mark">XXXXXX</span>^99VA4^987654321^^99VACLIA\|235-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ <span class="mark">XXXXXX</span>^D^^^^CLIA^LN^^A^987654321\|^Building 456^^<span class="mark">XX</span>^^USA

### Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA supports enhanced mode acknowledgments. Upon receipt of the result message, the receiving system responds with a general acknowledgment (ACK) message. The ACK message consists of the following segments. For this ‘broadcast’ type interface, VistA Laboratory does not expect or require application level acknowledgments. Commit acknowledgments are implemented to insure delivery to subscribers.

ACK General Acknowledgment Message

| Value | Description        |
|-------|------------------------|
| MSH   | Message Header         |
| MSA   | Message Acknowledgment |

Example: ACK General Acknowledgment message

MSH^~\|\\^LA7HDR^200HD~HDR.MED.VA.GOV~DNS ^LA7LAB^170~FS.ISC-<span class="mark">XXXXXX.XXX.XX.XXX</span>~DNS ^19970515093728^^ACK~R01^269^T^2.4

MSA^CA^229

# Communication Requirements for HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section specifies the requirements necessary to establish and maintain communications between VistA and all the participating systems. It includes requirements that must be satisfied by VistA, by all the participating systems, and by each system when sending or receiving a message.

## Using TCP/IP and HL7 Minimal Lower Level Protocol 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interface between VistA and each participating system is established through a persistent or a transient (non-persistent) TCP/IP connection. Two TCP sockets provide bi-directional communications between each participating system.

Within the context of the TCP socket, each participating system connects as the client when it initiates a message. The other system connects as the server to receive messages from the listen state.

### Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The participating system initiates the interface by establishing a TCP Server Socket. The participating system that initiates a message connects to the participating system TCP Server Socket as a TCP Client.

### TCP/IP Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA has a client (sender) process for each remote system to send HL7 messages. This process requires a TCP socket. The client process sends HL7 messages to the remote system and receives accept acknowledgment messages from the remote system. The diagram depicts the sequence of events for an outbound message regarding messages and acknowledgments.

![](la-5-2-68-laboratory-hl7-specification/003.png)

### Flow Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface uses the HL7 Minimal Lower Layer Protocol (MLLP) to format messages for data interchange, including acknowledgment messages. This protocol relies on the Message Header Segment (MSH) to define encoding, routing and acknowledgment rules governing the message.

### VistA Client/Server Process Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flow of messages between VistA and the remote system can be controlled by the VistA client process parameters. The parameters for the client/server process are definable at each installation site and can be customized for each remote system.

Examples of parameters

- Server IP addresses/ports
- Client IP addresses/ports
- Number of attempts to open a socket
- Hang time for the client process between attempts to send a message
- Maximum number of times the client process attempts to send a message
- Persistent/non-persistent client connection
- Retention time for client connection to keep a non-persistent connection established

### Automated Recovery Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When either side of the interface is disabled for any reason during any TCP connection, the remaining side begins its automatic recovery procedures.

- If the remote system (TCP server) detects that VistA (TCP client) becomes disabled, the remote system resets to listen mode.
- If VistA detects that the remote system becomes disabled, VistA resets to attempt connect state.

VistA continues to attempt the reconnect for a site-specified number of times or for a site-specified period of time, before logging the situation and terminating.

### Message Transmission Retry Attempts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the remote system is down, and VistA cannot transmit a message to the remote system, VistA waits for a specified period of time (default is one minute) before attempting to resend the message. VistA retries until the specified maximum number of attempts (default is 2) is reached.

### Error Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA and the participating systems use automated procedures to detect when connectivity is lost and to initiate recovery procedures. VistA and the participating systems use the HL7 2.4 enhanced acknowledgment mode, so the receiving system may respond to the message with an accept acknowledgment. When the receiving system commits the message to safe storage in a manner that releases the sending system from the need to retransmit the message, it sends a positive accept acknowledgment.

Accept acknowledgments are used for all messages and the value passed in the Accept Acknowledgment field of the MSH segment (MSH-15) of the originating message is observed. Application Acknowledg­ments are not used.

#### Requirements

1.  If VistA detects a remote end disconnect, it attempts to reconnect to the participating system TCP Server Socket for a locally defined number of retry attempts.
12. If VistA detects a remote end disconnect and is unable to reconnect to the participating system after a locally defined number of retry attempts, it shall log an error.
13. If the participating system detects a remote end disconnect, it closes the channel of its TCP Server Socket and awaits VistA reconnection.
14. The *receiving* system returns an accept acknowledgment with a Commit Accept (CA) status to the *sending* system for each incoming HL7 Message in which the Message Header Segment (MSH) conforms to the following criteria:
1.  The first segment is a Message Header Segment (MSH);
24. The Message Type Field (MSH-9) contains a valid message type; and
25. The Message Control ID Field (MSH-10) contains an ID.
15. The *receiving* system returns an accept acknowledgment with a Commit Reject (CR) status to the *sending* system for each incoming HL7 message in which the Message Header Segment (MSH) fails to conform to the following criteria:
1.  The first segment is a Message Header Segment (MSH)
26. The Sending Application (MSH-3) is valid
27. The Sending Facility (MSH-4) is valid
28. The Receiving Application (MSH-5) is valid
29. The Receiving Facility (MSH-6) is valid
30. The Message Type Field (MSH-9) contains a valid message type
31. The Message Control ID Field (MSH-10) contains a message ID
32. The Message Processing ID (MSH-11) contains the appropriate value for the systems communicating
33. The Message Version ID contains 2.4
16. The *receiving* system returns an accept acknowledgment with a Commit Error (CE) status to the *sending* system for each incoming HL7 message that it did not accept, for any reasons other than those requiring a Commit Reject (CR).
17. Upon receipt of an accept acknowledgment with either a Commit Reject (CR) or Commit Error (CE) status from the *receiving* system, the *sending* system ceases transmission of the original HL7 message.