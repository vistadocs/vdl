---
title: Patient Check In Clinical Staff Viewer (PCICSV) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: Patient Check In Clinical Staff Viewer (PCICSV)
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
  - pcicsv
  - maintenance
  - issues
  - patient
  - clinical
  - staff
  - defect
page_count: 0
word_count: 403
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 2
revision_newest: 2/23/2026
revision_oldest: 1/22/2026
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/pcicsv_release_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/pcicsv_release_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

---
title: |
  Patient Check In Clinical Staff Viewer (PCICSV)  
    
  Release Notes
---

for PCICSV Release 2.2.0

![](patient-check-in-clinical-staff-viewer-pcicsv-release-notes/001.png)

February 2026

Revision History

| Date      | Version | Description               | Author              |
|-----------|---------|---------------------------|---------------------|
| 2/23/2026 | 1.0     | Finalized Version         | Booz Allen Hamilton |
| 1/22/2026 | 0.1     | Baseline for PCICSV 2.2.0 | Booz Allen Hamilton |

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
Patient Check In Clinical Staff Viewer (PCICSV) is an updated web version of VSE for Clinical Staff (VSECS), utilizing JavaScript React framework and providing daily appointment lists and patient status tracking. The purpose of PCICSV is to deliver to users a modernized user interface while reducing operating costs and improving operational efficiencies.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide a summary of the maintenance and defect corrections that make up Patient Check In Clinical Staff Viewer (PCICSV) Release 2.2.0. The release software package is comprised of the following:

PCICSV application 2.2.0

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets the administrators and users of PCICSV.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see Features and Functionality for a summary of the maintenance and defect corrections implemented with PCICSV Release 2.2.0.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the features included in the PCICSV 2.2.0 release.

## Maintenance Implemented and Defects Fixed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the maintenance implemented and defects corrected in PCICSV Release 2.2.0. The work item ID is the Jira issue number.

