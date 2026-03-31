---
title: DG*5.3*425/951 Patient Record Flags HL7 Interface Specification
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: Patient Record Flags HL7
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*425
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 1
description: This document specifies the information needed for sharing National Patient Record Flag (PRF) assignment data between all sites that a patient visits. This data exchange will be triggered by specific events that relate to the assignment of a National PRF to a patient, the editing of an existing assi
audience: 
keywords: 
  - table
  - class
  - contents
  - message
  - style
  - even
  - width
  - patient
  - query
  - segment
page_count: 0
word_count: 7313
section_count: 20
table_count: 41
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfhl7is.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfhl7is.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

![](dg-5-3-425-951-patient-record-flags-hl7-interface-specification/001.png)

Patient Record FlagsHL7 Interface Specification

Patch DG\*5.3\*951

Patch DG\*5.3\*425

March 2019

Health Systems Design & Development (HSD&D)

Revision History

| Date | Description                                                        | Author                         |
|----------|------------------------------------------------------------------------|------------------------------------|
| 03/2019  | Updated to include Patch DG\*5.3\*951 information and formatting fixes | <span class="mark">REDACTED</span> |
| 09/2003  | Initial version for Patch DG\*5.3\*425                                 |                                    |

Table : MSH - Message Header Segment

Table of Contents

### # INTRODUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document specifies the information needed for sharing National Patient Record Flag (PRF) assignment data between all sites that a patient visits. This data exchange will be triggered by specific events that relate to the assignment of a National PRF to a patient, the editing of an existing assignment in Veterans Health Information Systems and Technology Architecture (VistA), or the registration of a new patient. The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application will use the abstract message approach and encoding rules specified by Health Level 7 (standard for electronic data exchange/messaging protocol) (HL7). HL7 is used for communicating data associated with various events that occur in health care environments.

