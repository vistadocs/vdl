---
title: RA*5*78 HL7 Interface Spec for Voice Recognition
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: HL7 Interface Spec for Voice Recognition
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: active
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*78
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: Radiology/Nuclear Medicine V. 5 Health Level 7 (HL7) Interface Specifications for Voice Recognition Dictation Systems
audience: 
keywords: 
  - message
  - table
  - contents
  - segment
  - definition
  - report
  - order
  - time
  - class
  - observation
page_count: 0
word_count: 7374
section_count: 11
table_count: 28
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: December 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0hl7is_vr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0hl7is_vr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=98"
---

![](ra-5-78-hl7-interface-spec-for-voice-recognition/001.png)

Radiology/Nuclear Medicine V. 5  
Health Level 7 (HL7) Interface Specifications  
for Voice Recognition Dictation Systems

December 1999

Revised for  
Patch \*5.0\*144  
March 2018

Office of Chief Information Officer

Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 62%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Page</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>December 1999</td>
<td>1.0</td>
<td>Initial version of this document</td>
<td></td>
</tr>
<tr class="even">
<td>July 2000</td>
<td>1.0</td>
<td><p>Note pertaining to OBX attributes, length of observation value field</p>
<p>Note pertaining to OBX attributes, multipart, single answer results</p>
<p>Patch RA*5*17 Radiology HL7 interfaces for the new VistA HL7 standards (post HL*1.6*57)</p></td>
<td><p><a href="#_Ref221329019">23</a></p>
<p><a href="#_Ref221329036">23</a></p>
<p><a href="#_Ref221328830">24</a></p></td>
</tr>
<tr class="odd">
<td>May 2009</td>
<td>2.0</td>
<td><p>Patch RA*5.0*78 (HL7 V2.3 messaging standards)<br />
Added information about query response</p>
<ul>
<li><p>Added a new segment field for ORU messages: QRD</p></li>
<li><p>Added a new segment field for ORU messages: QRF</p></li>
<li><p>Added a new segment field for ACK messages: DSC</p></li>
<li><p>Added an example of QRY~R02/ Accession number specification</p></li>
<li><p>Added an example of QRY~R02­/ Patient, date/time, and # of reports</p></li>
<li><p>Added an example of QRF~R04 –­ Radiology response to query</p></li>
</ul></td>
<td><p>25</p>
<p>26</p>
<p>27</p>
<p>33</p>
<p>33</p>
<p>33</p></td>
</tr>
<tr class="even">
<td>March 2018</td>
<td>3.0</td>
<td><p>RA*5.0*144 Removes HLO Query logic</p>
<ul>
<li><blockquote>
<p>Remove all references to QRY messages from patch 78</p>
</blockquote></li>
<li><blockquote>
<p>Add ‘VAQ’ observation result status</p>
</blockquote></li>
</ul></td>
<td><p>25,26,27,33</p>
<p>21,25</p></td>
</tr>
</tbody>
</table>

Table of Contents

Introduction

This document describes a bi-directional interface to the Radiology/Nuclear Medicine v5.0 package based upon HL7 V2.3 messaging standards. The COTS voice recognition systems currently interfaced to VISTA Radiology/Nuclear Medicine v5.0 are IBM MedSpeak, PowerScribe for Radiology, and TalkStation. Future interfaces to application, other than the aforementioned, should follow these specifications for compliance to the existing interface design.

