---
title: PSO*7*343 Java-FDA Medication Guides On-Demand Viewing Project Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Java-FDA Medication Guides On-Demand Viewing Project
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*343
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - updates
  - pharmacy
  - medication
  - guide
  - guides
  - project
  - management
  - outpatient
page_count: 0
word_count: 234
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/phar_fda_med_guide_rel2_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/phar_fda_med_guide_rel2_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-343-java-fda-medication-guides-on-demand-viewing-project-release-notes/001.png)

FDA MEDICATION GUIDES PROJECT

> RELEASE NOTES

> PSS\*1\*158 PSN\*4\*263 PSO\*7\*343

> April 2011

### Department of Veterans Affairs Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Department of Veterans Affairs Product Development](#department-of-veterans-affairs-product-development)
- [Introduction](#introduction)
  - [Project Enhancements](#project-enhancements)
- [NDF, Pharmacy Data Management and Outpatient Pharmacy Updates](#ndf-pharmacy-data-management-and-outpatient-pharmacy-updates)
  - [Field Updates](#field-updates)
  - [Modified Menu Option](#modified-menu-option)
  - [Routine Updates](#routine-updates)
  - [Protocol Updates](#protocol-updates)
> The National Drug File (NDF) module provides standardized drug information for all Department of Veterans Affairs Medical Centers (VAMCs). The Outpatient Pharmacy package provides a way to manage the medication regimen of veterans seen in outpatient clinics and to monitor and manage the workload and costs in the Outpatient Pharmacy. The Consolidated Mail Outpatient Pharmacy (CMOP) package provides a regional system resource to expedite the distribution of mail-out prescriptions to veteran patients
> This project provides VistA Pharmacy users the ability to distribute Food and Drug Administration (FDA) Medication Guides to patients for prescription drugs that pose a serious and significant public health concern as deemed by the FDA.
> This enhancement modifies the National Drug File menu to provide an additional option for accommodating the on-demand display of FDA Medication Guides.

## Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software provides the following enhancements:

- New link between VistA and the Medication Guides repository to provide for the on-demand display of FDA Medication Guides.
- New functionality in the Outpatient Pharmacy V. 7.0, Pharmacy Data Management V. 1.0 and National Drug File V. 4.0 applications to allow for the manual display of FDA Medication Guides.

> *(This page included for two-sided copying.)*

# NDF, Pharmacy Data Management and Outpatient Pharmacy Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the changes made to the NDF, Pharmacy Data Management and Outpatient Pharmacy packages for the on-demand display of the Food and Drug Administration (FDA) Medication Guide for the Veterans Health Information Systems and Technology Architecture (VistA).

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new field was added to the VA PRODUCT File (#50.68):

- FDA MED GUIDE field (#100)

> The following new field was added to the PHARMACY SYSTEM File (#59.7):

- FDA MED GUIDE SERVER URL (#100)

## Modified Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following menu option was modified:

- Display FDA Medication Guide \[PSN MED GUIDE\]

## Routine Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new routine was added:

- PSOFDAMG

> The following routines were modified:

- PSNMEDG
- PSNFDAMG
- PSNAPIS

## Protocol Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new protocol was added:

- PSO LM PRINT FDA MED GUIDE

> The following protocol was modified:

- PSO LM HIDDEN OTHER \#2

> *(This page included for two-sided copying.)*