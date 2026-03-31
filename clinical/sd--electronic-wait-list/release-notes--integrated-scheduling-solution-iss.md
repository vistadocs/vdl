---
title: Integrated Scheduling Solution (ISS) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: Integrated Scheduling Solution (ISS)
app_code: SD
app_name: Scheduling
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - release
  - maintenance
  - issues
  - scheduling
  - defect
  - defects
  - purpose
  - features
page_count: 0
word_count: 396
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 2
revision_newest: 3/18/2026
revision_oldest: 3/18/2026
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/iss_release_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/iss_release_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

---
title: |
  Integrated Scheduling Solution (ISS)  
    
  Release Notes
---

for ISS Release 1.32.0

![](integrated-scheduling-solution-iss-release-notes/001.png)

March 2026

Revision History

| Date      | Version | Description             | Author              |
|-----------|---------|-------------------------|---------------------|
| 3/18/2026 | 1.0     | Finalized Version       | Booz Allen Hamilton |
| 3/18/2026 | 0.1     | Baseline for ISS 1.32.0 | Booz Allen Hamilton |

<span id="_Toc179967959" class="anchor"></span>Table 1: Maintenance and Defect Fixes

Table of Contents

Table of Tables

[Table 1: Enhancements and Defects Fixes [1](#_Toc179967959)](#_Toc179967959)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
- [This Release](#this-release)
- [Features and Functionality](#features-and-functionality)
  - [Maintenance Implemented and Defects Fixed](#maintenance-implemented-and-defects-fixed)
- [User Documentation](#user-documentation)
- [Known Issues](#known-issues)
The Integrated Scheduling Solution (ISS) is a web version of the VistA Scheduling Enhancements (VSE) GUI, utilizing the JavaScript React framework and providing equivalent appointment management functions used in the original application. The purpose of ISS is to deliver users with a modernized look and feel while reducing operating costs and improving operational efficiencies.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide a summary of the maintenance and defect corrections that make up Integrated Scheduling Solution (ISS) Release 1.32.0. The release software package is comprised of the following:

ISS application 1.32.0

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets the administrators and users of ISS.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see Features and Functionality for a summary of the maintenance and defect corrections implemented with ISS Release 1.32.0.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the features included in the ISS 1.32.0 release.

## Maintenance Implemented and Defects Fixed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the maintenance implemented and defects corrected in ISS Release 1.32.0. The work item ID is the Jira issue number.

| Work Item ID | Type  | Summary of Change                                                                    |
|--------------|-------|--------------------------------------------------------------------------------------|
| ISS-10703    | Story | Remove Tooltip 9 Digit Social Security Number from ISS                               |
| ISS-10382    | Bug   | Create Appointment button is greyed out/disabled                                     |
| ISS-10391    | Bug   | Patient Comment Field Missing on View Veteran Request Page                           |
| ISS-10521    | Bug   | Demographics toast message appears in background of address validation modal         |
| ISS-10539    | Bug   | Close MRTC Request Page - Missing Reason for Disposition                             |
| ISS-10646    | Bug   | Appointments sort order is wrong after a browser refresh with the patient with flags |
| ISS-10649    | Bug   | Open Slot View: Time Slots not Displaying as Expected for Date Range Specified       |
| ISS-10653    | Bug   | Disposition MRTC Request does not include all prohibited clinics in the warning      |
| ISS-10654    | Bug   | Disposition MRTC Request warning ignores user's privilege                            |
| ISS-10656    | Bug   | Date Range Mismatch Between Open Slot View & Calendar View                           |
| ISS-10991    | Bug   | MRTC Calendar showing appointment for patient in other clinics                       |
| ISS-10992    | Bug   | Video Visit Successfully Created Modal is Not Displaying                             |

Enhancements and Defect FixesEnhancements and Defect Fixes

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distributed with ISS Release 1.32.0 is available for download from the VA Software Document Library (VDL).

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All known issues resolved by this release were documented in ServiceNow tickets and/or Jira issues as part of the ongoing, post-warranty, sustainment effort. Appropriate issues, workarounds, and step by step resolutions are documented in Knowledge Base articles and included in the searchable ServiceNow Knowledge Base hosted by the VA Enterprise Service Desk (ESD).