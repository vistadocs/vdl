---
title: VistA Scheduling Enhancement (VSE) GUI 1.7.29.0 Release Note
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: .0 Release Note
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 1.7.29
patch_id: SD*1.7.29
group_key: "SD:SD:1.7.29"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - release
  - enhancements
  - vista
  - scheduling
  - defects
  - fixes
  - issues
  - features
page_count: 0
word_count: 407
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2022
revision_count: 2
revision_newest: 09/07/2022
revision_oldest: 09/01/2022
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_release_1_7_29_0_release_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_release_1_7_29_0_release_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

---
title: |
  VistA Scheduling Enhancements (VSE)  
    
  GUI Release 1.7.29.0 Release Notes
---

![](vista-scheduling-enhancement-vse-gui-1-7-29-0-release-note/001.png)

September 2022  

Revision History

| Date       | Version | Description                                   | Author      |
|------------|---------|-----------------------------------------------|-------------|
| 09/07/2022 | 1.0     | Final draft                                   | Liberty ITS |
| 09/01/2022 | 0.1     | Baseline for VS GUI 1.7.29.0 and SD\*5.3\*823 | Liberty ITS |

<span id="_Toc104192920" class="anchor"></span>Table 1: Enhancements and Defects Fixes

Table of Contents

Table of Tables

[Table 1: Enhancements and Defects Fixes [1](#_Toc104192920)](#_Toc104192920)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
- [This Release](#this-release)
- [Features and Functionality](#features-and-functionality)
  - [Enhancements Implemented and Defects Fixes](#enhancements-implemented-and-defects-fixes)
- [User Documentation](#user-documentation)
- [Known Issues](#known-issues)
Department of Veterans Affairs (VA) has a need to improve the efficiencies of the outpatient medical scheduling processes through improved visibility of information. VA has created a comprehensive scheduling solution to modernize the Veterans Health Information Systems and Technology Architecture (VistA) Scheduling (VS) product.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide a summary of the enhancements and defect corrections that make up VS Graphical User Interface (GUI) Release 1.7.29.0. The release software package is comprised of the following:

VS GUI application 1.7.29.0

VistA M patch SD\*5.3\*823

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets the administrators and users of the VistA Scheduling package.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see Features and Functionality for a summary of the enhancements and defect corrections implemented with VS GUI Release 1.7.29.0 and VistA patch SD\*5.3\*823.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the features included in the VS GUI 1.7.29.0 package and VistA patch SD\*5.3\*823.

## Enhancements Implemented and Defects Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the enhancements implemented and defects corrected in VS GUI Release 1.7.29.0. The work item ID is the Jira issue number.

| Work Item ID | Summary of Change                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| VSE-171      | VS GUI: 508 fixes - Tasks Tab - Pending Appointments                                                                                                   |
| VSE-3152     | VistA: Refactor SDES create appointment request RPC.                                                                                                   |
| VSE-3231     | VistA: Rewrite SDES EDIT APPT REQ RPC.                                                                                                                 |
| VSE-3275     | VistA: Create RPC that will create APPT request and then schedule the appointment (VAOS).                                                              |
| VSE-3295     | VS GUI:: Adjust Walk-In Appointment Type to Automatically Generate Appointment Request.                                                                |
| VSE-3306     | VistA: Create a hash on clinics in Hospital Locations file \#44.                                                                                       |
| VSE-3310     | VistA: Create RPC for Walk-in Created Appointment Type to Automatically Generate Appointment Request.                                                  |
| VSE-3322     | VistA: Modify SDEC RPCs that return full SSN to only return last 4 of SSN.                                                                             |
| VSE-3324     | VS GUI: Modify SSN in VS GUI to only Display last 4.                                                                                                   |
| VSE-3385     | VistA: Update SDES GET CLINIC INFO to return Active and Inactive Clinics                                                                               |
| VSE-3387     | VistA: Create a new RPC to reactivate a clinic.                                                                                                        |
| VSE-3389     | VistA: Update SDES GET CLIN AVAILABILITY                                                                                                               |
| VSE-3395     | VistA: Update SDES GET APPTS BY CLIN IEN 2                                                                                                             |
| VSE-3396     | VistA: Update all appointment RPCs.                                                                                                                    |
| VSE-3436     | VistA: Modify SDES CREATE APPT REQ.                                                                                                                    |
| VSE-3452     | VS GUI – Fix issue where users cannot check-in appointments in prohibited clinics.                                                                     |
| VSE-3465     | I-0001352 - VS GUI: Update Preferred Gender and Gender to reflect VistA field names.                                                                   |
| VSE-3484     | VistA: Modify SDES RPCs that return full SSN to only return last 4 of SSN.                                                                             |
| VSE-3497     | VS GUI: 508 - Keyboard Control for Calendar Slots with No Scheduled Appointments.                                                                      |
| VSE-3509     | INC23549542: VS GUI: Day View Appointment Calendar - Timeslot Modifications.                                                                           |
| VSE-3524     | VistA: SDES Recall Clinic search RPC.                                                                                                                  |
| VSE-3525     | VistA: SDES Recall Provider search RPC.                                                                                                                |
| VSE-3534     | VistA: Modify SDES GET CLINIC INFO to add Division IEN, Stop Code Number, Credit Stop Code, Clinic IEN, return clinic special instructions as an array |
| VSE-3542     | VS GUI: Add Time Stamp to Patient Friendly Appointment List.                                                                                           |
| VSE-3621     | VistA: Update SDES GET INSURANCE VERIFY LIST and SDES GET INSURANCE VERIFY REQ to conform to SDES standards.                                           |
| VSE-3654     | VistA: Modify SDES GET APPT REQ BY IEN                                                                                                                 |
| VSE-3672     | VistA: Fix the issue with MRTC being stuck in pending status.                                                                                          |
| VSE-3457     | VS GUI: Fix issue where some Privileged Users do not Remove from Prohibited Clinics                                                                    |

Enhancements and Defect FixesEnhancements and Defect Fixes

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distributed with VS GUI Release 1.7.29.0 is available for download from the VA Software Document Library (VDL).

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All known issues resolved by this release were documented in ServiceNow tickets and/or Jira issues as part of the ongoing, post-warranty, sustainment effort. Appropriate issues, workarounds, and step by step resolutions are documented in Knowledge Base articles and included in the searchable ServiceNow Knowledge Base hosted by the VA Enterprise Service Desk (ESD).