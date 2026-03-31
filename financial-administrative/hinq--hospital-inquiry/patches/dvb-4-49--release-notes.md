---
title: DVB*4*49 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: HINQ
app_name: Hospital Inquiry
section: FIN
app_status: active
pkg_ns: DVB
patch_ver: 4
patch_id: DVB*4*49
group_key: "HINQ:DVB:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - hinq
  - access
  - date
  - vista
  - effective
  - service
  - displayed
  - required
page_count: 0
word_count: 2225
section_count: 23
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=41"
---

![](dvb-4-49-release-notes/001.png)

HINQ REPLACEMENT INTERIM SOLUTION PHASE 1

RELEASE NOTES

DG\*5.3.\*631

> DGBT\*1\*11

> DVB\*4\*49

November 2005

V*IST*A Health Systems Design & Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
- [Acronyms and Definitions](#acronyms-and-definitions)
  - [Acronyms](#acronyms)
  - [Definitions](#definitions)
- [User Release Notes](#user-release-notes)
  - [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
  - [Old HINQUP Field Display Options Removed](#old-hinqup-field-display-options-removed)
  - [HINQ Mail Message Changed](#hinq-mail-message-changed)
  - [Screen Options Changed](#screen-options-changed)
  - [Screen 0](#screen-0)
  - [Screen 1](#screen-1)
  - [Screen 2](#screen-2)
  - [Screen 3](#screen-3)
    - [Screen 4](#screen-4)
    - [## Screen 5](#screen-5)
  - [HINQ System Features](#hinq-system-features)
  - [New VBA Data Set](#new-vba-data-set)
    - [Up to 150 Service Connected (SC) codes and percents are returned and displayed](#up-to-150-service-connected-sc-codes-and-percents-are-returned-and-displayed)
    - [Up to 20 children are returned and displayed](#up-to-20-children-are-returned-and-displayed)
    - [Effective Date of Combined Evaluation, Extremity, Original Effective Date and Current Effective Date are displayed.](#effective-date-of-combined-evaluation-extremity-original-effective-date-and-current-effective-date-are-displayed)
  - [Crossmapping](#crossmapping)
  - [Redirecting HINQ Transaction](#redirecting-hinq-transaction)
- [Performance Requirements](#performance-requirements)
  - [Security and User Access](#security-and-user-access)
    - [All users are required to have a VBA BDN Password, and a VistA HINQ security key (employee number).](#all-users-are-required-to-have-a-vba-bdn-password-and-a-vista-hinq-security-key-employee-number)
    - [A user is required to access HINQ at least once every 90 days to avoid the system locking them out.](#a-user-is-required-to-access-hinq-at-least-once-every-90-days-to-avoid-the-system-locking-them-out)
    - [If a user has not accessed his/her HINQ account after 90 days an error code message will automatically appear preventing the user from accessing HINQ.](#if-a-user-has-not-accessed-hisher-hinq-account-after-90-days-an-error-code-message-will-automatically-appear-preventing-the-user-from-accessing-hinq)
    - [In the event that a user is denied access at any time, the user is required to contact their VBA ISO coordinator.](#in-the-event-that-a-user-is-denied-access-at-any-time-the-user-is-required-to-contact-their-vba-iso-coordinator)
    - [All users are responsible for following-up with their VBA ISO coordinator in expediting all access requests.](#all-users-are-responsible-for-following-up-with-their-vba-iso-coordinator-in-expediting-all-access-requests)
    - [All new and current employees are required to complete a VAF 20-8824e form and forward it to their VBA ISO coordinator to ensure access to the HINQ system. The application to request is called “Web HINQ.”](#all-new-and-current-employees-are-required-to-complete-a-vaf-20-8824e-form-and-forward-it-to-their-vba-iso-coordinator-to-ensure-access-to-the-hinq-system-the-application-to-request-is-called-web-hinq)
  - [HINQ Users Access](#hinq-users-access)
  - [## HINQ Employee Numbers](#hinq-employee-numbers)
- [Technical Release Notes](#technical-release-notes)
  - [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements-1)
  - [HEC Legacy](#hec-legacy)
    - [Data Dictionary](#data-dictionary)
  - [VistA](#vista)
    - [Input Template](#input-template)
    - [Print Template](#print-template)
    - [Data Dictionary](#data-dictionary-1)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEC Legacy/ V*ist*A Enhancements supports several critical business processes associated with congressionally mandated initiatives. As a result of several veterans complaints concerning improper billing issues from the VHA representatives from both VHA and VBA, a meeting was held in 2002 to discuss creating a 5-Step Action Plan for Improving VBA/VHA Sharing of Information. The decision was made to replace the existing HINQ which accesses VBA’s BIRLS, and C&P databases with a new HINQ that would access the VBA Corporate Database. VBA has been developing the Corporate Database to replace its older systems, and will begin transitioning its C&P claims processing to it in 2006.

The HINQ Replacement Interim Solution software package provides the current HEC Legacy/V*ist*A systems with the ability to continue to operate while the VBA transfers to the new VBA corporate database.

It introduces the following functionality for VHA and VBA Data Sharing Strategy –Interim Solution:

- A new single IP address is added to capture all HINQ requests that are directed to the AAC. The HINQ messages are translated and transmitted between VistA and the VBA environments through the AAC interface.
- VBA has added up to 150 Service Connected (SC) Disabilities conditions to the HINQ response.
- VBA will provide additional information about each disability that is retrieved from its Corporate Database. The additional data includes effective dates and the extremity, when appropriate.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide functionality support to the VBA and VHA facilities. The architectural objective is to enable the current HEC Legacy/V*ist*A systems to continue operating uniformly while VBA transfers to their new VBA Corporate database without disrupting day to day operations. This document provides the user with current information about the new features, enhancements, and updates that have been added to the HEC Legacy/V*ist*A environments.

# Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                 |
|-------------|-----------------------------------------------------------------|
| Acronym | Description                                                 |
| AAC         | Austin Automation Center                                        |
| BIRLS       | Beneficiary Identification and Records Locator Subsystem        |
| CBO         | Chief Business Office                                           |
| C&P         | Compensation and Pension                                        |
| EDB         | Enrollment Data Base                                            |
| ESR         | Enrollment System Redesign                                      |
| HAC         | Health Administration Center                                    |
| HEC         | Health Eligibility Center                                       |
| HINQ        | Hospital Inquiry                                                |
| HL7         | Health Level Seven                                              |
| MVR         | Master Veteran Record                                           |
| NSC         | Non-Service-Connected                                           |
| P&T         | Permanent and Total Disability                                  |
| SC          | Service-Connected                                               |
| VA          | Department of Veterans Affairs                                  |
| VAMC        | VA Medical Center                                               |
| VBA         | Veterans Benefit Administration                                 |
| VHA         | Veterans Health Administration                                  |
| VistA       | Veterans Health Information Systems and Technology Architecture |

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                    |                                                                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term           | Definition                                                                                                                                                                                                                                      |
| BIRLS              | VBA’s central legacy repository for veteran demographic, military service, and claim data                                                                                                                                                           |
| Corporate Database | VBA’s new central repository for all veteran demographic, military service, benefit determination and payment data                                                                                                                                  |
| C&P                | The service within VBA that manages the compensation and pension benefit payment programs. The Compensation and Pension benefit payment system.                                                                                                     |
| EDB                | The redesigned HEC database                                                                                                                                                                                                                         |
| ESR                | The redesign of VHA eligibility and enrollment processes in accordance with the HealtheVet Architecture.                                                                                                                                            |
| HL7                | Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*ist*A HL7 package to assist in transporting data using this specification. |
| HEC Legacy System  | M-based database currently in use                                                                                                                                                                                                                   |
| HINQ, MINQ, BINQ   | VBA inquiry commands used in its legacy systems                                                                                                                                                                                                     |
| MVR                | A national data broker at the AAC that shares selected data in the form of messages as needed among the different VA organization                                                                                                                   |
| P&T                | A determination made by C&P Service; a criterion for pension eligibility                                                                                                                                                                            |

# User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Old HINQUP Field Display Options Removed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VBA is no longer sending the following data fields found in the HINQ response.

1.  Disability Indicator SC Disabilities.
2.  Combat Disability Indicator
3.  Additional Service
4.  Rated Disabilities Verified
5.  Entitlement Code – replaced by Type of Benefit
6.  Amount Social Security
7.  Other Annual Retirement- Payee
8.  Amount Other Annual Retirement – Payee
9.  Amount Other Annual Income – Payee
10. Amount Social Security - Spouse
11. Other Annual Retirement – Spouse
12. Amount Other Annual Retirement - Spouse
13. Amount Other Annual Income - Spouse
14. Amount Other Annual Retirement – Spouse
15. Master Record Type
16. Number SC Disabilities - calculated
17. Additional Disabilities
18. Hardship Expenses
19. Severance Recoupment
20. PFOP/FDIB
21. Consolidated Payment
22. Special Provision
23. Special Monthly Compensation
24. Diary Date
25. Diary Reason
26. Nursing Home Indicator
27. Competency Payment Factor
28. CHAMPVA Indicator
29. SSI

## HINQ Mail Message Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HINQ Mail Group that issues a mail message is normally displayed when an Individual HINQ is performed. This feature has been changed to no longer display the fields in the list above, except those that are now calculated. A new field, “Income for VA Purposes,” has been added to the mail message. Four new fields pertaining to the Disabilities are currently displayed, which consist of the following elements:

- Effective Date of Combined Evaluation. This applies for each individual Disability Extremity Involved (if appropriate).
- Original Effective Date
- Current Effective Date.

## Screen Options Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update HINQ to the Patient File option is used to enter HINQ data directly into the PATIENT file. Listed below are the screens, which have been modified to remove the fields, listed above.

## Screen 0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 0 is a verification screen only, to allow the user visibility to review and compare if a HINQ response, and the PATIENT file data is the same for the veteran who was selected. The change made to this scene reflects the following message that will appear when a patient is deceased:

“\*\*VBA indicates Patient is deceased. {Date}\*\*”

## Screen 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen provides the user the ability to enter veterans address information for the following fields: street address, city, state, zip code and county.

## Screen 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 2 contains the following data elements: Claim Number, Date of Birth, Sex, Date of Death, Incompetency Rating, POW Status, Claims Folder Location, and Unemployable Status.

## Screen 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 3 contains information on individual Service Connected Disabilities, the Combined Disability percent, Active Duty Training, Total Active Service and P&T. It includes the new Disability fields: Effective Date of Combined Evaluation, and for individual Disabilities Extremity (if appropriate), Original Effective Date and Current Effective Date.

### Screen 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen consists of data elements that are connected with a period of service. This feature lists all information that pertains to the following services: Entry Date, Discharge Date, Branch of Service, Character of Discharge and Service Number. Screen 4 can capture and list up to three periods of service at one given time.

### ## Screen 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays eligibility information for the following entities: Type of Benefit, Net Award Amount, Combined Percentage of Disability, Check Amount, Income for VA Purposes, and Aid and Attendance status.

Users should refer to documentation on V*ist*A U for examples of screens and further information REDACTED  
<span id="_Toc96334292" class="anchor"></span>Specific Requirements

## HINQ System Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New VBA Data Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new release utilizes the new VBA data set stored in the VBA's Corporate Database. Listed below are the following enhancements captured by this project:

### Up to 150 Service Connected (SC) codes and percents are returned and displayed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Up to 20 children are returned and displayed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Income for VA Purposes is displayed.

### Effective Date of Combined Evaluation, Extremity, Original Effective Date and Current Effective Date are displayed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Crossmapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously all crossmapping was processed through the HEC and MVR interface components by using two non-standard HL7 transactions. With the implementation of the HINQ Interim Solution enhancements, the new VBA data set is crossmapped by the AAC interface engine to the existing HINQ response, and the existing HL7 Z11 formats.

## Redirecting HINQ Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Formerly all requests were processed through one of the five VBA regional concentrators. However with the new single IP address all HINQ requests are addressed to one interface connection at the AAC. The data packet elements are then translated and transmitted between V*ist*A and the VBA system.

# Performance Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security and User Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing HINQ security requirements maintained in V*ist*A will not change. VBA is instituting a Common Security Service (CSS) access table in its database to keep track of authorized users. To ensure that all HINQ users receive access to the HINQ system the following requirements are listed below:

### All users are required to have a VBA BDN Password, and a V*ist*A HINQ security key (employee number).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A user is required to access HINQ at least once every 90 days to avoid the system locking them out.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### If a user has not accessed his/her HINQ account after 90 days an error code message will automatically appear preventing the user from accessing HINQ.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### In the event that a user is denied access at any time, the user is required to contact their VBA ISO coordinator.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All users are responsible for following-up with their VBA ISO coordinator in expediting all access requests.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All new and current employees are required to complete a VAF 20-8824e form and forward it to their VBA ISO coordinator to ensure access to the HINQ system. The application to request is called “Web HINQ.”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HINQ Users Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to maintain a high security environment for the HINQ system data we strongly suggest that access be granted only to those who will use HINQ on a regular basis.

## ## HINQ Employee Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is strongly suggested that once a user no longer needs access to the HINQ system, that the employee number should be deleted from the HINQ Employee Number field located in the NEW PERSON file. This will assist in eliminating any future or potential problems with duplications.

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical information related to the HINQ Replacement Interim Solution Phase 1 Enhancements found in the following Patches

DVB\*4.0\*49, DGBT\*1\*11 and DG\*5.3\*631 on VistA and IVMB\*2\*792 on the HEC Legacy system.

## New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HEC Legacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name                              | Field                 | Change | comment |
|--------------------------------------------|---------------------------|------------|-------------|
| VETERANS ID & VERIFICATION ACCESS (300.11) | P&T EFFECTIVE DATE (#8.3) | n/a        | New Field   |
| HEC ERROR PROCESSING PROJECT (742085)      | P&T EFFECTIVE DATE (#8.1) | n/a        | New Field   |

## VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Input Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME        | Input Template                                                                                  |
|-----------------|-----------------------------------------------------------------------------------------------------|
| MENU TEXT:  | \[DVBHINQ UPDATE\]                                                                              |
| DESCRIPTION | To eliminate the display and editing options of (Screen 6) changes were made to the Input template. |

### Print Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME        | Print Template                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------------------|
| MENU TEXT:  | \[DVBHINQ PAT-HINQ COMP\]                                                                          |
| DESCRIPTION | This template creates the report display for option \[DVB HUPLOAD PRINT\] Review Patient vs. HINQ Data |

### Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name        | Field             | Change                                                     | comment                                      |
|----------------------|-----------------------|----------------------------------------------------------------|--------------------------------------------------|
| HINQ Parameter (395) | RDPC IP Address (#22) | Pattern match changed from 15 characters to 14 – 15 characters | To accommodate new “10.nnn.nnn.nnn” IP addresses |