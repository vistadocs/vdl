---
title: PREC*6*516 RELEASE NOTES
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PECS
app_name: 'Pharmacy: Pharmacy Enterprise Customization System'
section: GUI
app_status: active
pkg_ns: PREC
patch_ver: 6
patch_id: PREC*6*516
group_key: PECS:PREC:6
file_numbers: []
security_keys: []
menu_options: 0
description: '- Introduction - Purpose - Audience - This Release - New Features and Functions Added - Enhancements and Modifications to Existing - [Known...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 642
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: ''
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_0_rn_r0516.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_0_rn_r0516.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=204
audit_applied: '2026-05-31'
master_source: PREC*6*516 RELEASE NOTES
master_pub_date: ''
consolidated_from: 4 versions
prior_versions:
- PREC*3*714 RELEASE NOTES
- PREC*5*1114 RELEASE NOTES
- PREC*6.1*717 RELEASE NOTES
consolidated_title: release notes
---

Office of Information and Technology (OI&T)

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
The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. PRE is intended to build on the work accomplished in 2006 with the development of the Pharmacy Enterprise Product System (PEPS) Proof of Concept (POC). The first phase, PRE V.0.5, implemented enhanced order checking functionality utilizing Health*<u>e</u>*Vet (H*<u>e</u>*V) compatible architecture and First Databank (FDB) MedKnowledge Application Program Interfaces (APIs) and database. The Pharmacy Enterprise Customization System (PECS) is a component of PRE that is intended to customize the FDB MedKnowledge Framework COTS database in order to integrate VA custom records. A process to automatically update the standard and custom FDB data at the local database has also been provided.
In response to the Project Management Accountability System (PMAS) initiative instituted in the summer of 2009 that requires projects to complete an increment every six months, PRE now uses an Agile Development methodology, which focuses on developing a usable product at the end of small, iterative timeframes, with involvement and approval from the product owner at every iteration. Each small timeframe, called a sprint, ends with a workable product that is built on the previous efforts until the increment is complete and meets the PMAS schedule. Each increment produces agreed-upon functionality that is available to the entire user community upon National Deployment.
This Release Notes document provides a brief description of the new features and functions of PECS v6.0.01.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to Pharmacy Enterprise Customization System (PECS) for this release.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of Pharmacy Enterprise Customization System (PECS) and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, as well as enhancements and modifications to the existing software, and any known issues for Pharmacy Enterprise Customization (PECS) v6.0.01.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the PECS v6.0.01 release.

PECS v6.0.01 builds on the functionality provided by PECS 5v.0. Additional functionality includes:

- Implement sFTP for PECS, MOCHA Server, and DATUP
- WebLogic version Upgrade for PECS per TRM recommendation
- Implement design solution Comparison Report- redesigns PECS

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications to the PECS v6.0.01 release.

- Enhance User Roles functionality
- Enhancements for PECS Easy Search Dose Range: Add links to PECS records from search results
- Resolution of export query results limitations in Excel format

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

PECS v6.0 RSD

PECS IPT Review Portal:  
http://vaww.oed.portal.va.gov/projects/pre/PRE_IPT_Rev/PRE_IPT_Rev_PECS/Lists/Links/AllItems.aspx

PRE SharePoint Site:  
http://vaww.oed.portal.va.gov/projects/pre

PECS 6.0 SharePoint Site:  
http://vaww.oed.portal.va.gov/projects/pre/PRE_PECS_v6-0/

PRE Project Notebook (TSPR) Site:  
http://tspr.vista.med.va.gov/warboard/anotebk.asp?proj=1474&Type=Active

The following documents are referenced within the RSD:

- PRE V0 5 OC SRS 091611_V8_1
- Austin Information Technology Center (AITC)'s Application Contingency Plan document
- PECS System Design Document
- PECS Product Architecture Document
- PECS Interface Control Document (ICD)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*3*714 RELEASE NOTES

## Functional Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Easy Search:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added a query that produces a report that lists the drug pairs and their associated interactions for a Dispensable Generic Drug or a Dispensable Drug.
- Re-factored Easy Search to allow for additional searches to be added easily.
- Added the ability to search for Dispensable Drugs along with Dispensable Generics.
- Easy Search now returns DOSE HIGH, DOSE HIGH UNITS, DOSE RATE HIGH and DOSE RATE HIGH UNITS for dose range queries.

### Reports:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Updated the Duplicate Therapy and Drug-Drug Interaction-Drug Pair FDB Comparison Reports to fix the issues that were found in the PECS v2.2 Initial Operating Capability.

### Drug-Drug Interaction:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the ability hover the mouse on an icon next to any required field with changes and see the corresponding changes.
- Added the ability to download an Excel report on the full history.

### Drug Pairs:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the ability hover the mouse on an icon next to any required field with changes and see the corresponding changes.
- Added the ability to download an Excel report on the full history.
- Added the data grid to the custom drug pairs section of the Drug Pair customization page.
- Added the ability to search Routed Generic drugs.
- Added the ability to add multiple Routed Generic Drug pairs.

### Dose Range:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the ability hover the mouse on an icon next to any required field with changes and see the corresponding changes.
- Added the ability to download an Excel report on the full history.
- Added Not to Exceed fields.

### Duplicate Therapy:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the ability hover the mouse on an icon next to any required field with changes and see the corresponding changes.
- Added the ability to download an Excel report on the full history.
- Added the ability to see the FDB record of a customized Duplicate Therapy record.

### Professional Monograph:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the ability hover the mouse on an icon next to any required field with changes and see the corresponding changes.
- Added the ability to download an Excel report on the full history.
- Added the ability to see the FDB record of a customized Professional Monograph record.

### MOCHA Server:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Dosing Lookup now returns the Not-To-Exceed fields.
- Order Checks now returns Not-To-Exceed fields when performing a Drug Dose Check.

## Architectural Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PECS updated from FDB-DIF v3.3 to FDB-DIF v3.3 API and Schema
- MOCHA Server updated from FDB-DIF v3.3 Application Program Interface (API) and Schema
- Updated the PECS Custom Update file to be compatible with FDB-DIF v3.3 API and Schema
