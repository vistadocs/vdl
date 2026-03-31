---
title: SCIDO Version 3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: SPN
app_name: Spinal Cord Injury and Disorders Outcomes (SCIDO)
section: GUI
app_status: active
pkg_ns: SPN
patch_ver: 3
patch_id: SPN*3
group_key: "SPN:SPN:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - mark
  - class
  - contents
  - scido
  - spinal
  - cord
  - interim
  - disorders
page_count: 0
word_count: 1359
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_release_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_release_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=196"
---

> ![](scido-version-3-release-notes/001.png)

SPINAL CORD INJURY and DISORDERS

OUTCOMES INTERIM RELEASE NOTES

> ![](scido-version-3-release-notes/002.png)

> Version 3.0

> February 2011

Department of Veterans Affairs Office of Enterprise Development

Revision History

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 40%" />
<col style="width: 37%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Date</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
<td><blockquote>
<p>Author/Project Manager</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>February 2011</p>
</blockquote></td>
<td><blockquote>
<p>Minor revisions for VDL publication</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>June 2010</p>
</blockquote></td>
<td><blockquote>
<p>Update after ORT review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>October 2009</p>
</blockquote></td>
<td><blockquote>
<p>Make revisions per WPR</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>August 2009</p>
</blockquote></td>
<td><blockquote>
<p>Review and update Dependencies and Known Anomaly List</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>March 2009</p>
</blockquote></td>
<td><blockquote>
<p>Update</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>July 2007</p>
</blockquote></td>
<td><blockquote>
<p>Create document</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [New Features](#new-features)
- [Recommended Users](#recommended-users)
- [Related Manuals or Documents](#related-manuals-or-documents)
- [Section 508 Compliance](#section-508-compliance)
- [VA Service Desk](#va-service-desk)
- [Documentation Retrieval](#documentation-retrieval)
- [VistA Document Library](#vista-document-library)
- [VistA Software Requirements](#vista-software-requirements)
- [Known Anomaly List](#known-anomaly-list)
The Spinal Cord Injury and Disorders Outcomes (SCIDO) 3.0 Interim application is part of the Health*e*Vet platform, which converts the current Spinal Cord Dysfunction (SCD) Registry from a legacy command line system to a client server platform with a graphical user interface (GUI) and enhanced capabilities. The new system is built on the new Oracle/J2EE Health*e*Vet architecture.

# New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCIDO 3.0 Interim project aims to improve the health care of veterans by improving the ability to store, retrieve, and analyze outcome data from the treatment of veterans with spinal cord injuries and disorders with the following features:

- A Graphical User Interface (GUI)
- Role-based access
- Electronic signature codes for security
- Compliance with Section 508 of the Rehabilitation Act Amendments of 1998
- A page header that displays patient identifying information and selected demographic and medical information
- A cover sheet that displays patient information
- A browser-window interface with tabs for easy navigation
- Standard and ad hoc reports
- The SCIDO 3.0 Interim software will use the appropriate software interface to perform the following tasks:
- Receive SCIDO patient information and updates from the following VistA packages:
- Computerized Patient Record System-Text Integration Utilities
- Current Procedural Terminology (CPT)
- DRG Grouper
- Event Capture
- Fee Basis
- IFCAP
- Kernel
- Laboratory
- Nutrition and Food Service
- Outpatient Pharmacy
- Pharmacy Data Management
- Prosthetics
- Patient Care Encounters (PCE )
- Patient Registration
- Quasar
- Radiology
- Scheduling
- Surgery
- Vitals/Measurements
- VistA MailMan
- Provide requested information to:
- CPRS – Progress Notes
- Text Integration Utility
- VistA Functional Independence Measure (FIM)
- Provide requested data to populate other clinical data repositories as required by VA policies
- Provide patient data to populate the local SCIDO database

# Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are basic role responsibilities for the SCIDO 3.0 Interim application users:

- <u>SCIDO Administrators</u> – includes those individuals who have SCIDO 3.0 Interim application management permissions for maintaining patient records locally, i.e., Clinical Applications Coordinators (CACs), Automated Data Processing Application Coordinators (ADPACs), and SCIDO Coordinators. Administrators may also be included in the Clinicians’ group
- <u>SCIDO Clinicians</u> – includes SCIDO Clinicians who have clinical privileges to create, modify, display, store, and sign patient information into the computerized record system (CPRS)
- <u>SCIDO Researchers</u> – SCIDO Researchers who are allowed to query and generate reports from the national SCIDO database for non-identifiable patient data
- <u>SCIDO Information Resource Management staff–</u> modification of regional attributes, addition or deletion of medical centers from an associated SCI region, national or regional audits, and monitoring of system activity will be the responsibility of the IRM staff.

# Related Manuals or Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Spinal Cord Injury and Disorders Outcomes 3.0 Interim User Manual
- Spinal Cord Injury and Disorders Outcomes 3.0 Interim Regional J2EE Install Document
- Spinal Cord Injury and Disorders Outcomes 3.0 Interim Technical Manual/Security Guide
- Spinal Cord Injury and Disorders Outcomes 3.0 Interim J2EE Installation Guide
- Spinal Cord Injury and Disorders Outcomes 3.0 Interim VistA Installation Guide

# Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) fully supports Section 508 of The Rehabilitation Act and is committed to equal access for all users. The SCIDO application is Section 508 compliant.

# VA Service Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can find the documentation files for Spinal Cord Injury and Disorders Outcomes (SCIDO) on the OI Field Office \[ANONYMOUS.SOFTWARE\] directories. You are encouraged to use the TCP/IP FTP utility to obtain the documentation from one of the following OI Field Office ANONYMOUS.SOFTWARE directories.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>OI Field Office</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 53%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>File Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Retrieval Format</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPN3_0VIG.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Spinal Cord Injury and Disorders Outcomes 3.0 Interim VistA Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SPN3_0RIG.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Spinal Cord Injury and Disorders Outcomes 3.0 Interim Regional J2EE Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPN3_0RN.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Spinal Cord Injury and Disorders Outcomes 3.0 Interim Release Notes</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SPN3_0TM.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Spinal Cord Injury and Disorders Outcomes 3.0 Interim Technical Manual/Security Guide</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPN3_0UM.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Spinal Cord Injury and Disorders Outcomes 3.0 Interim User Manual</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
</tbody>
</table>

# VistA Document Library

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online documentation for this product is available in the VistA Document Library (VDL). Use the following internet address to access the VistA Document Library: <u><http://www.va.gov/vdl/>.</u> Select the Spinal Cord Injury and Disorders Outcomes link to access the SCIDO documentation.

The link below allows access to the Spinal Cord Injury and Disorders Outcomes home page: <span class="mark">REDACTED</span>

# VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of SCIDO 3.0 Interim application, the following packages must be installed and fully patched. The Installation Checklist provided in Addendum A of this document is organized in a step-wise manner to assist in loading any missing or new package/patch in the correct order.

|                         |         |                  |
|-------------------------|---------|------------------|
| Software                | Version | Required Patches |
| Kernel                  | V. 8    | Fully patched    |
| Kernel Toolkit          | V. 7.3  | Fully patched    |
| VA FileMan              | V. 22   | Fully patched    |
| VistALink               | V. 1.5  | Fully patched    |
| TIU                     | V. 1.0  | Fully patched    |
| Registration            | V. 5.3  | Fully patched    |
| Spinal Cord Dysfunction | V. 2.0  | Fully patched    |
| Surgery                 | V. 3.0  | Fully patched    |
| Prosthetics             | V. 3.0  | Fully patched    |

# Known Anomaly List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| SCI00001162 | Beta test - Registering patient with no Zip Code cause error                                                                                                                                                                          | Average         | Data checks in VistA make this a rare occurrence. If it persists request patient address update from HIMS.                                          | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001174 | Beta test - Etiology appears to duplicate on screen                                                                                                                                                                                   | Average         | Educate users that this only happens on the screen to avoid user confusion.                                                                         | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001178 | Linkage of patients with no Etiology data returns error                                                                                                                                                                               | Average         | Prior to merge update etiology records for both records                                                                                             | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001179 | Merge of patients with multiple/alias SSNs doesn't complete properly                                                                                                                                                                  | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000188 | Influenza Diagnoses and Treatment Report doesn't return expected data                                                                                                                                                                 | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000360 | BACK Button Selection Expires Page: Assessment page cannot be displayed on the second use of Back button on any assessment after assessment was calculated                                                                            | Average         | Not using the Back button, but select another button to go to the desired page.                                                                     | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00000801 | Outpatient Visit RPC Issue (SPN OUTPATIENT ICNS RPC): When same start/end date is used, the Outpatient Visit filter doesn’t work                                                                                                      | Average         | User can specify a larger time frame.                                                                                                               | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000827 | Clinician can submit an assessment within an EoC that Administrator inactivate                                                                                                                                                        | Average         | This won’t likely to happen as there will be communication between Administrator & Clinician if an episode of care is determined to be inactivated. | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000896 | Alpha Testing: ICD Code Search Report does not return expected results                                                                                                                                                                | Average         | Educate users that this only happens on the screen to avoid user confusion.                                                                         | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000958 | SCI Online Help Deficiencies                                                                                                                                                                                                          | Average         | The Online Help does exist & provide comprehensive help to users                                                                                    | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000961 | Unexpected results running report filters and the Breakdown of Patients Report                                                                                                                                                        | Average         | User can use a different report such as Basic Patient Info to see the result that they want to see                                                  | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001015 | UAT - Puget ICD Code Search Report Not Returning Data - All Patients Option                                                                                                                                                           | Average         | This happens with test data & unlikely to happen in production account with real data                                                               | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001016 | Patients With Future Appointments- 42 Minutes to Generate SCI Sorted XL Report                                                                                                                                                        | Average         | Run the report when system is not busy                                                                                                              | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001020 | UAT- Puget: Numerous Duplicate Prosthetics - Automatic Filters Prosthetics List Box                                                                                                                                                   | Average         | This doesn’t really affect day-to-day user’s job.                                                                                                   | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001023 | UAT-Puget: Excel Export Capacity Limitation for reports with Large Parameter size                                                                                                                                                     | Average         | User can run the report with a smaller number of parameters at one time.                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001025 | UAT - Puget: Duplicate items on the Medications filter list box                                                                                                                                                                       | Average         | This doesn’t really affect day-to-day user’s job.                                                                                                   | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001027 | UAT - Puget/R&D: Automatic Filters Page Capacity Limitations                                                                                                                                                                          | Average         | User can run the report with a smaller number of parameters at one time.                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001035 | UAT Puget - Converted CHART-SF subscore of 0 and Total Scores not displayed                                                                                                                                                           | Average         | User won’t work with this data; this is only for historical record.                                                                                 | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001036 | UAT Puget - Converted DUSOI total scores not displayed correctly                                                                                                                                                                      | Average         | User won’t work with this data; this is only for historical record.                                                                                 | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001038 | BETA-Puget: Admission Data Returned by SCI does not match Legacy System                                                                                                                                                               | Average         | Admission tracking messages will support day to day operations                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001039 | UAT-Puget: Discharge Data Returned by SCI does not match Legacy System                                                                                                                                                                | Average         | Discharge tracking messages will support day to day operations                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001040 | UAT-Puget: VA SCI Status In Patient Summary does not match Puget-Vista                                                                                                                                                                | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001044 | UAT-Puget: ICD Code Search Data Returned by SCI does not match Legacy System                                                                                                                                                          | Average         | Users could access the existing report                                                                                                              | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001046 | R&D-CHY 442: Discharges Report issue – VA SCI Status is not displayed for some patients                                                                                                                                               | Average         | Users can also view VA SCI Status for a patient on other page such as Registration page or Admission report.                                        | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001050 | Expected Data Not Returned for Multiple Filter Selections                                                                                                                                                                             | Average         | Report can always be run with individual filter                                                                                                     | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001055 | DUSOI assessment - Cancel button malfunction                                                                                                                                                                                          | Average         | This issue only appears on screen. Refresh the patient record will solve the problem.                                                               | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001077 | BETA - PUGET: Pharmacy Utilization at your Division Does not Match Legacy                                                                                                                                                             | Average         | This report won’t be available for version 3.0                                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001078 | BETA - PUGET: Pharmacy Utilization (Specific) at your Division Does not Match Legacy                                                                                                                                                  | Average         | This report won’t be available for version 3.0                                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001079 | BETA - PUGET: Patient Listing Report Issues – Means and Eligibility are misdisplayed                                                                                                                                                  | Average         | Patient Listing by State & County report can be run instead                                                                                         | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001080 | BETA - PUGET: Lab Utilization at Your Division Issues – section two of the report has missing tests                                                                                                                                   | Average         | This report won’t be available for version 3.0                                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001084 | BETA - PUGET: Radiology Utilization Report Issues - The descriptive procedural section is missing 3 records found in the VistA Legacy report                                                                                          | Average         | This report won’t be available for version 3.0                                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001085 | BETA - PUGET: Custom Reports Category Of Injury Filter Issue - Neurological Levels is displayed instead of "Tetraplegia" or "Paraplegia"                                                                                              | Average         | User can always translate from Neurological Levels to Category of Injury                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001090 | Service Connection filter issue: works fine on Non-peak hours, times out after 30-40 mins when system gets busy                                                                                                                       | Average         | Run report when system is not busy                                                                                                                  | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001102 | No warning message for unsaved data on Registration page                                                                                                                                                                              | Average         | User will pay more attention at saving all data                                                                                                     | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001105 | MPI Demographic Update unexpectedly updates blank middle name with “                                                                                                                                                                  | Average         | Unexpected side effect of issues with DG Load/Edit option. Should be reviewed in v 3.1                                                              | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001124 | Pneumonia and Respiratory Report - Nutrition or Dietary Precautions subpanel returns wrong data                                                                                                                                       | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001128 | Readmission report issue - The number of Admissions, Discharges & Readmissions on the Readmission report doesn't match the number of admissions on the admission report and the number of discharges on the Discharge (SCI&D) report. | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001134 | Service Connected filter on Custom report issue - Service Connected filter on the Custom report doesn't have the correct options                                                                                                      | Average         | Report can be run from the Filtered Reports                                                                                                         | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001135 | Missing impairment group on FIM instrument                                                                                                                                                                                            | Average         | Scheduled to be corrected in version 3.1                                                                                                            | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001136 | Researcher role access should be limited to only reports page                                                                                                                                                                         | Average         | Even researcher can navigate to other pages, but has no ability to edit to these pages.                                                             | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001152 | Nightly batch update SCIDO Date of Death with old Vista Date of Death                                                                                                                                                                 | Average         | If date of death is entered in Vista system first and then update in SCIDO later, this issue is prevented.                                          | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001154 | Foreign address doesn't completely display                                                                                                                                                                                            | Average         | Patient address can be viewed in Vista system.                                                                                                      | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001156 | Inpatient Visit filter                                                                                                                                                                                                                | Average         | Admission report can be run instead                                                                                                                 | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001161 | Age is displayed incorrect on Aggregate reports                                                                                                                                                                                       | Average         | Age can be calculated using patient’s date of birth.                                                                                                | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001187 | ICD's name with apostrophe couldn't be added to DUSOI assessment                                                                                                                                                                      | Average         | A complete list of diagnostic information is available in CPRS.                                                                                     | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000072 | Participation & SWLS Tab and Registration Tab: Metro/Micro/Rural SDS Functionality                                                                                                                                                    | Average         | This classification can be figured out by looking at the zip code.                                                                                  | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000154 | Print functionality defect on all tabs/pages                                                                                                                                                                                          | Average         | User can export reports to Excel spreadsheet and print the excel spread                                                                             | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000238 | All FIM polar charts should appear as elliptical polar charts                                                                                                                                                                         | Minor           | User can still understand what the polar charts say                                                                                                 | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00000433 | Cursor Movement through ASIA Assessment is not in correct order                                                                                                                                                                       | Minor           | Users just need to go through a different path to get to a specific field.                                                                          | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000598 | General Usability Issue-Disabled Fields gaining focus                                                                                                                                                                                 | Minor           | Users just need to skip these disabled fields to get to a specific field.                                                                           | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000765 | Custom Report - Missing Attributes in SCI                                                                                                                                                                                             | Minor           | These filters can be run using Filtered Reports                                                                                                     | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000798 | Active EOC does not display on EOC Management Page in Overlapping EOC scenario                                                                                                                                                        | Minor           | User can first inactivate and then re-activate the EOC to see it.                                                                                   | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000854 | SCI Charts Not Designed According to Customer Requirements                                                                                                                                                                            | Minor           | The current charts display correct data, just not with the color requested in requirement                                                           | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00000963 | Custom Report - Instrument Name filter doesn't return expected result                                                                                                                                                                 | Minor           | Custom report can be run in a different way to see Instrument Name data                                                                             | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| id      | Headline                                                                                                                                                                                                                          | Risk/Impact | Work Around                                                                                                                                     | Resolution                                                             |
| SCI00001005 | Audit Report - Pop-up message doesn't state parameter's name correctly                                                                                                                                                                | Minor           | This might cause users a small confusion, but doesn’t affect the report functionality                                                               | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001062 | SCI Assessment Date Validation Issues - unexpected validation messages are returned                                                                                                                                                   | Minor           | This might cause users a small confusion. User just needs to enter a valid date.                                                                    | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001063 | SF-MPQ Instrument HTML punctuation error – a colon should be added following the word Cramping                                                                                                                                        | Minor           | This is a very small cosmetic display issue.                                                                                                        | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001131 | Required Fields on FIM assessment are not marked                                                                                                                                                                                      | Minor           | The validation message will remind users to complete required fields                                                                                | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
| SCI00001133 | Primary Care Providers search validation message is not displayed when PCP search returns no result.                                                                                                                                  | Minor           | This only causes users a minor confusion. Users will attempt to do another search.                                                                  | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |