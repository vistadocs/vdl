---
title: Mental Health Assistant YS*5.01*202 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*202
group_key: YS:YS:5.01
file_numbers: []
security_keys: []
menu_options: 0
description: '| Date | Version | Description | Author | |--------------|-------------|-----------------|----------------------| | October 2022 | 1.0 | Initial version | Liberty IT Solutions'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 1485
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: October 2022
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_202_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_202_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=78
audit_applied: '2026-05-31'
master_source: Mental Health Assistant YS*5.01*202 Release Notes
master_pub_date: October 2022
consolidated_from: 6 versions
prior_versions:
- YS*5.01*187 Mental Health Assistant Release Notes
- YS*5.01*199 Mental Health Assistant Release Notes
- YS*5.01*204 Mental Health Assistant Release Notes
- YS*5.01*217 Mental Health Assistant Release Notes
- YS*5.01*218 Mental Health Assistant Release Notes
consolidated_title: mental health assistant release notes
---

October 2022

Office of Information and Technology (OIT)

Revision History

| Date     | Version | Description | Author           |
|--------------|-------------|-----------------|----------------------|
| October 2022 | 1.0         | Initial version | Liberty IT Solutions |

<span id="_Toc101433393" class="anchor"></span>Table 1: Acronyms List

Table of Contents

List of Tables

