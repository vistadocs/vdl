---
title: CPRS OR*3*569 AP Order Dialog Setup and Configuration Guide
doc_type: CFG
doc_label: Setup and Configuration Guide
doc_layer: patch
doc_subject: AP Order Dialog
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*569
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications,
audience: 
keywords: 
  - order
  - cprs
  - edit
  - dialog
  - pathology
  - table
  - contents
  - laboratory
  - anatomic
  - entry
page_count: 0
word_count: 2364
section_count: 11
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_569_setup.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_569_setup.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System (CPRS)  
  OR\*3.0\*569/LR\*5.2\*553

  Anatomic Pathology Order Dialog

  Setup and Configuration Guide
---

![](cprs-or-3-569-ap-order-dialog-setup-and-configuration-guide/001.png)

September 2022

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

| Date           | Version | Description      | Author                |
|----------------|---------|------------------|-----------------------|
|                |         |                  |                       |
| September 2022 | 1.0     | Initial version. | CPRS Development Team |

Table of Contents

# OR\*3.0\*569/LR\*5.2\*553


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [OR\3.0\569/LR\5.2\553](#or30569lr52553)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
- [Reporting Issues](#reporting-issues)
- [How to Configure Anatomic Pathology for CPRS](#how-to-configure-anatomic-pathology-for-cprs)
  - [Edit the 13 Laboratory Tests](#edit-the-13-laboratory-tests)
  - [Check the ORDERABLE ITEM (#101.43) File for all 13 Laboratory Tests](#check-the-orderable-item-10143-file-for-all-13-laboratory-tests)
  - [Additional AP Dialog Configuration (Optional Step)](#additional-ap-dialog-configuration-optional-step)
  - [Edit the LABORATORY SITE (#69.9) file](#edit-the-laboratory-site-699-file)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This document describes how to perform the setup of Anatomic Pathology in CPRS that was initially released in CPRS v32a which contained OR\*3.0\*539 and LR\*5.2\*469. CPRS v32a released the GUI for the Anatomic Pathology Order Dialog templates. Previously, the Order Dialog templates were released under several patches associated with the VistA Laboratory Enhancements (VLE) Anatomic Pathology (AP) project: LR\*5.2\*462, LR\*5.2\*469, LR\*5.2\*482, LR\*5.2\*479, and LR\*5.2\*483

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purposes of these patches are to resolve some technical issues so that Anatomic Pathology (AP) order dialogs can be enabled nationwide. Once these patches are released, sites are approved to enable Anatomic Pathology ordering in CPRS.

When your site is ready to enable Anatomic Pathology ordering in CPRS, please follow the setup instructions in this OR\*3\*569 CPRS AP Order Dialog Setup and Configuration Guide.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for those personnel who need to perform the setup of Anatomic Pathology Order Dialog. These groups include Information Technology Operations and Support (ITOPS) staff, Clinical Application Coordinator (CAC) personnel, and the site’s Lab ADPAC.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This set up/configuration guide provides instructions for how to Configure Anatomic Pathology Order Dialog released in CPRS v32a.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](https://www.va.gov/vdl/section.asp?secid=1)

- *OR\*3\*569 CPRS AP Order Dialog Setup and Configuration Guide*
- *CPRS User Manual: GUI Version (OR\*3.0\*569)*
- *CPRS Technical Manual - GUI Version (OR\*3.0\*569)*
- *CPRS Technical Manual: List Manager Version (OR\*3.0\*569)*
- *OR\*3\*569 Release Notes CPRS GUI*
- *LaboratoryAnatomic Pathology Version5.2 User Guide*
- *Laboratory Version 5.2 Planning Implementation Guide (PIG)*
- *Laboratory Version 5.2 Technical Manual*

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Sites should review their Auto-DC rules and determine if they need to make any changes for AP orders. For example, a test site found that an AP order was auto discontinued at discharge because they had “Lab Service” listed as a type of service to discontinue on discharge. To prevent this, the site chose to include the Anatomic Pathology display group in the “Except Orders in Display Group” section of their auto-DC rules, so that AP orders will not discontinue on discharge.

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with the patch, please enter a ticket with the National Help Desk.

# How to Configure Anatomic Pathology for CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

## Edit the 13 Laboratory Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lab ADPAC: In patch LR\*5.2\*469, there were instructions to create 13 laboratory AP tests. The patch created a CPRS AP Dialog for each of those tests.

These lab tests are:

- BONE MARROW
- BRONCHIAL BIOPSY
- BRONCHIAL CYTOLOGY
- DERMATOLOGY
- FINE NEEDLE ASPIRATE
- GASTROINTESTINAL ENDOSCOPY
- GENERAL FLUID
- GYNECOLOGY (PAP SMEAR)
- RENAL BIOPSY
- TISSUE EXAM
- URINE
- UROLOGY,BLADDER/URETER
- UROLOGY,PROSTATE

For any of these tests the site wants to order in CPRS, the following changes need to made in the LABORATORY TEST (#60) file:

- Make sure the TYPE field (#3) is set to BOTH
- Make sure the SUBSCRIPT field (#4) is set to SURGICAL PATHOLOGY, CYTOLOGY or ELECTRON MICROSCOPY
- Make sure the NATIONAL VA LAB CODE field (#64) is assigned
- Make sure there is at least one entry in the CPRS SCREEN multiple (#21661, sub field .01)

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: ORDER DIALOG// 60 LABORATORY TEST

(1254 entries)

EDIT WHICH FIELD: ALL// TYPE

THEN EDIT FIELD: SUBSCRIPT

THEN EDIT FIELD: NATIONAL VA LAB CODE

THEN EDIT FIELD: CPRS SCREEN (multiple)

EDIT WHICH CPRS SCREEN SUB-FIELD: ALL//

THEN EDIT FIELD:

Select LABORATORY TEST NAME: BONE MARROW

1 BONE MARROW

2 BONE MARROW JM BONE MARROW BROKEN

CHOOSE 1-2: 1 BONE MARROW

TYPE: BOTH//

SUBSCRIPT: SURGICAL PATHOLOGY//

NATIONAL VA LAB CODE: Surgical Pathology Tissue Exam

//

Select CPRS SCREEN: 118-BONE MARROW//

Select LABORATORY TEST NAME:

## Check the ORDERABLE ITEM (#101.43) File for all 13 Laboratory Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the TYPE field in the LABORATORY TEST (#60) file is updated to BOTH, it should automatically update the TYPE field in the ORDERABLE ITEM (#101.43) file to BOTH. For the Laboratory Test entries that were updated to BOTH, verify that the corresponding entries in the ORDERABLE ITEM (#101.43) file are also marked with a type of BOTH.

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: ORDERABLE ITEMS// (5084 entries)

EDIT WHICH FIELD: ALL// TYPE

THEN EDIT FIELD:

Select ORDERABLE ITEMS NAME:BONE MARROW

TYPE: BOTH//

## Additional AP Dialog Configuration (Optional Step)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lab ADPAC and CAC: Anatomic Pathology order dialogs have additional configuration, defined in the AP Dialog Config file (#101.45), that determines the following:

1.  Which order prompts to display, their default values, and if they are hidden or required. Available prompts are Urgency, Collection Date/Time, Specimen Submitted By, Collection Type, How Often, Surgeon/Provider, and Order Comment. All prompts will display in CPRS unless they are specifically hidden.
2.  Which documentation pages are displayed, if they are hidden or required, and any special controls associated with each page (such as radio button or checkbox lists). Available pages are Clinical History, Pre-Operative Diagnosis, Operative Findings and Post-Operative Findings.
3.  Which specimens are allowed for a given test, it’s default collection sample, and any special controls associated with that specific specimen (such as radio button or combo-box lists) that are combined into the specimen description field.

Sites may want to copy existing nationally released AP dialogs to customize prompts, pages, specimens, and any special controls specific to a page or specimen. Quick orders linked to an AP test can only define prompts, pages and specimens allowed by this configuration.

> **NOTE:** For Quick Orders instructions, refer to *Section 5. Creating Orders* in the CPRS Technical Manual: List Manager Version

If the site wants to use additional AP laboratory tests within CPRS, in addition to the 13 AP tests that were standardized nationally, they can do so.

To create a new AP Order Dialog, or copy an existing one, the following steps should be followed:

First, the Lab ADPAC should create a new AP test in the LABORATORY TEST File (#60). The test should:

1.  Have a SUBSCRIPT of SP, CY, or EM.
2.  Be mapped to a NATIONAL VA LAB CODE.
3.  Be mapped to a CPRS SCREEN.
4.  When it’s ready to be used in CPRS, the TYPE should be set to BOTH.

Then, the CAC will need to use the Update AP Order Dialogs \[ORCM UPDATE AP DIALOGS\] option to create a new AP Order Dialog which will be mapped to the Laboratory Test Orderable Item. From the Order Menu Management menu \[ORCM MGMT\], select the AP (Update AP Order Dialogs \[ORCM UPDATE AP DIALOGS\]) option. The option first prompts the user to select if they want to: 1) create a new AP Order Dialog from scratch (“New”); 2) create a new AP Order Dialog by copying an existing order dialog to a new order dialog (”Copy”); or 3) edit an existing Order Dialog (“Edit”). If there are no orderable items that can be used in a new AP order dialog it will automatically enter the Edit mode.

> **NOTE:** When editing one of the pre-configured national entries, the user can only edit the INACTIVE field.

> **NOTE:** A Laboratory Test can be mapped to only one AP Order Dialog. It’s a one-to-one relationship. The 13 pre-configured AP tests are already mapped to a national AP Order Dialog.

It is recommended that the site copy an existing AP Order Dialog (from one of the 13 national ones), instead of trying to create one from scratch, and then edit it as needed. When ready to be used, make sure the INACTIVE field is set to NO.

Select Order Menu Management Option: AP Update AP Order Dialogs

Update Anatomic Pathology Order Dialogs

Before you can copy existing anatomic pathology order dialogs,

or create new order dialogs, you must work with your laboratory

application coordinator to create new, active anatomic pathology

tests in the LABORATORY TEST File (#60) that are mapped to a

CPRS SCREEN.

New, Copy or Edit: (N/C/E): Copy

Existing Anatomic Pathology Order Dialogs:

1 \*BONE MARROW

2 \*BRONCHIAL BIOPSY

3 \*BRONCHIAL CYTOLOGY

4 \*DERMATOLOGY

5 \*FINE NEEDLE ASPIRATE

6 \*GASTROINTESTINAL ENDOSCOPY

7 \*GENERAL FLUID

8 \*GYNECOLOGY (PAP SMEAR)

9 \*RENAL BIOPSY

10 \*TISSUE EXAM

11 \*URINE

12 \*UROLOGY,BLADDER/URETER

13 \*UROLOGY,PROSTATE

\* Indicates a National Standard.

Select Order Dialog to Copy (1-17): 10

TISSUE EXAM

Anatomic Pathology Orderable Items not assigned to an Order Dialog:

1 TISSUE EXAM NEW

Attach Copied Order Dialog to which Orderable Item? (1-1): 1

TISSUE EXAM NEW

Copy TISSUE EXAM order dialog and link it to TISSUE EXAM NEW

orderable item? (Yes or No): NO// YES

NAME: TISSUE EXAM NEW//

INACTIVE: YES//

ALLOW OTHER SPECIMENS:

RESTRICT MULTIPLE SPECIMEN:

Select ORDER PROMPT: HOW OFTEN//

ORDER PROMPT: HOW OFTEN//

HIDE: TRUE//

REQUIRED:

DEFAULT:

Select ORDER PROMPT:

Select PAGE#: 4//

PAGE#: 4//

PAGE TYPE: Post-Operative Findings//

PAGE NAME: Post-Operative Findings Replace

HIDE:

REQUIRED:

WP TITLE:

Select PG BLOCK TITLE:

Select PAGE#:

Select SPECIMEN: TISSUE//

SPECIMEN: TISSUE//

HIDE FROM DESCRIPTION:

DESCRIPTION POSITION:

Select SP BLOCK TITLE: Submission Type//

SP BLOCK TITLE: Submission Type//

INACTIVATE:

REQUIRED:

DEFAULT:

DESCRIPTION POSITION:

Select VALUES: Intra-Op Consult//

VALUES: Intra-Op Consult//

SPECIAL: OPURG;1//

Select VALUES:

Select SP BLOCK TITLE:

COLLECTION SAMPLE HIDE: TRUE//

COLLECTION SAMPLE DEFAULT: AP SPECIMEN//

Select SPECIMEN:

PROMPT CHANGE MESSAGE: \<cType\> was changed from \<oVal\> to \<nVal\>. \$C(13,10)If yo

u do not desire this change, please change the \<cType\> prompt at the top of the

form. Replace

Update Anatomic Pathology Order Dialogs

## Edit the LABORATORY SITE (#69.9) file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Lab ADPAC: Edit the LABORATORY SITE (#69.9) file CPRS AP DIALOG ON field, changing it from NULL or NO to YES.

> Note: A setting of YES will change the function of the VistA option Log-in, anat path \[LRAPLG\] to include a prompt for the order number.

From FILEMAN:

Select OPTION: ?

Answer with OPTION NUMBER, or NAME

Choose from:

1 ENTER OR EDIT FILE ENTRIES

2 PRINT FILE ENTRIES

3 SEARCH FILE ENTRIES

4 MODIFY FILE ATTRIBUTES

5 INQUIRE TO FILE ENTRIES

6 UTILITY FUNCTIONS

7 OTHER OPTIONS

8 DATA DICTIONARY UTILITIES

9 TRANSFER ENTRIES

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: LABORATORY SITE//

EDIT WHICH FIELD: ALL// CPRS AP DIALOG ON

THEN EDIT FIELD:

Select LABORATORY SITE SITE NAME:

CPRS AP DIALOG ON: NO// Y YES

Select LABORATORY SITE SITE NAME:

2.  Clinical Application Coordinator (CAC): The Parameter ORWOR CATEGORY SEQUENCE defines for a site the order of display groups for orders on the Orders tab of CPRS. For the new orders in the ANATOMIC PATHOLOGY display group to be labeled properly, new sequence values must be entered as new Instances for this parameter. The Package level parameter has been exported with the new instance/values for the ANATOMIC PATHOLOGY display group as shown in the example below.

Select OPTION NAME: XPAR MENU TOOLS       General Parameter Tools

   LV     List Values for a Selected Parameter

   LE     List Values for a Selected Entity

   LP     List Values for a Selected Package

   LT     List Values for a Selected Template

   EP     Edit Parameter Values

   ET     Edit Parameter Values with Template

   EK     Edit Parameter Definition Keyword

Select General Parameter Tools Option: LV  List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE     Orders Category Sequence

Values for ORWOR CATEGORY SEQUENCE

Parameter                      Instance             Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 10                   M.A.S.

PKG: ORDER ENTRY/RESULTS REPOR 20                   ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 30                   VITALS/MEASUREMENTS

PKG: ORDER ENTRY/RESULTS REPOR 35                   ACTIVITY

PKG: ORDER ENTRY/RESULTS REPOR 40                   NURSING

PKG: ORDER ENTRY/RESULTS REPOR 50                   DIETETICS

PKG: ORDER ENTRY/RESULTS REPOR 59                   CLINIC INFUSIONS

PKG: ORDER ENTRY/RESULTS REPOR 60                   IV MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 65                   OUTPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 68                   NON-VA MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 69                   CLINIC MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 70                   INPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 74                   ANATOMIC PATHOLOGY

PKG: ORDER ENTRY/RESULTS REPOR 75                   LABORATORY

PKG: ORDER ENTRY/RESULTS REPOR 80                   IMAGING

PKG: ORDER ENTRY/RESULTS REPOR 90                   CONSULTS

PKG: ORDER ENTRY/RESULTS REPOR 100                  PROCEDURES

PKG: ORDER ENTRY/RESULTS REPOR 110                  SURGERY

PKG: ORDER ENTRY/RESULTS REPOR 120                  OTHER HOSPITAL SERVICES

> However, if your site has system or user level sequences defined, then the ANATOMIC PATHOLOGY display group will need to be manually placed in your custom sequences. It is suggested that it display just above LABORATORY. Below is an example of adding the display group to the sequence:

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE     Orders Category Sequence

ORWOR CATEGORY SEQUENCE may be set for the following:

4 User USR \[choose from NEW PERSON\]

8 System SYS \[TEST.SYSTEM.MED.VA.GOV\]

Enter selection: 8 System TEST.SYSTEM.MED.VA.GOV

--- Setting ORWOR CATEGORY SEQUENCE for System: TEST.SYSTEM.MED.VA.GOV ---

Select Sequence: 74

Are you adding 74 as a new Sequence? Yes// YES

Sequence: 74// 74

Display Group: ANATOMIC PATHOLOGY

Select Sequence:

3.  Clinical Application Coordinator (CAC) or other user with FileMan access to the DISPLAY GROUP (#100.98) file: Edit the ANATOMIC PATHOLOGY display group DEFAULT DIALOG and set the value to LR OTHER LAB AP TESTS.

VA FileMan 22.0

Select OPTION: ?

Answer with OPTION NUMBER, or NAME

Choose from:

1 ENTER OR EDIT FILE ENTRIES

2 PRINT FILE ENTRIES

3 SEARCH FILE ENTRIES

4 MODIFY FILE ATTRIBUTES

5 INQUIRE TO FILE ENTRIES

6 UTILITY FUNCTIONS

7 OTHER OPTIONS

8 DATA DICTIONARY UTILITIES

9 TRANSFER ENTRIES

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: DISPLAY GROUP//

EDIT WHICH FIELD: ALL// DEFAULT DIALOG

THEN EDIT FIELD:

Select DISPLAY GROUP NAME: ANATOMIC PATHOLOGY

DEFAULT DIALOG: LR OTHER LAB AP TESTS

Select DISPLAY GROUP NAME:

4.  CAC: Using the 'MN Enter/edit order menus' option, add the Anatomic Pathology order dialog (LR OTHER LAB AP TESTS) to the appropriate order menus for this dialog to be available in CPRS.