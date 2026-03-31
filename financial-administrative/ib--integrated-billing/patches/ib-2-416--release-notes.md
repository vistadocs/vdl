---
title: IB*2*416 Electronic Insurance Verification Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Electronic Insurance Verification
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*416
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - insurance
  - table
  - contents
  - patch
  - process
  - buffer
  - installation
  - patient
  - install
  - eligibility
page_count: 0
word_count: 2237
section_count: 16
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p416_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p416_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

Integrated Billing

eIV Phase 3 Iteration 1

Release Notes and Installation Guide

![](ib-2-416-electronic-insurance-verification-release-notes/001.png)

IB\*2\*416

September 2010

Department of Veterans AffairsVeterans Health Administration  

######## Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
  - [Patch IB\2\416 includes the following modifications](#patch-ib2416-includes-the-following-modifications)
    - [The eIV site parameters have been simplified](#the-eiv-site-parameters-have-been-simplified)
    - [Incoming 271 insurance coverage/eligibility/benefit data may now bypass the insurance buffer](#incoming-271-insurance-coverageeligibilitybenefit-data-may-now-bypass-the-insurance-buffer)
    - [Insurance Identification inquiries have been removed from service](#insurance-identification-inquiries-have-been-removed-from-service)
    - [Patient IDs and subscriber IDs will have all punctuation removed](#patient-ids-and-subscriber-ids-will-have-all-punctuation-removed)
  - [Patch IB\2\416 includes the following New Service Requests (NSRs)](#patch-ib2416-includes-the-following-new-service-requests-nsrs)
    - [- eIV Phase 3 Iteration 1](#eiv-phase-3-iteration-1)
  - [Patch IB\2\416 addresses the following Remedy Tickets](#patch-ib2416-addresses-the-following-remedy-tickets)
    - [Overview of Remedy Tickets](#overview-of-remedy-tickets)
  - [Documentation Retrieval](#documentation-retrieval)
  - [Test Sites](#test-sites)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
  - [Medicare (WNR) is now a valid insurance company](#medicare-wnr-is-now-a-valid-insurance-company)
  - [Much more of the 271 eligibility/benefit data will be stored](#much-more-of-the-271-eligibilitybenefit-data-will-be-stored)
  - [Additional eIV eligibility/benefit data will be displayed](#additional-eiv-eligibilitybenefit-data-will-be-displayed)
  - [The option 'Process Insurance Buffer' \[IBCN INSURANCE BUFFER PROCESS\] was enhanced](#the-option-process-insurance-buffer-ibcn-insurance-buffer-process-was-enhanced)
  - [Enhancements were made to several eIV-related reports](#enhancements-were-made-to-several-eiv-related-reports)
  - [The process to link VistA insurance companies was enhanced](#the-process-to-link-vista-insurance-companies-was-enhanced)
- [Technical Modifications](#technical-modifications)
  - [A. Files and Fields](#a-files-and-fields)
    - [Components Sent With Patch:](#components-sent-with-patch)
This patch contains electronic insurance verification (eIV) enhancements which are designed to improve the efficiency of the patient insurance verification process while reducing the workload of the insurance clerks. This is accomplished by direct, automatic updates to patient insurance information (bypassing the insurance buffer), by enhanced eIV reporting capabilities and enhanced user interface, and by including Medicare in the insurance verification process. In addition, VistA will now be able to receive, store, and display more eligibility and benefit information received from insurance companies.
Electronic insurance data is sent by payers and received by Austin FSC in an ANSI ASC X12.282 - Eligibility, Coverage, or Benefit Information (271) transaction set. This 271 data is converted to HL7 messages by Austin FSC and sent into VistA. When the 271 insurance data meets the requirements for the automatic updating of the patient's insurance, the insurance will be updated by the system when the HL7 transmission is received. This will eliminate the need for the insurance clerk to manually process this information. The time lag between the receipt of the transmission and the manual processing of the data will be eliminated. This functionality, plus the addition of Medicare to the eIV process, should significantly improve the quality and timeliness of the insurance data that is used to create claims for healthcare services provided to Veterans.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch IB\*2\*416 includes the following modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The eIV site parameters have been simplified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV site parameters as found in the option 'MCCR Site Parameter Display/Edit' \[IBJ MCCR SITE PARAMETERS\] have been simplified. The buffer and appointment data extracts are no longer editable and the “No Insurance” data extract has been removed from service.

### Incoming 271 insurance coverage/eligibility/benefit data may now bypass the insurance buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Incoming 271 insurance coverage/eligibility/benefit data may now bypass the insurance buffer and be filed directly to the patient insurance file if certain conditions are met.

### Insurance Identification inquiries have been removed from service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Insurance Identification inquiries have been removed from service. All of the electronic insurance transactions will now be insurance verification transactions. As a result, references to "IIV" have been changed to be "eIV" instead.

### Patient IDs and subscriber IDs will have all punctuation removed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient IDs and subscriber IDs will have all punctuation removed and will be converted into uppercase upon leaving VistA in the outbound HL7 insurance verification request messages. When the patient is the subscriber, the subscriber ID will be transmitted in the HL7 IN1 segment and no HL7 GT1 segment will be sent. When the patient is not the subscriber, the patient ID will be transmitted in the HL7 IN1 segment and the subscriber ID will be transmitted in the HL7 GT1 segment.

## Patch IB\*2\*416 includes the following New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### - eIV Phase 3 Iteration 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enables the business process to better align with the HIPAA electronic requirement, as well as the following: develop the ability of eIV transactions to bypass the buffer file and auto-update the insurance file, controllable by payer; push verified data returned by payers to all medical centers with record of patient; modify remote query to only return data on active coverage; modify eIV cache to function as the basis of a national insurance file. The request will meet the non-discretionary mandate that VHA implement the full HIPAA 270/271 transaction for Electronic Transactions under HIPAA.

Source: REDACTED Request ID# 20070582

## Patch IB\*2\*416 addresses the following Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HD287430 IBCNEKIT appears to violate SACC standards

HD063913 UNY-0504-10264 Error \<UNDEF(ECODE)\>DATA+10^IBCNERP3

### Overview of Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HD287430 IBCNEKIT appears to violate SACC standards

Problem

Routine IBCNEKIT calls vendor specific functions to enable and disable journaling during the eIV purge process. It also sets its own error trap so that journaling may be re-enabled in case it crashes. Differences between production systems and shadows may require database copies to re-sync the pairs.

Resolution

Remove all calls to disable journaling, local error trapping, and related code from routine IBCNEKIT.

#### HD063913 UNY-0504-10264 Error \<UNDEF(ECODE)\>DATA+10^IBCNERP3

Problem

Original IIV software used a utility called %XY^%RCR to merge global array data to/from local array data. There is a bug in this %XY^%RCR utility when two or more of the array subscripts contain a comma, which can produce an error detect in some IIV report software.

Resolution

Remove all references to the %XY^%RCR utility and replace with the standard MERGE command.

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

 

 1.  The preferred method is to FTP the files from REDACTED., which will transmit the files from the first available FTP server.
 2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

 

     Albany          [REDACTED](ftp://ftp.fo-albany.med.va.gov)

     Hines           [REDACTED](ftp://ftp.fo-hines.med.va.gov)

     Salt Lake City  [REDACTED](ftp://ftp.fo-slc.med.va.gov)
 3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address, <http://www.va.gov/vdl>.

 

The documentation distribution includes:

 

| FILE NAME     | DESCRIPTION |
|-------------------|-----------------|
| IB_2_P416_UM.PDF  | User Guide      |

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REDACTED

# Installation 

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before IB\*2\*416

> IB\*2\*284

> IB\*2\*316

> IB\*2\*377

> IB\*2\*399

> IB\*2\*400

> IB\*2\*411

> IB\*2\*413

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Post-Install routine is automatically deleted after this patch is installed.

The Post-Install routine re-sets all of the eIV parameter values to the new default settings, re-names some system entities to be "eIV" instead of "IIV", activates and links the MEDICARE WNR payer with the MEDICARE (WNR) insurance company.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that this patch be installed outside of normal working hours when no Integrated Billing users are on the system. However, if installed during the normal workday, it is recommended that the following selections in the OPTION (#19) file, and all of their descendants be disabled to prevent possible conflicts while running the KIDS Install. Other VISTA users will not be affected.

Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

MCCR Site Parameter Display/Edit \[IBJ MCCR SITE PARAMETERS\]

Insurance Company Entry/Edit \[IBCN INSURANCE CO EDIT\]

Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]

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

*3. Select Installation Option*

> **NOTE:** The following are OPTIONAL - (When prompted for the INSTALL NAME, enter IB\*2.0\*416):

a\. Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

*4. Select Installation Option: Install Package(s)*

\*\*This is the step to start the installation of this KIDS patch:

a\. Choose the Install Package(s) option to start the patch install.

b\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer YES, unless your system does this in a nightly TaskMan process.

c\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO

d\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer YES if installing during working hours.

e\. When prompted 'Enter options you wish to mark as 'Out Of Order':' Enter the following options:

Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

MCCR Site Parameter Display/Edit \[IBJ MCCR SITE PARAMETERS\]

Insurance Company Entry/Edit \[IBCN INSURANCE CO EDIT\]

Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]

f\. When prompted 'Enter protocols you wish to mark as 'Out Of Order':' press \<return\>.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Medicare (WNR) is now a valid insurance company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medicare (WNR) is now a valid insurance company for the eIV process.

## Much more of the 271 eligibility/benefit data will be stored

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Much more of the 271 eligibility/benefit data will be stored in the eIV Response file (file# 365) and also in corresponding fields in the patient INSURANCE TYPE sub-file (sub-file# 2.312).

## Additional eIV eligibility/benefit data will be displayed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional eIV eligibility/benefit data will be displayed in the Insurance Buffer, Patient Insurance, Claims Tracking, Third Party Joint Inquiry, and in the billing screens with the ?INX special help action.

## The option 'Process Insurance Buffer' \[IBCN INSURANCE BUFFER PROCESS\] was enhanced

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option 'Process Insurance Buffer' \[IBCN INSURANCE BUFFER PROCESS\] was enhanced by the addition of several new insurance buffer data views for positive responses, negative responses, Medicare buffer entries, and future appointment buffer entries.

## Enhancements were made to several eIV-related reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements were made to several eIV-related reports and one new eIV report was added.

## The process to link VistA insurance companies was enhanced

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process to link VistA insurance companies to VistA eIV payers in the option 'Link Insurance Companies to Payers' \[IBCNE PAYER LINK\] was enhanced to allow the user to link multiple insurance companies to a payer at one time.

# Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Components Sent With Patch:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of files included in this patch

| FILE \# | NAME                    | UP DATE DD | SEND SEC. CODE | DATA COMES W/FILE | SITE DATA | RSLV PTS |
|-------------|-----------------------------|----------------|--------------------|-----------------------|---------------|--------------|
| 2           | PATIENT                     | YES            | YES                | NO                    |               |              |
| 350.9       | IB SITE PARAMETERS          | YES            | YES                | NO                    |               |              |
| 355.33      | INSURANCE BUFFER            | YES            | YES                | NO                    |               |              |
| 365         | IIV RESPONSE                | YES            | YES                | NO                    |               |              |
| 365.011     | X12 271 ELIGIBILITY/BENEFIT | YES            | YES                | YES                   | OVER          | NO           |
| 365.013     | X12 271 SERVICE TYPE        | YES            | YES                | YES                   | OVER          | NO           |
| 365.014     | X12 271 INSURANCE TYPE      | YES            | YES                | YES                   | OVER          | NO           |
| 365.016     | X12 271 QUANTITY QUALIFIER  | YES            | YES                | YES                   | OVER          | NO           |
| 365.022     | X12 271 ENTITY ID CODE      | YES            | YES                | YES                   | OVER          | NO           |
| 365.023     | X12 271 ID QUAL             | YES            | YES                | YES                   | OVER          | NO           |
| 365.024     | X12 271 PROVIDER CODE       | YES            | YES                | YES                   | OVER          | NO           |
| 365.025     | X12 271 DELIVERY FREQ CODE  | YES            | YES                | YES                   | OVER          | NO           |
| 365.026     | X12 271 DATE QUALIFIER      | YES            | YES                | YES                   | OVER          | NO           |
| 365.028     | X12 271 REF IDENTIFICATION  | YES            | YES                | YES                   | OVER          | NO           |
| 365.1       | IIV TRANSMISSION QUEUE      | YES            | YES                | NO                    |               |              |
| 365.12      | PAYER                       | YES            | YES                | NO                    |               |              |
| 365.15      | IIV STATUS TABLE            | NO             | YES                | YES                   | OVER          | YES          |

The following is a list of fields included in this patch

| Field Name (Number)           | File Name (Number)                |
|-----------------------------------|---------------------------------------|
| DATE LAST EDITED (1.05)           | INSURANCE TYPE (sub-file) (2.312)     |
| EIV AUTO-UPDATE (4.04)            | INSURANCE TYPE (sub-file) (2.312)     |
| \*\*\*ALL SUBFIELDS\*\*\*         | ELIGIBIL/BENEFIT (sub-file) (2.322)   |
| DAILY MAILMAN MSG (51.02)         | IB SITE PARAMETERS (350.9)            |
| DAILY MSG TIME (51.03)            | IB SITE PARAMETERS (350.9)            |
| MESSAGES MAILGROUP (51.04)        | IB SITE PARAMETERS (350.9)            |
| NUMBER RETRIES (51.06)            | IB SITE PARAMETERS (350.9)            |
| HL7 RESPONSE PROCESSING (51.13)   | IB SITE PARAMETERS (350.9)            |
| HL7 START TIME (51.14)            | IB SITE PARAMETERS (350.9)            |
| HL7 MAXIMUM NUMBER (51.15)        | IB SITE PARAMETERS (350.9)            |
| HL7 STOP TIME (51.19)             | IB SITE PARAMETERS (350.9)            |
| FAILURE MAILMAN MSG (51.2)        | IB SITE PARAMETERS (350.9)            |
| REGISTRATION COMPLETE (51.22)     | IB SITE PARAMETERS (350.9)            |
| MEDICARE PAYER (51.25)            | IB SITE PARAMETERS (350.9)            |
| \*\*\*ALL SUBFIELDS\*\*\*         | BATCH EXTRACTS (sub-file) (350.9002)  |
| SUBSCRIBER ADDRESS LINE 1 (62.02) | INSURANCE BUFFER (355.33)             |
| SUBSCRIBER ADDRESS LINE 2 (62.03) | INSURANCE BUFFER (355.33)             |
| SUBSCRIBER ADDRESS CITY (62.04)   | INSURANCE BUFFER (355.33)             |
| SUBSCRIBER ADDRESS STATE (62.05)  | INSURANCE BUFFER (355.33)             |
| SUBSCRIBER ADDRESS ZIP (62.06)    | INSURANCE BUFFER (355.33)             |
| PT RELATIONSHIP TO INSURED (1.09) | IIV RESPONSE (365)                    |
| SUBSCRIBER ADDRESS LINE 1 (5.01)  | IIV RESPONSE (365)                    |
| SUBSCRIBER ADDRESS LINE 2 (5.02)  | IIV RESPONSE (365)                    |
| SUBSCRIBER ADDRESS CITY (5.03)    | IIV RESPONSE (365)                    |
| SUBSCRIBER ADDRESS STATE (5.04)   | IIV RESPONSE (365)                    |
| SUBSCRIBER ADDRESS ZIP (5.05)     | IIV RESPONSE (365)                    |
| \*\*\*ALL SUBFIELDS\*\*\*         | ELIGIBLT/BENEFIT (sub-file) (365.02)  |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 ELIGIBILITY/BENEFIT (365.011) |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 SERVICE TYPE (365.013)        |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 INSURANCE TYPE (365.014)      |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 QUANTITY QUALIFIER (365.016)  |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 ENTITY ID CODE (365.022)      |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 IDENT QUAL (365.023)          |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 PROVIDER CODE (365.024)       |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 DELIVERY FREQ CODE (365.025)  |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 DATE QUALIFIER (365.026)      |
| \*\*\*FULL DD BEING SENT\*\*\*    | X12 271 REF IDENTIFICATION (365.028)  |
| WHICH EXTRACT (.1)                | IIV TRANSMISSION QUEUE (365.1)        |
| HL7 PATIENT ID FIELD (.19)        | IIV TRANSMISSION QUEUE (365.1)        |
| \*\*\*ALL SUBFIELDS\*\*\*         | ACTIVE FLAG LOG (sub-file)(365.1212)  |
| \*\*\*ALL SUBFIELDS\*\*\*         | TRUSTED FLAG LOG(sub-file)(365.1213)  |

The following is a list of templates included in this patch

| Template Name            | Type | File Name (Number)     |
|------------------------------|----------|----------------------------|
| IBCNE GENERAL PARAMETER EDIT | INPUT    | IB SITE PARAMETERS (350.9) |

The following is a list of protocols included in this patch

| Protocol                          | Action   |
|---------------------------------------|--------------|
| IBCNB ENTRY EDIT ALL                  | SEND TO SITE |
| IBCNB ENTRY EDIT GROUP                | SEND TO SITE |
| IBCNB ENTRY EDIT INSURANCE            | SEND TO SITE |
| IBCNB ENTRY EDIT POLICY               | SEND TO SITE |
| IBCNB ENTRY RESPONSE REPORT           | SEND TO SITE |
| IBCNB ENTRY SCREEN MENU               | SEND TO SITE |
| IBCNB ENTRY VERIFY                    | SEND TO SITE |
| IBCNB EXPAND BENEFITS                 | SEND TO SITE |
| IBCNB FAST EXIT                       | SEND TO SITE |
| IBCNB LIST ADD                        | SEND TO SITE |
| IBCNB LIST APPOINTMENTS VIEW          | SEND TO SITE |
| IBCNB LIST CHECK NAMES                | SEND TO SITE |
| IBCNB LIST ENTRY SCREEN               | SEND TO SITE |
| IBCNB LIST MEDICARE VIEW              | SEND TO SITE |
| IBCNB LIST NEGATIVE VIEW              | SEND TO SITE |
| IBCNB LIST POSITIVE VIEW              | SEND TO SITE |
| IBCNB LIST PROCESS SCREEN             | SEND TO SITE |
| IBCNB LIST REJECT                     | SEND TO SITE |
| IBCNB LIST SCREEN MENU                | SEND TO SITE |
| IBCNB LIST SORT                       | SEND TO SITE |
| IBCNB PROCESS ACCEPT                  | SEND TO SITE |
| IBCNB PROCESS COMPARE/EDIT            | SEND TO SITE |
| IBCNB PROCESS ENTRY SCREEN            | SEND TO SITE |
| IBCNB PROCESS REJECT                  | SEND TO SITE |
| IBCNB PROCESS SCREEN MENU             | SEND TO SITE |
| IBCNB PROCESS TOGGLE                  | SEND TO SITE |
| IBCNE AB VIEW EXP ELIG BEN SCREEN     | SEND TO SITE |
| IBCNE ELIG BEN INFO MENU              | SEND TO SITE |
| IBCNE FAST EXIT                       | SEND TO SITE |
| IBCNE JT COVERAGE LIMIT DATE RANGE    | SEND TO SITE |
| IBCNE JT VIEW EXP ELIG BEN SCREEN     | SEND TO SITE |
| IBCNE PAYER EXIT                      | SEND TO SITE |
| IBCNE PAYER EXPAND                    | SEND TO SITE |
| IBCNE PAYER EXPAND MENU               | SEND TO SITE |
| IBCNE PAYER LINK                      | SEND TO SITE |
| IBCNE PAYER MAINT MENU                | SEND TO SITE |
| IBCNE SJ COVERAGE LIMIT DATE RANGE    | SEND TO SITE |
| IBCNE SP COVERAGE LIMIT DATE RANGE    | SEND TO SITE |
| IBCNE SV VIEW EXP ELIG BEN SCREEN     | SEND TO SITE |
| IBCNE VP VIEW EXP ELIG BEN SCREEN     | SEND TO SITE |
| IBCNS EXIT                            | SEND TO SITE |
| IBCNS QUIT                            | SEND TO SITE |
| IBCNSA AN BEN CH YR                   | SEND TO SITE |
| IBCNSA AN BEN ED ALL                  | SEND TO SITE |
| IBCNSA AN BEN HOME HEA                | SEND TO SITE |
| IBCNSA AN BEN HOSPC                   | SEND TO SITE |
| IBCNSA AN BEN INPT                    | SEND TO SITE |
| IBCNSA AN BEN IV MGMT                 | SEND TO SITE |
| IBCNSA AN BEN MEN H                   | SEND TO SITE |
| IBCNSA AN BEN OPT                     | SEND TO SITE |
| IBCNSA AN BEN POL INF                 | SEND TO SITE |
| IBCNSA AN BEN REHAB                   | SEND TO SITE |
| IBCNSA ANNUAL BENEFITS                | SEND TO SITE |
| IBCNSC PLAN DETAIL                    | SEND TO SITE |
| IBCNSJ CHANGE PLAN                    | SEND TO SITE |
| IBCNSJ EDIT COVERAGE LIMITS           | SEND TO SITE |
| IBCNSJ EDIT PLAN INFO                 | SEND TO SITE |
| IBCNSJ INACTIVATE PLAN                | SEND TO SITE |
| IBCNSJ INS CO EDIT COVERAGE LIMITS    | SEND TO SITE |
| IBCNSJ INS CO INACTIVATE PLAN         | SEND TO SITE |
| IBCNSJ PLAN COMMENT                   | SEND TO SITE |
| IBCNSJ PLAN UR INFO                   | SEND TO SITE |
| IBCNSJ SWITCH PLANS                   | SEND TO SITE |
| IBCNSJ UPDATE ANNUAL BENEFITS         | SEND TO SITE |
| IBCNSM ADD POLICY                     | SEND TO SITE |
| IBCNSM BENEFITS USED                  | SEND TO SITE |
| IBCNSM CHANGE PATIENT                 | SEND TO SITE |
| IBCNSM DELETE POLICY                  | SEND TO SITE |
| IBCNSM EDIT ALL                       | SEND TO SITE |
| IBCNSM PATIENT INSURANCE              | SEND TO SITE |
| IBCNSM PERSONAL RIDERS                | SEND TO SITE |
| IBCNSM PRINT PATIENT INS              | SEND TO SITE |
| IBCNSM PRINT WORKSHEET                | SEND TO SITE |
| IBCNSM UPDATE ANNUAL BENEFITS         | SEND TO SITE |
| IBCNSM VERIFY INS                     | SEND TO SITE |
| IBCNSM VIEW PAT POLICY                | SEND TO SITE |
| IBCNSP ADD COMMENT                    | SEND TO SITE |
| IBCNSP ANNUAL BENEFITS                | SEND TO SITE |
| IBCNSP BENEFITS USED                  | SEND TO SITE |
| IBCNSP EDIT ALL                       | SEND TO SITE |
| IBCNSP EDIT EFFECTIVE DATES           | SEND TO SITE |
| IBCNSP EDIT POLICY INFO               | SEND TO SITE |
| IBCNSP EMPLOYER INFO FOR CLAIMS       | SEND TO SITE |
| IBCNSP INSURANCE CONTACT INF          | SEND TO SITE |
| IBCNSP POLICY MENU                    | SEND TO SITE |
| IBCNSP SUBSCRIBER UPDATE              | SEND TO SITE |
| IBCNSP UR INFO                        | SEND TO SITE |
| IBCNSP VERIFY COVERAGE                | SEND TO SITE |
| IBCNSV ANNUAL BENEFITS                | SEND TO SITE |
| IBCNSV PATIENT INSURANCE              | SEND TO SITE |
| IBCNSV POLICY MENU                    | SEND TO SITE |
| IBCNSV VIEW AN BEN                    | SEND TO SITE |
| IBCNSV VIEW BEN USED                  | SEND TO SITE |
| IBCNSV VIEW EXP POL                   | SEND TO SITE |
| IBJ EXIT                              | SEND TO SITE |
| IBJP IIV BATCH EXTRACT EDIT           | SEND TO SITE |
| IBJP IIV GENERAL EDIT                 | SEND TO SITE |
| IBJP INS VER MENU                     | SEND TO SITE |
| IBJP INS VER SCREEN                   | SEND TO SITE |
| IBJT ACTIVE LIST SCREEN SKIP          | SEND TO SITE |
| IBJT AR ACCOUNT PROFILE SCREEN        | SEND TO SITE |
| IBJT AR COMMENT HISTORY SCREEN        | SEND TO SITE |
| IBJT BILL CHARGES SCREEN              | SEND TO SITE |
| IBJT BILL DX SCREEN                   | SEND TO SITE |
| IBJT BILL PROCEDURES SCREEN           | SEND TO SITE |
| IBJT CHANGE BILL                      | SEND TO SITE |
| IBJT CLAIM SCREEN MENU                | SEND TO SITE |
| IBJT CLAIM SCREEN SKIP                | SEND TO SITE |
| IBJT CT/IR COMMUNICATIONS LIST SCREEN | SEND TO SITE |
| IBJT EDI STATUS SCREEN                | SEND TO SITE |
| IBJT HS HEALTH SUMMARY                | SEND TO SITE |
| IBJT NS VIEW AN BEN MENU              | SEND TO SITE |
| IBJT NS VIEW AN BEN REDISPLAY         | SEND TO SITE |
| IBJT NS VIEW AN BEN SCREEN            | SEND TO SITE |
| IBJT NS VIEW EXP POL MENU             | SEND TO SITE |
| IBJT NS VIEW EXP POL REDISPLAY        | SEND TO SITE |
| IBJT NS VIEW EXP POL SCREEN           | SEND TO SITE |
| IBJT NS VIEW INS CO SCREEN            | SEND TO SITE |
| IBJT PT ELIGIBILITY SCREEN            | SEND TO SITE |
| VALM BLANK 1                          | SEND TO SITE |
| VALM PRINT LIST                       | SEND TO SITE |

The following is a list of List Templates included in this patch

| List Template              | Action   |
|--------------------------------|--------------|
| IBCNB INSURANCE BUFFER LIST    | SEND TO SITE |
| IBCNE ELIGIBILITY/BENEFIT INFO | SEND TO SITE |
| IBCNE REQUEST INS INQUIRY LIST | SEND TO SITE |
| IBCNS EXPANDED POLICY          | SEND TO SITE |
| IBCNS INS CO PLAN DETAIL       | SEND TO SITE |
| IBJP IIV SITE PARAMETERS       | SEND TO SITE |
| IBJT CLAIM INFO                | SEND TO SITE |

The following is a list of Options included in this patch

| Option                     | Type     |
|--------------------------------|--------------|
| IBCNE AUTO MATCH BUFFER        | SEND TO SITE |
| IBCNE AUTO MATCH ENTER/EDIT    | SEND TO SITE |
| IBCNE EIV UPDATE REPORT        | SEND TO SITE |
| IBCNE IIV AMBIGUOUS POLICY RPT | SEND TO SITE |
| IBCNE IIV BATCH PROCESS        | SEND TO SITE |
| IBCNE IIV INACTIVE POLICY RPT  | SEND TO SITE |
| IBCNE IIV MENU                 | SEND TO SITE |
| IBCNE IIV PAYER LINK REPORT    | SEND TO SITE |
| IBCNE IIV PAYER REPORT         | SEND TO SITE |
| IBCNE IIV RESPONSE REPORT      | SEND TO SITE |
| IBCNE IIV STATISTICAL REPORT   | SEND TO SITE |
| IBCNE POTENTIAL NEW INS FOUND  | SEND TO SITE |
| IBCNE PURGE IIV DATA           | SEND TO SITE |
| IBCNE REQUEST INQUIRY          | SEND TO SITE |

Routine Information:

The second line of each of these routines now looks like:

 ;;2.0;INTEGRATED BILLING;\*\*\[Patch List\]\*\*;21-MAR-94;Build 58

The checksums below are new checksums, and  can be checked with CHECK1^XTSUMBLD.

| Routine | Checksum Before | Checksum After | Patch List                                 |
|-------------|---------------------|--------------------|------------------------------------------------|
| IBCNBAA     | B59752666           | B67963575          | \*\*82,184,246,416\*\*                         |
| IBCNBAR     | B41255372           | B44012684          | \*\*82,240,345,413,416\*\*                     |
| IBCNBCD     | B35866486           | B84472806          | \*\*82,251,361,371,416\*\*                     |
| IBCNBEE     | B44866934           | B45989984          | \*\*82,184,252,251,356,361,371,377,416\*\*     |
| IBCNBLA     | B65200465           | B65832730          | \*\*82,149,153,184,271,416\*\*                 |
| IBCNBLA1    | B76644494           | B77705604          | \*\*82,133,149,184,252,271,416\*\*             |
| IBCNBLB     | n/a                 | B1130107           | \*\*416\*\*                                    |
| IBCNBLE     | B69021746           | B77550797          | \*\*82,231,184,251,371,416\*\*                 |
| IBCNBLE1    | B27903709           | B27906815          | \*\*184,271,416\*\*                            |
| IBCNBLL     | B58797432           | B90593913          | \*\*82,149,153,183,184,271,345,416\*\*         |
| IBCNBMI     | B80184806           | B85358524          | \*\*82,184,246,251,299,345,361,371,413,416\*\* |
| IBCNEBF     | B29002877           | B36248866          | \*\*184,271,361,371,416\*\*                    |
| IBCNEDE     | B21001833           | B20320433          | \*\*184,271,300,416\*\*                        |
| IBCNEDE1    | B33576444           | B37016330          | \*\*184,271,416\*\*                            |
| IBCNEDE2    | B63218575           | B58601408          | \*\*184,271,249,345,416\*\*                    |
| IBCNEDE3    | B51661172           | B57677467          | \*\*184,271,416\*\*                            |
| IBCNEDE4    | B79553596           | B81971988          | \*\*184,271,416\*\*                            |
| IBCNEDE5    | B30882453           | B26929333          | \*\*184,271,416\*\*                            |
| IBCNEDE6    | B30305878           | B32927570          | \*\*184,271,345,416\*\*                        |
| IBCNEDE7    | B21406402           | B24335491          | \*\*271,416\*\*                                |
| IBCNEDEP    | B95024002           | B83667847          | \*\*184,271,300,416\*\*                        |
| IBCNEDEQ    | B27345351           | B27902088          | \*\*184,271,300,416\*\*                        |
| IBCNEHL1    | B32996551           | B225142720         | \*\*300,345,416\*\*                            |
| IBCNEHL2    | B48625538           | B53025337          | \*\*300,345,416\*\*                            |
| IBCNEHL3    | B72666983           | B72667613          | \*\*300,416\*\*                                |
| IBCNEHL4    | B25894966           | B96805218          | \*\*300,416\*\*                                |
| IBCNEHLI    | B8071384            | B8196060           | \*\*184,252,251,271,300,416\*\*                |
| IBCNEHLM    | B21111301           | B21127175          | \*\*184,251,300,416\*\*                        |
| IBCNEHLQ    | B42736526           | B38577924          | \*\*184,271,300,361,416\*\*                    |
| IBCNEHLT    | B69606344           | B77352947          | \*\*184,251,271,300,416\*\*                    |
| IBCNEHLU    | B16427486           | B30725766          | \*\*184,300,416\*\*                            |
| IBCNEKI2    | B9265324            | B9273638           | \*\*271,316,416\*\*                            |
| IBCNEKIT    | B77702012           | B54158297          | \*\*184,271,316,416\*\*                        |
| IBCNEPM1    | B17662698           | B31433472          | \*\*184,416\*\*                                |
| IBCNEPY     | B21965484           | B17186468          | \*\*184,416\*\*                                |
| IBCNEQU     | B85417611           | B82573317          | \*\*184,271,416\*\*                            |
| IBCNERP0    | B5712540            | B5707694           | \*\*184,271,416\*\*                            |
| IBCNERP1    | B76118662           | B79692188          | \*\*184,271,416\*\*                            |
| IBCNERP2    | B33851537           | B30801647          | \*\*184,271,416\*\*                            |
| IBCNERP3    | B33550221           | B28161597          | \*\*184,271,416\*\*                            |
| IBCNERP4    | B61874953           | B61656289          | \*\*184,271,300,416\*\*                        |
| IBCNERP5    | B48772624           | B43579817          | \*\*184,271,300,416\*\*                        |
| IBCNERP6    | B76775707           | B74223457          | \*\*184,271,416\*\*                            |
| IBCNERP7    | B26918279           | B26715367          | \*\*184,416\*\*                                |
| IBCNERP8    | B55076349           | B66453982          | \*\*184,271,345,416\*\*                        |
| IBCNERP9    | B85343498           | B102330381         | \*\*184,271,416\*\*                            |
| IBCNERPA    | B29790461           | B6564371           | \*\*184,271,345,416\*\*                        |
| IBCNERPB    | B47281674           | B47288196          | \*\*184,252,271,416\*\*                        |
| IBCNERPC    | B46100582           | B46095484          | \*\*184,252,271,416\*\*                        |
| IBCNERPD    | B45776123           | B44163811          | \*\*184,252,416\*\*                            |
| IBCNERPE    | B68650966           | B36361133          | \*\*271,300,416\*\*                            |
| IBCNERPF    | n/a                 | B16361185          | \*\*416\*\*                                    |
| IBCNERPG    | n/a                 | B15534927          | \*\*416\*\*                                    |
| IBCNERPH    | n/a                 | B19008482          | \*\*416\*\*                                    |
| IBCNES      | n/a                 | B24997316          | \*\*416\*\*                                    |
| IBCNES1     | n/a                 | B103884237         | \*\*416\*\*                                    |
| IBCNES2     | n/a                 | B9476079           | \*\*416\*\*                                    |
| IBCNEUT2    | B2641881            | B2594683           | \*\*184,416\*\*                                |
| IBCNEUT3    | B58297927           | B56842259          | \*\*184,252,271,416\*\*                        |
| IBCNEUT4    | B50608524           | B50167663          | \*\*184,271,345,416\*\*                        |
| IBCNEUT5    | B60224642           | B57334702          | \*\*184,284,271,416\*\*                        |
| IBCNEUT8    | B7469707            | B5629329           | \*\*184,416\*\*                                |
| IBCNICB     | B105382395          | B106011881         | \*\*413,416\*\*                                |
| IBCNS3      | B55507373           | B62573337          | \*\*287,399,416\*\*                            |
| IBCNSC01    | B55064562           | B53646224          | \*\*52,137,191,184,232,320,349,371,399,416\*\* |
| IBCNSC4     | B17390042           | B17661433          | \*\*43,85,103,251,416\*\*                      |
| IBCNSC41    | B8406316            | B9252371           | \*\*43,416\*\*                                 |
| IBCNSP      | B42668156           | B42954824          | \*\*6,28,43,52,85,251,363,371,416\*\*          |
| IBCNSP01    | B32701738           | B33683555          | \*\*43,52,85,251,371,377,416\*\*               |
| IBCNSU1     | B18337578           | B18872542          | \*\*103,133,244,371,416\*\*                    |
| IBJPI       | B59509234           | B20701382          | \*\*184,271,316,416\*\*                        |
| IBJPI2      | B18769415           | B5452535           | \*\*184,271,316,416\*\*                        |
| IBJPM       | B11055331           | B10531686          | \*\*39,137,184,271,316,416\*\*                 |
| IBY416PO    | n/a                 | B137314065         | \*\*416\*\*                                    |

Routine list of preceding patches: 316, 377, 399, 413