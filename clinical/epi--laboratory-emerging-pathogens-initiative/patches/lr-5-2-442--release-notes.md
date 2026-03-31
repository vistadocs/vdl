---
title: LR*5.2*442 ICD-10 PTF Modifications Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10 PTF Modifications
app_code: EPI
app_name: "Laboratory: Emerging Pathogens Initiative"
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*442
group_key: "EPI:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - associated
  - patch
  - laboratory
  - does
  - modifications
  - changes
  - modify
  - fields
page_count: 0
word_count: 1617
section_count: 20
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 2
revision_newest: 8/26/2015
revision_oldest: 6/23/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lr_5_2_442_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lr_5_2_442_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=118"
---

---
title: |
  ICD-10 Patient Treatment File (PTF) Modifications

  Laboratory: Anatomic Pathology (AP)

  Laboratory: Emerging Pathogens Initiative (EPI)

  LR\*5.2\*442

  Release Notes
---

![](lr-5-2-442-icd-10-ptf-modifications-release-notes/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

| Date      | Version | Description                                                                         | Author                                    |
|-----------|---------|-------------------------------------------------------------------------------------|-------------------------------------------|
| 8/26/2015 | 1.1     | Incorporated Release Coordinator feedback (corrected typo).                         | VA OI&T PD, ICD-10 PTF Modifications Team |
| 6/23/2015 | 1.0     | Baseline document, created for ICD-10 PTF Modifications project patch LR\*5.2\*442. | VA OI&T PD, ICD-10 PTF Modifications Team |

<span id="_Toc428458404" class="anchor"></span>Table : Acronyms and Definitions

Table of Contents

List of Tables

[Table 1: Acronyms and Definitions [7](#_Toc428458404)](#_Toc428458404)

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
  - [Use New API to Obtain PTF Diagnoses](#use-new-api-to-obtain-ptf-diagnoses)
  - [Expand ICD-10 Diagnoses in EPI Message](#expand-icd-10-diagnoses-in-epi-message)
  - [Modify Tissue Review Case Report in Lab AP](#modify-tissue-review-case-report-in-lab-ap)
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
- [Blood Bank Clearance Statement](#blood-bank-clearance-statement)
  - [Effect on Blood Bank Functional Requirements](#effect-on-blood-bank-functional-requirements)
  - [Risk Analysis](#risk-analysis)
  - [Validation Requirements by Option](#validation-requirements-by-option)
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
Patch LR\*5.2\*442 enhances the Laboratory package to utilize a new Application Programmer Interface (API) to obtain PTF related diagnosis codes for reporting. Patch LR\*5.2\*442 changes the EPI module to accommodate up to 25 ICD-10 diagnosis codes in data messages sent to the Austin Information Technology Center (AITC). Patch LR\*5.2\*442 also changes the AP module to expand the number of ICD-10 Diagnosis codes retrieved and displayed in the Tissue Review Case Report.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Release Notes cover the new features provided to VHA VistA Laboratory users in patch LR\*5.2\*442.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the VistA Laboratory product and applies primarily to the changes made between this newest release and previous release packages of the software.

## Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105, of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

## Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before patch LR\*5.2\*442:

- LR\*5.2\*421
- LR\*5.2\*422
- DG\*5.3\*884

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation information, refer to the ICD-10 PTF Modifications Installation Guide on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=72>.

## Updated Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory: Anatomic Pathology (AP) documents are posted on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=72>.

The following Laboratory: AP documents have been updated with changes for LR\*5.2\*442:

- ICD-10 PTF Modifications Installation Guide
- ICD-10 PTF Modifications Laboratory LR\*5.2\*442 Release Notes
- Laboratory Anatomic Pathology (AP) User Guide

The Laboratory: Emerging Pathogens Initiative (EPI) documents are posted on the VDL website: <http://www.va.gov/vdl/application.asp?appid=118>.

The following Laboratory: EPI documents have been updated with changes for LR\*5.2\*442:

- ICD-10 PTF Modifications Installation Guide
- ICD-10 PTF Modifications Laboratory LR\*5.2\*442 Release Notes
- Laboratory EPI Roll Up Modifications Technical and User Manual
- Laboratory EPI Technical and User Guide
- Laboratory Hepatitis C and EPI Technical and User Guide
- Laboratory Search/Extract Technical and User Guide

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use New API to Obtain PTF Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 utilizes a new Application Programmer Interface (API) to retrieve up to 25 ICD-10 Diagnosis codes that can now be stored in the PTF (#45) file.

## Expand ICD-10 Diagnoses in EPI Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data related to specific emerging pathogens is collected and sent to AITC. The messages will now accommodate up to 25 ICD-10 diagnosis codes associated with a single EPI data record.

## Modify Tissue Review Case Report in Lab AP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Laboratory AP module, modifications will be made to the Tissue Review Case Report to permit retrieving and displaying up to 25 ICD-10 Diagnosis codes that can now be stored in the PTF (#45) file.

# Fixes and Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides the enhancements described above, patch LR\*5.2\*442 does not include any other fixes or code changes.

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not modify any fields.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add any fields.

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add, delete, or modify any forms.

# Associated Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add, delete, or modify any mail groups.

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add, delete, or modify any options.

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add, delete, or modify any protocols.

# Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Keys associated with patch LR\*5.2\*442.

# Associated Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not modify any templates.

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add any templates.

# Integration Control Registrations (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not modify any ICRs.

## New ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not add any ICRs.

# Blood Bank Clearance Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Effect on Blood Bank Functional Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 does not contain any changes to the VISTA BLOOD BANK software as defined by ProPath standard entitled, “BBM Team Review of VistA Patches.” Patch LR\*5.2\*442 does not modify any software design safeguards or safety critical elements functions.

## Risk Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes made by patch LR\*5.2\*442 have no effect on Blood Bank software functionality and therefore has no risk.

## Validation Requirements by Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of the nature of the changes made, no specific validation requirements exist as a result of installation of this patch.

# New Service Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*442 is associated with NSR \#20070902, ICD-10-CM Conversion.

# Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no patient safety issues associated with patch LR\*5.2\*442.

# Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Remedy Tickets associated with patch LR\*5.2\*442.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues associated with patch LR\*5.2\*442.

1.  <span id="_Toc428458440" class="anchor"></span>Acronyms and Definitions

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