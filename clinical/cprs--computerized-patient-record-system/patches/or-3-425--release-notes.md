---
title: OR*3*425 Release Notes Provider Orders Management CPRS GUI Version
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Provider Orders Management CPRS GUI Version
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*425
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - orders
  - delayed
  - patch
  - outpatient
  - release
  - features
  - functions
  - inpatient
page_count: 0
word_count: 473
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_425rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_425rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

Provide Orders Management

Patch OR\*3.0\*425

Release Notes

![](or-3-425-release-notes-provider-orders-management-cprs-gui-version/001.png)

December 2016Department of Veterans AffairsOffice of Information and Technology (OI&T)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
This patch allows inpatient delayed orders to be manually released to outpatient locations.
This modification to VistA originated as a field-developed enhancement for local use at VA facilities. It was determined that the modification would be of benefit to the wider VistA user community, and so it is now being deployed nationally.
The following New Service Request (NSR) is resolved with this patch:
- NSR20140205 Provide Orders Management

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to communicate changes to the VistA system resulting from implementation of OR\*3.0\*425.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users of the Order Entry/Results Reporting package in VistA and the Computerized Patient Record System (CPRS).

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for OR\*3.0\*425.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds no new VistA or CPRS features or functions.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3.0\*425 allows inpatient delayed orders (with the exception of Unit-Dose Meds orders and Diet orders) to be manually released to outpatient locations. Without this modification, care to patients can be delayed while providers re-enter orders previously entered as inpatient orders.

This solution is designed to address the specific scenario in which inpatient delayed orders are written for an admission event, but then the patient is not admitted (the patient remains an outpatient post treatment/post procedure) and the delayed orders are required at an outpatient location, such as a Post Anesthesia Care Unit. Under the current functionality, these inpatient delayed orders cannot be released to the outpatient location because the admission event never occurred. After implementation of this patch, the delayed orders (with the exception of Unit-Dose Meds orders and Diet orders) can be successfully released to an outpatient location.

The following routine was modified to implement this enhancement:

- ORCACT0 – Validates order action

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional end-user documentation is available for this patch.