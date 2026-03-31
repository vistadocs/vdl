---
title: OR*3*406 ICD-10 PTF Modifications Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10 PTF Modifications
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*406
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - patch
  - associated
  - codes
  - health
  - summary
  - reports
  - fields
  - templates
page_count: 0
word_count: 1903
section_count: 18
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_406_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_406_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  ICD-10 PTF Modifications

  CPRS: Order Entry/Results Reporting (OE/RR)

  OR\*3.0\*406

  Release Notes
---

![](or-3-406-icd-10-ptf-modifications-release-notes/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

| Date           | Version | Description                                                                         | Author                                    |
|----------------|---------|-------------------------------------------------------------------------------------|-------------------------------------------|
| September 2015 | 1.0     | Baseline document, created for ICD-10 PTF Modifications project patch OR\*3.0\*406. | VA OI&T PD, ICD-10 PTF Modifications Team |

Table of Contents

List of Tables

[Table 1: Acronyms and Definitions [8](#_Toc422840144)](#_Toc422840144)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Software Disclaimer](#software-disclaimer)
  - [Documentation Disclaimer](#documentation-disclaimer)
  - [Required Patches](#required-patches)
  - [Installation Instructions](#installation-instructions)
  - [Updated Documentation](#updated-documentation)
- [Enhancements](#enhancements)
  - [Relationship to Health Summary Patch GMTS\2.7\111](#relationship-to-health-summary-patch-gmts27111)
  - [Update OE/RR Reports](#update-oerr-reports)
  - [Set Default Value for ORWRP TIME/OCC LIMITS INDV Parameter](#set-default-value-for-orwrp-timeocc-limits-indv-parameter)
  - [Local Reports](#local-reports)
- [Fixes and Other Changes](#fixes-and-other-changes)
- [Associated Files and Fields](#associated-files-and-fields)
  - [Modified Fields](#modified-fields)
  - [New Fields](#new-fields)
- [Associated Forms](#associated-forms)
- [Associated Mail Groups](#associated-mail-groups)
- [Associated Options](#associated-options)
- [Associated Protocols](#associated-protocols)
- [Associated Security Keys](#associated-security-keys)
- [Associated Templates](#associated-templates)
  - [Modified Templates](#modified-templates)
  - [New Templates](#new-templates)
- [Integration Control Registrations (ICRs)](#integration-control-registrations-icrs)
  - [Modified ICRs](#modified-icrs)
  - [New ICRs](#new-icrs)
- [New Service Requests](#new-service-requests)
- [Patient Safety Issues](#patient-safety-issues)
- [Remedy Tickets](#remedy-tickets)
- [Known Issues](#known-issues)
Veterans Health Administration (VHA) software remediation for the International Classification of Diseases, Tenth Revision (ICD-10) enabled the transition to support the use of ICD-10 code sets. ICD-10-CM will replace ICD-9-CM as the diagnostic coding system, and ICD-10-PCS will replace ICD-9-CM as the procedural coding system. The Patient Treatment File (PTF) Modifications project will increase the maximum allowable codes in the entry, display, lookup, view, print, storage, and transmission of the ICD-10 code sets in the VistA legacy and Health*<u>e</u>*Vet systems. Effective as of the ICD-10 activation date, VHA will be able to utilize the ICD-10 code sets to include the increased number of diagnosis and procedures which can be recorded in its day-to-day operations (e.g. entry, display, lookup, print, storage, internal and/or external transmission) for inpatient episodes of care with discharges on or after this date.
The ICD-10 PTF Modifications project supports the expansion of the number of ICD-10 Diagnosis, Present on Admission (POA) indicators, and Procedure and Surgical codes that may be contained in a patient treatment record. The user will now be able to enter up to 25 ICD-10 diagnosis codes with their associated POA indicators in each Movement (501) screen and in the Discharge (701) screen of a patient treatment record. The user will also be able to enter up to 25 ICD-10 procedure codes in each Surgical Episode (401) screen and in each Non-OR Procedure (601) screen.
The ICD-10 PTF Modifications project is comprised of six patches, which are being released within a single KIDS host file:
- Admission, Discharge, Transfer (ADT), DG\*5.3\*884;
- CPRS: Health Summary (HS), GMTS\*2.7\*111;
- Integrated Billing (IB), IB\*2.0\*522;
- Laboratory: Anatomic Pathology (AP) and Laboratory: Emerging Pathogens Initiative (EPI), LR\*5.2\*442;
- CPRS: Order Entry/Results Reporting (OE/RR), OR\*3.0\*406;
- and Clinical Case Registries (CCR), ROR\*1.5\*25.
Patch OR\*3.0\*406 updates the following Health Summary Components (#142.1) to include the expanded fields: MAS ADMISSIONS/DISCHARGES, MAS ADT HISTORY EXPANDED, MAS DISCHARGE DIAGNOSIS, MAS PROCEDURES ICD CODES, and MAS SURGERIES ICD CODES. Health Summary Components can be used in several ways within VistA; some locally created items will also be affected by the newly updated display capability included in this patch if those items leverage any of the affected components to generate output. Objects may be of particular interest as the newly expanded display would be more noticeable when an object is embedded in areas such as boilerplate text, note templates, and reminder dialog templates. Patch OR\*3.0\*406 also updates reports that utilize one or more of the aforementioned Health Summary Components and will therefore now display the expanded data fields as appropriate.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Release Notes cover the new features provided to CPRS: Order Entry/Results Reporting (OE/RR) users in patch OR\*3.0\*406.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the CPRS: Order Entry/Results Reporting (OE/RR) product and applies primarily to the changes made between this newest release and previous release packages of the software.

## Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105, of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

## Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before patch OR\*3.0\*406:

- GMTS\*2.7\*101
- DG\*5.3\*884

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation information, refer to the ICD-10 PTF Modifications Installation Guide on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=61>.

## Updated Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS: Order Entry/Results Reporting documents are posted under Computerized Patient Record System (CPRS) on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=61>.

The following CPRS: Order Entry/Results Reporting documents have been updated with changes for OR\*3.0\*406:

- ICD-10 PTF Modifications Installation Guide
- ICD-10 PTF Modifications OERR OR\*3.0\*406 Release Notes

There are no Technical Manual or User Manual updates associated with patch OR\*3.0\*406.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Relationship to Health Summary Patch GMTS\*2.7\*111

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 works in conjunction with the CPRS: Health Summary GMTS\*2.7\*111 patch that is also part of the ICD-10 Modifications project. The Health Summary patch modifies several Health Summary Components (file \#142.1) to now return up to 25 ICD-10 codes when pulling data for a given PTF file entry. The following Health Summary Components are modified by patch GMTS\*2.7\*111:

- MAS ADMISSIONS/DISCHARGES – Updated to display up to 25 diagnosis codes with each occurrence
- MAS ADT HISTORY EXPANDED – Updated to display up to 25 diagnosis codes, up to 25 procedure codes, and up to 25 operation codes
- MAS DISCHARGE DIAGNOSIS – Updated to display up to 25 diagnosis codes with each occurrence
- MAS PROCEDURES ICD CODES – Updated to display up to 25 procedure codes with each occurrence
- MAS SURGERIES ICD CODES – Updated to display up to 25 operation codes with each occurrence

## Update OE/RR Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports in OE/RR REPORT (#101.24) file will now also display up to 25 ICD-10 codes per occurrence:

- ORRPW ADT ADM DC – Adm./Discharge
- ORRPW ADT DC DIAG – Discharge Diagnosis
- ORRPW ADT EXP – Expanded ADT
- ORRPW ADT ICD PROC – ICD Procedures
- ORRPW ADT ICD SURG – ICD Surgeries
- ORRPW DOD ADT EXP – DOD Expanded ADT

## Set Default Value for ORWRP TIME/OCC LIMITS INDV Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 will establish a default value at the PACKAGE level for the ORWRP TIME/OCC LIMITS INDV parameter. This parameter sets the date and time limits for an individual report. The parameter value for the reports listed above shall be: T-7;T;25. This value sets a date range of the previous seven days up to the current date and will return a maximum number of 25 occurrences. Setting the maximum occurrence value to 25 will ensure that all available ICD-10 codes shall be returned. Due to how the parameter ORWRP TIME/OCC LIMITS INDV is defined, a date range must also be set when setting the maximum occurrence value. T-7 and T were chosen as the date range defaults as these are the default values used by the application when no user/system/package values have already been defined.

> **NOTE:** The ORWRP TIME/OCC LIMITS INDV parameter may also be set for a report at the USER and SYSTEM levels. The precedence order for these values is defined as: USER, SYSTEM, PACKAGE. A report will first attempt to use any USER values. If none are defined, then SYSTEM values will be tried, followed by PACKAGE values. End users and support staff should be trained to use an occurrence limit of 25 for these reports when setting any USER or SYSTEM values for this parameter. Any occurrence limit less than 25 may not show the report reader all of the available ICD-10 data. This only applies to the OE/RR reports listed above.

## Local Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has created local (IEN \< 1000) report entries in OE/RR REPORT that use any of the Health Summary Components described in Section 2.1, Relationship to Health Summary Patch GMTS\*2.7\*111, then those reports should also have the ORWRP TIME/OCC LIMITS INDV parameter set with an occurrence limit of 25. If using FileMan to inquire to a given report file entry, the REPORT COMPONENT field will indicate which Health Summary Component(s) a report is using.

<u>Example:</u>

Select OE/RR REPORT NAME: ORRPW ADT ADM DC Adm./Discharge

NUMBER: 1036 NAME: ORRPW ADT ADM DC

ID: OR_ADC REMOTE: YES

QUALIFIER: HSComponent ROUTINE: ORDV01

ENTRY POINT: HSQUERY CATEGORY: LISTVIEW

TAB: REPORTS TAB TYPE: LISTVIEW

RPC: ORWRP REPORT TEXT

-\>REPORT COMPONENT: MAS ADMISSIONS/DISCHARGES \<\<------------------------

HEADING: Adm./Discharge DESCRIPTIVE TEXT: Adm./Discharge

PRINT TAG: HSTYPEB PRINT ROUTINE: ORWRPP1

> Individual users may set the USER level parameter value for any local reports via CPRS GUI.

1.  Select Tools -\> Options -\> Reports Tab -\> Set Individual Reports.
2.  Find the report name(s).
3.  Set the Max to 25.
4.  Click OK.

> Local/Region IT Staff may set the SYSTEM (or USER) level parameter value for any local report(s) via the General Parameter Tools \[XPAR MENU TOOLS\] option.

1.  Choose Edit Parameter Values.
2.  Enter the parameter definition name, ORWRP TIME/OCC LIMITS INDV.
3.  Select USER or SYSTEM as appropriate.
4.  Enter the local report name.
5.  Enter or (edit existing) time and occurrence limits. The occurrence limit should be set to 25.

# Fixes and Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides the enhancements described above, patch OR\*3.0\*406 does not include any other fixes or code changes.

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not modify any fields.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add any fields.

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add, delete, or modify any forms.

# Associated Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add, delete, or modify any mail groups.

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add, delete, or modify any options.

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add, delete, or modify any protocols.

# Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Keys associated with patch OR\*3.0\*406.

# Associated Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not modify any templates.

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not add any templates.

# Integration Control Registrations (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 does not modify any ICRs.

## New ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch OR\*3.0\*406 does not add any ICRs.

# New Service Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 is not associated with any New Service Requests.

# Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 is not associated with any patient safety issues.

# Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 is not associated with any Remedy Tickets.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues associated with patch OR\*3.0\*406.

1.  <span id="_Toc422840143" class="anchor"></span>Acronyms and Definitions

<span id="_Toc422840144" class="anchor"></span>Table 1: Acronyms and Definitions

| Acronym | Definition                                                                |
|---------|---------------------------------------------------------------------------|
| ADT     | Registration, Enrollment, Eligibility, Admission, Discharge, and Transfer |
| AP      | Anatomic Pathology                                                        |
| API     | Application Programmer Interface                                          |
| CCR     | Clinical Case Registries                                                  |
| DG      | Registration Namespace                                                    |
| EPI     | Emerging Pathogens Initiative                                             |
| GMTS    | Health Summary Namespace                                                  |
| GUI     | Graphical User Interface                                                  |
| HS      | Health Summary                                                            |
| IB      | Integrated Billing                                                        |
| ICD-10  | International Classification of Diseases, 10<sup>th</sup> Revision        |
| LR      | Laboratory Namespace                                                      |
| OE/RR   | Order Entry/Results Reporting                                             |
| OR      | Order Entry/Results Reporting Namespace                                   |
| POA     | Present on Admission                                                      |
| PTF     | Patient Treatment File                                                    |
| ROR     | Clinical Case Registries Namespace                                        |
| VHA     | Veterans Health Administration                                            |
| VistA   | Veterans Health Information Systems and Technology Architecture           |