| Work Item ID | Type  | Summary of Change                                                                                        |
|--------------|-------|----------------------------------------------------------------------------------------------------------|
| VSECS-109    | Story | Memo and Workflow Status to refresh faster than 2 minutes                                                |
| VSECS-719    | Story | Expanded Details Modal in Actions Menu                                                                   |
| VSECS-1485   | Story | Errors - Table Loading Error Message                                                                     |
| VSECS-1748   | Story | Display Column for Total Care Time                                                                       |
| VSECS-2149   | Story | Remove Workflow Status and Memos from Get Appointments processing                                        |
| VSECS-2325   | Story | Code Optimization (DRY) - Modals                                                                         |
| VSECS-2328   | Story | Code Optimization - Font change in the front page                                                        |
| VSECS-2361   | Story | Errors - Not All Sites Are Permissioned for User                                                         |
| VSECS-2363   | Story | Errors - General SSOi Errors                                                                             |
| VSECS-2364   | Story | Errors - General JWT Errors                                                                              |
| VSECS-2365   | Story | Errors - Could not load user's clinic lists                                                              |
| VSECS-2366   | Story | Errors - Could not load Current Day Appointments                                                         |
| VSECS-2367   | Story | Errors - Could not update Workflow Status for patient                                                    |
| VSECS-2368   | Story | Errors - Could not mark Queued patient as complete                                                       |
| VSECS-2371   | Story | Errors - Could not add memo to patient DWL/Queue                                                         |
| VSECS-2372   | Story | Errors - Could load memos for patient DWL/Queue                                                          |
| VSECS-2373   | Story | Errors - Could not load Appointment Comments                                                             |
| VSECS-2374   | Story | Errors - Clinic List - Could not load clinics after selecting site                                       |
| VSECS-2375   | Story | Errors - Clinic List - Could not add clinics to clinic list array on Create.                             |
| VSECS-2377   | Story | Errors - Clinic List - Could not delete clinic list                                                      |
| VSECS-2378   | Story | Errors - Clinic List - Could not save changes while editing (removing clinics from list)                 |
| VSECS-2379   | Story | Errors - Clinic List - Could not save changes while editing/Could not load clinic list being edited      |
| VSECS-2380   | Story | Errors - Could not fetch part of user profile (one or more sites could load but at least 1 fails)        |
| VSECS-2381   | Story | Errors - Could not load medications for patient                                                          |
| VSECS-2382   | Story | Errors - Could not load pre-visit summary                                                                |
| VSECS-2383   | Story | Errors - Could not log sensitive record audit                                                            |
| VSECS-2384   | Story | Errors - Messages - Could not retrieve/load message template for modal.                                  |
| VSECS-2385   | Story | Errors - Messages - Message could not be sent                                                            |
| VSECS-2386   | Story | Errors - Messages - Could not load messages (table)                                                      |
| VSECS-2387   | Story | Errors - Notifications - Validations and Could not save new notification on submit                       |
| VSECS-2388   | Story | Errors - Notifications - Could not save on notification edit                                             |
| VSECS-2389   | Story | Errors - Notifications - Could not load notifications table                                              |
| VSECS-2390   | Story | Errors - Notifications - Could not delete message                                                        |
| VSECS-2391   | Story | Errors - Queue - Could not create new queue on submit                                                    |
| VSECS-2392   | Story | Errors - Queue - Could not load queue on edit/Could not save edit queue                                  |
| VSECS-2394   | Story | Errors - Queue - Could not delete queue on click                                                         |
| VSECS-2395   | Story | Errors - Queue - Could not load queue table on queue tab                                                 |
| VSECS-2396   | Story | Errors - Queue - Could not add patient to queue (Manual Add)                                             |
| VSECS-2397   | Story | Errors - Queue - Could not add patient to queue from patient search                                      |
| VSECS-2398   | Story | Errors - Queue - Could not mark patient as complete/undo complete                                        |
| VSECS-2399   | Story | Errors - Queue - Could not load queues on app load                                                       |
| VSECS-2403   | Story | Errors - Button loading state/behavior                                                                   |
| VSECS-2514   | Story | Errors - Could Not Create Clinic List (the object shell before adding array)                             |
| VSECS-2520   | Story | Code Optimization - Remove all inline styles                                                             |
| VSECS-2530   | Story | Workflow Status/Memo call should be forced to fire any time get Appointments is called                   |
| VSECS-2608   | Story | Errors - Workflow Status/Memo Call Error                                                                 |
| VSECS-2708   | Story | Implement "split calls" logic in 2.1 version                                                             |
| VSECS-2729   | Story | Implement new endpoint from CWS for batch addition of clinics on a clinic list                           |
| VSECS-3077   | Story | Error Handling Overhaul Implementation                                                                   |
| VSECS-3125   | Story | Implement new endpoint from CWS for batch deletion of clinics on a clinic list                           |
| VSECS-3140   | Story | Swap to v3 of SAS call in PCICSV                                                                         |
| VSECS-3315   | Story | Clean up filter updates to use util method for exact matches instead of adding non visible white space   |
| VSECS-3469   | Story | Remove "VSECS is now PCICSV" modal                                                                       |
| VSECS-3581   | Story | Update Current Day Appointments table to MUI                                                             |
| VSECS-3605   | Story | Appt Comments Modal Info - Change red text to blue info alert.                                           |
| VSECS-3606   | Story | Include blue informational alert within expanded details modal sections                                  |
| VSECS-3607   | Story | Table filter fields - Size adjustment for each table                                                     |
| VSECS-3609   | Story | Demographics red not up to date hover tool tip                                                           |
| VSECS-3732   | Story | Changing Workflow Status and adding Memo refresh and load behavior                                       |
| VSECS-3834   | Story | Queue List - Filter options available at all times                                                       |
| VSECS-3836   | Story | DAL - Filter options available at all times                                                              |
| VSECS-4137   | Story | Remove Access/Keys Error Toast                                                                           |
| VSECS-2304   | Bug   | Memo time and user data lost with split call refresh                                                     |
| VSECS-2527   | Bug   | Workflow Status/Memos not appearing immediately on table load when navigating to DWL                     |
| VSECS-2528   | Bug   | Table showing loading indicator for every Workflow Status/Memo call                                      |
| VSECS-2529   | Bug   | Table not displaying newly added memo/workflow status change after closing modal                         |
| VSECS-2537   | Bug   | Memo user initials and time not appearing in memo cell                                                   |
| VSECS-2553   | Bug   | More memo issues                                                                                         |
| VSECS-2827   | Bug   | 508: Messages - each country is read by JAWS twice when user navigates list of countries.                |
| VSECS-2846   | Bug   | CVE-2025-58754 (High/7.5, 0.02%) - vse-cs                                                                |
| VSECS-3130   | Bug   | Empty state of table appearing on app load and browser refresh                                           |
| VSECS-3409   | Bug   | 508: "Please notify your supervisor" message fails color contrast ratio.                                 |
| VSECS-3504   | Bug   | Timeout results in being stuck on JWT error                                                              |
| VSECS-3734   | Bug   | Not redirecting to Login                                                                                 |
| VSECS-3740   | Bug   | Appt data is no older than and Refresh/Print button position change                                      |
| VSECS-3743   | Bug   | Medications responsiveness regression                                                                    |
| VSECS-3809   | Bug   | 508: Action buttons - Keyboard and JAWS users cannot use the tab key for navigation.                     |
| VSECS-3833   | Bug   | Service call duplication                                                                                 |
| VSECS-3835   | Bug   | Create new queue modal name field populated                                                              |
| VSECS-3837   | Bug   | Resolve Hook errors seen for Appointment Table                                                           |
| VSECS-3841   | Bug   | Initial load after clearing cookies results in an empty data table                                       |
| VSECS-3882   | Bug   | Initial Workflow Status Change - Workflow Status modal stays open                                        |
| VSECS-3884   | Bug   | User unable to remove a clinic from the "Current Clinic List"                                            |
| VSECS-3899   | Bug   | Printed Table Column Header Issue                                                                        |
| VSECS-3937   | Bug   | DAL - Reset Filters button active and APPT TIME column not sorted by default                             |
| VSECS-3946   | Bug   | Update wording on existing key permission error toast                                                    |
| VSECS-3947   | Bug   | Show clinic lists for sites that permissions were lost                                                   |
| VSECS-3953   | Bug   | URL not matching Page title                                                                              |
| VSECS-3967   | Bug   | Workflow status not sticking for checked in patients                                                     |
| VSECS-3998   | Bug   | Green memo toast not appearing for new memo                                                              |
| VSECS-3999   | Bug   | Messages action item not active for eChecked in Patients with previous Pre-Check In                      |
| VSECS-4000   | Bug   | Green workflow status change toast not appearing                                                         |
| VSECS-4025   | Bug   | Filters not persisting across DWL to DAL                                                                 |
| VSECS-4038   | Bug   | Default clinic list access lost alert                                                                    |
| VSECS-4057   | Bug   | Clinics for site are not clearing when switching facilities                                              |
| VSECS-4063   | Bug   | Printing Sorting/Filtering Not Persisting                                                                |
| VSECS-4066   | Bug   | Memo button state changing when split call refresh fires                                                 |
| VSECS-4071   | Bug   | Queue list table headers                                                                                 |
| VSECS-4073   | Bug   | Create Clinic List and Create Queue modal inactive for subdivision                                       |
| VSECS-4091   | Bug   | Patient Arrived option in the Action menu remains enabled after the Workflow status is marked as Arrived |
| VSECS-4100   | Bug   | “Patient Arrived" should not be displayed as an option in the Action menu on the DWL page                |
| VSECS-4105   | Bug   | Hidden workflow status appearing in dropdown                                                             |
| VSECS-4118   | Bug   | Memos column being cut off in Queues                                                                     |
| VSECS-4130   | Bug   | Sorting Icons not Functioning                                                                            |
| VSECS-4131   | Bug   | Arrived Column: Hide Filter Column Issue                                                                 |
| VSECS-4148   | Bug   | Queue List: Missing Toast for Creating New Memo                                                          |

Enhancements and Defect FixesEnhancements and Defect Fixes

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distributed with PCICSV Release 2.2.0 is available for download from the VA Software Document Library (VDL).

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All known issues resolved by this release were documented in ServiceNow tickets and/or Jira issues as part of the ongoing, post-warranty, sustainment effort. Appropriate issues, workarounds, and step by step resolutions are documented in Knowledge Base articles and included in the searchable ServiceNow Knowledge Base hosted by the VA Enterprise Service Desk (ESD).