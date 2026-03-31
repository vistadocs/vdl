---
title: OR*3.0*629 (CPRS v33R) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: (CPRS v33R)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*629
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: These release notes cover the changes to CPRS delivered in the CPRS v33R release.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - cprs
  - release
  - table
  - contents
  - notes
  - patient
  - record
  - software
  - issue
  - existing
page_count: 0
word_count: 860
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_629_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_629_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: <span id="_Toc205632711" class="anchor"></span>Computerized Patient Record System (CPRS) v33R (OR\*3.0\*629)
---

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
    - [Modifications to Existing Features](#modifications-to-existing-features)
    - [Defects](#defects)
    - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
![](or-3-0-629-cprs-v33r-release-notes/001.png)
March 2025
Artifact Rationale
Release Notes describe changes to existing software and new features and functions of a subsequent release of software, which makes them useful as a marketing tool.
For the initial distribution of software, Release Notes are optional. Revisions to a product that involve major changes to technical specifications or end-user functionality require Release Notes. Changes to software or documentation that have a minimal impact do not require Release Notes. The project manager, as the authoritative source and in consultation with the technical writer, determines if a Release Notes document is a required artifact for the project.
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) is part of the Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to CPRS delivered in the CPRS v33R release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the applications modified by the CPRS v33R release and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the modifications to the existing software for CPRS v33R.

### Modifications to Existing Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following item is modified for CPRS v33R.

Updated text on Sensitive Patient Record.

To comply with formal guidance from the VA Office of General Counsel (OGC), the process for displaying the final prompt when accessing a sensitive patient record in CPRS GUI has been modified. Previously, when opening a patient record marked as sensitive, CPRS GUI contained a “hardcoded” message stating: “Do you want to continue processing this patient record?”. With the release of CPRS GUI v33R, the hardcoded message has been removed and a new VistA PARAMETER DEFINITION (#8989.51) named OR SENSITIVE PATIENT PROMPT is being exported. The parameter definition is automatically set at the PACKAGE level during the post-install of CPRS GUI v33R.  
The updated prompt message now reads as: “Do you want to continue accessing this patient record?”.

![](or-3-0-629-cprs-v33r-release-notes/002.png)

### Defects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  INC35538779 - AEU missing "Change..." button in Surgery tab when creating an addendum.

> <u>Problem:</u>

> When CPRS is started with a font of 10 or greater, the 'Change' button is missing on the Surgery tab in CPRS.

> Example: Highlighted field should contain a “Change” button

> ![](or-3-0-629-cprs-v33r-release-notes/003.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> CPRS has been updated to correctly display the 'Change' button on the Surgery tab at all font size options.

2.  INC35545363 - CPRS Anatomic Pathology Order Dialog is missing sections when CPRS font size is 10 or greater.

> <u>Problem:</u>

> The AP dialog is missing some sections when CPRS is opened with a font size greater than 8. This can skip required fields.

> Example: Required HPV Test field is not displayed

> ![](or-3-0-629-cprs-v33r-release-notes/004.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> CPRS has been updated to correctly build the AP order dialog at all font size options.

3.  INC35791225 - Window/prompt size small in CPRS since CPRSv33SWD - resizing doesn't stick

> <u>Problem:</u>

> This ticket is being used to focus on the issue related to the order detail window cutting off text. (Multiple issues were reported, but for this build we are focusing on this one.) When viewing the order details, there is a horizontal scroll bar with text cut off on the right side.

> Example: Clinical Maintenance: Entry of Outside Tests/Reports pop-up requiring resize

> ![](or-3-0-629-cprs-v33r-release-notes/005.png)

> <u>Resolution:</u>

> The report box for displaying order details has been updated and will no longer truncate the display at any of the font size choices in CPRS.

4.  INC36181641 - Missing buttons on CPRS Manual Release dialog box: Due to Font SizeNote: This is also an issue for Delayed Orders.

> <u>Problem:</u>

> In the Release to Service window, the OK and Cancel buttons begin to disappear as the font size is increased. At font size 14, the buttons are no longer visible.

> Example: Font size 12 – cuts off buttons

> ![](or-3-0-629-cprs-v33r-release-notes/006.png)

> Example: Font size 14 – missing buttons

> ![](or-3-0-629-cprs-v33r-release-notes/007.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> The release event form was corrected to ensure the OK and Cancel buttons remain visible at all font size options.

5.  INC35358743 and INC35570040 - Display issues with pop-ups and larger font sizes

> <u>Problem:</u>

> Some pop-ups in CPRS GUI are unable to be resized when using font size 12 or 14. The Patient Selection, Progress Notes Properties dialogs and the Encounter form are affected by this issue.

> Example: Cannot resize pop-up when using size 12-14 font

> ![](or-3-0-629-cprs-v33r-release-notes/008.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> These forms have been updated to allow adjusting of the form size, regardless of the font size option being used.

6.  INC36651597 LAS - Personal Orders Quick List no longer allowing for selection of more than 1 order before returning to the entire general lab list

> <u>Problem:</u>

> When a user has saved lab quick orders, after entering the first quick order, the Available Lab Tests does not return to the top and display the list of saved quick orders.

> Example: Saved Quick Orders appear at the top of Available Lab Tests

> ![](or-3-0-629-cprs-v33r-release-notes/009.png)

> Example: Entering a new Quick Order

> ![](or-3-0-629-cprs-v33r-release-notes/010.png)

> Example: Available lab tests do not return to the top

> ![](or-3-0-629-cprs-v33r-release-notes/011.png)

> <u>Resolution:</u>

> After selecting a saved lab quick order and accepting the order, the selection list will scroll back up to redisplay the list of saved lab quick orders.

7.  INC35776717 - HRF PRF (cat I patient record flag) issue with note association

> <u>Problem:</u>

> When a user attempts to enter an HRF PRF note in CPRS, they receive an error message and cannot flag the patient.  

> ![](or-3-0-629-cprs-v33r-release-notes/012.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> VistA and CPRS flag actions were duplicated and not synched when attempting to sort. The duplicates are removed and duplication is prevented on flag actions.

8.  INC35740088 - R3 (DAN)CPRS issue with long notes and CTRL+end keyboard shortcut<u>  
    Problem:</u>

> When viewing a long note and using the CTRL+end shortcut, it messes up the existing text formatting, requiring the user to drag the slider bar to the top before successfully using the shortcut.

> Note display after using the CTRL+end shortcut – Not the end/bottom of the note

> ![](or-3-0-629-cprs-v33r-release-notes/013.png)

> Actual end of the note

> ![](or-3-0-629-cprs-v33r-release-notes/014.png)

> <span class="mark"></span>

> <u>Resolution:</u>

> The shortcut works correctly and the user can view the end of the note.

9.  INC36581092 - PAL "Find in Selected Note" option causes CPRS note window to lose relevant context<u>  
      
    Problem:</u>

> When viewing the CPRS Notes tab, the “Find in Selected Note” option displays the searched for text in the current section of the note the user is viewing, but does not bring the user to the section that the text appears in.

> ![](or-3-0-629-cprs-v33r-release-notes/015.png) <span class="mark"></span>

> <u>Resolution:</u>

> The “Find in Selected Note” option now brings the user to the section of the note for the searched for text.

> ![](or-3-0-629-cprs-v33r-release-notes/016.png)

10. INC35675727 - CPRS Cumulative report Issues - headings change with date range<u>  
      
    Problem:</u>

> When a user views Cumulative in Lab Results and selects a Heading and date range, the displayed result text does not update to the selected date range.

> <span class="mark"></span>

> First Cumulative view

> ![](or-3-0-629-cprs-v33r-release-notes/017.png)

> Different report selected with no heading change

> ![](or-3-0-629-cprs-v33r-release-notes/018.png)

> <u>Resolution:</u>

> The Heading’s rich text is refreshed after the user selects a date range, displaying the proper results for that period.

11. INC34126235 - Provider with issue when processing consult comment alerts <u>  
      
    Problem:</u>

> When selecting a patient in CPRS and viewing the “Comment added” notification, the user is not brought to the new comment just to the patient’s consult comments.

> New comment – 10/15/24 at 17:40

> ![](or-3-0-629-cprs-v33r-release-notes/019.png) <span class="mark"></span>

> Comments displayed – September, not the latest from October

> ![](or-3-0-629-cprs-v33r-release-notes/020.png)

<u>  
</u>

> <u>Resolution:</u>

> When viewing the “Comment added” notification, the user is brought to the latest patient consult comment.

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VISTAOR-38273 PDMP related issue – “Report already delivered” error message  
Issue: When attempting to view the PDMP report in CPRS, some users get an error message, “Report already delivered”.

![](or-3-0-629-cprs-v33r-release-notes/021.png)

Workaround: When receiving the error, close the report and click to rerun the query. If the error continues, query the state portal directly as a workaround and then document it in CPRS using the STATE PRESCRIPTION DRUG MONITORING PROGRAM note title to ensure queries are counted in the system.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- CPRS v33R (OR\*3.0\*629) Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
- CPRS v33R (OR\*3.0\*629) Release Notes

All CPRS documents are available at the VA (Software) Documentation Library (VDL) web site.

This website is usually updated within 1-3 days of the patch release date.