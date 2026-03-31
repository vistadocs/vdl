---
title: DG*5.3*869/892/TIU*1*279 Missing Patient PRF Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*869
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - flag
  - missing
  - record
  - category
  - table
  - contents
  - national
  - project
  - report
page_count: 0
word_count: 1305
section_count: 5
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 6
revision_newest: 04/20/15
revision_oldest: 05/29/13
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/missing_patient_prf_release_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/missing_patient_prf_release_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

Missing Patient

Patient Record Flag (PRF)

Patches

DG\*5.3\*892

DG\*5.3\*869

TIU\*1.0\*279

Release Notes

![](dg-5-3-869-892-tiu-1-279-missing-patient-prf-release-notes/001.png)

Version 0.6April 2015

Revision History

|          |          |                                                                                                                 |                                    |
|----------|----------|-----------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date     | Revision | Description                                                                                                     | Author                             |
| 04/20/15 | 0.6      | DG\*5.3\*892 - On page 6, update to National Category I Patient Record Flag (PRF).                              | <span class="mark">REDACTED</span> |
| 11/13/13 | 0.5      | Incorporated final comments. Updated and added TIU User Manual to list of Related Documentation, pages 1 and 2. | <span class="mark">REDACTED</span> |
| 11/06/13 | 0.4      | Incorporated comments from SQA review.                                                                          | <span class="mark">REDACTED</span> |
| 09/24/13 | 0.3      | Incorporated team comments.                                                                                     | <span class="mark">REDACTED</span> |
| 08/15/13 | 0.2      | Editing and formatting review.                                                                                  | <span class="mark">REDACTED</span> |
| 05/29/13 | 0.1      | Initial Draft of Missing - Patient Record Flag Release Notes.                                                   | <span class="mark">REDACTED</span> |

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [## Related Documentation](#related-documentation)
  - [Related Web Sites](#related-web-sites)
- [Release Notes](#release-notes)
  - [## Project Overview](#project-overview)
- [Project Features](#project-features)
    - [Registration – Patient Record Flag (DG)](#registration-patient-record-flag-dg)
  - [Text Integration Utility (TIU)](#text-integration-utility-tiu)
- [# Acronyms](#acronyms)
This request was submitted by the Veterans Health Administration (VHA) Head Quarters Clinical/Quality Assurance Liaison and Deputy under Secretary for Health for Operations & Management. In the early 1990s, the Government Accountability Office mandated that a mechanism be developed to identify missing patients. This request is to utilize Missing Patient - Patient Record Flag (PRF), replacing the no longer in use Missing Patient Registry software system.
The now defunct software system would have been costly due to required redesigning, to bring the registry into compliance with current Health Insurance Portability and Accountability Act (HIPAA) and encryption requirements. The requirements for this project are documented in the Missing Patient - PRF Requirements Specification Document (RSD).
The Missing Patient - PRF project includes two (2) patches.
TIU\*1\*279 Create Missing Patient - PRF TIU Title
The Text Integration Utilities (TIU) patch creates and installs a new TIU Progress Note Title, PATIENT RECORD FLAG CATEGORY I – MISSING PATIENT. This flag-title will have the MENTAL HEALTH PATIENT RECORD FLAG Enterprise Standard Title, and PATIENT RECORD FLAG CAT I Document Class.
DG\*5.3\*869 MISSING PATIENT - Patient Record Flag
A new National Category I Patient Record Flag (PRF) for missing or wandering patients/residents is introduced by this patch. This PRF is to ensure that each Department of Veterans Affairs' (VA) medical facility has an effective and reliable plan to prevent, and effectively manage wandering and missing patient events that place patients at-risk for harm.

## ## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIU\*1\*279 Documentation

|                                             |                                            |
|---------------------------------------------|--------------------------------------------|
| Documentation                           | Documentation File name                |
| Missing Patient PRF Installation Guide (IG) | Missing Patient PRF_Installation Guide.PDF |
| Missing Patient PRF Release Notes (RN)      | Missing Patient PRF_Release Notes.PDF      |
| TIU Technical Manual (TM)                   | TIUTM.PDF                                  |
| TIU User Manual (UM)                        | TIUUM.PDF                                  |

  
DG\*5.3\*869 Documentation

|                                                               |                                            |
|---------------------------------------------------------------|--------------------------------------------|
| Documentation                                             | Documentation File name                |
| Missing Patient PRF Installation Guide (IG)                   | Missing Patient PRF_Installation Guide.PDF |
| Missing Patient PRF Release Notes (RN)                        | Missing Patient PRF_Release Notes.PDF      |
| Patient Record Flags User Guide (UG)                          | Patient Record Flags_User Guide.PDF        |
| Patient Information Management System (PIMS) Technical Manual | PIMSTM.PDF                                 |

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                         |                          |                                                                   |
|-----------------------------------------------------------------------------------------|--------------------------|-------------------------------------------------------------------|
| SITE                                                                                | URL                  | DESCRIPTION                                                   |
| Veterans Health Information System and Technology Architecture (VistA) Document Library | <http://www.va.gov/vdl/> | Contains manuals for Clinical Reminders and related applications. |

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Project Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A request was submitted by the Veterans Health Administration (VHA) Head Quarters Clinical/Quality Assurance Liason and Deputy Under Secretary for Health for Operations and Management, to develop a mechanism for identifying missing patients.

This request is to utilize the new Missing Patient - Patient Record Flag replacing the Missing Patient Registry software system, which is no longer in use.

#### Remedy Tickets Fixed

There were no Remedy Tickets fixed in this release. This project is new development only.

# Project Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Registration – Patient Record Flag (DG)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*869 installs a new National Category I Patient Record Flag (PRF): MISSING PATIENT.

The Category I PRF for Missing Patient will not be available to the site until the install is completed. Furthermore, the official National, Category I MISSING PATIENT PRF cannot be assigned to a patient until all installation steps have been completed on each Veterans Health Information System and Technology Architecture (VistA) System.

The Missing Patient PRF project will implement the following features.

1\. Creates a new 'MISSING PATIENT' National Category I PRF entry in the PRF NATIONAL FLAG File (#26.15). This new, National Category I PRF will be defined as follows.

Name: MISSING PATIENT

Status: ACTIVE

Type: CLINICAL

Review Frequency Days: 30

Notification Days: 7

Review Mail Group: DGPF MISSING PT FLAG REVIEW

> TIU Progress Note (PN) Title: PATIENT RECORD FLAG CATEGORY I - MISSING PATIENT

> Description: The purpose of this flag is to identify a missing patient/resident (patient) in the electronic medical record, including a Text Integration Utilities (TIU) progress note describing the risk and circumstances.

> **NOTE:** Activating or deactivating the flag is a manual process. The status of the flag will remain Active while the patient is missing. The user will not have the ability to delete the flag but will have the ability to deactivate the flag when the patient has been found. Also, the flag and history remains within the PRF package.

> **IMPORTANT:** Users must be assigned the DGPF ASSIGNMENT security key to assign the Missing Patient PRF.

2\. Creates a new mail group, DGPF MISSING PT FLAG REVIEW. Members of this mail group will receive messages when the patient’s flag needs to be reviewed, following existing PRF review processes of continue, inactivate or delete.

3\. Update Dialog Number 261132-Patient has local ICN (field \#4) in file \#.84 to change the message that is displayed when there is an attempt by a user to assign any National, CAT I PRF to the record of a patient that does not have a National ICN. This component updates Text (field \#4) to not reference any specific National, Category I PRF (i.e. BEHAVIORAL) to be assigned.

4\. Updates the following PRF reports to include the new Missing Patient PRF.

- Assignment Action Not Linked Report
- Flag Assignment Report
- Patient Assignments Report
- Assignments Due For Review Report
- Assignments Approved By Report

These reports can be produced via the VistA, Record Flag Reports Menu

> Select OPTION NAME: DGPF RECORD FLAG REPORTS MENU Record Flag Reports Menu

> NLR Assignment Action Not Linked Report

> FAR Flag Assignment Report

> PAR Patient Assignments Report

> ADR Assignments Due For Review Report

> BAR Assignments Approved By Report

> Select Record Flag Reports Menu Option:

<span id="_Toc372118191" class="anchor"></span>Figure 1: DGPF Record Flag Reports Menu  
Report Example

Select Record Flag Reports Menu Option: FA Flag Assignment Report

Select one of the following:

1 Category I (National)

2 Category II (Local)

3 Both

Select Flag Category: 1 Category I (National)

Select one of the following:

S Single Flag

A All Flags

Select to report on a (S)ingle flag or (A)ll flags: Single Flag// Single Flag

Select Record Flag Name: MISSING PATIENT ACTIVE CLINICAL

Select Beginning Date: (3/14/2002 - 5/29/2013): T-60 (MAR 30, 2013)

Select Ending Date: (3/30/2013 - 5/29/2013): T (MAY 29, 2013)

DEVICE: HOME// DEC Windows

PATIENT RECORD FLAGS

FLAG ASSIGNMENT REPORT Page: 1

---------------------- Printed: May 29, 2013@09:01

CATEGORY: Category I (National)

DATE RANGE: 03/30/13 TO 05/29/13

FLAG NAME: MISSING PATIENT

PATIENT NAME SSN ASSIGNED REVIEW DT STATUS OWNING SITE

-------------------- --------- -------- -------- -------- -----------------

MPRFLZZZ,TESTZZZ 705101465P 05/28/13 06/04/13 ACTIVE CHEYENNE VAMC

ZZZPMS,XXXXX 666443498 05/09/13 06/08/13 ACTIVE CHEYENNE VAMC

ZZZZTESTPRF,PRFMP 666666665 05/09/13 06/08/13 ACTIVE CHEYENNE VAMC

Total Assignments for Flag: 3

\<End of Report\>

  
Ownership of Category I flag

Each Category I flag assignment to a specific patient’s record is owned by a single facility. The facility that placed the Category I flag on the patient’s record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:

- Review whether to remove or continue the flag
- Edit the flag
- Inactivate the flag
- Reactivate the flag
- Mark the flag as entered in error
- Change ownership of the flag
- Enter a Patient Record Flag Category I progress note for the flag

Ownership of a Category I flag assignment can be transferred. If a patient receives the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to that site. The owning site could then change the ownership to the second site through the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] menu option, which is located in the Patient Record Flags Main Menu \[DGPF RECORD FLAGS MAIN MENU\].

DG\*5.3\*869 post-installation steps on every VistA system

- For a user to have the ability to assign the National CAT I MISSING PATIENT, PRF, that user must hold the DGPF Assignment security key.

TIU\*1.0\*279 post-installation steps on every VistA system

- For a user to view PRF linked TIU Progress Note Titles, that user must be a member of the 'DGPF PATIENT RECORD FLAGS MGR' User Class.

Users can view the Category I, MISSING PATIENT, PRF via the Computerized Patient Record System (CPRS) graphical user interface (GUI).

![](dg-5-3-869-892-tiu-1-279-missing-patient-prf-release-notes/002.png)

<span id="_Toc372118192" class="anchor"></span>Figure 2: PRF Category I Flag Example

## Text Integration Utility (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIU\*1.0\*279 installs a new TIU DOCUMENT DEFINITION (file \#8925.1) title: PATIENT RECORD FLAG CATEGORY I – MISSING PATIENT to be used with the new Patient Record Flag. The patch installation links the title to the existing document class PATIENT RECORD FLAG CAT I.

![](dg-5-3-869-892-tiu-1-279-missing-patient-prf-release-notes/003.png)

<span id="_Toc372118193" class="anchor"></span>Figure 3: Missing Patient, TIU Progress Note Availability

\* Note: The user must be a member of the ‘DGPF PATIENT RECORD FLAGS MGR’ User Class to view and process any Patient Record Flag, Progress Note Title.

# # Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of acronyms from this document. For additional acronyms, refer to the [OIT Master Glossary](http://vaww.oed.wss.va.gov/process/OIT%20Master%20Glossary/Home.aspx).

| TERM  | DEFINITION                                                     |
|-------|----------------------------------------------------------------|
| CPRS  | Computerized Patient Record System                             |
| DG    | Registration and Enrollment Package namespace                  |
| GUI   | Graphic User Interface                                         |
| IG    | Install Guide                                                  |
| HIPAA | Health Insurance Portability and Accountability Act            |
| MPRF  | Missing - Patient Record Flag                                  |
| OIT   | Office of Information Technology                               |
| PIMS  | Patient Information Management System                          |
| PN    | Progress Note                                                  |
| PRF   | Patient Record Flag                                            |
| RN    | Release Notes                                                  |
| RSD   | Requirements Specification Document                            |
| TIU   | Text Integration Utilities                                     |
| TM    | Technical Manual                                               |
| UG    | User Guide                                                     |
| VA    | Department of Veteran Affairs                                  |
| VHA   | Veterans Health Administration                                 |
| VistA | Veterans Health Information System and Technology Architecture |