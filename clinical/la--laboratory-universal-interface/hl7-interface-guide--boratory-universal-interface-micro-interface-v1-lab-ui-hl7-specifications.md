---
title: "Laboratory: Universal Interface Micro Interface Version 1 Lab UI HL7 Specifications"
doc_type: INT
doc_label: Interface Specification
doc_layer: anchor
doc_subject: Lab UI HL7 Specifications
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - table
  - contents
  - message
  - vista
  - code
  - number
  - class
  - segment
  - span
  - identifier
page_count: 0
word_count: 13094
section_count: 91
table_count: 52
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_ui_specs_lab_micro_interface_rel_1_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_ui_specs_lab_micro_interface_rel_1_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

Laboratory Universal Interface (UI) Version 1.6Health Level 7 (HL7) Version 2.5.1Interface Specifications DocumentRelease: LAB_MICRO_INTERFACE_RELEASE_1.0(LA\*5.2\*90 and LR\*5.2\*474)

VistA Lab Enhancements (VLE) –

Chemistry/Hematology/Microbiology Instruments

![](laboratory-universal-interface-micro-interface-version-1-lab-ui-hl7-specificatio/001.png)

April 2017

Document Version 2.1

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p><span id="_Toc467575414" class="anchor"></span>Table 1: VistA Laboratory Subscript</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/12/2017</td>
<td>2.1</td>
<td>Minor formatting changes.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/22/2016</td>
<td>2.0</td>
<td>Updated Introduction for combined build. Moved table 1 to section 1.2. Updated ORM and ORU tables. Reformatted document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/11/2016</td>
<td>1.9</td>
<td>Updated ORM and ORU messages; message provided by Tampa Test Site. Updated release name.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/22/2016</td>
<td>1.8</td>
<td>Re-ordered segments.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/03/2016</td>
<td>1.7</td>
<td><p>Technical Edit provided by</p>
<p>John McCormack. Added preliminary ORU provided by Randal Frommater, DSS, Inc.; reformatted document.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/02/2016</td>
<td>1.6</td>
<td>Technical Edit; updated ORM message per Randal Frommater, DSS, Inc. Updated footer; reformatted document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/01/2016</td>
<td>1.5</td>
<td>Added Micro ORM example. Reformatted document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/27/2016</td>
<td>1.4</td>
<td>Updates based on technical review from John McCormack for Tables 2, 10, 14 and 23. Deleted OBX-44. Updated OBX-16. Updated examples for ORM and ORU with examples from Auto Verification LA*88 v.6. Reformatted document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/17/2016</td>
<td>1.3</td>
<td>Added Chemistry ORM example provided by Randal Frommater, DSS, Inc.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/16/2016</td>
<td>1.2</td>
<td>Edits based on technical review from John McCormack for segments: OBR, OBX, and ORC; and technical edits to Communication Requirement and ORU Message Acknowledgment sections.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/14/2016</td>
<td>1.1</td>
<td>Added ERR Segment; updated ORU to include ERR and updated example; deleted duplicate table OBX Segment fields in ORU; added Patch number *90 to cover sheet; reformatted heading numbers.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/02/2016</td>
<td>1.0</td>
<td>Added ORC segment; clarified the OBR and the OBX segments regarding ORU; reformatted document; updated TOC.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/29/2016</td>
<td>0.9</td>
<td>Technical Edit.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/21/2016</td>
<td>0.8</td>
<td>Added additional fields. Reformatted document. Incorporated updates to OBX-23 with information provided by John McCormack.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/20/2016</td>
<td>0.7</td>
<td>Added fields and Microbiology examples.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/12/2016 – 04/14/2016</td>
<td>0.6</td>
<td>Added HL7 Tables, fields and definitions. Reformatted document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/25/2016</td>
<td>0.5</td>
<td>Updated title to Chemistry/Hematology/Microbiology Instruments, Auto Verification/Auto Release; removed references to AP (surgical pathology, cytology, electron microscopy). Reformatted document and TOC.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/18/2016</td>
<td>0.4</td>
<td><p>Updated Urine Culture example; example provided by</p>
<p>Randal Frommater, DSS, Inc. Updated Table of Contents (TOC).</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/17/2016</td>
<td>0.3</td>
<td>Completed changes to paragraph and sentence structure. Addition of Section on Communication Requirements for HL7 Interfaces. Removed all reference to HL7 v1.6.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/16/2016</td>
<td>0.2</td>
<td>Technical content updates based on feedback from Randal Frommater, DSS, Inc. Document title change to comply with the official project title. Included a new section on Specific Transactions relating to ORM and ORU with examples provided by Randal Frommater, DSS, Inc.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>03/14/2016-</p>
<p>03/15/2016</p></td>
<td>0.1</td>
<td>Commenced the addition of HL7 Table and Figure entries.</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc467575414" class="anchor"></span>Table 1: VistA Laboratory Subscript

Table of Contents

List of Tables

List of Figures

