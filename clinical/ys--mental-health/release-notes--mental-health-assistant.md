---
consolidated_title: "mental health assistant release notes"
app_code: YS
doc_type: RN
master_source: "YS*5.01*199 Mental Health Assistant Release Notes"
master_pub_date: May 2022
consolidated_from: 5 versions
prior_versions:
  - "YS*5.01*187 Mental Health Assistant Release Notes"
  - "YS*5.01*204 Mental Health Assistant Release Notes"
  - "YS*5.01*217 Mental Health Assistant Release Notes"
  - "YS*5.01*218 Mental Health Assistant Release Notes"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Mental Health Assistant (MHA)

  YS\*5.01\*199

  Release Notes

  ![](ys-5-01-199-mental-health-assistant-release-notes/001.png)
---

May 2022

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author          |
|------------|-------------|-----------------|---------------------|
| April 2022 | 1.0         | Initial version | Booz Allen Hamilton |

<span id="_Toc101433393" class="anchor"></span>Table 1: Acronyms List

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
  - [Remediated Known Issues from Previous Releases](#remediated-known-issues-from-previous-releases)
  - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
- [Appendix A – Acronyms](#appendix-a-acronyms)
The Suicide Prevention Program (SPP) Mental Health Assistant (MHA) Project is comprised of 5 applications, one of which is MHA Web. The MHA Web application is the management tool for clinicians to create administrative assignments for patient completion, complete administrations through a Staff Entry interface, and review completed assessment reports. The MHA Web application was developed to create an effective and efficient tool for mental health clinicians and primary care clinicians to track assessment completion and administration trending. MHA Web is an enhancement of the current Core MHA capabilities. This provides Mental Health (MH) providers and managers tools (i.e., reports, graphs, etc.) to ensure effective MH care for Veterans. MHA Web supports MH instruments (e.g., psychological tests, structured interviews, and staff rating scales), pain assessments, nursing assessments, and additional instruments that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA) systems. Overall, MHA Web provides clinicians with a singular point for assessment assignment and report review from VistA data within a compact and user-friendly format. Core MHA has enjoyed widespread usage among MH clinicians over the past several years, and the current revisions of Core MHA and Mental Health Package (MHP) initiate steps toward re-engineering VistA Mental Health functionality.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to implement reports that affect the MHA application made by YS\*5.01\*199 to enhance clinician workflow and patient care.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users of the MHA Applications and applies to the changes made between this release and any previous release of this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for YS\*5.01\*199.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the features and functions added by YS\*5.01\*199:

- Added Special Reports functionality
  - Added a new functionality that will allow users to display multiple graphs on a single page. The Completed Reports panel was updated to display Completed Reports along with Special Reports. There will be a maximum of 8 graphable instruments.
- Added Patient in Context notification
  - If MHA Web loses context with CPRS, a red banner will be displayed along with an icon that shows the connection is broken
- Added an ID to error messages for troubleshooting
  - If an error appears to the user, it will contain a Universally Unique Identifier (UUID) that will allow for troubleshooting of the issue
- Added Computer Adaptive Testing (CAT) tests for Post-Traumatic Stress Disorder (PTSD)
  - Two test CAT tests (CAD-PTSD-DX and CAT-PTSD-E) were added for PTSD and are now available for use
- Added a collapse capability to the Active Assignment panel
  - The user can now collapse the Active Assignment panel to allow more room for viewing reports and graphs

## Enhancements and Modifications to Existing Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications by YS\*5.01\*199:

- The Batteries group is expanded to show four Batteries and is now consistent with the other groups on the Create/Edit Assignment screens
- Consolidated multi-instrument assessments into a single Progress Note
- Enabled graphing for Personality type instruments
  - 
  - PAI
  - MBMD
  - MCMI4
  - MMPI-2-RF
  - MCMI3
  - MMPI2
- 
- Removed extraneous information for the instrument description pop-up. Also corrected erroneous authors
- Removed the Options button from Staff Entry
- Changed timeout to be 45 minutes with a warning countdown modal to appear at 40 minutes
- Updated Barthel Index to be Staff Entry only
- Added hover over description to icons in the Active Assignment panel
- Updated format in BDI-2 Progress Note
- Updated “Show” button on graphing to be “Show All Dates” to explain the functionality
- If all scales on Completed Reports Graphing are un-checked, now displayed a blank graph.

## Remediated Known Issues from Previous Releases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues from previous releases that are remedied by YS\*5.01\*199:

- SPP-9600 - MHA Web - Deleting all instruments within Instrument Administration can lead to Error
  - This is a rare condition that has very little chance of happening in the field. This is when an assignment is created, the Delete button is pressed as fast as possible to remove all instruments in an assignment
- SPP-9549 – MHA Web - Staff Entry - BAM-R allows answers \>30 to be submitted
  - The BAM-R displays an error to the user when the answers are \>30 but still allows the instrument to be submitted
- SPP-9729 – Patient Entry – Cannot use Prior Question button to return to first question
  - For a few instruments (PSOCQ, STOP, ZBI SCREEN, ZBI SHORT) the “Prior Question” button will not return the user to the first question. The “Review Answers” button must be used
- SPP-9792 – Patient Entry – Cannot use “Prior Question” to go to first question in the administration
  - The “Prior Question” button is disabled when the second question is displayed, not allowing the user to click the button. The workaround is to click “Review Answers” and select the first question
- SPP-9782 – MHA Web – Free text field truncating text after ^ special character
  - When typing in the free text field for instrument testing, if a ^ happens to be typed, it causes any characters after the instrument to be erased when the note is saved, and the report viewed
- SPP-9789 – Patient Entry – Speed tab not working for scaled responses in 3 instruments (POQ, Promise29v2.1 and Promise29+2 V2.1)
  - When Patient Entry encounters a scaled question, the user must tab to get into focus. This causes speed entry to appear as if it’s not working
- SPP-9867 – MHA Web – Save message on Batteries covers a Battery Name
  - When adding a third battery (the fourth line), the successful message is no longer in focus
- SPP-9883 – MHA Web – Completed Reports – “Print” button workflow issues
  - In the Completed Reports view, the “Print” button remains highlighted after the print is completed and displays a blank screen. The workaround is to switch to the “Report” or “Graph” button

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This list outlines existing issues that will be corrected in a future release:

- SPP-9863 – MHA Web – Co-Signer causes the label to change to Save Edited Note
  - When using the co-signer functionality and selecting a co-signer, the “Save Note” button is relabeled to “Save Edited Note”, even though no changes were made to the note
- SPP-9887 – MHA Web – Some instrument names are duplicated in the Completed Instruments field
  - In certain cases, there are multiple instances of the same instrument buttons within the Completed Assignments field
- SPP-10268 - MHA Web - Patient Entry - Instructional text missing from instrument
  - Information related to the context of the question should be displayed for each question on Patient Entry. This will reduce any potential confusion
- SPP-10511 - MHA Web – Graphing – Maximum call stack size exceeded error
  - On occasion when a graph is zoomed in using the mouse, an error will appear in the graph stating “Maximum call stack size exceeded. If the page is refreshed or the graph is reloaded or changed, the error message will disappear.
- SPP-10561 – Special characters in clinic name caused internal server errors when searching for location.
  - Users are receiving “Internal Server Error – No Message Available” when searching for clinics via the location field using special characters. Workaround – do not use special characters in the search.
- SPP-10576 – MCMI-4 does not allow skipped questions.
  - The instrument needs to be updated to allow skipped questions. Examine the PDD for details and scoring for skipped questions. – Workaround – answer all questions for the instrument.

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*217 Mental Health Assistant Release Notes

## Remediated Issues from Patch 202

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues from previous releases that are remedied by YS\*5.01\*217:

- None
