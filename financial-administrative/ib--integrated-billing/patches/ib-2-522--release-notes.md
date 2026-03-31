---
title: IB*2*522 ICD-10 PTF Modifications Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD-10 PTF Modifications
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*522
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - associated
  - bill
  - diagnosis
  - billing
  - procedure
  - procedures
  - patch
  - codes
page_count: 0
word_count: 2410
section_count: 18
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 1
revision_newest: 9/2/2015
revision_oldest: 9/2/2015
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_522_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_522_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

---
title: |
  ICD-10 PTF Modifications

  Integrated Billing (IB)

  IB\*2.0\*522

  Release Notes
---

![](ib-2-522-icd-10-ptf-modifications-release-notes/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

| Date     | Version | Description                                                                         | Author                                    |
|----------|---------|-------------------------------------------------------------------------------------|-------------------------------------------|
| 9/2/2015 | 1.0     | Baseline document, created for ICD-10 PTF Modifications project patch IB\*2.0\*522. | VA OI&T PD, ICD-10 PTF Modifications Team |

<span id="_Toc422839365" class="anchor"></span>Table 1: Acronyms and Definitions

Table of Contents

List of Tables

[Table 1: Acronyms and Definitions [9](#_Toc422839365)](#_Toc422839365)

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
  - [Enter/Edit Billing Information Inpatient Bill/Claims Diagnosis](#enteredit-billing-information-inpatient-billclaims-diagnosis)
    - [Display and Select Up to 25 Diagnoses](#display-and-select-up-to-25-diagnoses)
    - [Display Diagnosis POA](#display-diagnosis-poa)
    - [Add Diagnosis POA to Bill Instead of DSS Encoder POA](#add-diagnosis-poa-to-bill-instead-of-dss-encoder-poa)
    - [Allow Upper and Lower Case Movement Diagnosis Identifiers](#allow-upper-and-lower-case-movement-diagnosis-identifiers)
  - [Enter/Edit Billing Information Inpatient Bill/Claims Procedures](#enteredit-billing-information-inpatient-billclaims-procedures)
    - [Display and Select Up to 25 Procedures](#display-and-select-up-to-25-procedures)
    - [Identify Billed PTF ICD Procedures](#identify-billed-ptf-icd-procedures)
    - [Allow Duplicate PTF ICD Procedures](#allow-duplicate-ptf-icd-procedures)
    - [Display and Select All CPT/HCPCS Codes for PTF Professional Services](#display-and-select-all-cpthcpcs-codes-for-ptf-professional-services)
    - [Include the Quantity of the Procedure Performed for PTF Professional Services](#include-the-quantity-of-the-procedure-performed-for-ptf-professional-services)
    - [Allow Upper and Lower Case Procedure Episode Identifiers](#allow-upper-and-lower-case-procedure-episode-identifiers)
  - [Modify Bill Charge (DRG) Calculation](#modify-bill-charge-drg-calculation)
  - [Third Party Autobiller](#third-party-autobiller)
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
Patch IB\*2\*522 will update the Inpatient Bill/Claim to accommodate the expanded number of Diagnosis and Procedure codes available in PTF. Enter/Edit Billing Information screens will display and allow selection of all diagnoses and procedures. The POA indicator associated with the diagnosis will also be displayed. The POA associated with an ICD-10 diagnosis will be added to the bill instead of the POA entered in the DSS Encoder. The display and selection of Movement Diagnosis identifiers will now include both upper and lower case alpha characters. The display and selection of the PTF Professional Services (801) has also been expanded to all CPT/HCPCS codes assigned within the bill date range, and the display will include the quantity of the procedure performed if greater than one. The display and selection of Procedure Episode identifiers will now include both upper and lower case alpha characters (A-Z and a-z). For Inpatient Facility bill charges, the calculation of the DRG has been modified to use all the PTF Diagnosis and Procedure codes within the appropriate date range. Inpatient bills created by the Third Party Autobiller will add all the PTF Diagnosis, POA, and Procedure codes within the bill date range.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Release Notes cover the new features provided to VHA VistA Integrated Billing users in patch IB\*2.0\*522.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the VistA Integrated Billing product and applies primarily to the changes made between this newest release and previous release packages of the software.

## Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105, of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

## Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before patch IB\*2.0\*522:

- IB\*2.0\*461
- IB\*2.0\*479
- IB\*2.0\*516
- DG\*5.3\*884

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation information, refer to the ICD-10 PTF Modifications Installation Guide on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=45>.

## Updated Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integrated Billing documents are posted on the VistA Documentation Library (VDL) website: <http://www.va.gov/vdl/application.asp?appid=45>.

The following IB documents have been updated with changes for IB\*2.0\*522:

- ICD-10 PTF Modifications Installation Guide
- ICD-10 PTF Modifications Integrated Billing IB\*2.0\*522 Release Notes
- Integrated Billing (IB) V. 2.0 Technical Manual

The following IB document is present on the VDL but does not require updates:

- Integrated Billing (IB) V. 2.0 User Manual

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*522 will update the Inpatient Bill/Claim to accommodate the expanded number of Diagnosis and Procedure codes available in PTF.

## Enter/Edit Billing Information Inpatient Bill/Claims Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display and Select Up to 25 Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 4, option 3, of Enter/Edit Billing Information \[IB EDIT BILLING INFO\] has been updated to display and allow selection of all diagnoses in the PTF record within the date range of the bill, i.e. up to 25 diagnoses for each Movement (501) and the Discharge (701).

### Display Diagnosis POA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 4, option 3, of Enter/Edit Billing Information \[IB EDIT BILLING INFO\] will also display the POA associated with the diagnosis, if present in PTF.

### Add Diagnosis POA to Bill Instead of DSS Encoder POA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Present on Admission (POA) indicator associated with any selected PTF diagnosis will be added to the bill. Beginning with bills containing ICD-10 codes on or after the ICD-10 implementation date, the POA indicator entered in the DSS Encoder will no longer be added to a bill. For ICD-10 bills, the Diagnosis POA will be available in PTF, where it will be accessed for placement on the bill.

### Allow Upper and Lower Case Movement Diagnosis Identifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the number of PTF Movements associated with the bill, the display and selection of Movement Diagnosis identifiers will now include both upper and lower case alpha characters (A-Z and a-z), with X/x being reserved for the Discharge. Previously, only upper case alpha characters were selectable.

## Enter/Edit Billing Information Inpatient Bill/Claims Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display and Select Up to 25 Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 4, option 4, of Enter/Edit Billing Information \[IB EDIT BILLING INFO\] has been updated to display and allow selection of all Procedures in the PTF record within the date range of the bill, i.e. up to 25 ICD-10 Procedures for each Surgical (401) and Non-O/R (601) Episode.

### Identify Billed PTF ICD Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The display of PTF Surgical (401) and Non-O/R (601) ICD Procedures has been updated to display an asterick “\*” before each PTF ICD procedure that matches a procedure and date already assigned to the bill.

### Allow Duplicate PTF ICD Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible that the same procedure may be completed multiple times on the same date.  These duplicate ICD procedures will be displayed in the list of PTF ICD procedures as separate line items.  If a duplicate ICD procedure is selected by the preceding indicator, then these duplicates will be added to the bill.

### Display and Select All CPT/HCPCS Codes for PTF Professional Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The display and selection of the PTF Professional Services (801) has also been expanded to all CPT/HCPCS codes assigned within the bill date range. Previously, a maximum of five CPT/HCPCS were displayed for each Professional Service, even though more than five codes may have been entered in PTF.

### Include the Quantity of the Procedure Performed for PTF Professional Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The display of the PTF Professional Services (801) will now include the quantity of the procedure performed if it is greater than one.

### Allow Upper and Lower Case Procedure Episode Identifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the number of PTF Procedure Episodes associated with the bill, the display and selection of Procedure Episode identifiers will now include both upper and lower case alpha characters (A-Z and a-z). Previously, only upper case alpha characters were selectable.

## Modify Bill Charge (DRG) Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Inpatient Facility bill charges, the calculation of the DRG has been modified to use all the PTF Diagnosis and Procedure codes within the appropriate date range.

## Third Party Autobiller

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient bills created by the Third Party Autobiller will add all the PTF Diagnosis, POA, and Procedure codes within the bill date range.

# Fixes and Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides the enhancements described above, patch IB\*2.0\*522 includes the fix for Remedy Ticket INC000001243424 (see Section 14, Remedy Tickets, below).

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not modify any fields.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add any fields.

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add, delete, or modify any forms.

# Associated Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add, delete, or modify any mail groups.

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add or delete any options.

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add, delete, or modify any protocols.

# Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Keys associated with patch IB\*2.0\*522.

# Associated Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not modify any templates.

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not add any templates.

# Integration Control Registrations (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 does not modify any ICRs.

## New ICRs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With patch IB\*2.0\*522, Integrated Billing has subscribed to the Registration ICR \#6130 to access the new PTF fields.

# New Service Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*522 is associated with NSR \#20070902, ICD-10-CM Conversion.

# Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no patient safety issues associated with patch IB\*2.0\*522.

# Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one Remedy Ticket corrected in patch IB\*2.0\*522:

- INC000001243424: Billing Screen 10, Section 3, Attending Provider Name missing.
  - <u>Problem</u>: Attending Provider is not being automatically added to Billing Screen 10, Section 3, when a bill is created by the AutoBiller and the provider has a valid National Provider Identifier (NPI). The Third Party AutoBiller had been modified to only add the Attending Provider if that provider had a valid NPI. However, the check for NPI was using the wrong field for the provider resulting in the NPI never being found and therefore the AutoBiller never added the Attending Provider to the bill.
  - <u>Resolution</u>: The software was updated to correctly identify the Attending Provider's NPI. The Third Party AutoBiller will add the Attending Provider to a bill it creates if that provider has a valid NPI. The Attending Provider is then viewable on Screen 10, Section 3, of Enter/Edit Billing Information \[IB EDIT BILLING INFO\] option.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues associated with patch IB\*2.0\*522.

1.  <span id="_Toc428455498" class="anchor"></span>Acronyms and Definitions

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
| NPI     | National Provider Identifier                                              |
| OE/RR   | Order Entry/Results Reporting                                             |
| OR      | Order Entry/Results Reporting Namespace                                   |
| POA     | Present on Admission                                                      |
| PTF     | Patient Treatment File                                                    |
| ROR     | Clinical Case Registries Namespace                                        |
| VHA     | Veterans Health Administration                                            |
| VistA   | Veterans Health Information Systems and Technology Architecture           |