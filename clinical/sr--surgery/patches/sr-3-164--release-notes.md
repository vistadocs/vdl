---
title: SR*3*164 Surgery CICSP - CT Surgery Consult Date 2007 Release
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery CICSP - CT Surgery Consult Date 2007 Release
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*164
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
  - assessment
  - consult
  - date
  - update
  - transmission
  - resource
  - print
page_count: 0
word_count: 294
section_count: 5
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p164_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p164_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

> ![](sr-3-164-surgery-cicsp-ct-surgery-consult-date-2007-release/001.png)

CICSP - CT SURGERY CONSULT DATE

> RELEASE NOTES

> SR\*3\*164

> Version 3.0

> November 2007

> Department of Veterans Affairs Veterans Health Information Technology
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Project Enhancements](#project-enhancements)
- [CICSP – CT Surgery Consult Date Enhancements](#cicsp-ct-surgery-consult-date-enhancements)
- [Option and Transmission Updates](#option-and-transmission-updates)
  - [Resource Data (Enter/Edit) Option](#resource-data-enteredit-option)
  - [Print a Surgery Risk Assessment Option](#print-a-surgery-risk-assessment-option)
  - [Update Assessment Status to 'COMPLETE' Option](#update-assessment-status-to-complete-option)
  - [Cardiac Transmission Updates](#cardiac-transmission-updates)
> This project enhances the Cardiac Risk Assessment module of the VistA Surgery application. The purpose of the Cardiac Risk Assessment module is to facilitate data entry of both preoperative and postoperative patient information pertaining to surgical risk assessments, and to transmit the data to a national database.
> A new field is being added to the Cardiac Risk Assessment module in support of the Continuous Improvement in Cardiac Surgery Program (CICSP).This new field, SURGERY CONSULT DATE (#513) in the SURGERY file (#130), will be used to document the date that the patient was notified that Surgery was needed. This new field will identify the start of the wait time.

# Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software provides the following enhancements:

- Add a new field titled SURGERY CONSULT DATE (#513) in the SURGERY file (#130).
- Update the *Resource Data (Enter/Edit)* \[SROA CARDIAC RESOURCE\] option to include the new SURGERY CONSULT DATE field (#513).
- Update the *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option to display the SURGERY CONSULT DATE when printing a cardiac assessment.
- Update the *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\] option to include the new field SURGERY CONSULT DATE to the list of missing items feature.
- Update the Cardiac Transmission to include the new field SURGERY CONSULT DATE.

> *(This page included for two-sided copying.)*

# CICSP – CT Surgery Consult Date Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the changes made to the VistA Surgery application for the CICSP – CT Surgery Consult Date enhancements.

# Option and Transmission Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These options are updated as part of the CICSP – CT Surgery Consult Date enhancements project.

- *Resource Data (Enter/Edit)* \[SROA CARDIAC RESOURCE\] option
- *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option
- *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\] option

## Resource Data (Enter/Edit) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new SURGERY CONSULT DATE field (#513) in the SURGERY file (#130) is added as item \#12 on the display of the *Resource Data (Enter/Edit)* \[SROA CARDIAC RESOURCE\] option.

> Example: Resource Data (Enter/Edit)

| SURPATIENT,TEN (000-12-3456) Case \#49413                        |     |
|------------------------------------------------------------------|-----|
| NOV 18,2007 CABG X3 USING LSVG TO OMB,LV EXT. OF RCA,LIMA TO LAD |     |
| 1\. Hospital Admission Date: NOV 16, 2007@08:00                  |     |
| 2\. Hospital Discharge Date: NOV 30, 2007@08:00                  |     |
| 3\. Cardiac Catheterization Date: NOV 17, 2007                   |     |
| 4\. Time Patient In OR: NOV 18, 2007@07:30                       |     |
| 5\. Time Patient Out OR: NOV 18, 2007@08:30                      |     |
| 6\. Date/Time Patient Extubated: NOV 18, 2007@15:05              |     |
| 7\. Date/Time Discharged from ICU:                               |     |
| 8\. Homeless: NO                                                 |     |
| 9\. Surg Performed at Non-VA Facility: NO                        |     |
| 10\. Resource Data Comments:                                     |     |
| 11\. Employment Status Preoperatively: SELF EMPLOYED             |     |
| 12\. CT Surgery Consult Date:                                    |     |
| Select number of item to edit: 12                            |     |

> Example: Resource Data (Enter/Edit) (continued)

| SURPATIENT,TEN (000-12-3456) Case \#49413                        |     |
|------------------------------------------------------------------|-----|
| NOV 18,2007 CABG X3 USING LSVG TO OMB,LV EXT. OF RCA,LIMA TO LAD |     |
| 1\. Hospital Admission Date: NOV 16, 2007@08:00                  |     |
| 2\. Hospital Discharge Date: NOV 30, 2007@08:00                  |     |
| 3\. Cardiac Catheterization Date: NOV 17, 2007                   |     |
| 4\. Time Patient In OR: NOV 18, 2007@07:30                       |     |
| 5\. Time Patient Out OR: NOV 18, 2007@14:30                      |     |
| 6\. Date/Time Patient Extubated: NOV 18, 2007@08:05              |     |
| 7\. Date/Time Discharged from ICU:                               |     |
| 8\. Homeless: NO                                                 |     |
| 9\. Surg Performed at Non-VA Facility: NO                        |     |
| 10\. Resource Data Comments:                                     |     |
| 11\. Employment Status Preoperatively: SELF EMPLOYED             |     |
| 12\. CT Surgery Consult Date: NOV 12, 2007                       |     |
| Select number of item to edit:                                   |     |

## Print a Surgery Risk Assessment Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option is updated to display the SURGERY CONSULT DATE when printing a cardiac assessment. The information will be displayed in section VIII of the report directly below the existing field “Cardiac Surg Performed at Non VA Facility:”

> Example:

## Update Assessment Status to 'COMPLETE' Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is updated to display the prompt “CT Surgery Consult Date” if the item is determined to be missing from the assessment. This field is displayed as missing only for cases with an Operation Date after September 30, 2007.

## Cardiac Transmission Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data transmission to the CICSP database now includes the new SURGERY CONSULT DATE field (#513) in the SURGERY file (#130).

> *(This page included for two-sided copying.)*