---
title: SR*3*174 Surgery VASQIP 2010 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery VASQIP 2010
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*174
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - cardiac
  - assessment
  - updates
  - table
  - contents
  - surgery
  - risk
  - enhancements
  - valve
  - added
page_count: 0
word_count: 1191
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p174_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p174_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

![](sr-3-174-surgery-vasqip-2010-release-notes/001.png)

ANNUAL Surgery UPDATES - VASQIP 2010

Release Notes

SR\*3\*174

December 2010

Office of Enterprise Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Project Enhancements](#project-enhancements)
- [Annual Surgery Updates - VASQIP](#annual-surgery-updates-vasqip)
- [Non-Cardiac Software Risk Assessment Enhancements](#non-cardiac-software-risk-assessment-enhancements)
  - [Field Updates](#field-updates)
  - [Non-Cardiac Assessment Option Updates](#non-cardiac-assessment-option-updates)
  - [Non-Cardiac Assessment Data Transmissions](#non-cardiac-assessment-data-transmissions)
  - [Data Updates](#data-updates)
- [Cardiac Risk Assessment Software Enhancements](#cardiac-risk-assessment-software-enhancements)
  - [Field Updates](#field-updates-1)
  - [Cardiac Assessment Option Updates](#cardiac-assessment-option-updates)
  - [Cardiac Assessment Data Transmissions](#cardiac-assessment-data-transmissions)
  - [Data Updates](#data-updates-1)
This project enhances the Vista Surgery package in support of the VA Surgery Quality Improvement Program (VASQIP).
The Annual Surgery Updates – VASQIP project addresses enhancements to the existing Risk Assessment Module within the VistA Surgery application. Enhancements are mainly field definitions and data entry screen changes.

# Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the following enhancements:

- Addition of new risk indicators for VASQIP
- Changes to data entry screens to reflect revisions to indicators
- Changes to field definitions for risk indicators
- Changes to print assessment options to reflect changes to risk indicators
- Changes to transmission of surgery risk assessments

*(This page included for two-sided copying.)*

# Annual Surgery Updates - VASQIP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application for the Annual Surgery Updates project.

The updates are described in the following two sections: Non-Cardiac Risk Assessment Software Enhancements and Cardiac Risk Assessment Software Enhancements.

# Non-Cardiac Software Risk Assessment Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Non-Cardiac Software Enhancements include data dictionary updates, option modifications, and data transmission updates.

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields in the SURGERY file (#130) were modified:

- The ASA CLASS (#1.13) was updated to change the list of choices for ASA Classification to include N – NONE ASSIGNED. No change in field definition was required.

The following fields in the SURGERY file (#130) were added:

- ASSESSMENT COMPLETED BY (#272.1)
- PREOPERATIVE SLEEP APNEA (#237.1)

The following Non-Cardiac fields in the SURGERY file (#130) were modified to include changes in the field definition or help text. Refer to the VASQIP SCNR Operations Manual for a complete list of current field definitions.

| Field Name and Number                                       | Description of Change |
|-----------------------------------------------------------------|---------------------------|
| BLEEDING DISORDER (#216)                                        | Definition Update         |
| DVT/THROMBOPHLEBITIS (#263)                                     | Definition Update         |
| HEIGHT (#236)                                                   | Definition Update         |
| HISTORY OF COPD (#203)                                          | Definition Update         |
| INTRAOPERATIVE ASCITES (#446)                                   | Definition Update         |
| INTRAOPERATIVE DISSEMINATED CANCER (#443)                       | Definition Update         |
| DISSEMINATED CANCER (Y/N)(#338)                                 | Definition Update         |
| ASCITES (#212)                                                  | Definition Update         |
| OTHER PROCEDURE (#.01 in OTHER PROCEDURES multiple field \#.42) | Definition Update         |
| WEIGHT (#237)                                                   | Definition Update         |

## Non-Cardiac Assessment Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options were modified:

- The following field in the *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\] option was added:
  - PREOPERATIVE SLEEP APNEA (*\#237.1)* is added as item 1G on page 1 of the option.
- The following fields in the *Patient Demographics (Enter/Edit)* \[SROA DEMOGRAPHICS\] option were removed:
  - DATE SURGERY CONSULT REQUESTED and SURGERY CONSULT DATE have been removed from the data entry screen.
- The *Operation Information (Enter/Edit)* \[SROA OPERATION DATA\] option was updated to include the following:
  - When selecting the field CPT Codes (view only) within the Operation Information (Enter/Edit) option, the following note will be displayed on the screen:

> CPT Codes should be verified. If need be, report discrepancies to the official CPT coder for surgery.

- When selecting the field for Concurrent Procedure within the Operation Information (Enter/Edit) option, the following note will be displayed on the screen:

> Concurrent Procedure: An additional operative procedure performed by a different surgical team (i.e., a different specialty/service) under the same anesthetic which has a CPT code different from that of the Principal Operative Procedure (e.g., fixation of a femur fracture in a patient undergoing a laparotomy for trauma). This field should be verified and, if need be, report discrepancies to the official CPT coder for surgery.

- The Print Risk Assessment \[SROA PRINT ASSESSMENT\] option was updated for Non-Cardiac Assessments

> The following fields were removed:

- DATE SURGERY CONSULT REQUESTED
- SURGERY CONSULT DATE

> The following field was added:

- PREOPERATIVE SLEEP APNEA (#237.1)

## Non-Cardiac Assessment Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 1-Liner cases will be transmitted on the 45th day past the end of the month rather than on the 45th day past the end of the quarter.
- Gender has been added to the 1-Liner cases.
- The name of the individual who completed the assessment has been added to all non-cardiac transmissions.

## Data Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Class N for None Assigned was added to the ASA CLASS file (#132.8).
- The description of DVT/THROMBOPHLEBITIS was updated in the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5).
- The CPT EXCLUSIONS file (#137) was updated with the excluded CPT codes for FY10. This file is used internally by the software to identify surgical cases eligible for assessment.

# Cardiac Risk Assessment Software Enhancements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cardiac Risk Assessment software enhancements include data dictionary updates and option modifications.

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields were added to the SURGERY file (#130):

- PREOPERATIVE ATRIAL FIBRILLATION (#509)
- PULMONARY VALVE PROCEDURE (#493)
- POSTOPERATIVE ATRIAL FIBRILLATION (#448)
- BNP (#507)
- BNP DATE (#507.1)

The following fields in the SURGERY file (#130) were modified:

- AORTIC VALVE REPLACEMENT (#367) was renamed AORTIC VALVE PROCEDURE.
- MITRAL VALVE REPLACEMENT (#368) was renamed MITRAL VALVE PROCEDURE.
- TRICUSPID VALVE REPLACEMENT (#369) was renamed TRICUSPID VALVE PROCEDURE.

The following Cardiac fields in the SURGERY file (#130) were modified to include changes in the field definition or help text. Refer to the VASQIP SCNR Operations Manual for a complete list of current field definitions.

| Field Name and Number                                    | Description of Change              |
|--------------------------------------------------------------|----------------------------------------|
| AORTIC VALVE REPLACEMENT (#367)                              | Definition Update                      |
| D/T PATIENT DISCH FROM ICU (#471)                            | Definition Update                      |
| ENDOVASCULAR REPAIR (#505)                                   | Title, Definition and Help Text Update |
| FUNCTIONAL STATUS (#240)                                     | Definition Update                      |
| PREOPERATIVE USE OF NEW MECHANICAL CIRCULATORY DEVICE (#474) | Definition Update                      |
| MITRAL VALVE REPLACEMENT (#368)                              | Definition Update                      |
| TRICUSPID VALVE REPLACEMENT (#369)                           | Definition Update                      |

## Cardiac Assessment Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options were modified:

- The following fields in the *Resource Data* \[SROA CARDIAC RESOURCE\] option were removed:
  - CT SURGERY CONSULT DATE (#513)
  - PRIMARY CAUSE FOR DELAY FOR CARDIAC SURGERY (#515)
- The *Print Risk Assessment* \[SROA PRINT ASSESSMENT\] option was updated for Cardiac Assessments

> The following fields were removed:

- CT SURGERY CONSULT DATE (#513)
- PRIMARY CAUSE FOR DELAY FOR CARDIAC SURGERY (#515)
- VALVE REPAIR (#370)

> The following fields were added:

- PREOPERATIVE ATRIAL FIBRILLATION (#509)
- PULMONARY VALVE PROCEDURE (#493)
- POSTOPERATIVE ATRIAL FIBRILLATION (#448)
- BNP (#507)
- BNP DATE (507.1)
- The following field in the *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\] option was added:
  - PREOP ATRIAL FIBRILLATION (#509). This field was added as item \#25.
- The following fields in the *Operative Risk Summary Data* (*Enter/Edit*) \[SROA CARDIAC OPERATIVE RISK\] option were removed:
  - TIME OPERATION BEGAN (#.22)
  - TIME OPERATION ENDED (#.23)
- The following fields in the *Resource Data* \[SROA CARDIAC RESOURCE\] option were added:
  - TIME OPERATION BEGAN (#.22)
  - TIME OPERATION ENDED (#.23)
- The following fields in the *Laboratory Test Results* (*Enter/Edit*) \[SROA LAB\] option were added:
  - BNP (#507). This lab test B-type Natriuretic Peptide was added as item 11.
  - BNP DATE (#507.1)
- The *Risk Model Lab Test (Enter/Edit)* \[SROA LAB TEST EDIT\] option was updated to allow B-Type Natriuretic Peptide (BNP) to be edited in the RISK MODEL LAB TEST file (#139.2).
- The *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] option section related to valve procedures was modified to display the following fields
- AORTIC VALVE PROCEDURE (#367)
- MITRAL VALVE PROCEDURE (#368)
- TRICIUSPID VALVE PROCEDURE (#369)
- PULMONARY VALVE PROCEDURE (#493)

> The following field is no longer displayed in the section related to valve procedures:

- VALVE REPAIR (#370)
- The *Quarterly Report - Surgical Service* \[SRO QUARTERLY REPORT\] option was modified to display the Postop Atrial Fibrillation total in the PERIOPERATIVE OCCURRENCE CATEGORIES section of the report and to include that total when the report transmits.

## Cardiac Assessment Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields were added to the cardiac assessment transmissions:

- PREOPERATIVE ATRIAL FIBRILLATION (#509)
- PULMONARY VALVE PROCEDURE (#493)
- POSTOPERATIVE ATRIAL FIBRILLATION (#448)
- BNP (#507)
- BNP DATE (#507.1)

## Data Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- B-TYPE NATRIURETIC PEPTIDE (BNP) was added to the RISK MODEL LAB TEST file (#139.2).
- POSTOPERATIVE ATRIAL FIBRILLATION was added to the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5).