For example, when a National PRF assignment occurs in VistA, the event will trigger an update patient information message. This message is an unsolicited transaction to all VistA sites listed for the patient in the TREATING FACILITY LIST file (#391.91).

The formats of these messages conform to the Version 2.5 HL7 Interface Standards where applicable.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sharing of National PRF assignments assumes that all VistA sites will have:

- Installed and operational VistA HL7 software;
- Patch HL\*1.6\*39 installed to provide valid TCP links for all VistA sites;
- Installed and operational Master Patient Index/Patient Demographics (MPI/PD) system;
- A currently synchronized TREATING FACILITY LIST file (#391.91).

### Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages will be limited to the information that is required to uniquely identify the patient and generate a complete PRF assignment record in the receiving site. The data transmitted will be limited to available VistA data.

### Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When National PRF assignments are created or edited, an event is generated to transmit the changes to all sites in the TREATING FACILITY LIST file (#391.91). Any changes made to the VistA database in non-standard ways, such as a direct global set by an application or by MUMPS code, will not be captured.

When a person is registered in VistA as a new patient, a query will be transmitted to the patient’s Coordinating Master of Record (CMOR) site, requesting all the patient’s existing National Patient Record Flag assignments.

### VA TCP/IP Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 V. 1.6 TCP/IP lower level protocol (LLP) will be used. Dynamic addressing via the HLL (“LINKS”) array will be used to enable the ORU~R01 Unsolicited Transmission of an Observation message to be transmitted to multiple VistA sites.

# HL7 CONTROL SEGMENTS


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [# INTRODUCTION](#introduction)
  - [General](#general)
  - [Assumptions](#assumptions)
    - [Message Content](#message-content)
    - [Data Capture and Transmission](#data-capture-and-transmission)
    - [VA TCP/IP Lower Level Protocol](#va-tcpip-lower-level-protocol)
- [HL7 CONTROL SEGMENTS](#hl7-control-segments)
  - [Message Definitions](#message-definitions)
  - [Segment Table Definitions](#segment-table-definitions)
  - [Message Control Segments](#message-control-segments)
    - [MSH - Message Header Segment](#msh-message-header-segment)
    - [MSA – Message Acknowledgment Segment](#msa-message-acknowledgment-segment)
    - [ERR – Error Segment](#err-error-segment)
    - [PID - Patient Identification Segment](#pid-patient-identification-segment)
    - [OBR – Observation Request Segment](#obr-observation-request-segment)
    - [OBX – Observation/Result Segment](#obx-observationresult-segment)
    - [QRD – Original Style Query Definition Segment](#qrd-original-style-query-definition-segment)
    - [QRF – Query Filter](#qrf-query-filter)
    - [QPD – Query Parameter Definition](#qpd-query-parameter-definition)
    - [NTE – Notes and Comments](#nte-notes-and-comments)
    - [RCP – Response Control Parameter](#rcp-response-control-parameter)
    - [QAK – Query Acknowledgement](#qak-query-acknowledgement)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions)
    - [Unsolicited Transmission of an Observation Message (R01)](#unsolicited-transmission-of-an-observation-message-r01)
    - [ORU Acknowledgment](#oru-acknowledgment)
    - [Query for Results of Observation (R02)](#query-for-results-of-observation-r02)
    - [Response to Query, Transmission of Requested Observation (R04)](#response-to-query-transmission-of-requested-observation-r04)
    - [Query by parameter requesting an RSP segment pattern response (Q11)](#query-by-parameter-requesting-an-rsp-segment-pattern-response-q11)
    - [Segment pattern response in response to QBP^Q11 (K11)](#segment-pattern-response-in-response-to-qbpq11-k11)
- [SUPPORTED AND USER-DEFINED HL7 TABLES](#supported-and-user-defined-hl7-tables)
  - [Table 0001 - Sex](#table-0001-sex)
  - [Table 0002 - Marital Status](#table-0002-marital-status)
  - [Table 0003 - Event Type Code](#table-0003-event-type-code)
  - [Table 0005 – Race](#table-0005-race)
  - [Table 0006 – Religion](#table-0006-religion)
  - [Table 0008 – Acknowledgment Code](#table-0008-acknowledgment-code)
  - [Table 0048 – What Subject Filter](#table-0048-what-subject-filter)
  - [Table 0076 - Message Type](#table-0076-message-type)
  - [Table 0091 – Query Priority](#table-0091-query-priority)
  - [Table 0106 – Query/Response Format Code](#table-0106-queryresponse-format-code)
  - [Table 0126 – Quantity Limited Request](#table-0126-quantity-limited-request)
  - [Table VA085 – Patient Record Flags](#table-va085-patient-record-flags)
  - [Table VA086 – PRF Error Codes](#table-va086-prf-error-codes)
This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the Message Control category.

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section, and the following sections, the following elements will be defined for each message:

- the trigger events;
- the message event code;
- a list of segments used in the message;
- a list of fields for each segment in the message.

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category there will be a list of HL7 standard segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL#), the element name, and the VistA description. Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings will be as specified here, unless otherwise specified in that section.

### MSH - Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Message Acknowledgment Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<blockquote>
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p><u>2 Components</u></p>
<ol type="1">
<li><p><em>Refer to Table 0076</em></p></li>
<li><p><em>Refer to Table 0003</em></p></li>
</ol></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VISTA HL7 Package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file<strong>.</strong></td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used</td>
</tr>
</tbody>
</table>

Table : Message Acknowledgment Segment

### MSA – Message Acknowledgment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                | VistA DESCRIPTION                                     |
|-----|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------|
| 1   | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | Refer to HL7 table 0008                               |
| 2   | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged. |
| 3   | 80  | ST  | O   |      |      | Text Message                | Error message text                                    |
| 4   | 15  | NM  | O   |      |      | Expected Sequence Number    | Not used                                              |
| 5   | 1   | ID  | B   |      | 0102 | Delayed Acknowledgment Type | Not used                                              |
| 6   | 100 | CE  | O   |      |      | Error Condition             | Not used                                              |

Table : Error Segment

### ERR – Error Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Patient Identification Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>80</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Error Code and Location</td>
<td><p><u>4 Components</u></p>
<p>1. Segment name</p>
<p>2. Sequence #</p>
<p>3. Field #</p>
<p>4. VA086 PRF Error Codes</p></td>
</tr>
</tbody>
</table>

Table : Patient Identification Segment

### PID - Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Observation Request Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Always set to ‘1’</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Social Security Number field of Patient file.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Integrated Control Number (ICN) field of Patient file.</p>
<p>Component 1: ICN w/checksum</p>
<p>Component 2: Checksum</p>
<p>Component 3: Null</p>
<p>Component 4: Assigning authority (subcomponent 1: ‘USVHA’, subcomponent 3: ‘L’</p>
<p>Component 5: Type ‘NI’</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>Name</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td><em>Refer to Table 0001</em></td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>County Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Language – Patient</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>Social security number and pseudo indicator.</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Driver's Lic Num – Patient</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>21</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Identifier</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>23</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Multiple Birth Indicator</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>3</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0171</td>
<td>Citizenship</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>27</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used</td>
</tr>
</tbody>
</table>

Table : Observation Request Segment

### OBR – Observation Request Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : OBX – Observation/Result Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>C</td>
<td></td>
<td></td>
<td>Set ID – OBR</td>
<td>Sequential number</td>
</tr>
<tr class="even">
<td>2</td>
<td>22</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>Placer Order Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>22</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>Filler Order Number +</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>4</td>
<td>200</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Universal Service ID</td>
<td><p><u>3 components:</u></p>
<p>1. Patient Record Flag IEN</p>
<p>2. Name</p>
<p>3. PRF table – VA085</p>
<p>Based on field.02/file 26.13</p>
<p>Example: 1~Behavioral~VA085</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>ID</td>
<td>X</td>
<td></td>
<td></td>
<td>Priority</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td></td>
<td></td>
<td>Requested Date/time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>Observation Date/Time #</td>
<td>Date/Time field .02/file 26.14</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Observation End Date/Time #</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>CQ</td>
<td></td>
<td></td>
<td></td>
<td>Collection Volume *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>60</td>
<td>XCN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Collector Identifier *</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0065</td>
<td>Specimen Action Code *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Danger Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>300</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Relevant Clinical Info.</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>Specimen Received Date/Time *</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>300</td>
<td>CM</td>
<td></td>
<td></td>
<td>0070</td>
<td>Specimen Source *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>XCN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Ordering Provider</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>40</td>
<td>XTN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Order Callback Phone Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Placer field 1</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Placer field 2</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>20</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Filler Field 1 +</td>
<td>Owner Site field .04/file 26.13</td>
</tr>
<tr class="odd">
<td>21</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Filler Field 2 +</td>
<td>Originating Site field .05/file 26.13 (Note: Used in ORF messages only.)</td>
</tr>
<tr class="even">
<td>22</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>Results Rpt/Status Chng - Date/Time +</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>23</td>
<td>40</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Charge to Practice +</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>10</td>
<td>ID</td>
<td></td>
<td></td>
<td>0074</td>
<td>Diagnostic Serv Sect ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>0123</td>
<td>Result Status +</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>400</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Parent Result +</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>27</td>
<td>200</td>
<td>TQ</td>
<td></td>
<td>Y</td>
<td></td>
<td>Quantity/Timing</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>28</td>
<td>150</td>
<td>XCN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Result Copies To</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>29</td>
<td>150</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Parent *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>30</td>
<td>20</td>
<td>ID</td>
<td></td>
<td></td>
<td>0124</td>
<td>Transportation Mode</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>31</td>
<td>300</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td></td>
<td>Reason for Study</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>32</td>
<td>200</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Principal Result Interpreter +</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>33</td>
<td>200</td>
<td>CM</td>
<td></td>
<td>Y</td>
<td></td>
<td>Assistant Result Interpreter +</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>34</td>
<td>200</td>
<td>CM</td>
<td></td>
<td>Y</td>
<td></td>
<td>Technician +</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>35</td>
<td>200</td>
<td>CM</td>
<td></td>
<td>Y</td>
<td></td>
<td>Transcriptionist +</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>36</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Scheduled Date/Time +</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>37</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Number of Sample Containers *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>38</td>
<td>60</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td></td>
<td>Transport Logistics of Collected Sample *</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>39</td>
<td>200</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td></td>
<td>Collector's Comment *</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>40</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Transport Arrangement Responsibility</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>41</td>
<td>30</td>
<td>ID</td>
<td></td>
<td></td>
<td>0224</td>
<td>Transport Arranged</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0225</td>
<td>Escort Required</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>43</td>
<td>200</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td></td>
<td>Planned Patient Transport Comment</td>
<td>Not used</td>
</tr>
</tbody>
</table>

Table : OBX – Observation/Result Segment

### OBX – Observation/Result Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : QRD – Original Style Query Definition Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>10</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID – OBX</td>
<td>Sequential number</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0125</td>
<td>Value Type</td>
<td><p>Always ‘ST’ for Status ID.</p>
<p>Always ‘TX’ for Narrative, Comment, and DBRS ID’s</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>590</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Observation Identifier</td>
<td><p>“S~Status~L” or “N~Narrative~L” or “C~Comment~L” or</p>
<p>"D~DBRS-Update~L" or</p>
<p>"D~DBRS-Delete~L"</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Observation Sub-ID</td>
<td>Sequential number when OBX.3 is “S” or “C”. Used to separate multiple assignment history entries.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td>*</td>
<td></td>
<td>Y</td>
<td></td>
<td>Observation Value</td>
<td><p>ACTION field .03/file 26.14 or Assignment Narrative field 1/file 26.13 or History Comments field 1/file 26.14 or, in case of OBX.3 containing either "D~DBRS-Update~L" or "D~DBRS-Delete~L” first repetition contains value from last history entry in file 26.14, sub-file 26.142, field .01 (DBRS #) and</p>
<p>second repetition contains value</p>
<p>from last history entry in file</p>
<p>26.14, sub-file 26.142, field .02</p>
<p>(DBRS OTHER).</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>References Range</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>5</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0078</td>
<td>Abnormal Flags</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>5</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Probability</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0080</td>
<td>Nature of Abnormal Test</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0085</td>
<td>Observ Result Status</td>
<td>Always ‘F’inal</td>
</tr>
<tr class="even">
<td>12</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date Last Obs Normal Values</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>User Defined Access Checks</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time of the Observation</td>
<td>Date/Time field .02/file 26.14 or from field .03, sub-file 26.142, file 26.14 in case of OBX.3.2 = "DBRS-Update" / "DBRS-Delete"</td>
</tr>
<tr class="odd">
<td>15</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Producer's ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>XCN</td>
<td></td>
<td></td>
<td></td>
<td>Responsible Observer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>60</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td></td>
<td>Observation Method</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>23</td>
<td>683</td>
<td>XON</td>
<td>O</td>
<td>N</td>
<td></td>
<td>Performing Organization Name</td>
<td>If OBX.3 = "C~Comment~L", component 3 of this field (OBX.23.3) contains station number from file 26.14, field .09</td>
</tr>
</tbody>
</table>

Table : QRD – Original Style Query Definition Segment

### QRD – Original Style Query Definition Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Query Filter</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Query Date/Time</td>
<td>Current Date/Time</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0106</td>
<td>Query Format Code</td>
<td>Always ‘R’ecord</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0091</td>
<td>Query Priority</td>
<td>Always ‘I’mmediate</td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Query ID</td>
<td>DFN (ex. ‘7171694’)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0107</td>
<td>Deferred Response Type</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Deferred Response Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>CQ</td>
<td>R</td>
<td></td>
<td>0126</td>
<td>Quantity Limited Request</td>
<td>10~‘RD’ records</td>
</tr>
<tr class="even">
<td>8</td>
<td>60</td>
<td>XCN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Who Subject Filter</td>
<td><p>Integrated Control Number</p>
<p><u>2 Components:</u></p>
<p>1. ICN field 991.01/file 2</p>
<p>9. Assigning authority (‘USVHA&amp;&amp;L’)</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>60</td>
<td>CE</td>
<td>R</td>
<td>Y</td>
<td>0048</td>
<td>What Subject Filter</td>
<td>Always ‘OTH~Other~HL0048’</td>
</tr>
<tr class="even">
<td>10</td>
<td>60</td>
<td>CE</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>What Department Data Code</td>
<td>Always ‘PRFA~Patient Record Flags~L’</td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>What Data Code Value Qual.</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0108</td>
<td>Query Results Level</td>
<td>Not used</td>
</tr>
</tbody>
</table>

Table : Query Filter

### QRF – Query Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                     | VistA DESCRIPTION                       |
|-----|-----|-----|-----|------|------|----------------------------------|-----------------------------------------|
| 1   | 20  | ST  | R   | Y    |      | Where Subject Filter             | Always ‘PRF’                            |
| 2   | 26  | TS  | O   |      |      | When Data Start Date/Time        | Not used                                |
| 3   | 26  | TS  | O   |      |      | When Data End Date/Time          | Not used                                |
| 4   | 60  | ST  | O   | Y    |      | What User Qualifier              | Social Security Number field .09/file 2 |
| 5   | 60  | ST  | O   | Y    |      | Other QRY Subject Filter         | Date of Birth field .03/file 2          |
| 6   | 12  | ID  | O   | Y    | 0156 | Which Date/Time Qualifier        | Not used                                |
| 7   | 12  | ID  | O   | Y    | 0157 | Which Date/Time Status Qualifier | Not used                                |
| 8   | 12  | ID  | O   | Y    | 0158 | Date/Time Selection Qualifier    | Not used                                |
| 9   | 60  | TQ  | O   |      |      | When Quantity/Timing Qualifier   | Not used                                |

Table : Query Parameter Definition

### QPD – Query Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Notes and Comments</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>250</td>
<td>CWE</td>
<td>R</td>
<td></td>
<td>0471</td>
<td>Message Query Name</td>
<td></td>
</tr>
<tr class="even">
<td>1-1</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Identifier</td>
<td>“PRFREQ01”</td>
</tr>
<tr class="odd">
<td>1-2</td>
<td>40</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Text</td>
<td>“PRF Ownership Transfer Request”</td>
</tr>
<tr class="even">
<td>2</td>
<td>32</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>Query Tag</td>
<td>Query ID – sequential query number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>30</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>User Parameter 1</td>
<td>Patient’s ICN</td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>User Parameter 2</td>
<td>PRF flag name from field 26.15/.01</td>
</tr>
<tr class="odd">
<td>5</td>
<td>50</td>
<td>XPN</td>
<td>R</td>
<td></td>
<td></td>
<td>User Parameter 3</td>
<td><p>Approver’s name from field 200/.01</p>
<p><strong>This field is used in RSP^K11 message only, it’s blank in QBP^Q11 message</strong></p></td>
</tr>
<tr class="even">
<td>6</td>
<td>24</td>
<td>DTM</td>
<td>R</td>
<td></td>
<td></td>
<td>User Parameter 4</td>
<td><p>Approval/denial time stamp</p>
<p><strong>This field is used in RSP^K11 message only, it’s blank in QBP^Q11 message</strong></p></td>
</tr>
</tbody>
</table>

Table : Notes and Comments

### NTE – Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Response Control Parameter</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID – NTE</td>
<td>“1”</td>
</tr>
<tr class="even">
<td>3</td>
<td>80</td>
<td>FT</td>
<td>O</td>
<td>1</td>
<td></td>
<td>Comment</td>
<td>“A” for approval or “D” for denial in RSP^K11 message. Request reason in QBP^Q11 message</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>FT</td>
<td>O</td>
<td>2</td>
<td></td>
<td>Comment</td>
<td><p>Response reason in RSP^K11 message.</p>
<p><strong>This field is used in RSP^K11 message only, it’s blank in QBP^Q11 message</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>CWE</td>
<td>O</td>
<td></td>
<td></td>
<td>Comment Type</td>
<td>“RE”</td>
</tr>
<tr class="odd">
<td>5</td>
<td>50</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Entered by</td>
<td><p><strong>In QBP^Q11 message:</strong></p>
<p>Requester’s name from field 200/.01</p>
<p><strong>In RSP^K11 message:</strong></p>
<p>Approver’s name from field 200/.01</p></td>
</tr>
<tr class="even">
<td>5.14</td>
<td>8</td>
<td>HD</td>
<td>R</td>
<td></td>
<td></td>
<td>Assigning Facility</td>
<td></td>
</tr>
<tr class="odd">
<td>5.14.2</td>
<td>7</td>
<td>FT</td>
<td>R</td>
<td></td>
<td></td>
<td>Universal ID</td>
<td>Station # of facility or division.</td>
</tr>
<tr class="even">
<td>6</td>
<td>24</td>
<td>DTM</td>
<td>O</td>
<td></td>
<td></td>
<td>Entered Date/Time</td>
<td><p><strong>In QBP^Q11 message:</strong></p>
<p>Request timestamp</p>
<p><strong>In RSP^K11 message:</strong></p>
<p>Approval/denial timestamp</p></td>
</tr>
</tbody>
</table>

Table : Response Control Parameter

### RCP – Response Control Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ   | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME             | VistA DESCRIPTION |
|-------|-----|-----|-----|------|------|--------------------------|-------------------|
| 1     | 1   | ID  | O   |      | 0091 | Query Priority           | “D” (deferred)    |
| 2     | 10  | CQ  | O   |      | 0126 | Quantity Limited Request |                   |
| 2-1   | 1   | NM  | O   |      |      | Quantity                 | “1”               |
| 2-2   |     | CWE | O   |      |      | Units                    |                   |
| 2-2-1 | 2   | ST  | O   |      |      | Identifier               | “LI”              |
| 3     | 250 | CNE | O   |      | 0394 | Response Modality        |                   |
| 3-1   | 1   | ST  | O   |      |      | Identifier               | “T”               |

Table : Query Acknowledgement

### QAK – Query Acknowledgement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME          | VistA DESCRIPTION                                                |
|-----|-----|-----|-----|------|------|-----------------------|------------------------------------------------------------------|
| 1   | 32  | ST  | C   |      |      | Query Tag             | Query ID – sequential query number                               |
| 2   | 2   | ID  | O   |      | 0208 | Query Response Status | “OK” if patient + PRF flag combo has been found, “AR” otherwise. |
| 3   | 250 | CE  | R   |      | 0471 | Message Query Name    |                                                                  |
| 3-1 | 20  | ST  | R   |      |      | Identifier            | “PRFREQ01”                                                       |
| 3-2 | 50  | ST  | R   |      |      | Text                  | “PRF Ownership Transfer Request”                                 |

Table : Observational Report Message

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below, along with the applicable form of the message to be exchanged. The notation used to describe the sequence, option, and repetition of segments is described in the HL7 V. 2.3 *Standard Specification Manual*, Chapter 2, and in summary form, in Section 2.1 of this document.

### Unsolicited Transmission of an Observation Message (R01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Category I PRF assignment and assignment edit events will trigger an R01 message (Table 13) to be sent to each site listed for the patient in the TREATING FACILITY LIST file (#391.91) under the following circumstances:

- when a PRF is initially assigned to a patient;
- when an existing PRF assignment is edited.

|         |                                  |             |
|---------|----------------------------------|-------------|
| ORU | Observational Report Message | Section |
| MSH     | Message Header                   | 2.3.1       |
| PID     | Patient Identification           | 2.3.4       |
| OBR     | Observation Request              | 2.3.5       |
| {OBX}   | Observation/Result               | 2.3.6       |

Table : Received Acknowledgement

*Sample Message*

MSH^~\|\\^PRF-SEND^500~DEVVPP.FO-XXXXX.MED.VA.GOV~DNS^PRF-RECV^500~FO-XXXXX.MED.VA.GOV~DNS^20030314133623-0500^^ORU~R01^50044^T^2.3^^^NE^AL^US

PID^1^999-99-9999\~~^1009999999V735077~735077\~~USVHA&&L~NI^9873^DOE~JOHN^SMITH,^19500404^M^^7^1 ROAD~RD 2~ANYTOWN~NY~33333^083^(555)555-5556^(555)555-5545^^S^0^^999999999

OBR^1^^^1~BEHAVIORAL~VA085^^^20030310111346-0500^^^^^^^^^^^^^1

OBX^1^TX^N~Narrative~L^^Description: This record flag was assigned to Mr. Doe because on^^^^^^F^^^20030311140002-0500

OBX^2^TX^N~Narrative~L^^March 1, 2003, he threatened a registration clerk with a weapon.^^^^^^F^^^20030311140002-0500

OBX^3^TX^N~Narrative~L^^\|On March 10, 2003, the patient exhibited hostile behavior towards the^^^^^^F^^^20030311140002-0500

OBX^4^TX^N~Narrative~L^^Enrollment supervisor. The flag is being re-activated^^^^^^F^^^20030311140002-0500

OBX^5^TX^N~Narrative~L^^\|Recommendation: Contact VA Police when the patient is on VA premises.^^^^^^F^^^20030311140002-0500

OBX^6^TX^N~Narrative~L^^\|Further comments:^^^^^^F^^^20030311140002-0500

OBX^7^ST^S~Status~L^^NEW ASSIGNMENT^^^^^^F^^^20030311140002-0500

OBX^8^TX^C~Comment~L^^New record flag assignment.^^^^^^F^^^20030311140002-0500

### ORU Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site receiving an Unsolicited Transmission of an Observation Message will return an application Acknowledgment message (Table 14) to the sending site after completion of processing.

|         |                        |             |
|---------|------------------------|-------------|
| ACK | Acknowledgment     | Section |
| MSH     | Message Header         | 2.3.1       |
| MSA     | Message Acknowledgment | 2.3.2       |
| \[ERR\] | Error                  | 2.3.3       |

Table : Query Message that Patient is Registered

*Sample Messages*

General Acknowledgment (ACK) message for a successful Unsolicited Transmission of an Observation Message (ORU~R01) (Figure 1).

Figure : Unsolicited Transmission Acknowledgement

MSH^~\|\\^PRF-RECV^500~FO-XXXXX.MED.VA.GOV~DNS^PRF-SEND^500~DEVVPP.FO-XXXXX.MED.VA.GOV~DNS^20030314133631-0400^^ACK~R01^50018490^T^2.3^^^NE^NE^US

MSA^AA^50044

A General Acknowledgment (ACK) message is displayed for a failed Unsolicited Transmission of an Observation Message (ORU~R01) (Figure 2.) This indicates that the transmitting site is not the owner of the Patient Record Flag assignment.

Figure : Unsolicited Transmission Observation Message- No Owner of Patient Record Flag

MSH^~\|\\^PRF-RECV^500~FO-XXXXX.MED.VA.GOV~DNS^PRF-SEND^500~DEVVPP.FO-XXXXX.MED.VA.GOV~DNS^20030314133631-0400^^ACK~R01^50018490^T^2.3^^^NE^NE^US

MSA^AE^50044^^^^UU~Unauthorized Update~VA086

General Acknowledgment (ACK) message for a failed Unsolicited Transmission of an Observation Message (ORU~R01) indicating that no patient was found with the corresponding identifiers (Figure 3).

Figure : Unsolicited Transmission Observation Message- No Patient Found with Corresponding Identifiers

MSH^~\|\\^PRF-RECV^500~FO-XXXXX.MED.VA.GOV~DNS^PRF-SEND^500~DEVVPP.FO-XXXXX.MED.VA.GOV~DNS^20030314133631-0400^^ACK~R01^50018490^T^2.3^^^NE^NE^US

MSA^AE^50044

ERR^PID~1~3~NM&No Match&VA086

### Query for Results of Observation (R02)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Register a Patient \[DG REGISTER PATIENT\], Load/Edit Patient Data \[DG LOAD PATIENT DATA\], and 10-10T Registration \[DGRPT 10-10T REGISTRATION\] options will trigger a Query message to be sent to the patient’s CMOR site when a new patient is registered and the MPI/PD system has successfully returned a national ICN (Table 17).

|         |                  |             |
|---------|------------------|-------------|
| QRY | Query        | Section |
| MSH     | Message Header   | 2.3.1       |
| QRD     | Query Definition | 2.3.7       |
| QRF     | Query Filter     | 2.3.8       |

Table : Observational Report

*Sample Message*

Figure : Query Message that Patient is Registered

MSH^~\|\\^PRF-QRY^500^PRF-QRYRESP^500^20030502094251-0500^^QRY~R02^500160^T^2.3^^^^^US

QRD^20030502111910-0500^R^I^21^^^10~RD^1001178082V735077\~\~\~\~\~\~\~~USVHA&&L^OTH~Other~HL0048^PRFA~Patient Record Flag Assignments~L

QRF^PRF^^^283769873^19500404

### Response to Query, Transmission of Requested Observation (R04)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CMOR site receiving a query will respond with all active and inactive Category I PRF assignments for the patient and associated assignment history data (Table 16).

|         |                          |             |
|---------|--------------------------|-------------|
| ORF | Observational Report | Section |
| MSH     | Message Header           | 2.3.1       |
| MSA     | Message Acknowledgment   | 2.3.2       |
| \[ERR\] | Error                    | 2.3.3       |
| QRD     | Query Definition         | 2.3.7       |
| {OBR    | Observation Request      | 2.3.5       |
| {OBX}}  | Observation/Result       | 2.3.6       |

Table : Message sent to Current Owner of PRF Flag in Question

*Sample Message*

Figure : Category 1 Patient Record Flag Assignments- Patient & History

MSH^~\|\\^PRF-QRYRESP^500^PRF-QRY^500^200305020943-0400^^ORF~R04^50018644^T^2.3^^^^^US

MSA^AA^500162

QRD^20030502112018-0400^R^I^21^^^10~RD^1001178082\~\~\~\~\~\~\~~USVHA&&L^OTH~Other~HL0048^PRFA~Patient Record Flag Assignments~L

OBR^1^^^1~BEHAVIORAL~VA085^^^20030502094037-0400^^^^^^^^^^^^^500^500

OBX^1^TX^N~Narrative~L^^Working on the HL7 Query testing.(rbs)^^^^^^F^^^20030502103408-0400

OBX^2^TX^N~Narrative~L^^\|Description: Mr. McGillicudy verbally abused and threatened a^^^^^^F^^^20030502103408-0400

OBX^3^TX^N~Narrative~L^^registration clerk on 5/1/2003.^^^^^^F^^^20030502103408-0400

OBX^4^TX^N~Narrative~L^^\|Recommendation: Contact VHA security when Mr. McGillicuddy presents^^^^^^F^^^20030502103408-0400

OBX^5^TX^N~Narrative~L^^himself on the VAMC premises.^^^^^^F^^^20030502103408-0400

OBX^6^ST^S~Status~L^^NEW ASSIGNMENT^^^^^^F^^^20030502094037-0400

OBX^7^TX^C~Comment~L^^New record flag assignment.^^^^^^F^^^20030502094037-0400

OBX^8^ST^S~Status~L^^CONTINUE^^^^^^F^^^20030502103408-0400

OBX^9^TX^C~Comment~L^^Testing the HL7 query from VPP to FEX.(rbs)^^^^^^F^^^20030502103408-0400

### Query by parameter requesting an RSP segment pattern response (Q11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CMOR site requesting transfer of Category I PRF flag ownership will send this message to the current owner of PRF flag in question (Table 17).

|         |                            |             |
|---------|----------------------------|-------------|
| QBP | Query                  | Section |
| MSH     | Message Header             | 2.3.1       |
| QPD     | Query Parameter Definition | 2.3.9       |
| NTE     | Notes and Comments         | 2.3.10      |
| RCP     | Response Control Parameter | 2.3.11      |

Table : CMOR Response

### Segment pattern response in response to QBP^Q11 (K11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CMOR site receiving transfer request for Category I PRF flag ownership (QBP^Q11) will respond with either approval or denial of the request (Table 18).

|         |                              |             |
|---------|------------------------------|-------------|
| RSP | Segment Pattern response | Section |
| MSH     | Message Header               | 2.3.1       |
| MSA     | Message Acknowledgment       | 2.3.2       |
| QAK     | Query Acknowledgement        | 2.3.12      |
| QPD     | Query Parameter Definition   | 2.3.9       |
| NTE     | Notes and Comments           | 2.3.10      |

Table : Table 0001 - Sex

# SUPPORTED AND USER-DEFINED HL7 TABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table 0001 - Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| F     | FEMALE      |
| M     | MALE        |
| O     | OTHER       |
| U     | UNKNOWN     |

Table : Table 0002 - Marital Status

## Table 0002 - Marital Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| A     | SEPARATED   |
| D     | DIVORCED    |
| M     | MARRIED     |
| S     | SINGLE      |
| W     | WIDOWED     |

Table : Table 0003 - Event Type Code

## Table 0003 - Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                 |
|-------|-----------------------------------------------------------------|
| VALUE | DESCRIPTION                                                     |
| R01   | ORU/ACK - Unsolicited transmission of an observation message.   |
| R02   | QRY – Query for results of observation.                         |
| R04   | ORF – Response to query; transmission of requested observation. |

Table : Table 0005 - Race

## Table 0005 – Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                  |
|-------|----------------------------------|
| VALUE | DESCRIPTION                      |
| 1     | HISPANIC, WHITE                  |
| 2     | HISPANIC, BLACK                  |
| 3     | AMERICAN INDIAN OR ALASKA NATIVE |
| 4     | BLACK, NOT OF HISPANIC ORIGIN    |
| 5     | ASIAN OR PACIFIC ISLANDER        |
| 6     | WHITE, NOT OF HISPANIC ORIGIN    |
| 7     | UNKNOWN                          |

Table : Table 0006 -– Religion

## Table 0006 – Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                             |
|-------|-----------------------------|
| VALUE | DESCRIPTION                 |
| 0     | CATHOLIC                    |
| 1     | JEWISH                      |
| 2     | EASTERN ORTHODOX            |
| 3     | BAPTIST                     |
| 4     | METHODIST                   |
| 5     | LUTHERAN                    |
| 6     | PRESBYTERIAN                |
| 7     | UNITED CHURCH OF CHRIST     |
| 8     | EPISCOPALIAN                |
| 9     | ADVENTIST                   |
| 10    | ASSEMBLY OF GOD             |
| 11    | BRETHREN                    |
| 12    | CHRISTIAN SCIENTIST         |
| 13    | CHURCH OF CHRIST            |
| 14    | CHURCH OF GOD               |
| 15    | DISCIPLES OF CHRIST         |
| 16    | EVANGELICAL COVENANT        |
| 17    | FRIENDS                     |
| 18    | JEHOVAH"S WITNESS           |
| 19    | LATTER-DAY SAINTS           |
| 20    | ISLAM                       |
| 21    | NAZARENE                    |
| 22    | OTHER                       |
| 23    | PENTECOSTAL                 |
| 24    | PROTESTANT, OTHER           |
| 25    | PROTESTANT, NO DENOMINATION |
| 26    | REFORMED                    |
| 27    | SALVATION ARMY              |
| 28    | UNITARIAN; UNIVERSALIST     |
| 29    | UNKNOWN/NO PREFERENCE       |
| 30    | NATIVE AMERICAN             |
| 31    | BUDDHIST                    |

Table : Table 0008 – Acknowledgment Code

## Table 0008 – Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table : Table 0048 – What Subject Filter</p></caption>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>DESCRIPTION</td>
</tr>
<tr class="even">
<td>AA</td>
<td>Original mode: Application Accept<br />
Enhanced mode: Application acknowledgment: Accept</td>
</tr>
<tr class="odd">
<td>AE</td>
<td>Original mode: Application Error<br />
Enhanced mode: Application acknowledgment: Error</td>
</tr>
<tr class="even">
<td>AR</td>
<td>Original mode: Application Reject<br />
Enhanced mode: Application acknowledgment: Reject</td>
</tr>
<tr class="odd">
<td>CA</td>
<td>Enhanced mode: Accept acknowledgment: Commit Accept</td>
</tr>
<tr class="even">
<td>CE</td>
<td>Enhanced mode: Accept acknowledgment: Commit Error</td>
</tr>
<tr class="odd">
<td>CR</td>
<td>Enhanced mode: Accept acknowledgment: Commit Reject</td>
</tr>
</tbody>
</table>

Table : Table 0048 – What Subject Filter

## Table 0048 – What Subject Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                                     |
|-------|-------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                         |
| ADV   | Advice/Diagnosis                                                                    |
| ANU   | Nursing unit lookup (returns patients in beds, excluding empty beds)                |
| APN   | Patient name lookup                                                                 |
| APP   | Physician lookup                                                                    |
| ARN   | Nursing unit lookup (returns patients in beds, including empty beds)                |
| APM   | Medical record number query, returns visits for a medical record number             |
| APA   | Account number query, return matching visit                                         |
| CAN   | Cancel. Used to cancel a query                                                      |
| DEM   | Demographics                                                                        |
| FIN   | Financial                                                                           |
| GOL   | Goals                                                                               |
| MRI   | Most recent inpatient                                                               |
| MRO   | Most recent outpatient                                                              |
| NCK   | Network clock                                                                       |
| NSC   | Network status change                                                               |
| NST   | Network statistic                                                                   |
| ORD   | Order                                                                               |
| OTH   | Other                                                                               |
| PRB   | Problems                                                                            |
| PRO   | Procedure                                                                           |
| RES   | Result                                                                              |
| RAR   | Pharmacy administration information                                                 |
| RER   | Pharmacy encoded order information                                                  |
| RDR   | Pharmacy dispense information                                                       |
| RGR   | Pharmacy give information                                                           |
| ROR   | Pharmacy prescription information                                                   |
| SAL   | All schedule related information, including open slots, booked slots, blocked slots |
| SBK   | Booked slots on the identified schedule                                             |
| SBL   | Blocked slots on the identified schedule                                            |
| SOP   | Open slots on the identified schedule                                               |
| SSA   | Time slots available for a single appointment                                       |
| SSR   | Time slots available for a recurring appointment                                    |
| STA   | Status                                                                              |
| VXI   | Vaccine Information                                                                 |

Table : Table 0076 - Message Type

## Table 0076 - Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                    |
|-------|------------------------------------|
| VALUE | DESCRIPTION                        |
| ACK   | GENERAL ACKNOWLEDGMENT MESSAGE     |
| ORU   | OBSERVATION RESULT/UNSOLICITED     |
| ORF   | OBSERVATION RESULT/RECORD RESPONSE |
| QRY   | QUERY, ORIGINAL MODE               |

Table : Table 0091 – Query Priority

## Table 0091 – Query Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| D     | Deferred    |
| I     | Immediate   |

Table : Table 0106 – Query/Response Format Code

## Table 0106 – Query/Response Format Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                               |
|-------|-------------------------------|
| VALUE | DESCRIPTION                   |
| D     | Response is in Display format |
| R     | Response is in Record format  |
| T     | Response is in Tabular format |

Table : Table 0126 – Quantity Limited Request

## Table 0126 – Quantity Limited Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                 |
|-------|-----------------|
| VALUE | DESCRIPTION     |
| CH    | Characters      |
| LI    | Lines           |
| PG    | Pages           |
| RD    | Records         |
| ZO    | Locally Defined |

Table : Table VA085 – Patient Record Flags

## Table VA085 – Patient Record Flags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 30 will reference the IEN of the PRF NATIONAL FLAG file (#26.15) and the Flag Name.

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| 1     | Behavioral  |

Table : Table VA086 – PRF Error Codes

## Table VA086 – PRF Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 31 will contain the application acknowledgment error codes.

|       |                                                                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                                                                                                                                 |
| FE    | Filer error – an error occurred at the remote site when attempting to add or update an assignment                                                                                           |
| IF    | Invalid Patient Record Flag – flag does not exist in receiving site’s PRF National Flag file                                                                                                |
| IID   | Invalid Observation ID – transmitted observation ID is not “N”arrative, “S”tatus or “C”omment                                                                                               |
| IOR   | Invalid Originating Site – originating site does not exist in receiving site’s Institution file                                                                                             |
| IOW   | Invalid Owner Site – owner site does not exist in receiving site’s Institution file                                                                                                         |
| NM    | No Match – transmitted ICN, DOB and SSN do not match the ICN, DOB and SSN at receiving site                                                                                                 |
| UU    | Unauthorized Update – originating site does not match the owner site in the receiving site’s assignment record or an invalid action was transmitted (i.e., reactivate an active assignment) |