# General Specifications


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Specifications](#general-specifications)
  - [Communication Protocol](#communication-protocol)
  - [Application Processing Rules](#application-processing-rules)
  - [Hl7 Concepts and Definitions](#hl7-concepts-and-definitions)
    - [Messages](#messages)
    - [Segments](#segments)
    - [Fields](#fields)
    - [Position (sequence within the segment)](#position-sequence-within-the-segment)
    - [Maximum Length](#maximum-length)
    - [Data Types](#data-types)
    - [Optionality](#optionality)
    - [Repetition](#repetition)
    - [Message Delimiters](#message-delimiters)
  - [## Data Types](#data-types-1)
  - [## Use of Escape Sequences in Text Fields](#use-of-escape-sequences-in-text-fields)
  - [Specification Conventions](#specification-conventions)
    - [Segment Tables Definitions](#segment-tables-definitions)
- [# HL7 Messages](#hl7-messages)
  - [HL7 Message Definitions](#hl7-message-definitions)
    - [ORM - General Order Message (Event type O01)](#orm-general-order-message-event-type-o01)
    - [ORU – Unsolicited transmission of an observation (Event type R01)](#oru-unsolicited-transmission-of-an-observation-event-type-r01)
    - [## HL7 Segment Definitions and Specifics](#hl7-segment-definitions-and-specifics)
    - [MSH Attributes](#msh-attributes)
    - [PID Attributes](#pid-attributes)
    - [ORC Attributes](#orc-attributes)
    - [OBR Attributes](#obr-attributes)
    - [OBX Attributes](#obx-attributes)
    - [MSA Attributes](#msa-attributes)
- [Transactions Specifications](#transactions-specifications)
  - [General](#general)
  - [Specific Transactions](#specific-transactions)
    - [Registration](#registration)
    - [Examined/Images Collected](#examinedimages-collected)
    - [Cancellation/Deletion](#cancellationdeletion)
    - [Verified/Released Unverified Report](#verifiedreleased-unverified-report)
  - [Messaging Specifics](#messaging-specifics)
    - [ORM Message](#orm-message)
    - [ORU Message](#oru-message)
    - [ACK Message](#ack-message)
- [# # # # # # Appendix – CPT Modifiers (RA\5\10)[^4]](#appendix-cpt-modifiers-ra5104)

## Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) Model. This is the application level. Levels one through six involve primarily communication protocols. With the implementation of patch HL\*1.6\*19, the VISTA HL7 package can now support TCP/IP interfaces. The TCP/IP network standard will be used to support the Transport layer and Network layer of the interface. The Minimal Lower Layer Protocol (MLLP) as specified in the HL7 V2.3 Implementation Guide Appendix C.4 will be used to support the Presentation layer protocol for the interface and will encapsulate the HL7 V2.3 messages with start and end markers. Two links will be required for message transactions. VISTA will send order messages and receive acknowledgments over one link and the other link will send results and receive acknowledgements.

## Application Processing Rules 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol will not be repeated here.

## Hl7 Concepts and Definitions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example the ADT Message type is used to transmit portions of a patient’s Patient Administration (ADT) data from one system to another. A three character code contained within each message identifies its type.

The real-world event that initiates an exchange of messages is called a trigger event. See section 2.2.1 “Trigger Events” of the HL7 2.3 Standard Specifications for more a detailed description of trigger events. These codes represent values such as A patient is admitted or An order event occurred. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.

### Segments 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of {xe "Data Fields"}data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is given a name. For example, the ADT message may contain the following segments: Message Header (MSH), Event Type (EVN), Patient ID (PID), and Patient Visit (PV1).Each segment is identified by a unique three-character code known as the Segment ID.

### Fields 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. HL7 does not care how systems actually store data within an application. When fields are transmitted, they are sent as character strings. Except where noted, HL7 data fields may take on the null value. Sending the null value, which is transmitted as two double quote marks (“”), is different from omitting an optional data field. The difference appears when the contents of a message will be used to update a record in a database rather than create a new one. If no value is sent, (i.e., it is omitted) the old value should remain unchanged. If the null value is sent, the old value should be changed to null.

### Position (sequence within the segment) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table. In the segment attribute tables this information is in a column labeled SEQ.

### Maximum Length 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Maximum number of characters that one occurrence of the data field may occupy. It is calculated to include the component and sub component separators. Because the maximum length is that of a single occurrence, the repetition separator is not included in calculating the maximum length. In the segment attribute tables this information is in a column labeled LEN.

### Data Types 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restrictions on the contents of the data field. There are a number of data types defined by HL7. The data types used in this specification are described in the next section titled Data Types. This information is in a column labeled DT in the segment attribute tables.

### Optionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whether the field is required, optional, or conditional in a segment. The designations are:

| R   | Required                                                   |
|-----|------------------------------------------------------------|
| O   | Optional                                                   |
| C   | Conditional on the trigger event or on some other field(s) |
| X   | Not used with this trigger event                           |

In the segment attribute tables this information is in a column labeled OPT.

### Repetition 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whether the field may repeat. The designations are:

| N         | No repetition                                                           |
|-----------|-------------------------------------------------------------------------|
| Y         | Field may repeat up to the number of times specified in the integer     |
| (integer) | the field may repeat up to the number of times specified in the integer |

Each occurrence may contain the number of characters specified by the field’s maximum length. In the segment attribute tables this information is in a column labeled RP/#.

### Message Delimiters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In constructing a message certain special characters are used. They are the segment terminator, the field separator, the component separator, subcomponent separator, repetition separator, and escape character. The segment terminator is always a carriage return (in ASCII, a hex 0D). The other delimiters are defined in the MSH segment, with the field delimiter in the 4th character position, and the other delimiters occurring as in the field called Encoding Characters, which is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the entire message. VISTA Radiology/Nuclear Medicine uses the HL7 recommended values found in the table below.

#### Delimiter Values 

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 35%" />
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
<td>&lt;cr&gt;<br />
hex 0D</td>
<td>-</td>
<td>Terminates a segment record. This value cannot be changed by implementers.</td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>|</td>
<td>-</td>
<td>Separates two adjacent data fields within a segment. It also separates the segment ID from the first data field in each segment.</td>
</tr>
<tr class="odd">
<td>Component Separator</td>
<td>^</td>
<td>1</td>
<td>Separates adjacent components of data fields where allowed.</td>
</tr>
<tr class="even">
<td>Subcomponent Separator</td>
<td>&amp;</td>
<td>4</td>
<td>Separates adjacent subcomponents of data fields where allowed. If there are no subcomponents, this character may be omitted.</td>
</tr>
<tr class="odd">
<td>Repetition Separator</td>
<td>~</td>
<td>2</td>
<td>Separates multiple occurrences of a field where allowed.</td>
</tr>
<tr class="even">
<td>Escape Character</td>
<td>\</td>
<td>3</td>
<td>Escape character for use with any field represented by an ST, TX, or FT data type, or for use with the data (fourth) component of the ED data type If no escape characters are used in a message, this character may be omitted. However, it must be present if subcomponents are used in the message.</td>
</tr>
</tbody>
</table>

## ## Data Types 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HL7 Data Types 

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Type Category/<br />
Data Type</th>
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
<td>CE</td>
<td>Coded Element</td>
<td>identifier ^ text ^ name of coding system ^alternate identifier ^ alternate text ^ name of alternate coding system</td>
</tr>
<tr class="odd">
<td>CM</td>
<td>Composite</td>
<td>Combination of components of varying data types</td>
</tr>
<tr class="even">
<td>CQ</td>
<td>Composite quantity with units</td>
<td>quantity (NM) ^ units (CE)</td>
</tr>
<tr class="odd">
<td>CX</td>
<td>Extended composite ID with check digit</td>
<td>ID ^ check digit ^ code identifying the check digit scheme employed</td>
</tr>
<tr class="even">
<td>EI</td>
<td>Entity identifier</td>
<td>entity identifier ^ namespace ID ^ universal ID ^universal ID type</td>
</tr>
<tr class="odd">
<td>FT</td>
<td>Formatted text</td>
<td>See section (Use of escape sequences in text fields) for a list of allowed formatting commands.</td>
</tr>
<tr class="even">
<td>HD</td>
<td>Hierarchic designator</td>
<td>namespace ID ^ universal ID ^ universal ID type</td>
</tr>
<tr class="odd">
<td>ID</td>
<td>Coded value for HL7 defined tables</td>
<td>Valued from a table of HL7 legal values</td>
</tr>
<tr class="even">
<td>IS</td>
<td>Coded value for user-defined tables</td>
<td>Valued from a table of site legal values</td>
</tr>
<tr class="odd">
<td>PT</td>
<td>Processing type</td>
<td>Processing ID ^ processing mode</td>
</tr>
<tr class="even">
<td>ST</td>
<td>String</td>
<td>String data is left justified with trailing blanks optional.</td>
</tr>
<tr class="odd">
<td>TQ</td>
<td>Timing quantity</td>
<td>Utilizes the Priority component for order priority</td>
</tr>
<tr class="even">
<td>TS</td>
<td>Time stamp</td>
<td>YYYYMMDDHHMMSS</td>
</tr>
<tr class="odd">
<td>TX</td>
<td>Text data</td>
<td>String data meant for user display.</td>
</tr>
<tr class="even">
<td>XCN</td>
<td>Extended composite id number and name for persons</td>
<td>ID ^ family name ^ given name ^ middle initial or name</td>
</tr>
<tr class="odd">
<td>XPN</td>
<td>Extended person name</td>
<td>family name ^ given name ^ middle initial or name</td>
</tr>
</tbody>
</table>

## ## Use of Escape Sequences in Text Fields 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a field of type TX, FT, or CF is being encoded, the escape character may be used to signal certain special characteristics of portions of the text field. The escape character is whatever display ASCII character is specified in the Escape Character component of MSH-2-encoding characters. The character \\ must be used to represent the character so designated in a message. An escape sequence consists of the escape character followed by an escape code ID of one character, and another occurrence of the escape character. The following escape sequences are decoded by the Rad/Nuc Med Interface for *OBX-5– Observation value* only:

| \S\\ | component separator    |
|------|------------------------|
| \T\\ | subcomponent separator |
| \R\\ | repetition separator   |
| \E\\ | escape character       |

No escape sequence may contain a nested escape sequence

## Specification Conventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Segment Tables Definitions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Seq Position</th>
<th>Ordinal position of the data field within the segment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Len</td>
<td>Maximum length of a field</td>
</tr>
<tr class="even">
<td>DT</td>
<td>HL7 data type</td>
</tr>
<tr class="odd">
<td>OPT</td>
<td><p>(R)equired</p>
<p>(O)ptional</p>
<p>(C)onditional</p></td>
</tr>
<tr class="even">
<td>RP/#</td>
<td>Repeating field (Y/N/#)</td>
</tr>
<tr class="odd">
<td>Element Name</td>
<td>Field description</td>
</tr>
<tr class="even">
<td>Comments</td>
<td><ul>
<li><p>NV - Not valued when VISTA Rad/Nuc Med is receiver</p></li>
<li><p>NV - No value when VISTA Rad/Nuc Med is the sender</p></li>
<li><p>The &lt;xx&gt;/&lt;xx&gt;/&lt;xx&gt; after each field definition is &lt;Seq&gt;/&lt;Len&gt;/&lt;DT&gt; for that field and is for reference only.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# # HL7 Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HL7 Message Definitions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ORM - General Order Message (Event type O01) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The function of this message is to initiate the transmission of information about an order. This includes placing new orders, cancellation of existing orders, discontinuation, holding, etc. ORM messages can originate also with a placer, filler, or an interested third party.

The trigger event{ XE “trigger event” } for this message is any change to an order. Such changes include submission of new orders, cancellations, updates, patient and non patient specific orders, etc.

|             |                        |                 |
|-------------|------------------------|-----------------|
| Segment | Order Message      | HL7 Chapter |
| MSH         | Message header         | 2               |
| PID         | Patient identification | 3               |
| ORC         | Common order           | 4               |
| OBR         | Order detail           | 4               |
| OBX         | Observation/Result     | 7               |

### ORU – Unsolicited transmission of an observation (Event type R01) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The function of this message is to initiate the transmission of information about a report. With the observation segment (OBX), and the OBR, one can construct almost any clinical report as a three-level hierarchy, with the PID segment at the upper level, an order segment (OBR) at the next level and one or more observation segments (OBX) at the bottom. One result segment (OBX) is transmitted for each component of a diagnostic report, such as an EKG or obstetrical ultrasound or electrolyte battery.

\Many report headers (OBR) may be sent beneath each patient segment, with many separate observation segments (OBX) beneath each OBR.

|             |                        |                 |
|-------------|------------------------|-----------------|
| Segment | Order Message      | HL7 Chapter |
| MSH         | Message header         | 2               |
| PID         | Patient identification | 3               |
| OBR         | Order detail           | 4               |
| OBX         | Observation/Result     | 7               |

### ## HL7 Segment Definitions and Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len | DT  | OPT | RP/# | Element Name                    | Comments  |
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

#### MSH field definitions 

######## MSH – Field Separator \<1\>/\<1\>/\<ST\> 

Definition: This field contains the separator between the segment ID and the first real field, MSH-2-encoding characters. As such it serves as the separator and defines the character to be used as a separator for the rest of the message. Recommended value is \|, (ASCII 124).

######## MSH – Encoding Characters \<2\>/\<4\>/\<ST\> 

Definition: This field contains the four characters in the following order: the component separator, repetition separator, escape character, and subcomponent separator. Recommended values are ^~\\, (ASCII 94, 126, 92, and 38, respectively).

######## MSH – Sending Application \<3\>/\<180\>/\<HD\> 

Definition: This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site defined.

######## MSH – Sending Facility \<4\>/\<180\>/\<HD\> 

Definition: This field contains the address of one of several occurrences of the same application within the sending system. Entirely user-defined.

######## MSH – Receiving Application \<5\>/\<180\>/\<HD\> 

Definition: This field uniquely identifies the receiving application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.

######## MSH – Receiving Facility \<6\>/\<180\>/\<HD\> 

Definition: This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations. See comments: *MSH-4–Sending facility*. Entirely site-defined.

######## MSH – Date/Time Of Message \<7\>/\<26\>/\<TS\> 

Definition: This field contains the date/time that the sending system created the message. If the time zone is specified, it will be used throughout the message as the default time zone.

Format

YYYYMMDDHHMMSS

######## MSH – Message Type \<9\>/\<7\>/\<CM\> 

Components

\<message type (ID)\> ^ \<trigger event (ID)\>

Definition: This field contains the message type and trigger event for the message.

VISTA Rad/Nuc Med sends an ORM message type with the trigger event O01 for orders and ORU message type with the trigger event R01 for unsolicited observation results.

######## MSH – Message Control ID \<10\>/\<20\>/\<ST\> 

Definition: This field contains a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message acknowledgment segment (MSA).

########  MSH – Processing ID \<11\>/\<3\>/\<PT\> 

Components

\<processing ID (ID)\> ^ \<processing mode (ID)\>

Definition: This field identifies the current status of the interface. The processing mode component is not used.

| Value | Description |
|-------|-------------|
| P     | Production  |
| D     | Debugging   |
| T     | Training    |

######## MSH – Version ID \<12\>/\<8\>/\<ID\> 

Definition: This field is matched by the receiving system to its own version to be sure the message will be interpreted correctly.

The VistA Rad/Nuc Med HL7 interface to COTS voice recognition systems use version

2.3 of the HL7 standard.

######## MSH – Country Code \<17\>/\<2\>/\<ID\> 

Definition: This field contains the country of origin for the message.

### PID Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len | DT     | OPT | RP/# | Element Name                      | Comments  |
|-----|-----|--------|-----|------|-----------------------------------|-----------|
| 1   | 4   | SI     | O   |      | Set ID - Patient ID               | NV        |
| 2   | 20  | CX     | O   |      | Patient ID (External ID)          | See Notes |
| 3   | 20  | CX     | R   | Y    | Patient ID (Internal ID)          | See Notes |
| 4   | 20  | CX     | O   | Y    | Alternate Patient ID - PID        | NV        |
| 5   | 48  | XPN    | R   | Y    | Patient Name                      | See Notes |
| 6   | 48  | XPN    | O   |      | Mother’s Maiden Name              | NV        |
| 7   | 26  | TS     | O   |      | Date/Time of Birth                | See Notes |
| 8   | 1   | IS     | O   |      | Sex                               | See Notes |
| 9   | 48  | XPN    | O   | Y    | Patient Alias                     | NV        |
| 10  | 1   | IS     | O   |      | Race                              | NV        |
| 11  | 106 | XAD    | O   | Y    | Patient Address                   | NV        |
| 12  | 4   | IS | B   |      | County Code                       | NV        |
| 13  | 40  | XTN    | O   | Y    | Phone Number - Home               | NV        |
| 14  | 40  | XTN    | O   | Y    | Phone Number - Business           | NV        |
| 15  | 60  | CE     | O   |      | Primary Language                  | NV        |
| 16  | 1   | IS     | O   |      | Marital Status                    | NV        |
| 17  | 3   | IS     | O   |      | Religion                          | NV        |
| 18  | 20  | CX     | O   |      | Patient Account Number            | NV        |
| 19  | 16  | ST     | O   |      | SSN - Patient                     | See Notes |
| 20  | 25  | DUN    | O   |      | Driver's License Number - Patient | NV        |
| 21  | 20  | CX     | O   | Y    | Mother's Identifier               | NV        |
| 22  | 3   | IS     | O   |      | Ethnic Group                      | NV        |
| 23  | 60  | ST     | O   |      | Birth Place                       | NV        |
| 24  | 2   | ID     | O   |      | Multiple Birth Indicator          | NV        |
| 25  | 2   | NM     | O   |      | Birth Order                       | NV        |
| 26  | 4   | IS     | O   | Y    | Citizenship                       | NV        |
| 27  | 60  | CE     | O   |      | Veterans Military Status          | NV        |
| 28  | 80  | CE     | O   |      | Nationality                       | NV        |
| 29  | 26  | TS     | O   |      | Patient Death Date and Time       | NV        |
| 30  | 1   | ID     | O   |      | Patient Death Indicator           | NV        |

#### PID field definitions 

######## PID – Patient ID (external ID) \<2\>/\<20\>/\<CX\> 

Components

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>

Definition: When the patient is from another institution, outside office, etc., the identifier used by that institution can be shown in this field.

VistA Rad/Nuc Med uses the Patient SSN or pseudo-SSN as the Patient ID in the format of “555-55-5555” and “555-55-5555P”. The “P” indicates a pseudo-SSN.

The ID component only is used in this field.

######## PID – Patient ID (internal ID) \<3\>/\<20\>/\<CX\> 

Components

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>

Definition: This field contains the primary identifier, or other identifiers used by the facility to identify a patient uniquely. VISTA Rad/Nuc Med uses the M10 coding scheme.

######## PID – Patient Name \<5\>/\<48\>/\<XPN\> 

Components

\<family name (ST)\> ^ \<given name (ST)\> ^ \<middle initial or name (ST)\>

Definition: This field contains the legal name of the patient.

######## PID – Date/Time of Birth \<7\>/\<26\>/\<TS\> 

Definition: This field contains the patient’s date of birth.

Format

YYYYMMDD

######## PID – Sex \<8\>/\<1\>/\<IS\> 

Definition: This field contains the patient’s sex.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |
| O     | Other       |
| U     | Unknown     |

######## PID – SSN – Patient \<19\>/\<16\>/\<ST\>

Definition: This field contains the patient’s social security number.

Format

\[555555555\] or \[555555555P\]

> **NOTE:** PID does not include the (-) in this field.

### ORC Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len | DT  | OPT | RP/# | Element Name              | Comments  |
|-----|-----|-----|-----|------|---------------------------|-----------|
| 1   | 2   | ID  | R   |      | Order Control             | See Notes |
| 2   | 22  | EI  | O   |      | Placer Order Number       | NV        |
| 3   | 22  | EI  | O   |      | Filler Order Number       | NV        |
| 4   | 22  | EI  | O   |      | Placer Group Number       | See Notes |
| 5   | 2   | ID  | O   |      | Order Status              | See Notes |
| 6   | 1   | ID  | O   |      | Response Flag             | NV        |
| 7   | 200 | TQ  | O   |      | Quantity/Timing           | NV        |
| 8   | 200 | CM  | O   |      | Parent                    | See Notes |
| 9   | 26  | TS  | O   |      | Date/Time of Transaction  | See Notes |
| 10  | 120 | XCN | O   |      | Entered By                | NV        |
| 11  | 120 | XCN | O   |      | Verified By               | NV        |
| 12  | 120 | XCN | O   |      | Ordering Provider         | NV        |
| 13  | 80  | PL  | O   |      | Enterer’s Location        | NV        |
| 14  | 40  | XTN | O   | Y/2  | Call Back Phone Number    | NV        |
| 15  | 26  | TS  | O   |      | Order Effective Date/Time | NV        |
| 16  | 200 | CE  | O   |      | Order Control Code Reason | NV        |
| 17  | 60  | CE  | O   |      | Entering Organization     | NV        |
| 18  | 60  | CE  | O   |      | Entering Device           | NV        |
| 19  | 120 | XCN | O   |      | Action By                 | NV        |

#### ORC field definitions 

######## ORC – Order Control \<1\>/\<2\>/\<ID\> 

Definition: Determines the function of the order segment.

| Value | Description               |
|-------|---------------------------|
| NW    | New Registered            |
| CA    | Cancelled or Deleted Exam |
| XO    | Examined /Images Captured |

######## ORC – Placer Group Number \<4\>/\<22\>/\<EI\> 

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \< universal ID type (ID)\>

Definition: This field allows an order placing application to group sets of orders together and subsequently identify them.

One of the features introduced in v5.0 of VISTA Radiology/Nuclear Medicine allows multiple exams to be combined in a comprehensive report. This feature is called a “printset”. The printset concept is addressed by HL7 through the use of a unique identifier passed to the receiving system in the placer group number to group a set of orders for a single report. An identical entity identifier will be sent in this field for each member of a printset.

The first component of this field, the entity identifier, only will be present only if the procedure is a member of a printset. The entity identifier will be represented by a combination of the patient SSN, or pseudo SSN, and the date and time that the printset was ordered in VISTA. Receiving application should group the results for all orders with the same placer group number and update the order status appropriately.

Example

4583359007009280.8678 or 458335900P7009280.8678

######## ORC – Order Status \<5\>/\<2\>/\<ID\> 

Definition: This field is the status of an order.

| Value | Description               |
|-------|---------------------------|
| IP    | Registered (In Progress)  |
| CA    | Cancelled or Deleted Exam |
| CM    | Examined /Images Captured |

######## ORC – Parent \<8\>/\<200\>/\<CM\> 

Definition: This field relates a child to its parent when a parent-child relationship exists.

The first component only will be present only if the procedure is part of an exam set (ordered under one procedure name) or printset (ordered under one procedure name and only one report message will be generated since a single report covers entire set of procedures.) See *ORC-4 Placer Group number* for details of printset operations.

Format

EXAMSET: parent_procedure_name

PRINTSET: parent_procedure_name

> **NOTE:** Under rare circumstances, the parent procedure order will have been purged at the time the message is created. If this is true, the parent_procedure_name will be replaced by the text “ORIGINAL ORDER PURGED”.

######## ORC – Date/Time of Transaction \<9\>/\<26\>/\<TS\> 

Definition: This field is the date and time the current transaction enters the ordering application. Date/time of registration, cancel, or image collection.

Format

YYYYMMDDHHMMSS

### OBR Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len | DT  | OPT | RP/# | Element Name                               | Comments  |
|-----|-----|-----|-----|------|--------------------------------------------|-----------|
| 1   | 4   | SI  | C   |      | Set ID - OBR                               | NV        |
| 2   | 75  | EI  | C   |      | Placer Order Number                        | See Notes |
| 3   | 75  | EI  | C   |      | Filler Order Number +                      | See Notes |
| 4   | 200 | CE  | R   |      | Universal Service ID                       | See Notes |
| 5   | 2   | ID  | B   |      | Priority                                   | NV        |
| 6   | 26  | TS  | B   |      | Requested Date/time                        | NV        |
| 7   | 26  | TS  | C   |      | Observation Date/Time \#                   | See Notes |
| 8   | 26  | TS  | O   |      | Observation End Date/Time \#               | NV        |
| 9   | 20  | CQ  | O   |      | Collection Volume \*                       | NV        |
| 10  | 60  | XCN | O   | Y    | Collector Identifier \*                    | NV        |
| 11  | 1   | ID  | O   |      | Specimen Action Code \*                    | NV        |
| 12  | 60  | CE  | O   |      | Danger Code                                | NV        |
| 13  | 300 | ST  | O   |      | Relevant Clinical Info.                    | NV        |
| 14  | 26  | TS  | C   |      | Specimen Received Date/Time \*             | See Notes |
| 15  | 300 | CM  | O   |      | Specimen Source \*                         | NV        |
| 16  | 80  | XCN | O   | Y    | Ordering Provider                          | See Notes |
| 17  | 40  | XTN | O   | Y/2  | Order Callback Phone Number                | NV        |
| 18  | 60  | ST  | O   |      | Placer field 1                             | See Notes |
| 19  | 60  | ST  | O   |      | Placer field 2                             | NV        |
| 20  | 60  | ST  | O   |      | Filler Field 1 +                           | See Notes |
| 21  | 60  | ST  | O   |      | Filler Field 2 +                           | NV        |
| 22  | 26  | TS  | C   |      | Results Rpt/Status Chng - Date/Time +      | See Notes |
| 23  | 40  | CM  | O   |      | Charge to Practice +                       | NV        |
| 24  | 10  | ID  | O   |      | Diagnostic Serv Sect ID                    | NV        |
| 25  | 1   | ID  | C   |      | Result Status +                            | See Notes |
| 26  | 400 | CM  | O   |      | Parent Result +                            | NV        |
| 27  | 200 | TQ  | O   | Y    | Quantity/Timing                            | See Notes |
| 28  | 150 | XCN | O   | Y/5  | Result Copies To                           | NV        |
| 29  | 150 | CM  | O   |      | Parent                                     | NV        |
| 30  | 20  | ID  | O   |      | Transportation Mode                        | NV        |
| 31  | 300 | CE  | O   | Y    | Reason for Study                           | NV        |
| 32  | 200 | CM  | O   |      | Principal Result Interpreter +             | See Notes |
| 33  | 200 | CM  | O   | Y    | Assistant Result Interpreter +             | See Notes |
| 34  | 200 | CM  | O   | Y    | Technician +                               | NV        |
| 35  | 200 | CM  | O   | Y    | Transcriptionist +                         | See Notes |
| 36  | 26  | TS  | O   |      | Scheduled Date/Time +                      | NV        |
| 37  | 4   | NM  | O   |      | Number of Sample Containers \*             | NV        |
| 38  | 60  | CE  | O   | Y    | Transport Logistics of Collected Sample \* | NV        |
| 39  | 200 | CE  | O   | Y    | Collector’s Comment \*                     | NV        |
| 40  | 60  | CE  | O   |      | Transport Arrangement Responsibility       | NV        |
| 41  | 30  | ID  | O   |      | Transport Arranged                         | NV        |
| 42  | 1   | ID  | O   |      | Escort Required                            | NV        |
| 43  | 200 | CE  | O   | Y    | Planned Patient Transport Comment          | NV        |

#### OBR Field Definitions 

######## OBR – Placer Order Number \<2\>/\<75\>/\<EI\> 

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \< universal ID type (ID)\>

Definition: This field contains the VISTA Rad/Nuc Med long case number. The first component only will be present. The data represented by the entity identifier component is a combination of the order date and case number. The component only is used in this field.

Format

071999-521

> **NOTE:** The order date used in this field is not used as an actual date. Its use is strictly limited to that of an identifier. No date calculations are performed on this field.

######## OBR – Filler Order Number \<3\>/\<75\>/\<EI\> 

Components

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \< universal ID type (ID)\>

Definition: This is a permanent identifier for an order and its associated observations. The first component contains the date/time the procedure was ordered on VistA and the procedure number for the case after the “-“. The procedure number will increment by one for each additional member of a printset. The second component contains the long case number. The third component is the coding scheme and is defined as “L” for Local. The fourth component is not used.

Format

7009280.8678-1^071999-521^L

######## OBR – Universal Service ID \<4\>/\<200\>/\<CE\> 

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

Definition: This field is the identifier code for the requested observation/test/battery.

> **NOTE:** VISTA Rad/Nuc Med uses the CPT-4 coding scheme. The name of coding system component is defined as “C4” for the CPT-4 coding scheme in the HL7 and ASTM 123888 standards.

Example

75659^X-RAY EXAM OF ARM ARTERIES^C4^280^ANGIO BRACHIAL RETROGRADE  
CP^99RAP

######## OBR – Observation Date/Time \<7\>/\<26\>/\<TS\> 

Definition: This field is the clinically relevant date/time of the observation. In the case of observations taken directly from a subject, it is the actual date and time the observation was obtained. In the case of a specimen-associated study, this field shall represent the date and time the specimen was collected or obtained. (This is a results-only field except when the placer or a third-party has already drawn the specimen.) This field is conditionally required. When the OBR is transmitted as part of a report message, the field must be filled in. If it is transmitted as part of a request and a sample has been sent along as part of the request, this field must be filled in because this specimen time is the physiologically relevant date/time of the observation.

Format

YYYYMMDDHHMMSS

######## OBR – Observation end date/time \<8\>/\<26\>/\<TS\> 

Definition: This field is the end date and time of a study or timed specimen collection. If an observation takes place over a substantial period of time, it will indicate when the observation period ended. For observations made at a point in time, it will be null. This is a results field except when the placer or a party other than the filler has already drawn the specimen.

> **NOTE:** VistA Rad/Nuc Med will always send a null value in this field.

######## OBR – Collection volume \<9\>/\<20\>/\<CQ\> 

Components

\<quantity (NM)\> ^ \<units (CE)\>

Definition: For laboratory tests, the collection volume is the volume of a specimen. The default unit is ML. Specifically, units should be expressed in the ISO Standard unit abbreviations (ISO-2955,1977). This is a results-only field except when the placer or a party has already drawn the specimen.

> **NOTE:** VistA Rad/Nuc Med will always send a null value in this field.

######## OBR – Received Date/Time \<14\>/\<26\>/\<TS\> 

Definition: For observations requiring a specimen, the specimen received date/time is the actual login time at the diagnostic service. This field must contain a value when the order is accompanied by a specimen, or when the observation required a specimen and the message is a report.

Format

YYYYMMDDHHMMSS

######## OBR – Ordering Provider \<16\>/\<80\>/\<XCN\> 

Components

\<ID number (ST)\> ^ \<family name (ST)\> ^ \<given name (ST)\> ^ \<middle initial or name (ST)\>

Definition: This field identifies the provider who ordered the procedure.

######## OBR – Placers Field \#1 \<18\>/\<60\>/\<ST\> 

Definition: This field contains the patient location, Ward/Clinic.

######## OBR – Fillers Field \#1 \<20\>/\<60\>/\<ST\> 

Definition: This field is definable for any use by the filler. However, Rad/Nuc Med will send information about the imaging location in this field to maintain backward compatibility with PACS systems. The information that is sent in the order message in this field is not required in the report message returned by voice recognition systems.

Format

IEN file \#79.1^name of imaging location^station \#^station name

Example

4^X-RAY CLINIC^499^SUPPORT ISC

########  OBR – Fillers Field \#2 \<21\>/\<60\>/\<ST\> 

Definition: This field is similar to filler field \#1. Rad/Nuc Med will send information about the imaging location in this field to maintain backward compatibility with PACS systems. The information that is sent in the order message in this field is not required in the report message returned by voice recognition systems.

Format

abbreviated Imaging-type^Imaging type name

Example

RAD^GENERAL RADIOLOGY

######## OBR – Results Rpt/Status Change Date/Time \<22\>/\<26\>/\<TS\> 

Definition: This field specifies the date/time when the results were reported or status changed. This field is used to indicate the date and time that the results are composed into a report and released, or that a status, as defined in ORC-5 order status, is entered or changed. (This is a results field only.)

When other applications (such as office or clinical database applications) query the laboratory application for untransmitted results, the information in this field may be used to control processing on the communications link. Usually, the ordering service would want only those results for which the reporting date/time is greater than the date/time the inquiring application last received results.

Format

YYYYMMDDHHMMSS

######## OBR – Result Status \<25\>/\<1\>/\<ID\> 

Definition: This field is the status of results for this order. This conditional field is required whenever the OBR is contained in a report message.

| Value | Description                        |
|-------|------------------------------------|
| A     | Addendum, Correction               |
| F     | Final, Verified                    |
| R     | Preliminary, Released/Not Verified |
| VAQ   | Release Study (NTP)                |

######## OBR – Quantity/Timing \<27\>/\<20\>/\<TQ\> 

Components

\<quantity (CQ)\> ^ \<interval (CM)\> ^ \<duration (ST)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<priority (ID)\> ^ \<condition (ST)\> ^ \<text (TX)\> ^ \<conjunction (ID)\> ^ \<order sequencing (CM)\>

Definition: This field contains the priority component of the order only.

Format

^^^^^S

| Value | Description |
|-------|-------------|
| S     | Stat        |
| A     | Urgent      |
| R     | Routine     |

######## OBR – Principal Result Interpreter \<32\>/\<200\>/\<CM\> 

Components

\<name (CN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<ID number (ST)\> & \<family name (ST)\> & \<given name (ST)\> & \<middle initial or name (ST)\> & \<suffix (e.g., JR or III) (ST)\> & \<prefix (e.g., DR) (ST)\> & \<degree (e.g., MD (ST)\> & \<source table (IS)\> & \<assigning authority (HD)\>

Definition: This field identifies the attending, or staff, physician or who interpreted the observation and is responsible for the report content.

> **NOTE:** The name component is the only component validated in this field by VistA Rad/Nuc Med. The Subcomponents of name must be followed according to the standard for correct validation. The identifier must match the IEN of the provider in the NEW PERSON File in VistA and must have a STAFF designation.

######## OBR – Assistant Result Interpreter \<33\>/\<200\>/\<CM\> 

Components

\<name (CN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> Subcomponents of name: \<identifier(ST)\> & \<test (ST)\> & \<name of coding system (ST)\> & \<alternate identifier (ST)\> & \<alternate text (ST)\> & \<name of alternate coding system (ST)\>

Definition: This field identifies the resident physician who assisted with the interpretation of this study.

> **NOTE:** The name component is the only component validated in this field by VistA Rad/Nuc Med. The Subcomponents of name must be followed according to the standard for correct validation. The identifier must match the IEN of the provider in the NEW PERSON File in VistA and must have RESIDENT designation

########  OBR – Transcriptionist \<35\>/\<200\>/\<CM\> 

Components

\<name (CN)\> ^ \<start date/time (TS)\> ^ \<end date/time (TS)\> ^ \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<patient location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\>

Subcomponents of name

\<identifier(ST)\> & \<test (ST)\> & \<name of coding system (ST)\> & \<alternate identifier (ST)\> & \<alternate text (ST)\> & \<name of alternate coding system (ST)\>

Definition: This field identifies the report transcriber.

> **NOTE:** The name component is the only component validated in this field by VISTA Rad/Nuc Med. The Subcomponents of name must be followed according to the standard for correct validation. The identifier must match the IEN of the transcriptionist in the NEW PERSON File in VISTA.

### OBX Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len       | DT  | OPT | RP/#  | Element Name                 | Comments  |
|-----|-----------|-----|-----|-------|------------------------------|-----------|
| 1   | 10        | SI  | O   |       | Set ID - OBX                 | NV        |
| 2   | 2         | ID  | C   |       | Value Type                   | See Notes |
| 3   | 590       | CE  | R   |       | Observation Identifier       | See Notes |
| 4   | 20        | ST  | C   |       | Observation Sub-ID           | NV        |
| 5   | 65536[^1] | \*  | C   | Y[^2] | Observation Value            | See Notes |
| 6   | 60        | CE  | O   |       | Units                        | NV        |
| 7   | 10        | ST  | O   |       | References Range             | NV        |
| 8   | 5         | ID  | O   | Y/5   | Abnormal Flags               | NV        |
| 9   | 5         | NM  | O   |       | Probability                  | NV        |
| 10  | 2         | ID  | O   | Y     | Nature of Abnormal Test      | NV        |
| 11  | 1         | ID  | R   |       | Observ Result Status         | See Notes |
| 12  | 26        | TS  | O   |       | Date Last Obs Normal Values  | NV        |
| 13  | 20        | ST  | O   |       | User Defined Access Checks   | NV        |
| 14  | 26        | TS  | O   |       | Date/Time of the Observation | NV        |
| 15  | 60        | CE  | O   |       | Producer's ID                | NV        |
| 16  | 80        | XCN | O   |       | Responsible Observer         | NV        |
| 17  | 60        | CE  | O   | Y     | Observation Method           | NV        |

#### OBX field definitions 

######## OBX – Value Type \<2\>/\<2\>/\<ID\> 

Definition: This field contains the format of the observation value in OBX. If the value is CE then the result must be a coded entry. When the value type is TX or FT then the results are bulk text. The valid values for the value type of an observation accepted by VistA Rad/Nuc Med are listed below.

| Value | Description                                                   |
|-------|---------------------------------------------------------------|
| CE    | Coded Element – Procedure or Diagnostic code follows          |
| FT    | Formatted Text                                                |
| TX    | Text Data - Modifier, clinical history or result text follows |
| ST    | String Data – Diagnostic code follows                         |

VistA Rad/Nuc Med will accept Diagnostic codes sent in two ways.

1.  OBX-2 Value Type is CE and OBX-5 Observation Value contains a valid Rad/Nuc Med Diagnosis code from file 78.3.

> Example

OBX\|1\|CE\|70551^MAGNETIC IMAGE, BRAIN (MRI)^CPT4\|0\|4^ABNORMALITY, ATTN. NEEDED^I9~5^MAJOR ABNORMALITY, PHYSICIAN AWARE^I9~8^POSSIBLE MALIGNANCY, FOLLOW-UP NEEDED^I9\|\|\|\|\|\|F

2.  OBX-2 Value Type is ST and identifier component of OBX-3 Observation Identifier is DIAG.

######## OBX – Observation Identifier \<3\>/\<590\>/\<CE\> 

Components

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

Definition: This field contains a unique identifier for the observation. The format is that of the Coded Element (CE). The valid identifier components are as follows.

| Value   | OBX Value Type | Description                                  |
|---------|----------------|----------------------------------------------|
| A       | TX             | Allergies                                    |
| D       | ST             | Signifies a locally defined Diagnosis code   |
| F       | TX ,FT         | Report Findings/Text History Impression Text |
| H       | TX             | Modifiers                                    |
| I       | TX             | CPT Modifiers                                |
| M       | TX             | Procedure                                    |
| C4 [^3] | CE             | Report Text                                  |
| P       | CE             | Allergies                                    |
| R       | TX             | Signifies a locally defined Diagnosis code   |

Diagnostic code must be from a predefined set contained in VISTA Rad/Nuc Med file \#78.3. If multiple diagnostic codes exist, the primary diagnosis will occur first.

######## OBX – Observation Value \<5\>/\<65536\>/\<\*\> 

Definition: This field contains the value observed by the observation producer. OBX-2value type contains the data type for this field according to which observation value is formatted.

######## Representation 

This field contains the value of OBX-3-observation identifier of the same segment. Depending upon the observation, the data type may be a number (e.g., a respiratory rate), a coded answer (e.g., a pathology impression recorded as SNOMED), or a date/time (the date/time that a unit of blood is sent to the ward). An observation value is always represented as the data type specified in OBX-2-value type of the same segment. Whether numeric or short text, the answer shall be recorded in ASCII text.

######## Reporting logically independent observations 

The main sections of dictated reports, such as radiologic studies or history and physicals, are reported as separate OBX segments. In addition, each logically independent observation should be reported in a separate OBX segment, i.e. one OBX segment should not contain the result of more than one logically independent observation.

######## OBX – Observ Result Status \<11\>/\<1\>/\<ID\> 

Definition: This field contains the observation result status. This field reflects the current completion status of the results for one Observation Identifier.

| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| F     | Final, results Verified; can only be changed with a corrected result |
| P     | Preliminary, results Released/Not Verified                           |
| C     | Record coming over is a correction and thus replaces a final result  |
| VAQ   | Release Study (VAQ)                                                  |

### MSA Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Seq | Len | DT  | OPT | RP/# | Element Name                | Comments  |
|-----|-----|-----|-----|------|-----------------------------|-----------|
| 1   | 2   | ID  | R   |      | Acknowledgment Code         | See Notes |
| 2   | 20  | ST  | R   |      | Message Control ID          | See Notes |
| 3   | 80  | ST  | O   |      | Text Message                | See Notes |
| 4   | 15  | NM  | O   |      | Expected Sequence Number    | NV        |
| 5   | 1   | ID  | B   |      | Delayed Acknowledgment Type | NV        |
| 6   | 100 | CE  | O   |      | Error Condition             | NV        |

#### MSA field definitions 

######## MSA – Acknowledgment Code \<1\>/\<2\>/\<ID\>

Definition: This field contains an acknowledgment code.

| Value | Description        |
|-------|--------------------|
| AA    | Application Accept |
| AE    | Application Error  |
| AR    | Application Reject |

######## MSA – Message Control ID \<2\>/\<20\>/\<ST\> 

Definition: This field contains the message control ID of the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

######## MSA – Text Message \<3\>/\<80\>/\<ST\> 

Definition: This field further describes an error condition. This text may be printed in the Rad/Nuc Med HL7 Voice Reporting Errors option and presented to an end user.

# Transactions Specifications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Radiology/Nuclear Medicine package will send an HL7 message with exam information to the COTS voice recognition system when each exam has been registered, examined (i.e., images have been collected), canceled, and when a report has been put in a status of Verified or Released/Not Verified.

## Specific Transactions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Registration 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VAMC may register a patient for an imaging exam at the time the patient arrives at the radiology or nuclear medicine reception desk for his/her appointment, or registration may be done up to a week prior to the appointment depending on the policy of that VAMC's imaging services. At this point, the registration message is broadcast as an Order (ORM) message and sent to the COTS voice recognition system. See the section on Messaging Specifics – ORM Message for details.

### Examined/Images Collected 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VISTA Rad/Nuc Med software allows the ADPAC to specify an exam status that will trigger this event. If, for example, the "Examined" status is specified, when the radiology tech enters the required data to cause the exam record to reach the "Examined" status, the examined message will be broadcast as an Order (ORM) message and sent to COTS voice recognition system. The segments used will be the same as the Registration module.

### Cancellation/Deletion 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an imaging tech or other VISTA Rad/Nuc Med software user cancels or deletes an exam, this will trigger the cancel message broadcast. An exam is usually canceled before it is done. However, since exam data may have been erroneously entered or entered for the wrong patient, the VISTA Rad/Nuc Med system allows users to back data out and cancel after an exam is done, and possibly after results reports are entered. So, there is a possibility that an examined message and a report message would have been broadcast prior to a cancellation message.

### Verified/Released Unverified Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report message is triggered when a VISTA Rad/Nuc Med radiologist or transcriptionist enters data causing the findings report to move to a "Verified" (final) or "Released/Unverified" (preliminary) status. Depending on the policy of the VAMC, the "Released/Unverified" status may or may not be allowed. If the released/unverified report is broadcast on a message, a later message will contain the verified (final) report. It is also possible for a verified report to be retracted ("Unverified"), then re-verified later. If this happens a second report message would be broadcast with the amended, re-verified report, or else an exam cancel/delete message would be broadcast retracting the entire exam.

## Messaging Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ORM Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an exam is registered, examined or canceled by the Radiology/Nuclear Medicine package, an Order (ORM) message is sent to the site-specified application. The ORM message consists of the following segments:

| Segment | Description            |
|---------|------------------------|
| MSH     | Message Header         |
| PID     | Patient Identification |
| ORC     | Common Order           |
| OBR     | Observational Request  |
| OBX     | Result                 |

Example: ORM message for new/registered order

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE­TCP\|POWERSCRIBE\|19990728125034\|\|ORM^O01\|4998329\|P\|2.3\|\|\|\|\|US

PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 ORC\|NW\|\|\|\|IP\|\|\|\|19990728125034 OBR\|\|072899-542\|7009271.8754-1^072899-542^L\|71030^CHEST X-RAY^C4^61^CHEST 4 VIEWS^99RAP\|\|\|19990728125034\|""\|""\|\|\|\|\|""\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|4^X-RAY CLINIC^499^SUPPORT ISC\|RAD^GENERAL RADIOLOGY\|19990728125034\|\|\|\|\|^^^^^R OBX\|\|CE\|P^PROCEDURE^L\|\|61^CHEST 4 VIEWS^L\|\|\|\|\|\|"" OBX\|\|TX\|M^MODIFIERS^L\|\|OPERATING ROOM EXAM\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This is the clinical history for the patient's exam. This is going to be \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|several lines in length so we can see what happens when we create the HL7 \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|message. \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This is the first line of the second paragraph. This is the second line of the\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|paragraph. \|\|\|\|\|\|""

Example: ORM messages for registration of a printset

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE­TCP\|POWERSCRIBE\|19990728150450\|\|ORM^O01\|4998367\|P\|2.3\|\|\|\|\|US PID\|\|000-66-999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 ORC\|NW\|\|\|0006699997009271.8496\|IP\|\|\|PRINTSET: HIP 1 VIEW\|19990728150450 OBR\|\|072899-549\|7009271.8496-1^072899-549^L\|75659^X-RAY EXAM OF ARM ARTERIES^C4^280^ANGIO BRACHIAL RETROGRADE CP^99RAP\|\|\|19990728150450\|""\|""\|\|\|\|\|""\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|4^X-RAY CLINIC^499^SUPPORT ISC\|RAD^GENERAL RADIOLOGY\|19990728150450\|\|\|\|\|^^^^^R OBX\|\|CE\|P^PROCEDURE^L\|\|280^ANGIO BRACHIAL RETROGRADE CP^L\|\|\|\|\|\|"" OBX\|\|TX\|M^MODIFIERS^L\|\|None\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This is the clinical history for the patient on the printset order \|\|\|\|\|\|""

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE­TCP\|POWERSCRIBE\|19990728150450\|\|ORM^O01\|4998372\|P\|2.3\|\|\|\|\|US PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 ORC\|NW\|\|\|0006699997009271.8496\|IP\|\|\|PRINTSET: HIP 1 VIEW\|19990728150450

OBR\|\|072899-550\|7009271.8496-2^072899-550^L\|75658^X-RAY EXAM OF ARM ARTERIES^C4^279^ANGIO BRACHIAL RETROGRADE S&I^99RAP\|\|\|19990728150450\|""\|""\|\|\|\|\|""\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|4^X-RAY  
CLINIC^499^SUPPORT ISC\|RAD^GENERAL RADIOLOGY\|19990728150450\|\|\|\|\|^^^^^R  
OBX\|\|CE\|P^PROCEDURE^L\|\|279^ANGIO BRACHIAL RETROGRADE S&I^L\|\|\|\|\|\|""  
OBX\|\|TX\|M^MODIFIERS^L\|\|None\|\|\|\|\|\|""  
OBX\|\|TX\|H^HISTORY^L\|\|This is the clinical history for the patient on the printset order \|\|\|\|\|\|""

A printset is a group of individual orders that comprise a single report. There are three differences between a printset order message and a single order message.

1.  ORC-4 Placer Group Number field will be populated with a unique identifier for each printset.  
    Each order message for a member of the printset will have the same identifier in ORC-4.
2.  ORC-8 Parent field will be populated with the printset parent name.  
    The format will always be in the form of

\[PRINTSET: {parent_procedure_name}\]

3.  OBR-3 Filler Order Number entity identifier component will have an incrementing procedure number for each member of the printset.  
    The format will always be in the form of

\[{nnnnnnn.nnnn-1}, {nnnnnnnn.nnnn-2}, etc.\]

Example: ORM message for an examined/images collected order

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE­TCP\|POWERSCRIBE\|19990728130506\|\|ORM^O01\|4998337\|P\|2.3\|\|\|\|\|US PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 ORC\|XO\|\|\|\|CM\|\|\|\|19990728130506 OBR\|\|072899-542\|7009271.8754-1^072899-542^L\|71030^CHEST X-RAY^C4^61^CHEST 4 VIEWS^99RAP\|\|\|19990728130506\|""\|""\|\|\|\|\|""\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|4^X-RAY CLINIC^499^SUPPORT ISC\|RAD^GENERAL RADIOLOGY\|19990728130506\|\|\|\|\|^^^^^R OBX\|\|CE\|P^PROCEDURE^L\|\|61^CHEST 4 VIEWS^L\|\|\|\|\|\|"" OBX\|\|TX\|M^MODIFIERS^L\|\|OPERATING ROOM EXAM\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This is the clinical history for the patient's exam. This is going to be \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|several lines in length so we can see what happens when we create the HL7 \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|message. \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This is the first line of the second paragraph. This is the second line of the\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|paragraph. \|\|\|\|\|\|""

Example: ORM message for a cancelled order

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE­TCP\|POWERSCRIBE\|19990728131832\|\|ORM^O01\|4998353\|P\|2.3\|\|\|\|\|US PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 ORC\|CA\|\|\|\|CA\|\|\|\|19990728131832 OBR\|\|072899-543\|7009271.8683-1^072899-543^L\|70551^MAGNETIC IMAGE, BRAIN (MRI)^C4^541^MAGNETIC IMAGE,BRAIN^99RAP\|\|\|19990728131832\|""\|"" \|\|\|\|\|""\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|6^MRI^499^SUPPORT ISC\|MRI^MAGNETIC RESONANCE IMAGING\|19990728131832 OBX\|\|CE\|P^PROCEDURE^L\|\|541^MAGNETIC IMAGE,BRAIN^L\|\|\|\|\|\|"" OBX\|\|TX\|M^MODIFIERS^L\|\|BILATERAL EXAM\|\|\|\|\|\|"" OBX\|\|TX\|H^HISTORY^L\|\|This order was created to show an HL7 cancel order message. \|\|\|\|\|\|""

> **NOTE:** The messages broadcast at these three event points (registered, examined and canceled) are almost identical, with the exception of the Order Control, Order Status, and Quantity/Timing fields. Differences to note between an HL7 message for registration, image collection (examined) and cancellation are shown here:

|                 |              |               |          |
|-----------------|--------------|---------------|----------|
| HL7 ORC Field   | Registration | Cancel/Delete | Examined |
| 1-Order Control | NW           | CA            | XO       |
| 5-Order Status  | IP           | CA            | CM       |

The Quantity/Timing value on the OBR segment (in the examples above, ^^^^^R) is omitted from the cancellation message.

The OBR segment may exceed 255 characters.

### ORU Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a report is Verified or Released/Not Verified by the Radiology/Nuclear Medicine package, an Order (ORU) message is sent to the site specified application. The ORU message consists of the following segments:

| Segment | Description            |
|---------|------------------------|
| MSH     | Message Header         |
| PID     | Patient Identification |
| OBR     | Observational Request  |
| OBX     | Result                 |

Example: ORU message containing report for single procedure

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK­TCP\|TalkStation\|19990728143025\|\|ORU^R01\|4998363\|P\|2.3\|\|\|\|\|US PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 OBR\|\|\|7009271.8754-1^072899-542^L\|71030^CHEST X-RAY^CPT4^61^CHEST 4 VIEWS^99RAP\|\|\|199907281245\|""\|""\|\|\|\|\|199907281430\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|\|\|199907281430\|\|\|F\|\| \|\|\|\|\|2172^RADPROVIDER^TWO^N\|2172^RADPROVIDER^TWO^N OBX\|\|TX\|I^IMPRESSION^L\|\|This is the impression text of a test report. \|\|\|\|\|\|F OBX\|\|ST\|D^DIAGNOSTIC CODE^L\|\|NORMAL\|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\|Report: Chest X-Ray \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\|\|\|\|\|\|\|F OBX\|\|CE\|P^PROCEDURE^L\|\|61^CHEST 4 VIEWS^L\|\|\|\|\|\|"" OBX\|\|TX\|M^MODIFIERS^L\|\|OPERATING ROOM EXAM\|\|\|\|\|\|""

Example: ORU message for "printset", (i.e., multiple procedures and single report)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK­TCP\|TalkStation\|19990728155951\|\|ORU^R01\|4998401\|P\|2.3\|\|\|\|\|US PID\|\|000-66-9999\|46^9^M10\|\|RADPATIENT^ONE\|\|19411225\|M\|\|\|\|\|\|\|\|\|\|\|000669999 OBR\|\|\|7009271.8496-1^072899-549^L\|75659^X-RAY EXAM OF ARM ARTERIES^CPT4^280^ANGIO BRACHIAL RETROGRADE CP^99RAP\|\|\|199907281503\|""\|""\|\|\|\|\|199907281559\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|\|\|199907281559\|\|\|F\|\|\|\|\| \|2172^RADPROVIDER^TWO^N\|2172^RADPROVIDER^TWO^N OBX\|\|CE\|P^PROCEDURE^L\|\|280^ANGIO BRACHIAL RETROGRADE CP^L\|\|\|\|\|\|"" OBR\|\|\|7009271.8496-2^072899-550^L\|75658^X-RAY EXAM OF ARM ARTERIES^CPT4^279^ANGIO BRACHIAL RETROGRADE S&I^99RAP\|\|\|199907281503\|""\|""\|\|\|\|\|199907281559\|\|2172^RADPROVIDER^TWO^N\|\|4AS\|\|\|\|199907281559\|\|\|F\|\|\|\| \|\|2172^RADPROVIDER^TWO^N\|2172^RADPROVIDER^TWO^N OBX\|\|CE\|P^PROCEDURE^L\|\|279^ANGIO BRACHIAL RETROGRADE S&I^L\|\|\|\|\|\|"" OBX\|\|TX\|I^IMPRESSION^L\|\|This is the impression text of the printset results. This text will be filed\|\|\|\|\|\|F OBX\|\|TX\|I^IMPRESSION^L\|\|for both procedures. \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\|Report: X-Ray of ARM ARTERIES \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F OBX\|\|TX\|R^REPORT^L\|\|\|\|\|\|\|\|F OBX\|\|TX\|M^MODIFIERS^L\|\|CONTRAST MEDIA USED\|\|\|\|\|\|""

### ACK Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The General Acknowledgment (ACK) message is sent by both systems as a response to ORM and ORU messages. The ACK message consists of the following segments:

| Segment | Description             |
|---------|-------------------------|
| MSH     | Message Header          |
| MSA     | Message Acknowledgement |

Example: ACK message

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-PSCRIBE-  
TCP\|POWERSCRIBE\|19990728155941\|\|ACK^R01\|4998399\|P\|2.3\|\|\|\|\|US  
MSA\|AA\|19990728160834

# # # # # # # Appendix – CPT Modifiers (RA\*5\*10)[^4] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine RAHLRU sets up the OBX segments for CPT Modifiers. This routine will be invoked when an HL7 message is sent due to any one of the following:

- An exam is registered,
- An exam is cancelled,
- An exam status is reached that is assigned to generate an HL7 message, or
- An exam report is verified.

The routine will set up the OBX segment(s) for CPT Modifier(s) in the following format:

OBX-2 = “CE”  
OBX-3 = “C4~CPT MODIFIERS~C4”  
OBX-5 = “nn~longname~C4~mmmmm~C4~longname~C4”  
OBX-11 = “X”

> **NOTE:** nn is field .01 of file \#81.3, CPT MODIFIER  
longname is field .02 of file \#81.3, CPT MODIFIER  
mmmmm is field .03 of file \#81.3, CPT MODIFIER; the triplet containing this value will be null if the CPT Modifier has no data for field .03 in file \#81.3.  
  
The delimiter symbol (~) may vary, as it is site configurable.

[^1]: <span id="_Ref221329019" class="anchor"></span> The length of the observation value field is variable, depending upon value type. See OBX-2-value type

[^2]: <span id="_Ref221329036" class="anchor"></span> May repeat for multipart, single answer results with appropriate data types, e.g., CE, TX, and FT data types

[^3]: <span id="_Ref221328830" class="anchor"></span> Patch RA\*5\*17 July 2000 Radiology HL7 interfaces for the new VISTA HL7 standards (post HL\*1.6\*57)

[^4]: Patch RA\*5\*10 CPT Modifiers