---
title: SR*3*175 Surgery VASQIP 2011 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery VASQIP 2011
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*175
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - surgery
  - table
  - contents
  - updates
  - assessment
  - updated
  - transplant
  - fields
  - risk
  - changes
page_count: 0
word_count: 2142
section_count: 7
table_count: 25
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p175_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p175_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

![](sr-3-175-surgery-vasqip-2011-release-notes/001.png)

ANNUAL Surgery UPDATES - VASQIP 2011 Increment 1

Release Notes

SR\*3\*175

September 2011

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Project Enhancements](#project-enhancements)
- [General Surgery Updates](#general-surgery-updates)
  - [Menu Options Placed Out of Order](#menu-options-placed-out-of-order)
    - [Menu Options Placed Out of Order, Relocated and/or Modified](#menu-options-placed-out-of-order-relocated-andor-modified)
  - [Remove/Replace References to “NSQIP” and “CICSP”](#removereplace-references-to-nsqip-and-cicsp)
    - [Field Description Updates – SURGERY File (#130)](#field-description-updates-surgery-file-130)
    - [Field Updates – SURGERY SITE PARAMETERS File (#133)](#field-updates-surgery-site-parameters-file-133)
    - [Data Update – PERIOPERATIVE OCCURRENCE CATEGORY File (#136.5)](#data-update-perioperative-occurrence-category-file-1365)
    - [File and Field Update – CPT EXCLUSIONS File (#137)](#file-and-field-update-cpt-exclusions-file-137)
    - [Field Updates – RISK MODEL LAB TEST File (#139.2)](#field-updates-risk-model-lab-test-file-1392)
    - [Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)](#field-updates-surgery-transplant-assessments-file-1395)
    - [Options Updated to Remove/Replace References to “NSQIP” and “CICSP”](#options-updated-to-removereplace-references-to-nsqip-and-cicsp)
  - [Addition of Scheduling Date Fields](#addition-of-scheduling-date-fields)
    - [New Scheduling Date Fields – SURGERY File (#130)](#new-scheduling-date-fields-surgery-file-130)
    - [Menu Options Changed to Capture Scheduling Date Fields](#menu-options-changed-to-capture-scheduling-date-fields)
  - [Time Out Verified Utilizing Checklist](#time-out-verified-utilizing-checklist)
    - [Time Out Verified Checklist Fields – SURGERY File (#130)](#time-out-verified-checklist-fields-surgery-file-130)
    - [Menu Options Updated or Added for Time Out Verified Utilizing Checklist](#menu-options-updated-or-added-for-time-out-verified-utilizing-checklist)
  - [Standard SURGERY CANCELLATION REASON File (#135)](#standard-surgery-cancellation-reason-file-135)
    - [Cancellation Comments Field – SURGERY File (#130)](#cancellation-comments-field-surgery-file-130)
    - [Standard Cancellation Reasons – Modified Option](#standard-cancellation-reasons-modified-option)
  - [Miscellaneous Changes](#miscellaneous-changes)
    - [Display Leading Zero – SURGERY File (#130)](#display-leading-zero-surgery-file-130)
    - [Miscellaneous Changes - Menu Option Updates](#miscellaneous-changes-menu-option-updates)
- [Surgery Risk Assessment Changes](#surgery-risk-assessment-changes)
    - [Risk Assessment Field Updates – SURGERY File (#130)](#risk-assessment-field-updates-surgery-file-130)
    - [Data Update – CPT EXCLUSIONS File (#137)](#data-update-cpt-exclusions-file-137)
    - [Risk Assessment Option Updates](#risk-assessment-option-updates)
- [Surgery Transplant Assessment Changes](#surgery-transplant-assessment-changes)
    - [- HLA typing fields in the SURGERY TRANSPLANT ASSESSMENTS file (#139.5) across all four organ types were updated to allow entry of 4 digits. The transplant transmissions were updated to allow the longer data items to be transmitted.](#hla-typing-fields-in-the-surgery-transplant-assessments-file-1395-across-all-four-organ-types-were-updated-to-allow-entry-of-4-digits-the-transplant-transmissions-were-updated-to-allow-the-longer-data-items-to-be-transmitted)
    - [### Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)](#field-updates-surgery-transplant-assessments-file-1395-1)
    - [Transplant Assessment Option Updates](#transplant-assessment-option-updates)
This project enhances the VistA Surgery package for increment 1in support of the VA Surgery Quality Improvement Program (VASQIP).
The Annual Surgery Updates – VASQIP 2011 Increment 1 project addresses enhancements to the existing VistA Surgery application. Enhancements include Field Description Updates as well as minor modifications to the Cardiac, Non-Cardiac and Transplant components of the VistA Surgery application.

# Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the following enhancements:

- Addition of new data fields
- Changes to existing fields
- Changes to data entry screens
- Changes to reports
- Changes to Surgery Risk Assessment transmissions
- Changes to Transplant components of the VistA Surgery Application

*(This page included for two-sided copying.)*

# General Surgery Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application related to general updates for the Annual Surgery Updates – VASQIP 2011 Increment 1project.

## Menu Options Placed Out of Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Quarterly Report Menu \[SROQ MENU\] was placed out of order and all the reports on that menu were placed out of order except for three reports that were moved to the Management Reports \[SRO-CHIEF REPORTS\] menu:
- Admitted w/in 14 days of Out Surgery If Postop Occ \[SROQADM\]
- Report of Missing Quarterly Report Data \[SROQ MISSING DATA\] (renamed Key Missing Surgical Package Data)
- Deaths Within 30 Days of Surgery \[SROQD\]
- The Ensuring Correct Surgery Compliance Report \[SRO ECS COMPLIANCE\] option was placed out of order.

### Menu Options Placed Out of Order, Relocated and/or Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                     | Description of Change                                           |
|---------------------------------------------------------------------|---------------------------------------------------------------------|
| *Quarterly Report Menu* \[SROQ MENU\]                               | Placed Out of Order                                                 |
| *Ensuring Correct Surgery Compliance Report* \[SRO ECS COMPLIANCE\] | Placed Out of Order                                                 |
| *Quarterly Report - Surgical Service* \[SRO QUARTERLY REPORT\]      | Placed Out of Order                                                 |
| *Deaths Within 30 Days of Surgery* \[SROQD\]                        | Relocated to *Management Reports* \[SRO-CHIEF REPORTS\]             |
| *Admitted w/in 14 days of Out Surgery If Postop Occ* \[SROQADM\]    | Relocated to *Management Reports* \[SRO-CHIEF REPORTS\]             |
| *List of Invasive Diagnostic Procedures* \[SROQIDP\]                | Placed Out of Order                                                 |
| *List of Operations Included on Quarterly Report* \[SROQ LIST OPS\] | Placed Out of Order                                                 |
| *Key Missing Surgical Package Data* \[SROQ MISSING DATA\]           | Renamed and Relocated to *Management Reports* \[SRO-CHIEF REPORTS\] |
| *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\]              | Functionality Update                                                |

## Remove/Replace References to “NSQIP” and “CICSP”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

References to “NSQIP” and “CICSP” in field labels and field definitions were replaced with “VASQIP” or with other terms, such as, non-cardiac or cardiac.

### Field Description Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number     | Description of Change |
|-------------------------------|---------------------------|
| IN/OUT-PATIENT STATUS (#.011) | Field Description Update  |
| MAJOR/MINOR (#.03)            | Field Description Update  |
| CASE SCHEDULE TYPE (#.035)    | Field Description Update  |
| SURGERY SPECIALTY (#.04)      | Field Description Update  |
| TIME PAT IN OR (#.205)        | Field Description Update  |

| Field Name and Number                                       | Description of Change |
|-----------------------------------------------------------------|---------------------------|
| ANES CARE START TIME (#.21)                                     | Field Description Update  |
| TIME OPERATION BEGAN (#.22)                                     | Field Description Update  |
| TIME OPERATION ENDS (#.23)                                      | Field Description Update  |
| TIME PAT OUT OR (#.232)                                         | Field Description Update  |
| ANES CARE END TIME (#.24)                                       | Field Description Update  |
| TRAUMA (#12 in ANESTHESIA TECHNIQUE multiple field \#.37)       | Field Description Update  |
| WOUND CLASSIFICATION (#1.09)                                    | Field Description Update  |
| SEPSIS CATEGORY (#7 in POSTOP OCCURRENCE multiple field \#1.16) | Field Description Update  |
| CPB STATUS (#8 in POSTOP OCCURRENCE multiple field \#1.16)      | Field Description Update  |
| PAC(U) DISCH TIME (#1.18)                                       | Field Description Update  |
| PRINCIPAL PROCEDURE (#26)                                       | Field Description Update  |
| CONCURRENT CASE (#35)                                           | Field Description Update  |
| CURRENT SMOKER (#202)                                           | Field Description Update  |
| PACK/YEARS (#202.1)                                             | Field Description Update  |
| HISTORY OF COPD (#203)                                          | Field Description Update  |
| VENTILATOR DEPENDENT (#204)                                     | Field Description Update  |
| CONGESTIVE HEART FAILURE (#207)                                 | Field Description Update  |
| HYPERTENSION REQUIRING MEDS (#208)                              | Field Description Update  |
| CARDIOMEGALY (#209)                                             | Field Description Update  |
| CURRENTLY ON DIALYSIS (#211)                                    | Field Description Update  |
| ESOPHAGEAL VARICES (#213)                                       | Field Description Update  |
| PGY OF PRIMARY SURGEON (#214)                                   | Field Description Update  |
| WEIGHT LOSS \> 10% (#215)                                       | Field Description Update  |
| TRANSFUSION \> 4 RBC UNITS (#217)                               | Field Description Update  |
| OPEN WOUND (#218)                                               | Field Description Update  |
| PREOPERATIVE SEPSIS (#218.1)                                    | Field Description Update  |
| PREOPERATIVE HEMOGLOBIN (#219)                                  | Field Description Update  |
| PREVIOUS PCI (#220)                                             | Field Description Update  |
| PREOPERATIVE SERUM CREATININE (#223)                            | Field Description Update  |
| PREOPERATIVE SERUM ALBUMIN (#225)                               | Field Description Update  |
| DNR STATUS (#238)                                               | Field Description Update  |
| ETOH \> 2 DRINKS/DAY (#246)                                     | Field Description Update  |
| LENGTH OF POST-OP STAY (#247)                                   | Field Description Update  |
| SUPERFICIAL INCISIONAL SSI (#248)                               | Field Description Update  |
| DEEP INCISIONAL SSI (#249)                                      | Field Description Update  |
| SYSTEMIC SEPSIS (#250)                                          | Field Description Update  |
| PNEUMONIA (#251)                                                | Field Description Update  |
| PULMONARY EMBOLISM (#252)                                       | Field Description Update  |
| OTHER RESPIRATORY OCCURRENCE (#253)                             | Field Description Update  |
| ACUTE RENAL FAILURE (#254)                                      | Field Description Update  |
| URINARY TRACT INFECTION (#255)                                  | Field Description Update  |
| STROKE/CVA (#256)                                               | Field Description Update  |
| POSTOP BLEEDING/TRANSFUSIONS (#257)                             | Field Description Update  |
| MYOCARDIAL INFARCTION (#258)                                    | Field Description Update  |

| Field Name and Number             | Description of Change |
|---------------------------------------|---------------------------|
| GRAFT/PROSTHESIS/FLAP FAILURE (#261)  | Field Description Update  |
| RETURN TO OR WITHIN 30 DAYS (#262)    | Field Description Update  |
| PREVIOUS CARDIAC SURGERY (#266)       | Field Description Update  |
| PREGNANCY (#269)                      | Field Description Update  |
| ON VENTILATOR \>48 HOURS (#285)       | Field Description Update  |
| OTHER URINARY TRACT OCCURRENCE (#286) | Field Description Update  |
| PERIPHERAL NERVE INJURY (#287)        | Field Description Update  |
| DYSPNEA (#325)                        | Field Description Update  |
| CURRENT PNEUMONIA (#326)              | Field Description Update  |
| RENAL FAILURE (#328)                  | Field Description Update  |
| REVASCULARIZATION/AMPUTATION (#329)   | Field Description Update  |
| REST PAIN/GANGRENE (Y/N) (#330)       | Field Description Update  |
| IMPAIRED SENSORIUM (#332)             | Field Description Update  |
| COMA (#333)                           | Field Description Update  |
| HISTORY OF TIA'S (#334)               | Field Description Update  |
| CVA/STROKE WITH NEURO DEFICIT (#335)  | Field Description Update  |
| CVA/STROKE - NO NEURO DEFICIT (#336)  | Field Description Update  |
| CHEMOTHERAPY IN LAST 30 DAYS (#338.1) | Field Description Update  |
| RADIOTHERAPY IN LAST 90 DAYS (#338.2) | Field Description Update  |
| STEROID USE FOR CHRONIC COND. (#339)  | Field Description Update  |
| INTRAOP RBC UNITS TRANSFUSED (#340)   | Field Description Update  |
| OTHER CNS OCCURRENCE (#343)           | Field Description Update  |
| OTHER CARDIAC OCCURRENCE (#344)       | Field Description Update  |
| DIABETES (#346)                       | Field Description Update  |
| PULMONARY RALES (#348)                | Field Description Update  |
| ACTIVE ENDOCARDITIS (#349)            | Field Description Update  |
| PCI (#351)                            | Field Description Update  |
| NUM OF PRIOR HEART SURGERIES (#352)   | Field Description Update  |
| LVEDP (#357)                          | Field Description Update  |
| AORTIC SYSTOLIC PRESSURE (#358)       | Field Description Update  |
| PA SYSTOLIC PRESSURE (#359)           | Field Description Update  |
| PAW MEAN PRESSURE (#360)              | Field Description Update  |
| LEFT MAIN STENOSIS (#361)             | Field Description Update  |
| LAD STENOSIS (#362.1)                 | Field Description Update  |
| RIGHT CORONARY STENOSIS (#362.2)      | Field Description Update  |
| CIRCUMFLEX STENOSIS (#362.3)          | Field Description Update  |
| LV CONTRACTION SCORE (#363)           | Field Description Update  |
| ESTIMATE OF MORTALITY (#364)          | Field Description Update  |
| VALVE REPAIR (#370)                   | Field Description Update  |
| GREAT VESSEL REPAIR (Y/N) (#372)      | Field Description Update  |
| CARDIAC TRANSPLANT (#373)             | Field Description Update  |
| OTHER TUMOR RESECTION (#379)          | Field Description Update  |
| OTHER CARDIAC PROCEDURES (#383.1)     | Field Description Update  |

| Field Name and Number               | Description of Change |
|-----------------------------------------|---------------------------|
| OPERATIVE DEATH (#384)                  | Field Description Update  |
| PERIOPERATIVE MI (#385)                 | Field Description Update  |
| ENDOCARDITIS (#386)                     | Field Description Update  |
| MEDIASTINITIS (#388)                    | Field Description Update  |
| REOPERATION FOR BLEEDING (#389)         | Field Description Update  |
| STROKE (#390)                           | Field Description Update  |
| REPEAT CARDIAC SURG PROCEDURE (#391)    | Field Description Update  |
| OTHER OCCURRENCES (ICD9) (#392)         | Field Description Update  |
| HISTORY OF MI (#394)                    | Field Description Update  |
| ANGINA ONE MONTH PRIOR (#395)           | Field Description Update  |
| CHF WITHIN ONE MONTH (#396)             | Field Description Update  |
| QUADRIPLEGIA (Y/N) (#398)               | Field Description Update  |
| PARAPLEGIA (Y/N) (#399)                 | Field Description Update  |
| HEMIPLEGIA/HEMIPARESIS (Y/N) (#400)     | Field Description Update  |
| TUMOR INVOLVING CNS (Y/N) (#401)        | Field Description Update  |
| WOUND DISRUPTION (#404)                 | Field Description Update  |
| RENAL INSUFFICIENCY (#409)              | Field Description Update  |
| COMA \> 24 HOURS POSTOP (#410)          | Field Description Update  |
| CARDIAC ARREST REQ CPR (#411)           | Field Description Update  |
| UNPLANNED INTUBATION (Y/N) (#412)       | Field Description Update  |
| TRANSFER STATUS (#413)                  | Field Description Update  |
| MITRAL REGURGITATION (#415)             | Field Description Update  |
| NUMBER WITH OTHER CONDUIT (#416)        | Field Description Update  |
| HOSPITAL ADMISSION DATE (#418)          | Field Description Update  |
| HOSPITAL DISCHARGE DATE (#419)          | Field Description Update  |
| ADMISSION/TRANSFER DATE (#420)          | Field Description Update  |
| DISCHARGE/TRANSFER DATE (#421)          | Field Description Update  |
| CARDIAC RISK PREOP COMMENTS (#430)      | Field Description Update  |
| CARDIAC RESOURCE DATA COMMENTS (#431)   | Field Description Update  |
| CLOSTRIDIUM DIFFICILE COLITIS (#447)    | Field Description Update  |
| OBSERVATION ADMISSION DATE (#452)       | Field Description Update  |
| OBSERVATION DISCHARGE DATE (#453)       | Field Description Update  |
| OBSERVATION TREATING SPECIALTY (#454)   | Field Description Update  |
| HDL (CARDIAC) (#457)                    | Field Description Update  |
| HDL, DATE (#457.1)                      | Field Description Update  |
| SERUM TRIGLYCERIDE (CARDIAC) (#458)     | Field Description Update  |
| SERUM TRIGLYCERIDE, DATE (CAR) (#458.1) | Field Description Update  |
| SERUM POTASSIUM (CARDIAC) (#459)        | Field Description Update  |
| SERUM POTASSIUM, DATE(CARDIAC) (#459.1) | Field Description Update  |
| SERUM BILIRUBIN (CARDIAC) (#460)        | Field Description Update  |
| SERUM BILIRUBIN, DATE (CARD) (#460.1)   | Field Description Update  |
| LDL (CARDIAC) (#461)                    | Field Description Update  |
| LDL, DATE (CARDIAC) (#461.1)            | Field Description Update  |

| Field Name and Number             | Description of Change |
|---------------------------------------|---------------------------|
| TOTAL CHOLESTEROL (CARDIAC) (#462)    | Field Description Update  |
| TOTAL CHOLESTEROL, DATE (#462.1)      | Field Description Update  |
| HYPERTENSION (#463)                   | Field Description Update  |
| TRACHEOSTOMY (#466)                   | Field Description Update  |
| NEW MECHANICAL CIRCULATORY (#467)     | Field Description Update  |
| CONVERT FROM OFF PUMP TO CPB (#469)   | Field Description Update  |
| D/T PATIENT EXTUBATED (#470)          | Field Description Update  |
| CARDIAC SURG PERFORMED NON-VA (#472)  | Field Description Update  |
| HOMELESS (#473)                       | Field Description Update  |
| DIABETES (CARDIAC) (#475)             | Field Description Update  |
| PROCEDURE TYPE (#476)                 | Field Description Update  |
| AORTIC STENOSIS (#477)                | Field Description Update  |
| RE-DO LAD STENOSIS (#478)             | Field Description Update  |
| RE-DO RT CORONARY STENOSIS (#479)     | Field Description Update  |
| RE-DO CIRCUMFLEX STENOSIS (#480)      | Field Description Update  |
| BRIDGE TO TRANSPLANT/DEVICE (#481)    | Field Description Update  |
| \*MAZE PROCEDURE (#482)               | Field Description Update  |
| TMR (#483)                            | Field Description Update  |
| OTHER CARDIAC PROCEDURES-LIST (#484)  | Field Description Update  |
| PRIOR HEART SURGERIES (#485)          | Field Description Update  |
| ORGAN/SPACE SSI (#488)                | Field Description Update  |
| OTHER WOUND OCCURRENCE (#489)         | Field Description Update  |
| REPEAT VENTILATOR W/IN 30 DAYS (#490) | Field Description Update  |
| OTHER NON-CT PROCEDURES (#491)        | Field Description Update  |
| PREOP FUNCT. HEALTH STATUS (#492)     | Field Description Update  |
| OTHER CARDIAC PROCEDURES (Y/N) (#502) | Field Description Update  |
| HEMOGLOBIN A1C (#504)                 | Field Description Update  |
| HEMOGLOBIN A1C, DATE (#504.1)         | Field Description Update  |
| ENDOVASCULAR REPAIR (#505)            | Field Description Update  |
| CURRENT SMOKER (CARDIAC) (#510)       | Field Description Update  |
| MAZE PROCEDURE (#512)                 | Field Description Update  |
| PRIMARY CAUSE FOR DELAY (#515)        | Field Description Update  |
| MALLAMPATI SCALE (#901.1)             | Field Description Update  |

### Field Updates – SURGERY SITE PARAMETERS File (#133)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields were modified to replace references to “NSQIP” with “VASQIP”.

| Field Name and Number            | Description of Change |
|--------------------------------------|---------------------------|
| LATEST CASE WORKLOAD REPORT (#16)    | Field Description Update  |
| VASQIP 30 DAY FOLLOW-UP LETTER (#31) | Field Description Update  |

### Data Update – PERIOPERATIVE OCCURRENCE CATEGORY File (#136.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard occurrence category definitions stored in the DESCRIPTION field (#2) were updated to replace references to “NSQIP” and to “CICSP”.

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| DESCRIPTION (#2)          | Data Update               |

### File and Field Update – CPT EXCLUSIONS File (#137)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The text of the file description was modified to replace “NSQIP” with “VASQIP” and the following field was modified to replace a reference to “NSQIP” with “VASQIP”.

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| CPT CODE (#.01)           | Field Description Update  |

### Field Updates – RISK MODEL LAB TEST File (#139.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following field names were modified to replace references to “CICSP” with “VASQIP”.

| Field Name and Number  | Description of Change |
|----------------------------|---------------------------|
| VASQIP REFERENCE LOW (#3)  | Name Update               |
| VASQIP REFERENCE HIGH (#4) | Name Update               |

### Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields were modified to replace/remove references to “NSQIP” and to “CICSP”.

| Field Name and Number             | Description of Change |
|---------------------------------------|---------------------------|
| ON VENTILATOR \>48 HOURS (#118)       | Field Description Update  |
| CARDIAC ARREST REQ CPR (#119)         | Field Description Update  |
| COMA \> 24 HOURS POSTOP (#122)        | Field Description Update  |
| SUPERFICIAL INCISIONAL SSI (#123)     | Field Description Update  |
| DEEP INCISIONAL SSI (#124)            | Field Description Update  |
| SYSTEMIC SEPSIS (#125)                | Field Description Update  |
| NEW MECHANICAL CIRCULATORY (#130)     | Field Description Update  |
| PREOP FUNCTIONAL HEALTH STATUS (#131) | Field Description Update  |
| REOPERATION FOR BLEEDING (#148)       | Field Description Update  |
| RENAL FAILURE REQ. DIALYSIS (#191)    | Field Description Update  |
| PERIOPERATIVE MI (#192)               | Field Description Update  |

### Options Updated to Remove/Replace References to “NSQIP” and “CICSP”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                          | Description of Change |
|--------------------------------------------------------------------------|---------------------------|
| *Monthly Surgical Case Workload Report* \[SROA MONTHLY WORKLOAD REPORT\] | Description Update        |
| *Queue Assessment Transmissions* \[SROA TRANSMIT ASSESSMENTS\]           | Description Update        |
| *Risk Model Lab Test (Enter/Edit)* \[SROA LAB TEST EDIT\]                | Description Update        |
| *Update 1-Liner Case* \[SROA ONE-LINER UPDATE\]                          | Description Update        |

## Addition of Scheduling Date Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New date fields were added with the intent of capturing the date the request for surgery is first scheduled, the desired date of surgery and, if the request date is changed, the subsequent changed date. These dates will be transmitted as part of the non-cardiac assessment transmission for non-cardiac assessed cases or as part of the 1-liner transmission for all other cases.

### New Scheduling Date Fields – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number            | Description of Change |
|--------------------------------------|---------------------------|
| ORIGINAL DESIRED DATE (#612)         | New field                 |
| D/T OF DESIRED PROCEDURE DATE (#613) | New field                 |
| ORIGINAL SCHEDULED DATE (#614)       | New field                 |
| D/T OF SCHEDULED DATE ENTRY (#615)   | New field                 |
| DESIRED PROCEDURE DATE (#616)        | New field                 |
| SCHEDULED DATE (#617)                | New field                 |

### Menu Options Changed to Capture Scheduling Date Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                          | Description of Change |
|----------------------------------------------------------|---------------------------|
| *Make Operation Requests* \[SROOPREQ\]                   | Functionality Update      |
| *Delete or Update Operation Requests* \[SRSUPRQ\]        | Functionality Update      |
| *Make a Request from the Waiting List* \[SRSWREQ\]       | Functionality Update      |
| *Make a Request for Concurrent Cases* \[SRSREQCC\]       | Functionality Update      |
| *Schedule Requested Operations* \[SRSCHD1\]              | Functionality Update      |
| *Schedule Unrequested Operations* \[SROSRES\]            | Functionality Update      |
| *Schedule Unrequested Concurrent Cases* \[SRSCHDC\]      | Functionality Update      |
| *Reschedule or Update a Scheduled Operation* \[SRSCHUP\] | Functionality Update      |
| *Operation Menu* \[SROPER\]                              | Functionality Update      |

## Time Out Verified Utilizing Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The time out verified functionality was replaced with the updated “Time Out Verified Utilizing Checklist” functionality. The checklist includes the following required items which will be transmitted as part of the non-cardiac assessment transmission for non-cardiac assessed cases or as part of the 1-liner transmission for all other cases.

### Time Out Verified Checklist Fields – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number            | Description of Change               |
|--------------------------------------|-----------------------------------------|
| CONFIRM PATIENT IDENTITY (#600)      | New field                               |
| PROCEDURE TO BE PERFORMED (#601)     | New field                               |
| SITE OF PROCEDURE (#602)             | New field                               |
| VALID CONSENT FORM (#603)            | New field                               |
| CONFIRM PATIENT POSITION (#604)      | New field                               |
| MARKED SITE CONFIRMED (#605)         | New field                               |
| PREOPERATIVE IMAGES CONFIRMED (#606) | New field                               |
| CORRECT MEDICAL IMPLANTS (#607)      | New field                               |
| ANTIBIOTIC PROPHYLAXIS (#608)        | New field                               |
| APPROPRIATE DVT PROPHYLAXIS (#609)   | New field                               |
| BLOOD AVAILABILITY (#610)            | New field                               |
| AVAILABILITY OF SPECIAL EQUIP (#611) | New field                               |
| CHECKLIST COMMENT (#85)              | New field                               |
| CHECKLIST CONFIRMED BY (#.69)        | Label, Title & Field Description Update |

A new option, *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\], was added to the Operation Menu \[SROPER\] to be used to enter checklist information. The old ensuring correct surgery fields were removed from the *Operation Menu* \[SROPER\] input options.

### Menu Options Updated or Added for Time Out Verified Utilizing Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                         | Description of Change                      |
|---------------------------------------------------------|------------------------------------------------|
| *Operation Menu* \[SROPER\]                             | Menu Items Update                              |
| *Operation Startup* \[SROMEN-START\]                    | Description Update                             |
| *Operation* \[SROMEN-OP\]                               | Input Template Update                          |
| *Operation (Short Screen)* \[SROMEN-OUT\]               | Input Template Update                          |
| *Nurse Intraoperative Report* \[SRONRPT\]               | Input Template Update and Functionality Update |
| *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\] | New Option                                     |

## Standard SURGERY CANCELLATION REASON File (#135)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Existing entries in the SURGERY CANCELLATION REASON file (#135) were made inactive so that they can no longer be selected when entering a cancellation reason. A standard set of cancellation reasons was added to the file and will be the only reasons that may be selected when cancelling a surgical case. The file was locked and no longer may be edited locally. The CANCEL REASON field (#18) description was updated to further describe the standard list. The cancellation reason was added to the list of transmitted data items transmitted to Denver.

This is the standard list of cancellation reasons:

1 - PATIENT ACTION (NO SHOW, ETC)

2 - CHANGE IN TREATMENT, PT HEALTH

3 - NO CONSENT

4 - NO LIP (SURG, ANESTH, ETC)

5 - NO PERIOP NURSING (OR, PACU)

6 - NO BED AVAILABLE

7 - NO EQUIPMENT, NOT RME, (C-ARM)

8 - NO RME (SPD, IMPLANT, DEFECT)

9 - OTHER

> **NOTE:** If “Other” is selected, the user will be prompted to enter a Comment.

### Cancellation Comments Field – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number   | Description of Change                  |
|-----------------------------|--------------------------------------------|
| CANCEL REASON (#18)         | Field Description and Functionality Update |
| CANCELLATION COMMENTS (#19) | New Field                                  |

### Standard Cancellation Reasons – Modified Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                      | Description of Change |
|------------------------------------------------------|---------------------------|
| *Update Site Configurable Files* \[SR UPDATE FILES\] | Functionality Update      |

## Miscellaneous Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Report of Non-O.R. Procedures \[SRONOR\] was updated to display the principal anesthetist and anesthesiologist supervisor for each case.
- The Surgery application was updated to display a value of less than 1 for the fields listed below with a leading zero when they are displayed in the Anesthesia Report and the Nurse Intraoperative Report.
- The Wound Classification Report \[SROWC\] was modified to include ORGAN/SPACE SSI in the algorithm for calculating the Clean Wound Infection Rate. For cardiac assessed cases, ENDOCARDITIS and MEDIASTINITIS will be included in the algorithm.
- The Morbidity & Mortality Reports \[SROMM\] option was modified to allow the Perioperative Occurrences Report to be printed for one of the following choices:

1\. Intraoperative Occurrences

2\. Postoperative Occurrences

3\. Intraoperative and Postoperative Occurrences

### Display Leading Zero – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number                                                                         | Description of Change |
|---------------------------------------------------------------------------------------------------|---------------------------|
| DOSE (#1) in ANESTHESIA AGENTS multiple field (#24) in ANESTHESIA TECHNIQUE multiple field (#.37) | Input Transform Update    |
| DOSE (#1) in TEST DOSE multiple field (#32) in ANESTHESIA TECHNIQUE multiple field (#.37)         | Input Transform Update    |
| DOSE (#1) in TIME ADM multiple field (#1) in MEDICATIONS multiple field (#.375)                   | Input Transform Update    |

### Miscellaneous Changes - Menu Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                            | Description of Change |
|--------------------------------------------|---------------------------|
| *Report of Non-O.R. Procedures* \[SRONOR\] | Functionality Update      |
| *Wound Classification Report* \[SROWC\]    | Functionality Update      |
| *Morbidity & Mortality Reports* \[SROMM\]  | Functionality Update      |

*(This page included for two-sided copying.)*

# Surgery Risk Assessment Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application for the Annual Surgery Updates – VASQIP 2011 Increment 1project related to the Surgery Risk Assessment Module.

- A new field called 30 DAY DEATH was added to the Patient Demographics (Enter/Edit) \[SROA DEMOGRAPHICS\] option. This YES/NO field indicates death occurred within 30 days of surgery and is populated automatically when the Date of Death is entered. This field is not transmitted.
- The set of codes for the PREOPERATIVE SLEEP APNEA field (#237.1) was updated to allow for an entry of “N” for “NONE”.
- The printed non-cardiac assessment was modified to include the ASSESSMENT COMPLETED BY field (#272.1).
- The “AT” cross reference in SURGERY file (#130) was updated to correct dates stored with trailing zeros.
- The help text for the D/T PATIENT EXTUBATED field (#470) was updated, replacing the word “final” with the word “first”.
- The name of the MYECTOMY FOR IHSS field (#378) was changed to “MYECTOMY”. The field title and definition were updated also.
- The set of codes and help text for the BRIDGE TO TRANSPLANT/DEVICE field (#481) were changed. The set of codes was changed from YES/NO to the following:

> N NONE

> B BRIDGE TO TRANSPLANT

> D DESTINATION THERAPY

- The WOUND CLASSIFICATION field (#1.09) was added to the Operative Risk Summary Data (Enter/Edit) \[SROA CARDIAC OPERATIVE RISK\] option, to the printed cardiac risk assessment and to the cardiac risk assessment transmission.
- The WOUND DISRUPTION field (#404) was added to the Outcome Information (Enter/Edit) \[SROA CARDIAC-OUTCOMES\] option, to the printed cardiac risk assessment and to the cardiac risk assessment transmission.
- The Clinical Information (Enter/Edit) \[SROA CLINICAL INFORMATION\] option was updated to allow a response of “N” or “NO” to update all the fields, where applicable, to a negative value.
- The CPT EXCLUSIONS file (#137) was updated with the excluded CPT codes for FY11. This file is used internally by the software to identify surgical cases eligible for assessment.

### Risk Assessment Field Updates – SURGERY File (#130)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number          | Description of Change                            |
|------------------------------------|------------------------------------------------------|
| 30 DAY DEATH (#342.1)              | New Field                                            |
| PREOPERATIVE SLEEP APNEA (#237.1)  | Set of Codes & Field Description Update              |
| D/T PATIENT EXTUBATED (#470)       | Help Text Update                                     |
| MYECTOMY (#378)                    | Label, Title, Help Text and Field Description Update |
| BRIDGE TO TRANSPLANT/DEVICE (#481) | Set of Codes & Help Text Update                      |

### Data Update – CPT EXCLUSIONS File (#137)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| CPT CODE (#.01)           | Data Update               |

### Risk Assessment Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options /reports have been added, modified or put out of order.

| Option Name                                                              | Description of Change |
|------------------------------------------------------------------------------|---------------------------|
| *Patient Demographics (Enter/Edit)* \[SROA DEMOGRAPHICS\]                    | Functionality Update      |
| *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]                  | Functionality Update      |
| *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] | Functionality Update      |
| *Operative Risk Summary Data (Enter/Edit)* \[SROA CARDIAC OPERATIVE RISK\]   | Functionality Update      |
| *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\]                 | Functionality Update      |
| *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]            | Functionality Update      |

# Surgery Transplant Assessment Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application for the Annual Surgery Updates – VASQIP 2011 Increment 1project related to the Surgery Transplant Assessment Module.

### - HLA typing fields in the SURGERY TRANSPLANT ASSESSMENTS file (#139.5) across all four organ types were updated to allow entry of 4 digits. The transplant transmissions were updated to allow the longer data items to be transmitted.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The C-PEPTIDE AT TIME OF LISTING field (#136) was updated to allow a value less than 1 to be entered and appropriately displayed. The field description was updated accordingly.
- The POST-TX PROPHYLAXIS field (#92) was updated to allow the entry of “N/A”.

COLD ISCHEMIA TIME FOR ORGAN field (#87) and WARM ISCHEMIA TIME FOR ORGAN (#85) were added to the Enter/Edit Transplant Assessments \[SR TRANSPLANT ENTER/EDIT\] option for heart transplant information entry. The Print Transplant Assessment \[SRTP PRINT ASSESSMENT\] option was updated to display these fields for heart transplants.

### ### Field Updates – SURGERY TRANSPLANT ASSESSMENTS File (#139.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name and Number           | Description of Change                  |
|-------------------------------------|--------------------------------------------|
| RECIPIENT HLA-A TYPING (#13)        | Field Description Update                   |
| RECIPIENT HLA-B TYPING (#14)        | Field Description Update                   |
| RECIPIENT HLA-C TYPING (#15)        | Field Description Update                   |
| RECIPIENT HLA-BW TYPING (#16)       | Field Description Update                   |
| RECIPIENT HLA-DR TYPING (#17)       | Field Description Update                   |
| RECIPIENT HLA-DQ TYPING (#18)       | Field Description Update                   |
| DONOR HLA-A TYPING (#64)            | Field Description Update                   |
| DONOR HLA-B TYPING (#65)            | Field Description Update                   |
| DONOR HLA-C TYPING (#66)            | Field Description Update                   |
| DONOR HLA-BW TYPING (#67)           | Field Description Update                   |
| DONOR HLA-DQ TYPING (#72)           | Field Description Update                   |
| DONOR HLA-DR TYPING (#73)           | Field Description Update                   |
| C-PEPTIDE AT TIME OF LISTING (#136) | Input Transform & Field Description Update |
| POST-TX PROPHYLAXIS – TB (#92)      | Set of Codes & Field Description Update    |

### Transplant Assessment Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                                  | Description of Change |
|------------------------------------------------------------------|---------------------------|
| *Enter/Edit Transplant Assessments* \[SR TRANSPLANT ENTER/EDIT\] | Functionality Update      |
| *Print Transplant Assessment* \[SRTP PRINT ASSESSMENT\]          | Functionality Update      |

*(This page included for two-sided copying.)*