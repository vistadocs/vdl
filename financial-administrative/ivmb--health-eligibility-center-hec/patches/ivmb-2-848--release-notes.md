---
title: IVMB*2*848/IVMB*2*849 Enrollment VistA Changes ER Release Notes
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
patch_id: IVMB*2*848
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - enrollment
  - disability
  - table
  - contents
  - date
  - military
  - class
  - retirement
  - reject
  - veteran
page_count: 0
word_count: 3039
section_count: 9
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p848_p849_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p848_p849_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

enrollment vista changes (evc)

early release

Release Notes

IVMB\*2\*848

IVMB\*2\*849

February 2006

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [Related Documents](#related-documents)
- [User Release Notes](#user-release-notes)
  - [New Features, Functions, Modifications, and Enhancements](#new-features-functions-modifications-and-enhancements)
    - [Effective Date of Change Modifications](#effective-date-of-change-modifications)
    - [Enhancements to the Continuous Enrollment Algorithm](#enhancements-to-the-continuous-enrollment-algorithm)
    - [Display and Entry for Military Disability Retirement](#display-and-entry-for-military-disability-retirement)
    - [Display and Entry for Discharge Due to Disability](#display-and-entry-for-discharge-due-to-disability)
    - [Modifications to the Enrollment Priority Algorithm for Enrollment Priority Group 3 Veterans](#modifications-to-the-enrollment-priority-algorithm-for-enrollment-priority-group-3-veterans)
    - [Modification to the Existing Disability Retirement from Military Field](#modification-to-the-existing-disability-retirement-from-military-field)
- [# Technical Release Notes](#technical-release-notes)
  - [Data Dictionary Changes](#data-dictionary-changes)
    - [New Fields](#new-fields)
    - [New Templates](#new-templates)
  - [Modifications to HL7 Messaging](#modifications-to-hl7-messaging)
    - [Modifications to ORF/ORUZ07 Messages](#modifications-to-orforuz07-messages)
    - [Modifications to ORF/ORUZ11 Messages](#modifications-to-orforuz11-messages)
  - [Conversion for Disability Retired from Military field](#conversion-for-disability-retired-from-military-field)
  - [Report of Disability Retirement Data Conversion](#report-of-disability-retirement-data-conversion)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enrollment VistA Changes (EVC) Early Release project supports the technology and business changes that are occurring with the implementation of the Enrollment System Redesign (ESR) project. It includes items that the HEC requested to be fast-tracked from the original (EVC) project and provides modifications to both the VistA and HEC Legacy systems. This project is being released to the field without ESR involvement.

Patch IVMB\*2\*848 provides the following functionality:

- Modifies effective date of change
- Modifies continuous enrollment algorithm
- Adds new fields to the inbound messages (Z07) going from VistA to HEC Legacy
- Adds a new field, Military Disability Retirement, to several files, menu options, and the HL7 ZEL segment
- Adds a new field, Discharge Due to Disability, to several files, menu options, and the HL7 ZEL segment
- Modifies the enrollment priority algorithm for Priority Group 3 veterans with Military Disability Retirement or Discharge Due to Disability
- Updates Means Test exemption for Priority Group 3 veterans with Military Disability Retirement or Discharge Due to Disability
- Continue support of the NED’s use of the Disability Retirement from Military field through usage of Military Disability Retirement and Discharge Due to Disability fields.

Patch IVMB\*2\*849 provides the following functionality:

- Modifies sharing of records with pending status via ORU/ORF~Z11
- Adds new fields to the ZEL segment of ORU/ORF~Z11
- Provides a conversion option to populate the new military disability fields added by Patch IVMB\*2\*848
- Provides a user-initiated status report for the conversion process

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the HEC Legacy system.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following related documents are available for download from the VistA Documentation Library (VDL):

|                          |                                                           |
|--------------------------|-----------------------------------------------------------|
| File Name                | Description                                               |
| DG_5_3_P672_ADTBE_UM.PDF | Revised PIMS, Menus, Intro, Orientation, etc. User Manual |
| DG_5_3_P672_REG_UM.PDF   | Revised PIMS Registration Menu User Manual                |
| DG_5_3_P672_SADT_U.PDF   | Revised PIMS Supervisor ADT Menu User Manual              |
| EAS_1_P62_UM.PDF         | Revised Enrollment Application System V. 1.0 User Manual  |
| IVM_2_P109_TM.PDF        | Revised IVM V. 2.0 Technical Manual                       |

# User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Features, Functions, Modifications, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Effective Date of Change Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The effective date used for the following enrollment statuses is changed to use the date the enrollment status is created.

- Deceased
- Not Eligible, Ineligible Date
- Not Eligible, Refused to Pay Copay

The Effective Date of Change in the HEC and VistA Legacy systems is calculated as shown in the tables below. No cleanup is needed. As records are updated with these statuses, the new rules are applied.

#### VistA Legacy

| STATUS     | Current Vista Value for Effective Date of Change Field | Future VistA Value for Effective Date of Change Field |
|------------|--------------------------------------------------------|-------------------------------------------------------|
| 6 Deceased | Date of Death                                          | The date of death last updated                        |

#### HEC Legacy

*Note*: Changing the date of Death does not change the enrollment status; there will not be a new enrollment record created.

| STATUS                                  | Current HEC Legacy Value for Effective Date of Change Field | Future HEC Legacy Value for Effective Date of Change Field |
|-----------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|
| 6 - Deceased                            | Date of Death                                               | The date the system created this enrollment status         |
| 19 - Not Eligible; Refused to Pay Copay | Effective Date of Current Enrollment                        | The date the system created this enrollment status         |
| 20 - Not Eligible; Ineligible Date      | Ineligible Date                                             | The date the system created this enrollment status         |

### Enhancements to the Continuous Enrollment Algorithm 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are enhancements to the Continuous Enrollment Algorithm. The rules are to be executed in the following order, with the following exceptions:

Current *and* prior enrollment records with any of the following enrollment statuses will be ignored for determination of continuous enrollment:

- Pending Means Test Required,
- Pending Purple Heart Unconfirmed
- Pending Eligibility Status Unverified
- Pending Other
- Pending No Eligibility Code VIVA
- Deceased
- Not Eligible; Ineligible Date

The table below describes the enhancements to the continuous enrollment rules, with the following exceptions:

- A manual override by a HEC User can either reject or continuously enroll a veteran’s enrolment record regardless of the business rules listed in the table below.
- Once an enrollment record is manually placed in a verified enrollment status via the override function, the veteran will not be placed in a rejected enrollment status until a new EGT is set (which could disqualify the veteran from enrollment), or if the record is manually overridden to a rejected status.
- Once a record is in a canceled/declined enrollment status, it will be treated the same as a rejected enrollment status, and not continuously enrolled as long as a veteran stays in a priority group that is not being accepted for new enrollments.

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Conditions</th>
<th>Results</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Current enrollment record has an Application Date that is prior to the EGT Effective Date</p>
<p>AND</p>
<p>Current or any previous enrollment record has an Effective Date of Change that is prior to the EGT Effective date</p></td>
<td>Veteran is continuously enrolled</td>
</tr>
<tr class="even">
<td><p>There is no application date</p>
<p>AND</p>
<p>The earliest Effective Date of change is prior to the EGT Effective Date</p></td>
<td>Veteran is continuously enrolled</td>
</tr>
<tr class="odd">
<td><p>If the current record has an enrollment status of Not Eligible; Refused to Pay Copay</p>
<p>AND</p>
<p>the veteran’s Agrees to Pay Deductible Indicator is being changed from NO to YES</p></td>
<td><p>The system ignores the application date and looks at the ESR Communications Module to see if a 601B OR 601C letter has been triggered for any of the following Communication Statuses:</p>
<p>0-send to AAC</p>
<p>1-sent to AAC</p>
<p>2-mailed by HEC</p>
<p>3-reject at HEC</p>
<p>4-reject by AAC</p>
<p>5- Error by AAC</p>
<p>6-Return by post office</p>
<p>7-mailed by AAC</p>
<p>8-Sent to HEC printer</p>
<p>9-address changed and mailed by AAC</p>
<p>Enrollment record is rejected</p></td>
</tr>
<tr class="even">
<td><p>If the letter was triggered</p>
<p>AND</p>
<p>the Communication Status is one of the above, it infers that an attempt was made to notify the veteran that s/he is not eligible</p></td>
<td>Enrollment record is rejected</td>
</tr>
<tr class="odd">
<td><p>If the letters were <em><strong>not</strong></em> triggered</p>
<p>AND</p>
<p>the Communication Status is Null or value 10-Cancel by the HEC, it is inferred that the veteran has not received notification of his/her ineligible status</p></td>
<td>Veteran is continuously enrolled</td>
</tr>
<tr class="even">
<td><p>If a veteran has ever had a verified enrollment record with an eligibility in the following list then the veteran will be considered continuously enrolled without regard to the rules in the table:</p>
<p>SC 10% or greater and SC% is changed to SC 0% non compensable (total check amount $0 or null)</p>
<p>Aid &amp; Attendance = YES and A&amp;A is now not YES</p>
<p>Housebound = YES and Housebound is now not YES</p>
<p>VA Pension = YES and VA Pension is now not YES</p>
<p>If AO indicator is currently = yes and location is currently = DMZ was entered prior to ESR implementation. (Date for this software to be used will be 12/29/2040 until ESR is implemented. Date will be modified with EVC)</p>
<p>CV End Date expires after Enrollment Application Date To clarify – the VERIFIED record must contain a CV end date and the CV end date must have expired after the Enrollment Application Date or in the absence of an Application Date, the earliest effective date of change.</p>
<p>Veteran is enrolled due to MT status, and a subsequent income year means test was added or edited that would place the veteran in a priority group not being enrolled then Continuously Enroll.</p></td>
<td>Veteran is continuously enrolled</td>
</tr>
</tbody>
</table>

The following table represents requirements to determine if an enrollment record is to be placed in a rejected enrollment status, with the following exception:

- Once an enrollment record is rejected, it will stay rejected as long as the veteran stays in an enrollment priority group that is not being accepted for new enrollments.
- If a determination cannot be made then the decision is to Reject Enrollment

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 36%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><p>If the EGT Setting is Enrollment Decision</p>
<p>AND</p>
<p>The veteran applied for enrollment on or after EGT Effective Date (in the absence of application date use the earliest effective date of change)</p>
<p>AND</p>
<p>a verified enrollment status with one or more of the following eligibility factors exists:</p></th>
<th>AND Eligibility is changed as follows (which results in veteran placed in an Enrollment Priority Group that is not eligible for enrollment):</th>
<th>Enrollment System Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SC 0% compensable (Total check amount is greater than $0)</td>
<td><p>SC 0% noncompensable</p>
<p>(Total check amount is 0 or Null)</p></td>
<td><p>Reject enrollment</p>
<p>(Enrollment Priority Group subpriority e or g)</p></td>
</tr>
<tr class="even">
<td>SC 0% -100%</td>
<td>SC is removed</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>AO and Location = Vietnam</td>
<td>AO Location is changed to DMZ after implementation of priority algorithm that considers AO Location</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>AO and Location = Vietnam</td>
<td>AO Location is changed to Other after implementation of priority algorithm that considers AO Location</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>AO and Location = DMZ</td>
<td>AO Location is changed to Other after implementation of priority algorithm that considers AO Location</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>Agent Orange = Yes</td>
<td>AO = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>Radiation Exposure = Yes</td>
<td>IR = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>Environmental Contaminants = Yes</td>
<td>EC = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>SHAD = Yes</td>
<td>SHAD = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>WWI Eligibility Code New Rules</td>
<td>WWI Eligibility Code is removed</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>Mexican Border War Eligibility Code</td>
<td>Mexican Border War Eligibility Code is removed</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>Purple Heart Indicator = Yes</td>
<td>PH Indicator = No</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>POW Indicator = Yes</td>
<td>POW = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>CV End Date Populated</td>
<td>CV End Date is Removed</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>Discharged due to Disability = Yes</td>
<td>Discharged due to Disability = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>Military Disability Retirement = Yes</td>
<td>Military Disability Retirement = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="odd">
<td>Catastrophic Disability = Yes</td>
<td>Catastrophic Disability = Not Yes</td>
<td>Reject enrollment</td>
</tr>
<tr class="even">
<td>Medicaid = Yes</td>
<td>Medicaid is edited to = No and a means test is completed that places the record in an enrollment priority group that is not being enrolled</td>
<td><p>Reject enrollment</p>
<p>If the veteran has a current MT or other eligibility that qualifies the veteran for enrollment, do not reject.</p></td>
</tr>
<tr class="odd">
<td>MT Status on the first verified enrollment record places the record in a priority group that was enrolled</td>
<td>The Means test is edited or converted by IVM to a Means Test Status that places the record in a priority group not being enrolled</td>
<td><p>Reject enrollment only if the veteran is currently in an enrollment priority group that is not being enrolled.</p>
<p>If the veteran has a current MT or other eligibility that qualifies the veteran for enrollment, do not reject.</p></td>
</tr>
<tr class="even">
<td>MT Hardship was granted on the first verified enrollment record that placed the record in a priority group that was being enrolled</td>
<td>The hardship is removed , converted by IVM, or a new test completed which places the record in a priority group that is not being enrolled</td>
<td><p>Reject enrollment only if the veteran is currently in an enrollment priority group that is not being enrolled.</p>
<p>If the veteran has a current MT or other eligibility that qualifies the veteran for enrollment, do not reject.</p></td>
</tr>
</tbody>
</table>

### Display and Entry for Military Disability Retirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Military Disability Retirement field is added to the following menu options:

- Enter/Edit VIVA Data
- View an Enrollment Record
- Inquire Data Received from DHCP
- Inquire VIVA Data

### Display and Entry for Discharge Due to Disability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Military Disability Retirement field is added to the following menu options:

- Enter/Edit VIVA Data
- View An Enrollment Record
- Inquire Data Received from DHCP
- Inquire VIVA Data

### Modifications to the Enrollment Priority Algorithm for Enrollment Priority Group 3 Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The enrollment priority algorithm has been updated to evaluate a veteran’s qualification to be placed in a PG3
- The means test exemption has been updated for Military Disability Retirement and Discharge Due to Disability fields.

### Modification to the Existing Disability Retirement from Military Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will continue to support the National Enrollment Database (NED) use of the Disability Retirement from Military field through usage of Military Disability Retirement and Discharge Due to disability fields.

# # Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Discharge Due to Disability and Military Disability Retirement Fields replace the old Disability Retired from Military Field in the following files:

- Veterans ID and Verification Access (#300.11)
- IVM Client Income (#300.13)
- Enrollment (#300.132)
- Prioritization Rules (#742024)

### New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Template Type  | Template Name        |
|----------------|----------------------|
| Print Template | IVMG VIEW ENROLLMENT |
| Input Template | IVME ENTER VIVA      |

## Modifications to HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Modifications to ORF/ORU~Z07 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields are added to the ZEL segment:

- Sequence 5 - Military Disability Retirement (Y/N)
- Sequence 39 - Discharge due to Disability (Y/N)

### Modifications to ORF/ORU~Z11 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Modifications for Pending Statuses

- ORF~Z11 messages return Z11s for pending status records.
- ORU~Z11 messages are transmitted for pending status records except the following enrollment statuses:
- Pending, No Eligibility Code
- Pending, Other
- Pending, Eligibility Status is Unverified (where no response has been received from VBA at AAC)

#### New Fields in the ZEL Segment

The following new fields are added to the ZEL segment. These fields are populated by the user-initiated post-installation conversion for Patch IVMB\*2\*849.

- Sequence 5 - Military Disability Retirement (Y/N)
- Sequence 39 - Discharge due to Disability (Y/N)

If the post-installation conversion is not complete at the time the message is sent, the following old value will be sent instead and the conversion of the field will be performed by VistA.

Sequence 5 - Disability Retired from Military (0,1)

## Conversion for Disability Retired from Military field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The conversion included with Patch IVMB\*2\*849 populates the Military Disability Retirement and Discharge Due to Disability fields from the Disability Retired from Military field.

## Report of Disability Retirement Data Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*SPECIAL note: The conversion process may take up to 10 days to complete and should not be started until all sites have installed VistA Patch DG\*5.3\*672.*

After installing Patch IVMB\*2\*849, schedule the task IVMB 849 DISAB RET MIL CONV (Disab. Ret from Mil. Conversion IVMB\*2\*849) using Task Manager (TaskMan) - Schedule/Unschedule Option.

In an effort to control the number of Z11 messages queued to VistA, the conversion must be scheduled to run once an hour (1H). The job is designed to queue a maximum of 50,000 Z11 messages to VistA during each scheduled execution.

The purpose of the conversion is to populate the Military Disability Retirement and Discharge Due to Disability fields based on translation from the Disability Retired from Military field. All involved fields reside on the VETERANS ID & VERIFICATION ACCESS File (#300.11). Upon the conclusion of each execution, a MailMan message reporting status information will be sent to the user who initiated the task. If a user terminates the task, the currently running conversion will soon abort and a status message will be sent.

When the conversion is complete the MailMan message will indicate, "The Disability Retirement Data Conversion has completed successfully." Upon receipt of this notification, unschedule the IVMB 849 DIAB RET MIL CONV option and delete any jobs that are scheduled to run in the future.