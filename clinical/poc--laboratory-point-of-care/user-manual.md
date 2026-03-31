---
consolidated_title: "laboratory: poc interface installation and user guide"
app_code: POC
doc_type: user-manual
master_source: "Laboratory: POC Interface Installation and User Guide (LR*5.2*548)"
master_pub_date: JUNE 2005
consolidated_from: 2 versions
prior_versions:
  - "Laboratory:  POC Interface Installation and User Guide"
---

<!-- image -->

**LABORATORY**

**POINT OF CARE (POC) INTERFACE**

**INSTALLATION AND USER GUIDE**

**PATCH LR*5.2*548**

**Version 2.0**

**JUNE 2005**

**REVISION**

**JUNE 2021**

**Department of Veterans Affairs**

**VistA Health Systems Design &amp; Development**

## Revision

| Date     |   Revision | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Author                        |
|----------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| 06/08/21 |        2   | LR*5.2*548:  - Added LEDI HL7 text, **The LEDI HL7 field is a pointer to the LAB INSTRUMENT CODE file (#64.061). The Whole Blood entry there has an HL7 ABBR of BLD, which is what the vendor needs to know.  This is the specimen code shown on the Print POC Test Code Mapping report.** - Added Print POC Test example **Note** - Added the **Prior to Setup** section - Added the **TROUBLESHOOTING** section - Added the **WHAT THE POC VENDOR NEEDS TO KNOW** section - Updated the Before POC Setup bullet 2, **It is preferred to use separate tests for POC testing. A test used for non-POC testing should not also be used for POC testing.** - Updated the Implementation Setup Instructions Note, **Use only one configuration for each POC vendor server** - Updated LA7POCn with, **The port assigned is the port the POC vendor uses to listen for ACK messages** - Updated the LA7POCnA with, **The port assigned is the port the POC vendor uses to listen for ADT messages** - Updated the note for LA7POCn and LA7POCnA, **Both LA7POCn and LA7POCnA will have the same TCP/IP ADDRESS assigned.  They must have different TCP/IP PORT numbers assigned. The port values should be provided by the POC vendor.** - Updated LOAD/WORK List, **Only ONE Profile is allowed for each LOAD/WORK LIST.** - Updated ORDERABLE TEST, **Each test in any one LA7POCn configuration should have a unique NATIONAL VA LAB CODE.** - Updated the Print POC Test Code Mapping to include, **The ORDER NLT CODE and HL7 SPECIMEN type are found in the LOAD/WORK LIST section of the report.  The RESULT NLT CODE is found in the AUTO INSTRUMENT section of the report.  This report should be given to the POC vendor to assist in mapping the vendor’s tests to the correct ORDER NLT CODE (sent in OBR-4), RESULT NLT CODE (sent in OBX-3) and HL7 SPECIMEN type (sent in OBR-15).** - Updated the Print POC Test example to include, **tells if ADT is used** - Updated the Print POC Test example to include, **Order Test Codes using Load/Work** - Updated the Print POC Test example to include, **Result Test Codes using Auto Instrument** - Update RESULT TEST, **Each test in any one LA7POCn configuration should have a unique RESULT NLT CODE.** - Updated specimen code, **This HL7 specimen code must be sent in the OBR-15 segment of the HL7 message.** - Updated SECOND of Step 1 with, **An ORDERABLE test can be either an atomic test or a panel test. These tests must have a TYPE of BOTH in the LABORATORY TEST file (#60).** - Updated THIRD of Step 1 with, **Add only atomic tests that store results to the AUTO INSTRUMENT.** - Updated Step 5 of OIT Staff, **The division of the ordering location is used as the accessioning division, therefore, each POC ordering location division should be assigned to the LRLAB,POC proxy user in the NEW PERSON file (#200), i.e., a DIVISION assignments is required for each facility division that performs POC testing.** - Updated the Use of the Software Note, **The software provided by the POC vendor must comply with the specifications defined in the Lab POC HL7 specifications document:** - Added the AUTO INSTRUMENT **NOTE** - Updated the specimen source example, **In the TOPOGRAPHY FIELD file (#61), BLOOD has a LEDI HL7 CODE of Whole Blood** - Update the Example of specimen source - Update the LA7 POC SETUP option, **The report should be given to the POC vendor to use for mapping of ORDER NLT codes, RESULT NLT codes and specimen HL7 codes.** - Update LA7 MESSAGE PARAMETER, **It is recommended to always enable the ERROR ON MESSAGE result condition and define a mail group to receive the alert. The LIM and ATC should be members of this mail group.** - Update LA7 POC SETUP option **NOTE** warning - Updated **Laboratory Information Manager** - Added **LIM** in the laboratory information manager paragraph - Added LOAD/WORK LIST NOTE - Added **must be** in the laboratory information manager paragraph - Added Ordering Location sub bullet, **Check for clinic appointment at same time as specimen** - Added Ordering Location sub bullet **Or check clinic appointment before specimen date/time on same date.** - Added Ordering Location sub bullet **If unable to find an appointment before the specimen date/time, then look for first appointment after specimen date/time** **.** - Added LA7 POC SETUP **NOTE** - Updated instrument not sending to VistA, **POC instrument has test normal values that are fixed and unchangeable** - Updated instrument not sending to VistA, **(OBX-8)** - Updated the Purpose section with, **To capture the Performing Lab information, the station # of the performing site must be sent in the OBX-15 segment of the HL7 message** - Updated the Purpose section with, **The DUZ of the performing user (RESPONSIBLE OBSERVER) must be sent in the OBX-16 segment of the HL7 message.** - Updated the Purpose section with, **The identifier of the device used (Equipment Instance Identifier, EII) must be sent in the OBX-18 segment of the HL7 message.** - Added **NOTE** in the Purpose section - Added **MSH-3** , **MSH-4** , **MSH-5** , **MSH-6** within the same paragraph of Step 3 OIT Staff - Added Step 3 OIT Staff Note - Updated Title page, Revision History, Table of Contents, and Footers | Liberty ITS                   |
| 06/15/18 |        1.1 | LA*5.2*87 – Add VHIC Card Guideline                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | HPS Clinical Sustainment Team |
| 06/19/08 |        1   | Section changed: Implementation Setup Instructions change: Reference to HOSPITAL LOCATION file (#44), DIVISION field (#3.5) to INSTITUTION field (#3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SQA                           |

## Preface

The Veterans Health Information Systems and Architecture (VistA) Laboratory Point of Care (POC) Interface Patch LR*5.2*290 and LA*5.2*67 Installation and User Guide Version 5.2 provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (OIT) staff, Automated Data Processing Application Coordinator (LIM), and Ancillary Testing Coordinator (ATC), with a straightforward means for installing and implementing the POC software application.

### Staffing Requirements:

#### OIT Staff

OIT staff is required to install the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 software application on the VistA systems. OIT staff **must** assist with the POC post implementation requirements setup, if needed. The POC post implementation requirements setup **must** be coordinated with the LIM staff and Laboratory’s LIM or ATC.

#### Laboratory Information Manager (LIM)/Ancillary Testing Coordinator (ATC)

The LIM and/or ATC are required to setup the POC post implementation requirements, if needed. POC post implementation requirements setup **must** be coordinated with the OIT staff and the Laboratory’s LIM and/or ATC.

#### Intended Users

The intended user of this software enhancement is VA Medical Center’s laboratory personnel.

### VistA Blood Bank Clearance

#### VISTA BLOOD BANK SOFTWARE VERSION 5. 2 DEVICE PRODUCT LABELING STATEMENT

#### Patch LA*5.2*67 POC Interface

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA*5.2*67 does not contain any changes to the VISTA BLOOD BANK Software as defined by VHA DIRECTIVE 99-053 titled VISTA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA*5.2*67 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LA*5.2*67 have no effect on Blood Bank software functionality, therefore RISK is none.

#### Patch LR*5.2*290 POC Interface

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR*5.2*290 does not contain any changes to the VISTA BLOOD BANK Software as defined by VHA DIRECTIVE 99-053 titled VISTA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR*5.2*290 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LR*5.2*290 have no effect on Blood Bank software functionality, therefore RISK is none.

### ## Orientation

This section addresses package-or audience-specific notations or directions (e.g., symbols used to indicate terminal dialogues or user responses).

### Installation and User Guide Screen Displays

#### Screen Captures

The computer dialogue appears in Courier font, no larger than 10 points.

**Example:** Courier font 10 points

#### User Response

User entry response appears in boldface type Courier font, no larger than 10 points.

**Example: Boldface type**

#### Return Symbol

User response to computer dialogue is followed by the **&lt;ENTER&gt;** symbol that appears in Courier font, no larger than 10 points, and bolded.

**Example: &lt;ENTER&gt;**

#### Tab Symbol

User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded.

**Example:** &lt;Tab&gt;

### Software and Documentation Retrieval Locations

**NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

VistA Point of Care (POC) Interface Patches LR*5.2*290 and LA*5.2*67 software and Installation and User Guide are available at the following Office of Information Field Offices (OIFOs) ANONYMOUS.SOFTWARE directories:

| **OI FIELD OFFICE**   | **FTP ADDRESS**   | **DIRECTORY**   |
|-----------------------|-------------------|-----------------|
|                       |                   |                 |
| REDACTED              | REDACTED          | REDACTED        |
|                       |                   |                 |
| REDACTED              | REDACTED          | REDACTED        |
|                       |                   |                 |
| REDACTED              | REDACTED          | REDACTED        |

### Software and Documentation Retrieval Format

VistA Laboratory Point of Care (POC) Interface Patches LR*5.2*290 and LA*5.2*67 software and documentation files are exported in the following retrieval formats:

| **FILE NAME**                      | **CONTENTS**                                                                                          | **RETRIEVAL FORMAT**   |
|------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------|
|                                    |                                                                                                       |                        |
| LAB_POC.KID                        | KIDS BUILD                                                                                            | ASCII                  |
|                                    |                                                                                                       |                        |
| LAB\_52\_LR290\_LA67\_POC\_IUG.doc | Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 Installation and User Guide | BINARY                 |
|                                    |                                                                                                       |                        |
| LAB\_52\_LR290\_LA67\_POC\_IUG.pdf | Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 Installation and User Guide | BINARY                 |
|                                    |                                                                                                       |                        |
| LAB_52_POC_HL7_SPEC.doc            | Laboratory HL7 Interface Specification for Point of Care (POC)                                        | BINARY                 |
|                                    |                                                                                                       |                        |
| LAB_52_POC_HL7_SPEC.pdf            | Laboratory HL7 Interface Specification for Point of Care (POC)                                        | BINARY                 |

### VistA Website Locations:

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 Installation and User Guide and is accessible at the following locations:

#### Laboratory Version 5.2 Home Page

REDACTED

#### VistA Documentation Library (VDL)

[http://www.va.gov/vdl/](http://www.va.gov/vdl/)

## Table of Contents

Revision	i

Preface	iv

Staffing Requirements:	iv

OIT Staff	iv

Laboratory Information Manager (LIM)/Ancillary Testing Coordinator (ATC)	iv

Intended Users	iv

VistA Blood Bank Clearance	v

VISTA BLOOD BANK SOFTWARE VERSION 5. 2 DEVICE PRODUCT LABELING STATEMENT	v

Patch LA*5.2*67 POC Interface	v

Patch LR*5.2*290 POC Interface	v

Orientation	vi

Installation and User Guide Screen Displays	vi

Screen Captures	vi

User Response	vi

Return Symbol	vi

Tab Symbol	vi

Software and Documentation Retrieval Locations	vii

Software and Documentation Retrieval Format	viii

VistA Website Locations:	ix

Laboratory Version 5.2 Home Page	ix

VistA Documentation Library (VDL)	ix

Table of Contents	x

Introduction	1

Overview	1

Enhancements and Modifications	3

Enhancements:	3

1. Database Repository	3

2. The Facility’s Name and Address for each Laboratory POC Test	3

3. Name of Person Performing Test for Each POC Test	3

4. Laboratory Supervisor Summary	4

5. Display the Equipment Instance Identifier (EII) with POC Result	4

6. Determine, Retrieve, Send a Patient’s Ordering Provider, and Location	4

Ordering Location	4

Ordering Provider	5

7. POC Test Normal Values and Abnormal Flags:	5

POC instrument does not send test normal values to VistA	5

POC instrument has test normal values that are fixed and unchangeable	5

POC instrument does not send test abnormal flags to VistA	5

8. Store as Comments HL7 Standard Abnormal Flags	6

9. Test Results Received that Do Not Match Location's Assigned Division	6

10. Order and Result Test Codes	6

11. CPRS Nature of Order 'AUTO'	6

12. Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] Option Ensures Scheduling in TaskMan.	6

Modifications:	7

1. Removed Prompt to Save Alert when Viewing Lab Messaging Alert	7

2. FileMan DIE call in routine LA7LOG was converted to FileMan Data Base Server (DBS) call	7

3. Routine LA7VIN5A Changed to Accept and Process ‘Canc’ Result with Status Code X	7

4. Added Performing Laboratory Information to Comments Section of the Computer Patient Record System (CPRS) Display	7

5. Routine LR7OGG Modified to Return External Values of Set of Codes to CPRS	7

Security Information	9

Security Management:	9

Security Features:	9

Mail Groups	9

Alerts	9

Remote Systems	9

Archiving\Purging Capabilities	9

Contingency Planning	9

Communications Interfaces	10

Electronic Signatures	10

Menus	10

Security Keys	10

File Security	10

References	10

Official Policies	10

Pre-Installation Information	11

Staffing Requirements:	11

OIT Staff	11

Automated Data Processing Application Coordinator (LIM)/Ancillary Testing Coordinator (ATC)	11

User Interfaces	11

Test Sites	11

POC Vendor/Interface Vendor Tested	12

Hardware Interfaces:	12

Operating System:	12

System Performance Capacity:	12

Disk Space:	12

Installation Time:	12

Users on the System:	12

Backup Routines:	12

Kernel Installation and Distribution System (KIDS):	13

Namespace:	13

Protocols:	13

VistA Software Applications Requirements:	13

VistA Health Level Seven	1.6	13

Associated VistA Patches:	14

Required Builds:	14

Database Integration Agreements (DBIAs):	14

Data Dictionary Changes	15

AUTO INSTRUMENT file (#62.4):	15

LA7 MESSAGE PARAMETER file (#62.48):	16

LOAD/WORK LIST file (#68.2)	18

LOAD/WORK LIST file (#68.2), TEST sub-file (#68.24)	19

LAB ORDER ENTRY file (#69)	20

Files with New Entries Added	21

LA7 MESSAGE PARAMETER file (#62.48) new entries	21

LA7 MESSAGE LOG BULLETINS file (#62.485) new entries	22

PROTOCOL file (#101) New Entries	26

HL7 APPLICATION PARAMETER file (#771) New Entries	28

HL LOGICAL LINK file (#870) New Entries	29

AUTO INSTRUMENT file (#62.4) New Entries	31

NEW PERSON file (#200) New Entries	32

Laboratory Menu/Options Changes	33

New Option	33

Lab Point of Care Setup [LA7 POC SETUP] option	33

Modified Options:	34

Summary list (supervisors') [LR SUP SUMMARY] option	34

Summary list (extended supervisors') [LRLISTE] option	34

Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option	34

Routine Summaries	35

LA*5.2*67	35

LR*5.2*290	36

Installation Instructions	37

Installation Time:	37

Installation Example:	39

Post Implementation Requirements	44

LIM and/or ATC:	44

POC Implementation Requirements	44

Use of the Software	46

Prior to Setup:	46

Lab Point of Care Setup [LA7 POC SETUP] option	47

Implementation Setup Instructions	49

Step 1: Laboratory’s LIM and/or ATC	49

Related Topographies need to be linked to Appropriate HL7 Specimen Source:	52

LA7 MESSAGE PARAMETER (#62.48) Configuration Process	53

It is recommended to always enable the ERROR ON MESSAGE result condition and define a mail group to receive the alert. The LIM and ATC should be members of this mail group.LOAD/WORK LIST (#68.2) Configuration Process	54

**Example: LOAD/WORK LIST (#68.2) configuration process	55**

AUTO INSTRUMENT (#62.4) Configuration Process	62

Print POC Test Code Mapping Process	64

Step 2: OIT staff	66

Step 3: OIT staff	66

Step 4: OIT Staff	67

Step 5: OIT staff	69

Modified Options	70

Summary list (supervisors') [LR SUP SUMMARY] option	70

Summary list (extended supervisors') [LRLISTE] option	72

Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option	74

TROUBLESHOOTING	76

WHAT THE POC VENDOR NEEDS TO KNOW	77

Glossary	80

## Introduction

### Overview

The VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 supports the Laboratory Health Level 7 (HL7) Point of Care (POC) interface. It utilizes existing functionality provided by Laboratory Universal Interface (UI) and Laboratory Electronic Data Interchange (LEDI) software. The software supports the transmission, processing and storing of POC TEST RESULTS in the VistA Laboratory package. The ability of POC interfaces to subscribe to VistA HL7 Admissions, Discharge, Transfer (ADT) messages for patient demographics and location information is provided as needed. Support for 5 separate POC interfaces is provided. Additional interfaces can be added locally when naming of additional interfaces are in conformance to name spacing instructions.

POC is a type of interface that downloads and stores results for a bed side analyzer/device or any instrument that performs laboratory testing at the site of care (examination, treatment, diagnosis, etc.). The accession and verification procedures are modified to accommodate POC type of data storage. POC results are not verified by the traditional laboratory methods.

**Purpose**

The first issue involves the need to identify the testing facility’s name and address for every POC test on the laboratory report. Therefore, when results are displayed via the Laboratory Interim Reports [SRO-LRRP] option or within the Computerized Patient Record System (CPRS) Graphic User Interface (GUI), they will list the performing laboratory’s name and address. Also, the system will be enhanced so the division that produces the result will be stored with the results like other “CH” (chemistry) subscript tests.

For instance, a remote Community-based outpatient clinic’s (CBOC) testing location only performs POC glucose testing. The CBOC location has a separate Clinical Laboratory Improvement Amendments (CLIA) number and is located at a different physical location than the main laboratory. The POC results are automatically entered into the patient record without a separate step of tech verification. The POC results do not indicate that the results were performed at a different physical location (CBOC), unless the laboratory has the capability of writing this into the scripted interface and stuffing the information into the comment section of the test report. The laboratory did not want to have the name of the testing staff and instrument number display as comments with the test result in Veterans Health Information System and Technology Architecture (VistA), since this would be a duplication of effort. Also, this process is cluttering and it causes difficulties for providers to review and note clinically significant comments that might be attached to the glucose results (i.e. sliding scale insulin given, patient fasting, etc.). To capture the Performing Lab information, the station # of the performing site must be sent in the OBX-15 segment of the HL7 message.

Secondly, every laboratory test result must be tagged in some manner to identify the person performing the testing on the report.  Therefore, the system will be enhanced so that the user who performs the test and the division will be stored with the results like other "CH" (chemistry) subscript tests.  For the Laboratory POC interface, when the POC vendor's system sends the POC results in the HL7 messages, VistA expects each result value to indicate the operator id (also known as DUZ, internal entry number of a user in VistA NEW PERSON file #200). The user who performed the test shall be stored with the results like other "CH" subscript tests. The DUZ of the performing user (RESPONSIBLE OBSERVER) must be sent in the OBX-16 segment of the HL7 message.

Thirdly, the Laboratory Supervisor Summary reports will have the capability to also display the name of the POC operator who generated the results.  This will eliminate the need to store this information as comments. Also, it avoids providing too much data on one report which can make it difficult for a provider to readily view any clinically significant comments.

Next, the Equipment Instance Identifier (EII) will be stored with the results. The vendor will transmit the EII with the make, model, and serial number of the POC device generating the results. This information will be available for display on the supervisor summary reports. This process will eliminate the need to record this information as comments. The identifier of the device used (Equipment Instance Identifier, EII) must be sent in the OBX-18 segment of the HL7 message.

Furthermore, many POC systems do not have the capability of determining the patient's ordering provider and/or ordering location. Additionally, POC systems do not have the capability of retrieving and sending the patient’s ordering provider and/or ordering location. Those vendors that do accept the admission/discharge/transfer (ADT) feed from VistA for patient demographics, inpatient movements and outpatient clinic appointments attempt to utilize this information. This ADT feed does not send orders.

Currently the VistA Laboratory POC interface employs the following logic when the POC system does not provide this information. If on the date of the specimen testing the patient is an inpatient, then the patient’s inpatient primary care provider/attending is used as the ordering provider and the patient inpatient location is used as the ordering location. If on the date of specimen testing the patient is not an inpatient, then the system checks for a valid outpatient appointment and uses this clinic location as the ordering location and uses the encounter provider or the patient's outpatient primary care provider as the ordering provider.

The rationale for this approach was to complete the business rules for laboratory orders. Using either the inpatient or outpatient primary care provider is to hopefully detect any patient discrepancies by the provider responsible for the patient's care. If the provider knows the patient is not diabetic and should not have glucose testing being performed then they can alert the site to a possible patient safety issue.

**NOTE:** Instructions for the setup of the POC interface are in the **Use of the Software** section of this manual.

## Enhancements and Modifications

### Enhancements:

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 is exporting the following enhancements:

#### Database Repository

Patches LA*5.2*67 and LR*5.2*290 add support for Laboratory POC interfaces. It utilizes existing functionality provided by Laboratory UI and LEDI software. It supports the transmission, processing, and storing of POC TEST RESULTS in the VistA Laboratory package. The ability of POC interfaces to subscribe to VistA HL7 ADT messages for patient demographics and location information is provided as needed. The support for a maximum of five separate POC interfaces is provided. Multiple POC instruments can be interfaces on a single vendor’s POC system. Additional interfaces can be added locally when naming of additional interfaces are in conformance to name spacing instructions.

#### The Facility’s Name and Address for each Laboratory POC Test

Every POC test result is tagged to identify the testing facility’s name and address on the report. When the POC vendor’s system sends the POC results in the HL7 messages, VistA expects each result value to indicate the division generating the result. The division that produced the result is stored with the results like other “CH” subscript tests. This division is a pointer to the site’s local INSTITUTION file (#4). When displaying these results via Laboratory Interim Reports or within the CPRS GUI, they shall list the name and address from the VistA INSTITUTION file (#4) as the performing laboratory and address. In LOAD/WORK LIST file (#68.2), the TYPE field (#03) was **modified** to add the **new code entry** (2-POINT OF CARE) to the existing set of codes. Also, the POC WKLD METHOD field (#3) was added to the TEST sub-file (#68.24) in LOAD/WORK LIST file (#68.2). To support multi-methodologies being processed via a vendor’s single POC interface the LAB ORDER ENTRY file (#69), SPECIMEN sub-file (#69.01), LAB, IMM OR WARD COLLECT field (#4) was **modified** to add the **new** “P” FOR POC code entry to the existing set of codes.

#### Name of Person Performing Test for Each POC Test

Every laboratory test result must be tagged in some manner to identify the person performing the testing on the report. For the Laboratory POC interface when the POC vendor’s system sends the POC results in the HL7 messages, VistA expects each result value to indicate the operator ID (also known as DUZ, internal entry number of user in VistA NEW PERSON file (#200). The user who performed the test shall be stored with the results like other “CH” subscript tests. If the user performing the testing is not an ‘active’ user in the VistA NEW PERSON file (#200) the results will be rejected.

#### Laboratory Supervisor Summary

The Laboratory Supervisor Summary reports is **enhanced** to have the capability to display the name of the POC operator who generated the results. This should eliminate the need to store this information as comments and avoid the situation referred to as “cluttering up” the report and making it difficult for a provider to see clinically significant comments. The information shall be printable on reports and retrievable.

#### Display the Equipment Instance Identifier (EII) with POC Result

The Laboratory application is **enhanced** to store the Equipment Instance Identifier (EII) with the results. The vendor shall transmit the EII with the make, model, and serial number of the POC device generating the results. This information is displayed on the supervisor summary reports. This should also eliminate the need to record this information as comments.

#### Determine, Retrieve, Send a Patient’s Ordering Provider, and Location

LA7 MESSAGE PARAMETER file (#62.48) is **enhanced** to determine a patient’s ordering provider and location. In the LA7 MESSAGE PARAMETER file (#62.48), INTERFACE TYPE field (#11) is modified to add two **new** codes (i.e., 20-POC and 21-POCA) entries to the existing set of codes. If sites have multiple POC interfaces, then they can designate and select which ones can receive an ADT feed from the VistA software. VistA Laboratory POC software uses a HL7 router protocol and only adds those interfaces that want the ADT feed based on interface type code 21-POCA.

The Vista Lab POC interface will employ the following logic when the POC system does not provide ordering location and/or provider information:

#### Ordering Location

- If on the date of the specimen testing the patient is an inpatient, then the patient's inpatient location is used as the ordering location.
- If on the date of specimen testing the patient is not an inpatient, then the system checks for a valid outpatient appointment and uses this clinic location as the ordering location. If multiple clinic appointments for the specific date, then the following logic is applied:
    - Check for clinic appointment at same time as specimen
    - Or check clinic appointment before specimen date/time on same date.
    - If unable to find an appointment before the specimen date/time, then look for first appointment after specimen date/time.
- If no valid ordering location can be identified, then the results will be rejected by VistA Laboratory package and an error message returned to the POC system.

#### Ordering Provider

- If on the date of specimen testing the patient is an inpatient then the patient’s primary care provider/attending is used as the ordering provider. The patient’s primary care physician is selected. If no inpatient primary care provider is specified, then the attending physician is used.
- If on the date of specimen testing the patient is an outpatient then the primary provider specified for the outpatient encounter associated with the outpatient clinic appointment. If no primary provider on the outpatient encounter then the first secondary provider.
- If the POC system provides an outpatient ordering location and no ordering provider and the location matches an outpatient clinic location then the primary provider specified for the outpatient encounter associated with the outpatient clinic appointment. If no primary provider on the outpatient encounter then the first secondary provider.
- When a valid outpatient appointment is identified, but there is no associated encounter provider, then the patient's outpatient primary care provider is used as the ordering provider.
- If no valid ordering provider can be identified then the results will be rejected by VistA Laboratory package and an error message returned to the POC system.

#### POC Test Normal Values and Abnormal Flags:

#### POC instrument does not send test normal values to VistA

The VistA application has the ability for the site to indicate that the normals from the VistA LABORATORY TEST file (#60) be stored with the results.

#### POC instrument has test normal values that are fixed and unchangeable

If the POC systems send reference range values in the OBX-7 segment of the HL7 message, those reference ranges will be used by VistA.

#### POC instrument does not send test abnormal flags to VistA

VistA accepts and report the abnormal flags transmitted by the POC system with the results (OBX-8). Since these test results are being processed and stored after being reported by the POC system and acted upon by clinical staff, it will not evaluate the results for abnormality based on current setting in VistA Laboratory for the reported test.

#### Store as Comments HL7 Standard Abnormal Flags

Store as comments HL7 Standard Abnormal Flags that do not correspond to standard abnormal flags displayed by CPRS: L- (low) /L*- (critical low) /H- (high) /H*- (critical high).

#### Test Results Received that Do Not Match Location's Assigned Division

Test Results received for locations that do not match the location’s assigned division (INSTITUTION) in either the POC HL7 Result (ORU) message or on VistA in the HOSPITAL LOCATION file (#44) will be rejected.

#### Order and Result Test Codes

VA National Laboratory Test codes shall be used to identify all orderable tests/panels and test results.

#### CPRS Nature of Order 'AUTO'

Laboratory orders created by this POC interface will have a CPRS Nature of Order ‘AUTO’ assigned.

#### Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] Option Ensures Scheduling in TaskMan.

Lab messaging will now check that Lab Messaging Nightly Cleanup [LA7TSK NIGHTY] option is scheduled in TaskMan. If not scheduled then an alert notifying members of mail group LAB MESSAGING will be generated. The alert message will read “Lab Messaging – Option LA7TASK NIGHTY is not scheduled in TaskMan.”

**NOTE:** Documentation regarding tasking can be found in the VistA Laboratory LEDI User Guide and on-line via OPTION file (#19), DESCRIPTION field (#3.5).

#### Modifications:

VistA Laboratory Point of Care (POC) Patches LA*5.2*67 and LR*5.2*290 contain the following modifications:

#### Removed Prompt to Save Alert when Viewing Lab Messaging Alert

Removed prompt to save alert when viewing lab messaging alert in routine LA7UXQA. This functionality is now part of Kernel Alert processing.

#### FileMan DIE call in routine LA7LOG was converted to FileMan Data Base Server (DBS) call

When logging lab messaging processing errors, FileMan DIE call in routine LA7LOG was converted to FileMan DBS call.

#### Routine LA7VIN5A Changed to Accept and Process ‘Canc’ Result with Status Code X

Result of ‘canc’ was not being processed if the test was configured to only accept ‘final’ type results (HL7 Table 0085 - Observation result status codes interpretation codes C, F, or U. **Modified** routine LA7VIN5A is changed to accept and process ‘canc’ result with status code X.

#### Added Performing Laboratory Information to Comments Section of the Computer Patient Record System (CPRS) Display

CPRS Lab Display of Recent Results will display performing laboratory name and address of tests in accordance with College of American Pathology (CAP) requirements. Routine LR7OGMG is **modified** to add performing laboratory information to comments section CPRS display.

#### Routine LR7OGG Modified to Return External Values of Set of Codes to CPRS

MAR-0105-20968/HD0000000071181 reported the CPRS Lab Worksheet did not display the external value of ‘set of codes’ data types in LAB DATA file (#63). Values that are ‘set of codes’ is displayed using the external value of the set of codes. Routine LR7OGG **modified** to return external values of set of codes to CPRS.

### ## Security Information

### Security Management:

According to VA Directive 6214, the existing Laboratory software meets the requirements for VA IT Security and Accreditation Program. The VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 does not constitute a major change that requires new risk assessment and re-accreditation of the Laboratory system. VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 security is maintained through menu assignments and VA FileMan protection.

### Security Features:

#### Mail Groups

LAB MESSAGING

Site specified local mail groups to receive interface related status and processing alerts.

#### Alerts

Interface provides ability for local users to be notified when:

1. POC results have been received and processed
2. POC results have been rejected.
3. Lab Messaging Nightly Cleanup [LA7TSK NIGHTY] option is not scheduled.

#### Remote Systems

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 does not transmit data to any remote system/facility database.

#### Archiving\Purging Capabilities

Purging capabilities provided by existing functionality of Lab Messaging Nightly Cleanup [LA7TSK NIGHTY] option. There are no archiving capabilities provided by this software release.

#### Contingency Planning

Each facility using the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 **must** develop a local contingency plan to be used in the event of application problems in alive environment. The facility contingency plan **must** identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

#### Communications Interfaces

POC devices upload and download to docking stations that are interfaced with POC vendor’s server located within the VA Medical Center. The POC vendor’s server interfaces with VistA using HL7 messaging via the VistA HL package which forwards these messages to the Laboratory package for application processing. HL7 messages are received on each VistA system on the standard HL7 service running on port 5000. Messages to the POC system are transmitted via a logical link LA7POCx for lab result acknowledgments and LA7POCxA for transmission of VistA ADT HL7 messages.

#### Electronic Signatures

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 does not require an electronic signature.

#### Menus

There are no menus or options of interest to Information Security Officers (ISOs) released by this software.

#### Security Keys

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 does not require any security key.

#### File Security

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 **does not** modify any existing file security schemes. VA FileMan security access Ll code is recommended if file security is deemed necessary by the VA facilities. It is strongly recommended that Kernel’s File Access security be utilized to provide file security.

#### References

The following references may be helpful when installing and implementing the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290:

- Kernel Systems Manual V. 8.0
- Kernel Toolkit V. 7.3
- VA FileMan V. 22.0
- VA MailMan V. 8.0
- VistA Health Level Seven (HL7) Site Manager &amp; Developer Manual V. 1.6*56

#### Official Policies

There are no official policies unique to the VistA Laboratory Point of Care Interface product distribution product distribution.

## Pre-Installation Information

This section provides technical information required prior to installing the VistA Laboratory Point of Care (POC) Interface Patches LR*5.2*290 and LA*5.2*67.

### Staffing Requirements:

#### OIT Staff

OIT staff is required to install the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 software application on the VistA systems. OIT staff **must** assist with the POC post implementation requirements setup, if needed. The POC post implementation requirements setup **must** to be coordinated with the LIM staff and Laboratory’s LIM or ATC.

#### Automated Data Processing Application Coordinator (LIM)/Ancillary Testing Coordinator (ATC)

The LIM and/or ATC are required to setup the POC post implementation requirements, if needed. POC post implementation requirements setup **must** to be coordinated with the OIT staff and the Laboratory’s LIM and/or ATC.

#### User Interfaces

Authorized laboratory personnel, such as the Laboratory Ancillary Testing Coordinator (ATC), will be required to monitor the Instrument Manager for POC devices.

### Test Sites

The VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 were tested by the following Veteran Affairs Medical Centers (VAMCs):

| **Test Sites**  **(At least One Integrated Site)**      | **Operating System Platform**   | **Test Site Size**   |
|---------------------------------------------------------|---------------------------------|----------------------|
| Madison VAMC                                            | Cache-VMS                       | Medium               |
| East Orange/Lyons New Jersey HCS  **(Integrated Site)** | Cache-VMS                       | Large                |
| Salt Lake City VAMC                                     | Cache-VMS                       | Large                |
| Shreveport VAMC                                         | Cache-VMS                       | Medium               |
| Upstate New York HCS  **(Integrated Site)**             | Cache-VMS                       | Large                |

### POC Vendor/Interface Vendor Tested

| Test Sites                       | POC Vendor/Interface Vendor   |
|----------------------------------|-------------------------------|
| Madison VAMC                     | Abbott/Sybase                 |
| East Orange/Lyons New Jersey HCS | Abbott/Sybase                 |
| Salt Lake City VAMC              | Abbott/Sybase                 |
| Shreveport VAMC                  | Abbott/Sybase                 |
| Upstate New York HCS             | Roche/RALS                    |

### Hardware Interfaces:

There is no special hardware interface associated with this functionality

### Operating System:

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 software runs on the standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters, and run either Cache-VMS or Cache-NT and the Open M product.

### System Performance Capacity:

There is no significant change in the performance of the system once the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 is installed. There are no memory constraints. Use of the software should not create any appreciable global growth or network transmission problems.

### Disk Space:

All participants **must** provide adequate disk space to store HL7 messages, ensure reasonable response time for message processing, and minimize system downtime.

### Installation Time:

Installation time for VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 is less than 5 minutes.

### Users on the System:

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 can be installed while Laboratory users are on the system. However, suggested time to install: Non-peak requirement hours.

### Backup Routines:

It is highly recommended that a backup of the transport global is performed before installing the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290.

### Kernel Installation and Distribution System (KIDS):

The VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 distribution is using KIDS. For further instructions on using KIDS, please refer to the Kernel Version 8.0 Systems Manual.

### Namespace:

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 namespaces are Laboratory LR and LA.

### Protocols:

POC Interface Patches LA*5.2*67 and LR*5.2*290 uses the following protocols:

- VAFC ADT-A01 SERVER
- VAFC ADT-A02 SERVER
- VAFC ADT-A03 SERVER
- VAFC ADT-A04 SERVER
- VAFC ADT-A08 SERVER
- VAFC ADT-A08-SDAM SERVER
- VAFC ADT-A08-TSP SERVER
- VAFC ADT-A11 SERVER
- VAFC ADT-A12 SERVER
- VAFC ADT-A13 SERVER
- VAFC ADT-A19 SERVER

### VistA Software Applications Requirements:

The following software applications **must** be installed:

**Software Applications	Versions**

Kernel	8.0

VA FileMan	22.0

VA MailMan	7.1

VistA Laboratory	5.2 (with all patches installed)

### VistA Health Level Seven	1.6

### Associated VistA Patches:

Prior to installing VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 the following Laboratory patches **must** be installed:

**Associated Patches:**

(v)LA*5.2*1     &lt;&lt;= must be installed BEFORE `LA*5.2*67'
(v)LA*5.2*17   &lt;&lt;= must be installed BEFORE `LA*5.2*67'
(v)LA*5.2*22   &lt;&lt;= must be installed BEFORE `LA*5.2*67'
(v)LA*5.2*27   &lt;&lt;= must be installed BEFORE `LA*5.2*67'
(v)LA*5.2*46   &lt;&lt;= must be installed BEFORE `LA*5.2*67'
(v)LA*5.2*47   &lt;&lt;= must be installed BEFORE `LA*5.2*67'

(v)LA*5.2*62   &lt;&lt;= must be installed BEFORE `LA*5.2*67'

(v)LA*5.2*64   &lt;&lt;= must be installed BEFORE `LA*5.2*67'

(v)LR*5.2*187 &lt;&lt;= must be installed BEFORE `LR*5.2*290'
(v)LR*5.2*202 &lt;&lt;= must be installed BEFORE `LR*5.2*290'
(v)LR*5.2*217 &lt;&lt;= must be installed BEFORE `LR*5.2*290'
(v)LR*5.2*230 &lt;&lt;= must be installed BEFORE `LR*5.2*290'
(v)LR*5.2*263 &lt;&lt;= must be installed BEFORE `LR*5.2*290'

(v)LR*5.2*286 &lt;&lt;= must be installed BEFORE `LR*5.2*290'

### Required Builds:

HL*1.6*117

LA*5.2*64

LR*5.2*202

LR*5.2*217

LR*5.2*263

LR*5.2*286

### Database Integration Agreements (DBIAs):

VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 DBIAs were approved as follows:

1. Use of these protocols is supported by DBIA #4418:

VAFC ADT-A01 SERVER

VAFC ADT-A02 SERVER

VAFC ADT-A03 SERVER

VAFC ADT-A04 SERVER

VAFC ADT-A08 SERVER

VAFC ADT-A08-SDAM SERVER

VAFC ADT-A08-TSP SERVER

VAFC ADT-A11 SERVER

VAFC ADT-A12 SERVER

VAFC ADT-A13 SERVER

VAFC ADT-A19 SERVER

2. Added LAB SERVICE to DBIA# 4129 and DBIA#4055 for NEW PERSON file (#200) entries.

### Data Dictionary Changes

The following files and fields were **modified** in support of VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 enhancements:

#### AUTO INSTRUMENT file (#62.4):

The AUTO INSTRUMENT file (#62.4), CHEM TESTS sub-file (#62.41), STORE REFERENCE RANGE field (#21), field description was updated to reflect it use by POC interfaces.

**Example:** STORE REFERENCE RANGE field (#21) Modification

STANDARD DATA DICTIONARY #62.41 -- CHEM TESTS SUB-FILE

MAY 25,2005@12:43:50 PAGE 1

STORED IN ^LAB(62.4,D0,3,   SITE: DALLAS ISC - LEDI ACCOUNT   UCI: VAH,VRR

DATA          NAME                  GLOBAL        DATA

ELEMENT       TITLE                 LOCATION      TYPE

----------------------------------------------------------------------------

62.41,21      STORE REFERENCE RANGE  2;10 SET

'0' FOR NO;

'1' FOR YES;

LAST EDITED:      NOV 29, 2004

HELP-PROMPT:      Store the reference range with results

DESCRIPTION:      Laboratory Electronic Data Interchange

(LEDI): Previous versions of LEDI used this

field. Current versions of LEDI do NOT use

this field. References ranges reported by

reference laboratories are always stored

with results.

Laboratory Point of Care (POC): Used to

determine if reference ranges reported by POC

system with the results should be processed

and stored with the results. Some POC systems

have references ranges that are fixed within

the POC system and may not be appropriate or

accurate on the VistA Laboratory system.

Set this field to 'YES' to use the reference

ranges reported by the POC system.

Set this field to 'NO' to disregard any

reference ranges transmitted by the POC

system and instead use the reference ranges

specified in LABORATORY TEST file (#60) for

this test/specimen.

#### LA7 MESSAGE PARAMETER file (#62.48):

The LA7 MESSAGE PARAMETER file (#62.48), INTERFACE TYPE field (#11) is **modified** to support Point of Care (POC) Interfaces and updating the field’s description. The following two **new** codes were added to the INTERFACE TYPE field (#11) existing set of codes entries:

- ‘21’ FOR POCA
- ‘30’ FOR HDR

If sites have multiple POC interfaces they can designate/select which ones can receive an ADT feed from VistA. Lab POC software uses a router protocol and only adds those interfaces that want the ADT feed based on interface type code 21-POCA.

**NOTE:** The code 30-HDR is for patch LA*5.2*68 (Lab HDR interface).

**Example:** LA7 MESSAGE PARAMETER file (#62.48) Modifications

STANDARD DATA DICTIONARY #62.48 -- LA7 MESSAGE PARAMETER FILE

STORED IN ^LAHM(62.48,  (31 ENTRIES)  SITE: DALLAS ISC - LEDI ACCOUNT UCI: VA

DATA          NAME                  GLOBAL        DATA

ELEMENT       TITLE                 LOCATION      TYPE

----------------------------------------------------------------------------

This file is used to store parameters associated with a Lab Messaging system configuration.

POINTED TO BY: MESSAGE CONFIGURATION field (#8), of the AUTO INSTRUMENT file (#62)

CONFIGURATION field (#.5) of the LA7 MESSAGE QUEUE File (#62.49)

LAB MESSAGING LINK field (#.07) of the LAB SHIPPING CONFIGURATION.

CROSS

REFERENCED BY: CONFIGURATION(B), REMOTE SYSTEM ID(C)

62.48,.01     CONFIGURATION          0;1 FREE TEXT (Required)

INPUT TRANSFORM:  K:$L(X)&gt;30!($L(X)&lt;3)!'(X'?1P.E) X

LAST EDITED:      APR 25, 1994

HELP-PROMPT:      Answer must be 3-30 characters in length.

DESCRIPTION:      This field contains the descriptive name for

all partner that the Lab system exchanges

messages with Universal Interface.

CROSS-REFERENCE:  62.48^B

1)= S ^LAHM(62.48,"B",$E(X,1,30),DA)=""

2)= K ^LAHM(62.48,"B",$E(X,1,30),DA)

**Example:** LA7 MESSAGE PARAMETER file (#62.48) Modifications *(continued)*

62.48,11      INTERFACE TYPE         0;9 SET

'1' FOR LAB UI;

'10' FOR LEDI;

'20' FOR POC;

'21' FOR POCA;

'30' FOR HDR;

'99' FOR OTHER;

LAST EDITED:      AUG 11, 2003

HELP-PROMPT:      Enter the purpose for this messaging

interface.

DESCRIPTION:      This field determines how and for what

Purpose this configuration is used. It allows

the laboratory software to generate, handle

and process messages.

LAB UI - Used to identify configurations that

are for processing laboratory automated

instrument data via a generic interface

manager.

LEDI - Designate entries involved with

Laboratory Electronic Data Interchange

(LEDI). Used to identify interfaces involved

in the generation, transmission and

processing of HL7 order (ORM)and result (ORU)

messages involving reference laboratory

testing between VistA and other VistA

systems, commercial reference laboratories,

DoD laboratories and civilian institutions.

POC - Point of Care (POC) interface. These

interfaces transmit laboratory test results

for which there is no pre-existing VistA

laboratory order. VistA creates an order as

part of result processing and storage.

POCA - Point of Care interface that

subscribes to HL7 patient demographic (ADT)

messages from VistA. Used by POC interfaces

that subscribe to patient information from

VistA to maintain the POC’s patient database.

HDR - Designate interface to the VA Health

Data Repository (HDR). (Currently reserved

for future use).

OTHER - Designate other non-laboratory

interfaces that utilize the Laboratory

package.

#### LOAD/WORK LIST file (#68.2)

LOAD/WORK LIST file (#68.2) modifications:

- TYPE field (#.03) - **modified** to add the **new** ‘2’ POINT OF CARE code to the existing set of codes entries.

- TEST sub-file (#68.24) - **modified** to add the following two **new** fields:

- **New** POC WKLD METHOD field (#3) - Designates the WKLD method suffix to be assigned to this Point of Care (POC) test results when this test is ordered. This allows multiple POC vendor systems to be interfaced to VistA via one POC interface and still assign the appropriate methodology to the test result.
- **New** POC COLLECTION SAMPLE field (#4) - Allows the site to specify the collection sample to use when ordering this test and specimen combination.

**Example:** LOAD/WORK LIST file (#68.2) Modifications

STANDARD DATA DICTIONARY #68.2 -- LOAD/WORK LIST FILE

AUG 23,2004@14:23:26  PAGE 1

STORED IN ^LRO(68.2,  (31 ENTRIES)  SITE: DALLAS ISC - LEDI ACCOUNT  UCI: VAH,VRR (VERSION 5.2)

DATA          NAME                  GLOBAL        DATA

ELEMENT       TITLE                 LOCATION      TYPE

----------------------------------------------------------------------------

68.2,.03      TYPE                   0;3 SET (Required)

'0' FOR SEQUENCE/BATCH;

'1' FOR TRAY,CUP;

'2' FOR POINT OF CARE;

LAST EDITED:      OCT 04, 2001

DESCRIPTION:      Determines if this list is a sequence/batch,

tray, cup or Point of Care (POC) type of

load/work list.

TECHNICAL DESCR:  Point of Care (POC) is a type of interface

That downloads and stores results for a bed

Side analyzer (device) i.e. Glucometers.

Accession and verification procedures are

modified to accommodate POC type of data

storage. POC results are not verified in the

classical laboratory method.

#### LOAD/WORK LIST file (#68.2), TEST sub-file (#68.24)

The LOAD/WORK LIST file (#68.2), TEST sub-file (#68.24) was **modified** to add the **new** POC WKLD METHOD field (#3) and POC COLLECTION SAMPLE field (#4). These two **new** fields support the multi-methodologies being processed via a vendor’s single POC interface.

**Example:** TEST sub-file (#68.24) Modifications

STANDARD DATA DICTIONARY #68.24 -- TEST SUB-FILE

AUG 23,2004@14:22:30  PAGE 1

STORED IN ^LRO(68.2,D0,10,D1,1, SITE: DALLAS ISC - LEDI ACCOUNT UCI:VAH,VRR

DATA          NAME                  GLOBAL        DATA

ELEMENT       TITLE                 LOCATION      TYPE

---------------------------------------------------------------------------

68.24,3       POC WKLD METHOD        0;4 POINTER TO WKLD SUFFIX CODES FILE (#64.2)

LAST EDITED:      AUG 17, 2004

HELP-PROMPT:      Enter the workload method suffix to be

associated with this POC test.

DESCRIPTION:      Designates the WKLD method suffix to be

assigned to this Point of Care (POC) test

results when this test is ordered. This

allows multiple POC vendor systems to be

interfaced to VistA via one POC interface

and still assign the appropriate methodology

to the test result.

FILES POINTED TO                      FIELDS

WKLD SUFFIX CODES (#64.2)         POC WKLD METHOD (#3)

68.24,4   POC COLLECTION SAMPLE  0;5 POINTER TO COLLECTION SAMPLE FILE (#62)

LAST EDITED:      MAY 25, 2005

HELP-PROMPT:      Enter the related collection sample for this

test/specimen

DESCRIPTION:      Allows the site to specify the collection

sample to use when ordering this test and

specimen combination.

FILES POINTED TO                      FIELDS

COLLECTION SAMPLE (#62)           POC COLLECTION SAMPLE (#4)

#### LAB ORDER ENTRY file (#69)

LAB ORDER ENTRY file (#69), SPECIMEN # sub-file (#69.01), LAB, IMM OR WARD COLLECT field (#4) was **modified** to add the **new** 'P' FOR POC code entry to the existing set of codes.

**Example:** SPECIMEN # sub-file (#69.01), LAB, IMM OR WARD COLLECT field (#4) Modification

STANDARD DATA DICTIONARY #69.01 -- SPECIMEN # SUB-FILE

AUG 23,2004@14:24:36  PAGE 1

STORED IN ^LRO(69,D0,1,   SITE: DALLAS ISC - LEDI ACCOUNT   UCI: VAH,VRR

DATA          NAME                  GLOBAL        DATA

ELEMENT       TITLE                 LOCATION      TYPE

----------------------------------------------------------------------------

69.01,4       LAB,IMM OR WARD COLLECT 0;4 SET

'LC' FOR LAB COLLECT;

'WC' FOR WARD COLLECT;

'SP' FOR SEND PATIENT;

'I' FOR IMM. LAB COLLECT;

'P' FOR POC;

LAST EDITED:      JUN 01, 2001

DESCRIPTION:      This designates how the sample or specimen is

to reach the lab

### Files with New Entries Added

The VistA Laboratory POC patches LA*5.2*67 and LR*5.2*290 are exporting **new** entries to the following files:

#### LA7 MESSAGE PARAMETER file (#62.48) new entries

Laboratory Point of Care software application uses the following entries to identify POC type interfaces to VistA.  It supports up to five separate vendor’s Point of Care systems. Each POC system (interface) can have multiple POC instruments interfaced via the vendor’s POC system.

**Example:** LA7 MESSAGE PARAMETER file (#62.48) contains the following **new** entries:

CONFIGURATION: LA7POC1                  PROTOCOL: HEALTH LEVEL SEVEN

STATUS: INACTIVE                      LOG ERRORS: ON

GRACE PERIOD FOR MESSAGES: 5          INTERFACE TYPE: POC

PROCESS IN: D QUE^LA7VIN

CONFIGURATION: LA7POC2                  PROTOCOL: HEALTH LEVEL SEVEN

STATUS: INACTIVE                      LOG ERRORS: ON

GRACE PERIOD FOR MESSAGES: 5          INTERFACE TYPE: POC

PROCESS IN: D QUE^LA7VIN

CONFIGURATION: LA7POC3                  PROTOCOL: HEALTH LEVEL SEVEN

STATUS: INACTIVE                      LOG ERRORS: ON

GRACE PERIOD FOR MESSAGES: 5          INTERFACE TYPE: POC

PROCESS IN: D QUE^LA7VIN

CONFIGURATION: LA7POC4                  PROTOCOL: HEALTH LEVEL SEVEN

STATUS: INACTIVE                      LOG ERRORS: ON

GRACE PERIOD FOR MESSAGES: 5          INTERFACE TYPE: POC

PROCESS IN: D QUE^LA7VIN

CONFIGURATION: LA7POC5                  PROTOCOL: HEALTH LEVEL SEVEN

STATUS: INACTIVE                      LOG ERRORS: ON

GRACE PERIOD FOR MESSAGES: 5          INTERFACE TYPE: POC

PROCESS IN: D QUE^LA7VIN

#### LA7 MESSAGE LOG BULLETINS file (#62.485) new entries

Laboratory Point of Care software application uses the following error code numbers to build the text of the error message. This file has been changed to add twenty **new** codes.

CODE: 101

Indicates the patient identifier (SSN) transmitted by the POC system does not resolve to an entry in the VistA PATIENT file (#2).

TEXT: Msg #|1|, SSN |2| not found in PATIENT file (#2).

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(LASSN)

CODE: 102

Indicates the patient internal entry number (DFN)in the PATIENT file (#2) does not match the patient’s DFN identified when the POC message was received.

TEXT: Msg #|1|, DFN do not match.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 103

Indicates the patient’s internal entry number (LRDFN) in LAB DATA file (#63) does not match the patient’s LRDFN identified when the POC message was received.

TEXT: Msg #|1|, LRDFN do not match.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 104

Indicates the specimen collection date/time received from the POC system was not a valid date/time.

TEXT: Msg #|1|, Invalid specimen collection date |2|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(LRCDT)

CODE: 105

Indicates the entry to be processed in the LAH global does not exist.

TEXT: Msg #|1|, Bad LAH(|2| entry # |3| for DFN |4|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=LRLL,

LA7TXT(3)=LAIEN,LA7TXT(4)=DFN

CODE: 106

Indicates the SSN determined for the patient when the POC results were received does not match the patient’s SSN currently specified in the PATIENT file (#2).

TEXT: Msg #|1|, LAH(|2| entry # |3| SSN: |4| doesn't match DPT(|5| SSN: |6|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(LRLL),LA7TXT(3)=

$G(LAIEN),LA7TXT(4)=$G(LRSSN),LA7TXT(5)=$G(DFN),LA7TXT(6)=$G(SSN(2))

**Example:** LA7 MESSAGE LOG BULLETINS file (#62.485) new entries *(continued)*

CODE: 107

Indicates the ordering location sent by the POC system does not exist in the VistA HOSPITAL LOCATION file (#44) or if no ordering location sent the POC interface was unable to determine the patient’s current location based on in/outpatient status at time of patient testing.

TEXT: Msg #|1|, No valid ordering location found for order.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 108

Indicates the patient internal entry number (DFN) in PATIENT file (#2) does not exist at time POC results were processed.

TEXT: Msg #|1|, Bad DPT(|2| entry for LAH(|3| - |4|

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(DFN),LA7TXT(3)=

$G(LRLL),LA7TXT(4)=$G(LAIEN)

CODE: 109

Indicates the Laboratory software was unable to determine an accession area assigned for the test to be processed.

TEXT: Msg #|1|, No accession area for test: |2|

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$P($G(LRTS),"^")

CODE: 110

Indicates the ordering provider sent by the POC system does not exist in the VistA NEW PERSON file (#200) or if no ordering provider sent, the POC interface was unable to determine the patient’s current provider based on in/outpatient status at date/time of patient testing.

TEXT: Msg #|1|, No valid provider found for order.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 111

Indicates the user transmitted by the POC system as the person performing the POC testing does not exist in the VistA NEW PERSON file (#200) or is not a current user on VistA.

TEXT: Msg #|1|, No valid responsible observer found for test result.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 112

Indicates the ordering division does not match the division associated with the ordering location in the VistA HOSPITAL LOCATION file (#44).

TEXT: Msg #|1|, Unable to determine if patient was in division |2| [|3|].

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$P($G(LRX),"^"),

LA7TXT(3)=$P($G(LRX),"^",2)

**Example:** LA7 MESSAGE LOG BULLETINS file (#62.485) **new** entries *(continued)*

CODE: 113

Indicates the ordered test from the POC system did not resolve to an orderable test in the VistA Laboratory file (#60).

TEXT: Msg #|1|, Message contained no identifiable orderable test in OBR segment.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 114

Indicates the specimen types transmitted by the POC system did not resolve to a VistA TOPOGRAPHY file (#61) entry or match a topography the site has associated with the ordered test.

TEXT: Msg #|1|, Unable to identify specimen (topography).

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 115

Indicates the site has not mapped a collection sample to the topography received from the POC system.

TEXT: Msg #|1|, Unable to identify collection sample.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 116

Indicates the POC test results cannot be associated with a VistA laboratory test.

TEXT: Msg #|1|, No test identified to store results.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249)

CODE: 117

Indicates the VistA laboratory test associated with the test results is not configured for the accession area and/or load list used to process POC results.

TEXT: Msg #|1|, Dataname |2| not in accession |3| or Load/work list |4| test profile.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(LRSB),LA7TXT(3)=

$G(LRUID),LA7TXT(4)=$P($G(LRLL(0)),"^")

CODE: 118

Indicates the orderable test is not specified on the load list used for POC tests.

TEXT: Msg #|1|, Test |2| not in LOAD/WORK LIST |3| profile.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$$GET1^DIQ(60,+

$G(LRTST),.01)\_" ["\_$G(LRTST)\_"]",LA7TXT(3)=$P($G(LRLL(0)),"^")

**Example:** LA7 MESSAGE LOG BULLETINS file (#62.485) **new** entries *(continued)*

CODE: 119

Indicates the ordering provider id (DUZ - internal entry number in VistA NEW PERSON) does not exist in the NEW PERSON file (#200).

TEXT: Msg #|1|, Invalid ordering provider id |2|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$P($G(LRX),"^")

CODE: 120

Indicates the orderable test for the POC results is not configured for the specimen type transmitted by the POC system for the specified POC load list.

TEXT: Msg #|1|, Order NLT code |2| not linked to a test in LOAD/WORK LIST |3|

profile |4| for HL7 specimen type |5|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=$G(LA76249),LA7TXT(2)=$G(LRY),LA7TXT(3)=$P

($G(LRLL(0)),"^"),LA7TXT(4)=$P($G(LRPROF(0)),"^"),LA7TXT(5)=$S($G(LROSPEC)'="":LROSPEC,1:"UNKNOWN")

#### PROTOCOL file (#101) New Entries

PROTOCOL file (#101) contains the following five **new** protocols that support HL7 messaging for Point of Care (POC) interfaces.

**Example:** PROTOCOL file (#101) five **new** protocol entries.

NAME: LA7POC ADT RTR                    TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7POC1

RESPONSE MESSAGE TYPE: ACK            SENDING FACILITY REQUIRED?: YES

RECEIVING FACILITY REQUIRED?: YES     SECURITY REQUIRED?: NO

ROUTING LOGIC: D RTRA^LA7POC Q

NAME: LA7POC ORU-R01 SUBS 2.4           TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7LAB

EVENT TYPE: R01                       RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: D ORU^LA7VHL      SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO      SECURITY REQUIRED?: NO

NAME: LA7POC1 ADT SUBS                  TYPE: subscriber

CREATOR: LABCREATOR, ONE              RECEIVING APPLICATION: LA7POC1

LOGICAL LINK: LA7POC1A                RESPONSE MESSAGE TYPE: ACK

SENDING FACILITY REQUIRED?: YES       RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

NAME: LA7POC1 ORU-R01 EVENT 2.4         TYPE: event driver

CREATOR: LABCREATOR, ONE             SENDING APPLICATION: LA7POC1

TRANSACTION MESSAGE TYPE: ORU         EVENT TYPE: R01

MESSAGE STRUCTURE: ORU\_R01            ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: AL              VERSION ID: 2.4

SUBSCRIBERS: LA7POC ORU-R01 SUBS 2.4

NAME: LA7POC2 ADT SUBS                  TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7POC2

LOGICAL LINK: LA7POC2A                RESPONSE MESSAGE TYPE: ACK

SENDING FACILITY REQUIRED?: YES       RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

**Example:** PROTOCOL file (#101) **new** protocol entries *(continued)*

NAME: LA7POC2 ORU-R01 EVENT 2.4         TYPE: event driver

CREATOR: LABCREATOR, ONE             SENDING APPLICATION: LA7POC2

TRANSACTION MESSAGE TYPE: ORU         EVENT TYPE: R01

MESSAGE STRUCTURE: ORU\_R01            ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: AL              VERSION ID: 2.4

SUBSCRIBERS: LA7POC ORU-R01 SUBS 2.4

NAME: LA7POC3 ADT SUBS                  TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7POC4

LOGICAL LINK: LA7POC3A                RESPONSE MESSAGE TYPE: ACK

SENDING FACILITY REQUIRED?: YES       RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

NAME: LA7POC3 ORU-R01 EVENT 2.4         TYPE: event driver

CREATOR: LABCREATOR, ONE             SENDING APPLICATION: LA7POC3

TRANSACTION MESSAGE TYPE: ORU         EVENT TYPE: R01

MESSAGE STRUCTURE: ORU\_R01            ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: AL              VERSION ID: 2.4

SUBSCRIBERS: LA7POC ORU-R01 SUBS 2.4

NAME: LA7POC4 ADT SUBS                  TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7POC4

LOGICAL LINK: LA7POC4A                RESPONSE MESSAGE TYPE: ACK

SENDING FACILITY REQUIRED?: YES       RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

NAME: LA7POC4 ORU-R01 EVENT 2.4         TYPE: event driver

CREATOR: LABCREATOR, ONE             SENDING APPLICATION: LA7POC4

TRANSACTION MESSAGE TYPE: ORU         EVENT TYPE: R01

MESSAGE STRUCTURE: ORU\_R01            ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: AL              VERSION ID: 2.4

SUBSCRIBERS: LA7POC ORU-R01 SUBS 2.4

NAME: LA7POC5 ADT SUBS                  TYPE: subscriber

CREATOR: LABCREATOR, ONE             RECEIVING APPLICATION: LA7POC5

LOGICAL LINK: LA7POC5A                RESPONSE MESSAGE TYPE: ACK

SENDING FACILITY REQUIRED?: YES       RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

NAME: LA7POC5 ORU-R01 EVENT 2.4         TYPE: event driver

CREATOR: LABCREATOR, ONE             SENDING APPLICATION: LA7POC5

TRANSACTION MESSAGE TYPE: ORU         EVENT TYPE: R01

MESSAGE STRUCTURE: ORU\_R01            ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: AL              VERSION ID: 2.4

SUBSCRIBERS: LA7POC ORU-R01 SUBS 2.4

#### HL7 APPLICATION PARAMETER file (#771) New Entries

HL7 APPLICATION PARAMETER file (#771) contains the following 6 **new** entries:

Laboratory Point of Care software application uses the following entries to identify POC type interfaces to VistA.  It supports up to five separate vendor’s Point of Care systems (LA7POCx). LA7POCx (where x is a number from 1-5) is the name to be assigned to a vendor’s POC system as the HL7 sending application. LA7LAB is the receiving application name for the VistA Laboratory package that will receive and process these POC HL7 messages.

**Example:** HL7 APPLICATION PARAMETER file (#771) **new** entries

NAME: LA7LAB                            ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

NAME: LA7POC1                           ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

NAME: LA7POC2                           ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

NAME: LA7POC3                           ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

NAME: LA7POC4                           ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

NAME: LA7POC5                           ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ^~\&amp;         HL7 FIELD SEPARATOR: |

#### HL LOGICAL LINK file (#870) New Entries

HL LOGICAL LINK file (#870) contains the following 12 **new** entries:

Laboratory Point of Care software application uses the following entries to identify POC related logical link interfaces on Vista. It supports up to five separate vendor’s Point of Care systems (LA7POCx). The logical links named LA7POCx (where x is a number from 1-5) are used by the HL7 package and Laboratory to transmit HL7 application acknowledgements from Laboratory to the POC system. The logical links named LA7POCxA are used by the HL7 package to send VistA ADT HL7 messages containing patient demographics when the POC system has subscribed to the VistA ADT information.

**Example:** HL LOGICAL LINK file (#870) contains the following **new** entries:

NODE: LA7POC1                           LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC1A                          LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC2                           LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC2A                          LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC3                           LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

**Example:** HL LOGICAL LINK file (#870) new entries ( *continued* )

NODE: LA7POC3A                          LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC4                           LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC4A                          LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC5                           LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

NODE: LA7POC5A                          LLP TYPE: TCP

AUTOSTART: Disabled                   QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5           READ TIMEOUT: 3

ACK TIMEOUT: 60                       UNI-DIRECTIONAL WAIT: 3

EXCEED RE-TRANSMIT ACTION: ignore     TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO                        RETENTION: 120

#### AUTO INSTRUMENT file (#62.4) New Entries

Laboratory Point of Care software application uses the following entries to identify POC type interfaces to VistA.  It supports up to five separate vendor’s Point of Care systems. Each POC system (interface) can have multiple POC instruments interfaced via the vendor’s POC system. These entries are used to link the POC test result with the corresponding VistA Laboratory test. They function in a manner like automated laboratory instruments that are interfaced to VistA Laboratory.

**Example:** AUTO INSTRUMENT file (#62.4) five **new** entries

NAME: LA7POC1

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7POC1

NAME: LA7POC2

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7POC2

NAME: LA7POC3

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7POC3

NAME: LA7POC4

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7POC4

NAME: LA7POC5

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7POC5

#### NEW PERSON file (#200) New Entries

NEW PERSON file (#200) contains two **new** ‘non-human’ entries (i.e., LRLAB,HL and LRLAB,POC). The **new** ‘non-human’ user LRLAB,HL is used by Laboratory when processing HL7 messages to insure a consistent Kernel environment with respect to the system-wide DUZ variable array. NOIS DAN-0105-41616 **/** HD0000000071211 reported undefined DUZ(“AG”) variable when processing Lab HL7 messages. The **new** ‘non-human’ user ‘LRLAB,POC’is used by this interface create the order and accession associated with the Point of Care TEST RESULTS. Local site personnel should assign DIVISIONS to this **new** ‘non-human’ user LRLAB,POC that corresponds to the accessions areas used for POC. These two **new** entries have the approval of VA VistA Data Base Administrator.

**Example:** NEW PERSON file (#200) new ‘Non-Human’ LRLAB,HL entry

NAME: LRLAB,HL             NAME COMPONENTS: 200

SIGNATURE BLOCK PRINTED NAME: HL LRLAB

**Example:** NEW PERSON file (#200) new non-human ‘LRLAB,POC’ entry

NAME: LRLAB,POC            NAME COMPONENTS: 200

SIGNATURE BLOCK PRINTED NAME: POC LRLAB

### Laboratory Menu/Options Changes

The following new and modified options are used in support of the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 **new** functionality:

#### New Option

#### Lab Point of Care Setup [LA7 POC SETUP] option

This **new** Lab Point of Care Setup [LA7 POC SETUP] option is located on the Lab Universal Interface Menu [LA7 MAIN MENU]. It is used to configure and setup the Lab HL7 Point of Care interface. It provides the means for configuring the various files related to receiving and processing POC test results in the VistA Laboratory package. The user can configure the three main files relating to this interface and print a report of the interface configuration which should be used in configuring the POC system.

**NOTE:** ***The LIM should use only the options on this menu to set up the POC interface. FileMan editing of the AUTO INSTRUMENT file and of the LOAD.WORK LIST file should not be used when setting up the interface*** **.**

1. LA7 MESSAGE PARAMETER (#62.48) process configure entries (LA7POC*) in the LA7 MESSAGE PARAMETER file (#62.48) relating to interface status, alerts and mail groups to notify when alerts are triggered.

2 LOAD/WORK LIST (#68.2) process configure related load list entries in the LOAD/WORK LIST file (#68.2) to determine ORDERABLE TESTS, specimen and collection samples and related accession areas involved in ORDERABLE TEST process.

3. AUTO INSTRUMENT (#62.4) process configure corresponding entries (LA7POC*) in AUTO INSTRUMENT file (#62.4) which determine how TEST RESULTS are processed.

4. Print POC Test Code Mapping prints a report which displays the ORDERABLE TESTS and RESULT TESTS configured for an interface, what order and result codes are specified, the specimens and collection types and accession areas that are used by the interface. It also warns if supporting information is missing for these or other laboratory related files which the interface is dependent on to successfully process a POC test result.

#### Modified Options:

#### Summary list (supervisors') [LR SUP SUMMARY] option

The Summary list (supervisors') [LR SUP SUMMARY] option is **modified** to display the performing user, performing laboratory, LOINC code, and Equipment Instance Identifier (EII) for each test result when long or extended format chosen. The EII contains the vendor’s make/model/serial number of the instrument/equipment that produced the test result. When the vendor’s instrument interface transmits this information, it is stored with the test results.

#### Summary list (extended supervisors') [LRLISTE] option

The Summary list (extended supervisors') [LRLISTE] option is **modified** to display the performing user, performing laboratory, LOINC code, and Equipment Instance Identifier (EII) for each test result when long or extended format chosen. The EII contains the vendor’s make/model/serial number of the instrument/equipment that produced the test result. When the vendor’s instrument interface transmits this information, it is stored with the test results.

#### Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option

Lab messaging will now check that Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option is scheduled in TaskMan. If not scheduled then an alert notifying members of mail group LAB MESSAGING will be generated. The alert message will read "Lab Messaging- Option LA7TASK NIGHTY is not scheduled in TaskMan". **Note:** Documentation regarding tasking can be found in the VistA Laboratory LEDI User Guide and on-line via the DESCRIPTION field of the OPTION file (#19) for this entry.

### Routine Summaries

The following routines are included in the VistA Laboratory Point of Care (POC) Interface Patch LR*5.2*290 and LA*5.2*67:

#### LA*5.2*67

The following routines are included in this patch. The second line of each of these routines now looks like:

&lt;tab&gt; ;;5.2;AUTOMATED LAB INSTRUMENTS;&lt;patchlist&gt;;Sep 27, 1994

Checksum       Checksum

Routine Name     Before Patch   After Patch    Patch List

------------     ------------   -----------    ------------

LA67             N/A            8196499        **67** (Deleted by KIDS)

LA7LOG           9009311        8393092        **17,27,67**

LA7PCFG          N/A            16069384       **67**

LA7POC           N/A            3454800        **67**

LA7UXQA          7260762        5623537        **27,67**

LA7VHL           5811383        6113752        **27,46,62,64,67**

LA7VIN           1398763        3056962        **46,67**

LA7VIN1A         13987419       14019173       **64,67**

LA7VIN4          12162627       12188308       **46,64,67**

LA7VIN5A         8695039        9628469        **46,64,67**

LAGEN            8715369        8613602        **1,17,22,27,47,46,64,67**

**List of preceding patches: 64**

**Sites should use CHECK^XTSUMBLD to verify checksums.**

#### LR*5.2*290

The following routines are included in this patch.  The second line of each of these routines now looks like:

&lt;tab&gt; ;;5.2;LAB SERVICE;&lt;patchlist&gt;;Sep 27, 1994

Checksum       Checksum

Routine Name     Before Patch   After Patch    Patch List

------------     ------------   -----------    ------------

LR290            N/A            4831439        **290** (Deleted by KIDS)

LR7OGG           11097271       10933227       **187,290**

LR7OGMG          3973477        5478031        **187,230,286,290**

LRDIQ            10128715       2599216        **86,153,263,290**

LRGP2            6353513        6108916        **153,221,263,290**

LRORDST          14420120       12502665       **100,107,121,153,202,290**

LROW2            8572259        8727104        **121,290**

LRUER            12281075       11948802       **201,290**

LRVRPOC          N/A            10290202       **290**

LRVRPOCU         N/A            8876916        **290**

LRWLST           17313871       14863929       **46,65,100,121,153,202,

290**

LRX              13923654       15315863       **65,153,201,217,290**

**List of preceding patches: 202, 217, 263, 286**

**Sites should use CHECK^XTSUMBLD to verify checksums.**

## Installation Instructions

The VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 are using the Kernel Installation and Distribution System (KIDS).

**NOTE:** For further instructions on using KIDS, please refer to the Kernel V. 8.0 Systems Manual.

**NOTE:** Kernel patches **must** be current on the target system to avoid problems loading and/or installing this patch.

**NOTE:** Patch installation needs to be coordinated with the Laboratory Information Manager (LIM/LIM).

#### Installation Time:

The install time for this patch is less than 5 minutes. This patch can be installed when Laboratory users are on the system.

Suggested time to install: Non-peak requirement hours.

1. Obtain the file LAB\_POC.KID.

2. If any of the above routines are mapped, disable mapping for them.

3. On the 'Kernel Installation &amp; Distribution System' Menu (KIDS), select the ‘Installation’ menu.

4. Use Load a Distribution using LAB\_POC.KID when prompted to enter a Host File name. You may need to prefix a directory name.

If given the option to run any Environment Check Routine(s), answer “YES.”

5. From this menu, you may then elect to use the following options (when prompted for the INSTALL NAME, enter LA*5.2*67):

a. Print Transport Global

b. Backup a Transport Global

c. Compare Transport Global to Current System

d. Verify Checksums in Transport Global

Use the ‘Verify Checksum in Transport Global’ [XPD PRINT CHECKSUM] option and verify that all routines have the correct checksums.

6. Use the ‘Install Package(s)’ [XPD INSTALL BUILD] option under the ‘Installation’ [XPD INSTALLATION MENU] menu and select the package ‘LA*5.2*67’.

When prompted      ‘Want KIDS to INHIBIT LOGONs during the install? YES//’ choose ‘NO’. When prompted      ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//’ choose ‘NO’

7. On a mapped system, rebuild your map set.

**NOTE:** Routine LA67 will be deleted after successful patch installation.

### Installation Example:

Select Installation Option: **6&lt;ENTER&gt;** Install Package(s)

Select INSTALL NAME: **LA*5.2*67&lt;ENTER&gt;** Loaded from Distribution 4/27/05@11:30:47

=&gt; LA*5.2*67/LR*5.2*290 on 13 April 2005; Created on Apr 13, 2005

This Distribution was loaded on Apr 27, 2005@11:30:47 with header of

LA*5.2*67/LR*5.2*290 on 13 April 2005; Created on Apr 13, 2005@17:26:59

It consisted of the following Install(s):

LA*5.2*67     LR*5.2*290

Checking Install for Package LA*5.2*67

Will first run the Environment Check Routine, LA67

--- Environment Check is Ok ---

Install Questions for LA*5.2*67

Incoming Files:

62.4      AUTO INSTRUMENT  (Partial Definition)

> **NOTE:** You already have the 'AUTO INSTRUMENT' File.

62.48     LA7 MESSAGE PARAMETER  (including data)

> **NOTE:** You already have the 'LA7 MESSAGE PARAMETER' File.

I will MERGE your data with mine.

62.485    LA7 MESSAGE LOG BULLETINS  (including data)

> **NOTE:** You already have the 'LA7 MESSAGE LOG BULLETINS' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package LR*5.2*290

Will first run the Environment Check Routine, LR290

Sending install started alert to mail group G.LMI

--- Environment Check is Ok ---

Install Questions for LR*5.2*290

Incoming Files:

68.2      LOAD/WORK LIST  (Partial Definition)

> **NOTE:** You already have the 'LOAD/WORK LIST' File.

69        LAB ORDER ENTRY  (Partial Definition)

> **NOTE:** You already have the 'LAB ORDER ENTRY' File.

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// **NO&lt;ENTER&gt;**

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// **&lt;ENTER&gt;** TELNET VIRTUAL

Install Started for LA*5.2*67 :

Aug 13, 2003@13:32:50

Build Distribution Date: Aug 13, 2003

Installing Routines:......

Aug 13, 2003@13:32:50

Running Pre-Install Routine: PRE^LA67.

Sending install started alert to mail group G.LMI

*** Pre install started ***

--- Creating stub entries to file #62.4 and #62.48 ---

*** Pre install completed ***

Installing Data Dictionaries: ..

Aug 13, 2003@13:32:50

Installing Data:

Aug 13, 2003@13:32:50

Installing PACKAGE COMPONENTS:

Installing HL LOGICAL LINK...........

Installing HL7 APPLICATION PARAMETER.......

Installing PROTOCOL.

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Located in the LA7 (LAB MESSAGING) namespace..

Aug 13, 2003@13:32:52

Running Post-Install Routine: POST^LA67.

*** Post install started ***

--- Completing LA7POC* entries in file #62.4 ---

*** Updating file #62.4 completed ***

*** Updating facility name for LA7POC* entries in file #771 ***

*** Updating facility name completed ***

*** Adding non-human user 'LRLAB,POC' to NEW PERSON file ***

*** Adding 'LRLAB,POC' Successful ***

*** Post install completed ***

Sending install completion alert to mail group G.LMI

Updating Routine file......

Updating KIDS files.......

LA*5.2*67 Installed.

Aug 13, 2003@13:32:53

Install Message sent #3532

Install Started for LR*5.2*290 :

Aug 13, 2003@13:32:53

Build Distribution Date: Aug 13, 2003

Installing Routines:

Aug 13, 2003@13:32:53

Running Pre-Install Routine: PRE^LR290.

*** Pre install started ***

*** No action required ***

*** Pre install completed ***

Installing Data Dictionaries: ...

Aug 13, 2003@13:32:54

Running Post-Install Routine: POST^LR290.

*** Post install started ***

*** No action required ***

*** Post install completed ***

Sending install completion alert to mail group G.LMI

Updating Routine file......

Updating KIDS files.......

LR*5.2*290 Installed.

Aug 13, 2003@13:32:55

Install Message sent #nnnnn

ENVIRONMENT CHECK : LA67                       DELETE ENV ROUTINE: Yes

PRE-INIT ROUTINE : PRE^LA67              DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE : POST^LA67            DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN :

UP    SEND  DATA                USER

DATE  SEC.  COMES  SITE   RSLV  OVER

FILE #      NAME                         DD    CODE  W/FILE DATA   PTS   RIDE

-----------------------------------------------------------------------------

62.4        AUTO INSTRUMENT              YES   NO    NO                  NO

Partial DD: subDD: 62.41      fld: 21

DATA SCREEN:

62.48       LA7 MESSAGE PARAMETER        YES   NO    YES    MERG   NO    NO

DATA SCREEN: I $E($P(^LAHM(62.48,Y,0),U),1,6)="LA7POC",$E($P(^LAHM(62.48,Y,0),

U),7)&lt;6

62.485      LA7 MESSAGE LOG BULLETINS    NO    NO    YES    OVER   NO    NO

DATA SCREEN: I Y&gt;100,Y&lt;121

ROUTINE:

LA7LOG                                         SEND TO SITE

LA7PCFG                                        SEND TO SITE

LA7POC                                         SEND TO SITE

LA7UXQA                                        SEND TO SITE

LA7VHL                                         SEND TO SITE

LA7VIN                                         SEND TO SITE

LA7VIN1A                                       SEND TO SITE

LA7VIN4                                        SEND TO SITE

LA7VIN5A                                       SEND TO SITE

LAGEN                                          SEND TO SITE

OPTION:

LA7 MAIN MENU                                  USE AS LINK FOR MENU ITEMS

LA7 POC SETUP                                  SEND TO SITE

PROTOCOL:

LA7POC ADT RTR                                 SEND TO SITE

LA7POC ORU-R01 SUBS 2.4                        SEND TO SITE

LA7POC1 ADT SUBS                               SEND TO SITE

LA7POC1 ORU-R01 EVENT 2.4                      SEND TO SITE

LA7POC2 ADT SUBS                               SEND TO SITE

LA7POC2 ORU-R01 EVENT 2.4                      SEND TO SITE

LA7POC3 ADT SUBS                               SEND TO SITE

LA7POC3 ORU-R01 EVENT 2.4                      SEND TO SITE

LA7POC4 ADT SUBS                               SEND TO SITE

LA7POC4 ORU-R01 EVENT 2.4                      SEND TO SITE

LA7POC5 ADT SUBS                               SEND TO SITE

LA7POC5 ORU-R01 EVENT 2.4                      SEND TO SITE

HL7 APPLICATION PARAMETER:

LA7LAB                                         SEND TO SITE

LA7POC1                                        SEND TO SITE

LA7POC2                                        SEND TO SITE

LA7POC3                                        SEND TO SITE

LA7POC4                                        SEND TO SITE

LA7POC5                                        SEND TO SITE

HL LOGICAL LINK:

LA7POC1                                        SEND TO SITE

LA7POC1A                                       SEND TO SITE

LA7POC2                                        SEND TO SITE

LA7POC2A                                       SEND TO SITE

LA7POC3                                        SEND TO SITE

LA7POC3A                                       SEND TO SITE

LA7POC4                                        SEND TO SITE

LA7POC4A                                       SEND TO SITE

LA7POC5                                        SEND TO SITE

LA7POC5A                                       SEND TO SITE

REQUIRED BUILDS:                                  ACTION:

LA*5.2*64                                      Don't install, leave global

HL*1.6*117                                     Don't install, leave global

## Post Implementation Requirements

This section of the guide provides the OIT staff and the Laboratory’s LIM and/or ATC post implementation requirement setup instructions to successfully configure the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 software application.

### LIM and/or ATC:

**NOTE:** If Point of Care (POC) interfaces are ‘NOT’ being used by the VA facility, ‘NO’ further actions are required.

#### POC Implementation Requirements

If these Point of Care (POC) interfaces are to be implemented by the VA facility the Laboratory’s LIM and/or ATC and OIT staff **must** coordinate the implementation requirements setup located in the following POC User Guide, ‘Use of the Software’ section of this guide:

**NOTE:**

Laboratory’s LIM and/or ATC should perform POC implementation setup **Step 1**

OIT staff should perform POC implementation setup **Steps 2, 3, 4, and 5** .

POINT OF CARE (POC) INTERFACE

USER GUIDE SECTION

## Use of the Software

This section of the VistA Laboratory Point of Care (POC) Interface Patches LA*5.2*67 and LR*5.2*290 User Guide provides the LIM and/or ATC and OIT staff task-oriented approaches with step-by-step instructions and examples for implementing the POC setup:

**NOTE:** These Point of Care (POC) interfaces are designed to operate with a variety of commercial POC Commercial off the Shelf (COTS) systems. Vendors implement different features and capabilities within their systems. Therefore, features and capabilities within the VistA Lab POC interface may or may not be utilized. Example is the ability of a POC system to subscribe to VistA patient ADT information. If a vendor’s system is unable to accept patient ADT information from VistA, then this feature cannot be activated on VistA. The software provided by the POC vendor must comply with the specifications defined in the Lab POC HL7 specifications document:

[https://www.va.gov/vdl/documents/Clinical/Lab-Point\_of\_Care/lab\_52\_poc\_hl7\_spec.pdf](https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/lab_52_poc_hl7_spec.pdf)

**VHIC CARD GUIDELINE:**

Some Point of Care vendors do not send the complete patient identifier when a VHIC card is scanned.  Trailing spaces on the barcode may be deleted by the vendor before sending the transaction to VistA, or the vendor may not be able to send all 15 to 18 characters which are required by VistA to identify the patient.

Other vendors are dependent on the Social Security number of the patient which must be sent to an ADT HL7 feed to determine patient identity.  ADT HL7 interfaces cannot accept a VHIC card identifier.

**VHIC cards may not be used when the ADT feed is in use by the site for a specific POC configuration.**

### Prior to Setup:

1. Decide whether the ADT feed will be used.  VistA can send ADT information to the vendor’s server, which includes data about admissions and clinic appointments, and providers associated with these events.  This information can be used to assign the ordering location and ordering provider information when the vendor sends the HL7 result message to VistA.
2. Decide which LA7POCn configuration will be used.  Use one LA7POCn configuration for each vendor’s server.
3. Create separate tests used only for POC testing.  The orderable test must have a TYPE of BOTH in the LABORATORY TEST file (#60).
4. Create a separate accession area specific to POC testing.
5. Use the options on the Lab Point of Care Setup menu to do all setup. **DO NOT USE FILEMAN!!!!** :
    - 5.1. Setup the LA7 MESSAGE PARAMETER.  Be sure to enable the ERROR ON MESSAGE alert condition and assign a MAIL GROUP of which the ATC and LIM are members.  You may need to have a local mail group created for this purpose.
    - 5.2. Create a LOAD/WORK LIST to use for POC testing.  Use only one PROFILE.  Assign only ORDERABLE tests.
    - 5.3. Configure the AUTO INSTRUMENT.  Assign atomic tests, i.e., the tests that store the results.
    - 5.4. Use the option Print POC Test Code Mapping to review the setup of your Load/Work list and Auto Instrument.  Use this document to notify the vendor of:
        - 5.4.1. Order NLT codes (from the Load/Work list)
        - 5.4.2. HL7 specimen code (from the Load/Work list)
        - 5.4.3. Result NLT codes (from the Auto Instrument)
6. DO NOT use FileMan to setup the LOAD/WORK LIST or AUTO INSTRUMENT!!!
7. Get the IP address and port(s) of the vendor’s server.  The LA7POCn HL7 link will be set up with the IP address of the vendor’s server and the port that the vendor listens on for acknowledgement messages from VistA.  If using the ADT feed, LA7POCnA will be set up with the IP address of the vendor’s server and the port that the vendor listens on  for ADT messages from VistA.
8. Work with local/region OIT to set up the LA7POCn HL7 link.

### Lab Point of Care Setup [LA7 POC SETUP] option

This **new** Lab Point of Care Setup [LA7 POC SETUP] option is located on the Lab Universal Interface Menu [LA7 MAIN MENU]. This **new** option is used to configure and setup the Lab HL7 Point of Care interface. It provides the means for configuring the various files related to receiving and processing POC TEST RESULTS in the VistA Laboratory package.

**NOTE:** Do not use FileMan to configure the LOAD/WORK LIST and AUTO INSTRUMET file entries.

The LIM and/or ATC and OIT staff can configure the three main files relating to the POC interface and print a report of the POC interface configuration (which should be used in configuring the POC system) via the **new** ‘Lab Point of Care Setup [LA7 POC SETUP]’ option. The report should be given to the POC vendor to use for mapping of ORDER NLT codes, RESULT NLT codes and specimen HL7 codes.

**Example:** The **new** ‘Lab Point of Care Setup [LA7 POC SETUP]’ option

Select OPTION NAME: **LA7 MAIN MENU&lt;ENTER&gt;** Lab Universal Interface Menu

1      Print Source of Specimen Table

2      Print Lab Universal Interface Log

Display Lab Universal Interface Message

Download to Universal Interface

Start/Stop Auto Download Background Job

PCS    Lab Point of Care Setup

FIC    Lab Messaging File Integrity Checker

PIC    Print Lab Messaging Integrity Check Report

Select *SITE SYNONYM* Lab Universal Interface Menu Option: **PCS&lt;ENTER&gt;** Lab Point of Care Setup

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

### Implementation Setup Instructions

**NOTE:** The VistA Laboratory POC interface has the capability to support up to 5 POC COTS systems. Each POC system can have multiple POC instruments interfaced to the POC system. To configure a point of care (POC) interface identify an interface to setup - LA7POCn where ‘n’ is a number from 1 to 5. If you have only one POC vendor system then select ‘LA7POC1’. If you have multiple POC vendor systems they will be referenced as LAPOC1, LA7POC2, LA7POC3, LA7POC4, and LA7POC5. **Use only one configuration for each POC vendor server.**

#### Step 1: Laboratory’s LIM and/or ATC

Use the **new** Lab Point of Care Setup [LA7 POC SETUP] option located on the Lab Universal Interface Menu [ **LA7 MAIN MENU]** to configure the following three Laboratory files:

**FIRST** - is the LA7 MESSAGE PARAMETER file (#62.48). This file configures how the HL7 messages are processed.

**SECOND** - is the LOAD/WORK LIST file (#68.2). This file configures the load list used to process results and determine which tests is ORDERABLE TEST which will handle TEST RESULTS. An ORDERABLE test can be either an atomic test or a panel test. These tests must have a TYPE of BOTH in the LABORATORY TEST file (#60).

**THIRD -** is the AUTO INSTRUMENT file (#62.4). This file configures how specific TEST RESULTS are linked to respective VistA Laboratory test. Add only atomic tests that store results to the AUTO INSTRUMENT.

**Example:** Select the **new** Lab Point of Care Setup [LA7 POC SETUP] option

Select OPTION NAME: **LA7 MAIN MENU&lt;ENTER&gt;** Lab Universal Interface Menu

1      Print Source of Specimen Table

2      Print Lab Universal Interface Log

Display Lab Universal Interface Message

Download to Universal Interface

Start/Stop Auto Download Background Job

PCS    Lab Point of Care Setup

FIC    Lab Messaging File Integrity Checker

PIC    Print Lab Messaging Integrity Check Report

Select Lab Universal Interface Menu Option: **PCS&lt;ENTER&gt;** Lab Point of Care Setup

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Before beginning the POC setup, the following files need to be configured within the general VistA Laboratory package.

- The appropriate ACCESSION file (#68) entry for the accession area(s) used to accession POC type testing. Entries setup for existing POC testing can be utilized.

- The appropriate LABORATORY TEST file (#60) entries utilized for POC testing need to be created and setup. Besides normal lab test configuration, this POC interface makes extensive use of the LABORATORY TEST file (#60), NATIONAL VA LAB CODE (aka Order NLT Code), and RESULT NLT CODE field (#64.1). **It is preferred to use separate tests for POC testing. A test used for non-POC testing should not also be used for POC testing.**

**Example:** POC Interface Required Fields

**FILE NAME                                                             FIELD NAMES/NUMBERS**

LABORATORY TEST file (#60)                              NATIONAL VA LAB CODE

(aka Order NLTCode) field (#64)

RESULT NLT CODE field (#64.1)

For the ORDERABLE TEST ensure that the NATIONAL VA LAB CODE (aka Order NLT Code) field (#64) is configured. **Each test in any one LA7POCn configuration should have a unique NATIONAL VA LAB CODE.**

For the RESULT TEST ensure that the RESULT NLT CODE field (#64.1) is configured. **Each test in any one LA7POCn configuration should have a unique RESULT NLT CODE.**

If the test is used for both ORDERABLE TEST and RESULT TEST then configure both NATIONAL VA LAB CODE (aka Order NLT Code) field (#64) and RESULT NLT CODE field (#64.1) or the test.

- Appropriate LOAD/WORK LIST file (#68.2) entry used for POC testing. Entries setup for existing POC testing should NOT be utilized if being used for an existing POC interface. This entry can be setup during step 2 of the POC setup. **Only ONE Profile is allowed for each LOAD/WORK LIST.**

#### Related Topographies need to be linked to Appropriate HL7 Specimen Source:

- For TOPOGRAPHY FIELD file (#61), LEDI HL7 field (#.09)

- For COLLECTION SAMPLE file (#62), DEFAULT SPECIMEN field (#2)

If the site does not or chooses not to have a default specimen linked to the collection sample used by this interface then linking can be accomplished in the POC setup when setting up the test on the load/work list. Specify the collection sample to use via the LOAD/WORK LIST file (#68.2), POC COLLECTION SAMPLE field (#4).

If sending admission/discharge/transfer and other patient demographics (ADT) messages from VistA PIMS package to POC system then answer ‘YES’ to prompt to “Does this POC interface want to receive VistA ADT messages?” when configuring LA7POCn configuration - LA7 MESSAGE PARAMETER (#62.48) function 1 located on the **new** Lab Point of Care Setup [LA7 POC SETUP] option.

For each ORDERABLE TEST/PANEL the POC system will transmit specify the ORDERABLE TEST in the VistA Laboratory test in the LOAD/WORK LIST file (#68.2), PROFILE field (#50) multiple of the associated Load/Work List. The order NLT code associated with this test will be the order code the POC system should use to identify the orderable test. Also specify the appropriate specimen type for each test which should have the same HL7 specimen source code as transmitted by the POC system. The accession area used for the ORDERABLE TEST and TEST RESULTS will be determined by the ordering division (INSTITUTION). If the HL7 ORU result message indicates the ordering division (or if missing) the division assigned to the location in the HOSPITAL LOCATION file (#44), INSTITUTION field (#3) will be used to select the appropriate accession area for the ORDERABLE TEST for the corresponding entry in the site’s LABORATORY TEST file (#60). If no division can be determined then the division and accession area specified for the associated load list profile will be used.

If more than one ORDERABLE TEST is contained in the HL7 ORU message then the division/accession area selected for the first test processed will be used for all ORDERABLE TESTS processed for a given POC specimen.

For each test result the POC system will transmit, specify in AUTO INSTRUMENT file (#62.4) field (#8 ) appropriate specimen for each test. This specimen type (topography) should have the same HL7 specimen source code as transmitted by the POC system. This HL7 specimen code must be sent in the OBR-15 segment of the HL7 message.

**NOTE:** It is recommended that the Print POC Test Code Mapping report be reviewed to determine any discrepancies and used as a tool to configure the POC system with the required NLT order/result codes and expected specimen types.

#### LA7 MESSAGE PARAMETER (#62.48) Configuration Process

**FIRST** - LA7 MESSAGE PARAMETER (#62.48) process configure one of the five **new** LA7POC entries relating to the POC interface. Configure various parameters such as status, alerts, purging, and mail groups that will be notified when alerts are triggered.

**Example:** LA7 MESSAGE PARAMETER (#62.48) configuration process

Select which file to setup: **1&lt;ENTER&gt;** LA7 MESSAGE PARAMETER (#62.48)

Select LA7 MESSAGE PARAMETER CONFIGURATION: **?&lt;ENTER&gt;**

Answer with LA7 MESSAGE PARAMETER CONFIGURATION, or REMOTE SYSTEM ID

Choose from:

LA7POC1

LA7POC2

LA7POC3

LA7POC4

LA7POC5

Select LA7 MESSAGE PARAMETER CONFIGURATION: **LA7POC1&lt;ENTER&gt;**

Does this POC interface want to receive VistA ADT messages? NO// **?&lt;ENTER&gt;**

Enter either 'Y' or 'N'.

Does this POC interface want to receive VistA ADT messages? NO// **YES&lt;ENTER&gt;**

Remember to add the LA7POC ADT RTR event protocol to the appropriate

ADT event protocols as specified in the Lab POC User Guide

STATUS: INACTIVE// **?&lt;ENTER&gt;**

Enter "Active" to allow this configuration to send and receive messages.

Choose from:

1        ACTIVE

0        INACTIVE

STATUS: INACTIVE// **1&lt;ENTER&gt;**

**Example:** LA7 MESSAGE PARAMETER (#62.48) configuration process *(continued)*

GRACE PERIOD FOR MESSAGES: // **?&lt;ENTER&gt;**

Type a Number between 1 and 31, 0 Decimal Digits.

GRACE PERIOD FOR MESSAGES: // **7&lt;ENTER&gt;**

Select ALERT CONDITION: ?&lt;ENTER&gt;

You may enter a new ALERT CONDITION, if you wish

Enter "1" to receive alerts for new results, a "2" to receive alerts

for errors during processing. and "3" when orders are received.

Error on message alert may only be selected if Field #4, LOG

ERRORS,is set to "ON".

Choose from:

1    NEW RESULTS

2    ERROR ON MESSAGE

3    ORDERS RECEIVED

Select ALERT CONDITION: **2&lt;ENTER&gt;** (2   ERROR ON MESSAGE)

Are you adding 'ERROR ON MESSAGE' as a new ALERT CONDITION (the 1ST for this LA7 MESSAGE PARAMETER)? No// **Y&lt;ENTER&gt;** (Yes)

MAIL GROUP: **LAB MESSAGING&lt;ENTER&gt;**

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

#### #### It is recommended to always enable the ERROR ON MESSAGE result condition and define a mail group to receive the alert. The LIM and ATC should be members of this mail group.LOAD/WORK LIST (#68.2) Configuration Process

**SECOND** - LOAD/WORK LIST file (#68.2) process configures related load list entry to determine orderable tests, specimen and collection samples, and related accession areas involved in the test ordering process.

**NOTE:**

- **Make sure all ORDERABLE tests have a TYPE of BOTH in the LABORATORY TEST file (#60) and each has a unique entry in the NATIONAL VA LAB CODE field.** This is necessary in order to see all of the prompts when using the option. For each TEST, you must identify the TEST, the SPECIMEN, the POC WKLD METHOD, and the POC COLLECITON SAMPLE.
- **Only add ORDERABLE tests to the LOAD/WORK LIST.  Do not add atomic tests that are part of a panel, which cannot be ordered separately.**
- **Only one PROFILE per LOAD/WORK LIST is allowed.**

#### Example: LOAD/WORK LIST (#68.2) configuration process

Select which file to setup: **2&lt;ENTER&gt;** LOAD/WORK LIST (#68.2)

Select LOAD/WORK LIST NAME: **?&lt;ENTER&gt;**

Answer with LOAD/WORK LIST NAME

Do you want the entire 25-Entry LOAD/WORK LIST List? **Y&lt;ENTER&gt;** (Yes)

Choose from:

AFB

ANCILLARY TESTING

ANTI-DS DNA AB

APO A

BLOOD CULTURE

BLOOD GAS

CHEM 7

CHEMISTRY

COAG

COBAS

DIFF

DRUGS

HEMATOLOGY

HEPATITIS

KODAK

MANUAL BENCH

MICROBIOLOGY

MYCOLOGY

RIA

SMAC

UA

VDRL

VITEK

WK-BB

WK-CYTOLOGY

WK-LITHIUM

You may enter a new LOAD/WORK LIST, if you wish

Answer must be 2-30 characters in length.

**Example:** LOAD/WORK LIST (#68.2) configuration process *(continued)*

Select LOAD/WORK LIST NAME: **POC&lt;ENTER&gt;**

Are you adding 'POC' as a new LOAD/WORK LIST (the 26TH)? No// **Y&lt;ENTER&gt;** (Yes)

NAME: POC// **&lt;ENTER&gt;**

WKLD METHOD: **PRECISION G &lt;ENTER&gt;** .3118     ABBOTT

MAJOR ACCESSION AREA: **?&lt;ENTER&gt;**

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire 25-Entry ACCESSION List? Y  (Yes)

Choose from:

AUTOPSY

BLOOD BANK

CHEM-20

CHEMISTRY

CLINTON CHEMISTRY

COAG

CYTOPATHOLOGY

DIF/PLT/EST/RBC/MORP

DIFFS, PLT. EST, RBC MORPHS

EM

GAS

HEMATOLOGY

MANUAL CHEM

MICROBIOLOGY

RETIC COUNT

RIA

SED RATES

SEND OUT

SENDOUT YEARLY

SEROLOGY

^

MAJOR ACCESSION AREA: **CHEMISTRY&lt;ENTER&gt;**

LAB SUBSECTION: **?&lt;ENTER&gt;**

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire 25-Entry ACCESSION List? **Y&lt;ENTER&gt;** (Yes)

Choose from:

AUTOPSY

BLOOD BANK

CHEM-20

CHEMISTRY

CLINTON CHEMISTRY

**Example:** LOAD/WORK LIST (#68.2) configuration process *(continued)*

COAG

CYTOPATHOLOGY

DIF/PLT/EST/RBC/MORP

DIFFS, PLT. EST, RBC MORPHS

EM

GAS

HEMATOLOGY

MANUAL CHEM

MICROBIOLOGY

RETIC COUNT

RIA

SED RATES

SEND OUT

SENDOUT YEARLY

SEROLOGY

STAT LAB

SURGICAL PATHOLOGY

TEST MONTHLY

TOXICOLOGY

URINALYSIS

WK-CHEMISTRY

LAB SUBSECTION:

WORK AREA: **?&lt;ENTER&gt;**

Select only accession area identified as work areas.

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire ACCESSION List? Y  (Yes)

Choose from:

CYTOPATHOLOGY

WK-CHEMISTRY

WORK AREA: **WK-CH&lt;ENTER&gt;** WK-CHEMISTRY

Select PROFILE: **?&lt;ENTER&gt;**

You may enter a new PROFILE, if you wish

ANSWER MUST BE 1-30 CHARACTERS IN LENGTH

**Example:** LOAD/WORK LIST (#68.2) configuration process *(continued)*

Select PROFILE: **POC TESTS&lt;ENTER&gt;**

Are you adding 'POC TESTS' as a new PROFILE (the 1ST for this LOAD/WORK LIST)? No// **Y&lt;ENTER&gt;** (Yes)

PROFILE ACCESSION AREA: ?&lt;ENTER&gt;

You cannot select an accession area designated Work Area.

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire ACCESSION List? **Y** (Yes)

Choose from:

AUTOPSY

BLOOD BANK

CHEM-20

CHEMISTRY

CLINTON CHEMISTRY

COAG

DIF/PLT/EST/RBC/MORP

DIFFS, PLT. EST, RBC MORPHS

EM

GAS

HEMATOLOGY

MANUAL CHEM

MICROBIOLOGY

RETIC COUNT

RIA

SED RATES

SEND OUT

SENDOUT YEARLY

SEROLOGY

STAT LAB

SURGICAL PATHOLOGY

TEST MONTHLY

TOXICOLOGY

URINALYSIS

PROFILE ACCESSION AREA: **CHEMISTRY&lt;ENTER&gt;**

ACCESSION AREA: CHEMISTRY// **&lt;ENTER&gt;**

STORE DUPLICATE COMMENTS: **? &lt;ENTER&gt;**

Should duplicate comments be stored with results.

Choose from:

0        NO

1        YES

**Example:** LOAD/WORK LIST (#68.2) configuration process *(continued)*

STORE DUPLICATE COMMENTS: **1&lt;ENTER&gt;** YES

Select TEST: **? &lt;ENTER&gt;**

You may enter a new TEST, if you wish

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME)

Select TEST: **GLUCOSE, ANCILLARY TESTING&lt;ENTER&gt;** FBS

SPECIMEN: **?&lt;ENTER&gt;**

Answer with TOPOGRAPHY FIELD NAME, or LEDI HL7, or SNOMED CODE, or

ABBREVIATION, or SYNONYM

Do you want the entire 8575-Entry TOPOGRAPHY FIELD List?

SPECIMEN: BLOOD

1   BLOOD       0X000

2   BLOOD BAND CELL       0X161

3   BLOOD BASOPHIL       0X180

4   BLOOD EOSINOPHIL       0X170

5   BLOOD ERYTHROCYTE       0X120

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **1&lt;ENTER&gt;** BLOOD     0X000

POC WKLD METHOD: **?&lt;ENTER&gt;**

Enter the workload method suffix to be associated with this POC test.

Answer with WKLD SUFFIX CODES, or NAME, or MANUFACTURER

Do you want the entire 3187-Entry WKLD SUFFIX CODES List?

POC WKLD METHOD: **ACCUCHECK&lt;ENTER&gt;** .4736     BMC

POC COLLECTION SAMPLE: **&lt;ENTER&gt;**

Select TEST: **?&lt;ENTER&gt;**

Answer with TEST:

GLUCOSE, ANCILLARY TESTING

You may enter a new TEST, if you wish

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME)

Do you want the entire 1036-Entry LABORATORY TEST List?

Select TEST: **BLOOD GASES&lt;ENTER&gt;** BLD GAS

SPECIMEN: ?

Answer with TOPOGRAPHY FIELD NAME, or LEDI HL7, or SNOMED CODE, or

ABBREVIATION, or SYNONYM

Do you want the entire 8575-Entry TOPOGRAPHY FIELD List?

SPECIMEN: **ARTERIAL BLOOD&lt;ENTER&gt;** 0X000

POC WKLD METHOD: **?&lt;ENTER&gt;**

Enter the workload method suffix to be associated with this POC test.

Answer with WKLD SUFFIX CODES, or NAME, or MANUFACTURER

**Example:** LOAD/WORK LIST (#68.2) configuration process *(continued)*

Do you want the entire 3187-Entry WKLD SUFFIX CODES List?

POC WKLD METHOD: **ISTAT&lt;ENTER&gt;**

1   ISTAT       .4456     I-STAT

2   ISTAT ALIFAX       .4751     ALIFAX DIAG

CHOOSE 1-2: **1&lt;ENTER&gt;** ISTAT     .4456     I-STAT

POC COLLECTION SAMPLE: **?&lt;ENTER&gt;**

Enter the related collection sample for this test/specimen

Answer with COLLECTION SAMPLE NAME, or TUBE TOP COLOR, or SYNONYM

Do you want the entire 50-Entry COLLECTION SAMPLE List?

POC COLLECTION SAMPLE: **ARTERIAL BLOOD&lt;ENTER&gt;** ARTERIAL BLOOD

Select TEST: **&lt;ENTER&gt;**

Select PROFILE: **&lt;ENTER&gt;**

GLUCOSE, ANCILLARY TESTING missing collection sample for specimen BLOOD

Now edit the associated division for accession area CHEMISTRY.

Select ASSOCIATED DIVISION: **?&lt;ENTER&gt;**

You may enter a new ASSOCIATED DIVISION, if you wish

Allows only divisions related to site.

Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

OFFICIAL VA NAME, or CURRENT LOCATION, or CODING SYSTEM/ID PAIR, or

NAME (CHANGED FROM), or CODING SYSTEM

Do you want the entire INSTITUTION List?

Select ASSOCIATED DIVISION: **NDBI DEVELOPMENT&lt;ENTER&gt;** DALLAS KRNTOP(NDBI) TX MC(M)  270

#### AUTO INSTRUMENT (#62.4) Configuration Process

**THIRD -** AUTO INSTRUMENT file (#62.4) configure corresponding entries in (LA7POC*). These entries are used to determine how TEST RESULTS are processed.

**NOTE:**

- **Add all orderable atomic tests, and all atomic tests included in orderable panels.**
- **The RESULT NLT CODE assigned to each test in the LABORATORY TEST file (#60) must be unique.  This code is automatically added to the field UI TEST CODE in the AUTO INSTRUMENT file.  The UI TEST CODE field should not be edited using FileMan.**

**Example:** AUTO INSTRUMENT (#62.4) configuration process

Select OPTION NAME: **LA7 POC SETUP** &lt;ENTER&gt;     Lab Point of Care Setup

Lab Point of Care Setup

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Select which file to setup: **3&lt;ENTER&gt;** AUTO INSTRUMENT (#62.4)

Select AUTO INSTRUMENT NAME: **LA7POC1&lt;ENTER&gt;**

LOAD/WORK LIST: POC// **&lt;ENTER&gt;**

MESSAGE CONFIGURATION: **LA7POC1&lt;ENTER&gt;**

METHOD: **ISTAT&lt;ENTER&gt;**

DEFAULT ACCESSION AREA: POINT OF CARE// **&lt;ENTER&gt;**

STORE REMARKS: YES// **&lt;ENTER&gt;**

Select TEST: GLUCOSE, ANCILLARY TESTING// **&lt;ENTER&gt;**

TEST: GLUCOSE, ANCILLARY TESTING// **&lt;ENTER&gt;**

PARAM 1: **&lt;ENTER&gt;**

SPECIMEN: ARTERIAL BLOOD// **&lt;ENTER&gt;**

NUMBER OF DECIMAL PLACES: **&lt;ENTER&gt;**

CONVERT RESULT TO REMARK: NO// **&lt;ENTER&gt;**

ACCEPT RESULTS FOR THIS TEST: YES// **&lt;ENTER&gt;**

REMOVE SPACES FROM RESULT: NO// **&lt;ENTER&gt;**

STORE REMARKS: YES// **&lt;ENTER&gt;**

REMARK PREFIX: For Glucose: // **&lt;ENTER&gt;**

STORE REFERENCE RANGE: YES// **&lt;ENTER&gt;**

Select TEST: **&lt;ENTER&gt;**

Select SITE NOTES DATE: **&lt;ENTER&gt;**

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Select which file to setup:

#### Print POC Test Code Mapping Process

The Print POC Test Code Mapping process prints a report which displays the orderable and result tests configured for an interface, what order and result codes are specified, the specimens and collection types and accession areas that are used by the interface. It also warns if supporting information is missing for these or other laboratory related files which the interface is dependent on to successfully process a POC test result. The ORDER NLT CODE and HL7 SPECIMEN type are found in the LOAD/WORK LIST section of the report.  The RESULT NLT CODE is found in the AUTO INSTRUMENT section of the report.  This report should be given to the POC vendor to assist in mapping the vendor’s tests to the correct ORDER NLT CODE (sent in OBR-4), RESULT NLT CODE (sent in OBX-3) and HL7 SPECIMEN type (sent in OBR-15).

**Example:** Print POC Test Code Mapping prints a report

Select OPTION NAME: **LA7 POC SETUP&lt;ENTER&gt;** Lab Point of Care Setup

Lab Point of Care Setup

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Select which file to setup: **4&lt;ENTER&gt;** Print POC Test Code Mapping

Select AUTO INSTRUMENT NAME: **LA7POC1&lt;ENTER&gt;**

DEVICE: HOME// **0;80;999999&lt;ENTER&gt;** UCX/TELNET

Point of Care Test Code Mapping                             Page: 1

for interface: LA7POC1                               Printed: May 19, 2005

===========================================================================

VistA ADT feed enabled: YES

POC Order Test Codes using Load/Work List: POC

# Lab Test                 Order NLT Code      Specimen(IEN)       HL7 Spec

Order NLT Name      Collection Sample   WKLD Code

-----------------------------------------------------------------------------

1 GLUCOSE, ANCILLARY TESTIN  82115.0000          BLOOD(70)           BLD

Glucose POC         BLOOD/BR            .4736

2 BLOOD GASES                82884.0000          ARTERIAL BLOO(8728) BLDA

Blood Gas POC       ARTERIAL BLOOD      .4456

3 GLUCOSE, ANCILLARY TESTIN  82115.0000          ARTERIAL BLOO(8728) BLDA

Glucose POC         ARTERIAL BLOOD      .4456

4 PO2                        &lt;Missing&gt;           &lt;Missing&gt;

No Mapping

Warning - test does not have NATIONAL VA LAB CODE assigned.

**Example:** Print POC Test Code Mapping prints a report *(continued)*

POC Result Test Codes using Auto Instrument: LA7POC1

# Lab Test                   Result NLT Code          Specimen(IEN)

Dataname(IEN)              Result NLT Name          HL7 Spec

----------------------------------------------------------------------------

1 GLUCOSE, ANCILLARY TESTIN  82115.0000               BLOOD(70)

GLUCOSE(2)                 Glucose POC              BLD

2 PH                         81248.0000               ARTERIAL BLOOD(8728)

PH(450)                    pH                       BLDA

3 PCO2                       82820.0000               ARTERIAL BLOOD(8728)

PCO2(451)                  PCO2 Direct Reading      BLDA

4 PO2                        82880.0000               ARTERIAL BLOOD(8728)

PO2(452)                   PO2 Direct Reading       BLDA

5 BICARBONATE (SBC)          81216.0000               ARTERIAL BLOOD(8728)

BICARBONATE(454)           Bicarbonate              BLDA

6 GLUCOSE, ANCILLARY TESTIN  82115.0000               ARTERIAL BLOOD(8728)

GLUCOSE(2)                 Glucose POC              BLDA

Enter RETURN to continue or '^' to exit:

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Select which file to setup:

#### Step 2: OIT staff

Use the HL package Link Edit [HL EDIT LOGICAL LINKS] option to configure the corresponding HL logical links:

- LA7POCn to send acknowledgment (ACK) messages to the point of care system. The port assigned is the port the POC vendor uses to listen for ACK messages.
- LA7POCnA to send ADT messages with patient demographics and appointment information if point of care system supports this functionality. The port assigned is the port the POC vendor uses to listen for ADT messages.

**NOTE:** The POC system vendor should indicate the respective ports that will be receiving these messages. OIT staff will have assigned the TCP IP address utilized by the POC system when installing the POC system on the VAMC’s LAN. Both LA7POCn and LA7POCnA will have the same TCP/IP ADDRESS assigned.  They must have different TCP/IP PORT numbers assigned. The port values should be provided by the POC vendor.

#### Step 3: OIT staff

The Point of Care (POC) system should be configured to send ORU result messages to the site’s standard HL7 listener (VAxxx) where xxx is the three-letter identifier assigned to your facility for HL7 messaging. The POC system can connect to this standard listener at domain name HL7.site\_name.MED.VA.GOV) on port 5000 when configuring this interface in a production VistA system. The point of care system will be identified as LA7POCn for the HL7 sending application (MSH-3) and VistA Laboratory will be identified as LA7LAB for the HL7 receiving application (MSH-5). Facility id for both the sending (MSH-4) and receiving facility (MSH-6) will be the facility’s primary VA station number.

**Note: The POC vendor must be made aware that the MSH segment of the HL7 message must be configured in this manner.**

#### Step 4: OIT Staff

If the Point of Care (POC) system is subscribing to VistA ADT messages then add the subscriber protocol LA7POC ADT RTR as a subscriber to the following event protocols using HL package Protocol Edit [HL EDIT INTERFACE] option. After selecting the event protocol, go to the second screen and add LA7POC ADT RTR as a protocol under the SUBSCRIBERS section (see example below).

**Example:** Event Protocols

For each of the following protocols add LA7POC ADT RTR as a subscriber.

VAFC ADT-A01 SERVER

VAFC ADT-A02 SERVER

VAFC ADT-A03 SERVER

VAFC ADT-A04 SERVER

VAFC ADT-A08 SERVER

VAFC ADT-A08-SDAM SERVER

VAFC ADT-A08-TSP SERVER

VAFC ADT-A11 SERVER

VAFC ADT-A12 SERVER

VAFC ADT-A13 SERVER

VAFC ADT-A19 SERVER

**Example:** ScreenMan display for editing the Event Protocols

HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

NAME: VAFC ADT-A01 SERVER

DESCRIPTION (wp):   [ ]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                           Press &lt;PF1&gt;H for help    Insert

HL7 EVENT DRIVER                PAGE 2 OF 2

VAFC ADT-A01 SERVER

----------------------------------------------------------------------

SENDING APPLICATION: VAFC PIMS

TRANSACTION MESSAGE TYPE: ADT                        EVENT TYPE: A01

MESSAGE STRUCTURE:

PROCESSING ID:                            VERSION ID: 2.3

ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

DG PTF ADT-A01 CLIENT

LA7POC ADT RTR

#### Step 5: OIT staff

In the NEW PERSON file (#200), DIVISION field (#16), for NON-HUMAN user ‘LRLAB,POC’ assign the DIVISION(s) associated with the accession area(s) used for POC TEST RESULTS. The Laboratory’s LIM and/or ATC will be able to identify which accession areas are used by which DIVISION. The division of the ordering location is used as the accessioning division, therefore, each POC ordering location division should be assigned to the LRLAB,POC proxy user in the NEW PERSON file (#200), i.e., a DIVISION assignments is required for each facility division that performs POC testing.

Use the Transmission Utilities [DG NPTF XMIT MENU] Menu options if there is a need to resend a patient’s demographic or admission data.

**Example:** Transmission Utilities [DG NPTF XMIT MENU] Menu

Transmission Utilities [DG NPTF XMIT MENU] menu

D      Retransmit Patient Demographics [DG NPTF XMIT DEMOGRAPHICS] option

A      Retransmit Admission Data [DG NPTF XMIT ADMISSION] option

P      Retransmit Entry in ADT/HL7 PIVOT File [DG NPTF XMIT PIVOT] option

### Modified Options

The VistA Laboratory Point of Care (POC) software release includes the following options modifications:

#### Summary list (supervisors') [LR SUP SUMMARY] option

The Summary list (supervisors') [LR SUP SUMMARY] option is **modified** to display the performing user, performing laboratory, LOINC code, and Equipment Instance Identifier (EII) for each test result when long or extended format chosen. The EII contains the vendor’s make/model/serial number of the instrument/equipment that produced the test result. When the vendor’s instrument interface transmits this information, it is stored with the test results.

**Example:** Summary list (supervisors') [LR SUP SUMMARY] option

Select OPTION NAME: **LR SUP SUMMARY&lt;ENTER&gt;** Summary list (supervisors')

Summary list (supervisors')

Summary List (Supervisors')  &gt;&gt;&gt; NOT FOR WARD USE &lt;&lt;&lt;

DATE: TODAY// **5-10&lt;ENTER&gt;** (MAY 10, 2005)

Select ACCESSION AREA: **CHEMISTRY&lt;ENTER&gt;**

ANOTHER ONE:

Select one of the following:

1         ACCESSION NUMBER

2         PATIENT

List By: **1&lt;ENTER&gt;** ACCESSION NUMBER

Select one of the following:

L         LONG

S         SHORT

E         EXTENDED

Enter response: S// **EXTENDED&lt;ENTER&gt;**

First Accession number: 1// **&lt;ENTER&gt;**

Last Accession number: LAST// **1&lt;ENTER&gt;**

Optional - Select Collecting Institution : **&lt;ENTER&gt;**

Do you wish to see all tests including Common Accessions? Yes// **&lt;ENTER&gt;** (Yes)

DEVICE: HOME// **&lt;ENTER&gt;** 0;P-OTHER;132;9999999

UCX/TELNET

**Example:** Summary list (supervisors') [LR SUP SUMMARY] option (continued)

SUMMARY LIST (SUPERVISORS') FOR DATE: May 10, 2005          PAGE: 1

&gt;&gt; NOT FOR WARD USE &lt;&lt;

ACCESSION AREA(S) :CHEMISTRY

============================================================================

----------------------------------------------------------------------------

LABpatient,One                               REDACTED

CHEMISTRY ACC:  CH 0510 1                      ORDER #: 1217

Person placing order: LRLAB,POC   Person performing test: LRLAB,POC

DATE/TIME SPECIMEN TAKEN: MAY 04, 2005@10:00:05                             DATE REPORT COMPLETED: MAY 10, 2005@15:37:41

VERIFY PERSON: LRLAB,POC              SPECIMEN TYPE: ARTERIAL BLOOD        ACCESSION: CH 0510 1

REQUESTING PERSON: LRLABprovider,One           REQUESTING LOCATION: NCN    REQUESTING LOC/DIV: NON-COUNT CREDIT

GLUCOSE: 126 H ( mg/dL)               PERFORMED/RELEASED BY: LRuser,One

PERFORMING LAB: REGION 7 ISC,TX (DEMO)                                   LOINC Code: 14743

EII: ;;UJ32018960;Roche GTS/HQ/Inform                                   PH: 7.47 H (7.35-7.45 units)

PERFORMED/RELEASED BY: LRuser,One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2744                  EII: ;;UJ32018960;Roche GTS/HQ/Inform PCO2: 56 H (34-40 mm Hg)

PERFORMED/RELEASED BY: LRuser,One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2019                  EII: ;;UJ32018960;Roche GTS/HQ/Inform PO2: 116 H (30-90 mm Hg)

PERFORMED/RELEASED BY: LRuser,One                                PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2703                EII: ;;UJ32018960;Roche GTS/HQ/Inform BICARBONATE: 46 H ( mmol/L)

PERFORMED/RELEASED BY: LRuser,One                                  PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 1960                EII: ;;UJ32018960;Roche GTS/HQ/Inform

UID: 0451300001                       ORDERING SITE UID: 305399

ORDERED TEST: Glucose POC

ORDERED TEST: Blood Gas POC

END OF REPORT

#### Summary list (extended supervisors') [LRLISTE] option

The Summary list (extended supervisors') [LRLISTE] option is **modified** to display the performing user, performing laboratory, LOINC code, and Equipment Instance Identifier (EII) for each test result when long or extended format chosen. The EII contains the vendor’s make/model/serial number of the instrument/equipment that produced the test result. When the vendor’s instrument interface transmits this information it is stored with the test results.

**Example:** Summary list (extended supervisors') [LRLISTE] option

Select OPTION NAME: **LRLISTE&lt;ENTER&gt;** Summary list (extended supervisors')

Summary list (extended supervisors')

Summary List (Supervisers')  &gt;&gt;&gt; NOT FOR WARD USE &lt;&lt;&lt;

DATE: TODAY// **5-10&lt;ENTER&gt;** (MAY 10, 2005)

Select ACCESSION AREA: **CHEMISTRY&lt;ENTER&gt;**

ANOTHER ONE: **&lt;ENTER&gt;**

1 ACCESSION NUMBER

2 PATIENT

LIST BY: **1&lt;ENTER&gt;**

(L)ONG OR (S)HORT LISTING: S// **L&lt;ENTER&gt;**

First Accession number: 1// **&lt;ENTER&gt;**

Last Accession number: LAST// **1&lt;ENTER&gt;**

Do you wish to see all tests including Common Accessions? Yes// **&lt;ENTER&gt;** (Yes)

DEVICE: HOME// **&lt;ENTER&gt;** 0;132;999999

UCX/TELNET

SUMMARY LIST (SUPERVISORS') FOR DATE: 05/10/2005                PAGE: 1

&gt;&gt; NOT FOR WARD USE &lt;&lt;

ACCESSION AREA(S): CHEMISTRY

===========================================================================

---------------------------------------------------------------------------

LABPATIENT, TWO                     000-00-000  CHEMISTRY ACC:  CH 0510 1

Person placing order: LABPOC, TWO

TEST: BLOOD GASES                   URGENCY OF TEST: ROUTINE            TECHNOLOGIST: LABPOC, TWO

COMPLETE DATE: MAY 10, 2005@15:37:41  TALLY TO WKLD: YES                 WKLD SUFFIX: 4456

PARENT TEST: BLOOD GASES

**Example:** Summary list (extended supervisors') [LRLISTE] option *(continued)*

TEST: GLUCOSE, ANCILLARY TESTING       URGENCY OF TEST: ROUTINE           TECHNOLOGIST: LABPOC, TWO

COMPLETE DATE: MAY 10, 2005@15:37:41  TALLY TO WKLD: YES                WKLD SUFFIX: 4456

PARENT TEST: GLUCOSE, ANCILLARY TESTING

ORD: 1217              ARTERIAL BLOOD

DATE/TIME SPECIMEN TAKEN: MAY 04, 2005@10:00:05                             DATE REPORT COMPLETED: MAY 10, 2005@15:37:41

VERIFY PERSON: LRLAB,POC              SPECIMEN TYPE: ARTERIAL BLOOD        ACCESSION: CH 0510 1

REQUESTING PERSON: LABProvider, Two    REQUESTING LOCATION: NCN              REQUESTING LOC/DIV: NON-COUNT CREDIT

GLUCOSE: 126 H                        PERFORMED/RELEASED BY: LABuser, One PERFORMING LAB: REGION 7 ISC,TX (DEMO)       LOINC Code: 14743   EII: ;;UJ32018960;Roche GTS/HQ/Inform                     PH: 7.47 H

PERFORMED/RELEASED BY: LABuser, One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2744                     EII: ;;UJ32018960;Roche GTS/HQ/Inform   PCO2: 56 H

PERFORMED/RELEASED BY: LABuser, One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2019                     EII: ;;UJ32018960;Roche GTS/HQ/Inform   PO2: 116 H

PERFORMED/RELEASED BY: LABuser, One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 2703                     EII: ;;UJ32018960;Roche GTS/HQ/Inform   BICARBONATE: 46 H

PERFORMED/RELEASED BY: LABuser, One                                      PERFORMING LAB: REGION 7 ISC,TX (DEMO)

LOINC Code: 1960                     EII: ;;UJ32018960;Roche GTS/HQ/Inform

END OF REPORT

#### Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option

Lab messaging has been **modified** and will now check that Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option is scheduled in TaskMan. If this option is not scheduled then alert message notifying members of the LAB MESSAGING mail group is generated. The alert message will read “Lab Messaging- Option LA7TASK NIGHTY is not scheduled in TaskMan.” The Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option is tasked to check the integrity of LA7 MESSAGE QUEUE file (#62.49) and purge messages that are eligible for purging. It also purges the following files related to LEDI - SHIPPING MANIFEST (#62.8), LAB SHIPPING EVENT (#62.85), and LAB PENDING ORDERS ENTRY (#69.6).

The Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option should be tasked daily, preferably during period when activity in the Lab Messaging (i.e. Universal Interface, LEDI) package is at a minimum.

Prior to the purge of LA7 MESSAGE QUEUE file (#62.49), an integrity check is performed. The integrity check can be run with the following switches.

**NOTE:** Documentation regarding tasking can be found in the VistA Laboratory LEDI User Guide and on-line via the DESCRIPTION field of the OPTION file (#19) for this entry.

**Example:** Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option

Select OPTION NAME: **LA7TASK NIGHTY &lt;ENTER&gt;** Lab Messaging Nightly Cleanup

ANOTHER ONE: **&lt;ENTER&gt;**

STANDARD CAPTIONED OUTPUT? Yes// **&lt;ENTER&gt;** (Yes)

Include COMPUTED fields:  (N/Y/R/B): NO// **&lt;ENTER&gt;** - No record number (IEN), no Computed Fields

DISPLAY AUDIT TRAIL? No// **&lt;ENTER&gt;** NO

NAME: LA7TASK NIGHTY                    MENU TEXT: Lab Messaging Nightly Cleanup

TYPE: run routine                     CREATOR: LABCREATOR, ONE

PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION:   This is a tasked option to check integrity of LA7 MESSAGE

QUEUE file (#62.49) and purge messages that are eligible for

purging. It also purges the following files related to

LEDI - SHIPPING MANIFEST (#62.8), LAB SHIPPING EVENT file

(#62.85) and LAB PENDING ORDERS ENTRY (#69.6)

**Example:** Lab Messaging Nightly Cleanup [LA7TASK NIGHTY] option *(continued)*

This option should be tasked daily, preferably during period when activity in the Lab Messaging (i.e. Universal Interface, LEDI) package is at a minimum.

Prior to the purge of LA7 MESSAGE QUEUE file (#62.49), an integrity check is performed. The integrity check can be run with a couple of switches.

LA7FIX = 0 - do not fix errors

1 - do fix errors

LA7LOG = 0 - do not log errors in XTMP global.

1 - do log errors in XTMP global

LA7ION = name of device to print error report if set to

log errors (LA7LOG=1).

These parameters can be setup by TaskMan if the site defines them when scheduling the task.

An example is given below:

Edit Option Schedule

Option Name: LA7TASK NIGHTY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VARIABLE NAME: LA7FIX                   VALUE: 0

VARIABLE NAME: LA7ION                   VALUE: "IRM DEVELOP LASER1"

VARIABLE NAME: LA7LOG                   VALUE: 1

If errors are found, an alert is sent to members of the mail group "LAB MESSAGING" notifying them that errors were detected. If logging of errors occurred then alert recipients will be able to print/view error log from the alert system. Alternatively, the error report can be printed using Print Lab Messaging Integrity Check [LA7 PRINT INTEGRITY CHECK] option.

The integrity report can be run alone using option Lab Messaging File

Integrity Checker [LA7 CHECK FILES].

INDEPENDENTLY INVOCABLE: YES          ROUTINE: EN^LA7PURG

SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: LAB MESSAGING NIGHTLY CLEANUP

## TROUBLESHOOTING

The following options on the Lab Universal Interface menu can be helpful in displaying POC HL7 messages and troubleshooting errors in those messages:

Print Lab Universal Interface Log          [LA7 PRINT LAB UI ERROR LOG]

Display Lab Universal Interface Message      [LA7 PRINT LAB UI MESSAGE]

To use the Print Lab Universal Interface Log option, select a date for messages, enter the LA7POCn configuration name, and answer NO at the prompt “Print message text with error?”.  A list of messages with errors and the specific error message will be displayed.  Use the “Msg #” to view the full message using the option Display Lab Universal Interface Message.

You may also search for an HL7 message for a specific patient by using the option Display Lab Universal Interface Message.  At the “Select Message” prompt, enter “LA7POCn-I-SSN”, where n is the number of the specific configuration uses, and SSN is the SSN of the patient (no dashes).  A list of messages will be displayed.  Select the appropriate message, and answer NO to the prompt “Use Browser to display message(s)? YES//”.

Notes about HL7 messages:

**MSH** |^~\&amp;|LA7POC2|506|LA7LAB|506|20210415085355||ORU^R01|2021041508530056|P|2.4|20210415085355||AL|AL

MSH-1 = |

MSH-2 = ^~\&amp;

MSH-3 = LA7POC2  -- SENDING APPLICAITON

MSH-4 = 506      -- SENDING FACILITY  (station # of the site)

MSH-5 = LA7LAB   -- RECEIVING APPLICATION

MSH-6 = 506      -- RECEIVING FACILITY (station # of the site)

The MSH must be formatted in this way in order for the application acknowledgement to be sent to the POC vendor.

**ORC** |NW|||||||||184258||6266|22105^^^506|||||214713|

- ORC-12  (6266)= Ordering Provider (DUZ from file #200)
- ORC-13-1 (22105) = Ordering Location (IEN from file #44)
- ORC-14-4 (506)= Facility (Institution STATION NUMBER from file #4)

It is normal for the POC vendor NOT to send an ordering location and ordering provider.  If that information is sent, it should be as shown above.

**OBR** |||296455|81353.0000|||201804270945||||||||UR||||||288048|||||||||||||450820

- OBR-4 (81353.0000) = Order NLT code (file 60 NATIONAL VA LAB CODE)
- OBR-15 (UR) = SPECIMEN (HL7 specimen from Print POC Test Code mapping for the Load/Work list)
- OBR-16 = Ordering Provider (DUZ from file 200).  There is no DUZ in this example, which is common.

**OBX** ||ST|81184.0000^GLU^99VA64||173|mg/dL||H|||F||||506|130945||^^UU13098225^Roche GTS/HQ/Inform|201804190046

- OBX-3 (81184.0000) = Result NLT Code
- OBX-5 (173) = Test result
- OBX-6 (mg/dL)= Units
- OBX-7 = Reference Range (not sent in this example)
- OBX-8 (H) = Abnormal Flag
- OBX-15 (506) = Performing Lab
- OBX-16 (130945) = Responsible Observer (who performed test; DUZ from file #200)

**NTE** |||Provider Notified~Patient Treated~No Venous Draw per MD

- Comments – note the operator ID and instrument serial number should NOT be sent in the NTE

## WHAT THE POC VENDOR NEEDS TO KNOW

1. **Is the site using the ADT feed?** Use of the ADT feed is NOT required, but may be helpful.
2. **Specimen source for the order** .  This is the entry in the LEDI HL7 field of the TOPOGRAPHY FIELD file (#61) entry that is linked to the COLLECTION SAMPLE.  This field points to the LAB ELECTRONIC CODES file (#64.061).  It will be displayed on the Print POC Test Code Mapping report. Sent on OBR-15.
3. **Order NLT code** .  Assigned to the test in file #60 in the field NATIONAL VA LAB CODE. It will be displayed in the Load/Work List section of the Print POC Test Code Mapping report. Sent in OBR-4.
4. **Result NLT code** . Assigned to the test in file #60 in the field RESULT NLT CODE. It will be displayed in the Auto Instrument section of the Print POC Test Code Mapping report. Sent in OBX-3.
5. The Print POC Test Code Mapping report from the Lab Point of Care Setup menu is very important to share with the vendor.  See example below.
6. **The station number (Facility ID) of the site performing the test must be sent in OBX-15.** Note, this will be different for each CBOC or NHCU.  The vendor should send the specific station number for the location where the test was performed.
7. **The DUZ of the person performing the test (Responsible Observer) must be sent in the OBX-16** segment of the HL7 message.
8. **The “Equipment Instance”, i.e., analyzer and serial number, are sent in OBX-18** .  The vendor does NOT need to send this information as a comment (NTE segment).
9. **The IP address and port of the VistA system** .  The IP should be in the form of the DNS name, i.e., HL7.sitename.med.va.gov.  You might need someone to check the DOMAIN file for the format of your specific “sitename”.  The port will always be 5000 for the production account.
10. **When testing the POC interface,** an error of **“** No valid ordering location” is going to happen with test patients, because the patient has no scheduled appointment to use for the ordering location.  You need to have the vendor stuff a default ordering location and default ordering provider when testing the interface.  You will need to provide the information for the ordering location (IEN of a valid entry in file #44), and the information for the ordering provider (DUZ of valid/active provider from file #200). This is what the vendor needs to add those defaults as follows:

The ordering location information is in ORC-13.

The ordering provider information is in ORC-12 and OBR-16.

1. For Ack messages to the vendor, you will use the LA7POCn logical link (whichever one you added the tests to the auto instrument by the same name).  Within that logical link, your IT folks will add the IP address of the vendor’s server, and the port that the vendor listens on for Ack messages.
2. The vendor will send results to Vista using the DNS of HL7.site DNS.MED.VA.GOV
3. **The link to the Lab Point of Care HL7 specifications document on the VDL** :

[https://www.va.gov/vdl/documents/Clinical/Lab-Point\_of\_Care/lab\_52\_poc\_hl7\_spec.pdf](https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/lab_52_poc_hl7_spec.pdf)

This is the standard they *must* use for configuring their HL7 messages.

**Example of the output from Print POC Test Code Mapping:**

**Note:**

1. Only ORDERABLE tests are added to the Load/Work List.  Those tests must have a TYPE of BOTH in file #60.
2. Only use the LOAD/WORK LIST option from the Lab Point of Care Setup menu to edit the load/work list.  Do NOT user FileMan.

Select Lab Universal Interface Menu Option: PCS  Lab Point of Care Setup

Select one of the following:

1         LA7 MESSAGE PARAMETER (#62.48)

2         LOAD/WORK LIST (#68.2)

3         AUTO INSTRUMENT (#62.4)

4         Print POC Test Code Mapping

Select which file to setup: 4  Print POC Test Code Mapping

Select AUTO INSTRUMENT NAME: LA7POC2

DEVICE: HOME// ;;9999  Linux Telnet/SSH

Point of Care Test Code Mapping                              Page: 1

for interface: LA7POC2                                   Printed: Jul 09, 2019

================================================================================

VistA ADT feed enabled: NO  &lt;&lt;&lt; tells if ADT is used

POC Order Test Codes using Load/Work List: CPOC

# Lab Test                   Order NLT Code      Specimen(IEN)       HL7 Spec

Order NLT Name      Collection Sample   WKLD Code

--------------------------------------------------------------------------------

1 WHOLE BLOOD GLUCOSE        82115.0000          BLOOD(70)           BLD

Glucose POC         CAPILLARY BLOOD     .9999

2 ACT.CLOTTING TIME          85059.0000          ARTERIAL BLOO(8728) BLDA

Activated Clotting TimeARTERIAL BLOOD   .9999

3 ACT.CLOTTING TIME          85059.0000          VENOUS BLOOD(9011)  BLD

Activated Clotting TimeVENOUS BLOOD     .9999

4 DIPSTICK UA (POC)-CO       81353.0000          URINE(71)           UR

Urine Dipstick ManualURIN,RAND          .9999

POC Result Test Codes using Auto Instrument: LA7POC2

# Lab Test                   Result NLT Code          Specimen(IEN)

Dataname(IEN)              Result NLT Name          HL7 Spec

--------------------------------------------------------------------------------

1 WHOLE BLOOD GLUCOSE        81184.0000               BLOOD(70)

WHOLEBLD GLUC(589926)      Glucose Stick            BLD

2 POC UR COLOR               81206.9999               URINE RANDOM(9046)

POC COLOR(591647)          Color Urine~DSS ACC      UR

3 POC UR APPEARANCE          84930.9999               URINE RANDOM(9046)

POC APPEARANCE(591648)     Appearance~DSS ACC       UR

4 POC UR SP GRAVITY          81198.9999               URINE RANDOM(9046)

POC SPECIF GRAVIT(591640)  Specific Gravity Uri     UR

**Example of specimen source:**

The test in file 60 has a collection sample of CAPILLARY BLOOD.  In the COLLECTION SAMPLE file (#62), CAPILLARY BLOOD has a DEFAULT SPECIMEN of BLOOD.

NUMBER: 174                             NAME: CAPILLARY BLOOD

DEFAULT SPECIMEN: BLOOD               TUBE TOP COLOR: FINGER

In the TOPOGRAPHY FIELD file (#61), BLOOD has a LEDI HL7 CODE of Whole Blood:

NUMBER: 70                              NAME: BLOOD

SNOMED CODE: 0X000                    ABBREVIATION: BLD

COLLECTION SAMPLE: BLOOD              HL7 CODE: BLD

LEDI HL7: Whole blood                 TIME ASPECT: POINT

The LEDI HL7 field is a pointer to the LAB INSTRUMENT CODE file (#64.061). The Whole Blood entry there has an HL7 ABBR of BLD, which is what the vendor needs to know.  This is the specimen code shown on the Print POC Test Code Mapping report.

SEQUENCE: 114                           NAME: Whole blood

LOINC ABBR: BLD                       HL7 ABBR: BLD

HL7 TABLE: 0070                       TYPE: SPECIMEN

DESCRIPTION: from LOINC system list

## Glossary

This Glossary contains terms and their definitions, acronyms, and phrases that are used throughout the VistA Laboratory environments:

| Term       | Definition                                                      |
|------------|-----------------------------------------------------------------|
| AAC        | Austin Automation Center                                        |
| LIM        | Automated Data Processing Application Coordinator               |
| ADT        | Admissions, Discharge, Transfer                                 |
| API        | Application Program Interface                                   |
| ATC        | Ancillary Testing Coordinator                                   |
| COTS       | Commercial of the Shelf                                         |
| CPRS       | Comments Section of the Computer Patient Record System          |
| DBS        | Data Base Server                                                |
| E3R        | Electronic Error and Enhancement Report                         |
| EEI        | Equipment Entity Identifier                                     |
| HCS        | Health Care Systems                                             |
| HL7        | Health Level Seven                                              |
| IDCU       | Integrated Data Communications Utility                          |
| KIDS       | Kernel Installation & Distribution System                       |
| LAN        | Local Area Network                                              |
| LEDI       | Laboratory Electronic Data Interchange                          |
| MUMPS      | Massachusetts General Hospital Utility Multi-Programming System |
| NLFT       | VA National Laboratory Test File                                |
| NOIS       | National Online Information System                              |
| OI         | Office of Information                                           |
| PIMS       | Patient Information Management System                           |
| PLMS       | Pathology and Laboratory Medicine Service                       |
| POC        | Point of Care                                                   |
| PTF        | Patient Treatment File                                          |
| RPC Broker | Remote Procedure Call Broker                                    |
| TCP/IP     | Transmission Control Protocol/Internet Protocol                 |
| UI         | Universal Interface                                             |
| VA         | Department of Veterans Affairs (never use DVA)                  |
| VAMC       | Department of Veterans Affairs Medical Centers                  |
| VAO        | VA Office                                                       |
| VISN       | Veterans Integrated Service Network                             |
| VistA      | Veterans Health Information Systems and Architecture            |