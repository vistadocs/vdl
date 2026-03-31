---
title: Profiles for HL7 Messages from VistA to Commercial PACS
doc_type: INT
doc_label: Interface Specification
doc_layer: plain
doc_subject: 
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 3
description: <span id="_bookmark0" class="anchor"></span>Profiles for HL7 Messages from VistA to Commercial PACS
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - style
  - width
  - even
  - table
  - colgroup
  - thead
  - tbody
page_count: 0
word_count: 97902
section_count: 32
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/vista_pacs_hl7_profile_1_2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/vista_pacs_hl7_profile_1_2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/001.png)

<span id="_bookmark0" class="anchor"></span>Profiles for HL7 Messages from VistA to Commercial PACS

> *Including Business and Functional Requirements*

> Version: 1.2

> Date: 5 September 2008

> Document History

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5-Sep-08</p>
</blockquote></td>
<td><blockquote>
<p>This document (Version 1.2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29-Mar-06</p>
</blockquote></td>
<td><blockquote>
<p>Version 1.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21-Nov-05</p>
</blockquote></td>
<td><blockquote>
<p>Version 1.0</p>
</blockquote></td>
</tr>
</tbody>
</table>
## Foreword

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document contains profiles for all messages using the Health Level Seven (HL7) Standard that are sent from the VistA medical center system to commercial Picture Archiving and Communication Systems (PACS). The purpose of this messaging is to support DICOM Modality Worklist functionality on PACS, indicate DICOM mapping of received order data into stored and forwarded IOD instances, and to allow storage of VistA reports on PACS. A suggested DICOM to HL7 mapping is also given for reports generated on PACS[<sup>\*</sup>](#_bookmark2) and forwarded to VistA via HL7.

> VA has been a leader in the development of HIS-RIS-PACS interfaces for over 10 years. The currently running VA-PACS interface is based on the DICOM standard. At the present time, VA is updating this interface by adding functionality to the current DICOM Text Gateway that will support an IHE-compliant HL7 interface as well as an ADT registration interface. VA will be sending HL7 Version 2.3.1 messages, as required by IHE. However, a number of HL7 Version 2.4 structures will be pre-adopted: for example, the ROL segment, which can accommodate multiple telephone numbers for clinicians.

> This document serves two purposes. It identifies the VistA HIS data elements that will be handled by the new interface, as well as the HL7 and DICOM fields that contain those data elements. It also defines the functional business requirements of this interface, including the various conditions that can occur during operation and the expected behavior of the PACS under the possible circumstances.

> Specifications in this document are organized into conformance profiles covering registration, order, and report messaging. The methodology used is that of the Conformance section (2.12) of Chapter 2 of HL7 Version 2.5. The order messages used are intended to support the Scheduled Workflow (SWF) profile of the Integrating the Healthcare Enterprise (IHE) Radiology Technical Framework (Rad-TF), while the ADT update messages used are intended to support the IHE Rad-TF Patient Information Reconciliation (PIR) profile.

## Organization of This Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The [<u>Introduction</u>](#introduction-basic-data-sets) to this document contains four tables that group the key elements that are communicated by the HL7 interface. These [<u>Basic Data Sets</u>](#introduction-basic-data-sets) include elements relating to [<u>patients</u>](#introduction-basic-data-sets), [<u>visits</u>](#_bookmark8), [<u>orders</u>](#_bookmark9), and [<u>reports</u>](#basic-report-data-set). Within the tables are the names of the elements in the VistA system, the names of the corresponding HL7 elements, and the names and tags of the corresponding DICOM elements. These tables will be referred to throughout the document.

- <span id="_bookmark2" class="anchor"></span>This option implies that the PACS owns the transcription system and provides report messages to VistA.

> Following the Introduction, three HL7 profiles are presented. Each of these profiles is divided into sections as prescribed by the Conformance section of the HL7 Standard:

- Use case, including actors and roles
- Interactions, showing the message sent and expected processing within the communications portion of the interface
- Dynamic definition, which contains the business and functional requirements for message processing
- Message level static definition, showing the segment structure of the HL7 message used for the profile
- Segment level static definition, showing the elements used in each segment
- Field level static definition, describing how field elements (and, where applicable, subelements) are populated, including values for enterprise-wide controlled vocabularies

> The sections listed above conform to the conventions used in the discussion of HL7 Conformance Profiles in the *Health Level Seven Standard*, Version 2.5, Section 2.12.

> IHE Radiology support is provided by the following HL7 messages:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Trigger Event(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Order Code(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Profile</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VistA IHE Actor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Destination IHE Actor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Transaction</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADT</p>
</blockquote></td>
<td><blockquote>
<p>A01, A04</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Scheduled Workflow</p>
</blockquote></td>
<td><blockquote>
<p>ADT</p>
</blockquote></td>
<td><blockquote>
<p>DSS/Order Filler</p>
</blockquote></td>
<td><blockquote>
<p>Patient Registration (1)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADT</p>
</blockquote></td>
<td><blockquote>
<p>A02, A03, A08, A11, A12, A13, A40, A47</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Patient Information Reconciliation</p>
</blockquote></td>
<td><blockquote>
<p>DSS/Order Filler</p>
</blockquote></td>
<td><blockquote>
<p>Image Manager</p>
</blockquote></td>
<td><blockquote>
<p>Patient Update (12)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORM</p>
</blockquote></td>
<td><blockquote>
<p>O01</p>
</blockquote></td>
<td><blockquote>
<p>NW</p>
</blockquote></td>
<td><blockquote>
<p>Scheduled Workflow</p>
</blockquote></td>
<td><blockquote>
<p>DSS/Order Filler</p>
</blockquote></td>
<td><blockquote>
<p>Image Manager</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Scheduled (4)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORM</p>
</blockquote></td>
<td><blockquote>
<p>O01</p>
</blockquote></td>
<td><blockquote>
<p>XO, CA</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Reconciliation</p>
</blockquote></td>
<td><blockquote>
<p>DSS/Order Filler</p>
</blockquote></td>
<td><blockquote>
<p>Image Manager</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Update (13)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Changes for Version 1.2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following changes are introduced in Version 1.2 of this specification.

1.  Syntax for the A11 (Cancel Admit) message has been added at Section 2.4.6.
2.  The usage of *PV1-7-Attending Doctor* is now CE (conditional but may be empty) in all cases. If a patient is an inpatient and an attending doctor’s name is on file, the attending doctor’s name will be sent.
3.  The usage of *PV1-8-Referring Doctor* has been changed from CE (conditional but may be empty) to RE (required but may be empty). If a referring doctor’s name is on file, the referring doctor’s name will be sent.
4.  Sensitive and employee patients are flagged in *PV1-16-VIP Indicator*, as directed by the IHE Radiology Technical Framework. Formerly, *PV1-18-Patient Type* had been used; this practice has been discontinued.
5.  *PV1-45-Discharge Date/Time* will not be populated for patient registration messages.
6.  The use of the CE data type for Field *ROL-3-Role* is now fully documented.
7.  The values to be used for *DG1-6-Diagnosis Type* are now fully documented.
8.  Field *ORC-7.6-Priority* is now the primary source for priority information. Formerly, the primary source for priority information had been *OBR-27.6- Priority*.
9.  *OBR-20-Filler Field 1* has been reserved by the IHE Radiology Technical Framework for the value of Scheduled Procedure Step, which is not used in this interface. The data formerly carried in *OBR-20-Filler Field 1* are now carried in *OBR-21-Filler Field 2.*
10. *OBR-31-Reason for Study* is now populated as specified in the IHE Radiology Technical Framework. Formerly, OBX segments had been used for Reason for Study; this practice has been discontinued.
11. The length and data type of *OBX-5-Observation Value* vary according to the value of *OBX-2-Value Type*, as specified by the HL7 Standard. The use of the ID data type has been discontinued.
12. In order and report messages, Field *OBX-6-Units* is populated for quantitative data if units of measure are available. The field was formerly shown as not used.
13. Metric units of measure are used in *OBX-6-Units*. The use of English units of measure has been discontinued.
14. In field *OBX-6-Units*, the usage of components *OBX-6.1-Identifier* and *OBX-6.3- Name of Coding System* has been changed from X (not used) to R (required).
15. In the Basic Order Data Set, technologists’ comments in OBX segments are mapped to DICOM element (0032,4000) in the Modality Worklist SOP Class.
16. Details of error acknowledgments are specified in the dynamic definitions in Sections 1.3, 2.3, and 3.3.
17. Discharge date and time have been added to the Basic Visit Data Set at Section 0.2.
18. Appropriate behavior when multiple ICNs are received in an order message has been documented.
19. The documentation of behavior when multiple identifiers are received in an ADT message has been revised to reflect the usage of ICN alone as a patient identifier.
20. Only the first triplet (CPT code and text) of *OBR-4-Universal Service Identifier*

> will be used to populate the procedure code field on PACS.

21. Review of patient merges initiated by VistA is now an optional step.
22. The data types and usages for field *OBX-5-Observation Value* in order messages have been clarified.

# Introduction: Basic Data Sets


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Foreword](#foreword)
  - [Organization of This Document](#organization-of-this-document)
  - [Changes for Version 1.2](#changes-for-version-12)
- [Introduction: Basic Data Sets](#introduction-basic-data-sets)
  - [Basic Patient Data Set](#basic-patient-data-set)
  - [Basic Visit Data Set](#basic-visit-data-set)
  - [Basic Order Data Set](#basic-order-data-set)
  - [Basic Report Data Set](#basic-report-data-set)
  - [Terminology](#terminology)
- [Patient Registration Profile](#patient-registration-profile)
  - [Use Case](#use-case)
    - [Scope](#scope)
    - [Actors and Roles](#actors-and-roles)
  - [Interactions](#interactions)
  - [Dynamic Definition](#dynamic-definition)
    - [Patient Registration Message (ADT)](#patient-registration-message-adt)
    - [Acknowledgment Message (ACK)](#acknowledgment-message-ack)
  - [Static Definition – Message Level](#static-definition-message-level)
    - [Patient Registration Message](#patient-registration-message)
    - [Acknowledgment Message](#acknowledgment-message)
  - [Static Definition – Segment Level](#static-definition-segment-level)
    - [MSH Segment](#msh-segment)
    - [EVN Segment](#evn-segment)
    - [PID Segment](#pid-segment)
    - [PV1 Segment](#pv1-segment)
    - [ROL Segment](#rol-segment)
    - [DG1 Segment](#dg1-segment)
    - [OBX Segment](#obx-segment)
    - [AL1 Segment](#al1-segment)
    - [MSA Segment](#msa-segment)
    - [ERR Segment](#err-segment)
  - [Static Definition – Field Level](#static-definition-field-level)
    - [MSH Segment Fields](#msh-segment-fields)
    - [EVN Segment Fields](#evn-segment-fields)
    - [PID Segment Fields](#pid-segment-fields)
    - [PV1 Segment Fields](#pv1-segment-fields)
    - [ROL Segment Fields](#rol-segment-fields)
    - [DG1 Segment Fields](#dg1-segment-fields)
    - [OBX Segment Fields](#obx-segment-fields)
    - [AL1 Segment Fields](#al1-segment-fields)
    - [MSA Segment Fields](#msa-segment-fields)
    - [ERR Segment Fields](#err-segment-fields)
- [Patient Update Profile](#patient-update-profile)
  - [Use Case](#use-case-1)
    - [Scope](#scope-1)
    - [Actors and Roles](#actors-and-roles-1)
  - [Interactions](#interactions-1)
  - [Dynamic Definition](#dynamic-definition-1)
    - [Patient Update Message (ADT)](#patient-update-message-adt)
    - [Acknowledgment Message (ACK)](#acknowledgment-message-ack-1)
  - [Static Definition – Message Level](#static-definition-message-level-1)
    - [Patient Update Message: Transfer](#patient-update-message-transfer)
    - [Patient Update Message: Discharge](#patient-update-message-discharge)
    - [Patient Update Message: Update Patient Information](#patient-update-message-update-patient-information)
    - [Patient Update Message: Merge Patient Identifier List](#patient-update-message-merge-patient-identifier-list)
    - [Patient Update Message: Change Patient Identifier List](#patient-update-message-change-patient-identifier-list)
    - [Patient Update Message: Cancel Admit](#patient-update-message-cancel-admit)
    - [Patient Update Message: Cancel Transfer](#patient-update-message-cancel-transfer)
    - [Patient Update Message: Cancel Discharge](#patient-update-message-cancel-discharge)
    - [Acknowledgment Message](#acknowledgment-message-1)
  - [Static Definition – Segment Level](#static-definition-segment-level-1)
    - [MSH Segment](#msh-segment-1)
    - [EVN Segment](#evn-segment-1)
    - [PID Segment](#pid-segment-1)
    - [MRG Segment](#mrg-segment)
    - [PV1 Segment](#pv1-segment-1)
    - [ROL Segment](#rol-segment-1)
    - [DG1 Segment](#dg1-segment-1)
    - [OBX Segment](#obx-segment-1)
    - [AL1 Segment](#al1-segment-1)
    - [MSA Segment](#msa-segment-1)
    - [ERR Segment](#err-segment-1)
  - [Static Definition – Field Level](#static-definition-field-level-1)
    - [MSH Segment Fields](#msh-segment-fields-1)
    - [EVN Segment Fields](#evn-segment-fields-1)
    - [PID Segment Fields](#pid-segment-fields-1)
    - [MRG Segment Fields](#mrg-segment-fields)
    - [PV1 Segment Fields](#pv1-segment-fields-1)
    - [ROL Segment Fields](#rol-segment-fields-1)
    - [DG1 Segment Fields](#dg1-segment-fields-1)
    - [OBX Segment Fields](#obx-segment-fields-1)
    - [AL1 Segment Fields](#al1-segment-fields-1)
    - [MSA Segment Fields](#msa-segment-fields-1)
    - [ERR Segment Fields](#err-segment-fields-1)
- [Order Entry/Update Profile](#order-entryupdate-profile)
  - [Use Case](#use-case-2)
    - [Scope](#scope-2)
    - [Actors and Roles](#actors-and-roles-2)
  - [Interactions](#interactions-2)
  - [Dynamic Definition](#dynamic-definition-2)
    - [Order Message (ORM)](#order-message-orm)
    - [Acknowledgment Message (ACK)](#acknowledgment-message-ack-2)
  - [Static Definition – Message Level](#static-definition-message-level-2)
    - [Order Message](#order-message)
    - [Acknowledgment Message](#acknowledgment-message-2)
    - [PID Segment](#pid-segment-2)
    - [PV1 Segment](#pv1-segment-2)
    - [ORC Segment](#orc-segment)
    - [OBR Segment](#obr-segment)
    - [ZDS Segment](#zds-segment)
    - [OBX Segment](#obx-segment-2)
    - [MSA Segment](#msa-segment-2)
    - [ERR Segment](#err-segment-2)
  - [Static Definition – Field Level](#static-definition-field-level-2)
    - [MSH Segment Fields](#msh-segment-fields-2)
    - [PID Segment Fields](#pid-segment-fields-2)
    - [PV1 Segment Fields](#pv1-segment-fields-2)
    - [ORC Segment Fields](#orc-segment-fields)
    - [OBR Segment Fields](#obr-segment-fields)
    - [ZDS Segment Fields](#zds-segment-fields)
    - [OBX Segment Fields](#obx-segment-fields-2)
    - [MSA Segment Fields](#msa-segment-fields-2)
    - [ERR Segment Fields](#err-segment-fields-2)
- [Report Transmission & Storage Profile](#report-transmission-storage-profile)
  - [Use Case](#use-case-3)
    - [Scope](#scope-3)
    - [Actors and Roles](#actors-and-roles-3)
  - [Interactions](#interactions-3)
  - [Dynamic Definition](#dynamic-definition-3)
    - [Report Message (ORU)](#report-message-oru)
    - [Acknowledgment Message (ACK)](#acknowledgment-message-ack-3)
  - [Static Definition – Message Level](#static-definition-message-level-3)
    - [Report Message](#report-message)
    - [Acknowledgment Message](#acknowledgment-message-3)
  - [Static Definition – Segment Level](#static-definition-segment-level-2)
    - [MSH Segment](#msh-segment-2)
    - [PID Segment](#pid-segment-3)
    - [OBR Segment](#obr-segment-1)
    - [OBX Segment](#obx-segment-3)
    - [MSA Segment](#msa-segment-3)
    - [ERR Segment](#err-segment-3)
  - [Static Definition – Field Level](#static-definition-field-level-3)
    - [MSH Segment Fields](#msh-segment-fields-3)
    - [PID Segment Fields](#pid-segment-fields-3)
    - [OBR Segment Fields](#obr-segment-fields-1)
    - [OBX Segment Fields](#obx-segment-fields-3)
    - [Fields Used in the MSA Segment](#fields-used-in-the-msa-segment)
    - [Fields Used in the ERR Segment](#fields-used-in-the-err-segment)
> The following basic data sets will be referred to throughout these profiles. These tables list the patient-related, order-related, and message-related elements that will be transmitted, stored, and/or used by interfaced systems.

## Basic Patient Data Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the elements of the Basic Patient Data Set. All mapped DICOM fields, if they were provided and listed below, must be preserved in the PACS generated DICOM Modality Worklist (C-FIND) SOP class, as well as in all C-STORE storage SOP classes that are used to store and forward Instances by PACS.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 52%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Social Security Number (SSN)</p>
</blockquote></td>
<td><blockquote>
<p>PID-19-SSN Number-Patient [HL7 recommends populating this field for backward compatibility: if PID-3 did not carry the Patient ID]</p>
</blockquote></td>
<td><blockquote>
<p>(0010,0020) Patient ID</p>
<p>(0010,0021) Issuer</p>
<p>of Patient ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICN [Integration Control Number]</p>
</blockquote></td>
<td><blockquote>
<p>PID-3-Patient Identifier List occurrence containing PID-3.4-Assigning Authority value <strong>USVHA</strong> and PID-3.5-Identifier Type value <strong>NI</strong></p>
</blockquote></td>
<td><blockquote>
<p>(0010,1000) Other</p>
<p>Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><blockquote>
<p>PID-5-Patient Name</p>
</blockquote></td>
<td><blockquote>
<p>(0010,0010) Patient Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sex</p>
</blockquote></td>
<td><blockquote>
<p>PID-8-Sex</p>
</blockquote></td>
<td><blockquote>
<p>(0010,0040) Patient Sex</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Race</p>
</blockquote></td>
<td><blockquote>
<p>PID-10-Race</p>
</blockquote></td>
<td><blockquote>
<p>(0010,2160) Patient Ethnic Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>PID-7-Date/Time of Birth</p>
<p>[may be as imprecise as YYYY; is NOT zero filled]</p>
</blockquote></td>
<td><blockquote>
<p>(0010,0030) Patient Birth Date</p>
<p>(0010,0032) Patient Birth Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Size</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing <strong>HEIGHT</strong> in <em>OBX- 3.2-Text</em></p>
</blockquote></td>
<td><blockquote>
<p>(0010,1020) Patient Size (height in meters)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Weight</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing <strong>WEIGHT</strong> in <em>OBX-</em></p>
</blockquote></td>
<td><blockquote>
<p>(0010,1030) Patient</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 52%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark8" class="anchor"></span><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><em>3.2-Text</em></p>
</blockquote></td>
<td><blockquote>
<p>Weight (weight in kg)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Address</p>
</blockquote></td>
<td><blockquote>
<p>PID-11-Patient Address</p>
</blockquote></td>
<td><blockquote>
<p>(0010,1040)</p>
<p>Patient’s Address</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Basic Visit Data Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the elements of the Basic Visit Data Set. All mapped DICOM fields, if they were provided and listed below, must be preserved in the PACS generated DICOM Modality Worklist (C-FIND) SOP class, as well as in all C-STORE storage SOP classes that are used to store and forward Instances by PACS. Superscript <sup>MWL</sup> is used if only the Modality Worklist applies.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Category of Exam [inpatient, outpatient, etc.]</p>
</blockquote></td>
<td><blockquote>
<p>PV1-2-Patient Class</p>
</blockquote></td>
<td><blockquote>
<p>(0038,4000) Visit</p>
<p>Comments</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Room-Bed</p>
</blockquote></td>
<td><blockquote>
<p>PV1-3-Assigned Patient Location</p>
</blockquote></td>
<td><blockquote>
<p>(0038,0300) Current Patient Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Attending Physician</p>
</blockquote></td>
<td><blockquote>
<p>PV1-7-Attending Doctor [also carried in an occurrence of the ROL segment]</p>
</blockquote></td>
<td><blockquote>
<p>(0008,1050) Performing Physician(s)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Ordering Physician</p>
</blockquote></td>
<td><blockquote>
<p>PV1-8-Referring Doctor [also carried in an occurrence of the ROL segment]</p>
</blockquote></td>
<td><blockquote>
<p>(0008,0090) Referring Physician(s)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Allergies</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing</p>
<p><strong>ALLERGIES</strong> in <em>OBX-3.2-Text</em></p>
</blockquote></td>
<td><blockquote>
<p>(0010,2000) Medical Alerts</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pregnancy Status</p>
</blockquote></td>
<td><blockquote>
<p>PV1-15-Ambulatory Status (value <strong>B6</strong> indicates that patient is pregnant)</p>
</blockquote></td>
<td><blockquote>
<p>(0010,21C0) Pregnancy Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Sensitivity (employee, flagged sensitive, etc.)</p>
</blockquote></td>
<td><blockquote>
<p>PV1-16-VIP Indicator</p>
</blockquote></td>
<td><blockquote>
<p>(0040,3001) Patient Confidentiality Constraint</p>
<p>(0040,1008) <sup>MWL</sup></p>
<p>Confidentiality Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark9" class="anchor"></span><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Admission ID</p>
</blockquote></td>
<td><blockquote>
<p>PV1-19-Visit Number</p>
</blockquote></td>
<td><blockquote>
<p>(0038,0010) Admission ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Date/Time of Admission</p>
</blockquote></td>
<td><blockquote>
<p>PV1-44-Admit Date and Time</p>
</blockquote></td>
<td><blockquote>
<p>(0038,0020) Admitting Date and</p>
<p>(0038,0021) Admitting Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Date/Time of Discharge</p>
</blockquote></td>
<td><blockquote>
<p>PV1-45-Discharge Date and Time</p>
</blockquote></td>
<td><blockquote>
<p>(0038,0030) Discharge Date and</p>
<p>(0038,0032) Discharge Time</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Basic Order Data Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the elements of the Basic Order Data Set. All mapped DICOM elements, if they were provided and listed below, must be preserved either in the PACS generated DICOM Modality Worklist (C-FIND) SOP class and/or in all C-STORE storage SOP classes that are used to store and forward Instances by PACS. Superscript <sup>MWL</sup> is used if only the Modality Worklist SOP class applies.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 30%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Order set</p>
</blockquote></td>
<td><blockquote>
<p>ORC-8-Parent</p>
</blockquote></td>
<td><blockquote>
<p>No DICOM mapping as this field merely holds together multiple VistA <em><strong>Cases</strong></em> (Imaging</p>
<p>Service Requests) for the same Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Location/Institution (Contains institution and location where imaging is performed)</p>
</blockquote></td>
<td><blockquote>
<p>OBR-20-Filler Field 1</p>
</blockquote></td>
<td><blockquote>
<p>(0040,0011) <sup>MWL</sup> Scheduled Procedure Step Location</p>
<p>(0008,0080) Institution Name</p>
<p>(0008,0082) Institution Code -- SQ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ordering Provider</p>
</blockquote></td>
<td><blockquote>
<p>OBR-16-Ordering Provider</p>
</blockquote></td>
<td><blockquote>
<p>(0032,1032) Requesting Physician</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Callback Phone Number</p>
</blockquote></td>
<td><blockquote>
<p>OBR-17-Order Callback Phone Number</p>
</blockquote></td>
<td><blockquote>
<p>(0040,2010) <sup>MWL</sup> Order</p>
<p>Callback Phone Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 30%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Full Accession Number (exam date concatenated with the Case Number: ‘MMDDYY-nnnnn’)</p>
</blockquote></td>
<td><blockquote>
<p>OBR-19-Placer Field 2</p>
</blockquote></td>
<td><blockquote>
<p><em><u>Full Accession Number:</u></em></p>
<p>(0008,0050) Accession Number</p>
<p><em><u>Case Number only (‘nnnnn’):</u></em></p>
<p>(0020,0010) Study ID</p>
<p>(0040,0100) <sup>MWL</sup> Sch.Proc.Step</p>
<p>(0040,1001)<sup>MWL</sup> Requested Procedure ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Procedure (orderable item codes – CPT code and text)</p>
</blockquote></td>
<td><blockquote>
<p>OBR-4-Universal Service ID</p>
</blockquote></td>
<td><blockquote>
<p><u><em>CPT-4 code and text</em>:</u></p>
<p>(0032,1064) <sup>MWL</sup> Requested Procedure Code Sequence – SQ:</p>
<p>(0008,0100) Code Value</p>
<p>(0008,0102) Coding Scheme Designator</p>
<p>(0008,0104) Code Meaning</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Request Urgency</p>
</blockquote></td>
<td><p>ORC-7.6-Priority:</p>
<blockquote>
<p>S = STAT (with</p>
<p>highest priority) A = ASAP (fill after</p>
</blockquote>
<p>Stat orders)</p>
<blockquote>
<p>R = ROUTINE (the</p>
<p>default)</p>
</blockquote></td>
<td><blockquote>
<p>(0040,1003) <sup>MWL</sup> Requested Procedure Priority</p>
<p>The HL7 values shown in the previous column are to be mapped to DICOM values as follows:</p>
<p><strong>HL7 DICOM</strong></p>
<p>S STAT</p>
<p>A HIGH</p>
<p>R ROUTINE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Modifiers – procedure and CPT</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing <strong>MODIFIERS</strong> in OBX- 3.2-Text -3</p>
<p>Types:</p>
<p>‘M’ - Procedure modifiers (local)</p>
<p>‘C4’ - CPT modifiers (national)</p>
</blockquote></td>
<td><blockquote>
<p>(0032,1060) <sup>MWL</sup> Requested Procedure Description: applicable modifiers concatenated and optionally appended with laterality indicator</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 30%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Modality</p>
</blockquote></td>
<td><blockquote>
<p>OBR-24 (Diagnostic Service Section ID)</p>
</blockquote></td>
<td><blockquote>
<p>(0008,0060) Modality</p>
<p>(0040,0100) <sup>MWL</sup></p>
<p>Sched.Procedure Step – SQ: (0008,0060) Modality</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduled Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>ORC-7.4.1-Time (in</p>
<p>Component OBR-27.4- Start Date/Time of Field OBR-27-</p>
<p>Quantity/Timing) OBR-27.4.1- Time (in</p>
<p>Component OBR-27.4-</p>
<p>Start Date/Time of Field OBR-27-</p>
<p>Quantity/Timing)</p>
</blockquote></td>
<td><blockquote>
<p>(0032,1000) <sup>MWL</sup> Sched.Study Start Date</p>
<p>(0032,1001) <sup>MWL</sup> Sched.Study Start Time</p>
<p>(0040,0100) <sup>MWL</sup> Scheduled Procedure Step -- SQ:</p>
<p>(0040,0002) <sup>MWL</sup> Sched.</p>
<p>Proc.</p>
<p>Step Start Date (0040,0003) <sup>MWL</sup> Sched.</p>
<p>Proc.</p>
<p>Step Start Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>History (unlimited text)</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing</p>
<p><strong>HISTORY</strong> in OBX-3.2-</p>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p><em>For backward compatibility, the following element may be populated:</em></p>
<p>(0010,21B0) Additional Patient History</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reason for Study</p>
</blockquote></td>
<td><blockquote>
<p>OBR-31-Reason for Study</p>
</blockquote></td>
<td><blockquote>
<p><em>Should be displayed for Modality Worklist and stored in DICOM header in the following elements:</em></p>
<p>(0040,1002) Reason for the Requested Procedure AND (0040,1400) Requested Procedure Comments</p>
<p>(0032,1030) Reason for Study</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Technologist’s Comment</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing <strong>TECH COMMENT</strong> in OBX-3.2-Text</p>
</blockquote></td>
<td><blockquote>
<p>(0032,4000) Study Comment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Study Instance UID</p>
</blockquote></td>
<td><blockquote>
<p>ZDS-1.1-Study Instance UID</p>
</blockquote></td>
<td><blockquote>
<p><em>Value sent in HL7 message</em></p>
<p><em><strong>MUST</strong> be used by PACS.</em></p>
<p>(0020,000D) Study Instance UID</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Basic Report Data Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the elements of the Basic Report Data Set. This is not a normative mapping for Report data. PACS is responsible for its own storage of report data, but if the PACS owns a transcription system, the context identified by the given DICOM tags must be stored in the appropriate <u>outgoing</u> HL7 ORU^R01 messages (which are not a part of this specification).

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA Data Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Report Status</p>
</blockquote></td>
<td><blockquote>
<p>OBR-25-Result Status</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0210) Interpretation Type ID – CS: [REPORT, AMENDMENT]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Report Status – Codes: F for final and R for released not verified</p>
</blockquote></td>
<td><blockquote>
<p>OBR-25-Result Status</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0212) Interpretation Status ID – CS:</p>
<p>[TRANSCRIBED, APPROVED]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Date/Time of Transaction</p>
</blockquote></td>
<td><blockquote>
<p>OBR-22-Results Rpt/Status Chg – Date/Time if OBR- 18 = ‘R’</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0108) Interpretation Transcription Date</p>
<p>(4008,0109) Interpretation Transcription Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Impression Text</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing</p>
<p><strong>IMPRESSION</strong> in OBX-</p>
<p>3.2-Text</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0300) Impressions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Report Text</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing</p>
<p><strong>REPORT</strong> in OBX-3.2-Text</p>
</blockquote></td>
<td><blockquote>
<p>(4008,100B) Interpretation</p>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Diagnostic Code</p>
</blockquote></td>
<td><blockquote>
<p>OBX instance containing <strong>DIAGNOSTIC CODE</strong> in OBX-3.2-Text</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0117) Interpretation Diagnosis Code Sequence – SQ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Primary Interpreting Resident</p>
</blockquote></td>
<td><blockquote>
<p>OBR-33-Assistant Result Interpreter</p>
</blockquote></td>
<td><blockquote>
<p>(4008,010C) Interpretation Author</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verifying Physician</p>
</blockquote></td>
<td><blockquote>
<p>OBR-32-Principal Result Interpreter</p>
</blockquote></td>
<td><blockquote>
<p>(4008,0114) Physician Approving Interpretation</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The term *file*, when used as a proper term, shall be understood to mean a VA File Manager file on the local VistA system, unless this document explicitly indicates otherwise. Likewise, the term *table*, when used as a proper term, shall be understood to mean a table (HL7-defined or user-defined) cited in the Health Level Seven Standard.

> In the static definition portions of the profile, the following abbreviations are employed in the Usage column. Note the constraints on the HL7 definitions of CE and X: the conformant receiving application shall NOT raise an error if such fields are populated.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 30%" />
<col style="width: 55%" />
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
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Required</p>
</blockquote></td>
<td><blockquote>
<p>A conforming sending application shall populate all “R” elements with a non-empty value. A conforming receiving application shall process (save/print/archive/etc.) or ignore the information conveyed by required elements. A conforming receiving application must not raise an error due to the presence of a required element, but may raise an error due to the absence of a required element.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>Required but may be empty</p>
</blockquote></td>
<td><blockquote>
<p>The element may be missing from the message, but must be sent by the sending application if there is relevant data. A conforming sending application must be <strong>capable</strong> of providing all "RE" elements. If the conforming sending application knows the required values for the element, then it must send that element. If the conforming sending application does not know the required values, then that element will be omitted.</p>
<p>Receiving applications will be expected to process (save/print/archive/etc.) or ignore data contained in the element, but must be able to successfully process the message if the element is omitted (no error message should be generated because the element is missing).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Conditional</p>
</blockquote></td>
<td><blockquote>
<p>This usage has an associated condition predicate.</p>
<p><strong>If the predicate is satisfied:</strong></p>
<p>A conformant sending application must always send the element. A conformant receiving application must process or ignore data in the element. It may raise an error if the element is not present.</p>
<p><strong>If the predicate is NOT satisfied:</strong></p>
<p>A conformant sending application must NOT send the element. A conformant receiving application must NOT raise an error if the condition predicate is false, whether the element is present or not.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 30%" />
<col style="width: 55%" />
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
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Conditional but it may be empty</p>
</blockquote></td>
<td><blockquote>
<p>This usage has an associated condition predicate.</p>
<p><strong>If the predicate is satisfied:</strong></p>
<p>If the conforming sending application knows the required values for the element, then the application must send the element. If the conforming sending application does not know the values required for this element, then the element shall be omitted. The conforming sending application must be <strong>capable</strong> of knowing the element (when the predicate is true) for all ‘CE’ elements.</p>
<p>If the element is present, the conformant receiving application shall process (display/print/archive/etc.) or ignore the values of that element. If the element is not present, the conformant receiving application shall <strong>not</strong> raise an error due to the presence or absence of the element.</p>
<p><strong>If the predicate is not satisfied:</strong></p>
<p>A conformant sending application must NOT send the element. A conformant receiving application must NOT raise an error if the condition predicate is false, whether the element is present or not.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Retained for backward compatibility</p>
</blockquote></td>
<td><blockquote>
<p>A conforming sending application may populate this element. However, this element has been deprecated in the HL7 Standard and may be withdrawn from a future version of the Standard. A future version of this Profile may withdraw support for this field.</p>
<p>A conforming receiving application shall process (save/print/archive/etc.) or ignore the information conveyed. A conforming receiving application must not raise an error due to the presence or absence of a deprecated element.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>Not supported</p>
</blockquote></td>
<td><blockquote>
<p>For conformant sending applications, the element will not be sent. Conformant receiving applications shall ignore the element whether it is sent or not.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Patient Registration Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Registration transaction conveys the patient demographic and visit information that was captured at the point of encounter. This transaction is used both for inpatients (*i.e.,* those who are assigned a bed at the facility) and outpatients (*i.e.,* those who are not assigned a bed at the facility). It is implemented only for PACS that assert support for the Modality Worklist Service Class Provider.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/002.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Actor: VistA Imaging

> Role: Receives patient registration notification from VistA Patient Information Management System. Transmits appropriate demographic and encounter information to associated imaging systems including commercial Picture Archiving and Communication Systems (PACS).

> Actor: PACS

> Role: Receives and stores patient demographic and encounter information for use in building the Modality Worklist (MWL) when orders are received from VistA Radiology.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The actors in this use case shall perform the behaviors shown in the following activity diagram.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/003.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vista and PACS shall generate and process HL7 messages according to the following functional and business requirements.

### Patient Registration Message (ADT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging shall transmit an ADT message to PACS upon patient registration.

> If PACS accepts ADT messages, it shall process the message in conformance with the following requirements.

#### ADT Message Received – ICN Not Found

> When PACS receives an ADT registration message for a patient for which it does not find an ICN in its system, PACS will create a new patient record and will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit</u>](#basic-patient-data-set) [<u>Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above).

#### ADT Received for Existing ICN (Non-Update, Non-Merge)

> When PACS receives an ADT registration message for a patient for which it finds an ICN in its system, PACS will verify that name, SSN, sex, and DOB exactly match what is already in its system: if so, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic</u>](#basic-patient-data-set) [<u>Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section

> [0.2](#basic-patient-data-set) above); if not, PACS will put the message onto a reconciliation queue and notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1- acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 below, including code 204 (unknown key identifier) in component 4.

#### ADT Received for Sensitive/Employee Patient

> When PACS receives an ADT registration message for a patient whose VIP Indicator value in PV1-16 is set to E (employee) or S (sensitive), PACS shall safeguard the identity of the patient using VA rules for suppressing patient name and other identifying information.

#### ADT Received – More than 1 Value for Same Identifier

> When PACS receives an ADT registration message containing more than one value for the ICN, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment and will not update any patient record. The application acknowledgment shall contain a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1- error code and location*, as described in Section 1.6.10 below, including code 207 (application internal error) in component 4. PACS is responsible for notifying support staff and users of anomalies as needed.

### Acknowledgment Message (ACK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Original Mode ACK To Be Returned

> If PACS accepts ADT registration messages, it shall return an original mode ACK application acknowledgment, as defined in the HL7 Standard and prescribed by the IHE Radiology Technical Framework. The trigger event of the

> <span id="_bookmark17" class="anchor"></span>acknowledgment message shall be equal to the trigger event of the message that was received.

#### ERR Segment To Be Sent for AE and AR Conditions

> When an error is determined to have occurred, PACS shall return the acknowledgment code AE (Application Error) or AR (Application Reject) as appropriate, and shall populate Field ERR-1-error code and location with the relevant error information including the appropriate error code from HL7 Table 0357. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Message Type, Trigger Event, Version ID, or Processing Code to Cause Reject

> If the value received in *MSH-9.1-message type, MSH-9.2-trigger event, MSH-11- processing code,* or *MSH-12-version ID* is invalid, the value AR (application reject) shall be returned in *MSA-1-acknowledgment code*, and the appropriate value from HL7 Table 0357 shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Receiving Application or Receiving Facility to Cause Error

> If the value received in *MSH-5-receiving application* or *MSH-6-receiving facility* is invalid, the value AE (application error) shall be returned in *MSA-1- acknowledgment code*, and the value 103 (table value not found) shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 messages shall be populated and processed according to the following abstract message definitions.

### Patient Registration Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 36%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { NK1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Next of Kin / Associated Parties</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark18" class="anchor"></span>[ { ROL } ]</p>
</blockquote></th>
<th><blockquote>
<p>Role</p>
</blockquote></th>
<th><blockquote>
<p>RE</p>
</blockquote></th>
<th><blockquote>
<p>[0..2]</p>
</blockquote></th>
<th>12</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation / Result</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[2..2]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { AL1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Information</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..99]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DG1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Information</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ DRG ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Related Group</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { PR1</p>
</blockquote></td>
<td><blockquote>
<p>Procedures</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { GT1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Guarantor</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN1</p>
</blockquote></td>
<td><blockquote>
<p>Insurance</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ IN2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN3 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info. – Cert.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ ACC ]</p>
</blockquote></td>
<td><blockquote>
<p>Accident Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ UB1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ UB2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill 92 Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
</tbody>
</table>

### Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 34%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ACK Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSA</p>
</blockquote></td>
<td><blockquote>
<p>Message Acknowledgment</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ ERR ]</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

## Static Definition – Segment Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fields in HL7 messages shall be populated and processed according to the following Segment Attribute Tables.

### MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.1](#msh-segment-fields), [<u>MSH Segment Fields</u>](#msh-segment-fields), for a detailed explanation of the fields used in this segment.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00001</p>
</blockquote></td>
<td><blockquote>
<p>Field Separator</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00002</p>
</blockquote></td>
<td><blockquote>
<p>Encoding Characters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>00003</p>
</blockquote></td>
<td><blockquote>
<p>Sending Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>00004</p>
</blockquote></td>
<td><blockquote>
<p>Sending Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>00005</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>00006</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark20" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00007</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00008</p>
</blockquote></td>
<td><blockquote>
<p>Security</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>00009</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00010</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00011</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>VID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>00012</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00013</p>
</blockquote></td>
<td><blockquote>
<p>Sequence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00014</p>
</blockquote></td>
<td><blockquote>
<p>Continuation Pointer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>00015</p>
</blockquote></td>
<td><blockquote>
<p>Accept Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>00016</p>
</blockquote></td>
<td><blockquote>
<p>Application Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00017</p>
</blockquote></td>
<td><blockquote>
<p>Country Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0211</p>
</blockquote></td>
<td><blockquote>
<p>00692</p>
</blockquote></td>
<td><blockquote>
<p>Character Set</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00693</p>
</blockquote></td>
<td><blockquote>
<p>Principal Language of Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0356</p>
</blockquote></td>
<td><blockquote>
<p>01317</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Character Set Handling Scheme</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01598</p>
</blockquote></td>
<td><blockquote>
<p>Conformance Statement ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

### EVN Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the EVN Segment in HL7. Refer to [Section 1.6.2](#evn-segment-fields), [<u>EVN Segment Fields</u>](#evn-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>3</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>00099</p>
</blockquote></td>
<td><blockquote>
<p>Event Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00100</p>
</blockquote></td>
<td><blockquote>
<p>Recorded Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00101</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time Planned Event</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0062</p>
</blockquote></td>
<td><blockquote>
<p>00102</p>
</blockquote></td>
<td><blockquote>
<p>Event Reason Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>60</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0188</p>
</blockquote></td>
<td><blockquote>
<p>00103</p>
</blockquote></td>
<td><blockquote>
<p>Operator ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01278</p>
</blockquote></td>
<td><blockquote>
<p>Event Occurred</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>180</td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01534</p>
</blockquote></td>
<td><blockquote>
<p>Event Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PID Segment in HL7. Refer to [Section 1.6.3](#pid-segment-fields), [<u>PID Segment Fields</u>](#pid-segment-fields), for a more detailed explanation of the fields used by VistA.

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>0001</p>
</blockquote></td>
<td><blockquote>
<p>00104</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00105</p>
</blockquote></td>
<td><blockquote>
<p>Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00106</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identifier List</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00107</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Patient ID - PID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00108</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00109</p>
</blockquote></td>
<td><blockquote>
<p>Mother’s Maiden Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>00110</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Birth</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>00111</p>
</blockquote></td>
<td><blockquote>
<p>Sex</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00112</p>
</blockquote></td>
<td><blockquote>
<p>Patient Alias</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark21" class="anchor"></span><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0005</p>
</blockquote></td>
<td><blockquote>
<p>00113</p>
</blockquote></td>
<td><blockquote>
<p>Race</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XAD</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00114</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>00115</p>
</blockquote></td>
<td><blockquote>
<p>County Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>13</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00116</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Home</p>
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
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00117</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Business</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0296</p>
</blockquote></td>
<td><blockquote>
<p>00118</p>
</blockquote></td>
<td><blockquote>
<p>Primary Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0002</p>
</blockquote></td>
<td><blockquote>
<p>00119</p>
</blockquote></td>
<td><blockquote>
<p>Marital Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>17</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0006</p>
</blockquote></td>
<td><blockquote>
<p>00120</p>
</blockquote></td>
<td><blockquote>
<p>Religion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>18</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00121</p>
</blockquote></td>
<td><blockquote>
<p>Patient Account Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>19</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00122</p>
</blockquote></td>
<td><blockquote>
<p>SSN Number - Patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>20</td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>DLN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00123</p>
</blockquote></td>
<td><blockquote>
<p>Driver's License Number - Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>21</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00124</p>
</blockquote></td>
<td><blockquote>
<p>Mother's Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>22</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0189</p>
</blockquote></td>
<td><blockquote>
<p>00125</p>
</blockquote></td>
<td><blockquote>
<p>Ethnic Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td>23</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00126</p>
</blockquote></td>
<td><blockquote>
<p>Birth Place</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>24</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00127</p>
</blockquote></td>
<td><blockquote>
<p>Multiple Birth Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>25</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00128</p>
</blockquote></td>
<td><blockquote>
<p>Birth Order</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0171</p>
</blockquote></td>
<td><blockquote>
<p>00129</p>
</blockquote></td>
<td><blockquote>
<p>Citizenship</p>
</blockquote></td>
</tr>
<tr class="even">
<td>27</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0172</p>
</blockquote></td>
<td><blockquote>
<p>00130</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Military Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>28</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0212</p>
</blockquote></td>
<td><blockquote>
<p>00739</p>
</blockquote></td>
<td><blockquote>
<p>Nationality</p>
</blockquote></td>
</tr>
<tr class="even">
<td>29</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00740</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Date and Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>30</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00741</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>31</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>01535</p>
</blockquote></td>
<td><blockquote>
<p>Identity Unknown Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>32</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0445</p>
</blockquote></td>
<td><blockquote>
<p>01536</p>
</blockquote></td>
<td><blockquote>
<p>Identity Reliability Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>33</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01537</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>34</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01538</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td>35</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0446</p>
</blockquote></td>
<td><blockquote>
<p>01539</p>
</blockquote></td>
<td><blockquote>
<p>Species Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>36</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0447</p>
</blockquote></td>
<td><blockquote>
<p>01540</p>
</blockquote></td>
<td><blockquote>
<p>Breed Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>37</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01541</p>
</blockquote></td>
<td><blockquote>
<p>Strain</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>38</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0429</p>
</blockquote></td>
<td><blockquote>
<p>01542</p>
</blockquote></td>
<td><blockquote>
<p>Production Class Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PV1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PV1 Segment in HL7. Refer to [Section 1.6.4](#pv1-segment-fields), [<u>PV1 Segment Fields</u>](#pv1-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00131</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PV1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0004</p>
</blockquote></td>
<td><blockquote>
<p>00132</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00133</p>
</blockquote></td>
<td><blockquote>
<p>Assigned Patient Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0007</p>
</blockquote></td>
<td><blockquote>
<p>00134</p>
</blockquote></td>
<td><blockquote>
<p>Admission Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00135</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00136</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00137</p>
</blockquote></td>
<td><blockquote>
<p>Attending Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00138</p>
</blockquote></td>
<td><blockquote>
<p>Referring Doctor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00139</p>
</blockquote></td>
<td><blockquote>
<p>Consulting Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0069</p>
</blockquote></td>
<td><blockquote>
<p>00140</p>
</blockquote></td>
<td><blockquote>
<p>Hospital Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00141</p>
</blockquote></td>
<td><blockquote>
<p>Temporary Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0087</p>
</blockquote></td>
<td><blockquote>
<p>00142</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Test Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0092</p>
</blockquote></td>
<td><blockquote>
<p>00143</p>
</blockquote></td>
<td><blockquote>
<p>Re-admission Indicator</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0023</p>
</blockquote></td>
<td><blockquote>
<p>00144</p>
</blockquote></td>
<td><blockquote>
<p>Admit Source</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td><blockquote>
<p>0009</p>
</blockquote></td>
<td><blockquote>
<p>00145</p>
</blockquote></td>
<td><blockquote>
<p>Ambulatory Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0099</p>
</blockquote></td>
<td><blockquote>
<p>00146</p>
</blockquote></td>
<td><blockquote>
<p>VIP Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00147</p>
</blockquote></td>
<td><blockquote>
<p>Admitting Doctor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0018</p>
</blockquote></td>
<td><blockquote>
<p>00148</p>
</blockquote></td>
<td><blockquote>
<p>Patient Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00149</p>
</blockquote></td>
<td><blockquote>
<p>Visit Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>FC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0064</p>
</blockquote></td>
<td><blockquote>
<p>00150</p>
</blockquote></td>
<td><blockquote>
<p>Financial Class</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0032</p>
</blockquote></td>
<td><blockquote>
<p>00151</p>
</blockquote></td>
<td><blockquote>
<p>Charge Price Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0045</p>
</blockquote></td>
<td><blockquote>
<p>00152</p>
</blockquote></td>
<td><blockquote>
<p>Courtesy Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0046</p>
</blockquote></td>
<td><blockquote>
<p>00153</p>
</blockquote></td>
<td><blockquote>
<p>Credit Rating</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0044</p>
</blockquote></td>
<td><blockquote>
<p>00154</p>
</blockquote></td>
<td><blockquote>
<p>Contract Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00155</p>
</blockquote></td>
<td><blockquote>
<p>Contract Effective Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00156</p>
</blockquote></td>
<td><blockquote>
<p>Contract Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00157</p>
</blockquote></td>
<td><blockquote>
<p>Contract Period</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0073</p>
</blockquote></td>
<td><blockquote>
<p>00158</p>
</blockquote></td>
<td><blockquote>
<p>Interest Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0110</p>
</blockquote></td>
<td><blockquote>
<p>00159</p>
</blockquote></td>
<td><blockquote>
<p>Transfer to Bad Debt Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00160</p>
</blockquote></td>
<td><blockquote>
<p>Transfer to Bad Debt Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0021</p>
</blockquote></td>
<td><blockquote>
<p>00161</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Agency Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00162</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Transfer Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00163</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Recovery Amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0111</p>
</blockquote></td>
<td><blockquote>
<p>00164</p>
</blockquote></td>
<td><blockquote>
<p>Delete Account Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00165</p>
</blockquote></td>
<td><blockquote>
<p>Delete Account Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0112</p>
</blockquote></td>
<td><blockquote>
<p>00166</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Disposition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td>25</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0113</p>
</blockquote></td>
<td><blockquote>
<p>00167</p>
</blockquote></td>
<td><blockquote>
<p>Discharged to Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0114</p>
</blockquote></td>
<td><blockquote>
<p>00168</p>
</blockquote></td>
<td><blockquote>
<p>Diet Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0115</p>
</blockquote></td>
<td><blockquote>
<p>00169</p>
</blockquote></td>
<td><blockquote>
<p>Servicing Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0116</p>
</blockquote></td>
<td><blockquote>
<p>00170</p>
</blockquote></td>
<td><blockquote>
<p>Bed Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0117</p>
</blockquote></td>
<td><blockquote>
<p>00171</p>
</blockquote></td>
<td><blockquote>
<p>Account Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00172</p>
</blockquote></td>
<td><blockquote>
<p>Pending Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00173</p>
</blockquote></td>
<td><blockquote>
<p>Prior Temporary Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00174</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00175</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00176</p>
</blockquote></td>
<td><blockquote>
<p>Current Patient Balance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00177</p>
</blockquote></td>
<td><blockquote>
<p>Total Charges</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00178</p>
</blockquote></td>
<td><blockquote>
<p>Total Adjustments</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00179</p>
</blockquote></td>
<td><blockquote>
<p>Total Payments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>00180</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Visit ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0326</p>
</blockquote></td>
<td><blockquote>
<p>01226</p>
</blockquote></td>
<td><blockquote>
<p>Visit Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>01274</p>
</blockquote></td>
<td><blockquote>
<p>Other Healthcare Provider</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ROL Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ROL Segment is used to give more complete information about the patient’s referring and attending physicians than is permitted by the PV1 Segment. Specifically, the ROL Segment allows for the transmission of multiple callback numbers for each physician.

> The following is a listing of all the fields defined for the ROL Segment in HL7. Refer to [Section 1.6.5](#rol-segment-fields), [<u>ROL Segment Fields</u>](#rol-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01206</p>
</blockquote></td>
<td><blockquote>
<p>Role Instance ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0287</p>
</blockquote></td>
<td><blockquote>
<p>00816</p>
</blockquote></td>
<td><blockquote>
<p>Action Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0443</p>
</blockquote></td>
<td><blockquote>
<p>01197</p>
</blockquote></td>
<td><blockquote>
<p>Role-ROL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01198</p>
</blockquote></td>
<td><blockquote>
<p>Role Person</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01199</p>
</blockquote></td>
<td><blockquote>
<p>Role Begin Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01200</p>
</blockquote></td>
<td><blockquote>
<p>Role End Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01201</p>
</blockquote></td>
<td><blockquote>
<p>Role Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01205</p>
</blockquote></td>
<td><blockquote>
<p>Role Action Reason</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01510</p>
</blockquote></td>
<td><blockquote>
<p>Provider Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0406</a></p>
</blockquote></td>
<td><blockquote>
<p>01461</p>
</blockquote></td>
<td><blockquote>
<p>Organization Unit Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XAD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00679</p>
</blockquote></td>
<td><blockquote>
<p>Office/Home Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..8]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00678</p>
</blockquote></td>
<td><blockquote>
<p>Phone</p>
</blockquote></td>
</tr>
</tbody>
</table>

### DG1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the DG1 Segment in HL7. Refer to [Section 1.6.6](#dg1-segment-fields), [<u>DG1 Segment Fields</u>](#dg1-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00375</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - DG1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0053</td>
<td><blockquote>
<p>00376</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Coding Method</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>0051</td>
<td><blockquote>
<p>00377</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Code - DG1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>40</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00378</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Description</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00379</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>0052</td>
<td><blockquote>
<p>00380</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0118</td>
<td><blockquote>
<p>00381</p>
</blockquote></td>
<td><blockquote>
<p>Major Diagnostic Category</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0055</td>
<td><blockquote>
<p>00382</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic Related Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0136</td>
<td><blockquote>
<p>00383</p>
</blockquote></td>
<td><blockquote>
<p>DRG Approval Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0056</td>
<td><blockquote>
<p>00384</p>
</blockquote></td>
<td><blockquote>
<p>DRG Grouper Review Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0083</td>
<td><blockquote>
<p>00385</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00386</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Days</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00387</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Cost</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00388</p>
</blockquote></td>
<td><blockquote>
<p>Grouper Version And Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0359</td>
<td><blockquote>
<p>00389</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Priority</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00390</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosing Clinician</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><a href="#_bookmark0">0228</a></td>
<td><blockquote>
<p>00766</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Classification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0136</td>
<td><blockquote>
<p>00767</p>
</blockquote></td>
<td><blockquote>
<p>Confidential Indicator</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark23" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00768</p>
</blockquote></td>
<td><blockquote>
<p>Attestation Date/Time</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the ADT registration message, the OBX Segment is used to communicate height and weight of the patient. The following is a listing of all the fields defined for the OBX Segment in HL7. Refer to Section [1.6.7](#obx-segment-fields), [<u>OBX Segment Fields</u>](#obx-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00569</p>
</blockquote></td>
<td><blockquote>
<p>Set ID – OBX</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0125</p>
</blockquote></td>
<td><blockquote>
<p>00570</p>
</blockquote></td>
<td><blockquote>
<p>Value Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00571</p>
</blockquote></td>
<td><blockquote>
<p>Observation Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00572</p>
</blockquote></td>
<td><blockquote>
<p>Observation Sub-ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>65536<a href="#_bookmark24"><sup>†</sup></a></td>
<td></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00573</p>
</blockquote></td>
<td><blockquote>
<p>Observation Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00574</p>
</blockquote></td>
<td><blockquote>
<p>Units</p>
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
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00575</p>
</blockquote></td>
<td><blockquote>
<p>Reference Range</p>
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
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0078</p>
</blockquote></td>
<td><blockquote>
<p>00576</p>
</blockquote></td>
<td><blockquote>
<p>Abnormal Flags</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>NM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00577</p>
</blockquote></td>
<td><blockquote>
<p>Probability</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00578</p>
</blockquote></td>
<td><blockquote>
<p>Nature of Abnormal Test</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0085</p>
</blockquote></td>
<td><blockquote>
<p>00579</p>
</blockquote></td>
<td><blockquote>
<p>Observation Result Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00580</p>
</blockquote></td>
<td><blockquote>
<p>Date Last Observation Normal Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00581</p>
</blockquote></td>
<td><blockquote>
<p>User Defined Access Checks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00582</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Observation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00583</p>
</blockquote></td>
<td><blockquote>
<p>Producer’s ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XCN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00584</p>
</blockquote></td>
<td><blockquote>
<p>Responsible Observer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00936</p>
</blockquote></td>
<td><blockquote>
<p>Observation Method</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01479</p>
</blockquote></td>
<td><blockquote>
<p>Equipment Instance Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01480</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Analysis</p>
</blockquote></td>
</tr>
</tbody>
</table>

### AL1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the AL1 Segment in HL7. Refer to [Section 1.6.8](#al1-segment-fields), [<u>AL1 Segment Fields</u>](#al1-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00203</p>
</blockquote></td>
<td><blockquote>
<p>Set ID – AL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0127</p>
</blockquote></td>
<td><blockquote>
<p>00204</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00205</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Code/Mnemonic/Description</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0128</p>
</blockquote></td>
<td><blockquote>
<p>00206</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Severity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..99]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00207</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Reaction</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00208</p>
</blockquote></td>
<td><blockquote>
<p>Identification Date</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark24" class="anchor"></span><sup>†</sup> The length and data type of this field are variable, depending on *OBX-2-Value Type*.

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the MSA Segment in HL7. MSA is used only in the acknowledgment message. Refer to Section [1.6.9](#msa-segment-fields), [<u>MSA Segment Fields</u>](#msa-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>0003</td>
<td><blockquote>
<p>00018</p>
</blockquote></td>
<td><blockquote>
<p>Acknowledgment Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00010</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00020</p>
</blockquote></td>
<td><blockquote>
<p>Text Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>15</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00021</p>
</blockquote></td>
<td><blockquote>
<p>Expected Sequence Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0102</td>
<td><blockquote>
<p>00022</p>
</blockquote></td>
<td><blockquote>
<p>Delayed Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00023</p>
</blockquote></td>
<td><blockquote>
<p>Error Condition</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the ERR Segment in HL7. ERR is used only in the acknowledgment message. Refer to Section [1.6.10](#err-segment-fields), [<u>ERR Segment</u>](#err-segment-fields) [<u>Fields</u>](#err-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>80</td>
<td>CM</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..999]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00024</p>
</blockquote></td>
<td><blockquote>
<p>Error Code and Location</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSH-1-Field Separator

> This field contains the top-level delimiter for HL7 elements within segments.

#### MSH-2-Encoding Characters

> This field contains the component separator (secondary element delimiter), repetition separator, escape character, and subcomponent separator (tertiary element delimiter).

#### MSH-3-Sending Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA registration message, Component 1 of this field shall be populated with the value VISTA IMAGING from user-defined Table 0361, *Sending/Receiving Application*. PACS shall return this value in component MSH-

> <span id="_bookmark29" class="anchor"></span>5.1 of the acknowledgment message. Components 2 and 3 of MSH-3 are not valued.

#### MSH-4-Sending Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA registration message, Component 1 of this field shall be populated from user-defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was generated. PACS shall return this value in component MSH-6.1 of the acknowledgment message. Components 2 and 3 of MSH-4 are not valued.

#### MSH-5-Receiving Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0361, *Sending/Receiving Application*, with the name of the PACS application. PACS shall return this value in component MSH-3.1 of the acknowledgment message. Components 2 and 3 of MSH-5 are not valued.

#### MSH-6-Receiving Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was received. PACS shall return this value in field MSH-4 of the acknowledgment message. Components 2 and 3 of MSH-6 are not valued.

#### MSH-7-Date/Time of Message

> This field contains the date and time that the sending system built the message.

#### MSH-9-Message Type

> This field is of data type CM. Its components are as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark31" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>Trigger Event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0354</p>
</blockquote></td>
<td><blockquote>
<p>Message Structure</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

> *MSH-9.1-Message Type*

> This component contains a value from HL7 Table 0076, *Message Type*. For the registration message, it will always contain the value ADT.

#### MSH-9.2-Trigger Event

> This component will contain one of the following values from HL7 Table 0003,

> *Event Type*.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A01</p>
</blockquote></td>
<td><blockquote>
<p>Admit/visit notification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A02</p>
</blockquote></td>
<td><blockquote>
<p>Transfer a patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A03</p>
</blockquote></td>
<td><blockquote>
<p>Discharge/end visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A04</p>
</blockquote></td>
<td><blockquote>
<p>Register a patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A08</p>
</blockquote></td>
<td><blockquote>
<p>Update patient information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A11</p>
</blockquote></td>
<td><blockquote>
<p>Cancel admission</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A12</p>
</blockquote></td>
<td><blockquote>
<p>Cancel transfer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A13</p>
</blockquote></td>
<td><blockquote>
<p>Cancel discharge</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A40</p>
</blockquote></td>
<td><blockquote>
<p>Merge patient – patient identifier list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A47</p>
</blockquote></td>
<td><blockquote>
<p>Change patient identifier list</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-10-Message Control ID

> This field will contain a unique identifier for the message.

#### MSH-11-Processing ID

> This field is of type PT, which is defined as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0103</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0207</p>
</blockquote></td>
<td><blockquote>
<p>Processing Mode</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

#### MSH-11.1-Processing ID

> This field contains one of the following values from HL7 Table 0103, *Processing ID.*

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark32" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>Production</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Debugging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T</td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-11.2-Processing Mode

> This field contains one of the following values from HL7 Table 0207, *Processing Mode*.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A</td>
<td><blockquote>
<p>Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>R</td>
<td><blockquote>
<p>Restore from archive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>I</td>
<td><blockquote>
<p>Initial load</p>
</blockquote></td>
</tr>
<tr class="even">
<td>T</td>
<td><blockquote>
<p>Current processing, transmitted at intervals (scheduled or on demand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>not present</p>
</blockquote></td>
<td><blockquote>
<p>Not present (the default, meaning <em>current</em> processing)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-12-Version ID

> This field is of type VID, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internationalization Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internal Version ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This field’s first component will always contain the value 2.3.1 from HL7 Table 0104, *Version ID*. Although the VistA message pre-adopts certain Version 2.4 structures, such as the ROL segment, receivers that are unable to recognize Version 2.4 may use Version 2.3.1 syntax rules as prescribed by IHE. It is expected that receivers not now using HL7 Version 2.3.1 will be able to process the V2.3.1 messages according to the HL7 rules for backward compatibility. At such time as IHE is revised to a later version of HL7, receivers will be expected to adapt to the new structures within a stated period of time following the revision.

> Other components of this field will not be used.

#### MSH-17-Country Code

> This field is of type ID. It will always contain the value USA from the ISO 3166 country code table.

### EVN Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### EVN-1-Event Type Code

> This field contains the 3-character code of the trigger event being communicated. It is retained for backward compatibility with versions of HL7 that do not communicate the event type in the second component of [<u>MSH-9-Message Type</u>](#msh-9-message-type).

#### EVN-2-Recorded Date/Time

> This field contains the date and time that the event was recorded in the system.

#### EVN-6-Event Occurred

> This field contains the date and time that the event actually took place. If it is not known when the event actually took place, this field is left blank.

### PID Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID-3-Patient Identifier List

> Field PID-3 is used to transmit the patient Integration Control Number (ICN). This field is of data type CX, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Check Digit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

> *PID-3.1-ID*

> This is the alphanumeric identification string.

#### PID-3.4-Assigning Authority

> This component contains the entity that assigned the identifier value in *PID-3.1- ID*. It is of data type HD, which has 3 subcomponents defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> At present, only the first subcomponent should be considered for the purpose of identifying the assigning authority. Subcomponent 1 will contain the value

> <span id="_bookmark37" class="anchor"></span>USVHA*,* meaning United States Veterans Health Administration, from user- defined Table 0300, *Namespace ID*.

> In future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-3.5-Identifier Type

> The value in this component distinguishes the kind of identifier contained in *PID- 3.1-ID*. It will contain the value NI, meaning National unique individual identifier, from user-defined Table 0203, *Identifier Type*.

#### PID-5-Patient Name

> This field is of data type XPN, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>35</td>
<td><blockquote>
<p>FN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0200</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 7, Name Type Code, indicates the type of name given in Components 1-6, such as legal, birth name, or alias. At present, VistA only uses name type L (legal).

#### PID-7-Date/Time of Birth

> This is the date and time that the patient was born, as far as is known. It may be as imprecise as the four-digit birth year (*e.g.*, 1962).

#### PID-8-Sex

> This field contains the sex of the patient. It is populated with one of the following values from user-defined Table 0001, *Sex*, if a value is known.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>Female</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Male</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Unknown</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10-Race

> This field contains a code for the patient’s race. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark38" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-10.1-Identifier

> This component contains the RACE INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0005, *Race*.

#### PID-10.3-Name of Coding System

> The value of this component shall be 0005.

#### PID-10.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1002-5</p>
</blockquote></td>
<td><blockquote>
<p>AMERICAN INDIAN OR ALASKA NATIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2028-9</p>
</blockquote></td>
<td><blockquote>
<p>ASIAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2054-5</p>
</blockquote></td>
<td><blockquote>
<p>BLACK OR AFRICAN AMERICAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2076-8</p>
</blockquote></td>
<td><blockquote>
<p>NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2106-3</p>
</blockquote></td>
<td><blockquote>
<p>WHITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10.6-Name of Coding System

> This component shall be populated CDC.

#### PID-11-Patient Address

> This field contains the patient’s address. It is of data type XAD, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="7"><blockquote>
<p>0190</p>
</blockquote></td>
<td><blockquote>
<p>Street Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Other Designation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>City</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>State or Province</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>ZIP or Postal Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Country</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Address Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark39" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Other Geographic Designation</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>County/Parish Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0288</p>
</blockquote></td>
<td><blockquote>
<p>Census Tract</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Address Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13-Phone Number – Home

> This field contains the patient’s home telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### PID-13.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-13.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14-Phone Number – Business

> This field contains the patient’s work telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### PID-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-14.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-19-SSN Number – Patient

> This field carries the patient Social Security Number, for backward compatibility with versions of HL7 prior to Version 2.3.1. The Social Security Number is a secondary patient identifier. For the primary patient identifier, use the Integration Control Number from [<u>PID-3-Patient Identifier List</u>](#pid-3-patient-identifier-list).

#### PID-22-Ethnic Group

> This field contains a code indicating whether the patient is of Hispanic descent. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-22.1-Identifier

> This component contains the ETHNICITY INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0189, *Ethnic Group*.

#### PID-22.3-Name of Coding System

> The value of this component shall be 0189.

#### PID-22.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2135-2</p>
</blockquote></td>
<td><blockquote>
<p>HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2186-5</p>
</blockquote></td>
<td><blockquote>
<p>NOT HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-22.6-Name of Coding System

> This component shall be populated CDC.

### PV1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PV1-2-Patient Class

> This field designates whether the patient is an inpatient (I) or an outpatient (O).

#### PV1-3-Assigned Patient Location

> For inpatient, this field designates the patient’s location in the medical center. The data type of this field is PL, which is defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark43" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0302</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0303</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0304</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0306</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0305</p>
</blockquote></td>
<td><blockquote>
<p>Person Location Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0307</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0308</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Location Description</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VistA sends Component 1, Point of Care, as three subcomponents, of which the first is an internal entry number into the VistA WARD LOCATION File (#42), and the second is the name of the ward location; the third is the internal designator of the WARD LOCATION File and should be ignored.

#### PV1-7-Attending Doctor

> This is the physician responsible for the care of the patient during the present encounter. VistA values this field for inpatient encounters only.

> The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-8-Referring Doctor

> This is the patient’s primary physician. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="4"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark46" class="anchor"></span><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="11"></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-10-Hospital Service

> This is the treating specialty assigned to the patient with the most recent movement. VistA values this field for inpatient encounters only. When populated, it contains a value from user-defined Table 0069, *Hospital Service*; VistA sends values from the HOSPITAL LOCATION File (#44).

#### PV1-15-Ambulatory Status

> This field indicates any permanent or transient conditions affecting the patient’s mode of transportation. It may contain one or more values from user-defined Table 0009, *Ambulatory Status.* If the patient’s ambulatory status is not known, this field is not populated.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A0</p>
</blockquote></td>
<td><blockquote>
<p>No functional limitations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A2</p>
</blockquote></td>
<td><blockquote>
<p>Wheelchair/stretcher bound</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B6</p>
</blockquote></td>
<td><blockquote>
<p>Pregnant</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PV1-16-VIP Indicator

> This field is used to indicate that the patient is an employee, or that patient record is sensitive and should not be made available for general personnel access. If one of these conditions applies, VistA populates this field with one of the following values from user-defined Table 0099, *VIP Indicator.*

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>E</td>
<td><blockquote>
<p>Patient is a VA employee</p>
</blockquote></td>
</tr>
<tr class="even">
<td>S</td>
<td><blockquote>
<p>Patient record is sensitive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ES</p>
</blockquote></td>
<td><blockquote>
<p>Patient is a VA employee and patient record is sensitive</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PV1-19-Visit

> This field indicates the patient movement with which this registration is associated. It contains a pointer to the VistA PATIENT MOVEMENT File.

#### PV1-44-Admit Date/Time

> This is the date and time when the patient was admitted (if the patient is an inpatient) or when the current encounter began (if the patient is an outpatient).

### ROL Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ROL-1-Role Instance ID

> This is the ordinal number of this occurrence of the ROL Segment under the PV1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### ROL-2-Action Code

> This field will always be valued UP, which indicates that the receiving system should update its database with the information contained in the ROL Segment(s) being sent in the current message.

#### ROL-3-Role

> This field indicates the involvement with the activity being transmitted. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component *PID-10.1-Identifier* is valued AT to indicate the attending physician or RP to indicate the referring physician.

#### ROL-4-Role Person

> This is the name of the person (physician) whose information is being transmitted. Its structure is identical to that of [<u>PV1-7-Attending Doctor</u>](#pv1-7-attending-doctor) and [<u>PV1-8-Referring</u>](#pv1-8-referring-doctor) [<u>Doctor</u>](#pv1-8-referring-doctor).

#### ROL-12-Phone

> This is the telephone number of the person (physician) whose information is being transmitted. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark49" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

> *ROL-12.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]*

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### ROL-12.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with one of the following values from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>Beeper Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ROL-12.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with one of the following values from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>Fax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>Beeper</p>
</blockquote></td>
</tr>
</tbody>
</table>

### DG1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### DG1-1-Set ID

> This is the ordinal number of this occurrence of the DG1 Segment under the PV1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### DG1-3-Diagnosis Code

> This field is of data type CE (Coded Element), which contains 6 components. Only the second component, “Text”, is populated. It contains the name of the diagnosis.

#### DG1-6-Diagnosis Type

> This field is of data type IS (coded value for user-defined tables). It will contain one of the following values from user-defined Table 0052, *Diagnosis Type*.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 75%" />
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
<td>A</td>
<td><blockquote>
<p>Admitting</p>
</blockquote></td>
<td><blockquote>
<p>The diagnosis associated with the patient admission</p>
</blockquote></td>
</tr>
<tr class="even">
<td>W</td>
<td><blockquote>
<p>Working</p>
</blockquote></td>
<td><blockquote>
<p>A diagnosis associated with any patient movement besides the admission</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBX Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-1-Set ID

> This is the ordinal number of this occurrence of the OBX Segment. The first occurrence is labeled 1, the second 2, and so on.

#### OBX-2-Value Type

> This field contains the data type of the information carried in *OBX-5-Observation Value.* It is populated with the value ST from HL7 Table 0125, *Value Type*.

#### OBX-3-Observation Identifier

> This field classifies the kind of information carried in *OBX-5-Observation Value.*

> Its data type is CE, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the ADT message, Component 2, Text, will contain either HEIGHT or

> WEIGHT. Other components are not populated.

#### OBX-5-Observation Value

> This field contains the actual value whose data type is given in *OBX-2-Value Type* and whose classification is given in *OBX-3-Observation Identifier*. Its formatting follows the rules for the data type given in OBX-2.

#### OBX-6-Units

> This field contains the units of the observation. Its data type is CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Components 1, *Identifier*, and 2, *Text*, are populated as follows.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Identifier</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Text</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>m</td>
<td><blockquote>
<p>meter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>kg</p>
</blockquote></td>
<td><blockquote>
<p>kilogram</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 3 is always valued ISO+, indicating the use of units of measure from ISO Standard 2955-1983.

#### OBX-11-Observation Result Status

> This field is of data type ID. In the ADT message, it is populated with the value F (final results) from HL7 Table 0085, *Observation Result Status Codes Interpretation.*

### AL1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### AL1-1-Set ID

> This is the ordinal number of this occurrence of the AL1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### AL1-2-Allergy Type

> This field indicates whether the allergy is to a drug and/or food. VistA shall populate this field with one of the following values from user-defined Table 0127, *Allergy Type*.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D</td>
<td><blockquote>
<p>Drug allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DF</p>
</blockquote></td>
<td><blockquote>
<p>Drug/food allergy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DFO</p>
</blockquote></td>
<td><blockquote>
<p>Drug/food/other allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DO</p>
</blockquote></td>
<td><blockquote>
<p>Drug/other allergy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>Food allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FO</p>
</blockquote></td>
<td><blockquote>
<p>Food/other allergy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>O</td>
<td><blockquote>
<p>Other allergy</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### AL1-3-Allergy Code/Mnemonic/Description

> The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 2, Text, is valued with the name of the allergy. Other components are not valued.

#### AL1-5-Allergy Reaction

> This field contains reactions related to this allergy.

#### AL1-6-Identification Date

> This field contains the date that the allergy was verified.

### MSA Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSA-1-Acknowledgment Code

> This field indicates whether the message was processed successfully. Original mode acknowledgment shall be used. PACS shall populate this field with one of the following values from HL7 Table 0008, *Acknowledgment Code*.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td><blockquote>
<p>Application Accept</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AE</p>
</blockquote></td>
<td><blockquote>
<p>Application Error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AR</p>
</blockquote></td>
<td><blockquote>
<p>Application Reject</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSA-2-Message Control ID

> This field contains the value of *MSH-10-Message Control ID* from the message being acknowledged.

#### MSA-3-Text Message

> This field contains a narrative description of the error found in the message. It is preferred that *ERR-1-Error Code and Location* be used to communicate precise error information.

#### MSA-6-Error Condition

> This field contains an encoded description of the error found in the message. It is preferred that *ERR-1-Error Code and Location* be used to communicate precise error information.

> <span id="_bookmark57" class="anchor"></span>Data type CE is used for this field, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>0357</p>
</blockquote></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Error condition codes are defined in HL7 Table 0357, *Message Error Condition.* If HL7 Table 0357 is used, the code shall be sent in Component 1, the description in Component 2, and the text HL70357 in Component 3.

### ERR Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ERR-1-Error Code and Location

> This field contains an encoded description of the error found in the message and the location of the error. Data type CM is used for this field. The components of this field are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="4"></td>
<td><blockquote>
<p>Segment ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Sequence</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Field Position</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying Error</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *ERR-1.1-Segment ID*

> This component contains the 3-character tag of the segment in the received message in which the error occurred. If the error is not related to a segment in the received message, this component is left blank.

#### ERR-1.2-Sequence

> This component is an index to the ordinal occurrence of the segment in the received message whose segment ID is given in ERR-1.1. If only one such segment occurred in the received message, or if the error is not related to a segment in the received message, this component is left blank.

#### ERR-1.3-Field Position

> This component is an index to the ordinal position of the field within the segment ID given in ERR-1.1. If the error is not related to a segment in the received message, this component is left blank.

#### ERR-1.4-Code Identifying Error

> This component contains an encoded description of the error found in the message. Data type CE is used for this field, whose subcomponents are defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>0357</p>
</blockquote></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>3</p>
<p>4</p></td>
<td><blockquote>
<p>250</p>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Error condition codes are defined in HL7 Table 0357, *Message Error Condition.* The appropriate entry from the Value column in the table below shall be sent in Subcomponent 1, and the corresponding text from the Description column shall be sent in Subcomponent 2. (The text in the Comment column is not sent.)

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
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>Segment sequence error</p>
</blockquote></td>
<td><blockquote>
<p>Error: The message segments were not in the proper order, or required segments are missing.</p>
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
<p>Error: The field contained data of the wrong data type, e.g. an NM field contained "FOO".</p>
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

> The text HL70357 shall be sent in Subcomponent 3.

# Patient Update Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Update transaction conveys changes to patient information, including demographics, patient identification, patient location/class changes, and patient merges. These changes may occur at any time for a patient record. This transaction is used both for inpatients (*i.e.,* those who are assigned a bed at the facility) and outpatients (*i.e.,* those who are not assigned a bed at the facility) if the patient has been previously registered.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/004.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Actor: VistA Imaging

> Role: Receives patient registration or update notification from VistA Patient Information Management System. Transmits appropriate demographic and encounter information to associated imaging systems including commercial Picture Archiving and Communication Systems (PACS).

> Actor: PACS

> Role: Tracks patient identifier, demographic and encounter information associated with orders.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The actors in this use case shall perform the behaviors shown in the following activity diagram.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/005.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vista and PACS shall generate and process HL7 messages according to the following functional and business requirements.

### Patient Update Message (ADT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging shall transmit an ADT message to PACS when patient information changes, including when patient records are merged. PACS shall process the message in conformance with the following requirements.

#### Update Received for Existing ICN (Non-Demo, Non-Merge)

> When PACS receives an ADT update message (other than A08-update patient information, A40-merge, or A47-change ID) for a patient for which it finds an ICN in its system, PACS will verify that name, SSN, sex, and DOB exactly match what is already in its system: if so, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above); if not, PACS will put the message onto a reconciliation queue and notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section

> 1.6.10 above, including code 204 (unknown key identifier) in component 4.

1.  If the update is a discharge, PACS shall display the patient’s discharged status.
2.  If the update is a transfer, PACS shall display the patient’s new location (*i.e.*, the location to which the patient was transferred).

#### Update Received for ICN Not on File (Non-Demo, Non-Merge)

> When PACS receives an ADT update message (other than A08-update patient information, A40-merge, or A47-change ID) for a patient for which it does not find an ICN in its system, PACS will create a new patient record and will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above).

#### Update Received for Existing ICN (Update Demographics)

> When PACS receives an ADT^A08 (update patient information) message for a patient for which finds an ICN already in its system, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic</u>](#basic-patient-data-set) [<u>Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section

> [0.2](#basic-patient-data-set) above).

#### Update Received for ICN Not on File (Update Demographics)

> When PACS receives an ADT^A08 (update patient information) message for a patient for which it does not find an ICN already in its system, PACS will create a new patient record and will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above).

#### Update Received for Existing ICN (Merge)

> When PACS receives an ADT^A40 (merge patient - patient identifier list) message for a patient for which it finds the merge-to ICN in its system, the PACS operator or administrator may review the patient IDs to be merged for correctness. Upon

> <span id="_bookmark62" class="anchor"></span>approval by the operator or administrator, if needed, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic</u>](#basic-patient-data-set) [<u>Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section

> [0.2](#basic-patient-data-set) above).

1.  If it finds the merge-from ICN in its system, PACS will retire the merge- from ICN as a lookup key.
2.  PACS will reject lookup requests for the retired merge-from ICN.

#### Update Received for ICN Not on File (Merge)

> When PACS receives an ADT^A40 (merge patient - patient identifier list) message for a patient for which it does not find the merge-to ICN in its system, PACS will create a new patient record and will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section

> [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above).

1.  If it finds the merge-from ICN in its system, PACS will retire the merge- from ICN as a lookup key.
2.  PACS will reject lookup requests for the retired merge-from ICN.

#### Update Received for Existing ICN (Change ID)

> When PACS receives an ADT^A47 (change patient identifier list) message for a patient for which it finds the change-from ICN (from *MRG-1-Prior Patient Identifier List*) in its system, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above). It will change the identifier value found in *MRG-1-Prior Patient Identifier List* to the value found for the corresponding assigning authority in *PID-3-Patient Identifier List.*

1.  PACS will retire the change-from ICN as a lookup key.
2.  PACS will reject lookup requests for the retired change-from ICN.

#### Update Received for ICN Not on File (Change ID)

> When PACS receives an ADT^A47 (change patient identifier list) message for a patient for which it does not find the change-from ICN or SSN (from *MRG-1- Prior Patient Identifier List*) in its system, PACS will create a new patient record and will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above).

#### Update Received – More than 1 Value for Same Identifier

> When PACS receives an ADT update message containing more than one value for the SSN or more than one value for the ICN, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment and will not update any patient record. The application acknowledgment shall contain a value of AE

> <span id="_bookmark63" class="anchor"></span>(application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 207 (application internal error) in component 4. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Update Received for Sensitive/Employee Patient

> When PACS receives an ADT update message for a patient whose VIP Indicator value in PV1-16 is set to E (employee) or S (sensitive), PACS shall safeguard the identity of the patient using VA rules for suppressing patient name and other identifying information.

### Acknowledgment Message (ACK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Original Mode ACK To Be Returned

> If PACS accepts ADT messages, it shall return an original mode ACK application acknowledgment, as defined in the HL7 Standard and prescribed by the IHE Radiology Technical Framework. The trigger event of the acknowledgment message shall be equal to the trigger event of the message that was received.

#### ERR Segment To Be Sent for AE and AR Conditions

> When an error is determined to have occurred, PACS shall return the acknowledgment code AE (Application Error) or AR (Application Reject) as appropriate, and shall populate Field ERR-1-error code and location with the relevant error information including the appropriate error code from HL7 Table 0357. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Message Type, Trigger Event, Version ID, or Processing Code to Cause Reject

> If the value received in *MSH-9.1-message type, MSH-9.2-trigger event, MSH-11- processing code,* or *MSH-12-version ID* is invalid, the value AR (application reject) shall be returned in *MSA-1-acknowledgment code*, and the appropriate value from HL7 Table 0357 shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Receiving Application or Receiving Facility to Cause Error

> If the value received in *MSH-5-receiving application* or *MSH-6-receiving facility* is invalid, the value AE (application error) shall be returned in *MSA-1- acknowledgment code*, and the value 103 (table value not found) shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 messages shall be populated and processed according to the following abstract message definitions.

### Patient Update Message: Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This message syntax is used for trigger event A02 (Transfer).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation / Result</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>7</td>
</tr>
</tbody>
</table>

### Patient Update Message: Discharge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This message syntax is used for trigger event A03 (Discharge).

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 33%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { DG1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Information</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ DRG ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Related Group</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { PR1</p>
</blockquote></td>
<td><blockquote>
<p>Procedures</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>7</td>
</tr>
</tbody>
</table>

### Patient Update Message: Update Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A08 (Update Patient Information). The Update Patient Information message is used to update demographic and other non-movement related information. Movement-related information should not be transmitted using trigger event A08 but instead should be transmitted using the appropriate movement- related trigger event code, such as A02 for patient transfer.

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { NK1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Next of Kin / Associated Parties</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation / Result</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { AL1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Information</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..99]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DG1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Information</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ DRG ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Related Group</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { PR1</p>
</blockquote></td>
<td><blockquote>
<p>Procedures</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { GT1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Guarantor</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN1</p>
</blockquote></td>
<td><blockquote>
<p>Insurance</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ IN2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info.</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN3 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info. – Cert.</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ ACC ]</p>
</blockquote></td>
<td><blockquote>
<p>Accident Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ UB1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ UB2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill 92 Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
</tbody>
</table>

### Patient Update Message: Merge Patient Identifier List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A40 (Merge Patient Identifier List).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>{ PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark66" class="anchor"></span>MRG</p>
</blockquote></th>
<th><blockquote>
<p>Merge Information</p>
</blockquote></th>
<th>R</th>
<th><blockquote>
<p>[1..1]</p>
</blockquote></th>
<th>3</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>[ PV1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>}</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Patient Update Message: Change Patient Identifier List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A47 (Change Patient Identifier List). The Change Patient Identifier List message is used to update any occurrence of field PID-3-Patient Identifier List. Updates to the ICN (Integration Control Number) must be sent using this message.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MRG</p>
</blockquote></td>
<td><blockquote>
<p>Merge Information</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
</tbody>
</table>

### Patient Update Message: Cancel Admit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A11 (Cancel Admit).

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
</tbody>
</table>

### Patient Update Message: Cancel Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A12 (Cancel Transfer).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation / Result</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[2..2]</p>
</blockquote></td>
<td>7</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark67" class="anchor"></span>[ { DG1 } ]</p>
</blockquote></th>
<th><blockquote>
<p>Diagnosis Information</p>
</blockquote></th>
<th><blockquote>
<p>RE</p>
</blockquote></th>
<th><blockquote>
<p>[0..1]</p>
</blockquote></th>
<th>6</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Patient Update Message: Cancel Discharge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This syntax is used for trigger event A13 (Cancel Discharge / End Visit).

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADT Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVN</p>
</blockquote></td>
<td><blockquote>
<p>Event Type</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { NK1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Next of Kin / Associated Parties</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ PV2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { DB1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Disability Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { OBX } ]</p>
</blockquote></td>
<td><blockquote>
<p>Observation / Result</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { AL1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Information</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { DG1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Information</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ DRG ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Related Group</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { PR1</p>
</blockquote></td>
<td><blockquote>
<p>Procedures</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { ROL } ]</p>
</blockquote></td>
<td><blockquote>
<p>Role</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { GT1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Guarantor</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN1</p>
</blockquote></td>
<td><blockquote>
<p>Insurance</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ IN2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info.</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { IN3 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info. – Cert.</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ ACC ]</p>
</blockquote></td>
<td><blockquote>
<p>Accident Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ UB1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ UB2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Universal Bill 92 Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
</tbody>
</table>

### Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 34%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ACK Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSA</p>
</blockquote></td>
<td><blockquote>
<p>Message Acknowledgment</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ ERR ]</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

## Static Definition – Segment Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fields in HL7 messages shall be populated and processed according to the following Segment Attribute Tables.

### MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [2.6.1](#msh-segment-fields-1), [<u>MSH Segment Fields</u>](#msh-segment-fields-1), for a detailed explanation of the fields used in this segment.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00001</p>
</blockquote></td>
<td><blockquote>
<p>Field Separator</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00002</p>
</blockquote></td>
<td><blockquote>
<p>Encoding Characters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>00003</p>
</blockquote></td>
<td><blockquote>
<p>Sending Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>00004</p>
</blockquote></td>
<td><blockquote>
<p>Sending Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>00005</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>00006</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00007</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00008</p>
</blockquote></td>
<td><blockquote>
<p>Security</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>00009</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00010</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00011</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>VID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>00012</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00013</p>
</blockquote></td>
<td><blockquote>
<p>Sequence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00014</p>
</blockquote></td>
<td><blockquote>
<p>Continuation Pointer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>00015</p>
</blockquote></td>
<td><blockquote>
<p>Accept Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>00016</p>
</blockquote></td>
<td><blockquote>
<p>Application Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00017</p>
</blockquote></td>
<td><blockquote>
<p>Country Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0211</p>
</blockquote></td>
<td><blockquote>
<p>00692</p>
</blockquote></td>
<td><blockquote>
<p>Character Set</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00693</p>
</blockquote></td>
<td><blockquote>
<p>Principal Language of Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0356</p>
</blockquote></td>
<td><blockquote>
<p>01317</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Character Set Handling Scheme</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01598</p>
</blockquote></td>
<td><blockquote>
<p>Conformance Statement ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

### EVN Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the EVN Segment in HL7. Refer to [Section 2.6.2](#evn-segment-fields-1), [<u>EVN Segment Fields</u>](#evn-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>3</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>00099</p>
</blockquote></td>
<td><blockquote>
<p>Event Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00100</p>
</blockquote></td>
<td><blockquote>
<p>Recorded Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00101</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time Planned Event</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0062</p>
</blockquote></td>
<td><blockquote>
<p>00102</p>
</blockquote></td>
<td><blockquote>
<p>Event Reason Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>60</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0188</p>
</blockquote></td>
<td><blockquote>
<p>00103</p>
</blockquote></td>
<td><blockquote>
<p>Operator ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01278</p>
</blockquote></td>
<td><blockquote>
<p>Event Occurred</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>180</td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01534</p>
</blockquote></td>
<td><blockquote>
<p>Event Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PID Segment in HL7. Refer to [Section 2.6.3](#pid-segment-fields-1), [<u>PID Segment Fields</u>](#pid-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00104</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00105</p>
</blockquote></td>
<td><blockquote>
<p>Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00106</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identifier List</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00107</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Patient ID - PID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00108</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00109</p>
</blockquote></td>
<td><blockquote>
<p>Mother’s Maiden Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00110</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Birth</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0001</p>
</blockquote></td>
<td><blockquote>
<p>00111</p>
</blockquote></td>
<td><blockquote>
<p>Sex</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00112</p>
</blockquote></td>
<td><blockquote>
<p>Patient Alias</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0005</p>
</blockquote></td>
<td><blockquote>
<p>00113</p>
</blockquote></td>
<td><blockquote>
<p>Race</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XAD</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00114</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>00115</p>
</blockquote></td>
<td><blockquote>
<p>County Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XTN</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00116</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Home</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XTN</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00117</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Business</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0296</p>
</blockquote></td>
<td><blockquote>
<p>00118</p>
</blockquote></td>
<td><blockquote>
<p>Primary Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0002</p>
</blockquote></td>
<td><blockquote>
<p>00119</p>
</blockquote></td>
<td><blockquote>
<p>Marital Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0006</p>
</blockquote></td>
<td><blockquote>
<p>00120</p>
</blockquote></td>
<td><blockquote>
<p>Religion</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00121</p>
</blockquote></td>
<td><blockquote>
<p>Patient Account Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00122</p>
</blockquote></td>
<td><blockquote>
<p>SSN Number - Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20</td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td>DLN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00123</p>
</blockquote></td>
<td><blockquote>
<p>Driver's License Number - Patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>21</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00124</p>
</blockquote></td>
<td><blockquote>
<p>Mother's Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>22</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0189</p>
</blockquote></td>
<td><blockquote>
<p>00125</p>
</blockquote></td>
<td><blockquote>
<p>Ethnic Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>23</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00126</p>
</blockquote></td>
<td><blockquote>
<p>Birth Place</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00127</p>
</blockquote></td>
<td><blockquote>
<p>Multiple Birth Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>25</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>NM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00128</p>
</blockquote></td>
<td><blockquote>
<p>Birth Order</p>
</blockquote></td>
</tr>
<tr class="even">
<td>26</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0171</p>
</blockquote></td>
<td><blockquote>
<p>00129</p>
</blockquote></td>
<td><blockquote>
<p>Citizenship</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>27</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0172</p>
</blockquote></td>
<td><blockquote>
<p>00130</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Military Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>28</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0212</p>
</blockquote></td>
<td><blockquote>
<p>00739</p>
</blockquote></td>
<td><blockquote>
<p>Nationality</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00740</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Date and Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>30</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00741</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>01535</p>
</blockquote></td>
<td><blockquote>
<p>Identity Unknown Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>32</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0445</p>
</blockquote></td>
<td><blockquote>
<p>01536</p>
</blockquote></td>
<td><blockquote>
<p>Identity Reliability Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>33</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01537</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>34</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td>HD</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01538</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>35</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0446</p>
</blockquote></td>
<td><blockquote>
<p>01539</p>
</blockquote></td>
<td><blockquote>
<p>Species Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>36</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0447</p>
</blockquote></td>
<td><blockquote>
<p>01540</p>
</blockquote></td>
<td><blockquote>
<p>Breed Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>37</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01541</p>
</blockquote></td>
<td><blockquote>
<p>Strain</p>
</blockquote></td>
</tr>
<tr class="even">
<td>38</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0429</p>
</blockquote></td>
<td><blockquote>
<p>01542</p>
</blockquote></td>
<td><blockquote>
<p>Production Class Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

### MRG Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the MRG Segment in HL7. Refer to [Section 2.6.4](#mrg-segment-fields), [<u>MRG Segment Fields</u>](#mrg-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..2]</p>
</blockquote></td>
<td rowspan="7"></td>
<td><blockquote>
<p>00211</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Identifier List</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00212</p>
</blockquote></td>
<td><blockquote>
<p>Prior Alternate Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00213</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Account Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00214</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>01279</p>
</blockquote></td>
<td><blockquote>
<p>Prior Visit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>01280</p>
</blockquote></td>
<td><blockquote>
<p>Prior Alternate Visit ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XPN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>01281</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Name</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PV1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PV1 Segment in HL7. Refer to [Section 2.6.5](#pv1-segment-fields-1), [<u>PV1 Segment Fields</u>](#pv1-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00131</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PV1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0004</p>
</blockquote></td>
<td><blockquote>
<p>00132</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00133</p>
</blockquote></td>
<td><blockquote>
<p>Assigned Patient Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0007</p>
</blockquote></td>
<td><blockquote>
<p>00134</p>
</blockquote></td>
<td><blockquote>
<p>Admission Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00135</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00136</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00137</p>
</blockquote></td>
<td><blockquote>
<p>Attending Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00138</p>
</blockquote></td>
<td><blockquote>
<p>Referring Doctor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00139</p>
</blockquote></td>
<td><blockquote>
<p>Consulting Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0069</p>
</blockquote></td>
<td><blockquote>
<p>00140</p>
</blockquote></td>
<td><blockquote>
<p>Hospital Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00141</p>
</blockquote></td>
<td><blockquote>
<p>Temporary Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0087</p>
</blockquote></td>
<td><blockquote>
<p>00142</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Test Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0092</p>
</blockquote></td>
<td><blockquote>
<p>00143</p>
</blockquote></td>
<td><blockquote>
<p>Re-admission Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0023</p>
</blockquote></td>
<td><blockquote>
<p>00144</p>
</blockquote></td>
<td><blockquote>
<p>Admit Source</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td><blockquote>
<p>0009</p>
</blockquote></td>
<td><blockquote>
<p>00145</p>
</blockquote></td>
<td><blockquote>
<p>Ambulatory Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0099</p>
</blockquote></td>
<td><blockquote>
<p>00146</p>
</blockquote></td>
<td><blockquote>
<p>VIP Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00147</p>
</blockquote></td>
<td><blockquote>
<p>Admitting Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0018</p>
</blockquote></td>
<td><blockquote>
<p>00148</p>
</blockquote></td>
<td><blockquote>
<p>Patient Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00149</p>
</blockquote></td>
<td><blockquote>
<p>Visit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>FC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0064</p>
</blockquote></td>
<td><blockquote>
<p>00150</p>
</blockquote></td>
<td><blockquote>
<p>Financial Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0032</p>
</blockquote></td>
<td><blockquote>
<p>00151</p>
</blockquote></td>
<td><blockquote>
<p>Charge Price Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0045</p>
</blockquote></td>
<td><blockquote>
<p>00152</p>
</blockquote></td>
<td><blockquote>
<p>Courtesy Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0046</p>
</blockquote></td>
<td><blockquote>
<p>00153</p>
</blockquote></td>
<td><blockquote>
<p>Credit Rating</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0044</p>
</blockquote></td>
<td><blockquote>
<p>00154</p>
</blockquote></td>
<td><blockquote>
<p>Contract Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00155</p>
</blockquote></td>
<td><blockquote>
<p>Contract Effective Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00156</p>
</blockquote></td>
<td><blockquote>
<p>Contract Amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00157</p>
</blockquote></td>
<td><blockquote>
<p>Contract Period</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0073</p>
</blockquote></td>
<td><blockquote>
<p>00158</p>
</blockquote></td>
<td><blockquote>
<p>Interest Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0110</p>
</blockquote></td>
<td><blockquote>
<p>00159</p>
</blockquote></td>
<td><blockquote>
<p>Transfer to Bad Debt Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark71" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><strong>Item #</strong></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00160</td>
<td><blockquote>
<p>Transfer to Bad Debt Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0021</p>
</blockquote></td>
<td>00161</td>
<td><blockquote>
<p>Bad Debt Agency Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00162</td>
<td><blockquote>
<p>Bad Debt Transfer Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00163</td>
<td><blockquote>
<p>Bad Debt Recovery Amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0111</p>
</blockquote></td>
<td>00164</td>
<td><blockquote>
<p>Delete Account Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00165</td>
<td><blockquote>
<p>Delete Account Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0112</p>
</blockquote></td>
<td>00166</td>
<td><blockquote>
<p>Discharge Disposition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td>25</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0113</p>
</blockquote></td>
<td>00167</td>
<td><blockquote>
<p>Discharged to Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0114</p>
</blockquote></td>
<td>00168</td>
<td><blockquote>
<p>Diet Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0115</p>
</blockquote></td>
<td>00169</td>
<td><blockquote>
<p>Servicing Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0116</p>
</blockquote></td>
<td>00170</td>
<td><blockquote>
<p>Bed Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0117</p>
</blockquote></td>
<td>00171</td>
<td><blockquote>
<p>Account Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00172</td>
<td><blockquote>
<p>Pending Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00173</td>
<td><blockquote>
<p>Prior Temporary Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td>00174</td>
<td><blockquote>
<p>Admit Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td>00175</td>
<td><blockquote>
<p>Discharge Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00176</td>
<td><blockquote>
<p>Current Patient Balance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00177</td>
<td><blockquote>
<p>Total Charges</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00178</td>
<td><blockquote>
<p>Total Adjustments</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td>00179</td>
<td><blockquote>
<p>Total Payments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td>00180</td>
<td><blockquote>
<p>Alternate Visit ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0326</p>
</blockquote></td>
<td>01226</td>
<td><blockquote>
<p>Visit Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td>01274</td>
<td><blockquote>
<p>Other Healthcare Provider</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ROL Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ROL Segment is used to give more complete information about the patient’s referring and attending physicians than is permitted by the PV1 Segment. Specifically, the ROL Segment allows for the transmission of multiple callback numbers for each physician.

> The following is a listing of all the fields defined for the ROL Segment in HL7. Refer to [Section 2.6.6](#rol-segment-fields-1), [<u>ROL Segment Fields</u>](#rol-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01206</p>
</blockquote></td>
<td><blockquote>
<p>Role Instance ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0287</p>
</blockquote></td>
<td><blockquote>
<p>00816</p>
</blockquote></td>
<td><blockquote>
<p>Action Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0443</p>
</blockquote></td>
<td><blockquote>
<p>01197</p>
</blockquote></td>
<td><blockquote>
<p>Role-ROL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01198</p>
</blockquote></td>
<td><blockquote>
<p>Role Person</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01199</p>
</blockquote></td>
<td><blockquote>
<p>Role Begin Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01200</p>
</blockquote></td>
<td><blockquote>
<p>Role End Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01201</p>
</blockquote></td>
<td><blockquote>
<p>Role Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01205</p>
</blockquote></td>
<td><blockquote>
<p>Role Action Reason</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01510</p>
</blockquote></td>
<td><blockquote>
<p>Provider Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0406</a></p>
</blockquote></td>
<td><blockquote>
<p>01461</p>
</blockquote></td>
<td><blockquote>
<p>Organization Unit Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XAD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00679</p>
</blockquote></td>
<td><blockquote>
<p>Office/Home Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..8]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00678</p>
</blockquote></td>
<td><blockquote>
<p>Phone</p>
</blockquote></td>
</tr>
</tbody>
</table>

### DG1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the DG1 Segment in HL7. Refer to [Section 2.6.7](#dg1-segment-fields-1), [<u>DG1 Segment Fields</u>](#dg1-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00375</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - DG1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0053</td>
<td><blockquote>
<p>00376</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Coding Method</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>0051</td>
<td><blockquote>
<p>00377</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Code - DG1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>40</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00378</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Description</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00379</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>0052</td>
<td><blockquote>
<p>00380</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0118</td>
<td><blockquote>
<p>00381</p>
</blockquote></td>
<td><blockquote>
<p>Major Diagnostic Category</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0055</td>
<td><blockquote>
<p>00382</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic Related Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0136</td>
<td><blockquote>
<p>00383</p>
</blockquote></td>
<td><blockquote>
<p>DRG Approval Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0056</td>
<td><blockquote>
<p>00384</p>
</blockquote></td>
<td><blockquote>
<p>DRG Grouper Review Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0083</td>
<td><blockquote>
<p>00385</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00386</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Days</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00387</p>
</blockquote></td>
<td><blockquote>
<p>Outlier Cost</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00388</p>
</blockquote></td>
<td><blockquote>
<p>Grouper Version And Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0359</td>
<td><blockquote>
<p>00389</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Priority</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00390</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosing Clinician</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><a href="#_bookmark0">0228</a></td>
<td><blockquote>
<p>00766</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Classification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0136</td>
<td><blockquote>
<p>00767</p>
</blockquote></td>
<td><blockquote>
<p>Confidential Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00768</p>
</blockquote></td>
<td><blockquote>
<p>Attestation Date/Time</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the ADT message, the OBX Segment is used to communicate height and weight of the patient. The following is a listing of all the fields defined for the OBX Segment in HL7. Refer to Section [2.6.8](#obx-segment-fields-1), [<u>OBX Segment Fields</u>](#obx-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00569</p>
</blockquote></td>
<td><blockquote>
<p>Set ID – OBX</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0125</p>
</blockquote></td>
<td><blockquote>
<p>00570</p>
</blockquote></td>
<td><blockquote>
<p>Value Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00571</p>
</blockquote></td>
<td><blockquote>
<p>Observation Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00572</p>
</blockquote></td>
<td><blockquote>
<p>Observation Sub-ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>65536<a href="#_bookmark73"><sup>‡</sup></a></td>
<td></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00573</p>
</blockquote></td>
<td><blockquote>
<p>Observation Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00574</p>
</blockquote></td>
<td><blockquote>
<p>Units</p>
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
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00575</p>
</blockquote></td>
<td><blockquote>
<p>Reference Range</p>
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
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0078</p>
</blockquote></td>
<td><blockquote>
<p>00576</p>
</blockquote></td>
<td><blockquote>
<p>Abnormal Flags</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00577</p>
</blockquote></td>
<td><blockquote>
<p>Probability</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00578</p>
</blockquote></td>
<td><blockquote>
<p>Nature of Abnormal Test</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0085</p>
</blockquote></td>
<td><blockquote>
<p>00579</p>
</blockquote></td>
<td><blockquote>
<p>Observation Result Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00580</p>
</blockquote></td>
<td><blockquote>
<p>Date Last Observation Normal Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00581</p>
</blockquote></td>
<td><blockquote>
<p>User Defined Access Checks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00582</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Observation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00583</p>
</blockquote></td>
<td><blockquote>
<p>Producer’s ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark73" class="anchor"></span><sup>‡</sup> The length and data type of this field are variable, depending on *OBX-2-Value Type*.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark74" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>X X X</p>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="4"></td>
<td rowspan="4"><blockquote>
<p>00584</p>
<p>00936</p>
<p>01479</p>
<p>01480</p>
</blockquote></td>
<td><blockquote>
<p>Responsible Observer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Observation Method</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Equipment Instance Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Analysis</p>
</blockquote></td>
</tr>
</tbody>
</table>

### AL1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the AL1 Segment in HL7. Refer to Section 2.6.9, <u>AL1 Segment Fields</u>, for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>R R R X RE</p>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00203</p>
</blockquote></td>
<td><blockquote>
<p>Set ID – AL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0127</p>
</blockquote></td>
<td><blockquote>
<p>00204</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00205</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Code/Mnemonic/Description</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0128</p>
</blockquote></td>
<td><blockquote>
<p>00206</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Severity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>[0..99]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00207</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Reaction</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00208</p>
</blockquote></td>
<td><blockquote>
<p>Identification Date</p>
</blockquote></td>
</tr>
</tbody>
</table>

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the MSA Segment in HL7. MSA is used only in the acknowledgment message. Refer to Section 2.6.10, <u>MSA Segment</u> <u>Fields</u>, for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>0003</td>
<td><blockquote>
<p>00018</p>
</blockquote></td>
<td><blockquote>
<p>Acknowledgment Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00010</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00020</p>
</blockquote></td>
<td><blockquote>
<p>Text Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>15</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00021</p>
</blockquote></td>
<td><blockquote>
<p>Expected Sequence Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>0102</td>
<td><blockquote>
<p>00022</p>
</blockquote></td>
<td><blockquote>
<p>Delayed Acknowledgment Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00023</p>
</blockquote></td>
<td><blockquote>
<p>Error Condition</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the ERR Segment in HL7. ERR is used only in the acknowledgment message. Refer to Section [2.6.11](#err-segment-fields-1), [<u>ERR Segment</u>](#err-segment-fields-1) [<u>Fields</u>](#err-segment-fields-1), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>80</td>
<td>CM</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..999]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00024</p>
</blockquote></td>
<td><blockquote>
<p>Error Code and Location</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSH-1-Field Separator

> This field contains the top-level delimiter for HL7 elements within segments.

#### MSH-2-Encoding Characters

> This field contains the component separator (secondary element delimiter), repetition separator, escape character, and subcomponent separator (tertiary element delimiter).

#### MSH-3-Sending Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA registration message, Component 1 of this field shall be populated with the value VISTA IMAGING from user-defined Table 0361, *Sending/Receiving Application*. PACS shall return this value in component MSH-

> 5.1 of the acknowledgment message. Components 2 and 3 of MSH-3 are not valued.

#### MSH-4-Sending Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was generated. PACS shall return this value in component MSH-6.1 of the acknowledgment message. Components 2 and 3 of MSH-4 are not valued.

#### MSH-5-Receiving Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark77" class="anchor"></span>In the VistA message, Component 1 of this field shall be populated from user- defined Table 0361, *Sending/Receiving Application*, with the name of the PACS application. PACS shall return this value in component MSH-3.1 of the acknowledgment message. Components 2 and 3 of MSH-5 are not valued.

#### MSH-6-Receiving Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was received. PACS shall return this value in field MSH-4 of the acknowledgment message. Components 2 and 3 of MSH-6 are not valued.

#### MSH-7-Date/Time of Message

> This field contains the date and time that the sending system built the message.

#### MSH-9-Message Type

> This field is of data type CM. Its components are as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>Trigger Event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0354</p>
</blockquote></td>
<td><blockquote>
<p>Message Structure</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

> *MSH-9.1-Message Type*

> This component contains a value from HL7 Table 0076, *Message Type*. For the registration message, it will always contain the value ADT.

#### MSH-9.2-Trigger Event

> This component will contain one of the following values from HL7 Table 0003,

> *Event Type*.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A01</p>
</blockquote></td>
<td><blockquote>
<p>Admit a patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A02</p>
</blockquote></td>
<td><blockquote>
<p>Transfer a patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A03</p>
</blockquote></td>
<td><blockquote>
<p>Discharge/end visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A04</p>
</blockquote></td>
<td><blockquote>
<p>Register a patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A08</p>
</blockquote></td>
<td><blockquote>
<p>Update patient information</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark78" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A11</p>
</blockquote></td>
<td><blockquote>
<p>Cancel admit/visit notification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A12</p>
</blockquote></td>
<td><blockquote>
<p>Cancel transfer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A13</p>
</blockquote></td>
<td><blockquote>
<p>Cancel discharge</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A40</p>
</blockquote></td>
<td><blockquote>
<p>Merge patient – patient identifier list</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A47</p>
</blockquote></td>
<td><blockquote>
<p>Change patient identifier list</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-10-Message Control ID

> This field will contain a unique identifier for the message.

#### MSH-11-Processing ID

> This field is of type PT, which is defined as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0103</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0207</p>
</blockquote></td>
<td><blockquote>
<p>Processing Mode</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

#### MSH-11.1-Processing ID

> This field contains one of the following values from HL7 Table 0103, *Processing ID.*

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>Production</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Debugging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T</td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-11.2-Processing Mode

> This field contains one of the following values from HL7 Table 0207, *Processing Mode*.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A</td>
<td><blockquote>
<p>Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>R</td>
<td><blockquote>
<p>Restore from archive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>I</td>
<td><blockquote>
<p>Initial load</p>
</blockquote></td>
</tr>
<tr class="even">
<td>T</td>
<td><blockquote>
<p>Current processing, transmitted at intervals (scheduled or on demand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>not present</p>
</blockquote></td>
<td><blockquote>
<p>Not present (the default, meaning <em>current</em> processing)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-12-Version ID

> This field is of type VID, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internationalization Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internal Version ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This field’s first component will always contain the value 2.3.1 from HL7 Table 0104, *Version ID*. The following table contains the full set of legal values for the first component.

> HL7 Table 0104 - Version ID

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 28%" />
<col style="width: 45%" />
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
<p><strong>Comment (Date)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.0</p>
</blockquote></td>
<td><blockquote>
<p>September 1988</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.0D</p>
</blockquote></td>
<td><blockquote>
<p>Demo 2.0</p>
</blockquote></td>
<td><blockquote>
<p>October 1988</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td><blockquote>
<p>Release 2. 1</p>
</blockquote></td>
<td><blockquote>
<p>March 1990</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.2</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.2</p>
</blockquote></td>
<td><blockquote>
<p>December 1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.3</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.3</p>
</blockquote></td>
<td><blockquote>
<p>March 1997</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.3.1</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.3.1</p>
</blockquote></td>
<td><blockquote>
<p>May 1999</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.4</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.4</p>
</blockquote></td>
<td><blockquote>
<p>November 2000</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>Release 2.5</p>
</blockquote></td>
<td><blockquote>
<p>May 2003</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Although the VistA message pre-adopts certain Version 2.4 structures, such as the ROL segment, receivers that are unable to recognize Version 2.4 may use Version

> 2.3.1 syntax rules as prescribed by IHE. It is expected that receivers not now using HL7 Version 2.3.1 will be able to process the V2.3.1 messages according to the HL7 rules for backward compatibility. At such time as IHE is revised to a later version of HL7, receivers will be expected to adapt to the new structures within a stated period of time following the revision.

> Other components of this field will not be used.

#### MSH-17-Country Code

> This field is of type ID. It will always contain the value USA from the ISO 3166 country code table.

### EVN Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### EVN-1-Event Type Code

> This field contains the 3-character code of the trigger event being communicated. It is retained for backward compatibility with versions of HL7 that do not communicate the event type in the second component of [MSH-9-Message Type](#_bookmark29).

#### EVN-2-Recorded Date/Time

> This field contains the date and time that the event was recorded in the system.

#### EVN-6-Event Occurred

> This field contains the date and time that the event actually took place. If it is not known when the event actually took place, this field is left blank.

### PID Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID-3-Patient Identifier List

> Field PID-3 is used to transmit the patient Integration Control Number (ICN). This field is of data type CX, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Check Digit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

> *PID-3.1-ID*

> This is the alphanumeric identification string.

#### PID-3.4-Assigning Authority

> This component contains the entity that assigned the identifier value in *PID-3.1- ID*. It is of data type HD, which has 3 subcomponents defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> At present, only the first subcomponent should be considered for the purpose of identifying the assigning authority. Subcomponent 1 will contain the value

> <span id="_bookmark83" class="anchor"></span>USVHA*,* meaning United States Veterans Health Administration, from user- defined Table 0300, *Namespace ID*.

> In future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-3.5-Identifier Type

> The value in this component distinguishes the kind of identifier contained in *PID- 3.1-ID*. It will contain the value NI, meaning National unique individual identifier, from user-defined Table 0203, *Identifier Type*.

#### PID-5-Patient Name

> This field is of data type XPN, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>35</td>
<td><blockquote>
<p>FN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0200</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 7, Name Type Code, indicates the type of name given in Components 1-6, such as legal, birth name, or alias. At present, VistA only uses name type L (legal).

#### PID-7-Date/Time of Birth

> This is the date and time that the patient was born, as far as is known. It may be as imprecise as the four-digit birth year (*e.g.*, 1962).

#### PID-8-Sex

> This field contains the sex of the patient. It is populated with one of the following values from user-defined Table 0001, *Sex*, if a value is known.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>Female</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Male</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Unknown</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10-Race

> This field contains a code for the patient’s race. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark84" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-10.1-Identifier

> This component contains the RACE INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0005, *Race*.

#### PID-10.3-Name of Coding System

> The value of this component shall be 0005.

#### PID-10.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1002-5</p>
</blockquote></td>
<td><blockquote>
<p>AMERICAN INDIAN OR ALASKA NATIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2028-9</p>
</blockquote></td>
<td><blockquote>
<p>ASIAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2054-5</p>
</blockquote></td>
<td><blockquote>
<p>BLACK OR AFRICAN AMERICAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2076-8</p>
</blockquote></td>
<td><blockquote>
<p>NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2106-3</p>
</blockquote></td>
<td><blockquote>
<p>WHITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10.6-Name of Coding System

> This component shall be populated CDC.

#### PID-11-Patient Address

> This field contains the patient’s address. It is of data type XAD, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="8"><blockquote>
<p>0190</p>
</blockquote></td>
<td><blockquote>
<p>Street Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Other Designation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>City</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>State or Province</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>ZIP or Postal Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Country</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Address Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Other Geographic Designation</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark85" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>County/Parish Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0288</p>
</blockquote></td>
<td><blockquote>
<p>Census Tract</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Address Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13-Phone Number – Home

> This field contains the patient’s home telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### PID-13.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-13.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14-Phone Number – Business

> This field contains the patient’s work telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### PID-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-14.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-19-SSN Number – Patient

> This field carries the patient Social Security Number, for backward compatibility with versions of HL7 prior to Version 2.3.1. The Social Security Number is a secondary patient identifier. For the primary patient identifier, use the Integration Control Number from [<u>PID-3-Patient Identifier List</u>](#pid-3-patient-identifier-list).

#### PID-22-Ethnic Group

> This field contains a code indicating whether the patient is of Hispanic descent. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-22.1-Identifier

> This component contains the ETHNICITY INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0189, *Ethnic Group*.

#### PID-22.3-Name of Coding System

> The value of this component shall be 0189.

#### PID-22.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2135-2</p>
</blockquote></td>
<td><blockquote>
<p>HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2186-5</p>
</blockquote></td>
<td><blockquote>
<p>NOT HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-22.6-Name of Coding System

> This component shall be populated CDC.

### MRG Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MRG-1-Prior Patient Identifier List

> This field contains the previous or “old” patient identifier. The current or “new” patient identifier will be contained in the repetition of PID-3-Patient Identifier List that has the same assigning authority and identifier type.

> This field is of data type CX. Its components are defined as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Check Digit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

> *MRG-1.1-ID*

> This is the alphanumeric identification string.

#### MRG-1.4-Assigning Authority

> This component contains the entity that assigned the identifier value in *MRG-1.1- ID*. It is of data type HD, which has 3 subcomponents defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> At present, only the first subcomponent should be considered for the purpose of identifying the assigning authority. Subcomponent 1 will contain one of the following values from user-defined Table 0300, *Namespace ID*.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Value</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>USVHA</td>
<td><blockquote>
<p>United States Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>USSSA</td>
<td><blockquote>
<p>United States Social Security Administration</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### MRG-1.5-Identifier Type

> The value in this component distinguishes the kind of identifier contained in *MRG-1.1-ID*. It will contain one of the following values from user-defined Table 0203, *Identifier Type*.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NI</p>
</blockquote></td>
<td><blockquote>
<p>National unique individual identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PI</p>
</blockquote></td>
<td><blockquote>
<p>Patient internal identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td><blockquote>
<p>Social Security number</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Integration Control Number (ICN) will be used as the primary identifier. This identifier is designated by Assigning Authority USVHA and Identifier Type NI.

### PV1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PV1-2-Patient Class

> This field designates whether the patient is an inpatient (I) or an outpatient (O).

#### PV1-3-Assigned Patient Location

> For inpatient, this field designates the patient’s location in the medical center. The data type of this field is PL, which is defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0302</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0303</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0304</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0306</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0305</p>
</blockquote></td>
<td><blockquote>
<p>Person Location Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0307</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0308</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Location Description</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VistA sends Component 1, Point of Care, as three subcomponents, of which the first is an internal entry number into the VistA WARD LOCATION File (#42), and the second is the name of the ward location; the third is the internal designator of the WARD LOCATION File and should be ignored.

#### PV1-7-Attending Doctor

> This is the physician responsible for the care of the patient during the present encounter. VistA values this field for inpatient encounters only.

> The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-8-Referring Doctor

> This is the patient’s primary physician. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-10-Hospital Service

> This is the treating specialty assigned to the patient with the most recent movement. VistA values this field for inpatient encounters only. When populated, it contains a value from user-defined Table 0069, *Hospital Service*; VistA sends values from the HOSPITAL LOCATION File (#44).

#### PV1-15-Ambulatory Status

> This field indicates any permanent or transient conditions affecting the patient’s mode of transportation. It may contain one or more values from user-defined Table 0009, *Ambulatory Status.* If the patient’s ambulatory status is not known, this field is not populated.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A0</p>
</blockquote></td>
<td><blockquote>
<p>No functional limitations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A2</p>
</blockquote></td>
<td><blockquote>
<p>Wheelchair/stretcher bound</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B6</p>
</blockquote></td>
<td><blockquote>
<p>Pregnant</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PV1-16-VIP Indicator

> This field is used to indicate that the patient is an employee, or that patient record is sensitive and should not be made available for general personnel access. If one of these conditions applies, VistA populates this field with one of the following values from user-defined Table 0099, *VIP Indicator.*

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark92" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>E</td>
<td><blockquote>
<p>Patient is a VA employee</p>
</blockquote></td>
</tr>
<tr class="even">
<td>S</td>
<td><blockquote>
<p>Patient record is sensitive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ES</p>
</blockquote></td>
<td><blockquote>
<p>Patient is a VA employee and patient record is sensitive</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PV1-19-Visit

> This field indicates the patient movement with which this registration is associated. It contains a pointer to the VistA PATIENT MOVEMENT File.

#### PV1-44-Admit Date/Time

> This is the date and time when the patient was admitted (if the patient is an inpatient) or when the current encounter began (if the patient is an outpatient).

#### PV1-45-Discharge Date/Time

> This is the date and time when the patient was discharged (if the patient was an inpatient and has been discharged) or when the current encounter ended (if the patient is an outpatient and the current encounter is complete).

### ROL Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ROL-1-Role Instance ID

> This is the ordinal number of this occurrence of the ROL Segment under the PV1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### ROL-2-Action Code

> This field will always be valued UP, which indicates that the receiving system should update its database with the information contained in the ROL Segment(s) being sent in the current message.

#### ROL-3-Role

> This field indicates the involvement with the activity being transmitted. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark94" class="anchor"></span>Component *PID-10.1-Identifier* is valued AT to indicate the attending physician and RP to indicate the referring physician.

#### ROL-4-Role Person

> This is the name of the person (physician) whose information is being transmitted. Its structure is identical to that of [<u>PV1-7-Attending Doctor</u>](#pv1-7-attending-doctor) and [<u>PV1-8-Referring</u>](#pv1-8-referring-doctor) [<u>Doctor</u>](#pv1-8-referring-doctor).

#### ROL-12-Phone

> This is the telephone number of the person (physician) whose information is being transmitted. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

> *ROL-12.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]*

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### ROL-12.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with one of the following values from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>Beeper Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ROL-12.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with one of the following values from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark95" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>Fax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>Beeper</p>
</blockquote></td>
</tr>
</tbody>
</table>

### DG1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### DG1-1-Set ID

> This is the ordinal number of this occurrence of the DG1 Segment under the PV1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### DG1-3-Diagnosis Code

> This field is of data type CE (Coded Element), which contains 6 components. Only the second component, “Text”, is populated. It contains the name of the diagnosis.

#### DG1-6-Diagnosis Type

> This field is of data type IS (coded value for user-defined tables). It will contain one of the following values from user-defined Table 0052, *Diagnosis Type*.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 75%" />
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
<td>A</td>
<td><blockquote>
<p>Admitting</p>
</blockquote></td>
<td><blockquote>
<p>The diagnosis associated with the patient admission</p>
</blockquote></td>
</tr>
<tr class="even">
<td>W</td>
<td><blockquote>
<p>Working</p>
</blockquote></td>
<td><blockquote>
<p>A diagnosis associated with any patient movement besides the admission</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBX Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-2-Value Type

> This field contains the data type of the information carried in *OBX-5-Observation Value.* It is populated with the value ST from HL7 Table 0125, *Value Type*.

#### OBX-3-Observation Identifier

> This field classifies the kind of information carried in *OBX-5-Observation Value.*

> Its data type is CE, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark98" class="anchor"></span>In the ADT message, Component 2, Text, will contain either HEIGHT or

> WEIGHT. Other components are not populated.

#### OBX-5-Observation Value

> This field contains the actual value whose data type is given in *OBX-2-Value Type* and whose classification is given in *OBX-3-Observation Identifier*. Its formatting follows the rules for the data type given in OBX-2.

#### OBX-6-Units

> This field contains the units of the observation. Its data type is CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Components 1, *Identifier*, and 2, *Text*, are populated as follows.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Identifier</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Text</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>m</td>
<td><blockquote>
<p>meter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>kg</p>
</blockquote></td>
<td><blockquote>
<p>kilogram</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 3 is always valued ISO+, indicating the use of units of measure from ISO Standard 2955-1983.

#### OBX-11-Observation Result Status

> This field is of data type ID. In the ADT message, it is populated with the value F (final results) from HL7 Table 0085, *Observation Result Status Codes Interpretation.*

### AL1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### AL1-1-Set ID

> This is the ordinal number of this occurrence of the AL1 Segment. The first occurrence is labeled 1, the second 2, and so on.

#### AL1-2-Allergy Type

> This field indicates whether the allergy is to a drug and/or food. VistA shall populate this field with one of the following values from user-defined Table 0127, *Allergy Type*.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D</td>
<td><blockquote>
<p>Drug allergy</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark99" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DF</p>
</blockquote></td>
<td><blockquote>
<p>Drug/food allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DFO</p>
</blockquote></td>
<td><blockquote>
<p>Drug/food/other allergy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DO</p>
</blockquote></td>
<td><blockquote>
<p>Drug/other allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>F</td>
<td><blockquote>
<p>Food allergy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FO</p>
</blockquote></td>
<td><blockquote>
<p>Food/other allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>O</td>
<td><blockquote>
<p>Other allergy</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### AL1-3-Allergy Code/Mnemonic/Description

> The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 2, Text, is valued with the name of the allergy. Other components are not valued.

#### AL1-5-Allergy Reaction

> This field contains reactions related to this allergy.

#### AL1-6-Identification Date

> This field contains the date that the allergy was verified.

### MSA Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSA-1-Acknowledgment Code

> This field indicates whether the message was processed successfully. Original mode acknowledgment shall be used. PACS shall populate this field with one of the following values from HL7 Table 0008, *Acknowledgment Code*.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td><blockquote>
<p>Application Accept</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AE</p>
</blockquote></td>
<td><blockquote>
<p>Application Error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AR</p>
</blockquote></td>
<td><blockquote>
<p>Application Reject</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSA-2-Message Control ID

> This field contains the value of *MSH-10-Message Control ID* from the message being acknowledged.

#### MSA-3-Text Message

> This field contains a narrative description of the error found in the message. It is preferred that *ERR-1-Error Code and Location* be used to communicate precise error information.

#### MSA-6-Error Condition

> This field contains an encoded description of the error found in the message. It is preferred that *ERR-1-Error Code and Location* be used to communicate precise error information.

> Data type CE is used for this field, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>0357</p>
</blockquote></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Error condition codes are defined in HL7 Table 0357, *Message Error Condition.* If HL7 Table 0357 is used, the code shall be sent in Component 1, the description in Component 2, and the text HL70357 in Component 3.

### ERR Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.10](#err-segment-fields), [<u>ERR Segment Fields</u>](#err-segment-fields), for a more detailed explanation of the ERR fields used in VistA messaging.

# Order Entry/Update Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This transaction is used by VistA Radiology to inform PACS of a new order. It also allows VistA Radiology to inform PACS that an order has been cancelled or otherwise updated.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/006.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Actor: VistA Radiology

> Role: Notifies ancillary VistA Modules and clinical systems when VistA Radiology orders have been placed or updated.

> Actor: PACS

> Role: Receives order entry and update messages. Optionally, maintains the DICOM Modality Worklist.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The actors in this use case shall perform the behaviors shown in the following activity diagram.

> ![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/007.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vista and PACS shall generate and process HL7 messages according to the following functional and business requirements.

### Order Message (ORM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Radiology shall transmit an ORM message to PACS upon order entry or when an order is updated.

> PACS shall process the message in conformance with the following requirements.

#### New Order – Case, Study Instance UID and ICN Not Found

> When PACS receives an order message containing order control code NW for a case and Study Instance UID not now in its system for a patient for which it does

> <span id="_bookmark104" class="anchor"></span>not find an ICN in its system, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above), and the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above).

#### New Order – Case and Study Instance UID Not Found, ICN Found

> When PACS receives an order message containing order control code NW for a case and Study Instance UID not now in its system for a patient for which it finds an ICN already in its system, PACS will verify that name, SSN, sex, and DOB exactly match what is already in its system: if so, PACS will extract from the HL7 message, and will store in its system, the data contained in the [<u>Basic Patient Data</u>](#basic-patient-data-set) [<u>Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above), and the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above); if not, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not file the order. At the present time, application acknowledgment details may be sent in MSA-3, MSA-6, or ERR-1; however, MSA-3 and MSA-6 will be phased out in the near future. PACS is responsible for notifying support staff and users of anomalies as needed.

#### New Order – Case and Study Instance UID Found, ICN Does Not Match

> When PACS receives an order message containing order control code NW for a case and Study Instance UID already in its system for which the ICN does not match the ICN in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing acknowledgement code AE and giving details of the error in the ERR segment, containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### New Study for Existing Order – Case and ICN Found, Study Instance UID Does Not Match

> When PACS receives an order message containing order control code NW for a case and ICN already in its system for which the Study Instance UID does not match a Study Instance UID currently associated with this study in its system, PACS will verify that name, SSN, sex, and DOB exactly match what is already in its system: if so, PACS will extract from the HL7 message, and will store in its system as a new study for the same case, the data contained in the [<u>Basic Patient</u>](#basic-patient-data-set) [<u>Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above), and the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above); if not, PACS will notify the sending system of the anomaly(ies) via an HL7 application

> <span id="_bookmark105" class="anchor"></span>acknowledgment containing a value of AE (application error) in field *MSA-1- acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not file a new study or otherwise alter the existing case information. At the present time, application acknowledgment details may be sent in MSA-3, MSA-6, or ERR-1; however, MSA-3 and MSA-6 will be phased out in the near future. PACS is responsible for notifying support staff and users of anomalies as needed.

#### New Order – Case, Study Instance UID and Matching ICN Found, Orderable Item Code Does Not Match

> If PACS asserts support for the DICOM Modality Worklist Provider, then when PACS receives an order message containing order control code NW for a case, study instance UID and ICN already in its system for which the orderable item code does not match the orderable item code on the case in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1- acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Order Cancellation – Case and Matching ICN Found

> When PACS receives an order message containing order control code CA for a case and ICN already in its system, PACS will cancel the order if no image acquisition has occurred. The order record will not be deleted, but rather marked as cancelled and removed from the DICOM Modality Worklist. If images have been acquired, PACS retains the already-acquired images as part of the legal record. PACS is responsible for notifying support staff and users as needed that images have already been acquired for this cancelled order.

#### Order Cancellation – Case Found, ICN, SSN and/or Study Instance UID Do Not Match

> When PACS receives an order message containing order control code CA for a case already in its system for which the ICN, SSN and/or Study Instance UID does not match the ICN, SSN and Study Instance UID in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not cancel or otherwise update any order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Order Cancellation – Case Found, DOB, Sex or Name Do Not Match

> When PACS receives an order message containing order control code CA for a case already in its system for which the date of birth, sex and/or name does not match the date of birth, sex and name in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section

> 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not cancel or otherwise update any order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Order Cancellation – Case and Matching ICN Not Found

> When PACS receives an order message containing order control code CA for a case and ICN not already in its system, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data</u>](#basic-patient-data-set) [<u>Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above), and the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above). PACS will record the status of the order as Cancelled.

#### Patient Examined – Case and Matching ICN Found

> When PACS receives an order message containing order control code XO and order status IP or CM for a case, Study Instance UID and ICN already in its system, PACS will update the status of the order to Examined.

#### Patient Examined – Case Not Found

> When PACS receives an order message containing order control code XO and order status IP or CM for a case and Study Instance UID not now in its system, PACS will extract from the HL7 message, and will store in its system, the information contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above) and the [<u>Basic Visit Data Set</u>](#basic-patient-data-set) (see Section [0.2](#basic-patient-data-set) above), and the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above). PACS will record the status of the order as Examined.

#### Patient Examined – Case Found, ICN, SSN and/or Study Instance UID Do Not Match

> When PACS receives an order message containing order control code XO and order status IP or CM for a case already in its system for which the ICN, SSN and/or Study Instance UID does not match the ICN, SSN and Study Instance UID in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Patient Examined – Case Found, DOB, Sex or Name Do Not Match

> When PACS receives an order message containing order control code XO and order status IP or CM for a case already in its system for which the date of birth, sex and/or name does not match the date of birth, sex and name in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1- acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### Patient Examined – Case and Matching ICN Found, Orderable Item Code Does Not Match

> When PACS receives an order message containing order control code XO and order status IP or CM for a case and ICN already in its system for which the orderable item code does not match the orderable item code on the case in its system, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 204 (unknown key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### New or Updated Order – Study Instance UID To Be Assigned from ZDS Segment

> When PACS receives an order message containing order control code NW or XO and there is no previous case assigned to this study instance UID, it shall assign the study instance UID from the ZDS segment to the case that it files on its system. The study instance UID shall be placed in the DICOM header of all images acquired for this study. It shall be available for queries. If there is a previous case already in PACS for which this study instance UID is assigned, then PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment containing a value of AE (application error) in field *MSA-1- acknowledgment code* and a fully populated occurrence of *ERR-1-error code and location*, as described in Section 1.6.10 above, including code 205 (duplicate key identifier) in component 4, and will not update the order. PACS is responsible for notifying support staff and users of anomalies as needed.

#### New Order –VistA Code To Be Stored, CPT Code May Be Stored

> When PACS receives an order message containing order control code NW or XO and there is no previous order on file for this case, PACS shall store the VistA Radiology order code for the orderable item from field OBR-4. PACS may also store the CPT code from field OBR-4, but is not required to do so.

#### Order Received and Filed for Pregnant Patient

> When PACS receives and files an order message for a patient whose Ambulatory Status value in PV1-15 contains B6 (pregnant), PACS shall record that the patient is pregnant.

#### Order Received and Filed for Sensitive/Employee Patient

> When PACS receives and files an order message for a patient whose VIP Indicator value in PV1-16 is set to E (employee) or S (sensitive), PACS shall store the value and shall safeguard the identity of the patient using VA rules for suppressing patient name and other identifying information.

#### Order or Order Update Received – More than 1 Value for Same Identifier

> When PACS receives an order or order update message containing more than one value for the ICN, PACS will notify the sending system of the anomaly(ies) via an HL7 application acknowledgment and will not update any patient record. The application acknowledgment shall contain a value of AE (application error) in field *MSA-1-acknowledgment code* and a fully populated occurrence of *ERR-1- error code and location*, as described in Section 1.6.10 below, including code 207 (application internal error) in component 4. PACS is responsible for notifying support staff and users of anomalies as needed.

### Acknowledgment Message (ACK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Original Mode ACK To Be Returned

> PACS shall return an ACK application acknowledgment, as defined in the HL7 Standard and prescribed by the IHE Radiology Technical Framework. The trigger event of the acknowledgment message shall be equal to the trigger event of the message that was received.

#### ERR Segment To Be Sent for AE and AR Conditions

> When an error is determined to have occurred, PACS shall return the acknowledgment code AE (Application Error) or AR (Application Reject) as appropriate, and shall populate Field *ERR-1-error code and location* with the relevant error information including the appropriate error code from HL7 Table 0357. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Message Type, Trigger Event, Version ID, or Processing Code to Cause Reject

> If the value received in *MSH-9.1-message type, MSH-9.2-trigger event, MSH-11- processing code,* or *MSH-12-version ID* is invalid, the value AR (application

> <span id="_bookmark109" class="anchor"></span>reject) shall be returned in *MSA-1-acknowledgment code*, and the appropriate value from HL7 Table 0357 shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Receiving Application or Receiving Facility to Cause Error

> If the value received in *MSH-5-receiving application* or *MSH-6-receiving facility* is invalid, the value AE (application error) shall be returned in *MSA-1- acknowledgment code*, and the value 103 (table value not found) shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 messages shall be populated and processed according to the following abstract message definitions.

### Order Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ORM Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { NTE } ]</p>
</blockquote></td>
<td><blockquote>
<p>Notes and Comments (for Header)</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ PD1 ]</p>
</blockquote></td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { NTE } ]</p>
</blockquote></td>
<td><blockquote>
<p>Notes and Comments (for Patient ID)</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PV2 ] ]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { IN1</p>
</blockquote></td>
<td><blockquote>
<p>Insurance</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ IN2 ]</p>
</blockquote></td>
<td><blockquote>
<p>Insurance Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td>[ [ IN3 ] ]</td>
<td><blockquote>
<p>Insurance Additional Info. – Cert.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { GT1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Guarantor</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { AL1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Allergy Information</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>{ ORC</p>
</blockquote></td>
<td><blockquote>
<p>Common Order</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ OBR</p>
</blockquote></td>
<td><blockquote>
<p>Observation Request</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ZDS</p>
</blockquote></td>
<td><blockquote>
<p>Additional Identification Information</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>§</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { NTE } ]</p>
</blockquote></td>
<td><blockquote>
<p>Notes and Comments (for Detail)</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ { DG1 } ]</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ { OBX</p>
</blockquote></td>
<td><blockquote>
<p>Observation/Result</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..999]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="odd">
<td>[ { NTE } ]</td>
<td><blockquote>
<p>Notes and Comments (for Results)</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>} ] ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <sup>§</sup> This segment is defined in IHE Rad-TF Transaction 4 (Procedure Scheduled).

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 34%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark110" class="anchor"></span><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ORM Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>{ [ CTI ] }</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Trial Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ BLG ]</p>
</blockquote></td>
<td><blockquote>
<p>Billing Segment</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>4</td>
</tr>
</tbody>
</table>

> }

### Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 35%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ACK Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSA</p>
</blockquote></td>
<td><blockquote>
<p>Message Acknowledgment</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ ERR ]</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

> d according to the following

> Refer to the definition in Section 1.5.1, <u>MSH Segment</u>, for a listing of all the fields defined for the MSH segment in HL7.

> Refer to Section 3.6.1, <u>MSH Segment Fields</u>, for a more detailed explanation of the fields used by VistA.

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PID Segment in HL7, and their usage in the order message. Refer to Section 3.6.2, <u>PID Segment Fields</u>, for a more detailed explanation of the fields used by VistA.

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00104</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00105</p>
</blockquote></td>
<td><blockquote>
<p>Patient ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00106</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identifier List</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>CX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00107</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Patient ID - PID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00108</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00109</p>
</blockquote></td>
<td><blockquote>
<p>Mother’s Maiden Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00110</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Birth</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0001</p>
</blockquote></td>
<td><blockquote>
<p>00111</p>
</blockquote></td>
<td><blockquote>
<p>Sex</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XPN</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00112</p>
</blockquote></td>
<td><blockquote>
<p>Patient Alias</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0005</p>
</blockquote></td>
<td><blockquote>
<p>00113</p>
</blockquote></td>
<td><blockquote>
<p>Race</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>XAD</td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00114</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>00115</p>
</blockquote></td>
<td><blockquote>
<p>County Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark112" class="anchor"></span><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00116</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Home</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00117</p>
</blockquote></td>
<td><blockquote>
<p>Phone Number - Business</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0296</p>
</blockquote></td>
<td><blockquote>
<p>00118</p>
</blockquote></td>
<td><blockquote>
<p>Primary Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0002</p>
</blockquote></td>
<td><blockquote>
<p>00119</p>
</blockquote></td>
<td><blockquote>
<p>Marital Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0006</p>
</blockquote></td>
<td><blockquote>
<p>00120</p>
</blockquote></td>
<td><blockquote>
<p>Religion</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00121</p>
</blockquote></td>
<td><blockquote>
<p>Patient Account Number</p>
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
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00122</p>
</blockquote></td>
<td><blockquote>
<p>SSN Number - Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20</td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>DLN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00123</p>
</blockquote></td>
<td><blockquote>
<p>Driver's License Number - Patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>21</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00124</p>
</blockquote></td>
<td><blockquote>
<p>Mother's Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>22</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0189</p>
</blockquote></td>
<td><blockquote>
<p>00125</p>
</blockquote></td>
<td><blockquote>
<p>Ethnic Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>23</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00126</p>
</blockquote></td>
<td><blockquote>
<p>Birth Place</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00127</p>
</blockquote></td>
<td><blockquote>
<p>Multiple Birth Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>25</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00128</p>
</blockquote></td>
<td><blockquote>
<p>Birth Order</p>
</blockquote></td>
</tr>
<tr class="even">
<td>26</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0171</p>
</blockquote></td>
<td><blockquote>
<p>00129</p>
</blockquote></td>
<td><blockquote>
<p>Citizenship</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>27</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0172</p>
</blockquote></td>
<td><blockquote>
<p>00130</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Military Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>28</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0212</p>
</blockquote></td>
<td><blockquote>
<p>00739</p>
</blockquote></td>
<td><blockquote>
<p>Nationality</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00740</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Date and Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>30</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>00741</p>
</blockquote></td>
<td><blockquote>
<p>Patient Death Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>01535</p>
</blockquote></td>
<td><blockquote>
<p>Identity Unknown Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>32</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0445</p>
</blockquote></td>
<td><blockquote>
<p>01536</p>
</blockquote></td>
<td><blockquote>
<p>Identity Reliability Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>33</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01537</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>34</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01538</p>
</blockquote></td>
<td><blockquote>
<p>Last Update Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>35</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0446</p>
</blockquote></td>
<td><blockquote>
<p>01539</p>
</blockquote></td>
<td><blockquote>
<p>Species Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>36</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0447</p>
</blockquote></td>
<td><blockquote>
<p>01540</p>
</blockquote></td>
<td><blockquote>
<p>Breed Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>37</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01541</p>
</blockquote></td>
<td><blockquote>
<p>Strain</p>
</blockquote></td>
</tr>
<tr class="even">
<td>38</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0429</p>
</blockquote></td>
<td><blockquote>
<p>01542</p>
</blockquote></td>
<td><blockquote>
<p>Production Class Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PV1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the PV1 Segment in HL7, together with their usage in the VistA order message. Refer to Section [3.6.3](#pv1-segment-fields-2), <u>[PV1 Segment Fields](#pv1-segment-fields-2),</u> for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00131</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - PV1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0004</p>
</blockquote></td>
<td><blockquote>
<p>00132</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00133</p>
</blockquote></td>
<td><blockquote>
<p>Assigned Patient Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0007</p>
</blockquote></td>
<td><blockquote>
<p>00134</p>
</blockquote></td>
<td><blockquote>
<p>Admission Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00135</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00136</p>
</blockquote></td>
<td><blockquote>
<p>Prior Patient Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00137</p>
</blockquote></td>
<td><blockquote>
<p>Attending Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00138</p>
</blockquote></td>
<td><blockquote>
<p>Referring Doctor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00139</p>
</blockquote></td>
<td><blockquote>
<p>Consulting Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0069</p>
</blockquote></td>
<td><blockquote>
<p>00140</p>
</blockquote></td>
<td><blockquote>
<p>Hospital Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00141</p>
</blockquote></td>
<td><blockquote>
<p>Temporary Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0087</p>
</blockquote></td>
<td><blockquote>
<p>00142</p>
</blockquote></td>
<td><blockquote>
<p>Preadmit Test Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0092</p>
</blockquote></td>
<td><blockquote>
<p>00143</p>
</blockquote></td>
<td><blockquote>
<p>Re-admission Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0023</p>
</blockquote></td>
<td><blockquote>
<p>00144</p>
</blockquote></td>
<td><blockquote>
<p>Admit Source</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..2]</p>
</blockquote></td>
<td><blockquote>
<p>0009</p>
</blockquote></td>
<td><blockquote>
<p>00145</p>
</blockquote></td>
<td><blockquote>
<p>Ambulatory Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0099</p>
</blockquote></td>
<td><blockquote>
<p>00146</p>
</blockquote></td>
<td><blockquote>
<p>VIP Indicator</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark113" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>00147</p>
</blockquote></td>
<td><blockquote>
<p>Admitting Doctor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0018</p>
</blockquote></td>
<td><blockquote>
<p>00148</p>
</blockquote></td>
<td><blockquote>
<p>Patient Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00149</p>
</blockquote></td>
<td><blockquote>
<p>Visit Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>FC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0064</p>
</blockquote></td>
<td><blockquote>
<p>00150</p>
</blockquote></td>
<td><blockquote>
<p>Financial Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0032</p>
</blockquote></td>
<td><blockquote>
<p>00151</p>
</blockquote></td>
<td><blockquote>
<p>Charge Price Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0045</p>
</blockquote></td>
<td><blockquote>
<p>00152</p>
</blockquote></td>
<td><blockquote>
<p>Courtesy Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0046</p>
</blockquote></td>
<td><blockquote>
<p>00153</p>
</blockquote></td>
<td><blockquote>
<p>Credit Rating</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0044</p>
</blockquote></td>
<td><blockquote>
<p>00154</p>
</blockquote></td>
<td><blockquote>
<p>Contract Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00155</p>
</blockquote></td>
<td><blockquote>
<p>Contract Effective Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00156</p>
</blockquote></td>
<td><blockquote>
<p>Contract Amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00157</p>
</blockquote></td>
<td><blockquote>
<p>Contract Period</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0073</p>
</blockquote></td>
<td><blockquote>
<p>00158</p>
</blockquote></td>
<td><blockquote>
<p>Interest Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0110</p>
</blockquote></td>
<td><blockquote>
<p>00159</p>
</blockquote></td>
<td><blockquote>
<p>Transfer to Bad Debt Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00160</p>
</blockquote></td>
<td><blockquote>
<p>Transfer to Bad Debt Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0021</p>
</blockquote></td>
<td><blockquote>
<p>00161</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Agency Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00162</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Transfer Amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00163</p>
</blockquote></td>
<td><blockquote>
<p>Bad Debt Recovery Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0111</p>
</blockquote></td>
<td><blockquote>
<p>00164</p>
</blockquote></td>
<td><blockquote>
<p>Delete Account Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00165</p>
</blockquote></td>
<td><blockquote>
<p>Delete Account Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0112</p>
</blockquote></td>
<td><blockquote>
<p>00166</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Disposition</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td>25</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0113</p>
</blockquote></td>
<td><blockquote>
<p>00167</p>
</blockquote></td>
<td><blockquote>
<p>Discharged to Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0114</p>
</blockquote></td>
<td><blockquote>
<p>00168</p>
</blockquote></td>
<td><blockquote>
<p>Diet Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0115</p>
</blockquote></td>
<td><blockquote>
<p>00169</p>
</blockquote></td>
<td><blockquote>
<p>Servicing Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0116</p>
</blockquote></td>
<td><blockquote>
<p>00170</p>
</blockquote></td>
<td><blockquote>
<p>Bed Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0117</p>
</blockquote></td>
<td><blockquote>
<p>00171</p>
</blockquote></td>
<td><blockquote>
<p>Account Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00172</p>
</blockquote></td>
<td><blockquote>
<p>Pending Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td>80</td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00173</p>
</blockquote></td>
<td><blockquote>
<p>Prior Temporary Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00174</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00175</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00176</p>
</blockquote></td>
<td><blockquote>
<p>Current Patient Balance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00177</p>
</blockquote></td>
<td><blockquote>
<p>Total Charges</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00178</p>
</blockquote></td>
<td><blockquote>
<p>Total Adjustments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00179</p>
</blockquote></td>
<td><blockquote>
<p>Total Payments</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>00180</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Visit ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0326</p>
</blockquote></td>
<td><blockquote>
<p>01226</p>
</blockquote></td>
<td><blockquote>
<p>Visit Indicator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0010</p>
</blockquote></td>
<td><blockquote>
<p>01274</p>
</blockquote></td>
<td><blockquote>
<p>Other Healthcare Provider</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ORC Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the ORC Segment in HL7. Refer to [Section 3.6.4](#orc-segment-fields), [<u>ORC Segment Fields</u>](#orc-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>0119</p>
</blockquote></td>
<td><blockquote>
<p>00215</p>
</blockquote></td>
<td><blockquote>
<p>Order Control</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00216</p>
</blockquote></td>
<td><blockquote>
<p>Placer Order Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00217</p>
</blockquote></td>
<td><blockquote>
<p>Filler Order Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>00218</p>
</blockquote></td>
<td><blockquote>
<p>Placer Group Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark114" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0038</p>
</blockquote></td>
<td><blockquote>
<p>00219</p>
</blockquote></td>
<td><blockquote>
<p>Order Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0121</p>
</blockquote></td>
<td><blockquote>
<p>00220</p>
</blockquote></td>
<td><blockquote>
<p>Response Flag</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00221</p>
</blockquote></td>
<td><blockquote>
<p>Quantity/Timing</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00222</p>
</blockquote></td>
<td><blockquote>
<p>Parent</p>
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00223</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Transaction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00224</p>
</blockquote></td>
<td><blockquote>
<p>Entered By</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00225</p>
</blockquote></td>
<td><blockquote>
<p>Verified By</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00226</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00227</p>
</blockquote></td>
<td><blockquote>
<p>Enterer’s Location</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..8]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00228</p>
</blockquote></td>
<td><blockquote>
<p>Call Back Phone Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00229</p>
</blockquote></td>
<td><blockquote>
<p>Order Effective Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00230</p>
</blockquote></td>
<td><blockquote>
<p>Order Control Code Reason</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00231</p>
</blockquote></td>
<td><blockquote>
<p>Entering Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00232</p>
</blockquote></td>
<td><blockquote>
<p>Entering Device</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00233</p>
</blockquote></td>
<td><blockquote>
<p>Action By</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0339</a></p>
</blockquote></td>
<td><blockquote>
<p>01310</p>
</blockquote></td>
<td><blockquote>
<p>Advanced Beneficiary Notice Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XON</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01311</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Facility Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XAD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01312</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Facility Address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01313</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Facility Phone Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XAD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01314</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Provider Address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CWE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01473</p>
</blockquote></td>
<td><blockquote>
<p>Order Status Modifier</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the OBR Segment in HL7. Refer to [Section 3.6.5](#obr-segment-fields), [<u>OBR Segment Fields</u>](#obr-segment-fields), for a more detailed explanation of the fields used in the VistA order message.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00237</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - OBR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00216</p>
</blockquote></td>
<td><blockquote>
<p>Placer Order Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00217</p>
</blockquote></td>
<td><blockquote>
<p>Filler Order Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00238</p>
</blockquote></td>
<td><blockquote>
<p>Universal Service Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00239</p>
</blockquote></td>
<td><blockquote>
<p>Priority - OBR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00240</p>
</blockquote></td>
<td><blockquote>
<p>Requested Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00241</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00242</p>
</blockquote></td>
<td><blockquote>
<p>Observation End Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CQ</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00243</p>
</blockquote></td>
<td><blockquote>
<p>Collection Volume</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00244</p>
</blockquote></td>
<td><blockquote>
<p>Collector Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0065</p>
</blockquote></td>
<td><blockquote>
<p>00245</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Action Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00246</p>
</blockquote></td>
<td><blockquote>
<p>Danger Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00247</p>
</blockquote></td>
<td><blockquote>
<p>Relevant Clinical Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00248</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Received Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>0070</p>
<p>0163</p>
<p>0369</p>
</blockquote></td>
<td><blockquote>
<p>00249</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00226</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..8]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00250</p>
</blockquote></td>
<td><blockquote>
<p>Order Callback Phone Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00251</p>
</blockquote></td>
<td><blockquote>
<p>Placer Field 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00252</p>
</blockquote></td>
<td><blockquote>
<p>Placer Field 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00253</p>
</blockquote></td>
<td><blockquote>
<p>Filler Field 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00254</p>
</blockquote></td>
<td><blockquote>
<p>Filler Field 2</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark115" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00255</p>
</blockquote></td>
<td><blockquote>
<p>Results Rpt/Status Chng - Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00256</p>
</blockquote></td>
<td><blockquote>
<p>Charge to Practice</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0074</p>
</blockquote></td>
<td><blockquote>
<p>00257</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic Serv Sect ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0123</p>
</blockquote></td>
<td><blockquote>
<p>00258</p>
</blockquote></td>
<td><blockquote>
<p>Result Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00259</p>
</blockquote></td>
<td><blockquote>
<p>Parent Result</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>27</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00221</p>
</blockquote></td>
<td><blockquote>
<p>Quantity/Timing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00260</p>
</blockquote></td>
<td><blockquote>
<p>Result Copies To</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00222</p>
</blockquote></td>
<td><blockquote>
<p>Parent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0124</p>
</blockquote></td>
<td><blockquote>
<p>00262</p>
</blockquote></td>
<td><blockquote>
<p>Transportation Mode</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00263</p>
</blockquote></td>
<td><blockquote>
<p>Reason for Study</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00264</p>
</blockquote></td>
<td><blockquote>
<p>Principal Result Interpreter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00265</p>
</blockquote></td>
<td><blockquote>
<p>Assistant Result Interpreter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00266</p>
</blockquote></td>
<td><blockquote>
<p>Technician</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00267</p>
</blockquote></td>
<td><blockquote>
<p>Transcriptionist</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00268</p>
</blockquote></td>
<td><blockquote>
<p>Scheduled Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01028</p>
</blockquote></td>
<td><blockquote>
<p>Number of Sample Containers</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01029</p>
</blockquote></td>
<td><blockquote>
<p>Transport Logistics of Collected Sample</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01030</p>
</blockquote></td>
<td><blockquote>
<p>Collector’s Comment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01031</p>
</blockquote></td>
<td><blockquote>
<p>Transport Arrangement Responsibility</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0224</a></p>
</blockquote></td>
<td><blockquote>
<p>01032</p>
</blockquote></td>
<td><blockquote>
<p>Transport Arranged</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0225</a></p>
</blockquote></td>
<td><blockquote>
<p>01033</p>
</blockquote></td>
<td><blockquote>
<p>Escort Required</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01034</p>
</blockquote></td>
<td><blockquote>
<p>Planned Patient Transport Comment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0088</p>
</blockquote></td>
<td><blockquote>
<p>00393</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0340</p>
</blockquote></td>
<td><blockquote>
<p>01316</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Code Modifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0411</a></p>
</blockquote></td>
<td><blockquote>
<p>01474</p>
</blockquote></td>
<td><blockquote>
<p>Placer Supplemental Service Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0411</a></p>
</blockquote></td>
<td><blockquote>
<p>01475</p>
</blockquote></td>
<td><blockquote>
<p>Filler Supplemental Service Information</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ZDS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the ZDS Segment in HL7. Refer to [Section 3.6.6](#zds-segment-fields), [<u>ZDS Segment Fields</u>](#zds-segment-fields), for a more detailed explanation of the fields used by VistA.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>RP</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Study Instance UID</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the order message, the OBX Segment is used to communicate ancillary order information including history. The following is a listing of all the fields defined for the OBX Segment in HL7. Refer to Section [3.6.7](#obx-segment-fields-2), [<u>OBX Segment Fields</u>](#obx-segment-fields-2), for a more detailed explanation of the fields used by VistA.

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>0125</p>
</blockquote></td>
<td><blockquote>
<p>00569</p>
</blockquote></td>
<td><blockquote>
<p>Set ID – OBX</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00570</p>
</blockquote></td>
<td><blockquote>
<p>Value Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00571</p>
</blockquote></td>
<td><blockquote>
<p>Observation Identifier</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark117" class="anchor"></span><strong>Seq</strong></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00572</p>
</blockquote></td>
<td><blockquote>
<p>Observation Sub-ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td>65536<a href="#_bookmark118"><sup></sup></a></td>
<td></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..4]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00573</p>
</blockquote></td>
<td><blockquote>
<p>Observation Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00574</p>
</blockquote></td>
<td><blockquote>
<p>Units</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00575</p>
</blockquote></td>
<td><blockquote>
<p>Reference Range</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0078</p>
</blockquote></td>
<td><blockquote>
<p>00576</p>
</blockquote></td>
<td><blockquote>
<p>Abnormal Flags</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00577</p>
</blockquote></td>
<td><blockquote>
<p>Probability</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00578</p>
</blockquote></td>
<td><blockquote>
<p>Nature of Abnormal Test</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0085</p>
</blockquote></td>
<td><blockquote>
<p>00579</p>
</blockquote></td>
<td><blockquote>
<p>Observation Result Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00580</p>
</blockquote></td>
<td><blockquote>
<p>Date Last Observation Normal Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td>13</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00581</p>
</blockquote></td>
<td><blockquote>
<p>User Defined Access Checks</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00582</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Observation</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00583</p>
</blockquote></td>
<td><blockquote>
<p>Producer’s ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00584</p>
</blockquote></td>
<td><blockquote>
<p>Responsible Observer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>17</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00936</p>
</blockquote></td>
<td><blockquote>
<p>Observation Method</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>18</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01479</p>
</blockquote></td>
<td><blockquote>
<p>Equipment Instance Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>19</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01480</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of the Analysis</p>
</blockquote></td>
</tr>
</tbody>
</table>

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.5.9](#msa-segment), [<u>MSA Segment</u>](#msa-segment), for a listing of all the fields defined for the MSA segment in HL7.

> Refer to the Sec[tion 1.6.9](#msa-segment-fields), [<u>MSA Segment Fields</u>](#msa-segment-fields), for a more detailed explanation of the fields used by VistA.

### ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the definitions in Sectio[n 1.5.10](#err-segment), [<u>ERR Segment</u>](#err-segment), for a listing of all the fields defined for the ERR segment in HL7.

> Refer to Section [1.6.10](#err-segment-fields), [<u>ERR Segment Fields</u>](#err-segment-fields), for a more detailed explanation of the fields used by VistA.

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSH-1-Field Separator

> This field contains the top-level delimiter for HL7 elements within segments.

#### MSH-2-Encoding Characters

> This field contains the component separator (secondary element delimiter), repetition separator, escape character, and subcomponent separator (tertiary element delimiter).

> <span id="_bookmark118" class="anchor"></span><sup>\*\*</sup> The length and data type of this field are variable, depending on *OBX-2-Value Type*.

#### MSH-3-Sending Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA order message, the first component of this field shall be populated with the value RA-SERVER-IMG from user-defined Table 0361, *Sending/Receiving Application*. PACS shall return this value in component MSH-

> 5.1 of the acknowledgment message. The second and third components of MSH-3 are not valued.

#### MSH-4-Sending Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, the first component of this field shall be populated from user-defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was generated. PACS shall return this value in component MSH-6.1 of the acknowledgment message. The second and third components of MSH-4 are not valued.

#### MSH-5-Receiving Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, the first component of this field shall be populated from user-defined Table 0361, *Sending/Receiving Application*, with the name of the PACS application. PACS shall return this value in component MSH-3.1 of the acknowledgment message. The second and third components of MSH-5 are not valued.

#### MSH-6-Receiving Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark120" class="anchor"></span>In the VistA message, the first component of this field shall be populated from user-defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was received. PACS shall return this value in field MSH-4 of the acknowledgment message. The second and third components of MSH-6 are not valued.

#### MSH-7-Date/Time of Message

> This field contains the date and time that the sending system built the message.

#### MSH-9-Message Type

> This field is of data type CM. Its components are as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>Trigger Event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0354</p>
</blockquote></td>
<td><blockquote>
<p>Message Structure</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

> *MSH-9.1-Message Type*

> This component contains a value from HL7 Table 0076, *Message Type*. For the order message, it will always contain the value ORM.

#### MSH-9.2-Trigger Event

> This component contains a value from HL7 Table 0003, *Event Type*. For the order message, it will always contain the value O01 (oh zero one).

#### MSH-10-Message Control ID

> This field will contain a unique identifier for the message.

#### MSH-11-Processing ID

> This field is of type PT, which is defined as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0103</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0207</p>
</blockquote></td>
<td><blockquote>
<p>Processing Mode</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

#### MSH-11.1-Processing ID

> This field contains one of the following values from HL7 Table 0103, *Processing ID.*

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark121" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>Production</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Debugging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T</td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-11.2-Processing Mode

> This field contains one of the following values from HL7 Table 0207, *Processing Mode*.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A</td>
<td><blockquote>
<p>Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>R</td>
<td><blockquote>
<p>Restore from archive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>I</td>
<td><blockquote>
<p>Initial load</p>
</blockquote></td>
</tr>
<tr class="even">
<td>T</td>
<td><blockquote>
<p>Current processing, transmitted at intervals (scheduled or on demand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>not present</p>
</blockquote></td>
<td><blockquote>
<p>Not present (the default, meaning <em>current</em> processing)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-12-Version ID

> This field is of type VID, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internationalization Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internal Version ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This field’s first component will always contain the value 2.3.1 from HL7 Table 0104, *Version ID*. Although the VistA message pre-adopts certain Version 2.4 structures, such as the ROL segment, receivers that are unable to recognize Version 2.4 may use Version 2.3.1 syntax rules as prescribed by IHE. It is expected that receivers not now using HL7 Version 2.3.1 will be able to process the V2.3.1 messages according to the HL7 rules for backward compatibility. At such time as IHE is revised to a later version of HL7, receivers will be expected to adapt to the new structures within a stated period of time following the revision.

> Other components of this field will not be used.

#### MSH-17-Country Code

> This field is of type ID. It will always contain the value USA from the ISO 3166 country code table.

### PID Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PID-3-Patient Identifier List

> Field PID-3 is used to transmit the patient Integration Control Number (ICN). This field is of data type CX, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Check Digit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

> *PID-3.1-ID*

> This is the alphanumeric identification string.

#### PID-3.4-Assigning Authority

> This component contains the entity that assigned the identifier value in *PID-3.1- ID*. It is of data type HD, which has 3 subcomponents defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> At present, only the first subcomponent should be considered for the purpose of identifying the assigning authority. Subcomponent 1 will contain the value USVHA*,* meaning United States Veterans Health Administration, from user- defined Table 0300, *Namespace ID*.

> In future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-3.5-Identifier Type

> The value in this component distinguishes the kind of identifier contained in *PID- 3.1-ID*. It will contain the value NI, meaning National unique individual identifier, from user-defined Table 0203, *Identifier Type*.

#### PID-5-Patient Name

> This field is of data type XPN, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>35</td>
<td><blockquote>
<p>FN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark124" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td>35</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>10</td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0200</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>10</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 7, Name Type Code, indicates the type of name given in Components 1-6, such as legal, birth name, or alias. At present, VistA only uses name type L (legal).

#### PID-7-Date/Time of Birth

> This is the date and time that the patient was born, as far as is known. It may be as imprecise as the four-digit birth year (*e.g.*, 1962).

#### PID-8-Sex

> This field contains the sex of the patient. It is populated with one of the following values from user-defined Table 0001, *Sex*, if a value is known.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>Female</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Male</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Unknown</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10-Race

> This field contains a code for the patient’s race. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-10.1-Identifier

> This component contains the RACE INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0005, *Race*.

#### PID-10.3-Name of Coding System

> The value of this component shall be 0005.

#### PID-10.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1002-5</p>
</blockquote></td>
<td><blockquote>
<p>AMERICAN INDIAN OR ALASKA NATIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2028-9</p>
</blockquote></td>
<td><blockquote>
<p>ASIAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2054-5</p>
</blockquote></td>
<td><blockquote>
<p>BLACK OR AFRICAN AMERICAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2076-8</p>
</blockquote></td>
<td><blockquote>
<p>NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2106-3</p>
</blockquote></td>
<td><blockquote>
<p>WHITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-10.6-Name of Coding System

> This component shall be populated CDC.

#### PID-11-Patient Address

> This field contains the patient’s address. It is of data type XAD, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Street Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Other Designation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>City</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>State or Province</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ZIP or Postal Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0190</p>
</blockquote></td>
<td><blockquote>
<p>Address Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Other Geographic Designation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0289</p>
</blockquote></td>
<td><blockquote>
<p>County/Parish Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0288</p>
</blockquote></td>
<td><blockquote>
<p>Census Tract</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Address Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13-Phone Number – Home

> This field contains the patient’s home telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="5"></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark126" class="anchor"></span>Only the first three components of this field are used. They are populated as follows.

#### PID-13.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-13.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-13.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14-Phone Number – Business

> This field contains the patient’s work telephone number. Data type XTN is used, whose structure is as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>0201</p>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### PID-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### PID-14.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with the following value from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-14.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with the following value from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-19-SSN Number – Patient

> This field carries the patient Social Security Number, for backward compatibility with versions of HL7 prior to Version 2.3.1. The Social Security Number is a secondary patient identifier. For the primary patient identifier, use the Integration Control Number from [<u>PID-3-Patient Identifier List</u>](#pid-3-patient-identifier-list).

#### PID-22-Ethnic Group

> This field contains a code indicating whether the patient is of Hispanic descent. The data type of this field is CE, whose components are as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are valued.

#### PID-22.1-Identifier

> This component contains the ETHNICITY INFORMATION value from the VistA PATIENT File, which is derived from user-defined Table 0189, *Ethnic Group*.

#### PID-22.3-Name of Coding System

> The value of this component shall be 0189.

#### PID-22.4-Alternate Identifier

> This component contains the appropriate value, if one exists, from the following table.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0000-0</p>
</blockquote></td>
<td><blockquote>
<p>DECLINED TO ANSWER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2135-2</p>
</blockquote></td>
<td><blockquote>
<p>HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2186-5</p>
</blockquote></td>
<td><blockquote>
<p>NOT HISPANIC OR LATINO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9999-4</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN BY PATIENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PID-22.6-Name of Coding System

> This component shall be populated CDC.

### PV1 Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PV1-2-Patient Class

> This field designates whether the patient is an inpatient (I) or an outpatient (O).

#### PV1-3-Assigned Patient Location

> For inpatients, this field designates the patient’s location in the medical center. The data type of this field is PL, which is defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0302</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0303</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0304</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0306</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0305</p>
</blockquote></td>
<td><blockquote>
<p>Person Location Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0307</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0308</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Location Description</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VistA sends Component 1, Point of Care, as three subcomponents, of which the first is an internal entry number into the VistA WARD LOCATION File (#42), and the second is the name of the ward location; the third is the internal designator of the WARD LOCATION File and should be ignored.

#### PV1-7-Attending Doctor

> This is the physician responsible for the care of the patient during the present encounter. VistA values this field for inpatient encounters only.

> The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-8-Referring Doctor

> This is the physician that placed the order. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### PV1-10-Hospital Service

> This is the treating specialty assigned to the patient with the most recent movement. VistA values this field for inpatient encounters only. When populated, it contains a value from user-defined Table 0069, *Hospital Service*; VistA sends values from the HOSPITAL LOCATION File (#44).

#### PV1-15-Ambulatory Status

> This field indicates any permanent or transient conditions affecting the patient’s mode of transportation. It may contain one or more values from user-defined Table 0009, *Ambulatory Status.* If the patient’s ambulatory status is not known, this field is not populated.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A0</p>
</blockquote></td>
<td><blockquote>
<p>No functional limitations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A2</p>
</blockquote></td>
<td><blockquote>
<p>Wheelchair/stretcher bound</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B6</p>
</blockquote></td>
<td><blockquote>
<p>Pregnant</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The VistA RAD/NUC MED ORDERS File contains two fields that decide the values set into this field: PREGNANT and MODE OF TRANSPORT. Because of this fact, this field may repeat when the patient is both ambulatory and pregnant.

#### PV1-16-VIP Indicator

> This field is used to indicate that the patient is an employee, or that patient record is sensitive and should not be made available for general personnel access. If one of these conditions applies, VistA populates this field with one of the following values from user-defined Table 0099, *VIP Indicator.*

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>E</td>
<td><blockquote>
<p>Patient is a VA employee</p>
</blockquote></td>
</tr>
<tr class="even">
<td>S</td>
<td><blockquote>
<p>Patient record is sensitive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ES</p>
</blockquote></td>
<td><blockquote>
<p>Patient is a VA employee and patient record is sensitive</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PV1-19-Visit

> This field contains a pointer to the VistA RAD/NUC MED ORDERS File.

### ORC Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ORC-1-Order Control

> This field is of data type ID. It will contain one of the following values from HL7 Table 0119, *Order Control Codes*.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CA</p>
</blockquote></td>
<td><blockquote>
<p>Cancel order/service request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NW</p>
</blockquote></td>
<td><blockquote>
<p>New order/service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XO</p>
</blockquote></td>
<td><blockquote>
<p>Change order/service request</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ORC-2-Placer Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### ORC-3-Filler Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### ORC-5-Order Status

> This field is of data type ID. It will contain one of the following values from HL7 Table 0038, *Order Status*.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CA</p>
</blockquote></td>
<td><blockquote>
<p>Order was canceled</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>Order is completed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>In process, unspecified</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ORC-7-Quantity/Timing

> This field is of data type TQ, whose components are as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CQ</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="10"></td>
<td><blockquote>
<p>Quantity</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Interval</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>End Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Priority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Condition</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>65535</td>
<td>TX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Conjunction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Order Sequencing</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark134" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Occurrence Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>NM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Total Occurrences</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are populated.

> *ORC-7.4-Start Date/Time*

> This is the date and time requested for the start of the order.

#### ORC-7.6-Priority

> This component contains the priority of the order. It will be populated with one of the following values.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>S</td>
<td><blockquote>
<p>Stat (with highest priority)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>A</td>
<td><blockquote>
<p>ASAP (fill after Stat orders)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>R</td>
<td><blockquote>
<p>Routine (the default)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ORC-8-Parent

> This field is valued either to identify an examset or printset, or to indicate that the parent order of the examset or printset has been purged.

> If the order is part of an examset, the field will be valued as follows:

> EXAMSET: *procedure_name*

> If the order is part of a printset, the field will be valued as follows:

> PRINTSET: *procedure_name*

> If the parent order has been purged, the field will be valued as follows:

#### ORIGINAL ORDER PURGED

#### ORC-9-Date/Time of Transaction

> This is the date and time that the order was entered into VistA.

#### ORC-10-Entered By

> This is the name of the person who entered the order into VistA. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="7"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark135" class="anchor"></span><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="8"></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### ORC-12-Ordering Provider

> This field contains the ID number and name of the provider that requested the order. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="15"></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### ORC-13-Enterer’s Location

> This is the location of the enterer in the medical center, if known. The data type of this field is PL, which is defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0302</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0303</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0304</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0306</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0305</p>
</blockquote></td>
<td><blockquote>
<p>Person Location Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0307</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0308</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Location Description</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark136" class="anchor"></span>Only the first component is populated. It contains the name of the enterer’s service/section from the VistA SERVICE/SECTION File (#49).

#### ORC-14-Call Back Phone Number

> This is the telephone number of the provider identified in *ORC-11-Ordering Provider*. It is used to get clarification of a request or other information regarding the order. Up to eight telephone numbers may be entered into this field.

> The data type of this field is XTN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="7"><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### ORC-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### ORC-14.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with one of the following values from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>Beeper Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ORC-14.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with one of the following values from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark137" class="anchor"></span>FX</p>
</blockquote></th>
<th><blockquote>
<p>Fax</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>Beeper</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ORC-17-Entering Organization

> This is the service/section of the medical center that contains the person identified in *ORC-10-Entered By*. Information in this field is obtained from the VistA SERVICE/SECTION File. The data type of this field is CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components of this field are defined as follows.

#### ORC-17.1-Identifier

> This is the abbreviation for the service/section of the medical center.

#### ORC-17.2-Text

> This is the full name of the service/section of the medical center.

#### ORC-17.3-Name of Coding System

> This component shall contain the value VISTA49.

### OBR Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBR-1-Set ID

> This is an integer corresponding to the ordinal position of this OBR segment in the message. The first occurrence is labeled 1, the second 2, and so on.

#### OBR-2-Placer Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### OBR-3-Filler Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### OBR-4-Universal Service Identifier

> This field is of data type CE (coded entity), which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components of this field are defined as follows.

> *OBR-4.1-Identifier*

> This component contains the CPT code from the VistA CPT File (#81).

#### OBR-4.2-Text

> This component contains the short name associated with the CPT code in *OBR- 4.1-Identifier*.

#### OBR-4.3-Name of Coding System

> This component always contains the value C4.

#### OBR-4.4-Alternate Identifier

> This component contains the internal entry number of this procedure in the VistA RAD/NUC MED PROCEDURES File (#71).

#### OBR-4.5-Alternate Text

> This component contains the name of the procedure as defined in the RAD/NUC MED PROCEDURES File.

#### OBR-4.6-Name of Alternate Coding System

> This component always contains the value 99RAP.

#### OBR-5-Priority

> This field contains the priority of the order. It is populated to satisfy IHE requirements, but is intended for backward compatibility only.

> <span id="_bookmark140" class="anchor"></span>Valid values are as follows.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>S</td>
<td><blockquote>
<p>Stat</p>
</blockquote></td>
</tr>
<tr class="even">
<td>A</td>
<td><blockquote>
<p>ASAP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Routine</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-15-Specimen Source

> This field is of data type CM. Its components are as follows.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Specimen Source Name or Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>65535</td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Additives</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>65535</td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Freetext</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Body Site</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Site Modifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Collection Method Modifier Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only component 5 is populated. When a body site modifier (LEFT and/or RIGHT) is included in the order, that value will be sent in subcomponent 2 of component 5.

#### OBR-16-Ordering Provider

> This field contains the ID number and name of the provider that requested the order. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0297</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0200</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### OBR-17-Order Callback Phone Number

> This field contains up to eight telephone numbers that may be used to report order status or results. The data type of this field is XTN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark141" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### OBR-17.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with one of the following values from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>Beeper Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-17.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with one of the following values from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>Fax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>Beeper</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-18-Placer Field 1

> This field contains the inverse date/time of the exam in internal VistA format, concatenated with the VistA exam sub-file internal entry number. Hyphen (-) is used as the delimiter.

#### OBR-19-Placer Field 2

> This field contains the exam date and time (as MMDDYY), concatenated with the case number. Hyphen (-) is used as the delimiter.

#### OBR-21-Filler Field 2

> This field contains the internal entry number of the VistA IMAGING LOCATION File (#79.1), concatenated with the name from the VistA HOSPITAL LOCATION File (#44), concatenated with the internal entry number from the VistA INSTITUTION File (#4), concatenated with the name from the INSTITUTION File. The component separator escape sequence (\S\\) is used as the delimiter.

#### OBR-24-Diagnostic Service Section ID

> This field contains the single known Procedure Modality associated with the type of examination being ordered. (If more than one Procedure Modality is known to VistA, nothing is sent in this field.) The terms used are from the VistA RAD MODALITY DEFINED TERMS File (#73.1).

#### OBR-27-Quantity/Timing

> This field is of data type TQ, whose components are as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><strong>DT</strong></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CQ</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="12"></td>
<td><blockquote>
<p>Quantity</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Interval</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>TS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>End Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Priority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Condition</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>65535</td>
<td>TX</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>ST</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Conjunction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Order Sequencing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>CE</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence Duration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>NM</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Total Occurrences</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following components are populated.

#### OBR-27.4-Start Date/Time

> This is the date and time requested for the start of the order.

#### OBR-27.6-Priority

> This component contains the priority of the order. It will be populated with one of the following values.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>S</td>
<td><blockquote>
<p>Stat (with highest priorify)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>A</td>
<td><blockquote>
<p>ASAP (fill after Stat orders)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark143" class="anchor"></span><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>R</td>
<td><blockquote>
<p>Routine (the default)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-29-Parent

> This field is valued either to identify an examset or printset, or to indicate that the parent order of the examset or printset has been purged.

> If the order is part of an examset, the field will be valued as follows:

> EXAMSET: *procedure_name*

> If the order is part of a printset, the field will be valued as follows:

> PRINTSET: *procedure_name*

> If the parent order has been purged, the field will be valued as follows:

#### ORIGINAL ORDER PURGED

#### OBR-30-Transportation Mode

> This field describes how, or whether, to transport a patient. It shall contain one of the following values from HL7 Table 0124, *Transportation Mode*:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 60%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HL7 Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VistA Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CART</p>
</blockquote></td>
<td><blockquote>
<p>Cart - patient travels on cart or gurney</p>
</blockquote></td>
<td><blockquote>
<p>STRETCHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PORT</p>
</blockquote></td>
<td><blockquote>
<p>The examining device goes to patient’s location</p>
</blockquote></td>
<td><blockquote>
<p>PORTABLE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WALK</p>
</blockquote></td>
<td><blockquote>
<p>Patient walks to diagnostic service</p>
</blockquote></td>
<td><blockquote>
<p>AMBULATORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WHLC</p>
</blockquote></td>
<td><blockquote>
<p>Wheelchair</p>
</blockquote></td>
<td><blockquote>
<p>WHEELCHAIR</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-31-Reason for Study

> This field is of data type CE. Its components are structured as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 2, Text, is populated with the narrative reason for study.

### ZDS Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ZDS-1-Study Instance UID

> This field contains the unique identifier that VistA assigns to the study. The data type of this field is RP, which is defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>250</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>250</td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Application ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0191</p>
</blockquote></td>
<td><blockquote>
<p>Type of Data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0291</p>
</blockquote></td>
<td><blockquote>
<p>Subtype</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components of this field are populated as follows.

> *ZDS-1.1-Pointer*

> This component contains the ISO Object Identifier (OID) value that VistA has assigned to the study. PACS and modalities shall use this value rather than assigning one of their own.

#### ZDS-1.2-Application ID

> This component identifies the application that generated the value in Component

1.  Its value will always be VISTA.

#### ZDS-1.3-Type of Data

> This component contains the general type of data that is being pointed to. Its value will always be Application.

#### ZDS-1.4-Subtype

> This component contains the specific type of data that is being pointed to. Its value will always be DICOM.

### OBX Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-2-Value Type

> This field contains the data type of the information carried in *OBX-5-Observation Value.* It is populated with one of the following values from HL7 Table 0125, *Value Type*.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Coded Element</p>
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

#### OBX-3-Observation Identifier

> This field classifies the kind of information carried in *OBX-5-Observation Value.*

> Its data type is CE, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Components 1, *Identifier*, and 2, *Text*, are populated as follows.

> Component 3 is always valued L. OBX-5-Observation Value

> This field contains the actual value whose data type is given in *OBX-2-Value Type* and whose classification is given in *OBX-3-Observation Identifier*. Its formatting follows the rules for the data type given in OBX-2.

> For observation identifier values C4 (CPT MODIFIERS), D (DIAGNOSTIC CODE), and P (PROCEDURE), the data type of OBX-5 shall be CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> For all other observation identifier values, the data type of OBX-5 shall be TX.

#### OBX-6-Units

> For quantitative measurements, this field contains the units of the observation. For observations other than quantitative measurements, this field is not populated.

> The data type of this field is CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 3 is always valued ISO+, indicating the use of units of measure from ISO Standard 2955-1983.

#### OBX-11-Observation Result Status

> This field is of data type ID. In the order message, it is populated with the value O (order detail description only, no result) from HL7 Table 0085, *Observation Result Status Codes Interpretation.*

### MSA Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.9](#msa-segment-fields), [<u>MSA Segment Fields</u>](#msa-segment-fields), for a more detailed explanation of the MSA fields used in VistA messaging.

### ERR Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.10](#err-segment-fields), [<u>ERR Segment Fields</u>](#err-segment-fields), for a more detailed explanation of the ERR fields used in VistA messaging.

# Report Transmission & Storage Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This transaction is used by VistA Radiology to transmit a radiology report to PACS.

![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/008.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Actor: VistA Radiology

> Role: Transmits radiology report information to ancillary VistA Modules and clinical systems when VistA Radiology reports are filed.

> Actor: PACS

> Role: Receives and files radiology report information.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The actors in this Profile shall perform the behaviors shown in the following activity diagram.

> ![](profiles-for-hl7-messages-from-vista-to-commercial-pacs/009.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vista and PACS shall generate and process HL7 messages according to the following functional and business requirements.

### Report Message (ORU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Radiology shall transmit an ORU message to PACS when a report is filed. PACS shall process the message in conformance with the following requirements.

#### VistA Is System of Legal Record

> VistA will maintain the legal record for radiology reports. PACS will receive radiology reports only through the VistA HL7 interface. Reports will have a status of either F for final verified report or R for released, not verified report.

#### Report Received by PACS – Case and ICN Found, No Previous Report on File

> When PACS receives a report message for a case and ICN already in its system for which it has not previously received a report, PACS will file the report labeled with its proper status and will display the report status on the report display.

> PACS will extract from the HL7 message, and will store in its system, the data contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above), the [<u>Basic Order</u>](#basic-order-data-set) [<u>Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above), and the [<u>Basic Report Data Set</u>](#basic-report-data-set) (see Section [0.4](#basic-report-data-set) above).

#### Report Received by PACS – Case and ICN Found, Previous Report Already on File

> When PACS receives a report message for a case and ICN already in its system for which it has already previously received a report, PACS will file the report labeled with its proper status if the value of *OBR-22-Results Rpt/Status Chng* in the message is later than the value of *OBR-22-Results Rpt/Status Chng* in the previous message. At a minimum, PACS will retain the most recently dated report, as determined by the value of *OBR-22-Results Rpt/Status Chng,* for the case, irrespective of the order in which reports for the case are received. PACS may store multiple versions of the report. The default for display shall be the most recently dated report, as determined by the value of *OBR-22-Results Rpt/Status Chng*. PACS will extract from the HL7 message, and will store in its system, the data contained in the [<u>Basic Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above), the [<u>Basic</u>](#basic-order-data-set) [<u>Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above), and the [<u>Basic Report Data Set</u>](#basic-report-data-set) (see Section [0.4](#basic-report-data-set) above).

#### Report Received by PACS – Case and ICN Not Found

> When PACS receives a report message for a case and ICN not already in its system, PACS will file the report labeled with its proper status. PACS will extract from the HL7 message, and will store in its system, the data contained in the [<u>Basic</u>](#basic-patient-data-set) [<u>Patient Data Set</u>](#basic-patient-data-set) (see Section [0.1](#basic-patient-data-set) above), the [<u>Basic Order Data Set</u>](#basic-order-data-set) (see Section [0.3](#basic-order-data-set) above), and the [<u>Basic Report Data Set</u>](#basic-report-data-set) (see Section [0.4](#basic-report-data-set) above). This allows for loading of historical reports.

### Acknowledgment Message (ACK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Original Mode ACK To Be Returned

> PACS shall return an ACK application acknowledgment, as defined in the HL7 Standard and prescribed by the IHE Radiology Technical Framework. The trigger event of the acknowledgment message shall be equal to the trigger event of the message that was received.

#### ERR Segment To Be Sent for AE and AR Conditions

> When an error is determined to have occurred, PACS shall return the acknowledgment code AE (Application Error) or AR (Application Reject) as appropriate, and shall populate Field ERR-1-error code and location with the relevant error information including the appropriate error code from HL7 Table 0357. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Message Type, Trigger Event, Version ID, or Processing Code to Cause Reject

> If the value received in *MSH-9.1-message type, MSH-9.2-trigger event, MSH-11- processing code,* or *MSH-12-version ID* is invalid, the value AR (application reject) shall be returned in *MSA-1-acknowledgment code*, and the appropriate value from HL7 Table 0357 shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

#### Incorrect Receiving Application or Receiving Facility to Cause Error

> If the value received in *MSH-5-receiving application* or *MSH-6-receiving facility* is invalid, the value AE (application error) shall be returned in *MSA-1- acknowledgment code*, and the value 103 (table value not found) shall be returned in *ERR-1-error code and location*. See Section 1.6.10 for more information on populating *ERR-1-error code and location*.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 messages shall be populated and processed according to the following abstract message definitions.

### Report Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 36%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ORU Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>{ [ PID</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identification</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td>[ PD1 ]</td>
<td><blockquote>
<p>Additional Demographics</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td>[ { NK1 } ]</td>
<td><blockquote>
<p>Next of Kin / Associated Parties</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td>[ { NTE } ]</td>
<td><blockquote>
<p>Notes and Comments</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>[ PV1</p>
</blockquote></td>
<td><blockquote>
<p>Patient Visit</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td>[ PV2 ] ]</td>
<td><blockquote>
<p>Patient Visit – Additional Info.</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>{ [ ORC ]</p>
</blockquote></td>
<td><blockquote>
<p>Common Order</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="even">
<td><blockquote>
<p>OBR</p>
</blockquote></td>
<td><blockquote>
<p>Observation Request</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="odd">
<td>[ { NTE } ]</td>
<td><blockquote>
<p>Notes and Comments (for Detail)</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark153" class="anchor"></span>[ { OBX</p>
</blockquote></th>
<th><blockquote>
<p>Observation/Result</p>
</blockquote></th>
<th><blockquote>
<p>RE</p>
</blockquote></th>
<th><blockquote>
<p>[0..999]</p>
</blockquote></th>
<th>7</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>[ { NTE } ]</p>
</blockquote></td>
<td><blockquote>
<p>Notes and Comments (for Results)</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>} ]</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>{ [ CTI ] }</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Trial Information</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="even">
<td><blockquote>
<p>}</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ DSC ]</p>
</blockquote></td>
<td><blockquote>
<p>Continuation Pointer</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

### Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 34%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ACK Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><strong>HL7 Chapter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>Message Header</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSA</p>
</blockquote></td>
<td><blockquote>
<p>Message Acknowledgment</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[ ERR ]</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

## Static Definition – Segment Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.5.1](#msh-segment), [<u>MSH Segment</u>](#msh-segment), for a listing of all the fields defined for the MSH segment in HL7.

> Refer to Section [4.6.1](#msh-segment-fields-3), [<u>MSH Segment Fields</u>](#msh-segment-fields-3), for a more detailed explanation of the fields used by VistA.

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the definition in Sec[tion 3.5.2](#pid-segment-2), [<u>PID Segment</u>](#pid-segment-2), for a listing of all the fields defined for the PID segment in HL7.

> Refer to Section [3.6.2](#pid-segment-fields-2), [<u>PID Segment Fields</u>](#pid-segment-fields-2), for a more detailed explanation of the PID fields used in the VistA order and report messages.

### OBR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of all the fields defined for the OBR Segment in HL7. Refer to [Section 4.6.3](#obr-segment-fields-1), [<u>OBR Segment Fields</u>](#obr-segment-fields-1), for a more detailed explanation of the fields used in the VistA order message.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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
<p>[1..1]</p>
</blockquote></td>
<td rowspan="4"></td>
<td><blockquote>
<p>00237</p>
</blockquote></td>
<td><blockquote>
<p>Set ID - OBR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00216</p>
</blockquote></td>
<td><blockquote>
<p>Placer Order Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00217</p>
</blockquote></td>
<td><blockquote>
<p>Filler Order Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00238</p>
</blockquote></td>
<td><blockquote>
<p>Universal Service Identifier</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark154" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00239</p>
</blockquote></td>
<td><blockquote>
<p>Priority - OBR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00240</p>
</blockquote></td>
<td><blockquote>
<p>Requested Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00241</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00242</p>
</blockquote></td>
<td><blockquote>
<p>Observation End Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CQ</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00243</p>
</blockquote></td>
<td><blockquote>
<p>Collection Volume</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00244</p>
</blockquote></td>
<td><blockquote>
<p>Collector Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0065</p>
</blockquote></td>
<td><blockquote>
<p>00245</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Action Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00246</p>
</blockquote></td>
<td><blockquote>
<p>Danger Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00247</p>
</blockquote></td>
<td><blockquote>
<p>Relevant Clinical Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00248</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Received Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0070</p>
<p>0163</p>
<p>0369</p>
</blockquote></td>
<td><blockquote>
<p>00249</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00226</p>
</blockquote></td>
<td><blockquote>
<p>Ordering Provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XTN</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..8]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00250</p>
</blockquote></td>
<td><blockquote>
<p>Order Callback Phone Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00251</p>
</blockquote></td>
<td><blockquote>
<p>Placer Field 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00252</p>
</blockquote></td>
<td><blockquote>
<p>Placer Field 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>00253</p>
</blockquote></td>
<td><blockquote>
<p>Filler Field 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>00254</p>
</blockquote></td>
<td><blockquote>
<p>Filler Field 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
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
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00255</p>
</blockquote></td>
<td><blockquote>
<p>Results Rpt/Status Chng - Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00256</p>
</blockquote></td>
<td><blockquote>
<p>Charge to Practice</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0074</p>
</blockquote></td>
<td><blockquote>
<p>00257</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic Serv Sect ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0123</p>
</blockquote></td>
<td><blockquote>
<p>00258</p>
</blockquote></td>
<td><blockquote>
<p>Result Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00259</p>
</blockquote></td>
<td><blockquote>
<p>Parent Result</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>TQ</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00221</p>
</blockquote></td>
<td><blockquote>
<p>Quantity/Timing</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>XCN</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00260</p>
</blockquote></td>
<td><blockquote>
<p>Result Copies To</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00222</p>
</blockquote></td>
<td><blockquote>
<p>Parent</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0124</p>
</blockquote></td>
<td><blockquote>
<p>00262</p>
</blockquote></td>
<td><blockquote>
<p>Transportation Mode</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00263</p>
</blockquote></td>
<td><blockquote>
<p>Reason for Study</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00264</p>
</blockquote></td>
<td><blockquote>
<p>Principal Result Interpreter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..10]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00265</p>
</blockquote></td>
<td><blockquote>
<p>Assistant Result Interpreter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00266</p>
</blockquote></td>
<td><blockquote>
<p>Technician</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00267</p>
</blockquote></td>
<td><blockquote>
<p>Transcriptionist</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>00268</p>
</blockquote></td>
<td><blockquote>
<p>Scheduled Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01028</p>
</blockquote></td>
<td><blockquote>
<p>Number of Sample Containers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01029</p>
</blockquote></td>
<td><blockquote>
<p>Transport Logistics of Collected Sample</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01030</p>
</blockquote></td>
<td><blockquote>
<p>Collector’s Comment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01031</p>
</blockquote></td>
<td><blockquote>
<p>Transport Arrangement Responsibility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0224</a></p>
</blockquote></td>
<td><blockquote>
<p>01032</p>
</blockquote></td>
<td><blockquote>
<p>Transport Arranged</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0225</a></p>
</blockquote></td>
<td><blockquote>
<p>01033</p>
</blockquote></td>
<td><blockquote>
<p>Escort Required</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>01034</p>
</blockquote></td>
<td><blockquote>
<p>Planned Patient Transport Comment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0088</p>
</blockquote></td>
<td><blockquote>
<p>00393</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0340</p>
</blockquote></td>
<td><blockquote>
<p>01316</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Code Modifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0411</a></p>
</blockquote></td>
<td><blockquote>
<p>01474</p>
</blockquote></td>
<td><blockquote>
<p>Placer Supplemental Service Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0">0411</a></p>
</blockquote></td>
<td><blockquote>
<p>01475</p>
</blockquote></td>
<td><blockquote>
<p>Filler Supplemental Service Information</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Refer to Section [4.6.3](#obr-segment-fields-1), [<u>OBR Segment Fields</u>](#obr-segment-fields-1), for a more detailed explanation of the fields used by VistA.

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the definition Sectio[n 3.5.7](#obx-segment-2), [<u>OBX Segment</u>](#obx-segment-2), for a listing of all the fields defined for the OBX segment in HL7.

> <span id="_bookmark155" class="anchor"></span>Refer to Section [4.6.4](#obx-segment-fields-3), [<u>OBX Segment Fields</u>](#obx-segment-fields-3), for a more detailed explanation of the fields used by VistA.

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the definition in Sec[tion 1.5.9](#msa-segment), <u>[MSA Segment](#msa-segment),</u> for a listing of all the fields defined for the MSA segment in HL7.

> Refer to Section [1.6.9](#msa-segment-fields), [<u>MSA Segment Fields</u>](#msa-segment-fields), for a more detailed explanation of the fields used by VistA.

### ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the definition in Sec[tion 1.5.10](#err-segment), [<u>ERR Segment</u>](#err-segment), for a listing of all the fields defined for the ERR segment in HL7.

> Refer to the Sec[tion 1.6.10](#err-segment-fields), [<u>ERR Segment Fields</u>](#err-segment-fields) for a more detailed explanation of the fields used by VistA.

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MSH-1-Field Separator

> This field contains the top-level delimiter for HL7 elements within segments.

#### MSH-2-Encoding Characters

> This field contains the component separator (secondary element delimiter), repetition separator, escape character, and subcomponent separator (tertiary element delimiter).

#### MSH-3-Sending Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA report message, Component 1 of this field shall be populated with the value RA-SERVER-IMG from user-defined Table 0361, *Sending/Receiving Application*. PACS shall return this value in component MSH-5.1 of the acknowledgment message. Components 2 and 3 of MSH-3 are not valued.

#### MSH-4-Sending Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was generated. PACS shall return this value in component MSH-6.1 of the acknowledgment message. Components 2 and 3 of MSH-4 are not valued.

#### MSH-5-Receiving Application

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0361, *Sending/Receiving Application*, with the name of the PACS application. PACS shall return this value in component MSH-3.1 of the acknowledgment message. Components 2 and 3of MSH-5 are not valued.

#### MSH-6-Receiving Facility

> This field is of data type HD, which has 3 components that are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Namespace ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Universal ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0301</p>
</blockquote></td>
<td><blockquote>
<p>Universal ID Type</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In the VistA message, Component 1 of this field shall be populated from user- defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was received. PACS shall return this value in field MSH-4 of the acknowledgment message. Components 2 and 3 of MSH-6 are not valued.

#### MSH-7-Date/Time of Message

> This field contains the date and time that the sending system built the message.

#### MSH-9-Message Type

> This field is of data type CM. Its components are as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark158" class="anchor"></span><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0003</p>
</blockquote></td>
<td><blockquote>
<p>Trigger Event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0354</p>
</blockquote></td>
<td><blockquote>
<p>Message Structure</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

> *MSH-9.1-Message Type*

> This component contains a value from HL7 Table 0076, *Message Type*. For the report message, it will always contain the value ORU.

#### MSH-9.2-Trigger Event

> This component contains a value from HL7 Table 0003, *Event Type*. For the report message, it will always contain the value R01.

#### MSH-10-Message Control ID

> This field will contain a unique identifier for the message.

#### MSH-11-Processing ID

> This field is of type PT, which is defined as follows.

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0103</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>0207</p>
</blockquote></td>
<td><blockquote>
<p>Processing Mode</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components used by VistA are defined as follows.

#### MSH-11.1-Processing ID

> This field contains one of the following values from HL7 Table 0103, *Processing ID.*

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>Production</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Debugging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T</td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-11.2-Processing Mode

> This field contains one of the following values from HL7 Table 0207, *Processing Mode*.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A</td>
<td><blockquote>
<p>Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>R</td>
<td><blockquote>
<p>Restore from archive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>I</td>
<td><blockquote>
<p>Initial load</p>
</blockquote></td>
</tr>
<tr class="even">
<td>T</td>
<td><blockquote>
<p>Current processing, transmitted at intervals (scheduled or on demand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>not present</p>
</blockquote></td>
<td><blockquote>
<p>Not present (the default, meaning <em>current</em> processing)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MSH-12-Version ID

> This field is of type VID, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>0104</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internationalization Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Internal Version ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This field’s first component will always contain the value 2.3.1 from HL7 Table 0104, *Version ID*. Although the VistA message pre-adopts certain Version 2.4 structures, such as the ROL segment, receivers that are unable to recognize Version 2.4 may use Version 2.3.1 syntax rules as prescribed by IHE. It is expected that receivers not now using HL7 Version 2.3.1 will be able to process the V2.3.1 messages according to the HL7 rules for backward compatibility. At such time as IHE is revised to a later version of HL7, receivers will be expected to adapt to the new structures within a stated period of time following the revision.

> Other components of this field will not be used.

#### MSH-17-Country Code

> This field is of type ID. It will always contain the value USA from the ISO 3166 country code table.

### PID Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [3.6.2](#pid-segment-fields-2), [<u>PID Segment Fields</u>](#pid-segment-fields-2), for a complete explanation of the PID fields used in the VistA order and report messages.

### OBR Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBR-1-Set ID

> This is an integer corresponding to the ordinal position of this OBR segment in the message. The first occurrence is labeled 1, the second 2, and so on.

#### OBR-2-Placer Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### OBR-3-Filler Order Number

> This is the medical center site number of the examination, concatenated with the date of the examination, concatenated with the case number of the examination. The elements of this field are separated by hyphens. Example: 688-102104-1693.

#### OBR-4-Universal Service Identifier

> This field is of data type CE (coded entity), which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The components of this field are defined as follows.

> *OBR-4.1-Identifier*

> This component contains the CPT code from the VistA CPT File (#81).

#### OBR-4.2-Text

> This component contains the short name associated with the CPT code in *OBR- 4.1-Identifier*.

#### OBR-4.3-Name of Coding System

> This component always contains the value C4.

#### OBR-4.4-Alternate Identifier

> This component contains the internal entry number of this procedure in the VistA RAD/NUC MED PROCEDURES File (#71).

#### OBR-4.5-Alternate Text

> This component contains the name of the procedure as defined in the RAD/NUC MED PROCEDURES File.

#### OBR-4.6-Name of Alternate Coding System

> This component always contains the value 99RAP.

#### OBR-7-Observation Date/Time

> This field contains the date and time the interpreting physician entered the report.

#### OBR-15-Specimen Source

> This field is of data type CM. Its components are defined as follows.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><strong>Len</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Specimen Source Name or Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>65535</td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Additives</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>65535</td>
<td><blockquote>
<p>TX</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Freetext</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Body Site</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Site Modifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Collection Method Modifier Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only component 5 is populated. When a body site modifier (LEFT or RIGHT) is included in the order, that value will be sent in subcomponent 2 of component 5.

#### OBR-16-Ordering Provider

> This field contains the ID number and name of the provider that requested the order. The data type of this field is XCN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Seq</strong></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Suffix</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Prefix</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>Degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0297</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0363</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0200</p>
</blockquote></td>
<td><blockquote>
<p>Name Type Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Identifier Check Digit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0061</p>
</blockquote></td>
<td><blockquote>
<p>Code Identifying the Check Digit Scheme Employed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0203</p>
</blockquote></td>
<td><blockquote>
<p>Identifier Type Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>0300</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Facility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>Name Representation Code</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note that only the first four components are used. Other components may be ignored.

#### OBR-17-Order Callback Phone Number

> This field contains up to eight telephone numbers that may be used to report order status or results. The data type of this field is XTN, whose components are as follows.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>[NNN] [(999)]999-9999 [X99999] [B99999] [C any text]</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0201</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication use code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>0202</p>
</blockquote></td>
<td><blockquote>
<p>Telecommunication equipment type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Email address</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Country code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Area/city code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Phone number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Extension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Any text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first three components of this field are used. They are populated as follows.

#### OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

> This component contains the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub-elements of the telephone number.

#### OBR-17.2-Telecommunication Use Code

> This component specifies what kind of number is contained in component 1. It is populated with one of the following values from HL7 Table 0201, *Telecommunication Use Code*.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRN</p>
</blockquote></td>
<td><blockquote>
<p>Primary Residence Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WPN</p>
</blockquote></td>
<td><blockquote>
<p>Work Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPN</p>
</blockquote></td>
<td><blockquote>
<p>Beeper Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-17.3-Telecommunication Equipment Type

> This component specifies the kind of device that is reached on the number contained in component 1. It is populated with one of the following values from HL7 Table 202, *Telecommunication Equipment Type*.

<table>
<colgroup>
<col style="width: 37%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FX</p>
</blockquote></td>
<td><blockquote>
<p>Fax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BP</p>
</blockquote></td>
<td><blockquote>
<p>Beeper</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-18-Placer Field 1

> This field contains the inverse date/time of the exam in internal VistA format, concatenated with the VistA exam sub-file internal entry number. Hyphen (-) is used as the delimiter.

#### OBR-19-Placer Field 2

> This field contains the exam date and time (as MMDDYY), concatenated with the case number. Hyphen (-) is used as the delimiter.

#### OBR-21-Filler Field 2

> This field contains the internal entry number of the VistA IMAGING LOCATION File (#79.1), concatenated with the name from the VistA HOSPITAL LOCATION File (#44), concatenated with the internal entry number from the VistA INSTITUTION File (#4), concatenated with the name from the INSTITUTION File. The component separator escape sequence (\S\\) is used as the delimiter.

#### OBR-22-Results Rpt/Status Chng – Date/Time

> This field contains the date/time the report was entered, if it is unverified, or the date/time of verification, if the report is verified.

#### OBR-25-Status

> This field indicates the status of the report. It shall contain one of the following values from HL7 Table 0123, *Result Status*.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>R</td>
<td><blockquote>
<p>Results stored; not yet verified</p>
</blockquote></td>
</tr>
<tr class="even">
<td>F</td>
<td><blockquote>
<p>Final results; results stored and verified. Can only be changed with a corrected result.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>C</td>
<td><blockquote>
<p>Correction to results</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-29-Parent

> This field is valued either to identify an examset or printset, or to indicate that the parent order of the examset or printset has been purged.

> If the order is part of an examset, the field will be valued as follows:

> EXAMSET: *procedure_name*

> If the order is part of a printset, the field will be valued as follows:

> PRINTSET: *procedure_name*

> If the parent order has been purged, the field will be valued as follows:

#### ORIGINAL ORDER PURGED

#### OBR-32-Principal Result Interpreter

> This field identifies the physician or other clinician who interpreted the observation and is responsible for the report content.

> The data type of this field is CM. Its components are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="11"></td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>End Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Location Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only Component 1, Name, is populated. It is of data type CN. The subcomponents of this component are defined and used as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix (<em>e.g.,</em> JR or III)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix (<em>e.g.</em>, DR)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree (<em>e.g.,</em> MD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-33-Assistant Result Interpreter

> This field identifies the clinical observer(s) who assisted with the interpretation of this study. Up to 10 Assistant Result Interpreters may be sent.

> The data type of this field is CM. Its components are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="11"></td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>End Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Location Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark166" class="anchor"></span>Only Component 1, Name, is populated. It is of data type CN. The subcomponents of this component are defined and used as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix (<em>e.g.,</em> JR or III)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix (<em>e.g.</em>, DR)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree (<em>e.g.,</em> MD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### OBR-35-Transcriptionist

> This field identifies the report transcriber.

> The data type of this field is CM. Its components are defined as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="11"></td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>End Date/Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Room</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Bed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Facility</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Location Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Patient Location Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Building</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Floor</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only Component 1, Name, is populated. It is of data type CN. The subcomponents of this component are defined and used as follows.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>0360</p>
</blockquote></td>
<td><blockquote>
<p>ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Family Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Given Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Middle Initial or Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Suffix (<em>e.g.,</em> JR or III)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Prefix (<em>e.g.</em>, DR)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>[0..1]</p>
</blockquote></td>
<td><blockquote>
<p>Degree (<em>e.g.,</em> MD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>IS</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Source Table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Assigning Authority</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Only the first four subcomponents are populated. Other subcomponents are not used.

### OBX Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### OBX-2-Value Type

> This field contains the data type of the information carried in *OBX-5-Observation Value.* It is populated with one of the following values from HL7 Table 0125, *Value Type*.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Coded Element</p>
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

#### OBX-3-Observation Identifier

> This field classifies the kind of information carried in *OBX-5-Observation Value.*

> Its data type is CE, whose definition is as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Components 1, *Identifier*, and 2, *Text*, are populated as follows.

> Component 3 is always valued L. OBX-5-Observation Value

> This field contains the actual value whose data type is given in *OBX-2-Value Type* and whose classification is given in *OBX-3-Observation Identifier*. Its formatting follows the rules for the data type given in OBX-2.

> In OBX segments for which OBX-3.1 contains a value of R, this field contains report text.

#### OBX-6-Units

> For quantitative measurements, this field contains the units of the observation. For observations other than quantitative measurements, this field is not populated.

> The data type of this field is CE, which is defined as follows.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Seq</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Len</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cardinality</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td rowspan="6"></td>
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>[1..1]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Coding System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>[0..0]</p>
</blockquote></td>
<td><blockquote>
<p>Name of Alternate Coding System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Component 3 is always valued ISO+, indicating the use of units of measure from ISO Standard 2955-1983.

#### OBX-11-Observation Result Status

> This field is of data type ID. In the report message, it is populated with the following values from HL7 Table 0085, *Observation Result Status Codes Interpretation.*

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>Final results; Can only be changed with a corrected result.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>C</td>
<td><blockquote>
<p>Record coming over is a correction and thus replaces a final result</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>R</td>
<td><blockquote>
<p>Results entered – not verified</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Fields Used in the MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.9](#msa-segment-fields), [<u>MSA Segment Fields</u>](#msa-segment-fields), for a more detailed explanation of the MSA fields used in VistA messaging.

### Fields Used in the ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Section [1.6.10](#err-segment-fields), [<u>ERR Segment Fields</u>](#err-segment-fields), for a more detailed explanation of the ERR fields used in VistA messaging.