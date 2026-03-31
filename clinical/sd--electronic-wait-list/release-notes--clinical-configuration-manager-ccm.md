---
title: Clinical Configuration Manager (CCM) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: Clinical Configuration Manager (CCM)
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
  - defect
  - defects
  - purpose
  - features
  - implemented
page_count: 0
word_count: 404
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 2
revision_newest: 3/5/2026
revision_oldest: 2/24/2026
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccm_release_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/ccm_release_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

---
title: |
  Clinic Configuration Manager (CCM)  
    
  Release Notes
---

for CCM Release 1.10.0

![](clinical-configuration-manager-ccm-release-notes/001.png)

March 2026

Revision History

| Date      | Version | Description             | Author              |
|-----------|---------|-------------------------|---------------------|
| 3/5/2026  | 1.0     | Finalized Version       | Booz Allen Hamilton |
| 2/24/2026 | 0.1     | Baseline for CCM 1.10.0 | Booz Allen Hamilton |

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
The Clinic Configuration Manager (CCM) is a web version of SD build, SD Inactivate, SD React, SD Restore, SD Cancel, and VA Toolset, utilizing the JavaScript React framework and providing equivalent clinic profile management functions used in the original applications. The purpose of CCM is to deliver users with a modernized look and feel while reducing operating costs and improving operational efficiencies.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide a summary of the maintenance and defect corrections that make up Clinic Configuration Manager (CCM) Release 1.10.0. The release software package is comprised of the following:

CCM application 1.10.0

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets the administrators and users of CCM.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see Features and Functionality for a summary of the maintenance and defect corrections implemented with CCM Release 1.10.0.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the features included in the CCM 1.10.0 release.

## Maintenance Implemented and Defects Fixed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the maintenance implemented and defects corrected in CCM Release 1.10.0. The work item ID is the Jira issue number.

| Work Item ID | Type  | Summary of Change                                                                                                                                        |
|--------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| VAS-2378     | Story | Generate a report that identifies clinics where availability could not be updated                                                                        |
| VAS-2438     | Story | Single Clinic Re-map                                                                                                                                     |
| VAS-2439     | Story | Division-wide Re-map                                                                                                                                     |
| VAS-3406     | Story | Copy/Paste Multiselect Dates UX/UI Updates                                                                                                               |
| VAS-3478     | Story | Annual Clinic Profile Review Spacing Adjustments                                                                                                         |
| VAS-3698     | Story | Have SECID removed from the Clinic Audit Report                                                                                                          |
| VAS-3833     | Story | Phase 2: Replace API end point details - Allow users to restore specific timeslots range                                                                 |
| VAS-3961     | Story | LOA/Holiday remap language changes                                                                                                                       |
| VAS-4071     | Story | Remove World War II Appt type from Default Appt type drop down list (Remove from Hard code list)                                                         |
| VAS-4271     | Story | Create Hide functions on Remap until all Holiday validation tests are complete w/ MUMPS VSE teams                                                        |
| VAS-3268     | Bug   | Address stop codes 192, 674 and 669 to be exceptions for not needing a provider to Reactivate a clinic                                                   |
| VAS-4102     | Bug   | Providers can be successfully removed from Inactive clinics that have Pending Reactivation date with no Validation Error message being shown to the User |
| VAS-4134     | Bug   | PROD Defect: No Show Letter edits showing a 500-error message                                                                                            |
| VAS-4146     | Bug   | Additional Calendar/holiday fix due to Time zone/Date line changes (Inact/React clinic status)                                                           |
| VAS-4160     | Bug   | Prevent users from copy and pasting 80+ characters in Spec Instruct & 30+ characters on Clinic Search fields                                             |
| VAS-4229     | Bug   | Remove open prop from the accordion items for the ClinicAccordionsCreateAndEdit component                                                                |

Enhancements and Defect FixesEnhancements and Defect Fixes

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distributed with CCM Release 1.10.0 is available for download from the VA Software Document Library (VDL).

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All known issues resolved by this release were documented in ServiceNow tickets and/or Jira issues as part of the ongoing, post-warranty, sustainment effort. Appropriate issues, workarounds, and step by step resolutions are documented in Knowledge Base articles and included in the searchable ServiceNow Knowledge Base hosted by the VA Enterprise Service Desk (ESD).