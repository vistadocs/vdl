---
title: RA5*158 HL7 Interface Specification
doc_type: INT
doc_label: Interface Specification
doc_layer: plain
doc_subject: RA5*158 HL7
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 200
security_keys: []
menu_options: 7
description: "<table> <colgroup> <col style=\\"width: 19%\\" /> <col style=\\"width: 10%\\" /> <col style=\\"width: 60%\\" /> <col style=\\"width: 9%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Version</th> <th>Change</th> <th>Page</th> </tr> </thead> <tbody> <tr class=\\"odd\\"> <td>December 1999</td> <td>1.0</t"
audience: 
keywords: 
  - table
  - class
  - segment
  - contents
  - message
  - fields
  - vista
  - number
  - order
  - component
page_count: 0
word_count: 22320
section_count: 32
table_count: 110
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0hl7is_p158.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0hl7is_p158.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra5-158-hl7-interface-specification/001.png)

Radiology/Nuclear Medicine 5.0

HL7 Interface Specification

Revised for

Patch RA\*5.0\*158

July 2019

Revision History

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 60%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Change</th>
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
<td>March 2007</td>
<td>2.0</td>
<td>Completely updated to include current functionality and to meet current HSD&amp;D Documentation Standards</td>
<td></td>
</tr>
<tr class="odd">
<td>August 2011</td>
<td>3.0</td>
<td><ul>
<li><p>Combined two HL7 specifications, VistA Imaging’s Profiles for HL7 Messages from VistA to Commercial PACs and VistA Radiology/Nuclear Medicine 5.0 HL7 Interface Specification for Voice Recognition Dictation Systems, reformatted the new version, Radiology/Nuclear Medicine 5.0 HL7 Interface Specification</p></li>
<li><p>Incorporated updates from VistA Imaging’s Profiles for HL7 Messages from VistA to Commercial PACs dated 03 Feb 11 version 1.2.9</p></li>
<li><p>Updated to HL7 v2.4 with Patch RA*5*47</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td>January 2012</td>
<td>3.1</td>
<td><p>Patch RA*5.0*107</p>
<ul>
<li><p>Updated the description of MSH Segment; for ORMs and ORUs Seq 15: Usage is <strong>X</strong> <strong>Not required</strong> and Cardinality is <strong>0..0</strong>.</p></li>
<li><p>Updated the description of MSH Segment; for ORMs and ORUs Seq 16: Usage is <strong>X</strong> <strong>Not required</strong> and Cardinality is <strong>0..0</strong>.</p></li>
<li><p>Updated the description of MSH-4-Sending Facility; for ORMs and ORUs Seq 2 and 3: Usage is <strong>X</strong> <strong>Not required</strong> and Cardinality is <strong>0..0</strong></p></li>
<li><p>Added 2 sections:</p></li>
</ul>
<ol type="a">
<li><p>5 Query Profile</p></li>
<li><p>6 Response Profile</p></li>
</ol>
<ul>
<li><p>Added a Query message example</p></li>
<li><p>Added a Response message example</p></li>
</ul></td>
<td><p>15<br />
<br />
<br />
15</p>
<p>24<br />
<br />
<br />
79</p>
<p>87</p>
<p>97</p>
<p>97</p></td>
</tr>
<tr class="odd">
<td>November 2016</td>
<td>3.2</td>
<td><p>Patch RA*5.0*131</p>
<ul>
<li><p>Usage 11 changed from “X” to “C”.</p></li>
<li><p>Usage 11 changed from “X” to “C”.</p></li>
<li><p>The field 'Referring Doctor PV1-8 documentation, edited to; This field contains information about the primary care physician for this patient. VistA values this field for inpatient encounters only. Only the first four components are used.</p></li>
<li><p>PV1-11 Temporary Location description added.</p></li>
<li><p>PV1-11 Temporary Location Table added.</p></li>
</ul></td>
<td><p>17</p>
<p>37</p>
<p>39</p>
<p>40</p>
<p>102</p></td>
</tr>
<tr class="even">
<td>March 2018</td>
<td>3.3</td>
<td><p>Patch RA*5.0*144</p>
<ul>
<li><p>Removed HLO Query Profile information</p></li>
<li><p>Add ‘VAQ’ observation result status</p></li>
</ul></td>
<td><p>80-112</p>
<p>78</p></td>
</tr>
<tr class="odd">
<td>July 2019</td>
<td>3.5</td>
<td><p>RA*5.0*158</p>
<p>RIS HL7 2.4 ORM message update: ORC-4 Placer group number field update.</p></td>
<td>19, 42, 43, 84, 85, 93</td>
</tr>
</tbody>
</table>

Table of Contents

1 Introduction 1

1.1 Organization of this Document 1

1.2 Overview of HL7 Terminology 1

1.2.1 Application Processing Rules 1

1.2.2 Communication Protocol 1

1.2.3 Data Type 2

1.2.4 Escape Sequences in Data Fields 2

1.2.5 Fields 3

1.2.6 File 3

1.2.7 Maximum Length 3

1.2.8 Messages 3

1.2.9 HL7 Messages 4

1.2.10 Message Delimiters 4

1.2.11 Position (sequence within the segment) 5

1.2.12 Segments 5

1.2.13 Table 6

1.2.14 Usage 6

1.3 References 7

2 Overview of Trigger Events 9

2.1 Patient Registration 9

2.2 Exam Edit 9

2.3 Exam Cancel 9

2.4 Report Verified or Released/Not Verified 10

3 Order Entry/Update Profile 11

3.1 Use Case 11

3.1.1 Scope 11

3.1.2 Actors and Roles 11

3.2 Interactions 12

3.3 Dynamic Definition 12

3.3.1 ORM - Order Message 12

3.3.2 ACK - Acknowledgment Message 13

3.3.2.1 Return Original Mode ACK 13

3.3.2.2 Send MSA Segment for AE and AR conditions 13

3.4 Static Definition – Message Level 13

3.4.1 Order Message (ORM) 13

3.4.2 Acknowledgment Message (ACK) 14

3.5 Static Definition – Segment Level 15

3.5.1 MSH Segment 15

3.5.2 PID Segment 16

3.5.3 PV1 Segment 17

3.5.4 ORC Segment 19

3.5.5 OBR Segment 20

3.5.6 ZDS Segment 21

3.5.7 OBX Segment 22

3.5.8 MSA Segment 22

3.6 Static Definition – Field Level 23

3.6.1 MSH Segment Fields in ORM and ORU 23

3.6.1.1 MSH-1-Field Separator 24

3.6.1.2 MSH-2-Encoding Characters 24

3.6.1.3 MSH-3-Sending Application 24

3.6.1.4 MSH-4-Sending Facility 5F 24

3.6.1.5 MSH-5-Receiving Application 25

3.6.1.6 MSH-6-Receiving Facility 25

3.6.1.7 MSH-7-Date/Time of Message 25

3.6.1.8 MSH-9-Message Type 25

3.6.1.8.1 MSH-9.1-Message Type 26

3.6.1.8.2 MSH-9.2-Trigger Event 26

3.6.1.9 MSH-10-Message Control ID 26

3.6.1.10 MSH-11-Processing ID 26

3.6.1.10.1 MSH-11.1-Processing ID 26

3.6.1.10.2 MSH-11.2-Processing Mode 26

3.6.1.11 MSH-12-Version ID 27

3.6.1.12 MSH-15-Accept Acknowledgment Type 27

3.6.1.13 MSH-16-Application Acknowledgment Type 27

3.6.1.14 MSH-17-Country Code 28

3.6.2 PID Segment Fields 28

3.6.3 PID-2-Patient ID 29

3.6.3.1.1 PID-2.1-ID 29

3.6.3.1.2 PID-2.4-Assigning Authority 30

3.6.3.1.3 PID-2.5-Identifier Type 30

3.6.3.2 PID-3-Patient Identifier List 30

3.6.3.2.1 PID-3.1-ID 30

3.6.3.2.2 PID-3.4-Assigning Authority 30

3.6.3.2.3 PID-3.5-Identifier Type 31

3.6.3.3 PID-4-Alternate Patient ID 31

3.6.3.3.1 PID-4.1-ID 31

3.6.3.3.2 PID-4.4-Assigning Authority 31

3.6.3.3.3 PID-4.5-Identifier Type 32

3.6.3.4 PID-5-Patient Name 32

3.6.3.5 PID-7-Date/Time of Birth 32

3.6.3.6 PID-8-Sex 33

3.6.3.7 PID-10-Race 33

3.6.3.7.1 PID-10.1-Identifier 33

3.6.3.7.2 PID-10.3-Name of Coding System 33

3.6.3.7.3 PID-10.4-Alternate Identifier 33

3.6.3.7.4 PID-10.6-Name of Coding System 34

3.6.3.8 PID-11-Patient Address 34

3.6.3.9 PID-13-Phone Number – Home 34

3.6.3.9.1 PID-13.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] 35

3.6.3.9.2 PID-13.2-Telecommunication Use Code 35

3.6.3.9.3 PID-13.3-Telecommunication Equipment Type 35

3.6.3.10 PID-14-Phone Number – Business 35

3.6.3.10.1 PID-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] 35

3.6.3.10.2 PID-14.2-Telecommunication Use Code 36

3.6.3.10.3 PID-14.3-Telecommunication Equipment Type 36

3.6.3.11 PID-19-SSN Number – Patient 36

3.6.3.12 PID-22-Ethnic Group 36

3.6.3.12.1 PID-22.1-Identifier 36

3.6.3.12.2 PID-22.3-Name of Coding System 36

3.6.3.12.3 PID-22.4-Alternate Identifier 37

3.6.3.12.4 PID-22.6-Name of Coding System 37

3.6.4 PV1 Segment Fields in ORM 37

3.6.4.1 PV1-2-Patient Class 38

3.6.4.2 PV1-3-Assigned Patient Location 38

3.6.4.3 PV1-7-Attending Doctor 39

3.6.4.4 PV1-8-Referring Doctor 39

3.6.4.5 PV1-10-Hospital Service 40

3.6.4.6 PV1-11-Temporary Location 40

3.6.4.7 PV1-15-Ambulatory Status 41

3.6.4.8 PV1-16-VIP Indicator 41

3.6.4.9 PV1-19-Visit 42

3.6.5 ORC Segment Fields in ORM 42

3.6.5.1 ORC-1-Order Control 42

3.6.5.2 ORC-2-Placer Order Number 43

3.6.5.3 ORC-3-Filler Order Number 43

3.6.5.4 ORC-4-Placer Group Number 43

3.6.5.5 ORC-5-Order Status 43

3.6.5.6 ORC-7-Quantity/Timing 43

3.6.5.6.1 ORC-7.4-Start Date/Time 44

3.6.5.6.2 ORC-7.6-Priority 44

3.6.5.7 ORC-8-Parent 44

3.6.5.8 ORC-9-Date/Time of Transaction 44

3.6.5.9 ORC-10-Entered By 44

3.6.5.10 ORC-12-Ordering Provider 45

3.6.5.11 ORC-13-Enterer’s Location 46

3.6.5.12 ORC-14-Call Back Phone Number 46

3.6.5.12.1 ORC-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] 48

3.6.5.12.2 ORC-14.2-Telecommunication Use Code 48

3.6.5.12.3 ORC-14.3-Telecommunication Equipment Type 48

3.6.5.13 ORC-17-Entering Organization 48

3.6.5.13.1 ORC-17.1-Identifier 48

*3.6.5.13.2* ORC-17.2-Text 49

*3.6.5.13.3* ORC-17.3-Name of Coding System 49

3.6.6 OBR Segment Fields in ORM 49

3.6.6.1 OBR-1-Set ID 50

3.6.6.2 OBR-2-Placer Order Number 50

3.6.6.3 OBR-3-Filler Order Number 50

3.6.6.4 OBR-4-Universal Service Identifier 50

3.6.6.4.1 OBR-4.1-Identifier 51

3.6.6.4.2 OBR-4.2-Text 51

3.6.6.4.3 OBR-4.3-Name of Coding System 51

3.6.6.4.4 OBR-4.4-Alternate Identifier 51

3.6.6.4.5 OBR-4.5-Alternate Text 51

3.6.6.4.6 OBR-4.6-Name of Alternate Coding System 51

3.6.6.5 OBR-5-Priority 51

3.6.6.6 OBR-15-Specimen Source 52

3.6.6.7 OBR-16-Ordering Provider 52

3.6.6.8 OBR-17-Order Callback Phone Number 53

3.6.6.8.1 OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] 53

3.6.6.8.2 OBR-17.2-Telecommunication Use Code 53

3.6.6.8.3 OBR-17.3-Telecommunication Equipment Type 53

3.6.6.9 OBR-18-Placer Field 1 54

3.6.6.10 OBR-19-Placer Field 2 54

3.6.6.11 OBR-20-Filler Field 1 54

3.6.6.12 OBR-21-Filler Field 2 54

3.6.6.13 OBR-24-Diagnostic Service Section ID 54

3.6.6.14 OBR-27-Quantity/Timing 55

3.6.6.14.1 OBR-27.4-Start Date/Time 55

3.6.6.14.2 OBR-27.6-Priority 55

3.6.6.15 OBR-29-Parent 55

3.6.6.16 OBR-30-Transportation Mode 56

3.6.6.17 OBR-31-Reason for Study 56

3.6.6.17.1 OBR-31.2-Reason for Study 56

3.6.7 ZDS Segment Fields in ORM and ORU 56

3.6.7.1 ZDS-1-Study Instance UID 56

3.6.7.1.1 ZDS-1.1-Pointer 57

3.6.7.1.2 ZDS-1.2-Application ID 57

3.6.7.1.3 ZDS-1.3-Type of Data 57

3.6.7.1.4 ZDS-1.4-Subtype 57

3.6.8 OBX Segment Fields in ORM and ORU 57

3.6.8.1 OBX-2-Value Type 58

3.6.8.2 OBX-3-Observation Identifier 58

3.6.8.2.1 OBX-3.1-Identifier and OBX-3.2-Text 58

3.6.8.2.2 OBX-3.3-Name of Coding System 58

3.6.8.3 OBX-5-Observation Value 59

3.6.8.4 OBX-11-Observation Result Status 59

3.6.9 MSA Segment Fields 59

4 Report Transmission/Storage Profile 61

4.1 Use Case 61

4.1.1 Scope 61

4.1.2 Actors and Roles 61

4.2 Interactions 62

4.3 Dynamic Definition 62

4.3.1 ORU – Unsolicited Observation Results 62

4.4 Static Definition – Message Level 63

4.4.1 Observation Result–Unsolicited (ORU) 63

4.5 Static Definition – Segment Level 64

4.5.1 MSH Segment 64

4.5.2 PID Segment 64

4.5.3 OBR Segment 64

4.5.4 ZDS Segment 66

4.5.5 OBX Segment 66

4.5.6 MSA Segment 66

4.6 Static Definition – Field Level 67

4.6.1 MSH Segment Fields in ORU Messages (Outbound and Inbound) 67

4.6.2 PID Segment Fields in ORU Messages (Outbound and Inbound) 67

4.6.3 OBR Segment Fields in ORU Messages (Outbound and Inbound) 67

4.6.3.1 OBR-1-Set ID 68

4.6.3.2 OBR-2-Placer Order Number 68

4.6.3.3 OBR-3-Filler Order Number 69

4.6.3.4 OBR-4-Universal Service Identifier 69

4.6.3.4.1 OBR-4.1-Identifier 69

4.6.3.4.2 OBR-4.2-Text 69

4.6.3.4.3 OBR-4.3-Name of Coding System 69

4.6.3.4.4 OBR-4.4-Alternate Identifier 69

4.6.3.4.5 OBR-4.5-Alternate Text 70

4.6.3.4.6 OBR-4.6-Name of Alternate Coding System 70

4.6.3.5 OBR-7-Observation Date/Time 70

4.6.3.6 OBR-15-Specimen Source 70

4.6.3.7 OBR-16-Ordering Provider 70

4.6.3.8 OBR-17-Order Callback Phone Number 71

4.6.3.8.1 OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] 71

4.6.3.8.2 OBR-17.2-Telecommunication Use Code 71

4.6.3.8.3 OBR-17.3-Telecommunication Equipment Type 72

4.6.3.9 OBR-18-Placer Field 1 72

4.6.3.10 OBR-19-Placer Field 2 72

4.6.3.11 OBR-20-Filler Field 1 72

4.6.3.12 OBR-21-Filler Field 2 72

4.6.3.13 OBR-22-Results Rpt/Status Chng – Date/Time 72

4.6.3.14 OBR-25-Result Status 72

4.6.3.15 OBR-29-Parent 73

4.6.3.16 OBR-32-Principal Result Interpreter 73

4.6.3.16.1 OBR-32.1-Name 73

4.6.3.17 OBR-33-Assistant Result Interpreter 74

4.6.3.17.1 OBR-33.1-Name 74

4.6.3.18 OBR-35-Transcriptionist 75

4.6.3.18.1 OBR-35.1-Name 75

4.6.4 ZDS Segment Fields in ORU and ORM 76

4.6.4.1 ZDS-1-Study Instance UID 76

4.6.4.1.1 ZDS-1.1-Pointer 76

4.6.4.1.2 ZDS-1.2-Application ID 76

4.6.4.1.3 ZDS-1.3-Type of Data 76

4.6.4.1.4 ZDS-1.4-Subtype 76

4.6.5 OBX Segment Fields in ORU Messages (Outbound and Inbound) 76

4.6.5.1 OBX-2-Value Type 77

4.6.5.2 OBX-3-Observation Identifier 77

4.6.5.2.1 OBX-3.1-Identifier and OBX-3.2-Text 78

4.6.5.2.2 OBX-3.3-Name of Coding System 78

4.6.5.3 OBX-5-Observation Value 78

4.6.5.4 OBX-6-Units 78

4.6.5.5 OBX-11-Observation Result Status 79

4.7 ACK – General Acknowledgment Message 79

4.7.1 MSA Segment Fields in ACK Messages 79

4.7.1.1 MSA-1-Acknowledgment Code 79

4.7.1.2 MSA-2-Message Control ID 80

4.7.1.3 MSA-3-Text Message 80

5 This page intentionally left blank 82

6 Appendix A – Message Examples 83

6.1 ORM Examples 83

6.1.1 ORM for new/registered order 83

6.1.2 ORM for registration of a Printset 84

6.1.2.1 ORC-8-Parent and OBR-29-Parent 84

6.1.2.2 OBR-2-Placer and OBR-3-Filler 84

6.1.3 ORM for an edited order 86

6.1.4 ORM for a canceled order 86

6.2 ORU Examples 87

6.2.1 ORU for report on a single procedure 87

6.2.2 ORU for Printset (single report on multiple procedures) 88

6.3 ACK Example 89

7 Appendix B – VistA Data Attributes 90

7.1 MSH Segments 90

7.2 PID Segments 91

7.3 PV-1 Segments 92

7.4 ORC Segments 92

7.5 OBR Segments 94

7.6 ZDS Segments ORM and ORU 99

7.7 OBX (ORU) Segments 99

