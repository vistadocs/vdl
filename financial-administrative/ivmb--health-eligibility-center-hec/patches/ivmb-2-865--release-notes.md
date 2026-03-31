---
title: IVMB*2*865 Operation Enduring Freedom Operation IRAQI Freedom Phase II
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Operation Enduring Freedom Operation IRAQI Freedom Phase II
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*865
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - conflict
  - service
  - modifications
  - added
  - military
  - fields
  - income
  - veterans
page_count: 0
word_count: 1376
section_count: 10
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p865_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p865_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

operation ENduring Freedom &

Operation Iraqi freedom

Phase 11

Release Notes

IVMB\*2\*865

July 2006

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [## Purpose of this Manual](#purpose-of-this-manual)
  - [## Related Documents](#related-documents)
  - [Acronyms and Definitions](#acronyms-and-definitions)
- [# User Release Notes](#user-release-notes)
  - [New Features, Functions, Modifications, and Enhancements](#new-features-functions-modifications-and-enhancements)
    - [New Features added to Conflict Location Data File](#new-features-added-to-conflict-location-data-file)
    - [Veterans ID & Verification Access File Enhancements](#veterans-id-verification-access-file-enhancements)
    - [IVM Client Income Features](#ivm-client-income-features)
    - [Modifications to the IVME VIVA DATA EDIT File](#modifications-to-the-ivme-viva-data-edit-file)
    - [OEF/OIF Data Registry Interface](#oefoif-data-registry-interface)
- [Technical Release Notes](#technical-release-notes)
  - [## Data Dictionary Changes](#data-dictionary-changes)
  - [Modifications to HL7 Messaging](#modifications-to-hl7-messaging)
    - [Modifications to ORF/ORUZ07 Messages](#modifications-to-orforuz07-messages)
    - [### Added New VA026 Military Service Component Table](#added-new-va026-military-service-component-table)
  - [## Updated VA038 Military History Type Table](#updated-va038-military-history-type-table)
  - [## ## Enrollment Trigger Events](#enrollment-trigger-events)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Operation Enduring Freedom & Operation Iraqi Freedom (OEF/OIF) initiative supports advanced technology and business changes made to the INCOME VERIFICATION MATCH V. 2.0. The Health Eligibility Center (HEC) has requested enhancements be made to the project that will identify the combat periods for veterans who were deployed to the areas covered under the Operation Enduring Freedom (OEF), and Operation Iraqi Freedom (OIF) project. These modifications made to the HEC system are in conjunction with the following VistA patches: DG\*5.3\*689, DG\*5.3\*673, and IVM\*2\*114.

The OEF/OIF data registry provides information from the following sources:

- Federal Health Information Exchange program (FHIE)
- Veterans Information System (VIS)
- Environmental Medicine (EM)

The data obtained through these departments are crucial for monitoring and maintaining veteran's information completed and supported by the VISN Support Service Center (VSSC). The OEF/OIF Data Registry warehouses existing patients that are filed in the HEC Legacy database. The initial seeding of the HEC database from the registry will be completed prior to implementing the ability to enter OEF/OIF conflicts in either the HEC or VistA systems.

Patch IVMB\*2\*865 provides the following functionality:

- Four new Conflicts Fields were added to the “Conflict Location File.”
- A new field, “Conflict Service” sub-record with seven fields was added to the Veterans Id & Verification Access (VIVA) File.
- Two new fields were added to the IVM Client Income File, one to Conflict Service sub-file and one to the Military Service sub-file.
- Modifications were made to the Enter/Edit menu option of the VIVA File.
- A new OEF/OIF Registry Interface was created to monitor and maintain conflict episodes.
- Sharing of OEF/OIF/UNK conflict data between the HEC and medical facilities will begin with the implementation of patch DG\*5.3\*673.
- The Combat Veteran (CV) End Date Algorithm was modified to include using OEF, OIF, Unknown OEF/OIF, or Conflict Unspecified conflicts for calculating precise dates.

## ## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the HEC Legacy system.

## ## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following related documents are available through the VistA Documentation Library (VDL):

|                        |                                            |
|------------------------|--------------------------------------------|
| File Name              | Description                                |
| DG_5_3_P678_REG_UM.PDF | Revised PIMS Registration Menu User Manual |
| DG_5_3_P678_REG_TM.PDF | Revised PIMS Technical Manual              |
| IVM_2_P114_TM.PDF      | Revised IVM V. 2.0 Technical Manual        |

## Acronyms and Definitions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acronyms

|         |                                       |
|---------|---------------------------------------|
| Acronym | Description                           |
| ADT     | Admissions, Discharges, Transfers     |
| CBO     | Chief Business Office                 |
| EC      | Environmental Contaminants            |
| EGT     | Enrollment Group Threshold            |
| HEC     | Health Eligibility Center             |
| HVE     | HEC V*IST*A Enhancements      |
| IVM     | Income Verification Matching          |
| MT      | Means Test                            |
| NSC     | Non-service-connected                 |
| PIMS    | Patient Information Management System |
| VA      | Veterans Administration               |
| VHA     | Veterans Health Administration        |

Definitions

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Disenrollment     | Voluntary request from veteran to discontinue enrollment in the VA Health Care system                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| GMT Thresholds    | a.k.a. HUD Indices. Geographical income level thresholds set yearly by the U.S. Department of Housing and Urban Development                                                                                                                                                                                                                                                                                                                                                                                                               |
| HL7               | Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*ist*A HL7 package to assist in transporting data using this specification.                                                                                                                                                                                                                                                                                       |
| IVM               | Income Verification Match. A program designed to verify income and insurance data reported by the veteran with that received from IRS (Internal Revenue Service), SSA (Social Security Administration), and other sources                                                                                                                                                                                                                                                                                                                 |
| Means Test        | Eligibility for VA hospital care and nursing home care is divided into two categories - mandatory and discretionary. An income assessment is made to determine whether a non service-connected veteran, who is not in receipt of VA monetary benefits or otherwise exempt from income assessment, is eligible for cost-free VA medical care. This income assessment is known as "Means Testing". Patients whose income is above the defined income levels must agree to make copayments to VA for outpatient and inpatient care rendered. |
| MT Thresholds     | Income threshold levels set yearly within the VA for the purpose of establishing benefit levels for veterans                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HEC Legacy System | M-based database currently in use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# # User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Features, Functions, Modifications, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Features added to Conflict Location Data File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary functionality delivered from this patch consists of adding the following four new Conflicts to the Conflict Location File:

- OEF – choose this option if the veteran served in Operation Enduring Freedom
- OIF – choose this option if the veteran served in Operation Iraqi Freedom
- UNK - Unknown OEF/OIF- select this option in the event a veteran is known to have served in either OEF or OIF, however not enough information is provided to make this determination
- UNS - Conflict Unspecified- select this option if a veteran is known to have received hostile fire/imminent danger pay and is combat eligible, however the specific conflict is not known

### Veterans ID & Verification Access File Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields have been added to the Veterans ID & Verification Access File which consists of the following Conflict Service options:

- Conflict Location
- Conflict From Date
- Conflict To Date
- Hostile Fire/Imm Danger Pay
- CZTE Indicator
- Data Source
- Record Date/Time Stamp

### IVM Client Income Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IVM Client Income Data File consists of two new sub-fields:

- In the Conflict Service Sub-field, Source Conflict Data
- In the Military Service Sub-field, Service Component

### Modifications to the IVME VIVA DATA EDIT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit menu option of the VIVA Data Edit file has been modified to allow a user the ability to enter and/or edit the new conflict fields.

The following rules apply when a user enters/edits a new conflict field:

- Whenever a conflict episode is updated the system will automatically

> “date/time,” stamp the record. The “Conflict Location,” “Conflict

From Date,” and “Conflict To Date,” are all required fields.

- A user that has full access to the system will have the ability to enter/edit

fields in the Conflict Service sub-field with the exception of the Record Date/Time

Stamp and Data Source which are system generated.

- When adding new episodes the following methods are determined:
  - The earliest Conflict Unspecified deployment from (start) date is 11/01/1998.
  - The earliest Unknown OEF/OIF and OEF deployment from (start) date is 09/01/2001.
  - The earliest OIF deployment from (start) date is 03/01/2003.
- The following fields (OEF, OIF, Unknown OEF/OIF, and Conflict Unspecified)

> cannot overlap each other and are the only conflicts stored in the Veterans ID & Verification Access. However, they may overlap other conflicts that are not OEF or OIF that are stored in the IVM Client Income File.

- No validation occurs between the military service episode information located in the IVM Client Income File and the conflicts in the Veterans Id & Verification Access (Viva) File.
- Any modifications made to the Conflict Service sub-field will automatically trigger an outbound HEC Legacy Enrollment/Eligibility (Z11) message back to the VistA sites of record.

### OEF/OIF Data Registry Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OEF/OIF Data Registry was created by the VISN Support Service Center (VSSC). The Registry is responsible for creating and maintaining conflict episode records that are acquired from the following sources:

- Federal Health Information Exchange (FHIE)
- Veterans Information System (VIS)
- Environmental Medicine (EM)

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVMB\*2\*114 must be installed before patch IVMB\*2\*865 (Income Verification Match Phase II).

## ## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields were added to the Data Dictionaries:

- Veterans ID and Verification Access VIVA File (#300.11)
- Conflict Service File (#300.1195)
- IVM Client Income File(#300.13)

## Modifications to HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Full Data Transmission dispatches a complete profile of patient demographic, eligibility, means test, income, insurance, and enrollment information to the HEC.

### Modifications to ORF/ORU~Z07 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new fields were added to the ZMH segment tables located in the Full Data Transmission section. These fields are populated by the user-initiated post-installation conversion for Patch IVMB\*2\*865 and they consist of the following Z07 messages:

- Added VA Specific Military History Message to ORF~Z07 Segment- Sequence 5
- Added VA Specific Military History Message to ORU~Z07 Segment- Sequence 5

### ### Added New VA026 Military Service Component Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table VA026 – Military Service Component

|      |                          |
|------|--------------------------|
| Code | Description              |
| R    | Regular                  |
| V    | Activated reserve        |
| G    | Activated national guard |

## ## Updated VA038 Military History Type Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table VA038 – Military History Type

|      |                                  |
|------|----------------------------------|
| Code | Description                      |
| OEIF | OPERATION ENDURING/IRAQI FREEDOM |

## ## ## Enrollment Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The conversion included with Patch IVMB\*2\*865 populates the Income Verification Match field with information from Military Data Service.

The table below illustrates the new fields that were added to the Enrollment Trigger Section.

|                                                                           |                     |               |
|---------------------------------------------------------------------------|---------------------|---------------|
| File or Field number                                                  | Cross Reference | API Call  |
| LOCATION OF SERVICE (.01) in the SERVICE \[OEF OR OIF\] sub-file (#23215) | AENR321501          | EVENT^IVMPLOG |
| OEF/OIF FROM DATE (2) in the SERVICE \[OEF OR OIF\] sub-file (#23215)     | AENR321502          | EVENT^IVMPLOG |
| OEF/OIF TO DATE (3) in the SERVICE \[OEF OR OIF\] sub-file (#23215)       | AENR321503          | EVENT^IVMPLOG |