---
title: IVMB*2*891/IVMB*2*900 Pending Verification Status HEC Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*891
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: Patches IVMB\2\891 and IVMB\2\900 will update “Pending Verification” changes included with enhancements to the INCOME VERIFICATION MATCH V. 2.0 software. The Health Eligibility Center (HEC) Enrollment system provides functionality to share patient information with sites of record. This process inclu
audience: 
keywords: 
  - table
  - contents
  - enrollment
  - pending
  - ivmb
  - changes
  - status
  - indicator
  - modifications
  - messages
page_count: 0
word_count: 1033
section_count: 8
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p891_p900_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p891_p900_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

Pending VERIFICATION Status

Release Notes

IVMB\*2\*891

&

IVMB\*2\*900

September 2006

Table of Contents

# *Introduction*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [## Related Documents](#related-documents)
  - [Acronyms and Definitions](#acronyms-and-definitions)
- [# User Release Notes](#user-release-notes)
  - [New Features, Functions, Modifications, and Enhancements](#new-features-functions-modifications-and-enhancements)
    - [Two AAC INDICATORS statuses added to IVM Master Client file values that screen the Z11 messages](#two-aac-indicators-statuses-added-to-ivm-master-client-file-values-that-screen-the-z11-messages)
    - [### New Bulletin Added](#new-bulletin-added)
- [Technical Release Notes](#technical-release-notes)
  - [Data Dictionary Changes](#data-dictionary-changes)
  - [Modifications to HL7 Messaging](#modifications-to-hl7-messaging)
    - [### Modifications to Routines](#modifications-to-routines)
    - [IVMB\2\900 consist of changes that affect the \[AYCHLSA4\] routine.](#ivmb2900-consist-of-changes-that-affect-the-aychlsa4-routine)
    - [## Enrollment Trigger Events](#enrollment-trigger-events)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches IVMB\*2\*891 and IVMB\*2\*900 will update “Pending Verification” changes included with enhancements to the INCOME VERIFICATION MATCH V. 2.0 software. The Health Eligibility Center (HEC) Enrollment system provides functionality to share patient information with sites of record. This process includes functionality to provide both solicited patient information and unsolicited patient information. Unsolicited patient information is shared via a background task that runs the following option:

- SEND BATCH Z11S TO SITES FOR RECORD UPDATES \[AYCB SEND Z11s\]

Patches IVMB\*2\*891 and IVMB\*2\*900 modify Z11 transmission screens used by the following functions as indicated:

- For both *Unsolicited Z11 transmissions* and *Solicited Z11 transmissions*, patient Z11s will be screened on the AAC INDICATOR field (#31.5) regardless of the Enrollment Status.
- Patient records with a VETERANS ID & VERIFICATION ACCESS file (#300.11) record having an ELIGIBILITY STATUS field (#3) of either "PENDING VERIFICATION" or "PENDING RE-VERIFICATION" \[regardless of ENROLLMENT STATUS (#3) in the ENROLLMENT file (#300.132)\], will screen Z11 message generation based on the respective IVM MASTER CLIENT file (#300.12) AAC INDICATOR field (#31.5).

All Z11 transmissions sent to VistA sites from the HEC Enrollment system are now screened based on the AAC INDICATOR (#31.5) \[in the IVM Master Client file (#300.12)\] with the following values:

- “PENDING RECEIPT OF DATA FROM AUSTIN”
- “QUERY PENDING”
- “DATA PENDING REVIEW”

The screening process applies to solicited Z11 messages that are queried through the HEC Enrollment system from the Vista sites and unsolicited Z11 messages sent as part of the background task that is indicated above.

Prior to installing these patches, the HEC Enrollment system would only screen for unsolicited Z11 messages for \[patients that had Enrollment Statuses of “PENDING; ELIGIBILITY STATUS IS UNVERIFIED”\] based on the following AAC INDICATOR (#31.5) value:

- “PENDING RECEIPT OF DATA FROM AUSTIN”

However, these new patches modify Z11 screening so two additional AAC INDICATOR (#31.5) values for both solicited Z11 messages (triggered through a Vista site query) and unsolicited Z11 messages. Additionally, the requirement that the patient have an Enrollment Status of “PENDING; ELIGIBILITY STATUS IS UNVERIFIED” before applying these AAC INDICATOR screens has been removed.

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the HEC Legacy system.

The modifications made to the HEC system are in conjunction with the following patches: DG\*5.3\*716, and IVMB\*2\*849.

## ## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no related documents with this patch.

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

# # *User Release Notes*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Features, Functions, Modifications, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Two AAC INDICATORS statuses added to IVM Master Client file values that screen the Z11 messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary functionality delivered with these patches consists of adding two AAC INDICATOR statuses to the existing Z11 screens and applying the screen on the AAC INDICATOR statuses regardless of Enrollment Status.

When a Z11 message query is generated from a VistA site, the HEC Enrollment system will automatically provide a solicited response and screen any patient that has the following AAC INDICATOR (#31.5) values:

- “QUERY PENDING”
- “DATA PENDING REVIEW”

In addition to this new screen functionality, another current feature screens Z11 messages for patients having the following AAC INDICATOR (#31.5) value:

- “PENDING RECEIPT OF DATA FROM AUSTIN”

For all unsolicited Z11 messages, the new screen functionality will affect patients that have any Enrollment Status (not just those with an Enrollment Status of PENDING; ELIGIBILITY STATUS IS UNVERIFIED).

### ### New Bulletin Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a solicited Z11 is queried from a VistA, site the HEC Enrollment system will automatically generate a Z11 message based on an AAC INDICATOR (#31.5) for all pending statuses. The following bulletin will be returned to a querying site when a Z11 is not generated because a patient has a pending status.

- “HEC UNABLE TO RESPOND TO QUERY – ENROLLMENT RECORD PENDING”

# *Technical Release Notes*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVMB\*2\*849 must be installed before IVMB\*2\*891 (Pending Verification Changes).

IVMB\*2\*891 must be installed before patch IVMB\*2\*900 (Fix AAC Indicator Check for ORU Z11’s).

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no changes made to the Data Dictionary with this patch.

## Modifications to HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no changes made to the HL7 Messaging with this patch.

### ### *Modifications to Routines*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVMB\*2\*891 consist of changes that affect the \[AYCHBQRY\] and \[AYCHLSA4\] routines.

The following table illustrates the changes that were made to the routines before and after the patch IVMB\*2\*891 was installed.

|                  |                  |                 |                                                         |
|------------------|------------------|-----------------|---------------------------------------------------------|
| Routine Name | Before Patch | After Patch | Patch List                                          |
| AYCHBQRY         | 9113968          | 9646348         | 642,662,703,811,849,891                                 |
| AYCHLSA4         | 7942268          | 7984991         | 412,435,473,452,458,455,627,686,793,800,811,814,849,891 |

### IVMB\*2\*900 consist of changes that affect the \[AYCHLSA4\] routine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table illustrates the changes that were made to the routine before and after the patch IVMB\*2\*900 was installed.

|                  |                  |                 |                                                             |
|------------------|------------------|-----------------|-------------------------------------------------------------|
| Routine Name | Before Patch | After Patch | Patch List                                              |
| AYCHLSA4         | 7984991          | 7976349         | 412,435,473,452,458,455,627,686,793,800,811,814,849,891,900 |

### ## Enrollment Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no modifications made to the Enrollment Trigger Events with this patch.