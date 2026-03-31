---
title: SR*3*178 Surgery Health Level 7 Interface Specifications
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: Surgery Health Level 7 s
app_code: SR
app_name: Surgery
section: CLI
app_status: active
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*178
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "3.5.17 Segment: ZIG - Appointment Information - General Resource [48](#_Toc93819559)"
audience: 
keywords: 
  - span
  - class
  - anchor
  - segment
  - message
  - surgery
  - null
  - code
  - table
  - vista
page_count: 0
word_count: 8707
section_count: 0
table_count: 144
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: June 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr3p178sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr3p178sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=103"
---

![](sr-3-178-surgery-health-level-7-interface-specifications/001.png)

SURGERY

Health Level 7  
Interface specifications

June 1998

V*IST*A Health Systems Design & Development

Table of Contents

1\. PURPOSE [1](#_Toc93819334)

2\. OVERVIEW [1](#_Toc93819336)

2.1 Statement of Intent [1](#_Toc93819337)

2.2 Scope [1](#_Toc93819339)

3\. GENERAL SPECIFICATIONS [1](#_Toc93819341)

3.1 Communication Protocol [1](#_Toc93819342)

3.2 Application Processing Rules [2](#_Toc93819343)

3.3 Messages [2](#_Toc93819345)

3.4 Segments [2](#_Toc93819348)

3.5 Fields [3](#_Toc93819352)

3.5.1 Segment: AL1 - Patient Allergy Information [5](#_Toc93819360)

3.5.1.0 AL1 field definitions [5](#_Toc93819362)

3.5.1.1 SET ID - ALLERGY (SI) [5](#_Toc93819363)

3.5.1.2 ALLERGY TYPE (ID) [5](#_Toc93819364)

3.5.1.3 ALLERGY CODE/MNEMONIC/DESCRIPTION (CE) [5](#_Toc93819365)

3.5.2 Segment: DG1 - Diagnosis [6](#_Toc93819366)

3.5.2.0 DG1 field definitions [6](#_Toc93819367)

3.5.2.1 SET ID - DIAGNOSIS (SI) [6](#_Toc93819368)

3.5.2.2 DIAGNOSIS CODING METHOD (ID) [6](#_Toc93819369)

3.5.2.3 DIAGNOSIS CODE (ID) [6](#_Toc93819370)

3.5.2.4 DIAGNOSIS DESCRIPTION (ST) [6](#_Toc93819372)

3.5.2.6 DIAGNOSIS/DRG TYPE (ID) [7](#_Toc93819374)

3.5.4 Segment: MFA - Master File Acknowledgement [9](#_Toc94060289)

3.5.4.0 MFA field definitions [9](#_Toc94060290)

3.5.4.1 RECORD-LEVEL EVENT CODE (ID) [9](#_Toc94060291)

3.5.4.4 ERROR RETURN CODE AND/OR TEXT (CE) [9](#_Toc94060292)

3.5.4.5 PRIMARY KEY VALUE (CE) [9](#_Toc94060293)

3.5.5 Segment: MFE - Master File Entry [10](#_Toc93819376)

3.5.5.0 MFE field definitions [10](#_Toc93985438)

3.5.5.1 RECORD-LEVEL EVENT CODE (ID) [10](#_Toc93985439)

3.5.5.2 MFN - CONTROL ID (ST) [10](#_Toc93819379)

3.5.5.3 EFFECTIVE DATE/TIME (TS) [11](#_Toc93819381)

3.5.5.4 PRIMARY KEY VALUE (CE) [11](#_Toc93819384)

3.5.6 Segment: MFI - Master File Identification [12](#_Toc93819386)

3.5.6.0 MFI field definitions [12](#_Toc93985444)

3.5.6.1 MASTER FILE IDENTIFIER (CE) [12](#_Toc93985445)

3.5.6.3 FILE-LEVEL EVENT CODE (ID) [13](#_Toc93985446)

3.5.6.6 RESPONSE LEVEL CODE (ID) [13](#_Toc93819389)

3.5.7 Segment: MSA - Message Acknowledgment [14](#_Toc93819391)

3.5.7.0 MSA field definitions [14](#_Toc93985449)

3.5.7.1 ACKNOWLEDGMENT CODE (ID) [14](#_Toc93985450)

3.5.7.2 MESSAGE CONTROL ID (ST) [14](#_Toc93819393)

3.5.7.3 TEXT MESSAGE (ST) [14](#_Toc93819395)

3.5.8 Segment: MSH - Message Header [15](#_Toc93819396)

3.5.8.0 MSH field definitions [15](#_Toc93900074)

3.5.8.1 FIELD SEPARATOR (ST) [15](#_Toc93900075)

3.5.8.2 ENCODING CHARACTERS (ST) [15](#_Toc93819399)

3.5.8.3 SENDING APPLICATION (ST) [15](#_Toc93819401)

3.5.8.4 SENDING FACILITY (ST) [16](#_Toc93819403)

3.5.8.5 RECEIVING APPLICATION (ST) [16](#_Toc93819406)

3.5.8.6 RECEIVING FACILITY (ST) [16](#_Toc93819409)

3.5.8.7 DATE/TIME OF MESSAGE (TS) [16](#_Toc93819412)

3.5.8.8 SECURITY (ST) [16](#_Toc93819414)

3.5.8.9 MESSAGE TYPE (CM) [16](#_Toc93819416)

3.5.8.10 MESSAGE CONTROL ID (ST) [17](#_Toc93819417)

3.5.8.11 PROCESSING ID (ID) [17](#_Toc93819418)

3.5.8.12 VERSION ID (ID) [17](#_Toc93819419)

3.5.8.15 ACCEPT ACKNOWLEDGMENT TYPE (ID) [17](#_Toc93819421)

3.5.8.16 APPLICATION ACKNOWLEDGMENT TYPE (ID) [18](#_Toc93819422)

3.5.9 Segment: NTE - Anesthesiologist Notes and Comments [19](#_Toc94060326)

3.5.9.0 NTE field definitions [19](#_Toc93900089)

3.5.9.1 SET ID - NOTES AND COMMENTS (SI) [19](#_Toc93900090)

3.5.9.2 SOURCE OF COMMENT (ID) [19](#_Toc93900091)

3.5.9.3 COMMENT (FT) [19](#_Toc93819424)

3.5.10 Segment: OBR - Observation Request [20](#_Toc93819426)

3.5.10.0 OBR field definitions [20](#_Toc93900094)

3.5.10.1 SET ID - OBSERVATION REQUEST (SI) [20](#_Toc93900095)

3.5.10.3 FILLER ORDER NUMBER (CM) [20](#_Toc93819430)

3.5.10.4 UNIVERSAL SERVICE ID (CE) [21](#_Toc93819432)

3.5.10.7 OBSERVATION DATE/TIME (TS) [22](#_Toc93819439)

3.5.10.8 OBSERVATION END DATE/TIME (TS) [22](#_Toc93819442)

3.5.10.16 ORDERING PROVIDER (CN) [22](#_Toc93819445)

3.5.11 Segment: OBX - Observation [23](#_Toc93819448)

3.5.11.0 OBX field definitions [23](#_Toc93900101)

3.5.11.1 SET ID - OBSERVATION SIMPLE (SI) [23](#_Toc93900102)

3.5.11.2 VALUE TYPE (ID) [23](#_Toc93819449)

3.5.11.3 OBSERVATION IDENTIFIER (CE) [24](#_Toc93819450)

3.5.11.5 OBSERVATION VALUE (ST) [29](#_Toc93819468)

3.5.11.6 UNITS (CE) [33](#_Toc93819474)

3.5.11.11 OBSERV RESULT STATUS (ID) [34](#_Toc93985487)

3.5.11.14 DATE/TIME OF THE OBSERVATION (TS) [34](#_Toc93819479)

3.5.11.16 RESPONSIBLE OBSERVER (CN) [34](#_Toc93819481)

3.5.12 Segment: PID – Patient Identification [35](#_Toc94060349)

3.5.12.0 PID field definitions [35](#_Toc93985491)

3.5.12.1 SET ID - PATIENT ID (SI) [35](#_Toc93985492)

3.5.12.3 PATIENT ID (INTERNAL ID) (CM) [35](#_Toc93819485)

3.5.12.4 ALTERNATE PATIENT ID (ST) [36](#_Toc93819487)

3.5.12.5 PATIENT NAME (PN) [36](#_Toc93985495)

3.5.12.6 MOTHER’S MAIDEN NAME (ST) [36](#_Toc93985496)

3.5.12.7 DATE OF BIRTH (DT) [36](#_Toc93985497)

3.5.12.8 SEX (ID) [36](#_Toc93985498)

3.5.12.10 RACE (ID) [36](#_Toc93819490)

3.5.12.11 PATIENT ADDRESS (AD) [37](#_Toc93985500)

3.5.12.13 PHONE NUMBER - HOME (TN) [37](#_Toc93985501)

3.5.12.16 MARITAL STATUS (ID) [37](#_Toc93985502)

3.5.12.17 RELIGION (ID) [37](#_Toc93819492)

3.5.12.19 SSN NUMBER - PATIENT (ST) [38](#_Toc93985504)

3.5.13 Segment: STF - Staff Identification [39](#_Toc93819495)

3.5.13.0 STF field definition [39](#_Toc93985506)

3.5.13.1 STF - PRIMARY KEY VALUE (CE) [39](#_Toc93985507)

3.5.13.3 STAFF NAME (PN) [39](#_Toc93819498)

3.5.13.13 INACTIVATION DATE (CM) [39](#_Toc93819500)

3.5.14 Segment: QRD - Query Definition [40](#_Toc93985510)

3.5.14.0 QRD field definitions [40](#_Toc93985511)

3.5.14.1 QUERY DATE/TIME (TS) [40](#_Toc93985512)

3.5.14.2 QUERY FORMAT CODE (ID) [40](#_Toc93819501)

3.5.14.3 QUERY PRIORITY (ID) [41](#_Toc93819505)

3.5.14.4 QUERY ID (ST) [41](#_Toc93819509)

3.5.14.7 QUANTITY LIMITED REQUEST (CQ) [41](#_Toc93819511)

3.5.14.8 WHO SUBJECT FILTER (ST) [41](#_Toc93819514)

3.5.14.9 WHAT SUBJECT FILTER (ID) [42](#_Toc93819516)

3.5.14.10 WHAT DEPARTMENT DATA CODE (ST) [42](#_Toc93819519)

3.5.15 Segment: QRF - Query Filter [43](#_Toc93819521)

3.5.15.0 QRF field definitions [43](#_Toc93985521)

3.5.15.1 WHERE SUBJECT FILTER (ST) [43](#_Toc93985522)

3.5.15.2 WHEN DATA START DATE/TIME (TS) [43](#_Toc93985523)

3.5.15.3 WHEN DATA END DATE/TIME (TS) [43](#_Toc93819525)

3.5.16 Segment: ZCH - Schedule Appointment Information [44](#_Toc93819527)

3.5.16.0 ZCH field definitions [44](#_Toc93985526)

3.5.16.1 PLACER SCHEDULE REQUEST ID (CM) [44](#_Toc93985527)

3.5.16.2 FILLER SCHEDULE REQUEST ID (CM) [44](#_Toc93819531)

3.5.16.3 PLACER GROUP NUMBER (CM) [45](#_Toc93971332)

3.5.16.4 EVENT REASON (CE) [45](#_Toc93819536)

3.5.16.5 APPOINTMENT REASON (CE) [46](#_Toc93819544)

3.5.16.6 APPOINTMENT DURATION (CQ) [46](#_Toc93819547)

3.5.16.7 APPOINTMENT TIMING QUANTITY (TQ) [46](#_Toc93819550)

3.5.16.12 FILLER CONTACT PERSON (CN) [47](#_Toc93819554)

3.5.16.17 PARENT FILLER SCHEDULE REQUEST (CM) [47](#_Toc93819557)

3.5.17 Segment: ZIG - Appointment Information - General Resource [48](#_Toc93819559)

3.5.17.0 ZIG field definitions [48](#_Toc93985537)

3.5.17.1 RESOURCE ID (CE) [48](#_Toc93985538)

3.5.17.2 RESOURCE TYPE (CE) [48](#_Toc93819562)

3.5.17.3 START DATE/TIME OFFSET (CQ) [49](#_Toc93819563)

3.5.17.4 DURATION (CQ) [49](#_Toc93819566)

3.5.17.6 FILLER STATUS CODE (ID) [49](#_Toc93819568)

3.5.18 Segment: ZIL - Appointment Information -Location Resource [50](#_Toc93971344)

3.5.18.0 ZIL field definitions [50](#_Toc93971345)

3.5.18.1 LOCATION RESOURCE ID (CM) [50](#_Toc93971346)

3.5.18.2 LOCATION TYPE (CE) [50](#_Toc93819575)

3.5.18.4 DURATION (CQ) [51](#_Toc93819581)

3.5.18.6 FILLER STATUS CODE (ID) [51](#_Toc93819584)

3.5.19 Segment: ZIP - Appointment Information -Personnel Resource [52](#_Toc93819587)

3.5.19.0 ZIP field definitions [52](#_Toc94060409)

3.5.19.1 RESOURCE ID (CN) [52](#_Toc94060410)

3.5.19.2 RESOURCE ROLE (CE) [52](#_Toc93819591)

3.5.19.6 FILLER STATUS CODE (ID) [53](#_Toc93819593)

3.5.20 Segment: ZIS - Appointment Information - Service [54](#_Toc93819596)

3.5.20.0 ZIS field definitions [54](#_Toc93971356)

3.5.20.1 UNIVERSAL SERVICE IDENTIFIER (CE) [54](#_Toc93819598)

3.5.20.5 FILLER STATUS CODE (ID) [54](#_Toc93819601)

3.5.21 Segment: ZI9 - ICD9 Identification [55](#_Toc93819604)

3.5.21.0 ZI9 - field definition [55](#_Toc94060418)

3.5.21.1 ZI9 - PRIMARY KEY VALUE (CE) [55](#_Toc94060419)

3.5.21.2 ICD9 CODE (ST) [55](#_Toc93819607)

3.5.21.3 DIAGNOSIS (ST) [55](#_Toc93819609)

3.5.21.4 ACTIVE/INACTIVE (ID) [55](#_Toc93819610)

3.5.22 Segment: ZMN - Monitor Identification [56](#_Toc94060423)

3.5.22.0 ZMN - field definition [56](#_Toc94060424)

3.5.22.1 ZMN - PRIMARY KEY VALUE (CE) [56](#_Toc94060425)

3.5.22.2 ACTIVE/INACTIVE (ID) [56](#_Toc93819614)

3.5.23.0 ZRF - field definitions [57](#_Toc94060427)

3.5.23.1 ZRF - PRIMARY KEY VALUE (CE) [57](#_Toc93819617)

3.5.23.2 ACTIVE/INACTIVE (ID) [57](#_Toc93819618)

3.5.24 Segment: ZRX - Medication Identification [58](#_Toc94060430)

3.5.24.0 ZRF - field definitions [58](#_Toc94060431)

3.5.24.1 ZRX - PRIMARY KEY VALUE (CE) [58](#_Toc93819621)

3.5.24.2 INACTIVE DATE (CM) [58](#_Toc93819623)

4\. TRANSACTION SPECIFICATIONS [59](#_Toc93819625)

4.1 General [59](#_Toc93819626)

4.2 Specific Transactions [59](#_Toc93819633)

A. Surgery Trigger Events [59](#_Toc93819634)
B. Message Acknowledgment [63](#_Toc93819637)
C. Query for Pre-operative Surgical Data [63](#_Toc93819640)
D. Respond with Requested Query Information [64](#_Toc93819646)
E. Message Acknowledgment [66](#_Toc93819650)
F. Unsolicited Update at Procedure Conclusion [66](#_Toc93819652)
G. Message Acknowledgment [68](#_Toc93819653)
H. Synchronize Reference Files [68](#_Toc93819655)
I. Message Acknowledgment of Master File Update [69](#_Toc93819660)

APPENDIX A: DATA SOURCES [71](#_Toc94060446)

Surgery

> V*IST*A

Birmingham CIO Field Office

HEALTH LEVEL 7

Interface Specifications

Exchange of Surgical Health Care Information

<span id="_Toc93819334" class="anchor"></span>1. PURPOSE

This document specifies an interface to the Veterans Health Information Systems and Technology Architecture (V*IST*A) Surgery package based upon the HL7 protocol. It is intended that this interface form the basis for the exchange of health care information between the V*IST*A Surgery package and any automated anesthesia information system (AAIS) or ancillary system.

<span id="_Toc93819336" class="anchor"></span>2. OVERVIEW

<span id="_Toc93819337" class="anchor"></span>2.1 Statement of Intent

The interface described by this document is a generic interface to the HL7 protocol for use by the V*IST*A Surgery package in communicating with any AAIS or ancillary system for the purpose of exchanging health care information. The interface strictly adheres to the HL7 protocol and avoids using Z type extensions to the protocol whenever possible.

<span id="_Toc93819339" class="anchor"></span>2.2 Scope

This document describes messages that are exchanged between the V*IST*A Surgery package and any AAIS or ancillary system for the purpose of exchanging information concerning surgical cases.

<span id="_Toc93819341" class="anchor"></span>3. GENERAL SPECIFICATIONS

<span id="_Toc93819342" class="anchor"></span>3.1 Communication Protocol

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that are used for interfacing with the V*IST*A Surgery package are based on the HL7 Hybrid Lower Level Protocol, which is described in the HL7 Implementation Guide.

<span id="_Toc93819343" class="anchor"></span>3.2 Application Processing Rules

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol is not repeated here; therefore, anyone wishing to interface with the V*IST*A Surgery package should become familiar with the HL7 protocol V. 2.2.

<span id="_Toc93819345" class="anchor"></span>3.3 Messages

Refer to section 4, Transaction Specifications, for details and examples of all messages used to interface with V*IST*A Surgery. The following HL7 messages are used to support the exchange of Surgery information. The Z-messages are based upon an early balloted version of the HL7 Scheduling chapter (which has now been accepted and released in V. 2.3 of the HL7 protocol).

ACK General Acknowledgment MFK Master File Application Acknowledgement MFN Master File Notification ORU Observational Results Unsolicited QRY Query Message ZIU Schedule Information Unsolicited ZSQ Scheduled Activity Transaction

<span id="_Toc93819348" class="anchor"></span>3.4 Segments

Refer to section 4, Transaction Specifications, for details and examples of all segments used to interface with V*IST*A Surgery. The following HL7 segments are used to support the exchange of Surgery information. The Z-segments (ZCH, ZIG, ZIL, ZIP, and ZIS) are based upon an early balloted version of the HL7 Scheduling chapter (which has now been accepted and released in V. 2.3 of the HL7 protocol). The other Z-segments (ZI9, ZMN, ZRF, and ZRX) are based upon the suggestion given in the Master Files Chapter and closely resemble the Staff Identification segment.

AL1 Allergy Information  
DG1 Diagnosis  
ERR Error  
MFA Master File Acknowledgement  
MFE Master File Entry  
MFI Master File Identification  
MSA Message Acknowledgment  
MSH Message Header  
NTE Notes and Comment  
OBR Observation Request  
OBX Observation

PID Patient Identification  
STF Staff Identification  
QRD Query Definition  
QRF Query Filter  
SCH Schedule Appointment Information  
AIG Appointment Information -General Resource  
AIL Appointment Information - Location Resource  
AIP Appointment Information - Personnel Resource  
AIS Appointment Information - Service  
ZI9 ICD9 Identification  
ZMN Monitor Identification  
ZRF Replacement Fluid Identification  
ZRX Medication Identification

<span id="_Toc93819352" class="anchor"></span>3.5 Fields

The segment definition tables list and describe the data fields in the segment and characteristics of their usage. The following information is specified about each data field.

Sequence Number (SEQ): The ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table.

Length (LEN): The maximum number of characters that one occurrence of the data field may occupy.

Data Type (DT): Restrictions on the contents of the data field as defined by the HL7 Standard.

Optionality (R/O/C): Whether the data field is required, optional, or conditional in a segment. The designations are: R - required; O (null) - optional; and C ­conditional on the trigger event.

Repetition (RP/#): Whether the field may repeat. The designations are: N (null)

-for no repetition allowed; Y - the field may repeat an indefinite or site determined number of times; and (integer) - the field may repeat up to the number of times specified in the integer.

Table (TBL#): A table of values which may be defined by HL7 or negotiated between the V*IST*A Surgery application and the vendor system.

Element Name: Globally unique descriptive name for the field.

The HL7 segment fields shown on the following page, are used to support the exchange of Surgery data for each of the segments listed in paragraph 3.4. Tables referenced in the segments can be found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for those fields which are utilized. The field definitions can include specific information (e.g., expected format) for transmission.

<span id="_Toc93819360" class="anchor"></span>3.5.1 Segment: AL1 - Patient Allergy Information

The AL1 segment contains patient allergy information of various types. Each AL1 segment describes a single patient allergy.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

1 4 SI R SET ID - ALLERGY

2 2 ID 127 ALLERGY TYPE

3 60 CE R ALLERGY CODE/MNEMONIC/DESCRIPTION

<span id="_Toc93819362" class="anchor"></span>3.5.1.0 AL1 field definitions

<span id="_Toc93819363" class="anchor"></span>3.5.1.1 SET ID - ALLERGY (SI)

SET ID is a number that uniquely identifies the individual transaction for adding, deleting or updating an allergy description in the patient’s record. The field is used to identify the segment repetitions.

<span id="_Toc93819364" class="anchor"></span>3.5.1.2 ALLERGY TYPE (ID)

ALLERGY TYPE indicates a general allergy category (drug, food, pollen, etc.). Only the following values are expected/accepted.

HL7 (User-defined) Table 127 ALLERGY TYPE

|       |                                |
|-------|--------------------------------|
| Value | Description                    |
| DA    | Drug Allergy                   |
| FA    | Food Allergy                   |
| MA    | Miscellaneous Allergy          |
| MC    | Miscellaneous Contraindication |
| DF    | Drug/Food Allergy              |
| DO    | Drug/Other Allergy             |
| FO    | Food/Other Allergy             |
| AT    | All Types                      |

<span id="_Toc93819365" class="anchor"></span>

3.5.1.3 ALLERGY CODE/MNEMONIC/DESCRIPTION (CE)

> ALLERGY CODE/MNEMONIC/DESCRIPTION is a coded element made up of the following:

> \<identifier\> \<text\> \<name of coding system\>

> For each allergy transmitted, only the text component is populated. The text component is the free text allergy name. All other field components are left blank.

<span id="_Toc93819366" class="anchor"></span>3.5.2 Segment: DG1 - Diagnosis

The DG1 segment contains patient diagnosis information of various types.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                         |
|-----|-----|-----|-----|-----|-------------------------|
| 1   | 4   | SI  | R   |     | SET ID - DIAGNOSIS      |
| 2   | 2   | ID  | R   | 53  | DIAGNOSIS CODING METHOD |
| 3   | 8   | ID  |     | 51  | DIAGNOSIS CODE          |
| 4   | 40  | ST  |     |     | DIAGNOSIS DESCRIPTION   |
| 6   | 2   | ID  | R   | 52  | DIAGNOSIS/DRG TYPE      |

<span id="_Toc93819367" class="anchor"></span>3.5.2.0 DG1 field definitions

<span id="_Toc93819368" class="anchor"></span>3.5.2.1 SET ID - DIAGNOSIS (SI)

> SET ID is a number that uniquely identifies the individual transaction for adding, deleting or updating the diagnosis in the patient’s record.

<span id="_Toc93819369" class="anchor"></span>3.5.2.2 DIAGNOSIS CODING METHOD (ID)

ICD9 is the recommended coding method. Only the following value is expected/accepted.

HL7 (user-defined) Table 53 DIAGNOSIS CODING METHOD

|       |             |
|-------|-------------|
| Value | Description |
| 19    | ICD9        |

<span id="_Toc93819370" class="anchor"></span>3.5.2.3 DIAGNOSIS CODE (ID)

> Diagnosis code assigned to this diagnosis. This field accepts any ICD9 (International Classification of Diseases, 9th Revision) diagnosis code.

When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field contains either the PRIN DIAGNOSIS CODE or the OTHER PREOP DIAG CODE. The field is the actual ICD9 code number.

<span id="_Toc93819372" class="anchor"></span>3.5.2.4 DIAGNOSIS DESCRIPTION (ST)

This field contains a description that best describes the diagnosis.

When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field contains the description from the DIAGNOSIS field (#3) in the ICD DIAGNOSIS file (#80).

<span id="_Toc93819374" class="anchor"></span>3.5.2.6 DIAGNOSIS/DRG TYPE (ID)

> This code identifies the type of diagnosis being sent. Only the following values are expected/accepted.

HL7 (user-defined) Table 52 DIAGNOSIS TYPE

|       |                          |
|-------|--------------------------|
| Value | Description              |
| P     | Principal Diagnosis      |
| PR    | Pre-Operative Diagnosis  |
| PO    | Post-Operative Diagnosis |

  
3.5.3 Segment: ERR - Error

The ERR segment is used to add error comments to acknowledgment messages. SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

1 80 CM R Y 60 ERROR CODE AND LOCATION

3.5.3.0 ERR field definitions

3.5.3.1 ERROR CODE AND LOCATION (CM)

> ERROR CODE AND LOCATION is a composite element made up of the following:  
> \<segment ID\> \<sequence\> \<field position\> \<code identifying error\>  
> This field identifies an erroneous segment in another message. The second component is an index if there are more than one segment of type \<segment ID\>. The fourth component references a user-defined error table. This segment is sent by the V*IST*A Surgery system only if there is an application error.

<span id="_Toc94060289" class="anchor"></span>3.5.4 Segment: MFA - Master File Acknowledgement

The MFA segment is used to acknowledge the change to the identified record.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |     |                               |
|-----|-----|-----|-----|-----|-----|-------------------------------|
| 1   | 3   | ID  | R   |     | 180 | RECORD-LEVEL EVENT CODE       |
| 4   | 60  | CE  | R   |     | 181 | ERROR RETURN CODE AND/OR TEXT |
| 5   | 60  | CE  | R   | Y   |     | PRIMARY KEY VALUE             |

<span id="_Toc94060290" class="anchor"></span>3.5.4.0 MFA field definitions

<span id="_Toc94060291" class="anchor"></span>3.5.4.1 RECORD-LEVEL EVENT CODE (ID)

> This field is used to define record-level events for the master file record identified by the MFI segment and the primary key field in this segment.

HL7 Table 180 RECORD-LEVEL EVENT CODE

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td><p>MAD</p>
<p>MDL</p>
<p>MUP MDC</p>
<p>MAC</p></td>
<td><p>Add record to master file</p>
<p>Delete record from master file</p>
<p>Update record for master file</p>
<p>Deactivate: discontinue using record in master file, but do not delete</p>
<p>Reactivate deactivated record</p></td>
</tr>
</tbody>
</table>

<span id="_Toc94060292" class="anchor"></span>3.5.4.4 ERROR RETURN CODE AND/OR TEXT (CE)

> This field reports on the status of the requested update. This is a site defined-table, specific to each master file being updated via this transaction.

> All such tables will have at least the following two return values:

HL7 (user-defined) Table 181 MFN RECORD-LEVEL ERROR CODE

|       |                                                               |
|-------|---------------------------------------------------------------|
| Value | Description                                                   |
| S     | Successful posting of the record defined by the MFE segment   |
| U     | Unsuccessful posting of the record defined by the MFE segment |

<span id="_Toc94060293" class="anchor"></span>3.5.4.5 PRIMARY KEY VALUE (CE)

> This field uniquely identifies the record of the master file (identified in the MFI segment) to be changed (as defined by the record-level event code).

<span id="_Toc93819376" class="anchor"></span>3.5.5 Segment: MFE - Master File Entry

The MFE segment identifies the record and the action that is to be taken upon that record.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                             |
|-----|-----|-----|-----|-----|-----------------------------|
| 1   | 3   | ID  | R   |     | 180 RECORD-LEVEL EVENT CODE |
| 2   | 20  | ST  | C   |     | MFN CONTROL ID              |
| 3   | 26  | TS  |     |     | EFFECTIVE DATE/TIME         |
| 4   | 60  | CE  | R   | Y   | PRIMARY KEY VALUE           |

<span id="_Toc93985438" class="anchor"></span>3.5.5.0 MFE field definitions

<span id="_Toc93985439" class="anchor"></span>3.5.5.1 RECORD-LEVEL EVENT CODE (ID)

> This field is used to define record-level events for the master file record identified by the MFI segment and the primary key field in this segment.

HL7 Table 180 RECORD-LEVEL EVENT CODE

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td><p>MAD</p>
<p>MDL</p>
<p>MUP MDC</p>
<p>MAC</p></td>
<td><p>Add record to master file</p>
<p>Delete record from master file</p>
<p>Update record for master file</p>
<p>Deactivate: discontinue using record in master file, but do not delete</p>
<p>Reactivate deactivated record</p></td>
</tr>
</tbody>
</table>

When V*IST*A sends an MFI-3 (MASTER FILE IDENTIFIER CODE) of REP this field will contain the value of MAD. This means that the ancillary system should replace the current file and add all of the new entries. When V*IST*A sends an MFI-3 of UPD this field will contain one of four values (MAD, MDL, MDC, or MAC).

<span id="_Toc93819379" class="anchor"></span>3.5.5.2 MFN - CONTROL ID (ST)

> A number or other identifier that uniquely identifies this change to this record from the point of view of the originating system.

> When V*IST*A sends this field it will contain the IEN for records in files or a sequential number starting at one for the V*IST*A field set of codes.

<span id="_Toc93819381" class="anchor"></span>3.5.5.3 EFFECTIVE DATE/TIME (TS)

> The date/time the originating system expects the event to have been completed on the receiving system.

> When V*IST*A sends this field it will contain the date/time that the new information was compiled and sent to the ancillary system.

<span id="_Toc93819384" class="anchor"></span>3.5.5.4 PRIMARY KEY VALUE (CE)

> This field uniquely identifies the record of the master file (identified in the MFI segment) to be changed (as defined by the record-level event code).

> When V*IST*A sends this field it will contain the text name of the field/file record in this form.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 31%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Identifier</td>
<td>Text</td>
<td>Coding System</td>
</tr>
<tr class="even">
<td><p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>CPT-4 code</p>
<p>null</p>
<p>null</p>
<p>ICD9 code</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>SSN#</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p></td>
<td><p>Administration method</p>
<p>ASA class</p>
<p>Attending code</p>
<p>Anesthesia approach</p>
<p>Anesthesia route</p>
<p>Baricity</p>
<p>Case schedule type</p>
<p>CPT-4 short description</p>
<p>Epidural method</p>
<p>Extubated in</p>
<p>ICD9 name</p>
<p>Hospital Location</p>
<p>Laryngoscope type</p>
<p>Medication name</p>
<p>Medication route</p>
<p>Monitor name</p>
<p>Patient status</p>
<p>Person’s name</p>
<p>Principal anesthesia technique (Y/N)</p>
<p>Replacement fluid</p>
<p>Site tourniquet applied</p>
<p>Tube type</p></td>
<td><p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>C4</p>
<p>null</p>
<p>null</p>
<p>I9</p>
<p>99VA44</p>
<p>null</p>
<p>99VA50</p>
<p>null</p>
<p>99VA133.4</p>
<p>null</p>
<p>99VA200</p>
<p>null</p>
<p>99VA133.7</p>
<p>null</p>
<p>null</p></td>
</tr>
</tbody>
</table>

<span id="_Toc93819386" class="anchor"></span>3.5.6 Segment: MFI - Master File Identification

The MFI segment identifies the reference file and the action that is to be taken upon that file.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                            |
|-----|-----|-----|-----|-----|----------------------------|
| 1   | 60  | CE  | R   | N   | 175 MASTER FILE IDENTIFIER |
| 3   | 3   | ID  | R   |     | 178 FILE-LEVEL EVENT CODE  |
| 6   | 2   | ID  | R   |     | 179 RESPONSE LEVEL CODE    |

<span id="_Toc93985444" class="anchor"></span>3.5.6.0 MFI field definitions

<span id="_Toc93985445" class="anchor"></span>3.5.6.1 MASTER FILE IDENTIFIER (CE)

> MASTER FILE IDENTIFIER identifies standard and Z-type HL7 master files.

HL7 Table 175 MASTER FILE IDENTIFIER CODE

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 54%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Identifier</td>
<td>Text</td>
<td>Coding System</td>
</tr>
<tr class="even">
<td><p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>null</p>
<p>ZI9</p>
<p>null</p>
<p>ZRX</p>
<p>null</p>
<p>ZMN</p>
<p>null</p>
<p>STF</p>
<p>null</p>
<p>ZRF</p>
<p>null</p>
<p>null</p></td>
<td><p>ADMINISTRATION METHOD</p>
<p>ASA CLASS</p>
<p>ATTENDING CODE</p>
<p>ANESTHESIA APPROACH</p>
<p>ANESTHESIA ROUTE</p>
<p>BARICITY</p>
<p>CASE SCHEDULE TYPE</p>
<p>EPIDURAL METHOD</p>
<p>EXTUBATED IN</p>
<p>HOSPITAL LOCATION</p>
<p>ICD9</p>
<p>LARYNGOSCOPE TYPE</p>
<p>MEDICATION</p>
<p>MEDICATION ROUTE</p>
<p>MONITOR</p>
<p>PATIENT STATUS</p>
<p>PERSONNEL</p>
<p>PRINCIPAL ANES TECHNIQUE (Y/N)</p>
<p>REPLACEMENT FLUID</p>
<p>SITE TOURNIQUET APPLIED</p>
<p>TUBE TYPE</p></td>
<td><p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>L</p>
<p>99VA44</p>
<p>I9</p>
<p>L</p>
<p>99VA50</p>
<p>L</p>
<p>99VA133.4</p>
<p>L</p>
<p>99VA200</p>
<p>L</p>
<p>99VA133.7</p>
<p>L</p>
<p>L</p></td>
</tr>
</tbody>
</table>

\*\*Note: See the CPT CODE Master File Update Specification Document for the details on interfacing the CPT4 codes.

<span id="_Toc93985446" class="anchor"></span>3.5.6.3 FILE-LEVEL EVENT CODE (ID)

> FILE-LEVEL EVENT CODE defines file-level event code.

> HL7 Table 175 MASTER FILE IDENTIFIER CODE

|       |                                                      |
|-------|------------------------------------------------------|
| Value | Description                                          |
| REP   | Replace current version of this master file with the |
|       | version contained in this message.                   |
| UPD   | Change file record as defined in the record level    |
|       | event code for each record that follows              |

Note that only MEDICATION, MONITOR, and REPLACEMENT FLUID files will contain UPD, all other files or fields will be sent as REP.

<span id="_Toc93819389" class="anchor"></span>3.5.6.6 RESPONSE LEVEL CODE (ID)

RESPONSE LEVEL CODE specifies the application response level defined for a given Master File Message at the MFE segment level as defined in table 179.

HL7 Table 179 RESPONSE LEVEL CODE

|       |                                                     |
|-------|-----------------------------------------------------|
| Value | Description                                         |
| NE    | Never. No application level response needed         |
| ER    | Error/Reject conditions only. Only MFA segments     |
|       | denoting errors must be returned via the            |
|       | application level acknowledgment for this message   |
| AL    | Always. All MFA segments (whether denoting          |
|       | errors or not) must be returned via the application |
|       | level acknowledgment message                        |
| SU    | Success. Only MFA segments denoting success must    |
|       | be returned via the application level               |
|       | acknowledgment for this message                     |

When V*IST*A sends this field it will contain NE.

<span id="_Toc93819391" class="anchor"></span>3.5.7 Segment: MSA - Message Acknowledgment

The MSA segment contains information sent while acknowledging another message.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                       |
|-----|-----|-----|-----|-----------------------|
| 1   | 2   | ID  | R   | 8 ACKNOWLEDGMENT CODE |
| 2   | 20  | ST  | R   | MESSAGE CONTROL ID    |
| 3   | 80  | ST  |     | TEXT MESSAGE          |

<span id="_Toc93985449" class="anchor"></span>3.5.7.0 MSA field definitions

<span id="_Toc93985450" class="anchor"></span>3.5.7.1 ACKNOWLEDGMENT CODE (ID)

The ACKNOWLEDGMENT CODE can have the following values:

> HL7 Table 8 ACKNOWLEDGMENT CODE

|       |                    |             |     |
|-------|--------------------|-------------|-----|
| Value |                    | Description |     |
| AA    | Application Accept |             |     |
| AE    | Application Error  |             |     |
| AR    | Application Reject |             |     |

<span id="_Toc93819393" class="anchor"></span>3.5.7.2 MESSAGE CONTROL ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

<span id="_Toc93819395" class="anchor"></span>3.5.7.3 TEXT MESSAGE (ST)

This is an optional text field that further describes an error condition. The text may be printed in error logs or presented to an end user.

<span id="_Toc93819396" class="anchor"></span>3.5.8 Segment: MSH - Message Header

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                                 |
|-----|-----|-----|-----|-----|---------------------------------|
| 1   | 1   | ST  | R   |     | FIELD SEPARATOR                 |
| 2   | 4   | ST  | R   |     | ENCODING CHARACTERS             |
| 3   | 15  | ST  |     |     | SENDING APPLICATION             |
| 4   | 20  | ST  |     |     | SENDING FACILITY                |
| 5   | 30  | ST  |     |     | RECEIVING APPLICATION           |
| 6   | 30  | ST  |     |     | RECEIVING FACILITY              |
| 7   | 26  | TS  |     |     | DATE/TIME OF MESSAGE            |
| 8   | 40  | ST  |     |     | SECURITY                        |
| 9   | 7   | CM  | R   | 76  | MESSAGE TYPE                    |
| 10  | 20  | ST  | R   |     | MESSAGE CONTROL ID              |
| 11  | 1   | ID  | R   | 103 | PROCESSING ID                   |
| 12  | 8   | ID  | R   | 104 | VERSION ID                      |
| 15  | 2   | ID  |     | 155 | ACCEPT ACKNOWLEDGMENT TYPE      |
| 16  | 2   | ID  |     | 155 | APPLICATION ACKNOWLEDGMENT TYPE |

<span id="_Toc93900074" class="anchor"></span>3.5.8.0 MSH field definitions

<span id="_Toc93900075" class="anchor"></span>3.5.8.1 FIELD SEPARATOR (ST)

> This field is the separator between the segment ID and the first real field, MSH-2-ENCODING CHARACTERS. It serves as the separator and defines the character to be used as a separator for the rest of the message.

<span id="_Toc93819399" class="anchor"></span>3.5.8.2 ENCODING CHARACTERS (ST)

> This field is four characters in the following order: the component separator, repetition separator, escape character and subcomponent separator.

<span id="_Toc93819401" class="anchor"></span>3.5.8.3 SENDING APPLICATION (ST)

> This field is used for interface with lower level protocols.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field will contain SR SURGERY. When the AAIS or ancillary system transmits to the V*IST*A Surgery system, this field will contain SR AAIS.

<span id="_Toc93819403" class="anchor"></span>3.5.8.4 SENDING FACILITY (ST)

This field addresses one of several occurrences of the same application within the sending system. It is entirely site-defined.

This field is the three digit number identifying the medical center division, as found in the V*IST*A INSTITUTION file (#4).

<span id="_Toc93819406" class="anchor"></span>3.5.8.5 RECEIVING APPLICATION (ST)

This field is used for interface with lower level protocols.

When the AAIS or ancillary system transmits to the V*IST*A Surgery system, this field will contain SR AAIS. When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field will contain SR SURGERY.

<span id="_Toc93819409" class="anchor"></span>3.5.8.6 RECEIVING FACILITY (ST)

This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations.

This field is the three digit number identifying the medical center division, as found in the V*IST*A INSTITUTION file (#4).

<span id="_Toc93819412" class="anchor"></span>3.5.8.7 DATE/TIME OF MESSAGE (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

<span id="_Toc93819414" class="anchor"></span>3.5.8.8 SECURITY (ST)

In some applications of HL7 this field is used to implement security features. Its use is not yet further specified.

<span id="_Toc93819416" class="anchor"></span>3.5.8.9 MESSAGE TYPE (CM)

MESSAGE TYPE is a composite element made up of the following:  
\<message type\> \<trigger event\>  
The first component is the message type, found in table 76 - MESSAGE TYPE.  
The second component is the trigger event code found in table 3 - EVENT TYPE  
CODE. The receiving system uses this field to know the data segments to  
recognize, and possibly, the application to which to route this message.

<span id="_Toc93819417" class="anchor"></span>3.5.8.10 MESSAGE CONTROL ID (ST)

This field is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

<span id="_Toc93819418" class="anchor"></span>3.5.8.11 PROCESSING ID (ID)

This field is used to decide whether to process the message as defined in the HL7 application processing rules.

HL7 Table 103 PROCESSING ID

|       |            |             |
|-------|------------|-------------|
| Value |            | Description |
| D     | Debugging  |             |
| P     | Production |             |
| T     | Training   |             |

<span id="_Toc93819419" class="anchor"></span>3.5.8.12 VERSION ID (ID)

This field is matched by the receiving system to its own version to be sure the message is interpreted correctly. Only the following values are expected/accepted.

HL7 Table 104 VERSION ID

|       |                           |
|-------|---------------------------|
| Value | Description               |
| 2.1   | Release 2.1 March 1990    |
| 2.2   | Release 2.2 December 1994 |

<span id="_Toc93819421" class="anchor"></span>3.5.8.15 ACCEPT ACKNOWLEDGMENT TYPE (ID)

This field defines the conditions under which accept acknowledgments are

required to be returned in response to this message.

HL7 Table 155 ACCEPT/APPLICATION ACKNOWLEDGMENT CONDITIONS

|       |                              |
|-------|------------------------------|
| Value | Description                  |
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

<span id="_Toc93819422" class="anchor"></span>3.5.8.16 APPLICATION ACKNOWLEDGMENT TYPE (ID)

> This field defines the conditions under which application acknowledgments are

> required to be returned in response to this message.

> HL7 Table 155 ACCEPT/APPLICATION ACKNOWLEDGMENT CONDITIONS

|       |                              |
|-------|------------------------------|
| Value | Description                  |
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/reject conditions only |
| SU    | Successful completion only   |

<span id="_Toc94060326" class="anchor"></span>3.5.9 Segment: NTE - Anesthesiologist Notes and Comments

The NTE segment is used to report the Anesthesiologists notes or comments.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                             |
|-----|-----|-----|-----|-----------------------------|
| 1   | 4   | SI  |     | SET ID - NOTES AND COMMENTS |
| 2   | 8   | ID  |     | 105 SOURCE OF COMMENT       |
| 3   | 80  | FT  | Y   | COMMENT                     |

<span id="_Toc93900089" class="anchor"></span>3.5.9.0 NTE field definitions

<span id="_Toc93900090" class="anchor"></span>3.5.9.1 SET ID - NOTES AND COMMENTS (SI)

> This field may be used where multiple NTE segments are included in a message. However, since this segment will be following the Anesthesia (OBR) segment, this field will be a sequential number starting at one.

<span id="_Toc93900091" class="anchor"></span>3.5.9.2 SOURCE OF COMMENT (ID)

> This field is used to identify the source of the note or comment.

> HL7 Table 105 SOURCE OF COMMENT

|       |                                                    |
|-------|----------------------------------------------------|
| Value | Description                                        |
| L     | Ancillary (filler) department is source of comment |
| P     | Orderer (placer) is source of comment              |
| O     | Other system is source of comment                  |

<span id="_Toc93819424" class="anchor"></span>3.5.9.3 COMMENT (FT)

> This field contains the comment.

> \*\* NOTE: This field has a length of 80 that will increase to its recommended 64k length with the release of the V*IST*A HL7 V. 1.6. package.

<span id="_Toc93819426" class="anchor"></span>3.5.10 Segment: OBR - Observation Request

In the reporting of clinical data, the OBR serves as the report header. It identifies the observation set represented by the following observations.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                              |
|-----|-----|-----|-----|-----|------------------------------|
| 1   | 4   | SI  |     |     | SET ID - OBSERVATION REQUEST |
| 3   | 75  | CM  |     |     | FILLER ORDER NUMBER          |
| 4   | 200 | CE  | R   |     | UNIVERSAL SERVICE ID         |
| 7   | 26  | TS  | C   |     | OBSERVATION DATE/TIME        |
| 8   | 26  | TS  | C   |     | OBSERVATION END DATE/TIME    |
| 16  | 60  | CN  |     | Y   | ORDERING PROVIDER            |

<span id="_Toc93900094" class="anchor"></span>3.5.10.0 OBR field definitions

<span id="_Toc93900095" class="anchor"></span>3.5.10.1 SET ID - OBSERVATION REQUEST (SI)

SET ID - OBSERVATION REQUEST is a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

Seven different types of observations can be returned. The possible OBRs include those dealing with operation and procedure data, tourniquets, monitors, medications, occurrences, and anesthesia.

<span id="_Toc93819430" class="anchor"></span>3.5.10.3 FILLER ORDER NUMBER (CM)

FILLER ORDER NUMBER is a composite element made up of the following:  
\<unique filler ID\> \<filler application ID\>  
This field is a permanent identifier for an order and its associated observations.  
The first component is a string that identifies an individual order segment. It  
identifies an order uniquely among all orders from a particular filling application.

When an observation result message is sent only the first component contains information. The information that is sent is the surgery case number.

<span id="_Toc93819432" class="anchor"></span>3.5.10.4 UNIVERSAL SERVICE ID (CE)

> UNIVERSAL SERVICE ID is a coded element made up of the following:  
> \<identifier\> \<text\> \<name of coding system\> \<alternate identifier\> \<alternate  
> text\> \<name of alternate coding system\>  
> This field is an identifier code for the observation. This can be based on local  
> and/or universal codes.

> When an observation result message is sent, two universal codes and four local  
> codes can be returned. The codes transmitted for the identifier, text, and coding  
> system are:

Identifier Text Coding System

|        |                           |     |
|--------|---------------------------|-----|
| 5000.7 | OPERATION                 | AS4 |
| 5000.8 | ANESTHESIA                | AS4 |
| null   | TOURNIQUET                | L   |
| null   | REPLACEMENT FLUID         | L   |
| null   | MONITOR                   | L   |
| null   | MEDICATION                | L   |
| null   | PROCEDURE                 | L   |
| null   | INTRAOPERATIVE OCCURRENCE | L   |
| null   | POSTOPERATIVE OCCURRENCE  | L   |
| null   | PROCEDURE OCCURRENCE      | L   |
| null   | NONOPERATIVE OCCURRENCE   | L   |

When an observation result message is sent, the alternate identifier, text, and coding system are used when the OBR is for ANESTHESIA or MEDICATION.

When the OBR is for ANESTHESIA the alternate text and coding system are

Alt. Identifier Alt. Text Alt. Coding System

null name of anesthesia technique listed below L

The expected anesthesia techniques are GENERAL, MONITORED ANESTHESIA CARE, SPINAL, EPIDURAL, LOCAL, and OTHER.

The alternate identifier, text, and coding system are

Alt. Identifier Alt. Text Alt. Coding System

null name of monitor 99VA133.4

> The alternate coding system component is 99VA133.4. The information comes from the VISTA MONITORS file (#133.4).

> When the OBR is for MEDICATION the alternate text and coding system are

Alt. Identifier Alt. Text Alt. Coding System

null name of medication 99VA50

The alternate coding system component is 99VA50. The information comes from the VISTA DRUG file (#50).

<span id="_Toc93819439" class="anchor"></span>3.5.10.7 OBSERVATION DATE/TIME (TS)

> The OBSERVATION DATE/TIME is the clinically relevant date/time of the observation. In the case of observations taken directly from a subject, it is the actual date and time the observation is obtained.

> When an observation result message is sent this field contains the time the operation begins, the tourniquet is applied, the monitor is installed, the procedure begins, or the medication is administered.

<span id="_Toc93819442" class="anchor"></span>3.5.10.8 OBSERVATION END DATE/TIME (TS)

> The OBSERVATION END DATE/TIME is the end date and time of a study or timed specimen collection. If an observation takes place over a substantial period of time, it indicates when the observation period ended.

> When an observation result message is sent this field contains the time the operation ends, the tourniquet is released, the procedure ends, or the monitor is removed.

<span id="_Toc93819445" class="anchor"></span>3.5.10.16 ORDERING PROVIDER (CN)

> ORDERING PROVIDER is a composite ID number and name made up of the  
> following:  
> \<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\>  
> \<prefix\> \<degree\> \<source table \>  
> This field identifies the provider who ordered the test. The ID code and the  
> name may be present.

When an observation result message is sent this field contains information  
about the person ordering the medication when the OBR is for MEDICATION.  
The id number (social security number), uniquely identifies the ordering  
provider. The name component is from the Surgery sub-field ORDERED BY (#2  
of Subfile \#130.34). All components must match the VISTA NEW PERSON file  
(#200).

<span id="_Toc93819448" class="anchor"></span>3.5.11 Segment: OBX - Observation

The OBX segment is used to transmit a single observation or observation fragment.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                              |
|-----|-----|-----|-----|-----|------------------------------|
| 1   | 4   | SI  |     |     | SET ID - OBSERVATION SIMPLE  |
| 2   | 2   | ID  | R   | 125 | VALUE TYPE                   |
| 3   | 80  | CE  | R   |     | OBSERVATION IDENTIFIER       |
| 5   | var | ST  |     |     | OBSERVATION VALUE            |
| 6   | 60  | CE  |     |     | UNITS                        |
| 11  | 2   | ID  | R   | 85  | OBSERV RESULT STATUS         |
| 14  | 26  | TS  |     |     | DATE/TIME OF THE OBSERVATION |
| 16  | 60  | CN  |     |     | RESPONSIBLE OBSERVER         |

<span id="_Toc93900101" class="anchor"></span>3.5.11.0 OBX field definitions

<span id="_Toc93900102" class="anchor"></span>3.5.11.1 SET ID - OBSERVATION SIMPLE (SI)

> SET ID - OBSERVATION SIMPLE is a sequence number used to identify the segment repetitions.

<span id="_Toc93819449" class="anchor"></span>3.5.11.2 VALUE TYPE (ID)

> This field is the format of the observation value in OBX.

> Although there are other entries in the HL7 table, only the following values are transmitted.

HL7 Table 125 VALUE TYPE

|       |                            |
|-------|----------------------------|
| Value | Description                |
| TX    | Text                       |
| TS    | Time stamp (date and time) |
| CN    | Composite ID and name      |
| CE    | Coded entry                |
| NM    | Numeric                    |

<span id="_Toc93819450" class="anchor"></span>3.5.11.3 OBSERVATION IDENTIFIER (CE)

> OBSERVATION IDENTIFIER is a coded element made up of the following:  
> \<identifier\> \<text\> \<name of coding system\> \<alternate identifier\> \<alternate  
> text\> \<name of alternate coding system\>  
> This field is a unique identifier for the observation.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the  
> identifier component is the Universal (AS4) Identifier for Common Test Battery  
> as defined in 7.A of the HL7 2.2 Standard. The text component indicates height,  
> body weight, blood pressure, pulse rate, or temperature. Additionally, the  
> PATIENT CLASS, ANES. SUPERVISE CODE, CANCEL DATE and CANCEL  
> REASON for canceled cases, MEDICAL SPECIALTY for NON-OR cases, and  
> SURGICAL SPECIALTY and SURGEON PGY for OR cases are transmitted.  
> Patient class refers to the patient’s hospital admission status at the time of  
> surgery. With this transmission, the identifier component is null, the text  
> component are as shown above, and the coding system is L.

When the AAIS or ancillary system transmits to the V*IST*A Surgery system, the identifier, text and coding system components are found in the tables below.

When the OBR is for OPERATION the OBX OBSERVATION IDENTIFIER is

Identifier Text Coding System

|        |                              |         |
|--------|------------------------------|---------|
| null   | ANES. SUPER.                 | 99VA200 |
| null   | ANES. SUPERVISE CODE         | L       |
| null   | ANESTHESIA AVAILABLE TIME    | L       |
| null   | ANESTHESIA CARE END TIME     | L       |
| null   | ANESTHESIA CARE START TIME   | L       |
| 1000   | ANESTHESIA TEMP              | AS4     |
| null   | ASA CLASS                    | L       |
| null   | ASSISTANT ANESTHETIST        | 99VA200 |
| null   | ATT. SURGEON                 | 99VA200 |
| null   | ATTENDING CODE               | L       |
| null   | BLOOD LOSS                   | L       |
| 1002   | BP                           | AS4     |
| null   | CASE SCHEDULE TYPE           | L       |
| 1006.2 | HR                           | AS4     |
| null   | INDUCTION COMPLETE           | L       |
| null   | NURSE PRESENT TIME           | L       |
| null   | OR LOCATION                  | 99VA44  |
| null   | OR SETUP TIME                | L       |
| null   | PAC(U) ADMIT TIME            | L       |
| null   | PAC(U) DISCHARGE TIME        | L       |
| null   | PRIN. ANES.                  | 99VA200 |
| null   | RELIEF ANESTHETIST           | 99VA200 |
| null   | REPLACEMENT FLUID            | 99VA200 |
| 1007   | RR                           | AS4     |
| null   | SURGEON                      | 99VA200 |
| null   | SURGEON PGY                  | L       |
| null   | SURGEON PRESENT TIME         | L       |
| null   | TIME PATIENT IN HOLDING AREA | L       |
| null   | TIME PATIENT IN OR           | L       |
| null   | TIME PATIENT OUT OR          | L       |
| null   | TOTAL URINE OUTPUT           | L       |

When the OBR is for TOURNIQUET the OBX OBSERVATION IDENTIFIER is

<u>Identifier Text Coding System</u>

null SITE TOURNIQUET APPLIED L

The alternate identifier, text and coding system are from the following table.

Alt Identifier Alt Text Alt Coding System

|      |                 |     |
|------|-----------------|-----|
| null | RIGHT UPPER LEG | L   |
| null | RIGHT UPPER ARM | L   |
| null | LEFT UPPER LEG  | L   |
| null | LEFT UPPER ARM  | L   |
| null | RIGHT ANKLE     | L   |
| null | LEFT ANKLE      | L   |

When the OBR is for MONITOR the OBX OBSERVATION IDENTIFIER is

<u>Identifier Text Coding System</u>

null MONITOR APPLIED BY L

When the OBR is for MEDICATION the OBX OBSERVATION IDENTIFIER is

|            |                  |               |
|------------|------------------|---------------|
| Identifier | Text             | Coding System |
| null       | MEDICATION USED  | L             |
| null       | MEDICATION ROUTE | L             |

When the OBR is for ANESTHESIA the OBX OBSERVATION IDENTIFIER is

<u>Identifier Text Coding System</u>

|      |                                |         |
|------|--------------------------------|---------|
| null | ADMINISTRATION METHOD          | L       |
| null | ANESTHESIA AGENT               | L       |
| null | ANESTHESIA APPROACH            | L       |
| null | ANESTHESIA ROUTE               | L       |
| null | BARICITY                       | L       |
| null | END VENT RATE                  | L       |
| null | END VENT TV                    | L       |
| null | EPIDURAL METHOD                | L       |
| null | EXTUBATED BY                   | 99VA200 |
| null | EXTUBATED IN                   | L       |
| null | LARYNGOSCOPE SIZE              | L       |
| null | LARYNGOSCOPE TYPE              | L       |
| null | PATIENT STATUS                 | L       |
| null | PRINCIPAL ANES TECHNIQUE (Y/N) | L       |
| null | TEST DOSE                      | L       |
| null | TUBE SIZE                      | L       |
| null | TUBE TYPE                      | L       |

For the ANESTHESIA AGENT and TEST DOSE OBXs, alternate identifier, text, and coding system are identified in the tables below.

For ANESTHESIA AGENT, the alternate fields are

|                                         |                          |                    |
|-----------------------------------------|--------------------------|--------------------|
| Alt. Identifier                         | Alt. Text                | Alt. Coding System |
| null                                    | name of anesthesia agent | 99VA50             |
| For TEST DOSE, the alternate fields are |                          |                    |
| Alt. Identifier                         | Alt. Text                | Alt. Coding System |
| null                                    | name of test dose drug   | 99VA50             |

The alternate coding system component is 99VA50. The information comes from the V*IST*A DRUG file (#50).

When the OBR is for PROCEDURE the OBX OBSERVATION IDENTIFIER is

> Identifier Text Coding System

|        |                            |         |
|--------|----------------------------|---------|
| null   | ANES. SUPER.               | 99VA200 |
| null   | ANES. SUPERVISE CODE       | L       |
| null   | ANESTHESIA AVAILABLE TIME  | L       |
| null   | ANESTHESIA CARE END TIME   | L       |
| null   | ANESTHESIA CARE START TIME | L       |
| 1000   | ANESTHESIA TEMP            | AS4     |
| null   | ASA CLASS                  | L       |
| null   | ASSISTANT ANESTHETIST      | 99VA200 |
| null   | ATTEND PROVIDER            | 99VA200 |
| null   | BLOOD LOSS                 | L       |
| 1002   | BP                         | AS4     |
| 1006.2 | HR                         | AS4     |
| null   | INDUCTION COMPLETE         | L       |
| null   | NON-OR LOCATION            | 99VA44  |
| null   | PRIN. ANES.                | 99VA200 |
| null   | PROVIDER                   | 99VA200 |
| null   | RELIEF ANESTHETIST         | 99VA200 |
| 1007   | RR                         | AS4     |
| null   | TOTAL URINE OUTPUT         | L       |

When the OBR is for PROCEDURE OCCURRENCE the OBX OBSERVATION IDENTIFIER is

> Identifier Text Coding System

null DATE PROCEDURE OCCURRENCE NOTED L

null PROCEDURE OCCURRENCE CATEGORY L

null PROCEDURE OCCURRENCE OUTCOME L

null PROCEDURE OCCURRENCE TREATMENT L

When the OBR is for INTRAOPERATIVE OCCURRENCE the OBX OBSERVATION IDENTIFIER is

|            |                             |               |     |
|------------|-----------------------------|---------------|-----|
| Identifier | Text                        | Coding System |     |
| null       | INTRAOP OCCURRENCE CATEGORY |               | L   |
| null       | INTRAOP OCCURRENCE CODE     |               | L   |
| null       | INTRAOP OCCURRENCE OUTCOME  |               | L   |

When the OBR is for POSTOPERATIVE OCCURRENCE the OBX OBSERVATION IDENTIFIER is

> Identifier Text Coding System

null DATE POSTOP OCCURRENCE NOTED L

null POSTOP OCCURRENCE CATEGORY L

null POSTOP OCCURRENCE CODE L

null POSTOP OCCURRENCE OUTCOME L

When the OBR is for NONOPERATIVE OCCURRENCE the OBX OBSERVATION IDENTIFIER is

> Identifier Text Coding System

> null DATE NONOP OCCURRENCE NOTED L

> null NONOP OCCURRENCE CATEGORY L

> null NONOP OCCURRENCE OUTCOME L

null NONOP OCCURRENCE TREATMENT L

<span id="_Toc93819468" class="anchor"></span>3.5.11.5 OBSERVATION VALUE (ST)

> This field is the value observed by the observation producer. The length of this field is variable, depending upon the value type.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, PATIENT CLASS is transmitted. This refers to the patient’s hospital admission status at the time of surgery. The identifier component is null, the text component is either INPATIENT or OUTPATIENT, and the coding system is L.

When an observation result message is sent the observation value varies based upon the OBX. The observation value is identified in the table below.

| Value Type | OBX                          | Observation Value             |
|------------|------------------------------|-------------------------------|
| TX         | BP                           | systolic/diastolic            |
| TX         | MEDICATION USED              | dose - text                   |
| TS         | ANESTHESIA AVAILABLE TIME    | date time                     |
| TS         | ANESTHESIA CARE END TIME     | date time                     |
| TS         | ANESTHESIA CARE START TIME   | date time                     |
| TS         | INDUCTION COMPLETE           | date time                     |
| TS         | NURSE PRESENT TIME           | date time                     |
| TS         | SURGEON PRESENT TIME         | date time                     |
| TS         | TIME PATIENT IN HOLDING AREA | date time                     |
| TS         | TIME PATIENT IN OR           | date time                     |
| TS         | TIME PATIENT OUT OR          | date time                     |
| TS         | PAC(U) ADMIT TIME            | date time                     |
| TS         | PAC(U) DISCHARGE TIME        | date time                     |
| CN         | ANES. SUPER.                 | ID, name in HL7 format        |
| CN         | ASSISTANT ANESTHETIST        | ID, name in HL7 format        |
| CN         | ATT. SURGEON                 | ID, name in HL7 format        |
| CN         | ATTEND PROVIDER              | ID, name in HL7 format        |
| CN         | EXTUBATED BY                 | ID, name in HL7 format        |
| CN         | MONITOR APPLIED BY           | ID, name in HL7 format        |
| CN         | PRIN. ANES.                  | ID, name in HL7 format        |
| CN         | PROVIDER                     | ID, name in HL7 format        |
| CN         | RELIEF ANESTHETIST           | ID, name in HL7 format        |
| CN         | SURGEON                      | ID, name in HL7 format        |
| NM         | ANESTHESIA AGENT             | dose in milligrams            |
| NM         | ANESTHESIA TEMP              | temperature °C                |
| NM         | BLOOD LOSS                   | number of milliliters         |
| NM         | END VENT RATE                | end vent rate                 |
| NM         | END VENT TV                  | end vent tidal volume setting |
| NM         | HR                           | pulse rate                    |
| NM         | LARYNGOSCOPE SIZE            | laryngoscope size             |
| NM         | OR SETUP TIME                | number of minutes             |
| NM         | REPLACEMENT FLUID USED       | number of milliliters         |
| NM         | RR                           | rate of respiration           |
| NM         | SITE TOURNIQUET APPLIED      | millimeter (HG)               |
| NM         | SURGEON PGY                  | number of post graduate years |
| NM         | TEST DOSE                    | dose in milligrams            |
| NM         | TOTAL URINE OUTPUT           | number of milliliters         |
| NM         | TUBE SIZE                    | tube size                     |

The remaining OBXs are coded elements which are V*IST*A Surgery set of codes values. The elements of the OBSERVATION VALUE coded entry consist of \<identifier\> \<text\> \<name of coding system\>. The identifier is always null. The name of the coding system is always L for local coding system. The text value is identified in the Observation Value column.

> OBX Observation Value

ADMINISTRATION METHOD BOLUS

DRIP INFUSION

INTERMITTENT

ANESTHESIA APPROACH BLIND

BLIND LARYNGOSCOPY

DIRECT VISION LARYNGOSCOPY FIBEROPTIC LARYNGOSCOPY

RAPID SEQUENCE

ANESTHESIA ROUTE NASAL

ORAL

TRACHEOSTOMY

ANES. SUPERVISE CODE 1. STAFF CASE

2\. STAFF ASSISTED BY RESIDENT OR...C.R.N.A.

3\. STAFF ASSISTING C.R.N.A.

4\. STAFF ASSISTING RESIDENT

5\. STAFF CONSULTING IN OR

6\. STAFF AVAILABLE IN OR SUITE

7\. STAFF AVAILABLE IN HOSP./UNIV  
.... COMPLEX

8\. STAFF CALLED FOR EMERGENCY

9\. C.R.N.A. INDEPENDENT DUTY -  
...MD/DDS SUP.

ASA CLASS 1-NO DISTURB.

1E-NO DISTURB-EMERG

2-MILD DISTURB.

2E-MILD DISTURB.-EMERG

3-SEVERE DISTURB.

3E-SEVERE DIST.-EMERG.

4-LIFE THREAT

4E-LIFE THREAT-EMERG.

5-MORIBUND

5E-MORIBUND-EMERG

> OBX Observation Value

ATTENDING CODE 0. STAFF ALONE

1\. ATTENDING IN O.R.

2\. ATTENDING IN O.R. SUITE

> 3\. ATTENDING NOT PRESENT, BUT AVAILABLE

> LEVEL 0. ATTENDING DOING THE OPERATION

> LEVEL 1. ATTENDING IN O.R. ASSISTING THE RESIDENT

> LEVEL 2. ATTENDING IN O.R., NOT SCRUBBED

> LEVEL 3. ATTENDING NOT PRESENT IN O.R. SUITE, IMMEDIATELY AVAILABLE

> LEVEL A: ATTENDING DOING THE OPERATION

> LEVEL B: ATTENDING IN O.R., SCRUBBED

> LEVEL C: ATTENDING IN O.R., NOT SCRUBBED

> LEVEL D: ATTENDING IN O.R. SUITE, IMMEDIATELY AVAILABLE

> LEVEL E: EMERGENCY CARE, ATTENDING CONTACTED ASAP

> LEVEL F: NON-OR PROCEDURE DONE IN THE OR, ATTENDING IDENTIFIED

BARICITY HYPERBARIC

HYPOBARIC

ISOBARIC

CASE SCHEDULE TYPE ADD ON (NON-EMERGENT)

ELECTIVE

EMERGENCY

STANDBY

URGENT

EPIDURAL METHOD HANGING DROP

LOSS OF RESISTANCE

BOTH

EXTUBATED IN OR

PACU

SICU

> OBX Observation Value

LARYNGOSCOPE TYPE FIBEROPTIC BRONCHOSCOPE

FIBEROPTIC LARYNGOSCOPE

FIBEROPTIC STYLET

GUEDEL

MACINTOSH

MILLER

WIS-FOREGGER

OTHER MEDICATION ROUTE INFILTRATE  
INTRAMUSCULAR  
INTRAVENOUS  
IRRIGATION  
PREPUMP  
RECTAL  
SUBCUTANEOUS  
SUBLINGUAL  
TOPICAL  
OTHER

PATIENT STATUS AWAKE  
INDUCED  
SEDATED

PRINCIPAL ANES

TECHNIQUE (Y/N) NO  
YES

TUBE TYPE 2 LUMEN, LT. ENDOBRONCHIAL 2 LUMEN, RT. ENDOBRONCHIAL BIVONA CUFF

LASER PROTECTED

PVC LOW PRESSURE REINFORCED

SILASTIC LOW PRESSURE TRACHEOSTOMY CUFFED OTHER

<span id="_Toc93819474" class="anchor"></span>3.5.11.6 UNITS (CE)

> UNITS is a coded element made up of the following:  
> \<identifier\> \<text\> \<name of coding system\>  
> The default coding system for UNITS consists of the ISO abbreviations as  
> defined in section 7.1.4 of the HL7 V. 2.2 Standard.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system and when the AAIS or ancillary system transmits to the V*IST*A Surgery system, only the ISO abbreviation is sent in the identifier component.

<span id="_Toc93985487" class="anchor"></span>3.5.11.11 OBSERV RESULT STATUS (ID)

> This field reflects the current completion status of the results for one OBSERVATION IDENTIFIER.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field contains S.

> When the AAIS or ancillary system transmits to the V*IST*A Surgery system, this  
> field contains F.

> Although there are other entries in the HL7 table, only the following values are transmitted.

HL7 Table 85 - OBSERVATION RESULT STATUS CODES INTERPRETATION

|       |                    |                                  |
|-------|--------------------|----------------------------------|
| Value |                    | Description                      |
| F     | Final results; can | only be changed with a corrected |
|       | result             |                                  |
| S     | Partial results    |                                  |

<span id="_Toc93819479" class="anchor"></span>3.5.11.14 DATE/TIME OF THE OBSERVATION (TS)

> The observation date-time is the physiologically relevant date-time or the closest approximation to that date-time. In the case of observations taken directly on the patient, the observation date-time is the date-time that the observation is performed. This field is used only when the V*IST*A Surgery system transmits to the AAIS or ancillary system.

<span id="_Toc93819481" class="anchor"></span>3.5.11.16 RESPONSIBLE OBSERVER (CN)

> RESPONSIBLE OBSERVER is a composite ID number and name made up of the following:

> \<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\> \<prefix\> \<degree\> \<source table ID\> This field identifies the person responsible for the observation (i.e., the person who either performed or verified it).

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system and when the AAIS or ancillary system transmits to the V*IST*A Surgery system, the id number (social security number), uniquely identifies the responsible observer. The name component is from the VISTA NEW PERSON file (#200).

<span id="_Toc94060349" class="anchor"></span>3.5.12 Segment: PID – Patient Identification

> The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that is not likely to change frequently.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |     |                          |
|-----|-----|-----|-----|-----|-----|--------------------------|
| 1   | 4   | SI  |     |     |     | SET ID - PATIENT ID      |
| 3   | 20  | CM  | R   | Y   |     | PATIENT ID (INTERNAL ID) |
| 4   | 12  | ST  |     |     |     | ALTERNATE PATIENT ID     |
| 5   | 48  | PN  | R   |     |     | PATIENT NAME             |
| 6   | 30  | ST  |     |     |     | MOTHER’S MAIDEN NAME     |
| 7   | 8   | DT  |     |     |     | DATE OF BIRTH            |
| 8   | 1   | ID  |     |     | 1   | SEX                      |
| 10  | 1   | ID  |     |     | 5   | RACE                     |
| 11  | 106 | AD  |     | Y   |     | PATIENT ADDRESS          |
| 13  | 40  | TN  |     | Y   |     | PHONE NUMBER - HOME      |
| 16  | 1   | ID  |     |     | 2   | MARITAL STATUS           |
| 17  | 3   | ID  |     |     | 6   | RELIGION                 |
| 19  | 16  | ST  |     |     |     | SSN NUMBER - PATIENT     |

<span id="_Toc93985491" class="anchor"></span>3.5.12.0 PID field definitions

<span id="_Toc93985492" class="anchor"></span>3.5.12.1 SET ID - PATIENT ID (SI)

> SET ID - PATIENT ID is a sequence number used to identify the segment repetitions.

<span id="_Toc93819485" class="anchor"></span>3.5.12.3 PATIENT ID (INTERNAL ID) (CM)

> PATIENT ID (INTERNAL ID) is a composite element made up of the following: \<patient ID\> \<check digit\> \<check digit scheme\> \<assigning facility ID\> \<type\>

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the first component is the unique internal entry number from the PATIENT file (#2). The second and third components are the check digit and check digit scheme.

<span id="_Toc93819487" class="anchor"></span>3.5.12.4 ALTERNATE PATIENT ID (ST)

> This field contains an alternate identification number.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the Brief ID for a patient is sent. It is composed of the last four numbers of the SSN.

<span id="_Toc93985495" class="anchor"></span>3.5.12.5 PATIENT NAME (PN)

> The PATIENT NAME field is in standard HL7 format.

<span id="_Toc93985496" class="anchor"></span>3.5.12.6 MOTHER’S MAIDEN NAME (ST)

> This field is the family name under which the mother was born. It is used to disambiguate patients with the same last name.

<span id="_Toc93985497" class="anchor"></span>3.5.12.7 DATE OF BIRTH (DT)

> This field is the patient’s date of birth.

<span id="_Toc93985498" class="anchor"></span>3.5.12.8 SEX (ID)

> This field is the patient’s sex. Although there are other entries in the HL7 table, only the following values are transmitted.

> HL7 Table 1 - SEX

|       |        |             |
|-------|--------|-------------|
| Value |        | Description |
| F     | Female |             |
| M     | Male   |             |

<span id="_Toc93819490" class="anchor"></span>

3.5.12.10 RACE (ID)

> This field is the patient’s race. V*IST*A Surgery is sending the table value and the text description from the user defined table 5.

HL7 (user defined) Table 5 - RACE

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 78%" />
<col style="width: 4%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Value</td>
<td>Description</td>
<td></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p></td>
<td>HISPANIC, WHITE<br />
HISPANIC, BLACK<br />
AMERICAN INDIAN OR ALASKA NATIVE<br />
BLACK, NOT OF HISPANIC ORIGIN<br />
ASIAN OR PACIFIC ISLANDER<br />
WHITE, NOT OF HISPANIC ORIGIN<br />
UNKNOWN</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc93985500" class="anchor"></span>3.5.12.11 PATIENT ADDRESS (AD)

> This field is the mailing address of the patient.

<span id="_Toc93985501" class="anchor"></span>3.5.12.13 PHONE NUMBER - HOME (TN)

> This field is the patient’s home phone number.

<span id="_Toc93985502" class="anchor"></span>3.5.12.16 MARITAL STATUS (ID)

> This field is the patient’s marital status. These entries correspond to the V*IST*A MARITAL STATUS file (#11).

HL7 (user defined) Table 2 - MARITAL STATUS

|       |               |
|-------|---------------|
| Value | Description   |
| S     | Separated     |
| D     | Divorced      |
| M     | Married       |
| N     | Never Married |
| W     | Widow/Widower |
| U     | Unknown       |

<span id="_Toc93819492" class="anchor"></span>

3.5.12.17 RELIGION (ID)

This field is the patient’s religion. These entries correspond to the V*IST*A RELGION file (#13).

HL7 (user defined) Table 6 - RELIGION

|       |                         |
|-------|-------------------------|
| Value | Description             |
| 0     | CATHOLIC                |
| 1     | JEWISH                  |
| 2     | EASTERN ORTHODOX        |
| 3     | BAPTIST                 |
| 4     | METHODIST               |
| 5     | LUTHERAN                |
| 6     | UNITED CHURCH OF CHRIST |
| 7     | PRESBYTERIAN            |
| 8     | EPISCOPALIAN            |
| 9     | ADVENTIST               |
| 10    | ASSEMBLY OF GOD         |
| 11    | BRETHREN                |
| 12    | CHRISTIAN SCIENTIST     |

HL7 (user defined) Table 6 - RELIGION cont.

|       |                             |
|-------|-----------------------------|
| Value | Description                 |
| 13    | CHURCH OF CHRIST            |
| 14    | CHURCH OF GOD               |
| 15    | DISCIPLES OF CHRIST         |
| 16    | EVANGELICAL COVENANT        |
| 17    | FRIENDS                     |
| 18    | JEHOVAH’S WITNESS           |
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

<span id="_Toc93985504" class="anchor"></span>3.5.12.19 SSN NUMBER - PATIENT (ST)

> This field is the patient’s social security number.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this number contains no dashes.

<span id="_Toc93819495" class="anchor"></span>3.5.13 Segment: STF - Staff Identification

The STF segment is used to identify personnel associated with cases in the Surgery Case file (#130).

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                         |
|-----|-----|-----|-----|-----|-------------------------|
| 1   | 60  | CE  | R   |     | STF - PRIMARY KEY VALUE |
| 3   | 48  | PN  | O   |     | STAFF NAME              |
| 13  | 26  | CM  | O   | Y   | INACTIVATION DATE       |

<span id="_Toc93985506" class="anchor"></span>3.5.13.0 STF field definition

<span id="_Toc93985507" class="anchor"></span>3.5.13.1 STF - PRIMARY KEY VALUE (CE)

> This field must match MFE-4 - PRIMARY KEY VALUE to identify which entry is being referenced.

<span id="_Toc93819498" class="anchor"></span>3.5.13.3 STAFF NAME (PN)

> This field identifies the staff person’s name in the form:  
> \<family name\>\<given name\>\<middle initial or name\>

<span id="_Toc93819500" class="anchor"></span>3.5.13.13 INACTIVATION DATE (CM)

> Components: \<date (TS)\>\<institution name (CE)\>  
> This field identifies the date the staff became inactive for an institution.  
> Note that the CE component of this field uses the subcomponent character for  
> its delimiters.

<span id="_Toc93985510" class="anchor"></span>3.5.14 Segment: QRD - Query Definition

The QRD segment is used to define a query.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |     |                           |
|-----|-----|-----|-----|-----|-----|---------------------------|
| 1   | 26  | TS  | R   |     |     | QUERY DATE/TIME           |
| 2   | 1   | ID  | R   |     | 106 | QUERY FORMAT CODE         |
| 3   | 1   | ID  | R   |     | 91  | QUERY PRIORITY            |
| 4   | 10  | ST  | R   |     |     | QUERY ID                  |
| 7   | 10  | CQ  | R   |     | 126 | QUANTITY LIMITED REQUEST  |
| 8   | 20  | ST  | R   | Y   |     | WHO SUBJECT FILTER        |
| 9   | 3   | ID  | R   | Y   | 48  | WHAT SUBJECT FILTER       |
| 10  | 20  | ST  | R   | Y   |     | WHAT DEPARTMENT DATA CODE |

<span id="_Toc93985511" class="anchor"></span>3.5.14.0 QRD field definitions

<span id="_Toc93985512" class="anchor"></span>3.5.14.1 QUERY DATE/TIME (TS)

> This field is the date and time the query is generated by the application program.

<span id="_Toc93819501" class="anchor"></span>3.5.14.2 QUERY FORMAT CODE (ID)

> This field contains the query format code.

> When the AAIS queries the V*IST*A Surgery system, this field always contains the code R.

HL7 Table 106 - QUERY FORMAT CODE

|       |                                       |     |
|-------|---------------------------------------|-----|
| Value | Description                           |     |
| D     | Response is in display format         |     |
| R     | Response is in record-oriented format |     |

<span id="_Toc93819505" class="anchor"></span>3.5.14.3 QUERY PRIORITY (ID)

> This field contains the time frame in which the response is expected.

> When the AAIS queries the V*IST*A Surgery system, this field always contains the priority I.

HL7 Table 91 - QUERY PRIORITY

|       |           |             |
|-------|-----------|-------------|
| Value |           | Description |
| D     | Deferred  |             |
| I     | Immediate |             |

<span id="_Toc93819509" class="anchor"></span>3.5.14.4 QUERY ID (ST)

> This field is a unique identifier for the query. It is assigned by the querying application, and returned intact by the responding application.

<span id="_Toc93819511" class="anchor"></span>3.5.14.7 QUANTITY LIMITED REQUEST (CQ)

> QUANTITY LIMITED REQUEST is a composite quantity with units made up of the following: \<quantity\> \<units\>  
> This field is the maximum length of the response that can be accepted by the requesting system. Valid responses are numerical values given in the units specified in the second component.

> When the AAIS queries the V*IST*A Surgery system, this field contains 1~RD (one record).

HL7 Table 126 - QUANTITY LIMITED REQUEST

|       |                 |             |
|-------|-----------------|-------------|
| Value |                 | Description |
| CH    | Characters      |             |
| LI    | Lines           |             |
| PG    | Pages           |             |
| RD    | Records         |             |
| ZO    | Locally defined |             |

<span id="_Toc93819514" class="anchor"></span>3.5.14.8 WHO SUBJECT FILTER (ST)

> This field identifies the subject, or who the inquiry is about.

> When the AAIS queries the V*IST*A Surgery system, this field contains either the selected patient’s name in HL7 format or the words ALL for all cases requested, scheduled, not complete or non-OR.

<span id="_Toc93819516" class="anchor"></span>3.5.14.9 WHAT SUBJECT FILTER (ID)

> This field describes the kind of information that is required to satisfy the request. Valid codes define the type of transaction inquiry and may be extended locally during implementation. Refer to HL7 table 48 for a complete list of table entries.

> When the AAIS queries the V*IST*A Surgery system, this field contains OTH.

<span id="_Toc93819519" class="anchor"></span>3.5.14.10 WHAT DEPARTMENT DATA CODE (ST)

> This field can include test number, procedure number, drug code, item number, order number, etc. The contents of this field are determined by the contents of the previous field.

> When the AAIS queries the V*IST*A Surgery system, this field contains either the selected patient’s social security number (no dashes) or the words ALL.

<span id="_Toc93819521" class="anchor"></span>3.5.15 Segment: QRF - Query Filter

The QRF segment is used with the QRD segment to further refine the content of a query.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                           |
|-----|-----|-----|-----|-----|---------------------------|
| 1   | 20  | ST  | R   | Y   | WHERE SUBJECT FILTER      |
| 2   | 26  | TS  |     |     | WHEN DATA START DATE/TIME |
| 3   | 26  | TS  |     |     | WHEN DATA END DATE/TIME   |

<span id="_Toc93985521" class="anchor"></span>3.5.15.0 QRF field definitions

<span id="_Toc93985522" class="anchor"></span>3.5.15.1 WHERE SUBJECT FILTER (ST)

> This field identifies the department, system, or subsystem to which the query pertains.

> When the AAIS queries the V*IST*A Surgery system, this field contains  
> SURGERY.

<span id="_Toc93985523" class="anchor"></span>3.5.15.2 WHEN DATA START DATE/TIME (TS)

> Data representing dates and times equal or after this date should be included.

> When the AAIS queries the V*IST*A Surgery system, this field contains the date for which surgery cases are requested. Date without time is transmitted.

<span id="_Toc93819525" class="anchor"></span>3.5.15.3 WHEN DATA END DATE/TIME (TS)

> Data representing dates and times the same as or before this date should be included.

> When the AAIS queries the V*IST*A Surgery system, this field contains the date for which surgery cases are requested. The date used for WHEN DATA END DATE/TIME is the same as the date sent in WHEN DATA START DATE/TIME. Date without time is transmitted.

<span id="_Toc93819527" class="anchor"></span>3.5.16 Segment: ZCH - Schedule Appointment Information

This segment is based upon the proposed HL7 Scheduling chapter, which is under development. The ZCH segment contains general information about the scheduled appointment.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |     |                                |
|-----|-----|-----|-----|-----|--------------------------------|
| 1   | 22  | CM  | R   |     | PLACER SCHEDULE REQUEST ID     |
| 2   | 22  | CM  | C   |     | FILLER SCHEDULE REQUEST ID     |
| 3   | 22  | CM  | R   |     | PLACER GROUP NUMBER            |
| 4   | 200 | CE  | R   |     | EVENT REASON                   |
| 5   | 200 | CE  |     |     | APPOINTMENT REASON             |
| 6   | 20  | CQ  |     |     | APPOINTMENT DURATION           |
| 7   | 200 | TQ  | R   | Y   | APPOINTMENT TIMING QUANTITY    |
| 12  | 38  | CN  | R   |     | FILLER CONTACT PERSON          |
| 17  | 22  | CM  |     |     | PARENT FILLER SCHEDULE REQUEST |

<span id="_Toc93985526" class="anchor"></span>3.5.16.0 ZCH field definitions

<span id="_Toc93985527" class="anchor"></span>3.5.16.1 PLACER SCHEDULE REQUEST ID (CM)

> PLACER SCHEDULE REQUEST ID is a composite element made up of the  
> following:  
> \<unique placer schedule request number\> \<placer application ID\>  
> This field is the placer application’s permanent identifier for the appointment  
> request.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, all components are null.

<span id="_Toc93819531" class="anchor"></span>3.5.16.2 FILLER SCHEDULE REQUEST ID (CM)

> FILLER SCHEDULE REQUEST ID is a composite element made up of the  
> following:  
> \<unique filler schedule request number\> \<filler application ID\>  
> This field is the filler application’s permanent identifier for the appointment  
> request.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, only  
> the first component is included. It is the surgery case number as found in the  
> VISTA SURGERY file (#130).

  
<span id="_Toc93971332" class="anchor"></span>3.5.16.3 PLACER GROUP NUMBER (CM)

> PLACER GROUP NUMBER is a composite element made up of the following:  
> \<unique placer group number\> \<placer application ID\>  
> This field allows a placer application to group sets of appointment requests  
> together, and subsequently identify the group.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, all  
> components are null.

<span id="_Toc93819536" class="anchor"></span>3.5.16.4 EVENT REASON (CE)

> EVENT REASON is a coded element made up of the following:  
> \<identifier\> \<text\> \<name of coding system\>  
> This field may contain any code describing the reason the specific event is  
> occurring.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the following components are included. The identifier is the CASE STATUS value or event code. The text is the CASE STATUS description or trigger event. The text is capitalized and in parentheses. Name of coding system is L, or local. The following values can be expected.

> CASE STATUS

> Value Description

> S12 Notification of New Appointment Booking - includes all new requested, scheduled or emergent cases. (REQUESTED), (SCHEDULED), or (NOT COMPLETE)

> S13 Notification of Appointment Rescheduling - includes changing an existing case’s requested or scheduled date. (REQUESTED) or (SCHEDULED)

> S14 Notification of Appointment Modification - includes modifications to an existing case. (REQUESTED), (SCHEDULED), (NOT COMPLETE), (COMPLETE), or (ABORTED)

> S15 Notification of Appointment Cancellation - includes cancelling a scheduled operation. (CANCELLED)

> S17 Notification of Appointment Deletion - includes deleting a request or emergent case. (DELETED)

<span id="_Toc93819544" class="anchor"></span>3.5.16.5 APPOINTMENT REASON (CE)

> APPOINTMENT REASON is a coded element made up of the following:  
> \<identifier\> \<text\> \<name of coding system\>  
> This field contains the identifier code for the reason the appointment is to be  
> performed.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the  
> identifier contains the Surgery PRINCIPAL PROCEDURE CODE, which is the  
> CPT code for the principal procedure. The text is the short description for the  
> CPT code. The coding system component is C4, the standard CPT coding  
> method.

<span id="_Toc93819547" class="anchor"></span>3.5.16.6 APPOINTMENT DURATION (CQ)

> APPOINTMENT DURATION is a composite quantity with units made up of the following:

> \<quantity\> \<units\> This field contains the amount of time being requested for the appointment. The first component contains the duration amount. The units component contains a code describing the units of time used in expressing the quantity component.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the quantity contains the Surgery ESTIMATED CASE LENGTH.

<span id="_Toc93819550" class="anchor"></span>3.5.16.7 APPOINTMENT TIMING QUANTITY (TQ)

> APPOINTMENT TIMING QUANTITY is a quantity/timing field made up of the  
> following:  
> \<quantity\> \<interval\> \<duration\> \<start date/time\> \<end date/time\> \<priority\>  
> \<condition\> \<text\> \<conjunction\> \<order sequencing\>  
> This field describes the scheduled appointment’s timing and quantity, as  
> scheduled by the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, only  
> the start date/time, end date/time and order sequencing components are  
> included.

> For a scheduled case, the start date/time is the Surgery field SCHEDULED  
> START TIME (#10). For all other cases, the start date/time is the Surgery field  
> DATE OF OPERATION (#.09).

> For a scheduled case, the end date/time is the Surgery field SCHEDULED END  
> TIME (#11). For all other cases, the end date/time is null.

> The order sequencing component contains the Surgery field CASE SCHEDULE ORDER (#.037). This field contains the sequence in which the surgeon expects to do the case if the surgeon has more than one case scheduled for the day.

<span id="_Toc93819554" class="anchor"></span>3.5.16.12 FILLER CONTACT PERSON (CN)

> FILLER CONTACT PERSON is a composite ID number and name made up of the following:

> \<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\> \<prefix\> \<degree\> \<source table ID\> This field identifies the person responsible for the scheduling of the requested appointment.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the id number (social security number), uniquely identifies the person requesting or scheduling this operative procedure. The name component is from the Surgery field SURG SCHED PERSON (#1.099). All components must match the VISTA NEW PERSON file (#200).

<span id="_Toc93819557" class="anchor"></span>3.5.16.17 PARENT FILLER SCHEDULE REQUEST (CM)

> PARENT FILLER SCHEDULE REQUEST is a composite element made up of the following: \<unique filler schedule request number\> \<filler application ID\> This field relates a child to its parent, when a parent-child relationship exists. It contains the filler application’s permanent identifier for the parent of the appointment request.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the unique filler schedule request number is the Surgery field CONCURRENT CASE (#35). This is the patient’s concurrent case number. It identifies the operation, by case number, which is to occur at the same time by another surgical specialty.

<span id="_Toc93819559" class="anchor"></span>3.5.17 Segment: ZIG - Appointment Information - General Resource

> This segment is based upon the proposed HL7 Scheduling chapter, which is under development. The ZIG segment contains information about various types of resources that can be scheduled. Resources included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Resources described by this segment are general types of resources, such as equipment, which are identified by a simple identification code.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                        |
|-----|-----|-----|-----|------------------------|
| 1   | 80  | CE  | C   | RESOURCE ID            |
| 2   | 15  | CE  | R   | RESOURCE TYPE          |
| 3   | 20  | CQ  |     | START DATE/TIME OFFSET |
| 4   | 20  | CQ  |     | DURATION               |
| 6   | 10  | ID  | C   | FILLER STATUS CODE     |

<span id="_Toc93985537" class="anchor"></span>3.5.17.0 ZIG field definitions

<span id="_Toc93985538" class="anchor"></span>3.5.17.1 RESOURCE ID (CE)

> RESOURCE ID is a coded element made up of the following: \<resource identifier\> \<text\> \<name of coding system\> This field contains the ID number and name of the resource being requested or scheduled for an appointment. This field is used to identify a specific resource being requested, or a specific resource which has been scheduled for an appointment.

<span id="_Toc93819562" class="anchor"></span>3.5.17.2 RESOURCE TYPE (CE)

> RESOURCE TYPE is a coded element made up of the following:  
> \<type identifier\> \<text\> \<name of coding system\>  
> This field identifies the role of the resource requested/scheduled for this  
> appointment.

<span id="_Toc93819563" class="anchor"></span>3.5.17.3 START DATE/TIME OFFSET (CQ)

> START DATE/TIME OFFSET is a composite quantity with units made up of the following:

> \<quantity\> \<units\> This field contains the offset this resource is needed for the appointment, expressed in units of time relative to the scheduled start date/time. The first component contains the offset amount. An offset of zero (0), or an unvalued field indicates that the resource is required at the start date/time of the appointment. The units component contains a code describing the units of time used in expressing the quantity component.

> A positive offset indicates that the resource is required after the appointment’s start date/time. Specifying a negative offset indicates that the resource is required prior to the specified start date/time of the appointment.

<span id="_Toc93819566" class="anchor"></span>3.5.17.4 DURATION (CQ)

> DURATION is a composite quantity with units made up of the following: \<quantity\> \<units\> This field contains the duration for which the resource is requested/scheduled for this appointment, if different from the overall duration of the requested/scheduled appointment. The first component contains the duration amount. The units component contains a code describing the units of time used in expressing the quantity component.

<span id="_Toc93819568" class="anchor"></span>3.5.17.6 FILLER STATUS CODE (ID)

> FILLER STATUS CODE is a code that describes the requested/scheduled status of the resource or activity, from the point of view of the filler application. This field is required for all transactions from the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, this field contains CONFIRMED for a scheduled case and PENDING for a request.

User Defined Table - FILLER STATUS CODES

|           |                                                        |
|-----------|--------------------------------------------------------|
| Value     | Description                                            |
| PENDING   | Pending schedule confirmation; resource not scheduled. |
| CONFIRMED | This resource has been scheduled and                   |
|           | confirmed.                                             |

  
<span id="_Toc93971344" class="anchor"></span>3.5.18 Segment: ZIL - Appointment Information -Location Resource

This segment is based upon the proposed HL7 Scheduling chapter, which is under development. The ZIL segment contains information about location resources (meeting rooms, operating rooms, examination rooms, or other locations) that can be scheduled. Resources included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. Location resources are identified with this specific segment because of the specific encoding of locations used by the HL7 specification.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                        |
|-----|-----|-----|-----|------------------------|
| 1   | 80  | CM  | C   | LOCATION RESOURCE ID   |
| 2   | 15  | CE  | R   | LOCATION TYPE          |
| 3   | 20  | CQ  |     | START DATE/TIME OFFSET |
| 4   | 20  | CQ  |     | DURATION               |
| 6   | 10  | ID  | C   | FILLER STATUS CODE     |

<span id="_Toc93971345" class="anchor"></span>3.5.18.0 ZIL field definitions

<span id="_Toc93971346" class="anchor"></span>3.5.18.1 LOCATION RESOURCE ID (CM)

> LOCATION RESOURCE ID is a composite element made up of the following: \<facility id\> \<building\> \<department or nurse unit\> \<room\> \<bed\> This field contains the coded identification of the specific location being requested or scheduled for an appointment.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, only the facility id and room components are utilized. The facility id is the 3-digit identifier from the VISTA INSTITUTION file (#4). The fourth component, room, is the operating room scheduled.

<span id="_Toc93819575" class="anchor"></span>3.5.18.2 LOCATION TYPE (CE)

> LOCATION TYPE is a coded element made up of the following:  
> \<type identifier\> \<text\> \<name of coding system\>  
> This field identifies the role of the location requested/scheduled for this  
> appointment.

> When the VISTA Surgery system transmits to the AAIS or ancillary system, only the text component is utilized. The text component contains the words OPERATING ROOM or NON OR to identify the role of the LOCATION RESOURCE ID.  
> 3.5.18.3 START DATE/TIME OFFSET (CQ)

> START DATE/TIME OFFSET is a composite quantity with units made up of the following:

> \<quantity\> \<units\> This field contains the offset this location is needed for the appointment, expressed in units of time relative to the scheduled start date/time. The first component contains the offset amount. An offset of zero (0), or an unvalued field indicates that the location is required at the start date/time of the appointment. The units component contains a code describing the units of time used in expressing the quantity component.

> The V*IST*A Surgery system transmits a null value for this field.

<span id="_Toc93819581" class="anchor"></span>3.5.18.4 DURATION (CQ)

> DURATION is a composite quantity with units made up of the following: \<quantity\> \<units\> This field contains the duration for which the location is requested/scheduled for this appointment. The first component contains the duration amount. The units component contains a code describing the units of time used in expressing the quantity component.

> The V*IST*A Surgery system transmits a null value for this field.

<span id="_Toc93819584" class="anchor"></span>3.5.18.6 FILLER STATUS CODE (ID)

> FILLER STATUS CODE is a code that describes the requested/scheduled status of the location, from the point of view of the filler application. This field is required for all transactions from the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the value of this field is affected by the SCHEDULE CLOSE TIME field (#13) in the VISTA SURGERY SITE PARAMETERS file (#133). The field contains PENDING for a request and all scheduled cases which are not passed the SCHEDULE CLOSE TIME. This field contains CONFIRMED for all other cases.

User Defined Table - FILLER STATUS CODES

|           |                                             |
|-----------|---------------------------------------------|
| Value     | Description                                 |
| PENDING   | Pending schedule confirmation; resource not |
|           | scheduled.                                  |
| CONFIRMED | This resource has been scheduled and        |
|           | confirmed.                                  |

<span id="_Toc93819587" class="anchor"></span>

3.5.19 Segment: ZIP - Appointment Information -Personnel Resource

> This segment is based upon the proposed HL7 Scheduling chapter, which is under development. The ZIP segment contains information about the personnel types that can be scheduled. Personnel included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application. The types of personnel described on this segment are any healthcare provider in the institution controlled by a schedule (e.g., technicians, physicians, nurses, surgeons, anesthesiologists, or CRNAs).

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                    |
|-----|-----|-----|-----|--------------------|
| 1   | 80  | CN  | C   | RESOURCE ID        |
| 2   | 15  | CE  | R   | RESOURCE ROLE      |
| 6   | 10  | ID  | C   | FILLER STATUS CODE |

<span id="_Toc94060409" class="anchor"></span>3.5.19.0 ZIP field definitions

<span id="_Toc94060410" class="anchor"></span>3.5.19.1 RESOURCE ID (CN)

> RESOURCE ID is a composite ID number and name made up of the following:  
> \<id number\> \<family name\> \<given name\> \<middle initial or name\> \<suffix\>  
> \<prefix\> \<degree\> \<source table ID\>  
> This field contains the ID number and name of the person being requested or  
> scheduled for an appointment.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the  
> id number (social security number), uniquely identifies the resource person. The  
> name component is from the Surgery fields SURGEON (#.14), FIRST ASST  
> (#.15), SECOND ASST (#.16), ATTEND SURG (#.164), PRINC ANESTHETIST  
> (#.31), PROVIDER (#123), ATTEND PROVIDER (#124) or  
> ANESTHESIOLOGIST SUPVR (#.34). All components must match the VISTA  
> NEW PERSON file (#200).

<span id="_Toc93819591" class="anchor"></span>3.5.19.2 RESOURCE ROLE (CE)

> RESOURCE ROLE is a coded element made up of: \<role identifier\> \<text\> \<name of coding system\> This field identifies the role of the personnel requested/scheduled for this appointment. In requests, if a specific person is not identified in the RESOURCE ID field, then this field identifies the type of person that should be scheduled by the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the text component contains the role of the person identified in the RESOURCE ID. The text is SURGEON, 1ST ASST., 2ND ASST., ATT. SURGEON, PRIN. ANES., PROVIDER, ATT. PROVIDER, or ANES. SUPER. The coding system component is blank.

<span id="_Toc93819593" class="anchor"></span>3.5.19.6 FILLER STATUS CODE (ID)

> FILLER STATUS CODE is a code that describes the requested/scheduled status of the resource, from the point of view of the filler application. This field is required for all transactions from the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the value of this field is affected by the SCHEDULE CLOSE TIME field (#13) in the VISTA SURGERY SITE PARAMETERS file (#133). The field contains PENDING for a request and all scheduled cases which are not passed the SCHEDULE CLOSE TIME. This field contains CONFIRMED for all other cases.

User Defined Table - FILLER STATUS CODES

|           |                                             |
|-----------|---------------------------------------------|
| Value     | Description                                 |
| PENDING   | Pending schedule confirmation; resource not |
|           | scheduled.                                  |
| CONFIRMED | This resource has been scheduled and        |
|           | confirmed.                                  |

<span id="_Toc93819596" class="anchor"></span>3.5.20 Segment: ZIS - Appointment Information - Service

> This segment is based upon the proposed HL7 Scheduling chapter, which is under development. The ZIS segment contains information about various types of services that can be scheduled. Services included in a transaction using this segment are assumed to be controlled by a schedule on a schedule filler application.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|                                                                              |     |     |     |                              |
|------------------------------------------------------------------------------|-----|-----|-----|------------------------------|
| 1                                                                            | 200 | CE  | R   | UNIVERSAL SERVICE IDENTIFIER |
| 5                                                                            | 10  | ID  | C   | FILLER STATUS CODE           |
| <span id="_Toc93971356" class="anchor"></span>3.5.20.0 ZIS field definitions |     |     |     |                              |

<span id="_Toc93819598" class="anchor"></span>3.5.20.1 UNIVERSAL SERVICE IDENTIFIER (CE)

> UNIVERSAL SERVICE IDENTIFIER is a coded element made up of the following: \<identifier\> \<text\> \<name of coding system\> This is the identifier code for the service to be scheduled. This field may contain a Universal Service Identifier describing the observation/test/battery/procedure or other activity that is to be performed during the requested appointment. This can be based on local and/or universal codes.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the identifier component is the OTHER PROCEDURE CPT CODE field (#3 of Subfile \#130.16). The text component is the short description from the CPT file (#81). The coding system component is C4.

<span id="_Toc93819601" class="anchor"></span>3.5.20.5 FILLER STATUS CODE (ID)

> FILLER STATUS CODE is a code that describes the requested/scheduled status of the resource or activity, from the point of view of the filler application. This field is required for all transactions from the filler application.

> When the V*IST*A Surgery system transmits to the AAIS or ancillary system, the value transmitted is based upon the Surgery COMPLETED field (#2 of Subfile \#130.16).

User Defined Table - FILLER STATUS CODES

|           |                                             |
|-----------|---------------------------------------------|
| Value     | Description                                 |
| PENDING   | Pending schedule confirmation; resource not |
|           | scheduled.                                  |
| CONFIRMED | This resource has been scheduled and        |
|           | confirmed.                                  |

<span id="_Toc93819604" class="anchor"></span>3.5.21 Segment: ZI9 - ICD9 Identification

This segment is used to identify all of the ICD9 codes with their corresponding short name.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |     |                           |
|-----|-----|-----|-----|---------------------------|
| 1   | 60  | CE  |     | ZI9 - PRIMARY KEY VALUE   |
| 2   | 5   | ST  | R   | ICD9 CODE (#80/.01)       |
| 3   | 30  | ST  |     | DIAGNOSIS (#80/3)         |
| 4   | 1   | ID  |     | ACTIVE/INACTIVE (#80/100) |

<span id="_Toc94060418" class="anchor"></span>3.5.21.0 ZI9 - field definition

<span id="_Toc94060419" class="anchor"></span>3.5.21.1 ZI9 - PRIMARY KEY VALUE (CE)

> This field contains the primary key value from the MFE-4 - PRIMARY KEY VALUE field.

<span id="_Toc93819607" class="anchor"></span>3.5.21.2 ICD9 CODE (ST)

> This field contains the identification or ICD9 code, which comes from the V*IST*A ICD9 file (#80).

<span id="_Toc93819609" class="anchor"></span>3.5.21.3 DIAGNOSIS (ST)

> This field contains the actual diagnosis name specified by the standard and identified from within the V*IST*A ICD9 file (#80).

<span id="_Toc93819610" class="anchor"></span>3.5.21.4 ACTIVE/INACTIVE (ID)

> This field contains the current status of the ICD9 code identified in the primary key.

Table 183 - ACTIVE/INACTIVE

|       |               |             |
|-------|---------------|-------------|
| Value |               | Description |
| A     | Active code   |             |
| I     | Inactive code |             |

<span id="_Toc94060423" class="anchor"></span>3.5.22 Segment: ZMN - Monitor Identification

This segment is used to identify all of the monitors used by the V*IST*A Surgery package.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

1 60 CE ZMN - PRIMARY KEY VALUE (#133.4/.01)

2 1 ID INACTIVE FLAG (#133.4/10)

<span id="_Toc94060424" class="anchor"></span>3.5.22.0 ZMN - field definition

<span id="_Toc94060425" class="anchor"></span>3.5.22.1 ZMN - PRIMARY KEY VALUE (CE)

> This field contains the primary key value from the MFE-4 - PRIMARY KEY VALUE field.

<span id="_Toc93819614" class="anchor"></span>3.5.22.2 ACTIVE/INACTIVE (ID)

> This field contains the current status of the monitor identified in the primary key.

Table 183 - ACTIVE/INACTIVE

|       |               |             |
|-------|---------------|-------------|
| Value |               | Description |
| A     | Active code   |             |
| I     | Inactive code |             |

3.5.23 Segment: ZRF - Replacement Fluid Identification

This segment is used to identify all of replacement fluids used by the V*IST*A Surgery package.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |                                      |             |
|-----|-----|-----|--------------------------------------|-------------|
| 1   | 60  | CE  | ZRF - PRIMARY KEY VALUE (#133.7/.01) |             |
| 2   | 1   | ID  | ACTIVE/INACTIVE                      | (#133.7/10) |

<span id="_Toc94060427" class="anchor"></span>3.5.23.0 ZRF - field definitions

<span id="_Toc93819617" class="anchor"></span>3.5.23.1 ZRF - PRIMARY KEY VALUE (CE)

> This field contains the primary key value from the MFE-4 - PRIMARY KEY VALUE field.

<span id="_Toc93819618" class="anchor"></span>3.5.23.2 ACTIVE/INACTIVE (ID)

> This field contains the current status of the replacement fluid identified in the primary key.

Table 183 - ACTIVE/INACTIVE

|       |               |             |
|-------|---------------|-------------|
| Value |               | Description |
| A     | Active code   |             |
| I     | Inactive code |             |

<span id="_Toc94060430" class="anchor"></span>3.5.24 Segment: ZRX - Medication Identification

This segment is used to identify all of medications used by the V*IST*A Surgery package.

SEQ LEN DT R/O RP/# TBL# ELEMENT NAME

|     |     |     |                                   |
|-----|-----|-----|-----------------------------------|
| 1   | 60  | CE  | ZRX - PRIMARY KEY VALUE (#50/.01) |
| 2   | 26  | CM  | INACTIVE DATE (#50/100)           |
|     |     |     |                                   |

<span id="_Toc94060431" class="anchor"></span>3.5.24.0 ZRF - field definitions

<span id="_Toc93819621" class="anchor"></span>3.5.24.1 ZRX - PRIMARY KEY VALUE (CE)

> This field contains the primary key value from the MFE-4 - PRIMARY KEY VALUE field.

<span id="_Toc93819623" class="anchor"></span>3.5.24.2 INACTIVE DATE (CM)

> Components: \<date (TS)\>\<institution name (CE)\>

> This field identifies the date the medication became inactive for an institution. Note that the CE component of this field uses the subcomponent character for its delimiters.

<span id="_Toc93819625" class="anchor"></span>4. TRANSACTION SPECIFICATIONS

<span id="_Toc93819626" class="anchor"></span>4.1 General

The interface between V*IST*A and an automated anesthesia information system (AAIS) or ancillary system is a two-phased project. Phase I of this specification addresses only the data that is readily available from the V*IST*A Surgery application. It is recognized that an AAIS or ancillary system can utilize laboratory, pharmacy, radiology and other V*IST*A data. The specification will be expanded in Phase II to address those needs.

The flow of transactions between the V*IST*A Surgery system and the automated anesthesia information system (AAIS) or ancillary system occurs in the following ways.

The V*IST*A Surgery system notifies the AAIS or ancillary system when a surgical case is requested, scheduled, cancelled, deleted, aborted, not complete (in progress) or completed. The receiving system responds with an acknowledgment.

The AAIS or ancillary system can query the V*IST*A Surgery system for pre­operative surgical data for one patient/date or for all cases for a date. The V*IST*A Surgery system responds with the appropriate information.

At the conclusion or during the operative procedure, the AAIS or ancillary system sends case-related data back to the V*IST*A Surgery system, and the V*IST*A Surgery system responds with an acknowledgment and visa-versa.

In order to synchronize common reference files on both systems, the V*IST*A Surgery package has created master file updates for several files and sets of codes.

<span id="_Toc93819633" class="anchor"></span>4.2 Specific Transactions

<span id="_Toc93819634" class="anchor"></span>A. Surgery Trigger Events

The following are surgery trigger events: a surgical case is requested, scheduled, cancelled, deleted, aborted, not complete (in progress) or completed. A trigger event causes the V*IST*A Surgery system to send an unsolicited update to the AAIS or ancillary system. This message is in the form of a scheduled information unsolicited (ZIU) message. The ZIU message consists of the following segments.

ZIU Schedule Information Unsolicited Message

MSH Message Header

{ZCH Schedule Appointment Information

PID Patient Identification

\[{AL1}\] Allergy Information

\[{OBX}\] Observation Segment

\[{DG1}\] Diagnosis Information

\[{ZIS}\] Appointment Information - Service

\[{ZIG}\] Appointment Information - General Resource

\[{ZIL}\] Appointment Information - Location Resource

\[{ZIP}\] Appointment Information - Personnel Resource

}

<u>EXAMPLE \#1: S12 - Notification of New Appointment Booking - Requested</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208092934^^ZIU^2941208. 092934^P^2.1 ZCH^^1887^^S12~(REQUESTED)~L^^^\~\~~2941209^^^^^000999991~SURSURGEON~ONE^^^^^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^3^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^4^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^5^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^6^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^PENDING

<u>EXAMPLE \#2: S13 - Notification of Appointment Rescheduling - Scheduled</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208095332^^ZIU^2941208. 095332^P^2.1 ZCH^^1887^^S13~(SCHEDULED)~L^47480~INCISION OF GALLBLADDER ~C4^165~min^\~\~~2941209^^^^^000999991~SURSURGEON~ONE^^^^^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^3^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^4^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^5^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~ SURNURSE~ONE OBX^6^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE DG1^0001^I9^574.01^CHOLELITH/AC GB INF-OBST^^P AL1^0001^FA^~DAIRY PRODUCTS ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^PENDING ZIP^000345678~SURSURGEON~THREE^~1ST ASST.~ ^^^^PENDING ZIP^000567009~SURSURGEON~FIVE^~ATT. SURGEON~^^^^PENDING ZIP^000456789~SURANESTHETIST~ONE^~PRIN. ANES.~ ^^^^PENDING ZIP^000122344~SURANESTHETIST~TW0^~ANES. SUPER.~ ^^^^PENDING

<u>  
EXAMPLE \#3: S14 - Notification of Appointment Modification - Requested</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208093730^^ZIU^2941208. 09373^P^2.1 ZCH^^1887^^S14~(REQUESTED)~L^47480~INCISION OF GALLBLADDER ~C4^165~min^\~\~~2941209^^^^^000999991~SURSURGEON~ONE^^^^^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^3^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^4^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^5^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^6^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE DG1^0001^I9^574.01^CHOLELITH/AC GB INF-OBST^^P AL1^0001^FA^~DAIRY PRODUCTS ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^PENDING ZIP^000345678~SURSURGEON~THREE^~1ST ASST.~ ^^^^PENDING ZIP^000567009~SURSURGEON~FIVE^~ATT. SURGEON~^^^^PENDING

<u>EXAMPLE \#4: S14 - Notification of Appointment Modification - Scheduled</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208094653^^ZIU^2941208. 094653^P^2.1 ZCH^^1887^^S14~(SCHEDULED)~L^47480~INCISION OF GALLBLADDER~C4 ^165~min^\~\~~199412091300~199412091545\~\~\~\~~1^^^^^000999991~SURSURGEON~ONE^^^^ ^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^3^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^4^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^5^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^6^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE DG1^0001^I9^574.01^CHOLELITH/AC GB INF-OBST^^P AL1^0001^FA^~DAIRY PRODUCTS ZIS^11100~BIOPSY OF SKIN LESION~C4^^^^ CONFIRMED ZIG^5~ECG~99VA133.4^~MONITOR~^^^^CONFIRMED ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^CONFIRMED ZIP^000345678~SURSURGEON~THREE^~1ST ASST.~ ^^^^CONFIRMED ZIP^000567009~SURSURGEON~FIVE^~ATT. SURGEON~^^^^CONFIRMED ZIP^000456789~SURANESTHETIST~ONE^~PRIN. ANES.~ ^^^^CONFIRMED ZIP^000122344~SURANESTHETIST~TW0^~ANES. SUPER.~ ^^^^CONFIRMED ZIL^521\~\~~OR1^~OPERATING ROOM^^^^CONFIRMED

<u>EXAMPLE \#5: S15 - Notification of Appointment Cancellation</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208095316^^ZIU^2941208. 095316^P^2.1 ZCH^^1887^^S15~(CANCELLED)~L^47480~INCISION OF GALLBLADDER~C4 ^165~min^\~\~~2941208^^^^^000999991~SURSURGEON~ONE^^^^^

PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~CANCEL REASON~L^^~BLOOD NOT AVAILABLE~L^^^^^ ^S^^^199412080936^^000289123~SURNURSE~ONE OBX^3^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^4^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^5^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^6^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^7^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE DG1^0001^I9^574.01^CHOLELITH/AC GB INF-OBST^^P AL1^0001^FA^~DAIRY PRODUCTS ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^PENDING ZIP^000345678~SURSURGEON~THREE^~1ST ASST.~ ^^^^PENDING ZIP^000567009~SURSURGEON~FIVE^~ATT. SURGEON~^^^^PENDING ZIP^000456789~SURANESTHETIST~ONE^~PRIN. ANES.~ ^^^^PENDING ZIP^000122344~SURANESTHETIST~TW0^~ANES. SUPER.~ ^^^^PENDING

<u>EXAMPLE \#6: S17 - Notification of Appointment Deletion</u>

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941208133341^^ZIU^2941208. 133341^P^2.1 ZCH^^1889^^S17~(DELETED)~L^^0~min^\~\~~2941208^^^^^^^^^^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^2^CE^~SURGICAL SPECIALTY~^^~CARDIAC SURGERY~99VA137.45^^ ^^^^S^^^^^ OBX^3^CE^1010.3~Height^^226.06^cm^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^4^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199412080700^ ^000289123~SURNURSE~ONE OBX^5^CE^1000~Temperature^^36.94^cel^^^^^S^^^199412080700^^000289123~SURNURSE~ONE OBX^6^CE^1006.2~HR^^60^min^^^^^S^^^199412080700^^000289123~SURNURSE~ONE DG1^0001^I9^540.9^ACUTE APPENDICITIS NOS^^P AL1^0001^FA^~DAIRY PRODUCTS ZIP^000567009~SURSURGEON~FIVE^~SURGEON~^^^^CONFIRMED ZIP^000345678~SURSURGEON~THREE^~1ST ASST.~^^^^CONFIRMED ZIP^000233455~SURSURGEON~SIX^~2ND ASST.~^^^^CONFIRMED ZIP^000234567~SURSURGEON~TWO^~ATT. SURGEON~^^^^CONFIRMED

<span id="_Toc93819637" class="anchor"></span>B. Message Acknowledgment

Upon receipt of the scheduled information unsolicited (ZIU) message, the AAIS or ancillary system responds with a general acknowledgment (ACK) message. The ACK message consists of the following segments.

ACK General Acknowledgment Message

MSH Message Header

MSA Message Acknowledgment

<u>EXAMPLE:</u>

MSH^~\|\\^SR AAIS^521^SR SURGERY^521^19941208133422^^ACK^19941208 .133422^P^2.1 MSA^AA^2941208.133341^

<span id="_Toc93819640" class="anchor"></span>C. Query for Pre-operative Surgical Data

The AAIS or ancillary system requests pre-operative surgical data for a single specified case/date or for all cases for a specified date. This request is in the form of a query (QRY) message. The QRY message consists of the following segments.

QRY Query Message

MSH Message Header

QRD Query Definition

QRF Query Filter

<u>EXAMPLE \#1: All Scheduled Cases for Selected Date</u>

MSH^~\|\\^SR AAIS^521^SR SURGERY^521^19941012140634^^QRY^2941012.  
140634^P^2.1  
QRD^19941012140634^R^I^0000^^^1~RD^ALL ^OTH^ALL^^  
QRF^SR SURGERY^19940930^19940930^^^^^

<u>EXAMPLE \#2: Selected Patient for Selected Date</u>

MSH^~\|\\^SR AAIS^521^SR SURGERY^521^19941012140634^^QRY^2941012. 140634^P^2.1 QRD^19941012140634^R^I^0000^^^1~RD^SURPATIENT~ONE^OTH^000381876^^ QRF^SR SURGERY^19940930^19940930^^^^^

<span id="_Toc93819646" class="anchor"></span>D. Respond with Requested Query Information

The V*IST*A Surgery system responds to the query with a scheduled activity transaction (ZSQ) message containing the requested information. The ZSQ message consists of the following segments.

<u>ZSQ Scheduled Activity Transaction Message</u>

MSH Message Header

MSA Message Acknowledgment

\[ERR\] Error

\[{ZCH Schedule Appointment Information

> PID Patient Identification

> \[AL1\] Allergy Information

> \[OBX\] Observation Segment

> \[DG1\] Diagnosis Information

> \[{ZIS}\] Appointment Information - Service

> \[{ZIG}\] Appointment Information - General Resource

> \[{ZIP}\] Appointment Information - Personnel Resource

> \[{ZIL}\] Appointment Information - Location Resource

}\]

EXAMPLE:

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19941012141231^^ZSQ^2941012. 141231^P^2.1 MSA^AA^2941012.140634^ ZCH^^163^^^27130~TOTAL HIP REPLACEMENT~C4^0~min^\~\~~199409290800 ~199409280920\~\~\~\~~^^^^^000999991~SURSURGEON~ONE^^^^^ PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBX^1^CE^~SURGICAL SPECIALTY~^^~ORTHOPEDIC~99VA723^^^^^^S^ ^^^^ OBX^2^CE^~ANES SUPERVISE CODE~L^^2^^^^^^S^^^^^ OBX^3^CE^~PATIENT CLASS ~L^^~INPATIENT~L^^^^^^S OBX^4^TX^1002~BP~AS4^^70/110^^^^^^S^^^199409270900^^000289123~SURNURSE~ONE OBX^5^CE^1010.3~Height~AS4^^100.08^cm^^^^^S^^^199409270900^^000289123~REED~DAN NY OBX^6^CE^1010.1~Body Weight~AS4^^93.00^kg^^^^^S^^^199409270900^^ 000289123~SURNURSE~ONE OBX^7^CE^1000~Temperature~AS4^^28.39^cel^^^^^S^^^199409270900^^000289123~REED~ DANNY OBX^8^CE^1006.2~HR~AS4^^60^min^^^^^S^^^199409270900^^000289123~SURNURSE~ONE DG1^0001^I9^100.0^LEPTOSPIROS ICTEROHEM^^P AL1^0001^FA^~DAIRY PRODUCTS ZIS^11000~SURGICAL CLEANSING OF SKIN~C4^^^^CONFIRMED ZIS^11100~BIOPSY OF SKIN LESION~C4^^^^CONFIRMED

ZIG^5~ECG~99VA133.4^~MONITOR~^^^^CONFIRMED ZIP^000234567~SURSURGEON~TWO^~SURGEON~^^^^CONFIRMED ZIP^000345678~SURSURGEON~THREE ^~1ST ASST.~^^^^CONFIRMED ZIP^000567009~SURSURGEON~FIVE ^~2ND ASST.~^^^^CONFIRMED ZIP^000999991~SURSURGEON~ONE^~ATT. SURGEON~^^^^CONFIRMED ZIP^000456789~SURANESTHETIST~ONE ^~PRIN. ANES.~^^^^CONFI

RMED

ZIL^BIRMINGHAM, AL.\~\~~OR1^~OPERATING ROOM^^^^CONFIRMED

.

.

.

ZCH^""^1992^""^~(NOT COMPLETE)~L^30620~INTRANASAL RECONSTRUCTION~C4^^\~\~~19950608\~\~\~\~\~~^^^^^^^^^^ PID^1^^71~8~M10^1876^SURPATIENT~ONE^""^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555^^555-5555^^^S^^^000381876 OBX^1^CE^~MEDICAL SPECIALTY~^^~ORTHOPEDIC~99VA723^^^^^^S OBX^2^CE^~ANES SUPERVISE CODE~L^^2^^^^^^S^^^^^ OBX^3^CE^~PATIENT CLASS~^^~OUTPATIENT~L^^^^^^S^^^^^ OBX^4^CE^1010.3~Height^^226.06^cm^^^^^S^^^199505020700^^000289123~SURNURSE~ONE OBX^5^CE^1010.1~Body Weight^^70.45^kg^^^^^S^^^199505020700^ ^000289123~SURNURSE~ONE OBX^6^CE^1000~Temperature^^36.94^cel^^^^^S^^^199505020700^^000289123~SURNURSE~ONE OBX^7^CE^1006.2~HR^^60^min^^^^^S^^^199505020700^^000289123~SURNURSE~ONE DG1^0001^I9^802.1^NASAL BONE FX-OPEN^^P AL1^0001^FA^~DAIRY PRODUCTS ZIS^00160~ANESTH, NOSE, SINUS SURGERY~C4^^^^PENDING ZIP^000456801~SURPROVIDER~ONE^~PROVIDER~^^^^

ZIP^000289123~SURNURSE~ONE^~ATTEND PROVIDER~^^^^CONFIRMED

ZIP^~SURANESTHETIST~TWO^~PRIN. ANES.~ ^^^^CONFIRMED ZIP^000456789~SURANESTHETIST~ONE^~ANES. SUPER.~^ ^^CONFIRMED

ZIL^521\~\~~HUFF CLINIC^~NON OR^^^^CONFIRMED

. . .

Segments ZCH through ZIL repeat for every case scheduled on the requested date.

<span id="_Toc93819650" class="anchor"></span>E. Message Acknowledgment

Upon receipt of the scheduled activity transaction (ZSQ) message, the message response process is complete.

<span id="_Toc93819652" class="anchor"></span>F. Unsolicited Update at Procedure Conclusion

At the conclusion of the operative procedure, the AAIS or ancillary system sends an unsolicited update to the V*IST*A Surgery system in the form of an observational results unsolicited (ORU) message. The ORU message consists of the following segments.

|              |         |                                           |
|--------------|---------|-------------------------------------------|
| ORU          |         | Observational Results Unsolicited Message |
| MSH          |         | Message Header                            |
| {            | \[PID\] | Patient Identification                    |
|              | {OBR    | Observations Report ID                    |
| {\[NTE\]}    |         | Anesthesia Notes or Comments              |
| {\[OBX\]}    |         | Observation Segment                       |
| }            |         |                                           |
| }            |         |                                           |
| EXAMPLE: |         |                                           |

MSH^~\|\\^SR AAIS^521^SR SURGERY^521^19950120130126^^ORU^2950120

.13^P^2.1

PID^0001^^71~8~M10^1876^SURPATIENT~ONE^^19580903^M^^^87 ANYPLACE STREET\~~ANYTOWN~AL~55555~USA^^555-5555^^^S^^^000381876 OBR^0001^^1935^5000.7~OPERATION~AS4^^^1995011107^199501110823

OBX^1^TS^~NURSE PRESENT TIME~L^^199501110658^^^^^^F

OBX^2^CN^~ASSISTANT ANESTHETIST~99VA200^^000456789~ SURANESTHETIST ~ONE^^^^^^F

OBX^3^NM^~BLOOD LOSS~L^^10^ml^^^^^F

OBX^4^CE^1000~ANESTHESIA TEMP~AS4^^10^cel^^^^^F

OBX^5^CE^~ASA CLASS~L^^~1E-NO DISTURB-EMERG~L^^^^^^F

OBX^6^TS^~TIME PATIENT IN HOLDING AREA~L^^199501110615^^^^^^F OBX^7^TS^~ANESTHESIA AVAILABLE TIME~L^^199501110659^^^^^^F

OBX^8^TS^~SURGEON PRESENT TIME~L^^199501110708^^^^^^F

OBX^9^TS^~ANESTHESIA CARE START TIME~L^^199501110659^^^^^^F OBX^10^TS^~ANESTHESIA CARE END TIME~L^^199501110710^^^^^^F OBX^11^TS^~INDUCTION COMPLETE~L^^199501110701^^^^^^F

OBX^12^TS^~TIME PATIENT IN OR~L^^1995011107^^^^^^F

OBX^13^TS^~TIME PATIENT OUT OR~L^^199501110830^^^^^^F

OBX^14^CN^~PRIN. ANES.~99VA200^^000289123~SURNURSE~ONE^^^^^^F OBX^15^CN^~RELIEF ANESTHETIST~99VA200^^000667889~SURANESTHETIST~THREE

LAS A^^^^^^F

OBX^16^CN^~ANES. SUPER.~99VA200^^000122344~SURANESTHETIST~TW0^^^^^^F OBX^17^NM^~TOTAL URINE OUTPUT~L^^3^ml^^^^^F

OBX^18^NM^~OR SETUP TIME~L^^150^min^^^^^F

OBX^19^NM^1006.2~HR~AS4^^100^^^^^^F

OBX^20^NM^1007~RR~AS4^^80^min^^^^^F

OBX^21^TX^1002~BP~AS4^^80/120^^^^^^F

OBX^22^CE^~CASE SCHEDULE TYPE~L^^~ELECTIVE~L^^^^^^F

OBX^23^CE^~ATTENDING CODE~L^^~0. STAFF ALONE~L^^^^^^F OBR^0002^^1935^~TOURNIQUET~L^^^199501110723^199501110726

OBX^1^CE^~SITE TOURNIQUET APPLIED~L\~~RIGHT UPPER LEG~L^ ^100^m(hg)^^^^^F^^^^^000999991~SURSURGEON~ONE

OBR^0003^^1935^~REPLACEMENT FLUID~L

OBX^1^CE^~REPLACEMENT FLUID USED~L\~~PLATELETS~99VA133.7^ ^200^ml^^^^^F OBR^0004^^1935^~MONITOR~L\~~ECG~99VA133.4^^^199501110700^199501110722 OBX^1^CE^~MONITOR APPLIED BY~L^^000999991~SURSURGEON~ONE ^^^^^^F OBR^5^^1935^~MEDICATION~L\~~FLUOROURACIL 5% TOP.SOL. ~99VA50^^^ 199501110723^^^^^^^^^000999991~SURSURGEON~ONE

OBX^1^TX^~MEDICATION USED~L^^10^^^^^^F^^^^^000999991~ SURSURGEON~ONE

OBX^2^CE^~MEDICATION ROUTE~L^^~INTRAVENOUS~L^^^^^^F OBR^6^^1935^5000.8~ANESTHESIA~AS4\~~GENERAL~L NTE^1^P^The first line of anesthesia comments up to 80 characters long NTE^2^P^and the start of the second line of anesthesia comments.

OBX^1^CE^~PRINCIPAL ANES TECHNIQUE (Y/N)~L^^~YES~L^^^^^^F

OBX^2^CE^~EPIDURAL METHOD~L^^~HANGING DROP~L^^^^^^F

OBX^3^CE^~ANESTHESIA AGENT~L\~~ENFLURANE 125ML~99VA50^^25^ml ^^^^^F OBX^4^CN^~EXTUBATED BY~99VA200^^151234567~ SURSURGEON~ONE ^^^^^^F OBX^5^CE^~PATIENT STATUS~L^^~SEDATED~L^^^^^^F

OBX^6^CE^~ANESTHESIA ROUTE~L^^~ORAL~L^ ^ ^ ^ ^ ^F

OBX^7^CE^~ANESTHESIA APPROACH~L^^~RAPID SEQUENCE~L^^^^^^F OBX^8^CE^~LARYNGOSCOPE TYPE~L^^~MILLER~L^^^^^^F

OBX^9^NM^~LARYNGOSCOPE SIZE~L^^30^^^^^^F

OBX^10^CE^~TUBE TYPE~L^^~PVC LOW PRESSURE~L^^^^^^F

OBX^11^NM^~TUBE SIZE~L^^40^^^^^^F

OBX^12^NM^~END VENT TV~L^^1000^^^^^^F

OBX^13^NM^~END VENT RATE~L^^900^^^^^^F

OBX^14^CE^~EXTUBATED IN~L^^~OR~L^^^^^^F OBX^15^CE^~BARICITY~L^^~HYPERBARIC~L^^^^^^F

OBX^16^CE^~ADMINISTRATION METHOD~L^^~BOLUS~L^^^^^^F

OBX^17^NM^~TEST DOSE~L\~~GENTAMICIN~99VA50^^20^^^^^^F

<span id="_Toc93819653" class="anchor"></span>G. Message Acknowledgment

Upon receipt of the unsolicited update, the V*IST*A Surgery system responds with a general acknowledgment (ACK) message. The ACK message consists of the following segments.

|          |                                |
|----------|--------------------------------|
| ACK      | General Acknowledgment Message |
| MSH      | Message Header                 |
| MSA      | Message Acknowledgment         |
| EXAMPLE: |                                |

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19950310145754^^ACK^2950310.  
145754^P^2.1  
MSA^AA^2950120.13^

<span id="_Toc93819655" class="anchor"></span>H. Synchronize Reference Files

The V*IST*A Surgery system will send Master File Update messages to initialize and update the AAIS. The MFN message consists of the following segments.

MFN Master File Notification Message

<u>MFN Master File Notification</u>

MSH Message Header

MFI Master File Identification

{MFE Master File Entry

\[Z..\] } Data for the entry identified in MFE

(STF,ZI9,ZRX,ZMN,ZRF)

EXAMPLE:

MSH^~\|\\^SR SURGERY^521^SR AAIS^521^19950523083809^^MFN^2950523.083809^D^2.1 MFI^~MONITOR~99VA133.4^^REP^^^AL MFE^MAD^1^19950523^~AUSCULTATORY NIBP~ ZMN^~AUSCULTATORY NIBP~^0 MFE^MAD^2^19950523^~CHEST STETHOSCOPE~ ZMN^~CHEST STETHOSCOPE~^0 MFE^MAD^3^19950523^~DOPPLER NIBP~

> .  
> .  
> .

MFE^MAD^27^19950523^~MYOCARDIAL PH~ ZMN^~MYOCARDIAL PH~^0 MFE^MAD^28^19950523^~ARP~ ZMN^~ARP~^0

<span id="_Toc93819660" class="anchor"></span>I. Message Acknowledgment of Master File Update

Upon receipt of a Master File update, the AAIS or ancillary system should respond with a Master File Application Acknowledgment (MFK) message. The MFK message consists of the following segments.

|              |        |     |                                         |
|--------------|--------|-----|-----------------------------------------|
| MFK          |        |     | Master File Application Acknowledgement |
| MSH          |        |     | Message Header                          |
| MSA          |        |     | Acknowledgement                         |
| \[           | ERR \] |     | Error                                   |
| MFI          |        |     | Master File Identification              |
| { \[MFA\]    |        | }   | Master File ACK segment                 |
| EXAMPLE: |        |     |                                         |

MSH^~\|\\^SR AAIS^521^SR SURGERY^521^19950516084643^^MFK^2950516.084643^D^2.1 MSA^AA^2950516.084643

MFI^~MONITOR ~99VA133.4^^REP^^^AL

MFA^MAD^^^S^~AUSCULTATORY NIBP~

MFA^MAD^^^S^~CHEST STETHOSCOPE~

MFA^MAD^^^S^~DOPPLER NIBP~

> .  
> .  
> .

MFA^MAD^^^S^~MYOCARDIAL PH~ MFA^MAD^^^S^~ARP~

<span id="_Toc94060446" class="anchor"></span>APPENDIX A: DATA SOURCESV*IST*A Surgery to AAIS and Ancillary Systems

|                                   |                         |                                         |
|-----------------------------------|-------------------------|-----------------------------------------|
| APPENDIX A: DATA SOURCES Data | Segment/Sequence \# | V*IST*A Mapping                     |
| Demographic Data:             |                         |                                         |
| Patient ID                        | PID-3                   | SURGERY file (#130), .01 field: PATIENT |
| Patient SSN                       | PID-19                  | VAFHLPID call                           |
| Alternate Patient ID              | PID-4                   | VAFHLPID call                           |
| Patient Name (L, F, M)            | PID-5                   | VAFHLPID call                           |
| Mother's Maiden Name              | PID-6                   | VAFHLPID call                           |
| Sex                               | PID-8                   | VAFHLPID call                           |
| Date of Birth                     | PID-7                   | VAFHLPID call                           |
| Race                              | PID-10                  | VAFHLPID call                           |
| Patient Address                   | PID-11                  | VAFHLPID call                           |
| Home Phone Number                 | PID-13                  | VAFHLPID call                           |
| Marital Status                    | PID-16                  | VAFHLPID call                           |
| Religion                          | PID-17                  | VAFHLPID call                           |
| Surgery Case Number               | ZCH-2                   | SURGERY file (#130), IEN                |
| Operating Room                    | ZIL-1 and 2             | Surgery field: OPERATING ROOM (#.09)    |
| Hospital Station Number           | MSH-4 and 6             | VISTA INSTITUTION file (#4) entry       |

  
V*IST*A Surgery to AAIS and Ancillary Systems

|                                                  |                         |                                                                                                             |
|--------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Data                                         | Segment/Sequence \# | V*IST*A Mapping                                                                                         |
| Scheduling Information:                      |                         |                                                                                                             |
| Allergies                                        | AL1-2 and 3             | GMRADPT call                                                                                                |
| Latest Preoperative Blood Pressure, Time Stamped | OBX-3, 5, 6 and 14      | GMRVUTL call                                                                                                |
| Latest Preoperative Pulse Rate, Time Stamped     | OBX-3, 5, 6 and 14      | GMRVUTL call                                                                                                |
| Latest Preoperative Temperature, Time Stamped    | OBX-3, 5, 6 and 14      | GMRVUTL call                                                                                                |
| Preoperative Weight                              | OBX-3, 5, 6 and 14      | GMRVUTL call                                                                                                |
| Height                                           | OBX-3, 5, 6 and 14      | GMRVUTL call                                                                                                |
| Principal Diagnosis                              | DG1-3 and 6             | Surgery field: PRIN DIAGNOSIS CODE (#66)                                                                    |
| Other Preoperative Diagnosis                     | DG1-3 and 6             | Surgery field: OTHER PREOP DIAGNOSIS (#.01 of Subfile \#130.17)                                             |
| ICD9 Diagnosis Description                       | DG1-4                   | Surgery field: ICD DIAGNOSIS CODE (#3 of Subfile \#130.17)                                                  |
| Scheduled Procedure                              | ZCH-5                   | Surgery field: PRINCIPAL PROCEDURE CODE (#27)                                                               |
| Other Procedures                                 | ZIS-1                   | Surgery field: OTHER PROCEDURE CODE (#3 of Subfile \#130.16) and OTHER PROCEDURE (#.01 of Subfile \#130.16) |
| Date of Operation                                | ZCH-7                   | Surgery field: SCHEDULED START TIME (#10), SCHEDULED END TIME (#11)                                         |

V*IST*A Surgery to AAIS and Ancillary Systems

|                                                       |                         |                                                                                           |
|-------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------|
| Data                                              | Segment/Sequence \# | V*IST*A Mapping                                                                       |
| Scheduling Information:                           |                         |                                                                                           |
| Surgeon                                               | ZIP-1 and 2             | Surgery field: SURGEON (#.14), FIRST ASST (#.15), SECOND ASST (#.16), ATTEND SURG (#.164) |
| Medical Specialty                                     | OBX-5                   | Surgery field: MEDICAL SPECIALTY (#125)                                                   |
| Surgical Specialty                                    | OBX-5                   | Surgery field: SURGERY SPECIALTY (#.04)                                                   |
| Number of Post Graduate Years for the Primary Surgeon | OBX-5                   | Surgery field: PGY OF PRIMARY SURGEON (#214)                                              |
| Anesthesiologist Supervise code                       | OBX-5                   | Surgery field: ANES SUPERVISE CODE (#.345)                                                |
| Patient Class                                         | OBX-5                   | Surgery field: IN/OUT-PATIENT STATUS (#.011)                                              |
| Cancel Reason                                         | OBX-5                   | Surgery field: CANCEL REASON (#18)                                                        |
| Cancel Date                                           | OBX-16                  | Surgery field: CANCEL DATE (#17)                                                          |
| Anesthesia Personnel                                  | ZIP-1 and 2             | Surgery field: PRINC ANESTHETIST (#.31) and ANESTHESIOLOGIST SUPVR (#.34)                 |

Bidirectional Information

|                                                                |                         |                                              |
|----------------------------------------------------------------|-------------------------|----------------------------------------------|
| Data                                                       | Segment/Sequence \# | V*IST*A Mapping                          |
| Observation Results:                                       |                         |                                              |
| Surgery Case Number                                            | OBR-3                   | SURGERY file (#130), IEN                     |
| Operating Room                                                 | OBX-5                   | Surgery field: OPERATING ROOM (#.02)         |
| Start Time of Surgical Procedure                               | OBR-7                   | Surgery field: TIME OPERATION BEGAN (#.22)   |
| Completion Time of All Operative Procedures for Case           | OBR-8                   | Surgery field: TIME OPERATION ENDS (#.23)    |
| Number of Minutes Necessary to Prepare Operating Room          | OBX-5 and 6             | Surgery field: OR SET­UP TIME (#.44)          |
| Time Patient Arrived in Holding Area                           | OBX-5                   | Surgery field: TIME PAT IN HOLD AREA (#.203) |
| Time Nurse Presents                                            | OBX-5                   | Surgery field: NURSE PRESENT TIME (#.202)    |
| Time Patient Transported into the Operation Room               | OBX-5                   | Surgery field: TIME PAT IN OR (#.205)        |
| Time Anesthetist Declares Patient Ready for Start of Procedure | OBX-5                   | Surgery field: INDUCTION COMPLETE (#.215)    |
| Anesthesiology Staff Supervisor                                | OBX-5                   | Surgery field: ANESTHESIOLOGIST SUPVR (#.34) |
| Anesthesiologist Supervise code                                | OBX-5                   | Surgery field: ANES SUPERVISE CODE (#.345)   |
| Principal Anesthesiologist                                     | OBX-5                   | Surgery field: PRINC ANESTHETIST (#.31)      |
| Assistant to the Principal Anesthetist                         | OBX-5                   | Surgery field: ASST ANESTHETIST (#.33)       |
| Anesthetist Relieving the Principal Anesthetist                | OBX-5                   | Surgery field: RELIEF ANESTHETIST (#.32)     |
| Time Anesthetist Available to Service Patient                  | OBX-5                   | Surgery field: ANES AVAIL TIME (#.204)       |

Bidirectional Information

|                                                                                        |                         |                                              |
|----------------------------------------------------------------------------------------|-------------------------|----------------------------------------------|
| Data                                                                               | Segment/Sequence \# | V*IST*A Mapping                          |
| Observation Results:                                                               |                         |                                              |
| Time Anesthesia Care Begins                                                            | OBX-5                   | Surgery field: ANES CARE START TIME (#.21)   |
| Time Anesthesia Care Ends                                                              | OBX-5                   | Surgery field: ANES CARE END TIME (#.24)     |
| Surgeon                                                                                | OBX-5                   | Surgery field: SURGEON (#.14)                |
| Number of Post Graduate Years completed by the Primary Surgeon                         | OBX-5                   | Surgery field: PGY OF PRIMARY SURGEON (#214) |
| Time Authorized Surgeon Available to Begin Operation                                   | OBX-5                   | Surgery field: SURG PRESENT TIME (#.206)     |
| Code Corresponding to Highest Level of Supervision Provided by Attending Staff Surgeon | OBX-5                   | Surgery field: ATTENDING CODE (#.166)        |
| Non-OR location for Non-OR Procedure                                                   | OBX-5                   | Surgery field: NON-OR LOCATION (#119)        |
| Date/Time the Non-OR Procedure Began                                                   | OBR-7                   | Surgery field: TIME PROCEDURE BEGAN (#121)   |
| Date/Time the Non-OR Procedure Ended                                                   | OBR-8                   | Surgery field: TIME PROCEDURE ENDED (#122)   |
| Provider for Non-OR Procedure                                                          | OBX-5                   | Surgery field: PROVIDER (#123)               |
| Attending Provider for Non-OR Procedure                                                | OBX-5                   | Surgery field: ATTEND PROVIDER (#124)        |
| Time Patient is Taken from Operating Room                                              | OBX-5                   | Surgery field: TIME PAT OUT OR (#.232)       |
| Case Schedule Type                                                                     | OBX-5                   | Surgery field: CASE SCHEDULE TYPE (#.035)    |
| ASA Classification                                                                     | OBX-5                   | Surgery field: ASA CLASS (#1.13)             |

  
Bidirectional Information

|                                                                           |                         |                                                                   |
|---------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------|
| Data                                                                  | Segment/Sequence \# | V*IST*A Mapping                                               |
| Observation Results:                                                  |                         |                                                                   |
| Estimated Number of Milliliters of Blood Lost During Procedure            | OBX-5 and 6             | Surgery field: BLOOD LOSS (ML) (#.25)                             |
| Temperature in Centigrade at End of Anesthesia Care                       | OBX-5 and 6             | Surgery field: FINAL ANESTHESIA TEMP (#.65)                       |
| Number of Milliliters of Urine Output During Operative Procedure          | OBX-5 and 6             | Surgery field: TOTAL URINE OUTPUT (ML) (#.255)                    |
| Patient’s Pulse Rate at End of Operative Procedure                        | OBX-5                   | Surgery field: END PULSE (#.84)                                   |
| Patient’s Rate of Respiration at End of Operative Procedure               | OBX-5 and 6             | Surgery field: END RESP (#.86)                                    |
| Patient’s Systolic/Diastolic Blood Pressure at End of Operative Procedure | OBX-5                   | Surgery field: END BP (#.85)                                      |
| Date/Time Tourniquet Applied                                              | OBR-5                   | Surgery field: TIME TOURNIQUET APPLIED (#.01 of Subfile \#130.02) |
| Date/Time Tourniquet Released                                             | OBR-6                   | Surgery field: TIME TOURNIQUET REL. (#3 of Subfile \#130.02)      |
| Site Tourniquet Applied                                                   | OBX-3                   | Surgery field: SITE APPLIED (#1 of Subfile \#130.02)              |
| Tourniquet Pressure Applied (in TORR)                                     | OBX-5 and 6             | Surgery field: PRESSURE (#4 of Subfile \#130.02)                  |
| Person Applying the Tourniquet                                            | OBX-16                  | Surgery field: TOURNIQUET APPL. BY (#2 of Subfile \#130.02)       |
| Type of Fluid Given Intravascularly During Operative Period               | OBX-3                   | Surgery field: REPLACEMENT FLUID TYPE (#.01 of Subfile \#130.04)  |

  
Bidirectional Information

|                                                                                             |                         |                                                                |
|---------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------|
| Data                                                                                    | Segment/Sequence \# | V*IST*A Mapping                                            |
| Observation Results:                                                                    |                         |                                                                |
| Number of Milliliters of Replacement Fluid Given Intravascularly During Operative Procedure | OBX-5 and 6             | Surgery field: QTY OF FLUID (ml) (#1 of Subfile \#130.04)      |
| Time Monitor Applied to Patient                                                             | OBR-6                   | Surgery field: TIME INSTALLED (#1 of Subfile \#130.41)         |
| Time Monitor Removed from Patient                                                           | OBR-7                   | Surgery field: TIME REMOVED (#2 of Subfile \#130.41)           |
| Type of Physiologic Monitor Used During Case                                                | OBX-3                   | Surgery field: MONITORS (#.01 of Subfile \#130.41)             |
| Person Applying the Monitor                                                                 | OBX-16                  | Surgery field: APPLIED BY (#3 of Subfile \#130.41)             |
| Name of Medication                                                                          | OBR-4                   | Surgery field: MEDICATIONS (#.01 of Subfile \#130.33)          |
| Date/Time Medication Administered                                                           | OBR-7                   | Surgery field: TIME ADM (#.01 of Subfile \#130.34)             |
| Medication Ordered By                                                                       | OBR-16                  | Surgery field: ORDERED BY (#2 of Subfile \#130.34)             |
| Medication Dosage                                                                           | OBX-5                   | Surgery field: DOSE (#1 of Subfile \#130.34)                   |
| Medication Administered By                                                                  | OBX-16                  | Surgery field: ADMIN BY (#3 of Subfile \#130.34)               |
| Medication Route                                                                            | OBX-5                   | Surgery field: ROUTE (#4 of Subfile \#130.34)                  |
| Anesthesia Technique Used During Case                                                       | OBR-4                   | Surgery field: ANESTHESIA TECHNIQUE (#.01 of Subfile \#130.06) |

Bidirectional Information

|                                                                       |                         |                                                              |
|-----------------------------------------------------------------------|-------------------------|--------------------------------------------------------------|
| Data                                                              | Segment/Sequence \# | V*IST*A Mapping                                          |
| Observation Results:                                              |                         |                                                              |
| Anesthesia Comments                                                   | NTE-3                   | Surgery field: ANESTHESIA COMMENTS (#.01 of Subfile \#130.5) |
| Principal Anesthesia Technique for Procedure (Y/N)?                   | OBX-5                   | Surgery field: PRINCIPAL TECH (#.05 of Subfile \#130.06)     |
| Method Used to Determine Placement of Epidural Needle                 | OBX-5                   | Surgery field: EPIDURAL METHOD (#30 of Subfile \#130.06)     |
| Anesthesia Agents Used for Technique                                  | OBX-3                   | Surgery field: ANESTHESIA AGENTS (#.01 of Subfile \#130.47)  |
| End Total Dose in Milligrams for Nonvolatile Agents                   | OBX-5 and 6             | Surgery field: DOSE (mg) (#1 of Subfile \#130.47)            |
| Person Responsible for Removing Endotracheal Tube                     | OBX-5                   | Surgery field: EXTUBATED BY (#39 of Subfile \#130.06)        |
| Patient Status While Anesthetized                                     | OBX-5                   | Surgery field: PATIENT STATUS (#2 of Subfile \#130.06)       |
| Endotracheal Tube Route                                               | OBX-5                   | Surgery field: ROUTE (#4 of Subfile \#130.06)                |
| Approach Technique Used for Endotracheal Intubation                   | OBX-5                   | Surgery field: APPROACH (#3 of Subfile \#130.06)             |
| Type of Laryngoscope Blade Used to Facilitate Endotracheal Intubation | OBX-5                   | Surgery field: LARYNGOSCOPE TYPE (#5 of Subfile \#130.06)    |
| Laryngoscope Size Used to Facilitate Endotracheal Intubation          | OBX-5                   | Surgery field: LARYNGOSCOPE SIZE (#6 of Subfile \#130.06)    |

  
Bidirectional Information

|                                                                  |                         |                                                                  |
|------------------------------------------------------------------|-------------------------|------------------------------------------------------------------|
| Data                                                         | Segment/Sequence \# | V*IST*A Mapping                                              |
| Observation Results:                                         |                         |                                                                  |
| Type of Endotracheal Tube Used During Major Portion of Procedure | OBX-5                   | Surgery field: TUBE TYPE (#10 of Subfile \#130.06)               |
| Endotracheal Tube Size                                           | OBX-5                   | Surgery field: TUBE SIZE (#11 of Subfile \#130.06)               |
| Anesthesia Ventilator Tidal Volume Setting at End of Case        | OBX-5                   | Surgery field: END VENT. T.V. (#19 of Subfile \#130.06)          |
| Anesthesia Ventilator Rate Setting at End of Operative Procedure | OBX-5                   | Surgery field: END VENT. RATE (#20 of Subfile \#130.06)          |
| Location Where the Endotracheal Tube Removed                     | OBX-5                   | Surgery field: EXTUBATED IN (#21 of Subfile \#130.06)            |
| Baricity                                                         | OBX-5                   | Surgery field: BARICITY (#26 of Subfile \#130.06)                |
| Method of Administration of Anesthetic Agent                     | OBX-5                   | Surgery field: ADMINISTRATION METHOD (#36 of Subfile \#130.06)   |
| Epidural Test Dose                                               | OBX-3                   | Surgery field: TEST DOSE (#.01 of Subfile \#130.48)              |
| Volume in Milligrams of Test Dose Fluid                          | OBX-5                   | Surgery field: TEST DOSE VOL (ml) (#33 of Subfile \#130.06)      |
| Non-OR Procedure Occurrence                                      | OBR-4                   | Surgery field: PROCEDURE OCCURRENCE (#.01 of Subfile \#130.0126) |
| Date that the non-OR Occurrence was Noted                        | OBX-5                   | Surgery field: DATE OCCURRENCE NOTED (#2 od Subfile \#130.0126)  |

Bidirectional Information

|                                                      |                         |                                                                      |
|------------------------------------------------------|-------------------------|----------------------------------------------------------------------|
| Data                                             | Segment/Sequence \# | V*IST*A Mapping                                                  |
| Observation Results:                             |                         |                                                                      |
| Non-OR Occurrence Category                           | OBX-5                   | Surgery field: OCCURRENCE CATEGORY (#5 of Subfile \#130.0126)        |
| Treatment Instituted to the Non-OR Occurrence        | OBX-5                   | Surgery field: TREATMENT INSTITUTED (#3 of Subfile \#130.0126)       |
| Outcome to date of the Non-OR Occurrence             | OBX-5                   | Surgery field: OUTCOME TO DATE (#1 of Subfile \#130.0126)            |
| Occurrence not related to the Surgery                | OBR-4                   | Surgery field: NON­OPERATIVE OCCURRENCE (#.01 of Subfile \#130.053)   |
| Date that the Non-Operative Occurrence was Noted     | OBX-5                   | Surgery field: DATE OCCURRENCE NOTED (#2 of Subfile \#130.053)       |
| Non-Operative Occurrence Category                    | OBX-5                   | Surgery field: OCCURRENCE CATEGORY (#5 of Subfile \#130.053)         |
| Treatment Instituted to the Non-Operative Occurrence | OBX-5                   | Surgery field: TREATMENT INSTITUTED (#3 of Subfile \#130.053)        |
| Outcome to date of the Non-Operative Occurrence      | OBX-5                   | Surgery field: OUTCOME TO DATE (#1 of Subfile \#130.053)             |
| Intraoperative Occurrence                            | OBR-4                   | Surgery field: INTRAOPERATIVE OCCURRENCES (#.01 of Subfile \#130.13) |
| Intraoperative Occurrence Category                   | OBX-5                   | Surgery field: OCCURRENCE CATEGORY (#3 of Subfile \#130.13)          |

Bidirectional Information

|                                                             |                         |                                                              |
|-------------------------------------------------------------|-------------------------|--------------------------------------------------------------|
| Data                                                    | Segment/Sequence \# | V*IST*A Mapping                                          |
| Observation Results:                                    |                         |                                                              |
| ICD Diagnosis Code related to the Intraoperative Occurrence | OBX-5                   | Surgery field: ICD DIAGNOSIS CODE (#4 of Subfile \#130.13)   |
| Outcome to date of the Intraoperative Occurrence            | OBX-5                   | Surgery field: OUTCOME TO DATE (#.05 of Subfile \#130.13)    |
| Postoperative Occurrence                                    | OBR-4                   | Surgery field: POSTOP OCCURRENCES (#.01 of Subfile \#130.22) |
| Postoperative Occurrence Category                           | OBX-5                   | Surgery field: OCCURRENCE CATEGORY (#5 of Subfile \#130.22)  |
| ICD Diagnosis Code related to the Postoperative Occurrence  | OBX-5                   | Surgery field: ICD DIAGNOSIS CODE (#6 of Subfile \#130.22)   |
| Outcome to date of the Postoperative Occurrence             | OBX-5                   | Surgery field: OUTCOME TO DATE (#.05 of Subfile \#130.22)    |