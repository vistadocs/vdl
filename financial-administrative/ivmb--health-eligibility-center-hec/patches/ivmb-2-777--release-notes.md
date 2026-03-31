---
title: IVMB*2*777 HEC/VistA Enhancements (HVE) Phase 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: HEC/VistA Enhancements (HVE) Phase 2
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*777
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - enrollment
  - veteran
  - date
  - combat
  - vista
  - changes
  - transmission
  - status
page_count: 0
word_count: 1303
section_count: 8
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p777_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p777_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

HEC/VISTA Enhancements (HVE)

Phase II

Release Notes

IVMB\*2\*777

June 2004

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [Related Documents](#related-documents)
  - [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
    - [Continuous Enrollment Rules Modifications](#continuous-enrollment-rules-modifications)
    - [Combat Veteran End Date and Agent Orange Location Indicator sharing with HEC](#combat-veteran-end-date-and-agent-orange-location-indicator-sharing-with-hec)
    - [Enrollment Letter Modifications](#enrollment-letter-modifications)
- [Technical Release Notes](#technical-release-notes)
  - [Data Dictionary Changes](#data-dictionary-changes)
  - [Enrollment Trigger Events](#enrollment-trigger-events)
  - [HL7 Messaging Changes](#hl7-messaging-changes)
    - [Z07, Full Data Transmission from VAMC to HEC](#z07-full-data-transmission-from-vamc-to-hec)
    - [Z10, Income Test Data Transmission from HEC to VAMC](#z10-income-test-data-transmission-from-hec-to-vamc)
    - [Z11, Enrollment/Eligibility Data Transmission from HEC to VAMC](#z11-enrollmenteligibility-data-transmission-from-hec-to-vamc)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HEC V*IST*A Enhancements (HVE) supports several critical business processes associated with congressionally mandated initiatives. The functional scope of this project was determined at a meeting held in Atlanta the week of January 26, 2004, between the Enrollment Legacy Development Team and representatives of the Chief Business Office (CBO).

HVE is being released in a series of three phases; work on all three phases will occur concurrently. The purpose of a multiple-phase release is twofold:

- It allows for a more rapid release of smaller, less complicated pieces of functionality
- Several components require a clean-up or seeding prior to transmission to the HEC database

Phase I introduced the Military Service Data Inconsistencies Report, which provides information on veteran records with missing or incorrect military service data. Sites first had to run an extract to determine how many inconsistencies existed in the Patient (#2) File so they could estimate the level of effort required to fix them. Confirmation emails were sent to members of the appropriate mail groups at both HEC and V*IST*A. Next, the sites had to run a detailed report that identified the individual veteran records containing inconsistent military service data.

Phase II adds the following functionality:

- Remove BEC as a selectable branch of service (V*IST*A)
- Validate WWII period for Merchant Seaman BOS (V*IST*A)
- MSD field-specific requirements (V*IST*A)
- MSD logical field requirements (V*IST*A)
- Continuous enrollment rules modifications (V*IST*A and HEC Legacy)
- Filipino Veteran (FV) Data (V*IST*A)
- V*IST*A Changes
- Combat Veteran end date sharing with HEC

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the HEC Legacy system.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>DG_5_3_P451_ADTBE_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Menus, Intro, Orientation, etc.</td>
</tr>
<tr class="even">
<td><ul>
<li><p>DG_5_3_P451_REG_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Registration Menu Module (includes MT pending adjudication changes)</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>DG_5_3_P451_SADT_U.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual Supervisor ADT Menu Module</td>
</tr>
<tr class="even">
<td><ul>
<li><p>IVM_2_P56_TM.PDF</p></li>
</ul></td>
<td>Revised IVM V. 2.0 Technical Manual</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>VM_2_P56_UM.PDF</p></li>
</ul></td>
<td>Revised IVM V. 2.0 User Manual</td>
</tr>
</tbody>
</table>

#### ## Acronyms and Definitions

#### Acronyms

|             |                                       |
|-------------|---------------------------------------|
| Acronym | Description                       |
| ADT         | Admissions, Discharges, Transfers     |
| AO          | Agent Orange                          |
| CBO         | Chief Business Office                 |
| EC          | Environmental Contaminants            |
| EGT         | Enrollment Group Threshold            |
| HEC         | Health Eligibility Center             |
| HVE         | HEC V*IST*A Enhancements      |
| IVM         | Income Verification Matching          |
| MT          | Means Test                            |
| NSC         | Non-service-connected                 |
| PIMS        | Patient Information Management System |
| SC          | Service-connected                     |
| VA          | Veterans Administration               |
| VHA         | Veterans Health Administration        |
Definitions
|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term          | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Disenrollment     | Voluntary request from veteran to discontinue enrollment in the VA Health Care system                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| GMT Thresholds    | a.k.a. HUD Indices. Geographical income level thresholds set yearly by the U.S. Department of Housing and Urban Development                                                                                                                                                                                                                                                                                                                                                                                                               |
| HL7               | Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*ist*A HL7 package to assist in transporting data using this specification.                                                                                                                                                                                                                                                                                       |
| IVM               | Income Verification Match. A program designed to verify income and insurance data reported by the veteran with that received from IRS (Internal Revenue Service), SSA (Social Security Administration), and other sources                                                                                                                                                                                                                                                                                                                 |
| Means Test        | Eligibility for VA hospital care and nursing home care is divided into two categories - mandatory and discretionary. An income assessment is made to determine whether a non service-connected veteran, who is not in receipt of VA monetary benefits or otherwise exempt from income assessment, is eligible for cost-free VA medical care. This income assessment is known as "Means Testing". Patients whose income is above the defined income levels must agree to make copayments to VA for outpatient and inpatient care rendered. |
| MT Thresholds     | Income threshold levels set yearly within the VA for the purpose of establishing benefit levels for veterans                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HEC Legacy System | M-based database currently in use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### # User Release Notes

## New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Continuous Enrollment Rules Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the following cases, if the veteran has a previous enrollment record, and would otherwise no longer qualify for enrollment due to Means Test (MT) expiration or change in eligibilities, the veteran will remain continuously enrolled.

- The Enrollment Application Date (and if absent - the Effective Date of Change) is ON or AFTER the EGT Effective Date, AND The Enrollment Category was ENROLLED or In-Process, AND MT was used to place the veteran in a Verified Enrollment Status (Enrollment Category = Enrolled).
- Those veterans whose FIRST Verified Enrollment Status is based on SC 10-100%, Aid and Attendance, Housebound, NSC VA Pension, Eligible for Medicaid, Combat Veteran, Agent Orange (AO) Exposure, or Environmental Contaminants (EC). If there is a change to these eligibilities, the record will not be placed in a REJECTED Enrollment Status but will be continuously enrolled. And, if changes to any of these eligibilities places the record in a Pending; MT required and the MT is completed, the record will not be placed in a REJECTED Enrollment Status based on the MT data but will be continuously enrolled.
- Those veterans whose Enrollment Priority Group was determined solely by their AO Exposure Indicator OR their EC Exposure Indicator, AND whose Application Date (or Effective Date of Change if no Application Date present) is prior to the date specified in the VHA Directive for the AO/EC Sunsetting, AND AO/EC is indicated on that enrollment record.

For these veterans, if there is a change to these eligibilities, the record will not be placed in a REJECTED Enrollment Status, but will instead be continuously enrolled. Likewise, if changes to any of these eligibilities place the record in a PENDING; MT REQUIRED status, and the MT is completed, the record will not be placed in a REJECTED Enrollment Status based on the MT data, but will instead be continuously enrolled.

### Combat Veteran End Date and Agent Orange Location Indicator sharing with HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications have been made to the HL7 ORF/ORU Z07 message processes to transmit (V*IST*A) and receive (HEC) the Combat Veteran Eligibility End Date and the Agent Orange Location Indicator.

### Enrollment Letter Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications have been made to the Enrollment Letters process to prevent the 621A and 623A rejection letters from being sent/resent to Combat Veterans.

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVMB\*2.0\*777 must be installed before patch IVMB\*2.0\*786 (HVE Phase III).

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields will be added to the data dictionaries:

IVM CLIENT INCOME (#300.13) File

|                |             |                                |       |
|----------------|-------------|--------------------------------|-------|
| NODE;PIECE | FLD NUM | FIELD NAME                 |       |
| 10;19          | 101.1       | AGENT ORANGE EXPOSURE LOCATION | \[S\] |
|                |             | K:KOREAN DMZ                   |       |
|                |             | V:VIETNAM                      |       |

## Enrollment Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added COMBAT VETERAN END DATE (.5295) Enrollment Trigger Event

## HL7 Messaging Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Z07, Full Data Transmission from VAMC to HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added Agent Orange Exposure Location to the ZEL Segment of the Z07 message and builder process
- Added Combat Veteran Status Indicator to the ZEL Segment of the Z07 message and builder process
- Added Combat Veteran End Date to the ZEL Segment of the Z07 message and builder process
- The ORF/ORU Z07 messages will be modified to include the following sequences in the ZEL segment:

SEQ-29 AGENT ORANGE EXPOSURE LOCATION

SEQ-36 Not used at this time (for future patch)

SEQ-37 COMBAT VETERAN STATUS (calculated)

SEQ-38 COMBAT VETERAN END DATE

### Z10, Income Test Data Transmission from HEC to VAMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added Means Test Signature Indicator, GMT Threshold, and Hardship Reason to the ZMT Segment

### Z11, Enrollment/Eligibility Data Transmission from HEC to VAMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added Medication Copayment Exemption Status to the ZPD Segment
- Added Ineligible Twx State to the ZIE Segment