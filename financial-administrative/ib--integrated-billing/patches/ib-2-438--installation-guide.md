---
title: IB*2*438 eIV Phase 3 Iteration 2 Release Notes/Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: eIV Phase 3 Iteration 2 Release Notes/
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*438
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - inquiry
  - service
  - eligibility
  - insurance
  - response
  - message
  - patch
  - time
page_count: 0
word_count: 2624
section_count: 10
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2011
revision_count: 1
revision_newest: 08/01/2011
revision_oldest: 08/01/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p438_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p438_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

Integrated Billing

eIV Phase 3 Iteration 2

![](ib-2-438-eiv-phase-3-iteration-2-release-notes-installation-guide/001.png)

Release Notes and Installation Guide

IB\*2\*438

August 2011

Veterans Affairs

Product Development (PD)

*(This page included for two-sided copying.)*

Revision History

| Date       | Version | Description | Author   |
|------------|---------|-------------|----------|
| 08/01/2011 | 1.0     | Initial     | REDACTED |
|            |         |             |          |

*(This page included for two-sided copying.))  
*

######## Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
  - [Overview of eIV Phase 3 Iteration 2 Software Enhancements](#overview-of-eiv-phase-3-iteration-2-software-enhancements)
  - [Patch IB\2\438 includes the following New Service Requests (NSRs)](#patch-ib2438-includes-the-following-new-service-requests-nsrs)
  - [Patch IB\2\438 addresses the following Remedy Tickets](#patch-ib2438-addresses-the-following-remedy-tickets)
  - [Documentation Retrieval](#documentation-retrieval)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
  - [Patch IB\2\438 includes the following modifications](#patch-ib2438-includes-the-following-modifications)
    - [Eligibility Inquiry Message](#eligibility-inquiry-message)
    - [MCCR Site Parameter Display/Edit – eIV](#mccr-site-parameter-displayedit-eiv)
    - [Service Type Inquiry- EI Request Electronic Insurance Inquiry](#service-type-inquiry-ei-request-electronic-insurance-inquiry)
    - [Inquiry Problem Information](#inquiry-problem-information)
    - [Eligibility Response Information](#eligibility-response-information)
    - [MailMan Notification](#mailman-notification)
    - [Real-time insurance verification functionality is now available](#real-time-insurance-verification-functionality-is-now-available)
    - [Buffer Extract](#buffer-extract)
    - [Non-Verified Extract](#non-verified-extract)
- [Appendix](#appendix)
  - [Service Codes](#service-codes)
This patch contains Electronic Insurance Verification (eIV) enhancements which allow Veterans Health Information Systems and Technology Architecture (VistA) to fully comply with Health Insurance Portability and Accountability Act (HIPAA) guidelines by allowing generation of service type specific transactions. It will also further enhance the eIV process by modifying existing reports and providing new notification for tracking payer links. Patch also includes real-time insurance verification functionality and changes to eIV inquiries and responses designed to accommodate for transmission of extra information and improved error handling.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview of eIV Phase 3 Iteration 2 Software Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Service Type Code Site Parameter
- Unlinked Payer Email Notification
- Activate Payer Email Notification
- Real-Time Insurance Verification Inquiry
- Additional Patient Insurance Information
- Additional Eligibility Benefit Information
- Enhancement to Response Reports
- Response Report Error Messages
- Enhancement to Error Reporting in VistA
- Eligibility Error Responses from FSC
- Additional VistA Error Reporting
- Appointment Extract / Non-Verified Extract Updates

## Patch IB\*2\*438 includes the following New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

20080221 - eIV Phase 3 Iteration 2

## Patch IB\*2\*438 addresses the following Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

 

 1.  The preferred method is to FTP the files from REDACTED, which will transmit the files from the first available FTP server.
 2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

 

     Albany          [REDACTED](ftp://ftp.fo-albany.med.va.gov)

     Hines           [REDACTED](ftp://ftp.fo-hines.med.va.gov)

     Salt Lake City  [REDACTED](ftp://ftp.fo-slc.med.va.gov)
 3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address, <http://www.va.gov/vdl>.

 

The documentation distribution includes:

 

| FILE NAME           | DESCRIPTION  |
|-------------------------|------------------|
| IB_2_P438_UM_R0811.PDF  | User Guide       |
| IB_2_P438_TM.PDF        | Technical Manual |

 

# Installation 

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches which must be installed before IB\*2\*438 are IB\*2\*399, IB\*2\*416 and IB\*2\*444.

## Pre/Post Installation Overview

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Post-Install routine (IBY438PO) is automatically deleted after this patch is installed.

The Post-Install routine sends site registration message to Financial Services Center (FSC) and schedules payer link notification option to be run weekly.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that this patch be installed outside of normal working hours when no Integrated Billing users are on the system. However, if installed during the normal workday, it is recommended that the following selections in the OPTION (#19) file and all of their descendants be disabled to prevent possible conflicts while running the KIDS Install. Other VISTA users will not be affected.

MCCR Site Parameter Display/Edit \[IBJ MCCR SITE PARAMETERS\]

Request Electronic Insurance Inquiry \[IBCNE REQUEST INQUIRY\]

Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]

eIV Menu \[IBCNE IIV MENU\]

\*\*\*\* Do not install this patch when the \[IBCNE IIV BATCH PROCESS\] nightly eIV background job is running or scheduled to run. \*\*\*\*

Install Time - less than 5 minutes

*1. LOAD TRANSPORT GLOBAL*

Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

*2. START UP KIDS*

Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

*3. Select Installation Option:*

> **NOTE:** The following are OPTIONAL - (When prompted for the INSTALL NAME, enter IB\*2.0\*438):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

*4. Select Installation Option: Install Package(s)*

\*\*This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer YES, unless your system does this in a nightly TaskMan process.
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer YES if installing during working hours
5.  When prompted 'Enter options you wish to mark as 'Out Of Order':' Enter the following options:

MCCR Site Parameter Display/Edit \[IBJ MCCR SITE PARAMETERS\]

> Request Electronic Insurance Inquiry \[IBCNE REQUEST INQUIRY\]

> Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]

eIV Menu \[IBCNE IIV MENU\]

6.  When prompted 'Enter protocols you wish to mark as 'Out Of Order':' press \<return\>.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch IB\*2\*438 includes the following modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Eligibility Inquiry Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections list the modifications and enhancements to the Eligibility Inquiry Message

#### Subscriber Name Length

The system provides the ability to send the Subscriber Name in an Eligibility Inquiry with a maximum length of 130 characters.

#### Group Number Length

The system will send the Group Number in an Eligibility Inquiry with a maximum length of 50 characters.

#### Payer Name Length

The system provides the ability to send the Payer Name in an Eligibility Inquiry with a maximum length of 60 characters.

#### Date Time Qualifier – Inactivate existing qualifier codes 

The system no longer provides the ability to send the following qualifier and dates in an Eligibility Inquiry:

> Code Definition

> 307 Admission Date

> 435 Service Date

> 472 Eligibility Date

#### Date Time Qualifier – Add New Qualifier Codes 

The system provides the ability to send the following qualifier code and date in an Eligibility Inquiry if available:

> Code Definition

> 291 Plan Date

#### Service Type Codes – Add New Service Type Codes 

The system provides the ability to send the new service codes listed in Appendix 5.1 in an Eligibility Inquiry if applicable.

#### Multiple Service Type Codes

The system provides the ability to send multiple service type codes in an Eligibility Inquiry.

#### Default Service Type Codes in Eligibility Inquiry 

The system will send the following service type codes in every Eligibility Inquiry unless the service type code is manually selected using “Request Electronic Inquiry” menu option

1.  30 - Health benefit eligibility inquiry
2.  1 - Medical Care
3.  47 - Hospital
4.  88 - Pharmacy
5.  98 - Professional (Physician) Visit - Office
6.  MH - Mental Health
7.  7 - Anesthesia
8.  54 - Long term care
9.  62 - MR/CAT scan
10. 75 - Prosthetics
11. 97 - Anesthesiologist

### MCCR Site Parameter Display/Edit – eIV 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### eIV Site Parameter- Service Type 

The system will have a new site parameter “Service Type” to provide the ability for users to manage up to 9 additional service types to be included in addition to the 11 hardcoded default service types in an Eligibility Inquiry.

#### Service Type Code Lookup

The system will list all the service type codes (except the 11 default service codes) and associated description in Appendix 5.1 when requested for more information.

### Service Type Inquiry- EI Request Electronic Insurance Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Prompt for Service Specific Inquiry

The system will prompt the user to choose or enter a service type code to generate a service type specific Eligibility Inquiry.

#### One Service Type Code per Inquiry

The system will allow user to select only one service type code per electronic insurance inquiry.

#### Service Type Code Look-up

> The system provides users with a list of all the 187 service type codes and description to look up when indicated.

#### No Service Type Code 

> The system utilizes the 11 “default” service type codes and (up to 9) additional service type codes defined by the site parameter “Service Type” when null or blank response is received from the user.

### Inquiry Problem Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Condition Codes

The system provides the ability to store and display all the reject reason codes when available from FSC in an Inquiry Problem Message. The reject reason codes are available only when the request transaction was unable to process successfully.

> Code Description

> 97 Invalid or Missing Provider Address

> 35 Out of Network

> 33 Input Errors

> 98 Experimental Service or Procedure

> A0 Additional Patient Condition Information Required

> AA Authorization Number Not Found

> AE Requires Primary Care Physician Authorization

> AF Invalid/Missing Diagnosis Code(s)

> AG Invalid/Missing Procedure Code(s)

> CI Certification Information Does Not Match Patient

> E8 Requires Medical Review

> IA Invalid Authorization Number Format

> MA Missing Authorization Number

### Eligibility Response Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Subscriber \Dependent Date Time Period Qualifiers

The system provides the ability to store and display the Subscriber and\or dependent associated date and time information when available from FSC in Eligibility Response Message. This information will be processed and displayed in the eIV Response Report.

> Code Description

> 96 Discharge

> 102 Issue

> 152 Effective Date of Change

> 291 Plan

> 340 Consolidated Omnibus Budget Reconciliation Act (COBRA) Begin

> 341 COBRA End

> 342 Premium Paid to Date Begin

> 343 Premium Paid to Date End

> 346 Plan Begin

> 347 Plan End

> 382 Enrollment

> 442 Date of Death

> 458 Certification

> 539 Policy Effective

> 540 Policy Expiration

#### Quantity Qualifiers 

The system provides the ability to store and display the following Quantity Qualifier codes when available from FSC in Eligibility Response Message. This information will be processed and displayed in the patient insurance when manually accepted or automatically updated.

Code Description

D3 Number of Co-insurance Days

8H Minimum

#### Communication Number Qualifier Code

The system provides the ability to store and display the Web address information when available from FSC in Eligibility Response Message. This information will be processed and displayed in the patient insurance when accepted or automatically updated.

> Code Description

> UR Uniform Resource Locator (URL)

#### Code List Qualifier Code

The system will skip processing the following Code List Qualifiers when available from FSC in Eligibility Response Message. This information will not be processed and displayed in the patient insurance when accepted or automatically updated.

> Code Description

> GR National Council on Compensation Insurance

> (NCCI) Nature of Injury Code

> NI Nature of Injury Code

#### #### Inactivate Code List Qualifiers

#### The system will inactivate the following code qualifiers:

> Code Description

> BF Diagnosis

> BK Principal Diagnosis

#### Subscriber’s Country Subdivision Codes 

The system provides the ability to store and display the Country Sub Codes when available from FSC in Eligibility Response Message. This information will be processed and displayed in the patient insurance when accepted or automatically updated.

#### Eligibility Benefit Date Time Period Qualifiers

The system provides the ability to store and display Subscriber and\or Dependent associated Eligibility Benefit date and time information when available from FSC in Eligibility Response Message. This information will be processed and displayed in the patient insurance when accepted or automatically updated.

> Code Description

> 96 Discharge

> 291 Plan

#### Eligibility Response with Multiple Service Type Codes

The system will be able to store multiple service codes within each set of Eligibility Benefit Information received from FSC. The service codes will be stored and displayed within the Eligibility Benefit Section of Patient Insurance.

#### Patient Relationship to Insured Translation 

The System will translate the values for the ‘Patient Relationship to Insured’ that is received from FSC in Eligibility Response Message in the following manner when updating the Patient’s insurance in VistA (automatic and manual updates):

- Self (18) (Response)= Self (18) (VistA)
- Spouse (01) (Response) = Spouse (01) (VistA)
- Child (19) (Response) = Child (19) (VistA)
- Unknown (21) (Response) = No change to Vista
- Employee (20) (Response) = Employee (20) (VistA)
- Organ Donor (39) (Response) = Organ Donor (39) (VistA)
- Life Partner (53) (Response)  = Life Partner (53) (VistA)
- Other Relationship (G8) (Response) = Other Relationship (G8) (VistA)
- Cadaver Donor (40) = Other Relationship (G8) (VistA)
- Other Adult Value (in Response) and existing value is  
  > Self/Spouse/Child = Other Relationship (G8) (VistA)
- Other Adult Value (in Response) and existing value is  
  > not Self/Spouse/Child = No change to VistA

### MailMan Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### (Modified 1/12/2011) MailMan Notification to Link Payers 

The system will trigger a mailman message on a weekly basis to IBCNE EIV Message

Mail group if the following information is available to notify:-

- Total Number of Nationally Active Unlinked Payers with Potential Matches to active insurance companies.
- Instructional Help Text:

> <u>Immediate Attention Required:</u> Please link the associated active insurance companies to these payers at your earliest convenience. Please visit the e-Business Projects Webpage on VistA University Website to download the Link Payer Instructions.

#### (Added 1/12/2011) MailMan Notification to Activate Payers

The system will trigger a mailman message on a weekly basis to IBCNE EIV Message

Mail group if the following information is available to notify:-

- A List of Payers who meet the following criteria:-
  1.  Locally inactive AND
  2.  Nationally Active AND
  3.  Have linked insurance companies.
- Instructional Help Text:

> <u>Immediate Attention Required</u>: Please locally activate the payers after you link insurance companies to them. Please visit the e-Business Projects Webpage on VistA University Website to download the Payer Activation Instructions.

### Real-time insurance verification functionality is now available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Real-time insurance verification functionality is now available. Verification inquiries will be generated and transmitted right after the creation of insurance buffer entry.

#### Trigger events for Real Time Verification

- The system will trigger real-time eligibility inquiry when there is a NEW entry in the insurance buffer.
- The system will trigger a real time eligibility, coverage and benefit inquiry when MODIFICATIONS are made to the following fields of the buffer entry:
  - Insurance Company; or
  - Group/Plan Name; or
  - Group Number; or
  - Subscriber ID.

#### Minimum criteria for Real Time Eligibility Inquiry

The system will send an eligibility inquiry message to Financial Service Center (FSC) for a patient when the following conditions are met:-

- The following information is available:
  - Patient Name
  - Subscriber ID
  - Patient’s Date of Birth
  - Insured’s Date of Birth
  - Insurance Company
- There is no other inquiry in the queue waiting to be transmitted for the same patient and policy for which the system is awaiting a response.
- The patient insurance information is not locked by another user.

#### No Site Registration Message to FSC for every Real time Inquiry

The system will not send registration request message to FSC each time a real time insurance verification is triggered.

#### Site Registration Message on Patch Installation

The system will send a Registration Message to FSC when the IB\*2\*438 patch is installed at a Facility.

#### Response to manually triggered real-time verification

The system will not auto-update or bypasses the Insurance Buffer when the Eligibility Response received is for a service type inquiry manually triggered from “Request Electronic Inquiry” option.

> **NOTE:** The following requirements were added due to enhancement requests submitted during field testing:

#### #### Prevent HMS buffer entries from Real Time Verification

The system will not trigger real time insurance verification inquires for buffer entries created by HMS data upload.

### Buffer Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### #### Buffer Extract Inquiries in transmission queue will override freshness days

The eIV system will no longer check for freshness days (‘Days between electronic re-verification checks’ defined in the MCCR site parameter) for eligibility benefit inquiries, which are available in the buffer and are awaiting transmission in the transmission queue.

### Non-Verified Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Set ‘Non-Verified’ Batch Extract Parameter to non-editable

The System will automatically set the “Non-Verified” Batch Extracts parameter when the software patch is installed to non-editable.

- Batch ExtractsNon-verified – Active/Non-Active Setting = Non-Active (non-editable).

Batch Extracts

Extract Selection Maximum \# to

<u>Name On/Off Criteria Extract/Day</u>

Buffer ON n/a 99999

Appt ON 10 99999

Non-verified OFF 180/180 99999 \<- Set “non-verified” non-editable and it will not be displayed on the screen.

#### Disable Batch Extract parameters from IV Site Parameters

The eIV system will automatically disable the Batch Extract Site Parameter within the IV Site Parameters when the software is installed.

*(This page included for two-sided copying.)*

# Appendix 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Service Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\* -- Indicates a new 5010 service code

| Service Codes - Description          |                                                     |                                                    |
|------------------------------------------|-----------------------------------------------------|----------------------------------------------------|
| 2 Surgical                               | 66 Pathology                                        | AR Experimental Drug Therapy                       |
| 3 Consultation                           | 67 Smoking Cessation                                | BA Independent Medical Eval                        |
| 4 Diagnostic X-Ray                       | 68 Well Baby Care                                   | BB Partial Hosp (Psych)                            |
| 5 Diagnostic Lab                         | 69 Maternity                                        | BC Day Care (Psych)                                |
| 6 Radiation Therapy                      | 70 Transplants                                      | BD Cognitive Therapy                               |
|                                          | 71 Audiology Exam                                   | BE Massage Therapy                                 |
| 8 Surgical Assistance                    | 72 Inhalation Therapy                               | BF Pulmonary Rehab                                 |
| 9 Other Medical                          | 73 Diagnostic Medical                               | BG Cardiac Rehab                                   |
| 10 Blood Charges                         | 74 Private Duty Nursing                             | BH Pediatric                                       |
| 11 Used Durable Medical Equipment        | 76 Dialysis                                         | BI Nursery                                         |
| 12 Durable Medical Equipment Purchase    | 77 Otological Exam                                  | BJ Skin                                            |
| 13 Ambulatory Service Center Facility    | 78 Chemotherapy                                     | BK Orthopedic                                      |
| 14 Renal Supplies in the Home            | 79 Allergy Testing                                  | BL Cardiac                                         |
| 15 Alternate Method Dialysis             | 80 Immunizations                                    | BM Lymphatic                                       |
| 16 Chronic Renal Disease (CRD) Equipment | 81 Routine Physical                                 | BN Gastrointestinal                                |
| 17 Pre-Admission Testing                 | 82 Family Planning                                  | BP Endocrine                                       |
| 18 Durable Medical Equipment Rental      | 83 Infertility                                      | BQ Neurology                                       |
| 19 Pneumonia Vaccine                     | 84 Abortion                                         | BR Eye                                             |
| 20 Second Surgical Opinion               | 85 AIDS                                             | BS Invasive Procedures                             |
| 21 Third Surgical Opinion                | 86 Emergency Services                               | B1 Burn Care\*                                     |
| 22 Social Work                           | 87 Cancer                                           | B2 Brand Name Prescription Drug – Formulary \*     |
| 23 Diagnostic Dental                     | 89 Free Standing Prescription Drug                  | B3 Brand Name Prescription Drug - Non-Formulary\*  |
| 24 Periodontics                          | 90 Mail Order Prescription Drug                     | BT Gynecological\*                                 |
| 25 Restorative                           | 91 Brand Name Prescription Drug                     | BU Obstetrical\*                                   |
| 26 Endodontics                           | 92 Generic Prescription Drug                        | BV Obstetrical/Gynecological\*                     |
| 27 Maxillofacial Prosthetics             | 93 Podiatry                                         | BW Mail Order Prescription Drug: Brand Name\*      |
| 28 Adjunctive Dental Services            | 94 Podiatry - Office Visits                         | BX Mail Order Prescription Drug: Generic\*         |
| 32 Plan Waiting Period                   | 95 Podiatry - Nursing Home Visits                   | BY Physician Visit - Office: Sick\*                |
| 33 Chiropractic                          | 96 Professional (Physician)                         | BZ Physician Visit - Office: Well\*                |
| 34 Chiropractic Office Vst               | 99 Professional (Physician) Visit - Inpatient       | C1 Coronary Care\*                                 |
| 35 Dental Care                           |                                                     | CA Private Duty Nursing - Inpatient\*              |
| 36 Dental Crowns                         | A0 Professional (Physician) Visit - Outpatient      | CB Private Duty Nursing - Home\*                   |
| 37 Dental Accident                       | A1 Professional (Physician) Visit - Nursing Home    | CC Surgical Benefits - Professional (Physician) \* |
| 38 Orthodontics                          | A2 Professional (Physician) Visit - Skilled Nursing | CD Surgical Benefits - Facility\*                  |
| 39 Prosthodontics                        | A3 Professional (Physician) Visit - Home            | CE Mental Health Provider - Inpatient\*            |
| 40 Oral Surgery                          | A4 Psychiatric                                      | CF Mental Health Provider - Outpatient\*           |
| 41 Rout/Preventive Dental                | A5 Psychiatric - Room and Board                     | CG Mental Health Facility - Inpatient\*            |
| 42 Home Health Care                      | A6 Psychotherapy                                    | CH Mental Health Facility - Outpatient\*           |
| 43 Home Health RX                        | A7 Psychiatric - Inpatient                          | CI Substance Abuse Facility - Inpatientc\*         |
| 44 Home Health Vst                       | A8 Psychiatric - Outpatient                         | CJ Substance Abuse Facility - Outpatient\*         |
| 45 Hospice                               | A9 Rehabilitation                                   | CK Screening X-ray\*                               |
| 46 Respite Care                          | AA Rehabilitation - Room and Board                  | CL Screening laboratory\*                          |
|                                          | AB Rehab/Inpt                                       | CM Mammogram, High Risk Patient\*                  |
| 48 Hosp/Inpatient                        | AC Rehab/Outpt                                      | CN Mammogram, Low Risk Patient\*                   |
| 49 Hosp/R & B                            | AD Occupational Therapy                             | CO Flu Vaccination\*                               |
| 50 Hosp/Outpatient                       | AE Physical Medicine                                | CP Eyewear and Eyewear Accessories\*               |
| 51 Hosp/Emergency Accident               | AF Speech Therapy                                   | CQ Case Management\*                               |
| 52 Hosp/Emergency Medical                | AG SNC                                              | DG Dermatology\*                                   |
| 53 Hosp/Ambulatory Surg                  | AH SNC/R & B                                        | DM Durable Medical Equipment\*                     |
| 55 Major Medical                         | AI Substance Abuse                                  | DS Diabetic Supplies\*                             |
| 56 Med Related Transport                 | AJ Alcoholism                                       | GF Generic Prescription Drug - Formulary\*         |
| 57 Air Transportation                    | AK Drug Addiction                                   | GN Generic Prescription Drug - Non-Formulary\*     |
| 58 Cabulance                             | AL Vision (Optometry)                               | GY Allergy\*                                       |
| 59 Licensed Ambulance                    | AM Frames                                           | IC Intensive Care\*                                |
| 60 General Benefits                      | AN Routine Exam                                     | NI Neonatal Intensive Care\*                       |
| 61 In-vitro Fertilization                | AO Lenses                                           | ON Oncology\*                                      |
| 63 Donor Procedures                      | AQ N/Medically Nec Physical                         | PT Physical Therapy\*                              |
| 64 Acupuncture                           | UC Urgent Care\*                                    | PU Pulmonary\*                                     |
| 65 Newborn Care                          |                                                     | RN Renal\*                                         |
|                                          |                                                     | RT Residential Psychiatric Treatment\*             |
|                                          |                                                     | TC Transitional Care\*                             |
|                                          |                                                     | TN Transitional Nursery Care\*                     |