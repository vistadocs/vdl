---
title: "Laboratory: Universal Interface HL V1.6 Upgrade Interface Specifications Document"
doc_type: INT
doc_label: Interface Specification
doc_layer: anchor
doc_subject: Upgrade s Document
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "LA::1.6"
file_numbers: []
security_keys: []
menu_options: 4
description: > ![](laboratory-universal-interface-hl-v1-6-upgrade-interface-specifications-document/001.png)
audience: 
keywords: 
  - blockquote
  - class
  - strong
  - table
  - style
  - width
  - bookmark
  - span
  - even
  - contents
page_count: 0
word_count: 13195
section_count: 12
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labui_hlv1_6_interfacespecificationsdocument.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labui_hlv1_6_interfacespecificationsdocument.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

> ![](laboratory-universal-interface-hl-v1-6-upgrade-interface-specifications-document/001.png)

> LABORATORY UNIVERSAL INTERFACE (UI)

> HEALTH LEVEL (HL) V1.6 UPGRADE

> INTERFACE SPECIFICATIONS DOCUMENT

> PATCH LA\*5.2\*88

> Version 5.2

> July 2016

> Department of Veterans Affairs

> VistA Health Systems Design & Development

> Revision

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>07/13/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.15</p>
</blockquote></td>
<td><blockquote>
<p>Updated cover page, inserted page numbers in the footer and completed updates for PATCH LA*5.2*88</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6/21/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.14</p>
</blockquote></td>
<td><blockquote>
<p>Fixed OBX 17 Header</p>
<p>Updated Data Types for 2.5.1 MSH, PID, PVI, ORC, OBR, OBX, NTE</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5/10/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.13</p>
</blockquote></td>
<td><blockquote>
<p>Added more detailed description of the message communication transmission and contents.</p>
<p>Changed/added sections in 4 and 5 to define and explain message flow and interface behavior.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5/10/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.12</p>
</blockquote></td>
<td><blockquote>
<p>Corrected section 3.3 to add ORR, Corrected section 3.4 to add ERR, corrected sections</p>
<p>3.5.2.15 and 3.5.2.16 to reflect enhanced mode not original mode.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5/3/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.11</p>
</blockquote></td>
<td><blockquote>
<p>Corrected ORM ORR Message Example</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5/3/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.10</p>
</blockquote></td>
<td><blockquote>
<p>Added example for ORM ACK Messages</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5/2/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.09</p>
</blockquote></td>
<td><blockquote>
<p>Added updated ACK Message and ERR Segment</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/23/2015</p>
</blockquote></td>
<td><blockquote>
<p>1.08</p>
</blockquote></td>
<td><blockquote>
<p>Peer reviewed</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/08/2015</p>
</blockquote></td>
<td><blockquote>
<p>1.07</p>
</blockquote></td>
<td><blockquote>
<p>Formatted TOC and Added the table to ORC 14 and OBR 17</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/01/2015</p>
</blockquote></td>
<td><blockquote>
<p>1.06</p>
</blockquote></td>
<td><blockquote>
<p>Initial Draft of changes for LA*5.2*88.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/17/2008</p>
</blockquote></td>
<td><blockquote>
<p>1.05</p>
</blockquote></td>
<td><blockquote>
<p>Updated NTE section with comments</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/05/2008</p>
</blockquote></td>
<td><blockquote>
<p>1.04</p>
</blockquote></td>
<td><blockquote>
<p>Updated Result message structure in 4.2.2</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/04/2008</p>
</blockquote></td>
<td><blockquote>
<p>1.03</p>
</blockquote></td>
<td><blockquote>
<p>Updated sources fields description for OBR segment. Documented NTE segment. Updated sample ORU message.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/29/2008</p>
</blockquote></td>
<td><blockquote>
<p>1.02</p>
</blockquote></td>
<td><blockquote>
<p>Updated sample ORM message, removed unused/non-supported fields</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/18/2008</p>
</blockquote></td>
<td><blockquote>
<p>1.01</p>
</blockquote></td>
<td><blockquote>
<p>ORC/OBR segments corrected</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/20/2007</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Initial Draft of changes for LA*5.2*66</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  [PURPOSE: 5](#purpose)
2.  [OVERVIEW: 5](#overview)
    1.  [Statement of Intent 5](#statement-of-intent)
    2.  [Scope 5](#scope)
3.  [GENERAL SPECIFICATIONS 6](#general-specifications)
    1.  [Communication Protocol 6](#communication-protocol)
    2.  [Application Processing Rules 6](#application-processing-rules)
    3.  [Messages 6](#messages)
    4.  [Segments 6](#segments)
    5.  [Fields 7](#fields)
        1.  [Segment: MSA - Message Acknowledgment 9](#segment-msa---message-acknowledgment)
            0.  [MSA Field Definitions 9](#bookmark11)
            1.  [ACKNOWLEDGMENT CODE (ID) 9](#bookmark12)
            2.  [MESSAGE CONTROL ID (ST) 9](#bookmark13)
            3.  [TEXT MESSAGE (ST) 9](#bookmark14)
        2.  [Segment: MSH - Message Header 10](#segment-msh---message-header)
            0.  [MSH Field Definitions 10](#bookmark16)
            1.  [FIELD SEPARATOR (ST) 10](#bookmark17)
            2.  [ENCODING CHARACTERS (ST) 10](#bookmark18)
            3.  [SENDING APPLICATION (HD) 10](#bookmark19)
            4.  [SENDING FACILITY (HD) 11](#bookmark20)
            5.  [RECEIVING APPLICATION (HD) 11](#bookmark21)
            6.  [RECEIVING FACILITY (HD) 11](#bookmark22)
            7.  [DATE/TIME OF MESSAGE (TS) 11](#bookmark23)
            8.  [SECURITY (ST) 11](#bookmark24)
            9.  [MESSAGE TYPE (MSG) 11](#bookmark25)
            11. [PROCESSING ID (PT) 12](#bookmark26)
            12. [VERSION ID (VID) 12](#bookmark27)
            15. [ACCEPT ACKNOWLEDGMENT TYPE (ID) 12](#bookmark28)
            16. [APPLICATION ACKNOWLEDGMENT TYPE (ID) 13](#bookmark29)
        3.  [Segment: ERR – Error Segment 14](#segment-err-error-segment)

[3.5.3.0 ERR Field Definitions 14](#_bookmark31)

3.  [HL7 ERROR CODE (CWE) 14](#bookmark32)
4.  [SEVERITY (ID) 15](#bookmark33)
5.  [APPLICATION ERROR CODE (CWE) 16](#bookmark34)
8.  [USER MESSAGE (TX) 17](#bookmark36)
9.  [INFORM PERSON INDICATOR (IS) 17](#bookmark37)
4.  [Segment: NTE – Laboratory Notes and Comments 19](#segment-nte-laboratory-notes-and-comments)
5.  [Segment: OBR - Observation Request 20](#segment-obr---observation-request)
    0.  [OBR Field Definitions 20](#bookmark44)
    1.  [SET ID - OBSERVATION REQUEST (SI) 20](#bookmark45)
    2.  [PLACER ORDER NUMBER (EI) 20](#bookmark46)
    3.  [FILLER ORDER NUMBER (EI) 21](#bookmark47)
    4.  [UNIVERSAL SERVICE ID (CE) 21](#bookmark48)

[3.5.5.7 OBSERVATION DATE/TIME (TS) 21](#_bookmark49)

12. [DANGER CODE (CE) 21](#_bookmark50)
13. [RELEVANT CLINICAL INFO. (ST) 21](#_bookmark51)
14. [SPECIMEN RECEIVED DATE/TIME (TS) 22](#bookmark52)
15. [SPECIMEN SOURCE (SPS) 22](#bookmark53)
16. [ORDERING PROVIDER (XCN) 22](#bookmark54)
17. [ORDER CALLBACK PHONE NUMBER (XTN) 22](#bookmark55)
6.  [Segment: OBX - Observation 25](#segment-obx---observation)
    0.  [OBX Field Definitions 26](#bookmark61)
    1.  [SET ID - OBSERVATION SIMPLE (SI) 26](#bookmark62)
    2.  [VALUE TYPE (ID) 26](#bookmark63)
    3.  [OBSERVATION IDENTIFIER (CE) 27](#bookmark64)
    5.  [OBSERVATION VALUE (ST) 27](#bookmark65)
    6.  [UNITS (CE) 27](#bookmark66)
    7.  [REFERENCE RANGE (ST) 27](#bookmark67)
    8.  [ABNORMAL FLAG (ID) 27](#bookmark68)

[3.5.6.11 OBSERV RESULT STATUS (ID) 28](#_bookmark69)

14. [DATE/TIME OF THE OBSERVATION (TS) 30](#bookmark70)
15. [PRODUCER’S REFERENCE (CE) 30](#bookmark71)
16. [RESPONSIBLE OBSERVER (XCN) 30](#bookmark72)
17. [Observation Method (CE) 31](#bookmark73)
18. [EQUIPMENT INSTANT IDENTIFIER (EI) 32](#bookmark74)
7.  [Segment: ORC - Common Order 33](#segment-orc---common-order)

[3.5.7.0 ORC Field Definitions 33](#_bookmark76)

2.  [PLACER ORDER NUMBER (EI) 33](#bookmark77)
3.  [FILLER ORDER NUMBER (EI) 33](#bookmark78)

[3.5.7.9 DATE/TIME OF TRANSACTION (TS) 34](#_bookmark79)

[3.5.7.12 ORDERING PROVIDER (XCN) 34](#_bookmark80)

8.  [Segment: PID - Patient Identification 36](#segment-pid---patient-identification)
    0.  [PID Field Definitions 36](#bookmark82)
    1.  [SET ID - (SI) 36](#bookmark83)

[3.5.8.3 PATIENT ID (CX) 36](#_bookmark84)

[3.5.8.5 PATIENT NAME (XPN) 36](#_bookmark85)

7.  [DATE OF BIRTH (TS) 36](#bookmark86)
8.  [ADMINISTRATIVE SEX (IS) 36](#bookmark87)

[3.5.8.19 SSN NUMBER - PATIENT (ST) 37](#_bookmark88)

9.  [Segment PV1 - Patient Visit 38](#segment-pv1---patient-visit)
    0.  [PV1 Field Definitions 38](#bookmark90)
    1.  [SET ID - PATIENT VISIT (SI) 38](#bookmark91)
    2.  [PATIENT CLASS (IS) 38](#bookmark92)
    3.  [ASSIGNED PATIENT LOCATION (PL) 38](#bookmark93)
4.  [TRANSACTION SPECIFICATIONS 39](#transaction-specifications)
    1.  [General 39](#general)
    2.  [Specific Transactions 39](#specific-transactions)
        1.  [Order Message (ORM) 39](#order-message-orm)

[4.2.1.2 ORM Message Acknowledgment 41](#_bookmark98)

2.  [Result Message (ORU) 41](#result-message-oru)

[4.2.2.1 ORU Message Acknowledgment 42](#bookmark100)

5.  [Communication Requirements for HL7 Interfaces 44](#communication-requirements-for-hl7-interfaces)
    1.  [Requirements 44](#requirements)
    2.  [TCP/IP Connections 44](#tcpip-connections)
    3.  [Flow Control 46](#flow-control)
    4.  [VistA Client/Server Process Parameters 46](#vista-clientserver-process-parameters)
    5.  [Automated Recovery Procedure 46](#automated-recovery-procedure)
    6.  [Message Transmission Retry Attempts 46](#message-transmission-retry-attempts)
    7.  [Error Management 46](#error-management)
        1.  [Requirements 47](#requirements-1)

> Note: Fourth level heading numbers are based on the sequence number of the elements in that table.

# PURPOSE:


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PURPOSE:](#purpose)
- [OVERVIEW:](#overview)
  - [<u>Statement of Intent</u>](#ustatement-of-intentu)
  - [<u>Scope</u>](#uscopeu)
- [GENERAL SPECIFICATIONS](#general-specifications)
  - [<u>Communication Protocol</u>](#ucommunication-protocolu)
  - [<u>Application Processing Rules</u>](#uapplication-processing-rulesu)
  - [<u>Messages</u>](#umessagesu)
  - [<u>Segments</u>](#usegmentsu)
  - [<u>Fields</u>](#ufieldsu)
    - [Segment: MSA - Message Acknowledgment](#segment-msa-message-acknowledgment)
    - [Segment: MSH - Message Header](#segment-msh-message-header)
    - [Segment: ERR – Error Segment](#segment-err-error-segment)
    - [Segment: NTE – Laboratory Notes and Comments](#segment-nte-laboratory-notes-and-comments)
    - [Segment: OBR - Observation Request](#segment-obr-observation-request)
    - [Example:](#example)
    - [Segment: OBX - Observation](#segment-obx-observation)
    - [Segment: ORC - Common Order](#segment-orc-common-order)
    - [Segment: PID - Patient Identification](#segment-pid-patient-identification)
    - [Segment PV1 - Patient Visit](#segment-pv1-patient-visit)
- [TRANSACTION SPECIFICATIONS](#transaction-specifications)
  - [General](#general)
  - [Specific Transactions](#specific-transactions)
    - [Order Message (ORM)](#order-message-orm)
    - [EXAMPLE:](#example-1)
    - [ORR General Order Acknowledgment Message](#orr-general-order-acknowledgment-message)
    - [EXAMPLE:](#example-2)
    - [Result Message (ORU)](#result-message-oru)
    - [EXAMPLE:](#example-3)
    - [EXAMPLE:](#example-4)
  - [Communication Requirements for HL7 Interfaces](#communication-requirements-for-hl7-interfaces)
    - [Requirements](#requirements)
    - [TCP/IP Connections](#tcpip-connections)
    - [Flow Control](#flow-control)
    - [VistA Client/Server Process Parameters](#vista-clientserver-process-parameters)
    - [Automated Recovery Procedure](#automated-recovery-procedure)
    - [Message Transmission Retry Attempts](#message-transmission-retry-attempts)
    - [Error Management](#error-management)
  - [<u>5.1.7.1 Requirements</u>](#u5171-requirementsu)
> This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard. The VistA Laboratory Universal Interface (UI) patch LA\*5.2\*88 forms the basis for the exchange of healthcare information between the VistA Laboratory software application and non-VistA systems, primarily laboratory automated instruments and generic instrument managers (GIMs) that receive laboratory orders and generate laboratory results information.
> The Generic Instrument Manager (GIM) is a locally procured commercial device that controls communications between the Laboratory instruments and VistA. The VistA system downloads work lists through the GIM to the various instruments, and the instruments upload results to VistA through the GIM, eliminating the need for Laboratory developers to write a new interface for each different instrument.

# OVERVIEW:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <u>Statement of Intent</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Laboratory Universal Interface (UI) patch LA\*5.2\*88 implements a generic interface to the HL7 Standard for use by the VistA Laboratory application in communicating with non- VistA systems to exchange healthcare information. The interface strictly adheres to the HL7 Standard and avoids using “Z” type extensions to the Standard. This interface specification is subject to modifications and revisions to incorporate changes, improvements, and enhancements. Later versions may support additional functionality of the current HL7 (V 2.5.1) Standard and new functionality released in future versions of the HL7 Standard.

## <u>Scope</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes messages transmitted between the VistA Laboratory application and a non-VistA automated system. The purpose of these messages is to exchange information concerning laboratory tests, specifically for orders and results related to the performance of this testing on laboratory automated instruments.

# GENERAL SPECIFICATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <u>Communication Protocol</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that are used for interfacing with the VistA Laboratory package are based on the HL7 Hybrid Lower Level Protocol which is described in the HL7 Implementation Guide.

## <u>Application Processing Rules</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 Standard describes the basic rules for application processing by the sending and receiving systems. Information contained in the Standard is not repeated here. Anyone wishing to interface with the VistA Laboratory package should become familiar with the HL7 Standard V. 2.2.

## <u>Messages</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following HL7 message types are used to support the exchange of Laboratory information: ACK General Acknowledgment

> ORM Order

> ORU Observational Results Unsolicited ORR General Order Response

## <u>Segments</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to section 4, Transaction Specifications, for details and examples of all segments used to interface with VistA Laboratory Package. The following HL7 segments are used to support the exchange of Laboratory information:

> MSA Message Acknowledgment MSH Message Header

> ERR Error

> NTE Notes and Comment OBR Observation Request OBX Observation

> ORC Common Order

> PID Patient Identification PV1 Patient Visit

## <u>Fields</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The segment definition tables list and describe the data fields in the segment and characteristics of their usage. The following information is specified about each data field.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SEQ</p>
</blockquote></td>
<td><blockquote>
<p>Sequence Number is the ordinal position of the data field within the segment. This number refers to the data field in the comments text that follows the segment definition table.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEN</p>
</blockquote></td>
<td><blockquote>
<p>Length is the maximum number of characters that one occurrence of the data field may occupy.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>Data Type identifies the restrictions on the contents of the data field as defined by the HL7 Standard.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R/O/C</p>
</blockquote></td>
<td><blockquote>
<p>R/O/C indicates whether the data field is required, optional, or conditional in a segment.</p>
<p><strong>R</strong>–required</p>
<p><strong>O</strong> (null)–optional</p>
<p><strong>X</strong>–not used with the trigger event</p>
<p><strong>C</strong>–conditional on the trigger event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA R/O/C</p>
</blockquote></td>
<td><blockquote>
<p>VA (R/O/C) indicates whether the data field is required, optional, or conditional in a segment used by the Department of Veterans Affairs (VA).</p>
<p><strong>R</strong>–required <strong>RE</strong>–required or empty <strong>O</strong> (null)–optional</p>
<p><strong>X</strong>–not used with the trigger event</p>
<p><strong>C</strong>–conditional on the trigger event</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RP/#</p>
</blockquote></td>
<td><blockquote>
<p>Repetition indicates the number of times you can repeat a field.</p>
<p><strong>N (null)</strong>–no repetition allowed</p>
<p><strong>Y</strong>–the field may repeat an indefinite or site determined number of times</p>
<p><strong>(integer)</strong>–you can repeat the field the number of times specified by the integer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TBL#</p>
</blockquote></td>
<td><blockquote>
<p>Table attribute of the data field defined by the HL7 standard (for a set of coded values) or negotiated between the VistA Laboratory application and the vendor system. Local tables used by the VA begin with the prefix <strong>99VA</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Element Name</p>
</blockquote></td>
<td><blockquote>
<p>Globally unique, descriptive name for the field</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following HL7 segment fields are used to support the exchange of Laboratory data for each of the segments listed in paragraph 3.4. Tables referenced in the segments can be found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for those fields which are utilized. The field definitions can include specific information (e.g., expected format) for transmission.

### Segment: MSA - Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MSA segment contains information sent while acknowledging another message.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>MSA</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>ACKNOWLEDGMENT CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>MESSAGE CONTROL ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TEXT MESSAGE</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark11" class="anchor"></span><u>MSA Field Definitions</u>
1.  <span id="bookmark12" class="anchor"></span><u>ACKNOWLEDGMENT CODE (ID)</u>

> The ACKNOWLEDGMENT CODE can have the following values:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>HL7 Table 8 ACKNOWLEDGMENT CODE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td><blockquote>
<p>Application Accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AE</p>
</blockquote></td>
<td><blockquote>
<p>Application Error</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AR</p>
</blockquote></td>
<td><blockquote>
<p>Application Reject</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  <span id="bookmark13" class="anchor"></span><u>MESSAGE CONTROL ID (ST)</u>

> Identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

3.  <span id="bookmark14" class="anchor"></span><u>TEXT MESSAGE (ST)</u>

> Further describes an error condition. The text may be printed in error logs or presented to an end user.

### Segment: MSH - Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>MSH</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA</strong></p>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>FIELD SEPARATOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ENCODING CHARACTERS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SENDING APPLICATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SENDING FACILITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING APPLICATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING FACILITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE/TIME OF MESSAGE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>MSG</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>76</p>
</blockquote></td>
<td><blockquote>
<p>MESSAGE TYPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>MESSAGE CONTROL ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>103</p>
</blockquote></td>
<td><blockquote>
<p>PROCESSING ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>VID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>104</p>
</blockquote></td>
<td><blockquote>
<p>VERSION ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>155</p>
</blockquote></td>
<td><blockquote>
<p>ACCEPT ACKNOWLEDGEMENT TYPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>155</p>
</blockquote></td>
<td><blockquote>
<p>APPLICATION ACKNOWLEDGEMENT TYPE</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark16" class="anchor"></span><u>MSH Field Definitions</u>
1.  <span id="bookmark17" class="anchor"></span><u>FIELD SEPARATOR (ST)</u>

> The separator between the segment ID and the first real field, MSH-2-ENCODING CHARACTERS. It serves as the separator and defines the character to be used as a separator for the rest of the message.

2.  <span id="bookmark18" class="anchor"></span><u>ENCODING CHARACTERS (ST)</u>

> Four characters in the following order: the component separator, repetition separator, escape character and subcomponent separator.

3.  <span id="bookmark19" class="anchor"></span><u>SENDING APPLICATION (HD)</u>

> Used for interfacing with lower level protocols.

> ORM uses LA7LAB

> ORU uses LA7UIx (where "x" is an integer 1-10)

4.  <span id="bookmark20" class="anchor"></span><u>SENDING FACILITY (HD)</u>

> The three-digit number identifying the medical center division, as found in the VistA INSTITUTION file (#4), STATION NUMBER field (#99). The VA station \# of the primary VistA facility should be used for all interfaces implemented at a multi-divisional/integrated VistA system.

5.  <span id="bookmark21" class="anchor"></span><u>RECEIVING APPLICATION (HD)</u>

> ORM uses LA7UIx: (where "x" is an integer 1-10) ORU uses LA7LAB

6.  <span id="bookmark22" class="anchor"></span><u>RECEIVING FACILITY (HD)</u>

> Same as sending facility.

7.  <span id="bookmark23" class="anchor"></span><u>DATE/TIME OF MESSAGE (TS)</u>

> The date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

8.  <span id="bookmark24" class="anchor"></span><u>SECURITY (ST)</u>

> In some applications of HL7 this field is used to implement security features. Its use is not yet further specified.

9.  <span id="bookmark25" class="anchor"></span><u>MESSAGE TYPE (MSG)</u>

> A composite element made up of the following:

> \<message type\> \<trigger event\>

> The first component is the message type, found in table 76 - MESSAGE TYPE. The second component is the trigger event code found in table 3 - EVENT TYPE CODE. The receiving system uses this field to know the data segments to recognize, and possibly, the application to which to route this message.

> ACK: General acknowledgment ORM~O01: Order message from VistA. ORU~R01: Result message to VistA.

> ORR~O02: General order response message response to any ORM (event O02)

10. <u>MESSAGE CONTROL ID (ST)</u>

> A number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

11. <span id="bookmark26" class="anchor"></span><u>PROCESSING ID (PT)</u>

> Used to decide whether to process the message as defined in the HL7 application processing rules.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>HL7 Table 103 PROCESSING ID</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
</tr>
<tr class="even">
<td>D</td>
<td><blockquote>
<p>Debugging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>Production</p>
</blockquote></td>
</tr>
<tr class="even">
<td>T</td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

12. <span id="bookmark27" class="anchor"></span><u>VERSION ID (VID)</u>

> Matched by the receiving system to its own version to be sure the message is interpreted correctly. Only the following values are expected/accepted: 2.5.1

15. <span id="bookmark28" class="anchor"></span><u>ACCEPT ACKNOWLEDGMENT TYPE (ID)</u>

> Defines the conditions under which accept acknowledgments are required to be returned in response to this message.

> HL7 Table 155 Accept/Application Acknowledgment Conditions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AL</p>
</blockquote></td>
<td><blockquote>
<p>Always</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>Never</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ER</p>
</blockquote></td>
<td><blockquote>
<p>Error/reject conditions only</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SU</p>
</blockquote></td>
<td><blockquote>
<p>Successful completion only</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This interface uses HL7 “enhanced mode” acknowledgements.

> Messages originating from VistA Laboratory will have this field valued “AL”.

16. <span id="bookmark29" class="anchor"></span><u>APPLICATION ACKNOWLEDGMENT TYPE (ID)</u>

> Defines the conditions under which application acknowledgments are required to be returned in response to this message.

> HL7 Table 155 Accept/Application Acknowledgment Conditions

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AL</p>
</blockquote></td>
<td><blockquote>
<p>Always</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>Never</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ER</p>
</blockquote></td>
<td><blockquote>
<p>Error/reject conditions only</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SU</p>
</blockquote></td>
<td><blockquote>
<p>Successful completion only</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This interface uses HL7 “enhanced mode” acknowledgements.

> Messages originating from VistA Laboratory will have this field valued “AL”.

### Segment: ERR – Error Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ERR segment is used to add error comments to acknowledgment messages when receiving ORU Result Messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEQ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>LEN</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>OPT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RP/#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ITEM #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>493</p>
</blockquote></td>
<td><blockquote>
<p>ELD</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00024</p>
</blockquote></td>
<td><blockquote>
<p>ERROR CODE AND LOCATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>ERL</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01812</p>
</blockquote></td>
<td><blockquote>
<p>ERROR LOCATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>705</p>
</blockquote></td>
<td><blockquote>
<p>CWE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0357</p>
</blockquote></td>
<td><blockquote>
<p>01813</p>
</blockquote></td>
<td><blockquote>
<p>HL7 ERROR CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0516</p>
</blockquote></td>
<td><blockquote>
<p>01814</p>
</blockquote></td>
<td><blockquote>
<p>SEVERITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>705</p>
</blockquote></td>
<td><blockquote>
<p>CWE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0533</p>
</blockquote></td>
<td><blockquote>
<p>01815</p>
</blockquote></td>
<td><blockquote>
<p>APPLICATION ERROR CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y/10</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01816</p>
</blockquote></td>
<td><blockquote>
<p>APPLICATION ERROR PARAMETER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>2048</p>
</blockquote></td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>01817</p>
</blockquote></td>
<td><blockquote>
<p>DIAGNOSTIC INFORMATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>01818</p>
</blockquote></td>
<td><blockquote>
<p>USER MESSAGE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td><blockquote>
<p>0517</p>
</blockquote></td>
<td><blockquote>
<p>01819</p>
</blockquote></td>
<td><blockquote>
<p>INFORM PERSON INDICATOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>705</p>
</blockquote></td>
<td><blockquote>
<p>CWE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0518</p>
</blockquote></td>
<td><blockquote>
<p>01820</p>
</blockquote></td>
<td><blockquote>
<p>OVERRIDE TYPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>705</p>
</blockquote></td>
<td><blockquote>
<p>CWE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td><blockquote>
<p>0519</p>
</blockquote></td>
<td><blockquote>
<p>01821</p>
</blockquote></td>
<td><blockquote>
<p>OVERRIDE REASON CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>652</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01822</p>
</blockquote></td>
<td><blockquote>
<p>HELP DESK CONTACT POINT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark31" class="anchor"></span><u>3.5.3.0 ERR Field Definitions</u>

3.  <span id="bookmark32" class="anchor"></span><u>HL7 ERROR CODE (CWE)</u>

> Components: \<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\> ^

> \<Coding System Version ID (ST)\> ^ \<Alternate Coding System Version ID (ST)\> ^ \<Original Text (ST)\>

> Implementation Example: ERR-3 = 207^Application internal error^HL70357

> Definition: Identifies the HL7 (communications) error code. Refer to *[<u>HL7 Table 0357 –</u>](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70357)* [*<u>Message Error Condition Codes</u>*](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70357) for valid values.

> HL7 Table 0357 - Message error condition codes

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>Message accepted</p>
</blockquote></td>
<td><blockquote>
<p>Success. Optional, as the AA conveys success. Used for systems that must always return a status code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>Segment sequence</p>
</blockquote></td>
<td><blockquote>
<p>Error: The message segments were not in the proper</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>error</p>
</blockquote></td>
<td><blockquote>
<p>order, or required segments are missing.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>101</p>
</blockquote></td>
<td><blockquote>
<p>Required field missing</p>
</blockquote></td>
<td><blockquote>
<p>Error: A required field is missing from a segment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>Data type error</p>
</blockquote></td>
<td><blockquote>
<p>Error: The field contained data of the wrong data type,</p>
<p>e.g. an NM field contained "FOO".</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>103</p>
</blockquote></td>
<td><blockquote>
<p>Table value not found</p>
</blockquote></td>
<td><blockquote>
<p>Error: A field of data type ID or IS was compared against the corresponding table, and no match was found.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>Unsupported message type</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The Message Type is not supported.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td><blockquote>
<p>Unsupported event code</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The Event Code is not supported.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>Unsupported processing id</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The Processing ID is not supported.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td><blockquote>
<p>Unsupported version id</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The Version ID is not supported.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>204</p>
</blockquote></td>
<td><blockquote>
<p>Unknown key identifier</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The ID of the patient, order, etc., was not found. Used for transactions <em>other than</em> additions, e.g. transfer of a non-existent patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td><blockquote>
<p>Duplicate key identifier</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>206</p>
</blockquote></td>
<td><blockquote>
<p>Application record locked</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: The transaction could not be performed at the application storage level, e.g., database locked.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>207</p>
</blockquote></td>
<td><blockquote>
<p>Application internal error</p>
</blockquote></td>
<td><blockquote>
<p>Rejection: A catchall for internal errors not explicitly covered by other codes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  <span id="bookmark33" class="anchor"></span><u>SEVERITY (ID)</u>

> Definition: Identifies the severity of an application error. Knowing if something is Error, Warning or Information is intrinsic to how an application handles the content. Refer to *[<u>HL7</u>](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70516)* [*<u>Table 0516 - Error severity</u>*](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70516) for valid values. If ERR-3 has a value of "0", ERR-4 will have a value of "I".

> HL7 Table 0516 – Error severity

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 41%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Warning</p>
</blockquote></td>
<td><blockquote>
<p>Transaction successful, but there may issues</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>Information</p>
</blockquote></td>
<td><blockquote>
<p>Transaction was successful</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 41%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>but includes information e.g., inform patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td><blockquote>
<p>Transaction was unsuccessful</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Implementation Example: ERR-4 = E

5.  <span id="bookmark34" class="anchor"></span><u>APPLICATION ERROR CODE (CWE)</u>

> Components: \<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\> ^

> \<Coding System Version ID (ST)\> ^ \<Alternate Coding System Version ID (ST)\> ^ \<Original Text (ST)\>

> Definition: Application specific code identifying the specific error that occurred. Refer to *[<u>User-</u>](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70533)* [*<u>Defined Table 0533 – Application Error Code</u>*](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70533) for suggested values.

> If the message associated with the code has parameters, it is recommended that the message be indicated in the format of the java .text.MessageFormat approach[\[1\]](#_bookmark35). This style provides information on the parameter type to allow numbers, dates and times to be formatted appropriately for the language.

> User-defined Table 0533 – Application error code

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 36%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>301</p>
</blockquote></td>
<td><blockquote>
<p>301 Msg #|1|, User |2| [DUZ: |3|] does not own the LRVERIFY security key.</p>
<p>Auto Release not allowed for accession UID |4|.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>302</p>
</blockquote></td>
<td><blockquote>
<p>302 Msg #|1|, User |2| [DUZ: |3|] is not an active user on the system. Auto</p>
<p>Release not allowed for accession UID |4|.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>303</p>
</blockquote></td>
<td><blockquote>
<p>303 Msg #|1|, No verifying user or application proxy found. Auto Release not allowed for accession UID</p>
<p>|2|.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark35" class="anchor"></span>\[1\] Details on Message Format can be found at

> [*http://java.sun.com/products/jdk/1.2/docs/api/java/text/MessageFormat.html*.](http://java.sun.com/products/jdk/1.2/docs/api/java/text/MessageFormat.html)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 36%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>304</p>
</blockquote></td>
<td><blockquote>
<p>304 Msg #|1|, User |2| [DUZ: |3|] is not a valid user to verify results. Auto Release not allowed for accession UID |4|.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>305</p>
</blockquote></td>
<td><blockquote>
<p>305 Msg #|1|, User |2| [DUZ: |3|] is not allowed to verify. Only auto verification enabled for this instrument. Auto Release not allowed for accession UID |4|.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>306</p>
</blockquote></td>
<td><blockquote>
<p>306 Msg #|1|, User |2| [DUZ: |3|] is not allowed to verify. Only tech verification enabled for this instrument. Auto Release not allowed for accession UID |4|.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>307</p>
</blockquote></td>
<td><blockquote>
<p>307 Msg #|1|, Auto Release not allowed for accession UID |2|. Results have previously been released.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Implementation Example: ERR-5 = 307^Msg \#30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.^99VA62.485

8.  <span id="bookmark36" class="anchor"></span><u>USER MESSAGE (TX)</u>

> Definition: The text message to be displayed to the application user. This differs from the actual error code and may provide more diagnostic information.

> Implementation Example: ERR-8 = Msg \#30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.

9.  <span id="bookmark37" class="anchor"></span><u>INFORM PERSON INDICATOR (IS)</u>

> Definition: A code to indicate who (if anyone) should be informed of the error. This field may also be used to indicate that a particular person should NOT be informed of the error (e.g. Do

> not inform patient). Refer to [*<u>User-defined table 0517- Inform Person Code</u>*](http://vaww.infoshare.va.gov/hpmo/SEIW/SEI_TRM/HL7_Public/Standard%20Specifications/hl7%202-5-1/V251_CH02.doc#HL70517) for suggested values.

> User-defined Table 0517 – Inform person code

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 36%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PAT</p>
</blockquote></td>
<td><blockquote>
<p>Inform patient</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NPAT</p>
</blockquote></td>
<td><blockquote>
<p>Do NOT inform patient</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USR</p>
</blockquote></td>
<td><blockquote>
<p>Inform User</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>Inform help desk</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Implementation Example: ERR-9 = USR

### Segment: NTE – Laboratory Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NTE segment is used to report the Laboratory notes or comments.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEQ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>LEN</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA</strong></p>
<p><strong>R/O/C</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RP/#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - NOTES AND COMMENTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0105</p>
</blockquote></td>
<td><blockquote>
<p>SOURCE OF COMMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>64k</p>
</blockquote></td>
<td><blockquote>
<p>FT</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark39" class="anchor"></span><u>3.5.4.0 NTE Field Definitions</u>

> <span id="_bookmark40" class="anchor"></span><u>3.5.4. 1 SET ID - NOTES AND COMMENTS (SI)</u>

> This field may be used where multiple NTE segments are included in a message.

> <span id="_bookmark41" class="anchor"></span><u>3.5.4.2 SOURCE OF COMMENT (ID)</u>

> Definition: This field is used when source of comment must be identified. This table may be extended locally during implementation. Refer to HL7 Table 0105 - Source of comment for valid values.

> HL7 Table 0105 - Source of comment

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 57%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
<th><blockquote>
<p>Comment</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>Ancillary (filler) department is source of comment</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p>Orderer (placer) is source of comment</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Other system is source of comment</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark42" class="anchor"></span><u>3.5.4.3. COMMENT (FT)</u>

> This field contains the comment associated with the specimen and/or a specific test.

> Comments generated by automated instruments that relate to the specimens can be transmitted by the external GIM following the OBR segment.

> Comments generated by automated instruments that relate to specific results can be transmitted by the external GIM following the OBX segment.

### Segment: OBR - Observation Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the reporting of clinical data, the OBR serves as the report header. It identifies the observation set represented by the following observations.

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>OBR</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O</strong></p>
<p><strong>/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - OBSERVATION REQUEST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>75</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACER ORDER NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>75</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FILLER ORDER NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>UNIVERSAL SERVICE ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>OBSERVATION DATE/TIME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0065</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMEN ACTION CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>DANGER CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>RELEVANT CLINICAL INFO.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>SPECIMEN RECEIVED DATE/TIME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>SPS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0070</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMEN SOURCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>XC N</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ORDERING PROVIDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y/2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ORDER CALLBACK PHONE NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACER FIELD #1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACER FIELD #2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>27</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>TQ</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>QUANTITY/TIMING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>49</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0507</p>
</blockquote></td>
<td><blockquote>
<p>RESULT HANDLING</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark44" class="anchor"></span><u>OBR Field Definitions</u>
1.  <span id="bookmark45" class="anchor"></span><u>SET ID - OBSERVATION REQUEST (SI)</u>

> A sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

2.  <span id="bookmark46" class="anchor"></span><u>PLACER ORDER NUMBER (EI)</u>

> A composite element made up of the following:

> \<unique filler ID\> \<filler application ID\>

> This field is a permanent identifier for an order and its associated observations. Currently the first component is filled in with the VistA unique accession number. This number is carried throughout the VistA testing cycle and returned with the results.

> This field contains either the accession number component of the accession or the 10 character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68) TYPE OF ACCESSION NUMBER field (#.092).

3.  <span id="bookmark47" class="anchor"></span><u>FILLER ORDER NUMBER (EI)</u>

> A composite element made up of the following:

> \<unique filler ID\> \<filler application ID\>

> This field contains either the accession number component of the accession or the 10 character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68) TYPE OF ACCESSION NUMBER field (#.092). This number is then returned with the results.

4.  <span id="bookmark48" class="anchor"></span><u>UNIVERSAL SERVICE ID (CE)</u>

> A coded element made up of the following:

> \<identifier\> \<text\> \<name of coding system\> \<alternate identifier\> \<alternate text\> \<name of alternate coding system\>

> This field is an identifier code for the observation or ordered test. This can be based on local and/or universal codes.

> The WKLD CODE file \#64 is used to identify the observed test and is indicated as the Order NLT. The UI Test code is the test code mapped via AUTO INSTRUMENT file (#62.4), CHEM TESTS sub file (#62.41), UI TEST CODE field (#6). This UI Test Code is usually the instrument specific code recognized by the automated instrument to perform the requested test.

> \<UI test code\>^\<text\>^\<99001\>^\<Order NLT\>^\<text\>^\<99VA64\><span id="_bookmark49" class="anchor"></span> <u>3.5.5.7 OBSERVATION DATE/TIME (TS)</u>

> The clinically relevant date/time of the observation. This is the actual date and time of the specimen collection. This data is pulled from the ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), DRAW TIME field (#9).

> <span id="_bookmark50" class="anchor"></span><u>3.5.5.12 DANGER CODE (CE)</u>

> Contains the information located within the LAB DATA file (#63), PAT.INFO field (#.091).<span id="_bookmark51" class="anchor"></span> <u>3.5.5.13 RELEVANT CLINICAL INFO. (ST)</u>

> Contains the information located within the ACCESSION file (#68), ACCESSION NUMBER sub file (68.02), COMMENT field (#13.6).

14. <span id="bookmark52" class="anchor"></span><u>SPECIMEN RECEIVED DATE/TIME (TS)</u>

> The actual time of a specimen's arrival at the diagnostic service. The lab arrival time from VistA ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), LAB ARRIVAL TIME

> field (#12).

15. <span id="bookmark53" class="anchor"></span><u>SPECIMEN SOURCE (SPS)</u>

> Contains the information on the specimen source.

> Components: \<specimen source name or code (CE)\>^\<\>^\<free text\>^\<\>^\<\>

> The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061) and are placed in the first three sub-components. The VistA TOPOGRAPHY FIELD file (#61) is mapped to corresponding entry in LAB ELECTRONIC CODES file (#64.061). The 2<sup>nd</sup> sub-component text will contain the Table 0070 description. The 3<sup>rd</sup> sub- component will contain the HL7 table identifier. The four through six sub-components will contain the local topography file entry. The 4<sup>th</sup> sub-component contains the internal entry number of the specimen’s relate entry in TOPOGRAPHY FIELD file (#61). The 5<sup>th</sup> component contains the text of the topography entry and the 6<sup>th</sup> component contains “99VA61” as the coding system. The 3<sup>rd</sup> component free text will contain the value “CONTROL” when the specimen is related to an entry in LAB CONTROL NAME file (#62.3).

16. <span id="bookmark54" class="anchor"></span><u>ORDERING PROVIDER (XCN)</u>

> A composite ID number and name made up of the following:

> \<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\> \<prefix\>

> \<degree\> \<source table\>

> This field identifies the provider who ordered the test. The ID code and the name may be present.

> Internal entry number of ordering provider in NEW PERSON file (#200) concatenated with “- VA” and VA station number is used as the id number.

17. <span id="bookmark55" class="anchor"></span><u>ORDER CALLBACK PHONE NUMBER (XTN)</u>

> Components: \<DEPRECATED-Telephone Number (ST)\> ^ \<Telecommunication Use Code (ID)\> ^\<Telecommunication Equipment Type (ID)\> ^ \<Email Address (ST)\> ^ \<Country Code (NM)\> ^ \<Area/City Code (NM)\> ^ \<Local Number (NM)\> ^ \<Extension (NM)\> ^ \<Any Text (ST)\> ^ \<Extension Prefix (ST)\> ^ \<Speed Dial Code (ST)\> ^ \<Unformatted Telephone number (ST)\>

> Definition: This field contains the telephone number for reporting a status or a result using the standard format with extension and/or beeper number when applicable.

> VistA values components based on the ordering provider’s NEW PERSON file \#200 entry using the following components:

> \#2 Telecommunication Use Code (ID) = WPN

> \#3 Telecommunication Equipment Type (ID) = PH or BP

> \#9 Any Text (ST) = VistA NEW PERSON file (#200) source field

> OFFICE PHONE (#.132)

> VOICE PAGER (#.137)

> DIGITAL PAGER (#.138)

> \#12 Unformatted Telephone number (ST) = phone or beeper number

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field #</p>
</blockquote></th>
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field Description</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 2:</p>
<p>Telecommunic ation Use Code</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 3:</p>
<p>Telecommun ication Equipment Type</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 9:</p>
<p>Any Text</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 12:</p>
<p>Unformatted Telephone number</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.131</p>
</blockquote></td>
<td><blockquote>
<p>PHONE (HOME)</p>
</blockquote></td>
<td><blockquote>
<p>This is the telephone number for the new person.</p>
</blockquote></td>
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE (HOME) (#.131)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.132</p>
</blockquote></td>
<td><blockquote>
<p>OFFICE PHONE</p>
</blockquote></td>
<td><blockquote>
<p>This is the business/office telephone for the new person.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>OFFICE PHONE (#.132)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.133</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #3</p>
</blockquote></td>
<td><blockquote>
<p>This is an alternate telephone number where</p>
<p>the new person might also be reached.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #3</p>
<p>(#.133)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.134</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #4</p>
</blockquote></td>
<td><blockquote>
<p>This is another alternate telephone number where the new person might also be reached.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #4</p>
<p>(#.134)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.135</p>
</blockquote></td>
<td><blockquote>
<p>COMMER CIAL PHONE</p>
</blockquote></td>
<td><blockquote>
<p>This is a commercial phone number</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>COMMERCI AL PHONE (#.135)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.136</p>
</blockquote></td>
<td><blockquote>
<p>FAX NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for a FAX machine for this user. It needs to be a format that can be</p>
<p>understood by a sending MODEM.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>FAX NUMBER (#.136)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.137</p>
</blockquote></td>
<td><blockquote>
<p>VOICE PAGER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for an ANALOG PAGER that this person carries with them.</p>
</blockquote></td>
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>VOICE PAGER (#.137)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.138</p>
</blockquote></td>
<td><blockquote>
<p>DIGITAL PAGER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for a DIGITAL PAGER that this person</p>
<p>carries with them.</p>
</blockquote></td>
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>DIGITAL PAGER (#.138)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

> A maximum of two repetitions will be encoded in the field of the possible eight fields which are site selectable.

### Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|

18. <u>PLACER FIELD \#1 (ST)</u>

> This field contains vital information for the processing of incoming results. The field contains the name of the auto-instrument from the AUTO INSTRUMENT file (#62.4), NAME field (#.01).

> The data should be passed in the following format:

> \<Name of Analyzer or Instrument\>^\<Card Address\>

19. <span id="bookmark56" class="anchor"></span><u>PLACER FIELD \#2 (ST)</u>

> Contains vital information for linking the incoming result with the original order. The data should be passed in the following format:

> \<Tray\>^\<Cup\>^\<Accession Area\>^\<Accession Date\>^\<Accession Number\>^\<Accession\>^\<Universal ID\>^\<Sequence Number\>

> All components are optional except the Universal ID which should match with the PLACER ORDER NUMBER.

> <span id="_bookmark57" class="anchor"></span><u>3.5.5.22 RESULTS REPORT/STATUS CHANGE - DATE/TIME (TS)</u>

> Contains the date and time the report is released.

> <span id="_bookmark58" class="anchor"></span><u>3.5.5.27 QUANTITY/TIMING (TQ)</u>

> Contains the information concerning the timing and urgency of certain tests.

> VistA values the 6<sup>th</sup> component priority with the related test urgency from VistA ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), TESTS field (#11) sub file (#68.04), URGENCY OF TEST field (#1).

> <span id="_bookmark59" class="anchor"></span><u>3.5.5.49 RESULT HANDLING (IS)</u>

> Definition: Transmits information regarding the handling of the result. For example, an order may specify that the result (e.g., an x-ray film) should be given to the patient for return to the requestor. Refer to *<u>User-defined Table 0507 Observation Result Handling</u>* for suggested values. If this field is not populated, then routine handling is implied.

> User-defined Table 0507 – Observation Result Handling

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
<th><blockquote>
<p>Comment</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AR</p>
</blockquote></td>
<td><blockquote>
<p>Auto release</p>
</blockquote></td>
<td><blockquote>
<p>Indicates that results when contained in an ORU message should be processed through the VistA Lab Auto Release process.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VistA – when valued in an ORU message the results contained in the message will be processed through the VistA Laboratory Auto Release process. This field is used in conjunction with OBX.16 and OBX.17 to determine the type of verification and the responsible user.

### Segment: OBX - Observation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The OBX segment is used to transmit a single observation or observation fragment.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th colspan="6"><blockquote>
<p><strong>OBX</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>L E N</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/ C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA</strong></p>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - OBSERVATION SIMPLE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td>R</td>
<td></td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td><blockquote>
<p>VALUE TYPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>OBSERVATION IDENTIFIER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>var</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>OBSERVATION VALUE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>22</p>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>UNITS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>REFERENCE RANGES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>C</td>
<td></td>
<td><blockquote>
<p>0078</p>
</blockquote></td>
<td><blockquote>
<p>ABNORMAL FLAGS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td>R</td>
<td></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
<td><blockquote>
<p>OBSERV RESULT STATUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE/TIME OF THE</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>OBSERVATION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>48</p>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PRODUCER’S REFERENCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>25</p>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td>C</td>
<td></td>
<td></td>
<td><blockquote>
<p>RESPONSIBLE OBSERVER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>25</p>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td>C</td>
<td></td>
<td></td>
<td><blockquote>
<p>OBSERVATION METHOD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>C</td>
<td></td>
<td></td>
<td><blockquote>
<p>EQUIPMENT INSTANT IDENTIFIER</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark61" class="anchor"></span><u>OBX Field Definitions</u>
1.  <span id="bookmark62" class="anchor"></span><u>SET ID - OBSERVATION SIMPLE (SI)</u>

> A sequence number used to identify the segment repetitions.

2.  <span id="bookmark63" class="anchor"></span><u>VALUE TYPE (ID)</u>

> This field is the format of the observation value in OBX.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>HL7 Table 0125 VALUE TYPE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Coded Entry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CNE</p>
</blockquote></td>
<td><blockquote>
<p>Coded with no exceptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FT</p>
</blockquote></td>
<td><blockquote>
<p>Formatted Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>Numeric</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SN</p>
</blockquote></td>
<td><blockquote>
<p>Structured Numeric</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>String Data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Although there are other entries in the HL7 table, only the above values are supported by VistA.

3.  <span id="bookmark64" class="anchor"></span><u>OBSERVATION IDENTIFIER (CE)</u>

> A coded element made up of the following:

> \<NLT or WKLD CODE\> \<text\> \<99VA64\> \<alternate identifier\> \<alternate text\> \<name of alternate coding system\>

> This field is a unique identifier for the observation test results. The UI Test code is the test code mapped via AUTO INSTRUMENT file (#62.4), CHEM TESTS sub file (#62.41), UI TEST CODE field (#6). This UI Test Code is usually the instrument specific code recognized by the automated instrument to perform and report the requested test.

> \<UI test code\>^\<text\>^\<99001\>

5.  <span id="bookmark65" class="anchor"></span><u>OBSERVATION VALUE (ST)</u>

> The value observed by the observation producer. The length of this field is variable, depending upon the value type.

6.  <span id="bookmark66" class="anchor"></span><u>UNITS (CE)</u>

> If OBR 49 contains AR, then this field is required when the observation in OBX-5 has associated units

7.  <span id="bookmark67" class="anchor"></span><u>REFERENCE RANGE (ST)</u>

> The field contains the identified range for this specific result.

> If OBR 49 contains AR, then this field is required when the observation in OBX-5 has associated reference ranges.

8.  <span id="bookmark68" class="anchor"></span><u>ABNORMAL FLAG (ID)</u>

> This field contains the entries identified by table 0078.

> If OBR 49 contains AR, then this field is required when the observation in OBX-5 has associated abnormal flags.

> HL7 Table 0078 – Value Type

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 66%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA Usage</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>Below low normal</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p>Above high normal</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LL</p>
</blockquote></td>
<td><blockquote>
<p>Below lower panic limits</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 66%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA Usage</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HH</p>
</blockquote></td>
<td><blockquote>
<p>Above upper panic limits</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>&lt;</p>
</blockquote></td>
<td><blockquote>
<p>Below absolute low-off instrument scale</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>&gt;</p>
</blockquote></td>
<td><blockquote>
<p>Above absolute high-off instrument scale</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>Normal (applies to non-numeric results)</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>Abnormal (applies to non-numeric results)</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td><blockquote>
<p>Very abnormal (applies to non-numeric results, analogous to panic limits for numeric results)</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Null</p>
</blockquote></td>
<td><blockquote>
<p>No range defined, or normal ranges don’t apply</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Significant change up</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Significant change down</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Better—use when direction not relevant</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Worse—use when direction not relevant</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><strong>For microbiology susceptibilities only</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>Susceptible</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Resistant</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>Intermediate</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS</p>
</blockquote></td>
<td><blockquote>
<p>Moderately susceptible</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VS</p>
</blockquote></td>
<td><blockquote>
<p>Very susceptible</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark69" class="anchor"></span><u>3.5.6.11 OBSERV RESULT STATUS (ID)</u>

> This field reflects the current completion status of the results for one OBSERVATION IDENTIFIER.

> Hl7 Table 0085 - Observation Result Status Codes Interpretation

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 74%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA Usage</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Record coming over is a correction and thus replaces a final result</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Deletes the OBX record</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>Final results; can only be changed with a corrected result</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>Specimen in lab; results pending</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>Not asked</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Order detail description only (no result)</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p>Preliminary results</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Results entered – not verified</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>Partial results</p>
</blockquote></td>
<td><blockquote>
<p>Used</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 74%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>X</p>
</blockquote></th>
<th><blockquote>
<p>Results cannot be obtained for this observation</p>
</blockquote></th>
<th><blockquote>
<p>Used</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Results status change to final without retransmitting results already sent as ‘preliminary’.</p>
</blockquote></td>
<td><blockquote>
<p>Not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Post original as wrong</p>
</blockquote></td>
<td><blockquote>
<p>Not Used</p>
</blockquote></td>
</tr>
</tbody>
</table>

14. <span id="bookmark70" class="anchor"></span><u>DATE/TIME OF THE OBSERVATION (TS)</u>

> The physiologically relevant date-time or the closest approximation to that date-time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

15. <span id="bookmark71" class="anchor"></span><u>PRODUCER’S REFERENCE (CE)</u>

> If OBR 49 = AR, then send this field.

16. <span id="bookmark72" class="anchor"></span><u>RESPONSIBLE OBSERVER (XCN)</u>

> When required, this field contains the identifier of the individual directly responsible for the observation (such as, the person who performed or verified the observation).

1.  In a nursing service, the observer is usually the professional who performed the observation (such as, took the blood pressure).
2.  In a laboratory, the observer is the technician who performed or verified the analysis.

> The code for the observer is recorded as a CE data type. If the code is sent as a local code, it must be unique and unambiguous when combined with OBX-15-producer ID. When available, the code is transmitted with results.

> Components

> \<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

> Subcomponents of assigning authority

> \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> Subcomponents of assigning facility ID

> \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS, and the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

1.  When the responsible observer is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA, and the identifier type code (thirteenth component) contains PN.
2.  If there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted, concatenated with -VA and the VA station number.

> The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

> VistA when OBR.49 indicates AR (auto release) and OBX.17 indicates the appropriate WKLD suffixes will use OBX.16 to determine the responsible observer based on the following table:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OBX.17 Identifier</p>
</blockquote></th>
<th><blockquote>
<p>OBX.16 Value</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.9750</p>
</blockquote></td>
<td><blockquote>
<p>ID of VistA application proxy LRLAB, AUTO VERIFY</p>
<p>|nnn-VAsss^LRLAB^AUTO^VERIFY^^^99VA4|</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.9760</p>
</blockquote></td>
<td><blockquote>
<p>ID of person verifying /releasing results on middleware.</p>
<p>|nnn-VAsss^LRUSER^TWO^^^^99VA4|</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Where nnn = the DUZ (internal record number) of the application proxy or user in VistA NEW PERSON file (#200)

> Where sss = the associated VA station number assigned to the VistA facility in VistA INSTITUTION file (#4)

> Example:

> \|101053-VA500^LRUSER^TWO^^^^99VA4\|

> \|101099-VA500^LRLAB^AUTO^VERIFY^^^99VA4\|

17. <span id="bookmark73" class="anchor"></span><u>Observation Method (CE)</u>

> Use this optional field to transmit the method or procedure by which an observation is obtained when the sending system needs to distinguish a measurement obtained by different methods where the distinction is not implicit in the test ID.

> Components

> \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

> VistA values this field, when available, with the related methodology associated with the result from WKLD SUFFIX CODES file (#64.2).

> \<WKLD SUFFIX CODE\> \<text\> \<99VA64_2 \> \<alternate identifier\> \<alternate text\> \<name of alternate coding system

> VistA uses this field in conjunction with OBR.49 RESULT HANDLING. When OBR.49 contains “AR” then VistA will process the results through the VistA Laboratory Auto Release system. OBX.17 should

> contain either of the following WKLD Suffixes to identify the results as being produced by an external (middleware) system’s auto verification process or user/tech verification on the middleware system.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 51%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Identifier</p>
</blockquote></th>
<th><blockquote>
<p>Text</p>
</blockquote></th>
<th><blockquote>
<p>Name of Coding System</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.9750</p>
</blockquote></td>
<td><blockquote>
<p>AUTO VERIFY, MIDDLEWARE</p>
</blockquote></td>
<td><blockquote>
<p>99VA64_2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.9760</p>
</blockquote></td>
<td><blockquote>
<p>TECH VERIFY, MIDDLEWARE</p>
</blockquote></td>
<td><blockquote>
<p>99VA64_2</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example:

> \|.9750^AUTO VERIFY, MIDDLEWARE^99VA64_2\|

> \|.9760^TECH VERIFY, MIDDLEWARE^99VA64_2\|

18. <span id="bookmark74" class="anchor"></span><u>EQUIPMENT INSTANT IDENTIFIER (EI)</u>

> This field identifies the Equipment Instance (such as, Analyzer, Analyzer module, group of Analyzers) responsible for the production of the observation.

> Components

> \<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

> VistA Laboratory values this field with the information and in the form originally transmitted by the automated instrument that produced the result

### Segment: ORC - Common Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The primary means of communicating specific lab order information. This segment contains data items that are common to all orders.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>ORC</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0119</p>
</blockquote></td>
<td><blockquote>
<p>ORDER CONTROL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACER ORDER NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>FILLER ORDER NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Date/time of TRANSACTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ORDERING PROVIDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Y/2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CALL BACK PHONE NUMBER</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark76" class="anchor"></span><u>3.5.7.0 ORC Field Definitions</u>

> The value that determines the function of the order segment. The contents are hard coded with “NW” for order messages and “RE” for result messages for messages originating from VistA.

> ORM message will contain “NW”. ORU message will contain “RE”.

2.  <span id="bookmark77" class="anchor"></span><u>PLACER ORDER NUMBER (EI)</u>

> The placer application’s order number, which should be returned with the result message. Components: \<unique placer ID\>^\<placer application ID\>

> This field contains either the accession number component of the accession or the 10 character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68), TYPE OF ACCESSION NUMBER field (#.092).

3.  <span id="bookmark78" class="anchor"></span><u>FILLER ORDER NUMBER (EI)</u>

> The filler application’s order number.

> Components: \<unique placer ID\>^\<placer application ID\>

> This field contains either the accession number component of the accession or the 10 character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68), TYPE OF ACCESSION NUMBER field (#.092).

> <span id="_bookmark79" class="anchor"></span><u>3.5.7.9 DATE/TIME OF TRANSACTION (TS)</u>

> Date ordered. VistA values this field with the related date ordered from VistA ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), DATE ORDERED field (#3).

> <span id="_bookmark80" class="anchor"></span><u>3.5.7.12 ORDERING PROVIDER (XCN)</u>

> The person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field is also repeated in OBR-16.

> Internal entry number of ordering provider in NEW PERSON file (#200) concatenated with “- VA” and VA station number is used as the id number.

> <u>3.5.7.14 CALL BACK PHONE NUMBER (XTN)</u>

> Components: \<DEPRECATED-Telephone Number (ST)\> ^ \<Telecommunication Use Code (ID)\> ^\<Telecommunication Equipment Type (ID)\> ^ \<Email Address (ST)\> ^ \<Country Code (NM)\> ^ \<Area/City Code (NM)\> ^ \<Local Number (NM)\> ^ \<Extension (NM)\> ^ \<Any Text (ST)\> ^ \<Extension Prefix (ST)\> ^ \<Speed Dial Code (ST)\> ^ \<Unformatted Telephone number (ST)\>

> Definition: This field contains the telephone number to call for clarification of a request or other information regarding the order. ORC-14-call back phone number is the same as OBR-17-order callback phone number.

> VistA values components based on the ordering provider’s NEW PERSON file \#200 entry using the following components:

> \#2 Telecommunication Use Code (ID) = WPN

> \#3 Telecommunication Equipment Type (ID) = PH or BP

> \#9 Any Text (ST) = VistA NEW PERSON file (#200) source field

> OFFICE PHONE (#.132)

> VOICE PAGER (#.137)

> DIGITAL PAGER (#.138)

> \#12 Unformatted Telephone number (ST) = phone or beeper number

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field #</p>
</blockquote></th>
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>VistA NEW PERSON</p>
<p>Field Description</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 2:</p>
<p>Telecommun ication Use Code</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 3:</p>
<p>Telecommu nication Equipment Type</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 9:</p>
<p>Any Text</p>
</blockquote></th>
<th><blockquote>
<p>HL7 SEQ 12:</p>
<p>Unformatted Telephone number</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.131</p>
</blockquote></td>
<td><blockquote>
<p>PHONE (HOME)</p>
</blockquote></td>
<td><blockquote>
<p>This is the telephone number for the new person.</p>
</blockquote></td>
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE (HOME) (#.131)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.132</p>
</blockquote></td>
<td><blockquote>
<p>OFFICE PHONE</p>
</blockquote></td>
<td><blockquote>
<p>This is the business/office telephone for the new person.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>OFFICE PHONE (#.132)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.133</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #3</p>
</blockquote></td>
<td><blockquote>
<p>This is an alternate telephone number where the new person might also</p>
<p>be reached.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #3</p>
<p>(#.133)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.134</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #4</p>
</blockquote></td>
<td><blockquote>
<p>This is another alternate telephone number where</p>
<p>the new person might also be reached.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>PHONE #4</p>
<p>(#.134)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.135</p>
</blockquote></td>
<td><blockquote>
<p>COMMER CIAL PHONE</p>
</blockquote></td>
<td><blockquote>
<p>This is a commercial phone number</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>COMMERCIAL PHONE (#.135)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.136</p>
</blockquote></td>
<td><blockquote>
<p>FAX NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for a FAX machine for this user. It needs to be a format that can be</p>
<p>understood by a sending MODEM.</p>
</blockquote></td>
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>FAX NUMBER (#.136)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.137</p>
</blockquote></td>
<td><blockquote>
<p>VOICE PAGER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for an ANALOG PAGER that this person carries with them.</p>
</blockquote></td>
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>VOICE PAGER (#.137)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.138</p>
</blockquote></td>
<td><blockquote>
<p>DIGITAL PAGER</p>
</blockquote></td>
<td><blockquote>
<p>This field holds a phone number for a DIGITAL PAGER that this person</p>
<p>carries with them.</p>
</blockquote></td>
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>DIGITAL PAGER (#.138)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;actual number&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|

### Segment: PID - Patient Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that is not likely to change frequently.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>PID</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - PATIENT ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PATIENT ID (INTERNAL ID)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>XPN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE OF BIRTH</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ADMINISTRATIVE SEX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SSN NUMBER - PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark82" class="anchor"></span><u>PID Field Definitions</u>
1.  <span id="bookmark83" class="anchor"></span><u>SET ID - (SI)</u>

> A sequence number used to identify the segment repetitions.<span id="_bookmark84" class="anchor"></span> <u>3.5.8.3 PATIENT ID (CX)</u>

> Vista Laboratory supports multiple “patient” types - both PATIENT file (#2) and other human and non-human patients. To insure a consistent “patient” identifier the internal entry number (LRDFN) of the “patient” in LAB DATA file (#63) is used.

> <span id="_bookmark85" class="anchor"></span><u>3.5.8.5 PATIENT NAME (XPN)</u>

> Standard HL7 format.

7.  <span id="bookmark86" class="anchor"></span><u>DATE OF BIRTH (TS)</u>

> The patient’s date of birth.

8.  <span id="bookmark87" class="anchor"></span><u>ADMINISTRATIVE SEX (IS)</u>

> The patient’s sex. Although there are other entries in the HL7 table, only the following values are transmitted.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>HL7 Table 1 - SEX</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>F</p>
</blockquote></th>
<th><blockquote>
<p>Female</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Male</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark88" class="anchor"></span><u>3.5.8.19 SSN NUMBER - PATIENT (ST)</u>

> The patient’s social security number.

### Segment PV1 - Patient Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Used to communicate information on a visit specific basis.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="7"><blockquote>
<p><strong>PVI</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><blockquote>
<p><strong>LEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA R/O/C</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>TBL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - PATIENT VISIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0004</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT CLASS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ASSIGNED PATIENT LOCATION</p>
</blockquote></td>
</tr>
</tbody>
</table>

0.  <span id="bookmark90" class="anchor"></span><u>PV1 Field Definitions</u>
1.  <span id="bookmark91" class="anchor"></span><u>SET ID - PATIENT VISIT (SI)</u>

> The number uniquely identifying this transaction.

2.  <span id="bookmark92" class="anchor"></span><u>PATIENT CLASS (IS)</u>

> Categorizes the patient by site. VA facilities will presently code either “I” – inpatient or “O” – outpatient.

3.  <span id="bookmark93" class="anchor"></span><u>ASSIGNED PATIENT LOCATION (PL)</u>

> Uses the current inpatient location from PATIENT file (#2), WARD LOCATION field (#.1). Otherwise the current report routing location as designated in the VistA LAB DATA file (#63), REPORT ROUTING (LOCATION) field (#.1).

# TRANSACTION SPECIFICATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA requires enhanced mode acknowledgments. See section 3.5.2.9 Message Type above for specifics.

> VistA sends ORM order messages that are acknowledged with an ACK commit acknowledgment and an ORR application acknowledgment.

> VistA receives ORU result messages that are acknowledged with an ACK commit acknowledgment and an ACK application acknowledgment.

## Specific Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Order Message (ORM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORM General Order Message

> MSH Message Header

> { PID Patient Identification

> \[PV1\] Patient Visit

> { ORC Common Order

> OBR Observations Report ID

> }

> }

### EXAMPLE:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MSH\|^~\\\|LA7LAB\|500\|LA7UI1\|500\|20150702123702- 0400\|\|ORM^O01\|500286\|P\|2.5.1\|\|\|AL\|AL\|USA

> PID\|1\|\|2^7^M11\|\|TEST^NEW^PATIENT^ZZ\|\|19220101\|F\|\|\|\|\|\|\|\|\|\|\|567-01-0122P PV1\|1\|O\|TC1

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|1\|CH51830005\|CH51830005\|01A^SODIUM^99001^176^SODIUM^99VA60\|\|\|20150702123658- 0400\|\|\|\|\|\|\|201507021237-0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053- VA500^LRUSER^TWO^^^^^99VA4

> \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|2\|CH51830005\|CH51830005\|02A^POTASSIUM^99001^177^POTASSIUM^99VA60\|\|\|201507021236 58-0400\|\|\|\|\|\|\|201507021237-

> 0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053-VA500^LRUSER^TWO^^^^^99VA4

> \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|3\|CH51830005\|CH51830005\|03A^CO2^99001^179^CO2^99VA60\|\|\|20150702123658- 0400\|\|\|\|\|\|\|201507021237-0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053- VA500^LRUSER^TWO^^^^^99VA4

> \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|4\|CH51830005\|CH51830005\|04A^CREATININE^99001^173^CREATININE^99VA60\|\|\|2015070212 3658-0400\|\|\|\|\|\|\|201507021237-

> 0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053-VA500^LRUSER^TWO^^^^^99VA4

> \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R

> <span id="_bookmark98" class="anchor"></span><u>4.2.1.2 ORM Message Acknowledgment</u>

> Upon receipt of the order message, the VistA Laboratory system expects a general order response message (ORR) message. The ORR message consists of the following segments.

### ORR General Order Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MSH Message Header

> MSA Message Acknowledgment

### EXAMPLE:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Result Message (ORU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORU Observational Results Unsolicited Message MSH Message Header

{ PID Patient Identification

\[PV1\] Patient Identification

> { ORC Common Order

> OBR Observations Report ID

> {\[NTE\]} Laboratory Note or Comment

> {OBX} Observation Segment

> {\[NTE\]} Laboratory Note or Comment

> }

> }

### EXAMPLE:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MSH\|^~\\\|LA7UI1\|500\|LA7LAB\|500\|20150702125056- 0400\|\|ORU^R01\|63735,46256\|T\|2.5.1\|\|\|AL\|AL

> PID\|1\|\|2\|\|TEST^NEW^PATIENT^ZZ\|\|19220101\|F\|\|\|\|\|\|\|\|\|\|\|567-01-0122P PV1\|1\|O\|TC1

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|1\|CH51830005\|CH51830005\|01A^SODIUM^99001^176^SODIUM^99VA60\|\|\|20150702123658- 0400\|\|\|\|\|\|\|201507021237-0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053- VA500^LRUSER^TWO^^^^^99VA4\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-

> 2222~^WPN^BP^^^^^^

> DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|AR NTE\|\|1\|L\|SPECIMEN HEMOLYZED\|

> OBX\|1\|ST\|01A^SODIUM\|\|135\|ng/mL\|0.0-50.0\|\|\|\|F\|\|\|20150613003115\|\|101099- VA500^LRLAB^AUTO^VERIFY^^^99VA4\|.9750^AUTO VERIFY, MIDDLEWARE^99VA64_2\|VISTA1

> NTE\|1\|L\|Specimen repeated\|

> ORC\|NW\|CH51830005\|CH51830005\|\|\|\|\|\|20150702\|\|\|101053- VA500^LRUSER^TWO^^^^^99VA4\|\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111- 2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123

> OBR\|2\|CH51830005\|CH51830005\|02A^POTASSIUM^99001^177^POTASSIUM^99VA60\|\|\|2015070212365 8-0400\|\|\|\|\|\|\|201507021237-0400\|SER&Serum&HL70070&72&SERUM&99VA61&&5.2&SERUM\|101053- VA500^LRUSER^TWO^^^^^99VA4\|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP

> ^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\|ASTRA\|\S\\S\11\S\3150702\S\5\S\CH 0702

> 5\S\CH51830005\|\|\|\|\|\|\|\|^^^^^R\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|AR

> OBX\|1\|ST\|02A^POTASSIUM\|\|5\|ng/mL\|0.0-50.0\|\|\|\|F\|\|\|20150613003115\|\|101053- VA500^LRUSER^TWO^^^^99VA4\|.9760^TECH VERIFY, MIDDLEWARE^99VA64_2\|VISTA1

1.  <span id="bookmark100" class="anchor"></span><u>ORU Message Acknowledgment</u>

> Upon receipt of the result message, the VistA Laboratory system responds with an application acknowledgment (ACK) message. The ACK message consists of the following segments.

> ACK General Acknowledgment Message MSH Message Header

> MSA Message Acknowledgment

> ERR Error

> MSA-2 Message Control ID will contain the message control ID of the ORU message being acknowledged.

> MSA-3 Text Message will contain either of the following:

- If MSA-1 Acknowledgment Code is AA then MSA-3 will be blank.
- If MSA-1 Acknowledgment Code is AE then MSA-3 will contain an error message.

> ERR-3 HL7 Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-3 will contain value 0 from HL7 Table 0357.
- If MSA-1 Acknowledgment Code is AE then ERR-3 will contain an error code/message from HL7 Table 0357.

> ERR-4 Severity

- If MSA-1 Acknowledgment Code is AA then ERR-4 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from HL7 Table 0357

> ERR-5 Application Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-5 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from VistA Laboratory LA7 MESSAGE LOG BULLETINS FILE (#62.485)

> ERR-8 User Message

- If MSA-1 Acknowledgment Code is AA then ERR-8 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-8 will contain text message from ERR-5.

> ERR-9 Inform Person Indicator

- If MSA-1 Acknowledgment Code is AA then ERR-9 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-9 will contain "USR".

### EXAMPLE:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message with an AA application accept

> Message with an AE application error

## Communication Requirements for HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section specifies the requirements necessary to establish and maintain communications between VistA and all the participating systems. It includes requirements to be satisfied by VistA, by all the participating systems, and by each system when sending or receiving a message.

> Utilizing TCP/IP and HL7 Minimal Lower Level Protocol (MLLP).

> The interface between VistA and each participating system is established via a persistent or a transient (non-persistent) TCP/IP connection. Transient (non-persistent) connections are recommended for network security. Two TCP sockets provide bi-directional communications between each participating system.

> Within the context of the TCP socket, each participating system will connect as the client when it initiates a message. The other system will connect as the server to receive messages from the listen state.

### Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The participating system shall initiate the interface by establishing a TCP Server Socket.

> The participating system that initiates a message shall connect to the participating system TCP Server Socket as a TCP Client.

### TCP/IP Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA has a client (sender) and a server (listener) process to each remote system for sending and receiving HL7 messages. Each of these processes requires a TCP socket. The client process sends HL7 messages (including Application Acknowledgment messages) to the remote system and receives Accept Acknowledgment messages from the remote system. The server process receives HL7 messages (including Application Acknowledgment messages) from the remote system and sends Accept Acknowledgment messages to the remote system. Figure 5.1 depicts the sequence of events for an inbound and an outbound message regarding messages and acknowledgments.

> Sending System

> Client Socket

> <u>1. HL7 Message</u>

> <u>2. Accept Acknowledgement</u>

> Server Socket

> Receiving System

> Server Socket

> <u>3. Application Acknowledgement</u>

> <u>4. Accept Acknowledgement</u>

> Client Socket

> Figure 5.1 Acknowledgements

### Flow Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This interface uses the HL7 Minimal Lower Layer Protocol to format messages for data interchange, including acknowledgement messages. This protocol relies on the Message Header (MSH) Segment to define encoding, routing and acknowledgement rules governing the message.

### VistA Client/Server Process Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The flow of messages between VistA and the GIM system can be controlled by the VistA client/server process parameters. The parameters for the client/server process are definable at each installation site and can be customized for each GIM system. The followings are examples of some of the parameters:

- Server IP addresses/ports
- Client IP addresses/ports
- Number of attempts to open a socket
- Hang time for the client process between attempts to send a message
- Maximum number of times the client process will attempt to send a message
- Persistent/non-persistent client connection, recommend non-persistent connection.
- Retention time for client connection to keep a non-persistent connection established.

### Automated Recovery Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Should either side of the interface be disabled for any reason during any TCP connection, the other side will begin its automatic recovery procedures.

> Specifically, if the GIM system (TCP server) detects that VistA (TCP client) becomes disabled, the GIM system will reset to “listen” mode. If VistA detects that the GIM system becomes disabled, VistA will reset to “attempt connect” state. VistA will continue to attempt the reconnect for a site specified number of times or for a site-specified period of time before logging the situation and terminating.

### Message Transmission Retry Attempts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the GIM system is down and VistA cannot transmit a message to the GIM system, VistA will wait for a specified period of time (defaults to one minute) before attempting to re-send the message. VistA will retry until the specified maximum number of attempts (defaults to 2) is reached.

### Error Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA and the GIM system will use automated procedures to detect when connectivity has been lost and to initiate recovery procedures. VistA and the GIM system will use the HL7 2.5.1 enhanced acknowledgement mode, so the receiving system may respond to the message with an Accept Acknowledgement, an Application Acknowledgement, or both. When the receiving system commits the message to safe storage in a manner that releases the sending system from the need to retransmit the message, it sends a positive Accept Acknowledgement. When the receiving system has processed the message, it sends an Application Acknowledgement to return the resultant status to the sending system.

> Accept Acknowledgements will be used for all messages and the value passed in the Accept Acknowledgement field of the MSH segment (MSH-15) of the originating message will be observed. Application Acknowledgements will be used in accordance with the value passed in the Application Acknowledgement Type field of the MSH segment (MSH-16) of the originating message.

## <u>5.1.7.1 Requirements</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  If VistA detects a remote end disconnect, it shall attempt to reconnect to the GIM system TCP Server Socket for a locally defined number of Retry Attempts.
2)  If VistA detects a remote end disconnect and is unable to reconnect to the GIM system after locally defined number of Retry Attempts, it shall log an error.
3)  If the GIM system detects a remote end disconnect, it shall close that channel of its TCP Server Socket and await VistA reconnection.
4)  The Receiving system shall return an Accept Acknowledgement with a Commit Accept (CA) status to the Sending System for each incoming HL7 Message in which the Message Header Segment (MSH) conforms to the following criteria:
    - The first segment is a Message Header Segment (MSH);
    - The Field Separator (MSH-1) is valued.
    - The Encoding characters (MSH-2) are valued.
    - The Sending Application field (MSH-3) contains the values LA7LAB or LA7UIn as appropriate.
    - The Sending Facility field (MSH-4) contains the VA stations number of the primary VA facility hosted on the VISTA system.
    - The Receiving Application field (MSH-5) contains the values LA7LAB or LA7UIn as appropriate.
    - The Receiving Facility field (MSH-6) contains the VA stations number of the primary VA facility hosted on the VISTA system
    - The Date/time Message (MSH-7) is valued.
    - The Message Type Field (MSH-9) contains a valid message and event (when appropriate) type.
    - The Message Control ID Field (MSH-10) contains an ID.
    - The Processing ID (MSH-11) contains a valid ID.
    - The Version ID (MSH-12) contains 2.5.1.
    - The Accept Acknowledgment Type (MSH-15) indicates a valid acknowledgment condition.
    - The Application Acknowledgment Type (MSH-16) contains a valid acknowledgment condition.
5)  The Receiving system shall return an Accept Acknowledgement with a Commit Reject (CR) status to the Sending System for each incoming HL7 Message in which the Message Header Segment (MSH) fails to conform to the criteria in \#4 above.
6)  The Receiving system shall return an Accept Acknowledgement with a Commit Error (CE) status to the Sending System for each incoming HL7 Message that it has not accepted for any reasons other than those requiring a Commit Reject.
7)  Upon receipt of an Accept Acknowledgment with a Commit Error (CE) status from the Receiving System, the Sending System shall institute appropriate notification actions.
8)  The Receiving System shall return an Application Acknowledgement to the Sending System for each incoming HL7 Message in which the Application Acknowledgement Type Field of the MSH Segment (MSH-16) is set to “AL”, “SU” or “ER”.