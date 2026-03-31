---
title: PSJ*5*275 Release Notes-Clinic Orders
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Clinic Orders
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*275
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document provides a brief description of new features of the Clinic Orders – Pharmacy for Inpatient Medications V.5.0 project for patch PSJ\5\275.
audience: 
keywords: 
  - table
  - contents
  - orders
  - associated
  - clinic
  - resolved
  - order
  - patient
  - options
  - tickets
page_count: 0
word_count: 633
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p275_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p275_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-275-release-notes-clinic-orders/001.png)

Inpatient Medications

Release Notes

PSJ\*5\*275

Product Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Associated Patches](#associated-patches)
- [Menu Options](#menu-options)
- [Associated Options](#associated-options)
- [New Menu Option](#new-menu-option)
- [Associated Protocols](#associated-protocols)
- [Templates](#templates)
- [Hardware Interfaces](#hardware-interfaces)
- [Software Interfaces](#software-interfaces)
- [User Documentation](#user-documentation)
- [New Service Requests Tickets Resolved](#new-service-requests-tickets-resolved)
- [Remedy Tickets Resolved](#remedy-tickets-resolved)
- [Patient Safety Issues Resolved](#patient-safety-issues-resolved)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document provides a brief description of new features of the Clinic Orders – Pharmacy for Inpatient Medications V.5.0 project for patch PSJ\*5\*275.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The scope of the Clinic Order project is to provide software modifications to enhance the Pharmacy Inpatient Medications application to support the following functionality:

- New menu options that will provide user prompts and filters to allow authorized users to mass edit a patient clinic orders Start Date/Time medication orders to a new Start Date/Time.
- A view in the patient medication profile that separates the clinic orders from all other orders.
- Improved Patient Safety allowing order checks for clinic orders.
- Eliminating the Patient Safety Issues surrounding writing Inpatient Medications for outpatients (IMO)/Clinic Medication orders and finishing these medication orders in Pharmacy.
- Improved work flows by providing easy access and minimal steps to write and process clinic orders. A future enhancement will allow documentation of and administration for clinic medications in BCMA.

# Associated Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches are associated with this patch and must be installed BEFORE PSJ\*5\*275:

- PSJ\*5\*260
- PSJ\*5\*276
- PSJ\*5\*278

# Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following existing menu options to the patient medication profile were enhanced to separate clinic orders from all other orders:

- [Inpatient Order Entry \[PSJ OE\]](#PSJOE)
- [Order Entry \[PSJU NE\]](#PSJNE)
- Non-[Verified/Pending Orders \[PSJU VBW\]](#PSJJU)
- [Order Entry (IV) \[PSJI ORDER\]](#PSJJI)
- Profile [(IV) \[PSJI PROFILE\]](#PSJJI)
- Action Profile \#1 \[PSJU AP-1\]
- Action Profile \#2 \[PSJU AP-2\]
- Patient Profile (Unit Dose) \[PSJU PR\]

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following options are associated with this patch:

- Clinic Orders Menu \[PSJ CLINIC ORDERS MENU\]
- Edit Clinic Med Orders Start Date/Time \[PSJ ECO\]
- Pharmacy Master Menu \[PHARMACY MASTER MENU\]
- Unit Dose Medications \[PSJU MGR\]
- IV Menu \[PSJI MGR\]

# New Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new menu option was created:

- Edit Clinic Med Orders Start Date/Time \[PSJ ECO\]

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are associated with this patch:

- PSJ LM ECO HIDDEN ACTIONS
- PSJ LM ECO IM PR
- PSJ LM ECO MENU
- PSJ LM ECO RANGE
- PSJ LM ECO SELECT
- PSJ LM ECO START
- PSJ LM VIEW ORDER DETAIL

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following templates are associated with this patch:

- PSJ LM CLINIC ORDERS

# Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinicians interface with VistA using personal computers, which are compatible with the standard software and hardware platforms outlined in Section 5, Software Interfaces.

# Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA operates on the following standard server platforms used in VAMCs: Open M V. 4.0 route 43 and MS Windows 2000, NT and VMS.

> Inpatient Medications require the following versions (or higher) of VA software packages for proper implementation. The software listed is not included in this build and must be installed for the build to be completely functional.

| Application                                       | Version |
|-------------------------------------------------------|-------------|
| Adverse Reaction Tracking                             | 4.0         |
| Decision Support System                               | 3.0         |
| Fee Basis                                             | 3.5         |
| Integrated Funds Control, Accounting, and Procurement | 5.0         |
| Inpatient Medications                                 | 5.0         |
| Integrated Billing                                    | 2.0         |
| Kernel                                                | 8.0         |
| Laboratory                                            | 5.2         |
| Mailman                                               | 7.1         |
| National Drug File                                    | 4.0         |
| Nursing                                               | 4.0         |
| Order Entry/Results Reporting                         | 3.0         |
| Outpatient Pharmacy                                   | 7.0         |
| Patient Information Management Systems                | 5.3         |
| Pharmacy Data Management                              | 1.0         |
| RPC Broker (32-bit)                                   | 1.1         |
| Toolkit                                               | 7.3         |
| VA FileMan                                            | 22.0        |

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User documentation for Inpatient Medications V.5.0 provides detailed information on the functionality, and can be found on the [VistA Document Library](http://www.va.gov/vdl/application.asp?appid=88) (VDL). Inpatient Medications documents available are listed below:

> Nurse's User Manual, PSJ_5_NURSE_UM_R0413.pdf

> Nurse's User Manual Change Pages, PSJ_5_P275_NURSE_UM_CP.pdf

> Pharmacist's User Manual V. 5.0, PSJ_5_PHAR_UM_R0413.pdf

> Pharmacist's User Manual Change Pages, PSJ_5_P275_PHAR_UM_CP.pdf

> Technical Manual/Security Guide V. 5.0, PSJ_5_TM_R0413.pdf

> Technical Manual/Security Guide Change Pages, PSJ_5_P275_TM_CP.pdf

> Release Notes, PSJ_5_P275_RN.pdf

# New Service Requests Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Service Request 20070506 is associated with this patch.

# Remedy Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remedy Tickets are resolved with this patch:

- HD 764596/781899 – Other Print Info display incorrectly
- HD 760186 – Other Print Info from IV Quick Code not used
- HD 763244 – Undefined error in 7 Day Mar
- HD 756354 – Undefined error in CPRS IV label print
- HD 763555 – Wrong intervention recommendation is filed
- HD 770025 – Long Special Instructions not retained after CPRS Renew
- INC 806890 – Order status not set correctly
- INC 815711 – Move enhanced order check so it quits correctly

# Patient Safety Issues Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Safety Issue is resolved with this patch:

- PSPO 2359 – Provider comments intended for a specific order are copied on another order upon renewal.