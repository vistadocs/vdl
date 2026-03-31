---
title: LA*5.2*80/LR*5.2*427 LDSI/LEDI IV Update HL7 Interface Specification
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*80
group_key: "LEDI:LA:5.2"
file_numbers: 
  - 62
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - code
  - vista
  - identifier
  - contains
  - specimen
  - message
  - mark
  - span
  - number
page_count: 0
word_count: 27177
section_count: 22
table_count: 56
figure_count: 9
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/la_52_74_la_52_80_hl7_interface_spec.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/la_52_74_la_52_80_hl7_interface_spec.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-hl7-interface-specification/001.png)

VA Shield

LEDI IV  
HL7 Interface Specification

Laboratory  

Revised for

Patches LA\*5.2\*74 and LA\*5.2\*80

September 2013

VistA Health Systems Design & Development

Revision History

<table>
<caption><p>Table 1. VistA Laboratory Subscript</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 27%" />
<col style="width: 33%" />
<col style="width: 14%" />
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
<td>08/13/04</td>
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
<td><p>U[Added ORD-17</p>
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
<td>03/14/06</td>
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
<td>12/10/07</td>
<td>1.33</td>
<td>Added OBR-25</td>
<td>OBR section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/03/08</td>
<td>1.34</td>
<td><p>Added OBR-44</p>
<p>Added OBX-25</p></td>
<td><p>OBR section</p>
<p>OBX section</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/26/08</td>
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
<td>September 2009</td>
<td>1.36</td>
<td>Reformat and update to OED Documentation Standards</td>
<td>Entire document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2010</td>
<td>1.36</td>
<td><p>Added J McCormick updates</p>
<p>Changed dates to Month 2010</p></td>
<td>Entire document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>August 2013</td>
<td>4.0</td>
<td><p>Updated HL7 field definitions, LOINC tables, and examples.</p>
<p>Added definitions for ORM segments.</p></td>
<td>Entire Document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>August 2013</td>
<td>4.1</td>
<td><p>Updated that HL7 ORU messaging is disabled for AP</p>
<p>Removed BB from HL7 Table 0074</p>
<p>Added example for CH ORM message</p></td>
<td><p>1 Introduction</p>
<p>2.4.1.6 OBR-24</p>
<p>3.3.1.1 Example of Chemistry/Hematology/Serology Order Message</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Sept 2013</td>
<td></td>
<td>Technical edit</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table 1. VistA Laboratory Subscript

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
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
- [HL7 Segments in ACK, ORM, ORR, and ORU Messages](#hl7-segments-in-ack-orm-orr-and-oru-messages)
  - [MSA Segment Fields in ORM and ORU](#msa-segment-fields-in-orm-and-oru)
    - [MSA Field Definitions](#msa-field-definitions)
  - [MSH Segment Fields in ORM and ORU](#msh-segment-fields-in-orm-and-oru)
    - [MSH Field Definitions](#msh-field-definitions)
  - [NTE Segment Fields in ORM and ORU](#nte-segment-fields-in-orm-and-oru)
    - [NTE Field Definitions](#nte-field-definitions)
  - [OBR Segment Fields in ORU](#obr-segment-fields-in-oru)
    - [OBR Field Definitions](#obr-field-definitions)
  - [OBR Segment Fields in ORM](#obr-segment-fields-in-orm)
    - [OBR Field Definitions](#obr-field-definitions-1)
  - [OBX Segment Fields in ORU](#obx-segment-fields-in-oru)
    - [OBX Field Definitions](#obx-field-definitions)
  - [OBX Segment Fields in ORM](#obx-segment-fields-in-orm)
    - [OBX Field Definitions](#obx-field-definitions-1)
  - [ORC Segment Fields in ORU](#orc-segment-fields-in-oru)
    - [ORC Field Definitions](#orc-field-definitions)
  - [ORC Segment Fields in ORM](#orc-segment-fields-in-orm)
    - [ORC Field Definitions](#orc-field-definitions-1)
  - [PID Segment Fields in ORM](#pid-segment-fields-in-orm)
    - [PID Field Definitions](#pid-field-definitions)
  - [PID Segment Fields in ORU](#pid-segment-fields-in-oru)
    - [PID Field Definitions](#pid-field-definitions-1)
  - [PV1 Segment Fields in ORM and ORU](#pv1-segment-fields-in-orm-and-oru)
    - [PV1 Field Definitions](#pv1-field-definitions)
  - [BLG Segment Fields in ORM](#blg-segment-fields-in-orm)
    - [BLG Field Definitions](#blg-field-definitions)
- [Transaction Specifications](#transaction-specifications)
  - [General](#general)
  - [Specific Message Consideration](#specific-message-consideration)
    - [Microbiology](#microbiology)
    - [Bacteriology](#bacteriology)
    - [Surgical Pathology](#surgical-pathology)
    - [Cytopathology](#cytopathology)
    - [Electron Microscopy](#electron-microscopy)
  - [Specific Transactions](#specific-transactions)
    - [Order Message](#order-message)
    - [Order Message Acknowledgments](#order-message-acknowledgments)
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
The Laboratory Electronic Data Interchange (LEDI) IV patches, LA\*5.2\*74/LR\*5.2\*350 and LA\*5.2\*80/LR\*5.2\*427, enhance a bi-directional interface that allows Department of Veterans Affairs (VA) laboratories to communicate with other VA facilities, Commercial Reference Laboratories, and Department of Defense (DoD). Included in these enhancements, is the support for the electronic exchange of Anatomic Pathology (AP) and Microbiology (Micro) orders and results over the LEDI interface. (At this time the outgoing HL7 result (ORU) messaging is disabled for AP).
This document contains the specifications for the interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard for LEDI IV. The interface forms the basis for the exchange of healthcare information between the VistA Laboratory software application and the DoD Composite Health Care System (CHCS). It is a point-to-point type of interface in which VistA Laboratory exchanges orders (ORM) and results (ORU) messages with CHCS. The interface supports several areas of VistA Laboratory. Additionally, it supports current interfaces that exist between VA Medical Centers (VAMCs) and between VAMCs and commercial reference laboratories.
| VistA Laboratory Subscript | Traditional Functional Sections                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| CH                         | Chemistry, Hematology, Coagulation, Serology, Urinalysis, etc.                        |
| MI                         | Microbiology (i.e., Bacteriology, Virology, Mycology, Parasitology, Mycobacteriology) |
| SP                         | Surgical Pathology                                                                    |
| CY                         | Cytopathology                                                                         |
| EM                         | Electron Microscopy                                                                   |
Table 2. Segment Definition Tables

## Statement of Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of Information developed and implemented an interface to the HL7 Standard for use by the VistA Laboratory application in communicating with DoD CHCS systems to exchange healthcare information. The interface adheres to the HL7 Standard and avoids using Z type extensions to the Standard. This interface specification is subject to modification and revision to incorporate changes, improvements, and enhancements.

Later versions may support additional functionality of the current HL7 v2.4 Standard and new functionality released in future versions of the HL7 Standard. In some cases, data types are pre-adopted from other versions of the HL7 standard when they are more appropriate to convey required information.

This specification supports the following uses:

- VA Medical Center interfacing with a DoD Laboratory within the Laboratory Data Sharing Interoperability (LDSI) program, where VA and DoD laboratories entered into a business relationship to share resources.
- VA Medical Center interfacing with another VA Medical Center to share laboratory resources.
- VA Medical Center interfacing with a commercial reference laboratory that entered into a business relationship for the commercial reference laboratory to provide laboratory-testing services.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes messages transmitted from the VistA Laboratory application system. The purpose of these messages is to exchange information concerning laboratory orders and results, specifically for test orders and reports.

## Overview of HL7 Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sections 1.3.1 through 1.3.6 define terms and concepts used throughout this interface specification.

### Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard defines only the seventh level of the Open System Inter-connect (OSI) protocol. This is the application level. Levels 1-6 primarily involve communication protocols. The HL7 Standard provides some guidance in this area. The communication Standard used for interfacing with the VistA Laboratory package is based on the HL7 Minimal Lower Level (MLLP) Standard as described in the HL7 Interface Standard document.

### Application Processing Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard describes the basic rules for application processing by the exchange of *sending* and *receiving* messages between systems. Information contained in the Standard is not repeated in this document. Interfacing with the VistA Laboratory package requires familiarization with the HL7 Standard v 2.x.

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message is the unit of data transferred between systems. It comprises a group of segments in a defined sequence. Each message has a message type that defines its purpose. A three-character code contained within each message identifies its type. The event that initiates an exchange of messages is called a trigger event. VistA Laboratory uses four HL7 messages.

| ACK | General Acknowledgment            |
|-----|-----------------------------------|
| ORM | Order                             |
| ORR | Order Response                    |
| ORU | Observational Results Unsolicited |

Table 3. Data Type

### Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or may be allowed to repeat. Each segment has a name and is identified by a unique three-character code known as the Segment ID.

For details and examples of all segments used to interface with the VistA Laboratory software application, refer to [Section 3 Transaction Specifications](#_Transaction_Specifications). The following HL7 segments are used to support the exchange of Laboratory information.

| MSA | Message Acknowledgment |
|-----|------------------------|
| MSH | Message Header         |
| NTE | Notes and Comment      |
| OBR | Observation Request    |
| OBX | Observation            |
| ORC | Common Order           |
| PID | Patient Identification |
| PV1 | Patient Visit          |
| BLG | Billing Segment        |

Table 4. MSA Segment Fields in ORM and ORU

The segment definition tables list and describe the data fields in the segment and the characteristics of usage, as well as the properties of each HL7 segment. These terms display in the headings of the segment tables.

<table>
<caption><p>Table 5. HL7 Table 0008 Acknowledgment Code</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
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
<p>R–required<br />
O (null)–optional<br />
C–conditional on the trigger event</p></td>
</tr>
<tr class="odd">
<td>VA R/O/C</td>
<td><p>VA (R/O/C) indicates whether the data field is required, optional, or conditional in a segment used by the Department of Veterans Affairs (VA).</p>
<p>R–required</p>
<p>O (null)–optional<br />
C–conditional on the trigger event</p></td>
</tr>
<tr class="even">
<td>RP/#</td>
<td><p>Repetition indicates the number of times you can repeat a field.</p>
<p>N (null)–no repetition allowed</p>
<p>Y–the field may repeat an indefinite or site determined number of times</p>
<p>(integer)–you can repeat the field the number of times specified by the integer</p></td>
</tr>
<tr class="odd">
<td>TBL#</td>
<td><p>Table attribute of the data field defined by the HL7 standard (for a set of coded values) or negotiated between the VistA Laboratory application and the vendor system.</p>
<p>Local tables used by the VA begin with the prefix 99VA.</p></td>
</tr>
<tr class="even">
<td>Element Name</td>
<td>Globally unique, descriptive name for the field</td>
</tr>
</tbody>
</table>

Table 5. HL7 Table 0008 Acknowledgment Code

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. The HL7 Messaging Standard does not specify how systems must store data within an application. Fields are transmitted as character strings.

### Data Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data type identifies the restrictions on the contents of a data field. HL7 defines a number of data types. This information is in a column labeled DT in the segment attribute tables in the HL7 Messaging Standards.

| Data Type | Data Type Name                                          |
|-----------|---------------------------------------------------------|
| AD        | Address                                                 |
| CD        | Channel definition                                      |
| CE        | Coded element                                           |
| CF        | Coded element with formatted values                     |
| CK        | Composite ID with check digit                           |
| CM        | Composite                                               |
| CN        | Composite ID number and name                            |
| CNE       | Coded with no exceptions                                |
| CP        | Composite price                                         |
| CQ        | Composite quantity with units                           |
| CWE       | Coded with exceptions                                   |
| CX        | Extended composite ID with check digit                  |
| DLN       | Driver's license number                                 |
| DR        | Date/time range                                         |
| DT        | Date                                                    |
| ED        | Encapsulated data                                       |
| EI        | Entity identifier                                       |
| FC        | Financial class                                         |
| FN        | Family name                                             |
| FT        | Formatted text                                          |
| HD        | Hierarchic designator                                   |
| ID        | Coded values for HL7 tables                             |
| IS        | Coded value for user-defined tables                     |
| JCC       | Job code/class                                          |
| MA        | Multiplexed array                                       |
| MO        | Money                                                   |
| NA        | Numeric array                                           |
| NM        | Numeric                                                 |
| PL        | Person location                                         |
| PN        | Person name                                             |
| PPN       | Performing person time stamp                            |
| PT        | Processing type                                         |
| QIP       | Query input parameter list                              |
| QSC       | Query selection criteria                                |
| RCD       | Row column definition                                   |
| RI        | Repeat interval                                         |
| RP        | Reference pointer                                       |
| SAD       | Street address                                          |
| SCV       | Scheduling class value pair                             |
| SI        | Sequence ID                                             |
| SN        | Structured numeric                                      |
| SRT       | Sort order                                              |
| ST        | String                                                  |
| TM        | Time                                                    |
| TN        | Telephone number                                        |
| TQ        | Timing/quantity                                         |
| TS        | Time stamp                                              |
| TX        | Text data                                               |
| VH        | Visiting hours                                          |
| VID       | Version identifier                                      |
| XAD       | Extended address                                        |
| XCN       | Extended composite ID number and name                   |
| XON       | Extended composite name and ID number for organizations |
| XPN       | Extended person name                                    |
| XTN       | Extended telecommunications number                      |

Table 6. MSH Segment Fields in ORM and ORU

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Messaging Standard version 2.x American National Standards Institute, 2000  
  <https://www.hl7.org/library/bookstore/>
- HL7 Technical Documentation  
  <span class="mark">REDACTED</span>
- Messaging & Interface Services (M&IS)  
  <span class="mark">REDACTED</span>
- VA Software Document Library (VDL), Laboratory Electronic Data Interchange (LEDI), Clinical Section Version 5.2  
  <http://www.va.gov/vdl/application.asp?appid=75>

# HL7 Segments in ACK, ORM, ORR, and ORU Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 segment fields support the exchange of laboratory data in ACK, ORM, ORR, and ORU messages.

Tables referenced in the segments are found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for the fields that are utilized. The field definitions can include specific information, such as, expected format for transmission.

## MSA Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSA segment contains information sent in response to receiving a message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name        |
|-----|-----|-----|-------|----------|-----|------|---------------------|
| 1   | 2   | ID  | R     | R        |     | 0008 | Acknowledgment Code |
| 2   | 20  | ST  | R     | R        |     |      | Message Control ID  |
| 3   | 80  | ST  | O     | RE       |     |      | Text Message        |

Table 7. HL7 Table 0103 Processing ID

### MSA Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSA-1 Acknowledgment Code (ID)

This field contains one of the following values.

| Value | Description                                         | VA Usage |
|-------|-----------------------------------------------------|----------|
| CA    | Enhanced mode: Accept Acknowledgment: Commit Accept | Used     |
| CE    | Enhanced mode: Accept Acknowledgment: Commit Error  | Used     |
| CR    | Enhanced mode: Accept Acknowledgment: Commit Reject | Used     |
| AA    | Application Accept                                  | Used     |
| AE    | Application Error                                   | Used     |
| AR    | Application Reject                                  | Used     |

Table 8. HL7 Table 0104 Version ID

#### MSA-2 Message Control ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the sent message.

#### MSA-3 Text Message (ST)

This field is optional text that describes an error condition. The text may be printed in error logs or presented to an end user.

## MSH Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name                    |
|-----|-----|-----|-------|----------|-----|------|---------------------------------|
| 1   | 1   | ST  | R     | R        |     |      | Field Separator                 |
| 2   | 4   | ST  | R     | R        |     |      | Encoding Characters             |
| 3   | 15  | ST  | O     | R        |     |      | Sending Application             |
| 4   | 20  | ST  | O     | R        |     |      | Sending Facility                |
| 5   | 30  | ST  | O     | R        |     |      | Receiving Application           |
| 6   | 30  | ST  | O     | R        |     |      | Receiving Facility              |
| 7   | 26  | TS  | R     | R        |     |      | Date/Time of Message            |
| 9   | 7   | CM  | R     | R        |     | 0076 | Message Type                    |
| 10  | 20  | ST  | R     | R        |     |      | Message Control ID              |
| 11  | 1   | ID  | R     | R        |     | 0103 | Processing ID                   |
| 12  | 8   | ID  | R     | R        |     | 0104 | Version ID                      |
| 15  | 2   | ID  | O     | RE       |     | 0155 | Accept Acknowledgment Type      |
| 16  | 2   | ID  | O     | RE       |     | 0155 | Application Acknowledgment Type |

Table 9. HL7 Table 0155 Accept/Application Acknowledgment Conditions

### MSH Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The segment terminator is always a carriage return (in ASCII, a hex 0D). The other delimiters are defined in the MSH segment, with the field delimiter in the fourth character position, and the other delimiters occurring as in the field called Encoding Characters. The Encoding Characters field is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the message.

#### MSH-1 Field Separator (ST)

This field contains the separator between the segment ID and the first real field, MSH-2–Encoding Characters. This field defines the character to be used as a separator for the rest of the message.

VistA Laboratory does not have pre-defined field separators. Applications are advised to use the value of this field to determine the field separator used throughout the message.

#### MSH-2 Encoding Characters (ST)

This field contains four characters in the following order: component separator, repetition separator, escape character, and subcomponent separator.

VistA Laboratory does not have pre-defined encoding characters. Applications are advised to use the value of this field to determine the encoding characters used throughout the message.

#### MSH-3 Sending Application (ST)

This field contains the interface used with lower level protocols.

- LA7V REMOTE \# to identify the remote ordering site.
- LA7V HOST \# to identify the Host testing site.
- When \# refers to a VA facility, it represents the VA station number from INSTITUTION file (#4), Station Number field (#99).
- When \# refers to a DoD facility it represents the DOD DMIS ID code assigned by DoD to the facility.
- When \# refers to a commercial reference laboratory, it represents the three-letter code the VA facility assigned to the reference lab via LAB SHIPPING CONFIGURATION file (#62.9), Other System Identifier field (#.11).

#### MSH-4 Sending Facility (ST)

This field contains one of several occurrences of the same application within the sending system. This field is the three-digit number identifying the medical center division, as in the VistA INSTITUTION file (#4), Station Number field (#99). For DoD facilities, this field is the DOD DMIS code. For commercial labs, this field is the three-letter code the VA facility assigned to the reference lab.

#### MSH-5 Receiving Application (ST) 

Refer to Sending Application. The actual application name of the subscriber is entered into this field by the VistA HL package when addressing the message to each subscriber.

#### MSH-6 Receiving Facility (ST)

Refer to Sending Facility. The actual facility identifier of the subscriber is entered into this field by the VistA HL package when addressing the message to each subscriber.

#### MSH-7 Date/Time of Message (TS)

This field contains the date/time the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

#### MSH-9 Message Type (CM)

This field contains a composite element made up of the following:

\<message type\> \<trigger event\>

- The first component is the message type, found in HL7 Table 0076 – Message Type.
- The second component is the trigger event code found in HL7 Table 0003 – Event Type Code.

The receiving system uses this field to recognize the data segments, and possibly the application to which to route this message.

#### MSH-10 Message Control ID (ST)

This field contains a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment (MSA) segment.

#### MSH-11 Processing ID (ID)

This field contains whether or not to process the message as defined in the HL7 application processing rules.

| Value | Description |
|-------|-------------|
| D     | Debugging   |
| P     | Production  |
| T     | Training    |

Table 10. HL7 Table 0155 Accept/Application Acknowledgment Conditions

#### MSH-12 Version ID (ID)

This field contains a match to the receiving system of its own version to be sure the message is interpreted correctly.

| Value | Description                |
|-------|----------------------------|
| 2.1   | Released 2.1 March 1990    |
| 2.2   | Released 2.2 December 1994 |
| 2.3   | Released 2.3 May 1997      |
| 2.3.1 | Released 2.3.1 May 1999    |
| 2.4   | Released 2.4 November 2000 |

Table 11. NTE Segment Fields in ORM and ORU

> **NOTE:** DoD CHCS requires V. 2.2.

- When communicating with a VA or commercial lab system, v. 2.3 will be used.
- When communicating with DoD, v. 2.2 will be used.

#### MSH-15 Accept Acknowledgment Type (ID)

This field contains the definitions of the conditions under which accept acknowledgments must be returned in response to this message.

| Value | Description                  |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

Table 12. User-defined Table 0105 - Source of Comment

#### MSH-16 Application Acknowledgment Type (ID)

This field contains the definitions of the conditions under which application acknowledgments are required in response to this message.

| Value | Description                  |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

Table 13. User-defined Table 0364 - Comment Type

## NTE Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NTE segment is used to report the Laboratory notes or comments.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name                |
|-----|-----|-----|-------|----------|-----|------|-----------------------------|
| 1   | 4   | SI  | O     | R        |     |      | Set ID - Notes and Comments |
| 2   | 8   | ID  | O     | RE       |     | 0105 | Source of Comment           |
| 3   | 64k | FT  | O     | R        | Y   |      | Comment                     |
| 4   | 250 | CE  | O     | RE       |     | 0364 | Comment Type                |

Table 14. OBR Segment Fields in ORU

### NTE Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NTE-1 Set ID - Notes and Comments (SI)

This field contains the location of multiple NTE segments in a message.

#### NTE-2 Source of Comment (ID)

This field is encoded by VistA Laboratory.

When communicating with DoD facilities, the following codes are used: comments that contain the name/address of the performing laboratory, use code DS; comments pertaining to test interpretation information, use code RI; comments pertaining to the report, use code RC; comments that contain the specimen source, use code RQ; all other comments use code AC.

When communicating with non-DoD facilities, only the code L is used.

| Value | Description                                                         | Comment                                          |
|-------|---------------------------------------------------------------------|--------------------------------------------------|
| L     | Ancillary (filler) department is source of comment                  | Used when communicating with non-DoD facilities. |
| DS    | Comments that contain the name/address of the performing laboratory | Used when communicating with DoD facilities.     |
| RI    | Comments pertaining to test interpretation information              | Used when communicating with DoD facilities.     |
| RC    | Comments pertaining to the report                                   | Used when communicating with DoD facilities.     |
| RQ    | Comments that contain the specimen source                           | Used when communicating with DoD facilities.     |
| AC    | All other comments                                                  | Used when communicating with DoD facilities.     |

Table 15. HL7 Table 0065 - Specimen Action Code

#### NTE-3 Comment (FT)

This field contains the comment associated with the specimen and/or a specific test.

#### NTE-4 Comment Type (CE)

This field contains the comment type.

- VA user-defined entries (VA-LR\*) indicate the type of comments and their source within a VistA Laboratory report.
- Entries (VA-LRMI\*) indicate Microbiology (MI-subscript) report comments. They are used when a microbiology report (MI subscript) contains comments that follow an OBR segment and describe the nature of the microbiology comment.

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
| VA-LRMI022 | Parasite Test(s) (#16.4)             | Lab microbiology comment              |
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

Table 16. Specimen Received Date/Time (TS) Field

## OBR Segment Fields in ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the reporting of clinical data, the OBR serves as the report header. The OBR segment identifies the observation set represented by the following observations.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name                  |
|-----|-----|-----|-------|----------|-----|------|-------------------------------|
| 1   | 4   | SI  | C     | R        |     |      | Set ID - Observation Request  |
| 2   | 22  | EI  | C     | R        |     |      | Placer Order Number           |
| 3   | 22  | EI  | C     | R        |     |      | Filler Order Number           |
| 4   | 250 | CE  | R     | R        |     |      | Universal Service ID          |
| 7   | 26  | TS  | C     | R        |     |      | Observation Date/Time         |
| 11  | 1   | ID  | O     | RE       |     | 0065 | Specimen Action Code          |
| 12  | 60  | CE  | O     | RE       |     |      | Danger Code                   |
| 14  | 26  | TS  | C     | RE       |     |      | Specimen Received Date/Time   |
| 15  | 300 | CM  | O     | R        |     | 0070 | Specimen Source               |
| 16  | 60  | XCN | O     | RE       | Y   |      | Ordering Provider             |
| 18  | 60  | ST  | O     | RE       |     |      | Placer Field \#1              |
| 19  | 60  | ST  | O     | RE       |     |      | Placer Field \#2              |
| 20  | 60  | ST  | O     | RE       |     |      | Filler Field \#1              |
| 21  | 60  | ST  | O     | RE       |     |      | Filler Field \#2              |
| 22  | 26  | TS  | O     | RE       |     |      | Results Rpt/Status Chng - D/T |
| 24  | 10  | ID  | O     | R        |     | 0074 | Diagnostic Serv Sect ID       |
| 25  | 1   | ID  | C     | CE       |     | 0123 | Result Status                 |
| 26  | 200 | CM  | O     | RE       |     |      | Parent Result                 |
| 29  | 200 | CM  | O     | RE       |     |      | Parent                        |
| 32  | 200 | CM  | O     | CE       |     |      | Principle Result Interpreter  |
| 33  | 200 | CM  | O     | CE       | Y   |      | Assistant Result Interpreter  |
| 34  | 200 | CM  | O     | CE       | Y   |      | Technician                    |
| 35  | 200 | CM  | O     | CE       | Y   |      | Transcriptionist              |
| 44  | 250 | CE  | O     | RE       |     | 0088 | Procedure Code                |

Table 17. Specimen Source (CM) Field

### OBR Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBR-1 Set ID - Observation Request (SI)

This field contains a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

#### OBR-2 Placer Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the placer. The first component contains the collecting site’s unique accession identifier. The placer order number sent in the ORM message is returned with the results.

This field is populated from the ORDERING SITE UID field (#16.4) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### OBR-3 Filler Order Number (EI) 

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

This field is a permanent identifier for an order and its associated observations on the system of the filler. The first component is filled in with the VistA unique accession number. The filler order number is returned with the results.

This field is populated from the HOST UID field (#16.3) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### OBR-4 Universal Service ID (CE)

This field contains a coded element made up of the following:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^\<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

This field is an identifier code for the requested observation or ordered test. This can be based on local and/or universal codes.

The Universal Service ID from the collecting site sent in the ORM message is returned.

If this test did not originate from the collecting site (e.g., it was an add-on or reflex test), the WKLD CODE file (#64) is used to identify the observed test. It contains the VA National Laboratory Test code. The LABORATORY TEST file (#60) is used to populate the alternate coding system. Future versions may utilize LOINC codes as the coding system.

\<NLT code (File \#64 Field \#1)\>^\<text\>^\<99VA64\>^\<Lab Test IEN\>^\<Lab Test Name (File \#60 Field \#.01)\>^\<99VA60\>

#### OBR-7 Observation Date/Time (TS)

This field contains the clinically relevant date/time of the observation. This is the date and time of the specimen collection. Value for this field is derived from Date/Time Specimen Taken field (#.01) within the VistA LAB DATA file (#63).

If the collection time is estimated or unknown, only the date will be sent back (without a time).

#### OBR-11 Specimen Action Code (ID)

This field contains the action to take with respect to the specimens that accompany or precede the order. The purpose of this field is to further qualify (when appropriate) the general action indicated by the order control code contained in the accompanying ORC segment.

| Value | Description                                    | Comment       |
|-------|------------------------------------------------|---------------|
| A     | Add ordered tests to the existing specimen     | Used by VistA |
| G     | Generated order; reflex order                  | Used by VistA |
| L     | Lab to obtain specimen from patient            |               |
| O     | Specimen obtained by service other than Lab    |               |
| P     | Pending specimen; Order sent prior to delivery | Used by VistA |
| R     | Revised order                                  | Used by VistA |
| S     | Schedule the tests specified below             |               |

Table 18. VistA LAB DATA File (#63) Fields to Derive Topography

#### OBR-12 Danger Code (CE)

This field contains the code and/or text indicating any known or suspected patient or specimen hazards, such as, patient with active tuberculosis or blood from a hepatitis patient. Either code and/or text may be absent. However, the code is always placed in the first component position and any free text in the second component position. Free text without a code must be preceded by a component delimiter.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

The Danger Code contains the information located within the LAB DATA file (#63) Pat. Info. field (#.091). VistA does not code this information. It is transmitted as text and occurs in the second component of this field.

#### OBR-14 Specimen Received Date/Time (TS)

This field contains the actual time of arrival of a specimen at the diagnostic service. Depending on the nature of the test, the value for this field is derived from the following fields within VistA.

| Subscript | File                 | Subfile | Field                             |
|-----------|----------------------|---------|-----------------------------------|
| CH        | ACCESSION file (#68) | 68.02   | Lab Arrival Time (#12)            |
| CY        | LAB DATA file (#63)  | 63.09   | Date/Time Specimen Received (#.1) |
| EM        | LAB DATA file (#63)  | 63.02   | Date/Time Specimen Received (#.1) |
| MI        | LAB DATA file (#63)  | 63.05   | Date/Time Received (#.1)          |
| SP        | LAB DATA file (#63)  | 63.08   | Date/Time Specimen Received (#.1) |

Table 19. VistA LAB DATA File (#63) Fields to Derive Collection Sample

> **NOTE:** Chemistry/Hematology (CH) – The Chem, Hem, Tox, Ria, Ser, etc. subfile (#63.04) within the Lab Data file (#63) does not support the Date/Time Specimen Received field. Therefore, for this subscript, the system attempts to populate this field from the LAB ARRIVAL TIME field (#12) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### OBR-15 Specimen Source (CM)

This field contains the information on the specimen source.

Components

\<specimen source name or code (CWE)\> ^ \<additives (TX)\> ^ \<freetext (TX)\> ^ \<body site (CE)\> ^ \<site modifier (CE)\> ^ \<collection method modifier code (CE)\>

The specimen source component is encoded as a CWE data type and contains nine subcomponents.

> **NOTE:** Use of CWE data type is pre-adopted from HL7 v2.5.1 to facilitate expression of coding system version and local terms.

\<SNOMED CT code\>&\<text\>&\<SCT\>&\<code from HL7 Table 0070\>&\<text\>&\<HL70070\>&\<coding system version id\>&\<alternate coding system version id\>&\<local specimen name\>

The code sets used for sending the specimen source component are outlined in this table.

<table>
<caption><p>Table 20. Results Report/Status Change – Date/Time (TS) Field</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 39%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>Code Set</th>
<th>Source in VistA</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SNOMED CT</td>
<td>The SNOMED CT ID field (#20) in the TOPOGRAPHY FIELD file (#61)</td>
<td>If mapped, it’s used as the primary identifier (first three subcomponents), with the ‘identifier’ being the SCT code, the ‘text’ being the SCT fully specified name, and the seventh subcomponent containing the version of the SCT code.</td>
</tr>
<tr class="even">
<td>HL7 0070 Table</td>
<td><p>The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061).</p>
<p>The LEDI HL7 field (#.09) in the TOPOGRAPHY FIELD file (#61) points to the associated entry in the LAB ELECTRONIC CODES file (#64.061).</p></td>
<td><ul>
<li><p>If an SCT code exists for this specimen, the HL7 0070 value will be used as the alternate identifier (the second three subcomponents).</p></li>
<li><p>If an SCT code does not exist, the HL7 0070 value will be used as the primary identifier (first three subcomponents).</p></li>
<li><p>When communicating with DoD, if the SCT code exists, the HL7 0070 value will not be sent.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>SNOMED I</td>
<td>The SNOMED CODE field (#2) in the TOPOGRAPHY FIELD file (#61)</td>
<td>Only used if there are no SNOMED CT and HL7 0070 codes for this specimen. If used, it will be sent as the primary identifier (first three subcomponents), and the seventh subcomponent will contain the version (i.e., “1974”).</td>
</tr>
<tr class="even">
<td>TOPOGRAPHY FIELD file (#61) Internal Entry Number (IEN)</td>
<td>The IEN and NAME (#.01) in the TOPOGRAPHY FIELD file (#61)</td>
<td>If no alternate identifier is populated based off the other code sets, the VistA Topography entry will be sent as the alternate identifier, with the IEN as the alternate identifier, the NAME as the alternate text, and “99VA61” as the name of the alternate coding system. The eighth subcomponent will contain the VistA Laboratory software version (currently “5.2”).</td>
</tr>
</tbody>
</table>

Table 20. Results Report/Status Change – Date/Time (TS) Field

When VistA processes an incoming result, only the SNOMED CT and HL7 0070 table codes are used.

Anatomic pathology orders and results that contain more than one specimen, are coded using HL7 Table 0070 entry XXX - Another Message Part.

> **NOTE:** For anatomic pathology, the specimen source and topography is expressed in an OBX segment (refer to [Section 2.6.1.5](#obx-5-observation-value)).

The ninth subcomponent of the specimen source component contains the name (text) of the related local topography.

The topography in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                      |
|-----------|---------|----------------------------|
| CH        | 63.04   | Specimen Type (#.05)       |
| CY        | 63.902  | Specimen Topography (#.06) |
| EM        | 63.202  | Specimen Topography (#.06) |
| MI        | 63.05   | Site/Specimen (#.05)       |
| SP        | 63.812  | Specimen Topography (#.06) |

Table 21. HL7 Table 0074 – Diagnostic Serv Sect ID Mapping

Example Specimen Source Component

HL7 delimiters \|^~\\

\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE

The body site component (fourth) contains the related collection sample encoded as a CWE data type. This component is only populated when the specimen relates to a microbiology (MI subscript) or Anatomic Pathology (CY, EM, or SP subscripts) report.

- When the collection sample is mapped to SNOMED CT, the first three subcomponents contain the applicable SNOMED CT code with the seventh subcomponent indicating the SNOMED CT version.
- The fourth through sixth subcomponents contain the local code based on the VistA Laboratory COLLECTION SAMPLE file (#62).

> **NOTE:** If the collection sample was not mapped to SNOMED CT, the local codes will be in the first three components).

- The ninth subcomponent contains the local name (text) of the related collection sample.

The collection sample in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                     |
|-----------|---------|---------------------------|
| CH        | N/A     | N/A                       |
| CY        | 63.51   | Collection Sample (#9)    |
| EM        | 63.52   | Collection Sample (#9)    |
| MI        | 63.05   | Collection Sample (#.055) |
| SP        | 63.53   | Collection Sample (#9)    |

Table 22. HL7 Table 0123 – Result Status

Example Body Site Component

HL7 delimiters \|^~\\

\|^^^257261003&Swab (specimen)&SCT&50&SWAB&99VA62&20060101&&SWAB\|

Example OBR-15

HL7 delimiters \|^~\\

\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE

#### OBR-16 Ordering Provider (XCN)

This field contains a composite ID number and name, and is made up of the following:

- It contains the identity of the person who is responsible for creating the request (i.e., ordering physician).
- It identifies the provider who ordered the test. The ID code and the name may be present.
- It is repeated in ORC-12 and contains the same value per the HL7 standards.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & universal ID type (ID)

Subcomponents of assigning facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

The Ordering Provider from the collecting site sent in the ORM message is returned.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), then the Ordering Provider sent with the parent (i.e., original ordered) test will be returned.

#### OBR-18 Placer Field (#1) (ST)

The Placer Field (#1) from the collecting site sent in the ORM message is returned here.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), then the Placer Field (#1) sent with the parent (i.e., original ordered) test will be returned.

#### OBR-19 Placer Field (#2) (ST)

The Placer Field (#2) from the collecting site sent in the ORM message is returned here.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), than the Placer Field (#2) sent with the parent (i.e., original ordered) test will be returned.

#### OBR-20 Filler Field (#1) (ST)

This field (#1) contains information relating to the filler of the results and the reference to the data storage location of the results in VistA LAB DATA file (#63).

The data is structured using the following format:

\<LRDFN (VistA LAB DATA file (#63) internal entry number)\>^\<File \#63 subscript (“CH”, “CY”,“MI”,”SP”,”EM”)\>^\<specimen date/time internal entry number in VistA LAB DATA file (#63\>

> **NOTE:** This field can be HL7 escape encoded when the data conflicts with the HL7 delimiters used to encode the HL7 message.

#### OBR-21 Filler Field (#2) (ST)

This field (#2) contains information relating to the filler of the results and the reference to the accession related to the results in VistA LAB DATA file (#63).

The data is structured using the following format:

LRACC^LRAA^LRAD^LRAN^Accession Area^Area Abbreviation^NLT

Where:

| LRACC             | Human readable accession                                                  |
|-------------------|---------------------------------------------------------------------------|
| LRAA              | Internal entry number of accession area in ACCESSION file (#68)           |
| LRAD              | FileMan accession date                                                    |
| LRAN              | Accession number                                                          |
| Accession Area    | Accession area name from ACCESSION file (#68) based on LRAA value         |
| Area Abbreviation | Accession area abbreviation from ACCESSION file (#68) based on LRAA value |
| NLT               | Order NLT code of ordered test                                            |

Table 23. Principle Result Interpreter (CM) Field

> **NOTE:** This field can be HL7 escape encoded when the data conflicts with the HL7 delimiters used to encode the HL7 message.

#### OBR-22 Results Report/Status Change – Date/Time (TS)

This field contains the date and time the report is released. It is derived from the following fields in VistA LAB DATA file (#63).

<table>
<caption><p>Table 24. OBR Segment Fields in ORM</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>Subscript</th>
<th>Subfile</th>
<th>Field</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CH</td>
<td>63.04</td>
<td>Date Report Completed (#.03)</td>
<td></td>
</tr>
<tr class="even">
<td>CY</td>
<td>63.09</td>
<td>Report Release Date/Time (#.11)</td>
<td></td>
</tr>
<tr class="odd">
<td>EM</td>
<td>63.02</td>
<td>Report Release Date/Time (#.11)</td>
<td></td>
</tr>
<tr class="even">
<td>MI - Bacteriology</td>
<td>63.05</td>
<td><p>Date Report Completed (#.03)</p>
<p>or</p>
<p>Bact Rpt Date Approved (#11)</p></td>
<td rowspan="5">If both the ‘Date Report Completed’ field and the ‘xxx Rpt Date Approved’ field are populated, the latter field will be used.</td>
</tr>
<tr class="odd">
<td>MI - Virology</td>
<td>63.05</td>
<td><p>Date Report Completed (#.03)</p>
<p>or</p>
<p>Virology Rpt Date (#33)</p></td>
</tr>
<tr class="even">
<td>MI - Mycology</td>
<td>63.05</td>
<td><p>Date Report Completed (#.03)</p>
<p>or</p>
<p>Mycology Rpt Date Approved (#18)</p></td>
</tr>
<tr class="odd">
<td>MI - Parasitology</td>
<td>63.05</td>
<td><p>Date Report Completed (#.03)</p>
<p>or</p>
<p>Parasite Rpt Date Approved (#14)</p></td>
</tr>
<tr class="even">
<td>MI - Mycobacteriology</td>
<td>63.05</td>
<td><p>Date Report Completed (#.03)</p>
<p>or</p>
<p>Tb Rpt Date Approved (#22)</p></td>
</tr>
<tr class="odd">
<td>SP</td>
<td>63.08</td>
<td>Report Release Date/Time (#.11)</td>
<td></td>
</tr>
</tbody>
</table>

Table 24. OBR Segment Fields in ORM

#### OBR-24 Diagnostic Serv Sect ID (ID)

This field contains a reference to the data storage location of the results in VistA LAB DATA file (#63).

The various subscripts are mapped as follows.

| VistA Subscript       | HL7 Table 0074 – Diagnostic Serv Sect ID |
|-----------------------|------------------------------------------|
| CH                    | CH                                       |
| MI-Micro bacteriology | MB                                       |
| MI-Parasitology       | PAR                                      |
| MI-Mycology           | MYC                                      |
| MI-Mycobacteriology   | MCB                                      |
| MI-Virology           | VR                                       |
| CY                    | CP                                       |
| SP                    | SP                                       |
| EM                    | PAT                                      |
| AU                    | PAT                                      |

Table 25. Code Sets Used for Sending the Specimen Source Component

#### OBR-25 Result Status (ID)

This field is the status of results for this order.

> **NOTE:** For chemistry/hematology, etc. (CH subscript) tests, this field is not valued. For status of the individual results, refer to [OBX-11 – Observ Result Status](#obx-11-observ-result-status-id).

For microbiology (MI) subscript and anatomic pathology (SP, CY, and EM) subscripts, this field contains the status of the whole report.

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

Table 26. Code Sets Used for Sending the Body Site Component

#### OBR-26 Parent Result (CM)

This field contains the OBX segment of the parent result related to this order.

\<OBX-3-observation identifier of parent result (CE\>^\<OBX-4-sub-ID of parent result (ST\>^\<part of OBX-5 observation result from parent (i.e., organism name) (TX)\>

If the current battery is an antimicrobial susceptibility, the parent results identified OBX contain a result, which identifies the organism on which the susceptibility was run.

VistA currently only uses this field for microbiology (MI) subscript results when reporting antibiotic susceptibility.

#### OBR-29 Parent (CM)

This field contains the relationship of a child to its parent when a parent-child relationship exists. Parent is a two-component field. The components of the placer order number and the filler order number are transmitted in subcomponents of this two-component field.

\<parent’s placer order number\>^\<parent’s filler order number\>

Antimicrobial susceptibilities spawned by cultures, need to record the parent (culture) filler order number.

#### OBR-32 Principle Result Interpreter (CM)

This field contains the name of the physician or other clinician who interpreted the observation and is responsible for the report content. For chemistry/hematology, etc. (CH subscript) tests, this field is not valued.

This information is derived from the following fields in the VistA LAB DATA file (#63).

<table>
<caption><p>Table 27. OBX Segment Fields in ORU</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 37%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Subscript</th>
<th>Subfile</th>
<th>Field</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CH</td>
<td>N/A</td>
<td>N/A</td>
<td></td>
</tr>
<tr class="even">
<td>CY</td>
<td>63.09</td>
<td>Pathologist/Cytotechnologist (#.02)</td>
<td></td>
</tr>
<tr class="odd">
<td>EM</td>
<td>63.02</td>
<td>Pathologist (#.02)</td>
<td></td>
</tr>
<tr class="even">
<td>MI</td>
<td>63.05</td>
<td><p>Verify Person (#.04)</p>
<p>Bact Person (#11.55)</p>
<p>Parasite Entering Person (#15.5)</p>
<p>Myc Person (#19.5)</p>
<p>Tb Entering Person (#25.5)</p>
<p>Virology Entering Person (#35)</p></td>
<td>Depending which Microbiology section is being reported will determine which field is used. (If both the ‘Verify Person’ field and the ‘xxxx Person’ field are populated, the latter field will be used.</td>
</tr>
<tr class="odd">
<td>SP</td>
<td>63.08</td>
<td>Pathologist (#.02)</td>
<td></td>
</tr>
</tbody>
</table>

Table 27. OBX Segment Fields in ORU

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID and the assigning authority (ninth component) contains USDHHS, the check digit is transmitted in identifier check digit (eleventh component).. NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).
- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (ninth component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (-VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### OBR-33 Assistant Result Interpreter (CM)

This field contains the name of the clinical observer who assisted in the interpretation of study. This information is derived from the Resident Pathologist field (# .021) for Surgical Pathology (SP); and Resident or Emtech (# .021) field for Electron Microscopy (EM) subscripts in the VistA LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID and the assigning authority (ninth component) contains USDHHS, the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).
- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (9th component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (-VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### OBR-34 Technician (CM)

This field contains the name of the performing technician. This information is derived from the Cytotech field (# .021) for Cytopathology (CY) and Resident or Emtech field (# .021) for Electron Microscopy (EM) subscripts in the VistA LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

- When the technician is assigned a VA Person ID (VPID), the VPID is transmitted as the ID and the assigning authority (ninth component) contains USVHA. PN is transmitted as the identifier type code (thirteenth component).
- When there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with (VA) and the VA station number.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### OBR-35 Transcriptionist (CM)

This field contains the name of the report transcriber.

For chemistry/hematology, etc. and Microbiology (CH and MI subscript) tests, this field is not valued.

This information is derived from Typist field (# .09) for Surgical Pathology (SP), Cytopathology (CY), and Electron Microscopy (EM) subscripts in the VistA LAB DATA file (#63).

Components

\<name (XCN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR. III) (ST)\> & \<prefix (e.g., DR)\> & \<degree (e.g., MD) (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

The typist field in VistA is stored as free text, so just the free-text name will be sent.

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### OBR-44 Procedure Code (CE)

This field contains a unique identifier assigned to the procedure, if any, associated with the charge. Refer to User-defined Table 0088 - Procedure Code for suggested values. This field is a CE data type for compatibility with clinical and ancillary systems.

Components

\<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\>

- When the ordered laboratory test has an associated order NLT code, the order NLT and CPT code is reported. The CPT code is reported as the primary code and the NLT code as the alternate.
- When the NLT code is not linked to an associated CPT code, the NLT code is reported as the primary code.

\<CPT code File \#81 Field \#1\>^\<text\>^\<C4 or HCPCS\>^\<NLT code File \#64 Field \#1\>^\<text\>^\<99VA64\>

> or

\<NLT code File \#64 Field \#1\>^\<text\>^\<99VA64\>

Example

\|84100~ASSAY OF PHOSPHORUS~C4~84100.0000~Phosphate Inorganic~99VA64\|

## OBR Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the reporting of clinical data, the OBR serves as the report header. The OBR segment identifies the observation set represented by the following observations.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name                 |
|-----|-----|-----|-------|----------|-----|------|------------------------------|
| 1   | 4   | SI  | C     | R        |     |      | Set ID - Observation Request |
| 2   | 22  | EI  | C     | R        |     |      | Placer Order Number          |
| 4   | 250 | CE  | R     | R        |     |      | Universal Service ID         |
| 7   | 26  | TS  | C     | R        |     |      | Observation Date/Time        |
| 8   | 26  | TS  | C     | RE       |     |      | Observation End Date/Time    |
| 9   | 20  | CQ  | O     | RE       |     |      | Collection Volume            |
| 11  | 1   | ID  | O     | RE       |     | 0065 | Specimen Action Code         |
| 12  | 60  | CE  | O     | RE       |     |      | Danger Code                  |
| 13  | 300 | ST  | O     | RE       |     |      | Relevant Clinical Info       |
| 14  | 26  | TS  | C     | RE       |     |      | Specimen Received Date/Time  |
| 15  | 300 | CM  | O     | R        |     | 0070 | Specimen Source              |
| 16  | 60  | XCN | O     | RE       | Y   |      | Ordering Provider            |
| 18  | 60  | ST  | O     | RE       |     |      | Placer Field \#1             |
| 19  | 60  | ST  | O     | RE       |     |      | Placer Field \#2             |
| 27  | 200 | TQ  | O     | RE       | Y   |      | Quantity/Timing              |
| 34  | 200 | CM  | O     | RE       | Y   |      | Technician                   |

Table 28. HL7 Table 0125 – Value Type

### OBR Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBR-1 Set ID - Observation Request (SI)

This field contains a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

#### OBR-2 Placer Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the placer. The first component contains the VistA unique accession identifier (UID).

This field is populated from the UID field (#16) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### OBR-4 Universal Service ID (CE)

This field contains a coded element made up of the following:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^\<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

This field is an identifier code for the requested observation or ordered test. This can be based on local and/or universal codes.

The WKLD CODE file (#64) is used to identify the observed test. It contains the VA National Laboratory Test code. The LABORATORY TEST file (#60) is used to populate the alternate coding system. Future versions may utilize LOINC codes as the coding system.

\<NLT code (File \#64 Field \#1)\>^\<text\>^\<99VA64\>^\<Lab Test IEN\>^\<Lab Test Name (File \#60 Field \#.01)\>^\<99VA60\>

If the test is configured on the VistA Shipping Configuration (file \#62.9) to use non-VA codes, then those codes will be used to identify the observed test , and the VA National Laboratory Test code will be used to populate the alternate code.

\<Non-NLT Test Order Code (File \#62.9, Subfile \#62.9001, Field \#5.1)\>^\<Non-NLT Test Order Name (File \#62.9, Subfile \#62.9001, Field \#5.2)\>^\<Non-NLT Test Coding System (File \#62.9, Subfile \#62.9001, Field \#5.5)\>^\<NLT code (File \#64 Field \#1)\>^\<text\>^\<99VA64\>

#### OBR-7 Observation Date/Time (TS)

This field contains the clinically relevant date/time of the observation. This is the date and time of the specimen collection. Value for this field is derived from DATE/TIME SPECIMEN TAKEN field (#.01) within the associated subfile of the VistA LAB DATA file (#63).

If the collection time is estimated or unknown, only the date will be sent back (without a time).

#### OBR-8 Observation End Date/Time (TS)

This field contains the end date and time of a study or timed specimen collection. This is the actual end date and time of the specimen collection. This information is derived from the COLLECTION END DATE/TIME field (#2.21) within the SPECIMENS subfile (#10) of the VistA LAB SHIPPING MANIFEST file (#62.8).

It will only be populated if the test is configured with the REQUIRE COLLECTION END D/T field (#2.2) set to YES within the TEST/PROFILE subfile (#60) of the VistA LAB SHIPPING CONFIGURATION file (#62.9).

#### OBR-9 Collection Volume (CQ)

This field contains the volume of the collection specimen.

\<quantity (NM)\>^\<units (CE)\>

It will only be populated if the test is configured with the REQUIRE COLLECTION VOLUME field (#2.1) set to YES within the TEST/PROFILE subfile (#60) of the VistA LAB SHIPPING CONFIGURATION file (#62.9).

The first component is populated with the volume of the collected specimen when applicable. This information is derived from VistA LAB SHIPPING MANIFEST file (#62.8), SPECIMENS subfile (#10), COLLECTION VOLUME field (#2.11).

The second component, units, are populated with three subcomponents. This information is derived from VistA LAB SHIPPING MANIFEST file (#62.8), SPECIMENS subfile (#10), COLLECTION VOLUME UNITS field (#2.13), which points to the LAB ELCTRONIC CODES file (#64.061).

- The first subcomponent is populated with the unit’s code. This information is from VistA LAB ELCTRONIC CODES file (#64.061), NAME field (#.01).
- The second component is populated with the abbreviation. This information is from VistA LAB ELCTRONIC CODES file (#64.061), LOINC ABBR field (#1).
- The third component is populated with the name of the coding system. The VA uses LOINC codes for this component.

\<identifier\>^\<text\>^\<LN\>

#### OBR-11 Specimen Action Code (ID)

This field contains the action to take with respect to the specimens that accompany or precede the order. The purpose of this field is to further qualify (when appropriate) the general action indicated by the order control code contained in the accompanying ORC segment.

When communicating with DoD facilities, VistA will send the I code in this field. For other facilities, VistA will send P.

#### OBR-12 Danger Code (CE)

This field contains the code and/or text indicating any known or suspected patient or specimen hazards, such as, patient with active tuberculosis or blood from a hepatitis patient. Either code and/or text may be absent. However, the code is always placed in the first component position and any free text in the second component position. Free text without a code must be preceded by a component delimiter.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

The Danger Code contains the information located within the LAB DATA file (#63) PAT. INFO. field (#.091). VistA does not code this information. It is transmitted as text and occurs in the second component of this field.

#### OBR-13 Relevant Clinical Info (ST)

This field contains the information located within the VistA LAB SHIPPING MANIFEST file (#62.8), SPECIMENS subfile (#10), RELEVANT CLINICAL INFORMATION field (#.1).

#### OBR-14 Specimen Received Date/Time (TS)

This field contains the actual time of arrival of a specimen at the diagnostic service.

Value for this field is derived from the LAB ARRIVAL TIME field (#12) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### OBR-15 Specimen Source (CM)

This field contains the information on the specimen source.

Components

\<specimen source name or code (CWE)\> ^ \<additives (TX)\> ^ \<freetext (TX)\> ^ \<body site (CE)\> ^ \<site modifier (CE)\> ^ \<collection method modifier code (CE)\>

The specimen source component is encoded as a CWE data type and contains nine subcomponents.

> **NOTE:** Use of CWE data type is pre-adopted from HL7 v2.5.1 to facilitate expression of coding system version and local terms.

\<SNOMED CT code\>&\<text\>&\<SCT\>&\<code from HL7 Table 0070\>&\<text\>&\<HL70070\>&\<coding system version id\>&\<alternate coding system version id\>&\<local specimen name\>

The code sets used for sending the specimen source component are outlined in this table.

<table>
<caption><p>Table 29. HL7 Table 0078 – Value Type</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Code Set</th>
<th>Source in VistA</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SNOMED CT</td>
<td><p>The SNOMED CT ID field (#20) in the TOPOGRAPHY FIELD file (#61)</p>
<p>If the SNOMED CT code for the specimen was overridden for this interface, the code will be populated from the SNOMED CT ID field (#.02) within the NON-VA ORDER SNOMED CODES subfile (#30) within the LA7 MESSAGE PARAMETER file (#62.48).</p></td>
<td>If mapped, it’s used as the primary identifier (first three subcomponents), with the ‘identifier’ being the SCT code, the ‘text’ being the SCT fully specified name, and the seventh subcomponent containing the version of the SCT code.</td>
</tr>
<tr class="even">
<td>HL7 0070 Table</td>
<td><p>The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061).</p>
<p>The LEDI HL7 field (#.09) in the TOPOGRAPHY FIELD file (#61) points to the associated entry in the LAB ELECTRONIC CODES file (#64.061).</p></td>
<td><p>If an SCT code exists for this specimen, the HL7 0070 value will be used as the alternate identifier (the second three subcomponents).</p>
<p>If an SCT code does not exist, the HL7 0070 value will be used as the primary identifier (first three subcomponents).</p>
<p>Currently, when communicating with another VA facility, if both the SCT code and HL7 0070 codes exist, then the HL7 0070 code with be used as the primary, and the SCT code will be the alternate (to maintain backward compatibility with VistA LEDI III).</p></td>
</tr>
<tr class="odd">
<td>Non-VA Codes</td>
<td>NON-HL7 SPECIMEN CODE (#5.3), NON-HL7 SPECIMEN NAME (#5.4), and NON-HL7 SPECIMEN CODING SYSTEM (#5.6) in the TEST/PROFILE subfile (#60) of the LAB SHIPPING CONFIGURATION file (#62.9)</td>
<td><p>If this specimen is configured on the VistA Shipping Configuration (file #62.9) to use a non-VA code, than that code will be used as the alternate identifier. (If no SCT code exists, than the non-VA code will be the primary identifier).</p>
<p>When communicating with DoD, the DoD coding system 99LRP will be used as the coding system for the Non-VA code.</p></td>
</tr>
<tr class="even">
<td>SNOMED I</td>
<td>The SNOMED CODE field (#2) in the TOPOGRAPHY FIELD file (#61)</td>
<td>Only used if there are no SNOMED CT, HL7 0070, or non-VA codes for this specimen. If used, it will be sent as the primary identifier (first three subcomponents), and the seventh subcomponent will contain the version (i.e., “1974”).</td>
</tr>
<tr class="odd">
<td>TOPOGRAPHY FIELD file (#61) Internal Entry Number (IEN)</td>
<td>The IEN and NAME (#.01) in the TOPOGRAPHY FIELD file (#61)</td>
<td>If no alternate identifier is populated based off the other code sets, the VistA Topography entry will be sent as the alternate identifier, with the IEN as the alternate identifier, the NAME as the alternate text, and “99VA61” as the name of the alternate coding system. The eighth subcomponent will contain the VistA Laboratory software version (currently “5.2”).</td>
</tr>
</tbody>
</table>

Table 29. HL7 Table 0078 – Value Type

Anatomic pathology orders and results that contain more than one specimen, are coded using HL7 Table 0070 entry XXX - Another Message Part.

> **NOTE:** For anatomic pathology, specimen source and topography are expressed in OBX segments (refer to [Section 2.7.1.5](#obx-5-observation-value-1)).

- The ninth subcomponent of the specimen source component contains the name (text) of the related local topography.
- The topography is derived from the VistA SPECIMEN field (#.01) within the SPECIMEN subfile (#50) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the ACCESSION file (#68).

Example Specimen Source Component

HL7 delimiters \|^~\\

\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE\|

The body site component (fourth) contains the related collection sample encoded as a CWE data type.

The code sets used for sending the body site component are outlined in this table.

<table>
<caption><p>Table 30. HL7 Table 0085 – Observation Result Status Codes Interpretation</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Code Set</th>
<th>Source in VistA</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SNOMED CT</td>
<td><p>The SNOMED CT ID field (#20) in the COLLECTION SAMPLE file (#62)</p>
<p>If the SNOMED CT code for the collection sample was overridden for this interface, the code will be populated from the SNOMED CT ID field (#.02) within the NON-VA ORDER SNOMED CODES subfile (#30) within the LA7 MESSAGE PARAMETER file (#62.48).</p></td>
<td>If mapped, it’s used as the primary identifier (first three subcomponents), with the ‘identifier’ being the SCT code, the ‘text’ being the SCT fully specified name, and the seventh subcomponent containing the version of the SCT code.</td>
</tr>
<tr class="even">
<td>Non-VA Codes</td>
<td>COLLECTION SAMPLE CODE (#5.7), COLLECTION SAMPLE NAME (#5.8), and COLLECT SAMPLE SYSTEM (#5.9) in the TEST/PROFILE subfile (#60) in the LAB SHIPPING CONFIGURATION file (#62.9)</td>
<td>If this collection sample is configured on the VistA Shipping Configuration file (#62.9) to use a non-VA code, then that code will be used as the alternate identifier. (If no SCT code exists, than the non-VA code will be the primary identifier).</td>
</tr>
<tr class="odd">
<td>COLLECTION SAMPLE file (#62) Internal Entry Number (IEN)</td>
<td>The IEN and NAME (#.01) in the COLLECTION SAMPLE file (#62)</td>
<td><p>The IEN will be the identifier, the NAME as the text, and “99VA62” as the name of the coding system.</p>
<p>This will be sent as the primary or alternate identifier – or not at all, depending if the previous code sets were sent as the primary and alternate identifier.</p></td>
</tr>
</tbody>
</table>

Table 30. HL7 Table 0085 – Observation Result Status Codes Interpretation

The ninth subcomponent contains the local name (text) of the related collection sample.

The collection sample is derived from the VistA COLLECTION SAMPLE field (#1) within the SPECIMEN subfile (#50) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the ACCESSION file (#68).

Example Body Site Component

HL7 delimiters \|^~\\

\|^^^257261003&Swab (specimen)&SCT&50&SWAB&99VA62&20060101&&SWAB\|  
The collection method modifier code component (sixth) contains the specimen shipping condition. The first three subcomponents contain the shipping condition abbreviation, shipping condition name, and 99VA62.93.

The shipping condition is derived from the VistA SHIPPING CONDITION field (#.06) within the TEST/PROFILE subfile (#60) of the LAB SHIPPING CONFIGURATION file (#62.9).

Example Collection Method Modifier Code Component

HL7 delimiters \|^~\\

\|^^^^^R&REFRIGERATE&99VA62.93\|

Example OBR-15

HL7 delimiters \|^~\\

\|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE^^R&REFRIGERATE&99VA62.93\|

#### OBR-16 Ordering Provider (XCN)

This field contains a composite ID number and name, and is made up of the following:

- It contains the identity of the person who is responsible for creating the request (i.e., ordering physician).
- It identifies the provider who ordered the test. The ID code and the name may be present.
- It is repeated in ORC-12 and contains the same value per the HL7 standards.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & universal ID type (ID)

Subcomponents of assigning facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

ID can be valued with one of three identifiers.

When the provider is assigned a National Provider ID (NPI) the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS. The check digit is transmitted in the identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

Example

HL7 delimiters \|^~\\

\|0000000003^LRPROVIDER^ONE^D^^^MD^^USDHHS^^3^NPI^NPI\|

- When the provider has no NPI and is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA and identifier type code (thirteenth component) contains PN.
- If there is no NPI or VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted concatenated with -VA and the VA station number.

The value for this field is derived from the PROVIDER field (#6.5) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the ACCESSION file (#68).

#### OBR-18 Placer Field (#1) (ST)

This field (#1) contains vital information for the processing of incoming results and the name of the HL7 application that is the recipient of the order.

The data is passed in the following format:

\<Receiving HL7 application\>

> **NOTE:** Data in this field can be encoded using HL7 escape sequences.

#### OBR-19 Placer Field (#2) (ST)

This field (#2) contains vital information for linking the incoming result with the original order. The data must be passed in the following format:

\<\>^\<\>^\<Accession Area\>^\<Accession Date\>^\<Accession Number\>^\<Accession\>^

\<Universal ID\>^\<Sequence Number\>

All data elements are optional except the Universal ID, which must match with the Placer Order Number.

> **NOTE:** Data in this field can be encoded using HL7 escape sequences.

#### OBR-27 Quantity/timing (TQ)

This field contains information concerning the duration and priority of certain tests. It is the same as ORC-7, except it reflects the test urgency for this specific test, while ORC-7 reflects the highest urgency of tests on the entire order.

Components

\<Quantity (CQ)\> ^ \<Interval (RI)\> ^ \<Duration (ST)\> ^ \<Start Date/Time (TS)\> ^ \<End Date/Time (TS)\> ^ \<Priority (ST)\> ^ \<Condition (ST)\> ^ \<Text (TX)\> ^ \<Conjunction (ID)\> ^ \<Order Sequencing (OSD)\> ^ \<Occurrence Duration (CE)\> ^ \<Total Occurrences (NM)\>

If it exists, VistA will send the duration in the third component. The value for this component is derived from the COLLECTION DURATION and COLLECTION DURATION UNIT fields (#2.22 and \#2.23) within the SPECIMENS subfile (#10) of the LAB SHIPPING MANIFEST file (#62.8).

The test urgency will be sent in the sixth component. The value for this field is derived from the URGENCY OF TEST field (#1) within the TESTS subfile (#11) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the ACCESSION file (#68).

#### OBR-34 Technician (CM)

Components

\<name (CN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

When communicating with another VA system, the seventh component will contain the VA station number of the Host site. The value for this field is derived from the HOST FACILITY field (#.03) in the LAB SHIPPING CONFIGURATION file (#62.9).

Example

HL7 delimiters \|^~\\

\|^^^^^^522

## OBX Segment Fields in ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBX segment transmits a single observation or observation fragment.

| Seq | Len | DT  | Usage | VA R/O/C | RP/# | TBL# | Element Name                    |
|-----|-----|-----|-------|----------|------|------|---------------------------------|
| 1   | 4   | SI  | O     | R        |      |      | Set ID – OBX                    |
| 2   | 3   | ID  | C     | R        |      | 0125 | Value Type                      |
| 3   | 250 | CWE | R     | R        |      |      | Observation Identifier          |
| 4   | 20  | ST  | C     | RE       |      |      | Observation Sub-ID              |
| 5   | 240 | \*  | O     | R        |      |      | Observation Value               |
| 6   | 250 | CE  | O     | RE       |      |      | Units                           |
| 7   | 60  | ST  | O     | RE       |      |      | Reference Ranges                |
| 8   | 5   | IS  | O     | RE       |      | 0078 | Abnormal Flags                  |
| 11  | 1   | ID  | R     | R        |      | 0085 | Observ Result Status            |
| 13  | 20  | ST  | O     | RE       |      |      | User Defined Access Checks      |
| 14  | 26  | TS  | O     | R        |      |      | Date/Time Of The Observation    |
| 15  | 250 | CE  | O     | R        |      |      | Producer’s ID                   |
| 16  | 250 | XCN | O     | RE       |      |      | Responsible Observer            |
| 17  | 250 | CE  | O     | RE       |      |      | Observation Method              |
| 18  | 22  | EI  | O     | RE       |      |      | Equipment Instant Identifier    |
| 19  | 26  | TS  | O     | RE       |      |      | Date/Time Of Analysis           |
| 23  | 567 | XON | O     | RE       |      |      | Performing Organization Name    |
| 24  | 631 | XAD | O     | RE       |      |      | Performing Organization Address |

Table 31. User Defined Access Checks

### OBX Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-1 Set ID - Observation Simple (SI)

This field contains a sequence number used to identify the segment repetitions.

#### OBX-2 Value Type (ID)

This field contains the format of the observation value in OBX.

| Value | Description           |
|-------|-----------------------|
| CE    | Coded Entry           |
| CWE   | Coded with exceptions |
| FT    | Formatted Text        |
| NM    | Numeric               |
| SN    | Structured Numeric    |
| ST    | String Data           |
| TX    | Text                  |

Table 32. OBX Segment Fields in ORM

Although there are other entries in the HL7 table, only the above values are transmitted by VistA.

#### OBX-3 Observation Identifier (CWE)

This field is a unique identifier for the observation test results.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\> ^ \<coding system version ID (ST)\> ^ alternate coding system version ID (ST)\> ^ \<original text (ST)\>

Observation Identifier is encoded as a CWE from CE by pre-adopting the HL 2.5.1 version due to requirements to convey:

- code set versioning information
- local terms

(This was a VACO requirement, as it was deemed a potential patient safety issue if the local term is not conveyed.)

For CH-subscripted tests, the following codes can be used, in order of precedence:

- When a result is LOINC (Logical Observation Identifiers Names and Codes) encoded, LOINC will be used as the primary coding system.
- A result NLT code, if it is available.
- A local code encoded as: \<”CH” data name number\>\<data name label\>\<99VA63\>.

The original text component (ninth) is the local test name is the VistA LABORATORY TEST file (#60), Name field (#.01), when expressing laboratory test results associated with the VistA CH subscript.

\<LOINC CODE\> \<text\> \<LN\> \<NLT CODE\> \<text\> \<99VA64\> \<LOINC version \#\> \< NLT version \#\> \<local test name\>

The following HL7 delimiters are used in the examples below: \|^~\\

Example

LOINC as primary, NLT as alternate

\|2345-7^GLUCOSE:MCNC:PT:SER/PLAS:QN^LN^81352.0000^Glucose Fasting^99VA64 ^2.19^2.14^Serum Glucose\|

Example

LOINC code as primary, local code as alternate (no NLT available)

\|2951-2^SODIUM:SCNC:PT:SER/PLAS:QN^LN^CH5^SODIUM^99VA63^2.19^5.2^SODIUM\|

Example

Local code as primary, (no LOINC/NLT available)

\|CH5^SODIUM^99VA63^^^^5.2^^SODIUM\|

For microbiology (MI subscript) and anatomic pathology (SP, CY and EM subscripts), the coding of this field is as specified in [Section 3.2](#specific-message-consideration) of this specification.

Example Microbiology

\|6584-7^Virus identified:Prid:Pt:XXX:Nom:Culture^LN^87590.0000^Viral Agent^99VA64^2.19^2.14^VIRUS\|

Example Anatomic Pathology

\|22633-2^Path report.site of origin:Anat:Pt:Specimen:Nar^LN^88539.0000^Specimen^99VA64^2.19^2.14\|

#### OBX-4 Observation Sub-ID (ST) 

This field contains a value that distinguishes between multiple OBX segments with the same observation ID organized under one OBR.

For chemistry/hematology type results (CH subscript), VistA values this field with “CH” concatenated with the field number of the field used to store the instance of this result within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63). This can be used to aid in linking updates to previous transmissions.

For Microbiology results that contain organisms, VistA populates this field with a unique Isolate ID that identifies this organism.

For Anatomic Pathology results, VistA uses this field to identify supplementary reports, specimens, and related special studies performed on those specimens.

#### OBX-5 Observation Value (\*)

This field contains the value observed by the observation producer. The length of this field is variable, depending upon the value type. The data type is determined by the value of OBX-2 – Value Type.

- For microbiology-type results reporting etiologic agents and living organisms, the value is encoded using the SNOMED CT coding system (SCT).

Example

HL7 delimiters \|^~\\

^112381006~Genus Dependovirus (organism)~SCT~1037~ADENO-ASSOCIATED (SATELLITE) VIRUSES~99VA61.2~20060101~5.2~ADENO-ASSOCIATED (SATELLITE) VIRUSES^

- For anatomic pathology-type results, when communicating with a DoD site, specimen source is expressed as a pair of OBX segments.
1.  The first OBX segment is populated with the free text specimen description provided by the submitter.
2.  The second OBX of the pair is populated with the SNOMED CT coding of the specimen (topography).
3.  When communicating with a non-DoD site, only one OBX is sent per specimen, containing the SNOMED CT coding of the specimen (topography).

#### OBX-6 Units (CE)

This field contains a coded element.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

VistA populates the first component with the units.

Example

HL7 delimiters \|^~\\

\|mg/dL\|

#### OBX-7 Reference Range (ST)

This field contains the identified range for this specific result.

Example

HL7 delimiters \|^~\\

\|60-123\|

#### OBX-8 Abnormal Flag (ID)

This field contains the entries identified by Table 0078 – Value Type.

| Value                                  | Description                                                                                   | VA Usage |
|----------------------------------------|-----------------------------------------------------------------------------------------------|----------|
| L                                      | Below low normal                                                                              | Used     |
| H                                      | Above high normal                                                                             | Used     |
| LL                                     | Below lower panic limits                                                                      | Used     |
| HH                                     | Above upper panic limits                                                                      | Used     |
| \<                                     | Below absolute low-off instrument scale                                                       | Not Used |
| \>                                     | Above absolute high-off instrument scale                                                      | Not Used |
| N                                      | Normal (applies to non-numeric results)                                                       | Not Used |
| A                                      | Abnormal (applies to non-numeric results)                                                     | Used     |
| AA                                     | Very abnormal (applies to non-numeric results, analogous to panic limits for numeric results) | Not Used |
| Null                                   | No range defined, or normal ranges do not apply                                               | Used     |
| U                                      | Significant change up                                                                         | Not Used |
| D                                      | Significant change down                                                                       | Not Used |
| B                                      | Better—use when direction not relevant                                                        | Not Used |
| W                                      | Worse—use when direction not relevant                                                         | Not Used |
| For microbiology susceptibilities only |                                                                                               |          |
| S                                      | Susceptible                                                                                   | Used     |
| R                                      | Resistant                                                                                     | Used     |
| I                                      | Intermediate                                                                                  | Used     |
| MS                                     | Moderately susceptible                                                                        | Used     |
| VS                                     | Very susceptible                                                                              | Used     |

Table 33. HL7 Table 0125 – Value Type

#### OBX-11 Observ Result Status (ID)

This field contains the current completion status of the results for one observation identifier.

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
| S     | Partial results                                                                              | Not Used |
| X     | Results cannot be obtained for this observation                                              | Used     |
| U     | Results status change to final without retransmitting results already sent as ‘preliminary’. | Not used |
| W     | Post original as wrong                                                                       | Not Used |

Table 34. HL7 Table 0085 – Observation Result Status Codes Interpretation

#### OBX-13 User Defined Access Checks

This field contains the permission of the producer to record results-dependent codes for classifying the observation at the receiving system.

VistA values this field when an antimicrobial susceptibility result is reported and access checks are specified by the reporting facility.

| Value            | VUID    | Description                                                                                                  |
|------------------|---------|--------------------------------------------------------------------------------------------------------------|
| Always Display   | 4500665 | Always display the result                                                                                    |
| Never Display    | 4500805 | Never display the result, unless the user has the LRLAB key that indicates user is laboratory personnel      |
| Restrict Display | 4500877 | Display the result only when the interpretation of all antibiotics, which are always displayed, is resistant |

Table 35. ORC Segment Fields in ORU

#### OBX-14 Date/Time of the Observation (TS)

This field contains the observation date/time that is the physiologically relevant date/time or the closest approximation to that date/time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

Value for this field is derived from DATE/TIME SPECIMEN TAKEN field (#.01) within the associated subfile of the VistA LAB DATA file (#63).

For CH-subscripted tests, if the collection time is estimated or unknown, only the date will be sent back (without a time).

#### OBX-15 Producer’s ID (CE)

This field contains the unique identifier of the responsible producing service and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories.

If this field is null, the receiving system assumes the observations are produced by the sending organization. This information supports CLIA regulations in the US. The code for producer ID is recorded as a CE data type. In the US, the Medicare number of the producing service is usually used as the identifier.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The ID number is the station number found in the VistA INSTITUTION file (#4), STATION NUMBER field (#99). The text is the value of the OFFICIAL VA NAME field (#100). If this value is null, the value of the NAME field (#.01) is used. The name of the coding system is 99VA4.

The Laboratory CLIA number, when available, is transmitted as the alternate identifier with the name of the coding system, 99VACLIA.

Example

HL7 delimiters \|^~\\

\|522^BONHAM^99VA4^987654321^^99VACLIA\|

#### OBX-16 Responsible Observer (XCN)

When required, this field contains the identifier of the individual directly responsible for the observation (such as, the person who performed or verified the observation).

- In a nursing service, the observer is usually the professional who performed the observation (such as, took the blood pressure).
- In a laboratory, the observer is the technician who performed or verified the analysis.

The code for the observer is recorded as a CE data type. If the code is sent as a local code, it must be unique and unambiguous when combined with OBX-15–Producer ID. When available, the code is transmitted with results.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility ID

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Example

HL7 delimiters \|^~\\

\|6738-VA522^LRPROVIDER^ONE^^^^^99VA4\|

When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS, and the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

Example

HL7 delimiters \|^~\\

\|0000000003^LRPROVIDER^ONE^D^^^MD^^USDHHS^^3^NPI^NPI\|

- When the responsible observer is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA, and the identifier type code (thirteenth component) contains PN.
- If there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted, concatenated with -VA and the VA station number.

The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

#### OBX-17 Observation Method (CE)

This optional field contains the method or procedure by which an observation is obtained, when the sending system needs to distinguish a measurement obtained by different methods, where the distinction is not implicit in the test ID.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

For CH-subscripted tests, VistA values this field, when available, with the related methodology associated with the result from WKLD SUFFIX CODES file (#64.2). Also, if the result NLT code is available, that will be sent as well.

\<WKLD SUFFIX CODE\> \<text\> \<99VA64.2\> \<NLT code of reported test\> \<alternate text\> \<99VA64\>

Example

HL7 delimiters \|^~\\

\|.3103^EKTACHEM 700^99VA64.2~81352.0000^Glucose Fasting^99VA64\|

#### OBX-18 Equipment Instant Identifier (EI)

This field contains the equipment instance (such as, Analyzer, Analyzer module, group of Analyzers) responsible for the production of the observation.

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

For CH-subscripted tests, VistA Laboratory values this field with the information and in the form originally transmitted by the automated instrument that produced the result.

#### OBX-19 Date/Time of the Analysis (TS)

This field transfers the time stamp associated with the generation of the analytical result by the instrument specified in Equipment Instance Identifier.

For CH-subscripted tests, VistA values this field with the date/time at which the associated results are verified and released.

#### OBX-23 Performing Organization Name (XON)

This field contains the name of the organization/service responsible for performing the service. When this field is null, the receiving system assumes the observations are produced by the sending organization. The information for producer ID is recorded as an XON data type.

For laboratories, this field specifies the laboratory that produced the test result described in this OBX segment and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories. This information supports CLIA regulations in the US. For producing laboratories, which are CLIA certified, the CLIA identifier is used as the organization identifier (component 10).

Components

\<Organization Name (ST)\> ^ \<Organization Name Type Code (IS)\> ^ ID Number (NM)\> ^ \<Check Digit (NM)\> ^ \<Check Digit Scheme (ID)\> ^ \<Assigning Authority (HD)\> ^ \<Identifier Type Code (ID)\> ^ \<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^ \<Organization Identifier (ST)\>

> **NOTE:** Pre-adopted from HL7 v2.5.1

- Organization Name (first component) contains the name of the VA facility or other organization.
- Organization Name Type (second component) contains:
1.  D to display the name when Facility is found in the VistA INSTITUTION file (#4)
4.  L to display the legal name when the OFFICIAL VA NAME field (#100) is found in the VistA INSTITUTION file (#4)
- ID Number (third component) contains the VA station number when it is numeric (it will only be populated when the CLIA identifier is not available).
- Assigning authority (sixth component) contains:
1.  USVHA when there is a facility ID
5.  CLIA when there is a CLIA identifier
- Identifier Type Code (seventh component) contains:
1.  FI when there is a facility identifier
6.  LN when there is a CLIA identifier
- Name Representation Code (ninth component) is A when it is a facility identifier
- Organization Identifier (tenth component) contains:
1.  VA station number when it is a VA facility identifier
7.  DoD DMIS ID when there is a DoD facility identifier
8.  3-letter local ID when there is a non-VA, non-DoD facility identifier
9.  Laboratory CLIA number when there is a CLIA identifier.

Example

<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999

#### OBX-24 Performing Organization Address (XAD)

This field contains the address of the organization/service responsible for performing the service. For laboratories, this field specifies the address of the laboratory that produced the test result described in this OBX segment and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories. This information supports CLIA regulations in the US.

Components

\<Street Address (SAD)\> ^ \<Other Designation (ST)\> ^ \<CITY (ST)\> ^ \<State or Province (ST)\> ^ \<Zip or Postal Code (ST)\> ^ \<Country (ID)\> ^ \<Address Type (ID)\> ^ \<Other Geographic Designation (ST)\> ^ \<County/Parish Code (IS)\> ^ \<Census Tract (IS)\> ^ \<Address Representation Code (ID)\> ^ \<DEPRECATED-Address Validity Range (DR)\> ^ \<Effective Date (TS)\> ^ \<Expiration Date (TS)\>

> **NOTE:** Pre-adopted from HL7 v2.5.1

Currently only components 1-6 are valued by VistA. Organization address is derived from the VistA INSTITUTION file (#4) using VistA HL supported API \$\$HLADDR^HLFNC.

Example

1234 Anyplace Avenue^Building 456^VistA City^TX^99999^USA

## OBX Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBX segment transmits a single observation or observation fragment.

VistA uses this to transmit the following information, when required:

- Patient height
- Patient weight
- Specimen weight
- Specimen collection volume
- Specimen collection duration

For anatomic pathology (SP, CY and EM subscripts) orders, it is also used to transmit specimen information.

| Seq | Len | DT  | Usage | VA R/O/C | RP/# | TBL# | Element Name                 |
|-----|-----|-----|-------|----------|------|------|------------------------------|
| 1   | 4   | SI  | O     | R        |      |      | Set ID – OBX                 |
| 2   | 3   | ID  | C     | R        |      | 0125 | Value Type                   |
| 3   | 250 | CWE | R     | R        |      |      | Observation Identifier       |
| 4   | 20  | ST  | C     | RE       |      |      | Observation Sub-ID           |
| 5   | 240 | \*  | O     | R        |      |      | Observation Value            |
| 6   | 250 | CE  | O     | RE       |      |      | Units                        |
| 11  | 1   | ID  | R     | R        |      | 0085 | Observ Result Status         |
| 14  | 26  | TS  | O     | RE       |      |      | Date/Time Of The Observation |
| 15  | 250 | CE  | O     | R        |      |      | Producer’s ID                |

Table 36. VistA LAB DATA File (#63) Fields to Derive Facility Information

### OBX Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-1 Set ID - Observation Simple (SI)

This field contains a sequence number used to identify the segment repetitions.

#### OBX-2 Value Type (ID)

This field contains the format of the observation value in OBX.

| Value | Description           |
|-------|-----------------------|
| CE    | Coded Entry           |
| CWE   | Coded with exceptions |
| NM    | Numeric               |
| ST    | String Data           |

Table 37. VISTA INSTITUTION File (#4) Fields to Derive Station Identifier Information

Although there are other entries in the HL7 table, only the above values are transmitted by VistA.

When transmitting patient height, patient weight, specimen weight, specimen collection volume, or specimen collection duration information, the NM value will be used.

#### OBX-3 Observation Identifier (CWE)

This field is a unique identifier for the observation test results.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\> ^ \<coding system version ID (ST)\> ^ alternate coding system version ID (ST)\> ^ \<original text (ST)\>

Observation Identifier is encoded as a CWE from CE by pre-adopting the HL 2.5.1 version due to requirements to convey:

- code set versioning information
- local terms

(This was a VACO requirement, as it was deemed a potential patient safety issue if the local term is not conveyed.)

When transmitting patient height, patient weight, specimen weight, specimen collection volume, or specimen collection duration information, LOINC codes will be used.

Example

HL7 delimiters \|^~\\

\|8301-4^Body height:Len:Pt:Patient:Qn:Estimated^LN^^^^2.19\|

For anatomic pathology (SP, CY and EM subscripts), the coding of this field is as specified in [Section 3.2](#specific-message-consideration) of this specification.

Example Anatomic Pathology

\|22633-2^Path report.site of origin:Anat:Pt:Specimen:Nar^LN^88539.0000^Specimen^99VA64^2.19^2.14\|

#### OBX-4 Observation Sub-ID (ST) 

This field contains a value that distinguishes between multiple OBX segments with the same observation ID organized under one OBR.

For Anatomic Pathology results, VistA uses this field to identify supplementary reports, specimens, and related special studies performed on those specimens.

#### OBX-5 Observation Value (\*)

This field contains the value observed by the observation producer. The length of this field is variable, depending upon the value type. The data type is determined by the value of OBX-2 – Value Type.

For anatomic pathology-type results, when communicating with a DoD site, specimen source is expressed as a pair of OBX segments.

- The first OBX segment is populated with the free text specimen description provided by the submitter.
- The second OBX of the pair is populated with the SNOMED CT coding of the specimen (topography).

When communicating with a non-DoD site, only one OBX is sent per AP specimen, containing the SNOMED CT coding of the specimen (topography).

#### OBX-6 Units (CE)

This field contains a coded element.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

- For AP specimen source, this field will be null.
- When transmitting patient height, patient weight, specimen weight, specimen collection volume, or specimen collection duration information, the first three components will be populated based off the LOINC code.

Example

HL7 delimiters \|^~\\

\|in~Inches~LN\|

#### OBX-11 Observ Result Status (ID)

This field contains the current completion status of the results for one observation identifier.

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
| S     | Partial results                                                                              | Not Used |
| X     | Results cannot be obtained for this observation                                              | Not Used |
| U     | Results status change to final without retransmitting results already sent as ‘preliminary’. | Not used |
| W     | Post original as wrong                                                                       | Not Used |

Table 38. VistA LAB DATA File (#63) Fields to Derive the Ordering Facility

#### OBX-14 Date/Time of the Observation (TS)

This field contains the observation date/time that is the physiologically relevant date/time or the closest approximation to that date/time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

Value for this field is derived from DATE/TIME SPECIMEN TAKEN field (#.01) within the associated subfile of the VistA LAB DATA file (#63).

#### OBX-15 Producer’s ID (CE)

This field contains the unique identifier of the responsible producing service and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories.

If this field is null, the receiving system assumes the observations are produced by the sending organization. This information supports CLIA regulations in the US. The code for producer ID is recorded as a CE data type. In the US, the Medicare number of the producing service is usually used as the identifier.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The ID number is the station number found in the VistA INSTITUTION file (#4), STATION NUMBER field (#99). The text is the value of the OFFICIAL VA NAME field (#100). If this value is null, the value of the NAME field (#.01) is used. The name of the coding system is 99VA4.

The Laboratory CLIA number, when available, is transmitted as the alternate identifier with the name of the coding system, 99VACLIA.

ExampleHL7 delimiters \|^~\\

\|522^BONHAM^99VA4^987654321^^99VACLIA\|

## ORC Segment Fields in ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All applications use the ORC segment as the primary means of communicating specific lab order information. This segment contains data items that are common to all orders.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name              |
|-----|-----|-----|-------|----------|-----|------|---------------------------|
| 1   | 2   | ID  | R     | R        |     | 0119 | Order Control             |
| 2   | 22  | EI  | C     | R        |     |      | Placer Order Number       |
| 3   | 22  | EI  | C     | R        |     |      | Filler Order Number       |
| 4   | 75  | EI  | O     | RE       |     |      | Placer Group Number       |
| 5   | 2   | ID  | O     | RE       |     | 0038 | Order Status              |
| 7   | 200 | TQ  | O     | RE       |     |      | Quantity/Timing           |
| 12  | 250 | XCN | O     | RE       |     |      | Ordering Provider         |
| 13  | 80  | PL  | O     | RE       |     |      | Enterer’s Location        |
| 17  | 60  | CE  | O     | RE       |     |      | Entering Organization     |
| 21  | 250 | XON | O     | RE       | N   |      | Ordering Facility Name    |
| 22  | 250 | XAD | O     | RE       | N   |      | Ordering Facility Address |

Table 39. VistA LAB DATA File (#63) Fields to Derive the Ordering Facility

### ORC Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ORC-1 Order Control (ID)

This field contains the value that determines the function of the order segment. The contents are hard-coded with RE for result messages (ORU) originating from VistA.

#### ORC-2 Placer Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the placer’s system. The first component contains the collecting site’s unique accession identifier. The placer order number is returned with the results.

This field is populated from the ORDERING SITE UID field (#16.4) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### ORC-3 Filler Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier(ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the filler. The first component is valued with the VistA Lab Unique Identifier (UID) or human readable accession. This identifier is returned with the results. The VistA Lab UID is a ten-character alpha/numeric identifier.

This field is populated from the HOST UID field (#16.3) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### ORC-4 Placer Group Number (EI)

This field contains the group number of the placer application for a specific shipment of lab orders.

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

The invoice number of the shipping manifest that was sent by the collecting facility in the ORM message will be returned in the first component.

The Laboratory Electronic Data Interchange (LEDI) software uses the INVOICE field (#.01) within the VistA LAB SHIPPING MANIFEST file (#62.8) to uniquely identify a specific shipment of lab orders. This field also contains updates to the VistA LAB SHIPPING MANIFEST file (#62.8).

#### ORC-5 Order Status (ID)

This field specifies the status of an order.

This field is only populated when communicating with a DoD facility, and will contain a value of CM.

#### ORC-7 Quantity/Timing (TQ)

Components:

\<quantity (CQ)\> ^ \<interval (CM)\> ^ \<duration (ST)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<priority (ST)\> ^ \<condition (ST)\> ^ \<text (TX)\> ^ \<conjunction (ID)\> ^ \<order sequencing (CM)\> ^ \<occurrence duration (CE)\> ^ \<total occurrences (NM)\>

This field contains information concerning the duration and priority of certain tests. It is the same as OBR-27, except it reflects the highest urgency of tests on the order.

Example

If one test has an urgency of Routine and another Stat, ORC-7 contains Stat. Receiving application needs to examine OBR-27 for individual test urgencies.

Only the priority component (sixth) will be populated. This component is populated from the ORDERED URGENCY field (#2) within the ORDERED TEST subfile within the related subscript subfile (i.e., CH, CY, EM, MI, or SP) of the LAB DATA file (#63).

#### ORC-12 Ordering Provider (XCN)

This field contains the person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field is repeated in OBR-16.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

The Ordering Provider from the collecting site sent in the ORM message is returned.

#### ORC-13 Enterer’s Location (PL)

This field specifies the location where the person who entered the request was physically located when the order was entered.

Components

\<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<person location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> ^ \<location description (ST)\>

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

This is only populated for CH and MI subscripted tests, and only the facility component (fourth) will be populated.

The facility information in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                      |
|-----------|---------|----------------------------|
| CH        | 63.04   | Requesting Loc/Div (#.111) |
| CY        | N/A     | N/A                        |
| EM        | N/A     | N/A                        |
| MI        | 63.05   | Requesting Loc/Div (#.111) |
| SP        | N/A     | N/A                        |

Table 40. ORC Segment Fields in ORM

#### ORC-17 Entering Organization (CE)

This field contains a coded element.

Components

\<identifier(ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The identifier number is the station number found in the VISTA INSTITUTION file (#4), STATION NUMBER field (#99). The text is the value of field OFFICIAL VA NAME (#100). If this value is null, the value of field NAME (#.01) is used. The coding system is “99VA4.”

This information in VistA is derived from the following fields.

| Subscript | File   | Subfile | Field                      |
|-----------|--------|---------|----------------------------|
| CH        | 63     | 63.04   | Requesting Loc/Div (#.111) |
| CY        | 8989.3 | N/A     | Default Institution (#217) |
| EM        | 8989.3 | N/A     | Default Institution (#217) |
| MI        | 63     | 63.05   | Requesting Loc/Div (#.111) |
| SP        | 8989.3 | N/A     | Default Institution (#217) |

Table 41. PID Segment Fields in ORM

#### ORC-21 Ordering Facility Name (XON)

This field contains the name of the facility placing the order.

Components

\<Organization Name (ST)\> ^ \<Organization Name Type Code (IS)\> ^\<DEPRECATED-ID Number (NM)\> ^ \<Check Digit (NM)\> ^ \<Check Digit Scheme (ID)\> ^ \<Assigning Authority (HD)\> ^ \<Identifier Type Code (ID)\> ^\<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^ \<Organization Identifier (ST)\>

Subcomponents for Assigning Authority (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

Subcomponents for Assigning Facility (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

- Organization Name (first component) contains the name of the VA facility or other organization.
- Organization Name Type (second component) contains:
1.  D to display the name when Facility is found in the VistA INSTITUTION file (#4)
2.  L to display the legal name when the OFFICIAL VA NAME field (#100) is found in the VistA INSTITUTION file (#4)
- ID Number (third component) contains the VA station number when it is numeric (it will only be populated when the CLIA identifier is not available)
- Assigning authority (sixth component) contains:
1.  USVHA when there is a facility ID
2.  CLIA when there is a CLIA identifier
- Identifier Type Code (seventh component) contains:
1.  FI when there is a facility identifier.
2.  LN when there is a CLIA identifier
- Name Representation Code (ninth component) is A when it is a facility identifier
- Organization Identifier (tenth component) contains:
1.  VA station number when it is a VA facility identifier
2.  DoD DMIS ID when there is a DoD facility identifier
3.  3-letter local ID when there is a non-VA, non-DoD facility identifier
4.  Laboratory CLIA number when there is a CLIA identifier

> **NOTE:** VistA uses the HL7 standard v2.5 field definition.

The ordering facility in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                  |
|-----------|---------|------------------------|
| CH        | 63.04   | Collecting Site (#.33) |
| CY        | 63.09   | Collecting Site (#.33) |
| EM        | 63.02   | Collecting Site (#.33) |
| MI        | 63.05   | Collecting Site (#.33) |
| SP        | 63.08   | Collecting Site (#.33) |

Table 42. User-defined Table 0001 - Administrative Sex

#### ORC-22 Ordering Facility Address (XAD)

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

1234 Anyplace Avenue^Building 456^VistA City^TX^99999^USA

The ordering facility in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                  |
|-----------|---------|------------------------|
| CH        | 63.04   | Collecting Site (#.33) |
| CY        | 63.09   | Collecting Site (#.33) |
| EM        | 63.02   | Collecting Site (#.33) |
| MI        | 63.05   | Collecting Site (#.33) |
| SP        | 63.08   | Collecting Site (#.33) |

Table 43. User-defined Table 0005 - Race

## ORC Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All applications use the ORC segment as the primary means of communicating specific lab order information. This segment contains data items that are common to all orders.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name              |
|-----|-----|-----|-------|----------|-----|------|---------------------------|
| 1   | 2   | ID  | R     | R        |     | 0119 | Order Control             |
| 2   | 22  | EI  | C     | R        |     |      | Placer Order Number       |
| 4   | 75  | EI  | O     | R        |     |      | Placer Group Number       |
| 7   | 200 | TQ  | O     | RE       |     |      | Quantity/Timing           |
| 9   | 26  | TX  | O     | RE       |     |      | Date/Time Of Transaction  |
| 12  | 250 | XCN | O     | RE       |     |      | Ordering Provider         |
| 17  | 60  | CE  | O     | RE       |     |      | Entering Organization     |
| 21  | 250 | XON | O     | RE       | N   |      | Ordering Facility Name    |
| 22  | 250 | XAD | O     | RE       | N   |      | Ordering Facility Address |

Table 44. HL7 (user-defined) Table 0002 – Marital Status

### ORC Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ORC-1 Order Control (ID)

This field contains the value that determines the function of the order segment. The contents are hard-coded with NW for order messages (ORM) originating from VistA.

#### ORC-2 Placer Order Number (EI)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the placer. The first component contains the VistA unique accession identifier (UID).

This field is populated from the UID field (#16) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### ORC-4 Placer Group Number (EI)

This field contains the group number of the placer application for a specific shipment of lab orders.

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

VistA populates the first component with the invoice number of the shipping manifest, which uniquely identifies a specific shipment of lab orders. This information is derived from the INVOICE field (#.01) within the VistA LAB SHIPPING MANIFEST file (#62.8).

If possible, this field must be echoed back in the ORR and ORU messages.

#### ORC-7 Quantity/Timing (TQ)

Components:

\<quantity (CQ)\> ^ \<interval (CM)\> ^ \<duration (ST)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<priority (ST)\> ^ \<condition (ST)\> ^ \<text (TX)\> ^ \<conjunction (ID)\> ^ \<order sequencing (CM)\> ^ \<occurrence duration (CE)\> ^ \<total occurrences (NM)\>

This field contains information concerning the duration and priority of certain tests. It is the same as OBR-27, except it reflects the highest urgency of tests on the order.

Example

If one test has an urgency of Routine and another Stat, ORC-7 contains Stat. Receiving application needs to examine OBR-27 for individual test urgencies.

If it exists, VistA will send the duration in the third component. The value for this component is derived from the COLLECTION DURATION and COLLECTION DURATION UNIT fields (#2.22 and \#2.23) within the SPECIMENS subfile (#10) of the LAB SHIPPING MANIFEST file (#62.8).

The test urgency will be sent in the sixth component. The value for this field is derived from the URGENCY OF TEST field (#1) within the TESTS subfile (#11) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the ACCESSION file (#68).

#### ORC-9 Date/Time Of Transaction (TS)

This field contains the date and time of the event that initiated the current transaction, as reflected in ORC-1.

This field is populated from the DATE ORDERED field (#3) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### ORC-12 Ordering Provider (XCN)

This field contains the person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field is repeated in OBR-16.

Components

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

This field is populated from the PROVIDER field (#6.5) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

#### ORC-17 Entering Organization (CE)

This field contains a coded element.

Components

\<identifier(ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The identifier number is the station number found in the VISTA INSTITUTION file (#4), STATION NUMBER field (#99). The text is the value of field OFFICIAL VA NAME (#100). If this value is null, the value of field NAME (#.01) is used. The coding system is 99VA4.

This field is populated from the COLLECTING FACILITY field (#.02) of the VistA LAB SHIPPING CONFIGURATION file (#62.9).

#### ORC-21 Ordering Facility Name (XON)

This field contains the name of the facility placing the order.

Components

\<Organization Name (ST)\> ^ \<Organization Name Type Code (IS)\> ^\<DEPRECATED-ID Number (NM)\> ^ \<Check Digit (NM)\> ^ \<Check Digit Scheme (ID)\> ^ \<Assigning Authority (HD)\> ^ \<Identifier Type Code (ID)\> ^\<Assigning Facility (HD)\> ^ \<Name Representation Code (ID)\> ^ \<Organization Identifier (ST)\>

Subcomponents for Assigning Authority (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

Subcomponents for Assigning Facility (HD)

\<Namespace ID (IS)\> & \<Universal ID (ST)\>& \<Universal ID Type (ID)\>

- Organization Name (first component) contains the name of the VA facility or other organization.
- Organization Name Type (second component) contains:
1.  D to display the name when Facility is found in the VistA INSTITUTION file (#4)
2.  L to display the legal name when the OFFICIAL VA NAME field (#100) is found in the VistA INSTITUTION file (#4)
- ID Number (third component) contains the VA station number when it is numeric (it will only be populated when the CLIA identifier is not available)
- Assigning authority (sixth component) contains:
1.  USVHA when there is a facility ID
10. CLIA when there is a CLIA identifier
- Identifier Type Code (seventh component) contains:
1.  FI when there is a facility identifier
11. LN when there is a CLIA identifier
- Name Representation Code (ninth component) is A when it is a facility identifier
- Organization Identifier (tenth component) contains:
1.  VA station number when it is a VA facility identifier
12. DoD DMIS ID when there is a DoD facility identifier
13. 3-letter local ID when there is a non-VA, non-DoD facility identifier
14. Laboratory CLIA number when there is a CLIA identifier

> **NOTE:** VistA uses the HL7 standard v2.5 field definition.

The ordering facility in VistA is derived from the COLLECTING FACILITY field (#.02) of the VistA LAB SHIPPING CONFIGURATION file (#62.9).

#### ORC-22 Ordering Facility Address (XAD)

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

1234 Anyplace Avenue^Building 456^VistA City^TX^99999^USA

The ordering facility in VistA is derived from the COLLECTING FACILITY field (#.02) of the VistA LAB SHIPPING CONFIGURATION file (#62.9).

## PID Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information that does not change frequently.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name            |
|-----|-----|-----|-------|----------|-----|------|-------------------------|
| 1   | 4   | SI  | O     | R        |     |      | Set Id - PID            |
| 3   | 250 | CX  | R     | R        | Y   |      | Patient Identifier List |
| 5   | 250 | XPN | R     | R        | Y   |      | Patient Name            |
| 6   | 250 | XPN | O     | RE       | Y   |      | Mother’s Maiden Name    |
| 7   | 26  | TS  | O     | RE       |     |      | Date/Time Of Birth      |
| 8   | 1   | IS  | O     | RE       |     | 0001 | Administrative Sex      |
| 10  | 250 | CE  | O     | RE       | Y   | 0005 | Race                    |
| 16  | 250 | CE  | O     | RE       |     | 0002 | Marital Status          |
| 19  | 16  | ST  | O     | RE       |     |      | SSN Number - Patient    |

Table 45. PID Segment Fields in ORU

### PID Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID-1 Set ID – PID (SI)

This field contains a sequence number used to identify the segment repetitions.

#### PID-3 Patient Identifier List (CX)

This field contains an extended composite element.

Components

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD)^ \<effective date (DT)\> ^ \<expiration date (DT)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

VistA sends VA Integration Control Number (ICN) and Social Security Number (SSN) (without dashes) when available in this field. Additionally, the internal entry number (IEN) on the local PATIENT file (#2) is transmitted.

When communicating with a DoD facility, VistA will only send the first repetition in this field.

#### PID-5 Patient Name (XPN)

This field contains the names of the patient. The primary or legal name of the patient is reported first.

Components

In Version 2.3, instead of the PN data type, use:

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name

\<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

#### PID-6 Mother’s Maiden Name (ST)

This field contains the family name under which the mother was born. It is used to differentiate patients with the same last name.

Components

In Version 2.3, instead of the PN data type, use:

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^\<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^\<name assembly order (ID)\> Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

#### PID-7 Date/Time of Birth (TS)

This field contains the date and time of the birth of the patient.

#### PID-8 Administrative Sex (ID)

This field contains the sex of the patient. Although there are other entries in the HL7 table, only the following values are transmitted.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |
| U     | Unknown     |

Table 46. User-defined Table 0001 - Administrative Sex

#### PID-10 Race (CE)

This field contains the race of the patient. These entries correspond to the VistA RACE file (#10). The primary identifier (components one through three) will be populated using values from HL7 Table 0005 (refer to the user-defined Table 0005 – Race below). The alternate identifier (components four through six), will be populated with CDC codes.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

| Value  | Description                               |
|--------|-------------------------------------------|
| 0000-0 | Declined to Answer                        |
| 1002-5 | American Indian or Alaska Native          |
| 2028-9 | Asian                                     |
| 2054-5 | Black or African American                 |
| 2076-8 | Native Hawaiian or Other Pacific Islander |
| 2106-3 | White                                     |
| 9999-4 | Unknown by Patient                        |

Table 47. User-defined Table 0005 - Race

> **NOTE:** The values contain a pre-calculated Mod 10 check digit separated by a dash.

#### PID-16 Marital Status (ID)

This field contains the marital status of the patient. These entries correspond to the VistA MARITAL STATUS file (#11). Refer to the user-defined Table 0002 – Marital Status.

| Value | Description   |
|-------|---------------|
| S     | Separated     |
| D     | Divorced      |
| M     | Married       |
| N     | Never Married |
| W     | Widow/Widower |
| U     | Unknown       |

Table 48. HL7 (user-defined) Table 0002 – Marital Status

#### PID-19 SSN Number – Patient (ST)

This field is for backward compatibility only.

- When used for backward compatibility, this field contains the Social Security Number (SSN) of the patient.
- This field must be populated, in order to maintain backward compatibility.
- For all patient identifiers, use PID-3 – Patient Identifier List.

## PID Segment Fields in ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information that does not change frequently.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name            |
|-----|-----|-----|-------|----------|-----|------|-------------------------|
| 1   | 4   | SI  | O     | R        |     |      | Set Id - PID            |
| 2   | 20  | CX  | B     | RE       |     |      | Patient ID              |
| 3   | 250 | CX  | R     | R        | Y   |      | Patient Identifier List |
| 4   | 20  | CX  | B     | RE       | Y   |      | Alternate Patient ID    |
| 5   | 250 | XPN | R     | R        | Y   |      | Patient Name            |
| 6   | 250 | XPN | O     | RE       | Y   |      | Mother’s Maiden Name    |
| 7   | 26  | TS  | O     | RE       |     |      | Date/Time Of Birth      |
| 8   | 1   | IS  | O     | RE       |     | 0001 | Administrative Sex      |
| 10  | 250 | CE  | O     | RE       | Y   | 0005 | Race                    |
| 16  | 250 | CE  | O     | RE       |     | 0002 | Marital Status          |
| 19  | 16  | ST  | O     | RE       |     |      | SSN Number - Patient    |

Table 49. PV1 Segment Fields in ORM and ORU

### PID Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID-1 Set ID – PID (SI)

This field contains a sequence number used to identify the segment repetitions.

#### PID-2 Patient ID – PID (CX)

This field is for backward compatibility only and is for systems with a negotiated understanding of *external*.

VistA populates this field with the information sent by the collecting site in PID-3 of the ORM message.

#### PID-3 Patient Identifier List (CX)

This field contains an extended composite element.

Components

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD)^ \<effective date (DT)\> ^ \<expiration date (DT)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

VistA populates this field based off the information in the IDENTIFIER field (#.09) in the REFERRAL PATIENT file (#67). If the information sent in PID-3 in the ORM message is different than the IDENTIFIER field, then VistA will return the value sent in PID-3 as well.

#### PID-4 Alternate Patient ID (CX)

This field is for backward compatibility only.

- When used for backward compatibility, this field contains the alternate, temporary, or pending optional patient identifier if needed, or contains additional numbers that may be required to identify a patient.
- For all patient identifiers, use PID-3 – Patient Identifier List.
- Use this field to convey multiple patient IDs when more than one exists for a patient.

If the Collecting facility populated PID-4 in the ORM message, then VistA will return that value. Otherwise, VistA will populate it with the Internal Entry Number (IEN) of the LAB DATA file (#63).

#### PID-5 Patient Name (XPN)

This field contains the names of the patient. The primary or legal name of the patient is reported first.

Components

In Version 2.3, instead of the PN data type, use

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name

\<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

#### PID-6 Mother’s Maiden Name (ST)

This field contains the family name under which the mother was born. It is used to differentiate patients with the same last name.

Components

In Version 2.3, instead of the PN data type, use

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^\<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^\<name assembly order (ID)\> Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

#### PID-7 Date/Time of Birth (TS)

This field contains the date and time of the birth of the patient.

#### PID-8 Administrative Sex (ID)

This field contains the sex of the patient. Although there are other entries in the HL7 table, only the following values are transmitted.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |
| U     | Unknown     |

Table 50. BLG Segment Fields in ORM

#### PID-10 Race (CE)

This field contains the race of the patient. These entries correspond to the VistA RACE file (#10). The primary identifier (components one through three) will be populated using values from HL7 Table 0005 (refer to the user-defined Table 0005 – Race below). The alternate identifier (components four through six), will be populated with CDC codes.

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

| Value  | Description                               |
|--------|-------------------------------------------|
| 0000-0 | Declined to Answer                        |
| 1002-5 | American Indian or Alaska Native          |
| 2028-9 | Asian                                     |
| 2054-5 | Black or African American                 |
| 2076-8 | Native Hawaiian or Other Pacific Islander |
| 2106-3 | White                                     |
| 9999-4 | Unknown by Patient                        |

Table 51. HL7 Table 0122 - Charge Type

> **NOTE:** The values contain a pre-calculated Mod 10 check digit separated by a dash.

#### PID-16 Marital Status (ID)

This field contains the marital status of the patient. These entries correspond to the VistA MARITAL STATUS file (#11). Refer to the user-defined Table 0002 – Marital Status.

| Value | Description   |
|-------|---------------|
| S     | Separated     |
| D     | Divorced      |
| M     | Married       |
| N     | Never Married |
| W     | Widow/Widower |
| U     | Unknown       |

Table 52. Default Mapping of NLT/LOINC Codes to Standard Fields within the MICROBIOLOGY Subfile (#5) Multiple of LAB DATA File (#63)

#### PID-19 SSN Number – Patient (ST)

This field is for backward compatibility only.

- When used for backward compatibility, this field contains the Social Security Number (SSN) of the patient.
- This field must be populated, in order to maintain backward compatibility.
- For all patient identifiers, use PID-3 – Patient Identifier List.

## PV1 Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV1 segment is used to communicate information on a visit-specific basis. When communicating with a DoD facility, VistA will not send this segment in the ORU message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name              |
|-----|-----|-----|-------|----------|-----|------|---------------------------|
| 1   | 4   | SI  | O     | R        |     |      | Set ID - Patient Visit    |
| 2   | 1   | IS  | R     | R        |     | 0004 | Patient Class             |
| 3   | 80  | PL  | O     | RE       |     |      | Assigned Patient Location |

Table 53. Default Mapping of NLT/LOINC Codes to Standard Fields within the Surgical Pathology Subfile (#8) Multiple of the LAB DATA File (#63)

### PV1 Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PV1-1 Set ID – Patient Visit (SI)

This field contains the unique number that identifies the transaction.

#### PV1-2 Patient Class (IS)

This field contains the category into which the patient falls at the site. VA facilities use the code, I for inpatient or O for outpatient.

#### PV1-3 Assigned Patient Location (PL)

This field contains the patient's initial assigned location or the location to which the patient is being moved.

Components

\<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<person location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> ^ \<location description (ST)

Subcomponents of facility

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

- For an Inpatient, VistA will populate the first component with the ward location on which this patient is currently residing.
- For an Outpatient, VistA will populate the first component with the most current location where a lab procedure was requested.

## BLG Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BLG segment is used to provide billing information, on the ordered service, to the filling application.

VistA will send this segment when the ACCOUNT NUMBER field (#.12) is populated in the VistA LAB SHIPPING CONFIGURATION file (#62.9).

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name |
|-----|-----|-----|-------|----------|-----|------|--------------|
| 2   | 50  | ID  | O     | R        |     | 0122 | Charge Type  |
| 3   | 100 | CK  | O     | R        |     |      | Account ID   |

Table 54. Default Mapping of NLT/LOINC Codes to Standard Fields within the Cytopathology (#9) Multiple of LAB DATA File (#63)

### BLG Field Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### BLG-2 Charge Type (ID)

This field identifies someone or something other than the patient to be billed for this service. It is used in conjunction with BLG-3-account ID.

VistA sends CO as the Charge Type.

| Value | Description  | VA Usage |
|-------|--------------|----------|
| CH    | Charge       | Not Used |
| CO    | Contract     | Used     |
| CR    | Credit       | Not Used |
| DP    | Department   | Not Used |
| GR    | Grant        | Not Used |
| NC    | No Charge    | Not Used |
| PC    | Professional | Not Used |
| RS    | Research     | Not Used |

Table 55. Default Mapping of NLT/LOINC Codes to Standard Fields within the Electron Microscopy (#2) Multiple of LAB DATA File (#63)

#### BLG-3 Account ID (CK)

This field identifies the account to be billed. It is used in conjunction with BLG-2-charge type.

Components

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \< assigning authority (HD)\>

Subcomponents of assigning authority

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

VistA populates this field from the ACCOUNT NUMBER field (#.12) in the VistA LAB SHIPPING CONFIGURATION file (#62.9). VistA uses the M11 algorithm to generate the check digit.

Example

HL7 delimiters \|^~\\

\|100032^2^M11\|

<span id="_Transaction_Specifications" class="anchor"></span>

# Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA initiates ORM order messages, they are acknowledged with an ACK commit acknowledgment message and an ORR application acknowledgment message. When VistA receives an ORM message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

When VistA initiates ORU result messages, they are acknowledged with an ACK commit acknowledgment message and an ACK application acknowledgment message. When VistA receives an ORU message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

## Specific Message Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of microbiology or AP results. A default encoding is enabled for LOINC to encode standard microbiology and AP tests.

> **NOTE:** The LOINC codes displayed in the sections below in the ‘LOINC Code’ column are the default LOINC Codes that the system will use. However, if the site mapped their Result NLT Code (displayed in the ‘Result NLT’ column) to a different LOINC code (in the WKLD CODE file (#64)), then the LOINC code to which the local site mapped their entry will override the LOINC code displayed in the tables below.

### Microbiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of microbiology results. A default encoding is enabled for LOINC to encode standard microbiology tests and antibiotics.

The default mapping of NLT/LOINC codes to standard fields within the MICROBIOLOGY subfile (#5) multiple of LAB DATA file (#63) is outlined in the table below.

| Test                                       | Order NLT  | Result NLT | LOINC Code |
|--------------------------------------------|------------|------------|------------|
| Bacteriology report (#11)                  | 87993.0000 | 93928.0000 |            |
| Urine Screen (#11.57)                      | 87993.0000 | 93948.0000 | 630-4      |
| Sputum screen (#11.58)                     | 87993.0000 | 93949.0000 | 6460-0     |
| Gram stain (#11.6)                         | 87993.0000 | 87754.0000 | 664-3      |
| Bacteriology organism (#12)                | 87993.0000 | 87570.0000 | 11475-1    |
| Bacteria colony count (#12,1)              |            | 87719.0000 | 564-5      |
| Bacteriology smear/prep (#11.7)            | 87993.0000 | 93967.0000 |            |
| Bacteriology test (#1.5)                   | 87993.0000 | 93969.0000 |            |
| Bacteriology Susceptibility                | 87565.0000 |            |            |
| Parasite report (#14)                      | 87925.0000 | 93929.0000 |            |
| Parasite organism (#16)                    | 87925.0000 | 87576.0000 | 20932-0    |
| Parasite Stages (#16,1,.01)                | 87925.0000 | 92930.0000 |            |
| Parasite organism stage quantity (#16,1,1) | 87925.0000 | 93997.0000 |            |
| Parasitology smear/prep (#15.51)           | 87925.0000 | 93971.0000 |            |
| Parasitology test (#16.4)                  | 87925.0000 | 93972.0000 |            |
| Mycology report (#18)                      | 87994.0000 | 93930.0000 |            |
| Mycology smear/prep (#19.6)                | 87994.0000 | 93984.0000 |            |
| Mycology test (#20.4)                      | 87994.0000 | 93974.0000 |            |
| Fungal organism (#20)                      | 87994.0000 | 87578.0000 | 580-1      |
| Fungal colony count (#20,1)                | 87994.0000 | 87723.0000 | 19101-5    |
| Mycobacterium report (#22)                 | 87995.0000 | 93931.0000 |            |
| Acid Fast stain (#24)                      | 87995.0000 | 87756.0000 | 11545-1    |
| Acid Fast stain quantity (#25)             | 87995.0000 | 87583.0000 |            |
| Mycobacterium organism (#26)               | 87995.0000 | 87589.0000 | 543-9      |
| Mycobacterium Susceptibility               | 87568.0000 |            |            |
| Mycobacterium colony count                 | 87995.0000 | 87719.0000 | 564-5      |
| TB test (#26.4)                            | 87995.0000 | 93977.0000 |            |
| Virology report (#33)                      | 87996.0000 | 93932.0000 |            |
| Viral agent (#36)                          | 87996.0000 | 87590.0000 | 6584-7     |
| Virology test (#36.4)                      | 87996.0000 | 93981.0000 |            |
| Sterility results (#11.52)                 | 93982.0000 | 93982.0000 |            |

Table 56. Order Message

### Bacteriology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The susceptibilities of a bacteriology or mycobacterium (TB) organism are based on the local site's mapping of the National VA Lab Code field (#64) in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and the related default LOINC code associated with the VA NLT code.

### Surgical Pathology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Surgical Pathology results.

The default mapping of NLT/LOINC codes to standard fields within the Surgical Pathology subfile (#8) multiple of the LAB DATA file (#63) is outlined in the table below.

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
| Supplementary report (#1.2)     | 88589.0000 | 88589.0000 | 22639-9    |
| Specimen weight (#10,2)         | 88515.0000 | 81233.0000 | 3154-2     |

Table 57. Order Message Acknowledgments

### Cytopathology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Cytopathology results.

The default mapping of NLT/LOINC codes to standard fields within the Cytopathology (#9) multiple of LAB DATA file (#63) is outlined in the table below.

| Test                            | Order NLT  | Result NLT | LOINC Code |
|---------------------------------|------------|------------|------------|
| Specimens (#.012)               | 88593.0000 | 88539.0000 | 22633-2    |
| Brief clinical history (#.013)  | 88593.0000 | 88542.0000 | 22636-5    |
| Preoperative diagnosis (#.014)  | 88593.0000 | 88544.0000 | 10219-4    |
| Operative findings (#.015)      | 88593.0000 | 88542.0000 | 10215-2    |
| Postoperative diagnosis (#.016) | 88593.0000 | 88547.0000 | 10218-6    |
| Gross description (#1)          | 88593.0000 | 88549.0000 | 22634-0    |
| Microscopic examination (#1.1)  | 88593.0000 | 88563.0000 | 22635-7    |
| Supplementary report (#1.2)     | 88589.0000 | 88589.0000 | 22639-9    |
| Cytopathology diagnosis (#1.4)  | 88593.0000 | 88571.0000 | 22637-3    |

Table 58. Result Message

### Electron Microscopy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of Electron Microscopy.

The default mapping of NLT/LOINC codes to standard fields within the Electron Microscopy (#2) multiple of LAB DATA file (#63) is outlined in the table below.

| Test                            | Order NLT  | Result NLT | LOINC Code |
|---------------------------------|------------|------------|------------|
| Specimens (#.012)               | 88597.0000 | 88057.0000 | 22633-2    |
| Brief clinical history (#.013)  | 88597.0000 | 88542.0000 | 22636-5    |
| Preoperative diagnosis (#.014)  | 88597.0000 | 88544.0000 | 10219-4    |
| Operative findings (#.015)      | 88597.0000 | 88542.0000 | 10215-2    |
| Postoperative diagnosis (#.016) | 88597.0000 | 88547.0000 | 10218-6    |
| Gross description (#1)          | 88597.0000 | 88549.0000 | 22634-0    |
| Microscopic examination (#1.1)  | 88597.0000 | 88563.0000 | 22635-7    |
| Supplementary report (#1.2)     | 88589.0000 | 88589.0000 | 22639-9    |
| EM diagnosis (#1.4)             | 88597.0000 | 88571.0000 | 22637-3    |

Table 59. Message Acknowledgment

## Specific Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Order Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA receives an ORM message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

| ORM       | General Order Message      |
|-----------|----------------------------|
| MSH       | Message Header             |
| {PID      | Patient Identification     |
| \[PV1\]   | Patient Visit              |
| {ORC      | Common Order               |
| OBR       | Observations Report ID     |
| {\[NTE\]} | Laboratory Note or Comment |
| {\[OBX\]} | Observation Segment        |
| }         |                            |
| }         |                            |

#### Example of Chemistry/Hematology/Serology Order Message

Figure . Example of Chemistry/Hematology/Serology Order Message

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130820093429-0400^^ORM~O01^52291733^T^2.3^^^AL^AL^

PID^1^^000009934\~\~~USSSA&&L~SS\|381~6~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^^LRPATIENT~TWO^^19000101^F^^\~~0005\~\~~CDC^^^^^^^^^000009934

PV1^1^O^1W

ORC^NW^0432320010^^522-20130820-1^^^\~\~\~\~~R^^20130820^^^6746-VA170K~LRUSER~TWO\~\~\~\~~99VA4^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^~Building 456\~~TX\~~USA

OBR^1^0432320010^^81352.0000~Glucose Fasting~99VA64~175~GLUCOSE~99VA60^^^20130820093405-0400^^^^P^^^20130820093410-0400^UR&Urine&HL70070&78014005&Urine (substance)&SCT&&20060101&URINE\~\~~78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE\~~REF&REFRIGERATED&99VA62.93^6746-VA170K~LRUSER~TWO\~\~\~\~~99VA4^^LA7V HOST 170^\F\\F\11\F\3130820\F\10\F\CH 0820 10\F\0432320010\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

BLG^^CO^1234567890~3~M11^

#### Examples of Microbiology Order Messages

Figure 2. Examples of Microbiology Order Messages

PARASITOLOGY:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130522011612-0400^^ORM~O01^522

90671^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^1W

ORC^NW^1413000098^^522-20130522-1^^^\~\~\~\~~R^^20130522^^^235-VA170K~LRUSER~ONE\~\~~

\~~99VA4^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^~Build

ing 456\~~TX\~~USA

OBR^1^1413000098^^93933.0000~Ova Parasite Exam~99VA64~550~PARASITE EXAM~99VA60^

^^20130522011506-0400^^^^P^^^20130522011515-0400^STL&Stool=Fecal&HL70070&39

477002&Feces (substance)&SCT&&20060101&FECES\~\~~119339001&Stool specimen (sp

ecimen)&SCT&17&S

TOOL&99VA62&20060101&&STOOL\~~RT&ROOM TEMPERATURE&99VA62.93^235-VA170K~LRUSER~ON

E\~\~\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\98\F\MICRO 13 98\F\14130000

98\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

-----------------------------------------------------------------------------

MYCOBACTERUM TB:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130617122442-0400^^ORM~O01^522

90836^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^1W

ORC^NW^1413000105^^522-20130617-1^^^\~\~\~\~~R^^20130617^^^235-VA170K~LRUSER~ONE\~\~~

\~~99VA4^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^~Build

ing 456\~~TX\~~USA

OBR^1^1413000105^^93935.0000~Culture \T\\ Sensitivity~99VA64~548~CULTURE \T\\ SUS

CEPTIBILITY~99VA60^^^20130617122333-0400^^^^P^^^20130617122341-0400^SPT&Spu

tum&HL70070&45710003&Sputum (substance)&SCT&&20060101&SPUTUM\~\~~119334006&Sp

utum specimen (s

pecimen)&SCT&18&SPUTUM&99VA62&20060101&&SPUTUM\~~RT&ROOM TEMPERATURE&99VA62.93^2

35-VA170K~LRUSER~ONE\~\~\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\105\F\MI

CRO 13 105\F\1413000105\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

-----------------------------------------------------------------------------

BACTERIOLOGY:

MSH^~\|\\^LA7V REMOTE 170^170^LA7V HOST 522^522^20130501112850-0400^^ORM~O01^170

28835^T^2.3^^^AL^AL^

PID^1^^467321321\~\~~USSSA&&L~SS\|7171914~6~M11\~~PI~170&FS.FO-ALBANY.MED.VA.GOV&DN

S\|5000000423V938388\~\~~USVHA&&HL70363~NI~VA FACILITY ID&200M&L^^LRPATIENT~ONE^

^19600101^M^^\~~0005\~\~~CDC^^^^^^M^^^467321321

PV1^1^O^MICU

ORC^NW^1413000033^^170-20130501-2^^^\~\~\~\~~R^^20130501^^^100884-VA170BP~LRPROVIDE

R~ONE\~\~\~\~~99VA4^^^^^170~<span class="mark">REDACTED</span>ice - Lab Dev

elopment~99VA4^^^^<span class="mark">REDACTED</span>ice - Lab Developme

nt~L~170\~\~~USVHA

~FI\~~A~170^2301 <span class="mark">REDACTED</span>

OBR^1^1413000033^^87553.0000~Urine Culture~99VA64~5077~URINE CULTURE~99VA60^^^2

0130501112740-0400^^^^P^^^20130501112744-0400^UR&Urine&HL70070&78014005&Uri

ne (substance)&SCT&&20060101&URINE\~\~~122575003&Urine specimen (specimen)&SC

T&15&URINE&99VA6

2&20060101&&URINE\~~RT&ROOM TEMPERATURE&99VA62.93^100884-VA170BP~LRPROVIDER~ONE~

\~\~\~~99VA4^^LA7V HOST 522^\F\\F\12\F\3130000\F\33\F\MICRO 13 33\F\1413000033

\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~522

-----------------------------------------------------------------------------

MYCOLOGY:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130521114919-0400^^ORM~O01^522

90645^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

---\>S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^1W

ORC^NW^1413000095^^522-20130521-1^^^\~\~\~\~~R^^20130521^^^235-VA170K~LRUSER~ONE\~\~~

\~~99VA4^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^~Build

ing 456\~~TX\~~USA

OBR^1^1413000095^^87994.0000~Micro Mycology Culture~99VA64~554~MYCOLOGY CULTURE

~99VA60^^^20130521105826-0400^^^^P^^^20130521105836-0400^SER&Serum&HL70070&

67922002&Serum (substance)&SCT&&20060101&SERUM\~\~~119297000&Blood specimen (

specimen)&SCT&4&

SERUM&99VA62&20060101&&SERUM\~~REF&REFRIGERATED&99VA62.93^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\95\F\MICRO 13 95\F\1413000095

\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

OBX^1^NM^8301-4~Body height:Len:Pt:\S\Patient:Qn:Estimated~LN\~\~\~~2.19^^198^in~I

nches~LN^^^^^F^^^^522~ZZ BONHAM~99VA4~987654321\~~99VACLIA

OBX^2^NM^8335-2~Body weight:Mass:Pt:\S\Patient:Qn:Estimated~LN\~\~\~~2.19^^86^lb~P

ounds~LN^^^^^F^^^^522~ZZ BONHAM~99VA4~987654321\~~99VACLIA

-----------------------------------------------------------------------------

VIROLOGY:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130521141619-0400^^ORM~O01^522

90654^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^1W

ORC^NW^1413000096^^522-20130521-2^^^\~\~\~\~~R^^20130521^^^235-VA170K~LRUSER~ONE\~\~~

\~~99VA4^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^~Build

ing 456\~~TX\~~USA

OBR^1^1413000096^^93937.0000~Culture Viral~99VA64~1081~VIRAL CULTURE~99VA60^^^2

0130521141513-0400^^^^P^^^20130521141520-0400^SPT&Sputum&HL70070&45710003&S

putum (substance)&SCT&&20060101&SPUTUM\~\~~119334006&Sputum specimen (specime

n)&SCT&18&SPUTUM

&99VA62&20060101&&SPUTUM\~~RT&ROOM TEMPERATURE&99VA62.93^235-VA170K~LRUSER~ONE\~~

\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\96\F\MICRO 13 96\F\1413000096\\

F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

#### Example of Surgical Pathology Order Messages

Figure 3. Example of Surgical Pathology Order Messages

BONE MARROW:

MSH^~\|\\^LA7V REMOTE 170^170^LA7V HOST 522^522^20130714164956-0400^^ORM~O01^170

29215^T^2.3^^^AL^AL^

PID^1^^467321321\~\~~USSSA&&L~SS\|7171914~6~M11\~~PI~170&FS.FO-ALBANY.MED.VA.GOV&DN

S\|5000000423V938388\~\~~USVHA&&HL70363~NI~VA FACILITY ID&200M&L^^LRPATIENT~ONE^

^19600101^M^^\~~0005\~\~~CDC^^^^^^M^^^467321321

PV1^1^O^UNK

ORC^NW^2213000023^^170-20130714-3^^^\~\~\~\~~R^^20130714^^^100884-VA170~LRPROVIDER~

ONE\~\~\~\~~99VA4^^^^^170~<span class="mark">REDACTED</span>ice - Lab Devel

opment~99VA4^^^^<span class="mark">REDACTED</span>ice - Lab Development

~L~170\~\~~USVHA~F

I\~~A~170^2301 <span class="mark">REDACTED</span>

OBR^1^2213000023^^85203.0000~Bone Marrow Aspirate Smear Interp.~99VA64~5093~BON

E MARROW BIOPSY~99VA60^^^201307141644-0400^^^^P^^^201307141647-0400^3138006

&Bone (tissue) structure (body structure)&SCT&322&BONE&99VA61&20060101&5.2&

BONE\~\~~119376003

&Tissue specimen (specimen)&SCT&40&TISSUE&99VA62&20060101&&TISSUE\~~RT&ROOM TEMP

ERATURE&99VA62.93^100884-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^LA7V HOST 522^\F\\

F\15\F\3130000\F\23\F\NSP 13 23\F\2213000023\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~~

\~~522

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^3138006~Bone (tissue) structure (body str

ucture)~SCT~322~BONE~99VA61~20060101~5.2~bone^^^^^^P^^^201307141644-0400^17

0~Dallas Office

of Information Field Office - Lab Development~99VA4

-----------------------------------------------------------------------------

SURGICAL PATHOLOGY:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130618095748-0400^^ORM~O01^522

90858^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^UNK

ORC^NW^2213000036^^522-20130618-1^^^\~\~\~\~~R^^20130618^^^1111111112~LRPROVIDER~ON

E\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~~

~USVHA~FI\~~A~522^~Building 456\~~TX\~~USA

OBR^1^2213000036^^93940.0000~Surgical Pathology Tissue Exam~99VA64~5062~SURGICA

L PATHOLOGY LOG-IN~99VA60^^^201306180953-0400^^^^P^^^201306180954-0400^3993

7001&Skin structure (body structure)&SCT&315&SKIN&99VA61&20060101&5.2&SKIN~

\~~119325001&Skin

(tissue) specimen (specimen)&SCT&37&SKIN&99VA62&20060101&&SKIN\~~RT&ROOM TEMPER

ATURE&99VA62.93^1111111112~LRPROVIDER~ONE\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^LA7

V HOST 170^\F\\F\15\F\3130000\F\36\F\NSP 13 36\F\2213000036\F\1-1^^^^^^^^\~~

\~\~~^^^^^^^\~\~\~\~\~~

170

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^39937001~Skin structure (body structure)~

SCT~315~SKIN~99VA61~20060101~5.2~skin^^^^^^P^^^201306180953-0400^522~ZZ BON

HAM~99VA4

ORC^NW^2213000036^^522-20130618-1^^^\~\~\~\~~R^^20130618^^^1111111112~LRPROVIDER~ON

E\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~~

~USVHA~FI\~~A~522^~Building 456\~~TX\~~USA

OBR^2^2213000036^^93940.0000~Surgical Pathology Tissue Exam~99VA64~5073~TISSUE

EXAM~99VA60^^^201306180953-0400^^^^P^^^201306180954-0400^39937001&Skin stru

cture (body structure)&SCT&315&SKIN&99VA61&20060101&5.2&SKIN\~\~~119325001&Sk

in (tissue) spec

imen (specimen)&SCT&37&SKIN&99VA62&20060101&&SKIN\~~RT&ROOM TEMPERATURE&99VA62.9

3^1111111112~LRPROVIDER~ONE\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^LA7V HOST 170^\F\\

\F\15\F\3130000\F\36\F\NSP 13 36\F\2213000036\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~~

\~\~~170

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^39937001~Skin structure (body structure)~

SCT~315~SKIN~99VA61~20060101~5.2~skin^^^^^^P^^^201306180953-0400^522~ZZ BON

HAM~99VA4

#### Example of Cytology Order Messages

Figure 4. Example of Cytology Order Messages

CYTOLOGY NON-GYN:

MSH^~\|\\^LA7V REMOTE 522^522^LA7V HOST 170^170^20130619090749-0400^^ORM~O01^522

90896^T^2.3^^^AL^AL^

PID^1^^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DN

S^^LRPATIENT~ONE^LRPATIENT~MOM^19600101^M^^\~~0005\~\~~CDC^^^^^^S^^^200911170

PV1^1^O^UNK

ORC^NW^0713000010^^522-20130619-2^^^\~\~\~\~~R^^20130619^^^1111111112~LRPROVIDER~ON

E\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~~

~USVHA~FI\~~A~522^~Building 456\~~TX\~~USA

OBR^1^0713000010^^88757.0000~Cytology Smear non GYN~99VA64~5079~CYTOLOGIC NON-G

YNECOLOGY~99VA60^^^201306190855-0400^^^^P^^^201306190905-0400^TISS&Tissue,

unspecified&HL70070&110925004&Cytologic material of mouth (cell structure)&

SCT&&20060101&CY

TOLOGIC MATERIAL OF MOUTH\~\~~119376003&Tissue specimen (specimen)&SCT&40&TISSUE&

99VA62&20060101&&TISSUE\~~RT&ROOM TEMPERATURE&99VA62.93^1111111112~LRPROVIDE

R~ONE\~~JR~DR~MD\~~USDHHS\~~2~NPI~NPI^^LA7V HOST 170^\F\\F\19\F\3130000\F\10\F

\NCY 13 10\F\071

3000010\F\1-1^^^^^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~170

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^110925004~Cytologic material of mouth (ce

ll structure)~SCT~5133~CYTOLOGIC MATERIAL OF MOUTH~99VA61~20060101~5.2~CYTO

LOGIC MATERIAL O

F MOUTH^^^^^^P^^^201306190855-0400^522~ZZ BONHAM~99VA4

-----------------------------------------------------------------------------

CYTOLOGY GYN:

MSH^~\|\\^LA7V REMOTE 170^170^LA7V HOST 522^522^20130714144052-0400^^ORM~O01^170

29207^T^2.3^^^AL^AL^

PID^1^^467321321\~\~~USSSA&&L~SS\|7171914~6~M11\~~PI~170&FS.FO-ALBANY.MED.VA.GOV&DN

S\|5000000423V938388\~\~~USVHA&&HL70363~NI~VA FACILITY ID&200M&L^^LRPATIENT~ONE^

^19600101^M^^\~~0005\~\~~CDC^^^^^^M^^^467321321

PV1^1^O^UNK

ORC^NW^0713000005^^170-20130714-2^^^\~\~\~\~~R^^20130714^^^100884-VA170~LRPROVIDER~

ONE\~\~\~\~~99VA4^^^^^170~<span class="mark">REDACTED</span>ice - Lab Devel

opment~99VA4^^^^<span class="mark">REDACTED</span>ice - Lab Development

~L~170\~\~~USVHA~F

I\~~A~170^2301 <span class="mark">REDACTED</span>

OBR^1^0713000005^^88577.0000~Cytology Smear GYN~99VA64~5095~CYTOLOGIC GYNECOLOG

Y~99VA60^^^201307141437-0400^^^^P^^^201307141439-0400^110925004&Cytologic m

aterial of mouth (cell structure)&SCT&5133&CYTOLOGIC MATERIAL OF MOUTH&99VA

61&20060101&5.2&

CYTOLOGIC MATERIAL OF MOUTH\~\~~119376003&Tissue specimen (specimen)&SCT&40&TISSU

E&99VA62&20060101&&TISSUE\~~RT&ROOM TEMPERATURE&99VA62.93^100884-VA170~LRPRO

VIDER~ONE\~\~\~\~~99VA4^^LA7V HOST 522^\F\\F\19\F\3130000\F\5\F\NCY 13 5\F\0713

000005\F\1-1^^^^

^^^^\~\~\~\~~R^^^^^^^\~\~\~\~\~~522

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^110925004~Cytologic material of mouth (ce

ll structure)~SCT~5133~CYTOLOGIC MATERIAL OF MOUTH~99VA61~20060101~5.2~CYTO

LOGIC MATERIAL O

F MOUTH^^^^^^P^^^201307141437-0400^170~<span class="mark">REDACTED</span>ic

e - Lab Development~99VA4

### Order Message Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA receives an ORM message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

| ORR | Order Response Message |
|-----|------------------------|
| MSH | Message Header         |
| MSA | Message Acknowledgment |

Upon receipt of the order message, the VistA HL7 package responds with an ACK commit acknowledgment message and the Laboratory system responds with an ORR application acknowledgment message.

#### Example of an Order Message Acknowledgment

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^^^^ORR~O02^^T^2.3^^^AL^NE

MSA^AA^52290654

### Result Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA receives an ORU message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

| ORU       | Observational Results Unsolicited Message |
|-----------|-------------------------------------------|
| MSH       | Message Header                            |
| {\[PID\]  | Patient Identification                    |
| \[PV1\]   | Patient Visit                             |
| {\[ORC\]  | Order Common                              |
| OBR       | Observations Report ID                    |
| {\[NTE\]} | Laboratory Note or Comment                |
| {\[OBX\]  | Observation Segment                       |
| {\[NTE\]} | Laboratory Note or Comment                |
| }         |                                           |
| }         |                                           |
| }         |                                           |

#### Examples of Chemistry/Hematology/Serology Result Messages

Figure 5. Examples of Chemistry/Hematology/Serology Result Messages

Chemistry/hematology/serology:

MSH\|^~\\\|LA7V HOST 522\|522\|LA7V REMOTE 9999\|9999\|20051013222223-0500\|\|ORU

^R01\|0960\|P\|2.2\|\|\|AL\|AL\|

PID\|1\|398^^^HP0124^\|398^0^M11\|01/800-33-0304\|INTEROP^DAUGHTER\|\|19660407\|F\|

\|\|\|\|\|\|\|\|\|\|\|

ORC\|RE\|040116 CH 354\|0452860005\|170-N00183-24\|CM\|\|\|\|\|\|\|^REF:11960^\|\|\|\|\|

9999^DOD-SAIC TEST SYSTEM^99VA4\|\|\|\|DOD-SAIC TEST SYSTEM^L^^^^USVHA&&L^FI^^^

9999\|^^^CA^^USA\|

OBR\|1\|040116 CH 354\|0452860005\|83756.0000^GLUCOSE^99VA64^3407^GLUCOSE^99LST

\|\|\|20040116122401-0500\|\|\|\|\|^\|\|20040116122401-0500\|SER&Serum&HL70070&T-0X500&SERUM&SCT\|^REF:11960^\|\|040116-00042-198149\|\|345\S\CH\S\6959882.877599\|\|

20051013222221-0500\|\|CH\|

OBX\|1\|NM\|2345-7^GLUCOSE:MCNC:PT:SER/PLAS:QN^LN^83756.0000^Glucose^99VA64\|\|

456\|mg/dL\|60-123\|HH\|\|\|F\|\|\|20040116122401-0500\|522^<span class="mark">REDACTED</span>ice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^99VA64_2\|

NTE\|1\|DS\|Glucose results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

Corrected chemistry/hematology/serology:

MSH\|^~\\\|LA7V HOST 522\|522\|LA7V REMOTE 9999\|9999\|20051013223123-0500\|\|ORU^R01

\|0961\|P\|2.2\|\|\|AL\|AL\|

PID\|1\|398^^^HP0124^\|398^0^M11\|01/800-33-0304\|INTEROP^DAUGHTER\|\|19660407\|F

\|\|\|\|\|\|\|\|\|\|\|\|

ORC\|RE\|040116 CH 354\|0452860005\|170-N00183-24\|CM\|\|\|\|\|\|\|^REF:11960^\|\|\|\|\|9999^

DOD-SAIC TEST SYSTEM^99VA4\|\|\|\|DOD-SAIC TEST SYSTEM^L^^^^USVHA&&L^FI^^^9999\|

^^^CA^^USA\|

OBR\|1\|040116 CH 354\|0452860005\|83756.0000^GLUCOSE^99VA64^3407^GLUCOSE^

99LST\|\|\|20040116122401-0500\|\|\|\|\|^\|\|20040116122401-0500\|SER&Serum&HL70070&T-0X500&SERUM&SCT\|^REF:11960^\|\|040116-00042-198149\|\|345\S\CH\S\6959882.877599\|\|

20051013223121-0500\|\|CH\|

NTE\|1\|AC\|GLUCOSE reported incorrectly as 456 by \[235-VA522\].\|VA-LR002^Result Comment^HL70356

NTE\|2\|AC\|Changed to 654 on Oct 13, 2005@22:31 by \[235-VA522\].\|VA-LR002^Result Comment^HL70356

OBX\|1\|NM\|2345-7^GLUCOSE:MCNC:PT:SER/PLAS:QN^LN^83756.0000^Glucose^99VA64\|\|

654\|mg/dL\|60-123\|HH\|\|\|C\|\|\|20040116122401-0500\|522^<span class="mark">REDACTED</span>ice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^

99VA64_2\|

NTE\|1\|DS\|Glucose results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

Add-on chemistry/hematology/serology:

MSH\|^~\\\|LA7V HOST 522\|522\|LA7V REMOTE 9999\|9999\|20051013231243-0500\|\|

ORU^R01\|0962\|P\|2.2\|\|\|AL\|AL\|

PID\|1\|398^^^HP0124^\|398^0^M11\|01/800-33-0304\|INTEROP^DAUGHTER\|\|19660407

\|F\|\|\|\|\|\|\|\|\|\|\|\|

ORC\|RE\|040116 CH 354\|0452860005\|170-N00183-24\|CM\|\|\|\|\|\|\|^REF:11960^\|\|\|\|\|9999

^DOD-SAIC TEST SYSTEM^99VA4\|\|\|\|DOD-SAIC TEST SYSTEM^L^^^^USVHA&&L^FI^^^9999\|

^^^CA^^USA\|

OBR\|1\|040116 CH 354\|0452860005\|81357.0000^Electrolytes^99VA64\|\|\|

20040116122401-0500\|\|\|\|A\|^\|\|20040116122401-0500\|SER&Serum&HL70070&T-0X500&SERUM&SCT\|^REF:11960^\|\|\|\|345\S\CH\S\6959882.877599\|\|20051013231242-0500\|\|CH\|

NTE\|1\|AC\|GLUCOSE reported incorrectly as 456 by \[235-VA522\].\|VA-LR002^Result Comment^HL70356

NTE\|2\|AC\|Changed to 654 on Oct 13, 2005@22:31 by \[235-VA522\].\|VA-LR002^Result Comment^HL70356

OBX\|1\|ST\|2947-0^SODIUM:SCNC:PT:BLD:QN^LN^84295.0000^Sodium^99VA64\|\|

145\|meq/L\|135-145\|\|\|\|F\|\|\|20040116122401-0500\|522^<span class="mark">REDACTED</span>ice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^99VA64_2\|

NTE\|1\|DS\|Sodium results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

OBX\|2\|NM\|2823-3^POTASSIUM:SCNC:PT:SER/PLAS:QN^LN^84140.0000^Potassium

^99VA64\|\|4.6\|meq/L\|3.8-5.3\|\|\|\|F\|\|\|20040116122401-0500\|522^<span class="mark">REDACTED</span>ice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^99VA64_2\|

NTE\|1\|DS\|Potassium results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

OBX\|3\|ST\|2075-0^CHLORIDE:SCNC:PT:SER/PLAS:QN^LN^82435.0000^Chloride^

99VA64\|\|90\|meq/L\|100-108\|L\|\|\|F\|\|\|20040116122401-0500\|522^Dallas Office of Information FieldOffice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^99VA64_2\|

NTE\|1\|DS\|Chloride results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

OBX\|4\|NM\|1963-8^BICARBONATE:SCNC:PT:SER:QN^LN^83646.0000^HCO3^99VA64\|\|

33\|meq/L\|23-31\|H\|\|\|F\|\|\|20040116122401-0500\|522^<span class="mark">REDACTED</span>ice^99VA4\|235-VA522^LRUSER^ONE\|.7000^MANUAL MICRO^99VA64_2\|

NTE\|1\|DS\|HCO3 results from <span class="mark">REDACTED</span>ice.\|

NTE\|2\|DS\|1234 Anyplace Avenue VistA City, TX 99999\|

#### Examples of Microbiology Result Messages

Figure 6. Examples of Microbiology Result Messages

VIROLOGY:

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130521142442-0400^^ORU~R01^170

28935^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^1413000096^1413000096^522-20130521-2^^^\~\~\~\~~R^^^^^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^\~\~~522&ZZ BONHAM&L^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~US

VHA~FI\~~A~522^1234 Anyplace Avenue~Bulding 456~VistA City~TX~99999~USA

OBR^1^1413000096^1413000096^93937.0000~Culture Viral~99VA64~1081~VIRAL CULTURE~

99VA60^^^20130521141513-0400^^^^O^^^20130521142122-0400^45710003&Sputum (su

bstance)&SCT&SPT&Sputum&HL70070&20060101&&SPUTUM\~\~~119334006&Sputum specime

n (specimen)&SCT

&18&SPUTUM&99VA62&20060101&&SPUTUM^235-VA170K~LRUSER~ONE\~\~\~\~~99VA4^^LA7V HOST 1

70^\F\\F\12\F\3130000\F\96\F\MICRO 13 96\F\1413000096\F\1-1^74\F\MI\F\68694

77.858487^MICRO 13 41\F\12\F\3130000\F\41\F\MICROBIOLOGY\F\MICRO\F\93937.00

00^201305211424-

0400^^VR^F^^^^^^^123456813-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-ALBANY.ME

D.VA.GOV&DNS^^^^^^^^^^^^93937.0000~Culture Viral~99VA64

NTE^1^L^Viral Culture 29^VA-LRMI001~Comment on Specimen (#.99)~HL70364

NTE^2^L^Ledi Pilot^VA-LRMI050~Virology Rpt Remark (#37)~HL70364

OBX^1^CWE^6584-7~Virus identified:Prid:Pt:XXX:Nom:Culture~LN~87590.0000~Viral A

gent~99VA64~2.19~2.14~VIRUS^99VA4:170:17-1^112381006~Genus Dependovirus (or

ganism)~SCT~1037~ADENO-ASSOCIATED (SATELLITE) VIRUSES~99VA61.2~20060101~5.2

~ADENO-ASSOCIATE

D (SATELLITE) VIRUSES^^^A^^^F^^^20130521141513-0400^170~Dallas Office of Inform

ation Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA

170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice -

Lab Development

~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 <span class="mark">REDACTED</span>

OBX^2^CWE^6584-7~Virus identified:Prid:Pt:XXX:Nom:Culture~LN~87590.0000~Viral A

gent~99VA64~2.19~2.14~VIRUS^99VA4:170:17-2^87149006~Aura virus (organism)~S

CT~861~AURA VIRUS~99VA61.2~20060101~5.2~AURA VIRUS^^^A^^^F^^^20130521141513

-0400^170~Dallas

Office of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA

^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Information F

ield Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blv

d.~Suite 600~Arl

ington~TX~76006~USA

-----------------------------------------------------------------------------

MYCOLOGY:

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130521121037-0400^^ORU~R01^170

28927^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^1413000095^1413000095^522-20130521-1^^^\~\~\~\~~R^^^^^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^\~\~~522&ZZ BONHAM&L^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~US

VHA~FI\~~A~522^1234 Anyplace Avenue~Bulding 456~VistA City~TX~99999~USA

OBR^1^1413000095^1413000095^87994.0000~Micro Mycology Culture~99VA64~554~MYCOLO

GY CULTURE~99VA60^^^20130521105826-0400^^^^O^^^20130521115622-0400^67922002

&Serum (substance)&SCT&SER&Serum&HL70070&20060101&&SERUM\~\~~119297000&Blood

specimen (specim

en)&SCT&4&SERUM&99VA62&20060101&&SERUM^235-VA170K~LRUSER~ONE\~\~\~\~~99VA4^^LA7V HO

ST 170^\F\\F\12\F\3130000\F\95\F\MICRO 13 95\F\1413000095\F\1-1^74\F\MI\F\6

869477.894174^MICRO 13 40\F\12\F\3130000\F\40\F\MICROBIOLOGY\F\MICRO\F\8799

4.0000^201305211

210-0400^^MYC^F^^^^^^^123456813-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-ALBA

NY.MED.VA.GOV&DNS^^^^^^^^^^^^87040~BLOOD CULTURE FOR BACTERIA~C4~87994.0000

~Micro Mycology Culture~99VA64

NTE^1^L^Patrick's Mycology test for HL7 Spec.^VA-LRMI001~Comment on Specimen (#

.99)~HL70364

NTE^2^L^Slow Growing^VA-LRMI030~Mycology RPT Remark (#21)~HL70364

OBX^1^CWE^580-1~Fungus identified:Prid:Pt:XXX:Nom:Culture~LN~87578.0000~Fungal

---\>Organism~99VA64~2.19~2.14~FUNGUS/YEAST^99VA4:170:9-1^57145009~Absidia (orga

---\>nism)~SCT~1191~ABSIDIA~99VA61.2~20060101~5.2~ABSIDIA^^^A^^^F^^^201305211058

---\>26-0400^170~Dall

as Office of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACL

---\>IA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Information

---\> Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar B

---\>lvd.~Suite 600~A

rlington~TX~76006~USA

NTE^1^L^Test comment...^RE~Remark~HL70364

OBX^2^ST^19101-5~Fungus colony count:NCnc:Pt:XXX:Qn:Culture~LN~87723.0000~Colon

---\>y Count Fungal~99VA64~2.19~2.14~QUANTITY^99VA4:170:9-1^2+^^^^^^F^^^20130521

---\>105826-0400^170~<span class="mark">REDACTED</span>ice - Lab Development

---\>~99VA4~ZZZZZ9999

\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Informa

---\>tion Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lam

---\>ar Blvd.~Suite 600~Arlington~TX~76006~USA

-----------------------------------------------------------------------------

MYCOBACTERIUM TB:

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130617124306-0400^^ORU~R01^170

29095^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^1413000105^1413000105^522-20130617-1^^^\~\~\~\~~R^^^^^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^\~\~~522&ZZ BONHAM&L^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~US

VHA~FI\~~A~522^1234 Anyplace Avenue~Bulding 456~VistA City~TX~99999~USA

OBR^1^1413000105^1413000105^93935.0000~Culture \T\\ Sensitivity~99VA64~548~CULTU

RE \T\\ SUSCEPTIBILITY~99VA60^^^20130617122333-0400^^^^O^^^20130617122617-04

00^45710003&Sputum (substance)&SCT&SPT&Sputum&HL70070&20060101&&SPUTUM\~\~~11

9334006&Sputum s

pecimen (specimen)&SCT&18&SPUTUM&99VA62&20060101&&SPUTUM^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\105\F\MICRO 13 105\F\14130001

05\F\1-1^74\F\MI\F\6869381.877667^MICRO 13 48\F\12\F\3130000\F\48\F\MICROBI

OLOGY\F\MICRO\F\\

93935.0000^201306171242-0400^^MB^F^^^^^^^123456813-VA170&HUA&PATRICK&&&&&99VA4~

\~\~\~\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^^^^^^^^^^93935.0000~Culture \T\\ Sens

itivity~99VA64

NTE^1^L^Med Induced^VA-LRMI001~Comment on Specimen (#.99)~HL70364

NTE^2^L^SO for Confirmation^VA-LRMI010~Bact Rpt Remark (#13)~HL70364

OBX^1^ST^664-3~Microscopic observation:Prid:Pt:XXX:Nom:Gram stain~LN~87754.0000

~Gram Stain~99VA64~2.19~2.14~GRAM STAIN^^ACID FAST STAIN^^^^^^F^^^201306171

22333-0400^170~<span class="mark">REDACTED</span>ice - Lab Development~

99VA4~ZZZZZ9999~

~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Informat

ion Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lama

r Blvd.~Suite 600~Arlington~TX~76006~USA

OBX^2^CWE^11475-1~Microorganism identified:Prid:Pt:XXX:Nom:Culture~LN~87570.000

0~Bacteriology Organism~99VA64~2.19~2.14~ORGANISM^99VA4:170:3-1^45662006~My

cobacterium terrae (organism)~SCT~642~MYCOBACTERIUM TERRAE~99VA61.2~2006010

1~5.2~MYCOBACTER

IUM TERRAE^^^A^^^F^^^20130617122333-0400^170~Dallas Office of Information Field

Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDE

R~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab Develo

pment~L\~\~\~~CLIA~

LN\~~A~ZZZZZ9999^2301 <span class="mark">REDACTED</span>

NTE^1^L^Heat treated^RE~Remark~HL70364

OBX^3^ST^564-5~Colony count:Num:Pt:XXX:Qn:VC~LN~87719.0000~Colony Count~99VA64~

2.19~2.14~QUANTITY^99VA4:170:3-1^3+^^^^^^F^^^20130617122333-0400^170~Dallas

Office of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VA

CLIA^123456813-V

A170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - La

b Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 <span class="mark">REACATED</span>

OBR^2^1413000105^1413000105^93935.0000~Culture \T\\ Sensitivity~99VA64~548~CULTU

RE \T\\ SUSCEPTIBILITY~99VA60^^^20130617122333-0400^^^^^^^20130617122617-040

0^45710003&Sputum (substance)&SCT&SPT&Sputum&HL70070&20060101&&SPUTUM\~\~~119

334006&Sputum sp

ecimen (specimen)&SCT&18&SPUTUM&99VA62&20060101&&SPUTUM^235-VA170K~LRUSER~ONE\~~

\~\~~99VA4^^LA7V HOST 170^\F\\F\12\F\3130000\F\105\F\MICRO 13 105\F\141300010

5\F\1-1^74\F\MI\F\6869381.877667^MICRO 13 48\F\12\F\3130000\F\48\F\MICROBIO

LOGY\F\MICRO\F\8

7565.0000^201306171242-0400^^MB^F^11475-1&Microorganism identified:Prid:Pt:XXX:

Nom:Culture&LN&87570.0000&Bacteriology Organism&99VA64&2.19&2.14&ORGANISM~9

9VA4:170:3-1~Mycobacterium terrae (organism)^^^1413000105~1413000105^^^1234

56813-VA170&LRPROVIDER&

ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^^^^^^^^^^87565.0000~Ba

cteriology Susc~99VA64

OBX^1^CWE^18953-0~Neomycin:Susc:Pt:Isolate:OrdQn~LN~93538.0000~Neomycin Susc~99

VA64~2.19~2.14~NEOMYCN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^^ALWA

YS DISPLAY^20130617122333-0400^170~<span class="mark">REDACTED</span>ic

e - Lab Developm

ent~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dalla

s Office of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZ

Z9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^2^CWE^18870-6~Bacitracin:Susc:Pt:Isolate:OrdQn~LN~93457.0000~Bacitracin Sus

c~99VA64~2.19~2.14~BACTRCN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^^

RESTRICT DISPLAY^20130617122333-0400^170~Dallas Office of Information Field

Office - Lab De

velopment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^

^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~LN\~~

A~ZZZZZ9999^2301 <span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^3^CWE^18964-7~Penicillin:Susc:Pt:Isolate:OrdQn~LN~93549.0000~Penicillin Sus

c~99VA64~2.19~2.14~PENICLN^^131196009~Susceptible~SCT\~\~\~~20060101\~~S^^^S^^^

F^^ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information Fiel

d Office - Lab D

evelopment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^

^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~LN~

~A~ZZZZZ9999^ <span class="mark">REDACTED</span>

OBX^4^CWE^18908-4~Clindamycin:Susc:Pt:Isolate:OrdQn~LN~93495.0000~Clindamycin S

usc~99VA64~2.19~2.14~CLINDAM^^131196009~Susceptible~SCT\~\~\~~20060101\~~S^^^S^

^^F^^ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information Fi

eld Office - Lab

Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^

^^^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~L

N\~~A~ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^5^CWE^18945-6~Methicillin:Susc:Pt:Isolate:OrdQn~LN~93530.0000~Methicillin S

usc~99VA64~2.19~2.14~METHCLN^^131196009~Susceptible~SCT\~\~\~~20060101\~~S^^^S^

^^F^^ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information Fi

eld Office - Lab

Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^

^^^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~L

N\~~A~ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^6^CWE^19000-9~Vancomycin:Susc:Pt:Isolate:OrdQn~LN~93585.0000~Vancomycin Sus

c~99VA64~2.19~2.14~VANCMCN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^^

ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information Field O

ffice - Lab Deve

lopment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^D

allas Office of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~

ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^7^CWE^18928-2~Gentamicin:Susc:Pt:Isolate:OrdQn~LN~93514.0000~Gentamicin Sus

c~99VA64~2.19~2.14~GENTMCN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^^

ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information Field O

ffice - Lab Deve

lopment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^D

allas Office of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~

ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^8^CWE^18903-5~Chloramphenicol:Susc:Pt:Isolate:OrdQn~LN~93490.0000~Chloramph

en Susc~99VA64~2.19~2.14~CHLORAM^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R

^^^F^^ALWAYS DISPLAY^20130617122333-0400^170~Dallas Office of Information F

ield Office - La

b Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^

^^^^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~

LN\~~A~ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^9^CWE^18935-7~Kanamycin:Susc:Pt:Isolate:OrdQn~LN~93520.0000~Kanamycin Susc~

99VA64~2.19~2.14~KANAMCN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^^AL

WAYS DISPLAY^20130617122333-0400^170~<span class="mark">REDACTED</span>

ice - Lab Develo

pment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dal

las Office of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZ

ZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

OBX^10^CWE^18878-9~Cefazolin:Susc:Pt:Isolate:OrdQn~LN~93465.0000~Cefazolin Susc

~99VA64~2.19~2.14~CEFAZOLIN^^30714006~Resistant~SCT\~\~\~~20060101\~~R^^^R^^^F^

^RESTRICT DISPLAY^20130617122333-0400^170~Dallas Office of Information Fiel

d Office - Lab D

evelopment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^

^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~LN~

~A~ZZZZZ9999^<span class="mark">REDACTED</span>

NTE^1^L^TESTING DISPLAY COMMENT^RE~Remark~HL70364

-----------------------------------------------------------------------------

PARASITOLOGY ORU:

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130522012431-0400^^ORU~R01^170

28951^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^1413000098^1413000098^522-20130522-1^^^\~\~\~\~~R^^^^^235-VA170K~LRUSER~ONE~

\~\~\~~99VA4^\~\~~522&ZZ BONHAM&L^^^^522~ZZ BONHAM~99VA4^^^^ZZ BONHAM~D~522\~\~~US

VHA~FI\~~A~522^1234 Anyplace Avenue~Bulding 456~VistA City~TX~99999~USA

OBR^1^1413000098^1413000098^93933.0000~Ova Parasite Exam~99VA64~550~PARASITE EX

AM~99VA60^^^20130522011506-0400^^^^O^^^20130522011939-0400^39477002&Feces (

substance)&SCT&STL&Stool=Fecal&HL70070&20060101&&FECES\~\~~119339001&Stool sp

ecimen (specimen

)&SCT&17&STOOL&99VA62&20060101&&STOOL^235-VA170K~LRUSER~ONE\~\~\~\~~99VA4^^LA7V HOS

T 170^\F\\F\12\F\3130000\F\98\F\MICRO 13 98\F\1413000098\F\1-1^74\F\MI\F\68

69476.988494^MICRO 13 43\F\12\F\3130000\F\43\F\MICROBIOLOGY\F\MICRO\F\93933

.0000^2013052201

24-0400^^PAR^F^^^^^^^123456813-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-ALBAN

Y.MED.VA.GOV&DNS^^^^^^^^^^^^93933.0000~Ova Parasite Exam~99VA64

NTE^1^L^Float Concentration^VA-LRMI001~Comment on Specimen (#.99)~HL70364

NTE^2^L^72 Hrs Specimen^VA-LRMI020~Parasite Rpt Remark (#17)~HL70364

OBX^1^CWE^20932-0~Parasite identified:Prid:Pt:XXX:Nom:Inspection~LN~87576.0000~

Parasite Organism~99VA64~2.19~2.14~PARASITE^99VA4:170:6-1^1425~ASCARIS, NOS

~99VA61.2\~\~\~~5.2\~~ASCARIS, NOS^^^A^^^F^^^20130522011506-0400^170~Dallas Off

ice of Informati

on Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER

~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab De

velopment~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlingt

on~TX~76006~USA

OBX^2^CWE^92930.0000~Parasite Stages~99VA64~MI-16-.01~STAGE~99VA63~2.14~5.2~STA

GE^99VA4:170:6-1^103552005~Cyst form of protozoa~SCT\~\~\~~20060101\~~CYSTS^^^A

^^^F^^^20130522011506-0400^170~<span class="mark">REDACTED</span>ice -

Lab Development~

99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Of

fice of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ999

9^<span class="mark">REDACTED</span>

OBX^3^ST^93997.0000~Parasite Stage Quant#~99VA64~MI-16-1~QUANTITY~99VA63~2.14~5

.2~QUANTITY^99VA4:170:6-1^10^^^A^^^F^^^20130522011506-0400^170~Dallas Offic

e of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^1

23456813-VA170~L

RPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab Deve

lopment~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlington

~TX~76006~USA

OBX^4^CWE^92930.0000~Parasite Stages~99VA64~MI-16-.01~STAGE~99VA63~2.14~5.2~STA

GE^99VA4:170:6-1^2105009~Microfilaria~SCT\~\~\~~20060101\~~MICROFILARIA^^^A^^^F

^^^20130522011506-0400^170~<span class="mark">REDACTED</span>ice - Lab

Development~99VA

4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office

of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^23

01 East Lamar Blvd.~Suite 600~Arlington~TX~76006~USA

OBX^5^ST^93997.0000~Parasite Stage Quant#~99VA64~MI-16-1~QUANTITY~99VA63~2.14~5

.2~QUANTITY^99VA4:170:6-1^15^^^A^^^F^^^20130522011506-0400^170~Dallas Offic

e of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^1

23456813-VA170~L

RPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab Deve

lopment~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlington

~TX~76006~USA

-----------------------------------------------------------------------------

BACTERIOLOGY (No growth):

MSH\|^~\\\|LA7V HOST 522\|522\|LA7V REMOTE 170\|170\|20130521190356-0400\|\|ORU^R01\|522

90667\|T\|2.3\|\|\|AL\|AL\|

PID\|1\|467321321^^^USSSA&&L^SS~7171914^6^M11^^PI^170&FS.FO-ALBANY.MED.VA.GOV&DNS

~5000000423V938388^^^USVHA&&HL70363^NI^VA FACILITY ID&200M&L\|467321321^^^US

SSA&&L^SS~7171914^6^M11^^PI^170&FS.FO-ALBANY.MED.VA.GOV&DNS~5000000423V9383

88^^^USVHA&&HL70

363^NI^VA FACILITY ID&200M&L\|391^3^M11^^U\|LRPATIENT^ONE\|\|19600101\|M\|\|\|\|\|\|\|\|\|\|\|467

321321

PV1\|1\|O\|1W

ORC\|RE\|1413000042\|1413000097\|170-20130521-1\|\|\|^^^^^R\|\|\|\|\|100884-VA170BP^LRPROVI

DER^ONE^^^^^99VA4\|^^^170&VAHVRR.FO-ALBANY.MED.VA.GOV&DNS\|\|\|\|170^Dallas Offi

ce of Information Field Office - Lab Development^99VA4\|\|\|\|Dallas Office of

Information Fiel

d Office - Lab Development^L^170^^^USVHA^FI^^A^170\|2301 East Lamar Blvd.^Suite

600^Arlington^TX^76006^USA

OBR\|1\|1413000042\|1413000097\|87553.0000^Urine Culture^99VA64^5077^URINE CULTURE^

---\>99VA60\|\|\|20130521183212-0400\|\|\|\|O\|\|\|20130521183927-0400\|78014005&Urine (sub

---\>stance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^60&URINE SPECIMEN&99VA62&&&&

---\>&&URINE SPECIMEN

\|100884-VA170BP^LRPROVIDER^ONE^^^^^99VA4\|\|LA7V HOST 522\|\S\\S\12\S\3130000\S\42

---\>\S\MICRO 13 42\S\1413000042\S\1-1\|391\S\MI\S\6869477.816788\|MICRO 13 97\S\1

---\>2\S\3130000\S\97\S\MICROBIOLOGY\S\MICRO\S\87553.0000\|201305211903-0400\|\|MB\|

---\>F\|\|\|\|\|\|\|6738-VA5

22&LRUSER&ONE&&&&&99VA4^^^^^^522&FS.FO-ALBANY.MED.VA.GOV&DNS\|\|\|\|\|\|\|\|\|\|\|\|81007^

---\>URINE SCREEN FOR BACTERIA^C4^87553.0000^Urine Culture^99VA64

NTE\|1\|L\|Testing LDSI urine culture\|VA-LRMI001^Comment on Specimen (#.99)^HL70364

NTE\|2\|L\|No growth\|VA-LRMI010^Bact Rpt Remark (#13)^HL70364

OBX\|1\|ST\|664-3^MICROSCOPIC OBSERVATION:PRID:PT:XXX:NOM:GRAM STAIN^LN^

87754.0000^Gram Stain^99VA64^2.19^2.14^GRAM STAIN\|\|No organism seen\|\|\|\|\|\|F\|\|\|20130521183212-0400\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|6738-VA522^LRUSER^

ONE^^^^^99VA4\|\|\|\|\|\|\|

OBX\|2\|CWE\|11475-1^MICROORGANISM IDENTIFIED:PRID:PT:XXX:NOM:CULTURE^LN^

87570.0000^Bacteriology Organism^99VA64^2.19^2.14^ORGANISM\|\|2648680006^No growth^SCT\|\|\|A\|\|\|F\|\|\|20130521183212-0400\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA \|6738-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

-----------------------------------------------------------------------------

BACTERIOLOGY (Growth):

MSH\|^~\\\|LA7V HOST 522\|522\|LA7V REMOTE 170\|170\|20130501113957-0400\|\|ORU^R01

\|52290568\|P\|2.3\|\|\|AL\|AL\|

PID\|1\|467321321^^^USSSA&&L^SS~7171914^6^M11^^PI^170&FS.FO-ALBANY.MED.VA.GOV&DNS

~5000000423V938388^^^USVHA&&HL70363^NI^VA FACILITY ID&200M&L\|467321321^^^US

SSA&&L^SS~7171914^6^M11^^PI^170&FS.FO-ALBANY.MED.VA.GOV&DNS~5000000423V9383

88^^^USVHA&&HL70

363^NI^VA FACILITY ID&200M&L\|391^3^M11^^U\|LRPATIENT^ONE\|\|19600101\|M\|\|\|\|\|\|\|\|\|\|\|467

321321

PV1\|1\|O\|1W

ORC\|RE\|1413000033\|1413000090\|170-20130501-2\|\|\|^^^^^R\|\|\|\|\|100884-VA170BP^LRPROVI

DER^ONE^^^^^99VA4\|^^^170&VAHVRR.FO-ALBANY.MED.VA.GOV&DNS\|\|\|\|170^Dallas Offi

ce of Information Field Office - Lab Development^99VA4\|\|\|\|Dallas Office of

Information Fiel

d Office - Lab Development^L^170^^^USVHA^FI^^A^170\|2301 East Lamar Blvd.^Suite

600^Arlington^TX^76006^USA

OBR\|1\|1413000033\|1413000090\|87553.0000^Urine Culture^99VA64^5077^URINE CULTURE^

99VA60\|\|\|20130501112740-0400\|\|\|\|O\|\|\|20130501113036-0400\|78014005&Urine (sub

stance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^60&URINE SPECIMEN&99VA62&&&&

&&URINE SPECIMEN

\|100884-VA170BP^LRPROVIDER^ONE^^^^^99VA4\|\|LA7V HOST 522\|\S\\S\12\S\3130000\S\33

\S\MICRO 13 33\S\1413000033\S\1-1\|391\S\MI\S\6869497.88726\|MICRO 13 90\S\12

\S\3130000\S\90\S\MICROBIOLOGY\S\MICRO\S\87553.0000\|201305011139-0400\|\|MB\|F

\|\|\|\|\|\|\|6738-VA52

2&LRUSER&ONE&&&&&99VA4^^^^^^522&FS.FO-ALBANY.MED.VA.GOV&DNS\|\|\|\|\|\|\|\|\|\|\|\|81007^U

RINE SCREEN FOR BACTERIA^C4^87553.0000^Urine Culture^99VA64

NTE\|1\|L\|LEDI ordering\|VA-LRMI001^Comment on Specimen (#.99)^HL70364

NTE\|2\|L\|Pos WBC inclusions \|VA-LRMI010^Bact Rpt Remark (#13)^HL70364

OBX\|1\|ST\|664-3^MICROSCOPIC OBSERVATION:PRID:PT:XXX:NOM:GRAM STAIN^LN^

87754.0000^Gram Stain^99VA64^2.19^2.14^GRAM STAIN\|\|GNC in clusters\|\|\|\|\|\|F\|\|\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|2\|CWE\|11475-1^MICROORGANISM IDENTIFIED:PRID:PT:XXX:NOM:CULTURE^LN

^87570.0000^Bacteriology Organism^99VA64^2.19^2.14^ORGANISM\|99VA4:522:3-1\|75566007^NEISSERIA FLAVESCENS (organism)^SCT^394^NEISSERIA FLAVESCENS^99VA61.2^20060101^5.2^NEISSERIA FLAVESCENS\|\|\|A\|\|\|F\|\|\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

NTE\|1\|L\|Mixed Culture \|RE^Remark^HL70364

OBX\|3\|ST\|564-5^COLONY COUNT:NUM:PT:XXX:QN:VC^LN^87719.0000^Colony Count^99VA64^2.19^2.14^QUANTITY\|99VA4:522:3-1\|1+\|\|\|\|\|\|F\|\|\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|4\|CWE\|11475-1^MICROORGANISM IDENTIFIED:PRID:PT:XXX:NOM:CULTURE^LN^

87570.0000^Bacteriology Organism^99VA64^2.19^2.14^ORGANISM\|99VA4:522:3-2\|68704007^NEISSERIA GONORRHOEAE (organism)^SCT^388^NEISSERIA GONORRHOEAE^99VA61.2^20060101^5.2^NEISSERIA GONORRHOEAE\|\|\|A\|\|\|F\|\|\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

NTE\|1\|L\|Confirmed\|RE^Remark^HL70364

OBX\|5\|ST\|564-5^COLONY COUNT:NUM:PT:XXX:QN:VC^LN^87719.0000^Colony Count^99VA64^2.19^2.14^QUANTITY\|99VA4:522:3-2\|2+\|\|\|\|\|\|F\|\|\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBR\|2\|1413000033\|1413000090\|87553.0000^Urine Culture^99VA64^5077^URINE CULTURE^

99VA60\|\|\|20130501112740-0400\|\|\|\|\|\|\|20130501113036-0400\|78014005&Urine (subs

tance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^60&URINE SPECIMEN&99VA62&&&&&

&URINE SPECIMEN\|

100884-VA170BP^LRPROVIDER^ONE^^^^^99VA4\|\|LA7V HOST 522\|\S\\S\12\S\3130000\S\33\\

S\MICRO 13 33\S\1413000033\S\1-1\|391\S\MI\S\6869497.88726\|MICRO 13 90\S\12\\

S\3130000\S\90\S\MICROBIOLOGY\S\MICRO\S\87565.0000\|201305011139-0400\|\|MB\|F\|

11475-1&Microorg

anism identified:Prid:Pt:XXX:Nom:Culture&LN&87570.0000&Bacteriology Organism&99

VA64&2.19&2.14&ORGANISM^99VA4:522:3-1^Neisseria flavescens (organism)\|\|\|141

3000033^1413000090\|\|\|6738-VA522&LRUSER&ONE&&&&&99VA4^^^^^^522&FS.FO-ALBANY

.MED.VA.GOV&DNS\|

\|\|\|\|\|\|\|\|\|\|\|87565.0000^Bacteriology Susc^99VA64

OBX\|1\|CWE\|356-6^NEOMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88211.0000^

Neomycin Susc^99VA64^2.19^2.14^NEOMYCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|2\|CWE\|10868-8^BACITRACIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^87824.0000

^Bacitracin Susc^99VA64^2.19^2.14^BACTRCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|3\|CWE\|13968-3^PENICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88243.0000

^Penicillin Susc^99VA64^2.19^2.14^PENICILLIN LONG NAME\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|4\|CWE\|194-1^CLINDAMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^87934.0000^

Clindamycin Susc^99VA64^2.19^2.14^CLINDAM\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|5\|CWE\|324-4^METHICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88189.0000^

Methicillin Susc^99VA64^2.19^2.14^METHCLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|6\|CWE\|525-6^VANCOMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88346.0000^Vancomycin Susc^99VA64^2.19^2.14^VANCMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|7\|CWE\|268-3^GENTAMICIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88154.0000^

Gentamicin Susc^99VA64^2.19^2.14^GENTMCN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|8\|CWE\|174-3^CHLORAMPHENICOL:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^

87916.0000^Chloramphenicol Susc^99VA64^2.19^2.14^CHLORAM\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|9\|CWE\|292-3^KANAMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88173.0000^

Kanamycin Susc^99VA64^2.19^2.14^KANAMCN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|10\|CWE\|77-8^CEFAZOLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^87843.0000^

Cefazolin Susc^99VA64^2.19^2.14^CEFAZOLIN\|\|30714006^Resistant^SCT^^^^20060101^^R\|\|\|R\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBR\|3\|1413000033\|1413000090\|87553.0000^Urine Culture^99VA64^5077^URINE CULTURE^

99VA60\|\|\|20130501112740-0400\|\|\|\|\|\|\|20130501113036-0400\|78014005&Urine (subs

tance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^60&URINE SPECIMEN&99VA62&&&&&

&URINE SPECIMEN\|

100884-VA170BP^LRPROVIDER^ONE^^^^^99VA4\|\|LA7V HOST 522\|\S\\S\12\S\3130000\S\33\\

S\MICRO 13 33\S\1413000033\S\1-1\|391\S\MI\S\6869497.88726\|MICRO 13 90\S\12\\

S\3130000\S\90\S\MICROBIOLOGY\S\MICRO\S\87565.0000\|201305011139-0400\|\|MB\|F\|

11475-1&Microorg

anism identified:Prid:Pt:XXX:Nom:Culture&LN&87570.0000&Bacteriology Organism&99

VA64&2.19&2.14&ORGANISM^99VA4:522:3-2^Neisseria gonorrhoeae (organism)\|\|\|14

13000033^1413000090\|\|\|6738-VA522&LRUSER&ONE&&&&&99VA4^^^^^^522&FS.FO-ALBAN

Y.MED.VA.GOV&DNS

\|\|\|\|\|\|\|\|\|\|\|\|87565.0000^Bacteriology Susc^99VA64

OBX\|1\|CWE\|13968-3^PENICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88243.0000^Penicillin Susc^99VA64^2.19^2.14^PENICILLIN LONG NAME\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|2\|CWE\|174-3^CHLORAMPHENICOL:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN

^87916.0000^Chloramphenicol Susc^99VA64^2.19^2.14^CHLORAM\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|3\|CWE\|497-8^TETRACYCLINE:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88303.0000^

Tetracycline Susc^99VA64^2.19^2.14^TETRCLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

OBX\|4\|CWE\|29-9^AMPICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^87809.0000^

Ampicillin Susc^99VA64^2.19^2.14^AMPICLN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

NTE\|1\|L\|DISPLAY COMMENT\|RE^Remark^HL70364

OBX\|5\|CWE\|234-5^ERYTHROMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION^LN^88096.0000^

Erythromycin Susc^99VA64^2.19^2.14^ERYTHROMYCIN\|\|131196009^Susceptible^SCT^^^^20060101^^S\|\|\|S\|\|\|F\|\|ALWAYS DISPLAY\|20050929184844-0500\|522^ZZ BONHAM^99VA4^987654321^^99VACLIA\|104-VA522^LRUSER^ONE^^^^^99VA4\|\|\|\|\|\|\|ZZ BONHAM^D^^^^CLIA^LN^^A^987654321\|^Building 456^^TX^^USA

Example of Surgical Pathology Result Message

Figure 7. Example of Surgical Pathology Result Message

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130618101744-0400^^ORU~R01^170

29115^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

---\>^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

---\>74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^2213000036^2213000036^522-20130618-1^^^\~\~\~\~~R^^^^^1111111112~LRPROVIDER~

ONE\~~JR DR\~\~\~~USDHHS\~\~\~~NPI^^^^^170~<span class="mark">REDACTED</span>i

ce - Lab Development~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^1234 Anypla

ce Avenue~Buldin

g 456~VistA City~TX~99999~USA

OBR^1^2213000036^2213000036^93940.0000~Surgical Pathology Tissue Exam~99VA64~50

62~SURGICAL PATHOLOGY LOG-IN~99VA60^^^20130618^^^^O^^^201306181007-0400^399

37001&Skin structure (body structure)&SCT&315&SKIN&99VA61&20060101&5.2&SKIN

\~\~~119325001&Ski

n (tissue) specimen (specimen)&SCT&37&SKIN&99VA62&20060101&&SKIN^1111111112~LRP

ROVIDER~ONE\~~JR DR\~\~\~~USDHHS\~\~\~~NPI^^LA7V HOST 170^\F\\F\15\F\3130000\F\36\\

F\NSP 13 36\F\2213000036\F\1-1^74\F\SP\F\6869380.9047^NSP 13 17\F\15\F\3130

000\F\17\F\SURGI

CAL PATHOLOGY\F\NSP\F\93940.0000^20130618101729-0400^^SP^F^^^^^^^100884-VA170&L

RPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^&PH&&&&&\~\~\~~

\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^^^^^^^93940.0000~Surgical Pathology Tis

sue Exam~99VA64

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^39937001~Skin structure (body structure)~

SCT~315~SKIN~99VA61~20060101~5.2~Skin structure (body structure)^^^^^^F^^^2

01306180953-0400

^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~ZZZZZ999

9\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of In

formation Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 Eas

t Lamar Blvd.~Su

ite 600~Arlington~TX~76006~USA

OBX^2^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-2^39937001~Skin structure (body structure)~

SCT~315~SKIN~99VA61~20060101~5.2~Skin structure (body structure)^^^^^^F^^^2

01306180953-0400

^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~ZZZZZ999

9\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of In

formation Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 Eas

t Lamar Blvd.~Su

ite 600~Arlington~TX~76006~USA

OBX^3^FT^22634-0~Path report.gross observation:Find:Pt:Specimen:Nar~LN~88549.00

00~Description Gross~99VA64~2.19~2.14^^This section will indicate the gross

description recorded for this \\br\specimen.\\br\\^^^^^F^^^201306180953-04

00^170~Dallas Of

fice of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^12

3456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Information Fiel

d Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~

Suite 600~Arling

ton~TX~76006~USA

OBX^4^FT^22635-7~Path report.microscopic observation:Prid:Pt:Specimen:Nar:XXX s

tain~LN~88563.0000~Description Micro~99VA64~2.19~2.14^^This section will in

dicate the microscopic description recorded for this \\br\specimen.\\br\\^^

^^^F^^^201306180

953-0400^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~

ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Offi

ce of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^

2301 East Lamar

Blvd.~Suite 600~Arlington~TX~76006~USA

OBX^5^FT^22635-7~Path report.microscopic observation:Prid:Pt:Specimen:Nar:XXX s

tain~LN~88569.0000~Frozen Section~99VA64~2.19~2.14^^This is the area of the

report which will contain the frozen section \\br\report if one was perfor

med.\\br\\^^^^^F

^^^201306180953-0400^170~<span class="mark">REDACTED</span>ice - Lab Develo

pment~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^

^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~LN\~~

A~ZZZZZ9999^2301

East Lamar Blvd.~Suite 600~Arlington~TX~76006~USA

OBX^6^FT^22637-3~Path report.final diagnosis:Imp:Pt:Specimen:Nar~LN~88571.0000~

Diagnosis Pathology~99VA64~2.19~2.14^^This section will indicate the surgic

al path diagnosis.\\br\\^^^^^F^^^201306180953-0400^170~Dallas Office of Inf

ormation Field O

ffice - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~~

\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab Development~

L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlington~TX~7600

6~USA

#### Example of Electron Microscopy Result Message

Figure 8. Example of Electron Microscopy Result Message

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130701120133-0400^^ORU~R01^170

29195^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^1013000002^1013000002^522-20130701-1^^^\~\~\~\~~R^^^^^1111111112~LRPROVIDER~

ONE\~~JR DR\~\~\~~USDHHS\~\~\~~NPI^^^^^170~<span class="mark">REDACTED</span>i

ce - Lab Development~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^1234 Anypla

ce Avenue~Buldin

g 456~VistA City~TX~99999~USA

OBR^1^1013000002^1013000002^88597.0000~Report Electron Microscopy~99VA64~5084~E

M TISSUE EXAM~99VA60^^^20130701^^^^O^^^20130701115505-0400^39937001&Skin st

ructure (body structure)&SCT&315&SKIN&99VA61&20060101&5.2&SKIN\~\~~119376003&

Tissue specimen

(specimen)&SCT&40&TISSUE&99VA62&20060101&&TISSUE^1111111112~LRPROVIDER~ONE\~~JR

DR\~\~\~~USDHHS\~\~\~~NPI^^LA7V HOST 170^\F\\F\16\F\3130000\F\2\F\EM 13 2\F\10130

00002\F\1-1^74\F\EM\F\6869297.8863^NEM 13 1\F\16\F\3130000\F\1\F\EM\F\NEM\F

\88597.0000^2013

0701120113-0400^^PAT^F^^^^^^^45-VA170&LRPROVIDER&TWO&&&&&99VA4\~\~\~\~\~~170&FS.FO-A

LBANY.MED.VA.GOV&DNS^100884-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-A

LBANY.MED.VA.GOV&DNS^100884-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&FS.FO-A

LBANY.MED.VA.GOV

&DNS^&PH&&&&&\~\~\~\~\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^^^^^^^88597.0000~Report El

ectron Microscopy~99VA64

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88057.0000

~EM Specimen~99VA64~2.19~2.14^SPEC-1^39937001~Skin structure (body structur

e)~SCT~315~SKIN~99VA61~20060101~5.2~Skin structure (body structure)^^^^^^F^

^^201307011137-0

400^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~ZZZZZ

9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of

Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301

East Lamar Blvd.

~Suite 600~Arlington~TX~76006~USA

OBX^2^FT^22634-0~Path report.gross observation:Find:Pt:Specimen:Nar~LN~88549.00

00~Description Gross~99VA64~2.19~2.14^^This section will indicate the gross

description recorded for this \\br\specimen.\\br\\^^^^^F^^^201307011137-04

00^170~Dallas Of

fice of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^12

3456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Information Fiel

d Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~

Suite 600~Arling

ton~TX~76006~USA

OBX^3^FT^22635-7~Path report.microscopic observation:Prid:Pt:Specimen:Nar:XXX s

tain~LN~88563.0000~Description Micro~99VA64~2.19~2.14^^This section will in

dicate the microscopic examination recorded for this \\br\specimen.\\br\\^^

^^^F^^^201307011

137-0400^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~

ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Offi

ce of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^

2301 East Lamar

Blvd.~Suite 600~Arlington~TX~76006~USA

OBX^4^FT^22637-3~Path report.final diagnosis:Imp:Pt:Specimen:Nar~LN~88571.0000~

Diagnosis Pathology~99VA64~2.19~2.14^^This section will indicate the EM dia

gnosis.\\br\\^^^^^F^^^201307011137-0400^170~Dallas Office of Information Fi

eld Office - Lab

Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~PROVIDER~ONE\~\~\~\~~99VA4^^^

^^^^<span class="mark">REDACTED</span>ice - Lab Development~L\~\~\~~CLIA~L

N\~~A~ZZZZZ9999^<span class="mark">REDACTED</span>

#### Example of Cytology Result Message

Figure 9. Example of Cytology Result Message

MSH^~\|\\^LA7V HOST 170^170^LA7V REMOTE 522^522^20130619092017-0400^^ORU~R01^170

29151^T^2.3^^^AL^AL^

PID^1^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS

^200911170\~\~~USSSA&&L~SS\|382~4~M11\~~PI~522&MHCVSS.FO-ALBANY.MED.VA.GOV&DNS^

74~4~M11\~~U^LRPATIENT~ONE^^19600101^M^^^^^^^^^^^200911170

PV1^1^O^

ORC^RE^0713000010^0713000010^522-20130619-2^^^\~\~\~\~~R^^^^^1111111112~LRPROVIDER~

ONE\~~JR DR\~\~\~~USDHHS\~\~\~~NPI^^^^^170~<span class="mark">REDACTED</span>i

ce - Lab Development~99VA4^^^^ZZ BONHAM~D~522\~\~~USVHA~FI\~~A~522^1234 Anypla

ce Avenue~Buldin

g 456~VistA City~TX~99999~USA

OBR^1^0713000010^0713000010^88757.0000~Cytology Smear non GYN~99VA64~5079~CYTOL

OGIC NON-GYNECOLOGY~99VA60^^^20130619^^^^O^^^20130619091351-0400^110925004&

Cytologic material of mouth (cell structure)&SCT&5133&CYTOLOGIC MATERIAL OF

MOUTH&99VA61&20

060101&5.2&CYTOLOGIC MATERIAL OF MOUTH\~\~~119376003&Tissue specimen (specimen)&S

CT&40&TISSUE&99VA62&20060101&&TISSUE^1111111112~LRPROVIDER~ONE\~~JR DR\~\~\~~US

DHHS\~\~\~~NPI^^LA7V HOST 170^\F\\F\19\F\3130000\F\10\F\NCY 13 10\F\0713000010

\F\1-1^74\F\CY\F

\6869379.9145^NCY 13 3\F\19\F\3130000\F\3\F\CYTOPATHOLOGY\F\NCY\F\88757.0000^20

130619091955-0400^^CP^F^^^^^^^45-VA170&LRPROVIDER&TWO&&&&&99VA4\~\~\~\~\~~170&FS

.FO-ALBANY.MED.VA.GOV&DNS^^100884-VA170&LRPROVIDER&ONE&&&&&99VA4\~\~\~\~\~~170&F

S.FO-ALBANY.MED.

VA.GOV&DNS^&PH&&&&&\~\~\~\~\~~170&FS.FO-ALBANY.MED.VA.GOV&DNS^^^^^^^^^88161~CYTOPATH

SMEAR OTHER SOURCE~C4~88757.0000~Cytology Smear non GYN~99VA64

OBX^1^CWE^22633-2~Path report.site of origin:Anat:Pt:Specimen:Nar~LN~88539.0000

~Specimen~99VA64~2.19~2.14^SPEC-1^110925004~Cytologic material of mouth (ce

ll structure)~SCT~5133~CYTOLOGIC MATERIAL OF MOUTH~99VA61~20060101~5.2~Cyto

logic material o

f mouth (cell structure)^^^^^^F^^^201306190855-0400^170~Dallas Office of Inform

ation Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA

170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice -

Lab Development

~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlington~TX~76006~U

SA

OBX^2^FT^22634-0~Path report.gross observation:Find:Pt:Specimen:Nar~LN~88549.00

00~Description Gross~99VA64~2.19~2.14^^This section will indicate the gross

description recorded for this\\br\specimen.\\br\\^^^^^F^^^201306190855-040

0^170~Dallas Off

ice of Information Field Office - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123

456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Office of Information Field

Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~S

uite 600~Arlingt

on~TX~76006~USA

OBX^3^FT^22635-7~Path report.microscopic observation:Prid:Pt:Specimen:Nar:XXX s

tain~LN~88563.0000~Description Micro~99VA64~2.19~2.14^^This section will in

dicate the microscopic examination recorded for this\\br\specimen.\\br\\^^^

^^F^^^2013061908

55-0400^170~<span class="mark">REDACTED</span>ice - Lab Development~99VA4~Z

ZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~\~\~\~~99VA4^^^^^^^Dallas Offic

e of Information Field Office - Lab Development~L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2

301 East Lamar B

lvd.~Suite 600~Arlington~TX~76006~USA

OBX^4^FT^22637-3~Path report.final diagnosis:Imp:Pt:Specimen:Nar~LN~88571.0000~

Diagnosis Pathology~99VA64~2.19~2.14^^This section will indicate the cytopa

thology diagnosis.\\br\\^^^^^F^^^201306190855-0400^170~Dallas Office of Inf

ormation Field O

ffice - Lab Development~99VA4~ZZZZZ9999\~~99VACLIA^123456813-VA170~LRPROVIDER~ONE\~~

\~\~~99VA4^^^^^^^<span class="mark">REDACTED</span>ice - Lab Development~

L\~\~\~~CLIA~LN\~~A~ZZZZZ9999^2301 East Lamar Blvd.~Suite 600~Arlington~TX~7600

6~USA

### Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA supports enhanced mode acknowledgments. Upon receipt of the result message, the VistA Laboratory system responds with a general acknowledgment (ACK) message. The ACK message consists of the following segments.

| ACK | General Acknowledgment Message |
|-----|--------------------------------|
| MSH | Message Header                 |
| MSA | Message Acknowledgment         |

Upon receipt of the result message, the VistA HL7 package responds with an ACK message for the commit acknowledgment and the Laboratory system responds with a general acknowledgment (ACK) message for the application acknowledgment.

#### Example of the Acknowledgment Message

Figure 10. Example of the Acknowledgment Message

MSH^~\|\\^LA7V REMOTE 170^170^LA7V HOST 522^522^20130714170315-0400^^ACK~R01^170

29221^T^2.3^^^AL^^

MSA^AA^52290975

*This page intentionally left blank for double-sided printing.  
*

# Communication Requirements for HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communication requirements for HL7 interfaces are necessary to establish and maintain communications between VistA and all the participating systems. When sending or receiving a message, there are requirements that must be satisfied by VistA, by all the participating systems, and by each system.

## Using TCP/IP and HL7 Minimal Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interface between VistA and each participating system is established through a persistent or a transient (non-persistent) TCP/IP connection. Two TCP sockets provide bi-directional communications between each participating system.

Within the context of the TCP socket, each participating system connects as the client when it initiates a message. The other system connects as the server to receive messages from the *listen* state.

### Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The participating system initiates the interface by establishing a TCP Server Socket. The participating system that initiates a message connects to the participating system TCP Server Socket as a TCP Client.

### TCP/IP Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA has client (sender) and server (listener) processes for each remote system to send and receive HL7 messages. Each of these processes requires a TCP socket.

- The client process sends HL7 messages (including Application Acknowledgment messages) to the remote system and receives Accept Acknowledgment messages from the remote system.
- The server process receives HL7 messages (including Application Acknowledgment messages) from the remote system and sends Accept Acknowledgment messages to the remote system.

The diagram depicts the sequence of events for both an inbound and an outbound message regarding messages and acknowledgments.

Figure 2. TCP/IP Connections

![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-hl7-interface-specification/002.png)

### Flow Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface uses the HL7 Minimal Lower Layer Protocol (MLLP) to format messages for data interchange, including acknowledgment messages. The MLLP protocol relies on the Message Header Segment (MSH) to define encoding, routing and acknowledgment rules governing the message.

### VistA Client/Server Process Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flow of messages between VistA and the remote system can be controlled by the VistA client/server process parameters. The parameters for the client/server process are definable at each installation site and can be customized for each remote system.

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

VistA and the participating systems use automated procedures to detect when connectivity is lost and to initiate recovery procedures. Because VistA and the participating systems use the HL7 2.2 enhanced acknowledgment mode, the receiving system may respond to the message with an accept acknowledgment. When the receiving system commits the message to safe storage in a manner that releases the sending system from the need to retransmit the message, it sends a positive accept acknowledgment.

Accept acknowledgments are used for all messages and the value passed in the Accept Acknowledgment field of the MSH segment (MSH-15) of the originating message is observed. Application Acknowledg­ments are not used.

#### Requirements

1.  When VistA detects a remote end disconnect, it attempts to reconnect to the participating system TCP Server Socket for a locally defined number of retry attempts.
2.  When VistA detects a remote end disconnect and is unable to reconnect to the participating system after a locally defined number of retry attempts, it logs an error.
3.  When the participating system detects a remote end disconnect, it closes the channel of its TCP Server Socket and awaits VistA reconnection.
4.  The receiving system returns an Accept Acknowledgment with a Commit Accept (CA) status to the sending system for each incoming HL7 message in which the Message Header (MSH) segment conforms to the following criteria:
1.  The first segment is a Message Header (MSH) segment;
15. The Message Type field (MSH-9) contains a valid message type; and
16. The Message Control ID field (MSH-10) contains an ID.
5.  The receiving system returns an Accept Acknowledgment with a Commit Reject (CR) status to the sending system for each incoming HL7 message in which the Message Header (MSH) segment fails to conform to the following criteria:
1.  The first segment is a Message Header (MSH) segment.
17. The Sending Application field (MSH-3) is valid.
18. The Sending Facility field (MSH-4) is valid.
19. The Receiving Application field (MSH-5) is valid.
20. The Receiving Facility field (MSH-6) is valid.
21. The Message Type field (MSH-9) contains a valid message type.
22. The Message Control ID field (MSH-10) contains a message ID.
23. The Message Processing ID field (MSH-11) contains the appropriate value for the systems communicating.
24. The Message Version ID contains 2.2 (DoD) or 2.3 (VA or Commercial Lab).
6.  The receiving system returns an Accept Acknowledgment with a Commit Error (CE) status to the sending system for each incoming HL7 message that it did not accept, for any reasons other than those requiring a Commit Reject.
7.  Upon receipt of an Accept Acknowledgment with either a Commit Reject (CR) or Commit Error (CE) status from the receiving system, the sending system ceases transmission of the original HL7 message.