[Table 1: Acronyms List [3](#_Toc101433393)](#_Toc101433393)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications to Existing Functionality](#enhancements-and-modifications-to-existing-functionality)
  - [Remediated Known Issues from Previous Releases](#remediated-known-issues-from-previous-releases)
  - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
- [Appendix A – Acronyms](#appendix-a-acronyms)
The Suicide Prevention Program (SPP) Mental Health Assistant (MHA) Project is comprised of 5 applications, one of which is MHA Web. The MHA Web application is the management tool for clinicians to create administrative assignments for patient completion, complete administrations through a Staff Entry interface, and review completed assessment reports. The MHA Web application was developed to create an effective and efficient tool for mental health clinicians and primary care clinicians to track assessment completion and administration trending. MHA Web is an enhancement of the current Core MHA capabilities. This provides Mental Health (MH) providers and managers tools (i.e., reports, graphs, etc.) to ensure effective MH care for Veterans. MHA Web supports MH instruments (e.g., psychological tests, structured interviews, and staff rating scales), pain assessments, nursing assessments, and additional instruments that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA) systems. Overall, MHA Web provides clinicians with a singular point for assessment assignment and report review from VistA data within a compact and user-friendly format. Core MHA has enjoyed widespread usage among MH clinicians over the past several years, and the current revisions of Core MHA and Mental Health Package (MHP) initiate steps toward re-engineering VistA Mental Health functionality.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to implement reports that affect the MHA application made by YS\*5.01\*202 to enhance clinician workflow and patient care.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users of the MHA Applications and applies to the changes made between this release and any previous release of this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for YS\*5.01\*202.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the features and functions added by YS\*5.01\*202:

- Added additional instruments to MHA Web
  - Added the following instruments to MHA Web
    - ASRS
    - CAT-PSYCHOSIS
    - EHS-14
    - PEBS-20
    - PEBS-27
    - WBS
- Added Preferences interface
  - Created an interface to allow clinicians to configure preferences outside of Staff Entry. It is available through Preferences icon (cog) -\> Favorites
- Added the High-Risk Patient Dashboard view to MHA Web.
  - A High-Risk Patient Dashboard was created to view information for all patients in a site that are labeled High-Risk. This will allow the clinicians to view critical data related to suicide risk.

## Enhancements and Modifications to Existing Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications by YS\*5.01\*202:

- Special Reports enhancements
  - Added the ability of creating a custom graph based upon the instruments selected in Special Reports.
  - Added interpretation information for the Special Reports graphs.
- Computer Adaptive Testing (CAT) Enhancements
  - Update CAT-Psychosis for administration in both Staff Entry and Patient Entry.
  - Inactivated CAT instruments
    - CAT-ADHD
    - CAT-SDOH
    - CAT-PTSD
- Update FOCI skip logic
  - Updated FOCI skip logic to: If any question in section A is answered "Yes", section B questions should be enabled. Only if every question in section A is answered "No" should section B questions be disabled.
- Update FAST instrument scoring
  - Currently the score for Functional Assessment Staging of Alzheimer's Disease (FAST) is calculated based on the first question with a negative response. The score should be based on the highest question with a positive response.
- Update MCMI4 to allow 13 skipped questions
  - The MCMI4 instrument did not allow skipped questions. The instrument was updated to allow skipped questions and alert clinicians when more than 13 questions are skipped.
- Update SLUMS and GDS Dementia instruments to contain the needed stories.
  - The SLUMS and GDS Dementia instruments rely on stories for administration. MHA Web was missing these stories.
- User Name entry fails when multiple names match 
  - When creating a new assignment, if the name for the ordering doctor or interviewer matches multiple users, the user's title will show up appended to the name to help the user select the correct name.  If a user selects the name with the title appended, trying to create the assignment by hitting Patient Entry or Staff Entry will result in an error message for an incorrect field
- Locations/Clinics with long names show as invalid 
  - Locations/Clinics with long names were failing the field validations which kept users from entering the correct location. 
- Updated VistA import to remove inactive instruments for Favorites, Special Reports and Batteries.
  - In a specific button click sequence it is possible for a user to create an Instrument Favorites list with a null instrument. Instead, the user should be notified that an instrument must be selected.
- Enabled graphing for Millon Behavioral Medicine Diagnostic (MBMD) instrument
  - The MBMD results can now be graphed on MHA Web from the Completed Instruments panel.
- Updated Select Instruments page to remove checkbox from a battery if an instrument is removed from the Instruments Chosen list
  - If an instrument is removed from the Instruments Chosen list, the Battery will become unchecked.
- Expand selectable locations to include Wards
  - Wards and Clinics are allowed to be displayed in MHA Web.
- Change the Division Selection list to alphabetical
  - The Division Selection drop down list is in alphanumeric order by Division ID.
- Update MHA Web Timeout to match CPRS timeout
  - There were multiple reports of MHA Web timing out too often. A change was made to allow MHA Web to use the VistA timeout of the current user, the same as CPRS/MHA Core does.
- Enhanced Completed Report delete button pop up message
  - The delete button pop up now displays the information that was in MHA Core.
- Moved capability of printing a blank instrument from Staff Entry to the main MHA Web landing page. A clinician can now print multiple instrumets from the Active Assignments pane.
  - Printing has been removed from Staff Entry.

## Remediated Known Issues from Previous Releases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues from previous releases that are remedied by YS\*5.01\*202:

- SPP-9863 – MHA Web – Co-Signer causes the label to change to Save Edited Note.
  - When using the co-signer functionality and selecting a co-signer, the "Save Note" button is relabeled to "Save Edited Note", even though no changes were made to the note.
- SPP-9887 – MHA Web – Some instrument names are duplicated in the Completed Instruments field.
  - In certain cases, there are multiple instances of the same instrument buttons within the Completed Assignments field.
- SPP-10268 - MHA Web - Patient Entry - Instructional text missing from instrument.
  - Information related to the context of the question should be displayed for each question on Patient Entry. This will reduce any potential confusion.
- SPP-10511 - MHA Web – Graphing – Maximum call stack size exceeded error.
  - On occasion when a graph is zoomed in using the mouse, an error will appear in the graph stating "Maximum call stack size exceeded. If the page is refreshed or the graph is reloaded or changed, the error message will disappear.
- SPP-10561 – Special characters in clinic name caused internal server errors when searching for location.
  - Users are receiving "Internal Server Error – No Message Available" when searching for clinics via the location field using special characters. Workaround – do not use special characters in the search.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This list outlines existing issues that will be corrected in a future release:

- SPP-10640 – Wording in the hover overs of various instruments are incorrect.
  - The hover over for CAGE is corrected to state: CAGE Alcohol Screening Tool.
  - The hover over for BPRS-A does not contain question marks.
  - The hover over for BSI-18 Norm Sample: Community sample (N = 1,134) and oncology sample (N = 1,543).
- SPP-10919 – Finishing last instrument in assignment sends user back to landing page instead of unfinished instrument.
  - Upon selecting the finish button on the last instrument in the assignment, the user is redirected to previous instruments in the assignment where they can either finish the instruments or Save & Exit.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents *(located at the VA Software Document Library)* apply to this release:

- Deployment, Installation, Back-out, and Rollback Guide (DIBRG)

# Appendix A – Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                         |
|-------------|--------------------------------------------------------|
| CAT         | Computer Adaptive Testing                              |
| CPRS        | Computerized Patient Record System                     |
| DIBRG       | Deployment, Installation, Back-out, and Rollback Guide |
| FAST        | Functional Assessment Staging of Alzheimer's Disease   |
| MBMD        | Millon Behavioral Medicine Diagnostic                  |
| MCMI        | Millon Clinical Multiaxial Inventory                   |
| MH          | Mental Health                                          |
| MHA         | Mental Health Assistant                                |
| MHP         | Mental Health Package                                  |
| OIT         | Office of Information and Technology                   |
| PTSD        | Post-Traumatic Stress Disorder                         |
| SPP         | Suicide Prevention Package                             |
| UUID        | Universally Unique Identifier                          |
| VA          | Department of Veteran Affairs                          |
| VistA       | Veterans Integrated Systems and Technical Architecture |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*217 Mental Health Assistant Release Notes

## Remediated Issues from Patch 202

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues from previous releases that are remedied by YS\*5.01\*217:

- None
