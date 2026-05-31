---
title: Release Notes VES 6.11
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: active
pkg_ns: VES
patch_ver: 6.11
patch_id: VES*6.11
group_key: VES:VES:6.11
file_numbers: []
security_keys: []
menu_options: 0
description: '- Release Notes for VHA Enrollment System VES 6.11.0 - Change Requests - Epics -'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 3311
section_count: 5
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: ''
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_11_rn.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_11_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=183
audit_applied: '2026-05-31'
master_source: Release Notes VES 6.11
master_pub_date: ''
consolidated_from: 17 versions
prior_versions:
- Release Notes VES 6.12
- Release Notes VES 6.13
- Release Notes VES 6.14.5
- Release Notes VES 6.14
- Release Notes VES 6.15
- Release Notes VES 6.5.2
- Release Notes VES 6.5.3
- Release Notes VES 6.5.4
- Release Notes VES 6.5.5
- Release Notes VES 6.5
- Release Notes VES 6.6.1
- Release Notes VES 6.6
- Release Notes VES 6.7.1
- Release Notes VES 6.7
- Release Notes VES 6.8.1
- Release Notes VES 6.8.2
consolidated_title: release notes ves
---

## Table of Contents

  - [Release Notes for VHA Enrollment System VES 6.11.0](#release-notes-for-vha-enrollment-system-ves-6110)
  - [Change Requests](#change-requests)
  - [Epics](#epics)
  - [Bugs](#bugs)

## Release Notes for VHA Enrollment System VES 6.11.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10-10-2024

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

## Change Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                    |
|-----------|----------------------------------------------------------------|
| VES-10687 | International Phone Number Updates (Phase 1)                   |
| VES-21827 | Ability to Edit All Employer Details on Personal Subtab        |
| VES-27342 | Add 180-Day Grace Period Indicator in Eligibility Screens      |
| VES-28742 | Other Health Insurance (OHI) - Private - Eligibility Plus File |
| VES-33381 | No OHI Received Indicator                                      |
| VES-36906 | Search & View Historical Correspondence in VFMP System         |
| VES-38900 | Add TERA Letters to VES                                        |
| VES-40511 | VES Site Correlation                                           |
| VES-42564 | Show TRICARE Indicator for All CHAMPVA Beneficiaries           |
| VES-43283 | PACT Act 405 Persian Gulf Deployed Cohort Identifier           |

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
<td>VES-2461</td>
<td>Phase 1: Enhance VistA and VES to include a new field to support Country Code and a new field for the phone number Extension (VES)</td>
<td>As a VES User, I want VistA, VES, and VA Profile to support the International Telecommunication Union - Telecommunication sector (ITU-T) E.164 standard format for geographic areas so that domestic phone numbers are captured, stored, and transmitted to interfacing applications correctly.</td>
</tr>
<tr class="even">
<td>VES-20952</td>
<td>Assign Denial Reason to CHAMPVA Records in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to create a denial reason and discontinue processing eligibility for Standard CHAMPVA, so that I can create a denial reason and discontinue processing eligibility when the categories for eligibility are not met.</td>
</tr>
<tr class="odd">
<td>VES-20953</td>
<td>Generate and Send Denial Letter to Person in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the reason(s) for denial and appeal rights, so that I can communicate via correspondence reasons for denial and appeal rights.</td>
</tr>
<tr class="even">
<td>VES-20954</td>
<td>Generate and Send Acceptance Letter with ID Card to Person in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the enrollment status of "eligible" as well as additional instructions and ID card, so that I can generate notification correspondence of enrollment "eligible" and additional instructions with an ID card to the applicant.</td>
</tr>
<tr class="odd">
<td>VES-20956</td>
<td>Provide Ability to Update and Record Eligibility Status Changes in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to provide the ability to record changes in eligibility status as the result of updated information received from authoritative sources, so that I can update information received from authoritative sources.</td>
</tr>
<tr class="even">
<td>VES-20966</td>
<td>Re-calculate Person for Medicare Verification in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to re-calculate Medicare Eligibility for persons selected for Medicare Verification and disentitle or reinstate the person from CHAMPVA based on business rules, so that I can update the applicant's eligibility.</td>
</tr>
<tr class="odd">
<td>VES-20968</td>
<td>Generate Medicare Enrollment Correspondence in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to generate Medicare Enrollment Requirement correspondence prior to the person's 65th birthday, so that I can send correspondence to the beneficiary regarding Medicare Enrollment Requirements.</td>
</tr>
<tr class="even">
<td>VES-20969</td>
<td>Generate Student Enrollment Correspondence in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to generate Student Requirement correspondence prior to the person's 18th birthday, so that I can send eligibility requirements correspondence to the beneficiary prior to the beneficiaries 18 birthday.</td>
</tr>
<tr class="odd">
<td>VES-20972</td>
<td>Receive Unsolicited VBA Data in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to receive unsolicited information that is a result of updates to Veteran and/or beneficiary/dependent information from the VBA system, so that I can determine eligibility.</td>
</tr>
<tr class="even">
<td>VES-20973</td>
<td>Receive Notifications from VBA in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to receive notifications from VBA systems when a relevant change is made that impacts VFMP eligibility, so that I can determine eligibility.</td>
</tr>
<tr class="odd">
<td>VES-20977</td>
<td>Re-Qualify a Sponsor After Receiving Unsolicited VBA Data in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to "re-qualify" a sponsor (Veteran)/dependent upon receipt of unsolicited VBA information, so that I can determine eligibility.</td>
</tr>
<tr class="even">
<td>VES-20978</td>
<td>Disentitle All Dependents Associated with an Unqualified Sponsor in VFMP System based on VBA data</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to disentitle all dependents associated to a sponsor who is determined to be "unqualified", upon receipt of unsolicited VBA information, so that I can determine eligibility.</td>
</tr>
<tr class="odd">
<td>VES-20979</td>
<td>Reprocess Eligibility for All Dependents Identified in Unsolicited VBA Updates in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to re-process eligibility for the dependents identified by VBA upon receipt of unsolicited VBA information, so that I can determine eligibility.</td>
</tr>
<tr class="even">
<td>VES-20980</td>
<td>Disentitile Ineligible Beneficiary Identified in Unsolicited VBA Data in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to disentitle a beneficiary who is determined to be "ineligible", upon receipt of unsolicited VBA information, so that I can determine eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21010</td>
<td>Provide Request and Response Capability to EE Service-For MVP, users can view fields within ES when queried.</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to prepare and return a response to a request or query for the Eligibility-Enrollment (E/E) information to determine member's enrollment status in any/all OCC Health Care Plans/ Groups, so that I can determine eligibility.</td>
</tr>
<tr class="even">
<td>VES-21048</td>
<td>Store and Associate Correspondence with Person in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to electronicallystore and associate with the record all generated correspondence, so that I can generate correspondence for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21050</td>
<td>Search and Re-Print Historical Correspondence in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to locate and "re-print" historical electronic files that are the result of generated correspondence, so that I can "re-print" historical electronic files for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21051</td>
<td>Indicate Additional Documents to be Enclosed with the Generated Correspondence in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to indicate, as part of the correspondence, additional documents that are to be "enclosed" with the generated correspondence, so that I can include additional documents to be "enclosed" with the generated correspondence.</td>
</tr>
<tr class="odd">
<td>VES-21058</td>
<td>Send Automatic Denial Correspondence from VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to send automatic denial correspondence based on the specific denial reason to comply with the Appeals Modernization process, so that I can send automatic denial correspondence for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21065</td>
<td>Support MPI Integration with Veteran Sponsors in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to support Master Person Index (MPI) integration for Veteran Sponsors for Family Member Programs, so that I can support MPI integration for Family Member Programs.</td>
</tr>
<tr class="odd">
<td>VES-21066</td>
<td>Support MPI Integration with Beneficiary Applicants in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to support Master Person Index (MPI) integration for beneficiary applicants for Family Member Programs, so that I can support MPI integration for Family Member Programs.</td>
</tr>
<tr class="even">
<td>VES-21071</td>
<td>Receive and Process VBA Data in VFMP System (Duplicate?)</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to receive and process VBA data/information that is the result of a query, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21072</td>
<td>Receive and Process VBA Data for CHAMPVA Applicants in VFMP System (Duplicate?)</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to receive and process unsolicited VBA data/information that is the result of an update that occurs at the VBA for persons who are enrolled in or who have applied for Standard CHAMPVA, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21088</td>
<td>Provide Eligibility Information to any VAMC from VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to access anddisplay eligibility information to any VAMC, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21108</td>
<td>Provide Ability to Send Daily Eligibility File to ClaimsXM via PEDTAS</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing eligibility information to ClaimsXM, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21111</td>
<td>Provide Ability to Send Daily OHI File to VFMP Vendorization System from VFMP System (Elig. Plus File)</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing changes to all Other Health Insurance (OHI) information to the vendorization system for Family Member Programs, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21119</td>
<td>View VFMP Eligibility Status in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to view eligibility status information related to any VFMP program, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21120</td>
<td>View VFMP Eligibility Period Information in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to view eligibility period information (dates) related to any VFMP program, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21122</td>
<td>View Application &amp; Evidence Information in VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to view application and evidence information for a person, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="even">
<td>VES-21126</td>
<td>View OHI Data for Persons within VFMP System</td>
<td>CP&amp;E<br />
As a VFMP Eligibility system, I need the ability to view OHI information for a person, so that I can manage data/information for eligibility.</td>
</tr>
<tr class="odd">
<td>VES-21348</td>
<td>CP&amp;E Migration for CHAMPVA Standard (M-Development)</td>
<td>Migration of CHAMPVA Standard</td>
</tr>
<tr class="even">
<td>VES-21637</td>
<td>Process CHAMPVA Medicare Rules Phase 2</td>
<td>Process CHAMPVA Medicare Rules Phase 2 </td>
</tr>
<tr class="odd">
<td>VES-22394</td>
<td>Ability to Edit All Employer details on Personal Subtab (VES)</td>
<td>Need the ability to edit, change, delete Employer details on Personal Subtab &amp; Financial -&gt; Dependents Subtab after Add-A-Person.<br />
<br />
Also need the ability to edit the Place of Birth (City/State) and Mother's Maiden Name fields on the Demographics -&gt; Identity Traits tab</td>
</tr>
<tr class="even">
<td>VES-23169</td>
<td>Send CP&amp;E Eligibility Plus Files</td>
<td>Send CP&amp;E Eligibility Plus Files</td>
</tr>
<tr class="odd">
<td>VES-26457</td>
<td>Manage Spina Bifida Eligibility</td>
<td>Manage Spina Bifida Eligibility</td>
</tr>
<tr class="even">
<td>VES-26752</td>
<td>Disable Existing CHAMPVA Fields within the VES Interface</td>
<td>CHAMPVA indicator on the eligibility tab as a selection - We don't want the users to set it; we want it controlled by the application. Radio button for CHAMPVA on VES currently - either remove or have it controlled by VFMP Elig. tab. Need to review with the HEC stakeholders. Camp Lejeune is there too</td>
</tr>
<tr class="odd">
<td>VES-28745</td>
<td>OHI Indicator Initial Application</td>
<td>As an EEV team member, I need the ability to indicate if a beneficiary has other health insurance, during the enrollment process, so that records needing OHI information can be marked for follow up by OHI team.</td>
</tr>
<tr class="even">
<td>VES-28746</td>
<td>Add OHI Information Existing Record</td>
<td>As an OHI team member, I need the ability to add new insurance carriers to a beneficiary record, so that I can record new carriers for coordination of benefits. </td>
</tr>
<tr class="odd">
<td>VES-28750</td>
<td>Capture Beneficiary OHI History</td>
<td>As an OHI team member, I need the ability to capture the history of updates made to a beneficiary's OHI record, so that I can monitor changes to the record and review individual employee work for quality assurance.</td>
</tr>
<tr class="even">
<td>VES-28751</td>
<td>Delete Insurance Information</td>
<td>As an OHI team member, I need the ability to delete insurance information from a beneficiary's record, so that I can correct input errors. </td>
</tr>
<tr class="odd">
<td>VES-28752</td>
<td>Flag Record Inconsistent OHI Info</td>
<td>As an OHI team member, I need the ability to flag a beneficiary record for inconsistent OHI information, so that downstream systems are notified to prevent improper claims payments.</td>
</tr>
<tr class="even">
<td>VES-29651</td>
<td>Spina Bifida CPE to ES Data Migration</td>
<td>Spina Bifida CPE to ES Data Migration</td>
</tr>
<tr class="odd">
<td>VES-29674</td>
<td>VFMP Overview Screen Support for CWVV and SB</td>
<td>VFMP Overview Screen - Add CWVV and SB<br />
VFMP Overview Screen Support for CWVV and SB</td>
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
<td>VES-29694</td>
<td>Send Spina Bifida in Eligibility Plus File</td>
<td>Send Spina Bifida in Eligibility Plus File</td>
</tr>
<tr class="odd">
<td>VES-29695</td>
<td>Send CWVV in Eligibility Plus File</td>
<td>Send CWVV in Eligibility Plus File</td>
</tr>
<tr class="even">
<td>VES-29703</td>
<td>Eligibility End and Restart Changes (all VFMPs)</td>
<td>Eligibility End and Restart Changes</td>
</tr>
<tr class="odd">
<td>VES-39219</td>
<td>Add TERA Letters to VES</td>
<td>As a VES User, when a final enrollment status is PG 7-8g trigger TERA Additional Evidence Letter (FL number forthcoming).</td>
</tr>
<tr class="even">
<td>VES-40388</td>
<td>Move P&amp;T Information to Eligibility Screen RSD</td>
<td>Move P&amp;T Information to Eligibility Screen</td>
</tr>
<tr class="odd">
<td>VES-40847</td>
<td>VES Site Correlation (VES)</td>
<td>As an end user I want to be able to select a radio button or a drop down to the demographics tab-Personal that states something to the nature of temporary site correlation for a one-time appointment, leaving the preferred facility alone.</td>
</tr>
<tr class="even">
<td>VES-43280</td>
<td>VFMP View Eligibility Plus File Transmission Log</td>
<td>VFMP View Eligibility Plus File Transmission Log</td>
</tr>
<tr class="odd">
<td>VES-43798</td>
<td>VFMP Add History Screens</td>
<td>VFMP Add History Screens</td>
</tr>
<tr class="even">
<td>VES-43799</td>
<td>VFMP Add Comments to Communications Tab and Remove Notes Field</td>
<td>VFMP Add Comments to Communications Tab and Remove Notes Field</td>
</tr>
<tr class="odd">
<td>VES-43802</td>
<td>Determine 180 Day Grace Period</td>
<td>Determine 180 Day Grace Period</td>
</tr>
<tr class="even">
<td>VES-43803</td>
<td>VFMP Determine CHAMPVA 180-Day Grace Period - Integration</td>
<td>VFMP Determine CHAMPVA 180-Day Grace Period</td>
</tr>
<tr class="odd">
<td>VES-44097</td>
<td>VFMP Always Allow Edit Tricare Indicator</td>
<td>VFMP Always Allow Edit Tricare Indicator</td>
</tr>
<tr class="even">
<td>VES-45132</td>
<td>PACT Act 405 Persian Gulf Deployed Cohort Identifier (VES)</td>
<td>Create a Persian Gulf Indicator on the Military Service tab in VES this information will be shared with VistA, CPRS, and EHRM.<br />
<br />
The indicator should be displayed mimicking the Compact Act indicator. The indicator should be shared with both VistA and EHRM/Cerner.<br />
Indicator should display on the Patient Inquiry screen in VistA and CPRS.</td>
</tr>
</tbody>
</table>

## Bugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                               |
|-----------|---------------------------------------------------------------------------|
| VES-38146 | Address lines saved with beginning or trailing tabs and non visible chars |
| VES-41530 | Failed document upload/retrieve blocks all other views and uploads        |
| VES-42299 | Z05 PID Address Line 1 too long                                           |
| VES-42303 | Z05 being sent with invalid email address                                 |
| VES-46310 | VOA Associate Relationship Regex validation is invalid                    |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Release Notes VES 6.7

## Release Notes for VHA Enrollment System - VES 6.7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

09-18-2023

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

### From: Release Notes VES 6.6

## Release Notes for VHA Enrollment System - VES v6.6.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

06-30-2023

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

### From: Release Notes VES 6.15

## Release Notes for VHA Enrollment System - VES 6.15.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

12-30-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.

The VA's goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran's personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Veteran Experience Services Enrollment and Eligibility (VESEE) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran's On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

VESEE defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.7.1

## Release Notes for VHA Enrollment System - VES 6.7.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10-30-2023

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

### From: Release Notes VES 6.5

## Stories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Key   | Summary                                                                           |
|-----------|---------------------------------------------------------------------------------------|
| VES-27141 | Implement Business Rules for CV End Date Calculation                                  |
| VES-27142 | Modification to Enrollment Determination Ruleflow                                     |
| VES-27143 | Batch Process for Cleanup                                                             |
| VES-27147 | Add New Option for AO and IR                                                          |
| VES-27148 | UI Changes for AO/IR Dropdown List Update on Eligibility and Military Service Screens |
| VES-27149 | UI Changes for AO/IR Popup Message for MSE on Military Service Screen                 |
| VES-28429 | Webhelp                                                                               |

### From: Release Notes VES 6.5.3

## Release Notes for VHA Enrollment System - VES 6.5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

05-15-2023

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

### From: Release Notes VES 6.5.2

## Release Notes for VHA Enrollment System - VES 6.5.2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

04-28-2023

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

### From: Release Notes VES 6.5.4

## Release Notes for VHA Enrollment System - VES 6.5.4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

05-16-2023

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

### From: Release Notes VES 6.5.5

## Release Notes for VHA Enrollment System - VES 6.5.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

05-26-2023

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

### From: Release Notes VES 6.6.1

## Release Notes for VHA Enrollment System - VES 6.6.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

09-18-2023

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
