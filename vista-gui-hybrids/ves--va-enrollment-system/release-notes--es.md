---
title: Release Notes ES 6.2
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: active
pkg_ns: VES
patch_ver: 6.2
patch_id: VES*6.2
group_key: VES:VES:6.2
file_numbers: []
security_keys: []
menu_options: 0
description: '- Introduction - Purpose - Audience - This Release - Enhancements and Modifications - Defects and Fixes - Known Issues - [Product...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 3139
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: September 2022
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_2_rn.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_2_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=183
audit_applied: '2026-05-31'
master_source: Release Notes ES 6.2
master_pub_date: September 2022
consolidated_from: 12 versions
prior_versions:
- Release Notes ES 6.0.1
- Release Notes ES 6.0
- Release Notes ES 6.1.1
- Release Notes ES 6.1
- Release Notes ES 6.10
- Release Notes ES 6.2.1
- Release Notes ES 6.2.2
- Release Notes ES 6.3
- Release Notes ES 6.4
- Release Notes ES 6.8
- Release Notes ES 6.9
consolidated_title: release notes es
---

![](release-notes-es-6-2/001.png)

September 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [Enhancements and Modifications](#enhancements-and-modifications)
  - [Defects and Fixes](#defects-and-fixes)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The mission of the VA OIT Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.
The VA's goals for its Veterans and families include:
- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran's personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.
To assist in meeting these goals, the Eligibility and Enrollment (E&E) program will provide enterprise wide enhancements and sustainment for the following systems/applications:
- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.
- The Veteran's On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.
E&E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care. Key enhancements to be completed include Pending Eligibility Determination, fixes to the VHA Enrollment System, Date of Death, Internal Controls, Workflow, Veterans Financial Assessment, converting of Military Service Data Sharing (MSDS) to Enterprise Military Information Service (eMIS), Manage Relationships, Veteran Contact Service and support for VES Integrated Veteran Care (IVC) Systems Impact (VES/IVC SI).

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to announce the release of the VES 6.2. This release, developed in Java technology, contains E&E development and upgrade efforts. This release includes enhancements and defect fixes to support Enrollment System Modernization (ESM), VES/IVC SI and VES Sustainment.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VES 6.2 and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VES will be upgraded from Version 6.1.1 to Version 6.2 and hosted by Amazon Web Services.

The following sections provide a summary of the enhancements and updates to the existing software and any known issues for VES 6.2.

## Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 shows the enhancements and modifications included in the VES 6.2 release as tracked in Atlassian Jira.

<table>
<caption><p><span id="_Ref533696768" class="anchor"></span>Table 1: VES 6.2 Enhancements and Modifications</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Jira Epic #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Summary</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://vajira.max.gov/browse/VES-12472">VES-12472</a></td>
<td>Standardize List of Ineligible Reasons and Add Rules</td>
</tr>
<tr class="even">
<td><a href="https://vajira.max.gov/browse/VES-17490">VES-17490</a></td>
<td>Update Rules for Not Eligible Reasons</td>
</tr>
<tr class="odd">
<td><a href="https://vajira.max.gov/browse/VES-22133">VES-22133</a></td>
<td>Change Application Date Field Label on Enrollment Tab</td>
</tr>
<tr class="even">
<td><a href="https://vajira.max.gov/browse/VES-22326">VES-22326</a></td>
<td>HUD-VASH Phase 2: Update "Expanded MH Care" Rule</td>
</tr>
<tr class="odd">
<td><a href="https://vajira.max.gov/browse/VES-22398">VES-22398</a></td>
<td>Change VHAP Assigned to Clinical Evaluation SRRO</td>
</tr>
<tr class="even">
<td><a href="https://vajira.max.gov/browse/VES-22399">VES-22399</a></td>
<td>Change VHAP to Humanitarian for Those Pending Proof of Qualifying Military Service</td>
</tr>
<tr class="odd">
<td><a href="https://vajira.max.gov/browse/VES-22400">VES-22400</a></td>
<td>Update Functionality for Removing All SC-Rated Disabilities</td>
</tr>
<tr class="even">
<td><a href="https://vajira.max.gov/browse/VES-22401">VES-22401</a></td>
<td>Change Rules for Placing Records in Not Eligible</td>
</tr>
<tr class="odd">
<td><a href="https://vajira.max.gov/browse/VES-22478">VES-22478</a></td>
<td>Update VHAP Descriptions</td>
</tr>
</tbody>
</table>

<span id="_Ref533696768" class="anchor"></span>Table 1: VES 6.2 Enhancements and Modifications

VES v5.18 added a lookup table containing a list of selectable Ineligible Reason Codes and added the Ineligible Reason Code selection field to the Edit Eligibility screen. The Ineligible Reason free text field was still available and, if blank, would be automatically populated with the value of the Ineligible Reason dropdown. With VES v6.2, the Ineligible Reason field label is changed, and usage of the Ineligible Reason free-text field is discontinued and removed from the user interface. All ineligible records will now have a standardized Ineligible Reason from the dropdown assigned. New business rules are implemented for processing Veterans Benefits Administration (VBA) data, entry of Service Connection (SC) data and VHA Profile (VHAP) assignment based on the value of the Ineligible Reason.

- Under the Edit Eligibility tab, the current "Ineligible Reason" free-text and "Ineligible VARO Decision" fields are removed from the display and the "Ineligible Reason Code" field label is renamed "Ineligible Reason".

![](release-notes-es-6-2/002.png)

<span id="_Toc111471032" class="anchor"></span>Figure : Edit Eligibility Tab – Ineligible Reason Dropdown

- Under the Overview tab, the "Ineligible Reason Code" field is renamed "Ineligible Reason" and the "Ineligible Reason" free-text field is removed.

![](release-notes-es-6-2/003.png)

<span id="_Toc111471033" class="anchor"></span>Figure : Overview Tab – Ineligible Reason Field

- Under the Eligibility tab -\> Other Ineligibility section, the "Ineligible VARO Decision" field is removed and the "Ineligible Reason" value displayed is the standardized ineligible reason assigned for the person.

![](release-notes-es-6-2/004.png)

<span id="_Toc111471034" class="anchor"></span>Figure : Other Ineligibility Section - Ineligible Reason Field

- Under the Eligibility History tab -\> Other Ineligibility section, the value for the "Ineligible Reason" field maps to the standardized ineligible reason.
- Records will be seeded with the standardized ineligible reasons.
  - For records with free text but no standardized ineligible reason assigned, the respective standardized ineligible reason value will be assigned based on mapping provided by stakeholders.
  - As a temporary solution for records that cannot be auto-assigned one of the currently identified list of eight ineligible reasons, a new ineligible reason of "other" will be used and will display as greyed out for all users who do not have the "Edit Fugitive Felon Program Reason" capability.

![](release-notes-es-6-2/005.png)

<span id="_Toc111471035" class="anchor"></span>Figure : Ineligible Reason - Other

- Upon completion of the record seeding and cleanup, VES will send all records with a standardized Ineligible Reason to correlated VistA sites via the ZIE segment of a Health Level Seven (HL7) ORU/ORF-Z11 message.
- When a VES user assigns an Ineligible Reason to a record that has one of the six ineligible reasons (Bad Conduct General Court Martial, Dishonorable Discharge, DVA 12D w/o Chapter 17, DVA 12C, Fugitive Felon Program (FFP)) or "ACDUTRA Only", and the person's record has the Military Sexual Trauma (MST) Indicator set to "Yes", VES will not assign the Secondary Eligibility Code of SPECIAL TX AUTHORITY CARE to the record.
  - Existing records meeting these criteria will be cleaned up to remove the SPECIAL TX AUTHORITY CARE Secondary Eligibility Code.
- When a VES user selects the "Remove All Rated SC Disabilities" button, VES will allow and accept entering an Ineligible Date and Reason without having to accept changes first, and will clear all data from the following fields:
  - Service Connected: %
  - Effective Date of Combined Evaluation
  - Rated SC Disabilities
  - Receiving VA Disability Compensation
  - Total Monthly Check Amount
  - Annual Check Amount
  - Unemployable
- The user interface under the Eligibility tab is updated to enable / disable / display error for manual entries of SC% and Ineligible information based on the below matrix.

> *Sample Error Message*: SC% Zero is not valid for bar-to-benefits records and/or when Veteran Indicator is "No".

<table>
<caption><p><span id="_Toc111471030" class="anchor"></span>Table : SC% / Ineligible Information Manual Entry Matrix</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SC %</strong></th>
<th><strong>Vet Indicator</strong></th>
<th><strong>Ineligible Date</strong></th>
<th><strong>Ineligible Reason</strong></th>
<th><strong>Manual Entry of Inel. Date</strong></th>
<th><strong>Manual Entry of Inel. Reason</strong></th>
<th><strong>Manual Entry of SC % = 0 </strong></th>
<th><strong>Manual Entry of SC % &gt; 0</strong></th>
<th><strong>Display Error upon Accept/Review OR Save Record</strong></th>
<th><p><strong>Requirement/</strong></p>
<p><strong>Statement</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NULL</td>
<td>N</td>
<td>Y</td>
<td>Not Bar-to-benefits</td>
<td></td>
<td></td>
<td>Disallow</td>
<td></td>
<td></td>
<td>When SC% is NULL, Vet Indicator is No, Ineligible Date exists with a not bar-to-benefits reason, VES user is not allowed to enter SC% of zero.</td>
</tr>
<tr class="even">
<td>NULL</td>
<td>N</td>
<td>Y</td>
<td>Bar-to-benefits</td>
<td></td>
<td></td>
<td>Disallow</td>
<td></td>
<td></td>
<td>When SC% is NULL, Vet Indicator is No, Ineligible Date exists with a bar-to-benefits reason, VES user is not allowed to enter SC% of zero.</td>
</tr>
<tr class="odd">
<td>NULL</td>
<td>N (Change to Y)</td>
<td>Y</td>
<td>Bar-to-benefits</td>
<td></td>
<td></td>
<td>Disallow</td>
<td></td>
<td></td>
<td>When SC% is NULL, VES user changes Vet Indicator from No to Yes, Ineligible Date exists with a bar-to-benefits reason, VES user is not allowed to enter SC% of zero.</td>
</tr>
<tr class="even">
<td>NULL</td>
<td>N (Change to Y) VI remains Y</td>
<td>Y</td>
<td>Not Bar-to-benefits</td>
<td></td>
<td></td>
<td>Allow</td>
<td></td>
<td>Save Record</td>
<td>When SC% is NULL, VES user changes Vet Indicator from No to Yes, Ineligible Date exists with a not bar-to-benefits reason, VES user is allowed to enter SC% of zero and save the record.</td>
</tr>
<tr class="odd">
<td>Is = 0</td>
<td>Y</td>
<td>NULL</td>
<td>NULL</td>
<td>Allow</td>
<td>Bar-to-benefits</td>
<td></td>
<td></td>
<td>Y</td>
<td>When SC% is zero, Vet Indicator is Yes, Ineligible Date is entered with a bar-to-benefits reason, VES user is not allowed to save the record. An error message will be displayed.</td>
</tr>
<tr class="even">
<td>Is = 0</td>
<td>N</td>
<td>NULL</td>
<td>NULL</td>
<td>Allow</td>
<td>Bar-to-benefits</td>
<td></td>
<td></td>
<td>Y</td>
<td>When SC% is zero, Vet Indicator is No, Ineligible Date is entered with a bar-to-benefits reason, VES user is not allowed to save the record. An error message will be displayed.</td>
</tr>
<tr class="odd">
<td>Is = 0</td>
<td>Y</td>
<td>NULL</td>
<td>NULL</td>
<td>Allow</td>
<td>Not Bar-to-benefits</td>
<td></td>
<td></td>
<td>Save Record</td>
<td>When SC% is zero, Vet Indicator is Yes, Ineligible Date is entered with a not bar-to-benefits reason, VES user is allowed to save the record.</td>
</tr>
<tr class="even">
<td>Is = 0</td>
<td>N</td>
<td>NULL</td>
<td>NULL</td>
<td>Allow</td>
<td>Not Bar-to-benefits</td>
<td></td>
<td></td>
<td>Y</td>
<td>When SC% is zero, Vet Indicator is No, Ineligible Date is entered with a not bar-to-benefits reason, VES user is not allowed to save the record. An error message will be displayed.</td>
</tr>
</tbody>
</table>

<span id="_Toc111471030" class="anchor"></span>Table : SC% / Ineligible Information Manual Entry Matrix

- When an Ineligible Date is assigned to a record and an update is received from VBA, any SC data received is ignored and a work item is created.

![](release-notes-es-6-2/006.png)

<span id="_Toc111471036" class="anchor"></span>Figure : Work Item Detail

- When a VES user clears the Ineligible Date and Ineligible Reason of "Fugitive Felon Program (FFP)" and saves the record, VES will clear the Ineligible Date and Ineligible Reason and initiate an automatic VBA query request.
- A new Clinical Evaluation eligibility for MST clinical reminder to be triggered in Computerized Patient Record System (CPRS) is added to VES and will be shared with VistA on the ZEL segment of the HL7 ORU/ORF-Z11 message.
- The descriptions of the following VHAPs are updated:
  - Veteran Restricted Med Benefits
  - Non Veteran Other Restricted Med Benefits
  - Ineligible
  - Restricted Examination Only
  - Humanitarian
  - Applicant in Process
- VHAP assignments are updated and VES shares the records with VistA:
  - When a record's Eligibility Status is "Pending" with Pending Reason "Pending Proof of Qualifying Military Service", and the Enrollment Status is either "Pending: Eligibility Status is Unverified" or "Closed Application", VES assigns the Humanitarian VHAP to the record.
- The rules for placing records in "Not Eligible" are updated:
  - When a VES user tries to enter an Ineligible Date and Ineligible Reason for a record with Eligibility Status of "Pending Verification/Re-verification", VES displays an error message indicating that an Ineligible record must always be Verified and does not save the changes.
  - When a VES user tries to modify the Eligibility Status to "Pending Verification/Re-verification" on a record that has the Ineligible Date and Ineligible Reason populated, VES displays an error message indicating that the Ineligible record must always be Verified and does not save the changes.
  - When a VOA/HCA update is received on a record that has the Ineligible Date and Ineligible Reason populated, VES rejects the update, creates a work item, and does not set the record to pending or execute any downstream queries or recalculations.
  - With the VES 6.2 rule that all Ineligible records should be in Verified status, the rules that set eligibility status to Pending Verification based on evaluation of military service information from a VOA update or existing data within the Administrative Data Repository (ADR) will not be executed.
- When a user accepts changes on the Eligibility tab for a record with the Self-Reported Registration Only Reason of "Clinical Evaluation", Veteran Indicator set to "No" and an Ineligible Date assigned, VES will not display an error message and will save the record.

As a continuation of the Housing and Urban Development-Veterans Affairs Supportive Housing (HUD-VASH) workflow introduced to VES in version 6.1, with version 6.2 VES will also be updated to prevent the VES user from assigning the Primary Eligibility Code of "Expanded MH Care Non-Enrollee" to a person who is not eligible.

- When a VES user attempts to save a record with Primary Eligibility of "Expanded MH Care Non-Enrollee", and that record also has an Ineligible Date, or if the user attempts to assign Expanded OTH factor to an ineligible record, VES will display an error message informing the user that the Primary Eligibility of "Expanded MH Care Non-Enrollee" is not valid when the Ineligible Date is populated, and not save the record.
- "Expanded MH Care Non-Enrollee" Primary Eligibility Code will be removed from ineligible records and Eligibility and Enrollment rules will be recalculated.
- VES will no longer accept an MH OTH Factor received from VistA if there is an Ineligible Date on the VES record.

With version 6.2, all instances of the label "Application Date" are updated to display "Application Received Date" on the VES user interface.

- Enrollment Screen
- Enrollment History Screen
- Overview Screen
- Eligibility Screen
- Eligibility History Screen
- Edit Current Eligibility Screen

![](release-notes-es-6-2/007.png)

<span id="_Toc111471037" class="anchor"></span>Figure : Application Received Date Label Example

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists the VES Sustainment defects and fixes and corresponding Jira issue numbers included in VES 6.2.

<table>
<caption><p><span id="_Ref99965903" class="anchor"></span>Table 3: VES Sustainment Defects and Fixes in VES 6.2</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jira Issue #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-17790</td>
<td><p><strong>Defect</strong>: The VBA query response is improperly handled.</p>
<p><strong>Fix</strong>: When a solicited message response is returned with no data on file, the call to the VBA rule is prevented in order to prevent the calculation based on previous verified and pending verification status. The status and reason will be updated, and the flow will be ended.</p></td>
</tr>
<tr class="even">
<td>VES-21146</td>
<td><p><strong>Defect:</strong> VES modifies IVM test status and Priority Group after eligibility update.</p>
<p><strong>Fix</strong>: Restricted financial changes when eligibility is updated.</p></td>
</tr>
<tr class="odd">
<td>VES-23615</td>
<td><p><strong>Defect:</strong> Remove references to "HL7_ARCHIVE_TRANSACTION_LOG".</p>
<p><strong>Fix</strong>: Permanently removed all references to the archive table.</p></td>
</tr>
<tr class="even">
<td>VES-24421</td>
<td><p><strong>Defect</strong>: There is a null pointer exception on the 10-10EZ PDF import for VOA.</p>
<p><strong>Fix</strong>: Added null checks during generation of the 10-10EZ PDF.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref99965903" class="anchor"></span>Table 3: VES Sustainment Defects and Fixes in VES 6.2

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- VES 6.2 Release Notes are uploaded to the [VA Software Document Library](http://www.va.gov/vdl/).
- Additional reference documentation related to this release is stored in GitHub.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Release Notes ES 6.8

## Change Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                                                                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------|
| VES-10646 | Veteran Medical Benefit Plan (VMBP): Extended Care (EC)                                                                  |
| VES-18141 | Add and Change Letters                                                                                                   |
| VES-18143 | Auto-Generate Not Eligible Letters                                                                                       |
| VES-20907 | Health Plan Administration / Integration                                                                                 |
| VES-21811 | Enable Communications History of Letters Being Triggered                                                                 |
| VES-24422 | Add Self-Identified Gender for Spouse                                                                                    |
| VES-26601 | Update Self-Identified Gender Identity (SIGI) Values & 10-10EZ/EZR Forms                                                 |
| VES-30308 | Change Combat Veteran Rules (Promise to Address Comprehensive Toxics (PACT) Act) and Toxic Exposure Risk Activity (TERA) |
| VES-30309 | Create SERVICE Act Indicator                                                                                             |
| VES-36635 | North Chicago Automated Batch Process (Employees)                                                                        |

## Epics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Key</strong></th>
<th><strong>Summary</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-20931</td>
<td>Enter/Edit Insurance Data in Veteran Family Medical Program (VFMP) System (Medicare)</td>
<td>As a VFMP Eligibility system, I need the ability to enter/key Insurance information contained in/written on the application, so that I can maintain a record of the key Insurance information.</td>
</tr>
<tr class="even">
<td>VES-20944</td>
<td>Apply Automated Eligibility Rules for Multiple VFMPs</td>
<td>As a VFMP Eligibility system, I need the ability to apply automated eligibility business rules for multiple Health Care Programs, so that I can manage the eligibility status for multiple Health Care Programs.</td>
</tr>
<tr class="odd">
<td>VES-20952</td>
<td>Assign Denial Reason to Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) Records in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to create a denial reason and discontinue processing eligibility for Standard CHAMPVA, so that I can create a denial reason and discontinue processing eligibility when the categories for eligibility are not met.</td>
</tr>
<tr class="even">
<td>VES-20953</td>
<td>Generate and Send Denial Letter to Person in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the reason(s) for denial and appeal rights, so that I can communicate via correspondence reasons for denial and appeal rights.</td>
</tr>
<tr class="odd">
<td>VES-20954</td>
<td>Generate and Send Acceptance Letter with ID Card to Person in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the enrollment status of "eligible" as well as additional instructions and ID card, so that I can generate notification correspondence of enrollment "eligible" and additional instructions with an ID card to the applicant.</td>
</tr>
<tr class="even">
<td>VES-20956</td>
<td>Provide Ability to Update and Record Eligibility Status Changes in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to provide the ability to record changes in eligibility status as the result of updated information received from authoritative sources, so that I can update information received from authoritative sources.</td>
</tr>
<tr class="odd">
<td>VES-20959</td>
<td>Allow a Person to be a Sponsor and Beneficiary in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to allow a person to be both a sponsor and a beneficiary within the Standard CHAMPVA program, so that a person when applicable is both determined by eligibility rules a sponsor and a beneficiary within the Standard CHAMPVA program.</td>
</tr>
<tr class="even">
<td>VES-20965</td>
<td>Identify a Person for Medicare Verification in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to identify/select a person for Medicare Verification based on a pre-defined, configurable date (annually, semi-annually, monthly, and quarterly) or business rules, so that I can determine eligibility based on Medicare Verification.</td>
</tr>
<tr class="odd">
<td>VES-20966</td>
<td>Re-calculate Person for Medicare Verification in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to re-calculate Medicare Eligibility for persons selected for Medicare Verification and disentitle or reinstate the person from CHAMPVA based on business rules, so that I can update the applicant's eligibility.</td>
</tr>
<tr class="even">
<td>VES-20994</td>
<td>Re-Process Eligibility for Dependent Identified in Centers for Medicare and Medicaid Services (CMS) Data in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to re-process eligibility for the dependents identified by CMS upon receipt of solicited Medicare information, so that I can determine eligibility.</td>
</tr>
<tr class="odd">
<td>VES-20998</td>
<td>Enroll FMP Applicants in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to automatically enroll Veterans, as the result of the receipt of a valid registration form, so that I can update eligibility for specified program.</td>
</tr>
<tr class="even">
<td>VES-21003</td>
<td>Register VFMP Person in Meds by Mail Group via Eligibility Plus file</td>
<td>As a VFMP Eligibility system, I need the ability to register a person who is enrolled in Standard, Caregiver CHAMPVA, Spina Bifida (SB) or Children of Women Vietnam Veterans (CWVV) plan, in the Meds by Mail group, so that I can update eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21005</td>
<td>Register Specific Enrolled Persons to Pharmacy Benefits Manager via Eligibility Plus file</td>
<td>As a VFMP Eligibility system, I need the ability to register a person who is enrolled in the Standard, Caregiver CHAMPVA, SB or CWVV plan, in the PHARMACY BENEFIT MANAGER group, so that I can determine eligibility.</td>
</tr>
<tr class="even">
<td>VES-21011</td>
<td>Provide Response to Query Indicating Person is Not Found in OCC</td>
<td>As a VFMP Eligibility system, I need the ability to prepare and return a response to a request or query indicating the person is not found when the person is not enrolled in any OCC Health Care Plans/ Groups, so that I can determine eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21051</td>
<td>Indicate Additional Documents to be Enclosed with the Generated Correspondence in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to indicate, as part of the correspondence, additional documents that are to be "enclosed" with the generated correspondence, so that I can include additional documents to be "enclosed" with the generated correspondence.</td>
</tr>
<tr class="even">
<td>VES-21058</td>
<td>Send Automatic Denial Correspondence from VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to send automatic denial correspondence based on the specific denial reason in order to comply with the Appeals Modernization process, so that I can send automatic denial correspondence for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21065</td>
<td>Support Master Person Index (MPI) Integration with Veteran Sponsors in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to support MPI integration for Veteran Sponsors for Family Member Programs, so that I can support MPI integration for Family Member Programs.</td>
</tr>
<tr class="even">
<td>VES-21066</td>
<td>Support MPI Integration with Beneficiary Applicants in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to support MPI integration for beneficiary applicants for Family Member Programs, so that I can support MPI integration for Family Member Programs.</td>
</tr>
<tr class="odd">
<td>VES-21086</td>
<td>Receive and Process Requests via Claims Processing System Interface in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to receive and process a query from the Claims Processing System for eligibility status on date of service and eligibility period information, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21088</td>
<td>Provide Eligibility Information to any VAMC from VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to access and display eligibility information to any VAMC, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21108</td>
<td>Provide Ability to Send Daily Eligibility File to ClaimsXM from VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing eligibility information to ClaimsXM, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21119</td>
<td>View VFMP Eligibility Status in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to view eligibility status information related to any VFMP program, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21120</td>
<td>View VFMP Eligibility Period Information in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to view eligibility period information (dates) related to any VFMP program, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21123</td>
<td>View VBA Information in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to view VBA information for a person, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21129</td>
<td>Re-print or Re-issue Enrollment ID Cards in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to reprint or re-issue enrollment ID cards, so that I can reprint or re-issue enrollment ID cards for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21348</td>
<td>Claims Processing and Eligibility (CP&amp;E) Migration for CHAMPVA Standard (M-Development)</td>
<td>Migration of CHAMPVA Standard</td>
</tr>
<tr class="odd">
<td>VES-21636</td>
<td>Process CHAMPVA Remarried Widow</td>
<td>Process CHAMPVA Remarried Widow</td>
</tr>
<tr class="even">
<td>VES-21637</td>
<td>Process CHAMPVA Medicare Rules Phase 2</td>
<td>Process CHAMPVA Medicare Rules Phase 2</td>
</tr>
<tr class="odd">
<td>VES-22314</td>
<td>Enable Communications History of Letters Being Triggered</td>
<td>When the Mail button is selected VES captures the details of the trigger (Name, Date, Time, Letter Type) and display this in the history for others to view.</td>
</tr>
<tr class="even">
<td>VES-22332</td>
<td>CP&amp;E Data Migration RSD</td>
<td>CP&amp;E Data Migration RSD</td>
</tr>
<tr class="odd">
<td>VES-23169</td>
<td>Send CP&amp;E Eligibility Plus Files</td>
<td>Send CP&amp;E Eligibility Plus Files: Draft, review, and approve</td>
</tr>
<tr class="even">
<td>VES-26457</td>
<td>Manage Spina Bifida Eligibility</td>
<td>Manage Spina Bifida Eligibility: Draft, review, and approve</td>
</tr>
<tr class="odd">
<td>VES-26664</td>
<td>Enter/Edit Foreign Phone Number in VFMP System</td>
<td>As a VFMP Eligibility system, I need the ability to enter a Foreign/International phone number</td>
</tr>
<tr class="even">
<td>VES-28605</td>
<td>Manage Marriage and Remarriage Dates</td>
<td>Manage Marriage and Remarriage Dates</td>
</tr>
<tr class="odd">
<td>VES-29674</td>
<td>VFMP Overview Screen Support for CWVV and SB</td>
<td>VFMP Overview Screen - Add CWVV and SB</td>
</tr>
<tr class="even">
<td>VES-29676</td>
<td>View VFMP Sponsor Information - CWVV and SB</td>
<td>View VFMP Sponsor Information - CWVV and SB</td>
</tr>
<tr class="odd">
<td>VES-29688</td>
<td>Manage VFMP Sponsor SB and CWVV Information</td>
<td>Manage VFMP Sponsor SB and CWVV Information</td>
</tr>
<tr class="even">
<td>VES-29689</td>
<td>View VFMP Beneficiary Spina Bifida Program</td>
<td>View VFMP Beneficiary Spina Bifida Program</td>
</tr>
<tr class="odd">
<td>VES-29691</td>
<td>View VFMP Beneficiary Children of Women Vietnam Vets Program</td>
<td>View VFMP Beneficiary Children of Women Vietnam Vets Program</td>
</tr>
<tr class="even">
<td>VES-29703</td>
<td>Eligibility End and Restart Changes</td>
<td>Eligibility End and Restart Changes</td>
</tr>
<tr class="odd">
<td>VES-29705</td>
<td>Manage Foreign Medical Eligibility</td>
<td>Manage Foreign Medical Eligibility</td>
</tr>
<tr class="even">
<td>VES-30135</td>
<td>Update SIGI Values &amp; 10-10EZ/EZR Forms (VES)</td>
<td>SIGI values need to be updated to match VA directive 1341.<br />
Existing 10-10EZ and 10-10EZR forms also need to be updated to the latest version which includes SIGI values matching Directive 1341 and removal of "Are you an Indian" question</td>
</tr>
<tr class="odd">
<td>VES-30508</td>
<td>Solution Architecture and Design</td>
<td>Solution Architecture and Design </td>
</tr>
<tr class="even">
<td>VES-31010</td>
<td>Create SERVICE Act Indicator (VES)</td>
<td>As a VES User, when a Veteran has Southwest Asia and COMPACT Act is Yes. Assign SERVICE Act as a Secondary Eligibility Code (treatment authority).<br />
As a VES User, when a Veteran has Combat Eligibility and COMPACT Act is Yes. Assign SERVICE Act Secondary Eligibility Code.</td>
</tr>
<tr class="odd">
<td>VES-31619</td>
<td>Phase 3 - Remove Z07 Inconsistency Checks from VistA to VES (VES)</td>
<td>61 total inconsistencies are included and will be broken down between additional phases.<br />
Currently there are Z07 transmission blocks that are triggered as the result of outbound message from VAMCs &amp; CBOCs going (or not going) from VistA to VES. Many of these blocks result from the multiple inconsistency checks that are performed by VistA, some of which are not necessary for VES to receive the transmission.  Some unnecessarily serve to reduce the chance of a Z07 effectively leaving VistA in the first place. </td>
</tr>
<tr class="even">
<td>VES-32654</td>
<td>Add Self-Identified Gender for Spouse (VES)</td>
<td>Under the Financials Tab Dependents Sub Tab in VES add the following Self-Identified Genders:<br />
* Female <br />
* Male<br />
* Transgender Female<br />
* Transgender Male<br />
* Other <br />
* Does Not Wish to Disclose<br />
* Non-binary</td>
</tr>
<tr class="odd">
<td>VES-33999</td>
<td>Change Combat Veteran Rules + TERA VHAP Changes - PACT (VES)</td>
<td>TERA VHAP Changes in support of PACT Act<br />
As a VES user, when a new Combat Veteran enrollment is added placed the Veteran in Priority Group 8c or higher.<br />
As a VES user, when a new Combat Veteran enrollment is created and if over the income threshold place in Priority Group 8c if no other eligibility exist.<br />
As a VES user, when a Combat Veteran enrolls outside of their Combat Veteran Eligibility window, place the Veteran if PG8c unless eligible for a higher priority group.<br />
As a VES User, when an existing Combat Veteran in PG 8e/8g and outside of their combat window updates their financial means test calculate to place in PG8c unless eligible for higher priority group.<br />
As a VES User, when an existing Combat Veteran in PG 8e/8g updates their financial means test calculate to place in PG6 unless eligible for higher priority group.</td>
</tr>
<tr class="even">
<td>VES-34003</td>
<td>SERVICE Act VHAP Changes (VES)</td>
<td>SERVICE Act + COMPACT VHAP Changes</td>
</tr>
<tr class="odd">
<td>VES-34349</td>
<td>Phase 4 - Remove Z07 Inconsistency Checks from VistA to VES (VES)</td>
<td>61 total inconsistencies are included and will be broken down between additional phases.<br />
<br />
Currently there are Z07 transmission blocks that are triggered as the result of outbound message from VAMCs &amp; CBOCs going (or not going) from VistA to VES. Many of these blocks result from the multiple (68) inconsistency checks that are performed by VistA, some of which are not necessary for VES to receive the transmission.  Some unnecessarily serve to reduce the chance of a Z07 effectively leaving VistA in the first place. </td>
</tr>
<tr class="even">
<td>VES-36636</td>
<td>Create a Job to Load Employee Records from VAMC Sites to VES</td>
<td>VES will be updated to add the ability to complete a bulk import of employee records from a file.</td>
</tr>
</tbody>
</table>

## Bugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                           |
|-----------|-----------------------------------------------------------------------|
| VES-30117 | VES sending wrong address type in MVI 1302 update                     |
| VES-34138 | VCE Effective Date has the wrong value when returned from E&E service |
| VES-34623 | VBA responses not correctly processed                                 |

### From: Release Notes ES 6.4

## Release Notes for VHA Enrollment System - VES v6.4.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

01-31-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.

The VA's goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran's personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran's On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

## Stories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                                                |
|-----------|--------------------------------------------------------------------------------------------|
| VES-25669 | Update Database to Add New Letter Templates and Update Form Numbers for Existing Templates |
| VES-25670 | Update Code to Support New Letter Templates and Changes to Existing Templates              |
| VES-25671 | Modify 60-Day Banner to Change Which Forms Cause Banner to be Displayed                    |
| VES-25672 | Disable Accept Changes Button on Edit Eligibility Screen When 60-Day Banner is Active      |
| VES-25673 | Rule Changes to Automatically Trigger Letters When Ineligible Reason is Selected           |
| VES-25674 | Add Communication Panel on History Screen                                                  |
| VES-25675 | Edit Eligibility With 60-Day Letter                                                        |
| VES-25676 | Expire Banner When an Ineligible Letter is Sent                                            |
| VES-25924 | DB Update for Delete Date Of Death User Permission                                         |
| VES-25925 | UI Changes for Demographic Person Screen To Control Date of Death Deletion                 |
| VES-25926 | UI Action for Preferred Language Changes                                                   |
| VES-25927 | Z07 Parser Changes for Preferred Language Data                                             |
| VES-25931 | Z05 Builder Changes for Preferred Language Data                                            |
| VES-25932 | Trigger Z05 on a Preferred Language Change                                                 |
| VES-27685 | VES 6.4.0 Production Deployment                                                            |
| VES-25991 | Develop and Integrate Functions to Return a State Code                                     |
| VES-27283 | Update Web Help for VES 6.4.0                                                              |
