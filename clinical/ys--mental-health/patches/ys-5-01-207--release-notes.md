---
title: Mental Health Assistant (MHA) YS*5.01*207 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*207
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - instrument
  - release
  - issues
  - mental
  - health
  - added
  - features
  - enhancements
page_count: 0
word_count: 897
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: June 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_207_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_207_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Mental Health Assistant (MHA)

  YS\*5.01\*207

  Release Notes

  ![](mental-health-assistant-mha-ys-5-01-207-release-notes/001.png)
---

June 2022

Office of Information and Technology (OIT)

Revision History

| Date  | Version | Description | Author           |
|-----------|-------------|-----------------|----------------------|
| June 2022 | 1.0         | Initial version | Liberty IT Solutions |

<span id="_Toc101433393" class="anchor"></span>Table : Acronyms List

Table of Contents

List of Tables

[Table 1: Acronyms List [4](#_Toc101433393)](#_Toc101433393)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications to Existing Functionality](#enhancements-and-modifications-to-existing-functionality)
  - [Remediated Issues from Patch 199](#remediated-issues-from-patch-199)
  - [Known Issues (from Patch 199)](#known-issues-from-patch-199)
  - [Product Documentation](#product-documentation)
- [Appendix A – Acronyms](#appendix-a-acronyms)
The Suicide Prevention Program (SPP) Mental Health Assistant (MHA) Project is comprised of 5 applications, one of which is MHA Web. The MHA Web application is the management tool for clinicians to create administrative assignments for patient completion, complete administrations through a Staff Entry interface, and review completed assessment reports. The MHA Web application was developed to create an effective and efficient tool for mental health clinicians and primary care clinicians to track assessment completion and administration trending. MHA Web is an enhancement of the current Core MHA capabilities. This provides Mental Health (MH) providers and managers tools (i.e., reports, graphs, etc.) to ensure effective MH care for Veterans. MHA Web supports MH instruments (e.g., psychological tests, structured interviews, and staff rating scales), pain assessments, nursing assessments, and additional instruments that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA) systems. Overall, MHA Web provides clinicians with a singular point for assessment assignment and report review from VistA data within a compact and user-friendly format. Core MHA has enjoyed widespread usage among MH clinicians over the past several years, and the current revisions of Core MHA and Mental Health Package (MHP) initiate steps toward re-engineering VistA Mental Health functionality.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to implement reports that affect the MHA application made by YS\*5.01\*207 to enhance clinician workflow and patient care.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users of the MHA Applications and applies to the changes made between this release and any previous release of this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for YS\*5.01\*207.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the features and functions added by YS\*5.01\*207:

- No new features added.

## Enhancements and Modifications to Existing Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications by YS\*5.01\*207:

- No enhancements/modifications added.

## Remediated Issues from Patch 199

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues from previous releases that are remedied by YS\*5.01\*207:

- SPP-10925 – NUDESC instrument not presenting questions to the Provider.
  - The NUDESC is a staff only instrument. An issue was found that kept the questions from being displayed to the Provider.
- SPP-10926 – Progress Notes are not saved for a multi-instrument administration with a Restricted Instrument last in the assignment list.
  - A situation was discovered when, during a multi-instrument administration including Restricted and Non-Restricted Instruments AND the last Instrument assigned is a Restricted Instrument, Progress Notes were not being saved.

## Known Issues (from Patch 199)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This list outlines existing issues that will be corrected in a future release:

- SPP-9863 – MHA Web – Co-Signer causes the label to change to “Save Edited Note”.
  - When using the co-signer functionality and selecting a co-signer, the “Save Note” button is relabeled to “Save Edited Note”, even though no changes were made to the note.
- SPP-9887 – MHA Web – Some instrument names are duplicated in the Completed Instruments field.
  - In certain cases, there are multiple instances of the same instrument buttons within the Completed Instruments field.
- SPP-10268 - MHA Web - Patient Entry - Instructional text missing from instrument.
  - Information related to the context of the question should be displayed for each question on Patient Entry. This will reduce any potential confusion.
- SPP-10511 - MHA Web – Graphing – Maximum call stack size exceeded error.
  - On occasion when a graph is zoomed in using the mouse, an error will appear in the graph stating, “Maximum call stack size exceeded”. If the page is refreshed or the graph is reloaded or changed, the error message will disappear.
- SPP-10561 – Special characters in clinic name caused internal server errors when searching for location.
  - Users are receiving “Internal Server Error – No Message Available” when searching for clinics via the location field using special characters. Workaround – do not use special characters in the search.
- SPP-10576 – MCMI-4 does not allow skipped questions.
  - The instrument needs to be updated to allow skipped questions.  
    Workaround – Answer all questions for the instrument.

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