7.8 OBX (ORM) Segments 101

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Organization of this Document](#organization-of-this-document)
  - [Overview of HL7 Terminology](#overview-of-hl7-terminology)
    - [Application Processing Rules](#application-processing-rules)
    - [Communication Protocol](#communication-protocol)
    - [Data Type](#data-type)
    - [Escape Sequences in Data Fields](#escape-sequences-in-data-fields)
    - [Fields](#fields)
    - [File](#file)
    - [Maximum Length](#maximum-length)
    - [Messages](#messages)
    - [HL7 Messages](#hl7-messages)
    - [Message Delimiters](#message-delimiters)
    - [Position (sequence within the segment)](#position-sequence-within-the-segment)
    - [Segments](#segments)
    - [Table](#table)
    - [Usage](#usage)
  - [References](#references)
- [Overview of Trigger Events](#overview-of-trigger-events)
  - [Patient Registration](#patient-registration)
  - [Exam Edit](#exam-edit)
  - [Exam Cancel](#exam-cancel)
  - [Report Verified or Released/Not Verified](#report-verified-or-releasednot-verified)
- [Order Entry/Update Profile](#order-entryupdate-profile)
  - [Use Case](#use-case)
    - [Scope](#scope)
    - [Actors and Roles](#actors-and-roles)
  - [Interactions](#interactions)
  - [Dynamic Definition](#dynamic-definition)
    - [ORM - Order Message](#orm-order-message)
    - [ACK - Acknowledgment Message](#ack-acknowledgment-message)
  - [Static Definition – Message Level](#static-definition-message-level)
    - [Order Message (ORM)](#order-message-orm)
    - [Acknowledgment Message (ACK)](#acknowledgment-message-ack)
  - [Static Definition – Segment Level](#static-definition-segment-level)
    - [MSH Segment](#msh-segment)
    - [PID Segment](#pid-segment)
    - [PV1 Segment](#pv1-segment)
    - [ORC Segment](#orc-segment)
    - [OBR Segment](#obr-segment)
    - [ZDS Segment](#zds-segment)
    - [OBX Segment](#obx-segment)
    - [MSA Segment](#msa-segment)
  - [Static Definition – Field Level](#static-definition-field-level)
    - [MSH Segment Fields in ORM and ORU](#msh-segment-fields-in-orm-and-oru)
    - [PID Segment Fields](#pid-segment-fields)
    - [PID-2-Patient ID](#pid-2-patient-id)
    - [PV1 Segment Fields in ORM](#pv1-segment-fields-in-orm)
    - [ORC Segment Fields in ORM](#orc-segment-fields-in-orm)
    - [OBR Segment Fields in ORM](#obr-segment-fields-in-orm)
    - [ZDS Segment Fields in ORM and ORU](#zds-segment-fields-in-orm-and-oru)
    - [OBX Segment Fields in ORM and ORU](#obx-segment-fields-in-orm-and-oru)
    - [MSA Segment Fields](#msa-segment-fields)
- [Report Transmission/Storage Profile](#report-transmissionstorage-profile)
  - [Use Case](#use-case-1)
    - [Scope](#scope-1)
    - [Actors and Roles](#actors-and-roles-1)
  - [Interactions](#interactions-1)
  - [Dynamic Definition](#dynamic-definition-1)
    - [ORU – Unsolicited Observation Results](#oru-unsolicited-observation-results)
  - [Static Definition – Message Level](#static-definition-message-level-1)
    - [Observation Result–Unsolicited (ORU)](#observation-resultunsolicited-oru)
  - [Static Definition – Segment Level](#static-definition-segment-level-1)
    - [MSH Segment](#msh-segment-1)
    - [PID Segment](#pid-segment-1)
    - [OBR Segment](#obr-segment-1)
    - [ZDS Segment](#zds-segment-1)
    - [OBX Segment](#obx-segment-1)
    - [MSA Segment](#msa-segment-1)
  - [Static Definition – Field Level](#static-definition-field-level-1)
    - [MSH Segment Fields in ORU Messages (Outbound and Inbound)](#msh-segment-fields-in-oru-messages-outbound-and-inbound)
    - [PID Segment Fields in ORU Messages (Outbound and Inbound)](#pid-segment-fields-in-oru-messages-outbound-and-inbound)
    - [OBR Segment Fields in ORU Messages (Outbound and Inbound)](#obr-segment-fields-in-oru-messages-outbound-and-inbound)
    - [ZDS Segment Fields in ORU and ORM](#zds-segment-fields-in-oru-and-orm)
    - [OBX Segment Fields in ORU Messages (Outbound and Inbound)](#obx-segment-fields-in-oru-messages-outbound-and-inbound)
  - [ACK – General Acknowledgment Message](#ack-general-acknowledgment-message)
    - [MSA Segment Fields in ACK Messages](#msa-segment-fields-in-ack-messages)
- [This page intentionally left blank](#this-page-intentionally-left-blank)
- [Appendix A – Message Examples](#appendix-a-message-examples)
  - [ORM Examples](#orm-examples)
    - [ORM for new/registered order](#orm-for-newregistered-order)
    - [ORM for registration of a Printset](#orm-for-registration-of-a-printset)
    - [ORM for an edited order](#orm-for-an-edited-order)
    - [ORM for a canceled order](#orm-for-a-canceled-order)
  - [ORU Examples](#oru-examples)
    - [ORU for report on a single procedure](#oru-for-report-on-a-single-procedure)
    - [ORU for Printset (single report on multiple procedures)](#oru-for-printset-single-report-on-multiple-procedures)
  - [ACK Example](#ack-example)
- [Appendix B – VistA Data Attributes](#appendix-b-vista-data-attributes)
  - [MSH Segments](#msh-segments)
  - [PID Segments](#pid-segments)
  - [PV-1 Segments](#pv-1-segments)
  - [ORC Segments](#orc-segments)
  - [OBR Segments](#obr-segments)
  - [ZDS Segments ORM and ORU](#zds-segments-orm-and-oru)
  - [OBX (ORU) Segments](#obx-oru-segments)
  - [OBX (ORM) Segments](#obx-orm-segments)
This document describes the messaging interface to the VistA Rad/Nuc Med 5.0 package (Rad/Nuc Med), which is based on the Integrating the Healthcare Enterprise (IHE) initiative. IHE promotes the coordinated use of established standards such as Health Level 7 (HL7) to support patient care. To comply with IHE, Rad/Nuc Med has implemented HL7 version 2.4 messaging standards for all electronic messages that are sent between VA medical center systems and commercial off-the-shelf (COTS) systems. These COTS systems include dictation systems (subscriber), picture archive and communication systems (subscriber), and other third-party information management software. This document primarily addresses bi-directional messaging between Rad/Nuc Med and COTS subscriber systems. It identifies the Rad/Nuc Med data elements and HL7 fields that are handled by the new interface, and it also defines the functional business requirements of this interface.
Several subscriber systems are already interfaced to Rad/Nuc Med, including PowerScribe, TalkStation, and RadWhere. Future COTS interfaces to Rad/Nuc Med must follow these specifications to comply with the existing interface design.

## Organization of this Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This specification is organized into six major sections.

1.  The Introduction gives a brief overview of the document and an overview of HL7 terminology.
2.  The Overview of Trigger Events chapter provides a high-level overview of four system events and the types of HL7 messages they trigger.
3.  The Order Entry/Update Profile chapter contains detailed information on the ORM and A CK HL7 messages used by Rad/Nuc Med.
4.  The Report Transmission/Storage Profile chapter contains detailed information on the ORU and ACK HL7 messages used by Rad/Nuc Med.
5.  Appendix A contains message examples, showing a variety of messaging scenarios.
6.  Appendix B contains VistA Data Attributes for the VistA HL7 messages.

## Overview of HL7 Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following terms and concepts are used throughout this interface specification. For more information, see the HL7 VistA Messaging manuals in the VistA Documentation Library (VDL) at <http://www.va.gov/vdl/application.asp?appid=8>

### Application Processing Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA HL7 protocols describe the basic rules for application processing by the sending and receiving systems. Information contained in the protocol is not repeated in this document.

### Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the implementation of patch HL\*1.6\*19, the VistA HL7 package can now support TCP/IP interfaces. The TCP/IP network standard supports the transport layer and network layer of the interface. The Minimal Lower Layer Protocol (MLLP) as specified in the HL7 v2.3.1 Implementation Guide Appendix C.4 supports the presentation layer protocol for the interface and encapsulates the HL7 v2.4 messages with start and end markers.

Two links are required for message transactions.

1.  VistA uses one link to send order messages and receive acknowledgments.
2.  VistA uses the second link to send results and receive acknowledgments.

### Data Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data type identifies the restrictions on the contents of the data field. HL7 defines a number of data types. This information is in a column labeled DT in the segment attribute tables.

| Data Type | Data Type Name                                    | Notes/Format                                                                                                        |
|-----------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| CE        | Coded Element                                     | identifier ^ text ^ name of coding system ^ alternate identifier ^ alternate text ^ name of alternate coding system |
| CM        | Composite                                         | Combination of components of varying data types                                                                     |
| CQ        | Composite quantity with units                     | quantity (NM) ^ units (CE)                                                                                          |
| CX        | Extended composite ID with check digit            | ID ^ check digit ^ code identifying the check digit scheme employed                                                 |
| EI        | Entity identifier                                 | entity identifier ^ namespace ID ^ universal ID ^ universal ID type                                                 |
| FT        | Formatted text                                    | See page [2](#escape-sequences-in-data-fields) for a list of escape sequences and allowed formatting commands.      |
| HD        | Hierarchic designator                             | namespace ID ^ universal ID ^ universal ID type                                                                     |
| ID        | Coded value for HL7 defined tables                | Valued from a table of HL7 legal values                                                                             |
| IS        | Coded value for user-defined tables               | Valued from a table of site legal values                                                                            |
| PT        | Processing type                                   | Processing ID ^ processing mode                                                                                     |
| ST        | String                                            | Data is left justified with trailing blanks optional.                                                               |
| TQ        | Timing quantity                                   | Utilizes the Priority component for order priority                                                                  |
| TS        | Time stamp                                        | YYYYMMDDHHMMSS                                                                                                      |
| TX        | Text data                                         | String data meant for user display.                                                                                 |
| XCN       | Extended composite id number and name for persons | ID ^ family name ^ given name ^ middle initial or name                                                              |
| XPN       | Extended person name                              | family name ^ given name ^ middle initial or name                                                                   |

### Escape Sequences in Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a field of type TX, FT, or CF is encoded, the escape character is used to signal certain special characteristics for portions of the text field. The escape character is whatever display ASCII character is specified in the Escape Character component of MSH-2-Encoding Characters. The character (\\ must be used to represent the character so designated in a message. An escape sequence consists of the escape character followed by a one-character escape code ID, then another occurrence of the escape character.

The following escape sequences are decoded by the Rad/Nuc Med interface for *OBX-5-Observation value* only:

| Sequence | Description            |
|----------|------------------------|
| \S\\     | Component separator    |
| \T\\     | Subcomponent separator |
| \R\\     | Repetition separator   |
| \E\\     | Escape character       |

> **NOTE:** No escape sequence may contain a *nested* escape sequence.

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. The HL7 Messaging Standard does not specify how systems must store data within an application. When fields are transmitted, they are sent as character strings. Except where noted, HL7 data fields can use the null value. Sending the null value, which is transmitted as two double quote marks (“”), is different from omitting an optional data field. The difference appears when the contents of a message are used to update a record in a database, rather than create a new one.

- If no value is sent, such as, it is omitted, the old value remains unchanged.
- If the null value is sent, the old value is changed to null.

### File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this document, a file is a VA File Manager file on the local VistA system, unless explicitly indicated otherwise.

### Maximum Length

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Maximum length is the number of characters that one occurrence of the data field can occupy. It is calculated to include the component and subcomponent separators. Because the maximum length is that of a single occurrence, the repetition separator is not included in calculating the maximum length. In segment attribute tables, this information is in a column labeled LEN.

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message is the atomic unit of data transferred between systems. It comprises a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ORU message type is used to transmit information about a patient’s order results from one system to another. A three-character code contained within each message identifies its type.

The real-world event that initiates an exchange of messages is called a trigger event. For a more detailed description of trigger events, refer to section 2.3.1 Trigger Events of the HL7 Messaging Standard v2.4. A trigger event code represents values, such as a*n order event occurred*. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code cannot be associated with more than one message type.

### HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rad/Nuc Med uses three HL7 message types to communicate with subscriber systems, subscribers, and additional HL7-subscribing applications: ORM, ORU, and ACK. HL7 messages are broadcast in response to trigger events. For instance, the order message (ORM) usually uses four statuses to trigger an HL7 message: Waiting, Examined, Transcribed, and Complete.

> **NOTE:** Individual sites can set parameters to define which HL7 message to broadcast when a specific status is reached. Consequently, HL7 messages are not triggered by the same statuses at all sites.

The business rules for the Rad/Nuc Med application state that when building HL7 messages, a continuation node must be created for any segment that exceeds 245 characters in length.0F[^1]

For examples of ORM, ORU, and ACK messages, refer to [Appendix A](#this-page-intentionally-left-blank).

### Message Delimiters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delimiters are special characters used in constructing a message. They are the segment terminator, the field separator, the component separator, the subcomponent separator, the repetition separator, and the escape character.

- The segment terminator is always a carriage return (in ASCII, a hex 0D).
- The other delimiters are defined in the MSH segment, with the field delimiter in the 4th character position and the other delimiters occurring as in the field called Encoding Characters, which is the first field after the segment ID.
- The delimiter values shown in the MSH segment are used throughout the message.

Rad/Nuc Med uses the HL7 recommended values.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 51%" />
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
<td><p>&lt;cr&gt;</p>
<p>hex 0D</p></td>
<td>-</td>
<td><p>Terminates a segment record</p>
<p>Implementers cannot change this value.</p></td>
</tr>
<tr class="even">
<td>Field Separator</td>
<td>|</td>
<td>-</td>
<td><p>Separates two adjacent data fields within a segment</p>
<p>It also separates the segment ID from the first data field in each segment.</p></td>
</tr>
<tr class="odd">
<td>Component Separator</td>
<td>^</td>
<td>1</td>
<td>Separates adjacent comp­onents of data fields where allowed</td>
</tr>
<tr class="even">
<td>Subcomponent Separator</td>
<td>&amp;</td>
<td>4</td>
<td><p>Separates adjacent subcomp­onents of data fields where allowed</p>
<p>Can be omitted when there are no subcomponents</p></td>
</tr>
<tr class="odd">
<td>Repetition Separator</td>
<td>~</td>
<td>2</td>
<td>Separates multiple occurrences of a field where allowed</td>
</tr>
<tr class="even">
<td>Escape Character</td>
<td>\</td>
<td>3</td>
<td><p>Use with any field represented by an ST, TX or FT data type, or use with the data (fourth) component of the ED data type.</p>
<p>If no escape characters are used in a message, this character can be omitted.</p>
<p>If subcomponents are used in a message, this character must be present.</p></td>
</tr>
</tbody>
</table>

### Position (sequence within the segment)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Position is the ordinal position of the data field within the segment. This number refers to the data field in the text comments that follow the segment definition table. In segment attribute tables, this information is in a column labeled SEQ.

### Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message are required or optional. They occur only once in a message or are allowed to repeat. Each segment has a name and is identified by a unique three-character code known as the Segment ID. For example, the ORU message contains four segments: Message Header (MSH), Patient ID (PID), Observation Request (OBR), and Observation Result (OBX).

Segment tables are used to define the fields and properties of each HL7 segment. These terms are used in the table headings:

| Term         | Description                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------|
| SEQ          | Ordinal position of the data field within the segment                                                    |
| LEN          | Maximum length of data for a specific HL7 field, in characters                                           |
| DT           | HL7 data type                                                                                            |
| Usage        | Defines whether data is required, optional, or conditional for a field                                   |
| Cardinality  | Number of times a data element can repeat within an individual field for a particular segment            |
| TBL#         | Table attribute of the data field definition that specifies the HL7 identifier for a set of coded values |
| Element Name | Name of the referenced component                                                                         |
| HL7 Chapter  | Reference to the *HL7 Messaging Standard*, version 2.4                                                   |

### Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A table is an HL7-defined or user-defined table, as cited in the HL7 Standard.

### Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Usage defines whether data is required, optional, or conditional for a field.

> **NOTE:** The constraints on the HL7 definitions of CE and X of a conforming receiving application must not raise an error, if these fields are populated.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>R</td>
<td>Required</td>
<td><p>A conforming <em>sending</em> application must populate all <strong>R</strong> elements with a non-empty value.</p>
<p>A conforming <em>receiving</em> application must process (save/print/archive, and so on) or ignore the information conveyed by required elements.</p>
<p>A conforming <em>receiving</em> application must not raise an error due to the presence of a required element, but can raise an error due to the absence of a required element.</p></td>
</tr>
<tr class="even">
<td>RE</td>
<td>Required but can be empty</td>
<td><p>The element can be missing from the message, but must be sent by the <em>sending</em> application when there is relevant data.</p>
<p>A conforming <em>sending</em> application must be capable of providing all <strong>RE</strong> elements.</p>
<p>If the conforming <em>sending</em> application knows the required values for the element, it must send that element.</p>
<p>If the conforming <em>sending</em> application does not know the required values, that element is omitted.</p>
<p><em>Receiving</em> applications must process (save/print/archive, and so on) or ignore data contained in the element, but must be able to successfully process the message when the element is omitted</p>
<p>No error message is generated when the element is missing.</p></td>
</tr>
<tr class="odd">
<td>C</td>
<td>Conditional</td>
<td><p>Usage with an associated condition predicate</p>
<p>If the predicate is satisfied:</p>
<p>A conforming <em>sending</em> application must always send the element.</p>
<p>A conforming <em>receiving</em> application must process or ignore data in the element. It can raise an error when the element is not present.</p>
<p>If the predicate is <strong>not</strong> satisfied:</p>
<p>A conforming <em>sending</em> application must <strong>not</strong> send the element.</p>
<p>A conforming <em>receiving</em> application must <strong>not</strong> raise an error when the condition predicate is false, whether the element is present or not.</p></td>
</tr>
<tr class="even">
<td>CE</td>
<td>Conditional but can be empty</td>
<td><p>Usage with an associated condition predicate</p>
<p>If the predicate is satisfied:</p>
<p>If the conforming <em>sending</em> application knows the required values for the element, then the application must send the element.</p>
<p>If the conforming <em>sending</em> application does not know the values required for this element, the element is omitted.</p>
<p>The conforming <em>sending</em> application must be capable of knowing the element (when the predicate is true) for all CE elements.</p>
<p>If the element is present, the conforming <em>receiving</em> application must process (display/print/archive, and so on) or ignore the values of that element.</p>
<p>If the element is <strong>not</strong> present, the conforming <em>receiving</em> application must <strong>not</strong> raise an error due to the presence or absence of the element.</p>
<p>If the predicate is <strong>not</strong> satisfied:</p>
<p>A conforming <em>sending</em> application must <strong>not</strong> send the element.</p>
<p>A conforming <em>receiving</em> application must <strong>not</strong> raise an error when the condition predicate is false, whether the element is present or not.</p></td>
</tr>
<tr class="odd">
<td>B</td>
<td>Retained for backward compatibility</td>
<td><p>A conforming <em>sending</em> application can populate this element.<br />
(This element was deprecated in the HL7 Standard and can be withdrawn from a future version of the Standard.)</p>
<p>A conforming <em>receiving</em> application must process (save/print/archive/and so on) or ignore the information conveyed.</p>
<p>A conforming <em>receiving</em> application must not raise an error due to the presence or absence of a deprecated element.</p></td>
</tr>
<tr class="even">
<td>X</td>
<td>Not supported</td>
<td><p>A conforming <em>sending</em> application does <strong>not</strong> send the element.</p>
<p>A conforming <em>receiving</em> application must ignore the element whether it is sent or not.</p></td>
</tr>
</tbody>
</table>

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[*VistA HL7 Site Manager & Developer Manual*](http://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p56_p66.doc) version 1.6\*56
[HL7 Messaging Standard](https://www.hl7.org/library/bookstore/) version 2.4, American National Standards Institute, 2000
For more information about Vista and HL7 messages, refer to [*Profiles for HL7 Messages from VistA to Commercial Subscriber*](http://www1.va.gov/imaging/docs/VistA_PACS_HL7_Profile_1_2.pdf)
[VistA HL7 - Optimized (HLO) Technical Manual](http://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl_1_6_126_tm.doc)
*This page intentionally left blank*

# Overview of Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 messages are created and transmitted in response to trigger events; real-world events that trigger messages.

- The VistA Rad/Nuc Med package sends an HL7 Order message (ORM) containing exam information to subscriber systems or subscribers whenever an exam is registered, edited, or canceled
- An Observation Results message (ORU) is sent whenever an exam report reaches a status of Verified or Released/Not Verified.
- An Acknowledgment message (ACK) is sent from the receiving system in response to all ORM and ORU messages.

## Patient Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is registered in Rad/Nuc Med, the registration process creates a *registration notification* as an ORM message, which is sent to the subscriber system, subscriber, and/or additional HL7 subscribers (depending on the site’s setup). In return, the receiving system sends an ACK message.

- A patient can be registered for an imaging exam when they arrive for the appointment, or registered up to a week in advance, depending on the VAMC’s policy.
- The ORM message is sent at the time of registration, which is not necessarily the time of the exam.

## Exam Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During an imaging exam, you can edit the exam order in Rad/Nuc Med. The exam editing process creates an *examined notification* as an ORM message, which is broadcast to the subscriber system and/or subscriber. In return, the receiving system sends an ACK message. The ORM format is the same as in the Patient Registration event.

When an examination reaches a predetermined *Examination Status*, the HL7 *Examined* ORM message is broadcast to subscribers. In return, the receiving system sends an ACK message back to VistA. The HL7 ORM format for an Examined event is identical to the HL7 ORM format of a Registration event

> **NOTE:** *Examination Status* is a data attribute of which *Canceled, Waiting for Exam, Called for Exam, Examined, Transcribed, and Complete* are data elements. The ADPAC can set a Radiology parameter to trigger an HL7 ORM Examined message when the exam reaches any one of the specific data elements of the *Examination Status*.

## Exam Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an examination is canceled, the canceling process creates a *cancel notification* as an ORM message, which is broadcast to the subscriber system and/or other HL7 subscribers. In return, the receiving system sends an ACK message.

## Report Verified or Released/Not Verified 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam results can be sent as outbound messages (from Rad/Nuc Med to vendor) or as inbound messages (from vendor to Rad/Nuc Med). These outbound and inbound messages contain the same four segments, but each segment has different required fields.

When an exam report is entered into Rad/Nuc Med by a radiologist or transcriptionist, it moves through a series of report statuses to a Verified (final report) or Released/Not Verified (preliminary report) status. Depending on the policies at a particular VAMC, the Released/Not Verified status may or may not be allowed.

- When an exam report reaches the Verified or Released/Not Verified status in VistA, a *report notification* is created as an ORU message and is broadcast to the subscriber system and/or additional HL7 subscribers. In return, the receiving system sends an ACK message.
- When an exam report is entered into a COTS subscriber system or other non-VistA system, the process is reversed. An ORU message is created and sent from the non-VistA system to Rad/Nuc Med, and in return, Rad/Nuc Med sends an ACK message.

Over the lifecycle of a case, multiple ORUs can be created and broadcast for a single imaging exam. For example, as soon as a preliminary report is available for an exam, an ORU for the *Released/Not Verified report* is broadcast.

- When the final verified report is available, another ORU message is broadcast to replace the previous message.
- When a *Verified report* is retracted or unverified and reverified later, a second ORU message is broadcast with the amended, reverified report.

# Order Entry/Update Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This transaction is used by VistA Radiology to inform the subscriber of a new order. It also allows VistA Radiology to inform the subscriber that an order was canceled or updated.

![](ra5-158-hl7-interface-specification/002.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Actor: VistA Radiology

Role: Notifies ancillary VistA Modules and clinical systems when VistA Radiology orders are placed or updated.

Actor: Subscriber

Role: Receives order entry and update messages. Optionally, maintains the DICOM Modality Worklist.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actors in this use case shall perform the behaviors shown in the following activity diagram.

![](ra5-158-hl7-interface-specification/003.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA and the subscribers shall generate and process HL7 messages according to the following functional and business requirements.

### ORM - Order Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rad/Nuc Med sends ORM messages to subscribers when an order is registered, examined, or cancelled.

The function of the order message is to transmit order information. The trigger events for an ORM message are patient registration, when an exam reaches the *Examined* status, and cancelling an exam.

ORM messages contain the following seven segments.

| Segment | Order Message          | HL7 Chapter |
|---------|------------------------|-------------|
| MSH     | Message header         | 2           |
| PID     | Patient identification | 3           |
| PV1     | Patient Visit          | 3           |
| ORC     | Common order           | 4           |
| OBR     | Order detail           | 4           |
| ZDS     | User Defined           | N/A         |
| OBX     | Observation/Result     | 7           |

For examples of ORM messages, refer to [Appendix A](#this-page-intentionally-left-blank).

### ACK - Acknowledgment Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Return Original Mode ACK

The subscriber needs to return an ACK application acknowledgment, as defined in the HL7 Standard and prescribed by the IHE Radiology Technical Framework. The trigger event of the acknowledgment message must be equal to the trigger event of the message that was received.

#### Send MSA Segment for AE and AR conditions

When an error occurs, subscriber must return the acknowledgment code AE (Application Error) or AR (Application Reject) as appropriate.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 messages must be populated and processed according to the following abstract message definitions.

### Order Message (ORM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Segment         | ORM Message                           | Usage | Cardinality | HL7 Chapter |
|-----------------|---------------------------------------|-------|-------------|-------------|
| MSH             | Message Header                        | R     | \[1..1\]    | 2           |
| \[ { NTE } \]   | Notes and Comments (for Header)       | X     | \[0..0\]    | 2           |
| \[              |                                       |       |             |             |
| PID             | Patient Identification                | R     | \[1..1\]    | 3           |
| \[ PD1 \]       | Additional Demographics               | X     | \[0..0\]    | 3           |
| \[ { NTE } \]   | Notes and Comments (for Patient ID)   | X     | \[0..0\]    | 2           |
| \[ PV1          | Patient Visit                         | R     | \[1..1\]    | 3           |
| \[ PV2 \] \]    | Patient Visit – Additional Info.      | X     | \[0..0\]    | 3           |
| \[ { IN1        | Insurance                             | X     | \[0..0\]    | 6           |
| \[ IN2 \]       | Insurance Additional Info.            | X     | \[0..0\]    | 6           |
| \[ \[ IN3 \] \] | Insurance Additional Info. – Cert.    | X     | \[0..0\]    | 6           |
| \[ { GT1 } \]   | Guarantor                             | X     | \[0..0\]    | 6           |
| \[ { AL1 } \]   | Allergy Information                   | X     | \[0..0\]    | 3           |
| \]              |                                       |       |             |             |
| { ORC           | Common Order                          | R     | \[1..1\]    | 4           |
| \[ OBR          | Observation Request                   | R     | \[1..1\]    | 4           |
| ZDS             | Additional Identification Information | R     | \[1..1\]    | 1F[^2]      |
| \[ { NTE } \]   | Notes and Comments (for Detail)       | X     | \[0..0\]    | 2           |
| \[ { DG1 } \]   | Diagnosis                             | X     | \[0..0\]    | 6           |
| \[ { OBX        | Observation/Result                    | RE    | \[0..999\]  | 7           |
| \[ { NTE } \]   | Notes and Comments (for Results)      | X     | \[0..0\]    | 2           |
| } \] \]         |                                       |       |             |             |
| { \[ CTI \] }   | Clinical Trial Information            | X     | \[0..0\]    | 7           |
| \[ BLG \]       | Billing Segment                       | X     | \[0..0\]    | 4           |
| }               |                                       |       |             |             |

### Acknowledgment Message (ACK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Segment   | ACK Message            | Usage | Cardinality | HL7 Chapter |
|-----------|------------------------|-------|-------------|-------------|
| MSH       | Message Header         | R     | \[1..1\]    | 2           |
| MSA       | Message Acknowledgment | R     | \[1..1\]    | 2           |
| \[ ERR \] | Error                  | RE    | \[0..1\]    | 2           |

## Static Definition – Segment Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fields in HL7 messages must be populated and processed according to the following Segment Attribute Tables.

### MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of all the fields defined for the MSH Segment in HL7, and their usage in the order message.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Seq</th>
<th>Len</th>
<th>DT</th>
<th>Usage</th>
<th>Cardinality</th>
<th>TBL#</th>
<th>Item #</th>
<th>Element Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00001</td>
<td>Field Separator</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00002</td>
<td>Encoding Characters</td>
</tr>
<tr class="odd">
<td>3</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td>[1..1]</td>
<td>0361</td>
<td>00003</td>
<td>Sending Application</td>
</tr>
<tr class="even">
<td>4</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td>[1..1]</td>
<td>0362</td>
<td>00004</td>
<td>Sending Facility</td>
</tr>
<tr class="odd">
<td>5</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td>[1..1]</td>
<td>0361</td>
<td>00005</td>
<td>Receiving Application</td>
</tr>
<tr class="even">
<td>6</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td>[1..1]</td>
<td>0362</td>
<td>00006</td>
<td>Receiving Facility</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00007</td>
<td>Date/Time of Message</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00008</td>
<td>Security</td>
</tr>
<tr class="odd">
<td>9</td>
<td>13</td>
<td>CM</td>
<td>R</td>
<td>[1..1]</td>
<td><p>0076</p>
<p>0003</p></td>
<td>00009</td>
<td>Message Type</td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00010</td>
<td>Message Control ID</td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>PT</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00011</td>
<td>Processing ID</td>
</tr>
<tr class="even">
<td>12</td>
<td>60</td>
<td>VID</td>
<td>R</td>
<td>[1..1]</td>
<td>0104</td>
<td>00012</td>
<td>Version ID</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00013</td>
<td>Sequence Number</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00014</td>
<td>Continuation Pointer</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td>X</td>
<td>[0..0]2F<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>0155</td>
<td>00015</td>
<td>Accept Acknowledgment Type</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td>X</td>
<td>[0..0]3F<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td>0155</td>
<td>00016</td>
<td>Application Acknowledgment Type</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00017</td>
<td>Country Code</td>
</tr>
<tr class="even">
<td>18</td>
<td>16</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0211</td>
<td>00692</td>
<td>Character Set</td>
</tr>
<tr class="odd">
<td>19</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00693</td>
<td>Principal Language of Message</td>
</tr>
<tr class="even">
<td>20</td>
<td>20</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0356</td>
<td>01317</td>
<td>Alternate Character Set Handling Scheme</td>
</tr>
<tr class="odd">
<td>21</td>
<td>10</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01598</td>
<td>Conformance Statement ID</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p> Patch 107 January 2012 Updated the description of MSH Segment; for ORMs and ORUs Seq 15: Usage is <strong>X</strong> <strong>Not required</strong> and Cardinality is <strong>0..0</strong>.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p> Patch 107 January 2012 Updated the description of MSH Segment; for ORMs and ORUs Seq 16: Usage is <strong>X</strong> <strong>Not required</strong> and Cardinality is <strong>0..0</strong>.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of all the fields defined for the PID Segment in HL7, and their usage in the order message.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Item \# | Element Name                      |
|-----|-----|-----|-------|-------------|------|---------|-----------------------------------|
| 1   | 4   | SI  | X     | \[0..0\]    |      | 00104   | Set ID – PID                      |
| 2   | 20  | CX  | R     | \[1..1\]    |      | 00105   | Patient ID                        |
| 3   | 250 | CX  | R     | \[1..1\]    |      | 00106   | Patient Identifier List           |
| 4   | 20  | CX  | R     | \[1..1\]    |      | 00107   | Alternate Patient ID – PID        |
| 5   | 250 | XPN | R     | \[1..1\]    |      | 00108   | Patient Name                      |
| 6   | 250 | XPN | X     | \[0..0\]    |      | 00109   | Mother’s Maiden Name              |
| 7   | 26  | TS  | RE    | \[0..1\]    |      | 00110   | Date/Time of Birth                |
| 8   | 1   | IS  | RE    | \[0..1\]    | 0001 | 00111   | Sex                               |
| 9   | 250 | XPN | X     | \[0..0\]    |      | 00112   | Patient Alias                     |
| 10  | 250 | CE  | RE    | \[0..1\]    | 0005 | 00113   | Race                              |
| 11  | 250 | XAD | RE    | \[0..1\]    |      | 00114   | Patient Address                   |
| 12  | 4   | IS  | X     | \[0..0\]    | 0289 | 00115   | County Code                       |
| 13  | 250 | XTN | RE    | \[0..1\]    |      | 00116   | Phone Number – Home               |
| 14  | 250 | XTN | RE    | \[0..1\]    |      | 00117   | Phone Number – Business           |
| 15  | 250 | CE  | X     | \[0..0\]    | 0296 | 00118   | Primary Language                  |
| 16  | 250 | CE  | X     | \[0..0\]    | 0002 | 00119   | Marital Status                    |
| 17  | 250 | CE  | X     | \[0..0\]    | 0006 | 00120   | Religion                          |
| 18  | 250 | CX  | X     | \[0..0\]    |      | 00121   | Patient Account Number            |
| 19  | 16  | ST  | R     | \[1..1\]    |      | 00122   | SSN Number – Patient              |
| 20  | 25  | DLN | X     | \[0..0\]    |      | 00123   | Driver’s License Number – Patient |
| 21  | 250 | CX  | X     | \[0..0\]    |      | 00124   | Mother’s Identifier               |
| 22  | 250 | CE  | RE    | \[0..1\]    | 0189 | 00125   | Ethnic Group                      |
| 23  | 250 | ST  | X     | \[0..0\]    |      | 00126   | Birth Place                       |
| 24  | 1   | ID  | X     | \[0..0\]    | 0136 | 00127   | Multiple Birth Indicator          |
| 25  | 2   | NM  | X     | \[0..0\]    |      | 00128   | Birth Order                       |
| 26  | 250 | CE  | X     | \[0..0\]    | 0171 | 00129   | Citizenship                       |
| 27  | 250 | CE  | X     | \[0..0\]    | 0172 | 00130   | Veterans Military Status          |
| 28  | 250 | CE  | X     | \[0..0\]    | 0212 | 00739   | Nationality                       |
| 29  | 26  | TS  | X     | \[0..0\]    |      | 00740   | Patient Death Date and Time       |
| 30  | 1   | ID  | X     | \[0..0\]    | 0136 | 00741   | Patient Death Indicator           |
| 31  | 1   | ID  | X     | \[0..0\]    | 0136 | 01535   | Identity Unknown Indicator        |
| 32  | 20  | IS  | X     | \[0..0\]    | 0445 | 01536   | Identity Reliability Code         |
| 33  | 26  | TS  | X     | \[0..0\]    |      | 01537   | Last Update Date/Time             |
| 34  | 40  | HD  | X     | \[0..0\]    |      | 01538   | Last Update Facility              |
| 35  | 250 | CE  | X     | \[0..0\]    | 0446 | 01539   | Species Code                      |
| 36  | 250 | CE  | X     | \[0..0\]    | 0447 | 01540   | Breed Code                        |
| 37  | 80  | ST  | X     | \[0..0\]    |      | 01541   | Strain                            |
| 38  | 250 | CE  | X     | \[0..0\]    | 0429 | 01542   | Production Class Code             |

### PV1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of all the fields defined for the PV1 Segment in HL7, together with their usage in the VistA order message.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Item \# | Element Name              |
|-----|-----|-----|-------|-------------|------|---------|---------------------------|
| 1   | 4   | SI  | X     | \[0..0\]    |      | 00131   | Set ID – PV1              |
| 2   | 1   | IS  | R     | \[1..1\]    | 0004 | 00132   | Patient Class             |
| 3   | 80  | PL  | C     | \[0..1\]    |      | 00133   | Assigned Patient Location |
| 4   | 2   | IS  | X     | \[0..0\]    | 0007 | 00134   | Admission Type            |
| 5   | 250 | CX  | X     | \[0..0\]    |      | 00135   | Pre-admit Number          |
| 6   | 80  | PL  | X     | \[0..0\]    |      | 00136   | Prior Patient Location    |
| 7   | 250 | XCN | CE    | \[0..1\]    | 0010 | 00137   | Attending Doctor          |
| 8   | 250 | XCN | RE    | \[0..1\]    | 0010 | 00138   | Referring Doctor          |
| 9   | 250 | XCN | X     | \[0..0\]    | 0010 | 00139   | Consulting Doctor         |
| 10  | 30  | IS  | C     | \[0..1\]    | 0069 | 00140   | Hospital Service          |
| 11  | 80  | PL  | C     | \[0..0\]    |      | 00141   | Temporary Location        |
| 12  | 2   | IS  | X     | \[0..0\]    | 0087 | 00142   | Pre-admit Test Indicator  |
| 13  | 2   | IS  | X     | \[0..0\]    | 0092 | 00143   | Re-admission Indicator    |
| 14  | 6   | IS  | X     | \[0..0\]    | 0023 | 00144   | Admit Source              |
| 15  | 2   | IS  | RE    | \[0..2\]    | 0009 | 00145   | Ambulatory Status         |
| 16  | 2   | IS  | RE    | \[0..1\]    | 0099 | 00146   | VIP Indicator             |
| 17  | 250 | XCN | X     | \[0..0\]    | 0010 | 00147   | Admitting Doctor          |
| 18  | 2   | IS  | X     | \[0..0\]    | 0018 | 00148   | Patient Type              |
| 19  | 250 | CX  | R     | \[1..1\]    |      | 00149   | Visit Number              |
| 20  | 50  | FC  | X     | \[0..0\]    | 0064 | 00150   | Financial Class           |
| 21  | 2   | IS  | X     | \[0..0\]    | 0032 | 00151   | Charge Price Indicator    |
| 22  | 2   | IS  | X     | \[0..0\]    | 0045 | 00152   | Courtesy Code             |
| 23  | 2   | IS  | X     | \[0..0\]    | 0046 | 00153   | Credit Rating             |
| 24  | 2   | IS  | X     | \[0..0\]    | 0044 | 00154   | Contract Code             |
| 25  | 8   | DT  | X     | \[0..0\]    |      | 00155   | Contract Effective Date   |
| 26  | 12  | NM  | X     | \[0..0\]    |      | 00156   | Contract Amount           |
| 27  | 3   | NM  | X     | \[0..0\]    |      | 00157   | Contract Period           |
| 28  | 2   | IS  | X     | \[0..0\]    | 0073 | 00158   | Interest Code             |
| 29  | 1   | IS  | X     | \[0..0\]    | 0110 | 00159   | Transfer to Bad Debt Code |
| 30  | 8   | DT  | X     | \[0..0\]    |      | 00160   | Transfer to Bad Debt Date |
| 31  | 10  | IS  | X     | \[0..0\]    | 0021 | 00161   | Bad Debt Agency Code      |
| 32  | 12  | NM  | X     | \[0..0\]    |      | 00162   | Bad Debt Transfer Amount  |
| 33  | 12  | NM  | X     | \[0..0\]    |      | 00163   | Bad Debt Recovery Amount  |
| 34  | 1   | IS  | X     | \[0..0\]    | 0111 | 00164   | Delete Account Indicator  |
| 35  | 8   | DT  | X     | \[0..0\]    |      | 00165   | Delete Account Date       |
| 36  | 3   | IS  | X     | \[0..0\]    | 0112 | 00166   | Discharge Disposition     |
| 37  | 25  | CM  | X     | \[0..0\]    | 0113 | 00167   | Discharged to Location    |
| 38  | 250 | CE  | X     | \[0..0\]    | 0114 | 00168   | Diet Type                 |
| 39  | 2   | IS  | X     | \[0..0\]    | 0115 | 00169   | Servicing Facility        |
| 40  | 1   | IS  | X     | \[0..0\]    | 0116 | 00170   | Bed Status                |
| 41  | 2   | IS  | X     | \[0..0\]    | 0117 | 00171   | Account Status            |
| 42  | 80  | PL  | X     | \[0..0\]    |      | 00172   | Pending Location          |
| 43  | 80  | PL  | X     | \[0..0\]    |      | 00173   | Prior Temporary Location  |
| 44  | 26  | TS  | X     | \[0..0\]    |      | 00174   | Admit Date/Time           |
| 45  | 26  | TS  | X     | \[0..0\]    |      | 00175   | Discharge Date/Time       |
| 46  | 12  | NM  | X     | \[0..0\]    |      | 00176   | Current Patient Balance   |
| 47  | 12  | NM  | X     | \[0..0\]    |      | 00177   | Total Charges             |
| 48  | 12  | NM  | X     | \[0..0\]    |      | 00178   | Total Adjustments         |
| 49  | 12  | NM  | X     | \[0..0\]    |      | 00179   | Total Payments            |
| 50  | 250 | CX  | X     | \[0..0\]    | 0203 | 00180   | Alternate Visit ID        |
| 51  | 1   | IS  | X     | \[0..0\]    | 0326 | 01226   | Visit Indicator           |
| 52  | 250 | XCN | X     | \[0..0\]    | 0010 | 01274   | Other Healthcare Provider |

### ORC Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of all the fields defined for the ORC Segment in HL7.

| Seq | Len | DT  | Usage | Cardinality | TBL#             | Item \# | Element Name                     |
|-----|-----|-----|-------|-------------|------------------|---------|----------------------------------|
| 1   | 2   | ID  | R     | \[1..1\]    | 0119             | 00215   | Order Control                    |
| 2   | 22  | EI  | R     | \[1..1\]    |                  | 00216   | Placer Order Number              |
| 3   | 22  | EI  | R     | \[1..1\]    |                  | 00217   | Filler Order Number              |
| 4   | 35  | EI  | RE    | \[1..1\]    |                  | 00218   | Placer Group Number              |
| 5   | 2   | ID  | R     | \[1..1\]    | 0038             | 00219   | Order Status                     |
| 6   | 1   | ID  | X     | \[0..0\]    | 0121             | 00220   | Response Flag                    |
| 7   | 200 | TQ  | R     | \[1..1\]    |                  | 00221   | Quantity/Timing                  |
| 8   | 200 | CM  | RE    | \[0..1\]    |                  | 00222   | Parent                           |
| 9   | 26  | TS  | R     | \[1..1\]    |                  | 00223   | Date/Time of Transaction         |
| 10  | 250 | XCN | R     | \[1..1\]    |                  | 00224   | Entered By                       |
| 11  | 250 | XCN | X     | \[0..0\]    |                  | 00225   | Verified By                      |
| 12  | 250 | XCN | RE    | \[0..1\]    |                  | 00226   | Ordering Provider                |
| 13  | 80  | PL  | RE    | \[0..1\]    |                  | 00227   | Enterer’s Location               |
| 14  | 250 | XTN | RE    | \[0..8\]    |                  | 00228   | Call Back Phone Number           |
| 15  | 26  | TS  | X     | \[0..0\]    |                  | 00229   | Order Effective Date/Time        |
| 16  | 250 | CE  | X     | \[0..0\]    |                  | 00230   | Order Control Code Reason        |
| 17  | 250 | CE  | RE    | \[0..1\]    |                  | 00231   | Entering Organization            |
| 18  | 250 | CE  | X     | \[0..0\]    |                  | 00232   | Entering Device                  |
| 19  | 250 | XCN | X     | \[0..0\]    |                  | 00233   | Action By                        |
| 20  | 250 | CE  | X     | \[0..0\]    | [0339](#HL70339) | 01310   | Advanced Beneficiary Notice Code |
| 21  | 250 | XON | X     | \[0..0\]    |                  | 01311   | Ordering Facility Name           |
| 22  | 250 | XAD | X     | \[0..0\]    |                  | 01312   | Ordering Facility Address        |
| 23  | 250 | XTN | X     | \[0..0\]    |                  | 01313   | Ordering Facility Phone Number   |
| 24  | 250 | XAD | X     | \[0..0\]    |                  | 01314   | Ordering Provider Address        |
| 25  | 250 | CWE | X     | \[0..0\]    |                  | 01473   | Order Status Modifier            |

### OBR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of all the fields defined for the OBR Segment in HL7.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Seq</th>
<th>Len</th>
<th>DT</th>
<th>Usage</th>
<th>Cardinality</th>
<th>TBL#</th>
<th>Item #</th>
<th>Element Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00237</td>
<td>Set ID ‑ OBR</td>
</tr>
<tr class="even">
<td>2</td>
<td>22</td>
<td>EI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00216</td>
<td>Placer Order Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>22</td>
<td>EI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00217</td>
<td>Filler Order Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00238</td>
<td>Universal Service Identifier</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00239</td>
<td>Priority - OBR</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00240</td>
<td>Requested Date/Time</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00241</td>
<td>Observation Date/Time</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00242</td>
<td>Observation End Date/Time</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>CQ</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00243</td>
<td>Collection Volume</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>XCN</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00244</td>
<td>Collector Identifier</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0065</td>
<td>00245</td>
<td>Specimen Action Code</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00246</td>
<td>Danger Code</td>
</tr>
<tr class="odd">
<td>13</td>
<td>300</td>
<td>ST</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00247</td>
<td>Relevant Clinical Information</td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00248</td>
<td>Specimen Received Date/Time</td>
</tr>
<tr class="odd">
<td>15</td>
<td>300</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td><p>0070</p>
<p>0163</p>
<p>0369</p></td>
<td>00249</td>
<td>Specimen Source</td>
</tr>
<tr class="even">
<td>16</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00226</td>
<td>Ordering Provider</td>
</tr>
<tr class="odd">
<td>17</td>
<td>250</td>
<td>XTN</td>
<td>RE</td>
<td>[0..8]</td>
<td></td>
<td>00250</td>
<td>Order Callback Phone Number</td>
</tr>
<tr class="even">
<td>18</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00251</td>
<td>Placer Field 1</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00252</td>
<td>Placer Field 2</td>
</tr>
<tr class="even">
<td>20</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00253</td>
<td>Filler Field 1</td>
</tr>
<tr class="odd">
<td>21</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00254</td>
<td>Filler Field 2</td>
</tr>
<tr class="even">
<td>22</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00255</td>
<td>Results Rpt/Status Chng - Date/Time</td>
</tr>
<tr class="odd">
<td>23</td>
<td>40</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00256</td>
<td>Charge to Practice</td>
</tr>
<tr class="even">
<td>24</td>
<td>10</td>
<td>ID</td>
<td>RE</td>
<td>[0..1]</td>
<td>0074</td>
<td>00257</td>
<td>Diagnostic Serv Sect ID</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0123</td>
<td>00258</td>
<td>Result Status</td>
</tr>
<tr class="even">
<td>26</td>
<td>400</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00259</td>
<td>Parent Result</td>
</tr>
<tr class="odd">
<td>27</td>
<td>200</td>
<td>TQ</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00221</td>
<td>Quantity/Timing</td>
</tr>
<tr class="even">
<td>28</td>
<td>250</td>
<td>XCN</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00260</td>
<td>Result Copies To</td>
</tr>
<tr class="odd">
<td>29</td>
<td>200</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td></td>
<td>00222</td>
<td>Parent</td>
</tr>
<tr class="even">
<td>30</td>
<td>20</td>
<td>ID</td>
<td>RE</td>
<td>[0..1]</td>
<td>0124</td>
<td>00262</td>
<td>Transportation Mode</td>
</tr>
<tr class="odd">
<td>31</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00263</td>
<td>Reason for Study</td>
</tr>
<tr class="even">
<td>32</td>
<td>200</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00264</td>
<td>Principal Result Interpreter</td>
</tr>
<tr class="odd">
<td>33</td>
<td>200</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00265</td>
<td>Assistant Result Interpreter</td>
</tr>
<tr class="even">
<td>34</td>
<td>200</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00266</td>
<td>Technician</td>
</tr>
<tr class="odd">
<td>35</td>
<td>200</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00267</td>
<td>Transcriptionist</td>
</tr>
<tr class="even">
<td>36</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00268</td>
<td>Scheduled Date/Time</td>
</tr>
<tr class="odd">
<td>37</td>
<td>4</td>
<td>NM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01028</td>
<td>Number of Sample Containers</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01029</td>
<td>Transport Logistics of Collected Sample</td>
</tr>
<tr class="odd">
<td>39</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01030</td>
<td>Collector’s Comment</td>
</tr>
<tr class="even">
<td>40</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01031</td>
<td>Transport Arrangement Responsibility</td>
</tr>
<tr class="odd">
<td>41</td>
<td>30</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td><a href="#HL70224">0224</a></td>
<td>01032</td>
<td>Transport Arranged</td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td><a href="#HL70225">0225</a></td>
<td>01033</td>
<td>Escort Required</td>
</tr>
<tr class="odd">
<td>43</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01034</td>
<td>Planned Patient Transport Comment</td>
</tr>
<tr class="even">
<td>44</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0088</td>
<td>00393</td>
<td>Procedure Code</td>
</tr>
<tr class="odd">
<td>45</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0340</td>
<td>01316</td>
<td>Procedure Code Modifier</td>
</tr>
<tr class="even">
<td>46</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td><a href="#HL70411">0411</a></td>
<td>01474</td>
<td>Placer Supplemental Service Information</td>
</tr>
<tr class="odd">
<td>47</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td><a href="#HL70411">0411</a></td>
<td>01475</td>
<td>Filler Supplemental Service Information</td>
</tr>
</tbody>
</table>

### ZDS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the field defined for the ZDS Segment in HL7. For a more detailed explanation of the fields used by VistA, refer to Section 3.6.6 on page [55](#_Ref232824764).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Item \# | Element Name       |
|-----|-----|-----|-------|-------------|------|---------|--------------------|
| 1   | 200 | RP  | R     | \[1..1\]    |      |         | Study Instance UID |

<span id="_OBX_Segment" class="anchor"></span>

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the order message, the OBX Segment is used to communicate ancillary order information including history. The following is a listing of all the fields defined for the OBX Segment in HL7.

| Seq | Len         | DT  | Usage | Cardinality | TBL# | Item \# | Element Name                       |
|-----|-------------|-----|-------|-------------|------|---------|------------------------------------|
| 1   | 4           | SI  | R     | \[1..1\]    |      | 00569   | Set ID – OBX                       |
| 2   | 2           | ID  | R     | \[1..1\]    | 0125 | 00570   | Value Type                         |
| 3   | 250         | CE  | R     | \[1..1\]    |      | 00571   | Observation Identifier             |
| 4   | 20          | ST  | X     | \[0..0\]    |      | 00572   | Observation Sub-ID                 |
| 5   | 655364F[^3] |     | R     | \[1..4\]    |      | 00573   | Observation Value                  |
| 6   | 250         | CE  | X     | \[0..0\]    |      | 00574   | Units                              |
| 7   | 60          | ST  | X     | \[0..0\]    |      | 00575   | Reference Range                    |
| 8   | 5           | IS  | X     | \[0..0\]    | 0078 | 00576   | Abnormal Flags                     |
| 9   | 5           | NM  | X     | \[0..0\]    |      | 00577   | Probability                        |
| 10  | 2           | ID  | X     | \[0..0\]    |      | 00578   | Nature of Abnormal Test            |
| 11  | 1           | ID  | R     | \[1..1\]    | 0085 | 00579   | Observation Result Status          |
| 12  | 26          | TS  | X     | \[0..0\]    |      | 00580   | Date Last Observation Normal Value |
| 13  | 20          | ST  | X     | \[0..0\]    |      | 00581   | User Defined Access Checks         |
| 14  | 26          | TS  | X     | \[0..0\]    |      | 00582   | Date/Time of the Observation       |
| 15  | 250         | CE  | X     | \[0..0\]    |      | 00583   | Producer’s ID                      |
| 16  | 250         | XCN | X     | \[0..0\]    |      | 00584   | Responsible Observer               |
| 17  | 250         | CE  | X     | \[0..0\]    |      | 00936   | Observation Method                 |
| 18  | 22          | EI  | X     | \[0..0\]    |      | 01479   | Equipment Instance Identifier      |
| 19  | 26          | TS  | X     | \[0..0\]    |      | 01480   | Date/Time of the Analysis          |

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSA is used only in the acknowledgment message. The following is a listing of all the fields defined for the MSA Segment in HL7.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Item \# | Element Name                |
|-----|-----|-----|-------|-------------|------|---------|-----------------------------|
| 1   | 2   | ID  | R     | \[1..1\]    | 0003 | 00018   | Acknowledgment Code         |
| 2   | 20  | ST  | R     | \[1..1\]    |      | 00010   | Message Control ID          |
| 3   | 80  | ST  | B     | \[0..1\]    |      | 00020   | Text Message                |
| 4   | 15  | NM  | X     | \[0..0\]    |      | 00021   | Expected Sequence Number    |
| 5   | 1   | ID  | X     | \[0..0\]    | 0102 | 00022   | Delayed Acknowledgment Type |
| 6   | 250 | CE  | B     | \[0..1\]    |      | 00023   | Error Condition             |

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Header segment is used in ORM and ORU messages. A description of each MSH field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values                                             |
|---------|--------|-------|---------------------------------------------------------------------------|
| MSH     | 1      | R     | Field Separator (determined by VistA HL7 package set-up)                  |
|         | 2      | R     | Encoding Characters (determined by VistA HL7 package set-up)              |
|         | 3      | R     | Sending Application (determined by VistA HL7 package set-up or by vendor) |
|         | 4      | R     | Sending Facility (determined by VistA HL7 package set-up or by vendor)    |
|         | 5      | R     | Receiving Application (determined by VistA HL7 package set-up)            |
|         | 6      | R     | Receiving Facility (determined by VistA HL7 package set-up)               |
|         | 7      | R     | Date/Time of Message                                                      |
|         | 8      | X     | Security                                                                  |
|         | 9      | R     | Message Type and Event Code                                               |
|         | 10     | R     | Message Control ID (determined by VistA HL7 package or by vendor)         |
|         | 11     | R     | Processing ID (determined by VistA HL7 Package set-up)                    |
|         | 12     | R     | Version ID (determined by VistA HL7Package set-up)                        |
|         | 13     | X     | Sequence Number                                                           |
|         | 14     | X     | Continuation Pointer                                                      |
|         | 15     | X     | Accept Acknowledgment Type                                                |
|         | 16     | X     | Application Acknowledgment Type                                           |
|         | 17     | R     | Country Code (determined by VistA HL7 Package set-up)                     |
|         | 18     | X     | Character Set                                                             |
|         | 19     | X     | Principal Language of Message                                             |
|         | 20     | X     | Alternate Character Set Handling Scheme                                   |
|         | 21     | X     | Conformance Statement ID                                                  |

#### MSH-1-Field Separator

This field contains the top-level delimiter for HL7 elements within segments.

#### MSH-2-Encoding Characters

This field contains the component separator (secondary element delimiter), repetition separator, escape character, and subcomponent separator (tertiary element delimiter).

#### MSH-3-Sending Application

This field contains three components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Universal ID      |
| 3   | 20  | ID  | X     | \[0..0\]    | 0301 | Universal ID Type |

In the VistA order message, the first component of this field is populated with the value RA-SERVER-IMG from user-defined Table 0361, *Sending/Receiving Application*. The subscriber returns this value in component MSH-5.1 of the acknowledgment message. The second and third components of MSH-3 are not valued.

#### MSH-4-Sending Facility 5F[^4]

This field contains three components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Universal ID      |
| 3   | 20  | ID  | X     | \[0..0\]    | 0301 | Universal ID Type |

In the VistA message, the first component of this field is populated from user-defined Table 0362, *Sending/Receiving Facility*, with the name of the medical center at which the message was generated. The subscriber returns this value in component MSH-6.1 of the acknowledgment message.

#### MSH-5-Receiving Application

This field contains three components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Universal ID      |
| 3   | 20  | ID  | X     | \[0..0\]    | 0301 | Universal ID Type |

In the VistA message, the first component of this field is populated from user-defined Table 0361, *Sending/Receiving Application*, with the name of the subscriber application. The subscriber returns this value in component MSH-3.1 of the acknowledgment message. The second and third components of MSH-5 are not valued.

#### MSH-6-Receiving Facility

This field contains three components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Universal ID      |
| 3   | 20  | ID  | X     | \[0..0\]    | 0301 | Universal ID Type |

In the VistA message, the first component of this field is populated from user-defined Table 0362, Sending/Receiving Facility, with the name of the medical center at which the message was received. The subscriber returns this value in field MSH-4 of the acknowledgment message. The second and third components of MSH-6 are not valued.

#### MSH-7-Date/Time of Message

This field contains the date and time of the sending system that built the message.

#### MSH-9-Message Type

This field contains three components used by VistA.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 3   | ID  | R     | \[1..1\]    | 0076 | Message Type      |
| 2   | 3   | ID  | R     | \[1..1\]    | 0003 | Trigger Event     |
| 3   | 7   | ID  | X     | \[0..0\]    | 0354 | Message Structure |

#### MSH-9.1-Message Type

This component is populated with a value from HL7 Table 0076, *Message Type*. For the order message, it always contains the value ORM.

For the observation result message, it always contains the value ORU.

#### MSH-9.2-Trigger Event

This component is populated with a value from HL7 Table 0003, *Event Type*. For the order message, it always contains the value O01 (letter O\> digit 0\>number 1).

For the observation result message, it always contains the value R01.

#### MSH-10-Message Control ID

This field contains a unique identifier for the message.

#### MSH-11-Processing ID

This field contains two components used by VistA.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name    |
|-----|-----|-----|-------|-------------|------|-----------------|
| 1   | 1   | ID  | R     | \[1..1\]    | 0103 | Processing ID   |
| 2   | 1   | ID  | RE    | \[0..1\]    | 0207 | Processing Mode |

#### MSH-11.1-Processing ID

This component is populated with one of the following values from HL7 Table 0103, *Processing ID.*

| Value | Description |
|-------|-------------|
| P     | Production  |
| D     | Debugging   |
| T     | Training    |

#### MSH-11.2-Processing Mode

This component is populated with one of the following values from HL7 Table 0207, *Processing Mode*.

| Value       | Description                                                           |
|-------------|-----------------------------------------------------------------------|
| A           | Archive                                                               |
| R           | Restore from archive                                                  |
| I           | Initial load                                                          |
| T           | Current processing, transmitted at intervals (scheduled or on demand) |
| not present | Not present (the default, meaning *current* processing)               |

#### MSH-12-Version ID

This field contains three components. The first component always contains a value from v2.3.1 from HL7 Table 0104, *Version ID*. Other components of this field are not used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name              |
|-----|-----|-----|-------|-------------|------|---------------------------|
| 1   | 10  | ID  | R     | \[1..1\]    | 0104 | Version ID                |
| 2   | 250 | CE  | X     | \[0..0\]    |      | Internationalization Code |
| 3   | 250 | CE  | X     | \[0..0\]    |      | Internal Version ID       |

Although the VistA message pre-adopts certain v2.4 structures, such as the ROL segment, receivers that are unable to recognize v2.4 can use v2.3.1 syntax rules as prescribed by IHE. Receivers not now using HL7 v2.3.1 can process the v2.3.1 messages according to the HL7 rules for backward compatibility. When IHE is revised to a newer version of HL7, receivers must adapt to the new structures within a stated period of time following the revision.

#### MSH-15-Accept Acknowledgment Type

This field contains the conditions under which accept acknowledgments are required in response to this message. The field is required for enhanced acknowledgment mode.

| Value | Text                         |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/Reject conditions only |
| SU    | Successful completion only   |

#### MSH-16-Application Acknowledgment Type

This field contains the conditions under which application acknowledgments are required in response to this message. The field is required for enhanced acknowledgment mode.

| Value | Text                         |
|-------|------------------------------|
| AL    | Always                       |
| NE    | Never                        |
| ER    | Error/Reject conditions only |
| SU    | Successful completion only   |

> **NOTE:** If MSH-15-Accept Acknowledgment Type and MSH-16-Application Acknowledgment Type are omitted, (or are both Null), the original acknowledgment mode rules are used.

#### MSH-17-Country Code

This field always contains the value USA from the ISO 3166 country code table.

For an explanation of the MSH segment fields used in the VistA order and report messages, refer to 3.6.1 MSH Segment Fields on page [23](#msh-segment-fields-in-orm-and-oru).

### PID Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Identification segment is used in ORM and ORU messages. A description of each PID field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values     |
|---------|--------|-------|-----------------------------------|
| PID     | 1      | X     | Set ID – PID                      |
|         | 2      | R     | Patient ID                        |
|         | 3      | R     | Patient Identifier List           |
|         | 4      | R     | Alternate Patient ID-PID          |
|         | 5      | R     | Patient Name                      |
|         | 6      | X     | Mother’s Maiden Name              |
|         | 7      | RE    | Date/Time of Birth                |
|         | 8      | RE    | Sex                               |
|         | 9      | X     | Patient Alias                     |
|         | 10     | RE    | Race                              |
|         | 11     | RE    | Patient Address                   |
|         | 12     | X     | County Code                       |
|         | 13     | RE    | Phone Number – Home               |
|         | 14     | RE    | Phone Number – Business           |
|         | 15     | X     | Primary Language                  |
|         | 16     | X     | Marital Status                    |
|         | 17     | X     | Religion                          |
|         | 18     | X     | Patient Account Number            |
|         | 19     | R     | SS Number – Patient               |
|         | 20     | X     | Driver’s License Number – Patient |
|         | 21     | X     | Mother’s Identifier               |
|         | 22     | RE    | Ethnic Group                      |
|         | 23     | X     | Birth Place                       |
|         | 24     | X     | Multiple Birth Indicator          |
|         | 25     | X     | Birth Order                       |
|         | 26     | X     | Citizenship                       |
|         | 27     | X     | Veterans Military Status          |
|         | 28     | X     | Nationality                       |
|         | 29     | X     | Patient Death Date and Time       |
|         | 30     | X     | Patient Death Indicator           |
|         | 31     | X     | Identity Unknown Indicator        |
|         | 32     | X     | Identity Reliability Code         |
|         | 33     | X     | Last Update Date/Time             |
|         | 34     | X     | Last Update Facility              |
|         | 35     | X     | Species Code                      |
|         | 36     | X     | Breed code                        |
|         | 37     | X     | Strain                            |
|         | 38     | X     | Production Class Code             |

### PID-2-Patient ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the station number and patient file internal entry number (DFN).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 20  | ID  | R     | \[1..1\]    |      | ID                                               |
| 2   | 2   | ST  | X     | \[0..0\]    |      | Check Digit                                      |
| 3   | 250 | CE  | X     | \[0..0\]    | 0061 | Code Identifying the Check Digit Scheme Employed |
| 4   | 180 | HD  | R     | \[1..1\]    | 0363 | Assigning Authority                              |
| 5   | 20  | ID  | R     | \[1..1\]    | 0203 | Identifier Type Code                             |
| 6   | 180 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |

The following components are valued.

#### PID-2.1-ID

This component is populated with the station number and DFN (patient file internal entry number).

The format of this component is mmm-nnnnnnnn, where mmm is the station number and nnnnnnnn (1-8 characters, not zero-filled) is the DFN.

#### PID-2.4-Assigning Authority

This component is populated with the entity that assigned the identifier value in PID-2.1-ID.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | RE    | \[0..1\]    |      | Universal ID      |
| 3   | 20  | ID  | CE    | \[0..1\]    | 0301 | Universal ID Type |

At present, only the first subcomponent is considered for identifying the assigning authority. Subcomponent 1 contains the value USVHA, meaning United States Veterans Health Administration, from user-defined Table 0300, Namespace ID.

In the future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-2.5-Identifier Type

The component is populated with a value that distinguishes the kind of identifier contained in PID-2.1-ID. It contains the value PI, meaning Patient Identifier, from user-defined Table 0203, *Identifier Type*.

#### PID-3-Patient Identifier List 

This field contains six components that transmit the patient Social Security Number (SSN). Other components of this field are not used. Within each repetition, the components are valued.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 20  | ID  | R     | \[1..1\]    |      | ID                                               |
| 2   | 2   | ST  | X     | \[0..0\]    |      | Check Digit                                      |
| 3   | 250 | CE  | X     | \[0..0\]    | 0061 | Code Identifying the Check Digit Scheme Employed |
| 4   | 180 | HD  | R     | \[1..1\]    | 0363 | Assigning Authority                              |
| 5   | 20  | ID  | R     | \[1..1\]    | 0203 | Identifier Type Code                             |
| 6   | 180 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |

#### PID-3.1-ID

This component is populated with the Social Security Number.

#### PID-3.4-Assigning Authority

This component is populated with three subcomponents and identifies the entity that assigned the identifier value in *PID-3.1-ID*.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | RE    | \[0..1\]    |      | Universal ID      |
| 3   | 20  | ID  | RE    | \[0..1\]    | 0301 | Universal ID Type |

At present, only the first subcomponent identifies the assigning authority. Subcomponent 1 contains the value USVHA*,* meaning United States Veterans Health Administration, from user-defined Table 0300, *Namespace ID*.

In the future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-3.5-Identifier Type

This component is populated with the kind of identifier in *PID-3.1-ID*. It contains the fixed value, NI (National Identifier), from user-defined Table 0203, *Identifier Type*.

> Note: NI, which is used by the VA, is the Integration Control Number found in PID-3.1.

#### PID-4-Alternate Patient ID

This field contains the patient Integration Control Number (ICN).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 20  | ID  | R     | \[1..1\]    |      | ID                                               |
| 2   | 2   | ST  | X     | \[0..0\]    |      | Check Digit                                      |
| 3   | 250 | CE  | X     | \[0..0\]    | 0061 | Code Identifying the Check Digit Scheme Employed |
| 4   | 180 | HD  | R     | \[1..1\]    | 0363 | Assigning Authority                              |
| 5   | 20  | ID  | R     | \[1..1\]    | 0203 | Identifier Type Code                             |
| 6   | 180 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |

The following components are valued.

#### PID-4.1-ID

This component is populated with an alphanumeric identification string.

#### PID-4.4-Assigning Authority

This component is populated with the entity that assigned the identifier value in PID-4.1-ID.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name      |
|-----|-----|-----|-------|-------------|------|-------------------|
| 1   | 20  | IS  | R     | \[1..1\]    | 0300 | Namespace ID      |
| 2   | 250 | ST  | RE    | \[0..1\]    |      | Universal ID      |
| 3   | 20  | ID  | CE    | \[0..1\]    | 0301 | Universal ID Type |

At present, only the first subcomponent identifies the assigning authority. Subcomponent 1 contains the value USVHA, meaning United States Veterans Health Administration, from user-defined Table 0300, *Namespace ID*.

In the future, the assigning authority may be designated as an Object Identifier (OID) in the second and third subcomponents of Component 4.

#### PID-4.5-Identifier Type

This component is populated with the value that distinguishes the kind of identifier contained in PID-4.1-ID. It contains the value NI, meaning National Unique Individual Identifier, from user-defined Table 0203, *Identifier Type*.

#### PID-5-Patient Name

This field contains the following components. Component 7, Name Type Code, indicates the type of name given in Components 1-6, such as legal, birth name, or alias. At present, VistA only uses name type L (legal).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name             |
|-----|-----|-----|-------|-------------|------|--------------------------|
| 1   | 35  | FN  | R     | \[1..1\]    |      | Family Name              |
| 2   | 35  | ST  | R     | \[1..1\]    |      | Given Name               |
| 3   | 35  | ST  | RE    | \[0..1\]    |      | Middle Initial or Name   |
| 4   | 10  | ST  | RE    | \[0..1\]    |      | Suffix                   |
| 5   | 10  | ST  | RE    | \[0..1\]    |      | Prefix                   |
| 6   | 10  | IS  | RE    | \[0..1\]    | 0360 | Degree                   |
| 7   | 10  | ID  | R     | \[1..1\]    | 0200 | Name Type Code           |
| 8   | 10  | ID  | X     | \[0..0\]    | 4000 | Name Representation Code |

#### PID-7-Date/Time of Birth

This field contains the date and time that the patient was born. It may be as imprecise as the four-digit birth year (*e.g.*, 1962).

#### PID-8-Sex

This field contains the sex of the patient and is populated with one of the values from user-defined Table 0001, *Sex*, if a value is known.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |
| U     | Unknown     |

#### PID-10-Race

This field contains a code indicating the race of the patient and uses four subcomponents.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | R     | \[1..1\]    |      | Name of Alternate Coding System |

#### PID-10.1-Identifier 

This component is populated with the Race Information value from the VistA PATIENT file, which is derived from user-defined Table 0005, *Race*.

#### PID-10.3-Name of Coding System

This component is populated with the value 0005.

#### PID-10.4-Alternate Identifier 

This component is populated with an appropriate value from the table, if one exists.

| Value  | Description                               |
|--------|-------------------------------------------|
| 0000-0 | Declined To Answer                        |
| 1002-5 | American Indian Or Alaska Native          |
| 2028-9 | Asian                                     |
| 2054-5 | Black Or African American                 |
| 2076-8 | Native Hawaiian Or Other Pacific Islander |
| 2106-3 | White                                     |
| 9999-4 | Unknown By Patient                        |

#### PID-10.6-Name of Coding System

This component is populated with the value CDC.

#### PID-11-Patient Address

This field contains the address of the patient.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                 |
|-----|-----|-----|-------|-------------|------|------------------------------|
| 1   | 250 | ST  | RE    | \[0..1\]    |      | Street Address               |
| 2   | 250 | ST  | RE    | \[0..1\]    |      | Other Designation            |
| 3   | 250 | ST  | RE    | \[0..1\]    |      | City                         |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | State or Province            |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | ZIP or Postal Code           |
| 6   | 20  | ID  | X     | \[0..0\]    |      | Country                      |
| 7   | 20  | ID  | X     | \[0..0\]    | 0190 | Address Type                 |
| 8   | 250 | ST  | X     | \[0..0\]    |      | Other Geographic Designation |
| 9   | 20  | IS  | X     | \[0..0\]    | 0289 | County/Parish Code           |
| 10  | 20  | IS  | X     | \[0..0\]    | 0288 | Census Tract                 |
| 11  | 20  | ID  | X     | \[0..0\]    | 4000 | Address Representation Code  |

#### PID-13-Phone Number – Home

This field contains the home telephone number of the patient. Only the first three components of this field are used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                                   |
|-----|-----|-----|-------|-------------|------|----------------------------------------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] |
| 2   | 3   | ID  | R     | \[1..1\]    | 0201 | Telecommunication use code                                     |
| 3   | 10  | ID  | R     | \[1..1\]    | 0202 | Telecommunication equipment type                               |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Email address                                                  |
| 5   | 20  | NM  | X     | \[0..0\]    |      | Country code                                                   |
| 6   | 20  | NM  | X     | \[0..0\]    |      | Area/city code                                                 |
| 7   | 20  | NM  | X     | \[0..0\]    |      | Phone number                                                   |
| 8   | 20  | NM  | X     | \[0..0\]    |      | Extension                                                      |
| 9   | 250 | ST  | X     | \[0..0\]    |      | Any text                                                       |

#### PID-13.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

This component is populated with the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub elements of the telephone number.

#### PID-13.2-Telecommunication Use Code

This component is populated with the kind of number that is contained in component 1 with a value from HL7 Table 0201, *Telecommunication Use Code*.

| Value | Description              |
|-------|--------------------------|
| PRN   | Primary Residence Number |

#### PID-13.3-Telecommunication Equipment Type

This component is populated with the kind of device that is reached on the number contained in component 1 with a value from HL7 Table 202, *Telecommunication Equipment Type*.

| Value | Description |
|-------|-------------|
| PH    | Telephone   |

#### PID-14-Phone Number – Business

This field contains the work telephone number of the patient. Only the first three components of this field are used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                                   |
|-----|-----|-----|-------|-------------|------|----------------------------------------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] |
| 2   | 3   | ID  | R     | \[1..1\]    | 0201 | Telecommunication use code                                     |
| 3   | 10  | ID  | R     | \[1..1\]    | 0202 | Telecommunication equipment type                               |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Email address                                                  |
| 5   | 20  | NM  | X     | \[0..0\]    |      | Country code                                                   |
| 6   | 20  | NM  | X     | \[0..0\]    |      | Area/city code                                                 |
| 7   | 20  | NM  | X     | \[0..0\]    |      | Phone number                                                   |
| 8   | 20  | NM  | X     | \[0..0\]    |      | Extension                                                      |
| 9   | 250 | ST  | X     | \[0..0\]    |      | Any text                                                       |

#### PID-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

This component is populated with the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub elements of the telephone number.

#### PID-14.2-Telecommunication Use Code

This component is populated with the kind of number contained in component 1 with a value from HL7 Table 0201, *Telecommunication Use Code*.

| Value | Description |
|-------|-------------|
| WPN   | Work Number |

#### PID-14.3-Telecommunication Equipment Type

This component is populated with the kind of device that is reached on the number contained in component 1 with a value from HL7 Table 202, *Telecommunication Equipment Type*.

| Value | Description |
|-------|-------------|
| PH    | Telephone   |

#### PID-19-SSN Number – Patient

This field contains the patient Social Security Number, for backward compatibility with versions of HL7 prior to v2.4. The Social Security Number is a secondary patient identifier. For the primary patient identifier, use the Integration Control Number from PID-3-Patient Identifier List.

#### PID-22-Ethnic Group

This field contains a code indicating whether the patient is of Hispanic descent.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | X     | \[0..0\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | R     | \[1..1\]    |      | Name of Alternate Coding System |

#### PID-22.1-Identifier 

This component is populated with the Ethnicity Information value from the VistA PATIENT file, which is derived from user-defined Table 0189, *Ethnic Group*.

#### PID-22.3-Name of Coding System 

This component is populated with the value 0189.

#### PID-22.4-Alternate Identifier 

This component is populated with an appropriate value from the table, if one exists.

| Value  | Description            |
|--------|------------------------|
| 0000-0 | Declined to Answer     |
| 2135-2 | Hispanic or Latino     |
| 2186-5 | Not Hispanic or Latino |
| 9999-4 | Unknown by Patient     |

#### PID-22.6-Name of Coding System 

This component is populated with the value CDC.

### PV1 Segment Fields in ORM 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Visit segment is used in ORM messages. A description of each PV1 field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values |
|---------|--------|-------|-------------------------------|
| PV1     | 1      | X     | Set ID – PV1                  |
|         | 2      | R     | Patient Class                 |
|         | 3      | C     | Assigned Patient Location     |
|         | 4      | X     | Admission Type                |
|         | 5      | X     | Preadmit Number               |
|         | 6      | X     | Prior Patient Location        |
|         | 7      | CE    | Attending Doctor              |
|         | 8      | RE    | Referring Doctor              |
|         | 9      | X     | Consulting Doctor             |
|         | 10     | C     | Hospital Service              |
|         | 11     | C     | Temporary Location            |
|         | 12     | X     | Pre-admit Test Indicator      |
|         | 13     | X     | Re-admission Indicator        |
|         | 14     | X     | Admit Source                  |
|         | 15     | RE    | Ambulatory Status             |
|         | 16     | RE    | VIP Indicator                 |
|         | 17     | X     | Admitting Doctor              |
|         | 18     | X     | Patient Type                  |
|         | 19     | RE    | Visit Number                  |
|         | 20     | X     | Financial Class               |
|         | 21     | X     | Charge Price Indicator        |
|         | 22     | X     | Courtesy Code                 |
|         | 23     | X     | Credit Rating                 |
|         | 24     | X     | Contract Code                 |
|         | 25     | X     | Contract Effective Date       |
|         | 26     | X     | Contract Amount               |
|         | 27     | X     | Contract Period               |
|         | 28     | X     | Interest Code                 |
|         | 29     | X     | Transfer to Bad Debt Code     |
|         | 30     | X     | Transfer to Bad Debt Date     |
|         | 31     | X     | Bad Debt Agency Code          |
|         | 32     | X     | Bad Debt Transfer Amount      |
|         | 33     | X     | Bad Debt Recovery Amount      |
|         | 34     | X     | Delete Account Indicator      |
|         | 35     | X     | Delete Account Date           |
|         | 36     | X     | Discharge Disposition         |
|         | 37     | X     | Discharge to Location         |
|         | 38     | X     | Diet Type                     |
|         | 39     | X     | Servicing Facility            |
|         | 40     | X     | Bed Status                    |
|         | 41     | X     | Account Status                |
|         | 42     | X     | Pending Location              |
|         | 43     | X     | Prior Temporary Location      |
|         | 44     | RE    | Admit Date/Time               |
|         | 45     | X     | Discharge Date/Time           |
|         | 46     | X     | Current Patient Balance       |
|         | 47     | X     | Total Charges                 |
|         | 48     | X     | Total Adjustments             |
|         | 49     | X     | Total Payments                |
|         | 50     | X     | Alternate Visit ID            |
|         | 51     | X     | Visit Indicator               |
|         | 52     | X     | Other Healthcare Provider     |

#### PV1-2-Patient Class

This field contains indicates either that the patient is an inpatient (I) or an outpatient (O).

#### PV1-3-Assigned Patient Location

For inpatients, this field contains the location of the patient in the medical center.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name         |
|-----|-----|-----|-------|-------------|------|----------------------|
| 1   | 30  | IS  | R     | \[1..1\]    | 0302 | Point of Care        |
| 2   | 30  | IS  | R     | \[1..1\]    | 0303 | Room                 |
| 3   | 30  | IS  | RE    | \[0..1\]    | 0304 | Bed                  |
| 4   | 30  | HD  | X     | \[0..0\]    |      | Facility             |
| 5   | 30  | IS  | X     | \[0..0\]    | 0306 | Location Status      |
| 6   | 30  | IS  | X     | \[0..0\]    | 0305 | Person Location Type |
| 7   | 30  | IS  | X     | \[0..0\]    | 0307 | Building             |
| 8   | 30  | IS  | X     | \[0..0\]    | 0308 | Floor                |
| 9   | 199 | ST  | X     | \[0..0\]    |      | Location Description |

VistA sends component 1, Point of Care, as three subcomponents.

1.  Internal entry number into the VistA WARD LOCATION file (#42)
2.  Name of the ward location
3.  Internal designator of the WARD LOCATION file and is ignored

#### PV1-7-Attending Doctor

This field contains the physician responsible for the care of the patient during the present encounter. VistA values this field for inpatient encounters only. Only the first four components are used and the other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | Suffix                                           |
| 6   | 250 | ST  | RE    | \[0..1\]    |      | Prefix                                           |
| 7   | 10  | IS  | RE    | \[0..1\]    |      | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    |      | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    |      | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    |      | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    |      | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    |      | Name Representation Code                         |

#### PV1-8-Referring Doctor

This field contains information about the primary care physician for this patient. VistA values this field for inpatient encounters only. Only the first four components are used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | Suffix                                           |
| 6   | 250 | ST  | RE    | \[0..1\]    |      | Prefix                                           |
| 7   | 10  | IS  | RE    | \[0..1\]    |      | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    |      | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    |      | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    |      | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    |      | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    |      | Name Representation Code                         |

#### PV1-10-Hospital Service

This field contains the treating specialty assigned to the patient with the most recent movement. VistA values this field for inpatient encounters only. When populated, it contains a value from user-defined Table 0069, *Hospital Service*; VistA sends values from the HOSPITAL LOCATION file (#44).

#### PV1-11-Temporary Location

For outpatients, this field contains the location of the patient in the medical center.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name         |
|-----|-----|-----|-------|-------------|------|----------------------|
| 1   | 30  | IS  | R     | \[1..1\]    |      | Point of Care        |
| 2   | 30  | IS  | X     | \[0..0\]    |      | Room                 |
| 3   | 30  | IS  | X     | \[0..0\]    |      | Bed                  |
| 4   | 30  | HD  | RE    | \[0..1\]    |      | Facility             |
| 5   | 30  | IS  | X     | \[0..0\]    |      | Location Status      |
| 6   | 30  | IS  | X     | \[0..0\]    |      | Person Location Type |
| 7   | 30  | IS  | X     | \[0..0\]    |      | Building             |
| 8   | 30  | IS  | X     | \[0..0\]    |      | Floor                |
| 9   | 199 | ST  | X     | \[0..0\]    |      | Location Description |

VistA sends component 1, Point of Care, as the name of the HOSPITAL LOCATION

VistA sends component 4, Facility, as the Internal Entry Number of the INSTITUTION from the INSTITUTION file (#4) where the HOSPITAL LOCATION resides into the VistA WARD LOCATION file (#42) concatenated with an underscore concatenated with the NAME (#.01) of the INSTITUTION.

#### PV1-15-Ambulatory Status

This field contains any permanent or transient conditions affecting the patient’s mode of transportation. This field may also contain the pregnancy status of the patient.

The RAD/NUC MED ORDERS file (#75.1) contains two fields that decide the values set into this field: Pregnant (#13) and Mode of Transport (#19). Because of this, the field may repeat when the patient is both ambulatory and pregnant.

This field may contain one or more values from user-defined Table 0009, *Ambulatory Status*. This field is not populated if the patient’s ambulatory status or pregnancy status is not known.

> **NOTE:** VistA populates this field with the value B6 to indicate that the patient is pregnant.

| Value | Description                |
|-------|----------------------------|
| A0    | No functional limitations  |
| A2    | Wheelchair/stretcher bound |
| B6    | Pregnant                   |

#### PV1-16-VIP Indicator

This field contains that the patient is an employee, or that the patient record is sensitive and must not be made available for general personnel access. If one of these conditions applies, VistA populates this field with a value from user-defined Table 0099, *VIP Indicator*.

| Value | Description                                              |
|-------|----------------------------------------------------------|
| E     | Patient is a VA employee                                 |
| S     | Patient record is sensitive                              |
| ES    | Patient is a VA employee and patient record is sensitive |

#### PV1-19-Visit

For an inpatient, this field contains an I concatenated with the inpatient visit number from the VistA PIMS package. 

For an outpatient, this field contains an O concatenated with an integer representing today’s date.

### ORC Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Common Order segment is used in ORM messages. A description of each ORC field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values    |
|---------|--------|-------|----------------------------------|
| ORC     | 1      | R     | Order Control                    |
|         | 2      | R     | Placer Order Number              |
|         | 3      | R     | Filler Order Number              |
|         | 4      | RE    | Placer Group Number              |
|         | 5      | R     | Order Status                     |
|         | 6      | X     | Response Flag                    |
|         | 7      | R     | Quantity/Timing                  |
|         | 8      | RE    | Parent                           |
|         | 9      | R     | Date/Time of Transaction         |
|         | 10     | R     | Entered By                       |
|         | 11     | X     | Verified By                      |
|         | 12     | RE    | Ordering Provider                |
|         | 13     | RE    | Enterer’s Location               |
|         | 14     | RE    | Call Back Phone Number           |
|         | 15     | X     | Order Effective Date/Time        |
|         | 16     | X     | Order Control Code Reason        |
|         | 17     | RE    | Entering Organization            |
|         | 18     | X     | Entering Device                  |
|         | 19     | X     | Action By                        |
|         | 20     | X     | Advanced Beneficiary Notice Code |
|         | 21     | X     | Ordering Facility Name           |
|         | 22     | X     | Ordering Facility Address        |
|         | 23     | X     | Ordering Facility Phone Number   |
|         | 24     | X     | Ordering Provider Address        |
|         | 25     | X     | Order Status Modifier            |

#### ORC-1-Order Control

This field contains a value from HL7 Table 0119, *Order Control Codes*.

| Value | Description                  |
|-------|------------------------------|
| CA    | Cancel order/service request |
| NW    | New order/service            |
| XO    | Change order/service request |

#### ORC-2-Placer Order Number

This field contains the medical center station number of the accession number of the case in question, concatenated with the Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.

Example: 578-102104-1693.

#### ORC-3-Filler Order Number

This field contains the medical center station number of the accession number of the case in question, concatenated with the Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.

Example: 688-102104-1693.

#### ORC-4-Placer Group Number

This field allows an order placing application to group sets of orders together

and subsequently identify them. One of the features introduced in v5.0 of VISTA Radiology/Nuclear Medicine allows multiple exams to be combined in a comprehensive report. This feature is called a “printset”. The printset concept is addressed by HL7 through the use of a unique identifier passed to the receiving system in the placer group number to group a set of

orders for a single report. An identical entity identifier will be sent in this field for each

member of a printset.

The first component of this field, the entity identifier, only will be present only if the

procedure is a member of a printset. The entity identifier will be represented by a

combination of the first three digits of the station number, the DFN of the patient and inverse date/time of the exam.

Example: 141-76-6809282.8562

#### ORC-5-Order Status

This field contains a value from HL7 Table 0038, *Order Status*.

| Value | Description             |
|-------|-------------------------|
| CA    | Order was canceled      |
| CM    | Order is completed      |
| IP    | In process, unspecified |

#### ORC-7-Quantity/Timing

This field contains twelve components.

| Seq | Len   | DT  | Usage | Cardinality | TBL# | Element Name        |
|-----|-------|-----|-------|-------------|------|---------------------|
| 1   | 250   | CQ  | X     | \[0..0\]    |      | Quantity            |
| 2   | 250   | CM  | X     | \[0..0\]    |      | Interval            |
| 3   | 250   | CM  | X     | \[0..0\]    |      | Duration            |
| 4   | 26    | TS  | R     | \[1..1\]    |      | Start Date/Time     |
| 5   | 26    | TS  | X     | \[0..0\]    |      | End Date/Time       |
| 6   | 20    | ST  | R     | \[1..1\]    |      | Priority            |
| 7   | 250   | ST  | X     | \[0..0\]    |      | Condition           |
| 8   | 65535 | TX  | X     | \[0..0\]    |      | Text                |
| 9   | 250   | ST  | X     | \[0..0\]    |      | Conjunction         |
| 10  | 250   | CM  | X     | \[0..0\]    |      | Order Sequencing    |
| 11  | 250   | CE  | X     | \[0..0\]    |      | Occurrence Duration |
| 12  | 10    | NM  | X     | \[0..0\]    |      | Total Occurrences   |

#### ORC-7.4-Start Date/Time

This component is populated with the date and time requested for the start of the order.

#### ORC-7.6-Priority

This component is populated with the priority of the order.

| Value | Description                   |
|-------|-------------------------------|
| S     | Stat (with highest priority)  |
| A     | ASAP (fill after Stat orders) |
| R     | Routine (the default)         |

#### ORC-8-Parent

This field contains a value to identify an examset or printset, or to indicate the parent order of the examset or printset that was purged.

- If the order is part of an examset, the field is valued as:  
  EXAMSET: *procedure_name*
- If the order is part of a printset, the field is valued as:  
  PRINTSET: *procedure_name*
- If the parent order was purged, the field is valued as:  
  ORIGINAL ORDER PURGED

#### ORC-9-Date/Time of Transaction

This field contains the date and time that the case was registered into VistA.

#### ORC-10-Entered By

This field contains the name of the person who entered the order into VistA. Only the first four components are used. Other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Suffix                                           |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Prefix                                           |
| 7   | 10  | IS  | X     | \[0..0\]    |      | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    |      | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    |      | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    |      | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    |      | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    |      | Name Representation Code                         |

#### ORC-12-Ordering Provider

This field contains the ID number and name of the provider that requested the order. Only the first four components are used. Other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Suffix                                           |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Prefix                                           |
| 7   | 10  | IS  | X     | \[0..0\]    |      | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    |      | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    |      | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    |      | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    |      | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    |      | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    |      | Name Representation Code                         |

#### ORC-13-Enterer’s Location

This field contains the location of the person in the medical center who entered the order, if known. Only the first component is populated. It contains the name of the enterer’s service/section from the VistA SERVICE/SECTION file (#49).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name         |
|-----|-----|-----|-------|-------------|------|----------------------|
| 1   | 30  | IS  | R     | \[1..1\]    | 0302 | Point of Care        |
| 2   | 30  | IS  | X     | \[0..0\]    | 0303 | Room                 |
| 3   | 30  | IS  | X     | \[0..0\]    | 0304 | Bed                  |
| 4   | 30  | HD  | X     | \[0..0\]    |      | Facility             |
| 5   | 30  | IS  | X     | \[0..0\]    | 0306 | Location Status      |
| 6   | 30  | IS  | X     | \[0..0\]    | 0305 | Person Location Type |
| 7   | 30  | IS  | X     | \[0..0\]    | 0307 | Building             |
| 8   | 30  | IS  | X     | \[0..0\]    | 0308 | Floor                |
| 9   | 199 | ST  | X     | \[0..0\]    |      | Location Description |

#### ORC-14-Call Back Phone Number

This field contains the telephone number of the provider identified in *ORC-11-Ordering Provider*. It clarifies the request or other information regarding the order. Up to eight telephone numbers can be entered into this field. Only the first three components are used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                                   |
|-----|-----|-----|-------|-------------|------|----------------------------------------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] |
| 2   | 3   | ID  | R     | \[1..1\]    | 0201 | Telecommunication use code                                     |
| 3   | 10  | ID  | R     | \[1..1\]    | 0202 | Telecommunication equipment type                               |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Email address                                                  |
| 5   | 20  | NM  | X     | \[0..0\]    |      | Country code                                                   |
| 6   | 20  | NM  | X     | \[0..0\]    |      | Area/city code                                                 |
| 7   | 20  | NM  | X     | \[0..0\]    |      | Phone number                                                   |
| 8   | 20  | NM  | X     | \[0..0\]    |      | Extension                                                      |
| 9   | 250 | ST  | X     | \[0..0\]    |      | Any text                                                       |

#### ORC-14.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

This component is populated with the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub elements of the telephone number.

#### ORC-14.2-Telecommunication Use Code

This component is populated with the kind of number that is in component 1 with a value from HL7 Table 0201, *Telecommunication Use Code*.

| Value | Description              |
|-------|--------------------------|
| PRN   | Primary Residence Number |
| WPN   | Work Number              |
| BPN   | Beeper Number            |

#### ORC-14.3-Telecommunication Equipment Type

This component is populated with the kind of device that is reached on the number in component 1 with a value from HL7 Table 202, *Telecommunication Equipment Type*.

| Value | Description |
|-------|-------------|
| PH    | Telephone   |
| FX    | Fax         |
| BP    | Beeper      |

#### ORC-17-Entering Organization

This field contains the service/section of the medical center of the person identified in *ORC-10-Entered By* from the VistA SERVICE/SECTION file (#49).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Name of Alternate Coding System |

#### ORC-17.1-Identifier

This component is populated with the abbreviation for the service/section of the medical center.

#### ORC-17.2-Text

This component is populated with the full name of the service/section of the medical center.

#### ORC-17.3-Name of Coding System

This component is populated with the value VISTA49.

### OBR Segment Fields in ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Request segment is used in ORM and ORU messages, though field usage is different for ORU messages. A description of each OBR field element is provided in the table of ORM message attributes; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values            |
|---------|--------|-------|------------------------------------------|
| OBR     | 1      | R     | Set ID – OBR                             |
|         | 2      | R     | Placer Order Number                      |
|         | 3      | R     | Filler Order Number (Exam & Case IDs)    |
|         | 4      | R     | Universal Service ID                     |
|         | 5      | R     | Priority – OBR                           |
|         | 6      | X     | Requested Date/Time                      |
|         | 7      | X     | Observation Date/Time                    |
|         | 8      | X     | Observation End Date/Time                |
|         | 9      | X     | Collection Volume                        |
|         | 10     | X     | Collector Identifier                     |
|         | 11     | X     | Specimen Action Code                     |
|         | 12     | X     | Danger Code                              |
|         | 13     | X     | Relevant Clinical Information            |
|         | 14     | X     | Specimen Received Date/Time              |
|         | 15     | RE    | Specimen Source                          |
|         | 16     | R     | Ordering Provider                        |
|         | 17     | RE    | Order Callback Phone Number              |
|         | 18     | R     | Placer Field 1                           |
|         | 19     | R     | Placer Field 2                           |
|         | 20     | R     | Filler Field 1                           |
|         | 21     | R     | Filler Field 2                           |
|         | 22     | X     | Results Report Status Change – Date/Time |
|         | 23     | X     | Charge to Practice                       |
|         | 24     | RE    | Diagnostic Service Section ID            |
|         | 25     | X     | Result Status                            |
|         | 26     | X     | Parent Result                            |
|         | 27     | R     | Quantity/Timing                          |
|         | 28     | X     | Result Copies To                         |
|         | 29     | RE    | Parent                                   |
|         | 30     | RE    | Transportation Mode                      |
|         | 31     | R     | Reason for Study                         |
|         | 32     | X     | Principal Result Interpreter             |
|         | 33     | X     | Assistant Result Interpreter             |
|         | 34     | X     | Technician                               |
|         | 35     | X     | Transcriptionist                         |
|         | 36     | X     | Scheduled Date/Time                      |
|         | 37     | X     | Number of Sample Containers              |
|         | 38     | X     | Transport Logistics of Collected Sample  |
|         | 39     | X     | Collector’s Comment                      |
|         | 40     | X     | Transport Arrangement Responsibility     |
|         | 41     | X     | Transport Arranged                       |
|         | 42     | X     | Escort Required                          |
|         | 43     | X     | Planned Patient Transfer Comment         |
|         | 44     | X     | Procedure Code                           |
|         | 45     | X     | Procedure Code Modifier                  |
|         | 46     | X     | Placer Supplemental Service Information  |
|         | 47     | X     | Filler Supplemental Service Information  |

> **NOTE:** OBR and OBX (for procedure only) segments repeat in pairs for printsets (such as, single report entered for multiple cases).

#### OBR-1-Set ID

This field contains an integer corresponding to the ordinal position of this OBR segment in the message. The first occurrence is labeled 1, the second 2, and so on.

#### OBR-2-Placer Order Number

This field contains the medical center station number of the accession number of the case in question, concatenated with Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.  
Example: 688-102104-1693.

#### OBR-3-Filler Order Number

This field contains the medical center station number of the accession number of the case in question, concatenated with Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.  
Example: 688-102104-1693.

> **NOTE:** For OBR-2 and OBR-3, when the site-specific accession number is not set to YES, the value for each is only the Day-Case \#.  
Example: 102104-1693

#### OBR-4-Universal Service Identifier

This field contains six components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | R     | \[1..1\]    |      | Alternate Text                  |
| 6   | 250 | ST  | R     | \[1..1\]    |      | Name of Alternate Coding System |

#### OBR-4.1-Identifier

This component is populated with the CPT code from the VistA CPT file (#81).

#### OBR-4.2-Text

This component is populated with the short name associated with the CPT code in *OBR-4.1-Identifier*.

#### OBR-4.3-Name of Coding System

This component is populated with the value C4.

#### OBR-4.4-Alternate Identifier

This component is populated with the internal entry number (IEN) of this procedure as defined in the VistA RAD/NUC MED PROCEDURES file (#71).

#### OBR-4.5-Alternate Text

This component is populated with the name of the procedure as defined in the RAD/NUC MED PROCEDURES file (#71).

#### OBR-4.6-Name of Alternate Coding System

This component is populated with the value 99RAP.

#### OBR-5-Priority

This field contains the priority of the order to satisfy IHE requirements, but is intended for backward compatibility only.

| Value | Description |
|-------|-------------|
| S     | Stat        |
| A     | ASAP        |
| R     | Routine     |

#### OBR-15-Specimen Source

This field contains six components. Only component 5 is populated. When a procedure modifier (LEFT and/or RIGHT) is included in the order, that value is sent in subcomponent 2 of component 5.

| Seq | Len   | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-------|-----|-------|-------------|------|---------------------------------|
| 1   | 250   | CE  | X     | \[0..0\]    |      | Specimen Source Name or Code    |
| 2   | 65535 | TX  | X     | \[0..0\]    |      | Additives                       |
| 3   | 65535 | TX  | X     | \[0..0\]    |      | Free text                       |
| 4   | 250   | CE  | X     | \[0..0\]    |      | Procedure Modifier              |
| 5   | 250   | CE  | RE    | \[0..1\]    |      | Site Modifier                   |
| 6   | 250   | CE  | X     | \[0..0\]    |      | Collection Method Modifier Code |

#### OBR-16-Ordering Provider

This field contains the ID number and name of the provider that requested the order. Only the first four components are used. Other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Suffix                                           |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Prefix                                           |
| 7   | 10  | IS  | X     | \[0..0\]    | 0360 | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    | 0297 | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    | 0363 | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    | 0200 | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    | 0061 | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    | 0203 | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    | 0300 | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    | 4000 | Name Representation Code                         |

#### OBR-17-Order Callback Phone Number

This field contains up to eight telephone numbers that can be used to report order status or results. Only the first three components of this field are used. Other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                                   |
|-----|-----|-----|-------|-------------|------|----------------------------------------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] |
| 2   | 3   | ID  | R     | \[1..1\]    | 0201 | Telecommunication use code                                     |
| 3   | 10  | ID  | R     | \[1..1\]    | 0202 | Telecommunication equipment type                               |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Email address                                                  |
| 5   | 20  | NM  | X     | \[0..0\]    |      | Country code                                                   |
| 6   | 20  | NM  | X     | \[0..0\]    |      | Area/city code                                                 |
| 7   | 20  | NM  | X     | \[0..0\]    |      | Phone number                                                   |
| 8   | 20  | NM  | X     | \[0..0\]    |      | Extension                                                      |
| 9   | 250 | ST  | X     | \[0..0\]    |      | Any text                                                       |

#### OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

This component is populated with the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub elements of the telephone number.

#### OBR-17.2-Telecommunication Use Code

This component is populated with the kind of number that is contained in component 1 with a value from HL7 Table 0201, *Telecommunication Use Code*.

| Value | Description              |
|-------|--------------------------|
| PRN   | Primary Residence Number |
| WPN   | Work Number              |
| BPN   | Beeper Number            |

#### OBR-17.3-Telecommunication Equipment Type

This component is populated with the kind of device that is reached on the number in component 1 with a value from HL7 Table 202, *Telecommunication Equipment Type*.

| Value | Description |
|-------|-------------|
| PH    | Telephone   |
| FX    | Fax         |
| BP    | Beeper      |

#### OBR-18-Placer Field 1

This field contains the Facility Identifier concatenated with Day-Case \# of the examination (Accession Number).

> **NOTE:** OBR-18 shares the same value as OBR-2, OBR-3, and OBR-20.

#### OBR-19-Placer Field 2

This field contains the case number, which is unique only to the facility that initiated the patient event.

#### OBR-20-Filler Field 1

This field contains the Facility Identifier concatenated with Day-Case \# of the examination (Accession Number).

Notes: OBR-20 shares the same value as OBR-2, OBR-3, and OBR-18.  
For both OBR-18 and OBR-20, when the site-specific accession number is not set to YES, the value for each is only the Day-Case \#.  
Example: 102104-1693

#### OBR-21-Filler Field 2

This field contains a number of different data attributes. The data string is as follows:

- The first component is populated with the imaging type abbreviation and the imaging type name.
- The second component is populated with the IEN of the IMAGING LOCATION (#79.1) record and the name of the HOSPITAL LOCATION (#44) referenced by that imaging location.
- The third component is populated with the IEN of the RAD/NUC MED DIVISION (#79) record and the name of the INSTITUTION (#4) referenced by that division.

The components are delimited by the accent grave (\`) and the subcomponents are delimited by the underscore (\_)

#### OBR-24-Diagnostic Service Section ID

This field contains the single known Procedure Modality associated with the type of exam ordered. If more than one Procedure Modality is known to VistA, nothing is sent in this field. The terms used are from the VistA RAD MODALITY DEFINED TERMS file (#73.1).

#### OBR-27-Quantity/Timing

This field contains twelve components.

| Seq | Len   | DT  | Usage | Cardinality | TBL# | Element Name        |
|-----|-------|-----|-------|-------------|------|---------------------|
| 1   | 250   | CQ  | X     | \[0..0\]    |      | Quantity            |
| 2   | 250   | CM  | X     | \[0..0\]    |      | Interval            |
| 3   | 250   | CM  | X     | \[0..0\]    |      | Duration            |
| 4   | 26    | TS  | R     | \[1..1\]    |      | Start Date/Time     |
| 5   | 26    | TS  | X     | \[0..0\]    |      | End Date/Time       |
| 6   | 20    | ST  | R     | \[1..1\]    |      | Priority            |
| 7   | 250   | ST  | X     | \[0..0\]    |      | Condition           |
| 8   | 65535 | TX  | X     | \[0..0\]    |      | Text                |
| 9   | 250   | ST  | X     | \[0..0\]    |      | Conjunction         |
| 10  | 250   | CM  | X     | \[0..0\]    |      | Order Sequencing    |
| 11  | 250   | CE  | X     | \[0..0\]    |      | Occurrence Duration |
| 12  | 10    | NM  | X     | \[0..0\]    |      | Total Occurrences   |

#### OBR-27.4-Start Date/Time

This component is populated with the scheduled start date and time requested for the order.

#### OBR-27.6-Priority

This component is populated with the priority of the order.

| Value | Description                   |
|-------|-------------------------------|
| S     | Stat (with highest priority)  |
| A     | ASAP (fill after Stat orders) |
| R     | Routine (the default)         |

#### OBR-29-Parent

This field contains a value to identify an examset or printset, or to indicate that the parent order of the examset or printset was purged.

- If the order is part of an examset, the field is valued as:  
  EXAMSET: *procedure_name*
- If the order is part of a printset, the field is valued as:  
  PRINTSET: *procedure_name*
- If the parent order was purged, the field is valued as:  
  ORIGINAL ORDER PURGED

#### OBR-30-Transportation Mode

This field contains how, or whether to transport a patient with a value from HL7 Table 0124, *Transportation Mode*.

| HL7 Value | HL7 Description                                 | VistA Value |
|-----------|-------------------------------------------------|-------------|
| CART      | Cart - patient travels on cart or gurney        | STRETCHER   |
| PORT      | The examining device goes to patient’s location | PORTABLE    |
| WALK      | Patient walks to diagnostic service             | AMBULATORY  |
| WHLC      | Wheelchair                                      | WHEELCHAIR  |

#### OBR-31-Reason for Study

This field contains six components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | X     | \[0..0\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | X     | \[0..0\]    |      | Name of Coding System           |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Name of Alternate Coding System |

#### OBR-31.2-Reason for Study

This component is populated with the Reason for Study, which is free text string entered when the order is requested.<span id="_Ref232824764" class="anchor"></span>

### ZDS Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZDS segment is a user-defined segment used in ORM and ORU messages. It contains one field, Study Instance Unique Identifier, which is made up of four components.

| Segment | Seq \# | Usage | Field Element Name and Values |
|---------|--------|-------|-------------------------------|
| ZDS     | 1      | R     | Study Instance UID            |

#### ZDS-1-Study Instance UID

This field contains the unique identifier that VistA assigns to the study.

| Seq | Len | DT  | Usage | Cardinality | Item \# | Element Name   |
|-----|-----|-----|-------|-------------|---------|----------------|
| 1   | 250 | ST  | R     | \[1..1\]    |         | Pointer        |
| 2   | 250 | HD  | R     | \[1..1\]    |         | Application ID |
| 3   | 20  | ID  | R     | \[1..1\]    | 0191    | Type of Data   |
| 4   | 20  | ID  | R     | \[1..1\]    | 0291    | Subtype        |

The components of this field are populated as follows.

#### ZDS-1.1-Pointer

This component is populated with the ISO Object Identifier (OID) value that VistA assigned to the study. The subscriber and modalities must use this value instead of assigning one.

#### ZDS-1.2-Application ID

This component is populated with the value VISTA, indicating the application that generated the value in Component 1.

#### ZDS-1.3-Type of Data

This component is populated with the value Application, indicating general type of data to which it is pointed.

#### ZDS-1.4-Subtype

This component is populated with the value DICOM, indicating the specific type of data to which it is pointed.

### OBX Segment Fields in ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Segment is used in ORM and ORU messages, though field usage is different for ORU messages. A description of each OBX field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values      |
|---------|--------|-------|------------------------------------|
| OBX     | 1      | R     | Set – ID OBX                       |
|         | 2      | R     | Value Type                         |
|         | 3      | R     | Observation Identifier             |
|         | 4      | X     | Observation Sub-ID                 |
|         | 5      | R     | Observation Value                  |
|         | 6      | X     | Units                              |
|         | 7      | X     | Reference Range                    |
|         | 8      | X     | Abnormal Flags                     |
|         | 9      | X     | Probability                        |
|         | 10     | X     | Nature of Abnormal Test            |
|         | 11     | R     | Observation Result Status          |
|         | 12     | X     | Date Last Observation Normal Value |
|         | 13     | X     | User Defined Access Checks         |
|         | 14     | X     | Date/Time of the Observation       |
|         | 15     | X     | Producer’s ID                      |
|         | 16     | X     | Responsible Observer               |
|         | 17     | X     | Observation Method                 |
|         | 18     | X     | Equipment Instance Identifier      |
|         | 19     | X     | Date/Time of Analysis              |

#### OBX-2-Value Type

This field contains the data type of the information carried in *OBX-5-Observation Value* with a value from HL7 Table 0125, *Value Type*.

| Value | Description   |
|-------|---------------|
| CE    | Coded Element |
| TX    | Text          |

#### OBX-3-Observation Identifier

This field contains the classification of the kind of information carried in *OBX-5-Observation Value.* Component 3 is always valued L.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Name of Alternate Coding System |

#### OBX-3.1-Identifier and OBX-3.2-Text

These two components are populated with one of the following values.

| Identifier | Text          |
|------------|---------------|
| P          | Procedure     |
| M          | Modifiers     |
| H          | History       |
| TCM        | Tech Comment  |
| A          | Allergies     |
| C4         | CPT Modifiers |

#### OBX-3.3-Name of Coding System 

This component is populated with the value L.

#### OBX-5-Observation Value

This field contains the actual value of the data type in *OBX-2-Value Type* and of the classification in *OBX-3-Observation Identifier*. Formatting follows the rules for the data type in OBX-2.

#### OBX-11-Observation Result Status

In the order message, this field contains the fixed value O (order detail description only, no result) from HL7 Table 0085, *Observation Result Status Codes Interpretation*.

### MSA Segment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a listing of all the fields defined for the MSA segments in HL7, refer to 3.5.8 MSA Segment on page [22](#msa-segment).

For an explanation of the MSA segment fields used by VistA acknowledgment messages, refer to 4.7.1 MSA Segment Fields in ACK Messages on page [78](#msa-segment-fields-in-ack-messages).

# Report Transmission/Storage Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This transaction is used by the VistA Rad/Nuc Med package to transmit a radiology report to subscribers.

![](ra5-158-hl7-interface-specification/004.png)

### Actors and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Actor: Rad/Nuc Med

Role: Transmits radiology report information to ancillary VistA modules and clinical systems when Rad/Nuc Med reports are filed.

Actor: Subscribers

Role: Receives and files radiology report information.

## Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actors perform the behaviors shown in the activity diagram.

![](ra5-158-hl7-interface-specification/005.png)

## Dynamic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA and subscribers generate and process HL7 messages according to functional and business requirements.

### ORU – Unsolicited Observation Results 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The function of the ORU message is to transmit information about a report. Almost any clinical report message can be constructed as a three‑level hierarchy, with the patient identification (PID) segment at the top level, an order segment (OBR) at the next level, and one or more observation segments (OBX) at the bottom. One OBX is transmitted for each component of a diagnostic report, such as an EKG or obstetrical ultrasound or electrolyte battery.

The business rules for the VistA Rad/Nuc Med application state that when building outbound ORU HL7 messages, a continuation node must be created for any segment that exceeds 245 characters in length.6F[^5]

Many OBR segments may be associated with a PID segment, with many separate OBX segments associated with each OBR.

| Segment | Order Message          | HL7 Chapter |
|---------|------------------------|-------------|
| MSH     | Message header         | 2           |
| PID     | Patient identification | 3           |
| OBR     | Order detail           | 4           |
| OBX     | Observation/Result     | 7           |

For examples of ORU messages, refer to [Appendix A](#oru-examples).

Rad/Nuc Med transmits an ORU message to a subscriber when a report is filed.

## Static Definition – Message Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 messages are populated and processed according to the following abstract message definitions.

### Observation Result–Unsolicited (ORU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Segment       | ORU Message                           | Usage | Cardinality | HL7 Chapter |
|---------------|---------------------------------------|-------|-------------|-------------|
| MSH           | Message Header                        | R     | \[1..1\]    | 2           |
| { \[ PID      | Patient Identification                | R     | \[1..1\]    | 3           |
| \[ PD1 \]     | Additional Demographics               | X     | \[0..0\]    | 3           |
| \[ { NK1 } \] | Next of Kin / Associated Parties      | X     | \[0..0\]    | 3           |
| \[ { NTE } \] | Notes and Comments                    | X     | \[0..0\]    | 2           |
| \[ PV1        | Patient Visit                         | X     | \[0..0\]    | 3           |
| \[ PV2 \] \]  | Patient Visit – Additional Info.      | X     | \[0..0\]    | 3           |
| \]            |                                       |       |             |             |
| { \[ ORC \]   | Common Order                          | X     | \[0..0\]    | 4           |
| OBR           | Observation Request                   | R     | \[1..1\]    | 4           |
| \[ { NTE } \] | Notes and Comments (for Detail)       | X     | \[0..0\]    | 2           |
| ZDS           | Additional Identification Information | R     | \[1..1\]    | ††          |
| \[ { OBX      | Observation/Result                    | RE    | \[0..999\]  | 7           |
| \[ { NTE } \] | Notes and Comments (for Results)      | X     | \[0..0\]    | 2           |
| } \]          |                                       |       |             |             |
| { \[ CTI \] } | Clinical Trial Information            | X     | \[0..0\]    | 7           |
| }             |                                       |       |             |             |
| \[ DSC \]     | Continuation Pointer                  | X     | \[0..0\]    | 2           |

> †† This segment is defined in IHE Rad-TF Transaction 4 (Procedure Scheduled).

## Static Definition – Segment Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For a listing of all the fields defined for the MSH segment in HL7, refer to 3.5.1 MSH Segment on page [15](#msh-segment).
- For an explanation of the MSH fields used in the VistA order and report messages, refer to 3.6.1 MSH Segment Fields in ORM and ORU on page [23](#msh-segment-fields-in-orm-and-oru).

### PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For a listing of all the fields defined for the PID segment in HL7, refer to 3.5.2 PID Segment on page [16](#pid-segment).
- For an explanation of the PID fields used in the VistA order and report messages, refer to 3.2.6 PID Segment Fields on page [28](#pid-segment-fields).

### OBR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For an explanation of the OBR fields used in the VistA order message, refer to 4.6.3 OBR Segment Fields on page [75](#_Fields_Used_in_6).

A listing of all the fields defined for the OBR segment in HL7.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Seq</th>
<th>Len</th>
<th>DT</th>
<th>Usage</th>
<th>Cardinality</th>
<th>TBL#</th>
<th>Item #</th>
<th>Element Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00237</td>
<td>Set ID ‑ OBR</td>
</tr>
<tr class="even">
<td>2</td>
<td>22</td>
<td>EI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00216</td>
<td>Placer Order Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>22</td>
<td>EI</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00217</td>
<td>Filler Order Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00238</td>
<td>Universal Service Identifier</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00239</td>
<td>Priority - OBR</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00240</td>
<td>Requested Date/Time</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00241</td>
<td>Observation Date/Time</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00242</td>
<td>Observation End Date/Time</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>CQ</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00243</td>
<td>Collection Volume</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>XCN</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00244</td>
<td>Collector Identifier</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0065</td>
<td>00245</td>
<td>Specimen Action Code</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00246</td>
<td>Danger Code</td>
</tr>
<tr class="odd">
<td>13</td>
<td>300</td>
<td>ST</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00247</td>
<td>Relevant Clinical Information</td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00248</td>
<td>Specimen Received Date/Time</td>
</tr>
<tr class="odd">
<td>15</td>
<td>300</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td><p>0070</p>
<p>0163</p>
<p>0369</p></td>
<td>00249</td>
<td>Specimen Source</td>
</tr>
<tr class="even">
<td>16</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00226</td>
<td>Ordering Provider</td>
</tr>
<tr class="odd">
<td>17</td>
<td>250</td>
<td>XTN</td>
<td>RE</td>
<td>[0..8]</td>
<td></td>
<td>00250</td>
<td>Order Callback Phone Number</td>
</tr>
<tr class="even">
<td>18</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00251</td>
<td>Placer Field 1</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00252</td>
<td>Placer Field 2</td>
</tr>
<tr class="even">
<td>20</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[0..0]</td>
<td></td>
<td>00253</td>
<td>Filler Field 1</td>
</tr>
<tr class="odd">
<td>21</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00254</td>
<td>Filler Field 2</td>
</tr>
<tr class="even">
<td>22</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td>[1..1]</td>
<td></td>
<td>00255</td>
<td>Results Rpt/Status Chng - Date/Time</td>
</tr>
<tr class="odd">
<td>23</td>
<td>40</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00256</td>
<td>Charge to Practice</td>
</tr>
<tr class="even">
<td>24</td>
<td>10</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0074</td>
<td>00257</td>
<td>Diagnostic Serv Sect ID</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td>[1..1]</td>
<td>0123</td>
<td>00258</td>
<td>Result Status</td>
</tr>
<tr class="even">
<td>26</td>
<td>400</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00259</td>
<td>Parent Result</td>
</tr>
<tr class="odd">
<td>27</td>
<td>200</td>
<td>TQ</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00221</td>
<td>Quantity/Timing</td>
</tr>
<tr class="even">
<td>28</td>
<td>250</td>
<td>XCN</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00260</td>
<td>Result Copies To</td>
</tr>
<tr class="odd">
<td>29</td>
<td>200</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td></td>
<td>00222</td>
<td>Parent</td>
</tr>
<tr class="even">
<td>30</td>
<td>20</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0124</td>
<td>00262</td>
<td>Transportation Mode</td>
</tr>
<tr class="odd">
<td>31</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00263</td>
<td>Reason for Study</td>
</tr>
<tr class="even">
<td>32</td>
<td>200</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td></td>
<td>00264</td>
<td>Principal Result Interpreter</td>
</tr>
<tr class="odd">
<td>33</td>
<td>200</td>
<td>CM</td>
<td>RE</td>
<td>[0..10]</td>
<td></td>
<td>00265</td>
<td>Assistant Result Interpreter</td>
</tr>
<tr class="even">
<td>34</td>
<td>200</td>
<td>CM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00266</td>
<td>Technician</td>
</tr>
<tr class="odd">
<td>35</td>
<td>200</td>
<td>CM</td>
<td>RE</td>
<td>[0..1]</td>
<td></td>
<td>00267</td>
<td>Transcriptionist</td>
</tr>
<tr class="even">
<td>36</td>
<td>26</td>
<td>TS</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>00268</td>
<td>Scheduled Date/Time</td>
</tr>
<tr class="odd">
<td>37</td>
<td>4</td>
<td>NM</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01028</td>
<td>Number of Sample Containers</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01029</td>
<td>Transport Logistics of Collected Sample</td>
</tr>
<tr class="odd">
<td>39</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01030</td>
<td>Collector’s Comment</td>
</tr>
<tr class="even">
<td>40</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01031</td>
<td>Transport Arrangement Responsibility</td>
</tr>
<tr class="odd">
<td>41</td>
<td>30</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0224</td>
<td>01032</td>
<td>Transport Arranged</td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>ID</td>
<td>X</td>
<td>[0..0]</td>
<td>0225</td>
<td>01033</td>
<td>Escort Required</td>
</tr>
<tr class="odd">
<td>43</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td></td>
<td>01034</td>
<td>Planned Patient Transport Comment</td>
</tr>
<tr class="even">
<td>44</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0088</td>
<td>00393</td>
<td>Procedure Code</td>
</tr>
<tr class="odd">
<td>45</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0340</td>
<td>01316</td>
<td>Procedure Code Modifier</td>
</tr>
<tr class="even">
<td>46</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0411</td>
<td>01474</td>
<td>Placer Supplemental Service Information</td>
</tr>
<tr class="odd">
<td>47</td>
<td>250</td>
<td>CE</td>
<td>X</td>
<td>[0..0]</td>
<td>0411</td>
<td>01475</td>
<td>Filler Supplemental Service Information</td>
</tr>
</tbody>
</table>

### ZDS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the field defined for the ZDS Segment in HL7. For a more detailed explanation of the fields used by VistA, refer to Section 4.6.4 on page [75](#_Fields_Used_in_6).

| Seq | Len | DT  | Usage | Cardinality | TBL# | Item \# | Element Name       |
|-----|-----|-----|-------|-------------|------|---------|--------------------|
| 1   | 200 | RP  | R     | \[1..1\]    |      |         | Study Instance UID |

### OBX Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For a listing of all the fields defined for the OBX segment in HL7, refer to 3.5.7 OBX Segment on page [22](#_OBX_Segment).
- For an explanation of the OBX segment fields used by VistA order and report messages, refer to 4.6.4 OBX Segment Fields in ORU Messages on page [75](#_Fields_Used_in_6).

### MSA Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For a listing of all the fields defined for the MSA segments in HL7, refer to 3.5.8 MSA Segment on page [22](#msa-segment).
- For an explanation of the MSA segment fields used by VistA acknowledgment messages, refer to 4.7.1 MSA Segment Fields on page[78](#msa-segment-fields-in-ack-messages) .

## Static Definition – Field Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MSH Segment Fields in ORU Messages (Outbound and Inbound)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When outbound ORU messages are sent from Rad/Nuc Med to an outside application (subscriber or other HL7 subscriber), the MSH segment attributes are the same as in the full MSH Segment table on page [15](#msh-segment).

When inbound ORU messages are sent from an outside application to Rad/Nuc Med, the MSH segment attributes are essentially the same as those listed in the MSH Segment table on page [15](#msh-segment).

### PID Segment Fields in ORU Messages (Outbound and Inbound)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Identifier segment is used in ORM and ORU messages. The PID segment attributes are the same as in the full PID Segment table, on page [16](#pid-segment); regardless of whether the ORU message is outbound from Rad/Nuc Med to an outside application (subscriber or HL7 subscriber), or inbound from an outside application to Rad/Nuc Med.

For an explanation of the PID segment fields used in the VistA order and report messages, refer to 3.6.2 PID Segment Fields on page [28](#pid-segment-fields).

### OBR Segment Fields in ORU Messages (Outbound and Inbound)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Request segment is used in ORM and ORU messages, though field usage is different for ORM messages. A description of each OBR segment field element is provided in the table; unsupported fields are not described.

This table of OBR segment attributes for ORU messages applies to outbound ORU messages, sent from Rad/Nuc Med to an outside application, and inbound ORU messages from an outside application to Rad/Nuc Med.

| Segment | Seq \# | Usage | Field Element Name and Values                                                              |
|---------|--------|-------|--------------------------------------------------------------------------------------------|
| OBR     | 1      | R     | Set ID – OBR                                                                               |
|         | 2      | R     | Placer Order Number                                                                        |
|         | 3      | R     | Filler Order Number (Exam & Case IDs)                                                      |
|         | 4      | R     | Universal Service ID                                                                       |
|         | 5      | X     | Priority – OBR                                                                             |
|         | 6      | X     | Requested Date/Time                                                                        |
|         | 7      | R     | Observation Date/Time                                                                      |
|         | 8      | X     | Observation End Date/Time                                                                  |
|         | 9      | X     | Collection Volume                                                                          |
|         | 10     | X     | Collector Identifier                                                                       |
|         | 11     | X     | Specimen Action Code                                                                       |
|         | 12     | X     | Danger Code                                                                                |
|         | 13     | X     | Relevant Clinical Information                                                              |
|         | 14     | X     | Specimen Received Date/Time                                                                |
|         | 15     | RE    | Specimen Source                                                                            |
|         | 16     | R     | Ordering Provider                                                                          |
|         | 17     | RE    | Order Callback Phone Number                                                                |
|         | 18     | R     | Placer Field 1                                                                             |
|         | 19     | R     | Placer Field 2                                                                             |
|         | 20     | R     | Filler Field 1                                                                             |
|         | 21     | R     | Filler Field 2                                                                             |
|         | 22     | R     | Results Report Status Change – Date/Time                                                   |
|         | 23     | X     | Charge to Practice                                                                         |
|         | 24     | X     | Diagnostic Service Section ID                                                              |
|         | 25     | R     | Result Status (F=final, R=results stored, not verified, C=correction to results, verified) |
|         | 26     | X     | Parent Result                                                                              |
|         | 27     | X     | Quantity/Timing                                                                            |
|         | 28     | X     | Result Copies To                                                                           |
|         | 29     | RE    | Parent                                                                                     |
|         | 30     | X     | Transportation Mode                                                                        |
|         | 31     | X     | Reason for Study                                                                           |
|         | 32     | RE    | Principal Result Interpreter                                                               |
|         | 33     | RE    | Assistant Result Interpreter                                                               |
|         | 34     | X     | Technician                                                                                 |
|         | 35     | RE    | Transcriptionist                                                                           |
|         | 36     | X     | Scheduled Date/Time                                                                        |
|         | 37     | X     | Number of Sample Containers                                                                |
|         | 38     | X     | Transport Logistics of Collected Sample                                                    |
|         | 39     | X     | Collector’s Comment                                                                        |
|         | 40     | X     | Transport Arrangement Responsibility                                                       |
|         | 41     | X     | Transport Arranged                                                                         |
|         | 42     | X     | Escort Required                                                                            |
|         | 43     | X     | Planned Patient Transfer Comment                                                           |
|         | 44     | X     | Procedure Code                                                                             |
|         | 45     | X     | Procedure Code Modifier                                                                    |
|         | 46     | X     | Placer Supplemental Service Information                                                    |
|         | 47     | X     | Filler Supplemental Service Information                                                    |

#### OBR-1-Set ID

This field contains an integer corresponding to the ordinal position of the OBR segment in the message. The first occurrence is labeled 1, the second 2, and so on.

#### OBR-2-Placer Order Number

This field contains the medical center site number (Facility Identifier) of the examination, concatenated with the date of the examination, concatenated with Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.

Example: 688-102104-1693

#### OBR-3-Filler Order Number

This field contains the medical center site number (Facility Identifier) of the examination, concatenated with the date of the examination, concatenated with Day-Case \# of the examination (Accession Number). The elements of this field are separated by hyphens.

Example: 688-102104-1693

#### OBR-4-Universal Service Identifier

This field contains six components.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | R     | \[1..1\]    |      | Alternate Text                  |
| 6   | 250 | ST  | R     | \[1..1\]    |      | Name of Alternate Coding System |

#### OBR-4.1-Identifier

This component is populated with the CPT code from the VistA CPT file (#81).

#### OBR-4.2-Text

This component is populated with the short name associated with the CPT code in the OBR-4.1-Identifier.

#### OBR-4.3-Name of Coding System

This component is populated with the value C4.

#### OBR-4.4-Alternate Identifier

This component contains the internal entry number (IEN) of the procedure in the VistA RAD/NUC MED PROCEDURES file (#71).

#### OBR-4.5-Alternate Text

This component is populated with the name of the procedure as defined in the RAD/NUC MED PROCEDURES file (#71).

#### OBR-4.6-Name of Alternate Coding System

This component is populated with the value 99RAP.

#### OBR-7-Observation Date/Time

This field contains the date and time the interpreting physician entered the report.

#### OBR-15-Specimen Source

This field contains six components. Only component 5 is populated. When a procedure modifier (LEFT or RIGHT) is included in the order, that value is sent in subcomponent 2 of component 5.

| Seq | Len   | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-------|-----|-------|-------------|------|---------------------------------|
| 1   | 250   | CE  | X     | \[0..0\]    |      | Specimen Source Name or Code    |
| 2   | 65535 | TX  | X     | \[0..0\]    |      | Additives                       |
| 3   | 65535 | TX  | X     | \[0..0\]    |      | Free text                       |
| 4   | 250   | CE  | X     | \[0..0\]    |      | Procedure Modifier              |
| 5   | 250   | CE  | RE    | \[0..1\]    |      | Site Modifier                   |
| 6   | 250   | CE  | X     | \[0..0\]    |      | Collection Method Modifier Code |

#### OBR-16-Ordering Provider

This field contains the ID number and name of the provider who requested the order. Only the first four components are used. Other components are ignored.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                     |
|-----|-----|-----|-------|-------------|------|--------------------------------------------------|
| 1   | 10  | ST  | R     | \[1..1\]    |      | ID Number                                        |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name                                      |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name                                       |
| 4   | 250 | ST  | R     | \[1..1\]    |      | Middle Initial or Name                           |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Suffix                                           |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Prefix                                           |
| 7   | 10  | IS  | X     | \[0..0\]    | 0360 | Degree                                           |
| 8   | 10  | IS  | X     | \[0..0\]    | 0297 | Source Table                                     |
| 9   | 250 | HD  | X     | \[0..0\]    | 0363 | Assigning Authority                              |
| 10  | 10  | ID  | X     | \[0..0\]    | 0200 | Name Type Code                                   |
| 11  | 1   | ST  | X     | \[0..0\]    |      | Identifier Check Digit                           |
| 12  | 10  | ID  | X     | \[0..0\]    | 0061 | Code Identifying the Check Digit Scheme Employed |
| 13  | 10  | IS  | X     | \[0..0\]    | 0203 | Identifier Type Code                             |
| 14  | 250 | HD  | X     | \[0..0\]    | 0300 | Assigning Facility                               |
| 15  | 10  | ID  | X     | \[0..0\]    | 4000 | Name Representation Code                         |

#### OBR-17-Order Callback Phone Number

This field contains up to eight telephone numbers that can be used to report order status or results. Only the first three components of this field are used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                                                   |
|-----|-----|-----|-------|-------------|------|----------------------------------------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] |
| 2   | 3   | ID  | R     | \[1..1\]    | 0201 | Telecommunication use code                                     |
| 3   | 10  | ID  | R     | \[1..1\]    | 0202 | Telecommunication equipment type                               |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Email address                                                  |
| 5   | 20  | NM  | X     | \[0..0\]    |      | Country code                                                   |
| 6   | 20  | NM  | X     | \[0..0\]    |      | Area/city code                                                 |
| 7   | 20  | NM  | X     | \[0..0\]    |      | Phone number                                                   |
| 8   | 20  | NM  | X     | \[0..0\]    |      | Extension                                                      |
| 9   | 250 | ST  | X     | \[0..0\]    |      | Any text                                                       |

#### OBR-17.1-\[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\]

This component is populated with the full telephone number as recorded in VistA. Components 5-9 are not used to break out the sub elements of the telephone number.

#### OBR-17.2-Telecommunication Use Code

This component is populated with the kind of number that is in component 1 with a value from HL7 Table 0201, *Telecommunication Use Code*.

| Value | Description              |
|-------|--------------------------|
| PRN   | Primary Residence Number |
| WPN   | Work Number              |
| BPN   | Beeper Number            |

#### OBR-17.3-Telecommunication Equipment Type

This component is populated with the kind of device that is reached on the number in component 1 with a value from HL7 Table 202, *Telecommunication Equipment Type*.

| Value | Description |
|-------|-------------|
| PH    | Telephone   |
| FX    | Fax         |
| BP    | Beeper      |

#### OBR-18-Placer Field 1

This field contains the Facility Identifier concatenated with the Day-Case \# of the examination (Accession Number).

> **NOTE:** OBR-18 shares the same value as OBR-2, OBR-3, and OBR-20.

#### OBR-19-Placer Field 2

This field contains the case number, which is unique only to the facility that initiated the patient event.

#### OBR-20-Filler Field 1

This field contains the Facility Identifier concatenated with Day-Case \# of the examination (Accession Number).

> **NOTE:** OBR-20 shares the same value as OBR-2, OBR-3, and OBR-18.

#### OBR-21-Filler Field 2

This field contains a number of different data attributes.

- The first component is populated with the imaging type abbreviation and the imaging type name.
- The second component is populated with the IEN of the IMAGING LOCATION (#79.1) record and the name of the HOSPITAL LOCATION (#44) referenced by that imaging location.
- The third component is populated with the IEN of the RAD/NUC MED DIVISION (#79) record and the name of the INSTITUTION (#4) referenced by that division.

The components are delimited by the accent grave (\`) and the subcomponents are delimited by the underscore (\_).

#### OBR-22-Results Rpt/Status Chng – Date/Time

This field contains the date/time the report was entered, if the report is unverified, or the date/time of verification, if the report is verified.

#### OBR-25-Result Status

This field contains the status of the report with a value from HL7 Table 0123, *Result Status*.

| Value | Description                                                                              |
|-------|------------------------------------------------------------------------------------------|
| R     | Results stored; not yet verified                                                         |
| F     | Final results; results stored and verified. Can only be changed with a corrected result. |
| C     | Correction to results                                                                    |
| VAQ   | Release Study (NTP)                                                                      |

#### OBR-29-Parent

This field contains a value to identify an examset or printset, or to indicate that the parent order of the examset or printset was purged.

- If the order is part of an examset, the field is valued as:  
  EXAMSET: *procedure_name*
- If the order is part of a printset, the field is valued as:  
  PRINTSET: *procedure_name*
- If the parent order was purged, the field is valued as:  
  ORIGINAL ORDER PURGED

#### OBR-32-Principal Result Interpreter

This field identifies the physician or other clinician who interpreted the observation and is responsible for the report content. Only component 1, Name, is populated.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name          |
|-----|-----|-----|-------|-------------|------|-----------------------|
| 1   | 250 | CN  | R     | \[1..1\]    |      | Name                  |
| 2   | 26  | TS  | X     | \[0..0\]    |      | Start Date/Time       |
| 3   | 26  | TS  | X     | \[0..0\]    |      | End Date/Time         |
| 4   | 20  | IS  | X     | \[0..0\]    |      | Point of Care         |
| 5   | 20  | IS  | X     | \[0..0\]    |      | Room                  |
| 6   | 20  | IS  | X     | \[0..0\]    |      | Bed                   |
| 7   | 250 | HD  | X     | \[0..0\]    |      | Facility              |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Location Status       |
| 9   | 20  | IS  | X     | \[0..0\]    |      | Patient Location Type |
| 10  | 20  | IS  | X     | \[0..0\]    |      | Building              |
| 11  | 20  | IS  | X     | \[0..0\]    |      | Floor                 |

#### OBR-32.1-Name

This component is populated with subcomponents.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name             |
|-----|-----|-----|-------|-------------|------|--------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | ID Number                |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name              |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name               |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | Middle Initial or Name   |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | Suffix (e.g., JR or III) |
| 6   | 250 | ST  | RE    | \[0..1\]    |      | Prefix (e.g., DR)        |
| 7   | 20  | IS  | RE    | \[0..1\]    | 0360 | Degree (e.g., MD)        |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Source Table             |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority      |

#### OBR-33-Assistant Result Interpreter

This field contains the clinical observer(s) who assisted with the interpretation of the study. Up to 10 Assistant Result Interpreters can be sent. Only component 1, Name, is populated.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name          |
|-----|-----|-----|-------|-------------|------|-----------------------|
| 1   | 250 | CN  | R     | \[1..1\]    |      | Name                  |
| 2   | 26  | TS  | X     | \[0..0\]    |      | Start Date/Time       |
| 3   | 26  | TS  | X     | \[0..0\]    |      | End Date/Time         |
| 4   | 20  | IS  | X     | \[0..0\]    |      | Point of Care         |
| 5   | 20  | IS  | X     | \[0..0\]    |      | Room                  |
| 6   | 20  | IS  | X     | \[0..0\]    |      | Bed                   |
| 7   | 250 | HD  | X     | \[0..0\]    |      | Facility              |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Location Status       |
| 9   | 20  | IS  | X     | \[0..0\]    |      | Patient Location Type |
| 10  | 20  | IS  | X     | \[0..0\]    |      | Building              |
| 11  | 20  | IS  | X     | \[0..0\]    |      | Floor                 |

#### OBR-33.1-Name

This component is populated with subcomponents.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name             |
|-----|-----|-----|-------|-------------|------|--------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | ID Number                |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name              |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name               |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | Middle Initial or Name   |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | Suffix (e.g., JR or III) |
| 6   | 250 | ST  | RE    | \[0..1\]    |      | Prefix (e.g., DR)        |
| 7   | 20  | IS  | RE    | \[0..1\]    | 0360 | Degree (e.g., MD)        |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Source Table             |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority      |

#### OBR-35-Transcriptionist

This field contains the report transcriber. Only component 1, Name, is populated.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name          |
|-----|-----|-----|-------|-------------|------|-----------------------|
| 1   | 250 | CN  | R     | \[1..1\]    |      | Name                  |
| 2   | 26  | TS  | X     | \[0..0\]    |      | Start Date/Time       |
| 3   | 26  | TS  | X     | \[0..0\]    |      | End Date/Time         |
| 4   | 20  | IS  | X     | \[0..0\]    |      | Point of Care         |
| 5   | 20  | IS  | X     | \[0..0\]    |      | Room                  |
| 6   | 20  | IS  | X     | \[0..0\]    |      | Bed                   |
| 7   | 250 | HD  | X     | \[0..0\]    |      | Facility              |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Location Status       |
| 9   | 20  | IS  | X     | \[0..0\]    |      | Patient Location Type |
| 10  | 20  | IS  | X     | \[0..0\]    |      | Building              |
| 11  | 20  | IS  | X     | \[0..0\]    |      | Floor                 |

#### OBR-35.1-Name

This component is populated with subcomponents. Only the first four subcomponents are populated; other subcomponents are not used.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name             |
|-----|-----|-----|-------|-------------|------|--------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | ID Number                |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Family Name              |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Given Name               |
| 4   | 250 | ST  | RE    | \[0..1\]    |      | Middle Initial or Name   |
| 5   | 250 | ST  | RE    | \[0..1\]    |      | Suffix (e.g., JR or III) |
| 6   | 250 | ST  | RE    | \[0..1\]    |      | Prefix (e.g., DR)        |
| 7   | 20  | IS  | RE    | \[0..1\]    | 0360 | Degree (e.g., MD)        |
| 8   | 20  | IS  | X     | \[0..0\]    |      | Source Table             |
| 9   | 250 | HD  | X     | \[0..0\]    |      | Assigning Authority      |

<span id="_Fields_Used_in_6" class="anchor"></span>

### ZDS Segment Fields in ORU and ORM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZDS segment is a user-defined segment used in ORM and ORU messages. It contains one field, Study Instance Unique Identifier, which is made up of four components.

| Segment | Seq \# | Usage | Field Element Name and Values |
|---------|--------|-------|-------------------------------|
| ZDS     | 1      | R     | Study Instance UID            |

#### ZDS-1-Study Instance UID

This field contains the unique identifier that VistA assigns to the study.

| Seq | Len | DT  | Usage | Cardinality | Item \# | Element Name   |
|-----|-----|-----|-------|-------------|---------|----------------|
| 1   | 250 | ST  | R     | \[1..1\]    |         | Pointer        |
| 2   | 250 | HD  | R     | \[1..1\]    |         | Application ID |
| 3   | 20  | ID  | R     | \[1..1\]    | 0191    | Type of Data   |
| 4   | 20  | ID  | R     | \[1..1\]    | 0291    | Subtype        |

The components of this field are populated as follows.

#### ZDS-1.1-Pointer

This component is populated with the ISO Object Identifier (OID) value that VistA assigned to the study. The subscriber and modalities must use this value instead of assigning one.

#### ZDS-1.2-Application ID

This component is populated with the value VISTA, indicating the application that generated the value in Component 1.

#### ZDS-1.3-Type of Data

This component is populated with the value Application, indicating general type of data to which it is pointed.

#### ZDS-1.4-Subtype

This component is populated with the value DICOM, indicating the specific type of data to which it is pointed.

### OBX Segment Fields in ORU Messages (Outbound and Inbound)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Segment is used in ORM and ORU messages. The OBX segment attributes are substantially the same for both outbound (from Rad/Nuc Med to an outside application) and inbound (from outside applications to Rad/Nuc Med). Certain field values are used only in inbound messages. A description of each OBX field element is provided in the table; unsupported fields are not described.

| Segment | Seq \# | Usage | Field Element Name and Values      |
|---------|--------|-------|------------------------------------|
| OBX     | 1      | R     | Set – ID OBX                       |
|         | 2      | R     | Value Type                         |
|         | 3      | R     | Observation Identifier             |
|         | 4      | X     | Observation Sub-ID                 |
|         | 5      | R     | Observation Value                  |
|         | 6      | X     | Units                              |
|         | 7      | X     | Reference Range                    |
|         | 8      | X     | Abnormal Flags                     |
|         | 9      | X     | Probability                        |
|         | 10     | X     | Nature of Abnormal Test            |
|         | 11     | R     | Observation Result Status          |
|         | 12     | X     | Date Last Observation Normal Value |
|         | 13     | X     | User Defined Access Checks         |
|         | 14     | X     | Date/Time of the Observation       |
|         | 15     | X     | Producer’s ID                      |
|         | 16     | X     | Responsible Observer               |
|         | 17     | X     | Observation Method                 |
|         | 18     | X     | Equipment Instance Identifier      |
|         | 19     | X     | Date/Time of Analysis              |

#### OBX-2-Value Type

This field contains the data type of the information carried in *OBX-5-Observation Value*. The field is populated with a value from HL7 Table 0125, *Value Type*.

| Value | Description   |
|-------|---------------|
| CE    | Coded Element |
| TX    | Text          |

#### OBX-3-Observation Identifier

This field contains the kind of information carried in *OBX-5-Observation Value*.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Name of Alternate Coding System |

#### OBX-3.1-Identifier and OBX-3.2-Text

These two components, Identifier and Text, are populated with one of the following.

| Identifier | Text            |
|------------|-----------------|
| P          | Procedure       |
| I          | Impression      |
| D          | Diagnostic Code |
| M          | Modifiers       |
| TCM        | Tech Comment    |
| C4         | CPT Modifiers   |
| R          | Report Text     |

#### OBX-3.3-Name of Coding System

This component is always populated with the value L.

#### OBX-5-Observation Value

This field contains the actual value of the data type given in *OBX-2-Value Type* and of the classification given in *OBX-3-Observation Identifier*. Formatting follows the rules for the data type given in OBX-2.

#### OBX-6-Units

For quantitative measurements, this field contains the units of the observation. For observations other than quantitative measurements, this field is not populated.

| Seq | Len | DT  | Usage | Cardinality | TBL# | Element Name                    |
|-----|-----|-----|-------|-------------|------|---------------------------------|
| 1   | 250 | ST  | R     | \[1..1\]    |      | Identifier                      |
| 2   | 250 | ST  | R     | \[1..1\]    |      | Text                            |
| 3   | 250 | ST  | R     | \[1..1\]    |      | Name of Coding System           |
| 4   | 250 | ST  | X     | \[0..0\]    |      | Alternate Identifier            |
| 5   | 250 | ST  | X     | \[0..0\]    |      | Alternate Text                  |
| 6   | 250 | ST  | X     | \[0..0\]    |      | Name of Alternate Coding System |

#### OBX-11-Observation Result Status

In the report message, this field contains a value from HL7 Table 0085, *Observation Result Status Codes Interpretation*.

| Value | Description                                                                   |
|-------|-------------------------------------------------------------------------------|
| F     | Final Results – Report Verified; can only be changed with a corrected result. |
| C     | Correction – Report replaces a previous final result                          |
| R     | Results entered but not verified; can be replaced with final results          |
| VAQ   | Release Study (NTP)                                                           |

## ACK – General Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application acknowledgment message (ACK) is sent in response to ORM and ORU messages. The function of this message is to acknowledge receipt of a message. If an ORM or ORU is sent from VistA to a subscriber vendor system, the subscriber vendor system must return an ACK in response; conversely, if a subscriber vendor system sends an ORU to VistA, VistA must return an ACK to the vendor.

ACK messages contain two segments:

| Segment | ACK Message            | HL7 Chapter |
|---------|------------------------|-------------|
| MSH     | Message Header         | 2           |
| MSA     | Message Acknowledgment | 2           |

For an example of an ACK message, refer to [Appendix A](#ack-example).

### MSA Segment Fields in ACK Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Acknowledgment segment contains three fields. A description of each MSA field element is in the table.

| Segment | Seq \# | Usage | Field Element Name and Values |
|---------|--------|-------|-------------------------------|
| MSA     | 1      | R     | Acknowledgment Code           |
|         | 2      | R     | Message Control ID            |
|         | 3      | C     | Text Message                  |

#### MSA-1-Acknowledgment Code

This field contains acknowledgment that the message was processed successfully with a value from HL7 Table 0008, *Acknowledgment Code*. Original mode acknowledgment is used.

| Value | Description        |
|-------|--------------------|
| AA    | Application Accept |
| AE    | Application Error  |
| AR    | Application Reject |

#### MSA-2-Message Control ID

This field contains the value of MSH-10-Message Control ID from the acknowledged message.

#### MSA-3-Text Message

This field contains a narrative description of the error found in the message. The ERR-1-Error Code and Location is used to communicate precise error information.

For a listing of all the fields defined for the MSA segments in HL7, refer to 3.5.8 MSA Segment on page [22](#msa-segment).

# This page intentionally left blank

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Appendix A – Message Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For reference, Appendix A contains examples of ORM, ORU, and ACK messages.

## ORM Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an exam is registered, edited, or canceled by the Rad/Nuc Med package, an Order (ORM) message is sent to the site-specified application. The messages broadcast at these three event points (registered, edited, and canceled) are almost identical, with the exception of the Order Control (ORC-1) and Order Status (ORC-5) fields.

> **NOTE:** An HL7 message for edited messages: if the exam is complete, ORC-5 is CM, otherwise the Order Status is IP.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>ORC Field</th>
<th>Registration</th>
<th>Cancel/Delete</th>
<th>Edited</th>
<th>Edited<br />
(complete)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORC-1</td>
<td>NW</td>
<td>CA</td>
<td>XO</td>
<td>XO</td>
</tr>
<tr class="even">
<td>ORC-5</td>
<td>IP</td>
<td>CA</td>
<td>IP</td>
<td>CM</td>
</tr>
</tbody>
</table>

> **NOTE:** The OBR segment can exceed 255 characters.

### ORM for new/registered order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629092627-

0500\|\|ORM^O01\|4993885697\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS-1^410^1\|\|\|\|28^RAD^PROVIDER1\|28^RAD^PROVIDER1\|\|CARDIOLOGY\|\|\|\|\|A2\|\|28^RAD

^PROVIDER1\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|NW\|141-062911-3432\|141-062911-3432\|\|IP\|\|^^^^^R\|\|201106290920-0500\|1901^RADIOLOGY

^USER1\|\|1901^RADIOLOGY^USER1\|INFORMATION RESOURCE MGMT\|123-456-7890^PRN^PH~098-7

65-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION RESOURCE MGMT^VISTA49

OBR\|1\|141-062911-3432\|141-062911-3432\|73562^X-RAY EXAM OF KNEE 3^C4^155^KNEE 3 VIEWS

^99RAP\|R\|\|\|\|\|\|\|\|\|\|^^^^&right\|1901^RADIOLOGY^USER1\|123-456-7890^PRN^PH~098-765-4321

^WPN^PH~543-543-5435^^PH\|141-062911-3432\|3432\|141-062911-3432\|RAD_GENERAL RADIOLO

GY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|\|WHLC\|^Pain in right knee when

walking.

ZDS\|1.2.840.113754.1.4.141.6889370.9079.1.141.62911.3432^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|155^KNEE 3 VIEWS^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|O

OBX\|3\|CE\|C4^CPT MODIFIERS^L\|\|26^PROFESSIONAL COMPONENT^C4\|\|\|\|\|\|O

OBX\|4\|CE\|C4^CPT MODIFIERS^L\|\|LT^LEFT SIDE^C4\|\|\|\|\|\|O

OBX\|5\|TX\|H^HISTORY^L\|\|Reason for Study: Pain in right knee when walking.\|\|\|\|\|\|O

OBX\|6\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|7\|TX\|H^HISTORY^L\|\|Clinical history text entered here for this sample case us

ing the v2.4 HL7\|\|\|\|\|\|O

OBX\|8\|TX\|H^HISTORY^L\|\|interface. \|\|\|\|\|\|O

OBX\|9\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|10\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|11\|TX\|TCM^TECH COMMENT^L\|\|The tech comment is that this is case \#3432.\|\|\|\|\|\|O

### ORM for registration of a Printset

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A printset is a group of individual orders that comprise a single report; an examset is a group of individual orders that are linked to individual reports. There are two differences between an exam or printset order message and a single order message.

#### ORC-8-Parent and OBR-29-Parent

The Parent field is populated with either the printset or examset parent name. The format is always in the form of \[PRINTSET: {*parent_procedure_name*}\] or \[EXAMSET: {*parent_procedure_name*}\].

#### OBR-2-Placer and OBR-3-Filler

These fields are populated with the site-specific accession number (Facility Identifier concatenated with Day-Case \# of the examination), which contains the same date for each descendant within a print or examset.

> **NOTE:** The same value is used to populate OBR-2, ORC-2 (for orders), OBR-3, ORC-3 (only for orders), OBR-18, and OBR-20.

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629093257-

0500\|\|ORM^O01\|4993885698\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS1^410^1\|\|\|\|28^PROVIDER^RADFOUR\|28^PROVIDER^RADFOUR\|\|CARDIOLOGY\|\|\|\|\|\|\|28^PROV

IDER^RADFOUR\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|NW\|141-062911-3433\|141-062911-3433\|141-167-6889370.907\|IP\|\|^^^^^R\|Printset: ZZPRINTSET PROCEDURE\|20

1106290929-0500\|1901^PROVIDER^RADTHREE\|\|1901^PROVIDER^RADTHREE\|INFORMATION RESOURCE

MGMT\|123-456-7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION

RESOURCE MGMT^VISTA49

OBR\|1\|141-062911-3433\|141-062911-3433\|74330^X-RAY BILE/PANC ENDOSCOPY^C4^207^ENDOSCO

PIC CATH BIL \T\\ PANC DUCTS S\T\I^99RAP\|R\|\|\|\|\|\|\|\|\|\|\|1901^PROVIDER^RADTHREE\|123-4567

890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3433\|3433\|141-062911-3

433\|RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|Printset:

ZZPRINTSET PROCEDURE\|PORT\|^Example of a printset study for use in documentation.

ZDS\|1.2.840.113754.1.4.141.6889370.907.1.141.62911.3433^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|207^ENDOSCOPIC CATH BIL \T\\ PANC DUCTS S\T\I^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|PORTABLE EXAM\|\|\|\|\|\|O

OBX\|3\|TX\|H^HISTORY^L\|\|Reason for Study: Example of a printset study for use in d

ocumentation.\|\|\|\|\|\|O

OBX\|4\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|5\|TX\|H^HISTORY^L\|\|The Clinical History text is entered here. \|\|\|\|\|\|O

OBX\|6\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|7\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|8\|TX\|TCM^TECH COMMENT^L\|\|This is the first case (3433) in the Printset.\|\|\|\|\|\|O

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629093257-

0500\|\|ORM^O01\|4993885699\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS1^410^1\|\|\|\|28^PROVIDER^RADFOUR\|28^PROVIDER^RADFOUR\|\|CARDIOLOGY\|\|\|\|\|\|\|28^PROV

IDER^RADFOUR\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|NW\|141-062911-3434\|141-062911-3434\|141-167-6889370.907\|IP\|\|^^^^^R\|Printset: ZZPRINTSET PROCEDURE\|20

1106290929-0500\|1901^PROVIDER^RADTHREE\|\|1901^PROVIDER^RADTHREE\|INFORMATION RESOURCE

MGMT\|123-456-7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION

RESOURCE MGMT^VISTA49

OBR\|1\|141-062911-3434\|141-062911-3434\|74328^X-RAY BILE DUCT ENDOSCOPY^C4^205^ENDOSCO

PIC CATH BIL DUCTS S\T\I^99RAP\|R\|\|\|\|\|\|\|\|\|\|\|1901^PROVIDER^RADTHREE\|123-4567890^PRN^P

H~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3434\|3434\|141-062911-3434\|RAD_G

ENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|Printset: ZZPRINTS

ET PROCEDURE\|PORT\|^Example of a printset study for use in documentation.

ZDS\|1.2.840.113754.1.4.141.6889370.907.2.141.62911.3434^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|205^ENDOSCOPIC CATH BIL DUCTS S\T\I^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|PORTABLE EXAM\|\|\|\|\|\|O

OBX\|3\|TX\|H^HISTORY^L\|\|Reason for Study: Example of a printset study for use in d

ocumentation.\|\|\|\|\|\|O

OBX\|4\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|5\|TX\|H^HISTORY^L\|\|The Clinical History text is entered here. \|\|\|\|\|\|O

OBX\|6\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|7\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|8\|TX\|TCM^TECH COMMENT^L\|\|This is the second case (3434) in the Printset.\|\|\|\|\|\|O

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629093258-

0500\|\|ORM^O01\|4993885700\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS1^410^1\|\|\|\|28^PROVIDER^RADFOUR\|28^PROVIDER^RADFOUR\|\|CARDIOLOGY\|\|\|\|\|\|\|28^PROV

IDER^RADFOUR\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|NW\|141-062911-3435\|141-062911-3435\|141-167-6889370.907\|IP\|\|^^^^^R\|Printset: ZZPRINTSET PROCEDURE\|20

1106290929-0500\|1901^PROVIDER^RICH\|\|1901^PROVIDER^RICH\|INFORMATION RESOURCE MGMT

\|123-456-7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION RESOU

RCE MGMT^VISTA49

OBR\|1\|141-062911-3435\|141-062911-3435\|74329^X-RAY FOR PANCREAS ENDOSCOPY^C4^206^ENDO

SCOPIC CATH PANC DUCTS S\T\I^99RAP\|R\|\|\|\|\|\|\|\|\|\|\|1901^PROVIDER^RICH\|123-456-7890^P

RN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3435\|3435\|141-062911-3435\|R

AD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|Printset: ZZPR

INTSET PROCEDURE\|PORT\|^Example of a printset study for use in documentation.

ZDS\|1.2.840.113754.1.4.141.6889370.907.3.141.62911.3435^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|206^ENDOSCOPIC CATH PANC DUCTS S\T\I^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|PORTABLE EXAM\|\|\|\|\|\|O

OBX\|3\|TX\|H^HISTORY^L\|\|Reason for Study: Example of a printset study for use in d

ocumentation.\|\|\|\|\|\|O

OBX\|4\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|5\|TX\|H^HISTORY^L\|\|The Clinical History text is entered here. \|\|\|\|\|\|O

OBX\|6\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|7\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|8\|TX\|TCM^TECH COMMENT^L\|\|This is the third and last case (3435) in the Print

set.\|\|\|\|\|\|O

### ORM for an edited order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629100417-

0500\|\|ORM^O01\|4993885701\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS1^410^1\|\|\|\|28^PROVIDER^RADFOUR\|28^PROVIDER^RADFOUR\|\|CARDIOLOGY\|\|\|\|\|A2\|\|28^PR

OVIDER^RADFOUR\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|XO\|141-062911-3432\|141-062911-3432\|\|IP\|\|^^^^^R\|\|201106290920-0500\|1901^PROVIDER

^RADTHREE\|\|1901^PROVIDER^RADTHREE\|INFORMATION RESOURCE MGMT\|123-4567890^PRN^PH~098-

765-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION RESOURCE MGMT^VISTA49

OBR\|1\|141-062911-3432\|141-062911-3432\|73562^X-RAY EXAM OF KNEE 3^C4^155^KNEE 3 VIEWS

^99RAP\|R\|\|\|\|\|\|\|\|\|\|^^^^&right\|1901^PROVIDER^RADTHREE\|123-456-7890^PRN^PH~098-7654321

^WPN^PH~543-543-5435^^PH\|141-062911-3432\|3432\|141-062911-3432\|RAD_GENERAL RADIOLO

GY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|\|WHLC\|^Pain in right knee when

walking.

ZDS\|1.2.840.113754.1.4.141.6889370.9079.1.141.62911.3432^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|155^KNEE 3 VIEWS^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|O

OBX\|3\|CE\|C4^CPT MODIFIERS^L\|\|26^PROFESSIONAL COMPONENT^C4\|\|\|\|\|\|O

OBX\|4\|CE\|C4^CPT MODIFIERS^L\|\|LT^LEFT SIDE^C4\|\|\|\|\|\|O

OBX\|5\|CE\|C4^CPT MODIFIERS^L\|\|99^MULTIPLE MODIFIERS^C4\|\|\|\|\|\|O

OBX\|6\|TX\|H^HISTORY^L\|\|Reason for Study: Pain in right knee when walking.\|\|\|\|\|\|O

OBX\|7\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|8\|TX\|H^HISTORY^L\|\|Clinical history text entered here for this sample case us

ing the v2.4 HL7\|\|\|\|\|\|O

OBX\|9\|TX\|H^HISTORY^L\|\|interface. \|\|\|\|\|\|O

OBX\|10\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|11\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|12\|TX\|TCM^TECH COMMENT^L\|\|The tech comment is that this is case \#3432.\|\|\|\|\|\|O

OBX\|13\|TX\|TCM^TECH COMMENT^L\|\|\|\|\|\|\|\|O

### ORM for a canceled order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629100555-

0500\|\|ORM^O01\|4993885702\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

PV1\|\|I\|4AS1^410^1\|\|\|\|28^PROVIDER^RADFOUR\|28^PROVIDER^RADFOUR\|\|CARDIOLOGY\|\|\|\|\|A2\|\|28^PR

OVIDER^RADFOUR\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

ORC\|CA\|141-062811-3431\|141-062811-3431\|\|CA\|\|^^^^^R\|\|201106281148-0500\|1901^PROVIDER

^RADTHREE\|\|4683^PROVIDER^ONE\|INFORMATION RESOURCE MGMT\|\|\|\|IRM^INFORMATION RESOURC

E MGMT^VISTA49

OBR\|1\|141-062811-3431\|141-062811-3431\|73500^X-RAY EXAM OF HIP^C4^145^HIP 1 VIEW^99RA

P\|R\|\|\|\|\|\|\|\|\|\|^^^^&right\|4683^PROVIDER^ONE\|\|141-062811-3431\|3431\|141-062811-3431\|

RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|\|WHLC\|^Pain in

hip when walking

ZDS\|1.2.840.113754.1.4.141.6889371.8851.1.141.62811.3431^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|145^HIP 1 VIEW^L\|\|\|\|\|\|O

OBX\|2\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|O

OBX\|3\|CE\|C4^CPT MODIFIERS^L\|\|99^MULTIPLE MODIFIERS^C4\|\|\|\|\|\|O

OBX\|4\|CE\|C4^CPT MODIFIERS^L\|\|AD^MD SUPERVISION, \>4 ANES PROC^C4\|\|\|\|\|\|O

OBX\|5\|TX\|H^HISTORY^L\|\|Reason for Study: Pain in hip when walking\|\|\|\|\|\|O

OBX\|6\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

OBX\|7\|TX\|H^HISTORY^L\|\|This is some clinical history text for a sample case using

HL7 version 2.4\|\|\|\|\|\|O

OBX\|8\|TX\|H^HISTORY^L\|\|interface messaging. \|\|\|\|\|\|O

OBX\|9\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

OBX\|10\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

OBX\|11\|TX\|TCM^TECH COMMENT^L\|\|The tech comments are entered here for this sample

case (#3431)\|\|\|\|\|\|O

OBX\|12\|TX\|TCM^TECH COMMENT^L\|\|\|\|\|\|\|\|O

OBX\|13\|TX\|TCM^TECH COMMENT^L\|\|The tech comments are entered here for this sample

case (#3431) -- CANCELLING THIS CASE!!\|\|\|\|\|\|O

## ORU Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a report is Verified or Released/Not Verified by the Rad/Nuc Med package, an Order Results (ORU) message is sent to the site-specified application.

### ORU for report on a single procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629133221-

0500\|\|ORU^R01\|4993885703\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

OBR\|1\|141-062911-3432\|141-062911-3432\|73562^X-RAY EXAM OF KNEE 3^C4^155^KNEE 3 VIEWS

^99RAP\|\|\|20110629132828-0500\|\|\|\|\|\|\|\|^^^^&right\|1901^PROVIDER^RADTHREE\|123-456-

7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3432\|3432\|141

0629113432\|RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|201106291331-

0500\|\|\|F\|\|\|\|\|\|\|76^OERR^CLINICIAN^G\|2188^RADIOLOGY^USER^G~22^STAFF^PROVIDER~4569^

STAFF^PROVIDERTWO\|\|1901^PROVIDER^RADTHREE

ZDS\|1.2.840.113754.1.4.141.6889370.9079.1.141.62911.3432^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|155^KNEE 3 VIEWS^L\|\|\|\|\|\|F

OBX\|2\|TX\|I^IMPRESSION^L\|\|This is the generic impression text entered for this sa

mple report for \|\|\|\|\|\|F

OBX\|3\|TX\|I^IMPRESSION^L\|\|documentation purposed. \|\|\|\|\|\|F

OBX\|4\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

OBX\|5\|TX\|I^IMPRESSION^L\|\|This is the last line of the sample impression text. \|

\|\|\|\|\|F

OBX\|6\|CE\|D^DIAGNOSTIC CODE^L\|\|1^NORMAL^L\|\|\|\|\|\|F

OBX\|7\|CE\|D^DIAGNOSTIC CODE^L\|\|1000^NO ALERT REQUIRED^L\|\|\|\|\|\|F

OBX\|8\|CE\|D^DIAGNOSTIC CODE^L\|\|9^NO DISCRETE MASS^L\|\|\|\|\|\|F

OBX\|9\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|F

OBX\|10\|TX\|TCM^TECH COMMENT^L\|\|The tech comment is that this is case \#3432.\|\|\|\|\|\|F

OBX\|11\|CE\|C4^CPT MODIFIERS^L\|\|26^PROFESSIONAL COMPONENT^C4\|\|\|\|\|\|F

OBX\|12\|CE\|C4^CPT MODIFIERS^L\|\|LT^LEFT SIDE^C4\|\|\|\|\|\|F

OBX\|13\|CE\|C4^CPT MODIFIERS^L\|\|99^MULTIPLE MODIFIERS^C4\|\|\|\|\|\|F

OBX\|14\|TX\|R^REPORT^L\|\|This is the report text for case \#3432, which was a Knee e

xam for the \|\|\|\|\|\|F

OBX\|15\|TX\|R^REPORT^L\|\|patient. This sample report text will be filed in the Rad

iology Report \|\|\|\|\|\|F

OBX\|16\|TX\|R^REPORT^L\|\|file for the patient/exam. \|\|\|\|\|\|F

### ORU for Printset (single report on multiple procedures)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629134632-

0500\|\|ORU^R01\|4993885704\|P\|2.4\|\|\|\|\|USA

PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

89^""^^CDC

OBR\|1\|141-062911-3433\|141-062911-3433\|74330^X-RAY BILE/PANC ENDOSCOPY^C4^207^ENDOSCO

PIC CATH BIL \T\\ PANC DUCTS S\T\I^99RAP\|\|\|20110629133257-0500\|\|\|\|\|\|\|\|\|1901^PROVIDER

^RADTHREE\|123-456-7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3433

\|3433\|141-062911-3433\|RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|2011

06291346-0500\|\|\|F\|\|\|\|Printset: ZZPRINTSET PROCEDURE\|\|\|76^OERR^CLINICIAN^G\|2188^R

ADIOLOGY^USER^G~2178^STAFF^PROVIDER~4569^STAFF^PROVIDERTWO\|\|1901^PROVIDER^RADTHREE

ZDS\|1.2.840.113754.1.4.141.6889370.907.1.141.62911.3433^VISTA^Application^DICOM

OBX\|1\|CE\|P^PROCEDURE^L\|\|207^ENDOSCOPIC CATH BIL \T\\ PANC DUCTS S\T\I^L\|\|\|\|\|\|F

OBX\|2\|TX\|I^IMPRESSION^L\|\|This is the impression text for the printset. \|\|\|\|\|\|F

OBX\|3\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

OBX\|4\|TX\|I^IMPRESSION^L\|\|Cases 3433, 3434 and 3435 will all receive the same text.

\|\|\|\|\|\|F

OBX\|5\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

OBX\|6\|TX\|I^IMPRESSION^L\|\|Final line of impression text. \|\|\|\|\|\|F

OBX\|7\|CE\|D^DIAGNOSTIC CODE^L\|\|1^NORMAL^L\|\|\|\|\|\|F

OBX\|8\|CE\|D^DIAGNOSTIC CODE^L\|\|9^NO DISCRETE MASS^L\|\|\|\|\|\|F

OBX\|9\|CE\|D^DIAGNOSTIC CODE^L\|\|13^CODE WITH AN \T\\ IN IT (HL7 TEST)^L\|\|\|\|\|\|F

OBX\|10\|TX\|M^MODIFIERS^L\|\|PORTABLE EXAM\|\|\|\|\|\|F

OBX\|11\|TX\|TCM^TECH COMMENT^L\|\|This is the first case (3433) in the Printset.\|\|\|\|\|\|F

OBX\|12\|TX\|R^REPORT^L\|\|This is the report text for the printset exam, case number

s 3433, 3434 and\|\|\|\|\|\|F

OBX\|13\|TX\|R^REPORT^L\|\|3435. \|\|\|\|\|\|F

OBX\|14\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F

OBX\|15\|TX\|R^REPORT^L\|\|This sample report text will be filed in the Radiology Rep

ort file and all\|\|\|\|\|\|F

OBX\|16\|TX\|R^REPORT^L\|\|3 cases in the printset will point to the same report. \|\|\|\|\|\|F

OBX\|17\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F

OBX\|18\|TX\|R^REPORT^L\|\|This is the last line of the report text. \|\|\|\|\|\|F

## ACK Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The General Acknowledgment (ACK) message is sent by both systems in response to ORM and ORU messages. The ACK message format is the same for ORM and ORU messages.

MSH\|^~\\\|RA-TALKLINK-TCP\|TALKSTATION\|RA-VOICE-SERVER\|HINES

CIOFO\|\|\|ACK\|200503311137070234\|P\|2.3\|\|

MSA\|AA\|4993680801\|

# Appendix B – VistA Data Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tables show the relationship between VistA Radiology data attributes and the HL7 message segment counterparts.

## MSH Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of MSH segment field elements in ORM and ORU messages, refer to MSH Segment Fields in ORM on page [23](#msh-segment-fields-in-orm-and-oru) and MSH Segment Fields in ORU on page [66](#msh-segment-fields-in-oru-messages-outbound-and-inbound).

| MSH Segment | PID Field Name        | VistA File                        | VistA Field(s)                 |
|-------------|-----------------------|-----------------------------------|--------------------------------|
| MSH-2       | ENCODING CHARACTERS   | HL7 APPLICATION PARAMETER (#771)  | HL7 ENCODING CHARACTERS (#101) |
| MSH-3       | SENDING APPLICATION   | HL7 APPLICATION PARAMETER (#771)  | NAME (#.01)                    |
| MSH-4       | SENDING FACILITY      | HL7 APPLICATION PARAMETER (#771)  | FACILITY NAME (#3)             |
| MSH-5       | RECEIVING APPLICATION | HL7 APPLICATION PARAMETER (#771)  | NAME (#.01)                    |
| MSH-6       | RECEIVING FACILITY    | HL7 APPLICATION PARAMETER (#771)  | FACILITY NAME (#3)             |
| MSH-7       | DATE/TIME OF MESSAGE  | HL7 MESSAGE TEXT (#772)           | DATE/TIME ENTERED (#.01)       |
| MSH-9       | MESSAGE TYPE          | HL7 MESSAGE ADMINISTRATION (#773) | TRANSMISSION TYPE (#3)         |
| MSH-10      | MESSAGE CONTROL ID    | HL7 MESSAGE ADMINISTRATION (#773) | MESSAGE ID (#2)                |
| MSH-11      | PROCESSING ID         | HL7 MESSAGE TEXT (#772)           | MESSAGE ID (#6)                |
| MSH-12      | VERSION ID            | HL7 VERSION (#771.5)              | VERSION (#.01)                 |
| MSH-17      | COUNTRY CODE          | HL7 APPLICATION PARAMETER (#771)  | COUNTRY CODE (#7)              |

## PID Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of PID segment field elements in ORM and ORU messages, refer to PID Segment Fields in ORM on page [28](#pid-segment-fields) and PID Segment Fields in ORU on page [66](#pid-segment-fields-in-oru-messages-outbound-and-inbound).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th>PID Segment<br />
$$PID^MAGDHLS</th>
<th>PID Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PID-2</td>
<td>PATIENT ID</td>
<td>INSTITUTION (#4) and PATIENT (#2)</td>
<td>STATION NUMBER (#99) of INSTITUTION (#4) file concatenated with Patient DFN</td>
</tr>
<tr class="even">
<td>PID-3</td>
<td>PATIENT IDENTIFIER LIST</td>
<td>PATIENT (#2)</td>
<td>SSN (#.09)</td>
</tr>
<tr class="odd">
<td>PID-4</td>
<td>ALTERNATE PATIENT ID</td>
<td>PATIENT (#2)</td>
<td>INTEGRATION CONTROL NUMBER (#991.01)</td>
</tr>
<tr class="even">
<td>PID-5</td>
<td>PATIENT NAME</td>
<td>PATIENT (#2)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="odd">
<td>PID-7</td>
<td>DATE/TIME OF BIRTH</td>
<td>PATIENT (#2)</td>
<td>DATE OF BIRTH (#.03)</td>
</tr>
<tr class="even">
<td>PID-8</td>
<td>ADMINISTRATIVE SEX</td>
<td>PATIENT (#2)</td>
<td>SEX (#.02)</td>
</tr>
<tr class="odd">
<td>PID-10</td>
<td>RACE</td>
<td>PATIENT (#2)</td>
<td>RACE (#.06)</td>
</tr>
<tr class="even">
<td>PID-11</td>
<td>PATIENT ADDRESS</td>
<td>PATIENT (#2)</td>
<td>STREET ADDRESS [LINE 1] (#.111)<br />
STREET ADDRESS [LINE 1] (#.112)<br />
STREET ADDRESS [LINE 1] (#.113)<br />
CITY (#.114)<br />
STATE (#.115)<br />
ZIP CODE (#.116)</td>
</tr>
<tr class="odd">
<td>PID-13</td>
<td>PHONE NUMBER-HOME</td>
<td>PATIENT (#2)</td>
<td>PHONE NUMBER [RESIDENCE] (#.131)</td>
</tr>
<tr class="even">
<td>PID-14</td>
<td>PHONE NUMBER-BUSINESS</td>
<td>PATIENT (#2)</td>
<td>PHONE NUMBER [WORK] (#.132)</td>
</tr>
<tr class="odd">
<td>PID-19</td>
<td>SS NUMBER-PATIENT</td>
<td>PATIENT (#2)</td>
<td>SOCIAL SECURITY NUMBER (#09)</td>
</tr>
<tr class="even">
<td>PID-22</td>
<td>ETHNIC GROUP</td>
<td>PATIENT (#2)</td>
<td>ETHNICITY INFORMATION (#6)</td>
</tr>
</tbody>
</table>

> **NOTE:** Functions \$\$PID^MAGDHLS and \$\$PV1^MAGDHLS are covered by Integration Agreement 5023.

## PV-1 Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of PV-1 segment field elements, refer to PV-1 Segment Fields in ORM on page [37](#pv1-segment-fields-in-orm).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th>PV1 Segment<br />
$$PV1^MAGDHLS</th>
<th>PV1 Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PV1-2</td>
<td>PATIENT CLASS</td>
<td></td>
<td>“I” if patient is an Inpatient, “O” if patient is an Outpatient</td>
</tr>
<tr class="even">
<td>PV1-3</td>
<td>ASSIGNED PATIENT LOCATION</td>
<td>WARD LOCATION (#42)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="odd">
<td>PV1-7</td>
<td>ATTENDING DOCTOR</td>
<td>NEW PERSON (#200)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="even">
<td>PV1-8</td>
<td>REFERRING DOCTOR</td>
<td>NEW PERSON (#200)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="odd">
<td>PV1-10</td>
<td>HOSPITAL SERVICE</td>
<td>HOSPITAL LOCATION (#44)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="even">
<td>PV1-11</td>
<td>TEMPORARY LOCATION</td>
<td><p>HOSPITAL LOCATION (#44)</p>
<p>INSTITUTION (#4)</p></td>
<td><p>NAME (#.01)</p>
<p>INSTITUTION (#3)</p>
<p>NAME (#.01)</p></td>
</tr>
<tr class="odd">
<td>PV1-15</td>
<td>AMBULATORY STATUS</td>
<td>RAD/NUC MED PATIENT (#70) or if that is null RAD/NUC MED ORDERS (#75.1)</td>
<td>PREGNANCY SCREEN (#70.03, #32) or PREGNANT (#75.1, #13) AND MODE OF TRANSPORT (#75.1, #19)</td>
</tr>
<tr class="even">
<td>PV1-16</td>
<td>VIP INDICATOR</td>
<td></td>
<td>“E” if patient is a VA Employee, “S” if the patient record is sensitive, “ES” if patient is a VA Employee and patient record is sensitive.</td>
</tr>
<tr class="odd">
<td>PV1-19</td>
<td>VISIT</td>
<td>PATIENT MOVEMENT (#405)</td>
<td>“I” concatenated with a Pointer Value to the Patient Movement File (#405) if patient is an Inpatient, “O” concatenated with today’s date if patient is an Outpatient.</td>
</tr>
</tbody>
</table>

## ORC Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of ORC segment field elements in ORM messages, refer to ORC Segment Fields in ORM on page [42](#orc-segment-fields-in-orm).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 19%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>ORC Segment</th>
<th>ORC Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORC-1</td>
<td>ORDER CONTROL</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4">ORC-2</td>
<td rowspan="4"><p>PLACER ORDER NUMBER (station #-day-case #)</p>
<p>Note: The first 3 characters of the possible 7-character station number are used as the site identifier. Integration Agreements 2171 ($$NS^XUAF4) &amp; 2541 ($$KSP^XUPARAM) are used to create the site identifier.</p></td>
<td>KERNEL SYSTEM PARAMETERS (#8989.3)</td>
<td>DEFAULT INSTITUTION (#217)</td>
</tr>
<tr class="odd">
<td>INSTITUTION (#4)</td>
<td>STATION NUMBER (#99)</td>
</tr>
<tr class="even">
<td>REGISTERED EXAMS subfile (#70.02)</td>
<td>EXAM DATE (#.01)</td>
</tr>
<tr class="odd">
<td>EXAMINATIONS EXAMS subfile (#70.03)</td>
<td>CASE NUMBER (#.01)</td>
</tr>
<tr class="even">
<td>ORC-3</td>
<td>FILLER ORDER NUMBER (station #-day-case #)</td>
<td>See ORC-2</td>
<td><p>See ORC-2</p>
<p><strong>Note:</strong> ORC-2, ORC-3, OBR-2, OBR-3, OBR-18, &amp; OBR-20 share the same values. 7F<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></td>
</tr>
<tr class="odd">
<td rowspan="3">ORC-4</td>
<td rowspan="3">PLACER GROUP NUMBER (station #-patient DFN-inverse exam date/time)</td>
<td>INSTITUTION (#4),</td>
<td>STATION NUMBER (#99),</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PATIENT DFN</td>
</tr>
<tr class="odd">
<td>REGISTERED EXAMS subfile (#70.02)</td>
<td>EXAM DATE (#.01)</td>
</tr>
<tr class="even">
<td>ORC-5</td>
<td>ORDER STATUS</td>
<td>EXAMINATION STATUS (#72)</td>
<td>ORDER (#3)</td>
</tr>
<tr class="odd">
<td>ORC-7</td>
<td>QUANTITY/TIMING</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ORC-7.4</td>
<td>START DATE/TIME</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>SCHEDULED DATE (TIME optional) (#23)</td>
</tr>
<tr class="odd">
<td>ORC-7.6</td>
<td>PRIORITY</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>REQUEST URGENCY (#6)</td>
</tr>
<tr class="even">
<td>ORC-8</td>
<td>PARENT</td>
<td>EXAMINATIONS SUBFILE (#70.03)</td>
<td><p>MEMBER OF SET (#25)</p>
<p><strong>Note:</strong> ORC-8 &amp; OBR-29 share the same value.</p></td>
</tr>
<tr class="odd">
<td>ORC-9</td>
<td>DATE/TIME OF TRANSACTION</td>
<td>REGISTERED EXAMS subfile (#70.02)</td>
<td>EXAM DATE (#.01)</td>
</tr>
<tr class="even">
<td>ORC-10</td>
<td>ENTERED BY</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>USER ENTERING REQUEST (#15)</td>
</tr>
<tr class="odd">
<td>ORC-12</td>
<td>ORDERING PROVIDER</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>REQUESTING PHYSICIAN (#14)</td>
</tr>
<tr class="even">
<td>ORC-13</td>
<td>ENTERER'S LOCATION</td>
<td>NEW PERSON (#200)</td>
<td>SERVICE/SECTION (#29)</td>
</tr>
<tr class="odd">
<td>ORC-14</td>
<td>CALL BACK PHONE NUMBER</td>
<td>NEW PERSON (#200)</td>
<td><p>OFFICE PHONE (#.132)</p>
<p><strong>Note:</strong> The function NPFON^MAG7UFO (IA: 5021) is called to build the call back phone number list</p></td>
</tr>
<tr class="even">
<td>ORC-17</td>
<td>ENTERER'S ORGANIZATION</td>
<td>NEW PERSON (#200)</td>
<td><p>SERVICE/SECTION (#29)</p>
<p><strong>Note:</strong> returns SERVICE/SECTION NAME (#.01) &amp; ABBREVIATION (#1)</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>July 2007 Updated the note to reflect the definition changes for the HL7 fields of both the ORM and ORU messages.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

## OBR Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of OBR segment field elements in ORM and ORU messages, refer to OBR Segment Fields in ORM on page [48](#obr-segment-fields-in-orm) and OBR Segment Fields in ORU on page [66](#obr-segment-fields-in-oru-messages-outbound-and-inbound).

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 19%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>OBR Segment</th>
<th>OBR Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OBR-1</td>
<td>SET ID</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4">OBR-2</td>
<td rowspan="4"><p>PLACER ORDER NUMBER (station #-day-case #)</p>
<p><strong>Note:</strong> The first three characters of the possible seven-character station number are used as the site identifier. Integration Agreements 2171 ($$NS^XUAF4) &amp; 2541 ($$KSP^XUPARAM) are used to create the site identifier.</p></td>
<td>REGISTERED EXAMS subfile (#70.02)</td>
<td>EXAM DATE (#.01)</td>
</tr>
<tr class="odd">
<td>EXAMINATIONS EXAMS subfile (#70.03)</td>
<td>CASE NUMBER (#.01)</td>
</tr>
<tr class="even">
<td>KERNEL SYSTEM PARAMETERS (#8989.3)</td>
<td>DEFAULT INSTITUTION (#217)</td>
</tr>
<tr class="odd">
<td>INSTITUTION (#4)</td>
<td>STATION NUMBER (#99)</td>
</tr>
<tr class="even">
<td>OBR-3</td>
<td>FILLER ORDER NUMBER (station #-day-case #)</td>
<td>See OBR-2</td>
<td><p>See OBR-2</p>
<p><strong>Note:</strong> ORC-2, ORC-3, OBR-2, OBR-3, OBR-18, &amp; OBR-20 share the same values.</p></td>
</tr>
<tr class="odd">
<td>OBR-4</td>
<td>UNIVERSAL SERVICE ID</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBR-4.1</td>
<td>IDENTIFIER</td>
<td>CPT (#81)</td>
<td>CPT CODE (#.01)</td>
</tr>
<tr class="odd">
<td>OBR-4.2</td>
<td>TEXT</td>
<td>CPT (#81)</td>
<td>SHORT NAME (#2)</td>
</tr>
<tr class="even">
<td>OBR-4.3</td>
<td><p>NAME OF CODING SYSTEM</p>
<p>Field is populated with a value of C4</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="odd">
<td>OBR-4.4</td>
<td>ALTERNATE IDENTIFIER</td>
<td>RAD/NUC MED PROCEDURES (#71)</td>
<td>IEN</td>
</tr>
<tr class="even">
<td>OBR-4.5</td>
<td>ALTERNATE TEXT</td>
<td>RAD/NUC MED PROCEDURES (#71)</td>
<td>NAME (#.01)</td>
</tr>
<tr class="odd">
<td>OBR-4.6</td>
<td><p>NAME OF ALTERNATE CODING SYSTEM</p>
<p>Field is populated with a value of 99RAP</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td>OBR-5</td>
<td>PRIORITY</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>REQUEST URGENCY (#6)</td>
</tr>
<tr class="odd">
<td><p>OBR-7</p>
<p><strong>Note:</strong> in ORU message only</p></td>
<td>OBSERVATION DATE/TIME</td>
<td>RAD/NUC MED REPORTS (#74)</td>
<td>DATE REPORT ENTERED (#6)</td>
</tr>
<tr class="even">
<td>OBR-15</td>
<td>SPECIMEN SOURCE</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OBR-15.5</td>
<td><p>SITE MODIFIER</p>
<p><strong>Note:</strong> Only ‘Left’ and ‘Right’ procedure modifiers are captured.</p></td>
<td>PROCEDURE MODIFIERS (#75.1125)</td>
<td>PROCEDURE MODIFIERS (#.01)</td>
</tr>
<tr class="even">
<td>OBR-16</td>
<td>ORDERING PROVIDER</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td><p>REQUESTING PHYSICIAN (#14)</p>
<p><strong>Note:</strong> Integration Agreement 3065 breaks the REQUESTING PHYSICIAN name into the four HL7 name components below.</p></td>
</tr>
<tr class="odd">
<td>OBR-16.1</td>
<td>ID NUMBER</td>
<td>NEW PERSON (#200)</td>
<td>IEN from File #200</td>
</tr>
<tr class="even">
<td>OBR-16.2</td>
<td>FAMILY NAME</td>
<td>See OBR-16</td>
<td>See OBR-16</td>
</tr>
<tr class="odd">
<td>OBR-16.3</td>
<td>GIVEN NAME</td>
<td>See OBR-16</td>
<td>See OBR-16</td>
</tr>
<tr class="even">
<td>OBR-16.4</td>
<td>MIDDLE INITIAL OR NAME</td>
<td>See OBR-16</td>
<td>See OBR-16</td>
</tr>
<tr class="odd">
<td>OBR-17</td>
<td>ORDER CALLBACK PHONE NUMBER</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBR-17.1</td>
<td>[NNN] [(999)]999-9999 [X99999] [B99999] [C ANY TEXT]</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OBR-17.2</td>
<td><p>TELECOMMUNICATION USE CODE</p>
<p>Field is populated with one of the values below:</p>
<p>PRN-Primary Residence Number</p>
<p>WPN-Work Number</p>
<p>BPN-Beeper</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td>OBR-17.3</td>
<td><p>TELECOMMUNICATION EQUIPMENT TYPE</p>
<p>Field is populated with one of the values below:</p>
<p>PH-Telephone</p>
<p>FX-Fax</p>
<p>BP-Beeper</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="odd">
<td>OBR-18</td>
<td>PLACER FIELD 1</td>
<td>See OBR-2</td>
<td><p>See OBR-2</p>
<p><strong>Note:</strong> ORC-2, ORC-3, OBR-2 &amp; OBR-3, OBR-18, OBR-20 share the same values.</p></td>
</tr>
<tr class="even">
<td>OBR-19</td>
<td>PLACER FIELD 2</td>
<td>CASE NUMBER (#.01) field of the EXAMINATIONS subfile (#70.03)</td>
<td>The case number of the exam</td>
</tr>
<tr class="odd">
<td>OBR-20</td>
<td>FILLER FIELD 1</td>
<td>See OBR-18</td>
<td>See OBR-18</td>
</tr>
<tr class="even">
<td>OBR-21</td>
<td>FILLER FIELD 2</td>
<td><p>IMAGING TYPE (#79.2)</p>
<p>IMAGING LOCATION (#79.1)</p>
<p>HOSPITAL LOCATION file (#44)</p>
<p>RAD/NUC MED DIVISION (#79)</p>
<p>INSTITUTION (#4)</p></td>
<td>Imaging type (#79.2) abbreviation concatenated to (by an underscore as a separator) imaging type name concatenated (by the tick “`” mark) to imaging location (#79.1) record IEN concatenated (underscore) to the name of the imaging location from the HOSPITAL LOCATION file (#44) concatenated (tick) to the RAD/NUC MED DIVISION (#79) file IEN concatenated (underscore) to the name of the hospital division from the INSTITUTION (#4) file</td>
</tr>
<tr class="odd">
<td><p>OBR-22</p>
<p><strong>Note:</strong> in ORU message only</p></td>
<td>RESULTS REPORT STATUS CHANGE - DATE/TIME</td>
<td>RAD/NUC MED REPORTS (#74)</td>
<td><p>If verified: VERIFIED DATE (#7)</p>
<p>Else: DATE REPORT ENTERED (#6)</p></td>
</tr>
<tr class="even">
<td><p>OBR-24</p>
<p><strong>Note:</strong> in ORM message only</p></td>
<td><p>DIAGNOSTIC SERVICE SECTION ID</p>
<p><em>Note</em>: this field is populated only if one modality is associated with the CPT.</p></td>
<td>RAD MODALITY DEFINED TERMS (#73.1)</td>
<td>MODALITY ABBREVIATION (#.01)</td>
</tr>
<tr class="odd">
<td>OBR-25</td>
<td><p>STATUS</p>
<p>Field is populated with one of the values below:</p>
<p>C-Correction to results</p>
<p>R-Results stored</p>
<p>F-Final results</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td><p>OBR-27</p>
<p><strong>Note:</strong> in ORM message only</p></td>
<td>QUANTITY/TIMING</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OBR-27.4</td>
<td>START DATE/TIME</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>SCHEDULED DATE (TIME optional) (#23)</td>
</tr>
<tr class="even">
<td>OBR-27.6</td>
<td>PRIORITY</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>REQUEST URGENCY (#6)</td>
</tr>
<tr class="odd">
<td>OBR-29</td>
<td>PARENT</td>
<td>EXAMINATIONS SUBFILE (#70.03)</td>
<td><p>MEMBER OF SET (#25)</p>
<p><strong>Note:</strong> ORC-8 &amp; OBR-29 share the same value.</p></td>
</tr>
<tr class="even">
<td><p>OBR-30</p>
<p><strong>Note:</strong> in ORM message only</p></td>
<td>TRANSPORTATION MODE</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>(#19) MODE OF TRANSPORT</td>
</tr>
<tr class="odd">
<td>OBR-31</td>
<td>REASON FOR STUDY</td>
<td>RAD/NUC MED ORDERS (#75.1)</td>
<td>REASON FOR STUDY (#1.1)</td>
</tr>
<tr class="even">
<td>OBR-32</td>
<td>PRINCIPAL RESULT INTERPRETER</td>
<td>EXAMINATIONS EXAMS subfile (70.03)</td>
<td><p>PRIMARY INTERPRETING STAFF (#15)</p>
<p><strong>Note:</strong> Integration Agreement 3065 breaks the REQUESTING PHYSICIAN name into the HL7 name component.</p></td>
</tr>
<tr class="odd">
<td>OBR-32.1</td>
<td>NAME</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBR-33</td>
<td>ASSISTANT RESULT INTERPRETER</td>
<td>EXAMINATIONS EXAMS subfile (70.03)</td>
<td><p>PRIMARY INTERPRETING RESIDENT (#12)</p>
<p>PRIMARY INTERPRETING STAFF (#15)</p>
<p><strong>Note:</strong> The first resident is the Primary Resident; subsequent residents associated with the report are Secondary Residents. All ASSISTANT RESULT INTERPRETER members classified as ‘staff’ will be deemed as secondary staff in the VistA Rad/Nuc Med application.</p>
<p>Also: Integration Agreement 3065 breaks the REQUESTING PHYSICIAN name into the HL7 name component.</p></td>
</tr>
<tr class="odd">
<td>OBR-33.1</td>
<td>NAME</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBR-35</td>
<td>TRANSCRIPTIONIST</td>
<td>RAD/NUC MED REPORTS (#74)</td>
<td><p>(#11) TRANSCRIPTIONIST</p>
<p><strong>Note:</strong> Integration Agreement 3065 breaks the REQUESTING PHYSICIAN name into the HL7 name component.</p></td>
</tr>
<tr class="odd">
<td>OBR-35.1</td>
<td>NAME</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## ZDS Segments ORM and ORU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of ZDS segment field elements in ORM and ORU messages, refer to ZDS Segment Fields in ORM on page [55](#_Ref232824764) and ORU on page [65](#zds-segment-1).

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>ZDS Segment<br />
$$ZDS^MAGDRAHL</th>
<th>ZDS Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ZDS-1</td>
<td>STUDY INSTANCE UID</td>
<td>DICOM UID ROOT (#2006.15) and INSTITUTION (#4)</td>
<td>This component is populated with the ISO Object Identifier (OID) value that VistA assigned to the study, 2 of the components are the UID ROOT (#1) field of the DICOM UID ROOT file (#2006.15) and a pointer to the Institution File (#4).</td>
</tr>
</tbody>
</table>

> **NOTE:** Function \$\$ZDS^MAGDRAHL is covered by Integration Agreement 5022.

## OBX (ORU) Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of OBX segment field elements in ORU messages, refer to OBX Segment Fields in ORU Messages on page [75](#_Fields_Used_in_6).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 19%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>OBX Segment</th>
<th>OBX Field Name</th>
<th>VistA File</th>
<th>VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OBX-2</td>
<td>VALUE TYPE</td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td>OBX-3</td>
<td>OBSERVATION ID</td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="odd">
<td>OBX-3.1</td>
<td><p>IDENTIFIER</p>
<p>Field is populated with one of the values below:</p>
<p>P</p>
<p>I</p>
<p>M</p>
<p>D</p>
<p>TCM</p>
<p>C4</p>
<p>R</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td>OBX-3.2</td>
<td><p>TEXT</p>
<p>Field is populated with one of the values below:</p>
<p>PROCEDURE</p>
<p>IMPRESSION</p>
<p>MODIFIERS</p>
<p>DIAGNOSTIC CODE</p>
<p>TECH COMMENT</p>
<p>CPT MODIFIERS</p>
<p>REPORT</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="odd">
<td>OBX-3.3</td>
<td><p>NAME OF CODING SYSTEM</p>
<p>Field is populated with a fixed value of L</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4">OBX-5</td>
<td><p>OBSERVATION VALUE</p>
<p>Field is populated with one of the values below, which map to the VistA files/fields at right:</p>
<p>PROCEDURE</p>
<p>IMPRESSION TEXT</p>
<p>PROCEDURE MODIFIERS</p>
<p>PRIMARY DIAGNOSTIC CODE</p></td>
<td><p>RAD/NUC MED<br />
PATIENT (#70)</p>
<p>RAD/NUC MED<br />
REPORTS (#74)</p>
<p>RAD/NUC MED PATIENT (#70)</p>
<p>RAD/NUC MED PATIENT (#70)</p></td>
<td><p>PROCEDURE (70.03;2)</p>
<p>IMPRESSION TEXT (74; 300)</p>
<p>PROCEDURE MODIFIERS (70.03;125)</p>
<p>PRIMARY DIAGNOSTIC CODE (70.03;13)</p></td>
</tr>
<tr class="odd">
<td>TECHNOLOGIST COMMENT</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>TECHNOLOGIST COMMENT (70.03;4)</td>
</tr>
<tr class="even">
<td>CPT MODIFIERS</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>CPT MODIFIERS (70.03;135)</td>
</tr>
<tr class="odd">
<td>REPORT TEXT</td>
<td>RAD/NUC MED REPORTS (#74)</td>
<td>REPORT TEXT (74; 200)</td>
</tr>
<tr class="even">
<td>OBX-11</td>
<td><p>OBSERVATION RESULT STATUS</p>
<p>Field is populated with one of the values below:</p>
<p>F for final results</p>
<p>C for record correction (amended)</p>
<p>R for results entered</p></td>
<td>Field not mapped to a VistA File</td>
<td></td>
</tr>
</tbody>
</table>

## OBX (ORM) Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For descriptions of OBX segment field elements in ORM messages, refer to OBX Segment Fields in ORM messages on page [56](#obx-segment-fields-in-orm-and-oru).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 19%" />
<col style="width: 38%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th>OBX Segment</th>
<th>OBX Field Name</th>
<th>VistA File</th>
<th colspan="2">VistA Field(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OBX-2</td>
<td>VALUE TYPE</td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>OBX-3</td>
<td>OBSERVATION ID</td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>OBX-3.1</td>
<td><p>IDENTIFIER</p>
<p>Field is populated with one of the values below:</p>
<p>P</p>
<p>M</p>
<p>H</p>
<p>TCM</p>
<p>A</p>
<p>C4</p></td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>OBX-3.2</td>
<td><p>TEXT</p>
<p>Field is populated with one of the values below:</p>
<p>PROCEDURE</p>
<p>MODIFIERS</p>
<p>CLINICAL HISTORY</p>
<p>TECH COMMENT</p>
<p>ALLERGIES</p>
<p>CPT MODIFIERS</p></td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>OBX-3.3</td>
<td><p>NAME OF CODING SYSTEM</p>
<p>Field is populated with a fixed value of L</p></td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td rowspan="7">OBX-5</td>
<td><p>OBSERVATION VALUE</p>
<p>Field is populated with one of the values below, which map to the VistA files/fields at right:</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PROCEDURE</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>PROCEDURE (70.03;2)</td>
<td></td>
</tr>
<tr class="even">
<td>PROCEDURE MODIFIERS</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>PROCEDURE MODIFIERS (70.03;125)</td>
<td></td>
</tr>
<tr class="odd">
<td>CLINICAL HISTORY FOR EXAM</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>CLINICAL HISTORY FOR EXAM (70.03;400)</td>
<td></td>
</tr>
<tr class="even">
<td>TECHNOLOGIST COMMENT</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>TECHNOLOGIST COMMENT (70.03;4)</td>
<td></td>
</tr>
<tr class="odd">
<td>ALLERGIES</td>
<td>PATIENT ALLERGIES (#120.8)</td>
<td>ALLERGIES DBIA #10099</td>
<td></td>
</tr>
<tr class="even">
<td>CPT MODIFIERS</td>
<td>RAD/NUC MED PATIENT (#70)</td>
<td>CPT MODIFIERS (70.03;135)</td>
<td></td>
</tr>
<tr class="odd">
<td>OBX-11</td>
<td><p>OBSERVATION RESULT STATUS</p>
<p>Field is populated with a fixed value of O</p></td>
<td>Field not mapped to a VistA File</td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

[^1]:  June 2008 Updated the business rule for the VistA Rad/Nuc Med application when building an HL7 message for a segment that exceeds 245 characters in length.

[^2]: This segment is defined in IHE Rad-TF Transaction 4 (Procedure Scheduled).

[^3]: The length and data type of this field are variable, depending on *OBX-2-Value Type*.

[^4]:  Patch RA\*5\*107 January 2012: Updated the description of MSH-4-Sending Facility; for ORMs and ORUs Seq 2 and 3: Usage is XNot required and Cardinality is 0..0.

[^5]: June 2008 Updated the business rule for the VistA Rad/Nuc Med application when building an HL7 message for a segment that exceeds 245 characters in length.