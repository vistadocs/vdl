---
title: SR*3*176 Surgery VASQIP 2012 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery VASQIP 2012
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*176
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - surgery
  - updates
  - options
  - associated
  - cardiac
  - fields
  - report
  - prosthesis
page_count: 0
word_count: 1788
section_count: 13
table_count: 19
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p176_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p176_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

![](sr-3-176-surgery-vasqip-2012-release-notes/001.png)

ANNUAL Surgery UPDATES - VASQIP Increment 2

Release Notes

SR\*3\*176

March 2012

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Project Enhancements](#project-enhancements)
- [Surgery Application Updates](#surgery-application-updates)
  - [Surgery Cancellation Modifications](#surgery-cancellation-modifications)
    - [Field Updates – SURGERY File (#130)](#field-updates-surgery-file-130)
    - [Menu Options Updated for Cancellation Modifications](#menu-options-updated-for-cancellation-modifications)
  - [Miscellaneous Additions to Risk Assessment Transmissions](#miscellaneous-additions-to-risk-assessment-transmissions)
    - [Menu Options Associated With Miscellaneous Additions](#menu-options-associated-with-miscellaneous-additions)
  - [Positive Drug Screening](#positive-drug-screening)
    - [Field Updates – SURGERY File (#130)](#field-updates-surgery-file-130-1)
    - [Menu Options Associated With Positive Drug Screening](#menu-options-associated-with-positive-drug-screening)
  - [Consolidation of Shared Cardiac, Non-Cardiac and Transplant Fields](#consolidation-of-shared-cardiac-non-cardiac-and-transplant-fields)
    - [Field Updates – SURGERY File (#130)](#field-updates-surgery-file-130-2)
    - [Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)](#field-updates-surgery-transplant-assessments-file-1395)
    - [Data Update – PERIOPERATIVE OCCURRENCE CATEGORY File (#136.5)](#data-update-perioperative-occurrence-category-file-1365)
    - [Menu Options Updated in Association with Consolidated Fields](#menu-options-updated-in-association-with-consolidated-fields)
  - [Add Serial Number for Prosthesis Items](#add-serial-number-for-prosthesis-items)
    - [Field Updates – SURGERY File (#130), PROSTHESIS INSTALLED (Sub-file \#130.01)](#field-updates-surgery-file-130-prosthesis-installed-sub-file-13001)
    - [Field Updates – PROSTHESIS File (#131.9)](#field-updates-prosthesis-file-1319)
    - [Menu Options Associated With Prosthesis Items](#menu-options-associated-with-prosthesis-items)
  - [Flash Sterilization](#flash-sterilization)
    - [Field Updates – SURGERY File (#130)](#field-updates-surgery-file-130-3)
    - [Menu Options Associated With Flash Sterilization](#menu-options-associated-with-flash-sterilization)
  - [30-Day Readmission](#30-day-readmission)
    - [Field Updates – SURGERY SITE PARAMETERS File (#133)](#field-updates-surgery-site-parameters-file-133)
    - [Menu Options Associated With 30-Day Readmission](#menu-options-associated-with-30-day-readmission)
  - [Update ICD9 to ICD](#update-icd9-to-icd)
    - [Menu Options Associated With Update ICD9 to ICD](#menu-options-associated-with-update-icd9-to-icd)
  - [Remove Quarterly Report References](#remove-quarterly-report-references)
    - [Menu Options Associated With Removing Quarterly Report References](#menu-options-associated-with-removing-quarterly-report-references)
  - [Add Superficial Incisional SSI to Cardiac Outcomes](#add-superficial-incisional-ssi-to-cardiac-outcomes)
    - [Menu Options Associated With Adding Superficial Incisional SSI to Cardiac Outcomes](#menu-options-associated-with-adding-superficial-incisional-ssi-to-cardiac-outcomes)
  - [Defect Fix for Remedy Ticket HD0000000528445](#defect-fix-for-remedy-ticket-hd0000000528445)
  - [Update CPT EXCLUSIONS File (#137)](#update-cpt-exclusions-file-137)
This project enhances the VistA Surgery package for increment 2 in support of the VA Surgery Quality Improvement Program (VASQIP).
The Annual Surgery Updates – VASQIP Increment 2 project addresses enhancements to the existing VistA Surgery application. Enhancements include Field Description Updates as well as minor modifications to the Cardiac, Non-Cardiac and Transplant components of the VistA Surgery application.

# Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the following enhancements:

- Addition of new data fields
- Changes to existing fields
- Changes to data entry screens
- Changes to reports
- Changes to Surgery Risk Assessment and Transplant Assessment transmissions

*(This page included for two-sided copying.)*

# Surgery Application Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application for the Annual Surgery Updates – VASQIP Increment 2 project.

## Surgery Cancellation Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Surgery cancellation functionality is modified so that any surgery case that is placed on the surgery schedule and then cancelled will be retained in the SURGERY file (#130) as a cancelled case regardless of when the case is cancelled. A cancellation reason will be required for every cancellation. Consequently, any scheduled case that is cancelled will be counted as a cancellation on the Report of Cancellations generated by the *Report of Cancellations* \[SROCAN\] option.
- When the *Cancel Scheduled Operation* \[SRSCAN\] option is used to cancel a case and the user chooses to create a new request for the cancelled case, a link to the new request will be stored in the cancelled case in the new field called RESCHEDULED CASE (#79). In the new requested case, the cancelled case will be identified in the new field called PREVIOUSLY SCHEDULED CASE (#78).
- The Report of Cancellations, generated by the *Report of Cancellations* \[SROCAN\] option, is modified to group patient data together within specialty so that all cases for a single patient will be shown together.

### Field Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number       | Description of Change |
|---------------------------------|---------------------------|
| PREVIOUSLY SCHEDULED CASE (#78) | New Field                 |
| RESCHEDULED CASE (#79)          | New Field                 |

### Menu Options Updated for Cancellation Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                         | Description of Change |
|-----------------------------------------|---------------------------|
| *Cancel Scheduled Operation* \[SRSCAN\] | Functionality Update      |
| *Report of Cancellations* \[SROCAN\]    | Functionality Update      |

## Miscellaneous Additions to Risk Assessment Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The name of the operating room as defined in the HOSPITAL LOCATION file (#44) is added to each cardiac and non-cardiac risk assessment transmission and to each 1-liner case transmission.
- The following four fields in the SURGERY file (#130) are added to each 1-liner case transmission and to the list of items checked for by the List of 1-Liner Cases Missing Information which is one of the reports generated by the *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\] option:
- TIME OPERATION BEGAN (#.22)
- TIME OPERATION ENDS (#.23)
- TIME PAT IN OR (#.205)
- TIME PAT OUT OR (#.232)

### Menu Options Associated With Miscellaneous Additions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                | Description of Change |
|----------------------------------------------------------------|---------------------------|
| *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\]    | Functionality Update      |
| *Queue Assessment Transmissions* \[SROA TRANSMIT ASSESSMENTS\] | Functionality Update      |
| *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\]         | Functionality Update      |

## Positive Drug Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new POSITIVE DRUG SCREENING field (#618) is added to the SURGERY file (#130). This field is added to the *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\] option, the *Clinical Information (Enter/Edit*) \[SROA CLINICAL INFORMATION\] option and the *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option. This field is also added to the cardiac and non-cardiac risk assessment transmissions and is added to the list of missing items functionality.

### Field Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number      | Description of Change |
|--------------------------------|---------------------------|
| POSITIVE DRUG SCREENING (#618) | New Field                 |

### Menu Options Associated With Positive Drug Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                   | Description of Change |
|-------------------------------------------------------------------|---------------------------|
| *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\]       | Functionality Update      |
| *Clinical Information (Enter/Edit*) \[SROA CLINICAL INFORMATION\] | Functionality Update      |
| *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]       | Functionality Update      |

## Consolidation of Shared Cardiac, Non-Cardiac and Transplant Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates various fields in the SURGERY file (#130) and in the SURGERY TRANSPLANT ASSESSMENTS file (#139.5) as well as various occurrence category descriptions in the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5) so that common items share common definitions. This patch also replaces various fields with new fields in order to enhance and refine certain data elements that are in common with cardiac and non-cardiac risk assessments and transplant assessments. All the associated data input options, assessment printouts and transmissions are updated accordingly.

### Field Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number                                           | Description of Change |
|---------------------------------------------------------------------|---------------------------|
| STROKE/CVA DURATION (#9 in POSTOP OCCURRENCE multiple field \#1.16) | New Field                 |
| \*CURRENT SMOKER (#202)                                             | Field Marked as Obsolete  |
| FUNCTIONAL HEALTH STATUS (#240)                                     | Field Description Update  |
| ACUTE RENAL FAILURE (#254)                                          | Field Description Update  |
| STROKE/CVA (#256)                                                   | Field Description Update  |
| MYOCARDIAL INFARCTION (#258)                                        | Field Description Update  |
| \*CEREBRAL VASCULAR DISEASE (#264)                                  | Field Marked as Obsolete  |
| \*HISTORY OF TIA'S (#334)                                           | Field Marked as Obsolete  |
| \*CVA/STROKE WITH NEURO DEFICIT (#335)                              | Field Marked as Obsolete  |
| \*CVA/STROKE - NO NEURO DEFICIT (#336)                              | Field Marked as Obsolete  |
| \*DIABETES (#346)                                                   | Field Marked as Obsolete  |
| \*PERIOPERATIVE MI (#385)                                           | Field Marked as Obsolete  |
| \*STROKE (#390)                                                     | Field Marked as Obsolete  |
| \*DIABETES (CARDIAC) (#475)                                         | Field Marked as Obsolete  |
| \*CURRENT SMOKER (CARDIAC) (#510)                                   | Field Marked as Obsolete  |
| TOBACCO USE (#517)                                                  | New Field                 |
| TOBACCO USE TIMEFRAME (#518)                                        | New Field                 |
| DIABETES MELLITUS CHRONIC (#519)                                    | New Field                 |
| DIABETES MELLITUS PREOP MGMT (#520)                                 | New Field                 |
| CVD REPAIR/OBSTRUCTION (#521)                                       | New Field                 |
| HISTORY OF CVD (#522)                                               | New Field                 |

### Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number           | Description of Change |
|-------------------------------------|---------------------------|
| STROKE/CVA (#121)                   | New Field                 |
| \*DIABETES MELLITUS (#147)          | Field Marked as Obsolete  |
| \*CURRENT SMOKER (#171)             | Field Marked as Obsolete  |
| \*CEREBRAL VASCULAR DISEASE (#174)  | Field Marked as Obsolete  |
| RENAL FAILURE REQ. DIALYSIS (#191)  | Field Description Update  |
| PERIOPERATIVE MI (#192)             | Field Description Update  |
| TOBACCO USE (#198)                  | New Field                 |
| TOBACCO USE TIMEFRAME (#199)        | New Field                 |
| DIABETES MELLITUS CHRONIC (#200)    | New Field                 |
| DIABETES MELLITUS PREOP MGMT (#201) | New Field                 |
| CVD REPAIR/OBSTRUCTION (#202)       | New Field                 |
| HISTORY OF CVD (#203)               | New Field                 |

### Data Update – PERIOPERATIVE OCCURRENCE CATEGORY File (#136.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Occurrence Category | Description of Change      |
|-------------------------|--------------------------------|
| ACUTE RENAL FAILURE     | DESCSRIPTION Field (#2) Update |
| MYOCARDIAL INFARCTION   | DESCSRIPTION Field (#2) Update |
| STROKE/CVA              | DESCSRIPTION Field (#2) Update |

### Menu Options Updated in Association with Consolidated Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                       | Description of Change |
|-----------------------------------------------------------------------|---------------------------|
| *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\]           | Menu Items Update         |
| *Postoperative Occurrences (Enter/Edit)* \[SRO POSTOP COMP\]          | Menu Items Update         |
| *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\] | Menu Items Update         |
| *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]     | Menu Items Update         |
| *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\]          | Menu Items Update         |
| *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]           | Menu Items Update         |
| *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\]           | Menu Items Update         |
| *Enter/Edit Transplant Assessments* \[SR TRANSPLANT ENTER/EDIT\]      | Menu Items Update         |
| *Print Transplant Assessment* \[SRTP PRINT ASSESSMENT\]               | Menu Items Update         |

## Add Serial Number for Prosthesis Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Two new fields, LOT NUMBER (#11) and SERIAL NUMBER (#12) are added to the PROSTHESIS INSTALLED multiple field (#.47, sub-file \#130.01) to replace the existing LOT/SERIAL NO field (#2.5). The *Operation* \[SROMEN-OP\] option and the *Nurse Intraoperative Report* \[SRONRPT\] option are updated to allow editing and display of these two new fields. For each prosthesis item entered for a surgical case, these two new fields will be required for signing the Nurse Intraoperative Report.
- LOT NUMBER field (#8) and SERIAL NUMBER field (#9) are added to the PROSTHESIS file (#131.9). The *Update Site Configurable Files* \[SR UPDATE FILES\] option is modified to allow editing of these new fields and to disallow editing of the LOT/SERIAL NO field (#4) and the STERILE CODE field (#3).

### Field Updates – SURGERY File (#130), PROSTHESIS INSTALLED (Sub-file \#130.01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| LOT NUMBER (#11)          | New Field                 |
| SERIAL NUMBER (#12)       | New Field                 |

### Field Updates – PROSTHESIS File (#131.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| LOT NUMBER (#8)           | New Field                 |
| SERIAL NUMBER (#9)        | New Field                 |

### Menu Options Associated With Prosthesis Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                      | Description of Change                      |
|------------------------------------------------------|------------------------------------------------|
| *Operation* \[SROMEN-OP\]                            | Input Template Update                          |
| *Nurse Intraoperative Report* \[SRONRPT\]            | Input Template Update and Functionality Update |
| *Update Site Configurable Files* \[SR UPDATE FILES\] | Functionality Update                           |

## Flash Sterilization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Six new fields are added to the SURGERY file (#130) for use in documenting the number of episodes of each type of flash sterilization that happened for an operation. These fields are added to the *Post Operation* \[SROMEN-POST\] option and the *Nurse Intraoperative Report* \[SRONRPT\] option to allow editing and display of this information.

### Field Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number     | Description of Change |
|-------------------------------|---------------------------|
| FLASH-CONTAMINATION (#619)    | New Field                 |
| FLASH-SPD/OR MAN ISSUE (#620) | New Field                 |
| FLASH-EMERGENCY CASE (#621)   | New Field                 |
| FLASH-NO BETTER OPTION (#622) | New Field                 |
| FLASH-LOANER (#623)           | New Field                 |
| FLASH-DECONTAMINATION (#624)  | New Field                 |

### Menu Options Associated With Flash Sterilization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                           | Description of Change                      |
|-------------------------------------------|------------------------------------------------|
| *Post Operation* \[SROMEN-POST\]          | Input Template Update                          |
| *Nurse Intraoperative Report* \[SRONRPT\] | Input Template Update and Functionality Update |

## 30-Day Readmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch creates a transmission report that lists inpatient surgery cases that were followed by the patient being readmitted within 30 days of discharge. This report is run by the *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\] option and will transmit to the VASQIP database automatically each quarter, using the new LATEST 30-DAY READMISSION field (#8), added to the SURGERY SITE PARAMETERS file (#133), to determine when the report is due for transmission.

### Field Updates – SURGERY SITE PARAMETERS File (#133)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number         | Description of Change |
|-----------------------------------|---------------------------|
| LATEST 30-DAY READMIT REPORT (#8) | New Field                 |

### Menu Options Associated With 30-Day Readmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                        | Description of Change |
|--------------------------------------------------------|---------------------------|
| *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\] | Functionality Update      |

## Update ICD9 to ICD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three menu options are modified to replace references to ICD9 with ICD.

### Menu Options Associated With Update ICD9 to ICD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                               | Description of Change        |
|---------------------------------------------------------------|----------------------------------|
| *CPT/ICD9 Coding Menu* \[SRCODING MENU\]                      | Menu Text and Description Update |
| *CPT/ICD9 Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] | Menu Text and Description Update |
| *Update/verify Procedure/Diagnosis Codes* \[SRCODING EDIT\]   | Description Update               |

## Remove Quarterly Report References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- References to "Quarterly Report" are removed from the *Deaths Within 30 Days of Surgery* \[SROQD\] option.
- The routine functionality that generated the Surgery Quarterly Report is removed.

### Menu Options Associated With Removing Quarterly Report References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                | Description of Change |
|----------------------------------------------------------------|---------------------------|
| *Deaths Within 30 Days of Surgery* \[SROQD\]                   | Functionality Update      |
| *Quarterly Report - Surgical Service* \[SRO QUARTERLY REPORT\] | Functionality Update      |

## Add Superficial Incisional SSI to Cardiac Outcomes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SUPERFICIAL INCISIONAL SSI field (#248) in the SURGERY file (#130) is added to the *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\] option, the cardiac assessment transmission and to the cardiac assessment printout.

### Menu Options Associated With Adding Superficial Incisional SSI to Cardiac Outcomes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                | Description of Change |
|----------------------------------------------------------------|---------------------------|
| *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\]   | Functionality Update      |
| *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]    | Functionality Update      |
| *Queue Assessment Transmissions* \[SROA TRANSMIT ASSESSMENTS\] | Functionality Update      |
| *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\]         | Functionality Update      |

## Defect Fix for Remedy Ticket HD0000000528445

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remedy ticket, HD0000000528445, involving two fields from the Time Out Verified Utilizing Checklist has been resolved. The Nurse Intraoperative Report has been updated to correctly display the values entered for the PREOPERATIVE IMAGES CONFIRMED (#606) field and the MARKED SITE CONFIRMED (#605) field.

## Update CPT EXCLUSIONS File (#137)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPT EXCLUSIONS file (#137) is updated with the excluded CPT codes for Fiscal Year 2012. This file is used internally by the software to identify surgical cases eligible for assessment.

##