[Figure 1: Inbound and Outbound Messaging [51](#_Toc464030610)](#_Toc464030610)

# PURPOSE


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PURPOSE](#purpose)
  - [Statement of Intent](#statement-of-intent)
  - [Scope](#scope)
- [Overview of HL7 Terminology](#overview-of-hl7-terminology)
  - [Communication Protocol](#communication-protocol)
  - [Application Processing Rules](#application-processing-rules)
  - [Messages](#messages)
  - [Segments](#segments)
  - [Fields](#fields)
  - [Data Type](#data-type)
- [Segment: MSH - Message Header](#segment-msh-message-header)
  - [MSH-1 FIELD SEPARATOR (ST)](#msh-1-field-separator-st)
  - [MSH-2 ENCODING CHARACTERS (ST)](#msh-2-encoding-characters-st)
  - [MSH-3 SENDING APPLICATION (ST)](#msh-3-sending-application-st)
  - [MSH-4 SENDING FACILITY (ST)](#msh-4-sending-facility-st)
  - [MSH-5 RECEIVING APPLICATION (ST)](#msh-5-receiving-application-st)
  - [MSH-6 RECEIVING FACILITY](#msh-6-receiving-facility)
  - [MSH-7 DATE/TIME OF MESSAGE (TS)](#msh-7-datetime-of-message-ts)
  - [MSH-8 SECURITY (ST)](#msh-8-security-st)
  - [MSH-9 MESSAGE TYPE (CM)](#msh-9-message-type-cm)
  - [MSH-10 MESSAGE CONTROL ID (ST)](#msh-10-message-control-id-st)
  - [MSH-11 PROCESSING ID (ID)](#msh-11-processing-id-id)
  - [MSH-12 VERSION ID (ID)](#msh-12-version-id-id)
  - [MSH-13 SEQUENCE NUMBER](#msh-13-sequence-number)
  - [MSH-14 CONTINUATION POINTER](#msh-14-continuation-pointer)
  - [MSH-15 ACCEPT ACKNOWLEDGMENT TYPE (ID)](#msh-15-accept-acknowledgment-type-id)
  - [MSH-16 APPLICATION ACKNOWLEDGMENT TYPE (ID)](#msh-16-application-acknowledgment-type-id)
  - [MSH-17 COUNTRY CODE](#msh-17-country-code)
  - [MSH-18 CHARACTER SET](#msh-18-character-set)
  - [MSH-19 PRINCIPLE LANGUAGE OF MESSAGE](#msh-19-principle-language-of-message)
  - [MSH-20 ALTERNATE CHARACTER SET HANDLING SCHEME](#msh-20-alternate-character-set-handling-scheme)
  - [MSH-21 CONFORMANCE STATEMENT ID](#msh-21-conformance-statement-id)
- [Segment: PID - Patient Identification](#segment-pid-patient-identification)
  - [PID-1 Set ID – PID (SI)](#pid-1-set-id-pid-si)
  - [PID-3 Patient Identifier List (CX)](#pid-3-patient-identifier-list-cx)
  - [PID-5 Patient Name (XPN)](#pid-5-patient-name-xpn)
  - [PID-6 Mother’s Maiden Name (ST)](#pid-6-mothers-maiden-name-st)
  - [PID-7 Date/Time of Birth (TS)](#pid-7-datetime-of-birth-ts)
  - [PID-8 Administrative Sex (ID)](#pid-8-administrative-sex-id)
  - [PID-10 Race (CE)](#pid-10-race-ce)
  - [PID-16 Marital Status (ID)](#pid-16-marital-status-id)
  - [PID-19 SSN Number – Patient (ST)](#pid-19-ssn-number-patient-st)
- [Segment: PV1 - Patient Visit](#segment-pv1-patient-visit)
  - [PV1-1 Set ID – Patient Visit (SI)](#pv1-1-set-id-patient-visit-si)
  - [PV1-2 Patient Class (IS)](#pv1-2-patient-class-is)
  - [PV1-3 Assigned Patient Location (PL)](#pv1-3-assigned-patient-location-pl)
- [Segment: ORC - Common Order](#segment-orc-common-order)
  - [ORC-1 Order Control (ID)](#orc-1-order-control-id)
  - [ORC-2 Placer Order Number (EI)](#orc-2-placer-order-number-ei)
  - [ORC-3 Filler Order Number (EI)](#orc-3-filler-order-number-ei)
  - [ORC-9 Date/Time of Transaction (TS)](#orc-9-datetime-of-transaction-ts)
  - [ORC-12 Ordering Provider (XCN)](#orc-12-ordering-provider-xcn)
  - [ORC-14 Callback Phone Number (XTN)](#orc-14-callback-phone-number-xtn)
- [Segment: OBR - Observation Request](#segment-obr-observation-request)
  - [OBR-1 SET ID - OBSERVATION REQUEST (SI)](#obr-1-set-id-observation-request-si)
  - [OBR-2 PLACER ORDER NUMBER (CM)](#obr-2-placer-order-number-cm)
  - [OBR-3 FILLER ORDER NUMBER (CM)](#obr-3-filler-order-number-cm)
  - [OBR-4 UNIVERSAL SERVICE ID (CE)](#obr-4-universal-service-id-ce)
  - [OBR-7 OBSERVATION DATE/TIME (TS)](#obr-7-observation-datetime-ts)
  - [OBR-12 DANGER CODE (CE)](#obr-12-danger-code-ce)
  - [OBR-13 RELEVANT CLINICAL INFORMATION](#obr-13-relevant-clinical-information)
  - [OBR-15 SPECIMEN SOURCE (CM)](#obr-15-specimen-source-cm)
    - [Example OBR-15](#example-obr-15)
    - [Example OBR-15](#example-obr-15-1)
    - [Example OBR-15](#example-obr-15-2)
  - [OBR-16 ORDERING PROVIDER (CN)](#obr-16-ordering-provider-cn)
  - [OBR-17 ORDER CALLBACK PHONE NUMBER (XTN)](#obr-17-order-callback-phone-number-xtn)
    - [Example OBR-17](#example-obr-17)
  - [OBR-18 Placer Field (#1) (ST)](#obr-18-placer-field-1-st)
  - [OBR-19 Placer Field (#2) (ST)](#obr-19-placer-field-2-st)
  - [OBR-24 Diagnostic Service Sect ID (ID)](#obr-24-diagnostic-service-sect-id-id)
  - [OBR-26 Parent Result (CM)](#obr-26-parent-result-cm)
  - [OBR-27 QUANTITY/TIMING](#obr-27-quantitytiming)
  - [OBR-29 Parent (CM)](#obr-29-parent-cm)
  - [OBR-49 RESULT HANDLING (IS)](#obr-49-result-handling-is)
- [Segment: OBX - Observation](#segment-obx-observation)
  - [OBX-1 Set ID - Observation Simple (SI)](#obx-1-set-id-observation-simple-si)
  - [OBX-2 Value Type (ID)](#obx-2-value-type-id)
  - [OBX-3 Observation Identifier (CWE)](#obx-3-observation-identifier-cwe)
    - [Example OBX-3](#example-obx-3)
    - [Example OBX-3](#example-obx-3-1)
    - [Example OBX-3](#example-obx-3-2)
    - [Example OBX-3](#example-obx-3-3)
  - [OBX-4 Observation Sub-ID (ST)](#obx-4-observation-sub-id-st)
  - [OBX-5 Observation Value (\)](#obx-5-observation-value)
  - [OBX-6 Units (CE)](#obx-6-units-ce)
    - [Example OBX-6](#example-obx-6)
  - [OBX-7 Reference Range (ST)](#obx-7-reference-range-st)
    - [Example OBX-7](#example-obx-7)
  - [OBX-8 Abnormal Flag (ID)](#obx-8-abnormal-flag-id)
  - [OBX-14 Date/Time of the Observation (TS)](#obx-14-datetime-of-the-observation-ts)
  - [OBX-15 Producer’s ID (CE)](#obx-15-producers-id-ce)
    - [Example OBX-15](#example-obx-15)
  - [OBX-16 Responsible Observer (XCN)](#obx-16-responsible-observer-xcn)
  - [OBX-17 Observation Method (CE)](#obx-17-observation-method-ce)
    - [Example OBX-17](#example-obx-17)
  - [OBX-18 Equipment Instant Identifier (EI)](#obx-18-equipment-instant-identifier-ei)
    - [Example OBX-14](#example-obx-14)
- [Segment: NTE – Laboratory Notes and Comments](#segment-nte-laboratory-notes-and-comments)
  - [NTE-1 SET ID - NOTES AND COMMENTS (SI)](#nte-1-set-id-notes-and-comments-si)
  - [## NTE-3 COMMENT (FT)](#nte-3-comment-ft)
- [Segment: MSA Message Acknowledgment](#segment-msa-message-acknowledgment)
  - [10.1MSA-1 ACKNOWLEDGMENT CODE (ID)](#101msa-1-acknowledgment-code-id)
  - [MSA-2 MESSAGE CONTROL ID (ST)](#msa-2-message-control-id-st)
  - [MSA-3 TEXT MESSAGE (ST)](#msa-3-text-message-st)
- [Segment: ERR – Error Segment](#segment-err-error-segment)
    - [Example ERR-1](#example-err-1)
  - [ERR-4 SEVERITY (ID)](#err-4-severity-id)
    - [Example ERR-4](#example-err-4)
  - [ERR-5 APPLICATION ERROR CODE (CWE)](#err-5-application-error-code-cwe)
  - [ERR-8 USER MESSAGE (TX)](#err-8-user-message-tx)
  - [ERR-9 INFORM PERSON INDICATOR (IS)](#err-9-inform-person-indicator-is)
    - [Example ERR-9](#example-err-9)
- [TRANSACTION SPECIFICATIONS](#transaction-specifications)
  - [General](#general)
  - [Specific Message Consideration](#specific-message-consideration)
    - [Microbiology](#microbiology)
    - [Bacteriology](#bacteriology)
  - [Specific Transactions](#specific-transactions)
    - [Order Message (ORM)](#order-message-orm)
    - [ORM Message Acknowledgment](#orm-message-acknowledgment)
    - [Result Message (ORU)](#result-message-oru)
    - [ORU Message Acknowledgment](#oru-message-acknowledgment)
- [Communication Requirements for HL7 Interfaces](#communication-requirements-for-hl7-interfaces)
  - [Using TCP/IP and HL7 Minimal Lower Level Protocol](#using-tcpip-and-hl7-minimal-lower-level-protocol)
    - [Requirements](#requirements)
    - [TCP/IP Connections](#tcpip-connections)
    - [Flow Control](#flow-control)
    - [VistA Client/Server Process Parameters](#vista-clientserver-process-parameters)
    - [Automated Recovery Procedure](#automated-recovery-procedure)
    - [Error Management](#error-management)
This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (VistA) Laboratory software application based upon the Health Level Seven (HL7) Standard.
The VistA Laboratory Universal Interface (UI) forms the basis for the exchange of healthcare information between the VistA Laboratory software application and non-VistA systems, primarily laboratory automated instruments and generic instrument managers (GIMs) that receive laboratory orders and generate laboratory results information.
The Generic Instrument Manager (GIM) is a locally procured commercial device that controls communications between the Laboratory instruments and VistA. The VistA system downloads laboratory test orders through the GIM to the various instruments, and the instruments upload results to VistA through the GIM, eliminating the need for Laboratory developers to write a new interface for each different instrument.
> **NOTE:** New Generic Instrument Manager (GIM) software must be obtained from the vendor in order for this new interface to work.

## Statement of Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Universal Interface (UI) implements an interface to the HL7 Standard for use by the VistA Laboratory application in communicating with non-VistA systems to exchange healthcare information. The interface strictly adheres to the HL7 Standard and avoids using “Z” type extensions to the Standard. This interface specification is subject to modifications and revisions to incorporate changes, improvements, and enhancements. Later versions may support additional functionality of the current HL7 (V 2.5.1) Standard and new functionality released in future versions of the HL7 Standard.

The combined build LAB_MICRO_INTERFACE_RELEASE_1.0 contains the LR\*5.2\*474 and the LA\*5.2\*90 releases in support of the VistA Laboratory Microbiology initiative.

Patch LR\*5.2\*474 will provide new functionality to the Enter/Verify Data option of the Lab UI package. Three new release actions will now be available to the Technologist with the authority to release results. Results will be available to the applicable authorized clinicians and providers. In addition, the patch will allow a VA Medical Center the option of setting release defaults at the Package or User level.

Patch LA\*5.2\*90 will provide the constructs necessary to allow Microbiology or MI subscripted tests to be added to an Auto Instrument entry. An enhancement is also included for antibiotic susceptibility result processing which will now allow laboratories the ability to report susceptibilities to antimicrobial agents by utilizing SNOMED CT codes such as Positive and Negative. The handling of variations is also included in the build, such as the reporting of extended-spectrum beta-lactamases or ESBL enzymes that are resistant to most beta-lactam antibiotics. Locally mapped codes using an “L” for code set ID will now be processed for antibiotic susceptibilities.

All of the following SNOMED CT codes shall be supported with the release of patch LA\*5.2\*90:

- 131196009 Susceptible
- 260357007 Moderately susceptible
- 264841006 Intermediately susceptible
- 30714006 Resistant
- 10828004 Positive
- 260385009 Negative

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes messages transmitted between the VistA Laboratory application and a non-VistA automated system. The purpose of these messages is to exchange information concerning laboratory tests, specifically for orders and results related to the performance of the testing, on laboratory automated instruments.

The table below explains the Laboratory Subscripts utilized by VistA.

| VistA Laboratory Subscript | Traditional Functional Sections                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| CH                         | Chemistry, Hematology, Coagulation, Serology, Urinalysis, etc.                        |
| MI                         | Microbiology (i.e., Bacteriology, Virology, Mycology, Parasitology, Mycobacteriology) |

<span id="_Toc467575415" class="anchor"></span>Table 2: Segment Definition Tables

# Overview of HL7 Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that are used for interfacing with the VistA Laboratory package are based on the HL7 Hybrid Lower Level Protocol which is described in the HL7 Implementation Guide.

## Application Processing Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard describes the basic rules for application processing by the sending and receiving systems. Information contained in the Standard is not repeated here. Anyone wishing to interface with the VistA Laboratory package should become familiar with the HL7 Standard V. 2.5.1.

## Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following HL7 message types are used to support the exchange of Laboratory information:

> ACK General Acknowledgment

> ORM Order

> ORR General Order Response Message response to any ORM

> ORU Observational Results Unsolicited

## Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or may be allowed to repeat. Each segment has a name and is identified by a unique three-character code known as the Segment ID.

Please refer to Section entitled Transaction Specifications, for details and examples of all segments used to interface with VistA Laboratory Package. The following HL7 segments are used to support the exchange of Laboratory information:

> MSH Message Header

> PID Patient Identification

> PV1 Patient Visit

> ORC Common Order

> OBR Observation Request

> OBX Observation

> NTE Notes and Comment

> MSA Message Acknowledgment

> ERR Error

The segment definition tables list and describe the data fields in the segment and the characteristics of usage, as well as the properties of each HL7 segment. These terms display in the headings of the segment tables.

<table>
<caption><blockquote>
<p><span id="_Toc467575416" class="anchor"></span>Table 3: Data Type</p>
</blockquote></caption>
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
<p><strong>R</strong>–required</p>
<p><strong>RE</strong>–required or empty<br />
<strong>O</strong> (null)–optional</p>
<p><strong>X</strong>–not used with the trigger event<br />
<strong>C</strong>–conditional on the trigger event</p></td>
</tr>
<tr class="odd">
<td>VA R/O/C</td>
<td><p>VA (R/O/C) indicates whether the data field is required, optional, or conditional in a segment used by the Department of Veterans Affairs (VA).</p>
<p><strong>R</strong>–required</p>
<p><strong>O</strong> (null)–optional</p>
<p><strong>X</strong>–not used with the trigger event<br />
<br />
<strong>C</strong>–conditional on the trigger event</p></td>
</tr>
<tr class="even">
<td>RP/#</td>
<td><p>Repetition indicates the number of times you can repeat a field.</p>
<p><strong>N</strong> (null)–no repetition allowed</p>
<p><strong>Y</strong>–the field may repeat an indefinite or site determined number of times</p>
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

<span id="_Toc467575416" class="anchor"></span>Table 3: Data Type

## Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. The HL7 Messaging Standard does not specify how systems must store data within an application. Fields are transmitted as character strings.

The Segment Definition table in the HL7 Messaging Standard lists and describes the data fields in the segment and the characteristics of their usage.

HL7 segment fields support the exchange of laboratory data in ACK, ORM, ORR, and ORU messages.

## Data Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data type identifies the restrictions on the contents of a data field. HL7 defines a number of data types; the information is in a column labeled “DT” in the Segment Attribute table in the HL7 Messaging Standards.

| Data Type | Data Type Name                                                                       |
|-----------|--------------------------------------------------------------------------------------|
| AD        | Address                                                                              |
| CD        | Channel definition                                                                   |
| CE        | Coded element                                                                        |
| CF        | Coded element with formatted values                                                  |
| CK        | Composite ID with check digit                                                        |
| CM        | Composite                                                                            |
| CN        | Composite ID number and name                                                         |
| CNE       | Coded with no exceptions                                                             |
| CP        | Composite price                                                                      |
| CQ        | Composite quantity with units                                                        |
| CWE       | Coded with exceptions                                                                |
| CX        | Extended composite ID with check digit                                               |
| DLN       | Driver's license number                                                              |
| DR        | Date/time range                                                                      |
| DT        | Date                                                                                 |
| ED        | Encapsulated data                                                                    |
| EI        | Entity identifier                                                                    |
| FC        | Financial class                                                                      |
| FN        | Family name                                                                          |
| FT        | Formatted text                                                                       |
| HD        | Hierarchic designator                                                                |
| ID        | Coded values for HL7 tables                                                          |
| IS        | Coded value for user-defined tables                                                  |
| JCC       | Job code/class                                                                       |
| MA        | Multiplexed array                                                                    |
| MO        | Money                                                                                |
| NA        | Numeric array                                                                        |
| NM        | Numeric                                                                              |
| PL        | Person location                                                                      |
| PN        | Person name                                                                          |
| PPN       | Performing person time stamp                                                         |
| PT        | Processing type                                                                      |
| QIP       | Query input parameter list                                                           |
| QSC       | Query selection criteria                                                             |
| RCD       | Row column definition                                                                |
| RI        | Repeat interval                                                                      |
| RP        | Reference pointer                                                                    |
| SAD       | Street address                                                                       |
| SCV       | Scheduling class value pair                                                          |
| SI        | Sequence ID                                                                          |
| SN        | Structured numeric                                                                   |
| SRT       | Sort order                                                                           |
| ST        | String                                                                               |
| TM        | Time                                                                                 |
| TN        | Telephone number                                                                     |
| TQ        | Timing/quantity                                                                      |
| TS        | Time stamp                                                                           |
| TX        | Text data                                                                            |
| VH        | Visiting hours                                                                       |
| VID       | Version identifier                                                                   |
| XAD       | Extended address                                                                     |
| XCN       | Extended composite ID number and name                                                |
| XON       | Extended composite name and ID number for organizations                              |
| XPN       | Extended person name                                                                 |
| XTN       | Extended telecommunications number                                                   |
| A         | Active                                                                               |
| I         | Inactive                                                                             |
| L         | Inactive - Lost to follow-up (cancel contract)                                       |
| M         | Inactive - Moved or gone elsewhere (cancel contract)                                 |
| O         | Other                                                                                |
| P         | Inactive - Permanently inactive (Do not reactivate or add new entries to the record) |

<span id="_Toc467575025" class="anchor"></span>Table 4: MSH Segment

# Segment: MSH - Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message. Please see tables 2 and 3 above for definitions and abbreviations used in the following table.

| SEQ | LEN | DT | R/O/C | VA R/O/C | RP | TBL | ELEMENT NAME                 |
|---------|---------|--------|-----------|--------------|--------|---------|----------------------------------|
| 1       | 1       | ST     | R         | R            |        |         | FIELD SEPARATOR                  |
| 2       | 4       | ST     | R         | R            |        |         | ENCODING CHARACTERS              |
| 3       | 15      | ST     | R         | R            |        |         | SENDING APPLICATION              |
| 4       | 20      | ST     | R         | R            |        |         | SENDING FACILITY                 |
| 5       | 30      | ST     | R         | R            |        |         | RECEIVING APPLICATION            |
| 6       | 30      | ST     | R         | R            |        |         | RECEIVING FACILITY               |
| 7       | 26      | TS     | R         | R            |        |         | DATE/TIME OF MESSAGE             |
| 9       | 7       | CM     | R         | R            |        | 0076    | MESSAGE TYPE                     |
| 10      | 20      | ST     | R         | R            |        |         | MESSAGE CONTROL ID               |
| 11      | 1       | ID     | R         | R            |        | 0103    | PROCESSING ID                    |
| 12      | 8       | ID     | R         | R            |        | 0104    | VERSION ID                       |
| 15      | 2       | ID     | R         | R            |        | 0155    | ACCEPT ACKNOWLEDGEMENT TYPE      |
| 16      | 2       | ID     | R         | R            |        | 0155    | APPLICATION ACKNOWLEDGEMENT TYPE |

<span id="_Toc467575419" class="anchor"></span>Table 6: Accept/Application Acknowledgment Conditions

The segment terminator is always a carriage return (in ASCII, a hex 0D). The other delimiters are defined in the MSH segment, with the field delimiter in the fourth character position, and the other delimiters occurring as in the field called Encoding Characters. The Encoding Characters field is the first field after the segment ID. The delimiter values used in the MSH segment are the delimiter values used throughout the message.

## MSH-1 FIELD SEPARATOR (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the separator between the segment ID and the first real field, MSH-2–Encoding Characters. This field defines the character to be used as a separator for the rest of the message.

VistA Laboratory does not have pre-defined field separators. Applications are advised to use the value of this field to determine the field separator used throughout the message.

## MSH-2 ENCODING CHARACTERS (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains four characters in the following order: component separator, repetition separator, escape character, and subcomponent separator.

VistA Laboratory does not have pre-defined encoding characters. Applications are advised to use the value of this field to determine the encoding characters used throughout the message.

## MSH-3 SENDING APPLICATION (ST) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the interface used with lower level protocols.

- LA7LAB when VistA Lab originates the message (sending system).
- LA7UIx (where "x" is an integer 1-10) when the GIM originates the message.

## MSH-4 SENDING FACILITY (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sending Facility uses a three-digit number that identifies the medical center division, as found in the VistA INSTITUTION file (#4), STATION NUMBER field (#99). The VA station number of the primary VistA facility should be used for all interfaces implemented at a multi-divisional/integrated VistA system.

## MSH-5 RECEIVING APPLICATION (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- LA7LAB when VistA Lab originates the message (sending system).
- LA7UIx (where "x" is an integer 1-10) when the GIM originates the message.

## MSH-6 RECEIVING FACILITY 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Receiving Facility uses a three-digit number that identifies the receiving medical center division. Same as sending facility. See MSH-4.

## MSH-7 DATE/TIME OF MESSAGE (TS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Date/Time of Message is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

## MSH-8 SECURITY (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In some applications of HL7, the Security field is used to implement security features. At this time, its use is not yet further specified.

## MSH-9 MESSAGE TYPE (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The receiving system uses the Message Type field to know the data segments to recognize, and possibly, the application to which to route this message.

Components:

\<message type\> \<trigger event\>

- The first component is the message type, found in HL7 Table 0076 – Message Type.
- The second component is the trigger event code found in HL7 Table 0003 – Event Type Code.

> ORM~O01: Order message from VistA.

> ORU~R01: Result message to VistA.

> ORR~O02: General Order Acknowledgment Message to VistA

> ACK: General acknowledgment message

## MSH-10 MESSAGE CONTROL ID (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Message Control ID is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

## MSH-11 PROCESSING ID (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Processing ID is used to decide whether to process the message as defined in the HL7 application processing rules.

|           |                 |
|-----------|-----------------|
|           |                 |
| Value | Description |
| D         | Debugging       |
| P         | Production      |
| T         | Training        |

<span id="_Toc467575420" class="anchor"></span>Table 7: HL7 Table 0155 Accept/Application Acknowledgment Conditions

## MSH-12 VERSION ID (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Version ID is matched by the receiving system to its own version to be sure the message is interpreted correctly. Only the following values are expected/accepted: 2.5.1.

## MSH-13 SEQUENCE NUMBER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A non-null value in this field implies that the sequence number protocol is in use. This numeric field incremented by one for each subsequent value.

## MSH-14 CONTINUATION POINTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is used to define continuations in application-specific ways.

## MSH-15 ACCEPT ACKNOWLEDGMENT TYPE (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accept Acknowledgement defines the conditions under which accept acknowledgments are required to be returned in response to this message.

|           |                              |
|-----------|------------------------------|
| Value | Description              |
| AL        | Always                       |
| NE        | Never                        |
| ER        | Error/reject conditions only |
| SU        | Successful completion only   |

<span id="_Toc467575421" class="anchor"></span>Table 8: PID Segment Fields in ORM

This interface uses HL7 “original mode” acknowledgements.

## MSH-16 APPLICATION ACKNOWLEDGMENT TYPE (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Acknowledgment defines the conditions under which application acknowledgments are required to be returned in response to this message.

<table>
<caption><blockquote>
<p><span id="_Toc467575054" class="anchor"></span>Table 9: User-defined Table 0001 - Administrative Sex</p>
</blockquote></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AL</p>
</blockquote></td>
<td><blockquote>
<p>Always</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>Never</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ER</p>
</blockquote></td>
<td><blockquote>
<p>Error/reject conditions only</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SU</p>
</blockquote></td>
<td><blockquote>
<p>Successful completion only</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc467575054" class="anchor"></span>Table 9: User-defined Table 0001 - Administrative Sex

This interface uses HL7 enhanced mode acknowledgements.

## MSH-17 COUNTRY CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the country of origin for the message. It will be used primarily to specify default elements, such as currency denominations. ISO 3166 provides a list of country codes that may be used.

## MSH-18 CHARACTER SET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the character set for the entire message.

> **NOTE:** Refer to *HL7 Table 0211 - Alternate character sets* for valid values.

## MSH-19 PRINCIPLE LANGUAGE OF MESSAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the principal language of the message. Codes come from ISO 639.

Components:

\<identifier (ID)\> ^ \<text (ST)\> ^\< name of coding system (ST)\> ^ \<alternate identifier (ID)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

## MSH-20 ALTERNATE CHARACTER SET HANDLING SCHEME

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field specifies the value for the alternate character set handling scheme to be used when any alternative character sets are used and a special handling scheme is necessary.

> **NOTE:** See *HL7 Table 0356*. 

## MSH-21 CONFORMANCE STATEMENT ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Conformance Statement ID (Message Profile Identifier in version 2.5) is a unique identifier that applies to a query’s Conformance Statement, or as a Message Profile Identifier, asserts constancy with a message profile (grammar, syntax, usage, and so on). 

# Segment: PID - Patient Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information which does not change frequently.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name            |
|-----|-----|-----|-------|----------|-----|------|-------------------------|
| 1   | 4   | SI  | O     | R        |     |      | SET ID - PID            |
| 3   | 250 | CX  | R     | R        | Y   |      | PATIENT IDENTIFIER LIST |
| 5   | 250 | XPN | R     | R        | Y   |      | PATIENT NAME            |
| 6   | 250 | XPN | O     | RE       | Y   |      | MOTHER’S MAIDEN NAME    |
| 7   | 26  | TS  | O     | RE       |     |      | DATE/TIME OF BIRTH      |
| 8   | 1   | IS  | O     | RE       |     | 0001 | ADMINISTRATIVE SEX      |
| 10  | 250 | CE  | O     | RE       | Y   | 0005 | RACE                    |
| 16  | 250 | CE  | O     | RE       |     | 0002 | MARITAL STATUS          |
| 19  | 16  | ST  | O     | RE       |     |      | SSN NUMBER - PATIENT    |

<span id="_Toc467575423" class="anchor"></span>Table 10: HL7 Table 0005 (User-defined) - Race

## PID-1 Set ID – PID (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a sequence number used to identify the segment repetitions.

## PID-3 Patient Identifier List (CX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains an extended composite element.

Components:

\<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\>^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD)^ \<effective date (DT)\> ^ \<expiration date (DT)\>

Subcomponents of assigning authority:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

VistA sends VA Integration Control Number (ICN) and Social Security Number (SSN) (without dashes) when available in this field. Additionally, the internal entry number (IEN) on the local PATIENT file (#2) is transmitted.

When communicating with a DoD facility, VistA will only send the first repetition in this field.

## PID-5 Patient Name (XPN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the names of the patient. The primary or legal name of the patient is reported first.

Components:

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name:

\<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

## PID-6 Mother’s Maiden Name (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the family name under which the mother was born. It is used to differentiate patients with the same last name.

Components:

\<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^\<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^\<name assembly order (ID)\> Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

## PID-7 Date/Time of Birth (TS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the date and time of the birth of the patient.

## PID-8 Administrative Sex (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the sex of the patient. Although there are other entries in the HL7 table, only the following values are transmitted.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |
| U     | Unknown     |

<span id="_Toc467575057" class="anchor"></span>Table 11: HL7 Table 0002 (User-defined) – Marital Status

## PID-10 Race (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the race of the patient. These entries correspond to the VistA RACE file (#10). The primary identifier (components one through three) will be populated using values from HL7 Table 0005 (refer to the user-defined Table 0005 – Race below). The alternate identifier (components four through six), will be populated with CDC codes.

Components:

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

<span id="_Toc467575425" class="anchor"></span>Table 12: PV1 Segment Fields in ORM and ORU

> **NOTE:** The values contain a pre-calculated Mod 10 check digit separated by a dash.

## PID-16 Marital Status (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the marital status of the patient. These entries correspond to the VistA MARITAL STATUS file (#11).

> **NOTE:** Refer to the user-defined *Table 0002*, *Marital Status*.

| Value | Description   |
|-------|---------------|
| S     | Separated     |
| D     | Divorced      |
| M     | Married       |
| N     | Never Married |
| W     | Widow/Widower |
| U     | Unknown       |

<span id="_Toc467575427" class="anchor"></span>Table 14: ORC-14 Callback Phone Number

## PID-19 SSN Number – Patient (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is for backward compatibility only. When used for backward compatibility, this field contains the Social Security Number (SSN) of the patient.

> **NOTE:** In order to maintain backward compatibility, this field must be populated,.

For all patient identifiers, use PID-3 – Patient Identifier List.

# Segment: PV1 - Patient Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV1 segment is used to communicate information on a visit-specific basis. When communicating with a DoD facility, VistA will not send this segment in the ORU message.

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name              |
|-----|-----|-----|-------|----------|-----|------|---------------------------|
| 1   | 4   | SI  | O     | R        |     |      | SET ID - PATIENT VISIT    |
| 2   | 1   | IS  | R     | R        |     | 0004 | PATIENT CLASS             |
| 3   | 80  | PL  | O     | RE       |     |      | ASSIGNED PATIENT LOCATION |

<span id="_Toc467575428" class="anchor"></span>Table 15: OBR Fields in ORM

## PV1-1 Set ID – Patient Visit (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the unique number that identifies the transaction.

## PV1-2 Patient Class (IS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the category into which the patient falls at the site. VA facilities use the code, I for inpatient or O for outpatient.

## PV1-3 Assigned Patient Location (PL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the patient's initial assigned location or the location to which the patient is being moved.

Components:

\<point of care (IS)\> ^ \<room (IS)\> ^ \<bed (IS)\> ^ \<facility (HD)\> ^ \<location status (IS)\> ^ \<person location type (IS)\> ^ \<building (IS)\> ^ \<floor (IS)\> ^ \<location description (ST)

Subcomponents of facility:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

For an Inpatient, VistA will populate the first component with the ward location on which this patient is currently residing.

For an Outpatient, VistA will populate the first component with the most current location where a lab procedure was requested.

# Segment: ORC - Common Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All applications use the ORC segment as the primary means of communicating specific lab order information. This segment contains data items that are common to all orders.

<span id="_Toc467575426" class="anchor"></span>Table 13: ORC Segment Fields in ORM and ORU

| Seq | Len | DT  | R/O/C | VA R/O/C | RP# | TBL# | Element Name             |
|-----|-----|-----|-------|----------|-----|------|--------------------------|
| 1   | 2   | ID  | R     | R        |     | 0119 | ORDER CONTROL            |
| 2   | 22  | CM  | C     | C        |     |      | PLACER ORDER NUMBER      |
| 3   | 22  | CM  | C     | C        |     |      | FILLER ORDER NUMBER      |
| 9   | 26  | TS  | R     | R        |     |      | DATE/TIME OF TRANSACTION |
| 12  | 250 | CN  | R     | R        |     |      | ORDERING PROVIDER        |
| 14  | 250 | XTN | O     | O        | Y/2 |      | CALL BACK PHONE NUMBER   |

<span id="_Toc467575429" class="anchor"></span>Table 16: OBR Fields in ORU

The definition of this segment is the value that determines the function of the order segment. The contents for ORC-2, PLACER ORDER NUMBER are hard-coded with “NW” for order messages (ORM) and “RE” for result messages (ORU) originating from VistA.

## ORC-1 Order Control (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the value that determines the function of the order segment. The contents are hard-coded with RE for result messages (ORU) originating from VistA.

## ORC-2 Placer Order Number (EI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines the placer application’s order number, which should be returned with the result message.

Components:

\<unique placer ID\>^\<placer application ID\>

> This field contains either the accession number component of the accession or the 10-character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68), TYPE OF ACCESSION NUMBER field (#.092).

## ORC-3 Filler Order Number (EI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines the filler application’s order number.

Components:

\<unique placer ID\>^\<placer application ID\>

> This field contains either the accession number component of the accession or the 10-character unique identifier (UID) associated with the accession. Determination of which ID is used is based on the ACCESSION file (#68), TYPE OF ACCESSION NUMBER field (#.092).

## ORC-9 Date/Time of Transaction (TS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines the date ordered. VistA values this field with the related date ordered from VistA ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), DATE ORDERED field (#3).

## ORC-12 Ordering Provider (XCN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the person responsible for creating the request. The sequence is in the standard HL7 Composite Name format. This field is repeated in OBR-16.

Internal entry number of ordering provider in NEW PERSON file (#200) concatenated with “-VA” and VA station number is used as the id number.

## ORC-14 Callback Phone Number (XTN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the telephone number to call for clarification of a request or other information regarding the order. ORC-14-call back phone number is the same as OBR-17-order callback phone number.

Components:

\<DEPRECATED-Telephone Number (ST)\> ^ \<Telecommunication Use Code (ID)\> ^\<Telecommunication Equipment Type (ID)\> ^ \<Email Address (ST)\> ^ \<Country Code (NM)\> ^ \<Area/City Code (NM)\> ^ \<Local Number (NM)\> ^ \<Extension (NM)\> ^ \<Any Text (ST)\> ^ \<Extension Prefix (ST)\> ^ \<Speed Dial Code (ST)\> ^ \<Unformatted Telephone number (ST)\>

VistA values components based on the ordering provider’s NEW PERSON file \#200 entry using the following components:

- \#2 Telecommunication Use Code (ID) = WPN
- \#3 Telecommunication Equipment Type (ID) = PH or BP
- \#9 Any Text (ST) = VistA NEW PERSON file (#200) source field
- OFFICE PHONE (#.132)
- VOICE PAGER (#.137)
- DIGITAL PAGER (#.138)
- \#12 Unformatted Telephone number (ST) = phone or beeper number

| VistA NEW PERSON Field \# | VistA NEW PERSON Field Name | VistA NEW PERSON Field Description                                                                                               | HL7 SEQ 2: Telecommunication Use Code | HL7 SEQ 3: Telecommunication Equipment Type | HL7 SEQ 9: Any Text  | HL7 SEQ 12: Unformatted Telephone number |
|-------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------|--------------------------|----------------------------------------------|
| .131                          | PHONE (HOME)                    | This is the telephone number for the new person.                                                                                     | PRN                                       | PH                                              | PHONE (HOME) (#.131)     | \<actual number\>                            |
| .132                          | OFFICE PHONE                    | This is the business/office telephone for the new person.                                                                            | WPN                                       | PH                                              | OFFICE PHONE (#.132)     | \<actual number\>                            |
| .133                          | PHONE \#3                       | This is an alternate telephone number where the new person might also be reached.                                                    | WPN                                       | PH                                              | PHONE \#3 (#.133)        | \<actual number\>                            |
| .134                          | PHONE \#4                       | This is another alternate telephone number where the new person might also be reached.                                               | WPN                                       | PH                                              | PHONE \#4 (#.134)        | \<actual number\>                            |
| .135                          | COMMERCIAL PHONE                | This is a commercial phone number                                                                                                    | WPN                                       | PH                                              | COMMERCIAL PHONE (#.135) | \<actual number\>                            |
| .136                          | FAX NUMBER                      | This field holds a phone number for a FAX machine for this user.  It needs to be a format that can be understood by a sending MODEM. | WPN                                       | FX                                              | FAX NUMBER (#.136)       | \<actual number\>                            |
| .137                          | VOICE PAGER                     | This field holds a phone number for an ANALOG PAGER that this person carries with them.                                              | BPN                                       | BP                                              | VOICE PAGER (#.137)      | \<actual number\>                            |
| .138                          | DIGITAL PAGER                   | This field holds a phone number for a DIGITAL PAGER that this person carries with them.                                              | BPN                                       | BP                                              | DIGITAL PAGER (#.138)    | \<actual number\>                            |

<span id="_Toc467575430" class="anchor"></span>Table 17: Specimen Source (CM) Field

# Segment: OBR - Observation Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the reporting of clinical data, the OBR segment is utilized in all ORU messages as the report header. It identifies the observation set represented by the following observations. The OBR segment is part of a collection that can be used more than once for each observation result that is reported in the message.

| SEQ | LEN | DT | R/O/C | VA R/O/C | RP | TBL | ELEMENT NAME              |
|---------|---------|--------|-----------|--------------|--------|---------|-------------------------------|
| 1       | 4       | SI     | C         | C            |        |         | SET ID - OBSERVATION REQUEST  |
| 2       | 75      | CM     | C         | R            |        |         | PLACER ORDER NUMBER           |
| 3       | 75      | CM     | R         | O            |        |         | FILLER ORDER NUMBER           |
| 4       | 200     | CE     | R         | R            |        |         | UNIVERSAL SERVICE ID          |
| 7       | 26      | TS     | C         | C            |        |         | OBSERVATION DATE/TIME         |
| 12      | 60      | CE     | C         | C            |        |         | DANGER CODE                   |
| 13      | 300     | ST     | C         | C            |        |         | RELEVANT CLINICAL INFORMATION |
| 14      | 26      | TS     | R         | R            |        |         | SPECIMEN RECEIVED DATE/TIME   |
| 15      | 300     | CM     | R         | R            |        | 0070    | SPECIMEN SOURCE               |
| 16      | 60      | CN     | C         | R            | Y      |         | ORDERING PROVIDER             |
| 17      | 250     | XTN    | O         | O            | Y/2    |         | ORDER CALLBACK PHONE NUMBER   |
| 18      | 60      | ST     | R         | R            |        |         | PLACER FIELD \#1              |
| 19      | 60      | ST     | R         | R            |        |         | PLACER FIELD \#2              |

<span id="_Toc467575431" class="anchor"></span>Table 18: VistA LAB DATA File (#63) Fields to Derive Topography

| SEQ | LEN | DT | R/O/C | VA R/O/C | RP | TBL | ELEMENT NAME              |
|---------|---------|--------|-----------|--------------|--------|---------|-------------------------------|
| 1       | 4       | SI     | C         | C            |        |         | SET ID - OBSERVATION REQUEST  |
| 2       | 75      | CM     | C         | R            |        |         | PLACER ORDER NUMBER           |
| 3       | 75      | CM     | R         | O            |        |         | FILLER ORDER NUMBER           |
| 4       | 200     | CE     | R         | R            |        |         | UNIVERSAL SERVICE ID          |
| 7       | 26      | TS     | C         | C            |        |         | OBSERVATION DATE/TIME         |
| 12      | 60      | CE     | C         | C            |        |         | DANGER CODE                   |
| 13      | 300     | ST     | C         | C            |        |         | RELEVANT CLINICAL INFORMATION |
| 14      | 26      | TS     | R         | R            |        |         | SPECIMEN RECEIVED DATE/TIME   |
| 15      | 300     | CM     | R         | R            |        | 0070    | SPECIMEN SOURCE               |
| 16      | 60      | CN     | C         | C            | Y      |         | ORDERING PROVIDER             |
| 17      | 250     | XTN    | O         | O            | Y/2    |         | ORDER CALLBACK PHONE NUMBER   |
| 18      | 60      | ST     | R         | R            |        |         | PLACER FIELD \#1              |
| 19      | 60      | ST     | R         | R            |        |         | PLACER FIELD \#2              |
| 20      | 60      | ST     | O         | RE           |        |         | FILLER FIELD \#1              |
| 21      | 60      | ST     | O         | RE           |        |         | FILLER FIELD \#2              |
| 22      | 26      | TS     | O         | RE           |        |         | RESULTS RPT/STATUS CHNG - D/T |
| 24      | 10      | ID     | O         | RE           |        | 0074    | DIAGNOSTIC SERV SECT ID       |
| 25      | 1       | ID     | C         | CE           |        | 0123    | RESULT STATUS                 |
| 26      | 200     | CM     | O         | RE           |        |         | PARENT RESULT                 |
| 27      | 200     | TQ     | R         | R            | Y      |         | QUANTITY/TIMING               |
| 29      | 200     | CM     | O         | RE           |        |         | PARENT                        |
| 32      | 200     | CM     | O         | X            |        |         | PRINCIPLE RESULT INTERPRETER  |
| 33      | 200     | CM     | O         | X            | Y      |         | ASSISTANT RESULT INTERPRETER  |
| 34      | 200     | CM     | O         | X            | Y      |         | TECHNICIAN                    |
| 35      | 200     | CM     | O         | X            | Y      |         | TRANSCRIPTIONIST              |
| 44      | 250     | CE     | O         | RE           |        | 0088    | PROCEDURE CODE                |
| 49      | 2       | IS     | O         | C            |        | 0507    | RESULT HANDLING               |

<span id="_Toc467575432" class="anchor"></span>Table 19: VistA LAB DATA File (#63) Fields to Derive Collection Sample

## OBR-1 SET ID - OBSERVATION REQUEST (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set ID – Observation Request is a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

## OBR-2 PLACER ORDER NUMBER (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

It is a permanent identifier for an order and its associated observations on the system of the placer. The first component contains the collecting site’s unique accession identifier. The placer order number sent in the ORM message is returned with the results.

This field is populated from the ORDERING SITE UID field (#16.4) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

## OBR-3 FILLER ORDER NUMBER (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains an entity identifier made up of the following:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

This field is a permanent identifier for an order and its associated observations on the system of the filler. The first component is filled in with the VistA unique accession number. The filler order number is returned with the results.

This field is populated from the HOST UID field (#16.3) within the ACCESSION NUMBER subfile (#1) within the DATE subfile (#2) of the VistA ACCESSION file (#68).

## OBR-4 UNIVERSAL SERVICE ID (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a coded element made up of the following:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^\<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

This field is an identifier code for the requested observation or ordered test. This can be based on local and/or universal codes.

The Universal Service ID from the collecting site sent in the ORM message is returned.

If this test did not originate from the collecting site (e.g., it was an add-on or reflex test), the WKLD CODE file (#64) is used to identify the observed test. It contains the VA National Laboratory Test code. The LABORATORY TEST file (#60) is used to populate the alternate coding system. Future versions may utilize LOINC codes as the coding system.

\<NLT code (File \#64 Field \#1)\>^\<text\>^\<99VA64\>^\<Lab Test IEN\>^\<Lab Test Name (File \#60 Field \#.01)\>^\<99VA60\>

## OBR-7 OBSERVATION DATE/TIME (TS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Date/Time is the clinically relevant date/time of the observation. This is the actual date and time of the specimen collection. This data is pulled from the ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), DRAW TIME field (#9).

## OBR-12 DANGER CODE (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Danger Code contains the information located within the LAB DATA file (#63), PAT.INFO field (#.091).

## OBR-13 RELEVANT CLINICAL INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Relevant Clinical Info. contains the information located within the ACCESSION file (#68), ACCESSION NUMBER sub file (68.02), COMMENT field (#13.6).

## OBR-15 SPECIMEN SOURCE (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the information on the specimen source.

Components:

\<specimen source name or code (CWE)\> ^ \<additives (TX)\> ^ \<freetext (TX)\> ^ \<body site (CE)\> ^ \<site modifier (CE)\> ^ \<collection method modifier code (CE)\>

The specimen source component is encoded as a CWE data type and contains nine subcomponents. The ninth subcomponent of the specimen source component contains the name (text) of the related local topography.

> **NOTE:** Use of CWE data type is pre-adopted from HL7 v2.5.1 to facilitate expression of coding system version and local terms.

\<SNOMED CT code\>&\<text\>&\<SCT\>&\<code from HL7 Table 0070\>&\<text\>&\<HL70070\>&\<coding system version id\>&\<alternate coding system version id\>&\<local specimen name\>

The code sets used for sending the specimen source component are explained in the table below.

<table>
<caption><p><span id="_Toc467575433" class="anchor"></span>Table 20: Order Callback Phone Number</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 38%" />
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
<td>The SNOMED CT ID field (#20) in the TOPOGRAPHY FIELD file (#61)</td>
<td>If mapped, it’s used as the primary identifier (first three subcomponents), with the ‘identifier’ being the SCT code, the ‘text’ being the SCT fully specified name, and the seventh subcomponent containing the version of the SCT code.</td>
</tr>
<tr class="even">
<td>HL7 0070 Table</td>
<td><p>The entries in Table 0070 are mapped to one specific entry in the LAB ELECTRONIC CODES file (#64.061).</p>
<p>The LEDI HL7 field (#.09) in the TOPOGRAPHY FIELD file (#61) points to the associated entry in the LAB ELECTRONIC CODES file (#64.061).</p></td>
<td><p>If an SCT code exists for this specimen, the HL7 0070 value will be used as the alternate identifier (the second three subcomponents).</p>
<p>If an SCT code does not exist, the HL7 0070 value will be used as the primary identifier (first three subcomponents).</p>
<p>When communicating with DoD, if the SCT code exists, the HL7 0070 value will not be sent.</p></td>
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

<span id="_Toc467575433" class="anchor"></span>Table 20: Order Callback Phone Number

When VistA processes an incoming result, only the SNOMED CT and HL7 0070 table codes are used.

The topography in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                |
|-----------|---------|----------------------|
| CH        | 63.04   | Specimen Type (#.05) |
| MI        | 63.05   | Site/Specimen (#.05) |

<span id="_Toc208293873" class="anchor"></span>Table 21: HL7 Table 0074 – Diagnostic Serv Sect ID Mapping

### Example OBR-15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE |
|-------------------------------------------------------------------|

<span id="HL70aap" class="anchor"></span>Table 22: User-defined Observation Result Handling

The body site component (fourth) contains the related collection sample encoded as a CWE data type. This component is only populated when the specimen relates to a Microbiology (MI subscript) report.

- When the collection sample is mapped to SNOMED CT, the first three subcomponents contain the applicable SNOMED CT code with the seventh subcomponent indicating the SNOMED CT version.
- The fourth through sixth subcomponents contain the local code based on the VistA Laboratory COLLECTION SAMPLE file (#62).

> **NOTE:** If the collection sample was not mapped to SNOMED CT, the local codes will be in the first three components).

- The ninth subcomponent contains the local name (text) of the related collection sample.

The collection sample in VistA is derived from the following fields in the VistA LAB DATA file (#63).

| Subscript | Subfile | Field                     |
|-----------|---------|---------------------------|
| CH        | N/A     | N/A                       |
| MI        | 63.05   | Collection Sample (#.055) |

<span id="_Toc467575436" class="anchor"></span>Table 23: OBX Segment Fields in ORU

### Example OBR-15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|^^^257261003&Swab (specimen)&SCT&50&SWAB&99VA62&20060101&&SWAB\| |
|--------------------------------------------------------------------|

<span id="_Toc467575096" class="anchor"></span>Table 24: HL7 Table 0125 – Value Type

### Example OBR-15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|78014005&Urine (substance)&SCT&UR&Urine&HL70070&20060101&&URINE^^^78014005&Urine (substance)&SCT&15&URINE&99VA62&20060101&&URINE |
|------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc467575109" class="anchor"></span>Table 25: HL7 Table 0078 – Value Type

## OBR-16 ORDERING PROVIDER (CN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a composite ID number and name, and is made up of the following:

- It contains the identity of the person who is responsible for creating the request (i.e., ordering physician).
- It identifies the provider who ordered the test. The ID code and the name may be present.
- It is repeated in ORC-12 and contains the same value per the HL7 standards.

  Components:

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority:

\<namespace ID (IS)\> & \<universal ID (ST)\> & universal ID type (ID)

Subcomponents of assigning facility:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)

The Ordering Provider from the collecting site sent in the ORM message is returned.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), then the Ordering Provider sent with the parent (i.e., original ordered) test will be returned.

## OBR-17 ORDER CALLBACK PHONE NUMBER (XTN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Order Callback Phone Number field contains the telephone number for reporting a status or a result using the standard format with extension and/or beeper number when applicable.

Components:

\<DEPRECATED-Telephone Number (ST)\> ^ \<Telecommunication Use Code (ID)\> ^\<Telecommunication Equipment Type (ID)\> ^ \<Email Address (ST)\> ^ \<Country Code (NM)\> ^ \<Area/City Code (NM)\> ^ \<Local Number (NM)\> ^ \<Extension (NM)\> ^ \<Any Text (ST)\> ^ \<Extension Prefix (ST)\> ^ \<Speed Dial Code (ST)\> ^ \<Unformatted Telephone number (ST)\>

VistA values components based on the ordering provider’s NEW PERSON file \#200 entry using the following components:

- \#2 Telecommunication Use Code (ID) = WPN
- \#3 Telecommunication Equipment Type (ID) = PH or BP
- \#9 Any Text (ST) = VistA NEW PERSON file (#200) source field
- OFFICE PHONE (#.132)
- VOICE PAGER (#.137)
- DIGITAL PAGER (#.138)
- \#12 Unformatted Telephone number (ST) = phone or beeper number

| VistA NEW PERSON Field \# | VistA NEW PERSON Field Name | VistA NEW PERSON Field Description                                                                                               | HL7 SEQ 2: Telecommunication Use Code | HL7 SEQ 3: Telecommunication Equipment Type | HL7 SEQ 9: Any Text  | HL7 SEQ 12: Unformatted Telephone number |
|-------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------|--------------------------|----------------------------------------------|
| .131                          | PHONE (HOME)                    | This is the telephone number for the new person.                                                                                     | PRN                                       | PH                                              | PHONE (HOME) (#.131)     | \<actual number\>                            |
| .132                          | OFFICE PHONE                    | This is the business/office telephone for the new person.                                                                            | WPN                                       | PH                                              | OFFICE PHONE (#.132)     | \<actual number\>                            |
| .133                          | PHONE \#3                       | This is an alternate telephone number where the new person might also be reached.                                                    | WPN                                       | PH                                              | PHONE \#3 (#.133)        | \<actual number\>                            |
| .134                          | PHONE \#4                       | This is another alternate telephone number where the new person might also be reached.                                               | WPN                                       | PH                                              | PHONE \#4 (#.134)        | \<actual number\>                            |
| .135                          | COMMERCIAL PHONE                | This is a commercial phone number                                                                                                    | WPN                                       | PH                                              | COMMERCIAL PHONE (#.135) | \<actual number\>                            |
| .136                          | FAX NUMBER                      | This field holds a phone number for a FAX machine for this user.  It needs to be a format that can be understood by a sending MODEM. | WPN                                       | FX                                              | FAX NUMBER (#.136)       | \<actual number\>                            |
| .137                          | VOICE PAGER                     | This field holds a phone number for an ANALOG PAGER that this person carries with them.                                              | BPN                                       | BP                                              | VOICE PAGER (#.137)      | \<actual number\>                            |
| .138                          | DIGITAL PAGER                   | This field holds a phone number for a DIGITAL PAGER that this person carries with them.                                              | BPN                                       | BP                                              | DIGITAL PAGER (#.138)    | \<actual number\>                            |

<span id="_Toc467575439" class="anchor"></span>Table 26: OBX-17 Identifier and OBX-16 Value

> **NOTE:** A maximum of two repetitions will be encoded in the field of the possible eight fields which are site selectable.

### Example OBR-17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\| |
|----------------------------------------------------------------------------------------------------------|

<span id="_Toc467575115" class="anchor"></span>Table 27: Identifier and Coding System

## OBR-18 Placer Field (#1) (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Placer Field (#1) from the collecting site sent in the ORM message is returned here.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), then the Placer Field (#1) sent with the parent (i.e., original ordered) test will be returned.

## OBR-19 Placer Field (#2) (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Placer Field (#2) from the collecting site sent in the ORM message is returned here.

When sending to a non-DoD site, if this OBR is for a reflex test (that was reflexed at the performing site), than the Placer Field (#2) sent with the parent (i.e., original ordered) test will be returned.

## OBR-24 Diagnostic Service Sect ID (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a reference to the data storage location of the results in VistA LAB DATA file (#63).

The various subscripts are mapped as indicated in the table below.

| VistA Subscript       | HL7 Table 0074 – Diagnostic Serv Sect ID |
|-----------------------|------------------------------------------|
| CH                    | CH                                       |
| MI-Micro bacteriology | MB                                       |
| MI-Parasitology       | PAR                                      |
| MI-Mycology           | MYC                                      |
| MI-Mycobacteriology   | MCB                                      |
| MI-Virology           | VR                                       |

<span id="_Toc467575441" class="anchor"></span>Table 28: NTE

## OBR-26 Parent Result (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the OBX segment of the parent result related to this order.

Components:

\<OBX-3-observation identifier of parent result (CE\>^\<OBX-4-sub-ID of parent result (ST\>^\<part of OBX-5 observation result from parent (i.e., organism name) (TX)\>

If the current battery is an antimicrobial susceptibility, the parent results identified OBX contain a result, which identifies the organism on which the susceptibility was run.

VistA currently only uses this field for microbiology (MI) subscript results when reporting antibiotic susceptibility.

## OBR-27 QUANTITY/TIMING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Quantity/Timing contains the information concerning the timing and urgency of certain tests.

VistA values the 6<sup>th</sup> component priority with the related test urgency from VistA ACCESSION file (#68), ACCESSION NUMBER sub file (#68.02), TESTS field (#11) sub file (#68.04), URGENCY OF TEST field (#1).

## OBR-29 Parent (CM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the relationship of a child to its parent when a parent-child relationship exists. Parent is a two-component field. The components of the placer order number and the filler order number are transmitted in subcomponents of this two-component field.

Components:

\<parent’s placer order number\>^\<parent’s filler order number\>

Antimicrobial susceptibilities spawned by cultures, need to record the parent (culture) filler order number.

## OBR-49 RESULT HANDLING (IS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Result Handling transmits information regarding the handling of the result. For example, an order may specify that the result (e.g., an x-ray film) should be given to the patient for return to the requestor. If this field is not populated, then routine handling is implied.

| Value | Description | Comment                                                                                                             |
|-----------|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| AR        | Auto release    | Indicates that results when contained in an ORU message should be processed through the VistA Lab Auto Release process. |

<span id="_Toc467575442" class="anchor"></span>Table 29: MSA Segment Fields in ORM and ORU

VistA – when valued in an ORU message the results contained in the message will be processed through the VistA Laboratory Auto Release process. This field is used in conjunction with OBX.16 and OBX.17 to determine the type of verification and the responsible user.

# Segment: OBX - Observation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBX segment is used to transmit a single observation or observation fragment. The OBX segments can also be used more than one time in the message, and they may be followed by one or more NTE segments.

The OBX segment transmits a single observation or observation fragment.

| Seq | Len | DT  | Usage | VA R/O/C | RP/# | TBL# | Element Name                 |
|-----|-----|-----|-------|----------|------|------|------------------------------|
| 1   | 4   | SI  | O     | R        |      |      | SET ID – OBX                 |
| 2   | 3   | ID  | C     | R        |      | 0125 | VALUE TYPE                   |
| 3   | 250 | CWE | R     | R        |      |      | OBSERVATION IDENTIFIER       |
| 4   | 20  | ST  | C     | RE       |      |      | OBSERVATION SUB-ID           |
| 5   | 240 | \*  | O     | R        |      |      | OBSERVATION VALUE            |
| 6   | 250 | CE  | O     | RE       |      |      | UNITS                        |
| 7   | 60  | ST  | O     | RE       |      |      | REFERENCE RANGES             |
| 8   | 5   | IS  | O     | RE       |      | 0078 | ABNORMAL FLAGS               |
| 11  | 1   | ID  | R     | R        |      | 0085 | OBSERV RESULT STATUS         |
| 14  | 26  | TS  | O     | R        |      |      | DATE/TIME OF THE OBSERVATION |
| 15  | 250 | CE  | O     | R        |      |      | PRODUCER’S ID                |
| 16  | 250 | XCN | O     | RE       |      |      | RESPONSIBLE OBSERVER         |
| 17  | 250 | CE  | O     | RE       |      |      | OBSERVATION METHOD           |
| 18  | 22  | EI  | O     | RE       |      |      | EQUIPMENT INSTANT IDENTIFIER |

<span id="_Toc467575124" class="anchor"></span>Table 30: HL7 Table 0008 Acknowledgement Code

## OBX-1 Set ID - Observation Simple (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a sequence number used to identify the segment repetitions.

## OBX-2 Value Type (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

<span id="_Toc467575444" class="anchor"></span>Table 31: ERR Field Definitions

Although there are other entries in the HL7 table, only the above values are transmitted by VistA.

## OBX-3 Observation Identifier (CWE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is a unique identifier for the observation test results.

Components:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\> ^ \<coding system version ID (ST)\> ^ alternate coding system version ID (ST)\> ^ \<original text (ST)\>

Observation Identifier is encoded as a CWE from CE by pre-adopting the HL 2.5.1 version due to requirements to convey:

- Code set versioning information
- Local terms

(This was a VACO requirement, as it was deemed a potential patient safety issue if the local term is not conveyed.)

For CH-subscripted tests, the following codes can be used, in order of precedence:

- When a result is LOINC (Logical Observation Identifiers Names and Codes) encoded, LOINC will be used as the primary coding system.
- A result NLT code, if it is available.
- A local code encoded as: \<”CH” data name number\>\<data name label\>\<99VA63\>.

The original text component (ninth) is the local test name is the VistA LABORATORY TEST file (#60), Name field (#.01), when expressing laboratory test results associated with the VistA CH subscript.

\<LOINC CODE\> \<text\> \<LN\> \<NLT CODE\> \<text\> \<99VA64\> \<LOINC version \#\> \< NLT version \#\> \<local test name\>

The following HL7 delimiters are used in the examples below: \|^~\\

### Example OBX-3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LOINC as primary, NLT as alternate.

| \|2345-7^GLUCOSE:MCNC:PT:SER/PLAS:QN^LN^81352.0000^Glucose Fasting^99VA64 ^2.19^2.14^Serum Glucose\| |
|------------------------------------------------------------------------------------------------------|

<span id="_Toc467575130" class="anchor"></span>Table 32: HL7 Table 0357 - Message error condition codes

### Example OBX-3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LOINC code as primary, local code as alternate (no NLT available).

| \|29512^SODIUM:SCNC:PT:SER/PLAS:QN^LN^CH5^SODIUM^99VA63^2.19^5.2^SODIUM\| |
|---------------------------------------------------------------------------|

<span id="HL70516" class="anchor"></span>Table 33: HL7 Table 0516 – Error severity

### Example OBX-3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local code as primary, (no LOINC/NLT available).

| \|CH5^SODIUM^99VA63^^^^5.2^^SODIUM\| |
|--------------------------------------|

<span id="HL70533" class="anchor"></span>Table 34: User-defined Table 0533 – Application error code

For microbiology (MI subscript) the coding of this field is as specified in the Transaction Specifications section of this document.

### Example OBX-3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \|6584-7^Virus identified:Prid:Pt:XXX:Nom:Culture^LN^87590.0000^Viral Agent^99VA64^2.19^2.14^VIRUS\| |
|------------------------------------------------------------------------------------------------------|

<span id="HL70517" class="anchor"></span>Table 35: User-defined Table 0517 – Inform person code

## OBX-4 Observation Sub-ID (ST) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a value that distinguishes between multiple OBX segments with the same observation ID organized under one OBR.

For chemistry/hematology type results (CH subscript), VistA values this field with “CH” concatenated with the field number of the field used to store the instance of this result within the CHEM, HEM, TOX, RIA, SER, etc. subfile (#4) of the VistA LAB DATA file (#63). This can be used to aid in linking updates to previous transmissions.

For Microbiology results that contain organisms, VistA populates this field with a unique Isolate ID that identifies this organism.

## OBX-5 Observation Value (\*)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the value observed by the observation producer. The length of this field is variable, depending upon the value type. The data type is determined by the value of OBX-2 – Value Type.

For microbiology-type results reporting etiologic agents and living organisms, the value is encoded using the SNOMED CT coding system (SCT).

## OBX-6 Units (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a coded element.

Components:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

VistA populates the first component with the units.

### Example OBX-6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|mg/dL\| |
|-----------|

<span id="_Toc467575143" class="anchor"></span>Table 36: MI Order and Result NLT, LOINC Code

## OBX-7 Reference Range (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the identified range for this specific result.

### Example OBX-7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|60-123\| |
|------------|

## OBX-8 Abnormal Flag (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the entries identified by Table 0078, Value Type.

| Value                                       | Description                                                                                   | VA Usage |
|---------------------------------------------|-----------------------------------------------------------------------------------------------|----------|
| L                                           | Below low normal                                                                              | Used     |
| H                                           | Above high normal                                                                             | Used     |
| LL                                          | Below lower panic limits                                                                      | Used     |
| HH                                          | Above upper panic limits                                                                      | Used     |
| \<                                          | Below absolute low-off instrument scale                                                       | Not Used |
| \>                                          | Above absolute high-off instrument scale                                                      | Not Used |
| N                                           | Normal (applies to non-numeric results)                                                       | Not Used |
| A                                           | Abnormal (applies to non-numeric results)                                                     | Used     |
| AA                                          | Very abnormal (applies to non-numeric results, analogous to panic limits for numeric results) | Not Used |
| Null                                        | No range defined, or normal ranges do not apply                                               | Used     |
| U                                           | Significant change up                                                                         | Not Used |
| D                                           | Significant change down                                                                       | Not Used |
| B                                           | Better—use when direction not relevant                                                        | Not Used |
| W                                           | Worse—use when direction not relevant                                                         | Not Used |
| For microbiology susceptibilities only: |                                                                                               |          |
| S                                           | Susceptible                                                                                   | Used     |
| R                                           | Resistant                                                                                     | Used     |
| I                                           | Intermediate                                                                                  | Used     |
| MS                                          | Moderately susceptible                                                                        | Used     |
| VS                                          | Very susceptible                                                                              | Used     |

## OBX-14 Date/Time of the Observation (TS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the observation date/time that is the physiologically relevant date/time or the closest approximation to that date/time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed.

Value for this field is derived from DATE/TIME SPECIMEN TAKEN field (#.01) within the associated subfile of the VistA LAB DATA file (#63).

For CH-subscripted tests, if the collection time is estimated or unknown, only the date will be sent back (without a time).

## OBX-15 Producer’s ID (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the unique identifier of the responsible producing service and must be reported accurately. For instance, accuracy is imperative when the test results are produced at outside laboratories.

If this field is null, the receiving system assumes the observations are produced by the sending organization. This information supports CLIA regulations in the US. The code for producer ID is recorded as a CE data type. In the US, the Medicare number of the producing service is usually used as the identifier.

Components:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

The ID number is the station number found in the VistA INSTITUTION file (#4), STATION NUMBER field (#99). The text is the value of the OFFICIAL VA NAME field (#100). If this value is null, the value of the NAME field (#.01) is used. The name of the coding system is 99VA4.

The Laboratory CLIA number, when available, is transmitted as the alternate identifier with the name of the coding system, 99VACLIA.

### Example OBX-15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiters \|^~\\

| \|522^BONHAM^99VA4^987654321^^99VACLIA\| |
|------------------------------------------|

## OBX-16 Responsible Observer (XCN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When required, this field contains the identifier of the individual directly responsible for the observation (such as, the person who performed or verified the observation).

- In a nursing service, the observer is usually the professional who performed the observation (such as, took the blood pressure).
- In a laboratory, the observer is the technician who performed or verified the analysis.

The code for the observer is recorded as a CE data type. If the code is sent as a local code, it must be unique and unambiguous when combined with OBX-15-producer ID. When available, the code is transmitted with results.

Components:

\<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second or further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

Subcomponents of assigning authority:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility ID:

\<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

When the provider is assigned a National Provider ID (NPI), the NPI is transmitted as the ID, the assigning authority (ninth component) contains USDHHS, and the check digit is transmitted in identifier check digit (eleventh component). NPI is transmitted as the code identifying the check digit scheme employed (twelfth component) and NPI is transmitted as the identifier type code (thirteenth component).

- When the responsible observer is assigned a VA Person ID (VPID), the VPID is transmitted as the ID, the assigning authority (ninth component) contains USVHA, and the identifier type code (thirteenth component) contains PN.
- If there is no VPID, the internal entry number (DUZ) of the person in the VistA NEW PERSON file (#200) is transmitted, concatenated with -VA and the VA station number.

The Facility field is expressed as a DNS ID with the namespace ID (first component) containing the VA station number of the facility, the universal ID (second component) containing the related domain name of the facility (xxx.med.va.gov), and the universal ID type (third component) containing DNS.

VistA when OBR.49 indicates AR (auto release) and OBX.17 indicates the appropriate WKLD suffixes will use OBX.16 to determine the responsible observer based on the table below.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OBX-17 Identifier</strong></th>
<th><strong>OBX-16 Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.9750</td>
<td><p>ID of VistA application proxy LRLAB, AUTO VERIFY</p>
<p>|nnn-VAsss^LRLAB^AUTO^VERIFY^^^99VA4|</p></td>
</tr>
<tr class="even">
<td>.9760</td>
<td><p>ID of person verifying /releasing results on middleware.</p>
<p>|nnn-VAsss^LRUSER^TWO^^^^99VA4|</p></td>
</tr>
</tbody>
</table>

Where nnn = the DUZ (internal record number) of the application proxy or user in VistA NEW PERSON file (#200)

Where sss = the associated VA station number assigned to the VistA facility in VistA INSTITUTION file (#4)

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|101053-VA500^LRUSER^TWO^^^^99VA4|</p>
<p>|101099-VA500^LRLAB^AUTO^VERIFY^^^99VA4|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## OBX-17 Observation Method (CE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This optional field contains the method or procedure by which an observation is obtained, when the sending system needs to distinguish a measurement obtained by different methods, where the distinction is not implicit in the test ID.

Components:

\<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

VistA values this field, when available, with the related methodology associated with the result from WKLD SUFFIX CODES file (#64.2).

\<WKLD SUFFIX CODE\> \<text\> \<99VA64_2 \> \<alternate identifier\> \<alternate text\> \<name of alternate coding system

VistA uses this field in conjunction with OBR.49 RESULT HANDLING. When OBR.49 contains “AR” then VistA will process the results through the VistA Laboratory Auto Release system. OBX.17 should contain either of the following WKLD Suffixes to identify the results as being produced by an external (middleware) system’s auto verification process or user/tech verification on the middleware system.

| Identifier | Text                | Name of Coding System |
|----------------|-------------------------|---------------------------|
| .9750          | AUTO VERIFY, MIDDLEWARE | 99VA64_2                  |
| .9760          | TECH VERIFY, MIDDLEWARE | 99VA64_2                  |

### Example OBX-17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|.9750^AUTO VERIFY, MIDDLEWARE^99VA64_2|</p>
<p>|.9760^TECH VERIFY, MIDDLEWARE^99VA64_2|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## OBX-18 Equipment Instant Identifier (EI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the equipment instance (such as, Analyzer, Analyzer module, group of Analyzers) responsible for the production of the observation.

Components:

\<entity identifier (ST)\> ^ \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

For CH-subscripted tests, VistA Laboratory values this field with the information and in the form originally transmitted by the automated instrument that produced the result.

### Example OBX-14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123\| |
|----------------------------------------------------------------------------------------------------------|

# Segment: NTE – Laboratory Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NTE segment is used to report the Laboratory notes or comments.

|         |         |        |           |              |          |          |                             |
|---------|---------|--------|-----------|--------------|----------|----------|-----------------------------|
| SEQ | LEN | DT | R/O/C | VA R/O/C | RP/# | TBL# | ELEMENT NAME            |
| 1       | 4       | SI     | O         | R            |          |          | SET ID - NOTES AND COMMENTS |
| 3       | 64k     | FT     | O         | R            | Y        |          | COMMENT                     |

## NTE-1 SET ID - NOTES AND COMMENTS (SI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set ID Notes and Comments field may be used where multiple NTE segments are included in a message.

## ## NTE-3 COMMENT (FT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Comment field contains the comment associated with the specimen and/or a specific test.

Comments generated by automated instruments that relate to the specimens can be transmitted by the external GIM following the OBR segment.

Comments generated by automated instruments that relate to specific results can be transmitted by the external GIM following the OBX segment.

# Segment: MSA Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSA segment contains information sent in response to receiving a message.

| SEQ | LEN | DT | R/O/C | VA R/O/C | RP | TBL | ELEMENT NAME    |
|---------|---------|--------|-----------|--------------|--------|---------|---------------------|
| 1       | 2       | ID     | R         | R            |        | 0008    | ACKNOWLEDGMENT CODE |
| 2       | 20      | ST     | R         | R            |        |         | MESSAGE CONTROL ID  |
| 3       | 80      | ST     | C         | RE           |        |         | TEXT MESSAGE        |

## 10.1MSA-1 ACKNOWLEDGMENT CODE (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The acknowledgment code can have the following value:

|       |                                                     |
|-------|-----------------------------------------------------|
| Value | Description                                         |
| CA    | Enhanced mode: Accept Acknowledgment: Commit Accept |
| CE    | Enhanced mode: Accept Acknowledgment: Commit Error  |
| CR    | Enhanced mode: Accept Acknowledgment: Commit Reject |
| AA    | Enhanced mode: Application acknowledgment: Accept   |
| AE    | Enhanced mode: Application acknowledgment: Error    |
| AR    | Enhanced mode: Application acknowledgment: Reject   |

## MSA-2 MESSAGE CONTROL ID (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Control ID identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

## MSA-3 TEXT MESSAGE (ST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Text Message further describes an error condition. The text may be printed in error logs or presented to an end user.

# Segment: ERR – Error Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ERR segment is used to add error comments to acknowledgment messages when receiving ORU Result Messages.

| SEQ | LEN  | DT   | OPT | VA R/O/C | RP/# | TBL# | ITEM \# | ELEMENT NAME                |
|-----|------|------|-----|----------|------|------|---------|-----------------------------|
| 1   | 493  |  ELD | B   | R        | Y    |      | 00024   | Error Code and Location     |
| 2   | 18   | ERL  | O   | X        | Y    |      | 01812   | Error Location              |
| 3   | 705  | CWE  | R   | X        |      | 0357 | 01813   | HL7 Error Code              |
| 4   | 2    | ID   | R   | R        |      | 0516 | 01814   | Severity                    |
| 5   | 705  | CWE  | O   | RE       |      | 0533 | 01815   | Application Error Code      |
| 6   | 80   | ST   | O   | X        | Y/10 |      | 01816   | Application Error Parameter |
| 7   | 2048 | TX   | O   | X        |      |      | 01817   | Diagnostic Information      |
| 8   | 250  | TX   | O   | RE       |      |      | 01818   | User Message                |
| 9   | 20   | IS   | O   | R        | Y    | 0517 | 01819   | Inform Person Indicator     |
| 10  | 705  | CWE  | O   | X        |      | 0518 | 01820   | Override Type               |
| 11  | 705  | CWE  | O   | X        | Y    | 0519 | 01821   | Override Reason Code        |
| 12  | 652  | XTN  | O   | X        | Y    |      | 01822   | Help Desk Contact Point     |

#### #### ## ERR-1 Error Code and Location (CWE)

Components:  \<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\> ^ \<Coding System Version ID (ST)\> ^ \<Alternate Coding System Version ID (ST)\> ^ \<Original Text (ST)\>

### Example ERR-1 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ERR 3 = 207^Application internal error^HL70357 |
|------------------------------------------------|

This field identifies the HL7 (communications) error code.

> **NOTE:** Refer to *HL7 Table 035, Message Error Condition Codes* for valid values.

| Value | Description                | Comment                                                                                                                                              |
|-------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Message accepted           | Success. Optional, as the AA conveys success. Used for systems that must always return a status code.                                                |
| 100   | Segment sequence error     | Error: The message segments were not in the proper order, or required segments are missing.                                                          |
| 101   | Required field missing     | Error: A required field is missing from a segment                                                                                                    |
| 102   | Data type error            | Error: The field contained data of the wrong data type, e.g. an NM field contained "FOO".                                                            |
| 103   | Table value not found      | Error: A field of data type ID or IS was compared against the corresponding table, and no match was found.                                           |
| 200   | Unsupported message type   | Rejection: The Message Type is not supported.                                                                                                        |
| 201   | Unsupported event code     | Rejection: The Event Code is not supported.                                                                                                          |
| 202   | Unsupported processing id  | Rejection: The Processing ID is not supported.                                                                                                       |
| 203   | Unsupported version id     | Rejection:  The Version ID is not supported.                                                                                                         |
| 204   | Unknown key identifier     | Rejection: The ID of the patient, order, etc., was not found. Used for transactions *other than* additions, e.g. transfer of a non-existent patient. |
| 205   | Duplicate key identifier   | Rejection: The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.).                   |
| 206   | Application record locked  | Rejection: The transaction could not be performed at the application storage level, e.g., database locked.                                           |
| 207   | Application internal error | Rejection: A catchall for internal errors not explicitly covered by other codes.                                                                     |

## ERR-4 SEVERITY (ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field identifies the severity of an application error. Knowing if something is Error, Warning or Information is intrinsic to how an application handles the content.

> **NOTE:** Refer to *HL7 Table 0516, Error severity* for valid values.

If ERR-3 has a value of "0", ERR-4 will have a value of "I".

| Value | Description | Comment                                                                  |
|-------|-------------|--------------------------------------------------------------------------|
| W     | Warning     | Transaction successful, but there may issues                             |
| I     | Information | Transaction was successful but includes information e.g., inform patient |
| E     | Error       | Transaction was unsuccessful                                             |

### Example ERR-4 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ERR-4 = E |
|-----------|

## ERR-5 APPLICATION ERROR CODE (CWE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines the application specific code identifying the specific error that occurred.

> **NOTE:** Refer to *User-Defined Table 0533, Application Error Code* for suggested values.

If the message associated with the code has parameters, it is recommended that the message be indicated in the format of the java .text.MessageFormat approach[^1]. This style provides information on the parameter type to allow numbers, dates and times to be formatted appropriately for the language.

Components: 

\<Identifier (ST)\> ^ \<Text (ST)\> ^ \<Name of Coding System (ID)\> ^ \<Alternate Identifier (ST)\> ^ \<Alternate Text (ST)\> ^ \<Name of Alternate Coding System (ID)\> ^ \<Coding System Version ID (ST)\> ^ \<Alternate Coding System Version ID (ST)\> ^ \<Original Text (ST)\>

| Value | Description                                                                                             | Comment |
|-------|---------------------------------------------------------------------------------------------------------|---------|
| 307   | Msg \#30, Auto Release not allowed for accession UID CH53230012. Results have previously been released. |         |

## ERR-8 USER MESSAGE (TX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines the text message to be displayed to the application user. This differs from the actual error code and may provide more diagnostic information.

## ERR-9 INFORM PERSON INDICATOR (IS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field defines a code to indicate who (if anyone) should be informed of the error. This field may also be used to indicate that a particular person should NOT be informed of the error (e.g. Do not inform patient).

> **NOTE:** Refer to *User-defined table 0517, Inform Person Code* for suggested values.

| Value | Description           | Comment           |
|-------|-----------------------|-------------------|
| PAT   | Inform patient        | Not used by VistA |
| NPAT  | Do NOT inform patient | Not used by VistA |
| USR   | Inform User           | Used by VistA     |
| HD    | Inform help desk      | Not used by VistA |

### Example ERR-9 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ERR-9 = USR |
|-------------|

# TRANSACTION SPECIFICATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA initiates ORM order messages, they are acknowledged with an ACK commit acknowledgment message and an ORR application acknowledgment message.

When VistA receives an ORM message, an ACK commit acknowledgment message and an ORR application acknowledgment message are sent in response.

When VistA initiates ORU result messages, they are acknowledged with an ACK commit acknowledgment message and an ACK application acknowledgment message.

## Specific Message Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Microbiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Laboratory package does not support LOINC encoding of microbiology results. A default encoding is enabled to LOINC encode standard microbiology tests and antibiotics. There is default mapping of NLT/LOINC codes to standard fields within the Microbiology subfile (#5) multiple of LAB DATA file (#63).

| Test                       | Order NLT | Result NLT | LOINC Code |
|--------------------------------|---------------|----------------|----------------|
| Bacteriology report (#11)      | 87993.0000    |                |                |
| Gram stain (#11.6)             | 87993.0000    | 87754.0000     | 664-5          |
| Bacteriology organism (#12)    | 87993.0000    | 87570.0000     | 11475-1        |
| Bacteria colony count (#12,1)  |               | 87719.0000     | 564-5          |
| Bacteriology Susceptibility    | 87565.0000    |                |                |
| Parasite report (#14)          | 87505.0000    |                |                |
| Parasite organism (#16)        | 87505.0000    | 87576.0000     | 17784-0        |
| Parasite Stages                | 87505.0000    | 92930.0000     |                |
| Mycology report (#18)          | 87994.0000    |                |                |
| Fungal organism (#20)          | 87994.0000    | 87578.0000     | 580-1          |
| Fungal colony count (#20,1)    | 87994.0000    | 87723.0000     | 19101-5        |
| Mycobacterium report (#22)     | 87995.0000    |                |                |
| Acid Fast stain (#24)          | 87995.0000    | 87756.0000     | 11545-1        |
| Acid Fast stain quantity (#25) | 87995.0000    | 87583.0000     | 11545-1        |
| Mycobacterium organism (#26)   | 87995.0000    | 87589.0000     | 543-9          |
| Mycobacterium Susceptibility   | 87568.0000    |                |                |
| Virology report (#33)          | 87996.0000    |                |                |
| Viral agent (#36)              | 87996.0000    | 87590.0000     | 6584-7         |

### Bacteriology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The susceptibilities of a bacteriology or mycobacterium (TB) organism are based on the local site's mapping of the National VA Lab Code field (#64) in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and the related default LOINC code associated with the VA NLT code.

## Specific Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Order Message (ORM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>ORM General Order Message</u>

> MSH Message Header

> { PID Patient Identification

> \[PV1\] Patient Visit

> { ORC Common Order

> OBR Observations Report ID

> }

> }

#### Example of Microbiology Order Message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MSH|^~\&amp;|LA7LAB|442|LA7UI2|442|20160602073552-0500||ORM^O01|442157219542|T|2.5.1|||AL|AL|USA</p>
<p>PID|1||485922^7^M11||ZZTEST^AP^ONE||19170110|M|||||||||||159-01-1017P</p>
<p>PV1|1|O|ANTI</p>
<p>ORC|NW|3716000006|3716000006||||||20160520|||520736434-VA442^LRUSER^ONE^^</p>
<p>^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^561-555-1212~^BPN^BP^^^^^^DIGITAL</p>
<p>PAGER (#.138)^^^910-555-5555</p>
<p>OBR|1|3716000006|3716000006|BC123^BLOOD CULTURE^99001^87512.0000^Blood Culture</p>
<p>Automated^99VA64|||20160520145723-0500|||||||20160520145725-0500|BLD&amp;Whole blood</p>
<p>&amp;HL70070&amp;70&amp;BLOOD&amp;99VA61&amp;&amp;5.2&amp;BLOOD|520736434-VA442^LRUSER^ONE^^^^^99VA4</p>
<p>|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^561-555-1212~^BPN^BP^^^^^^DIGITAL PAGER (#</p>
<p>.138)^^^910-555-5555|BAC-TEC|2\S\2\S\37\S\3160000\S\6\S\BC 16 6\S\3716000006||||</p>
<p>||||^^^^^R</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example of Chemistry Order Message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MSH|^~\&amp;|LA7LAB|500|LA7UI1|500|20150702123702-0400||ORM^O01|500286|P|2.5.1|||||USA</p>
<p>PID|1||2^7^M11||TEST^NEW^PATIENT^ZZ||19220101|F|||||||||||567-01-0122P</p>
<p>PV1|1|O|TC1</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|1|CH51830005|CH51830005|01A^SODIUM^99001^176^SODIUM^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4</p>
<p>|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|2|CH51830005|CH51830005|02A^POTASSIUM^99001^177^POTASSIUM^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4</p>
<p>|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|3|CH51830005|CH51830005|03A^CO2^99001^179^CO2^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4</p>
<p>|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|4|CH51830005|CH51830005|04A^CREATININE^99001^173^CREATININE^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4</p>
<p>|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ORM Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon receipt of the order message, the VistA Laboratory system expects a general order response message (ORR) message. The ORR message consists of the following segments.

> <u>ORR General Order Acknowledgment Message</u>

> MSH Message Header

> MSA Message Acknowledgment

#### Example of ORM Message Acknowledgement:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MSH|^~\&amp;|LA7UI4|636|LA7LAB|636|20160421085751||ORR|2413|T|2.5.1|||AL</p>
<p>MSA|AA|6361465477663</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Result Message (ORU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is currently under analysis and review by Development.

> <u>ORU Observational Results Unsolicited Message</u>

> MSH Message Header

> { PID Patient Identification

> \[PV1\] Patient Identification

> { ORC Common Order

> OBR Observations Report ID

> {\[NTE\]} Laboratory Note or Comment

> {OBX} Observation Segment

> {\[NTE\]} Laboratory Note or Comment

> }

> }

#### Example of Microbiology Result Message

The following example is sample result message based on testing results with Vitek instrumentation.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MSH|^~\&amp;|LA7UI2|442|LA7LAB|442|20160511904413-0500||ORU^R01|VITUE008|T|2.5.1|||AL|ER|USA</p>
<p>PID|1||P0001||ZZTEST^AP^ONE||20040229|M</p>
<p>PV1|1</p>
<p>ORC|RE|3716000006</p>
<p>OBR|1|3716000006|||||2016051092300|||||||||||VITEK FOR TESTING|||||||||||||||||||||||||||||||</p>
<p>OBX|1|ST|93928.0000^Bact Rpt Remark^99VA64||Inst_Positve||||||P|||20160510124106||||VITEK FOR TESTING</p>
<p>NTE|1||BACT RPT REMARK COMMENT</p>
<p>OBX|2|CE|11475-1^ORGANISM^LN|1|3092008^Staphylococcus aureus^SCT||||||P|||20160511924106||||VITEK FOR TESTING</p>
<p>NTE|1|| organism comment found in NTE after Staph aureus ID OBX</p>
<p>OBX|3|NM|185-9^Ciprofloxacin^LN|1|&lt;=0.5|||R|||P|||20160519133754||</p>
<p>NTE|1|| cirpo comment found in NTE after Cirpo OBX</p>
<p>OBX|4|NM|193-3^Clindamycin^LN|1|&lt;=0.25|||R|||P|||20160519133754||</p>
<p>OBX|5|CE|11475-1^ORGANISM^LN|2|446870005^KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT (CRE)^L||||||P|||20160519124106||||VITEK FOR TESTING</p>
<p>OBX|6|CE|11475-1^ORGANISM^LN|3|9861002^STREPTOCOCCUS PNEUMONIAE^SCT||||||P|||20160519124106||||VITEK FOR TESTING</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example of Chemistry Result Message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MSH|^~\&amp;|LA7UI1|500|LA7LAB|500|20150702125056-0400||ORU^R01|63735,46256|T|2.5.1|||AL|AL</p>
<p>PID|1||2||TEST^NEW^PATIENT^ZZ||19220101|F|||||||||||567-01-0122P</p>
<p>PV1|1|O|TC1</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|1|CH51830005|CH51830005|01A^SODIUM^99001^176^SODIUM^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^</p>
<p>DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R||||||||||||||||||||||AR</p>
<p>NTE||1|L|SPECIMEN HEMOLYZED|</p>
<p>OBX|1|ST|01A^SODIUM||135|ng/mL|0.0-50.0||||F|||20150613003115||101099-VA500^LRLAB^AUTO^VERIFY^^^99VA4|.9750^AUTO VERIFY, MIDDLEWARE^99VA64_2|VISTA1</p>
<p>NTE|1|L|Specimen repeated|</p>
<p>ORC|NW|CH51830005|CH51830005||||||20150702|||101053-VA500^LRUSER^TWO^^^^^99VA4||^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123</p>
<p>OBR|2|CH51830005|CH51830005|02A^POTASSIUM^99001^177^POTASSIUM^99VA60|||20150702123658-0400|||||||201507021237-0400|SER&amp;Serum&amp;HL70070&amp;72&amp;SERUM&amp;99VA61&amp;&amp;5.2&amp;SERUM|101053-VA500^LRUSER^TWO^^^^^99VA4|^WPN^PH^^^^^^OFFICE PHONE (#.132)^^^999-111-2222~^WPN^BP</p>
<p>^^^^^^DIGITAL PAGER (#.138)^^^9-123-456-1123|ASTRA|\S\\S\11\S\3150702\S\5\S\CH 0702 5\S\CH51830005||||||||^^^^^R||||||||||||||||||||||AR</p>
<p>OBX|1|ST|02A^POTASSIUM||5|ng/mL|0.0-50.0||||F|||20150613003115||101053-VA500^LRUSER^TWO^^^^99VA4|.9760^TECH VERIFY, MIDDLEWARE^99VA64_2|VISTA1</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ORU Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon receipt of the result message, the VistA Laboratory system responds with a general acknowledgment (ACK) message. The ACK message consists of the following segments:

> <u>ACK General Acknowledgment Message</u>

> MSH Message Header

> MSA Message Acknowledgment

> ERR Error

> MSA-2 Message Control ID will contain the message control ID of the ORU message being acknowledged.

MSA-3 Text Message will contain either of the following:

- If MSA-1 Acknowledgment Code is AA then MSA-3 will be blank.
- If MSA-1 Acknowledgment Code is AE then MSA-3 will contain an error message.

> ERR-3 HL7 Error Code:

- If MSA-1 Acknowledgment Code is AA then ERR-3 will contain value 0 from HL7 Table 0357.
- If MSA-1 Acknowledgment Code is AE then ERR-3 will contain an error code/message from HL7 Table 0357.

> ERR-4 Severity

- If MSA-1 Acknowledgment Code is AA then ERR-4 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from HL7 Table 0357

> ERR-5 Application Error Code:

- If MSA-1 Acknowledgment Code is AA then ERR-5 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from VistA Laboratory LA7 MESSAGE LOG BULLETINS FILE (#62.485)

ERR-8 User Message:

- If MSA-1 Acknowledgment Code is AA then ERR-8 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-8 will contain text message from ERR-5.

ERR-9 Inform Person Indicator:

- If MSA-1 Acknowledgment Code is AA then ERR-9 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-9 will contain ”USR”.

#### Examples of ORU Message Acknowledgments

#### Message with an AA application accept.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MSH|^~\&amp;|LA7LAB|500|LA7UI1|500|20160108183946-0500||ACK^R01|500396|T|2.5.1|||AL|NE|USA</p>
<p>MSA|AA|64014,61262</p>
<p>ERR|||0^Message accepted^HL70357|I"</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Message with an AE application error.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MSH|^~\&amp;|LA7LAB|500|LA7UI1|500|20160108183946-0500||ACK^R01|500399|T|2.5.1|||AL|NE|USA</p>
<p>MSA|AE|63886,49648|Msg #30, Auto Release not allowed for accession UID CH53230012</p>
<p>ERR|||207^Application internal error^HL70357|E|307^Msg #30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.^99VA62.485|||Msg #30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.|USR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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

The client process sends HL7 messages (including Application Acknowledgment messages) to the remote system and receives Accept Acknowledgment messages from the remote system.

The server process receives HL7 messages (including Application Acknowledgment messages) from the remote system and sends Accept Acknowledgment messages to the remote system.

The diagram below depicts the sequence of events for both an inbound and an outbound message regarding messages and acknowledgments.

<span id="_Toc464030610" class="anchor"></span>Figure 1: Inbound and Outbound Messaging

![](laboratory-universal-interface-micro-interface-version-1-lab-ui-hl7-specificatio/002.png)

### Flow Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface uses the HL7 Minimal Lower Layer Protocol (MLLP) to format messages for data interchange, including acknowledgment messages. The MLLP protocol relies on the Message Header Segment (MSH) to define encoding, routing and acknowledgment rules governing the message.

### VistA Client/Server Process Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flow of messages between VistA and the remote system can be controlled by the VistA client/server process parameters. The parameters for the client/server process are definable at each installation site and can be customized for each remote system.

#### Examples of Parameters

The following list depicts examples of parameters:

- Server IP addresses/ports
- Client IP addresses/ports
- Number of attempts to open a socket
- Hang time for the client process between attempts to send a message
- Maximum number of times the client process attempts to send a message
- Persistent/non-persistent client connection
- Retention time for client connection to keep a non-persistent connection established

### Automated Recovery Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Should either side of the interface be disabled for any reason during any TCP connection, the other side will begin its automatic recovery procedures.

Specifically, if the GIM system (TCP server) detects that VistA (TCP client) becomes disabled, the GIM system will reset to “listen” mode. If VistA detects that the GIM system becomes disabled, VistA will reset to “attempt connect” state. VistA will continue to attempt the reconnect for a site specified number of times or for a site-specified period of time before logging the situation and terminating.

### Error Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA and the participating systems use automated procedures to detect when connectivity is lost and to initiate recovery procedures. Because VistA and the participating systems use the HL7 2.5.1 enhanced acknowledgment mode, the receiving system may respond to the message with an accept acknowledgment. When the receiving system commits the message to safe storage in a manner that releases the sending system from the need to retransmit the message, it sends a positive accept acknowledgment.

Accept acknowledgments are used for all messages and the value passed in the Accept Acknowledgment field of the MSH segment (MSH-15) of the originating message is observed. Application Acknowledg­ments are not used.

#### Requirements

1.  When VistA detects a remote end disconnect, it attempts to reconnect to the participating system TCP Server Socket for a locally defined number of retry attempts.
1.  When VistA detects a remote end disconnect and is unable to reconnect to the participating system after a locally defined number of retry attempts, it logs an error.
2.  When the participating system detects a remote end disconnect, it closes the channel of its TCP Server Socket and awaits VistA reconnection.
3.  The *receiving* system returns an accept acknowledgment with a Commit Accept (CA) status to the *sending* system for each incoming HL7 message in which the Message Header (MSH) segment conforms to the following criteria:
1.  The first segment is a Message Header (MSH) segment;
2.  The Message Type Field (MSH-9) contains a valid message type; and
3.  The Message Control ID Field (MSH-10) contains an ID.
4.  The *receiving* system returns an accept acknowledgment with a Commit Reject (CR) status to the *sending* system for each incoming HL7 message in which the Message Header (MSH) segment fails to conform to the following criteria:
1.  The first segment is a Message Header (MSH) segment;
2.  The Sending Application (MSH-3) is valid;
3.  The Sending Facility (MSH-4) is valid;
4.  The Receiving Application (MSH-5) is valid;
5.  The Receiving Facility (MSH-6) is valid;
6.  The Message Type Field (MSH-9) contains a valid message type;
7.  The Message Control ID Field (MSH-10) contains a message ID;
8.  The Message Processing ID (MSH-11) contains the appropriate value for the systems

    communicating;
9.  The Message Version ID contains 2.5.1.
5.  The *receiving* system returns an accept acknowledgment with a Commit Error (CE) status to the *sending* system for each incoming HL7 message that it did not accept, for any reasons other than those requiring a Commit Reject.
6.  Upon receipt of an accept acknowledgment with either a Commit Reject (CR) or Commit Error (CE) status from the *receiving* system, the *sending* system ceases transmission of the original HL7 message.

[^1]: \[1\] Details on MessageFormat can be found at [*http://java.sun.com/products/jdk/1.2/docs/api/java/text/MessageFormat.html*](http://java.sun.com/products/jdk/1.2/docs/api/java/text/MessageFormat.html).