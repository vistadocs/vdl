---
title: PSJ*5*267 Release Notes-Special Instructions/Other Print Info
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Special Instructions/Other Print Info
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*267
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document provides a brief description of new features of the Special Instructions/Other Print Info and No Allergy Assessments for Inpatient Medications V.5.0 project for patch PSJ\5\267.
audience: 
keywords: 
  - table
  - contents
  - allergy
  - assessment
  - interfaces
  - pharmacist
  - special
  - print
  - info
  - included
page_count: 0
word_count: 357
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p267_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p267_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-267-release-notes-special-instructions-other-print-info/001.png)

Inpatient Medications

Release Notes

PSJ\*5\*267

Product Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [Enhancements](#enhancements)
  - [Special Instructions/Other Print Info](#special-instructionsother-print-info)
  - [No Allergy Assessment](#no-allergy-assessment)
- [Hardware Interfaces](#hardware-interfaces)
- [Software Interfaces](#software-interfaces)
- [User Documentation](#user-documentation)
- [Remedy Tickets Resolved](#remedy-tickets-resolved)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document provides a brief description of new features of the Special Instructions/Other Print Info and No Allergy Assessments for Inpatient Medications V.5.0 project for patch PSJ\*5\*267.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: The following patches must be installed BEFORE PSJ\*5\*267:

> PSJ\*5\*200

> PSJ\*5\*253

> PSJ\*5\*254

> PSJ\*5\*263

> PSJ\*5\*265

> PSJ\*5\*273

> PSS\*1\*171

## Special Instructions/Other Print Info

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Special Instructions and Other Print Info have been modified to support an unlimited amount of text. The functionality that copies the provider comments from the Computerized Patient Record System (CPRS) to be copied into each field has been retained, and an additional action has been added to (optionally) open a word processing edit dialog after copying the provider comments into the appropriate field (Special Instructions for Unit Dose, Other Print Info for IV). Special Instructions and Other Print Info may also be entered and/or edited from within Inpatient Medications V. 5.0 order entry options. Prior to this enhancement, Inpatient Medications maximum character length for Special Instructions was 180 characters and for Other Print Info the maximum length was 60 characters.

> A new activity log option, “Instruction History”, was created to assist in capturing edits to Special Instructions/Other Print Info.

> This enhancement resolves Patient Safety Issues PSPO 42, 1466/Remedy Ticket HD336419 - Comment lengths between CPRS and Pharmacy.

############################### Associated Files and Fields

| Files                       | Fields                             |
|-----------------------------|------------------------------------|
| Non-Verified Orders (#53.1) | SPECIAL INSTRUCTIONS (LONG) (#135) |
| Non-Verified Orders (#53.1) | OTHER PRINT INFO (LONG) (#136)     |

## No Allergy Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The No Allergy Assessment enhancement provides an interactive alert to the pharmacist in Inpatient Medications V. 5.0 when no allergy assessment is on file for the patient, and a method for the pharmacist to enter an allergy assessment after receiving the alert. A pharmacy intervention is automatically created if the pharmacist chooses not to enter an assessment.

> The No Allergy Assessment functionality will be available at the following options:

> Inpatient Order Entry \[PSJ OE\]

> Non-Verified/Pending Orders \[PSJU VBW\]

> Order Entry \[PSJU NE\]

> Order Entry (IV) \[PSJI ORDER\]

> Profile (IV) \[PSJI PROFILE\]

When a patient with no allergy assessment is selected from one of the affected options, the following message will be displayed to the pharmacist: "NO ALLERGY ASSESSMENT exists for this patient! Would you like to enter one now?"

If the pharmacist enters 'YES' at this prompt, they are prompted for allergy information.

If the pharmacist enters 'NO' at this prompt, a pharmacist intervention is created, with a type of 'NO ALLERGY ASSESSMENT'. The pharmacist is then prompted for Provider and Recommendation. A new Recommendation, 'UNABLE TO ASSESS', has been created specifically for this type of intervention.

This enhancement addresses Patient Safety Issue PSPO 445 and 480.

# Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications interfaces directly with printers for labels and reports.

> Inpatient Medications functions on the following standard server platforms used in VA Medical Center (VAMC) s:

- Open M V. 4.0 route 43 and MS Windows 2000, NT, XP and VMS

# Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications requires the following versions (or higher) of VA software packages for proper implementation. The software listed in the table below is not included in this build and must be installed for the build to be completely functional.

| Package              | Version |
|--------------------------|-------------|
| BCMA                     | 3.0         |
| Inpatient Medications    | 5.0         |
| Kernel                   | 8.0         |
| MailMan                  | 8.0         |
| Nursing                  | 4.0         |
| CPRS                     | 1.0         |
| Pharmacy Data Management | 1.0         |
| RPC Broker (32-bit)      | 1.1         |
| Toolkit                  | 7.3         |
| VA FileMan               | 22.0        |
| Vitals/Measurements      | 5.0         |

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User documentation for Inpatient Medications V.5.0 provides detailed information on the functionality, and can be found on the [VistA Document Library](http://www.va.gov/vdl/application.asp?appid=88) (VDL). Inpatient Medications documents available are listed below:

> Nurse's User Manual

> Nurse's User Manual Change Pages

> Pharmacist's User Manual

> Pharmacist's User Manual Change Pages

> Technical Manual/Security Guide

> Technical Manual/Security Guide Change Pages

> Release Notes

# Remedy Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remedy Tickets were resolved with this patch:

- HD 187184 – IV Med Stop Date
- HD 176676/PSPO 480 - Inpatient doesn't change order status to Expired.
- HD 377288 (original) - Default response should be "No"
- HD 273000 (original) - Field Validation Not Correct
- HD 517634/PSPO 2137 - Provider Comments not displayed.
- HD 586428/PSPO 2137 - Provider Comments not displayed after Verify.

*(This page included for two-sided copying.)*