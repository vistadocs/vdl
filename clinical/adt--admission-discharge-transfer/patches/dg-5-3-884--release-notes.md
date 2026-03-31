---
title: DG*5.3*884 ICD-10 PTF Modifications Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10 PTF Modifications
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*884
group_key: "ADT:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - codes
  - associated
  - diagnosis
  - record
  - census
  - span
  - manual
  - patch
page_count: 0
word_count: 2874
section_count: 26
table_count: 15
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/dg_5_3_884_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/dg_5_3_884_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

---
title: |
  ICD-10 PTF Modifications

  Admission, Discharge, Transfer (ADT)

  DG\*5.3\*884

  Release Notes
---

![](dg-5-3-884-icd-10-ptf-modifications-release-notes/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

| Date           | Version | Description                                                                         | Author                                    |
|----------------|---------|-------------------------------------------------------------------------------------|-------------------------------------------|
| September 2015 | 1.0     | Baseline document, created for ICD-10 PTF Modifications project patch DG\*5.3\*884. | VA OI&T PD, ICD-10 PTF Modifications Team |

<span id="_Toc428467126" class="anchor"></span>Table : Fields Modified by DG\*5.3\*884

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Software Disclaimer](#software-disclaimer)
  - [Documentation Disclaimer](#documentation-disclaimer)
  - [Required Patches](#required-patches)
  - [Installation Instructions](#installation-instructions)
  - [Updated Documentation](#updated-documentation)
- [Enhancements](#enhancements)
  - [Increase Diagnosis Codes and POA Indicators in 501 Transactions](#increase-diagnosis-codes-and-poa-indicators-in-501-transactions)
  - [Increase Procedure Codes in 401 Transactions](#increase-procedure-codes-in-401-transactions)
  - [Increase Procedure Codes in 601 Transactions](#increase-procedure-codes-in-601-transactions)
  - [Increase Diagnosis Codes and POA Indicators in 701 Transactions](#increase-diagnosis-codes-and-poa-indicators-in-701-transactions)
  - [Display ICD-10 Codes and POA Indicators on 501, 401, 601, and 701 Screens](#display-icd-10-codes-and-poa-indicators-on-501-401-601-and-701-screens)
  - [Calculate the Diagnosis Related Groups](#calculate-the-diagnosis-related-groups)
  - [Modify PTF MailMan Message to Transmit More ICD-10 Codes](#modify-ptf-mailman-message-to-transmit-more-icd-10-codes)
- [Fixes and Other Changes](#fixes-and-other-changes)
  - [Delete POA Indicator when Associated Diagnosis is Deleted](#delete-poa-indicator-when-associated-diagnosis-is-deleted)
  - [Prevent Population of POA if Associated Diagnosis is Not Present](#prevent-population-of-poa-if-associated-diagnosis-is-not-present)
  - [Allow Duplicate ICD Codes for 401 Surgeries and 601 Procedures](#allow-duplicate-icd-codes-for-401-surgeries-and-601-procedures)
  - [Entry of Gender-specific ICD Codes](#entry-of-gender-specific-icd-codes)
- [Associated Files and Fields](#associated-files-and-fields)
  - [Modified Fields](#modified-fields)
  - [New Fields](#new-fields)
- [Associated Forms](#associated-forms)
- [Associated Mail Groups](#associated-mail-groups)
- [Associated Menu Listings](#associated-menu-listings)
- [Modified Reports](#modified-reports)
- [Associated Protocols](#associated-protocols)
- [Associated Security Keys](#associated-security-keys)
- [Associated Templates](#associated-templates)
  - [Modified Templates](#modified-templates)
  - [New Templates](#new-templates)
- [Integration Control Registrations (ICRs)](#integration-control-registrations-icrs)
  - [Modified ICRs](#modified-icrs)
  - [New ICRs](#new-icrs)
- [Other Database Changes](#other-database-changes)
  - [New Error Codes Added to PTF AUSTIN ERROR CODES (#45.64)](#new-error-codes-added-to-ptf-austin-error-codes-4564)
- [New Service Requests](#new-service-requests)
- [Patient Safety Issues](#patient-safety-issues)
- [Remedy Tickets](#remedy-tickets)
- [Known Issues](#known-issues)
Veterans Health Administration (VHA) software remediation for the International Classification of Diseases, Tenth Revision (ICD-10) enabled the transition to support the use of ICD-10 code sets. ICD-10-CM will replace ICD-9-CM as the diagnostic coding system, and ICD-10-PCS will replace ICD-9-CM as the procedural coding system. The ICD-10 Patient Treatment File (PTF) Modifications project will increase the maximum allowable codes in the entry, display, lookup, view, print, storage, and transmission of the ICD-10 code sets in the Veterans Health Information Systems and Technology Architecture (VistA) legacy and Health*<u>e</u>*Vet systems. Effective as of the ICD-10 activation date, VHA will be able to utilize the ICD-10 code sets to include the increased number of diagnosis and procedures which can be recorded in its day-to-day operations (e.g. entry, display, lookup, print, storage, internal and/or external transmission) for inpatient episodes of care with discharges on or after this date.
The ICD-10 PTF Modifications project supports the expansion of the number of ICD-10 Diagnosis, Present on Admission (POA) indicators, and Procedure and Surgical codes that may be contained in a patient treatment record. This patch introduces additional ICD-10 implementation-related modifications into the VistA Registration V5.3 package. The enhancements being made support the existing business processes in the Admission Discharge Transfer (ADT) and PTF modules. The user will now be able to enter up to 25 ICD-10 diagnosis codes with their associated POA indicators in each Movement (501) screen and in the Discharge (701) screen of a patient treatment record. The user will also be able to enter up to 25 ICD-10 procedure codes in each Surgical Episode (401) screen and in each Non-OR Procedure (601) screen.
The ICD-10 PTF Modifications project is comprised of six patches, which are being released within a single KIDS host file:
- Admission, Discharge, Transfer (ADT), DG\*5.3\*884
- CPRS: Health Summary (HS), GMTS\*2.7\*111
- Integrated Billing (IB), IB\*2.0\*522
- Laboratory: Anatomic Pathology (AP) and Laboratory: Emerging Pathogens Initiative (EPI), LR\*5.2\*442
- CPRS: Order Entry/Results Reporting (OE/RR), OR\*3.0\*406
- Clinical Case Registries (CCR), ROR\*1.5\*25

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to highlight enhancements and changes to the ADT package related to the ICD-10 PTF Modifications project contained in patch DG\*5.3\*884.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the VistA ADT product and applies primarily to the changes made between this newest release and previous release packages of the software.

The intended audience for this document includes users of VistA ADT application and users of the PTF module.

## Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105, of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

## Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before patch DG\*5.3\*884:

- DG\*5.3\*850
- DG\*5.3\*862
- DG\*5.3\*867
- DG\*5.3\*898
- DG\*5.3\*905
- XM\*999\*179

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information regarding the installation of this software, please refer to the ICD-10 PTF Modifications Installation Guide on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=55>.

## Updated Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ADT manuals are posted on the VDL website: [http://www.va.gov/vdl/](http://www.va.gov/vdl/application.asp?appid=55) .

The following ADT documents have been updated for DG\*5.3\*884:

- ICD-10 PTF Modifications Installation Guide
- ICD-10 PTF Modifications ADT DG\*5.3\*884 Release Notes
- PIMS Technical Manual (Patient Information Management System (PIMS) Patient Registration, Admission, Discharge, Transfer, and Appointment Scheduling Technical Manual)
- User Manual – PTF Menu (PIMS V. 5.3 ADT Module User Manual: PTF Menu)

The Clinical Reminders Index Technical Manual has also been updated for DG\*5.3\*884 and is posted under CPRS: Clinical Reminders on the VDL website: [http://www.va.gov/vdl/](http://www.va.gov/vdl/application.asp?appid=60) .

The following manual does not exist for this package:

- Security Guide

> NOTE: Security information is contained within the PIMS Technical Manual.

The following ADT documents are present on the VDL but do not require updates:

- PIMS User Manual – ADT Module
- PIMS User Manual – Menus, Intro & Orientation
- PIMS User Manual – Outputs Menu
- User Manual - ADT Outputs Menu
- User Manual - Bed Control Menu
- User Manual - Contract Nursing Home RUG Menu
- User Manual - Copay Exemption Test Supervisor Menu
- User Manual – MAS Code Sheet Manager Menu
- User Manual – Registration Menu
- User Manual – RUG-II Menu
- User Manual – Security Officer Menu
- User Manual – Supervisor ADT Menu
- User Manual – Veteran ID Card Menu
- User Manual – Means Test Supervisor Menu
- PIMS Installation Guide

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*884 provides enhancements to increase the number of ICD-10 diagnosis and procedure codes that can be entered and displayed primarily within the following options (see Section 7, Associated Options, below for other options affected): Load/Edit PTF Data, Quick Load/Edit PTF Data, Set Up Non-VA PTF Record, and DRG Calculation.

## Increase Diagnosis Codes and POA Indicators in 501 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 501 transactions will allow up to 25 diagnosis codes, each with an associated POA indicator, for a total of 25 diagnosis codes and 25 POA indicators.

## Increase Procedure Codes in 401 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 401 Surgeries transactions will allow up to 25 Procedure codes.

## Increase Procedure Codes in 601 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 601 Non-OR Procedures transactions will allow up to 25 Procedure codes.

## Increase Diagnosis Codes and POA Indicators in 701 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 701 transaction will allow one principal diagnosis with a POA indicator and up to 24 secondary diagnoses with POA indicators (data stored in 702 record) for a total of 25 diagnosis codes and 25 POA Indicators.

## Display ICD-10 Codes and POA Indicators on 501, 401, 601, and 701 Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ADT package shall display up to 25 active ICD-10 diagnosis codes with their associated POA indicator and up to 25 each ICD-10 Surgical and Procedure codes. The user shall be able to view all the data when the records scroll off the screen.

## Calculate the Diagnosis Related Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ADT package shall provide the ability to calculate the Diagnosis Related Groups (DRG) within the PTF record from the ICD-10 codes in the record or through manual entry.

## Modify PTF MailMan Message to Transmit More ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are being made to the content of PTF Transmission (VistA MailMan) messages to accommodate the inclusion of up to 25 ICD-10 Diagnosis and associated POA indicators, up to 25 ICD-10 Non-OR Procedure codes, and up to 25 Surgical codes that could be included in a record for transmission.

Modifications are being made to the delivery of the PTF Transmission messages to the Austin Information Technology Center (AITC). The messages will be sent to a new queue; Q-PTI.VA.GOV. The confirmation messages from the AITC will be sent to a new local mail group called PTI. The new PTI mail group will replace the current PTT mail group and should contain the same member recipients.

Modifications are being made to the 099 Transmission, 099 Transmission for Census, and Record Output (RPO) options to ensure acceptance of the following Mailman message transaction types when transmitted to the new PTI queue at the AITC:

- 099 – Request to delete a PTF record at the AITC.
- 150 – Request a printout for a single admission record for a patient.
- 151 – Request a printout for all admissions for a patient.

# Fixes and Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides the enhancements described above, patch DG\*5.3\*884 also includes the following fixes and other changes.

## Delete POA Indicator when Associated Diagnosis is Deleted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user deletes an ICD-10 diagnosis code within the following PTF options, its associated Present on Admission (POA) indicator is automatically deleted:

- Load/Edit PTF Data
- Quick Load/Edit PTF Data
- Set Up Non-VA PTF Record

This change applies to the deletion of primary, secondary, and 501 movement diagnosis codes.

## Prevent Population of POA if Associated Diagnosis is Not Present

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user will not be able to enter a POA indicator field when an associated ICD-10 diagnosis code is not present within the following PTF options:

- Load/Edit PTF Data
- Quick Load/Edit PTF Data
- Set Up Non-VA PTF Record

This change applies to POA indicator fields associated with primary, secondary, and 501 movement diagnosis codes.

## Allow Duplicate ICD Codes for 401 Surgeries and 601 Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user will be able to enter duplicate ICD codes for 401 Surgery and 601 Procedure transactions within the following options:

- Load/Edit PTF Data
- Quick Load/Edit PTF Data
- Set Up Non-VA PTF Record

> **NOTE:** Entry of duplicate ICD codes will NOT be allowed for 701 Primary/Secondary Diagnosis or 501 Movement transactions.

## Entry of Gender-specific ICD Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user will be able to enter any gender-specific ICD-10 code into a 501 Movement, 401 Surgery, and 601 Procedure transaction whether or not it matches the patient’s gender. Within the following options, the user will receive a warning message when attempting to enter a gender-specific ICD-10 code for a patient of the opposite gender, but the user will not be prevented from entering the gender-specific code:

- Load/Edit PTF Data
- Quick Load/Edit PTF Data
- Set Up Non-VA PTF Record

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 modified the following fields.

| File Name (File Number)     | Field Name                 | Field Number |
|-----------------------------|----------------------------|--------------|
| PTF (#45)                   | PRINCIPAL DIAGNOSIS        | \#79         |
| PTF (#45)                   | SECONDARY DIAGNOSIS 1      | \#79.16      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 2      | \#79.17      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 3      | \#79.18      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 4      | \#79.19      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 5      | \#79.201     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 6      | \#79.21      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 7      | \#79.22      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 8      | \#79.23      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 9      | \#79.24      |
| PTF (#45)                   | SECONDARY DIAGNOSIS 10     | \#79.241     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 11     | \#79.242     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 12     | \#79.243     |
| PTF (#45)                   | SECODNARY DIAGNOSIS 13     | \#79.244     |
| PTF (#45)                   | POA PRINCIPAL DIAGNOSIS    | \#82.01      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 1  | \#82.02      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 2  | \#82.03      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 3  | \#82.04      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 4  | \#82.05      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 5  | \#82.06      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 6  | \#82.07      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 7  | \#82.08      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 8  | \#82.09      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 9  | \#82.1       |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 10 | \#82.11      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 11 | \#82.12      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 12 | \#82.13      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 13 | \#82.14      |
|                             |                            |              |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 1           | \#8          |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 2           | \#9          |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 3           | \#10         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 4           | \#11         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 5           | \#12         |
|                             |                            |              |
| PTF (#45) Subfile 501 (#50) | ICD 1                      | \#5          |
| PTF (#45) Subfile 501 (#50) | ICD 2                      | \#6          |
| PTF (#45) Subfile 501 (#50) | ICD 3                      | \#7          |
| PTF (#45) Subfile 501 (#50) | ICD 4                      | \#8          |
| PTF (#45) Subfile 501 (#50) | ICD 5                      | \#9          |
| PTF (#45) Subfile 501 (#50) | ICD 6                      | \#11         |
| PTF (#45) Subfile 501 (#50) | ICD 7                      | \#12         |
| PTF (#45) Subfile 501 (#50) | ICD 8                      | \#13         |
| PTF (#45) Subfile 501 (#50) | ICD 9                      | \#14         |
| PTF (#45) Subfile 501 (#50) | ICD 10                     | \#15         |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 1              | \#82.01      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 2              | \#82.02      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 3              | \#82.03      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 4              | \#82.04      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 5              | \#82.05      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 6              | \#82.06      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 7              | \#82.07      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 8              | \#82.08      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 9              | \#82.09      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 10             | \#82.1       |
|                             |                            |              |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 1           | \#4          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 2           | \#5          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 3           | \#6          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 4           | \#7          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 5           | \#8          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 6           | \#9          |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 7           | \#10         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 8           | \#11         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 9           | \#12         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 10          | \#13         |

<span id="_Toc428467127" class="anchor"></span>Table : Fields Added by DG\*5.3\*884

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 added the following fields.

| File Name (File Number)     | Field Name                 | Field Number |
|-----------------------------|----------------------------|--------------|
| PTF (#45)                   | SECONDARY DIAGNOSIS 14     | \#79.245     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 15     | \#79.246     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 16     | \#79.247     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 17     | \#79.248     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 18     | \#79.249     |
| PTF (#45)                   | SECONDARY DIAGNOSIS 19     | \#79.2491    |
| PTF (#45)                   | SECONDARY DIAGNOSIS 20     | \#79.24911   |
| PTF (#45)                   | SECONDARY DIAGNOSIS 21     | \#79.24912   |
| PTF (#45)                   | SECONDARY DIAGNOSIS 22     | \#79.24913   |
| PTF (#45)                   | SECONDARY DIAGNOSIS 23     | \#79.24914   |
| PTF (#45)                   | SECONDARY DIAGNOSIS 24     | \#79.24915   |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 14 | \#82.15      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 15 | \#82.16      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 16 | \#82.17      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 17 | \#82.18      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 18 | \#82.19      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 19 | \#82.2       |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 20 | \#82.21      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 21 | \#82.22      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 22 | \#82.23      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 23 | \#82.24      |
| PTF (#45)                   | POA SECONDARY DIAGNOSIS 24 | \#82.25      |
|                             |                            |              |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 6           | \#13         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 7           | \#14         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 8           | \#15         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 9           | \#16         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 10          | \#17         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 11          | \#18         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 12          | \#19         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 13          | \#20         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 14          | \#21         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 15          | \#22         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 16          | \#23         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 17          | \#24         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 18          | \#25         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 19          | \#26         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 20          | \#27         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 21          | \#28         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 22          | \#29         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 23          | \#30         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 24          | \#31         |
| PTF (#45) Subfile 401 (#40) | OPERATION CODE 25          | \#32         |
|                             |                            |              |
| PTF (#45) Subfile 501 (#50) | ICD 11                     | \#81.01      |
| PTF (#45) Subfile 501 (#50) | ICD 12                     | \#81.02      |
| PTF (#45) Subfile 501 (#50) | ICD 13                     | \#81.03      |
| PTF (#45) Subfile 501 (#50) | ICD 14                     | \#81.04      |
| PTF (#45) Subfile 501 (#50) | ICD 15                     | \#81.05      |
| PTF (#45) Subfile 501 (#50) | ICD 16                     | \#81.06      |
| PTF (#45) Subfile 501 (#50) | ICD 17                     | \#81.07      |
| PTF (#45) Subfile 501 (#50) | ICD 18                     | \#81.08      |
| PTF (#45) Subfile 501 (#50) | ICD 19                     | \#81.09      |
| PTF (#45) Subfile 501 (#50) | ICD 20                     | \#81.1       |
| PTF (#45) Subfile 501 (#50) | ICD 21                     | \#81.11      |
| PTF (#45) Subfile 501 (#50) | ICD 22                     | \#81.12      |
| PTF (#45) Subfile 501 (#50) | ICD 23                     | \#81.13      |
| PTF (#45) Subfile 501 (#50) | ICD 24                     | \#81.14      |
| PTF (#45) Subfile 501 (#50) | ICD 25                     | \#81.15      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 11             | \#82.11      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 12             | \#82.12      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 13             | \#82.13      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 14             | \#82.14      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 15             | \#82.15      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 16             | \#82.16      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 17             | \#82.17      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 18             | \#82.18      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 19             | \#82.19      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 20             | \#82.2       |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 21             | \#82.21      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 22             | \#82.22      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 23             | \#82.23      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 24             | \#82.24      |
| PTF (#45) Subfile 501 (#50) | POA FOR ICD 25             | \#82.25      |
|                             |                            |              |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 11          | \#14         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 12          | \#15         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 13          | \#16         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 14          | \#17         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 15          | \#18         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 16          | \#19         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 17          | \#20         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 18          | \#21         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 19          | \#22         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 20          | \#23         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 21          | \#24         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 22          | \#25         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 23          | \#26         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 24          | \#27         |
| PTF (#45) Subfile 601 (#60) | PROCEDURE CODE 25          | \#28         |

<span id="_Toc428467128" class="anchor"></span>Table : Modified Templates

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 does not add, delete, or modify any forms.

# Associated Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 adds one new mail group called PTI. This mail group will accept confirmation messages from the AITC. The PTI mail group replaces the PTT mail group and should contain the same group members.

# Associated Menu Listings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 modifies the code for the following options to accommodate the expanded number of ICD-10 codes which can now be present in a given PTF record:

- PTF Menu \> Census Menu
- PTF Menu \> Census Menu \> Load/Edit PTF Data
- PTF Menu \> Census Menu \> Inquire Census Record
- PTF Menu \> Census Menu \> Other Census Outputs
- PTF Menu \> Census Menu \> Other Census Outputs \> Comprehensive Census Report
- PTF Menu \> Census Menu \> Release Closed Census Records
- PTF Menu \> Census Menu \> Transmit Census Records
- PTF Menu \> Census Menu \> Open Closed Census Records
- PTF Menu \> Census Menu \> Open Released or Transmitted Census Records
- PTF Menu \> Census Menu \> 099 Transmission for Census Record
- PTF Menu \> DRG Calculation
- PTF Menu \> Load/Edit PTF Data
- PTF Menu \> PTF Output Menu
- PTF Menu \> PTF Output Menu \> Comprehensive Report by Admission
- PTF Menu \> PTF Output Menu \> Diagnostic Code PTF Record Search
- PTF Menu \> PTF Output Menu \> DRG Information Report
- PTF Menu \> PTF Output Menu \> Inquire PTF Record
- PTF Menu \> PTF Output Menu \> Patient Summary by Admission
- PTF Menu \> PTF Output Menu \> Surgical Code PTF Record Search
- PTF Menu \> Quick Load/Edit PTF Data
- PTF Menu \> Set Up Non-VA PTF Record
- PTF Menu \> Validity Check of PTF Record

# Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 modifies the code for the following reports to accommodate the expanded number of ICD-10 codes which can now be present in a given PTF record:

- Inquire Census Record \[DGPT CENSUS INQUIRE\]
- Comprehensive Census Report \[DGPT CENSUS RECORD REPORT\]
- Comprehensive Report by Admission \[DG PTF COMPREHENSIVE REPORT\]
- Diagnostic Code PTF Record Search \[DG PTF ICD DIAGNOSTIC SEARCH\]
- DRG Information Report \[DG PTF DRG INFORMATION OUTPUT\]
- DRG Case Mix Summary \[DG PTF DRG CASE MIX SUMMARY\]
- Inquire PTF Record \[DG PTF COMPREHENSIVE INQUIRY\]
- Patient Summary by Admission \[DG PTF SUMMARY DIAG/OP OUTPUT\]
- Surgical Code PTF Record Search \[DG PTF ICD SURGICAL SEARCH\]
- Update Transfer DRGs for Current FY \[DG PTF UPDATE TRANSFER DRG’S\]
- Validity Check of PTF Record \[DG PTF VALIDITY CHECK\]

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 does not add, delete, or modify any protocols.

# Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Keys associated with patch DG\*5.3\*884.

# Associated Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 modifies the following template.

| Template | Type of Template | File Name (Number) |
|----------|------------------|--------------------|
| DG601    | Input            | PTF (#45)          |

<span id="_Toc428467129" class="anchor"></span>Table : New Templates

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 adds the following templates.

| Template   | Type of Template | File Name (Number) |
|------------|------------------|--------------------|
| DG401-10P  | Input            | PTF (#45)          |
| DG501-10D  | Input            | PTF (#45)          |
| DG501F-10D | Input            | PTF (#45)          |
| DG601-10P  | Input            | PTF (#45)          |
| DG701-10D  | Input            | PTF (#45)          |

<span id="_Toc428467130" class="anchor"></span>Table : Modified ICRs

# Integration Control Registrations (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 modifies the following ICRs.

| ICR Number | ICR Name                    |
|------------|-----------------------------|
| 418        | DBIA418                     |
| 3157       | Patient Treatment File Data |
| 3164       | DG Patient Treatment Data   |
| 3511       | DBIA3511                    |

<span id="_Toc428467131" class="anchor"></span>Table : New ICRs

## New ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 adds the following ICR.

| ICR Number | ICR Name |
|------------|----------|
| 6130       | DGPTFUT  |

<span id="_Toc428467132" class="anchor"></span>Table : Error Codes Added to PTF AUSTIN ERROR CODES (#45.64)

# Other Database Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Error Codes Added to PTF AUSTIN ERROR CODES (#45.64)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 adds the following 149 new error codes to the PTF AUSTIN ERROR CODES (#45.64) file.

| Error Code | Description                                       |
|------------|---------------------------------------------------|
| 152        | Invalid MST indicator                             |
| 154        | Invalid Combat Veteran Date                       |
| 155        | Invalid Combat Veteran indicator                  |
| 156        | Invalid SHAD indicator^23                         |
| 574        | Invalid POA for ICD 2                             |
| 577        | Invalid POA for ICD 3                             |
| 578        | Invalid POA for ICD 4                             |
| 579        | Invalid POA for ICD 5                             |
| 580        | Invalid POA for ICD 6                             |
| 581        | Invalid POA for ICD 7                             |
| 582        | Invalid POA for ICD 8                             |
| 583        | Invalid POA for ICD 9                             |
| 584        | Invalid POA for ICD 10                            |
| 585        | Invalid POA for ICD 11                            |
| 586        | Invalid POA for ICD 12                            |
| 587        | Invalid POA for ICD 13                            |
| 588        | Invalid POA for ICD 14                            |
| 589        | Invalid POA for ICD 15                            |
| 590        | Invalid POA for ICD 16                            |
| 569        | Invalid POA for ICD 1                             |
| 591        | Invalid POA for ICD 17                            |
| 592        | Invalid POA for ICD 18                            |
| 593        | Invalid POA for ICD 19                            |
| 594        | Invalid POA for ICD 20                            |
| 595        | Invalid POA for ICD 21                            |
| 596        | Invalid POA for ICD 22                            |
| 597        | Invalid POA for ICD 23                            |
| 598        | Invalid POA for ICD 24                            |
| 599        | Invalid POA for ICD 25                            |
| 746        | Invalid treatment for service condition indicator |
| 747        | Invalid agent orange indicator                    |
| 748        | Invalid ionizing radiation indicator              |
| 749        | Invalid southwest Asia indicator                  |
| 752        | Invalid military sexual trauma indicator          |
| 754        | Invalid head/neck cancer indicator                |
| 755        | Invalid combat veteran indicator                  |
| 758        | Invalid race 1 indicator                          |
| 759        | Invalid race 2 indicator                          |
| 760        | Invalid race 3 indicator                          |
| 761        | Invalid race 4 indicator                          |
| 762        | Invalid race 5 indicator                          |
| 763        | Invalid race 6 indicator                          |
| 756        | Invalid SHAD indicator                            |
| 757        | Invalid POA for DXLS                              |
| 501        | Incorrect Attending Physician SSN                 |
| 516        | Invalid diagnostic code \#6                       |
| 517        | Invalid diagnostic code \#7                       |
| 518        | Invalid diagnostic code \#8                       |
| 519        | Invalid diagnostic code \#9                       |
| 520        | Invalid diagnostic code \#10                      |
| 521        | Invalid diagnostic code \#11                      |
| 522        | Invalid diagnostic code \#12                      |
| 523        | Invalid diagnostic code \#13                      |
| 524        | Invalid diagnostic code \#14                      |
| 525        | Invalid diagnostic code \#15                      |
| 526        | Invalid diagnostic code \#16                      |
| 527        | Invalid diagnostic code \#17                      |
| 528        | Invalid diagnostic code \#18                      |
| 529        | Invalid diagnostic code \#19                      |
| 558        | Invalid diagnostic code \#20                      |
| 559        | Invalid diagnostic code \#21                      |
| 560        | Invalid diagnostic code \#22                      |
| 561        | Invalid diagnostic code \#23                      |
| 562        | Invalid diagnostic code \#24                      |
| 563        | Invalid diagnostic code \#25                      |
| 764        | Invalid POA for principle diagnosis               |
| 765        | Invalid POA for secondary diagnosis 1             |
| 766        | Invalid POA for secondary diagnosis 2             |
| 767        | Invalid POA for secondary diagnosis 3             |
| 768        | Invalid POA for secondary diagnosis 4             |
| 769        | Invalid POA for secondary diagnosis 5             |
| 777        | Invalid POA for secondary diagnosis 6             |
| 778        | Invalid POA for secondary diagnosis 7             |
| 779        | Invalid POA for secondary diagnosis 8             |
| 780        | Invalid POA for secondary diagnosis 9             |
| 781        | Invalid POA for secondary diagnosis 10            |
| 782        | Invalid POA for secondary diagnosis 11            |
| 783        | Invalid POA for secondary diagnosis 12            |
| 784        | Invalid POA for secondary diagnosis 13            |
| 785        | Invalid POA for secondary diagnosis 14            |
| 786        | Invalid POA for secondary diagnosis 15            |
| 787        | Invalid POA for secondary diagnosis 16            |
| 788        | Invalid POA for secondary diagnosis 17            |
| 789        | Invalid POA for secondary diagnosis 18            |
| 790        | Invalid POA for secondary diagnosis 19            |
| 791        | Invalid POA for secondary diagnosis 20            |
| 792        | Invalid POA for secondary diagnosis 21            |
| 793        | Invalid POA for secondary diagnosis 22            |
| 794        | Invalid POA for secondary diagnosis 23            |
| 795        | Invalid POA for secondary diagnosis 24            |
| 796        | Invalid POA for secondary diagnosis 25            |
| 797        | Invalid ""summary diagnostic"" code \#10          |
| 798        | Invalid ""summary diagnostic"" code \#11          |
| 799        | Invalid ""summary diagnostic"" code \#12          |
| 800        | Invalid ""summary diagnostic"" code \#13          |
| 801        | Invalid ""summary diagnostic"" code \#14          |
| 802        | Invalid ""summary diagnostic"" code \#15          |
| 803        | Invalid ""summary diagnostic"" code \#16          |
| 804        | Invalid ""summary diagnostic"" code \#17          |
| 805        | Invalid ""summary diagnostic"" code \#18          |
| 806        | Invalid ""summary diagnostic"" code \#19          |
| 807        | Invalid ""summary diagnostic"" code \#20          |
| 808        | Invalid ""summary diagnostic"" code \#21          |
| 809        | Invalid ""summary diagnostic"" code \#22          |
| 810        | Invalid ""summary diagnostic"" code \#23          |
| 811        | Invalid ""summary diagnostic"" code \#24          |
| 812        | Invalid ""summary diagnostic"" code \#25          |
| 137        | Invalid value in position 65. Should be a space." |
| 704        | Invalid ethnic indicator                          |
| 418        | Invalid Operative code \#6                        |
| 419        | Invalid Operative code \#7                        |
| 420        | Invalid Operative code \#8                        |
| 421        | Invalid Operative code \#9                        |
| 422        | Invalid Operative code \#10                       |
| 423        | Invalid Operative code \#11                       |
| 424        | Invalid Operative code \#12                       |
| 425        | Invalid Operative code \#13                       |
| 426        | Invalid Operative code \#14                       |
| 427        | Invalid Operative code \#15                       |
| 428        | Invalid Operative code \#16                       |
| 429        | Invalid Operative code \#17                       |
| 430        | Invalid Operative code \#18                       |
| 431        | Invalid Operative code \#19                       |
| 432        | Invalid Operative code \#20                       |
| 433        | Invalid Operative code \#21                       |
| 434        | Invalid Operative code \#22                       |
| 446        | Invalid Operative code \#23                       |
| 447        | Invalid Operative code \#24                       |
| 448        | Invalid Operative code \#25                       |
| 610        | Invalid procedure code \#6                        |
| 611        | Invalid procedure code \#7                        |
| 612        | Invalid procedure code \#8                        |
| 613        | Invalid procedure code \#9                        |
| 614        | Invalid procedure code \#10                       |
| 615        | Invalid procedure code \#11                       |
| 616        | Invalid procedure code \#12                       |
| 617        | Invalid procedure code \#13                       |
| 618        | Invalid procedure code \#14                       |
| 619        | Invalid procedure code \#15                       |
| 620        | Invalid procedure code \#16                       |
| 621        | Invalid procedure code \#17                       |
| 622        | Invalid procedure code \#18                       |
| 623        | Invalid procedure code \#19                       |
| 624        | Invalid procedure code \#20                       |
| 625        | Invalid procedure code \#21                       |
| 626        | Invalid procedure code \#22                       |
| 627        | Invalid procedure code \#23                       |
| 628        | Invalid procedure code \#24                       |
| 629        | Invalid procedure code \#25                       |

<span id="_Toc428467133" class="anchor"></span>Table : Known Issues

# New Service Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 is associated with NSR \#20070902, ICD-10-CM Conversion.

# Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no patient safety issues associated with patch DG\*5.3\*884.

# Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Remedy Tickets associated with patch DG\*5.3\*884.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*884 is currently subject to the change request described in the table below.

<table>
<caption><p><span id="_Toc428467134" class="anchor"></span>Table : Acronyms and Definitions</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Code Change Request Number</th>
<th>Headline</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADTFR00000613</td>
<td>Quick Load Edit – after ICD-10 activation – ICD-9 codes have no *</td>
<td><p>This record has been changed to a discharge date of 10/28/15 so ICD-10 coding rules should apply.</p>
<p>ICD-9 codes do not have an asterisk “*” after them to indicate that the ICD-9 codes need to be removed. It does provide the POA indicator. In testing, I changed part of the codes through the regular Load Edit option. Then I went to the Quick Load Edit and was going to do those for the 701, 601, and 501. There were no asterisks on any ICD-9 codes in the 701, 601, or 501.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc428467134" class="anchor"></span>Table : Acronyms and Definitions

1.  <span id="_Toc428467191" class="anchor"></span>Acronyms and Definitions

| Acronym | Definition                                                                |
|---------|---------------------------------------------------------------------------|
| ADT     | Registration, Enrollment, Eligibility, Admission, Discharge, and Transfer |
| AITC    | Austin Information Technology Center                                      |
| AP      | Anatomic Pathology                                                        |
| CCR     | Clinical Case Registries                                                  |
| DG      | Registration Namespace                                                    |
| EPI     | Emerging Pathogens Initiative                                             |
| GMTS    | Health Summary Namespace                                                  |
| GUI     | Graphical User Interface                                                  |
| HS      | Health Summary                                                            |
| IB      | Integrated Billing                                                        |
| ICD-10  | International Classification of Diseases, 10<sup>th</sup> Revision        |
| LR      | Laboratory Namespace                                                      |
| OE/RR   | Order Entry/Results Reporting                                             |
| OR      | Order Entry/Results Reporting Namespace                                   |
| POA     | Present on Admission                                                      |
| PTF     | Patient Treatment File                                                    |
| ROR     | Clinical Case Registries Namespace                                        |
| VHA     | Veterans Health Administration                                            |
| VistA   | Veterans Health Information Systems and Technology Architecture           |