---
title: "LA*5.2*67/LR*5.2*290 Laboratory: POC HL7 Interface Specifications Document"
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: 
app_code: POC
app_name: "Laboratory: Point of Care"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*67
group_key: "POC:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 1
description: This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard. This interface forms the basis for the exchange of healthcare information between the VistA Laboratory
audience: 
keywords: 
  - message
  - vista
  - table
  - number
  - segment
  - code
  - application
  - laboratory
  - observation
  - identifier
page_count: 0
word_count: 5711
section_count: 4
table_count: 34
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/lab_52_poc_hl7_spec.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/lab_52_poc_hl7_spec.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=149"
---

![](la-5-2-67-lr-5-2-290-laboratory-poc-hl7-interface-specifications-document/001.png)

LABORATORY

HL7 INTERFACE

SPECIFICATIONS

POINT OF CARE

(POC)

June 2005

VistA Health Systems Design & Development

# # # # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # # Revision History](#revision-history)
- [# HEALTH LEVEL 7 INTERFACE SPECIFICATIONS](#health-level-7-interface-specifications)
  - [VistA Laboratory Point of Care Health Level 7 (HL7) Interface Standard Specifications V. 1.33](#vista-laboratory-point-of-care-health-level-7-hl7-interface-standard-specifications-v-133)
    - [Purpose](#purpose)
    - [Overview](#overview)
    - [General Specifications](#general-specifications)
    - [Transaction Specifications](#transaction-specifications)
    - [Communication Requirements for HL7 Interfaces](#communication-requirements-for-hl7-interfaces)
  - [#### Requirements:](#requirements)
  - [#### Error Management:](#error-management)
    - [### Requirements:](#requirements-1)
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Description</td>
<td>Section</td>
<td>Author</td>
</tr>
<tr class="even">
<td>8/13/04</td>
<td>Version 1.0</td>
<td>Initial Draft.</td>
<td>All</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/01/04</td>
<td>Version 1.1</td>
<td>Incorporated comments from Telcor implementation call of 9/01/04</td>
<td>All</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/13/04</td>
<td>Version 1.2</td>
<td>Incorporated change to R/O/C of placer and filler order number.</td>
<td>3.5.4</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/22/04</td>
<td>Version 1.3</td>
<td>Added clarification regarding how ordering provider and location is determined and processed.</td>
<td><p>3.5.6.12</p>
<p>3.5.6.13</p>
<p>3.5.4.16</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/12/05</td>
<td>Version 1.31</td>
<td>Update patient/provide names in examples messages to VA specified test names</td>
<td>4.2</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/24/05</td>
<td>Version 1.32</td>
<td><p>Updated OBR-16 Ordering Provider</p>
<p>Updated ORC-12 Ordering Provider</p>
<p>Corrected optionality of ORC/OBR segments in ORU message.</p>
<p>Added NTE segments to example ORU message.</p></td>
<td><p>3.5.4.16</p>
<p>3.5.6.12</p>
<p>4.2</p>
<p>4.2.a</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/23/05</td>
<td>Version 1.33</td>
<td>Corrected spelling of event type R01.</td>
<td><p>3.5.2.9</p>
<p>4.2.b</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# # HEALTH LEVEL 7 INTERFACE SPECIFICATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Laboratory Point of Care Health Level 7 (HL7) Interface Standard Specifications V. 1.33

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard. This interface forms the basis for the exchange of healthcare information between the VistA Laboratory software application and all non- VistA systems, especially those non- VistA systems that generate laboratory result information.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Statement of Intent

The Office of Information developed and implemented a generic interface to the HL7 Standard for use by the VistA Laboratory application in communicating with non- VistA systems to exchange point of care healthcare information. The interface strictly adheres to the HL7 Standard and avoids using “Z” type extensions to the Standard. This interface specification is subject to modification and revision to incorporate changes, improvements, and enhancements. This version supports HL7 V 2.4 Standard,

#### Scope

This document describes messages transmitted between the VistA Laboratory application and a non- VistA automated system. The purpose of these messages is to exchange information concerning laboratory results that relate to Point of Care (POC) testing.

### General Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Communication Protocol

The HL7 Standard defines only the seventh level of the Open System Inter-connect (OSI) protocol. This is the application level. Levels 1-6 involve primarily communication protocols. The HL7 Standard provides some guidance in this area. The communication Standard used for interfacing with the VistA Laboratory package is based on the HL7 Hybrid Lower Level Standard and Minimal Lower Level Standard as described in the HL7 Interface Standard document.

#### Application Processing Rules

The HL7 Standard describes the basic rules for application processing by the sending and receiving systems. Information contained in the Standard is not repeated here. Anyone wishing to interface with the VistA Laboratory package should become familiar with the HL7 Standard V. 2.4.

#### Messages

|     |                                   |
|-----|-----------------------------------|
| ACK | General Acknowledgment            |
| ORU | Observational Results Unsolicited |

#### Segments

Refer to section 4, Transaction Specifications, for details and examples of all segments used to interface with VistA Laboratory software application. The following HL7 segments are used to support the exchange of Laboratory information.

|     |                        |
|-----|------------------------|
| MSA | Message Acknowledgment |
| MSH | Message Header         |
| NTE | Notes and Comment      |
| OBR | Observation Request    |
| OBX | Observation            |
| ORC | Common Order           |
| PID | Patient Identification |

#### Fields

The segment definition tables list and describe the data fields in the segment and characteristics of their usage. The following information is specified about each data field.

Sequence Number (SEQ): The ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table.

Length (LEN): The maximum numbers of characters that one occurrence of the data field may occupy.

Data Type (DT): Restrictions on the contents of the data field as defined by the HL7 Standard.

Optionally (R/O/C): Whether the data field is required, optional, or conditional in a segment. The designations are R - required; O (null) -optional; and C - conditional on the trigger event.

VA (R/O/C): Designates whether the data field is required, optional, or conditional in a segment by the Department of Veterans Affairs (VA). The designations are R - required; O (null) -optional; and C - conditional on the trigger event.

Repetition (RP/#): Whether the field may repeat. The designations are N (null) - for no repetition allowed; Y - the field may repeat an indefinite or site determined number of times; and (integer) - the field may repeat up to the number of times specified in the integer.

Table (TBL#): A table of values that may be defined by HL7 or negotiated between the V*IST*A Laboratory application and the vendor system. Local tables used by the VA will begin with the prefix 99VA.

Element Name: Globally unique descriptive name for the field.

The following HL7 segment fields are used to support the exchange of Laboratory data for each of the segments listed in paragraph 3.4. Tables referenced in the segments can be found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for those fields that are utilized. The field definitions can include specific information (e.g., expected format) for transmission.

#### Segment: MSA - Message Acknowledgment

The MSA segment contains information sent while acknowledging another message.

|     |     |     |       |          |      |      |                     |
|-----|-----|-----|-------|----------|------|------|---------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME        |
| 1   | 2   | ID  | R     | R        |      | 8    | ACKNOWLEDGMENT CODE |
| 2   | 20  | ST  | R     | R        |      |      | MESSAGE CONTROL ID  |
| 3   | 80  | ST  |       | O        |      |      | TEXT MESSAGE        |

#### MSA field definitions

#### ACKNOWLEDGMENT CODE (ID)

The ACKNOWLEDGMENT CODE can have the following values:

|                                    |                    |
|------------------------------------|--------------------|
| HL7 Table 0008 ACKNOWLEDGMENT CODE |                    |
| Value                              | Description        |
| CA                                 | Commit Accept      |
| CE                                 | Commit Error       |
| CR                                 | Commit Reject      |
| AA                                 | Application Accept |
| AE                                 | Application Error  |
| AR                                 | Application Reject |

#### MESSAGE CONTROL ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

#### TEXT MESSAGE (ST)

This optional text field further describes an error condition. The text may be printed in error logs or presented to an end user.

When an ORU result message is accepted (AA) then this field will contain the unique identifier (UID) of the Laboratory accession that was created to store the results. If the message has an error it will contain the reason the results were unable to be processed.

#### Segment: MSH - Message Header

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

|     |     |     |       |          |      |      |                                 |
|-----|-----|-----|-------|----------|------|------|---------------------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME                    |
| 1   | 1   | ST  | R     | R        |      |      | FIELD SEPARATOR                 |
| 2   | 4   | ST  | R     | R        |      |      | ENCODING CHARACTERS             |
| 3   | 15  | ST  |       | R        |      |      | SENDING APPLICATION             |
| 4   | 20  | ST  |       | R        |      |      | SENDING FACILITY                |
| 5   | 30  | ST  |       | R        |      |      | RECEIVING APPLICATION           |
| 6   | 30  | ST  |       | R        |      |      | RECEIVING FACILITY              |
| 7   | 26  | TS  |       | R        |      |      | DATE/TIME OF MESSAGE            |
| 9   | 7   | CM  | R     | R        |      | 76   | MESSAGE TYPE                    |
| 10  | 20  | ST  | R     | R        |      |      | MESSAGE CONTROL ID              |
| 11  | 1   | ID  | R     | R        |      | 103  | PROCESSING ID                   |
| 12  | 8   | ID  | R     | R        |      | 104  | VERSION ID                      |
| 15  | 2   | ID  |       | R        |      | 155  | ACCEPT ACKNOWLEDGMENT TYPE      |
| 16  | 2   | ID  |       | R        |      | 155  | APPLICATION ACKNOWLEDGMENT TYPE |

#### MSH field definitions

The segment terminator is always a carriage return (in ASCII, a hex 0D).

The other delimiters are defined in the MSH segment, with the field delimiter in the 4th character position, and the other delimiters occurring as in the field called Encoding Characters, which is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the entire message.

#### FIELD SEPARATOR (ST)

This field is the separator between the segment ID and the first real field, MSH-2-encoding characters. It serves as the separator and defines the character to be used as a separator for the rest of the message.

VISTA Laboratory does not have pre-defined field separators. Applications are advised to use the value of this field to determine the field separator used throughout the message.

#### ENCODING CHARACTERS (ST)

This field is four characters in the following order: The component separator, repetition separator, escape character, and sub-component separator. VistA Laboratory does not have pre-defined encoding characters. Applications are advised to use the value of this field to determine the encoding characters used throughout the message.

> **NOTE:** VistA Laboratory will escape-encode those HL7 data types which support escape encoding to signal certain special characteristics of portions of the text field.

#### SENDING APPLICATION (ST)

This field is used for interfacing with lower level protocols.

> LA7LAB to identify the VistA Laboratory package.

> LA7POC# to identify the point of care system.

The character ‘#’ represents a sequential number 1-5 assigned by the site to each point of care interface installed.

#### SENDING FACILITY (ST)

This field addresses one of several occurrences of the same application within the sending system. This field is the three-digit number identifying the primary medical center division, as found in the VISTA INSTITUTION file (#4), Station Number field (#99).

#### RECEIVING APPLICATION (ST)

See sending application.

#### RECEIVING FACILITY (ST)

See sending facility.

#### DATE/TIME OF MESSAGE (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

#### MESSAGE TYPE (CM)

MESSAGE TYPE is a composite element made up of the following:

\<message type\> \<trigger event\>

The first component is the message type, found in Table 76 - message type.

The second component is the trigger event code found in Table 3 - event type code.

The receiving system uses this field to know the data segments to recognize, and possibly the application to which to route this message.

The Laboratory POC interface requires the message and event type (when appropriate) code.

ACK – for accept acknowledgment messages

ACK^ – for application acknowledgment messages

ORU^ – for unsolicited result messages

#### MESSAGE CONTROL ID (ST)

This field is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

#### PROCESSING ID (ID)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p>This field is used to decide whether to process the message as defined in the HL7 application processing rules.</p>
<p>HL7 Table 0103 PROCESSING ID</p></td>
</tr>
<tr class="even">
<td>Value</td>
<td>Description</td>
</tr>
<tr class="odd">
<td>D</td>
<td>Debugging</td>
</tr>
<tr class="even">
<td>P</td>
<td>Production</td>
</tr>
<tr class="odd">
<td>T</td>
<td>Training</td>
</tr>
</tbody>
</table>

VistA HL7 requires this field be valued. If communicating with a production VistA system it should contains ‘P’. If communicating with a test/training VistA system it should contain ‘T’. VistA HL7 will reject messages containing a processing id not in conformance with the VistA system receiving the message.

#### VERSION ID (ID)

This field is matched by the receiving system to its own version to be sure the message is interpreted correctly.

|                           |                            |
|---------------------------|----------------------------|
| HL7 Table 0104 VERSION ID |                            |
| Value                     | Description                |
| 2.1                       | Released 2.1 March 1990    |
| 2.2                       | Released 2.2 December 1994 |
| 2.3                       | Released 2.3 May 1997      |
| 2.3.1                     | Released 2.3.1 May 1999    |
| 2.4                       | Released 2.4 November 2000 |

The VistA Laboratory POC interface requires HL7 v 2.4.

#### ACCEPT ACKNOWLEDGMENT TYPE (ID)

This field defines the conditions under which accept acknowledgments are required to be returned in response to this message.

HL7 Table 0155 ACCEPT/APPLICATION ACKNOWLEDGMENT CONDITIONS

|       |                              |
|-------|------------------------------|
| Value | Description                  |
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

#### APPLICATION ACKNOWLEDGMENT TYPE (ID)

This field defines the conditions under which application acknowledgments are required in response to this message.

HL7 Table 155 ACCEPT/APPLICATION ACKNOWLEDGMENT CONDITIONS

|       |                              |
|-------|------------------------------|
| Value | Description                  |
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

#### Segment: NTE - Laboratory Notes and Comments

The NTE segment is used to report the Laboratory notes or comments.

|     |     |     |       |          |      |      |                             |
|-----|-----|-----|-------|----------|------|------|-----------------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME                |
| 1   | 4   | SI  | O     | O        |      |      | SET ID - NOTES AND COMMENTS |
| 2   | 8   | ID  | O     | O        |      | 0105 | SOURCE OF COMMENT           |
| 3   | 64k | FT  | O     | O        | Y    |      | COMMENT                     |

#### NTE field definitions

#### SET ID - NOTES AND COMMENTS (SI)

This field may be used where multiple NTE segments are included in a message.

#### SOURCE OF COMMENT (ID)

Definition: This field is used when source of comment must be identified. Refer to *HL7 Table 0105 - Source of comment* for valid values.

#### COMMENT (FT)

This field contains the comment. This information will be stored in VISTA LAB DATA file (#63), CHEM, HEM, TOX, RIA, SER, etc. Subfile (#63.04), Comment field (# .99). VISTA Laboratory prefers identifying performing laboratories using OBX-15 Producer’s ID.

#### Segment: OBR - Observation Request

In the reporting of clinical data, the OBR serves as the report header. It identifies the observation set represented by the following observations.

|     |     |     |       |          |      |      |                              |
|-----|-----|-----|-------|----------|------|------|------------------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME                 |
| 1   | 4   | SI  | C     | R        |      |      | SET ID - OBSERVATION REQUEST |
| 2   | 75  | CM  | C     | C        |      |      | PLACER ORDER NUMBER          |
| 3   | 75  | CM  | R     | C        |      |      | FILLER ORDER NUMBER          |
| 4   | 200 | CE  | R     | R        |      |      | UNIVERSAL SERVICE ID         |
| 7   | 26  | TS  | R     | R        |      |      | OBSERVATION DATE/TIME        |
| 15  | 300 | CM  | O     | R        |      | 0070 | SPECIMEN SOURCE              |
| 16  | 60  | CN  | O     | C        | Y    |      | ORDERING PROVIDER            |

#### OBR field definitions

#### SET ID - OBSERVATION REQUEST (SI)

SET ID - OBSERVATION REQUEST is a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

#### PLACER ORDER NUMBER (CM)

PLACER ORDER NUMBER is a composite element made up of the following:

\<unique filler ID\> \<filler application ID\>

This field is a permanent identifier for an order and it’s associated observations.

#### FILLER ORDER NUMBER (CM)

FILLER ORDER NUMBER is a composite element made up of the following:

\<unique filler ID\> \<filler application ID\>

This field is a permanent identifier for an order and its associated observations on the filler’s system.

#### UNIVERSAL SERVICE ID (CE)

UNIVERSAL SERVICE ID is a coded element made up of the following:

\<identifier\> \<text\> \<name of coding system\> \<alternate identifier\> \<alternate text\> \<name of alternate coding system\>

This field is an identifier code for the observation or ordered test. The WKLD CODE file (#64), specifically the Order NLT code is used to identify the observed test.

\<NLT order code File \#64 Field \#1\>^\<text\>^\<99VA64\>^\<alt id\>^\<text\>^\<alt code scheme\>

#### OBSERVATION DATE/TIME (TS)

The OBSERVATION DATE/TIME is the clinically relevant date/time of the observation. This is the actual date and time of the specimen collection.

#### SPECIMEN SOURCE

The SPECIMEN SOURCE will contain the information on the specimen source.

Components: \<specimen source name or code\>^\<additives\>^\<freetext\>^\<body site\>^\<site modifier\>^\<collection method modifier code\>

The specimen source component will contain six sub-components:

\<code from HL7 Table 0070\>&\<text\>&\<HL70070\>^

The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061) and are placed in the first three sub-components. The 2<sup>nd</sup> sub-component text will contain the Table 0070 description. The 3<sup>rd</sup> sub-component will contain the HL7 table identifier

#### ORDERING PROVIDER (CN)

ORDERING PROVIDER is a composite ID number and name made up of the following:

\<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\> \<prefix\> \<degree\> \<source table \>

This field identifies the provider who ordered the test. The ID code and the name must be present. ID number should be the internal entry number of the provider in the VistA NEW PERSON file (#200), aka DUZ.

If this field is not valued then VISTA will attempt to determine the patient’s ordering provider using:

- If inpatient then patient’s inpatient primary care provider/attending
- If outpatient then primary outpatient encounter provider or primary outpatient provider.

3.5.5. Segment: OBX - Observation

The OBX segment is used to transmit a single observation or observation fragment.

|     |       |     |       |          |      |      |                              |
|-----|-------|-----|-------|----------|------|------|------------------------------|
| SEQ | LEN   | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME                 |
| 1   | 4     | SI  | O     | O        |      |      | SET ID – OBX                 |
| 2   | 3     | ID  | R     | R        |      | 0125 | VALUE TYPE                   |
| 3   | 250   | CE  | R     | R        |      |      | OBSERVATION IDENTIFIER       |
| 5   | 65536 |     | O     | R        |      |      | OBSERVATION VALUE            |
| 6   | 250   | CE  | O     | C        |      |      | UNITS                        |
| 7   | 60    | ST  | O     | C        |      |      | REFERENCE RANGES             |
| 8   | 5     | IS  | O     | C        |      | 0078 | ABNORMAL FLAGS               |
| 11  | 1     | ID  | R     | R        |      | 0085 | OBSERV RESULT STATUS         |
| 14  | 26    | TS  | O     | C        |      |      | DATE/TIME OF THE OBSERVATION |
| 15  | 250   | CE  | O     | R        |      |      | PRODUCER’S ID                |
| 16  | 250   | XCN | O     | R        |      |      | RESPONSIBLE OBSERVER         |
| 17  | 250   | CE  | O     | O        |      |      | OBSERVATION METHOD           |
| 18  | 22    | EI  | O     | R        |      |      | EQUIPMENT INSTANT IDENTIFIER |
| 19  | 26    | TS  | O     | O        |      |      | DATE/TIME OF ANALYSIS        |

#### OBX field definitions

#### SET ID - OBSERVATION SIMPLE (SI)

SET ID - OBSERVATION SIMPLE is a sequence number used to identify the segment repetitions.

#### VALUE TYPE (ID)

This field is the format of the observation value in OBX.

|                           |                    |     |
|---------------------------|--------------------|-----|
| HL7 Table 0125 VALUE TYPE |                    |     |
| Value                     | Description        |     |
| CE                        | Coded Entry        |     |
| FT                        | Formatted Text     |     |
| NM                        | Numeric            |     |
| SN                        | Structured Numeric |     |
| ST                        | String Data        |     |
| TX                        | Text               |     |

Although there are other entries in the HL7 table, only the above values are transmitted or accepted by VistA.

#### OBSERVATION IDENTIFIER (CE)

OBSERVATION IDENTIFIER is a coded element made up of the following:

If result is coded using LOINC then LOINC will be the coding system and VA NLT the alternate coding system.

\<LOINC CODE\> \<text\> \<LN\> \<NLT CODE\> \<text\> \<99VA64\>

Otherwise the field will be encoded using the VA NLT code with a local/other system code as alternate.

\<NLT or WKLD CODE\> \<text\> \<99VA64\> \<alternate identifier\> \<alternate text\> \<name of alternate coding system

This field is a unique identifier for the observation test results. The results codes are stored in the WKLD CODE file (#64), WKLD Code field (#1). Each test result in the VistA LABORATORY TEST file (#60) is mapped using the Result NLT Code field (#64.1) to a National Laboratory Test Code in the VistA WKLD CODE file (#64). The result is processed using the LOINC or NLT (WKLD) code and is linked on the VistA system using the UI Test Code field (#6) in the VistA AUTO INSTRUMENT file (#62.4).

#### OBSERVATION VALUE (ST)

This field is the value observed by the observation producer. The length of this field is variable, depending upon the value type.

#### UNITS (CE)

UNITS is a coded element made up of the following:

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The default coding system for UNITS consists of the ISO abbreviations as defined in section 7.1.4 of the HL7 Standard V. 2.4. The identifier component is the only component being used at this time.

#### REFERENCE RANGE (ST)

The REFERENCE RANGE will contain the identified range for this specific result.

#### ABNORMAL FLAG (ID)

The ABNORMAL FLAG will contain the entries identified by table 0078.

HL7 Table 0078 - VALUE TYPE

|                                         |                                                                                               |
|-----------------------------------------|-----------------------------------------------------------------------------------------------|
| Value                                   | Description                                                                                   |
| L                                       | Below low normal                                                                              |
| H                                       | Above high normal                                                                             |
| LL                                      | Below lower panic limits                                                                      |
| HH                                      | Above upper panic limits                                                                      |
| \<                                      | Below absolute low-off instrument scale                                                       |
| \>                                      | Above absolute high-off instrument scale                                                      |
| N                                       | Normal (applies to non-numeric results)                                                       |
| A                                       | Abnormal (applies to non-numeric results)                                                     |
| AA                                      | Very abnormal (applies to non-numeric results, analogous to panic limits for numeric results) |
| Null                                    | No range defined, or normal ranges don’t apply                                                |
| U                                       | Significant change up                                                                         |
| D                                       | Significant change down                                                                       |
| B                                       | Better—use when direction not relevant                                                        |
| W                                       | Worse—use when direction not relevant                                                         |
| For microbiology susceptibilities only: |                                                                                               |
| S                                       | Susceptible                                                                                   |
| R                                       | Resistant                                                                                     |
| I                                       | Intermediate                                                                                  |
| MS                                      | Moderately susceptible                                                                        |
| VS                                      | Very susceptible                                                                              |

This field reflects the current completion status of the results for one OBSERVATION IDENTIFIER.

HL7 Table 0085 - OBSERVATION RESULT STATUS CODES INTERPRETATION

|       |                                                                                              |
|-------|----------------------------------------------------------------------------------------------|
| Value | Description                                                                                  |
| C     | Record coming over is a correction and thus replaces a final result                          |
| D     | Deletes the OBX record                                                                       |
| F     | Final results; can only be changed with a corrected result                                   |
| I     | Specimen in lab; results pending                                                             |
| N     | Not asked                                                                                    |
| O     | Order detail description only (no result)                                                    |
| P     | Preliminary results                                                                          |
| R     | Results entered – not verified                                                               |
| S     | Partial results                                                                              |
| X     | Results cannot be obtained for this observation                                              |
| U     | Results status change to final without retransmitting results already sent as ‘preliminary’. |
| W     | Post original as wrong                                                                       |

#### DATE/TIME OF THE OBSERVATION (TS)

The observation date-time is the physiologically relevant date-time or the closest approximation to that date-time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

#### PRODUCER’S ID (CE)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains a unique identifier of the responsible producing service. It should be reported explicitly when the test results are produced at outside laboratories, for example. When this field is null, the receiving system assumes that the observations were produced by the sending organization. This information supports CLIA regulations in the US. The code for producer ID is recorded as a CE data type.

Required to be transmitted and should be the VA station number of the facility producing the result. It is found in the VistA INSTITIUTION file (#4), STATION NUMBER field (#99).

#### #### RESPONSIBLE OBSERVER (XCN)

Components: In Version 2.3 and later, use instead of the CN data type. \<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility ID: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Required, this field contains the identifier of the individual directly responsible for the observation (i.e., the person who either performed or verified it). The code for the observer is recorded as a CE data type.

ID number should be the internal entry number of the individual in the VistA NEW PERSON file (#200), aka DUZ.

#### OBX-17 Observation method (CE) 00936

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

This optional field can be used to transmit the method or procedure by which an observation was obtained when the sending system wishes to distinguish among one measurement obtained by different methods and the distinction is not implicit in the test ID.

VistA will accept this field with the related methodology associated with the result from WKLD SUFFIX CODES file (#64.2).

\<WKLD SUFFIX CODE\> \<text\> \<99VA64_2 \> \<alternate identifier\> \<alternate text\> \<name of alternate coding system

#### OBX-18 EQUIPMENT INSTANT IDENTIFIER (EI)

Components: \<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field identifies the Equipment Instance (e.g., Analyzer, Analyzer module, group of Analyzers) responsible for the production of the observation.

Point of care vendors required to transmit with results.

#### Segment: ORC - Common Order

The ORC segment is used by all applications as the primary means of communicating specific lab order information. This segment contains data items that are common to all orders.

|     |     |     |       |          |      |      |                     |
|-----|-----|-----|-------|----------|------|------|---------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME        |
| 1   | 2   | ID  | R     | R        |      | 0119 | ORDER CONTROL       |
| 2   | 22  | EI  | C     | C        |      |      | PLACER ORDER NUMBER |
| 3   | 22  | EI  | C     | C        |      |      | FILLER ORDER NUMBER |
| 5   | 2   | ID  | O     | O        |      | 0038 | ORDER STATUS        |
| 7   | 2OO | TQ  | O     | O        |      |      | QUANTITY/TIMING     |
| 12  | 250 | XCN | O     | C        |      |      | ORDERING PROVIDER   |
| 13  | 80  | PL  | O     | C        |      |      | ENTERER’S LOCATION  |

3.5.6.0 ORC field definitions

3.5.6.1 ORDER CONTROL (SI)

ORDER CONTROL is the value that determines the function of the order segment. The contents are hard coded with “NW” for order messages and “RE” for result messages for messages originating from VistA.

Point of care vendors should indicate “NW” when no lab order exists on VistA. “RE” when an order exists on VistA.

3.5.6.7. QUANTITY/TIMING (TQ)

The QUANTITY/TIMING contains the information concerning the duration and priority of certain tests, same as OBR-27 except will reflect the highest urgency of tests on the order.

3.5.6.12 ORDERING PROVIDER (CN)

This is the person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field is also repeated in OBR-16.

Id number should be the internal entry number of the provider in the VistA NEW PERSON file (#200), aka DUZ.

If this field is not valued then VistA will attempt to determine the patient’s ordering provider using:

- If inpatient then patient’s inpatient primary care provider/attending
- If outpatient then primary outpatient encounter provider or primary outpatient provider.

3.5.6.13 ENTERER’S LOCATION (PL)

Components: \<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<person location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> ^ \<location description (ST)\>

Subcomponents of facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

Point of care is the inpatient or outpatient location of the patient. It can be valued with the internal entry number or abbreviation of the location from the VistA HOSPTIAL LOCATION file (#44). If this field is not valued then VistA will attempt to determine the patient’s inpatient location as of the date/time of the observation. If outpatient then clinic location of nearest valid clinic appointment on the day of the observation. If invalid or otherwise unable to determine then the message will be rejected.

The facility is the station number found in the VistA INSTITIUTION file (#4), STATION NUMBER field (#99). If valued and is not associated with the patient’s inpatient/outpatient location then VistA will reject the message.

#### Segment: PID - Patient Identification

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that is not likely to change frequently.

|     |     |     |       |          |      |      |                         |
|-----|-----|-----|-------|----------|------|------|-------------------------|
| SEQ | LEN | DT  | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME            |
| 1   | 4   | SI  | O     | O        |      |      | SET ID - PID            |
| 3   | 250 | CX  | R     | R        | Y    |      | PATIENT IDENTIFIER LIST |
| 5   | 250 | XPN | R     | C        | Y    |      | PATIENT NAME            |
| 7   | 26  | TS  | O     | O        |      |      | DATE OF BIRTH           |
| 19  | 16  | ST  | O     | O        |      |      | SSN NUMBER - PATIENT    |

PID field definitions

3.5.7.1 PID-1 SET ID - PID (SI)

SET ID - PID is a sequence number used to identify the segment repetitions.

3.5.7.3 PID-3 PATIENT IDENTIFIER LIST (CX)

PATIENT IDENTIFIER is an extended composite element made up of the following:

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD)^ \<effective date (DT)\> ^ \<expiration date (DT)\>

Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

VistA will accept VA Integration Control Number (ICN) and/or Social Security Number (SSN) in this field.

3.5.7.5 PATIENT NAME (XPN)

Components: In Version 2.3, replaces the PN data type. \<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

Definition: This field contains the names of the patient; the primary or legal name of the patient is reported first.

3.5.7.7 DATE OF BIRTH (TS)

This field is the patient’s date and time of birth.

3.5.7.8 SEX (ID)

This field is the patient’s sex. Although there are other entries in the HL7 table, only the following values are transmitted.

|                      |                |
|----------------------|----------------|
| HL7 Table 0001 – SEX |                |
| Value                | Description    |
| F                    | Female         |
| M                    | Male           |
| N                    | Not Applicable |
| A                    | Ambiguous      |
| O                    | Other          |
| U                    | Unknown        |

### Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### General

> VistA receives ORU result messages that are acknowledged with an ACK commit acknowledgment and an ACK application acknowledgment.

#### Specific Transactions

#### <u>A. Result Message</u>

ORU Observational Results Unsolicited Message

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td>Message Header</td>
</tr>
<tr class="even">
<td>{PID</td>
<td>Patient Identification</td>
</tr>
<tr class="odd">
<td>{ORC</td>
<td>Order Common</td>
</tr>
<tr class="even">
<td>OBR</td>
<td>Observations Report ID</td>
</tr>
<tr class="odd">
<td>{[NTE]}</td>
<td>Laboratory Note or Comment</td>
</tr>
<tr class="even">
<td>{OBX</td>
<td>Observation Segment</td>
</tr>
<tr class="odd">
<td>{[NTE]}</td>
<td>Laboratory Note or Comment</td>
</tr>
<tr class="even">
<td>}</td>
<td></td>
</tr>
<tr class="odd">
<td>}</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>}</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

Example POC result message:

MSH\|^~\\\|LA7POC99\|170\|LA7LAB\|170\|20040707114606\|\|ORU^R01\|040621114606:01:0101@305398\|T\|2.4\|\|\|AL\|AL\|\|\|\|

PID\|\|\|999999999^^^170^SS\|\|LRpatient^One\|\|19550502000000\|M\|\|\|\|\|\|\|\|\|\|1006926423V927391\|\|\|\|\|\|\|\|\|\|\|\|

ORC\|NW\|\|\|\|\|\|\|\|\|1177\|\|181^LRPROVIDER^ONE\|14^5 NORTH^^170\|\|\|\|\|UJ32018960\|

OBR\|\|\|305399\|82115.0000^Glucose POC^99VA64\|\|\|200408080014\|\|\|\|\|\|\|\|BLDA^Blood arterial^

HL70070 \|181^LRPROVIDER^ONE\|\|\|\|Roche HQ\|UJ32018960\|\|\|\|\|\|\|\|\|\|\|\|\|1177\|\|\|\|\|\|\|\|\|

OBX\|\|ST\|14743-9^GLUCOSE:SCNC:PT:BLDC:QN:GLUCOMETER^LN^82115.0000

^Glucose POC^99VA64\|\|416\|mg/dl\|65-115\|H\|\|\|F\|\|\|\|170^Dallas Office of Information Field Office^99VA4\|235^LRUSER^ONE \|\|^^UJ32018960^Roche GTS/HQ/Inform\|200408080014

NTE\|\|\|Provider Notified~Patient Treated~No Venous Draw per MD

ORC\|NW\|\|\|\|\|\|\|\|\|1177\|\|181^LRPROVIDER^ONE\|14^5 NORTH^^170\|\|\|\|\|UJ32018960\|

OBR\|\|\|305399\|82884.0000^Blood Gas POC^99VA64\|\|\|200408080014\|\|\|\|\|\|\|\|BLDA^Blood arterial^

HL70070 \|181^LRPROVIDER^ONE\|\|\|\|Roche HQ\|UJ32018960\|\|\|\|\|\|\|\|\|\|\|\|\|1177\|\|\|\|\|\|\|\|\|

NTE\|\|\|CPB Applied: No

OBX\|\|ST\|2744-1^PH: SCNC: PT:BLDA: QN^LN^81248.0000^pH^99VA64\|\|7.49\|units\|7.35-7.45\|H\|\|\|F\|\|\|\|170^Dallas Office of Information Field Office^99VA4\|235^LRUSER^ONE\|

\|^^UJ32018960^Roche GTS/HQ/Inform\|200408080014

OBX\|\|ST\|2703-7^OXYGEN:PPRES:PT:BLDA:QN^LN^82880.0000^PO2 Direct Reading^99VA642\|\|156\|mm Hg\|75-100\|H\|\|\|F\|\|\|\|170^Dallas Office of Information Field Office^99VA4\|235^LRUSER^ONE\|\|^^UJ32018960^Roche GTS/HQ/Inform\|200408080014

NTE\|\|\| Provider Notified

OBX\|\|ST\|2019-8^CARBON DIOXIDE:PPRES:PT:BLDA:QN^LN^82820.0000^PCO2 Direct Reading

^99VA64\|\|46\|mm Hg\|34-40\|H\|\|\|F\|\|\|\|170^Dallas Office of Information Field Office^99VA4

\|235^LRUSER^ONE\|\|^^UJ32018960^Roche GTS/HQ/Inform\|200408080014

OBX\|\|ST\|1960-4^BICARBONATE:SCNC:PT:BLDA:QN^LN^81216.0000^Bicarbonate^99VA64\|\|36\|

mmol/L\|22-33\|H\|\|\|F\|\|\|\|170^Dallas Office of Information Field Office^99VA4\|235^

LRUSER^ONE\|\|^^UJ32018960^Roche TS/HQ/Inform\|200408080014

#### <u>B. Message Acknowledgment</u>

VistA supports enhanced mode acknowledgments. Upon receipt of the result message, the VistA HL7 package responds with an ACK message for the commit acknowledgment and the VistA Laboratory system responds with a general acknowledgment (ACK) message for the application acknowledgment. The ACK message consists of the following segments.

ACK General Acknowledgment Message

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MSH</td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MSA</td>
<td><blockquote>
<p>Message Acknowledgment</p>
</blockquote></td>
</tr>
</tbody>
</table>

MSA-2 Message Control ID will contain the message control ID of the ORU message being acknowledged.

MSA-3 Text Message will contain either of the following:

- If MSA-1 Acknowledgment Code is AA then MSA-3 will contain the accession’s UID assigned to the result by the VistA Laboratory system.
- If MSA-1 Acknowledgement Code is AE then MSA-3 will contain an error message.

Example:

MSH\|^~\\\|LA7LAB\|528\|LA7POC1\|528\|20040820081620-0400\|\|ACK\|528199776706\|P\|2.4

MSA\|CA\|040820082059:01:0101@336942

MSH\|^~\\\|LA7LAB\|528\|LA7POC1\|528\|20040130101855-0400\|\|ACK^\|528140676975

\|P\|2.4\|AL\|NE\|

MSA\|AA\|031022161321:01:0101@171527\|M532950106\|

MSH\|^~\\\|LA7LAB\|528\|LA7POC1\|528\|20040820081623-0400\|\|ACK^R01\|528199776709\|P\|2.4

\|\|\|AL\|NE\|

MSA\|AE\|040820082059:01:0101@336942\|Msg \#13755103, No valid provider found for order.\|

### Communication Requirements for HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section specifies the requirements necessary to establish and maintain communications between VistA and all the participating systems. It includes requirements to be satisfied by VistA, by all the participating systems, and by each system when sending or receiving a message.

Utilizing TCP/IP and HL7 Minimal Lower Level Protocol (MLLP).

The interface between VistA and each participating system is established via a persistent or a transient (non-persistent) TCP/IP connection. Two TCP sockets provide bi-directional communications between each participating system.

Within the context of the TCP socket, each participating system will connect as the client when it initiates a message. The other system will connect as the server to receive messages from the listen state.

## #### Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The participating system shall initiate the interface by establishing a TCP Server Socket.

The participating system that initiates a message shall connect to the participating system TCP Server Socket as a TCP Client.

#### TCP/IP Connections:

VistA has a client (sender) and a server (listener) process to each remote system for sending and receiving HL7 messages. Each of these processes requires a TCP socket. The client process sends HL7 messages (including Application Acknowledgment messages) to the remote system and receives Accept Acknowledgment messages from the remote system. The server process receives HL7 messages (including Application Acknowledgment messages) from the remote system and sends Accept Acknowledgment messages to the remote system. Figure 4.1 depicts the sequence of events for an inbound and an outbound message regarding messages and acknowledgments.

![Figure 4.1 Acknowledgements](la-5-2-67-lr-5-2-290-laboratory-poc-hl7-interface-specifications-document/002.png)

*Figure 4.1 Acknowledgements*

#### Flow Control:

This interface uses the HL7 Minimal Lower Layer Protocol to format messages for data interchange, including acknowledgement messages. This protocol relies on the Message Header (MSH) Segment to define encoding, routing and acknowledgement rules governing the message.

#### VistA Client/Server Process Parameters:

The flow of messages between VistA and the POC system can be controlled by the VistA client/server process parameters. The parameters for the client/server process are definable at each installation site and can be customized for each POC system. The followings are examples of some of the parameters:

- Server IP addresses/ports
- Client IP addresses/ports
- Number of attempts to open a socket
- Hang time for the client process between attempts to send a message
- Maximum number of times the client process will attempt to send a message
- Persistent/non-persistent client connection
- Retention time for client connection to keep a non-persistent connection established.

#### Automated Recovery Procedure:

Should either side of the interface be disabled for any reason during any TCP connection, the other side will begin its automatic recovery procedures.

Specifically, if the POC system (TCP server) detects that VistA (TCP client) becomes disabled, the POC system will reset to “listen” mode. If VistA detects that the POC system becomes disabled, VistA will reset to “attempt connect” state. VistA will continue to attempt the reconnect for a site specified number of times or for a site-specified period of time before logging the situation and terminating.

#### Message Transmission Retry Attempts:

When the POC system is down and VistA cannot transmit a message to the POC system, VistA will wait for a specified period of time (defaults to one minute) before attempting to re-send the message. VistA will retry until the specified maximum number of attempts (defaults to 2) is reached.

## #### Error Management:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA and the POC system will use automated procedures to detect when connectivity has been lost and to initiate recovery procedures. VistA and the POC system will use the HL7 2.4 enhanced acknowledgement mode, so the receiving system may respond to the message with an Accept Acknowledgement, an Application Acknowledgement, or both. When the receiving system commits the message to safe storage in a manner that releases the sending system from the need to retransmit the message, it sends a positive Accept Acknowledgement. When the receiving system has processed the message, it sends an Application Acknowledgement to return the resultant status to the sending system.

Accept Acknowledgements will be used for all messages and the value passed in the Accept Acknowledgement field of the MSH segment (MSH-15) of the originating message will be observed. Application Acknowledge­ments will be used in accordance with the value passed in the Application Acknowledgement Type field of the MSH segment (MSH-16) of the originating message.

### ### Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\(1\) If VistA detects a remote end disconnect, it shall attempt to reconnect to the POC system TCP Server Socket for a locally defined number of Retry Attempts.

\(2\) If VistA detects a remote end disconnect and is unable to reconnect to the POC system after locally defined number of Retry Attempts, it shall log an error.

\(3\) If the POC system detects a remote end disconnect, it shall close that channel of its TCP Server Socket and await VistA reconnection.

\(4\) The Receiving system shall return an Accept Acknowledgement with a Commit Accept (CA) status to the Sending System for each incoming HL7 Message in which the Message Header Segment (MSH) conforms to the following criteria:

- The first segment is a Message Header Segment (MSH);
- The Field Separator (MSH-1) is valued.
- The Encoding characters (MSH-2) are valued.
- The Sending Application field (MSH-3) contains the values LA7LAB or LA7POCn as appropriate.
- The Sending Facility field (MSH-4) contains the VA stations number of the primary VA facility hosted on the VISTA system.
- The Receiving Application field (MSH-5) contains the values LA7LAB or LA7POCn as appropriate.
- The Receiving Facility field (MSH-6) contains the VA stations number of the primary VA facility hosted on the VISTA system
- The Date/time Message (MSH-7) is valued.
- The Message Type Field (MSH-9) contains a valid message and event (when appropriate) type.
- The Message Control ID Field (MSH-10) contains an ID.
- The Processing ID (MSH-11) contains a valid ID.
- The Version ID (MSH-12) contains 2.4.
- The Accept Acknowledgment Type (MSH-15) indicates a valid acknowledgment condition.
- The Application Acknowledgment Type (MSH-16) contains a valid acknowledgment condition.

\(5\) The Receiving system shall return an Accept Acknowledgement with a Commit Reject (CR) status to the Sending System for each incoming HL7 Message in which the Message Header Segment (MSH) fails to conform to the criteria in \#4 above.

\(6\) The Receiving system shall return an Accept Acknowledgement with a Commit Error (CE) status to the Sending System for each incoming HL7 Message that it has not accepted for any reasons other than those requiring a Commit Reject.

\(7\) Upon receipt of an Accept Acknowledgment with a Commit Error (CE) status from the Receiving System, the Sending System shall institute appropriate notification actions.

\(8\) The Receiving System shall return an Application Acknowledgement to the Sending System for each incoming HL7 Message in which the Application Acknowledgement Type Field of the MSH Segment (MSH-16) is set to “AL”